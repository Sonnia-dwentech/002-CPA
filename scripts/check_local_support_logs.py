"""B027 inspect real, allowlisted local rehearsal logs without secret output."""
import argparse
import http.client
import json
from pathlib import Path
import re
import secrets
import ssl
import time
from uuid import UUID

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('setup_id')
    args=parser.parse_args()
    if not re.fullmatch('[0-9a-f]{32}',args.setup_id):
        parser.error('Recorded B027 setup ID required')
    workspace=ROOT/'.local/b027'/args.setup_id/'workspace'
    metadata=json.loads((workspace/'docs/evidence/B024-runtime.json').read_text(encoding='utf-8'))
    name=metadata['container']
    assert re.fullmatch('cpa-b024-rehearsal-[0-9a-f]{32}',name)
    private=workspace/'.local/b024'/name.removeprefix('cpa-b024-rehearsal-')
    assert metadata['https_url']=='https://127.0.0.1:3543'
    trust=ssl.create_default_context(cafile=str(private/'ca.pem'))
    canary='b027-private-'+secrets.token_hex(12)
    client=http.client.HTTPSConnection('127.0.0.1',3543,context=trust,timeout=15)
    try:
        client.request('GET','/api/'+canary+'?private='+canary,headers={'User-Agent':canary,'Cookie':'unused='+canary})
        response=client.getresponse()
        assert response.status==404 and canary.encode() not in response.read()
    finally:
        client.close()
    time.sleep(.1)
    text=(private/'operational.jsonl').read_text(encoding='utf-8')
    events=[json.loads(line) for line in text.splitlines()]
    assert events and canary not in text
    settings=json.loads((private/'database-secrets.json').read_text(encoding='utf-8'))
    for value in (settings['runtime_password'],settings['migration_password']):
        assert value not in text
    routes={'ready','login','logout','status','query','record','frontend','health','unmatched'}
    for event in events:
        assert set(event)=={'request_id','route','method','status','duration_ms'}
        assert UUID(event['request_id']).version==4
        assert event['route'] in routes and event['method'] in {'GET','POST','PUT','PATCH','DELETE','HEAD','OPTIONS','OTHER'}
        assert 100<=event['status']<=599 and event['duration_ms']>=0
    statuses=sorted({e['status'] for e in events})
    assert {200,400,401,403,404,503}<=set(statuses)
    source=json.loads((workspace/'docs/evidence/B024-local-rehearsal-checks.json').read_text(encoding='utf-8'))
    assert len(source['passed'])==6
    (ROOT/'docs/evidence/B027-operational-events.jsonl').write_text(text,encoding='utf-8')
    (ROOT/'docs/evidence/B027-rehearsal-runtime.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf-8')
    report={'events_checked':len(events),'statuses':statuses,'redaction_canary_absent':True,
            'database_passwords_absent':True,'allowed_fields_only':True,'rehearsal_checks':source['passed'],
            'existing_services_restarted':False,'resources_retained':True}
    (ROOT/'docs/evidence/B027-support-log-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':
    main()
