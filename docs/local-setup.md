# Windows local foundation setup — B027

This guide covers the delivered local foundation on Windows x64. The project is `C:\Users\Win11\Documents\002 CPA`. The earlier B010 guide is preserved in `docs/evidence/B027-before.zip`; its old paths and deferred-install notes are historical.

## Existing working environment

Use PowerShell from the project root. These commands invoke executables directly; no PowerShell execution-policy change is needed.

```powershell
Set-Location -LiteralPath 'C:\Users\Win11\Documents\002 CPA'
.\backend\.venv312\Scripts\python.exe -B scripts/check_local_ci.py
```

The verified runtime is Python 3.12.14 in `backend/.venv312`, Node 24.22.0 and npm 11.19.1. `backend/requirements-installed-py312.txt` pins all 17 Python distributions; `frontend/package-lock.json` pins the frontend dependency graph and integrity checks. The source/config scan, dependency consistency, backend/runner tests, dashboard contract and three TypeScript checks must pass. Earlier backend README test counts describe earlier milestones.

The normal shell starts with `node scripts/next-local.mjs dev` **from frontend**, binding only port 3000. From the project root use:

```powershell
Set-Location -LiteralPath 'C:\Users\Win11\Documents\002 CPA\frontend'
& 'C:\Program Files\nodejs\node.exe' scripts/next-local.mjs dev
```

The normal API is started from backend with `.\.venv312\Scripts\python.exe -B run_local.py`, binding 127.0.0.1:8000. It exposes liveness, not the connected synthetic application. Do not start another process on an occupied port or stop an existing service to take its port.

## Connected previews and database

- Main Command Centre and connected synthetic reference dashboard: http://127.0.0.1:3000 and http://127.0.0.1:3000/dashboard. Same-origin API/session handling depends on the retained B027 HTTPS service at 3543 and its scoped exported public CA; [connection guide](evidence/main-dashboard-connection.md).
- B022 synthetic browser harness: http://127.0.0.1:3100/dashboard, separate backend 8100 and retained test database. The launcher is `backend/check_local_dashboard_ui.py --serve`; it requires free 3100/8100 and creates a new retained test database. Do not run it merely to reconnect to the current preview.
- B024 production-mode local HTTPS rehearsal: https://127.0.0.1:3443, internal frontend 3200, separate persistent PostgreSQL container/volume. [Operating guide](../deployments/local-rehearsal/README.md). Browser trust is not installed; programmatic checks use its explicit private CA with hostname verification. Do not bypass a browser warning.
- B025 backup/restore resources stay separate. [Recovery runbook](../deployments/local-rehearsal/recovery.md).

No private `.env` is required by these explicit harnesses. Root `.env.example` remains a placeholder, not runtime configuration. Live AI, cloud services, real identity and client data remain disabled/deferred. Do not print `.local` credential/key files or process environments.

Docker Desktop Linux engine must be running and the already-installed PostgreSQL 17 image available. The helper uses the explicit named pipe and an immutable inspected image with `--pull=never`. Add the installed CLI to this PowerShell session if needed:

```powershell
$env:PATH='C:\Program Files\Docker\Docker\resources\bin;'+$env:PATH
```

## Fresh isolated walkthrough

The runner copies active source into a new UUID folder under `.local/b027`, excluding existing dependency installs, builds, runtime state and logs. It preserves the working installs and earlier attempts.

```powershell
Set-Location -LiteralPath 'C:\Users\Win11\Documents\002 CPA'
.\backend\.venv312\Scripts\python.exe -B scripts/check_fresh_local_setup.py
```

It recreates approved wheels from this workstation's pip HTTP cache, records hashes, creates a new virtual environment and installs Python pins using `--no-index`. It then runs `npm ci --offline --ignore-scripts --no-audit --no-fund`, the full local suite, a separate retained PostgreSQL migration/dashboard check and a production frontend build. A cache miss stops the run without online fallback. This is a clean dependency install from a source copy on the same workstation, not a clean OS or cross-platform certification. Python wheel hashes record the used local inputs; no independent package provenance review is implied.

B027's initial frontend install stopped on missing locked npm packages. The user explicitly approved exact locked package downloads on 21 October 2026. For that approved run only:

```powershell
.\backend\.venv312\Scripts\python.exe -B scripts/check_fresh_local_setup.py --allow-locked-downloads
```

That option permits npm's exact lock resolution from `registry.npmjs.org`, retains lock integrity verification and disables lifecycle scripts, audit/funding requests and telemetry. Python remains offline. No package versions or lockfile are upgraded. Fresh folders and output logs are retained. A failed setup can be resumed after a reviewed runner correction with `--resume-run <recorded-32-character-ID>`; it preserves successful installs and skips previously successful steps. It is not a general source-refresh mechanism. Review `docs/evidence/B027-setup-checks.json` for the actual outcome rather than treating the command's existence as success.

## Isolated integrated rehearsal after setup

Use the successfully copied workspace recorded in the results, not the main project's metadata. From its backend directory, run the copied launcher with free alternate ports:

```powershell
.\.venv312\Scripts\python.exe -B run_local_rehearsal.py --frontend-port 3300 --https-port 3543 --certificate-python 'C:\Users\Win11\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' --serve
```

It generates separate protected credentials/TLS material, creates a fresh named persistent volume, applies migrations, seeds wholly synthetic references and builds the rehearsal frontend from the fresh dependencies. Six HTTPS/database/access/failure checks must pass before it holds the new service open. It records its own container, build, endpoints and protected state path in the copied workspace's `docs/evidence/B024-runtime.json`. The main B024/B025 records and services stay separate. Default-port callers are unchanged by the new alternate-port options.

## Operational logs and diagnosis

The updated rehearsal launcher explicitly wires the existing `OperationalCapture` middleware to `operational.jsonl` under its protected state directory; the path is in that run's runtime metadata. Each line contains only `request_id`, an allowlisted route name (or `unmatched`), normalized method, HTTP status and nonnegative duration_ms. It does not capture raw paths, queries, request bodies, headers, cookies, tokens, SQL or exception messages. Proxy requests have no per-user request content in the log. Framework access/exception output remains disabled. A random request ID distinguishes events; it is not yet propagated to the response/client, so client-to-server correlation is a documented limitation.

Use statuses to distinguish anonymous 401, boundary 403, unknown/hidden 404, invalid input 422 and unavailable 503. `/health` is process liveness; `/ready` also checks the expected database/runtime identity, migrations and required tables. Never diagnose a database outage from health alone. The controlled table-rename fault exists only inside the isolated verification launcher, with restoration in finally; do not manually repeat it against retained previews.

Existing B024 was launched before this new capture wiring and is not restarted automatically. Do not claim its historical access events can be recovered. Frontend build/start logs exist in the protected directory, but they are not an HTTP audit trail. These logs are local operational support evidence, not completed production monitoring or the separate B017 audit-event contract.

## Retention and handover

Retain all created containers, volumes, setup folders, certificates and backups until the user's explicit cleanup request. A service's documented stop marker ends only that launcher's preview processes; use it only when requested. Test helpers may stop their own short-lived verification processes after checks; that is distinct from deleting retained state. No cleanup command is part of this guide.

For local review, use [B027 evidence](evidence/B027-accessibility-setup.md), [B026 verification](evidence/B026-local-foundation.md) and progress.md. Hosted staging logs, a human spoken screen-reader walkthrough, independent review and G1 sign-offs need separate evidence. B028 is not automatically started by setup completion.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.


## Adopted local foundation boundary

G1-L v0.1 is adopted and B028 Done for local scope only; see [reassessment](evidence/B028-g1-local-adoption.md). Full G1 remains Hold with every review/operational/accessibility deferral preserved. B029 unstarted. No runtime, service, data or cleanup change accompanied this documentation-only adoption.


## Main dashboard connection — subsequent user request

The user authorised connecting the reference dashboard inside the normal frontend. /api/reference accepts only dashboard/session actions and uses verified HTTPS to the existing B027 rehearsal at 3543. Public certificate configuration is deployments/local-rehearsal/reference-dashboard-ca.pem; it is a public CA certificate, not a secret or a Windows trust-store installation. Keep the exact rehearsal running and its certificate valid; on outage/expiry the dashboard returns unavailable. Do not weaken TLS or reseed a replacement database to recover it. Loopback HTTP cookies are host-only, HttpOnly/SameSite=Strict, path /api/reference; hosted identity/TLS/session work remains deferred. Historical standalone/disconnected-main statements are superseded only for this explicit local connection. No packages or new database created; all resources retained.
