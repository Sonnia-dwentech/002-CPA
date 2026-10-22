"""B013 synthetic persisted-policy checks; fresh disposable database each run."""
from uuid import UUID

import psycopg
from fastapi import HTTPException

from app.access import AccessStore, VerifiedIdentity
from check_local_database import main


def key(number):
    return UUID(int=number)


def run_checks(connection):
    outcomes = []

    def expect_error(code, operation):
        try:
            operation()
        except HTTPException as error:
            assert error.status_code == code, (error.status_code, code)
        else:
            raise AssertionError("Expected access denial")

    def constraint(operation):
        try:
            with connection.transaction():
                operation()
        except psycopg.IntegrityError:
            return
        raise AssertionError("Expected integrity rejection")

    # Entirely synthetic, deliberately non-live issuer and opaque subjects.
    def identity(number):
        return VerifiedIdentity("synthetic://b013", f"synthetic-{number}")

    with connection.transaction():
        connection.execute("INSERT INTO cpa.client_organisations VALUES (%s),(%s)", (key(101), key(102)))
        users = [
            (1, "internal", None, "cpa"), (2, "internal", None, "cpa"),
            (3, "internal", None, "executive"), (4, "internal", None, "access_admin"),
            (5, "internal", None, "product_authority"),
            (6, "client", 101, "client_user"), (7, "client", 101, "client_user"),
            (8, "client", 102, "client_user"), (9, "internal", None, "technical"),
        ]
        for number, category, client, role in users:
            connection.execute(
                "INSERT INTO cpa.users VALUES (%s,%s,%s,%s,%s,true,true)",
                (key(number), identity(number).issuer, identity(number).subject, category,
                 key(client) if client else None),
            )
            connection.execute("INSERT INTO cpa.user_roles VALUES (%s,%s,%s)",
                               (key(number), category, role))
        for number, kind, owner, client, case, author, state in [
            (201, "idea", 1, None, None, None, "draft"),
            (202, "dossier", 1, None, None, None, "draft"),
            (203, "technical", 1, None, None, None, "draft"),
            (301, "client_intake", 6, 101, None, None, "submitted"),
            (302, "client_intake", 8, 102, None, None, "submitted"),
            (303, "client_note", 6, 101, 301, 1, "draft"),
            (304, "client_response", 6, 101, 301, 1, "draft"),
            (305, "client_response", 6, 101, 301, 1, "published"),
        ]:
            connection.execute(
                "INSERT INTO cpa.access_records VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (key(number), kind, key(owner), key(client) if client else None,
                 key(case) if case else None, key(author) if author else None, state),
            )
        connection.execute("INSERT INTO cpa.case_assignments VALUES (%s,%s,'cpa'),(%s,%s,'approver')",
                           (key(301), key(1), key(301), key(5)))
    store = AccessStore(connection, {"idea", "dossier", "technical", "client_intake", "client_note", "client_response"})
    assert store.require(identity(1), key(201))["id"] == key(201)
    expect_error(401, lambda: store.require(None, key(201)))
    expect_error(401, lambda: store.require({"issuer": "synthetic://b013", "subject": "synthetic-1"}, key(201)))
    expect_error(401, lambda: store.require(identity(99), key(201)))
    expect_error(404, lambda: store.require(identity(2), key(201)))
    expect_error(404, lambda: store.require(identity(1), "invalid-id"))
    expect_error(404, lambda: AccessStore(connection).require(identity(1), key(201)))
    outcomes.append("identity mapping, private owner access, spoof rejection and default-disabled features")

    connection.execute("INSERT INTO cpa.record_grants VALUES (%s,%s,'read')", (key(201), key(2)))
    assert store.require(identity(2), key(201))["id"] == key(201)
    expect_error(403, lambda: store.require(identity(2), key(201), "edit"))
    expect_error(403, lambda: store.require(identity(2), key(201), "grant_role"))
    connection.execute("DELETE FROM cpa.record_grants WHERE user_id=%s", (key(2),))
    expect_error(404, lambda: store.require(identity(2), key(201)))
    outcomes.append("explicit grant, action separation and immediate grant revocation")

    for user in (3, 4, 5):
        expect_error(404, lambda user=user: store.require(identity(user), key(201)))
    connection.execute("INSERT INTO cpa.record_grants VALUES (%s,%s,'read')", (key(201), key(4)))
    expect_error(404, lambda: store.require(identity(4), key(201)))
    outcomes.append("executive, product-authority and administrator have no automatic content access")

    assert store.require(identity(6), key(301))["id"] == key(301)
    for user, resource in ((7, 301), (8, 301), (6, 302), (6, 303), (6, 304), (6, 201)):
        expect_error(404, lambda user=user, resource=resource: store.require(identity(user), key(resource)))
    assert store.require(identity(6), key(305))["state"] == "published"
    assert [r["id"] for r in store.visible(identity(6), "client_intake")] == [key(301)]
    assert [r["id"] for r in store.visible(identity(6), "client_response")] == [key(305)]
    assert store.visible(identity(7), "client_intake") == []
    outcomes.append("cross-client/same-organisation isolation, internal-note denial and filtered lists")

    assert store.require(identity(1), key(303))["id"] == key(303)
    connection.execute("DELETE FROM cpa.case_assignments WHERE user_id=%s", (key(1),))
    expect_error(404, lambda: store.require(identity(1), key(303)))
    expect_error(404, lambda: store.require(identity(1), key(305)))
    outcomes.append("case assignment revoked for direct and derived output access")

    assert store.require(identity(5), key(304), "publish")["id"] == key(304)
    connection.execute("UPDATE cpa.access_records SET author_id=%s WHERE id=%s", (key(5), key(304)))
    expect_error(403, lambda: store.require(identity(5), key(304), "publish"))
    outcomes.append("response author cannot self-approve")

    connection.execute("UPDATE cpa.users SET enabled=false WHERE id=%s", (key(1),))
    expect_error(401, lambda: store.require(identity(1), key(201)))
    connection.execute("UPDATE cpa.users SET enabled=true,membership_active=false WHERE id=%s", (key(1),))
    expect_error(401, lambda: store.require(identity(1), key(201)))
    outcomes.append("account suspension and membership removal revoke owner access")

    constraint(lambda: connection.execute(
        "INSERT INTO cpa.user_roles VALUES (%s,'client','access_admin')", (key(6),)))
    constraint(lambda: connection.execute(
        "INSERT INTO cpa.user_roles VALUES (%s,'internal','access_admin')", (key(6),)))
    constraint(lambda: connection.execute(
        "INSERT INTO cpa.users VALUES (%s,%s,%s,'internal',NULL,true,true)",
        (key(10), identity(2).issuer, identity(2).subject)))
    constraint(lambda: connection.execute(
        "UPDATE cpa.access_records SET client_id=%s WHERE id=%s", (key(102), key(305))))
    outcomes.append("database constraints reject role-category escalation, duplicate identity and cross-client linkage")

    # Corrupt metadata that is not covered by a simple FK still fails closed.
    connection.execute("UPDATE cpa.access_records SET owner_id=%s WHERE id=%s", (key(7), key(305)))
    expect_error(404, lambda: store.require(identity(7), key(305)))
    outcomes.append("inconsistent case ownership fails closed")

    # PostgreSQL query failure, inside a rolled-back schema change.
    try:
        with connection.transaction():
            connection.execute("ALTER TABLE cpa.record_grants RENAME TO grants_unavailable")
            expect_error(503, lambda: store.require(identity(2), key(201)))
            raise RuntimeError("rollback synthetic failure")
    except RuntimeError:
        pass
    assert connection.execute("SELECT to_regclass('cpa.record_grants')").fetchone()[0] is not None
    outcomes.append("database policy failure returns generic unavailable and never allows")
    return outcomes


if __name__ == "__main__":
    main(task="B013", extra_checks=run_checks)
