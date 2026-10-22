"""B024 loopback HTTPS rehearsal. No cloud, downloads, trust install or cleanup.

Creates a new retained PostgreSQL volume/container each run. Runtime secrets
stay under an ACL-restricted .local directory. --serve keeps the preview open.
"""
import argparse
import http.client
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import socket
import ssl
import subprocess
import sys
import threading
import time
from uuid import UUID, uuid4

import psycopg
from psycopg import sql
import uvicorn
from app.database import apply_migrations
from app.local_rehearsal import create_rehearsal, COOKIE, ORIGIN
from check_local_database import docker

ROOT = Path(__file__).resolve().parents[1]


def run(command, cwd=ROOT, env=None, timeout=240):
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, timeout=timeout,
                            creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
    if result.returncode:
        raise RuntimeError("Rehearsal setup command failed; private output withheld")
    return result.stdout.decode(errors="replace")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate-python", required=True, help="Existing Python with cryptography; no package installation")
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--resume", action="store_true", help="Resume the exact recorded B024 container and private state")
    parser.add_argument("--reuse-build", action="store_true", help="Explicitly reuse the existing rehearsal production artifact")
    parser.add_argument("--frontend-port", type=int, default=3200)
    parser.add_argument("--https-port", type=int, default=3443)
    args = parser.parse_args()
    if not all(1024 <= port <= 65535 for port in (args.frontend_port, args.https_port)) or args.frontend_port == args.https_port:
        parser.error("Distinct unprivileged loopback ports required")
    origin = 'https://127.0.0.1:' + str(args.https_port)
    for port in (args.frontend_port,args.https_port):
        with socket.socket() as probe:
            probe.bind(("127.0.0.1",port))
    node = shutil.which("node")
    if not node:
        raise RuntimeError("Existing Node runtime required")
    run([node,"-e","require('@next/swc-win32-x64-msvc')"],ROOT/'frontend')
    if args.resume:
        metadata=json.loads((ROOT/'docs/evidence/B024-runtime.json').read_text())
        name=metadata['container']
        if not re.fullmatch(r'cpa-b024-rehearsal-[0-9a-f]{32}',name):
            raise RuntimeError('Invalid recorded rehearsal identity')
        identifier=name.removeprefix('cpa-b024-rehearsal-')
        private=ROOT/'.local'/'b024'/identifier
        volume=name+'-data'
        if docker('inspect',name,'--format','{{index .Config.Labels "cpa.task"}}') != 'B024-local-rehearsal':
            raise RuntimeError('Refusing unrelated container')
        saved=json.loads((private/'database-secrets.json').read_text())
        if saved['database']!='cpa_b024' or saved['runtime_user']!='cpa_runtime' or saved['migration_user']!='cpa_migrator':
            raise RuntimeError('Unexpected rehearsal credential scope')
        admin_password=saved['migration_password'];runtime_password=saved['runtime_password']
        image_id=metadata['image_id']
        print('Resuming retained rehearsal container: '+name,flush=True)
    else:
        identifier = uuid4().hex
        name = "cpa-b024-rehearsal-" + identifier
        volume = name + "-data"
        private = ROOT / '.local' / 'b024' / identifier
        private.mkdir(parents=True, exist_ok=False)
        if os.name == 'nt':
            account = run(['whoami']).strip()
            run(['icacls',str(private),'/inheritance:r','/grant:r',account+':(OI)(CI)F'])
        else:
            private.chmod(0o700)
        run([args.certificate_python, '-B', str(ROOT/'scripts/create_rehearsal_certificate.py'), str(private)])
        admin_password, runtime_password = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
        image_id = docker('image','inspect','postgres:17','--format','{{.Id}}')
        docker('volume','create','--label','cpa.task=B024-local-rehearsal',volume)
        docker('run','--pull=never','--detach','--name',name,'--label','cpa.task=B024-local-rehearsal',
               '--publish','127.0.0.1::5432','--mount','type=volume,source='+volume+',target=/var/lib/postgresql/data',
               '-e','POSTGRES_PASSWORD','-e','POSTGRES_USER=cpa_migrator','-e','POSTGRES_DB=cpa_b024',image_id,
               env=dict(os.environ,POSTGRES_PASSWORD=admin_password))
        print('Created retained rehearsal container: '+name,flush=True)
        endpoint = docker('port',name,'5432/tcp')
        if not endpoint.startswith('127.0.0.1:') or '\n' in endpoint:
            raise RuntimeError('Unexpected database binding')
        port = int(endpoint.rsplit(':',1)[1])
        (private/'database-secrets.json').write_text(json.dumps({'port':port,'database':'cpa_b024',
            'migration_user':'cpa_migrator','migration_password':admin_password,'runtime_user':'cpa_runtime','runtime_password':runtime_password}))
        metadata = {'scope':'local-synthetic-rehearsal','container':name,'volume':volume,'https_url':origin,
                    'frontend_internal_url':'http://127.0.0.1:'+str(args.frontend_port),'private_state_directory':str(private),
                    'image_id':image_id,'retained':True,'global_certificate_trust_installed':False}
        (ROOT/'docs/evidence/B024-runtime.json').write_text(json.dumps(metadata,indent=2)+'\n')

    def refresh_binding():
        endpoint=docker('port',name,'5432/tcp')
        if not endpoint.startswith('127.0.0.1:') or '\n' in endpoint:
            raise RuntimeError('Unexpected database binding')
        value=int(endpoint.rsplit(':',1)[1])
        (private/'database-secrets.json').write_text(json.dumps({'port':value,'database':'cpa_b024',
            'migration_user':'cpa_migrator','migration_password':admin_password,'runtime_user':'cpa_runtime','runtime_password':runtime_password}))
        return value
    port=refresh_binding()

    def connect(user, password):
        return psycopg.connect(host='127.0.0.1',port=port,dbname='cpa_b024',user=user,password=password,autocommit=True,connect_timeout=3)

    def admin_ready():
        deadline=time.monotonic()+45
        while time.monotonic()<deadline:
            try:return connect('cpa_migrator',admin_password)
            except psycopg.OperationalError:time.sleep(.3)
        raise RuntimeError('Rehearsal PostgreSQL did not start')

    admin=admin_ready()
    expected_count=len(list((ROOT/'backend/migrations').glob('*.sql')))
    migration_names=apply_migrations(admin,ROOT/'backend/migrations')
    if args.resume:
        assert migration_names==[]
    if not args.resume:
        with admin.transaction():
            for number,subject in ((1,'owner'),(2,'shared-owner'),(3,'hidden-owner')):
                admin.execute("INSERT INTO cpa.users VALUES (%s,'synthetic://b024',%s,'internal',NULL,true,true)",(UUID(int=number),subject))
                admin.execute("INSERT INTO cpa.user_roles VALUES (%s,'internal','cpa')",(UUID(int=number),))
            for number,owner,kind,state in ((11,1,'idea','draft'),(12,2,'idea','draft'),(13,1,'dossier','archived'),(14,3,'idea','draft')):
                admin.execute('INSERT INTO cpa.access_records VALUES (%s,%s,%s,NULL,NULL,NULL,%s)',(UUID(int=number),kind,UUID(int=owner),state))
            admin.execute("INSERT INTO cpa.record_grants VALUES (%s,%s,'read')",(UUID(int=12),UUID(int=1)))
            admin.execute(sql.SQL('CREATE ROLE cpa_runtime LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE PASSWORD {}').format(sql.Literal(runtime_password)))
            admin.execute('REVOKE ALL ON DATABASE cpa_b024 FROM PUBLIC')
            admin.execute('GRANT CONNECT ON DATABASE cpa_b024 TO cpa_runtime')
            admin.execute('REVOKE CREATE ON SCHEMA public FROM PUBLIC')
            admin.execute('GRANT USAGE ON SCHEMA cpa,cpa_meta TO cpa_runtime')
            admin.execute('GRANT SELECT ON ALL TABLES IN SCHEMA cpa TO cpa_runtime')
            admin.execute('GRANT SELECT ON cpa_meta.schema_migrations TO cpa_runtime')
            admin.execute('GRANT INSERT,UPDATE ON cpa.sessions TO cpa_runtime')
            # Existing SessionStore locks users before session rows. PostgreSQL
            # requires an UPDATE column privilege for SELECT FOR UPDATE.
            admin.execute('GRANT UPDATE(id) ON cpa.users TO cpa_runtime')
    admin.close()
    docker('restart',name)
    port=refresh_binding()
    admin=admin_ready()
    assert admin.execute('SELECT count(*) FROM cpa.access_records').fetchone()[0]==4
    assert apply_migrations(admin,ROOT/'backend/migrations')==[]
    runtime=connect('cpa_runtime',runtime_password)
    for statement in ('CREATE TABLE cpa.forbidden(id int)', 'UPDATE cpa.users SET membership_active=false', 'DELETE FROM cpa.access_records'):
        try:runtime.execute(statement)
        except psycopg.errors.InsufficientPrivilege:pass
        else:raise AssertionError('Runtime role exceeded intended privileges')
    outcomes=['separate persistent PostgreSQL and migrations survive container restart',
              'distinct runtime credential rejects schema creation, membership edits and record deletion']
    env=dict(os.environ,NEXT_TELEMETRY_DISABLED='1',npm_config_offline='true',npm_config_ignore_scripts='true')
    next_cli=str(ROOT/'frontend/node_modules/next/dist/bin/next')
    build_id_path=ROOT/'frontend/rehearsal/.next/BUILD_ID'
    if args.reuse_build:
        if not build_id_path.is_file():
            raise RuntimeError('No existing rehearsal production build')
        print('Reusing existing rehearsal production artifact',flush=True)
    else:
        print('Building isolated production frontend with installed dependencies...',flush=True)
        output=run([node,next_cli,'build','--webpack'],ROOT/'frontend/rehearsal',env,360)
        (private/'frontend-build.log').write_text(output,encoding='utf-8')
    metadata['frontend_build_id']=build_id_path.read_text().strip()
    (ROOT/'docs/evidence/B024-runtime.json').write_text(json.dumps(metadata,indent=2)+'\n')
    child_log=open(private/'frontend-server.log','wb')
    child=subprocess.Popen([node,next_cli,'start','--hostname','127.0.0.1','--port',str(args.frontend_port)],
        cwd=ROOT/'frontend/rehearsal',env=env,stdout=child_log,stderr=child_log,
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    event_log = private/'operational.jsonl'
    def write_event(event):
        # OperationalCapture emits only an allowlisted shape; never raw requests.
        with event_log.open('a',encoding='utf-8') as stream:
            stream.write(json.dumps(event,separators=(',',':'))+'\n')
    metadata['operational_log_path']=str(event_log)
    (ROOT/'docs/evidence/B024-runtime.json').write_text(json.dumps(metadata,indent=2)+'\n')
    server=None
    thread=None
    try:
        deadline=time.monotonic()+45
        while time.monotonic()<deadline:
            try:
                c=http.client.HTTPConnection('127.0.0.1',args.frontend_port,timeout=3);c.request('GET','/');r=c.getresponse();body=r.read();c.close()
                if r.status==200:break
            except OSError:time.sleep(.2)
        else:raise RuntimeError('Production frontend did not start')
        server=uvicorn.Server(uvicorn.Config(create_rehearsal(runtime,expected_count,origin=origin,frontend_port=args.frontend_port,log_sink=write_event),host='127.0.0.1',port=args.https_port,
            ssl_certfile=str(private/'server.pem'),ssl_keyfile=str(private/'server-key.pem'),access_log=False,log_level='critical'))
        thread=threading.Thread(target=server.run,daemon=True);thread.start()
        deadline=time.monotonic()+20
        while not server.started and time.monotonic()<deadline:time.sleep(.1)
        assert server.started
        trust=ssl.create_default_context(cafile=str(private/'ca.pem'))

        def call(path='/',method='GET',headers=None,context=trust):
            c=http.client.HTTPSConnection('127.0.0.1',args.https_port,context=context,timeout=20)
            try:
                c.request(method,path,headers=headers or {});r=c.getresponse()
                return r.status,dict(r.getheaders()),r.read().decode()
            finally:c.close()

        try:call(context=ssl.create_default_context())
        except ssl.SSLCertVerificationError:pass
        else:raise AssertionError('Unconfigured trust unexpectedly accepted local certificate')
        status,_,html=call()
        assert status==200 and 'LOCAL STAGING REHEARSAL' in html and 'Reference dashboard' in html
        asset=re.search(r'<script[^>]+src="([^"]+)"',html)
        assert asset and call(asset.group(1))[0]==200
        assert call('/health')[0]==200 and call('/ready')[0]==200
        assert call('/api/dashboard')[0]==401
        assert call('/api/dashboard',headers={'Host':'untrusted.invalid'})[0]==403
        assert call('/api/session/login','POST')[0]==403
        assert call('/api/session/login','POST',{'Origin':'https://untrusted.invalid'})[0]==403
        status,headers,body=call('/api/session/login','POST',{'Origin':origin})
        assert status==200
        raw=headers['set-cookie'];cookie=raw.split(';',1)[0]
        assert all(v in raw.lower() for v in ('secure','httponly','samesite=strict','path=/')) and 'domain=' not in raw.lower()
        assert cookie.split('=',1)[1] not in body
        auth={'Cookie':cookie}
        status,_,body=call('/api/dashboard',headers=auth)
        assert status==200 and json.loads(body)['total']==3 and str(UUID(int=14)) not in body
        assert call('/api/records/'+str(UUID(int=14)),headers=auth)[0]==404
        assert call('/api/records/'+str(UUID(int=11)),headers=auth)[0]==200
        assert call('/api/dashboard',headers={'Cookie':cookie+'; '+cookie})[0]==401
        assert call('/api/dashboard',headers={**auth,'Authorization':'Bearer spoof'})[0]==400
        assert json.loads(call('/api/dashboard?kind=idea&state=draft&owner_id='+str(UUID(int=2)),headers=auth)[2])['total']==1
        assert json.loads(call('/api/dashboard?state=submitted',headers=auth)[2])['total']==0
        assert json.loads(call('/api/dashboard?kind=research',headers=auth)[2])['total'] is None
        outcomes.extend(['production build and assets served through hostname-verified loopback HTTPS; default trust rejects private CA',
                         'readiness, secure cookie, exact origin/host checks and unauthenticated denial verified',
                         'stored dashboard filters and direct record isolation verified; spoofed/duplicate credentials rejected'])
        admin.execute('ALTER TABLE cpa.access_records RENAME TO rehearsal_failure_probe')
        try:
            assert call('/ready')[0]==503
            status,_,body=call('/api/dashboard',headers=auth)
            assert status==503 and 'total' not in body and 'rehearsal_failure_probe' not in body
        finally:admin.execute('ALTER TABLE cpa.rehearsal_failure_probe RENAME TO access_records')
        assert call('/ready')[0]==200 and json.loads(call('/api/dashboard',headers=auth)[2])['total']==3
        assert call('/api/session/logout','POST',{**auth,'Origin':origin})[0]==200
        assert call('/api/dashboard',headers=auth)[0]==401
        outcomes.append('actual database error fails readiness/query safely, recovers, and logout replay is denied')
        report={**metadata,'passed':outcomes,'database_server_version':admin.execute('SHOW server_version').fetchone()[0],
                'certificate_validation':'explicit generated CA; hostname validation enabled; no insecure skip',
                'cloud_deployed':False,'production_identity':False}
        (ROOT/'docs/evidence/B024-local-rehearsal-checks.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({'B024_checks_passed':outcomes,'preview':origin,'retained_container':name}),flush=True)
        if args.serve:
            print('Rehearsal running. Certificate trusted only by explicit test CA; no system trust changes. Create '+str(private/'stop')+' to end servers; database/volume retained.',flush=True)
            while not (private/'stop').exists():
                if child.poll() is not None or not thread.is_alive():raise RuntimeError('Rehearsal service stopped')
                time.sleep(.5)
    finally:
        if server:server.should_exit=True
        if thread:thread.join(timeout=10)
        if child.poll() is None:
            subprocess.run(['taskkill','/PID',str(child.pid),'/T','/F'],capture_output=True,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            child.wait(timeout=15)
        child_log.close();runtime.close();admin.close()
        print('RETAINED: '+name+' and '+volume,flush=True)


if __name__=='__main__':
    main()
