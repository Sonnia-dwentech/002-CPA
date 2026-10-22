"""B026 checks against the retained local rehearsal; no restart or cleanup."""
from datetime import datetime, timezone
import http.client
import json
from pathlib import Path
import re
import ssl
from uuid import UUID

import psycopg

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://127.0.0.1:3443'


def main():
    metadata = json.loads((ROOT/'docs/evidence/B024-runtime.json').read_text(encoding='utf-8'))
    name = metadata['container']
    assert re.fullmatch(r'cpa-b024-rehearsal-[0-9a-f]{32}', name)
    private = ROOT/'.local/b024'/name.removeprefix('cpa-b024-rehearsal-')
    trust = ssl.create_default_context(cafile=str(private/'ca.pem'))
    passed = []

    def call(path='/', method='GET', headers=None, context=trust):
        connection = http.client.HTTPSConnection('127.0.0.1', 3443, context=context, timeout=20)
        try:
            connection.request(method, path, headers=headers or {})
            result = connection.getresponse()
            return result.status, dict(result.getheaders()), result.read().decode()
        finally:
            connection.close()

    try:
        call(context=ssl.create_default_context())
    except ssl.SSLCertVerificationError:
        pass
    else:
        raise AssertionError('Unexpected default trust')
    status, headers, html = call()
    assert status == 200 and 'Reference dashboard' in html and 'LOCAL STAGING REHEARSAL' in html
    assets = re.findall(r'<script[^>]+src="([^"]+)"', html)
    assert assets
    for asset in assets:
        assert asset.startswith('/_next/') and call(asset)[0] == 200
    assert headers['x-content-type-options'] == 'nosniff'
    assert headers['x-frame-options'] == 'DENY'
    assert headers['referrer-policy'] == 'no-referrer'
    assert call('/health')[0] == call('/ready')[0] == 200
    passed.append('Production HTML and all referenced scripts served with verified TLS; readiness and security headers pass')
    own, shared, hidden, absent = [str(UUID(int=n)) for n in (11, 12, 14, 999)]
    for path in ('/api/dashboard', '/api/session/status', '/api/records/'+own):
        assert call(path)[0] == 401
    for headers in ({}, {'Origin':'https://invalid.example'}, {'Origin':ORIGIN,'Sec-Fetch-Site':'cross-site'}):
        assert call('/api/session/login', 'POST', headers)[0] == 403
    assert call('/api/dashboard', headers={'Host':'invalid.example'})[0] == 403
    passed.append('AT-01 anonymous denial and exact host/origin/cross-site boundaries pass')
    cookie = None
    try:
        status, headers, body = call('/api/session/login', 'POST', {'Origin':ORIGIN})
        assert status == 200
        raw = headers['set-cookie']
        cookie = raw.split(';', 1)[0]
        assert all(flag in raw.lower() for flag in ('secure','httponly','samesite=strict','path=/'))
        assert 'domain=' not in raw.lower() and cookie.split('=',1)[1] not in body
        auth = {'Cookie':cookie}
        status, headers, body = call('/api/dashboard', headers=auth)
        data = json.loads(body)
        assert status == 200 and headers['cache-control'] == 'no-store'
        assert data['total'] == 3 and len(data['records']) == 3 and hidden not in body
        assert call('/api/session/status', headers=auth)[0] == 200
        for record in (own, shared):
            assert call('/api/records/'+record, headers=auth)[0] == 200
        denied = call('/api/records/'+hidden, headers=auth)
        missing = call('/api/records/'+absent, headers=auth)
        assert denied[0] == missing[0] == 404 and denied[2] == missing[2]
        assert hidden not in denied[2]
        for path in ('/api/files/'+hidden, '/api/search?q='+hidden, '/records/'+hidden):
            status, _, body = call(path, headers=auth)
            assert status == 404 and '"owner_id"' not in body
        passed.append('Authenticated stored query, owned/shared records, indistinguishable hidden/missing denial and unavailable file/search routes pass')
        filters = {'kind=idea&state=draft&owner_id='+str(UUID(int=2)):1,
                   'owner_id='+str(UUID(int=3)):0, 'state=submitted':0, 'kind=research':None}
        for query, count in filters.items():
            status, _, body = call('/api/dashboard?'+query, headers=auth)
            assert status == 200 and json.loads(body)['total'] == count and hidden not in body
        for query in ('owner_id=invalid','kind=idea&kind=dossier','unexpected=true'):
            status, _, body = call('/api/dashboard?'+query, headers=auth)
            assert status == 422 and '"total"' not in body and 'Traceback' not in body
        assert call('/api/dashboard', headers={'Cookie':cookie+'; '+cookie})[0] == 401
        assert call('/api/dashboard', headers={**auth,'Authorization':'Bearer spoof'})[0] == 400
        passed.append('Permission-filtered counts, zero/unavailable distinction, observable validation failures and credential ambiguity rejection pass')
    finally:
        if cookie:
            assert call('/api/session/logout','POST',{'Cookie':cookie,'Origin':ORIGIN})[0] == 200
    assert call('/api/dashboard',headers={'Cookie':cookie})[0] == 401
    passed.append('Only the check session is revoked; replay fails')
    secret = json.loads((private/'database-secrets.json').read_text(encoding='utf-8'))
    assert secret['database'] == 'cpa_b024' and secret['runtime_user'] == 'cpa_runtime'
    with psycopg.connect(host='127.0.0.1',port=secret['port'],dbname=secret['database'],
                          user=secret['runtime_user'],password=secret['runtime_password']) as db:
        db.execute('SET TRANSACTION READ ONLY')
        assert db.execute('SELECT current_database(),current_user').fetchone() == ('cpa_b024','cpa_runtime')
        assert db.execute('SELECT rolsuper,rolcreatedb,rolcreaterole FROM pg_roles WHERE rolname=current_user').fetchone() == (False,False,False)
        assert not db.execute("SELECT has_schema_privilege(current_user,'cpa','CREATE')").fetchone()[0]
        assert not db.execute("SELECT has_table_privilege(current_user,'cpa.access_records','DELETE')").fetchone()[0]
        assert not db.execute("SELECT has_column_privilege(current_user,'cpa.users','membership_active','UPDATE')").fetchone()[0]
        assert db.execute('SELECT count(*) FROM cpa.access_records').fetchone()[0] == 4
    assert call('/ready')[0] == 200
    passed.append('Read-only live database inspection confirms fixture persistence and restricted runtime role')
    report = {'checked_at':datetime.now(timezone.utc).isoformat(),'scope':'local-synthetic-rehearsal',
              'passed':passed,'container':name,'browser_https_verified':False,'hosted_staging_verified':False,
              'retained':True,'database_mutations':'check session issuance/validation/revocation only; no fixture or schema changes'}
    (ROOT/'docs/evidence/B026-local-foundation-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':passed,'retained':True}))


if __name__ == '__main__':
    main()
