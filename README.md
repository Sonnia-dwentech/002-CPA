# CPA — Local Working Project

## Local check runner — B020 preparation

From this project root, run
`.\backend\.venv312\Scripts\python.exe -B scripts/check_local_ci.py`.
The local checks pass, including backend/runner tests and both frontend type
checks. [Coverage and evidence](docs/evidence/B020-local-checks.md) explain the
limited syntax/secret/dependency checks. B020 is approved and Done under the user-approved
local-only scope. GitHub remains deferred; [RCI-01](docs/planning/remote-ci-handoff.md)
retains required remote CI and merge verification before remote collaboration/merge or release.

**Organisation:** Dwen Tech Ltd  
**Classification:** Confidential — Internal  
**Project:** Chief Product Architect AI Laboratory

This is the user-selected local CPA project. It currently contains source material, planning documents, a connected local synthetic reference dashboard and verification evidence. A minimal local foundation API is present; no complete product or verified remote checkout is established by this folder.

## Start here

1. Read [progress.md](progress.md) for current task status, authorisation and handoff.
2. Read [build-order.md](build-order.md) for task definitions, dependencies and gate boundaries.
3. Consult [decisions.md](decisions.md) and [risks.md](risks.md) before resolving design questions or starting affected work.
4. Use the [documentation index](docs/README.md) for source documents, ADRs, policy and evidence; use [project layout](docs/project-layout.md) to distinguish existing files from proposed future application paths.

Product context is in [blueprint.md](blueprint.md); behaviour and acceptance criteria are in [feature-spec.md](feature-spec.md). Document existence does not establish implementation or technical approval.

## Current working boundary

[G0-L v0.1](docs/planning/G0-local-only-proposal.md) was adopted and [reassessed](docs/evidence/B008-g0-local-reassessment.md) for separately selected local work. All GitHub connections, remote operations, live services, real-client data and deployment remain deferred. Task-specific decisions still apply; no blanket Phase 1 execution authority is implied. Current statuses belong in progress.md.

Preserve the original handover folder, Word documents, archive and UI reference. Original pack instructions describe an earlier proposed remote workflow; the user's current local-only instruction governs this project. Do not interpret original GitHub/Render setup text as authority to connect or provision services.

Justice is the user-nominated interim accountable implementation owner and product/scope approver. Codex may execute selected local tasks; this does not establish Justice's personal acceptance or independent human review. Refer to the ledgers for actual approval evidence.

## Setup and execution

[B010 local setup preparation](docs/local-setup.md) records provisional tooling and deferred fresh-setup verification. [Backend instructions](backend/README.md) cover the loopback API on port 8000; accepted B012–B014 evidence covers disposable local PostgreSQL, access boundaries and synthetic sessions.

The frontend uses http://127.0.0.1:3000/ when started. [Frontend instructions](frontend/README.md) cover the B015 responsive navigation shell, cache-only dependencies and run/build commands. B016's isolated synthetic browser integration and B017's local audit scope are accepted. B018's [mock AI adapter](docs/evidence/B018-local-ai-adapter.md) is approved and accepted, with 15 adapter tests and all 42 backend tests passing. Real sign-in and application data remain unconnected. Fresh isolated setup is reserved for B027 before G1.

On the current workstation (`C:\Users\Win11\Documents\002 CPA`), the user subsequently authorised Python dependency installation. The working environment is `backend/.venv312` (Python 3.12.14), with original dependency pins and Windows psycopg binary support. All 42 backend tests pass and `pip check` is clean. See the [backend guide](backend/README.md) for commands. Earlier machine paths/tool inventories and missing-package observations are historical. PostgreSQL integration checks have not been rerun in this session.

Use the [allowed-data and test-fixture policy](docs/policies/allowed-data-and-test-fixtures.md) before future test-data work. Local examples must not be confused with live research or client records.


B019 [local AI configuration and usage controls](docs/evidence/B019-local-ai-controls.md) are approved and Done for the local scope. All 54 backend tests pass, including 12 B019 tests. Live calls remain disabled even with complete configuration; no live budget or quota policy is selected. B020 local checks are approved and Done under the revised local scope.


B021 local dashboard query service is implemented for approved synthetic reference counts. All 68 backend tests pass; actual PostgreSQL verification remains blocked by the unavailable Docker runtime. No business metrics or dashboard UI were enabled. See [B021 evidence](docs/evidence/B021-local-dashboard.md).


Current B021 update — 21 October 2026: actual PostgreSQL 17.11 verification passed all 15 harness checks after Docker recovery and approved image download; full local checks passed. Earlier unavailable-runtime statements are historical. B021 is approved and Done for local scope; B022 unstarted. The test container was already removed before the user requested no cleanup; retain future test containers and adjust the automatic-cleanup harness before reuse. See the B021 evidence and progress tracker.


## B021 local deliverable approved — 21 October 2026

User: “Approve B021”. B021 is Done for the verified local synthetic-reference dashboard queries and filters. Existing 68 backend tests, 15 actual PostgreSQL checks and full local check runner passed; no tests rerun for this documentation-only acceptance. Earlier blocked/pending-acceptance wording is historical and superseded. B022 remains unstarted. Business metrics and frontend/API exposure remain outside this accepted scope; GitHub/RCI-01 remains deferred. Retain future test containers unless the user asks otherwise and keep approvals in chat. Pre-approval records: docs/evidence/B021-before-acceptance.zip.


## B022 local dashboard preview

B022 is approved and Done for verified local synthetic reference metadata. Preview: http://127.0.0.1:3100/dashboard. It connects the isolated session harness to B021 stored queries; the normal app stays disconnected. Evidence: docs/evidence/B022-local-dashboard-ui.md (project root). The retained container and preview remain running by user preference. Future database checks retain containers by default; tmpfs contents are not durable across container stop/reboot. The B022-stop marker ends preview servers only when requested. B023 has not started.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.


## B023 staging preparation

[Review the local staging pack](deployments/staging/README.md): inert service manifest, empty-value environment template, ownership/cost worksheets and conditional deployment/rollback instructions. Local validation passed; B023 is approved and Done for local preparation. It is not deployable: provider/exact values/owners/budget and normal-runtime integration remain unresolved. B024 is unstarted. No external changes or cleanup performed.


## B023 local preparation approved — 21 October 2026

User: “Approve B023”. The local staging preparation pack is accepted; B023 Done for that scope. Existing draft validation and eight rejection checks retained; no tests rerun for documentation-only acceptance. Earlier pending-review wording is superseded for local preparation. Provider, exact configuration, ownership/budget, target runtime integration and independent review remain unresolved before deployment. Manifest stays draft-not-deployable and deployment_authorized=false; no spending, secret population, GitHub, provisioning or B024 authority is inferred. B024 remains unstarted. Preview/database were left untouched. Prior records: docs/evidence/B023-before-acceptance.zip.


## B024 separate local rehearsal

The user selected a local staging rehearsal; it is approved and Done for the verified local scope. HTTPS endpoint: https://127.0.0.1:3443, with separate production frontend and persistent PostgreSQL volume. The private CA was validated explicitly in tests; browser/system trust was not modified. Existing B022 preview/data remain untouched. See deployments/local-rehearsal/README.md and docs/evidence/B024-local-rehearsal.md from project root for operation, scope and retained-state details. Cloud deployment and B025 remain unstarted.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.


## B025 local recovery

The [recovery runbook](deployments/local-rehearsal/recovery.md) records the verified manual backup and isolated restore procedure, retained state and migration/application rollback boundaries. Eight recovery/control groups and the full local check runner passed. B025 is approved and Done for local recovery; B026 remains unstarted. Backup and restored database are retained; no cleanup performed.


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.


## B026 local verification

User “Start with B026” selected verification of the retained local rehearsal. [Evidence](docs/evidence/B026-local-foundation.md) records six passing HTTPS/API/database groups, the passing full local runner and supplemental shared-dashboard browser checks. B026 approved and Done for local scope; B027 unstarted. Initial browser sign-in failure recovered after explicit logout/retry; B026-OBS-01 remains open with cause unproven. No risk acceptance, hosted staging, remote CI, real identity or independent review inferred. Existing services, backups and databases retained; no cleanup.


## B026 local verification approved — 21 October 2026

User: “Approve B026”. B026 is Done for the verified local foundation scope. Six live check groups, the full local runner and supplemental browser evidence are retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. B026-OBS-01 remains open with cause unproven; approval does not resolve it. Hosted staging, trusted-browser HTTPS, real identity, remote CI and independent review remain deferred. Existing previews, backups and database resources were left untouched; no cleanup. B027 remains unstarted. Prior records: docs/evidence/B026-before-acceptance.zip.


## B027 current setup and support handover

Use the [current setup guide](docs/local-setup.md) for the delivered Windows foundation, isolated setup, alternate rehearsal ports and safe operational logs. B027 local checks passed and the verified local scope is approved and Done; spoken screen-reader verification remains outstanding. The additional B027 rehearsal runs at https://127.0.0.1:3543, with separate persistent data and protected redacted logs. Original services and all resources remain retained. B028 unstarted.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.


## B028 foundation review

The [foundation review pack](docs/evidence/B028-foundation-review.md) links B009–B027 and the current passing local demo/checks. B028 is Done for the adopted [G1-L v0.1 local milestone](docs/planning/G1-local-foundation-proposal.md); original full G1 remains on Hold for required human decisions and original-scope assurance. B029 remains unstarted. All previews/data retained; no cleanup.


## G1-L v0.1 adopted — 21 October 2026

User: “Adopt G1-L v0.1 and accept B028 for local scope only”. B028 Done for the demonstrated local milestone; [adoption/reassessment](docs/evidence/B028-g1-local-adoption.md) preserves original full G1 Hold and every stated deferral. No named Justice/CEO or independent review is inferred. Spoken-reader verification and B026-OBS-01 remain open. B029 unstarted; later local tasks need separate selection and substantive decisions. Documentation-only adoption; no tests rerun or resource changes. All services/data retained; no cleanup. Pre-adoption records: docs/evidence/B028-before-local-adoption.zip.


## Current work — B007 planning reconciliation

The [B007 reassessment](docs/evidence/B007-foundation-reconciliation.md) and [current worksheet](docs/planning/phase-1-design-operations.md) align Phase 1 planning with accepted local evidence. B007 is Done for approved local planning following user-confirmed Justice interim-role acceptance and approved task-by-task local cadence; [completion record](docs/evidence/B007-local-completion.md). G1-L and B009–B028 local acceptances remain intact; full G1 Hold, B029 unstarted. No service/data changes or cleanup.


## Connected main reference dashboard — 21 October 2026

Open http://127.0.0.1:3000/dashboard or the Command Centre at http://127.0.0.1:3000. Synthetic sign-in, persisted permitted reference counts, filters, quick views, Clear filters, refresh and session restoration are connected inside the main navigation. [Connection evidence](docs/evidence/main-dashboard-connection.md) records main-API/browser checks, passing full local suite and separate production build. It depends on the retained B027 HTTPS service/public CA; no real identity/live business features enabled. Existing services/data retained. B029 remains unstarted; full G1 and other deferrals unchanged.
