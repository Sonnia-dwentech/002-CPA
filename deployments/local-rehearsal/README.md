# B024 — Local staging rehearsal

User-selected scope: “Keep it local: build and verify a separate staging rehearsal.” This is a local synthetic rehearsal, not hosted staging, real identity verification or production deployment. The original cloud/GitHub requirements remain deferred. Existing B022 services and data are not reused.

## What runs

- Production-mode Next.js frontend from `frontend/rehearsal`, bound to 127.0.0.1:3200. A separate build directory preserves B022 and normal frontend builds.
- HTTPS FastAPI gateway at https://127.0.0.1:3443. It serves the production frontend through loopback and implements only the explicit synthetic rehearsal session/dashboard routes. Normal `app.main` stays disconnected.
- A separately named PostgreSQL container and named persistent volume. Credentials, database name and role differ from B022. Actual names and non-secret state paths are in [runtime record](../../docs/evidence/B024-runtime.json).
- Runtime role has table SELECT, session INSERT/UPDATE and users.id column UPDATE needed by existing SessionStore row locks. It cannot create schema objects, modify membership or delete reference rows. Migration/bootstrap role remains privileged and separate; this is a local minimum tested boundary, not a completed hosted database-role design.
- Live AI, workers, cloud storage and external identity remain disabled. The sign-in endpoint issues only the fixed synthetic owner identity, never a caller-selected account.

## HTTPS and access

The launcher generates a seven-day local CA and certificate for 127.0.0.1/localhost using already-installed cryptography. Tests use that CA explicitly with hostname verification enabled. No certificate validation bypass is used and no certificate is installed into Windows/browser trust stores. A browser may show a trust warning for this private CA; browser trust setup is a separate user-controlled action. The internal HTTP frontend at port 3200 has no API/session handlers and cannot perform the authenticated dashboard journey by itself.

All services bind to loopback. Exact Host and Origin checks plus cross-site denial protect the HTTPS gateway; cookies are Secure, HttpOnly, SameSite=Strict and host-only. API permissions remain enforced independently of the dashboard. The PostgreSQL host connection is loopback-only, not a validated remote-TLS database configuration.

`/health` is liveness only. `/ready` verifies the expected database/runtime role, migration count and required tables. Failure must return 503; a matching process-health response alone does not make the rehearsal ready.

## Secrets and retained data

Private state lives under `.local/b024/<run-id>/`, whose Windows ACL is restricted to the launching user before secret files are written. No credential values appear in evidence or command arguments. A new root .gitignore excludes local state, private environment files and build/dependency caches; no Git command was run. The CA signing private key is not saved. The server TLS key and database credentials remain in the protected directory for the retained rehearsal.

The database uses a named volume, not tmpfs. The verification restarts only this new container and checks records/migrations survive. Docker can reassign a dynamic loopback port on restart; the launcher rediscovers and stores the current port. No container or volume is automatically deleted. Owner: Justice (existing nomination). Retention/deletion trigger: explicit user instruction. This local retention preference is not a hosted-data retention policy.

## Run or resume

The launcher requires the existing Docker PostgreSQL 17 image, installed Node/Next native compiler, project Python environment and an existing Python interpreter with cryptography. It downloads nothing. The latest run's certificate interpreter path is recorded in the execution evidence rather than selecting a new package source.

From `backend`, use the project virtual environment to run `run_local_rehearsal.py --certificate-python <existing-python-with-cryptography> --serve`. A new invocation without `--resume` creates a new retained rehearsal; do not run it again just to reconnect.

Use `--resume` with the same options to reopen the exact container recorded in B024-runtime.json. It validates the B024 label and expected credential scope, checks migrations, repeats the restart verification and rebuilds the production frontend. Do not resume while the existing services still occupy 3200/3443. The resume option is a controlled rehearsal verification restart, not a zero-downtime operator command. Certificate expiry requires a separately reviewed renewal; the launcher does not silently trust or replace certificates.

With --serve, the process stays active. Creating a file named `stop` in the recorded private state directory ends only the frontend/HTTPS processes. Database and volume stay running/retained. Do not create that marker unless the user requests stopping. Runtime errors also preserve database/volume and private state for diagnosis.

## Verification and remaining boundaries

[Execution evidence](../../docs/evidence/B024-local-rehearsal.md) and [machine-readable checks](../../docs/evidence/B024-local-rehearsal-checks.json) record observed results. Hosted deployment, real identity/MFA, independent review, provider portability, remote CI, cloud budget/ownership and production readiness are not established by this rehearsal. B025 backup/restore remains a separate selected task; a container restart is not a backup restoration test.


### Verified artifact reuse

`--reuse-build` skips building and requires an existing rehearsal .next/BUILD_ID. Use only for a reviewed build when frontend sources have not changed; otherwise rebuild. This recovered a successful build after a Windows log-encoding failure without replacing any database. The launcher records the build ID and reruns HTTPS/data checks; it does not automatically attest source-to-artifact equivalence.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.


## B025 local recovery

The [recovery runbook](recovery.md) records the verified manual backup and isolated restore procedure, retained state and migration/application rollback boundaries. Eight recovery/control groups and the full local check runner passed. B025 is approved and Done for local recovery; B026 remains unstarted. Backup and restored database are retained; no cleanup performed.


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.


## B027 current setup and support handover

Use the [current setup guide](../../docs/local-setup.md) for the delivered Windows foundation, isolated setup, alternate rehearsal ports and safe operational logs. B027 local checks passed and the verified local scope is approved and Done; spoken screen-reader verification remains outstanding. The additional B027 rehearsal runs at https://127.0.0.1:3543, with separate persistent data and protected redacted logs. Original services and all resources remain retained. B028 unstarted.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.
