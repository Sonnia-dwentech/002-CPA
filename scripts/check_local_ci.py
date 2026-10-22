"""B020 offline checks. This local runner does not enforce GitHub merges."""
import argparse
import ast
import importlib.metadata
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"node_modules", ".next", ".venv", ".venv312", "__pycache__", ".git"}
EXTENSIONS = {".py", ".ts", ".tsx", ".js", ".mjs", ".json", ".sql", ".toml", ".yaml", ".yml"}
PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b"),
    "provider_key": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{32,}\b"),
    "aws_access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
}


def sources(root):
    """Active source/config only; never traverse environments or source archives."""
    for folder in ("backend", "frontend", "scripts"):
        pending = [root / folder]
        while pending:
            current = pending.pop()
            if not current.exists():
                raise ValueError("missing source directory")
            for path in sorted(current.iterdir()):
                if path.is_symlink():
                    raise ValueError("symlink in scan scope")
                if path.is_dir() and path.name not in EXCLUDED:
                    pending.append(path)
                elif path.is_file() and path.suffix in EXTENSIONS:
                    yield path
    yield root / ".env.example"


def findings(text):
    return [(text.count("\n", 0, match.start()) + 1, kind)
            for kind, pattern in PATTERNS.items() for match in pattern.finditer(text)]


def inspect_sources(root):
    errors = []
    count = 0
    for path in sources(root):
        count += 1
        text = path.read_text(encoding="utf-8-sig")
        name = path.relative_to(root).as_posix()
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=name)
            except SyntaxError as error:
                errors.append(f"{name}:{error.lineno}: python_syntax")
        if path.suffix == ".json":
            try:
                json.loads(text)
            except ValueError:
                errors.append(f"{name}: invalid_json")
        errors.extend(f"{name}:{line}: {kind}" for line, kind in findings(text))
    return count, errors


def normalise(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def dependency_errors(root):
    errors = []
    for filename in ("requirements-local.txt", "requirements-installed-py312.txt"):
        for line in (root / "backend" / filename).read_text(encoding="utf-8-sig").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            match = re.fullmatch(r"([A-Za-z0-9_.-]+)==([A-Za-z0-9.+-]+)", line)
            if not match:
                errors.append("invalid_python_pin")
                continue
            name, expected = match.groups()
            try:
                actual = importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError:
                actual = None
            if actual != expected:
                errors.append("python_dependency_mismatch:" + normalise(name))
    package = json.loads((root / "frontend/package.json").read_text())
    lock = json.loads((root / "frontend/package-lock.json").read_text())
    for group in ("dependencies", "devDependencies"):
        if package.get(group, {}) != lock["packages"][""].get(group, {}):
            errors.append("frontend_lock_mismatch:" + group)
        for name in package.get(group, {}):
            installed = root / "frontend/node_modules" / name / "package.json"
            if not installed.exists() or json.loads(installed.read_text())["version"] != lock["packages"]["node_modules/" + name]["version"]:
                errors.append("frontend_dependency_mismatch:" + name)
    return errors


def run_steps(steps):
    for name, command, cwd in steps:
        # Never echo child output: tests or tools could include private payloads.
        result = subprocess.run(command, cwd=cwd, capture_output=True, timeout=180)
        print(f"{name}: {'PASS' if result.returncode == 0 else 'FAIL'}", flush=True)
        if result.returncode:
            return 1
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test-failure", action="store_true",
                        help="Run an isolated child that exits nonzero to verify failure propagation.")
    args = parser.parse_args()
    if args.self_test_failure:
        return run_steps([("controlled_failure", [sys.executable, "-c", "raise SystemExit(7)"], ROOT)])
    try:
        count, errors = inspect_sources(ROOT)
        errors.extend(dependency_errors(ROOT))
        for error in errors:
            print(error)
        if errors:
            return 1
        print(f"source/config checks: PASS ({count} files); installed dependency pins: PASS", flush=True)
        node = shutil.which("node")
        if node is None:
            print("node_runtime: MISSING")
            return 1
        tsc = str(ROOT / "frontend/node_modules/typescript/bin/tsc")
        return run_steps([
            ("python_dependencies", [sys.executable, "-m", "pip", "check"], ROOT),
            ("backend_tests", [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"], ROOT / "backend"),
            ("runner_tests", [sys.executable, "-B", "-m", "unittest", "discover", "-s", "scripts/tests"], ROOT),
            ("dashboard_contract", [node, str(ROOT / "scripts/test_dashboard_contract.mjs")], ROOT),
            ("frontend_types", [node, tsc, "--noEmit", "--incremental", "false", "-p", "tsconfig.json"], ROOT / "frontend"),
            ("harness_types", [node, tsc, "--noEmit", "--incremental", "false", "-p", "tsconfig.json"], ROOT / "frontend/harness"),
            ("rehearsal_types", [node, tsc, "--noEmit", "--incremental", "false", "-p", "tsconfig.json"], ROOT / "frontend/rehearsal"),
        ])
    except (OSError, ValueError, KeyError, subprocess.TimeoutExpired):
        print("check_infrastructure: FAIL (details withheld)")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
