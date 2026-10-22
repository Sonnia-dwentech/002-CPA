"""Explicit local B024 composition. Never imported by the normal API entrypoint."""
import asyncio
from dataclasses import asdict
import http.client
import re
from uuid import UUID

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse, Response
import psycopg
from app.main import create_app
from app.access import AccessStore, VerifiedIdentity
from app.dashboard import DashboardStore
from app.sessions import SessionStore
from app.audit import OperationalCapture

ORIGIN = "https://127.0.0.1:3443"
COOKIE = "cpa_b024_session"


def create_rehearsal(connection, migration_count, *, origin=ORIGIN, frontend_port=3200, log_sink=None):
    if not re.fullmatch(r"https://127\.0\.0\.1:[0-9]{1,5}", origin):
        raise ValueError("Explicit loopback HTTPS origin required")
    if not 1024 <= int(origin.rsplit(':', 1)[1]) <= 65535 or not 1024 <= frontend_port <= 65535:
        raise ValueError("Invalid loopback port")
    app = create_app()
    sessions = SessionStore(connection)
    dashboard = DashboardStore(connection, {"idea", "dossier"})
    access = AccessStore(connection, {"idea", "dossier"})
    lock = asyncio.Lock()

    @app.middleware("http")
    async def local_boundary(request, next_handler):
        if (request.client.host not in {"127.0.0.1", "::1"}
                or request.headers.get("host") != origin.removeprefix("https://")
                or request.headers.get("sec-fetch-site") == "cross-site"
                or request.headers.get("origin") not in (None, origin)):
            return JSONResponse({"status": 403}, status_code=403)
        if request.method not in {"GET", "HEAD"} and request.headers.get("origin") != origin:
            return JSONResponse({"status": 403}, status_code=403)
        if request.headers.get("authorization"):
            return JSONResponse({"status": 400}, status_code=400)
        try:
            if request.url.path.startswith("/api/") or request.url.path == "/ready":
                async with lock:
                    response = await next_handler(request)
                response.headers["Cache-Control"] = "no-store"
            else:
                response = await next_handler(request)
        except psycopg.Error:
            response = JSONResponse({"status": 503}, status_code=503, headers={"Cache-Control":"no-store"})
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-Frame-Options"] = "DENY"
        return response

    def token(request):
        raw = request.headers.get("cookie", "").split(";")
        matching = [c for c in raw if c.strip().split("=", 1)[0] == COOKIE]
        if len(matching) != 1:
            raise HTTPException(401)
        return request.cookies.get(COOKIE)

    def actor(request):
        return sessions.validate(token(request)).identity

    @app.get("/ready")
    async def ready():
        try:
            if connection.execute("SELECT current_database(),current_user").fetchone() != ("cpa_b024", "cpa_runtime"):
                raise HTTPException(503)
            if connection.execute("SELECT count(*) FROM cpa_meta.schema_migrations").fetchone()[0] != migration_count:
                raise HTTPException(503)
            connection.execute("SELECT id FROM cpa.access_records LIMIT 0")
            connection.execute("SELECT token_digest FROM cpa.sessions LIMIT 0")
        except psycopg.Error:
            raise HTTPException(503) from None
        return {"status":"ready", "scope":"local_synthetic_rehearsal"}

    @app.post("/api/session/login")
    async def login(request: Request):
        if request.cookies.get(COOKIE):
            raise HTTPException(409)
        # Fixed synthetic identity only; no caller-selected identity or grants.
        issued = sessions.issue_after_verification(VerifiedIdentity("synthetic://b024", "owner"))
        response = JSONResponse({"synthetic":True})
        response.set_cookie(COOKIE, issued, secure=True, httponly=True, samesite="strict", max_age=28800, path="/")
        return response

    @app.post("/api/session/logout")
    async def logout(request: Request):
        sessions.logout(token(request))
        response = JSONResponse({"logged_out":True})
        response.delete_cookie(COOKIE, secure=True, httponly=True, samesite="strict", path="/")
        return response

    @app.get("/api/session/status")
    async def status(request: Request):
        actor(request)
        return {"authenticated":True,"synthetic":True}

    @app.get("/api/dashboard")
    async def query(request: Request):
        identity = actor(request)
        if any(len(request.query_params.getlist(k)) != 1 for k in request.query_params):
            raise HTTPException(422)
        return asdict(dashboard.query(identity, dict(request.query_params)))

    @app.get("/api/records/{record_id}")
    async def record(record_id: UUID, request: Request):
        row = access.require(actor(request), record_id)
        return {key: row[key] for key in ("id", "kind", "state", "owner_id")}

    # Replace only the minimal status homepage in this explicitly selected app.
    app.router.routes = [r for r in app.router.routes if getattr(r, "path", None) != "/"]

    @app.get("/{path:path}")
    async def frontend(path: str, request: Request):
        if path.startswith("api/"):
            raise HTTPException(404)
        def forward():
            upstream = http.client.HTTPConnection("127.0.0.1", frontend_port, timeout=15)
            try:
                target = "/" + path + ("?" + request.url.query if request.url.query else "")
                upstream.request("GET", target)
                result = upstream.getresponse()
                return Response(result.read(), status_code=result.status, headers={
                    "Content-Type": result.getheader("Content-Type", "application/octet-stream"),
                    "Cache-Control":"no-store",
                })
            finally:
                upstream.close()
        try:
            return await asyncio.to_thread(forward)
        except (OSError, http.client.HTTPException):
            raise HTTPException(503) from None
    if log_sink is not None:
        return OperationalCapture(app, log_sink, {"ready", "login", "logout", "status", "query", "record", "frontend", "health"})
    return app
