from datetime import datetime, timedelta, timezone
import unittest
from fastapi import HTTPException
from starlette.requests import Request

from app.sessions import bearer_token, within_lifetime, digest_token, authenticate


class SessionContractTests(unittest.TestCase):
    def test_idle_boundary_is_exclusive(self):
        start = datetime(2026, 10, 20, tzinfo=timezone.utc)
        expires = start + timedelta(hours=8)
        self.assertTrue(within_lifetime(start + timedelta(minutes=30, microseconds=-1), start, start, expires))
        self.assertFalse(within_lifetime(start + timedelta(minutes=30), start, start, expires))

    def test_absolute_boundary_cannot_be_extended_by_activity(self):
        start = datetime(2026, 10, 20, tzinfo=timezone.utc)
        expires = start + timedelta(hours=8)
        seen = expires - timedelta(seconds=1)
        self.assertTrue(within_lifetime(expires - timedelta(microseconds=1), start, seen, expires))
        self.assertFalse(within_lifetime(expires, start, seen, expires))
        self.assertFalse(within_lifetime(expires, start, seen, expires + timedelta(hours=1)))

    def test_future_or_invalid_timestamps_deny(self):
        start = datetime(2026, 10, 20, tzinfo=timezone.utc)
        self.assertFalse(within_lifetime(start, start, start + timedelta(seconds=1), start + timedelta(hours=8)))
        self.assertFalse(within_lifetime(start, start, start - timedelta(seconds=1), start + timedelta(hours=8)))

    def test_credential_parser_rejects_ambiguity_without_echo(self):
        token = "A" * 43
        for values in ([], ["Bearer"], ["Basic " + token], ["Bearer  " + token],
                       ["Bearer " + token + " "], ["Bearer " + token, "Bearer " + token],
                       ["Bearer private-canary"], ["Bearer " + "A" * 44]):
            request = Request({"type": "http", "headers": [(b"authorization", v.encode()) for v in values]})
            with self.assertRaises(HTTPException) as error:
                bearer_token(request)
            self.assertEqual(error.exception.status_code, 401)
            self.assertNotIn("private-canary", str(error.exception))
        request = Request({"type": "http", "headers": [(b"authorization", ("bEaReR " + token).encode())]})
        self.assertEqual(bearer_token(request), token)
        self.assertEqual(len(digest_token(token)), 64)
        self.assertNotEqual(digest_token(token), token)

    def test_unconfigured_store_fails_closed(self):
        request = Request({"type": "http", "headers": [(b"authorization", b"Bearer " + b"A" * 43)]})
        with self.assertRaises(HTTPException) as error:
            authenticate(request)
        self.assertEqual(error.exception.status_code, 503)
