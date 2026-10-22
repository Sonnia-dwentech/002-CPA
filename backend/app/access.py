"""B013 server-side access boundary. No login, token parsing or HTTP identity input."""
from dataclasses import dataclass
from uuid import UUID

import psycopg
from psycopg.rows import dict_row
from fastapi import HTTPException

INTERNAL = frozenset({"idea", "research", "dossier", "technical"})
CLIENT = frozenset({"client_intake", "client_note", "client_response"})


@dataclass(frozen=True)
class VerifiedIdentity:
    """Only an approved B014 validator may construct this in application code.

    Tests construct synthetic identities directly. Never bind this class to
    request data or expose an endpoint accepting its fields.
    """
    issuer: str
    subject: str


def permits(actor, record, action, grants=frozenset(), assignments=frozenset()):
    """Pure policy over trusted repository state; unknown combinations deny."""
    if not actor or not record or not actor["enabled"] or not actor["membership_active"]:
        return False
    roles = actor["roles"]
    kind, state = record["kind"], record["state"]
    owner = actor["id"] == record["owner_id"]
    if kind in INTERNAL:
        if actor["category"] != "internal" or actor["client_id"] is not None or record["client_id"] is not None:
            return False
        cpa = "cpa" in roles
        technical = "technical" in roles
        reader = (
            (cpa and (owner or bool(grants & {"read", "edit"})))
            or (technical and bool(grants & {"read", "edit"}))
            or ("executive" in roles and "read" in grants)
        )
        editor = (cpa and (owner or "edit" in grants)) or (
            technical and kind == "technical" and "edit" in grants
        )
        if action == "read":
            return bool(reader)
        if action == "edit":
            return state == "draft" and bool(editor)
        if action in {"share", "revoke_share", "request_transfer"}:
            return cpa and owner
        if action == "archive":
            return cpa and owner and state == "draft"
        if action == "restore":
            return cpa and owner and state == "archived"
        if action == "export":
            return kind == "dossier" and bool(reader) and ((cpa and owner) or "export" in grants)
        if action == "run":
            return cpa and state == "draft" and bool(editor) and "run" in grants
        if action == "decision":
            return kind == "dossier" and "executive" in roles and bool(reader) and "decision" in grants
        return False
    if kind not in CLIENT or record["client_id"] is None:
        return False
    if actor["category"] == "client":
        if actor["client_id"] != record["client_id"] or "client_user" not in roles or not owner:
            return False
        if kind == "client_intake":
            return (action == "read" and state in {"draft", "submitted"}) or (
                action in {"edit", "submit"} and state == "draft"
            )
        return kind == "client_response" and state == "published" and action == "read"
    if actor["category"] != "internal" or actor["client_id"] is not None:
        return False
    cpa = "cpa" in roles and "cpa" in assignments
    approver = "product_authority" in roles and "approver" in assignments
    if action == "read":
        return bool(cpa or approver)
    if action == "edit":
        return cpa and kind in {"client_note", "client_response"} and state == "draft"
    if action == "publish":
        return (approver and kind == "client_response" and state == "draft"
                and record["author_id"] is not None and record["author_id"] != actor["id"])
    return False


class AccessStore:
    """Loads current policy metadata on each call; never caches permissions.

    All feature kinds are disabled by default. Later feature services must
    deliberately enable their approved kinds and use this boundary for every
    retrieval. This stores metadata, not business payloads.
    """
    def __init__(self, connection, enabled_kinds=frozenset()):
        self.connection = connection
        self.enabled_kinds = frozenset(enabled_kinds) & (INTERNAL | CLIENT)

    def _one(self, sql, args):
        with self.connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute(sql, args)
            return cursor.fetchone()

    def _actor(self, identity):
        if not isinstance(identity, VerifiedIdentity) or not identity.issuer or not identity.subject:
            return None
        actor = self._one(
            "SELECT * FROM cpa.users WHERE issuer=%s AND subject=%s",
            (identity.issuer, identity.subject),
        )
        if actor and actor["enabled"] and actor["membership_active"]:
            actor["roles"] = frozenset(row[0] for row in self.connection.execute(
                "SELECT role FROM cpa.user_roles WHERE user_id=%s", (actor["id"],)
            ).fetchall())
            return actor
        return None

    def _record(self, record_id):
        record = self._one("SELECT * FROM cpa.access_records WHERE id=%s", (record_id,))
        if not record or record["kind"] not in self.enabled_kinds:
            return None
        owner = self._one("SELECT category,client_id FROM cpa.users WHERE id=%s", (record["owner_id"],))
        if record["kind"] in INTERNAL:
            return record if owner and owner["category"] == "internal" else None
        if not owner or owner["category"] != "client" or owner["client_id"] != record["client_id"]:
            return None
        if record["case_id"] is not None:
            case = self._one("SELECT * FROM cpa.access_records WHERE id=%s", (record["case_id"],))
            if (not case or case["kind"] != "client_intake" or
                    case["client_id"] != record["client_id"] or case["owner_id"] != record["owner_id"]):
                return None
        return record

    def _permissions(self, actor, record):
        grants = frozenset(row[0] for row in self.connection.execute(
            "SELECT permission FROM cpa.record_grants WHERE record_id=%s AND user_id=%s",
            (record["id"], actor["id"]),
        ).fetchall())
        case_id = record["case_id"] or (record["id"] if record["kind"] == "client_intake" else None)
        assignments = frozenset(row[0] for row in self.connection.execute(
            "SELECT assignment FROM cpa.case_assignments WHERE case_id=%s AND user_id=%s",
            (case_id, actor["id"]),
        ).fetchall()) if case_id else frozenset()
        return grants, assignments

    def require(self, identity, record_id, action="read"):
        """Return authorised metadata, otherwise generic 401/404/403/503."""
        try:
            with self.connection.transaction():
                actor = self._actor(identity)
                if not actor:
                    raise HTTPException(401, "Authentication required.")
                try:
                    key = UUID(str(record_id))
                except (ValueError, TypeError, AttributeError):
                    raise HTTPException(404, "Resource not found.") from None
                record = self._record(key)
                if not record:
                    raise HTTPException(404, "Resource not found.")
                grants, assignments = self._permissions(actor, record)
                if not permits(actor, record, "read", grants, assignments):
                    raise HTTPException(404, "Resource not found.")
                if not permits(actor, record, action, grants, assignments):
                    raise HTTPException(403, "Access denied.")
                return record
        except psycopg.Error:
            raise HTTPException(503, "Service unavailable.") from None

    def visible(self, identity, kind):
        """Filtered reference list; counts must derive from this filtered result."""
        if kind not in self.enabled_kinds:
            return []
        try:
            with self.connection.transaction():
                if not self._actor(identity):
                    raise HTTPException(401, "Authentication required.")
                ids = self.connection.execute(
                    "SELECT id FROM cpa.access_records WHERE kind=%s ORDER BY id", (kind,)
                ).fetchall()
                result = []
                for (key,) in ids:
                    try:
                        result.append(self.require(identity, key))
                    except HTTPException as error:
                        if error.status_code != 404:
                            raise
                return result
        except psycopg.Error:
            raise HTTPException(503, "Service unavailable.") from None
