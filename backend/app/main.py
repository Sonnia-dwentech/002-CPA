"""Minimal local API: no database, credentials, provider calls or client data."""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException


class HealthResponse(BaseModel):
    status: str


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    error: ErrorDetail


def error_response(status: int, code: str, message: str) -> JSONResponse:
    return JSONResponse(
        status_code=status,
        content={"error": {"code": code, "message": message}},
        headers={"Cache-Control": "no-store"},
    )


def create_app() -> FastAPI:
    application = FastAPI(
        title="CPA Local Foundation API",
        version="0.1.0",
        description=(
            "Local liveness only. Database, authentication, providers and "
            "deployment readiness are not implemented."
        ),
        debug=False,
        docs_url=None,
        redoc_url=None,
        openapi_url="/openapi.json",
        responses={
            404: {"model": ErrorResponse, "description": "Resource not found"},
            405: {"model": ErrorResponse, "description": "Method not allowed"},
            422: {"model": ErrorResponse, "description": "Invalid request"},
            500: {"model": ErrorResponse, "description": "Internal server error"},
        },
    )

    @application.exception_handler(HTTPException)
    async def http_error(_request: Request, exc: HTTPException) -> JSONResponse:
        known = {
            400: ("bad_request", "Invalid request."),
            401: ("unauthorized", "Authentication required."),
            403: ("forbidden", "Access denied."),
            404: ("not_found", "Resource not found."),
            405: ("method_not_allowed", "Method not allowed."),
            422: ("validation_error", "Invalid request."),
            429: ("too_many_requests", "Too many requests."),
            503: ("service_unavailable", "Service unavailable."),
        }
        code, message = known.get(
            exc.status_code, ("http_error", "Request could not be completed.")
        )
        response = error_response(exc.status_code, code, message)
        if exc.status_code == 401:
            response.headers["WWW-Authenticate"] = "Bearer"
        # Preserve protocol-required routing information, not arbitrary headers
        # or exception details that could contain private data.
        if exc.status_code == 405 and exc.headers:
            allowed = exc.headers.get("Allow")
            if allowed:
                response.headers["Allow"] = allowed
        return response

    @application.exception_handler(RequestValidationError)
    async def invalid_request(
        _request: Request, _exc: RequestValidationError
    ) -> JSONResponse:
        # Framework validation details can echo submitted values.
        return error_response(422, "validation_error", "Invalid request.")

    @application.exception_handler(Exception)
    async def unexpected_error(_request: Request, _exc: Exception) -> JSONResponse:
        return error_response(500, "internal_error", "Internal server error.")

    @application.get(
        "/health",
        response_model=HealthResponse,
        summary="Process liveness",
        description=(
            "Confirms the API process can answer. Does not check database, "
            "identity, providers or overall application readiness."
        ),
    )
    async def health() -> JSONResponse:
        return JSONResponse(
            content={"status": "ok"}, headers={"Cache-Control": "no-store"}
        )

    @application.get("/", response_class=HTMLResponse, include_in_schema=False)
    async def local_status() -> HTMLResponse:
        return HTMLResponse(
            """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CPA — Local backend</title>
<style>
body{font-family:system-ui,sans-serif;line-height:1.6;margin:0;background:#f4f6f8;color:#182331}
main{max-width:40rem;margin:10vh auto;padding:2rem;background:white;border:1px solid #d9e0e7;border-radius:12px}
h1{font-size:1.8rem;line-height:1.2}a{color:#1558a0}li{margin:.6rem 0}
.status{color:#14633b;font-weight:600}
@media(max-width:44rem){main{margin:1rem;padding:1.5rem}}
</style>
</head>
<body><main>
<p>CPA · Local development</p>
<h1>The backend is running</h1>
<p class="status">This server can respond to requests.</p>
<p>The CPA frontend runs as a separate local service. This page reports backend
process liveness; use the frontend for navigation and the synthetic dashboard.</p>
<ul>
<li><a href="/health">Check backend health</a></li>
<li><a href="/openapi.json">View the API schema</a></li>
</ul>
<p>Database connectivity, live sign-in and external services are not checked by this page.</p>
</main></body></html>""",
            headers={
                "Cache-Control": "no-store",
                "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'",
            },
        )

    return application


app = create_app()
