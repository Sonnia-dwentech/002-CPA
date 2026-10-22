"""B014 tests with actual disposable PostgreSQL and backend HTTP processing."""
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
import uvicorn

from app.access import AccessStore, VerifiedIdentity
from app.main import create_app
from app.sessions import SessionStore, authenticate, require_record, require_privileged, logout_request, digest_token
from check_local_access import run_checks as access_checks
from check_local_database import main
from tests.test_api import request as asgi_request


def run_checks(connection):
    outcomes = access_checks(connection)
    store = SessionStore(connection)
    access = AccessStore(connection, {"idea", "client_intake"})
    tokens = []
    key = lambda n: UUID(int=n)
    for n, category, client, role in [
        (401, "internal", None, "cpa"),
        (402, "client", 101, "client_user"),
        (403, "client", 102, "client_user"),
    ]:
        connection.execute("INSERT INTO cpa.users VALUES (%s,'synthetic://b014',%s,%s,%s,true,true)",
                           (key(n), f"synthetic-{n}", category, key(client) if client else None))
        connection.execute("INSERT INTO cpa.user_roles VALUES (%s,%s,%s)", (key(n), category, role))
    for n, owner, kind, client in [(501, 401, "idea", None), (502, 402, "client_intake", 101),
                                   (503, 403, "client_intake", 102)]:
        connection.execute(
            "INSERT INTO cpa.access_records VALUES (%s,%s,%s,%s,NULL,NULL,'draft')",
            (key(n), kind, key(owner), key(client) if client else None))

    def issue(n=401):
        token = store.issue_after_verification(VerifiedIdentity("synthetic://b014", f"synthetic-{n}"))
        tokens.append(token)
        return token

    app = create_app()

    @app.middleware("http")
    async def synthetic_test_connections(request: Request, call_next):
        # Test-only wiring; production needs request-scoped connection lifecycle.
        request.state.session_store = store
        request.state.access_store = access
        return await call_next(request)

    @app.get("/test-only/session")
    async def session(request: Request):
        principal = authenticate(request)
        return {"authenticated": True, "user_id": str(principal.user_id)}

    @app.get("/test-only/records/{record_id}")
    async def read_record(request: Request, record_id: str):
        record = require_record(request, record_id)
        return {"id": str(record["id"]), "synthetic": True}

    @app.post("/test-only/privileged")
    async def privileged(request: Request):
        require_privileged(request)
        raise AssertionError("Privileged action must not execute")

    @app.post("/test-only/logout")
    async def logout(request: Request):
        logout_request(request)
        return {"logged_out": True}

    def call(token=None, path="/test-only/session", method="GET", extra=None, query=b""):
        headers = [(b"authorization", ("Bearer " + token).encode())] if token is not None else []
        headers += extra or []
        result = asyncio.run(asgi_request(app, path, method=method, headers=headers, query=query))
        assert all(t not in json.dumps(result[2]) for t in tokens)
        return result

    captured = io.StringIO()
    with redirect_stdout(captured), redirect_stderr(captured):
        token = issue()
        assert call(token)[0] == 200
        assert call(token, "/test-only/records/" + str(key(501)))[0] == 200
        outcomes.append("valid persisted session reaches an authorised B013 record over HTTP")

        missing_status, missing_headers, _ = call()
        assert missing_status == 401
        assert missing_headers[b"www-authenticate"] == b"Bearer"
        assert missing_headers[b"cache-control"] == b"no-store"
        tampered = ("B" if token[0] != "B" else "C") + token[1:]
        assert call(tampered)[0] == 401
        assert call(secrets.token_urlsafe(32))[0] == 401
        assert call("malformed-SYNTHETIC-CREDENTIAL")[0] == 401
        assert call(token, extra=[(b"authorization", ("Bearer " + token).encode())])[0] == 401
        assert call(query=("token=" + token).encode())[0] == 401
        assert call(extra=[(b"cookie", ("session=" + token).encode())])[0] == 401
        outcomes.append("missing/unknown/malformed/duplicate/query/cookie credentials rejected")

        absolute = connection.execute("SELECT expires_at FROM cpa.sessions WHERE token_digest=%s",
                                      (digest_token(token),)).fetchone()[0]
        assert call(token)[0] == 200
        assert connection.execute("SELECT expires_at FROM cpa.sessions WHERE token_digest=%s",
                                  (digest_token(token),)).fetchone()[0] == absolute
        outcomes.append("activity leaves the absolute expiry unchanged")

        idle = issue()
        # One timestamp CTE ensures exact 8-hour constraint despite clock changes.
        connection.execute(
            "WITH t AS (SELECT clock_timestamp() AS n) UPDATE cpa.sessions SET "
            "issued_at=t.n-interval '2 hours',last_seen_at=t.n-interval '31 minutes',"
            "expires_at=t.n+interval '6 hours' FROM t WHERE token_digest=%s", (digest_token(idle),))
        assert call(idle)[0] == 401
        assert connection.execute("SELECT revoked_at IS NOT NULL FROM cpa.sessions WHERE token_digest=%s",
                                  (digest_token(idle),)).fetchone()[0]
        outcomes.append("idle-expired session rejected and invalidation committed")

        expired = issue()
        connection.execute(
            "WITH t AS (SELECT clock_timestamp() AS n) UPDATE cpa.sessions SET "
            "issued_at=t.n-interval '9 hours',last_seen_at=t.n-interval '2 hours',"
            "expires_at=t.n-interval '1 hour' FROM t WHERE token_digest=%s", (digest_token(expired),))
        assert call(expired)[0] == 401
        outcomes.append("absolute-expired session rejected against actual database time")

        future = issue()
        connection.execute(
            "WITH t AS (SELECT clock_timestamp() AS n) UPDATE cpa.sessions SET "
            "issued_at=t.n+interval '1 minute',last_seen_at=t.n+interval '1 minute',"
            "expires_at=t.n+interval '481 minutes' FROM t WHERE token_digest=%s", (digest_token(future),))
        assert call(future)[0] == 401
        outcomes.append("future session timestamps fail closed")

        second = issue()
        assert call(token, "/test-only/logout", "POST")[0] == 200
        assert call(token)[0] == 401
        assert call(second)[0] == 200
        store.logout(second)
        assert call(second)[0] == 401
        outcomes.append("logout and explicit revocation deny replay without ending another session")

        suspended = issue()
        connection.execute("UPDATE cpa.users SET enabled=false WHERE id=%s", (key(401),))
        # Restore before the first validation: trigger must still invalidate.
        connection.execute("UPDATE cpa.users SET enabled=true WHERE id=%s", (key(401),))
        assert call(suspended)[0] == 401
        removed = issue()
        connection.execute("UPDATE cpa.users SET membership_active=false WHERE id=%s", (key(401),))
        assert call(removed)[0] == 401
        connection.execute("UPDATE cpa.users SET membership_active=true WHERE id=%s", (key(401),))
        assert call(removed)[0] == 401
        outcomes.append("suspension/remembership cannot resurrect old sessions")

        client = issue(402)
        assert call(client, "/test-only/records/" + str(key(502)))[0] == 200
        assert call(client, "/test-only/records/" + str(key(503)),
                    extra=[(b"x-user-id", str(key(403)).encode()), (b"x-role", b"access_admin")])[0] == 404
        assert call(client, "/test-only/records/" + str(key(501)))[0] == 404
        outcomes.append("session identity cannot be overridden; cross-client/internal requests denied")

        active = issue()
        assert call(active, "/test-only/privileged", "POST",
                    extra=[(b"x-mfa", b"true"), (b"x-role", b"access_admin")])[0] == 403
        assert call(None, "/test-only/privileged", "POST")[0] == 401
        outcomes.append("privileged actions cannot bypass unconfigured MFA")

        try:
            with connection.transaction():
                connection.execute("ALTER TABLE cpa.sessions RENAME TO sessions_unavailable")
                status, _, body = call(active)
                assert status == 503 and body["error"]["message"] == "Service unavailable."
                raise RuntimeError("rollback synthetic outage")
        except RuntimeError:
            pass
        assert call(active)[0] == 200
        outcomes.append("session-store outage returns generic 503 with no protected response")

        data = repr(connection.execute("SELECT * FROM cpa.sessions").fetchall())
        assert all(t not in data for t in tokens)
        outcomes.append("session table contains hashes rather than raw credentials")

        # Actual loopback HTTP server, no browser, external service or token log.
        with socket.socket() as listener:
            listener.bind(("127.0.0.1", 0))
            listener.listen(10)
            port = listener.getsockname()[1]
            server = uvicorn.Server(uvicorn.Config(
                app, host="127.0.0.1", port=port, access_log=False,
                log_level="critical", server_header=False, proxy_headers=False,
            ))
            thread = threading.Thread(target=server.run, kwargs={"sockets": [listener]}, daemon=True)
            thread.start()
            try:
                deadline = time.monotonic() + 10
                while not server.started and thread.is_alive() and time.monotonic() < deadline:
                    time.sleep(0.02)
                assert server.started
                for headers, expected in (({}, 401), ({"Authorization": "Bearer " + active}, 200)):
                    client_http = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
                    try:
                        client_http.request("GET", "/test-only/session", headers=headers)
                        response = client_http.getresponse()
                        payload = response.read().decode()
                        assert response.status == expected
                        assert all(t not in payload for t in tokens)
                    finally:
                        client_http.close()
            finally:
                server.should_exit = True
                thread.join(10)
                assert not thread.is_alive(), "Loopback server did not stop"
        outcomes.append("real loopback HTTP rejects missing credentials and accepts valid session; server stopped")
    assert all(t not in captured.getvalue() for t in tokens)
    assert "malformed-SYNTHETIC-CREDENTIAL" not in captured.getvalue()
    outcomes.append("captured application diagnostics contain no test credentials")
    return outcomes


if __name__ == "__main__":
    main(task="B014", extra_checks=run_checks)
