"""B028 evidence demo: retained HTTPS fixture plus explicit mock AI controls."""
import asyncio
from datetime import datetime, timezone
import http.client
import json
from pathlib import Path
import re
import ssl
from uuid import UUID, uuid4

from app.ai_adapter import AssessmentRequest, MockAdapter, ProviderReply, SCHEMA_VERSION
from app.ai_controls import LocalAIControls

ROOT=Path(__file__).resolve().parents[1]


class DemoProvider:
    def __init__(self, malformed=False):
        self.calls=0
        self.malformed=malformed

    async def generate(self, request):
        self.calls+=1
        body='{}' if self.malformed else json.dumps({'schema_version':SCHEMA_VERSION,
            'summary':'Synthetic foundation review draft.', 'assumptions':['Synthetic fixture only.'],
            'evidence_kind':'synthetic'})
        return ProviderReply(body,input_tokens=8,output_tokens=6)


async def demonstrate_mock():
    request=AssessmentRequest(uuid4(),UUID(int=1),UUID(int=11),'Synthetic review only.')
    provider=DemoProvider()
    adapter=MockAdapter(provider,timeout_seconds=1)
    result=await LocalAIControls({'LIVE_AI_ENABLED':'false'},adapter).assess(request)
    assert result.code=='draft' and result.outcome.draft.status=='draft'
    assert result.outcome.draft.evidence_kind=='synthetic' and result.usage.cost is None
    malformed=await MockAdapter(DemoProvider(True),timeout_seconds=1).assess(request)
    assert malformed.code=='malformed_output' and malformed.draft is None
    before=provider.calls
    live=await LocalAIControls({'LIVE_AI_ENABLED':'true','OPENAI_MODEL':'fixture-model',
        'OPENAI_API_KEY':'synthetic-not-a-secret','MAX_AI_RUN_COST':'1.00'},adapter).assess(request)
    assert live.code=='live_unavailable' and provider.calls==before
    return {'valid_mock':'synthetic draft','malformed_output':'rejected',
            'cost':'unknown','live_request':'blocked before adapter','provider_network_calls':0,
            'http_adapter_route':'not implemented; direct Python demonstration'}


def main():
    metadata=json.loads((ROOT/'docs/evidence/B027-rehearsal-runtime.json').read_text(encoding='utf-8'))
    name=metadata['container']
    assert re.fullmatch('cpa-b024-rehearsal-[0-9a-f]{32}',name)
    setup=json.loads((ROOT/'docs/evidence/B027-setup-checks.json').read_text(encoding='utf-8'))
    assert setup['completed']
    target=Path(setup['retained_directory']).resolve()
    assert target.parent==(ROOT/'.local/b027').resolve() and re.fullmatch('[0-9a-f]{32}',target.name)
    private=target/'workspace/.local/b024'/name.removeprefix('cpa-b024-rehearsal-')
    origin='https://127.0.0.1:3543'
    assert metadata['https_url']==origin
    trust=ssl.create_default_context(cafile=str(private/'ca.pem'))

    def call(path,method='GET',headers=None):
        client=http.client.HTTPSConnection('127.0.0.1',3543,context=trust,timeout=15)
        try:
            client.request(method,path,headers=headers or {})
            response=client.getresponse()
            return response.status,dict(response.getheaders()),response.read().decode()
        finally:
            client.close()

    assert call('/')[0]==200 and call('/health')[0]==200 and call('/ready')[0]==200
    assert call('/api/dashboard')[0]==401
    cookie=None
    try:
        status,headers,_=call('/api/session/login','POST',{'Origin':origin})
        assert status==200
        cookie=headers['set-cookie'].split(';',1)[0]
        status,_,body=call('/api/dashboard',headers={'Cookie':cookie})
        dashboard=json.loads(body)
        assert status==200 and dashboard['total']==3
        assert {r['id'] for r in dashboard['records']}=={str(UUID(int=n)) for n in (11,12,13)}
        assert call('/api/records/'+str(UUID(int=14)),headers={'Cookie':cookie})[0]==404
        status,_,body=call('/api/dashboard?owner_id='+str(UUID(int=3)),headers={'Cookie':cookie})
        assert status==200 and json.loads(body)['total']==0
    finally:
        if cookie:
            assert call('/api/session/logout','POST',{'Origin':origin,'Cookie':cookie})[0]==200
    assert call('/api/dashboard',headers={'Cookie':cookie})[0]==401
    mock=asyncio.run(demonstrate_mock())
    report={'checked_at':datetime.now(timezone.utc).isoformat(),'scope':'local synthetic foundation demonstration',
        'https_endpoint':origin,'tls':'explicit private CA and hostname verified',
        'ui_delivery':200,'readiness':200,'anonymous_dashboard':401,'authenticated_reference_count':3,
        'hidden_record':404,'hidden_owner_count':0,'logout_replay':401,'mock':mock,
        'browser_https_journey':False,'human_gate_signoffs_recorded':False,
        'existing_services_restarted':False,'resources_retained':True}
    (ROOT/'docs/evidence/B028-foundation-demo.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':
    main()
