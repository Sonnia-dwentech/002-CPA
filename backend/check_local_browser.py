"""B016 isolated browser/BFF/backend/PostgreSQL harness. No production login."""
import asyncio
import http.client
import json
import os
from pathlib import Path
import secrets
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time

from fastapi import HTTPException, Request
import uvicorn
from app.main import create_app
from app.access import AccessStore, VerifiedIdentity
from app.sessions import SessionStore, authenticate, require_record, require_privileged, logout_request
from check_local_database import main
from check_local_sessions import run_checks as previous_checks
from tests.test_api import request as asgi_request

ROOT = Path(__file__).resolve().parent.parent
STOP = ROOT / "docs/evidence/B016-stop"


def call(port, path, method="GET", headers=None):
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=40)
    try:
        connection.request(method, path, headers=headers or {})
        response = connection.getresponse()
        return response.status, dict(response.getheaders()), response.read().decode()
    finally:
        connection.close()


def run_checks(connection):
    outcomes = previous_checks(connection)
    # Reject port collisions before any server startup; never replace listeners.
    for port in (8100, 3100):
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", port))
    key = secrets.token_urlsafe(32)
    store = SessionStore(connection)
    access = AccessStore(connection, {"idea", "client_intake"})
    app = create_app()
    available = True
    issued_tokens = []
    lock = asyncio.Lock()

    @app.middleware("http")
    async def stores(request, next_handler):
        async with lock:
            request.state.session_store = store if available else None
            request.state.access_store = access if available else None
            response = await next_handler(request)
            response.headers["Cache-Control"] = "no-store"
            return response

    @app.post("/fixture-login")
    async def fixture_login(request: Request):
        if not secrets.compare_digest(request.headers.get("x-b016-harness-key", ""), key):
            raise HTTPException(404)
        # Fixed synthetic identity only; no caller-controlled account/role.
        return {"token": store.issue_after_verification(VerifiedIdentity("synthetic://b013", "synthetic-6"))}

    @app.get("/session")
    async def session(request: Request):
        authenticate(request)
        return {"authenticated": True, "synthetic": True}

    @app.get("/records/{record_id}")
    async def record(request: Request, record_id: str):
        require_record(request, record_id)
        return {"synthetic": True}

    @app.post("/privileged")
    async def privileged(request: Request):
        require_privileged(request)
        raise AssertionError("Privileged operation must never execute")

    @app.post("/logout")
    async def logout(request: Request):
        logout_request(request)
        return {"logged_out": True}

    config = uvicorn.Config(app, host="127.0.0.1", port=8100, access_log=False, log_level="critical")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    child = None
    STOP.unlink(missing_ok=True)
    with tempfile.TemporaryFile(mode="w+b") as logs:
        try:
            thread.start()
            deadline = time.monotonic() + 20
            while not server.started and time.monotonic() < deadline:
                time.sleep(.1)
            assert server.started, "Backend harness did not start"
            node = shutil.which("node")
            assert node, "Installed Node required"
            # Verify native package before Next can attempt compiler fallback.
            subprocess.run([node, "-e", "require('@next/swc-win32-x64-msvc')"],
                           cwd=ROOT / "frontend", check=True, capture_output=True)
            child = subprocess.Popen(
                [node, str(ROOT / "frontend/node_modules/next/dist/bin/next"),
                 "dev", "--webpack", "--hostname", "127.0.0.1", "--port", "3100"],
                cwd=ROOT / "frontend/harness", stdout=logs, stderr=logs,
                env=dict(os.environ, CPA_B016_HARNESS_KEY=key, NEXT_TELEMETRY_DISABLED="1",
                         npm_config_offline="true", npm_config_ignore_scripts="true"),
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            deadline = time.monotonic() + 90
            while time.monotonic() < deadline:
                if child.poll() is not None:
                    raise RuntimeError("Next harness exited before readiness")
                try:
                    if call(3100, "/")[0] == 200:
                        break
                except (OSError, TimeoutError):
                    time.sleep(.25)
            else:
                raise RuntimeError("Next harness did not become ready")

            def bff(action, token=None, method=None, origin="http://127.0.0.1:3100", extra=None):
                headers = {"Origin": origin}
                if token:
                    headers["Cookie"] = "cpa_b016_session=" + token
                headers.update(extra or {})
                return call(3100, "/api/session/" + action, method or (
                    "GET" if action in {"status", "own", "other"} else "POST"), headers)

            def login():
                status, headers, body = bff("login")
                assert status == 200, "Synthetic login failed"
                cookie = headers.get("set-cookie", headers.get("Set-Cookie", ""))
                lower = cookie.lower()
                assert "httponly" in lower and "samesite=strict" in lower and "path=/" in lower
                assert "domain=" not in lower and "max-age=28800" in lower
                token = cookie.split(";", 1)[0].split("=", 1)[1]
                issued_tokens.append(token)
                assert token not in body and key not in body
                return token

            assert bff("status")[0] == 401
            assert bff("login", origin="http://untrusted.invalid")[0] == 403
            assert bff("login", origin="")[0] == 403
            assert bff("login", method="GET")[0] == 405
            assert bff("status", extra={"Authorization": "Bearer spoof"})[0] == 400
            assert call(8100, "/fixture-login", "POST")[0] == 404
            outcomes.append("B016 missing auth, origin and method rejection; fixture issuance requires private harness key")
            token = login()
            assert bff("status", token, extra={"Cookie": f"cpa_b016_session={token}; cpa_b016_session={token}"})[0] == 401
            assert bff("status", "malformed")[0] == 401
            for action, status in [("status", 200), ("own", 200), ("other", 404), ("privileged", 403)]:
                result = bff(action, token)
                assert result[0] == status, action
                assert token not in result[2]
            assert bff("login", token)[0] == 409
            outcomes.append("B016 cookie login, own record, cross-client concealment and privileged denial")
            own = "/records/00000000-0000-0000-0000-00000000012d"
            other = "/records/00000000-0000-0000-0000-00000000012e"
            assert call(8100, own)[0] == 401
            assert call(8100, own, headers={"Authorization": "Bearer malformed"})[0] == 401
            assert call(8100, other, headers={"Authorization": "Bearer " + token,
                        "X-Role": "cpa", "X-Client-Id": "102"})[0] == 404
            outcomes.append("B016 direct API denial remains effective independently of UI and spoofed headers")
            assert bff("logout", token, origin="null")[0] == 403
            assert bff("status", token)[0] == 200
            status, headers, _ = bff("logout", token)
            assert status == 200 and "Max-Age=0" in headers.get("set-cookie", "")
            assert bff("status", token)[0] == 401
            outcomes.append("B016 logout revocation, cookie clearing and replay denial")
            for interval in ("31 minutes", "9 hours"):
                token = login()
                connection.execute("UPDATE cpa.sessions SET "
                                   f"issued_at=issued_at-interval '{interval}', "
                                   f"last_seen_at=last_seen_at-interval '{interval}', "
                                   f"expires_at=expires_at-interval '{interval}'"
                                   " WHERE user_id='00000000-0000-0000-0000-000000000006'")
                assert bff("own", token)[0] == 401
            token = login()
            connection.execute("UPDATE cpa.users SET membership_active=false WHERE id=%s",
                               ("00000000-0000-0000-0000-000000000006",))
            assert bff("status", token)[0] == 401
            connection.execute("UPDATE cpa.users SET membership_active=true WHERE id=%s",
                               ("00000000-0000-0000-0000-000000000006",))
            assert bff("status", token)[0] == 401
            outcomes.append("B016 idle/absolute expiry and membership revocation survive browser forwarding")
            token = login()
            available = False
            assert bff("status", token)[0] == 503
            status, headers, _ = bff("logout", token)
            assert status == 503 and "set-cookie" not in headers
            available = True
            assert bff("logout", token)[0] == 200
            outcomes.append("B016 unavailable validation fails closed; logout failure is not reported as success")
            normal = create_app()
            for path in ("/fixture-login", "/session", own):
                assert asyncio.run(asgi_request(normal, path, method="POST" if path == "/fixture-login" else "GET"))[0] == 404
            outcomes.append("B016 normal backend has no fixture issuance/session/record routes")
            print("B016 automated checks passed. Isolated browser UI: http://127.0.0.1:3100/", flush=True)
            if "--serve" in sys.argv:
                print("Create docs/evidence/B016-stop to finish; automatic cleanup after 20 minutes.", flush=True)
                deadline = time.monotonic() + 1200
                while not STOP.exists() and time.monotonic() < deadline:
                    if child.poll() is not None:
                        raise RuntimeError("Browser harness exited")
                    time.sleep(.5)
            logs.seek(0)
            captured = logs.read().decode(errors="replace")
            assert key not in captured and all(value not in captured for value in issued_tokens), "Credential in harness logs"
            outcomes.append("B016 captured frontend logs contain no harness key or issued test session tokens")
            return outcomes
        finally:
            if child is not None and child.poll() is None:
                subprocess.run(["taskkill", "/PID", str(child.pid), "/T", "/F"],
                               capture_output=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                child.wait(timeout=15)
            server.should_exit = True
            thread.join(timeout=10)
            STOP.unlink(missing_ok=True)
            if thread.is_alive():
                raise RuntimeError("Backend harness cleanup not confirmed")


if __name__ == "__main__":
    main("B016", run_checks)
