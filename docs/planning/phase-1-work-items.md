# Phase 1 Local Work-Item Pack — B007

**Version:** 0.6 · **Reconciled:** 21 October 2026 (Atlantic/Reykjavik)  
**State:** B009–B028 accepted for recorded local scopes; B007 Done for approved local planning; owner acceptance confirmed by user and local cadence approved. Original full G1 Hold.

B IDs are local work-item identifiers, not GitHub issue numbers. [Build order](../../build-order.md) owns scope/criteria; [progress](../../progress.md) owns status. [Pre-reconciliation snapshot](../evidence/B007-before-foundation-reconciliation.zip) preserves earlier wording. [Current B007 reassessment](../evidence/B007-foundation-reconciliation.md) records remaining gaps. This reconciliation neither starts B029 nor grants external authority.

## Current readiness interpretation

D006 defines Ready as user value, scope, non-goals, acceptance criteria, dependencies, test plan, security implications, owner and design reference. Every card contains these fields. Estimates and calendar dates are not additional D006 Ready criteria; they remain unset rather than invented. Field presence alone does not prove adequate scope or accepted assignments.

B009–B028 are Done for user-approved local slices/G1-L. Original Not Ready/no-tests statements have been reconciled against actual evidence. Completed work is not relabelled Ready, and acceptance is not backdated into pre-execution readiness approval. Original/full-scope dependencies and completion criteria remain visible with approved local interpretations in linked reports.

Justice remains interim accountable implementation owner/product-scope approver; the user confirmed his acceptance on 21 October 2026. This is user-reported role acceptance, not a claim that the user is Justice or a technical/independent/CEO signature. Codex actually prepared/executed selected local work; user task selections and scoped acceptances are recorded. This is not a human developer appointment or independent review. Justice technical decisions, independent reviewer eligibility and CEO full-gate/release decisions remain separate. If Justice authors changes, another eligible human must review them.

G0-L/G1-L are accepted for local work only. B004 remains Blocked, B005 In review and original full G1 Hold. Substantive architecture, real identity, hosted operations and remote controls retain checkpoints before affected future work. [Current design/operations worksheet](phase-1-design-operations.md) records local decisions, authorities, external restrictions and remaining human choices. Later dated acceptance paragraphs describe milestone history; current ledger/reconciled records govern status.

<a id="b009"></a>
## B009 — Prepare approved repository structure and import handover/ADR references at valid paths

- **User value:** Give developers a coherent, traceable project layout.
- **Scope:** Prepare approved repository structure and import handover/ADR references at valid paths
- **Non-goals:** No empty scaffold, remote import or source overwrite.
- **Acceptance criteria (unchanged build-order check):** Meaningful files and working source links exist; original material is preserved
- **Dependencies:** G0/B008 and B008; Approved architecture/layout; B004 repository authority; correct local source paths. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Check meaningful files, resolved imports/document links and preservation of originals. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Exclude secrets and restricted source material from imports. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-02; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B009-local-structure.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b010"></a>
## B010 — Prepare Windows-compatible local setup guidance and placeholder configuration

- **User value:** Make setup repeatable on the supported Windows workstation.
- **Scope:** Prepare Windows-compatible local setup guidance and placeholder configuration
- **Non-goals:** No cloud provisioning or production configuration.
- **Acceptance criteria (user-revised local preparation check):** Provisional tooling and local setup guidance recorded; `.env.example` contains placeholders only; known launch/database limitations and later executable-verification checkpoints are explicit
- **Dependencies:** G0/B008 and B009; Runtime/package-manager choices; local database and test isolation approach. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Validate guidance, recorded local tool inventory and placeholder-only configuration now; fresh setup and runtime/configuration behaviour require the later implementation and B027 checks. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Keep real credentials out of templates and logs; confirm test destination. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-02; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Recorded outcome:** B010 Done for the accepted local preparation slice. Fresh executable verification remains deferred to B011/B012/B015–B016 and B027; no implementation permission or full-stack readiness inferred.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B010-local-setup.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b011"></a>
## B011 — Add FastAPI startup, health contract and initial OpenAPI/error structure

- **User value:** Provide a predictable API startup and diagnostic contract.
- **Scope:** Add FastAPI startup, health contract and initial OpenAPI/error structure
- **Non-goals:** No application feature endpoints beyond approved foundation scope.
- **Acceptance criteria (unchanged build-order check):** Health and error checks pass; public health response leaks no secrets
- **Dependencies:** G0/B008 and B010; Approved API stack, health/error disclosure policy and contract conventions. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Exercise startup, health, validation/error responses and unavailable dependencies against agreed behaviour. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Health/errors must not disclose credentials, internals or private payloads. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-04; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B011-local-api.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b012"></a>
## B012 — Add PostgreSQL connectivity and versioned migration workflow

- **User value:** Persist foundation records through repeatable schema changes.
- **Scope:** Add PostgreSQL connectivity and versioned migration workflow
- **Non-goals:** No live-client import or production migration.
- **Acceptance criteria (unchanged build-order check):** Apply/reapply checks pass; recovery/rollback implications are demonstrated on disposable data
- **Dependencies:** G0/B008 and B011; Database/migration-tool choice; approved initial schema and disposable test destination. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Apply/reapply migrations; verify constraints and rollback/recovery implications on disposable data. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Use scoped database credentials; avoid destructive operations on unknown targets. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-05; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B012-local-database.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b013"></a>
## B013 — Implement identity/user references and the approved role/record authorisation boundary

- **User value:** Protect each record before protected features are enabled.
- **Scope:** Implement identity/user references and the approved role/record authorisation boundary
- **Non-goals:** No guessed roles, broad admin grants or future client portal.
- **Acceptance criteria (unchanged build-order check):** Permission tests deny unauthorised records; tenancy assumptions are explicit before client records exist
- **Dependencies:** G0/B008 and B012; O-04 role/action/resource matrix, ownership/sharing and tenancy decision; B006 deferred technical review. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Positive owner/grant cases and negative direct-ID/cross-client cases with synthetic actors. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Deny by default at server boundary; test all approved access paths. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-05/P1-06; F01; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B013-local-authorisation.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b014"></a>
## B014 — Implement approved authentication/session validation in the backend

- **User value:** Reject unauthorised sessions consistently.
- **Scope:** Implement approved authentication/session validation in the backend
- **Non-goals:** No unapproved identity vendor or improvised account recovery.
- **Acceptance criteria (unchanged build-order check):** AC-F01-01 passes; invalid/expired credentials cannot obtain protected responses
- **Dependencies:** G0/B008 and B013; Identity/session validation, expiry/revocation and privileged MFA decisions. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Check valid, missing, malformed, expired and revoked credentials according to approved session policy. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** No token logging or acceptance of client-supplied identity without validation. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-06; F01; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B014-local-authentication.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b015"></a>
## B015 — Build responsive Next.js navigation shell with accurate feature availability

- **User value:** Give users accessible navigation that reflects delivered capabilities.
- **Scope:** Build responsive Next.js navigation shell with accurate feature availability
- **Non-goals:** No operational scanner, voice, research workflow or invented dashboard counts.
- **Acceptance criteria (unchanged build-order check):** Routes/state labels reflect delivered scope; keyboard/focus checks pass; no fake service availability
- **Dependencies:** G0/B008 and B014; O-11 route/label/token/asset and unavailable-navigation decisions; approved UI stack. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Check routes, keyboard focus, responsive layout and unavailable controls against F02/D005. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** UI visibility never substitutes for backend permission enforcement. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-03; F02; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B015-local-navigation.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b016"></a>
## B016 — Connect sign-in/session and access-denied UI to backend permissions

- **User value:** Make sign-in and access-denied states usable without weakening backend controls.
- **Scope:** Connect sign-in/session and access-denied UI to backend permissions
- **Non-goals:** No broad role grants or client workflow expansion.
- **Acceptance criteria (unchanged build-order check):** Permitted sign-in journey works; direct API denial remains effective independently of the UI
- **Dependencies:** G0/B008 and B015; B013/B014 permissions/session contract; approved authentication UI states. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Exercise sign-in/session loss and denied-record routes; direct API denial must remain effective. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Avoid restricted-content flashes, token exposure or unsafe redirects. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-03/P1-06; F01/F02; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B016-local-sign-in.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b017"></a>
## B017 — Implement initial audit events and redacted operational request logging

- **User value:** Make actions and failures traceable without exposing payloads.
- **Scope:** Implement initial audit events and redacted operational request logging
- **Non-goals:** No full request/prompt logging or invented retention period.
- **Acceptance criteria (unchanged build-order check):** Actor/resource/action/time are retained for defined actions; secrets and private payloads are absent from logs
- **Dependencies:** G0/B008 and B016; Approved event taxonomy, metadata, access, redaction and retention decisions. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Generate representative events/errors and synthetic secret canaries; inspect emitted records and denied log access. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Actor/resource metadata needs controlled access; redact secrets and sensitive fields. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** F19/F20; D007/D009; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local planning disposition:** Completed local slice accepted; see current record below. This does not certify original/full-scope Ready or backdate an earlier approval.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B017-local-audit.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b018"></a>
## B018 — Define AI adapter interface, output/error contracts and mock provider tests

- **User value:** Verify a stable AI boundary without paid calls.
- **Scope:** Define AI adapter interface, output/error contracts and mock provider tests
- **Non-goals:** No live provider enablement, source ingestion or autonomous agents.
- **Acceptance criteria (unchanged build-order check):** Success, timeout, refusal and malformed fixtures behave predictably; no live call is needed
- **Dependencies:** G0/B008 and B017; Approved adapter input/output/refusal/error contracts and synthetic fixtures. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Mock success, timeout, refusal and malformed output; assert no live fallback or secret leakage. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Treat outputs as untrusted drafts; meter mocks honestly. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-07; F06; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User selected B018 under G0-L; Codex implemented the [local contract](B018-local-ai-contract.md). [15 synthetic tests passed](../evidence/B018-local-ai-adapter.md); B018 Done following user “Approve and accept B018”. Dependencies were subsequently installed in backend/.venv312; all 42 backend tests pass and pip check is clean. Broader reviews remain deferred. The earlier planning test language above describes the original plan.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B018-local-ai-adapter.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b019"></a>
## B019 — Implement baseline configuration/usage hooks and fail-closed live-AI enablement

- **User value:** Prevent accidental or unbounded paid usage.
- **Scope:** Implement baseline configuration/usage hooks and fail-closed live-AI enablement
- **Non-goals:** No actual credential creation, billing changes or live calls.
- **Acceptance criteria (unchanged build-order check):** Missing model/credential/budget configuration cannot trigger an uncontrolled paid call; unknown cost is not reported as zero
- **Dependencies:** G0/B008 and B018; O-07 approved model/budget/limit policy and enablement authority; config contract. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Use mocks for missing/invalid configuration and unknown usage cost; ensure fail-closed behaviour. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Unknown cost is not zero; live enablement requires separate authority. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-07; F19; O-07; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User selected B019; [local configuration/usage controls](../evidence/B019-local-ai-controls.md) implemented with all live requests disabled. 54 backend tests pass. B019 Done following user “Approve B019” on 21 October 2026; O-07 actual live policy remains open. Earlier planning language above is retained as history.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B019-local-ai-controls.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b020"></a>
## B020 — Add local syntax/type, test, dependency and limited secret checks

- **User value:** Provide reliable checks before eligible merges.
- **Scope:** Add local syntax/type, test, dependency and limited secret checks
- **Non-goals:** No bypassing protections or remote workflow changes while deferred.
- **Acceptance criteria (user-revised local scope):** Clean local checks pass; a controlled failure returns nonzero and stops subsequent steps; coverage limits are recorded. Remote merge protection verification is deferred to RCI-01 before remote collaboration/merge or release
- **Dependencies:** G0-L and accepted B019 for the selected local slice. B004 remote controls and CI/merge verification are deferred to [RCI-01](remote-ci-handoff.md) before remote collaboration/merge or release.
- **Test plan:** Demonstrate controlled failing and passing checks; verify required-merge settings when authorised. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Sanitise CI output and scope workflow permissions/secrets. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-08; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User approved the local-only replan. [Local checks](../evidence/B020-local-checks.md) pass; B020 Done following user “Approve B020” on 21 October 2026. Original remote criteria are retained under RCI-01; B021 remains unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B020-local-checks.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b021"></a>
## B021 — Implement approved current-record dashboard queries and filter contracts

- **User value:** Return accurate, permission-filtered current-record aggregates.
- **Scope:** Implement approved current-record dashboard queries and filter contracts
- **Non-goals:** No Phase 2 schemas added solely to fill a card; no synthetic live metrics.
- **Acceptance criteria (unchanged build-order check):** Aggregates honour permissions and metric definitions; only meaningful delivered record types are counted
- **Dependencies:** G0/B008 and B020; Approved Phase 1 metric catalogue, available persisted record types, filter semantics and ownership rules. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Known synthetic dataset with differing permissions/filters; verify counts, empty sets and errors against approved definitions. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Prevent aggregate/count leakage across unauthorised records/clients. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-10; F02; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User approved the [synthetic-reference baseline](B021-local-dashboard-contract.md); implementation and 14 new unit tests delivered, 68 backend tests pass. [Actual PostgreSQL verification](../evidence/B021-local-dashboard.md) remains outstanding because Docker is unavailable. B021 Blocked; B022 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B021-local-dashboard.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b022"></a>
## B022 — Connect dashboard cards/lists with loading, empty and error states

- **User value:** Present real query outcomes clearly.
- **Scope:** Connect dashboard cards/lists with loading, empty and error states
- **Non-goals:** No hard-coded production figures or fabricated integrations.
- **Acceptance criteria (unchanged build-order check):** AC-F02-01–AC-F02-03 pass; fixtures are labelled and query errors do not display invented counts
- **Dependencies:** G0/B008 and B021; B021 contracts; O-11 labels/tokens; approved fixture labelling. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Exercise F02-01 through F02-03 with loading/empty/error/unavailable states and retained filters. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Errors must not expose payloads or convert unknown counts into zero. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-10; F02; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User selected B022; approved B021 reference scope, B015 styling and isolated session pattern reused. [Local implementation and verification](../evidence/B022-local-dashboard-ui.md) delivered; Done for local scope following user “Approve B022” on 21 October 2026. Full production/staging and independent review prerequisites remain outstanding. B023 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B022-local-dashboard-ui.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b023"></a>
## B023 — Prepare reviewed staging service/configuration manifests and deployment instructions

- **User value:** Make staging prerequisites reviewable before spending or deployment.
- **Scope:** Prepare reviewed staging service/configuration manifests and deployment instructions
- **Non-goals:** No provisioning, secret population or deploy.
- **Acceptance criteria (unchanged build-order check):** Database, secret, CORS, redirect, worker and cost requirements are reviewable; configuration contains no live secrets
- **Dependencies:** G0/B008 and B022; Approved topology, origins/redirects, secret ownership, service sizing/cost and operations decisions. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Validate manifests/instructions against approved constraints; check placeholders and separate environments. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** No live secrets in manifests; identify every paid/external action and required authority. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-09; F20; O-03/O-16/O-17; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User selected B023. [Preparation pack](../../deployments/staging/README.md) and [validation evidence](../evidence/B023-staging-preparation.md) delivered; Done for local preparation following user “Approve B023” on 21 October 2026. Executable manifest, approved topology/values/owners/budget and staging runtime integration remain unresolved before deployment. B024 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B023-staging-preparation.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b024"></a>
## B024 — Provision authorised staging resources and deploy the reviewed foundation

- **User value:** Establish an authorised isolated staging foundation.
- **Scope:** Provision authorised staging resources and deploy the reviewed foundation
- **Non-goals:** No production deployment or assumption that a draft manifest permits spending.
- **Acceptance criteria (unchanged build-order check):** Separate approved DB/secrets, HTTPS and access restrictions are verified; actual deployment evidence is recorded
- **Dependencies:** G0/B008 and B023; Fresh explicit provisioning/deployment authority; budget owner and ceiling; verified account rights; reviewed B023. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Record actual service/DB health, HTTPS, restricted access and environment separation when authorised. Record actual results, failures and mock/live distinctions; see reconciled execution evidence below for actual local checks; this is the test plan, not a missing current run.
- **Security implications:** Keep staging credentials/data separate; record recovery and failure handling. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-09; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current local outcome — 21 October 2026:** User explicitly selected a separate local staging rehearsal. [Execution evidence](../evidence/B024-local-rehearsal.md): dedicated retained PostgreSQL, production-mode frontend, explicit-CA HTTPS/access/readiness/recovery checks passed. Done for local scope following user “Approve B024” on 21 October 2026. Original hosted deployment and independent-review prerequisites remain deferred. B025 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B024-local-rehearsal.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b025"></a>
## B025 — Establish foundation backups, restoration procedure and migration rollback assessment

- **User value:** Demonstrate recoverability before relying on stored data.
- **Scope:** Establish foundation backups, restoration procedure and migration rollback assessment
- **Non-goals:** No production destructive drill or assumption backup existence proves recovery.
- **Acceptance criteria (unchanged build-order check):** Disposable restore drill succeeds; documented rollback distinguishes app image from database recovery
- **Dependencies:** G0/B008 and B024; Approved retention/recovery targets, backup access and safe restore destination; migration rollback policy. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Run disposable backup/restore and verify recovered records; assess app rollback separately from schema/data recovery. Actual local snapshot/restore and eight recovery/control groups passed; full local check runner passed. See [B025 evidence](../evidence/B025-local-recovery.md).
- **Security implications:** Backup/restore copies retain access and data-class restrictions. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** P1-05/P1-09; F20; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local outcome:** Done for the verified local scope following user “Approve B025” on 21 October 2026. User “Start B025” selected the retained local synthetic rehearsal. Consistent backup restored to a separate fresh target with exact record fingerprints; destination access/session/audit controls and failed-migration atomicity passed. [Recovery runbook](../../deployments/local-rehearsal/recovery.md) distinguishes application rollback from database recovery. Keep the manual snapshot and destination until explicit cleanup instruction. Hosted retention/cadence and RPO/RTO, off-machine recovery and independent review remain outstanding; local timings establish no recovery guarantee. B026 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B025-local-recovery.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b026"></a>
## B026 — Verify staging UI/API/DB, direct-record denial and secure configuration

- **User value:** Prove the integrated foundation behaves securely.
- **Scope:** Verify staging UI/API/DB, direct-record denial and secure configuration
- **Non-goals:** No acceptance inferred from unit tests or mocked deployment.
- **Acceptance criteria (unchanged build-order check):** AC-F20-01 and applicable AC-F01-02 pass; issues remain open until resolved or accepted within permitted risk rules
- **Dependencies:** G0/B008 and B025; Actual authorised staging; approved auth/record rules; test accounts/data permission. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Exercise AC-F20-01 and applicable AC-F01-02; check direct-record/API denial and configuration. Record actual results, failures and mock/live distinctions; local checks are recorded in [B026 evidence](../evidence/B026-local-foundation.md).
- **Security implications:** Do not use real-client records; report failures and unresolved defects. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** F01/F02/F20; AT-01; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local outcome:** Done for retained synthetic rehearsal verification following user “Approve B026” on 21 October 2026: six HTTPS/API/DB groups, full local CI and supplemental B022 shared-component browser checks passed. B026-OBS-01 initial browser login failure recovered after explicit logout/retry; cause unproven and observation remains open. Full hosted AC-F20-01, trusted browser HTTPS journey, real identity and independent review remain deferred. B027 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B026-local-foundation.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b027"></a>
## B027 — Verify accessible shell/dashboard, operational logs and local setup handover

- **User value:** Make the foundation accessible and supportable.
- **Scope:** Verify accessible shell/dashboard, operational logs and local setup handover
- **Non-goals:** No unsupported accessibility claim or inferred staging-log availability.
- **Acceptance criteria (unchanged build-order check):** Keyboard/screen-reader/responsive evidence exists; staging logs and documented setup are usable
- **Dependencies:** G0/B008 and B026; Approved UI scope/tokens and supported test environments; actual staging logs and setup guide. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Record keyboard, screen-reader and responsive checks; follow setup guide and inspect redacted operational logs. Record actual results, failures and mock/live distinctions; actual local results and limits are recorded in [B027 evidence](../evidence/B027-accessibility-setup.md).
- **Security implications:** Use permitted fixtures; keep private data out of screenshots and handover evidence. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. 
- **Design / traceability:** F02/F19/F20; D005/D008; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Local outcome:** Done for verified local scope following user “Approve B027” on 21 October 2026. Fresh isolated dependency setup, CI/build, retained PostgreSQL and integrated rehearsal passed; actual redacted logs are usable. Keyboard, accessibility-tree semantics and mobile/desktop evidence recorded. Spoken screen-reader walkthrough remains outstanding; hosted logs, independent review and G1 sign-offs remain deferred. B026-OBS-01 stays open. B028 unstarted.


- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B027-accessibility-setup.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

<a id="b028"></a>
## B028 — **G1: Demonstrate and accept the foundation**

- **User value:** Obtain a documented foundation acceptance decision.
- **Scope:** **G1: Demonstrate and accept the foundation**
- **Non-goals:** No automatic Phase 2 start or production approval.
- **Acceptance criteria:** Adopted G1-L v0.1 local milestone accepted. Original full-G1 check preserved: Justice technical and CEO functional acceptance recorded; Phase 2 still requires its scope/issue approval
- **Dependencies:** G0/B008 and B027; B009–B027 evidence; Justice technical and CEO functional reviewers; unresolved-defect disposition. The numeric predecessor is a sequencing dependency; named controls above are additional substantive dependencies.
- **Test plan:** Demonstrate signed-in staging UI/API/DB, mock adapter, accurate dashboard and checks; record human outcomes. Record actual results, failures and mock/live distinctions; current local demonstration and full local runner passed; see [B028 review](../evidence/B028-foundation-review.md). Required human outcomes remain pending.
- **Security implications:** Missing required sign-off or unresolved critical control gaps prevent gate exit. Follow [B006 policy](../policies/allowed-data-and-test-fixtures.md).
- **Owner / reviewer:** Accountable owner: Justice, interim implementation owner/product-scope approver; acceptance confirmed by the user on 21 October 2026. This does not supply technical/independent/CEO review. Actual local executor: Codex under recorded user task selection; user accepted each bounded local result. Formal Justice technical/eligible independent review remains pending; another eligible human must review Justice-authored work. CEO functional sign-off also required.
- **Design / traceability:** P1-01–P1-10; D006; [feature specification](../../feature-spec.md), [architecture pack](../adr/README.md), [Phase 1 design boundaries](phase-1-design-operations.md).
- **Estimate / target date:** Unset; assess after architecture and assignment review. No approved schedule.
- **Current outcome:** Done for adopted G1-L v0.1 following user “Adopt G1-L v0.1 and accept B028 for local scope only”; original full G1 Hold. Review pack and current synthetic TLS/API/DB/dashboard/mock demonstration completed. Justice technical, CEO functional and eligible independent review/full-scope assurance are not recorded. [G1-L v0.1](G1-local-foundation-proposal.md) is adopted for the local milestone only; [reassessment](../evidence/B028-g1-local-adoption.md) preserves full G1 and all deferrals. B029 unstarted.


## User approval — 20 October 2026 UTC

User: “Approve B007”. Approval of the local planning pack is recorded, covering the refined work-item structure, proposed scope/operational boundaries, interim Justice nomination and proposed cadence. This does not select unanswered design/architecture options, establish Justice's assignment acceptance or technical sign-off, identify an eligible independent reviewer, or authorise spending or GitHub access.

B007 remains In review because its unchanged completion check requires work items satisfying Definition of Ready. Outstanding scope/design and technical decisions must receive explicit outcomes or valid deferrals; the user approval is not represented as proof those readiness gaps are resolved. G0/B008 is a separate execution gate and remains unstarted. No implementation or successor task is authorised.


20 October 2026 UTC: B010 title/check updated to the user-approved preparation scope. Earlier blanket readiness statements describe the B007 planning snapshot; current task outcomes are in progress.md. Full fresh-setup verification is retained at B027 before G1, with component checks at B011/B012/B015–B016.


Current B021 update — 21 October 2026: actual PostgreSQL 17.11 verification passed all 15 harness checks after Docker recovery and approved image download; full local checks passed. Earlier unavailable-runtime statements are historical. B021 is approved and Done for local scope; B022 unstarted. The test container was already removed before the user requested no cleanup; retain future test containers and adjust the automatic-cleanup harness before reuse. See the B021 evidence and progress tracker.


## B021 local deliverable approved — 21 October 2026

User: “Approve B021”. B021 is Done for the verified local synthetic-reference dashboard queries and filters. Existing 68 backend tests, 15 actual PostgreSQL checks and full local check runner passed; no tests rerun for this documentation-only acceptance. Earlier blocked/pending-acceptance wording is historical and superseded. B022 remains unstarted. Business metrics and frontend/API exposure remain outside this accepted scope; GitHub/RCI-01 remains deferred. Retain future test containers unless the user asks otherwise and keep approvals in chat. Pre-approval records: docs/evidence/B021-before-acceptance.zip.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.


## B023 local preparation approved — 21 October 2026

User: “Approve B023”. The local staging preparation pack is accepted; B023 Done for that scope. Existing draft validation and eight rejection checks retained; no tests rerun for documentation-only acceptance. Earlier pending-review wording is superseded for local preparation. Provider, exact configuration, ownership/budget, target runtime integration and independent review remain unresolved before deployment. Manifest stays draft-not-deployable and deployment_authorized=false; no spending, secret population, GitHub, provisioning or B024 authority is inferred. B024 remains unstarted. Preview/database were left untouched. Prior records: docs/evidence/B023-before-acceptance.zip.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.


## B026 local verification approved — 21 October 2026

User: “Approve B026”. B026 is Done for the verified local foundation scope. Six live check groups, the full local runner and supplemental browser evidence are retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. B026-OBS-01 remains open with cause unproven; approval does not resolve it. Hosted staging, trusted-browser HTTPS, real identity, remote CI and independent review remain deferred. Existing previews, backups and database resources were left untouched; no cleanup. B027 remains unstarted. Prior records: docs/evidence/B026-before-acceptance.zip.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.

- **Reconciled current record — 21 October 2026:** Done for the exact accepted local scope. [Execution/acceptance evidence](../evidence/B028-g1-local-adoption.md); [authoritative status](../../progress.md). Full-scope reviews/operations retain common and task-specific checkpoints; no new execution or external authority.

