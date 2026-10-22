"""Synthetic repository doubles; not evidence of actual PostgreSQL execution."""
from contextlib import contextmanager
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from uuid import UUID

from fastapi import HTTPException
import psycopg
from psycopg.pq import TransactionStatus

from app.access import VerifiedIdentity, permits
from app.dashboard import DashboardStore, parse_filters


def key(number):
    return UUID(int=number)


class Connection:
    def __init__(self):
        self.info = SimpleNamespace(transaction_status=TransactionStatus.IDLE)
        self.commands = []
        self.transactions = 0

    @contextmanager
    def transaction(self):
        self.transactions += 1
        yield

    def execute(self, sql):
        self.commands.append(sql)


class References:
    """Test-only backing data uses the actual pure B013 permission function."""
    def __init__(self):
        self.actor = dict(id=key(1), category="internal", client_id=None,
                          enabled=True, membership_active=True, roles=frozenset({"cpa"}))
        self.rows = [self.row(11, "idea", 1), self.row(12, "idea", 2),
                     self.row(13, "dossier", 1, "archived"), self.row(14, "idea", 3)]
        self.grants = {key(12): frozenset({"read", "edit"})}
        self.assignments = {}
        self.fail = False

    @staticmethod
    def row(number, kind, owner, state="draft", client=None, case=None):
        return dict(id=key(number), kind=kind, owner_id=key(owner), state=state,
                    client_id=client, case_id=case, author_id=None)

    def _actor(self, identity):
        return self.actor if (identity.subject == "known" and self.actor["enabled"]
                              and self.actor["membership_active"]) else None

    def visible(self, identity, kind):
        if self.fail:
            raise psycopg.OperationalError("synthetic-private-database-canary")
        return [r for r in self.rows if r["kind"] == kind and permits(
            self.actor, r, "read", self.grants.get(r["id"], frozenset()),
            self.assignments.get(r["case_id"] or r["id"], frozenset()))]


class DashboardTests(unittest.TestCase):
    def setUp(self):
        self.conn = Connection()
        self.refs = References()
        self.identity = VerifiedIdentity("synthetic://b021", "known")
        with patch("app.dashboard.AccessStore", return_value=self.refs):
            self.store = DashboardStore(self.conn, {"idea", "dossier", "client_intake"})

    def error(self, code, operation):
        with self.assertRaises(HTTPException) as caught:
            operation()
        self.assertEqual(caught.exception.status_code, code)
        return caught.exception

    def test_counts_equal_visible_list_not_all_records(self):
        result = self.store.query(self.identity)
        self.assertEqual(result.total, 3)
        self.assertEqual([r.id for r in result.records], [key(11), key(12), key(13)])
        self.assertEqual(result.data_kind, "synthetic_reference_records")
        self.assertEqual(result.business_metrics_status, "unavailable")

    def test_filters_combine_and_include_archived_when_omitted(self):
        self.assertEqual(self.store.query(self.identity, {"state": "archived"}).total, 1)
        result = self.store.query(self.identity, {"kind": "idea", "state": "draft", "owner_id": str(key(2))})
        self.assertEqual([r.id for r in result.records], [key(12)])
        self.assertEqual(self.store.query(self.identity, {"kind": "dossier", "state": "draft"}).status, "empty")

    def test_owner_filter_cannot_disclose_inaccessible_owner(self):
        for owner in (3, 999):
            result = self.store.query(self.identity, {"owner_id": str(key(owner))})
            self.assertEqual((result.status, result.total, result.records), ("empty", 0, ()))

    def test_grant_revocation_reflected_on_next_query(self):
        self.assertEqual(self.store.query(self.identity).total, 3)
        self.refs.grants.clear()
        self.assertEqual(self.store.query(self.identity).total, 2)

    def test_disabled_and_unknown_actors_deny(self):
        self.error(401, lambda: self.store.query(None))
        self.error(401, lambda: self.store.query(VerifiedIdentity("synthetic://b021", "unknown")))
        for field in ("enabled", "membership_active"):
            self.refs.actor[field] = False
            self.error(401, lambda: self.store.query(self.identity))
            self.refs.actor[field] = True

    def test_clients_denied_dashboard_even_for_own_references(self):
        self.refs.actor.update(category="client", client_id=key(100), roles=frozenset({"client_user"}))
        self.error(403, lambda: self.store.query(self.identity))

    def test_titles_do_not_grant_aggregate_access(self):
        self.refs.grants.clear()
        for role in ("executive", "access_admin", "developer"):
            self.refs.actor["roles"] = frozenset({role})
            self.assertEqual(self.store.query(self.identity).total, 0)

    def test_case_assignment_limits_client_reference_visibility(self):
        self.refs.rows = [self.refs.row(21, "client_intake", 6, client=key(100)),
                          self.refs.row(22, "client_intake", 7, client=key(200))]
        self.refs.assignments[key(21)] = frozenset({"cpa"})
        self.assertEqual([r.id for r in self.store.query(self.identity).records], [key(21)])

    def test_unavailable_is_not_empty(self):
        result = self.store.query(self.identity, {"kind": "research"})
        self.assertEqual((result.status, result.total), ("unavailable", None))
        with patch("app.dashboard.AccessStore", return_value=self.refs):
            disabled = DashboardStore(self.conn)
        self.assertIsNone(disabled.query(self.identity).total)

    def test_invalid_filters_rejected_without_echo(self):
        for values in ({"kind": "invalid"}, {"state": None}, {"owner_id": "private-canary"},
                       {"date": "today"}, {"geography": "all"}, {"owner_id": 1}, {"kind": []}, []):
            error = self.error(422, lambda: parse_filters(values))
            self.assertNotIn("private-canary", error.detail)

    def test_query_error_never_becomes_zero(self):
        self.refs.fail = True
        error = self.error(503, lambda: self.store.query(self.identity))
        self.assertNotIn("canary", error.detail)

    def test_snapshot_requested_and_busy_connection_rejected(self):
        self.store.query(self.identity)
        self.assertEqual(self.conn.commands, ["SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY"])
        self.assertEqual(self.conn.transactions, 1)
        self.conn.info.transaction_status = TransactionStatus.INTRANS
        self.error(503, lambda: self.store.query(self.identity))

    def test_duplicate_rows_do_not_inflate_count(self):
        self.refs.rows.append(dict(self.refs.rows[0]))
        self.assertEqual(self.store.query(self.identity).total, 3)

    def test_invalid_enabled_kind_rejected(self):
        with self.assertRaisesRegex(ValueError, "^Invalid dashboard kinds$"):
            DashboardStore(self.conn, {"unknown"})
