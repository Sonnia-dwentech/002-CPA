"""B019 local configuration and ephemeral usage hooks; live AI stays disabled.

No environment file is loaded and no provider transport is constructed here.
Trusted composition supplies the mapping and an explicit B018 mock adapter.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import re
from time import monotonic
from uuid import UUID

from app.ai_adapter import AssessmentRequest, MockAdapter, Outcome


@dataclass(frozen=True)
class Configuration:
    # Retain no raw model, key, budget string or arbitrary environment values.
    requested_live: bool
    errors: tuple[str, ...]
    live_allowed: bool = False


def inspect_configuration(values) -> Configuration:
    """Inspect explicit string settings; never interpret a missing budget as zero.

    This checks shape/presence only. It does not validate credentials, select a
    model, establish currency/pricing or authorise spending.
    """
    errors = []
    switch = values.get("LIVE_AI_ENABLED", "false")
    if switch not in ("true", "false"):
        errors.append("invalid_live_switch")
    requested_live = switch == "true"
    if requested_live:
        model = values.get("OPENAI_MODEL")
        credential = values.get("OPENAI_API_KEY")
        budget = values.get("MAX_AI_RUN_COST")
        if type(model) is not str or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}", model):
            errors.append("missing_or_invalid_model")
        if (type(credential) is not str or not credential.strip()
                or credential != credential.strip() or any(c.isspace() for c in credential)):
            errors.append("missing_or_invalid_credential")
        try:
            if type(budget) is not str or not re.fullmatch(r"[0-9]{1,12}(?:\.[0-9]{1,8})?", budget):
                raise ValueError
            if not Decimal(budget).is_finite() or Decimal(budget) <= 0:
                raise ValueError
        except (ValueError, InvalidOperation):
            errors.append("missing_or_invalid_budget")
    return Configuration(requested_live, tuple(errors))


@dataclass(frozen=True)
class UsageRecord:
    actor_id: UUID
    request_id: UUID
    resource_id: UUID
    purpose: str
    timestamp: datetime
    model: str | None
    usage_kind: str
    input_tokens: int | None
    output_tokens: int | None
    elapsed_seconds: float
    outcome: str
    cost_status: str = "unknown"
    cost: None = None


@dataclass(frozen=True)
class ControlledResult:
    code: str
    outcome: Outcome | None
    usage: UsageRecord


class LocalAIControls:
    """Runs mocks explicitly; blocks all live requests before touching the adapter.

    Usage is returned to the trusted caller, not persisted or logged. There is no
    quota ledger, estimated-price policy or production budget enforcement claim.
    """
    def __init__(self, settings, mock_adapter: MockAdapter):
        self._configuration = inspect_configuration(settings)
        self._mock = mock_adapter

    async def assess(self, request: AssessmentRequest) -> ControlledResult:
        # Validate before telemetry creation; never trust IDs from an HTTP body.
        if (not isinstance(request, AssessmentRequest)
                or any(not isinstance(value, UUID) for value in (request.actor_id, request.request_id, request.resource_id))
                or type(request.prompt) is not str or not request.prompt.strip() or len(request.prompt) > 8000):
            raise ValueError("invalid assessment request")
        start = monotonic()
        outcome = None
        if self._configuration.errors:
            code = "configuration_invalid"
        elif self._configuration.requested_live:
            code = "live_unavailable"
        else:
            outcome = await self._mock.assess(request)
            code = outcome.code
        usage = UsageRecord(
            actor_id=request.actor_id, request_id=request.request_id,
            resource_id=request.resource_id, purpose="synthetic_assessment",
            timestamp=datetime.now(timezone.utc),
            model=outcome.model if outcome is not None else None,
            usage_kind="synthetic" if outcome is not None else "unavailable",
            input_tokens=outcome.input_tokens if outcome is not None else None,
            output_tokens=outcome.output_tokens if outcome is not None else None,
            elapsed_seconds=max(0.0, monotonic() - start), outcome=code,
        )
        return ControlledResult(code, outcome, usage)
