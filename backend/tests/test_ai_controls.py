"""B019 synthetic fixtures; no real credential, price, model or provider."""
from dataclasses import asdict, replace
import json
import socket
import unittest
from unittest.mock import patch
from uuid import UUID

from app.ai_adapter import AssessmentRequest, MockAdapter, ProviderReply, SCHEMA_VERSION
from app.ai_controls import inspect_configuration, LocalAIControls

REQUEST = AssessmentRequest(UUID(int=11), UUID(int=12), UUID(int=13), "synthetic-private-prompt")
SETTINGS = dict(LIVE_AI_ENABLED="true", OPENAI_MODEL="synthetic-model",
                OPENAI_API_KEY="nonfunctional-synthetic-secret", MAX_AI_RUN_COST="1.25")


class Provider:
    def __init__(self, reply=None, error=None):
        self.calls = 0
        self.error = error
        self.reply = reply or ProviderReply(json.dumps(dict(schema_version=SCHEMA_VERSION,
            summary="Synthetic draft", assumptions=[], evidence_kind="synthetic")), input_tokens=7, output_tokens=4)

    async def generate(self, request):
        self.calls += 1
        if self.error:
            raise self.error
        return self.reply


class ControlTests(unittest.IsolatedAsyncioTestCase):
    async def run_control(self, settings, provider=None):
        provider = provider or Provider()
        result = await LocalAIControls(settings, MockAdapter(provider, timeout_seconds=1)).assess(REQUEST)
        return result, provider

    async def test_each_missing_live_requirement_blocks_transport(self):
        for key in ("OPENAI_MODEL", "OPENAI_API_KEY", "MAX_AI_RUN_COST"):
            settings = dict(SETTINGS)
            del settings[key]
            with self.subTest(key=key):
                result, provider = await self.run_control(settings)
                self.assertEqual(result.code, "configuration_invalid")
                self.assertEqual(provider.calls, 0)
                self.assertIsNone(result.outcome)

    async def test_complete_configuration_still_cannot_enable_live(self):
        with patch.object(socket.socket, "connect", side_effect=AssertionError("network forbidden")) as network:
            result, provider = await self.run_control(SETTINGS)
            self.assertEqual(result.code, "live_unavailable")
            self.assertEqual(provider.calls, 0)
            network.assert_not_called()
        self.assertFalse(inspect_configuration(SETTINGS).live_allowed)

    async def test_malformed_switch_does_not_fall_back_to_mock(self):
        for switch in ("TRUE", "1", "", None, True, False, 1, " true "):
            result, provider = await self.run_control(dict(SETTINGS, LIVE_AI_ENABLED=switch))
            self.assertEqual(result.code, "configuration_invalid")
            self.assertEqual(provider.calls, 0)

    async def test_missing_switch_defaults_to_explicitly_labelled_mock(self):
        result, provider = await self.run_control({})
        self.assertEqual(result.code, "draft")
        self.assertEqual(provider.calls, 1)
        self.assertEqual(result.usage.usage_kind, "synthetic")
        self.assertEqual(result.usage.model, "synthetic-v1")

    async def test_invalid_budget_values_block(self):
        for value in ("", "0", "-1", "NaN", "Infinity", "1e9", " 1", "1.123456789", "9" * 13, 1, True, None):
            result, provider = await self.run_control(dict(SETTINGS, MAX_AI_RUN_COST=value))
            self.assertEqual(result.code, "configuration_invalid")
            self.assertEqual(provider.calls, 0)

    async def test_invalid_model_and_credential_block(self):
        for key, values in (("OPENAI_MODEL", ("", "a b", "x" * 129, None)),
                            ("OPENAI_API_KEY", ("", " ", "a\nb", " x", None))):
            for value in values:
                result, provider = await self.run_control(dict(SETTINGS, **{key: value}))
                self.assertEqual(result.code, "configuration_invalid")
                self.assertEqual(provider.calls, 0)

    async def test_usage_context_and_cost_are_honest(self):
        result, _ = await self.run_control({})
        usage = result.usage
        self.assertEqual((usage.actor_id, usage.request_id, usage.resource_id), (REQUEST.actor_id, REQUEST.request_id, REQUEST.resource_id))
        self.assertEqual((usage.input_tokens, usage.output_tokens), (7, 4))
        self.assertEqual(usage.purpose, "synthetic_assessment")
        self.assertIsNotNone(usage.timestamp.tzinfo)
        self.assertGreaterEqual(usage.elapsed_seconds, 0)
        self.assertEqual(usage.cost_status, "unknown")
        self.assertIsNone(usage.cost)

    async def test_denied_usage_is_unavailable_never_zero(self):
        result, _ = await self.run_control(SETTINGS)
        self.assertEqual(result.usage.usage_kind, "unavailable")
        for name in ("model", "input_tokens", "output_tokens", "cost"):
            self.assertIsNone(getattr(result.usage, name))

    async def test_failure_outcomes_retain_safe_usage(self):
        for provider, expected in ((Provider(error=TimeoutError("synthetic-secret")), "timeout"),
                                  (Provider(error=RuntimeError("synthetic-secret")), "provider_error"),
                                  (Provider(ProviderReply(refused=True)), "refused"),
                                  (Provider(ProviderReply("synthetic-secret")), "malformed_output")):
            result, _ = await self.run_control({}, provider)
            self.assertEqual(result.usage.outcome, expected)
            self.assertIsNone(result.usage.cost)
            self.assertIsNone(result.usage.input_tokens)
            self.assertNotIn("synthetic-secret", repr(result))

    async def test_secrets_and_prompt_not_in_configuration_or_usage(self):
        config = inspect_configuration(SETTINGS)
        result, _ = await self.run_control(SETTINGS)
        text = repr(config) + str(asdict(config)) + str(asdict(result.usage))
        for private in (SETTINGS["OPENAI_API_KEY"], REQUEST.prompt, SETTINGS["OPENAI_MODEL"]):
            self.assertNotIn(private, text)

    async def test_settings_snapshot_cannot_be_enabled_by_later_mutation(self):
        settings = dict(SETTINGS)
        provider = Provider()
        controls = LocalAIControls(settings, MockAdapter(provider, timeout_seconds=1))
        settings["LIVE_AI_ENABLED"] = "false"
        self.assertEqual((await controls.assess(REQUEST)).code, "live_unavailable")
        self.assertEqual(provider.calls, 0)

    async def test_bad_request_is_rejected_before_telemetry(self):
        provider = Provider()
        controls = LocalAIControls({}, MockAdapter(provider, timeout_seconds=1))
        with self.assertRaisesRegex(ValueError, "^invalid assessment request$"):
            await controls.assess(replace(REQUEST, actor_id="untrusted"))
        self.assertEqual(provider.calls, 0)
