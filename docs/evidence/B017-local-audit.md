# B017 — Initial audit events and redacted operational request logging

**Date:** 20 October 2026 UTC  
**Status:** Done — user accepted the verified local scope on 20 October 2026 UTC  
**Authority:** User “Approve local event baseline” and “Approve disposable storage baseline” following Start B017  
**Executor:** Codex; formal independent reviews remain deferred

## Delivered and approved boundary

[Approved baseline and run guide](../planning/B017-local-audit-baseline.md) records the exact event, storage/access, failure and cleanup contract. Only synthetic test activity is enabled. Normal application startup and the existing B016 browser harness do not silently enable audit capture.

- [Migration 0004](../../backend/migrations/0004_local_audit.sql): event ID, timezone-aware database timestamp, nullable actor/resource UUIDs and constrained action/outcome codes. No free-text metadata field. PUBLIC table privileges revoked; existing migrations untouched.
- [Audit service](../../backend/app/audit.py): actual B013/B014 session and permission operations wrapped in a transaction with their audit insert. Server-resolved identifiers only. Unknown identities/resources omitted. Catalogue: session.issue, session.logout, record.read and privileged.check. No raw session token or digest is logged.
- Operational capture: allowlisted route label, bounded method/status, server-generated request ID and duration. No body, header, cookie, query, raw path, IP, user agent or exception text. Unmatched routes have a fixed label.
- [Isolated runner](../../backend/check_local_audit.py): explicit test-only wiring and in-memory operational sink, disposable PostgreSQL audit storage, actual HTTP/redaction checks and automatic cleanup. No application audit reader/export endpoint or role grant added.

Successful session changes require audit persistence in the same transaction. Audit-write failure returns generic 503 and rolls back issuance/logout. Handled denial is audited before returning the error. A session-store outage records unavailable if audit storage works; if audit storage itself fails, no row can be retained there and no payload/file fallback is created. Minimal operational status remains available during capture. This is not a durable production delivery/retry or tamper-proof audit system.

## Actual verification — 20 October 2026 UTC

- `python -B -m unittest discover -s tests -v` from backend: **27 tests passed**.
- Final `python -B check_local_audit.py`: **39 verification groups passed** — 33 prior migration/permission/session groups and 6 B017 groups.
- Actual PostgreSQL rows verified issuance, permitted read, cross-client denied read, invalid identifier, privileged denial, logout and unauthenticated requests. IDs match trusted stored fixtures; unknown values are null. Database timestamps are timezone-aware and ordered in the exercised sequence.
- Synthetic private-content canaries placed in request body, query, raw path, headers/cookies and exception text were absent from audit rows, operational capture and captured process output. Raw tokens/digests were absent. Request IDs were generated independently of supplied headers.
- Audit-table outage: issuance and logout return 503; no session is created and revocation is rolled back. Restoring the table permits successful audited logout. Separate session-table outage records unavailable with unknown IDs omitted.
- Writer/schema reject unknown action/outcome and raw string identifiers. PUBLIC grants absent. Normal and harness audit-reader routes return 404.
- Real loopback HTTP 500/404/401 responses and operational metadata were checked. The dedicated test Uvicorn server disables access logs and exception-text output; its captured output contained no canary. It was stopped and joined. Normal server logging configuration was not changed or certified by these checks.
- PostgreSQL 17.11, existing offline image `sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3`, `--pull=never`, loopback and tmpfs. Both runs confirmed disposable container removal. No audit rows or canary values persisted in project evidence.

The initial run passed 38 groups; after adding the explicit unavailable-session-storage case, the final full suite passed 39. No dependencies installed, UI changes, provider calls or GitHub operations. Frontend build/browser checks were not repeated because frontend code was unchanged.

## Preservation and acceptance

[Pre-implementation snapshot](B017-before-implementation.zip) retains affected existing files. Original handover/UI sources, build definitions, migrations 0001–0003, backend session/access implementations and frontend remain unchanged. Existing disposable runner only adds B017 as an allowed task label.

**Acceptance recorded — 20 October 2026 UTC:** User “Accept B017” accepts the verified local synthetic audit and redacted operational-capture deliverable. Persistent/production retention, live-data permissions, viewer grants, deployment and formal reviews remain deferred. Current application routes do not gain persistent logging merely through this acceptance.

B017 is Done. This acceptance changes records only; no code, runtime or database changes and no tests rerun. [Pre-acceptance snapshot](B017-before-acceptance.zip) preserves previous records. B018 is Not started. B004 remains Blocked; B005/B007 review boundaries remain unchanged.

---

## Historical preparation — superseded by approvals and execution above

### Initial preparation

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B017”; local-only restrictions retained  
**Status:** Blocked for implementation pending event and disposable-storage baseline approval  
**Executor:** Codex; Justice remains nominated technical authority

## Scope and prerequisites

[Build-order completion check](../../build-order.md): **“Actor/resource/action/time are retained for defined actions; secrets and private payloads are absent from logs.”**

The [B017 work item](../planning/phase-1-work-items.md#b017) requires B016 and approved event taxonomy, metadata, access, redaction and retention decisions. B016 is accepted and Done for the isolated local scope. F19/F20 and D007/D009 require minimal, protected audit/operational metadata; they do not set a retention duration or grant anyone audit-viewer access.

[B006 policy](../policies/allowed-data-and-test-fixtures.md) allows separately authorised synthetic work and explicitly says unknown retention is not indefinite permission. O-12 remains partly resolved. No current approval establishes a persistent audit destination or real-data log retention. The B016 harness already supplies synthetic identities, records and actual PostgreSQL session/permission checks; it is a suitable proposed verification boundary without enabling real login or business modules.

## Two approval questions

1. **Event baseline:** synthetic session issuance/logout, permission checks and privileged-action denials; server-verified actor/resource IDs, fixed action/outcome codes and UTC timestamps. Omit unknown IDs and all payloads, credentials, IPs and user-agent strings.
2. **Storage/access baseline:** audit events only in a disposable PostgreSQL test database, available only to the local test runner, discarded at the end of each run. Operational logs captured only during tests with fixed route names, method, status, request ID and duration. Persistent/production retention and audit-viewer permissions remain deferred.

Answers are pending. These are task prerequisites recorded in the work item and B006, not a GitHub dependency. No provider, package download, production logging, audit-role grant or broader data permission is implied.

## Proposed catalogue

| Action | Event trigger | Actor | Resource | Outcome |
| --- | --- | --- | --- | --- |
| `session.issue` | Internal issuance after fixed synthetic identity verification | Resolved application user UUID | No session token or token digest; resource omitted | issued / denied / unavailable |
| `session.logout` | Revocation of the current verified session | Verified user UUID when resolvable | Omitted; never raw session identifier | revoked / denied / unavailable |
| `record.read` | Backend record permission check | Authenticated user UUID, if available | Resolved synthetic record UUID only; never arbitrary path text | allowed / denied / unavailable |
| `privileged.check` | Attempt to exercise a privileged action | Authenticated user UUID, if available | Omitted unless a trusted resource is actually resolved | denied / unavailable |

The catalogue records only exercised local actions; it does not imply product approvals, exports, AI usage or other future workflows are implemented. No actor is invented for anonymous requests. Never take actor, role, resource name, event action, timestamp or request ID directly from caller-supplied headers.

## Proposed implementation

- Add a new versioned audit migration without editing migrations 0001–0003. Constrain fields and action/outcome values; use database-generated event IDs and UTC-aware timestamps.
- Provide a narrow audit writer accepting trusted typed identifiers and allowlisted codes, with no free-text metadata or payload field. Configure it only for the isolated test application until persistent storage/access is separately approved.
- Couple successful audited state changes with audit persistence in the same transaction where feasible. A required audit write failure must not yield a false success. Test failure/recovery and document precise semantics before claiming completeness.
- Capture operational metadata through an explicit sink in tests. Use a fixed route identifier, server-generated request ID, bounded method/status values and elapsed duration. Unknown paths become a constant unmatched-route code; do not log raw URLs, query strings, headers, cookies, bodies, exceptions or database error text.
- Do not expose an audit listing/export HTTP endpoint or attach a new viewer grant to an existing role. No log dashboard, background exporter, external collector or scheduled retention job.
- Keep application events distinct from framework access/error logs. Inspect the actual process output as well as structured events so framework logging cannot invalidate the redaction claim.

## Planned verification — not executed

1. Apply/reapply the new migration in a fresh disposable PostgreSQL destination; retain migration-history and recovery checks.
2. Exercise allowed and denied requests through actual session/permission boundaries. Verify fixed actions/outcomes, server-resolved IDs and timestamp presence/order. Omit unknown identity/resource information rather than logging attacker-supplied strings.
3. Place wholly synthetic secret/private-content canaries in headers, cookies, query strings, paths, bodies and exception text. Capture structured audit rows, operational output and relevant framework output; assert canaries and credentials are absent.
4. Verify request IDs cannot be spoofed and unknown routes cannot inject log text or unbounded route labels.
5. Verify audit records cannot be retrieved through normal or harness HTTP routes and do not create blanket access grants.
6. Exercise audit-storage failure and recovery. Verify no successful audited state change is falsely reported or left unaudited under the chosen contract.
7. Rerun relevant backend/session/permission regression checks. Confirm disposable container/data cleanup, and preserve only redacted result summaries in project evidence.

## Preservation and handoff

[Pre-edit snapshot](B017-before.zip) preserves the tracker and documentation index. This preparation changes documentation only; no source code, migration, database, running service or dependency changed. No GitHub or external service activity.

B017 implementation and acceptance checks remain blocked on the two requested baseline decisions. B018 is Not started. Real-data retention, persistent destinations, designated audit viewers, deployment and formal specialist/independent reviews remain deferred.
