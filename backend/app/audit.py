"""Explicitly wired local audit boundary. Not enabled by normal app startup."""
from time import monotonic
from uuid import UUID, uuid4

from fastapi import HTTPException
import psycopg

from app.access import AccessStore, VerifiedIdentity
from app.sessions import SessionStore, bearer_token

CATALOGUE = {
    "session.issue": {"issued", "denied", "unavailable"},
    "session.logout": {"revoked", "denied", "unavailable"},
    "record.read": {"allowed", "denied", "unavailable"},
    "privileged.check": {"denied", "unavailable"},
}


class AuditWriter:
    def __init__(self, connection):
        self.connection = connection

    def write(self, action, outcome, actor=None, resource=None):
        if action not in CATALOGUE or outcome not in CATALOGUE[action]:
            raise ValueError("Unknown audit code")
        if any(value is not None and not isinstance(value, UUID) for value in (actor, resource)):
            raise ValueError("Audit identifiers must be resolved UUIDs")
        self.connection.execute(
            "INSERT INTO cpa.audit_events(action,outcome,actor_id,resource_id) VALUES (%s,%s,%s,%s)",
            (action, outcome, actor, resource),
        )


class AuditedActions:
    """Run actual session/access operations and audit in one transaction.

    A required audit insert failure rolls back the operation and returns 503.
    Handled denials are audited and committed before raising their HTTP error.
    Unavailable audit storage cannot record its own outage; no fallback file.
    """
    def __init__(self, connection):
        self.connection = connection
        self.sessions = SessionStore(connection)
        self.access = AccessStore(connection, {"idea", "client_intake"})
        self.writer = AuditWriter(connection)

    def execute(self, action, *, request=None, identity=None, record_id=None):
        if action not in CATALOGUE:
            raise ValueError("Unknown audit action")
        actor = resource = None
        error = None
        result = None
        try:
            with self.connection.transaction():
                try:
                    if action == "session.issue":
                        if not isinstance(identity, VerifiedIdentity):
                            raise HTTPException(401)
                        # Resolve through the trusted verified identity, never headers.
                        row = self.connection.execute(
                            "SELECT id FROM cpa.users WHERE issuer=%s AND subject=%s",
                            (identity.issuer, identity.subject),
                        ).fetchone()
                        actor = row[0] if row else None
                        result = self.sessions.issue_after_verification(identity)
                        outcome = "issued"
                    else:
                        token = bearer_token(request)
                        principal = self.sessions.validate(token)
                        actor = principal.user_id
                        if action == "session.logout":
                            self.sessions.logout(token)
                            outcome = "revoked"
                        elif action == "privileged.check":
                            raise HTTPException(403)
                        else:
                            try:
                                parsed = UUID(str(record_id))
                            except (ValueError, TypeError, AttributeError):
                                raise HTTPException(404) from None
                            row = self.connection.execute(
                                "SELECT id FROM cpa.access_records WHERE id=%s", (parsed,)
                            ).fetchone()
                            resource = row[0] if row else None
                            result = self.access.require(principal.identity, record_id)
                            outcome = "allowed"
                except HTTPException as exc:
                    error = exc
                    outcome = "unavailable" if exc.status_code == 503 else "denied"
                self.writer.write(action, outcome, actor, resource)
            if error:
                raise error
            return result
        except psycopg.Error:
            raise HTTPException(503, "Service unavailable.") from None


class OperationalCapture:
    """Explicit test sink; never reads payloads, headers, query or raw path."""
    def __init__(self, app, sink, route_names):
        self.app, self.sink = app, sink
        self.route_names = frozenset(route_names)

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        started = monotonic()
        status = 500
        request_id = str(uuid4())

        async def safe_send(message):
            nonlocal status
            if message["type"] == "http.response.start":
                status = message["status"]
            await send(message)

        try:
            await self.app(scope, receive, safe_send)
        finally:
            name = getattr(scope.get("route"), "name", None)
            method = scope.get("method")
            self.sink({
                "request_id": request_id,
                "route": name if name in self.route_names else "unmatched",
                "method": method if method in {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"} else "OTHER",
                "status": status if isinstance(status, int) and 100 <= status <= 599 else 500,
                "duration_ms": round(max(0, monotonic() - started) * 1000, 3),
            })
