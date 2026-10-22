# B012 — PostgreSQL Connectivity and Migration Workflow

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B012”, under accepted G0-L; local-only restrictions retained  
**Status:** Done — user accepted the executed local deliverable on 20 October 2026 UTC  
**Executor:** Codex; Justice remains nominated technical authority

## Acceptance recorded — 20 October 2026 UTC

User: “I accept B012”. Marked B012 Done for the executed local PostgreSQL connectivity, initial migration, apply/reapply and demonstrated transactional recovery/rollback scope under G0-L. Existing evidence of nine database checks and nine API tests is retained; no code changed or tests rerun for this documentation-only acceptance.

The disposable database was removed after verification; no persistent database or broader disaster-recovery readiness is claimed. B013 access-policy decisions remain unresolved. Formal technical/independent review, original governance and G1 remain deferred; no GitHub or B014 work authorised.

[Pre-acceptance snapshot](B012-before-final-acceptance.zip) preserves the preceding records. Earlier status statements below are historical execution snapshots; this acceptance governs the current status.

## Current execution outcome — 20 October 2026 UTC

The user instructed: “Approve a usable local PostgreSQL destination , migration approach and initial  schema and followed by an actual migration/recovery checks.” This supersedes the earlier setup deferral for disposable local B012 work. The previous approval/deferral entries below remain historical. All GitHub, download/install, cloud, real-data and deployment restrictions remain.

Selected bounded approach: existing offline Docker PostgreSQL image, installed psycopg, ordered transactional SQL migrations, and initial migration bookkeeping plus an empty `cpa` namespace. No user/client/role/business tables were selected. No broad Justice architecture or independent-review sign-off is inferred.

### Actual destination and verification

- Native inspection had not found a usable server. Docker's local named-pipe engine was initially stopped. A start attempt hit filesystem permissions; the authorised elevated retry started Docker Desktop. Elevated local image inspection and test execution were needed for named-pipe access. No image pull or install occurred.
- Existing `postgres:17` image ID: `sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3`.
- Actual server: PostgreSQL **17.11 (Debian 17.11-1.pgdg13+2)**. Driver: psycopg **3.3.6**.
- Destination: a newly generated `cpa-b012-check-<uuid>` container, database/user `cpa_b012`, random temporary password, ephemeral port bound to `127.0.0.1`, tmpfs data storage. The actual container was removed and tmpfs discarded; there is no retained database destination to reconnect to. The script reproducibly creates a fresh disposable destination.
- Command from backend: `python -B check_local_database.py`. **Nine database checks passed:** loopback connection; initial apply; no-op reapply; changed-history rejection; missing-history rejection; failed migration rollback of DDL/data/history; corrected pending migration recovery; failed data transaction preservation; explicit synthetic rollback to baseline.
- Existing API command: `python -B -m unittest discover -s tests -v`. **Nine API tests passed**, including actual loopback startup/shutdown. Public health is unchanged.
- Cleanup confirmed the uniquely named test container no longer exists. Docker Desktop was left running; existing containers/volumes were not targeted by this script.

### Deliverable and limits

[Database module](../../backend/app/database.py), [initial SQL](../../backend/migrations/0001_application_namespace.sql), [executable disposable checks](../../backend/check_local_database.py), and [run guide/fixture manifest](../../backend/README.md) provide the implementation and reproducible checks. Migration history records filename, checksum and timestamp; the pending batch and its history commit together under an advisory transaction lock. Applied files must match the recorded prefix and checksums.

Recovery demonstrated here is transactional rollback and a specifically tested destructive rollback of synthetic fixture data. It is not backup/restore, disaster recovery, arbitrary migration reversibility or least-privilege role verification. The disposable bootstrap role is privileged; application roles belong to later approved design. Business schemas, persistent development setup, secrets storage and full-stack fresh setup are not delivered by this check. B013 remains blocked by its unresolved access-policy decisions and pending B012 acceptance, rather than the now-lifted setup deferral.

B012 is **In review**, ready for acceptance of this executed local scope; it is no longer blocked by absent local PostgreSQL verification. Formal governance/review and G1 remain deferred. No B013 code or B014 work was started.

[Execution snapshot](B012-before-execution.zip) and [execution input hashes](B012-execution-input-hashes.json) preserve pre-execution records and source state. Earlier reports below describe earlier states, not the current setup authority.

## User approval — 20 October 2026 UTC

User: “Approve B012”. Recorded approval of the delivered local prerequisite review, native inspection findings and execution plan. The prior explicit setup deferral remains in force. Approval does not select between the unresolved migration-tool alternatives or establish an approved schema/destination.

B012 remains **Blocked** against its unchanged build-order completion check: PostgreSQL connectivity, apply/reapply and disposable-data recovery have not been demonstrated. No task-scope revision or waiver of those checks is inferred. B013 is not started. All local-only restrictions and deferred reviews remain in force.

[Pre-approval snapshot](B012-before-approval.zip) preserves the report and tracker before this approval was recorded.

## Scope and acceptance

[Build order](../../build-order.md) requires PostgreSQL connectivity and a versioned migration workflow. Its unchanged completion check is: “Apply/reapply checks pass; recovery/rollback implications are demonstrated on disposable data.”

B011 is accepted and Done. B004 remote governance and B005/B007 reviews remain deferred under G0-L. Those deferred reviews do not alone prohibit independent local preparation, but the [B012 work item](../planning/phase-1-work-items.md#b012) requires a database/migration-tool choice, approved initial schema and disposable destination before implementation. Starting B012 does not constitute approval of unspecified schema or targets.

The earlier user instruction “Defer database setup; document blocker” remains recorded. A clarification has been requested whether the new task selection lifts that deferral, and whether to inspect native PostgreSQL, existing Docker images or a user-specified local destination. The subsequent user response retained option 2 (keep database setup deferred; prepare only) and selected native PostgreSQL inspection first. This authorises read-only local inspection, not database setup.

## Local evidence

- Installed Python package metadata: psycopg 3.3.6 and SQLAlchemy 2.1.4; Alembic, psycopg2, psycopg2-binary and asyncpg not installed in the inspected default Python environment.
- `psql`, `postgres` and `pg_ctl` were not found on PATH. Docker CLI was found; no daemon connection or image inventory was performed.
- Windows service query returned no service with “postgres” in its name; the conventional `C:\Program Files\PostgreSQL` directory query returned no installation entries. These limited checks do not establish that PostgreSQL is absent from the computer.
- Package metadata does not prove that a driver imports successfully, connects, or is compatible with a server.
- No database service was started, no database connected/created/modified, and no migration was executed. No download, install, GitHub, cloud or provider activity occurred.

## Decisions needed before database work

| Decision | Proposed bounded option for review | Authority / evidence still needed |
| --- | --- | --- |
| Database-setup boundary | Keep setup deferred; continue local preparation only | Confirmed by user; future setup requires a separate instruction |
| Destination and lifecycle | Inspect the selected local approach; establish its exact identity, isolation, ownership and cleanup boundary before writing | Native PostgreSQL inspection selected by user; no verified destination found; no automatic Docker pull or existing-service modification |
| Driver and migration tool | Evaluate installed psycopg with ordered SQL migrations, or Alembic with SQLAlchemy if separately authorised and available | Justice task-level choice; neither approach adopted |
| Initial schema | Limit B012 to migration bookkeeping and a clearly separate disposable verification fixture; leave business/user/tenancy tables to their selected tasks | Justice approval of exact schema and scope before creation; this is a proposal |
| Credentials and connection configuration | Loopback-only, scoped local access; no credential values in reports, command arguments or source | Confirm target-specific authentication and safe local configuration; `.env.example` remains unchanged |
| Recovery approach | Demonstrate transactional failure recovery on synthetic data, then approved rollback or restore with documented limits | Agree tool-specific procedure and data-loss boundary; do not assume every migration is reversible |

No hosting vendor, business schema, identity grants or tenancy model is selected by this report. No credentials should be supplied in chat. Broader architecture and independent review remain deferred requirements before shared integration/deployment.

## Execution and evidence plan after decisions

1. Verify installed client/driver functionality and the approved local server version without downloading dependencies. If unavailable, report the exact missing component.
2. Verify the disposable destination explicitly; reject unknown or nonlocal targets. Establish isolation and preservation before any write.
3. Implement the approved connection configuration and version tracking. Avoid exposing connection strings or private database errors through health/error responses. B011 health remains process liveness.
4. Apply the initial approved migration to an empty disposable target; inspect the actual schema, version record and constraints.
5. Reapply with no duplicate objects or data loss. Verify version ordering and changed-migration handling according to the selected tool.
6. Exercise a deliberately failing migration against synthetic data. Verify the resulting schema/version state and successful recovery; report transactional limitations.
7. Demonstrate the approved rollback or restore path with a known synthetic fixture. Compare recovered schema/data and document any irreversible operations.
8. Run relevant existing API checks if application code changes; record exact commands, versions, outcomes and cleanup. Leave unrelated local services/data untouched.

None of these execution checks is claimed passed. A planning report, SQLite substitute or mocked driver cannot satisfy B012's PostgreSQL apply/reapply/recovery acceptance check.

## Preservation and handoff

[Pre-edit snapshot](B012-before.zip) preserves the tracker and documentation index. [Input hashes](B012-input-hashes.json) record all 88 pre-existing files. Only those two navigation/ledger files are edited; this report and its preservation artifacts are new. Backend code, original source material, build-order acceptance criteria and prior reports remain unchanged.

B012 is started but blocked pending the decisions above. B013 remains Not started. User acceptance of this report alone would not demonstrate the unchanged database acceptance criteria.

## User clarification and native inspection — 20 October 2026 UTC

The user answered “2. and keep on doing things locally” to the setup question and “Inspect existing native PostgreSQL first” to the approach question. Database setup remains deferred. Docker inspection, service startup, database creation and migrations were not performed.

Read-only native checks found:

- No `psql`, `postgres` or `pg_ctl` command on PATH.
- No matching PostgreSQL/pgsql service from the successful `Get-Service` query.
- Neither standard machine PostgreSQL installation registry key exists (64-bit or WOW6432Node).
- No PostgreSQL directory at either Program Files location or the current user's LocalAppData/Programs location.
- No matching PostgreSQL installed-app entry returned from the inspected machine/user uninstall registry locations.
- The separate `Get-CimInstance Win32_Service` query failed with Access denied. Its empty initial output is not evidence of service absence; the successful Get-Service result is the bounded service evidence. No elevation attempted.

These checks do not search every portable/custom installation location and do not establish that PostgreSQL is absent. No native server version or usable database destination is verified. The existing execution plan is ready for later use after setup authority and task-level decisions; none of its database checks has run.

[B012-before-clarification.zip](B012-before-clarification.zip) preserves the preceding report and tracker. Only those two documents changed in this clarification update; existing backend and original sources are preserved. B012 remains Blocked and B013 remains Not started.
