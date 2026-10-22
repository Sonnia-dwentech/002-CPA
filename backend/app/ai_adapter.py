"""B018 local AI contract. No provider SDK, credentials, persistence or HTTP route.

Callers supply already-authorised context. This boundary does not authenticate
actors. Injected transports must be asynchronous and cancellation-cooperative.
"""
import asyncio
from dataclasses import dataclass, field
import json
import math
from typing import Literal, Protocol
from uuid import UUID


SCHEMA_VERSION = "cpa.synthetic-assessment.v1"
PROMPT_VERSION = "cpa.synthetic-prompt.v1"
SYNTHETIC_PROMPT = "Return synthetic draft analysis only; never grant human approval."
MAX_OUTPUT_BYTES = 16384


@dataclass(frozen=True)
class AssessmentRequest:
    request_id: UUID
    actor_id: UUID
    resource_id: UUID
    prompt: str = field(repr=False)


@dataclass(frozen=True)
class ProviderReply:
    body: str = field(default="", repr=False)
    refused: bool = False
    input_tokens: int | None = None
    output_tokens: int | None = None


class Provider(Protocol):
    async def generate(self, request: AssessmentRequest) -> ProviderReply: ...


@dataclass(frozen=True)
class Draft:
    schema_version: str
    summary: str = field(repr=False)
    assumptions: tuple[str, ...] = field(repr=False)
    evidence_kind: Literal["synthetic"] = "synthetic"
    status: Literal["draft"] = "draft"


@dataclass(frozen=True)
class Outcome:
    request_id: UUID
    actor_id: UUID
    resource_id: UUID
    code: str
    draft: Draft | None = None
    provider: str = "mock"
    model: str = "synthetic-v1"
    prompt_version: str = PROMPT_VERSION
    usage_kind: str = "synthetic"
    input_tokens: int | None = None
    output_tokens: int | None = None
    cost: None = None  # Unknown/unpriced; never represented as zero paid cost.


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate field")
        result[key] = value
    return result


def _draft(body):
    if type(body) is not str or len(body.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise ValueError("invalid body")
    data = json.loads(body, object_pairs_hook=_unique_object)
    if type(data) is not dict or set(data) != {"schema_version", "summary", "assumptions", "evidence_kind"}:
        raise ValueError("invalid fields")
    if data["schema_version"] != SCHEMA_VERSION or data["evidence_kind"] != "synthetic":
        raise ValueError("invalid version or provenance")
    summary, assumptions = data["summary"], data["assumptions"]
    if type(summary) is not str or not summary.strip() or len(summary) > 2000:
        raise ValueError("invalid summary")
    if type(assumptions) is not list or len(assumptions) > 20:
        raise ValueError("invalid assumptions")
    if any(type(item) is not str or not item.strip() or len(item) > 500 for item in assumptions):
        raise ValueError("invalid assumption")
    return Draft(SCHEMA_VERSION, summary, tuple(assumptions))


class MockAdapter:
    """Explicit mock-only composition; no fallback, retries or live selection.

    The provider injection is trusted Python test wiring, not user configuration.
    The caller chooses a finite timeout; this is not a production timeout policy.
    """
    def __init__(self, provider: Provider, *, timeout_seconds: float):
        if type(timeout_seconds) not in (int, float) or not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
            raise ValueError("timeout must be finite and positive")
        self._provider = provider
        self._timeout = timeout_seconds

    async def assess(self, request: AssessmentRequest) -> Outcome:
        if (not isinstance(request, AssessmentRequest)
                or any(not isinstance(value, UUID) for value in (request.request_id, request.actor_id, request.resource_id))
                or type(request.prompt) is not str or not request.prompt.strip() or len(request.prompt) > 8000):
            raise ValueError("invalid assessment request")

        def result(code, **kwargs):
            return Outcome(request.request_id, request.actor_id, request.resource_id, code, **kwargs)

        try:
            reply = await asyncio.wait_for(self._provider.generate(request), self._timeout)
        except TimeoutError:
            return result("timeout")
        except Exception:
            return result("provider_error")
        # CancelledError deliberately propagates, allowing caller cancellation.
        try:
            if not isinstance(reply, ProviderReply) or type(reply.refused) is not bool:
                return result("malformed_output")
            if reply.refused:
                return result("refused")
            for count in (reply.input_tokens, reply.output_tokens):
                if count is not None and (type(count) is not int or count < 0):
                    return result("malformed_output")
            draft = _draft(reply.body)
        except (ValueError, TypeError, RecursionError):
            return result("malformed_output")
        return result("draft", draft=draft, input_tokens=reply.input_tokens, output_tokens=reply.output_tokens)
