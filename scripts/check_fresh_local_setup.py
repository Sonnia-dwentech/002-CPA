"""B027 offline setup into a new retained folder, never the working installs."""
from datetime import datetime, timezone
import argparse
from email.parser import Parser
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--allow-locked-downloads',action='store_true',help='Requires explicit user approval; exact npm lock only, no lifecycle scripts')
    parser.add_argument('--resume-run',help='Resume a retained B027 setup ID after correcting a setup-runner issue')
    args=parser.parse_args()
    if args.resume_run and not re.fullmatch('[0-9a-f]{32}',args.resume_run):
        parser.error('A recorded UUID hex ID is required')
    target = ROOT/'.local/b027'/(args.resume_run or uuid.uuid4().hex)
    target.mkdir(parents=True,exist_ok=bool(args.resume_run))
    workspace = target/'workspace'
    wheels = target/'wheelhouse'
    wheels.mkdir(exist_ok=bool(args.resume_run))
    steps = []
    report = {'started_at':datetime.now(timezone.utc).isoformat(), 'retained_directory':str(target),
              'network':'approved exact npm lock downloads; Python offline' if args.allow_locked_downloads else 'disabled for dependency installs', 'steps':steps, 'completed':False}
    if args.resume_run:
        report=json.loads((target/'setup-state.json').read_text(encoding='utf-8'))
        steps=report['steps']
        report['resumed_at']=datetime.now(timezone.utc).isoformat()

    def save():
        (ROOT/'docs/evidence/B027-setup-checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        (target/'setup-state.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')

    def run(label, command, cwd=workspace, timeout=240):
        if args.resume_run and any(s['check']==label and s['exit_code']==0 for s in steps):
            print(label+': prior successful step retained',flush=True)
            return ''
        result = subprocess.run(command,cwd=cwd,capture_output=True,timeout=timeout,
                                creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0),
                                env=dict(os.environ,NEXT_TELEMETRY_DISABLED='1',PIP_NO_INDEX='1',PIP_DISABLE_PIP_VERSION_CHECK='1'))
        (target/(label+'.log')).write_bytes(result.stdout+result.stderr)
        steps.append({'check':label,'exit_code':result.returncode})
        save()
        print(label+': '+('PASS' if result.returncode==0 else 'FAIL'),flush=True)
        if result.returncode:
            raise RuntimeError('Offline setup stopped at '+label+'; retained log available')
        return result.stdout.decode(errors='replace')

    save()
    ignored = shutil.ignore_patterns('node_modules','.next','.venv*','__pycache__','*.tsbuildinfo','.npm-logs')
    if not args.resume_run:
        for folder in ('backend','frontend','scripts'):
            shutil.copytree(ROOT/folder,workspace/folder,ignore=ignored)
        (workspace/'docs/evidence').mkdir(parents=True)
    shutil.copyfile(ROOT/'.env.example',workspace/'.env.example')
    pins = {}
    for line in (ROOT/'backend/requirements-installed-py312.txt').read_text(encoding='utf-8').splitlines():
        if line.strip():
            name,version=line.split('==')
            pins[re.sub(r'[-_.]+','-',name).lower()]=version
    cache = Path(subprocess.check_output([sys.executable,'-m','pip','cache','dir'],text=True).strip())
    selected = {}
    for body in (cache/'http-v2').rglob('*.body'):
        try:
            with ZipFile(body) as archive:
                metadata = next((n for n in archive.namelist() if n.endswith('.dist-info/METADATA')),None)
                if not metadata:
                    continue
                info=Parser().parsestr(archive.read(metadata).decode())
                name=re.sub(r'[-_.]+','-',info['Name']).lower()
                if pins.get(name)!=info['Version']:
                    continue
                wheel=metadata.rsplit('/',1)[0]+'/WHEEL'
                tags=Parser().parsestr(archive.read(wheel).decode()).get_all('Tag')
                tag=next((t for t in tags if t=='py3-none-any' or t=='cp312-cp312-win_amd64'),None)
                if not tag:
                    continue
                filename=name.replace('-','_')+'-'+info['Version']+'-'+tag+'.whl'
                shutil.copyfile(body,wheels/filename)
                selected[name]={'file':filename,'sha256':hashlib.sha256(body.read_bytes()).hexdigest()}
        except (OSError,ValueError,KeyError,BadZipFile):
            continue
    report['cached_wheels']=selected
    report['missing_wheels']=sorted(set(pins)-set(selected))
    save()
    if report['missing_wheels']:
        raise RuntimeError('Missing approved offline wheels; no network fallback')
    run('create_venv',[sys.executable,'-m','venv',str(workspace/'backend/.venv312')])
    python=str(workspace/'backend/.venv312/Scripts/python.exe')
    run('install_python',[python,'-m','pip','install','--no-index','--find-links',str(wheels),'-r','requirements-installed-py312.txt'],workspace/'backend')
    npm=shutil.which('npm.cmd')
    if not npm:
        raise RuntimeError('Installed npm.cmd required')
    lock=json.loads((workspace/'frontend/package-lock.json').read_text(encoding='utf-8'))
    if any(p.get('resolved') and not p['resolved'].startswith('https://registry.npmjs.org/') for p in lock['packages'].values()):
        raise RuntimeError('Only the approved npm registry lock is supported')
    mode=['--offline=false','--prefer-offline'] if args.allow_locked_downloads else ['--offline']
    run('install_frontend',[npm,'ci',*mode,'--ignore-scripts','--no-audit','--no-fund'],workspace/'frontend')
    run('fresh_local_ci',[python,'-B','scripts/check_local_ci.py'])
    run('fresh_postgres',[python,'-B','check_local_dashboard.py'],workspace/'backend')
    run('fresh_frontend_build',[shutil.which('node'), 'scripts/next-local.mjs','build'],workspace/'frontend',360)
    report['completed']=True
    report['completed_at']=datetime.now(timezone.utc).isoformat()
    save()
    print('Fresh setup complete; all files and database retained',flush=True)


if __name__=='__main__':
    main()
