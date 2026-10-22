# B018 — Local AI adapter implementation and evidence

Date: 21 October 2026 (America/Los_Angeles). Status: Done; user approved and accepted the local scope on 21 October 2026.

User authority: “Start B018”. Codex executed the local definition and synthetic testing scope under G0-L, following accepted B017. Justice remains the nominated accountable owner; independent review has not been recorded.

## Delivered

- [Adapter and versioned contracts](../../backend/app/ai_adapter.py).
- [Synthetic provider fixtures and tests](../../backend/tests/test_ai_adapter.py).
- [Contract, limits and deferred decisions](../planning/B018-local-ai-contract.md).
- [Pre-change records](B018-before.zip), preserving progress, decisions, root/backend READMEs and Phase 1 work-item pack.

The four build-order outcomes are covered: validated draft success, timeout, refusal and malformed output. Tests also exercise a real asynchronous deadline and provider cancellation, safe exception handling, strict token counts, unknown usage/cost, duplicate/extra fields, provenance/version validation, input validation, no automatic retry/fallback, synthetic-canary exclusion and human-approval separation. Network connection calls are mocked to fail in the primary outcome test and asserted unused.

## Actual verification

From the current project's `backend` folder:

```powershell
& 'C:\Python315\python.exe' -B -m unittest tests.test_ai_adapter -v
```

Result: **15 tests passed**, exit code 0. No packages were installed. Runtime: installed Python 3.15. The new module depends only on the Python standard library and is not wired into the normal application.

The initial `python --version` command failed because `python` resolves to an unusable Windows Store alias. `py -0p` located `C:\Python315\python.exe`. Read-only package detection found FastAPI, Uvicorn and psycopg absent in that runtime. Therefore the existing 27 backend tests and PostgreSQL checks were **not rerun** here; prior B017 results remain historical evidence. No full-stack compatibility claim is made for this computer. This is a verification limitation for review, not a hidden passing result.

## Boundaries and handoff

No live provider, credentials, network requests, API route, database migration, persistent audit events, frontend changes or environment configuration were added. Original sources and existing application code were preserved. There is no inference of Justice acceptance, independent review, deployment approval or full F06 completion. Local contract choices remain reviewable.

B018 awaits acceptance. B019 remains Not started. Restore of missing backend dependencies/fresh setup belongs to separately selected setup work; no download or install was attempted.


### Dependency installation follow-up — 21 October 2026

User explicitly requested Python dependency installation. Network installation was authorised for this local setup. Python 3.15 lacked a wheel for pinned pydantic-core; existing bundled Python 3.12.14 was used in `backend/.venv312`. Original direct pins were preserved, with `psycopg-binary==3.3.6` added for Windows libpq support. Installed versions are saved in `backend/requirements-installed-py312.txt`. All 42 backend tests passed and pip check found no broken requirements. This supersedes the earlier missing-dependency regression limitation for this environment. PostgreSQL integration checks were not rerun. B018 acceptance and B019 selection remain pending; live-provider and deployment boundaries are unchanged.


## Local acceptance — 21 October 2026

User: “Approve and accept B018”. The local adapter contract and verified implementation are accepted; B018 is Done. This supersedes earlier pending-acceptance wording. Evidence retained: 42 backend tests passed, including 15 adapter tests, and clean pip check. No tests were rerun for this documentation-only update. PostgreSQL integration, full F06 delivery, live provider/model/budget configuration, formal independent review and deployment remain outside this acceptance. B019 remains Not started. Prior records are preserved in [B018-before-acceptance.zip](B018-before-acceptance.zip).
