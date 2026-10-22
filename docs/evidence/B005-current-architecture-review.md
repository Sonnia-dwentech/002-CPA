# B005 — Current architecture decision review

**Date:** 21 October 2026 (Atlantic/Reykjavik)  
**State:** Accepted local architecture; user confirmed Justice approval  
**Authority:** User: “Let's sort out B005”. Codex prepares; Justice decides architecture.  
**Scope:** Existing synthetic local foundation. B004 remains Blocked; B029 remains unstarted.

## Accepted local decisions

| Decision | Recommended selection | Reason and consequence |
| --- | --- | --- |
| [ADR-001](../adr/001-core-stack.md) — stack | Retain Next.js/TypeScript, FastAPI/Python, PostgreSQL and the checked SQL migration runner locally | Retains the tested contracts/data boundary; two runtimes and transaction-compatible migrations require coordinated maintenance |
| [ADR-002](../adr/002-identity-roles-tenancy.md) — identity and tenancy | Retain approved synthetic B013 grants, B014 opaque sessions and application-enforced shared-schema scope locally | Enables repeatable access checks; does not authenticate real humans or provide database row isolation |
| [ADR-003](../adr/003-environments.md) — environments | Retain separately configured local verification, rehearsals and recovery target; require staging/production separation later | Preserves scoped failure/recovery evidence; creates no hosting commitment and does not qualify local credentials/backup as production ready |
| [ADR-004](../adr/004-service-boundaries.md) — services | Retain cohesive backend modules, thin frontend bridge and mock provider adapter; reserve a future worker boundary | Avoids unsupported distributed-service obligations; durable execution and real research workflows still need contracts |

Each ADR records alternative options, rationale, consequences, current evidence and explicit limits. The confirmed approval includes the deliberate deferrals below; it does not assert that deferred capabilities exist.

## Deliberate deferrals with owners and checkpoints

Roles below are required decision authorities, not newly assigned operators or promised deadlines.

| ID | Deferred decision / reason | Required authority | Checkpoint |
| --- | --- | --- | --- |
| D005-01 | Real identity provider, enrolment/recovery, MFA, real grants and tenant isolation: synthetic fixtures do not settle them | Justice; product owner for business grants | Before real-user/client data or affected shared/client implementation; O-04/B006 |
| D005-02 | Hosting/account/region/domain, costs and normal-runtime configuration: no external deployment authorised | Justice and business/budget authority | Before hosted staging/provisioning or spending; O-03/O-16/O-17 |
| D005-03 | Least-privilege migration/runtime locking and database TLS: local bootstrap is privileged and UPDATE(id) is a write grant | Justice | Before hosted staging; evidence must verify actual grants and transport |
| D005-04 | Backup location, retention, RPO/RTO, certificate/secret lifecycle and operators: manual same-machine rehearsal is insufficient | Justice and relevant operational/business authority | Before hosted staging or real data; O-16/O-17; preserve retained local state meanwhile |
| D005-05 | Durable jobs/retry/cancel/idempotency, source rights, model budgets, storage/export and lifecycle contracts: product behavior still undefined | Justice and product owner; source/budget authority as applicable | B029 before affected implementation; O-05–O-09 |
| D005-06 | Audit integration for new writes/exports/jobs: tested helper is not global route coverage | Justice | Before enabling each affected operation; test transaction/access/failure behavior |
| D005-07 | Log rotation, monitoring, alerting and support ownership: minimum redaction capture is not production operations | Justice and operational authority | Before hosted operations |
| D005-08 | Remote code alignment, repository access/protections/CI and eligible independent review: GitHub remains deferred | Justice; user authority needed to resume remote activity | B004/RCI-01 before remote collaboration/merge/release |
| D005-09 | Current full setup after the dashboard bridge, hosted compatibility and support/version policy: prior fresh setup and later build are distinct evidence | Justice | Before claiming a current reproducible normal-runtime deployment or hosted readiness |

A deferral does not waive its checkpoint. If a chosen future task reaches one, obtain the required decision before dependent implementation.

## Evidence reviewed and limitations

The accepted local B012–B028 evidence and current source informed this revision. Principal evidence: [database](B012-local-database.md), [access](B013-local-authorisation.md), [sessions](B014-local-authentication.md), [audit](B017-local-audit.md), [mock adapter](B018-local-ai-adapter.md), [rehearsal](B024-local-rehearsal.md), [recovery](B025-local-recovery.md), [fresh setup/support](B027-accessibility-setup.md), [adopted G1-L](B028-g1-local-adoption.md), and [main dashboard](main-dashboard-connection.md).

The last dashboard follow-up recorded 70 backend tests, 5 runner tests, contracts/types, separate production build, four actual main-API check groups and browser journeys. These are existing scoped results; this documentation review did not rerun runtime tests or inspect remote infrastructure. The dashboard on 3000 uses the separate rehearsal on 3543; port 8000 liveness alone does not establish dashboard readiness. No live identity, provider, durable jobs, complete audit coverage or production tenant isolation is asserted.

## Completion and approval record

B005 requires Justice's recorded decisions/options/trade-offs. The earlier “I accept B005” accepted the old review pack without identifying a technical outcome. The later confirmation of Justice's interim-role acceptance resolved B007 ownership, not these four ADR decisions.

**Decision received — 21 October 2026 (Atlantic/Reykjavik):** User answered “Justice approves the four local ADR decisions and listed deferrals” to the explicit question naming ADR-001–004, D005-01–D005-09 and their checkpoints. This is recorded as the user confirming Justice's technical approval of those local choices and deliberate deferrals; no personal identity or direct signature is inferred.

B005 is Done for the approved local architecture review. Totals: 27 Done / 1 Blocked / 0 In review / 77 Not started. O-03 is Partly resolved: the local architecture is adopted; hosting and other explicit future choices remain open. O-04 remains Partly resolved. G0-L/G1-L acceptances persist; original full G1 remains Hold. This outcome does not supply independent code review, CEO functional acceptance, deployment approval or Phase 2 authority. See [acceptance record](B005-local-architecture-acceptance.md).

## Preservation and checks

[Pre-review snapshot](B005-before-current-review.zip) preserves ten inputs, including the original ADRs and unchanged build order. [Input hashes](B005-current-review-input-hashes.json) and [review checks](B005-current-review-checks.json) record preservation, link and ledger checks. The original [B005 report](B005-local-architecture-review.md) remains historical and links here. No service, database, fixture, container, volume, backup or source code was changed or cleaned up.
