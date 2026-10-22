"""B025 snapshot backup and isolated restore; retain every backup/container.

Source is the recorded B024 rehearsal only. Restore never targets that source.
No application outage, source data change, deletion or cloud operation.
"""
from datetime import datetime, timezone
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import secrets
import ssl
import subprocess
import time
from uuid import UUID, uuid4

import psycopg
from psycopg import sql
from fastapi import HTTPException
from app.access import VerifiedIdentity
from app.dashboard import DashboardStore
from app.sessions import SessionStore
from app.database import apply_migrations
from check_local_database import docker, DOCKER
from run_local_rehearsal import run

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(connection):
    tables = connection.execute("SELECT schemaname,tablename FROM pg_tables WHERE schemaname IN ('cpa','cpa_meta') ORDER BY 1,2").fetchall()
    result = {}
    for schema, table in tables:
        rows = connection.execute(sql.SQL('SELECT to_jsonb(t) FROM {}.{} t').format(sql.Identifier(schema),sql.Identifier(table))).fetchall()
        canonical = sorted(json.dumps(row[0],sort_keys=True,separators=(',',':')) for row in rows)
        result[schema+'.'+table] = {'rows':len(rows),'sha256':hashlib.sha256('\n'.join(canonical).encode()).hexdigest()}
    return result


def loopback_port(name):
    binding=docker('port',name,'5432/tcp')
    if not re.fullmatch(r'127\.0\.0\.1:[0-9]+',binding):
        raise RuntimeError('Unexpected database binding')
    return int(binding.rsplit(':',1)[1])


def verify_restored_controls(restored, runtime):
    maximum=restored.execute('SELECT COALESCE(max(id),0) FROM cpa.audit_events').fetchone()[0]
    next_id=restored.execute("SELECT nextval(pg_get_serial_sequence('cpa.audit_events','id'))").fetchone()[0]
    assert next_id>maximum
    store=SessionStore(runtime)
    token=store.issue_after_verification(VerifiedIdentity('synthetic://b024','owner'))
    restored.execute('UPDATE cpa.users SET membership_active=false WHERE id=%s',(UUID(int=1),))
    restored.execute('UPDATE cpa.users SET membership_active=true WHERE id=%s',(UUID(int=1),))
    try:store.validate(token)
    except HTTPException as error:assert error.status_code==401
    else:raise AssertionError('Restored revocation trigger failed')


def main():
    started=time.monotonic()
    record=json.loads((ROOT/'docs/evidence/B024-runtime.json').read_text(encoding='utf-8'))
    source=record['container']
    if not re.fullmatch(r'cpa-b024-rehearsal-[0-9a-f]{32}',source):
        raise RuntimeError('Refusing unrecognized backup source')
    if docker('inspect',source,'--format','{{index .Config.Labels "cpa.task"}}')!='B024-local-rehearsal':
        raise RuntimeError('Source label mismatch')
    private_source=ROOT/'.local'/'b024'/source.removeprefix('cpa-b024-rehearsal-')
    credentials=json.loads((private_source/'database-secrets.json').read_text(encoding='utf-8'))
    if credentials['database']!='cpa_b024' or credentials['migration_user']!='cpa_migrator':
        raise RuntimeError('Source credential scope mismatch')
    source_port=loopback_port(source)
    source_db=psycopg.connect(host='127.0.0.1',port=source_port,dbname='cpa_b024',user='cpa_migrator',
                               password=credentials['migration_password'],autocommit=True,connect_timeout=5)
    identifier=uuid4().hex
    destination='cpa-b025-restore-'+identifier
    volume=destination+'-data'
    assert destination!=source
    private=ROOT/'.local'/'b025'/identifier
    private.mkdir(parents=True,exist_ok=False)
    if os.name=='nt':
        account=run(['whoami']).strip()
        run(['icacls',str(private),'/inheritance:r','/grant:r',account+':(OI)(CI)F'])
    else:private.chmod(0o700)
    archive=private/'b024-snapshot.dump'
    image_id=docker('inspect',source,'--format','{{.Image}}')
    snapshot_at=datetime.now(timezone.utc).isoformat()
    backup_start=time.monotonic()
    try:
        with source_db.transaction():
            source_db.execute('SET TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY')
            snapshot=source_db.execute('SELECT pg_export_snapshot()').fetchone()[0]
            expected=fingerprint(source_db)
            with archive.open('xb') as output:
                dumped=subprocess.run([*DOCKER,'exec',source,'pg_dump','-U','cpa_migrator','-d','cpa_b024',
                    '--format=custom','--no-owner','--no-acl','--snapshot='+snapshot],stdout=output,stderr=subprocess.PIPE,
                    timeout=120,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
            if dumped.returncode:
                raise RuntimeError('Backup failed; diagnostic payload withheld')
    finally:source_db.close()
    backup_seconds=time.monotonic()-backup_start
    digest=hashlib.sha256(archive.read_bytes()).hexdigest()
    assert archive.stat().st_size>0
    (private/'snapshot-manifest.json').write_text(json.dumps({'snapshot_at_utc':snapshot_at,'sha256':digest,'tables':expected},indent=2),encoding='utf-8')
    print('Snapshot backup captured; source data unchanged. Preparing isolated restore.',flush=True)
    # New target name, new named volume, new database and credentials. No --clean.
    password=secrets.token_urlsafe(32)
    runtime_password=secrets.token_urlsafe(32)
    docker('volume','create','--label','cpa.task=B025-local-recovery',volume)
    docker('run','--pull=never','--detach','--name',destination,'--label','cpa.task=B025-local-recovery',
           '--publish','127.0.0.1::5432','--mount','type=volume,source='+volume+',target=/var/lib/postgresql/data',
           '-e','POSTGRES_PASSWORD','-e','POSTGRES_USER=cpa_restore','-e','POSTGRES_DB=cpa_b025_restore',image_id,
           env=dict(os.environ,POSTGRES_PASSWORD=password))
    port=loopback_port(destination)
    (private/'restore-secrets.json').write_text(json.dumps({'port':port,'database':'cpa_b025_restore',
        'restore_user':'cpa_restore','restore_password':password,'runtime_user':'cpa_restore_runtime','runtime_password':runtime_password}),encoding='utf-8')
    runtime_record={'source_container':source,'destination_container':destination,'volume':volume,
                    'private_directory':str(private),'backup_file':str(archive),'sha256':digest,'retained':True}
    (ROOT/'docs/evidence/B025-runtime.json').write_text(json.dumps(runtime_record,indent=2)+'\n',encoding='utf-8')
    deadline=time.monotonic()+45
    restored=None
    while time.monotonic()<deadline:
        try:
            restored=psycopg.connect(host='127.0.0.1',port=port,dbname='cpa_b025_restore',user='cpa_restore',password=password,autocommit=True,connect_timeout=3)
            break
        except psycopg.OperationalError:time.sleep(.3)
    if restored is None:raise RuntimeError('Restore destination not ready; resources retained')
    runtime=None
    restore_started=time.monotonic()
    try:
        assert restored.execute('SELECT current_database()').fetchone()[0]=='cpa_b025_restore'
        assert restored.execute("SELECT to_regnamespace('cpa')").fetchone()[0] is None
        if hashlib.sha256(archive.read_bytes()).hexdigest()!=digest:
            raise RuntimeError('Archive checksum mismatch; no restore attempted')
        with archive.open('rb') as input_file:
            result=subprocess.run([*DOCKER,'exec','-i',destination,'pg_restore','-U','cpa_restore','-d','cpa_b025_restore',
                '--no-owner','--no-acl','--exit-on-error','--single-transaction'],stdin=input_file,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                timeout=120,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        if result.returncode:raise RuntimeError('Isolated restore failed; target and backup retained')
        actual=fingerprint(restored)
        assert actual==expected, 'Recovered table fingerprints differ from backup snapshot'
        assert apply_migrations(restored,ROOT/'backend/migrations')==[]
        restore_seconds=time.monotonic()-restore_started
        # Restored credentials/sessions must not become access to a different environment.
        restored.execute('UPDATE cpa.sessions SET revoked_at=COALESCE(revoked_at,clock_timestamp())')
        assert restored.execute('SELECT count(*) FROM cpa.sessions WHERE revoked_at IS NULL').fetchone()[0]==0
        restored.execute(sql.SQL('CREATE ROLE cpa_restore_runtime LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE PASSWORD {}').format(sql.Literal(runtime_password)))
        restored.execute('REVOKE ALL ON DATABASE cpa_b025_restore FROM PUBLIC')
        restored.execute('GRANT CONNECT ON DATABASE cpa_b025_restore TO cpa_restore_runtime')
        restored.execute('REVOKE CREATE ON SCHEMA public FROM PUBLIC')
        restored.execute('GRANT USAGE ON SCHEMA cpa,cpa_meta TO cpa_restore_runtime')
        restored.execute('GRANT SELECT ON ALL TABLES IN SCHEMA cpa TO cpa_restore_runtime')
        restored.execute('GRANT SELECT ON cpa_meta.schema_migrations TO cpa_restore_runtime')
        restored.execute('GRANT INSERT,UPDATE ON cpa.sessions TO cpa_restore_runtime')
        restored.execute('GRANT UPDATE(id) ON cpa.users TO cpa_restore_runtime')
        runtime=psycopg.connect(host='127.0.0.1',port=port,dbname='cpa_b025_restore',user='cpa_restore_runtime',password=runtime_password,autocommit=True,connect_timeout=3)
        dashboard=DashboardStore(runtime,{'idea','dossier'})
        identity=VerifiedIdentity('synthetic://b024','owner')
        result=dashboard.query(identity)
        assert result.total==3 and UUID(int=14) not in [r.id for r in result.records]
        assert dashboard.query(identity,{'kind':'idea','owner_id':str(UUID(int=2))}).total==1
        sessions=SessionStore(runtime)
        token=sessions.issue_after_verification(identity)
        assert sessions.validate(token).identity==identity
        sessions.logout(token)
        try:sessions.validate(token)
        except HTTPException as error:assert error.status_code==401
        else:raise AssertionError('Restored-session logout replay allowed')
        for command in ('CREATE TABLE cpa.forbidden(id int)','UPDATE cpa.users SET enabled=false'):
            try:runtime.execute(command)
            except psycopg.errors.InsufficientPrivilege:pass
            else:raise AssertionError('Restore runtime role excessive')
        verify_restored_controls(restored,runtime)
        # Exercise failed-migration rollback on the new restore target only.
        before_probe=fingerprint(restored)
        probes=private/'migration-probe';probes.mkdir()
        for file in (ROOT/'backend/migrations').glob('*.sql'):
            (probes/file.name).write_bytes(file.read_bytes())
        (probes/'9000_failed_recovery_probe.sql').write_text('CREATE TABLE cpa.b025_probe (id integer PRIMARY KEY); INSERT INTO cpa.b025_probe VALUES (1),(1);',encoding='utf-8')
        try:apply_migrations(restored,probes)
        except psycopg.errors.UniqueViolation:pass
        else:raise AssertionError('Expected failed migration')
        assert restored.execute("SELECT to_regclass('cpa.b025_probe')").fetchone()[0] is None
        assert fingerprint(restored)==before_probe
        # Existing running source: certificate-verified readiness only, no login or writes.
        trust=ssl.create_default_context(cafile=str(private_source/'ca.pem'))
        client=http.client.HTTPSConnection('127.0.0.1',3443,context=trust,timeout=10)
        client.request('GET','/ready');health=client.getresponse();health.read();assert health.status==200;client.close()
        checks=['snapshot-consistent backup exported with matching source fingerprints',
                'archive checksum verified before single-transaction restore to new empty database',
                'all application and migration table counts/digests match snapshot; migration reapply is no-op',
                'restored sessions invalidated; new independent runtime credentials and synthetic login/logout verified',
                'restored dashboard visibility and filters work; runtime DDL and membership edits denied',
                'restored audit identity sequence advances beyond existing IDs and membership trigger revokes sessions',
                'failed migration rolls back schema/data/history on restore target',
                'original B024 HTTPS readiness remains healthy without source writes or downtime']
        report={**runtime_record,'snapshot_at_utc':snapshot_at,'backup_bytes':archive.stat().st_size,
                'backup_seconds':round(backup_seconds,3),'restore_and_compare_seconds':round(restore_seconds,3),
                'total_drill_seconds':round(time.monotonic()-started,3),'snapshot_tables':expected,'passed':checks,
                'retention':'until explicit user instruction; no scheduled cleanup','recovery_objective':'measured local drill only; no hosted RPO/RTO approved',
                'source_modified':False,'app_artifact_rollback_executed':False}
        (ROOT/'docs/evidence/B025-local-recovery-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'passed':checks,'backup_seconds':report['backup_seconds'],'restore_and_compare_seconds':report['restore_and_compare_seconds'],
                          'retained_restore_container':destination}),flush=True)
    finally:
        if runtime:runtime.close()
        restored.close()
        print('RETAINED: backup, private state, restore container and volume. Source untouched.',flush=True)


if __name__=='__main__':
    main()
