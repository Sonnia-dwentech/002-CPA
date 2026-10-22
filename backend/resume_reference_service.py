"""Resume only the retained reference API; never seed, migrate or restart data."""
import json
from pathlib import Path
import socket

import psycopg
import uvicorn
from app.local_rehearsal import create_rehearsal
from check_local_database import docker

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / '.local/b027/4ad0f577510342bcb2ae551e37e343c2/workspace'


def main():
    metadata = json.loads((WORKSPACE / 'docs/evidence/B024-runtime.json').read_text())
    private = Path(metadata['private_state_directory']).resolve()
    if not private.is_relative_to((WORKSPACE / '.local/b024').resolve()):
        raise RuntimeError('Unexpected private state location')
    if metadata['https_url'] != 'https://127.0.0.1:3543':
        raise RuntimeError('Unexpected service origin')
    if (private / 'ca.pem').read_bytes() != (ROOT / 'deployments/local-rehearsal/reference-dashboard-ca.pem').read_bytes():
        raise RuntimeError('Retained certificate does not match configured trust')
    with socket.socket() as probe:
        probe.bind(('127.0.0.1', 3543))
    name = metadata['container']
    if docker('inspect', name, '--format', '{{index .Config.Labels "cpa.task"}}') != 'B024-local-rehearsal':
        raise RuntimeError('Unexpected database container')
    endpoint = docker('port', name, '5432/tcp')
    if not endpoint.startswith('127.0.0.1:') or '\n' in endpoint:
        raise RuntimeError('Unexpected database binding')
    saved = json.loads((private / 'database-secrets.json').read_text())
    if saved['database'] != 'cpa_b024' or saved['runtime_user'] != 'cpa_runtime':
        raise RuntimeError('Unexpected runtime identity')
    connection = psycopg.connect(host='127.0.0.1', port=int(endpoint.rsplit(':', 1)[1]),
        dbname=saved['database'], user=saved['runtime_user'], password=saved['runtime_password'],
        autocommit=True, connect_timeout=5)
    del saved
    def write_event(event):
        with (private / 'operational.jsonl').open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(event, separators=(',', ':')) + '\n')
    try:
        expected = len(list((WORKSPACE / 'backend/migrations').glob('*.sql')))
        if connection.execute('SELECT count(*) FROM cpa_meta.schema_migrations').fetchone()[0] != expected:
            raise RuntimeError('Retained schema does not match')
        app = create_rehearsal(connection, expected, origin=metadata['https_url'],
            frontend_port=3300, log_sink=write_event)
        print('Resuming retained reference API on https://127.0.0.1:3543', flush=True)
        uvicorn.run(app, host='127.0.0.1', port=3543, ssl_certfile=str(private / 'server.pem'),
            ssl_keyfile=str(private / 'server-key.pem'), access_log=False, log_level='critical')
    finally:
        connection.close()


if __name__ == '__main__':
    try:
        main()
    except Exception:
        raise SystemExit('Reference service could not resume; private diagnostic details withheld.') from None
