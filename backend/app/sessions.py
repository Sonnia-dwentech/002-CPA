"""Opaque local sessions; no password, provider, browser or public issuance flow."""
from dataclasses import dataclass, field
from datetime import timedelta
import hashlib
import re
import secrets
from uuid import UUID

from fastapi import HTTPException, Request
import psycopg
from psycopg.rows import dict_row

from app.access import AccessStore, VerifiedIdentity

IDLE_TIMEOUT = timedelta(minutes=30)
ABSOLUTE_TIMEOUT = timedelta(hours=8)
TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_-]{43}\Z")
PRIVILEGED_ACTIONS = frozenset({
    "publish", "decision", "grant_role", "grant", "share", "revoke_share",
    "transfer", "admin", "invite", "suspend", "restore_account",
})


def digest_token(token):
    if not isinstance(token, str) or not TOKEN_PATTERN.fullmatch(token):
        raise HTTPException(401, "Authentication required.")
    return hashlib.sha256(token.encode("ascii")).hexdigest()


def within_lifetime(now, issued_at, last_seen_at, expires_at):
    return (
        issued_at <= last_seen_at <= now
        and expires_at == issued_at + ABSOLUTE_TIMEOUT
        and now < expires_at
        and now < last_seen_at + IDLE_TIMEOUT
    )


def bearer_token(request: Request):
    values = request.headers.getlist("authorization")
    if len(values) != 1:
        raise HTTPException(401, "Authentication required.")
    parts = values[0].split(" ")
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(401, "Authentication required.")
    digest_token(parts[1])  # Exact syntax/length; never echo submitted values.
    return parts[1]


@dataclass(frozen=True)
class SessionPrincipal:
    identity: VerifiedIdentity
    user_id: UUID
    token_digest: str = field(repr=False)


class SessionStore:
    """Server-internal session service. Use a request-scoped connection.

    issue_after_verification is not a login endpoint. Only a future approved
    identity adapter may call it after verifying the human. Tests use synthetic
    identities; there is no route or configuration flag for issuing sessions.
    """
    def __init__(self, connection):
        self.connection = connection

    def issue_after_verification(self, identity):
        if not isinstance(identity, VerifiedIdentity):
            raise HTTPException(401, "Authentication required.")
        try:
            with self.connection.transaction():
                user = self.connection.execute(
                    "SELECT id FROM cpa.users WHERE issuer=%s AND subject=%s "
                    "AND enabled AND membership_active FOR UPDATE",
                    (identity.issuer, identity.subject),
                ).fetchone()
                if not user:
                    raise HTTPException(401, "Authentication required.")
                token = secrets.token_urlsafe(32)
                now = self.connection.execute("SELECT clock_timestamp()").fetchone()[0]
                self.connection.execute(
                    "INSERT INTO cpa.sessions VALUES (%s,%s,%s,%s,%s,NULL)",
                    (digest_token(token), user[0], now, now, now + ABSOLUTE_TIMEOUT),
                )
            return token
        except psycopg.Error:
            raise HTTPException(503, "Service unavailable.") from None

    def validate(self, token):
        digest = digest_token(token)
        principal = None
        try:
            with self.connection.transaction():
                # User first, then session: same lock order as account-change
                # revocation trigger and issuance. Recheck session after locking.
                user_id = self.connection.execute(
                    "SELECT user_id FROM cpa.sessions WHERE token_digest=%s", (digest,)
                ).fetchone()
                if user_id:
                    with self.connection.cursor(row_factory=dict_row) as cursor:
                        cursor.execute("SELECT * FROM cpa.users WHERE id=%s FOR UPDATE", (user_id[0],))
                        user = cursor.fetchone()
                        cursor.execute("SELECT * FROM cpa.sessions WHERE token_digest=%s FOR UPDATE", (digest,))
                        session = cursor.fetchone()
                    now = self.connection.execute("SELECT clock_timestamp()").fetchone()[0]
                    valid = (
                        user and session and session["user_id"] == user["id"]
                        and user["enabled"] and user["membership_active"]
                        and session["revoked_at"] is None
                        and within_lifetime(now, session["issued_at"], session["last_seen_at"], session["expires_at"])
                    )
                    if valid:
                        self.connection.execute(
                            "UPDATE cpa.sessions SET last_seen_at=%s WHERE token_digest=%s", (now, digest)
                        )
                        principal = SessionPrincipal(
                            VerifiedIdentity(user["issuer"], user["subject"]), user["id"], digest
                        )
                    elif session:
                        self.connection.execute(
                            "UPDATE cpa.sessions SET revoked_at=COALESCE(revoked_at,%s) WHERE token_digest=%s",
                            (now, digest),
                        )
            # Raise after commit so invalidation cannot be undone by the denial.
            if principal is None:
                raise HTTPException(401, "Authentication required.")
            return principal
        except psycopg.Error:
            raise HTTPException(503, "Service unavailable.") from None

    def logout(self, token):
        """Revoke exactly this session; no refresh or automatic reissuance."""
        digest = digest_token(token)
        try:
            with self.connection.transaction():
                self.connection.execute(
                    "UPDATE cpa.sessions SET revoked_at=COALESCE(revoked_at,clock_timestamp()) "
                    "WHERE token_digest=%s", (digest,)
                )
        except psycopg.Error:
            raise HTTPException(503, "Service unavailable.") from None


def authenticate(request: Request):
    token = bearer_token(request)
    store = getattr(request.state, "session_store", None)
    if not isinstance(store, SessionStore):
        raise HTTPException(503, "Service unavailable.")
    return store.validate(token)


def require_record(request: Request, record_id, action="read"):
    """Future routes call this instead of trusting a request's identity fields."""
    principal = authenticate(request)
    if action in PRIVILEGED_ACTIONS:
        # No caller-controlled MFA flag or invented assurance claim.
        raise HTTPException(403, "Access denied.")
    access = getattr(request.state, "access_store", None)
    if not isinstance(access, AccessStore):
        raise HTTPException(503, "Service unavailable.")
    return access.require(principal.identity, record_id, action)


def require_privileged(request: Request):
    """All privileged operations unavailable until approved MFA exists."""
    authenticate(request)
    raise HTTPException(403, "Access denied.")


def logout_request(request: Request):
    token = bearer_token(request)
    store = getattr(request.state, "session_store", None)
    if not isinstance(store, SessionStore):
        raise HTTPException(503, "Service unavailable.")
    store.logout(token)
