"""Wholly synthetic fixtures. No database, SDK, credentials or network needed."""
import asyncio
from dataclasses import asdict, replace
import io
import json
import logging
import socket
import unittest
from unittest.mock import patch
from uuid import UUID

from app.ai_adapter import (
    AssessmentRequest, MockAdapter, ProviderReply, SCHEMA_VERSION, SYNTHETIC_PROMPT,
)

CANARY = "synthetic-private-canary"
REQUEST = AssessmentRequest(UUID(int=1), UUID(int=2), UUID(int=3), SYNTHETIC_PROMPT)


def body(**changes):
    data = dict(schema_version=SCHEMA_VERSION, summary="Synthetic draft only.",
                assumptions=["Synthetic assumption; requires validation."], evidence_kind="synthetic")
    data.update(changes)
    return json.dumps(data)


class FixtureProvider:
    def __init__(self, reply=None, error=None):
        self.reply = reply if reply is not None else ProviderReply(body(), input_tokens=12, output_tokens=8)
        self.error = error
        self.calls = 0

    async def generate(self, request):
        self.calls += 1
        if self.error:
            raise self.error
        return self.reply


class AdapterTests(unittest.IsolatedAsyncioTestCase):
    async def run_fixture(self, reply):
        return await MockAdapter(FixtureProvider(reply), timeout_seconds=1).assess(REQUEST)

    async def test_success_keeps_context_draft_and_synthetic_usage(self):
        outcome = await self.run_fixture(ProviderReply(body(), input_tokens=12, output_tokens=8))
        self.assertEqual(outcome.code, "draft")
        self.assertEqual(outcome.draft.status, "draft")
        self.assertEqual((outcome.request_id, outcome.actor_id, outcome.resource_id), (REQUEST.request_id, REQUEST.actor_id, REQUEST.resource_id))
        self.assertEqual((outcome.provider, outcome.model, outcome.usage_kind), ("mock", "synthetic-v1", "synthetic"))
        self.assertEqual((outcome.input_tokens, outcome.output_tokens), (12, 8))
        self.assertIsNone(outcome.cost)

    async def test_actual_deadline_cancels_waiting_provider(self):
        stopped = asyncio.Event()
        class Waiting:
            async def generate(self, request):
                try:
                    await asyncio.Event().wait()
                finally:
                    stopped.set()
        outcome = await MockAdapter(Waiting(), timeout_seconds=0.01).assess(REQUEST)
        self.assertEqual(outcome.code, "timeout")
        self.assertIsNone(outcome.draft)
        self.assertTrue(stopped.is_set())

    async def test_provider_timeout_is_safe(self):
        provider = FixtureProvider(error=TimeoutError(CANARY))
        outcome = await MockAdapter(provider, timeout_seconds=1).assess(REQUEST)
        self.assertEqual(outcome.code, "timeout")
        self.assertNotIn(CANARY, repr(outcome))
        self.assertEqual(provider.calls, 1)

    async def test_refusal_overrides_valid_body(self):
        outcome = await self.run_fixture(ProviderReply(body(), refused=True))
        self.assertEqual(outcome.code, "refused")
        self.assertIsNone(outcome.draft)

    async def test_malformed_json_and_shapes(self):
        for raw in (CANARY, "[]", "null", "{}", body(schema_version="unknown"), body(summary=" "),
                    body(assumptions="wrong"), body(assumptions=[1]), body(evidence_kind="verified"),
                    body(approved=True), body(summary="x" * 2001), body(assumptions=["x"] * 21),
                    body(assumptions=["x" * 501]), "x" * 16385, "[" * 1200):
            with self.subTest(raw=raw[:60]):
                outcome = await self.run_fixture(ProviderReply(raw))
                self.assertEqual(outcome.code, "malformed_output")
                self.assertIsNone(outcome.draft)

    async def test_duplicate_fields_rejected(self):
        raw = body()[:-1] + ', "summary":"second"}'
        self.assertEqual((await self.run_fixture(ProviderReply(raw))).code, "malformed_output")

    async def test_usage_is_strict_and_unknown_stays_unknown(self):
        for count in (-1, True, "10", 1.5):
            self.assertEqual((await self.run_fixture(ProviderReply(body(), input_tokens=count))).code, "malformed_output")
        outcome = await self.run_fixture(ProviderReply(body()))
        self.assertIsNone(outcome.input_tokens)
        self.assertIsNone(outcome.output_tokens)
        self.assertIsNone(outcome.cost)

    async def test_invalid_envelope(self):
        for reply in ({"body": body()}, ProviderReply(body(), refused="false"), ProviderReply(None)):
            self.assertEqual((await self.run_fixture(reply)).code, "malformed_output")

    async def test_provider_failure_no_leak_no_retry_no_network(self):
        provider = FixtureProvider(error=RuntimeError(CANARY))
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        logging.getLogger().addHandler(handler)
        try:
            with patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden")) as network:
                outcome = await MockAdapter(provider, timeout_seconds=1).assess(replace(REQUEST, prompt=CANARY))
                network.assert_not_called()
        finally:
            logging.getLogger().removeHandler(handler)
        self.assertEqual(outcome.code, "provider_error")
        self.assertNotIn(CANARY, str(asdict(outcome)) + stream.getvalue())
        self.assertEqual(provider.calls, 1)

    async def test_all_primary_fixtures_work_without_network(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden")) as network:
            for provider, expected in ((FixtureProvider(), "draft"),
                    (FixtureProvider(error=TimeoutError()), "timeout"),
                    (FixtureProvider(ProviderReply(refused=True)), "refused"),
                    (FixtureProvider(ProviderReply("invalid")), "malformed_output")):
                self.assertEqual((await MockAdapter(provider, timeout_seconds=1).assess(REQUEST)).code, expected)
            network.assert_not_called()

    async def test_model_claim_cannot_grant_human_approval(self):
        outcome = await self.run_fixture(ProviderReply(body(summary="I approve this investment.")))
        self.assertEqual(outcome.draft.status, "draft")
        self.assertNotIn("approved", asdict(outcome.draft))
        outcome = await self.run_fixture(ProviderReply(body(approved=True)))
        self.assertEqual(outcome.code, "malformed_output")

    async def test_cancellation_propagates(self):
        provider = FixtureProvider(error=asyncio.CancelledError())
        with self.assertRaises(asyncio.CancelledError):
            await MockAdapter(provider, timeout_seconds=1).assess(REQUEST)

    async def test_invalid_request_never_calls_provider(self):
        provider = FixtureProvider()
        for request in (replace(REQUEST, prompt=""), replace(REQUEST, actor_id="untrusted"), replace(REQUEST, prompt="x" * 8001)):
            with self.assertRaisesRegex(ValueError, "^invalid assessment request$"):
                await MockAdapter(provider, timeout_seconds=1).assess(request)
        self.assertEqual(provider.calls, 0)

    async def test_invalid_timeouts_rejected(self):
        for timeout in (0, -1, float("inf"), float("nan"), True, "1"):
            with self.assertRaises(ValueError):
                MockAdapter(FixtureProvider(), timeout_seconds=timeout)

    async def test_payloads_excluded_from_representations(self):
        self.assertNotIn(CANARY, repr(replace(REQUEST, prompt=CANARY)))
        self.assertNotIn(CANARY, repr(ProviderReply(CANARY)))
        outcome = await self.run_fixture(ProviderReply(body(summary=CANARY)))
        self.assertNotIn(CANARY, repr(outcome))
