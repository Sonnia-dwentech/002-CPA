"""B021 actual PostgreSQL harness; requires existing offline Docker setup.

Prepared on the current workstation; not executed without Docker. Uses only the
disposable runner's database and synthetic metadata, never an existing store.
"""
from uuid import UUID
from fastapi import HTTPException

from app.access import VerifiedIdentity
from app.dashboard import DashboardStore
from check_local_database import main


def run_checks(connection):
    key = lambda value: UUID(int=value)
    identity = lambda value: VerifiedIdentity("synthetic://b021", str(value))
    outcomes = []

    def deny(code, operation):
        try:
            operation()
        except HTTPException as error:
            assert error.status_code == code
        else:
            raise AssertionError("Expected dashboard denial")

    with connection.transaction():
        for number in (1, 2, 3):
            connection.execute("INSERT INTO cpa.users VALUES (%s,%s,%s,'internal',NULL,true,true)",
                               (key(number), identity(number).issuer, identity(number).subject))
            connection.execute("INSERT INTO cpa.user_roles VALUES (%s,'internal','cpa')", (key(number),))
        for number, owner, kind, state in ((11, 1, "idea", "draft"), (12, 2, "idea", "draft"),
                                           (13, 1, "dossier", "archived"), (14, 3, "idea", "draft")):
            connection.execute("INSERT INTO cpa.access_records VALUES (%s,%s,%s,NULL,NULL,NULL,%s)",
                               (key(number), kind, key(owner), state))
        connection.execute("INSERT INTO cpa.record_grants VALUES (%s,%s,'read'),(%s,%s,'edit')",
                           (key(12), key(1), key(12), key(1)))
    store = DashboardStore(connection, {"idea", "dossier"})
    result = store.query(identity(1))
    assert result.total == 3 and [r.id for r in result.records] == [key(11), key(12), key(13)]
    outcomes.append("persisted owner/shared references counted once; unshared reference excluded")
    assert store.query(identity(1), {"kind": "idea", "state": "draft", "owner_id": str(key(2))}).total == 1
    assert store.query(identity(1), {"state": "archived"}).total == 1
    assert store.query(identity(1), {"owner_id": str(key(3))}).status == "empty"
    assert store.query(identity(1), {"kind": "research"}).total is None
    outcomes.append("combined filters, archived references, empty and unavailable states")
    connection.execute("DELETE FROM cpa.record_grants WHERE user_id=%s", (key(1),))
    assert store.query(identity(1)).total == 2
    outcomes.append("revocation visible on next snapshot")
    connection.execute("UPDATE cpa.users SET membership_active=false WHERE id=%s", (key(1),))
    deny(401, lambda: store.query(identity(1)))
    connection.execute("UPDATE cpa.users SET membership_active=true WHERE id=%s", (key(1),))
    deny(401, lambda: store.query(identity(999)))
    outcomes.append("inactive and unknown identities denied")
    deny(422, lambda: store.query(identity(1), {"date": "unsupported"}))
    with connection.transaction():
        deny(503, lambda: store.query(identity(1)))
    outcomes.append("unsupported filters and pre-existing transactions rejected")
    connection.execute("ALTER TABLE cpa.access_records RENAME TO synthetic_hidden_records")
    try:
        deny(503, lambda: store.query(identity(1)))
    finally:
        connection.execute("ALTER TABLE cpa.synthetic_hidden_records RENAME TO access_records")
    assert store.query(identity(1)).total == 2
    outcomes.append("real query failure returns unavailable, then recovers without false zero")
    return outcomes


if __name__ == "__main__":
    main(task="B021", extra_checks=run_checks)
