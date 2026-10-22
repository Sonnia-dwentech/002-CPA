"""Run actual PostgreSQL checks in a new isolated offline Docker container.

No existing container/database is selected. No image pull, volume or .env use.
"""
import json
import os
from pathlib import Path
import secrets
import shutil
import subprocess
import tempfile
import time
import uuid

import psycopg
from app.database import apply_migrations, connect_local

ROOT = Path(__file__).resolve().parent
DOCKER = ["docker", "--host", "npipe:////./pipe/dockerDesktopLinuxEngine"]


def docker(*args, env=None):
    result = subprocess.run(
        [*DOCKER, *args], env=env, capture_output=True, text=True,
        timeout=60, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    if result.returncode:
        # Do not disclose Docker output, environment or credentials.
        raise RuntimeError("Local Docker command failed: " + args[0])
    return result.stdout.strip()


def main(task="B012", extra_checks=None, *, retain=True):
    if task not in {"B012", "B013", "B014", "B016", "B017", "B021", "B022"}:
        raise ValueError("Unsupported disposable check task")
    name = "cpa-" + task.lower() + "-check-" + uuid.uuid4().hex
    password = secrets.token_urlsafe(32)
    env = dict(os.environ, POSTGRES_PASSWORD=password)
    results = []
    created = False
    try:
        image_id = docker("image", "inspect", "postgres:17", "--format", "{{.Id}}")
        # Use the inspected immutable local image ID and prohibit any pull.
        docker("run", "--pull=never", "--detach", "--name", name,
               "--label", "cpa.task=" + task + "-disposable-check",
               "--publish", "127.0.0.1::5432",
               "--tmpfs", "/var/lib/postgresql/data:rw",
               "-e", "POSTGRES_PASSWORD", "-e", "POSTGRES_USER=cpa_b012",
               "-e", "POSTGRES_DB=cpa_b012", image_id, env=env)
        created = True
        print("Isolated synthetic container: " + name, flush=True)
        endpoint = docker("port", name, "5432/tcp")
        if not endpoint.startswith("127.0.0.1:") or "\n" in endpoint:
            raise RuntimeError("Unexpected database binding")
        port = int(endpoint.rsplit(":", 1)[1])
        deadline = time.monotonic() + 40
        connection = None
        while time.monotonic() < deadline:
            try:
                connection = connect_local(port=port, password=password)
                break
            except psycopg.OperationalError:
                time.sleep(0.5)
        if connection is None:
            raise RuntimeError("Local PostgreSQL did not become ready")
        with connection:
            version = connection.execute("SHOW server_version").fetchone()[0]
            results.append("loopback connectivity")
            migrations = ROOT / "migrations"
            baseline = sorted(p.name for p in migrations.glob("*.sql"))
            assert apply_migrations(connection, migrations) == baseline
            assert connection.execute("SELECT to_regnamespace('cpa')").fetchone()[0] == "cpa"
            results.append("initial migration apply")
            assert apply_migrations(connection, migrations) == []
            results.append("reapply is a no-op")
            with tempfile.TemporaryDirectory(prefix="cpa-b012-") as temporary:
                test_dir = Path(temporary)
                for p in migrations.glob("*.sql"):
                    shutil.copyfile(p, test_dir / p.name)
                first = test_dir / "0001_application_namespace.sql"
                first.write_text(first.read_text() + "\n-- changed\n")
                try:
                    apply_migrations(connection, test_dir)
                except ValueError:
                    pass
                else:
                    raise AssertionError("Changed history accepted")
                shutil.copyfile(migrations / first.name, first)
                results.append("changed migration rejected")
                first.rename(test_dir / "0000_renamed.sql")
                try:
                    apply_migrations(connection, test_dir)
                except ValueError:
                    pass
                else:
                    raise AssertionError("Missing history accepted")
                (test_dir / "0000_renamed.sql").rename(first)
                results.append("missing history rejected")
                probe = test_dir / "9000_synthetic_probe.sql"
                valid = (
                    "CREATE TABLE cpa.recovery_probe "
                    "(id integer PRIMARY KEY, value integer NOT NULL CHECK(value > 0));"
                    "INSERT INTO cpa.recovery_probe VALUES (1, 7);"
                )
                probe.write_text(valid + "INSERT INTO cpa.recovery_probe VALUES (2, -1);")
                try:
                    apply_migrations(connection, test_dir)
                except psycopg.errors.CheckViolation:
                    pass
                else:
                    raise AssertionError("Expected constraint failure")
                assert connection.execute("SELECT to_regclass('cpa.recovery_probe')").fetchone()[0] is None
                assert connection.execute("SELECT count(*) FROM cpa_meta.schema_migrations").fetchone()[0] == len(baseline)
                results.append("failed migration rolls back DDL/data/history")
                probe.write_text(valid)
                assert apply_migrations(connection, test_dir) == [probe.name]
                assert connection.execute("SELECT * FROM cpa.recovery_probe").fetchall() == [(1, 7)]
                results.append("corrected pending migration recovers")
                try:
                    with connection.transaction():
                        connection.execute("UPDATE cpa.recovery_probe SET value=9")
                        connection.execute("INSERT INTO cpa.recovery_probe VALUES (1, 10)")
                except psycopg.errors.UniqueViolation:
                    pass
                else:
                    raise AssertionError("Expected duplicate-key failure")
                assert connection.execute("SELECT * FROM cpa.recovery_probe").fetchall() == [(1, 7)]
                results.append("failed data transaction preserves original fixture")
                # Explicit test-only rollback, safe solely for this synthetic table.
                with connection.transaction():
                    connection.execute("DROP TABLE cpa.recovery_probe")
                    connection.execute(
                        "DELETE FROM cpa_meta.schema_migrations WHERE name=%s", (probe.name,)
                    )
                assert apply_migrations(connection, migrations) == []
                assert connection.execute("SELECT to_regclass('cpa.recovery_probe')").fetchone()[0] is None
                results.append("explicit synthetic rollback restores baseline")
            if extra_checks is not None:
                results.extend(extra_checks(connection))
        print(json.dumps({"server_version": version, "image_id": image_id, "passed": results}, indent=2))
    finally:
        if created and retain:
            print("RETAINED: " + name + "; no container stop or removal requested", flush=True)
        if created and not retain:
            docker("stop", "--time", "5", name)
            docker("rm", name)
            remaining = docker("ps", "-a", "--filter", "name=^/" + name + "$", "--format", "{{.Names}}")
            if remaining:
                raise RuntimeError("Disposable container cleanup not confirmed")
            print("PASS: disposable container removed; tmpfs data discarded")


if __name__ == "__main__":
    main()
