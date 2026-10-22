import unittest

from app.access import permits


def actor(role="cpa", category="internal", user="owner", client=None):
    return dict(id=user, category=category, client_id=client, enabled=True,
                membership_active=True, roles=frozenset({role}))


def record(kind="idea", owner="owner", client=None, state="draft", author=None):
    return dict(kind=kind, owner_id=owner, client_id=client, state=state, author_id=author)


class AccessPolicyTests(unittest.TestCase):
    def test_owner_grants_are_limited(self):
        a, r = actor(), record()
        for action in ("read", "edit", "share", "archive", "request_transfer"):
            self.assertTrue(permits(a, r, action), action)
        for action in ("delete", "publish", "transfer", "grant_role", "run", "unknown"):
            self.assertFalse(permits(a, r, action), action)
        self.assertTrue(permits(a, r, "run", {"run"}))

    def test_read_does_not_imply_edit_or_export(self):
        a, r = actor(user="reader"), record(kind="dossier")
        self.assertTrue(permits(a, r, "read", {"read"}))
        for action in ("edit", "export", "run", "share"):
            self.assertFalse(permits(a, r, action, {"read"}))
        self.assertTrue(permits(a, r, "export", {"read", "export"}))

    def test_titles_do_not_grant_content(self):
        for role in ("executive", "technical", "product_authority", "access_admin", "developer"):
            self.assertFalse(permits(actor(role), record(), "read"), role)
        self.assertFalse(permits(actor("access_admin"), record(), "read", {"read", "edit", "export"}))

    def test_technical_edit_only_technical_draft(self):
        a = actor("technical", user="reviewer")
        self.assertTrue(permits(a, record("technical"), "edit", {"edit"}))
        self.assertFalse(permits(a, record("idea"), "edit", {"edit"}))
        self.assertFalse(permits(a, record("technical", state="published"), "edit", {"edit"}))

    def test_client_cannot_stack_internal_role(self):
        a = actor("cpa", "client", client="client-a")
        self.assertFalse(permits(a, record(), "read", {"read", "edit"}))

    def test_same_organisation_is_not_ownership(self):
        a = actor("client_user", "client", user="other", client="client-a")
        r = record("client_intake", client="client-a")
        self.assertFalse(permits(a, r, "read", {"read"}))

    def test_client_own_intake_only_editable_before_submit(self):
        a = actor("client_user", "client", client="client-a")
        r = record("client_intake", client="client-a")
        for action in ("read", "edit", "submit"):
            self.assertTrue(permits(a, r, action))
        r["state"] = "submitted"
        self.assertTrue(permits(a, r, "read"))
        self.assertFalse(permits(a, r, "edit"))
        self.assertFalse(permits(a, r, "submit"))

    def test_client_only_published_response_never_notes(self):
        a = actor("client_user", "client", client="client-a")
        for kind, state, expected in (("client_response", "draft", False),
                                      ("client_response", "published", True),
                                      ("client_note", "published", False)):
            self.assertEqual(permits(a, record(kind, client="client-a", state=state), "read"), expected)
        self.assertFalse(permits(a, record("client_response", client="client-b", state="published"), "read"))

    def test_assignment_and_role_both_required(self):
        r = record("client_note", client="client-a")
        a = actor(user="worker")
        self.assertFalse(permits(a, r, "read"))
        self.assertTrue(permits(a, r, "read", assignments={"cpa"}))
        self.assertFalse(permits(actor("developer"), r, "read", assignments={"cpa"}))

    def test_response_author_cannot_approve_own_response(self):
        a = actor("product_authority", user="approver")
        r = record("client_response", client="client-a", author="approver")
        self.assertFalse(permits(a, r, "publish", assignments={"approver"}))
        r["author_id"] = "different-human"
        self.assertTrue(permits(a, r, "publish", assignments={"approver"}))
        r["state"] = "published"
        self.assertFalse(permits(a, r, "publish", assignments={"approver"}))

    def test_disabled_membership_and_unknown_inputs_deny(self):
        a, r = actor(), record()
        a["enabled"] = False
        self.assertFalse(permits(a, r, "read"))
        a["enabled"], a["membership_active"] = True, False
        self.assertFalse(permits(a, r, "read"))
        self.assertFalse(permits(None, r, "read"))
        self.assertFalse(permits(actor(), None, "read"))
        self.assertFalse(permits(actor(), record("unknown"), "read"))

    def test_executive_decision_needs_read_and_capability(self):
        a, r = actor("executive"), record("dossier")
        self.assertFalse(permits(a, r, "decision", {"read"}))
        self.assertTrue(permits(a, r, "decision", {"read", "decision"}))
        self.assertFalse(permits(a, record("idea"), "decision", {"read", "decision"}))
