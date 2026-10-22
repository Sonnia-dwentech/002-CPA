# B013 — Local Identity and Record Authorisation Preparation

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B013”, under G0-L; subsequent B012 disposable database execution authorised separately  
**Status:** Done — user accepted the verified local deliverable on 20 October 2026 UTC  
**Executor:** Codex; Justice remains nominated technical authority

## Acceptance recorded — 20 October 2026 UTC

User: “i accept B013”. Marked B013 Done for the executed local identity references and record-authorisation boundary under G0-L. Retained evidence of 21 policy/API tests and 19 PostgreSQL verification groups; this acceptance changes documentation only, with no code changes or test reruns.

B014's B013 local-acceptance prerequisite is satisfied. Identity-provider/session validation, expiry/revocation, MFA and named-account bootstrap remain separate decisions; B014 remains Blocked. Formal specialist/independent reviews, real-data use and deployment approval are not inferred. No live sign-in, persistent database or full client portal is claimed.

[Pre-acceptance snapshot](B013-before-acceptance.zip) preserves the previous records. Earlier In review/Blocked statements below describe historical snapshots; this acceptance governs current B013 status.

## Current implementation and user approval — 20 October 2026 UTC

User: “Approve B013 to continue”. Adopted access matrix v0.1 for local continuation and implemented its core identity/reference and record-permission boundary. The approval is recorded as the user's instruction, not an attributed Justice or independent specialist sign-off. Earlier blocked/proposed entries below remain historical.

### Delivered

- [Migration 0002](../../backend/migrations/0002_identity_access_references.sql): unique issuer/subject mapping; disabled-by-default users; internal/client account categories; one client organisation per client user; constrained role categories; record-scope references; explicit grants and case assignments. No live accounts or business content seeded.
- [Access boundary](../../backend/app/access.py): current-state identity/membership and record checks; private owner access; explicit read/edit/export/run/decision separation; assigned-client access; no automatic administrator/CEO access; non-author response approval; filtered reference lists; generic denials and fail-closed database errors. Invalid parent/owner/client combinations are denied.
- [Policy tests](../../backend/tests/test_access.py) and [persisted checks](../../backend/check_local_access.py). Existing disposable runner supports the expanded migration set without modifying applied migration 0001. The synthetic recovery migration is now 9000.
- [Run guide and fixture manifest](../../backend/README.md). All feature kinds default disabled; normal application routes remain only B011 liveness/OpenAPI. No mock authentication switch, public grant mutation endpoint or named-account bootstrap was added.

### Actual verification

- `python -B -m unittest discover -s tests -v`: **21 tests passed** (12 permission-policy tests and 9 existing API tests).
- `python -B check_local_access.py`: **19 verification groups passed**, comprising 9 migration/connectivity/recovery groups plus 10 persisted access groups. Tests cover unknown/spoofed identity, owner access, revoked grants, forbidden actions, role-only access denial, cross-client and same-organisation isolation, unpublished/internal-note denial, filtered lists, revoked case assignments, non-author publication, disabled accounts/memberships, database integrity and generic policy failure.
- PostgreSQL 17.11; installed offline image `sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3`; psycopg 3.3.6. Local elevated execution was used for Docker named-pipe access.
- New uniquely named B013 container only; cleanup confirmed removal and tmpfs data discarded. No existing application database targeted, no downloads/installs or GitHub commands.

### Acceptance boundary and remaining work

The core application-layer permission checks and persisted identity/scope references are demonstrated against actual disposable PostgreSQL. Tenancy assumptions are explicit in the approved matrix: one internal workspace, separate client organisations, one organisation per client user, no automatic same-organisation intake sharing and explicit staff case assignment.

B013 is **In review** for this executed local foundation scope. Acceptance is still needed; approval to implement is not recorded as acceptance of code that did not yet exist.

No B014 credential validation, live sign-in, real-account bootstrap, row-level database security or least-privilege database role is claimed. The public API has no protected business endpoints yet. The access store returns internal metadata to future trusted feature services, not an approved client projection. Invitations, grant-management workflows, publication, search/export/file/job endpoints and other future business workflows remain unavailable; the local tests exercise their policy decisions/reference access only. Later feature implementations must enforce the boundary and add endpoint/lifecycle/concurrency tests. No real/client data or live provider access is authorised.

The user's instruction permits local synthetic implementation while named assignments and formal B006/independent review remain deferred before affected real operation, shared integration or deployment. B014 remains Blocked by its identity/session/MFA choices and pending B013 acceptance; no B014 code was added.

[Pre-implementation snapshot](B013-before-implementation.zip) and [input hashes](B013-implementation-input-hashes.json) preserve previous files. Existing original sources, prior reports, API implementation/tests and migration 0001 remain unchanged. The earlier preparation narrative follows for history.

## Scope and prerequisites

[B013](../../build-order.md) requires identity/user references and the approved role/record authorisation boundary. Its unchanged completion check is: “Permission tests deny unauthorised records; tenancy assumptions are explicit before client records exist.”

The [work-item card](../planning/phase-1-work-items.md#b013) depends on B012, O-04 ownership/sharing/tenancy decisions and B006 deferred technical review. B012's local preparation report is user-approved but PostgreSQL implementation and verification remain blocked by the explicit setup deferral. [ADR-002](../adr/002-identity-roles-tenancy.md) is proposed, and O-04 remains open. The existing backend provides liveness/OpenAPI/error handling; it has no user store or protected record routes.

The user's selection permits this local dependency review and decision/test worksheet. It does not resolve database readiness or approve unspecified business grants. No database, provider, account, credential, schema or application permission was created. B014 is not started.

## Work independent of B012

- Identify who must decide each business and technical access rule.
- Specify the information needed at the server authorisation boundary without choosing database columns or an identity provider.
- Prepare positive and negative test cases against synthetic actors, with positive grants left pending until approved.
- Trace future API/search/export/file/job checks to F01 and document what local mock tests would and would not prove.

Persisted user references, ownership relationships, integrity constraints, database-backed filtering and their real integration tests require B012's approved schema/migration/connectivity foundation. A future isolated policy test can precede that foundation only after its own grants and policy contract are approved; it cannot establish persisted isolation.

## Approval worksheet

Justice owns technical decisions with the product owner for business grants, as recorded in [O-04](../../decisions.md). The user previously nominated Justice as interim product/scope approver; no decision below is inferred from that nomination.

| Decision | Concrete outcome required | Current state |
| --- | --- | --- |
| Initial actor scope | Internal humans only, or explicit client access in the initial scope; treatment of future analysts | User selected inclusion of client sign-in in the local proposal; future analyst scope and actual release enablement remain undecided |
| Identity references | Source of verified identity; stable subject mapping, uniqueness and disabled/deleted-account handling | Unselected; do not trust caller-supplied user IDs |
| Role/action/resource matrix | For each enabled role: explicitly permitted actions, resource types and scope; who assigns/revokes grants | Unapproved; titles confer no automatic access |
| Ownership and sharing | Who owns new records; private versus team-visible defaults; explicit sharing, transfer and revocation rules | Unapproved; ownership alone is not an assumed allow rule |
| Tenancy | Internal workspace boundary; how future client data is separated; membership source and cross-scope exceptions, if any | Unapproved; no client records permitted |
| Administration | Whether an application admin exists; exact grants and any elevated-access controls | Unapproved; Justice/CEO/developer roles do not imply unrestricted record access |
| Server policy contract | Trusted actor context, scope resolution, denial response, query filtering and policy enforcement on derived outputs | Proposal below, subject to technical review |
| Security/policy review | B006 technical review for the selected access boundary and synthetic fixtures | Deferred; no sign-off inferred |

Session/provider integration is B014 work. B013 needs an agreed trusted-identity contract to avoid inventing that integration. No provider account, session lifetime or recovery mechanism is selected here.

### Grant worksheet to complete before allow-path code

Complete one row per approved role/action/resource combination, rather than approving broad role names. Required fields:

`Role | Resource type | Action | Ownership/membership condition | Sharing condition | Explicit allow or deny | Grant authority | Revocation behaviour | Approver/date`

Potential actors are the Founder/CEO, human CPA, Justice, human assistant developer, future analyst and Discovery client. Client sign-in is included in this proposal by user direction; specific role enablement and all grants remain undecided. AI cannot exercise human approval/investment/contract/release authority. No allow rows are populated because the source documents do not approve them.

## Client sign-in proposal scope — user decision, 20 October 2026 UTC

User: “Include client sign-in in the proposal”. The design must consider client identities alongside internal human identities now. This is proposal scope, not approval to implement a client portal or move Discovery delivery into Phase 1. B014 authentication integration remains unstarted.

The client design must resolve:

- How a client account is enrolled and verified, and who may establish or revoke its membership in a client organisation. Invitation versus self-registration remains unselected.
- Whether one client organisation may have multiple users, whether a user may belong to several clients, and how active scope is selected and checked. Do not derive membership from a submitted client ID or email domain alone.
- Which intake, approved-response, file and other actions are explicitly granted; how ownership/sharing works within a client organisation; which internal staff may access those records. No grants are inferred from successful sign-in.
- Account suspension, membership removal and session revocation behaviour, with the authentication contract completed under separately selected B014 work.

Extend the planned synthetic checks to cover signed-in clients without membership, membership in another client, forged scope changes, client attempts to use internal-only actions and revoked membership. Include an allowed client action only after its grant is approved. These cases are planned, not executed. Real-client data remains prohibited.

[Pre-change snapshot](B013-before-client-scope.zip) preserves the report, tracker and decision register before this clarification. B012/B013 remain Blocked and no task status changes.

## Proposed server contract for technical review

1. Receive a verified actor context through the later approved authentication boundary, never from an arbitrary request user/role/client field.
2. Resolve the resource and its ownership/scope from trusted application state. Unknown identity, resource scope, action or required policy data must not produce an allow decision.
3. Evaluate explicit role/action/resource grants together with the approved ownership/sharing/tenancy rules. Missing approval is not a permissive default.
4. Apply the same scope to direct reads/writes and collections, counts, search, file downloads, exports and job outputs. Recheck current permissions when a delayed output is retrieved.
5. Return only the approved public denial response; do not expose record existence/content or internal policy details. Decide 403-versus-concealed-404 semantics before endpoint tests.

These properties reflect F01 and ADR-002; they are a proposed implementation contract, not implemented controls. B011 public liveness remains separate from protected application records.

## Planned verification matrix — no tests run

| Case | Expected outcome / decision dependency |
| --- | --- |
| Missing/unverified actor | Deny protected access; authentication integration verified later with B014 |
| Authenticated actor with no applicable grant | Deny; no protected content or derived private information |
| Explicitly permitted actor and matching record scope | Allow only the approved action; positive grant needed before encoding expectation |
| Owner without an approved action grant | Do not infer allow from ownership; encode final approved ownership rule |
| Different synthetic owner or client changes a direct record ID | Deny unauthorised record access; tenancy model needed for fixture construction |
| Request spoofs role, user or client fields | No privilege change; use trusted context/state |
| List/search/count/export/file/job uses a restricted record | No restricted content or derived private information through alternate paths |
| Grant/membership revoked after job starts | No retrieval based only on stale privileges; final revocation contract required |
| Unknown action, missing scope or policy failure | Fail closed; no fallback global access |
| API/database integration | Verify real persisted scoping after B012; mock success alone cannot pass this check |

Synthetic fixture plan: create distinct fictional actors and two isolated client scopes only after the scope/schema is approved. Record a manifest with synthetic origin, purpose, expected results, schema/version, owner, location and cleanup method under B006. No fixtures or persistent test stores have been created.

## Completion and handoff

To complete B013, resolve the task-level approvals above, unblock and verify the required B012 persistence foundation, implement the approved boundary, and run positive and negative permission checks. Record explicit tenancy assumptions before any client records exist. Retain independent review and original governance checks before shared integration/deployment.

This preparation does not meet B013's implementation acceptance criteria. Local policy design can continue while database setup is deferred; database changes and invented access grants cannot.

[Pre-edit snapshot](B013-before.zip) and [input hashes](B013-input-hashes.json) preserve the starting state. Only progress.md and the documentation index are edited; this report and preservation artifacts are new. Existing backend, original sources, prior evidence and build-order definitions remain unchanged. No GitHub, downloads, installs, external service calls or database actions occurred.

## B012 dependency update — 20 October 2026 UTC

The user subsequently lifted the B012 setup deferral for disposable local PostgreSQL work. Nine actual database checks and nine API checks passed; see [current B012 evidence](B012-local-database.md). B012 is now In review, with no persistent database retained. Earlier references to the setup deferral above describe the preparation snapshot. B013 remains Blocked pending its identity/grant/ownership/tenancy decisions, B006 technical review and B012 acceptance. Client sign-in remains in proposal scope only. No B013 implementation or permission tests occurred.

## B012 acceptance update — 20 October 2026 UTC

User accepted B012's executed local deliverable. B012 is Done and its local acceptance prerequisite is satisfied. B013 remains Blocked by unresolved identity/grant/ownership/tenancy decisions and B006 technical review. The database check destination was disposable and removed; future persistence work must use an authorised isolated destination. No B013 code or B014 work performed during this update.

## Recommended access matrix drafted — 20 October 2026 UTC

User requested a recommended matrix for Justice approval. [Version 0.1](../planning/B013-recommended-access-matrix.md) proposes internal/client permissions, invite-only identity, scope/ownership/sharing rules, administrative boundaries, revocation and a verification matrix. It includes explicit approval fields and separates future-feature permissions from implementation scope.

These are proposed choices, not approved grants. The earlier empty worksheet is superseded as the review artifact by this populated recommendation; O-04 remains Open and B013 remains Blocked pending approval and B006 technical review. B012 is Done. No code, database or account changes occurred; B014 remains unstarted.

[Pre-draft snapshot](B013-before-access-matrix.zip) and [input hashes](B013-access-matrix-input-hashes.json) preserve existing records before this documentation update.
