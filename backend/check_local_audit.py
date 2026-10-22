"""B017 disposable audit/redaction and transactional failure verification."""
import asyncio
from contextlib import redirect_stderr, redirect_stdout
import http.client
import io
import json
import secrets
import socket
import threading
import time
from uuid import UUID

from fastapi import Request
import psycopg
import uvicorn
from app.access import VerifiedIdentity
from app.audit import AuditedActions, AuditWriter, OperationalCapture
from app.main import create_app
from app.sessions import digest_token
from check_local_database import main
from check_local_sessions import run_checks as prior_checks
from tests.test_api import request as asgi_request


def run_checks(connection):
    outcomes = prior_checks(connection)
    service = AuditedActions(connection)
    events = []
    canary = "SYNTHETIC_PRIVATE_" + secrets.token_hex(12)
    identity = VerifiedIdentity("synthetic://b013", "synthetic-6")
    app = create_app()
    tokens = []

    @app.post("/fixture", name="fixture_issue")
    async def issue():
        # Only this in-process fixture app exposes issuance. Never normal startup.
        token = service.execute("session.issue", identity=identity)
        tokens.append(token)
        return {"token": token}

    @app.post("/logout", name="fixture_logout")
    async def logout(request: Request):
        service.execute("session.logout", request=request)
        return {"ok": True}

    @app.get("/records/{record_id}", name="fixture_read")
    async def read(request: Request, record_id: str):
        service.execute("record.read", request=request, record_id=record_id)
        return {"synthetic": True}

    @app.post("/privileged", name="fixture_privileged")
    async def privileged(request: Request):
        service.execute("privileged.check", request=request)

    @app.get("/failure", name="fixture_failure")
    async def failure():
        raise RuntimeError(canary)

    captured_app = OperationalCapture(app, events.append, {
        "fixture_issue", "fixture_logout", "fixture_read", "fixture_privileged", "fixture_failure",
    })
    output = io.StringIO()

    def call(path, method="GET", token=None, body=b"", query=b""):
        headers = [(b"x-request-id", canary.encode()), (b"user-agent", canary.encode()),
                   (b"x-role", canary.encode()), (b"cookie", canary.encode())]
        if token:
            headers.append((b"authorization", ("Bearer " + token).encode()))
        return asyncio.run(asgi_request(captured_app, path, method=method, headers=headers, body=body, query=query))

    own = "/records/" + str(UUID(int=301))
    other = "/records/" + str(UUID(int=302))
    with redirect_stdout(output), redirect_stderr(output):
        assert call(own)[0] == 401
        token = call("/fixture", "POST", body=canary.encode())[2]["token"]
        assert call(own, token=token, query=canary.encode())[0] == 200
        assert call(other, token=token)[0] == 404
        assert call("/records/" + canary, token=token)[0] == 404
        assert call("/privileged", "POST", token)[0] == 403
        assert call("/failure")[0] == 500
        assert call("/" + canary)[0] == 404
        assert call("/logout", "POST", token)[0] == 200
        assert call(own, token=token)[0] == 401
        assert call("/audit")[0] == 404
        assert call("/audit/export")[0] == 404
    rows = connection.execute(
        "SELECT id,occurred_at,actor_id,resource_id,action,outcome FROM cpa.audit_events ORDER BY id"
    ).fetchall()
    assert len(rows) == 8
    assert rows[0][2:4] == (None, None)
    assert rows[1][2] == UUID(int=6) and rows[1][4:] == ("session.issue", "issued")
    assert rows[2][2:4] == (UUID(int=6), UUID(int=301))
    assert rows[3][3] == UUID(int=302) and rows[3][5] == "denied"
    assert rows[4][3] is None
    assert rows[5][4:] == ("privileged.check", "denied")
    assert rows[6][4:] == ("session.logout", "revoked")
    assert all(row[1].tzinfo is not None for row in rows)
    assert all(a[1] <= b[1] for a, b in zip(rows, rows[1:]))
    outcomes.append("B017 actual session/read/logout/privileged events retain verified IDs, fixed outcomes and ordered timezone-aware times")

    assert all(set(e) == {"request_id", "route", "method", "status", "duration_ms"} for e in events)
    assert len({e["request_id"] for e in events}) == len(events)
    assert all(UUID(e["request_id"]) and e["duration_ms"] >= 0 for e in events)
    assert any(e["route"] == "unmatched" and e["status"] == 404 for e in events)
    assert any(e["route"] == "fixture_failure" and e["status"] == 500 for e in events)
    serialized = json.dumps(rows, default=str) + json.dumps(events) + output.getvalue()
    assert canary not in serialized and all(t not in serialized and digest_token(t) not in serialized for t in tokens)
    outcomes.append("B017 canaries in payload/header/cookie/query/path/exception absent from audit and operational output; request IDs cannot be spoofed")

    # Force audit persistence failure; successful session changes must roll back.
    token = service.execute("session.issue", identity=identity)
    before = connection.execute("SELECT count(*) FROM cpa.sessions").fetchone()[0]
    connection.execute("ALTER TABLE cpa.audit_events RENAME TO audit_events_temporarily_offline")
    try:
        assert call("/fixture", "POST")[0] == 503
        assert connection.execute("SELECT count(*) FROM cpa.sessions").fetchone()[0] == before
        assert call("/logout", "POST", token)[0] == 503
        assert connection.execute("SELECT revoked_at FROM cpa.sessions WHERE token_digest=%s",
                                  (digest_token(token),)).fetchone()[0] is None
    finally:
        connection.execute("ALTER TABLE cpa.audit_events_temporarily_offline RENAME TO audit_events")
    assert call("/logout", "POST", token)[0] == 200
    outcomes.append("B017 missing audit storage returns 503 and rolls back session issuance/logout; restored storage recovers")

    connection.execute("ALTER TABLE cpa.sessions RENAME TO sessions_temporarily_offline")
    try:
        assert call(own, token=token)[0] == 503
        latest = connection.execute(
            "SELECT actor_id,resource_id,action,outcome FROM cpa.audit_events ORDER BY id DESC LIMIT 1"
        ).fetchone()
        assert latest == (None, None, "record.read", "unavailable")
    finally:
        connection.execute("ALTER TABLE cpa.sessions_temporarily_offline RENAME TO sessions")
    outcomes.append("B017 session-storage outage records unavailable with unknown IDs omitted")

    # Reject free text and untrusted identifier types before reaching storage.
    writer = AuditWriter(connection)
    for args in [(canary, "allowed"), ("record.read", canary), ("record.read", "allowed", canary)]:
        try:
            writer.write(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("Unapproved metadata accepted")
    try:
        with connection.transaction():
            connection.execute("INSERT INTO cpa.audit_events(action,outcome) VALUES ('record.read','invented')")
    except psycopg.errors.CheckViolation:
        pass
    else:
        raise AssertionError("Database accepted unknown outcome")
    assert connection.execute(
        "SELECT count(*) FROM information_schema.role_table_grants WHERE table_schema='cpa' "
        "AND table_name='audit_events' AND grantee='PUBLIC'"
    ).fetchone()[0] == 0
    normal = create_app()
    assert asyncio.run(asgi_request(normal, "/audit"))[0] == 404
    outcomes.append("B017 audit schema/writer reject arbitrary metadata; no PUBLIC grants or HTTP audit reader")

    # Actual HTTP capture, with framework access/exception output disabled for
    # this explicit test server. Normal server configuration is untouched.
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    server = uvicorn.Server(uvicorn.Config(captured_app, host="127.0.0.1", port=port,
                                          access_log=False, log_level="critical"))
    thread = threading.Thread(target=server.run, daemon=True)
    wire_output = io.StringIO()
    with redirect_stdout(wire_output), redirect_stderr(wire_output):
        try:
            thread.start()
            deadline = time.monotonic() + 10
            while not server.started and time.monotonic() < deadline:
                time.sleep(.05)
            assert server.started
            for path, expected in [("/failure?private=" + canary, 500), ("/" + canary, 404), (own, 401)]:
                client = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
                try:
                    client.request("GET", path, headers={"User-Agent": canary, "Authorization": "Bearer " + canary})
                    response = client.getresponse()
                    assert response.status == expected
                    assert canary.encode() not in response.read()
                finally:
                    client.close()
        finally:
            server.should_exit = True
            thread.join(timeout=10)
    assert not thread.is_alive()
    assert canary not in wire_output.getvalue() + json.dumps(events)
    outcomes.append("B017 real loopback HTTP 500/404/401 capture redacted; framework output contains no canary and server stopped")
    return outcomes


if __name__ == "__main__":
    main("B017", run_checks)
