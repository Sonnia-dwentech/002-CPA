"""B021 synthetic reference dashboard; no business metrics or HTTP route."""
from dataclasses import dataclass
from uuid import UUID

from fastapi import HTTPException
import psycopg
from psycopg.pq import TransactionStatus

from app.access import AccessStore, VerifiedIdentity, INTERNAL, CLIENT

KINDS = INTERNAL | CLIENT
STATES = frozenset({"draft", "submitted", "published", "archived"})


@dataclass(frozen=True)
class Filters:
    kind: str | None = None
    state: str | None = None
    owner_id: UUID | None = None


def parse_filters(values):
    """Strict query contract. Omit optional fields; empty/null is not omission."""
    try:
        if type(values) is not dict or set(values) - {"kind", "state", "owner_id"}:
            raise ValueError
        kind, state = values.get("kind"), values.get("state")
        if "kind" in values and (type(kind) is not str or kind not in KINDS):
            raise ValueError
        if "state" in values and (type(state) is not str or state not in STATES):
            raise ValueError
        owner = None
        if "owner_id" in values:
            raw = values["owner_id"]
            if type(raw) is not str:
                raise ValueError
            owner = UUID(raw)
        return Filters(kind, state, owner)
    except (ValueError, TypeError, AttributeError):
        raise HTTPException(422, "Invalid dashboard filters.") from None


@dataclass(frozen=True)
class Reference:
    id: UUID
    kind: str
    state: str
    owner_id: UUID


@dataclass(frozen=True)
class Dashboard:
    status: str
    total: int | None
    records: tuple[Reference, ...]
    available_kinds: tuple[str, ...]
    data_kind: str = "synthetic_reference_records"
    metric: str = "visible_reference_count"
    business_metrics_status: str = "unavailable"


class DashboardStore:
    """Trusted synthetic harness only; kinds disabled by default.

    Supply an idle connection dedicated to this request. REPEATABLE READ keeps
    counts, rows and permission reads in one snapshot; the next request reloads
    grants. This small local reference query is not a production-scale paginator.
    """
    def __init__(self, connection, enabled_kinds=frozenset()):
        enabled = frozenset(enabled_kinds)
        if not enabled <= KINDS:
            raise ValueError("Invalid dashboard kinds")
        self.connection = connection
        self.access = AccessStore(connection, enabled)
        self.enabled = enabled

    def query(self, identity, values=None):
        filters = parse_filters({} if values is None else values)
        if not isinstance(identity, VerifiedIdentity):
            raise HTTPException(401, "Authentication required.")
        try:
            if self.connection.info.transaction_status != TransactionStatus.IDLE:
                raise HTTPException(503, "Dashboard unavailable.")
            with self.connection.transaction():
                self.connection.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY")
                # Reuse B013 actor and row policy; do not infer access from IDs.
                actor = self.access._actor(identity)
                if not actor:
                    raise HTTPException(401, "Authentication required.")
                if actor["category"] != "internal" or actor["client_id"] is not None:
                    raise HTTPException(403, "Access denied.")
                available = tuple(sorted(self.enabled))
                if not available or (filters.kind is not None and filters.kind not in self.enabled):
                    return Dashboard("unavailable", None, (), available)
                kinds = (filters.kind,) if filters.kind else available
                selected = {}
                for kind in kinds:
                    for row in self.access.visible(identity, kind):
                        if filters.state is not None and row["state"] != filters.state:
                            continue
                        if filters.owner_id is not None and row["owner_id"] != filters.owner_id:
                            continue
                        selected[row["id"]] = Reference(row["id"], row["kind"], row["state"], row["owner_id"])
                records = tuple(selected[key] for key in sorted(selected))
                return Dashboard("ok" if records else "empty", len(records), records, available)
        except psycopg.Error:
            raise HTTPException(503, "Dashboard unavailable.") from None
