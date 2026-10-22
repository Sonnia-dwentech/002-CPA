# B024 — Local staging rehearsal evidence

Date: 21 October 2026 (client date; Atlantic/Reykjavik). **Done for the user-selected local rehearsal scope; approved 21 October 2026.**

## Authority and boundary

User selected “Start B024”, then explicitly chose “Keep it local: build and verify a separate staging rehearsal”. This replaces hosted deployment with a local rehearsal for this task. The original hosted environment, account/budget/identity, GitHub/RCI-01 and independent-review requirements remain deferred. No cloud service, provider account, remote repository, purchase or system certificate-trust installation occurred. B025 remains unstarted.

## Delivered and running

[Operating guide](../../deployments/local-rehearsal/README.md), [runtime metadata](B024-runtime.json) and [executed check results](B024-local-rehearsal-checks.json).

- Separate production Next.js build from frontend/rehearsal, served internally at 127.0.0.1:3200.
- Explicit local HTTPS application at https://127.0.0.1:3443: synthetic session issuance, secure cookie, B021 dashboard queries, direct record authorization and readiness. Normal app.main still has its original scope.
- Separate PostgreSQL database cpa_b024, runtime credential, privileged bootstrap/migration credential, retained named container and persistent named volume.
- New local CA/leaf certificate generated offline using installed cryptography. Tests validate certificate chain and hostname using the explicit CA. Default system trust correctly rejects it; browser trust remains user-controlled, and no browser warning was bypassed.
- Private key and database secrets saved under a user-only Windows ACL directory beneath .local/b024; root .gitignore now excludes private runtime state and environment files. No Git command executed. CA signing private key is not persisted.
- Actual database/environment boundaries are enforced by loopback binds and exact host/origin checks. Runtime cannot perform DDL, membership changes or reference deletion. Existing session locking needs UPDATE(id) on cpa.users; record reads/permissions are enforced by the existing backend policy, not database row-level security.

## Executed checks

All six real rehearsal groups passed:

1. New PostgreSQL database, migrations and four synthetic records survive container restart on a named volume; migrations reapply as a no-op.
2. Distinct cpa_runtime role rejects schema creation, membership edits and reference deletion.
3. Production build, HTML and JavaScript asset delivery through TLS with explicit CA and hostname validation; default trust rejects the private CA.
4. Liveness versus database readiness; Secure/HttpOnly/SameSite=Strict host-only cookie; exact Origin/Host enforcement; anonymous access and unauthorized POST rejected.
5. Stored dashboard count/list/filter checks, honest zero and unavailable distinction; direct access to hidden record returns 404; spoofed Bearer and duplicate cookies rejected.
6. Actual database-table failure makes readiness/query return 503 without counts or SQL details; restoring the table recovers both; sign-out revokes the session and replay returns 401.

Full local runner exited 0 after the final implementation: 68 source/config files; dependency pins/consistency; 68 backend tests; 5 runner tests; dashboard contract cases; normal frontend, B016/B022 harness and B024 rehearsal TypeScript checks. Rehearsal frontend production build succeeded. Tests use synthetic users/references only; no real identity or client data.

Original B022 preview independently returned HTTP 200 at 127.0.0.1:3100/dashboard after completion. Its database/container was not stopped, renamed or reused.

## Failures found and fixed

First rehearsal attempt could not reconnect after its container restart. Docker assigned a new loopback port; the launcher now rediscovers the mapping and updates private connection state. Added --resume to operate on the exact recorded B024-labelled container instead of creating replacement databases. Restart/persistence checks then passed on the same retained container.

Production build succeeded but saving its output hit a Windows character-encoding error. Build-log writing now specifies UTF-8. Explicit --reuse-build reused the successful artifact in the final check; frontend sources were unchanged between build and verification. The actual build identifier is recorded in B024-runtime.json. No failed attempt's data was discarded. The --serve verification remains running, so a completed-process exit code is not claimed for it; passing groups were emitted and persisted before the service hold loop.

## Retention and limits

The loopback HTTPS endpoint is running, but browsers do not automatically trust its private CA. No browser-rendered end-to-end HTTPS claim is made: production HTML/assets and HTTPS API journey were checked programmatically with certificate verification; the reused dashboard's browser behavior was verified at B022. A browser trust installation or warning bypass is not performed here.

PostgreSQL host traffic remains local loopback, not a validated hosted database TLS setup. The migration/bootstrap role is privileged; hosted least-privilege migration design remains deferred. The frontend build uses this Windows workstation; cross-platform cloud packaging is not established. A container restart tests persistence, not B025 backup restoration. Certificate expiry is seven days; renewal is not automatic.

The running frontend/HTTPS processes, protected secrets, container and volume are retained. Creating the private stop marker ends preview processes only when requested; it does not delete data or stop the database. No automatic cleanup or schedule added. Use the operating guide for controlled resume. B024 local scope is accepted; B025 has not started. Pre-change records: B024-before.zip.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.
