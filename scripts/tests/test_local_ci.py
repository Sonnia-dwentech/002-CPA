import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("check_local_ci", Path(__file__).resolve().parents[1] / "check_local_ci.py")
ci = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ci)


class LocalCheckTests(unittest.TestCase):
    def test_synthetic_tokens_are_detected_without_returning_values(self):
        examples = ["ghp_" + "a" * 36, "sk-" + "x" * 40, "AKIA" + "A" * 16,
                    "-----BEGIN " + "PRIVATE KEY-----"]
        for example in examples:
            result = ci.findings("safe\n" + example)
            self.assertTrue(result)
            self.assertEqual(result[0][0], 2)
            self.assertNotIn(example, repr(result))

    def test_placeholder_is_not_a_secret(self):
        self.assertEqual(ci.findings("OPENAI_API_KEY=\nLIVE_AI_ENABLED=false"), [])

    def test_failed_child_stops_remaining_checks_and_hides_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), patch.object(ci.subprocess, "run") as run:
            run.return_value.returncode = 7
            run.return_value.stdout = b"synthetic-private-canary"
            self.assertEqual(ci.run_steps([("first", ["unused"], Path.cwd()),
                                          ("second", ["unused"], Path.cwd())]), 1)
            self.assertEqual(run.call_count, 1)
        self.assertNotIn("synthetic-private-canary", output.getvalue())

    def test_actual_child_failure_propagates(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ci.run_steps([("failure", [sys.executable, "-c", "raise SystemExit(7)"], Path.cwd())]), 1)

    def test_actual_child_success_passes(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(ci.run_steps([("success", [sys.executable, "-c", "pass"], Path.cwd())]), 0)
