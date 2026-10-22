"""B022 isolated synthetic dashboard UI/API/PostgreSQL verification.

Retains the new test container per user instruction. --serve holds loopback
servers for inspection, until docs/evidence/B022-stop exists (no auto timeout).
"""
import asyncio
from dataclasses import asdict
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
from uuid import UUID

from fastapi import HTTPException, Request
import uvicorn
from app.main import create_app
from app.access import VerifiedIdentity
from app.dashboard import DashboardStore
from app.sessions import SessionStore, authenticate, logout_request
from check_local_database import main
from check_local_browser import call

ROOT = Path(__file__).resolve().parent.parent
STOP = ROOT / "docs/evidence/B022-stop"


def run_checks(connection):
    for port in (8100, 3100):
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", port))
    if STOP.exists():
        raise RuntimeError("Existing B022 stop marker; inspect it before relaunch")
    key = secrets.token_urlsafe(32)
    identity = VerifiedIdentity("synthetic://b022", "owner")
    with connection.transaction():
        for number, subject in ((1, "owner"), (2, "shared-owner"), (3, "hidden-owner")):
            connection.execute("INSERT INTO cpa.users VALUES (%s,'synthetic://b022',%s,'internal',NULL,true,true)", (UUID(int=number), subject))
            connection.execute("INSERT INTO cpa.user_roles VALUES (%s,'internal','cpa')", (UUID(int=number),))
        for number, owner, kind, state in ((11, 1, "idea", "draft"), (12, 2, "idea", "draft"), (13, 1, "dossier", "archived"), (14, 3, "idea", "draft")):
            connection.execute("INSERT INTO cpa.access_records VALUES (%s,%s,%s,NULL,NULL,NULL,%s)", (UUID(int=number), kind, UUID(int=owner), state))
        for permission in ("read", "edit"):
            connection.execute("INSERT INTO cpa.record_grants VALUES (%s,%s,%s)", (UUID(int=12), UUID(int=1), permission))
    store = SessionStore(connection)
    dashboard = DashboardStore(connection, {"idea", "dossier"})
    app = create_app()
    lock = asyncio.Lock()

    @app.middleware("http")
    async def stores(request, next_handler):
        async with lock:
            request.state.session_store = store
            response = await next_handler(request)
            response.headers["Cache-Control"] = "no-store"
            return response

    @app.post("/fixture-login")
    async def fixture_login(request: Request):
        if not secrets.compare_digest(request.headers.get("x-b016-harness-key", ""), key):
            raise HTTPException(404)
        return {"token": store.issue_after_verification(identity)}

    @app.get("/session")
    async def session(request: Request):
        authenticate(request)
        return {"authenticated": True, "synthetic": True}

    @app.post("/logout")
    async def logout(request: Request):
        logout_request(request)
        return {"logged_out": True}

    @app.get("/dashboard")
    async def query(request: Request):
        principal = authenticate(request)
        if any(len(request.query_params.getlist(k)) != 1 for k in request.query_params):
            raise HTTPException(422)
        return asdict(dashboard.query(principal.identity, dict(request.query_params)))

    server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=8100, access_log=False, log_level="critical"))
    thread = threading.Thread(target=server.run, daemon=True)
    child = None
    outcomes = []
    with tempfile.TemporaryFile(mode="w+b") as logs:
        try:
            thread.start()
            deadline = time.monotonic() + 20
            while not server.started and time.monotonic() < deadline:
                time.sleep(.1)
            assert server.started
            node = shutil.which("node")
            assert node
            subprocess.run([node, "-e", "require('@next/swc-win32-x64-msvc')"], cwd=ROOT / "frontend", check=True, capture_output=True)
            child = subprocess.Popen([node, str(ROOT / "frontend/node_modules/next/dist/bin/next"), "dev", "--webpack", "--hostname", "127.0.0.1", "--port", "3100"],
                cwd=ROOT / "frontend/harness", stdout=logs, stderr=logs,
                env=dict(os.environ, CPA_B016_HARNESS_KEY=key, CPA_B022_HARNESS="1", NEXT_TELEMETRY_DISABLED="1", npm_config_offline="true", npm_config_ignore_scripts="true"),
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            deadline = time.monotonic() + 90
            while time.monotonic() < deadline:
                if child.poll() is not None:
                    raise RuntimeError("Next harness exited")
                try:
                    if call(3100, "/dashboard")[0] == 200:
                        break
                except (OSError, TimeoutError):
                    time.sleep(.25)
            else:
                raise RuntimeError("Next harness not ready")

            assert call(3100, "/api/dashboard")[0] == 401
            assert call(8100, "/dashboard")[0] == 401
            assert call(8100, "/fixture-login", "POST")[0] == 404
            status, headers, body = call(3100, "/api/session/login", "POST", {"Origin": "http://127.0.0.1:3100"})
            assert status == 200
            cookie = headers["set-cookie"].split(";", 1)[0]
            token = cookie.split("=", 1)[1]
            assert token not in body and key not in body

            def get(query="", extra=None):
                return call(3100, "/api/dashboard" + query, headers={"Cookie": cookie, **(extra or {})})

            status, headers, body = get()
            data = json.loads(body)
            assert status == 200 and data["total"] == 3 and len(data["records"]) == 3
            assert "no-store" in headers.get("cache-control", "")
            assert str(UUID(int=14)) not in body and str(UUID(int=3)) not in body
            assert token not in body and key not in body
            outcomes.append("UI proxy counts/list match persisted owner/shared references; hidden record and credentials excluded")
            assert json.loads(get("?kind=idea&state=draft&owner_id=" + str(UUID(int=2)))[2])["total"] == 1
            assert json.loads(get("?state=submitted")[2])["status"] == "empty"
            unavailable = json.loads(get("?kind=research")[2])
            assert unavailable["status"] == "unavailable" and unavailable["total"] is None
            for query in ("?kind=idea&kind=dossier", "?date=bad", "?owner_id=bad"):
                assert get(query)[0] == 422
            assert get(extra={"Authorization": "Bearer spoof"})[0] == 400
            assert get(extra={"Sec-Fetch-Site": "cross-site"})[0] == 403
            assert get(extra={"Cookie": cookie + "; " + cookie})[0] == 401
            outcomes.append("AND filters, empty/unavailable distinctions, duplicate filters/cookies and spoofed requests checked")
            connection.execute("ALTER TABLE cpa.access_records RENAME TO synthetic_hidden_records")
            try:
                status, _, body = get()
                assert status == 503 and "total" not in body and "synthetic_hidden" not in body
            finally:
                connection.execute("ALTER TABLE cpa.synthetic_hidden_records RENAME TO access_records")
            assert json.loads(get()[2])["total"] == 3
            outcomes.append("actual database query failure returns safe error without counts; recovery succeeds")
            connection.execute("DELETE FROM cpa.record_grants WHERE user_id=%s", (UUID(int=1),))
            assert json.loads(get()[2])["total"] == 2
            connection.execute("INSERT INTO cpa.record_grants VALUES (%s,%s,'read')", (UUID(int=12), UUID(int=1)))
            assert call(3100, "/api/session/logout", "POST", {"Origin": "http://127.0.0.1:3100", "Cookie": cookie})[0] == 200
            assert get()[0] == 401
            outcomes.append("grant revocation and logout replay denial through frontend proxy")
            from tests.test_api import request as asgi_request
            for path in ("/dashboard", "/fixture-login"):
                assert asyncio.run(asgi_request(create_app(), path, method="POST" if path == "/fixture-login" else "GET"))[0] == 404
            outcomes.append("normal API still has no synthetic dashboard or issuance route")
            logs.seek(0)
            captured = logs.read().decode(errors="replace")
            assert key not in captured and token not in captured
            outcomes.append("captured frontend logs exclude harness key and issued token")
            print(json.dumps({"B022_checks_passed": outcomes}), flush=True)
            print("B022 ready: http://127.0.0.1:3100/dashboard ; database retained", flush=True)
            if "--serve" in sys.argv:
                print("Servers stay open until docs/evidence/B022-stop is created. Database container will remain running.", flush=True)
                while not STOP.exists():
                    if child.poll() is not None:
                        raise RuntimeError("Next harness exited")
                    time.sleep(.5)
            return outcomes
        finally:
            # Stop only the processes this harness launched; never the retained database.
            if child is not None and child.poll() is None:
                subprocess.run(["taskkill", "/PID", str(child.pid), "/T", "/F"], capture_output=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
                child.wait(timeout=15)
            server.should_exit = True
            thread.join(timeout=10)


if __name__ == "__main__":
    main("B022", run_checks, retain=True)
