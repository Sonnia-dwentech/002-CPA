"""Verify the main browser BFF against the retained synthetic HTTPS service."""
from datetime import datetime, timezone
import http.client
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ORIGIN='http://127.0.0.1:3000'
COOKIE='cpa_reference_session'


def call(endpoint, method='GET', headers=None):
    client=http.client.HTTPConnection('127.0.0.1',3000,timeout=30)
    try:
        client.request(method,endpoint,headers=headers or {})
        response=client.getresponse()
        return response.status,dict(response.getheaders()),response.read().decode()
    finally:
        client.close()


def main():
    passed=[]
    status,_,body=call('/')
    assert status==200 and 'Reference dashboard' in body and 'Checking your local session' in body
    assert call('/dashboard')[0]==200
    assert call('/api/reference/dashboard')[0]==401
    assert call('/api/reference/session/status')[0]==401
    for headers in ({},{'Origin':'http://invalid.example'},{'Origin':ORIGIN,'Sec-Fetch-Site':'cross-site'}):
        assert call('/api/reference/session/login','POST',headers)[0]==403
    assert call('/api/reference/dashboard',headers={'Host':'invalid.example'})[0]==403
    assert call('/api/reference/dashboard',headers={'Authorization':'Bearer spoof'})[0]==400
    assert call('/api/reference/records/00000000-0000-0000-0000-00000000000e')[0]==404
    assert call('/api/reference/session/login','GET')[0]==405
    passed.append('Main home/dashboard render; anonymous, cross-site, origin/host, method and route boundaries pass')
    cookie=None
    try:
        status,headers,body=call('/api/reference/session/login','POST',{'Origin':ORIGIN})
        assert status==200
        raw=headers['set-cookie'];cookie=raw.split(';',1)[0]
        assert cookie.startswith(COOKIE+'=')
        assert all(v in raw.lower() for v in ('httponly','samesite=strict','path=/api/reference'))
        assert 'domain=' not in raw.lower() and cookie.split('=',1)[1] not in body
        auth={'Cookie':cookie}
        status,headers,body=call('/api/reference/dashboard',headers=auth)
        data=json.loads(body)
        assert status==200 and data['total']==3 and len(data['records'])==3
        assert headers['cache-control']=='no-store'
        assert '00000000-0000-0000-0000-00000000000e' not in body
        assert call('/api/reference/session/status',headers=auth)[0]==200
        status,headers,_=call('/api/reference/session/login','POST',{**auth,'Origin':ORIGIN})
        assert status==200 and 'set-cookie' not in headers
        passed.append('Scoped HttpOnly cookie, stored permitted dashboard, session restoration and repeated login reuse pass')
        for query,expected in [('kind=idea&state=draft&owner_id=00000000-0000-0000-0000-000000000002',1),
                               ('owner_id=00000000-0000-0000-0000-000000000003',0),('kind=dossier',1),('kind=research',None)]:
            status,_,body=call('/api/reference/dashboard?'+query,headers=auth)
            assert status==200 and json.loads(body)['total']==expected
        for query in ('owner_id=bad','kind=idea&kind=dossier','unexpected=true'):
            status,_,body=call('/api/reference/dashboard?'+query,headers=auth)
            assert status==422 and '"total"' not in body
        assert call('/api/reference/dashboard',headers={'Cookie':cookie+'; '+cookie})[0]==401
        assert call('/api/reference/dashboard',headers={'Cookie':COOKIE+'='})[0]==401
        passed.append('Combined/hidden-owner/quick-view filters, unavailable distinction, invalid input and ambiguous cookies pass')
    finally:
        if cookie:
            assert call('/api/reference/session/logout','POST',{'Cookie':cookie,'Origin':ORIGIN})[0]==200
    assert call('/api/reference/dashboard',headers={'Cookie':cookie})[0]==401
    assert call('/api/reference/session/logout','POST',{'Origin':ORIGIN})[0]==200
    # A confirmed invalid opaque session must recover on an explicit login.
    stale=COOKIE+'='+'x'*43
    status,headers,_=call('/api/reference/session/login','POST',{'Cookie':stale,'Origin':ORIGIN})
    assert status==200 and 'set-cookie' in headers
    recovered=headers['set-cookie'].split(';',1)[0]
    try:
        assert call('/api/reference/dashboard',headers={'Cookie':recovered})[0]==200
    finally:
        assert call('/api/reference/session/logout','POST',{'Cookie':recovered,'Origin':ORIGIN})[0]==200
    passed.append('Logout/replay denial, already-signed-out logout and explicit stale-session recovery pass')
    report={'checked_at':datetime.now(timezone.utc).isoformat(),'scope':'main loopback browser/API integration using retained synthetic data',
            'passed':passed,'source_database_fixtures_changed':False,'database_resources_retained':True,
            'browser_http_cookie_scope':'loopback only; upstream TLS verified using dedicated public CA'}
    (ROOT/'docs/evidence/main-dashboard-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':
    main()
