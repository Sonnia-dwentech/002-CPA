"""Local PostgreSQL connectivity and transactional, checksum-checked migrations."""
import hashlib
import re
from pathlib import Path

import psycopg


def connect_local(*, port: int, password: str):
    """Connect only to the disposable B012 database on IPv4 loopback."""
    if not 1024 <= port <= 65535:
        raise ValueError("Invalid local port")
    return psycopg.connect(
        host="127.0.0.1", port=port, dbname="cpa_b012",
        user="cpa_b012", password=password, connect_timeout=5,
        autocommit=True,
    )


def apply_migrations(connection, directory: Path) -> list[str]:
    """Apply one pending batch atomically; refuse changed or missing history.

    SQL files must contain transaction-compatible operations and no transaction
    control statements. This is a local foundation workflow, not a SQL parser.
    """
    files = sorted(directory.glob("*.sql"))
    names = [p.name for p in files]
    if not names or any(not re.fullmatch(r"\d{4}_[a-z0-9_]+\.sql", n) for n in names):
        raise ValueError("Expected ordered NNNN_name.sql migration files")
    if len({n[:4] for n in names}) != len(names):
        raise ValueError("Duplicate migration version")
    sources = [(p.name, p.read_bytes()) for p in files]
    checksums = {name: hashlib.sha256(data).hexdigest() for name, data in sources}
    applied = []
    with connection.transaction():
        connection.execute("SELECT pg_advisory_xact_lock(12012013)")
        connection.execute("CREATE SCHEMA IF NOT EXISTS cpa_meta")
        connection.execute("""
            CREATE TABLE IF NOT EXISTS cpa_meta.schema_migrations (
                name text PRIMARY KEY,
                checksum text NOT NULL CHECK (length(checksum) = 64),
                applied_at timestamptz NOT NULL DEFAULT now()
            )
        """)
        history = connection.execute(
            "SELECT name, checksum FROM cpa_meta.schema_migrations ORDER BY name"
        ).fetchall()
        if [row[0] for row in history] != names[:len(history)]:
            raise ValueError("Migration history is not a prefix of local files")
        if any(checksums[name] != digest for name, digest in history):
            raise ValueError("Applied migration checksum mismatch")
        for name, data in sources[len(history):]:
            connection.execute(data.decode("utf-8"))
            connection.execute(
                "INSERT INTO cpa_meta.schema_migrations(name, checksum) VALUES (%s, %s)",
                (name, checksums[name]),
            )
            applied.append(name)
    return applied
