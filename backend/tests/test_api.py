"""Standard-library test runner: no pytest/httpx installation required."""

import asyncio
import http.client
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

from fastapi import HTTPException

from app.main import create_app


async def request(app, path, method="GET", body=b"", query=b"", headers=None, raw=False):
    messages = []
    delivered = False

    async def receive():
        nonlocal delivered
        if not delivered:
            delivered = True
            return {"type": "http.request", "body": body, "more_body": False}
        await asyncio.Event().wait()

    async def send(message):
        messages.append(message)

    try:
        await app(
            {
                "type": "http",
                "asgi": {"version": "3.0"},
                "http_version": "1.1",
                "method": method,
                "scheme": "http",
                "path": path,
                "raw_path": path.encode(),
                "query_string": query,
                "root_path": "",
                "headers": [(b"content-type", b"application/json"), *(headers or [])],
                "client": ("127.0.0.1", 12000),
                "server": ("127.0.0.1", 8000),
            },
            receive,
            send,
        )
    except Exception:
        # Starlette re-raises server exceptions after sending its handled 500.
        if not any(m.get("status") == 500 for m in messages):
            raise
    start = next(m for m in messages if m["type"] == "http.response.start")
    payload = b"".join(
        m.get("body", b"") for m in messages if m["type"] == "http.response.body"
    )
    return start["status"], dict(start["headers"]), payload.decode() if raw else json.loads(payload)


class ContractTests(unittest.TestCase):
    def test_root_explains_backend_only_and_does_not_echo_input(self):
        status, headers, page = asyncio.run(request(
            create_app(), "/", raw=True, query=b"SYNTHETIC_PRIVATE_CANARY"
        ))
        self.assertEqual(status, 200)
        self.assertIn(b"text/html", headers[b"content-type"])
        self.assertEqual(headers[b"cache-control"], b"no-store")
        self.assertIn("The backend is running", page)
        self.assertIn("frontend runs as a separate local service", page)
        self.assertIn('href="/health"', page)
        self.assertIn('href="/openapi.json"', page)
        self.assertNotIn("SYNTHETIC_PRIVATE_CANARY", page)

    def setUp(self):
        self.app = create_app()

    def call(self, path, **kwargs):
        return asyncio.run(request(self.app, path, **kwargs))

    def test_liveness_does_not_expose_environment_or_query(self):
        canary = "SYNTHETIC_SECRET_DO_NOT_DISCLOSE"
        with patch.dict(os.environ, {"OPENAI_API_KEY": canary, "DATABASE_URL": canary}):
            status, headers, payload = self.call("/health", query=canary.encode())
        self.assertEqual((status, payload), (200, {"status": "ok"}))
        self.assertEqual(headers[b"cache-control"], b"no-store")

    def test_missing_route_does_not_echo_path(self):
        status, _, payload = self.call("/SYNTHETIC_PRIVATE_IDENTIFIER")
        self.assertEqual(status, 404)
        self.assertEqual(payload["error"]["code"], "not_found")
        self.assertNotIn("SYNTHETIC", json.dumps(payload))

    def test_wrong_method_is_structured_and_preserves_allow(self):
        status, headers, payload = self.call("/health", method="POST")
        self.assertEqual(status, 405)
        self.assertEqual(payload["error"]["code"], "method_not_allowed")
        self.assertIn(b"GET", headers[b"allow"])

    def test_validation_does_not_echo_invalid_value(self):
        @self.app.get("/test-only/number")
        async def number(value: int):
            return {"value": value}

        status, _, payload = self.call(
            "/test-only/number", query=b"value=SYNTHETIC_PRIVATE_VALUE"
        )
        self.assertEqual(status, 422)
        self.assertEqual(
            payload, {"error": {"code": "validation_error", "message": "Invalid request."}}
        )

    def test_http_exception_does_not_echo_detail_or_private_header(self):
        @self.app.get("/test-only/denied")
        async def denied():
            raise HTTPException(
                403, detail="SYNTHETIC_SECRET", headers={"X-Private": "SYNTHETIC_SECRET"}
            )

        status, headers, payload = self.call("/test-only/denied")
        self.assertEqual(status, 403)
        self.assertNotIn(b"x-private", headers)
        self.assertEqual(payload["error"]["message"], "Access denied.")

    def test_unhandled_exception_is_generic(self):
        @self.app.get("/test-only/crash")
        async def crash():
            raise RuntimeError("SYNTHETIC_SECRET_IN_EXCEPTION")

        status, _, payload = self.call("/test-only/crash")
        self.assertEqual(status, 500)
        self.assertEqual(
            payload,
            {"error": {"code": "internal_error", "message": "Internal server error."}},
        )

    def test_openapi_matches_health_contract_and_excludes_test_routes(self):
        status, _, schema = self.call("/openapi.json")
        self.assertEqual(status, 200)
        self.assertEqual(set(schema["paths"]), {"/health"})
        operation = schema["paths"]["/health"]["get"]
        self.assertEqual(
            operation["responses"]["200"]["content"]["application/json"]["schema"]["$ref"],
            "#/components/schemas/HealthResponse",
        )
        for code in ("404", "405", "422", "500"):
            self.assertEqual(
                operation["responses"][code]["content"]["application/json"]["schema"]["$ref"],
                "#/components/schemas/ErrorResponse",
            )
        self.assertFalse(self.app.debug)
        self.assertIsNone(self.app.docs_url)
        self.assertIsNone(self.app.redoc_url)

    def test_browser_docs_disabled(self):
        for path in ("/docs", "/redoc"):
            with self.subTest(path=path):
                self.assertEqual(self.call(path)[0], 404)


class StartupTests(unittest.TestCase):
    def test_real_loopback_startup_and_shutdown(self):
        backend = Path(__file__).resolve().parents[1]
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        # Child process has no visible console and is always stopped.
        with tempfile.TemporaryFile(mode="w+b") as log:
            process = subprocess.Popen(
                [sys.executable, str(backend / "run_local.py"), "--port", str(port)],
                cwd=backend,
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=log,
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            try:
                deadline = time.monotonic() + 15
                result = None
                while time.monotonic() < deadline and process.poll() is None:
                    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=1)
                    try:
                        connection.request("GET", "/health?SYNTHETIC_SECRET")
                        response = connection.getresponse()
                        result = (response.status, json.loads(response.read()))
                        self.assertIsNone(response.getheader("server"))
                        break
                    except (OSError, http.client.HTTPException):
                        time.sleep(0.1)
                    finally:
                        connection.close()
                self.assertEqual(result, (200, {"status": "ok"}), "Local startup failed.")
            finally:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
            log.seek(0)
            self.assertNotIn(b"SYNTHETIC_SECRET", log.read())


if __name__ == "__main__":
    unittest.main()
