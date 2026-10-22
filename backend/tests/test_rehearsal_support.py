"""B027 alternate-port and redacted support-log boundaries."""
import asyncio
import json
import unittest

from app.local_rehearsal import create_rehearsal
from tests.test_api import request


class RehearsalSupportTests(unittest.TestCase):
    def test_explicit_loopback_origin_and_redacted_denial(self):
        events = []
        app = create_rehearsal(None, 0, origin='https://127.0.0.1:3543', frontend_port=3300, log_sink=events.append)
        headers = [(b'host', b'127.0.0.1:3543'), (b'authorization', b'Bearer synthetic-secret-canary')]
        status, _, _ = asyncio.run(request(app, '/api/dashboard', query=b'private=synthetic-secret-canary', headers=headers))
        self.assertEqual(status, 400)
        self.assertEqual(len(events), 1)
        self.assertEqual(set(events[0]), {'request_id','route','method','status','duration_ms'})
        self.assertEqual(events[0]['status'], 400)
        self.assertNotIn('synthetic-secret-canary', json.dumps(events))

    def test_non_loopback_and_invalid_ports_rejected(self):
        for origin in ('http://127.0.0.1:3543', 'https://example.com:3543', 'https://127.0.0.1:99999'):
            with self.assertRaises(ValueError):
                create_rehearsal(None, 0, origin=origin)
        with self.assertRaises(ValueError):
            create_rehearsal(None, 0, frontend_port=80)


if __name__ == '__main__':
    unittest.main()
