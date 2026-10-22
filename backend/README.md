# CPA Local Foundation API — B011

## B019 local configuration and usage controls

`app/ai_controls.py` wraps the B018 mock adapter with explicit configuration
validation and ephemeral usage records. Live requests always stop before the
adapter, including with complete settings. Unknown cost remains unknown.
See [B019 evidence and contract](../docs/evidence/B019-local-ai-controls.md).
The normal HTTP application does not load or expose this harness. Latest
verification: **54 backend tests passed**, including 12 B019 tests. No new
dependencies, actual budget policy, persistent usage store or live calls.

## Current workstation setup — 21 October 2026

The user authorised dependency installation. The working environment is now
`backend/.venv312`, using locally bundled Python 3.12.14. All original direct
dependency pins are preserved; `psycopg-binary==3.3.6` supplies the Windows libpq
runtime. [Installed versions](requirements-installed-py312.txt) capture all
resolved packages. Python 3.15 could not install the pinned Pydantic core wheel;
the earlier `backend/.venv` is unused. Older runtime/path notes below are historical.

From `C:\Users\Win11\Documents\002 CPA\backend`:

```powershell
.\.venv312\Scripts\python.exe -B run_local.py
.\.venv312\Scripts\python.exe -B -m unittest discover -s tests -v
.\.venv312\Scripts\python.exe -m pip check
```

Verification: all **42 tests passed**, including loopback startup/shutdown and
the 15 B018 adapter tests; `pip check` found no broken requirements. PostgreSQL
integration checks were not rerun. No server was left running by the tests.

This is a minimal local FastAPI application, not the completed CPA backend.
It uses the already-installed Python 3.14.8 environment; no packages were installed
or downloaded for B011. See [requirements-local.txt](requirements-local.txt) for
the observed direct/framework versions exercised by the tests. This is not a
complete dependency lock or proof of a clean-machine installation.

## Run locally

In PowerShell:

```powershell
Set-Location -LiteralPath 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B run_local.py
```

The launcher binds only to `127.0.0.1:8000`. Stop it with Ctrl+C.
If that port is occupied, select another local port:

```powershell
python -B run_local.py --port 8001
```

In a second PowerShell terminal:

```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/health'
Invoke-RestMethod -Uri 'http://127.0.0.1:8000/openapi.json'
```

These requests use loopback only. They do not connect to GitHub or an external
provider. No service is left running by the test suite.

## Contract

| Request | Result |
| --- | --- |
| `GET /health` | HTTP 200, `{"status":"ok"}`, `Cache-Control: no-store` |
| `GET /openapi.json` | Generated local API schema; no external documentation assets |
| Unknown route | HTTP 404, generic `not_found` error |
| Unsupported method on `/health` | HTTP 405, generic error and `Allow` header |
| Invalid validated request | HTTP 422, generic `validation_error`; no submitted values echoed |
| Unexpected application exception | HTTP 500, generic `internal_error`; no exception text returned |

Error body:

```json
{"error":{"code":"not_found","message":"Resource not found."}}
```

The health check means **process liveness only**. It does not check or claim database,
identity, provider, migration, deployment or overall product readiness. The app has
no business-data routes. Validation and exception behaviour is tested through
test-only routes added to isolated app instances; those routes are not exposed by
the actual application or its OpenAPI schema.

Browser `/docs` and `/redoc` are disabled, so viewing a schema does not require CDN
assets. Debug mode is off. The local launcher disables access logging, proxy-header
trust and the server-version header. It uses critical-only server logging to avoid
printing raw request/exception details. Proper redacted operational logging is
still B017 work; this launcher is not a production logging/deployment design.

The app does not load `.env`, connect to a database, initialise credentials or call
a model. Existing configuration templates remain future configuration guidance,
not active protection mechanisms. No authentication or CORS policy is implemented;
keep this process local and do not expose it through public tunnels or deployment.

## Verify

```powershell
Set-Location -LiteralPath 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B -m unittest discover -s tests -v
```

Tests use Python's standard-library runner, direct ASGI requests and a short-lived
loopback server. No pytest/httpx installation is needed. The startup test chooses
an available local port, starts the actual launcher without a visible child
console, checks the health response and stops the child in a cleanup block.
All inputs and secret canaries are synthetic.

This provides B011 component startup/health/error evidence, not B010's deferred
complete fresh-setup walkthrough. B012 now has a separately authorised disposable PostgreSQL check workflow below. B005's formal technical review and other G0-L deferrals remain
outstanding. See [B011 evidence](../docs/evidence/B011-local-api.md) and
[current progress](../progress.md) for actual acceptance status.


## B012 disposable PostgreSQL migration checks

The user lifted the setup deferral for this local scope on 20 October 2026. Uses installed psycopg 3.3.6 and an existing Docker `postgres:17` image. No downloads or installs are performed. Start the installed Docker Desktop engine first if stopped; this may require local permissions.

```powershell
Set-Location -LiteralPath 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B check_local_database.py
```

The script targets only the local Windows Docker named pipe, inspects the existing image and runs its immutable ID with `--pull=never`. Each invocation creates a uniquely named container, ephemeral loopback port, random password passed through the child environment, and tmpfs storage. The script never selects an existing database/container. Credentials are not saved in source or printed. It stops/removes its test container in cleanup; Docker Desktop itself remains running.

`app/database.py` supplies local connectivity and an atomic batch migration runner with transaction-scoped advisory locking, a history-prefix check and SHA-256 checksums. Ordered SQL files live in `migrations/`. The first migration creates only the empty `cpa` namespace; bookkeeping lives in `cpa_meta.schema_migrations`. Do not edit applied migrations. Add transaction-compatible SQL in a new numbered file; transaction control and nontransactional DDL are outside this runner's supported contract.

The checks demonstrate rollback on constraint failure, recovery by correcting an unapplied migration, preservation of synthetic data after transaction failure, and an explicit test-only rollback to the baseline. They do not prove backup/restore or production disaster recovery. Destructive down-migrations need their own data-loss assessment; there is no automatic general rollback command.

Fixture manifest: `B012-synthetic-probe`, version 1, created by Codex for this task; entirely invented integer pair `(1, 7)` in `cpa.recovery_probe`, temporary test migration 0002. Owner is the B012 executor. Storage is only the generated container's tmpfs; cleanup occurs at the end of each run, with the fixture removed earlier by the tested rollback. Expected outcomes are defined in the script and [B012 evidence](../docs/evidence/B012-local-database.md).

The generated PostgreSQL bootstrap role is privileged solely inside this disposable instance. It is not an approved application runtime role or evidence of least-privilege access. B013/B014 still need user/role/tenancy/session decisions; the API's public health remains liveness-only. No persistent development database or application-wide database readiness is claimed.


## B013 local identity and permission boundary

User approved matrix v0.1 for local continuation on 20 October 2026. `0002_identity_access_references.sql` adds reference metadata for users, client organisations, roles, record scope, grants and case assignments. It creates no accounts or business payloads. Applied migration 0001 is unchanged. The database check runner now discovers all migration files and uses temporary migration 9000 for its recovery fixture.

```powershell
Set-Location -LiteralPath 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B -m unittest discover -s tests -v
python -B check_local_access.py
```

The second command uses the installed offline Docker image and the B012 disposable-database mechanism; Docker named-pipe access may require local permissions. It creates a new `cpa-b013-check-<uuid>` container, runs migrations plus persisted permission checks, and removes the container/tmpfs. No real accounts or persistent store remain. The internal disposable database/user names remain `cpa_b012` for compatibility with the existing local connector; this is never an existing database selection.

`AccessStore.require()` checks current persisted identity, active membership, role/grants, record scope and case assignments. It returns authorised **internal reference metadata**, not a client-safe payload or a business workflow response. A future feature service must construct its approved projection, call this boundary for every access and keep its own content mutations atomic with authorisation. `visible()` returns filtered references; derive visible counts from that result. It is a correctness-first local implementation, not a measured large-dataset query plan.

All feature kinds are disabled by default. Tests explicitly enable synthetic kinds. Neither the normal application nor an environment flag enables a mock login or feature service. `VerifiedIdentity` is a server-only input contract for a future B014 validator; never construct it from request user/role/client fields. Authentication, session verification and endpoint wiring are not implemented by B013.

The evaluator handles the approved record actions, including separate read/edit/export/run/decision permissions and the independent response-author rule. There are no public account, grant or assignment mutation APIs: self-grants, bootstrap, invitations, role changes and account linking cannot be performed through the application. Named bootstrap and approval-backed administration remain prerequisites before real account operation. Policy decisions for future publication, research, exports and client flows do not activate those workflows or waive their later lifecycle gates.

Fixture manifest: `B013-synthetic-access`, version 1, creator/executor Codex; synthetic issuer `synthetic://b013`, nine invented users, two invented client organisations and eight reference records with UUIDs generated from fixed integers in the test script. No names, email addresses, credentials or business content originate from real users. Schema migrations 0001–0002. Expected positive and negative results are in `check_local_access.py`; storage is the new container's tmpfs, cleaned up after each run. Fixture grants are inserted directly by the isolated test harness, not through an unapproved administrator route.

B013 verifies application-layer reference isolation, not PostgreSQL row-level security or a least-privilege database role. The temporary bootstrap role is privileged and must never be used as a deployed application role. Permission checks run anew on every call; in-flight operations and future multi-step mutations need their own transaction/concurrency tests. MFA, session expiry, provider validation and named real-account assignments remain B014/approval work. No claim of complete client-portal or deployment readiness is made.


## B014 approved local session validation

Policy v0.1 is user-approved. Migration 0003 stores opaque-session SHA-256 digests, user references, activity/absolute-expiry timestamps and revocation. Prior migrations remain unchanged. Tokens use 32 random bytes; raw tokens are never saved in the session table. The validator enforces a 30-minute idle timeout and fixed 8-hour absolute lifetime using database UTC time, with equality treated as expired. Activity never renews absolute expiry, and there is no refresh mechanism.

```powershell
Set-Location -LiteralPath 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B -m unittest discover -s tests -v
python -B check_local_sessions.py
```

The integration command creates a fresh `cpa-b014-check-<uuid>` container from the installed image with pulling disabled, uses loopback only, runs migration/B013/session checks, starts and stops a short-lived HTTP test server, then removes the container/tmpfs. Docker named-pipe access may require local permissions. No credentials are printed and no provider is contacted. Docker Desktop itself remains running.

`app/sessions.py` implements the parser, validator, server-internal issuance helper, session logout and request dependencies. It accepts exactly one well-formed Bearer header; tokens in query strings/cookies and user/role/MFA headers confer no identity or assurance. Logout revokes only the presented session. A database trigger revokes sessions on account disablement, membership removal or identity/scope change, including when the account is restored before the next request.

Future protected routes must use `require_record()` (authentication plus B013 authorisation) or `authenticate()` followed by the appropriate approved policy, and use `require_privileged()` for privileged operations. Privileged operations remain denied because no MFA mechanism is configured. No caller-supplied flag can enable MFA. Database failure is generic 503; invalid credentials are generic 401 with `WWW-Authenticate: Bearer` and no-store. B013 record denial remains 403/404.

Connection stores must be supplied by trusted server wiring through request state, using a request-scoped connection lifecycle. Missing store wiring fails closed. The test harness wires its own database connection and test-only routes. The normal app still exposes only liveness/OpenAPI: no login, session minting, mock-auth toggle, account recovery, logout HTTP route or protected business feature has been enabled. The server-internal issuance helper can only be integrated after a future approved identity verification step. It is not evidence of a human sign-in.

Fixture manifest: `B014-synthetic-sessions`, version 1, Codex executor; reuses B013 synthetic baseline, then adds three invented users (one internal/two clients), three reference records and ephemeral random session tokens under issuer `synthetic://b014`. Schema 0001–0003. Expected outcomes are defined in `check_local_sessions.py` and `tests/test_sessions.py`. Data lives only in the generated tmpfs database; tokens live in test process memory; the whole instance is removed after the run. Test HTTP requests stay on loopback with access logging disabled; never reuse these test credentials in a real environment.

The complete command passes 33 verification groups (9 migration, 10 B013 reference/access, 14 session/HTTP), plus the separate 26-test unit/API suite. No real identity provider, password system, browser sign-in/storage, MFA verification or full sign-in journey has been demonstrated. B016 retains UI work. Request connection pooling, production roles/TLS, operational session-retention cleanup and deployed concurrency/load evidence remain future integration/operations requirements; local expiry is access denial, not a retention policy.


## Localhost status page

Opening `http://127.0.0.1:8000/` now displays a small backend status page with links to health and the API schema. `/health` intentionally remains JSON: `{"status":"ok"}`. The root page confirms that this process responds; it does not check database/provider readiness or provide the B015 frontend. No external assets are loaded. Added after the user's localhost 404 report; 27 unit/API tests passed, including the HTML route and existing security/session checks.


## B018 local AI contract — 21 October 2026

`app/ai_adapter.py` provides the isolated mock-only async interface and strict synthetic draft schema. See the [contract](../docs/planning/B018-local-ai-contract.md) and [evidence](../docs/evidence/B018-local-ai-adapter.md). It is not connected to HTTP, credentials or persistence. No live provider is implemented. From this folder, run `& 'C:\Python315\python.exe' -B -m unittest tests.test_ai_adapter -v` on the current workstation. Fifteen tests passed. The earlier machine paths and dependency inventory above are historical: the current Python 3.15 runtime lacks FastAPI/Uvicorn/psycopg, so existing backend tests were not rerun.


B021 `app/dashboard.py` adds the approved synthetic reference count/list service with strict filters and B013 permissions. All 68 backend tests pass. `check_local_dashboard.py` is the prepared disposable PostgreSQL harness, not yet executed because Docker is absent. See [B021 evidence](../docs/evidence/B021-local-dashboard.md) before claiming database verification. No normal HTTP route is added.


Current B021 update — 21 October 2026: actual PostgreSQL 17.11 verification passed all 15 harness checks after Docker recovery and approved image download; full local checks passed. Earlier unavailable-runtime statements are historical. B021 is approved and Done for local scope; B022 unstarted. The test container was already removed before the user requested no cleanup; retain future test containers and adjust the automatic-cleanup harness before reuse. See the B021 evidence and progress tracker.


## B021 local deliverable approved — 21 October 2026

User: “Approve B021”. B021 is Done for the verified local synthetic-reference dashboard queries and filters. Existing 68 backend tests, 15 actual PostgreSQL checks and full local check runner passed; no tests rerun for this documentation-only acceptance. Earlier blocked/pending-acceptance wording is historical and superseded. B022 remains unstarted. Business metrics and frontend/API exposure remain outside this accepted scope; GitHub/RCI-01 remains deferred. Retain future test containers unless the user asks otherwise and keep approvals in chat. Pre-approval records: docs/evidence/B021-before-acceptance.zip.


## B022 local dashboard preview

B022 is approved and Done for verified local synthetic reference metadata. Preview: http://127.0.0.1:3100/dashboard. It connects the isolated session harness to B021 stored queries; the normal app stays disconnected. Evidence: docs/evidence/B022-local-dashboard-ui.md (project root). The retained container and preview remain running by user preference. Future database checks retain containers by default; tmpfs contents are not durable across container stop/reboot. The B022-stop marker ends preview servers only when requested. B023 has not started.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.


## B024 separate local rehearsal

The user selected a local staging rehearsal; it is approved and Done for the verified local scope. HTTPS endpoint: https://127.0.0.1:3443, with separate production frontend and persistent PostgreSQL volume. The private CA was validated explicitly in tests; browser/system trust was not modified. Existing B022 preview/data remain untouched. See deployments/local-rehearsal/README.md and docs/evidence/B024-local-rehearsal.md from project root for operation, scope and retained-state details. Cloud deployment and B025 remain unstarted.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.


## B025 local recovery

The [recovery runbook](../deployments/local-rehearsal/recovery.md) records the verified manual backup and isolated restore procedure, retained state and migration/application rollback boundaries. Eight recovery/control groups and the full local check runner passed. B025 is approved and Done for local recovery; B026 remains unstarted. Backup and restored database are retained; no cleanup performed.


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.


## B027 current setup and support handover

Use the [current setup guide](../docs/local-setup.md) for the delivered Windows foundation, isolated setup, alternate rehearsal ports and safe operational logs. B027 local checks passed and the verified local scope is approved and Done; spoken screen-reader verification remains outstanding. The additional B027 rehearsal runs at https://127.0.0.1:3543, with separate persistent data and protected redacted logs. Original services and all resources remain retained. B028 unstarted.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.
