# CPA Build Order

**Organisation:** Dwen Tech Ltd  
**Product:** Chief Product Architect AI Laboratory  
**Version:** 1.1 draft  
**Date:** 21 October 2026 (Atlantic/Reykjavik)  
**Classification:** Confidential — Internal  
**Status:** Proposed sequence; CEO product approval and Justice technical review pending

This document orders CPA delivery into small, reviewable tasks from baseline reconciliation to the foundation, Idea Studio MVP and subsequent capabilities. Use it with [blueprint.md](blueprint.md), [feature-spec.md](feature-spec.md) and the original [development roadmap](CPA_Development_Handover_Pack_v1/docs/006-development-roadmap-sprint-backlog.md). The foundation and Idea Studio together constitute the MVP.

Task status is recorded in [progress.md](progress.md); this file defines scope and sequence rather than live completion. Current status and acceptance are maintained there. No application, repository access, credentials, live integration, staging environment, acceptance result or production readiness is established by this document. Drafting a build order does not authorise implementation, paid service provisioning or release.

**Current local working instruction:** Use this existing `002 CPA` folder and `progress.md`. All GitHub activity is deferred: no remote access, clone, pull, merge or modification. References to GitHub issues, branches, PRs and remote checks below describe the deferred delivery workflow, not a prerequisite for the currently selected local documentation task. B001 was accepted by the user; later tasks and gates need their own evidence.

## 1. How to execute this order

1. Justice and the product owner approve the applicable scope and blocking decisions. Justice creates/refines an issue for the selected task with owner, acceptance criteria, non-goals, test plan and security implications.
2. Complete only the selected task or explicitly authorised batch. Do not start a successor merely because its predecessor is complete.
3. For current local work, use this existing folder as explicitly selected by the user. It is not a checked-out remote branch. The original feature-branch workflow from `develop` is deferred with all GitHub activity.
4. Include relevant tests and documentation with each functional task. Later verification tasks integrate and exercise the journey; they do not postpone unit, permission or failure tests.
5. Record local changes, checks and user review in progress.md for currently selected documentation tasks. The issue-linked PR workflow is deferred; do not claim it occurred. Staging and release acceptance remain separate later requirements.
6. Stop at the task boundary and report the result, unresolved issues and next eligible task. Phase gates require recorded technical and business acceptance before the next phase is activated.

Task IDs B001–B105 are local planning identifiers, not GitHub issue numbers. P1-01 through P5-07 retain the original handover backlog IDs. F01–F20 and AC-Fxx-nn refer to the feature specification. G0–G6 are gates defined here.

### 1.1 Dependency rule

The default order is strictly numeric: B002 depends on B001, B003 on B002, and so on. Each gate row blocks all subsequent tasks until its exit is recorded. This deliberately conservative sequence avoids hidden dependencies; it is not a claim that all work is inherently serial. Justice may approve a reordered/parallel plan only after recording its explicit dependencies and preserving the gates. Task selection never bypasses scope, rights, credential or release approval.

If a task proves too broad for one reviewed change, split it into documented subtasks before implementation and preserve its parent acceptance criteria. Do not mark it complete while required work remains.

### Controlled exception — B005 local review, 20 October 2026 UTC

The user explicitly instructed: “Start B005 as a controlled exception while B004 remains blocked and should work on B005 that is independent of B004”. This direct instruction authorises only the local architecture review despite the default numeric dependency. It is user execution authority, not a claimed Justice technical approval.

Accepted B001–B003 and the supplied local requirements support this review. B004 remains Blocked: repository access, protections, MFA, reviewer eligibility, remote code alignment and PR #2 outcome remain unverified. B005 may review logical stack choices, application identity/roles/tenancy, environment separation and service boundaries without those claims. See [ADR review pack](docs/adr/README.md).

No GitHub access, clone, pull, merge, remote modification, provisioning, implementation or live-provider use is authorised. Justice's B005 decision requirement and product-owner authority for business grants remain unchanged. G0 still requires access foundations and reviewer workflow; the exception does not clear B004, approve a gate, authorise B006 or reorder any other task.

### Subsequent user selection — B006 local policy preparation

On 20 October 2026 UTC, after accepting the B005 local deliverable, the user instructed “Start B006”. This later direct instruction authorises local preparation of B006's policy despite B005's outstanding Justice review. It supersedes the earlier stop-before-B006 instruction only for this documentation work. It does not mark B005 Done, extend the B005 exception to remote activity, or claim Justice approved a general reorder.

Prepare architecture-independent data/fixture, secrets and source/IP boundaries; keep O-04-dependent controls provisional. B004 stays Blocked and B005 In review. Required policy approvals and all phase gates remain in force. No live data, external access, implementation or provisioning is authorised. Stop before B007.

### Subsequent user selection — B007 local refinement

The user instructed “Start B007” after approving B006's limited local policy. This authorises local Phase 1 work-item/design/operations refinement and recording outstanding approvals. It does not clear B004, complete B005, approve implementation or bypass G0. B007's original Definition of Ready completion check remains unchanged. No external access or paid action is authorised; stop before B008.

### Subsequent user selection — B008 local gate assessment

The user instructed “Start B008”. This authorises assessment and recording of current local G0 evidence, not gate acceptance or clearance of B004/B005/B007 gaps. [B008 assessment](docs/evidence/B008-g0-readiness-assessment.md) records the outcome; the original G0 completion check and task definitions remain unchanged. No GitHub connection or implementation is authorised. Stop before B009.

### Adopted G0-L — local-only entry gate

On 20 October 2026 UTC the user approved [G0-L version 0.1](docs/planning/G0-local-only-proposal.md) and its B009 local structure/reference scope, retained all restrictions/deferred reviews, and instructed reassessment without starting B009. [Reassessment](docs/evidence/B008-g0-local-reassessment.md) passed the limited gate.

For explicitly selected, sufficiently specified local slices only, completion of B004/B005/B007 is no longer a blanket entry prerequisite. Their unresolved substantive decisions still block affected work. Later numeric ordering remains unchanged; reaching a remote-dependent task such as B020 requires a separate scoped replan, not silent skipping. No GitHub connection, live service, real-client data or deployment is permitted.

**Original full-G0 checkpoint preserved:** Reconciled documents, reviewed architecture/access foundations, approved Phase 1 issues and human review workflow; CEO confirms scope, Justice confirms technical readiness/reviewer workflow, and unresolved foundation blockers prevent exit. These requirements remain before applicable remote/shared integration or deployment, together with fresh user authority. G0-L is not evidence they passed. G1–G6 are unchanged. Stop before B009 until separately selected.

### Adopted G1-L — local foundation milestone

On 21 October 2026 the user explicitly chose “Adopt G1-L v0.1 and accept B028 for local scope only”. [Adopted scope](docs/planning/G1-local-foundation-proposal.md) and [reassessment](docs/evidence/B028-g1-local-adoption.md) record PASS for the limited local foundation milestone. B028 is Done **for G1-L only**.

Original full G1 remains **Hold**. Its secure signed-in staging assurance, Justice technical and CEO functional acceptance, eligible independent review and unresolved-control disposition are retained, not claimed passed. The earlier G0-L statement preserving G1 unchanged describes the original checkpoint; this subsequent adoption adds only the explicit local milestone. B004/B005/B007 statuses and every stated deferral remain unchanged.

Only separately selected, sufficiently specified local work may follow. B029 is **not started**; Phase 2 workflow/source/queue/model/budget/scoring/export decisions still require their own approval. No GitHub/cloud/live-provider/real-data/remote-CI/release or deployment authority is created. Spoken-reader verification, B026-OBS-01 and the original review/operational checkpoints stay open. Preserve all services/data; no cleanup.

### 1.2 Evidence and progress records

The user selected progress.md as the local ledger. B003 record maintenance is documented in progress.md Section 3.1, with [decisions.md](decisions.md) and [risks.md](risks.md); acceptance status is in progress.md. Keep task definitions here and actual status/evidence in progress.md. No additional tracker or remote adoption is needed to close the local B001 inventory.

For each task record:

```text
Task ID and linked approved issue
Status: Not started | Ready | In progress | Blocked | In review | Done
Owner and approved scope
Dependencies and decision/ADR references
Changed files and PR/commit reference
Commands/checks and actual outcomes
Demonstration or deployment evidence, if applicable
Migration, backup and rollback evidence, if applicable
Known defects, blockers and residual risks
Reviewer and acceptance references
Next eligible task and handoff
```

Do not include secrets, private client records or restricted research content in evidence. A failed check is recorded as a failure; a mocked provider result is labelled mocked. All gates are pending until signed evidence exists.

## 2. Resolve source inconsistencies before coding

B001 identified R01–R08. B002 records corrections in [the reconciliation report](docs/evidence/B002-baseline-reconciliation.md):

- R01: blueprint schedule explicitly labelled illustrative; estimates remain open under O-18.
- R02: O-01–O-18 references aligned in blueprint, feature spec and progress tracker; no underlying decision approved by adding labels.
- R03: user confirmed a human developer with AI assistance during B002; no named developer/access assignment is inferred.
- R04: actual local source paths documented; original handover pack preserved.
- R05: user confirmed all five recommendations during B002: Continue, Improve, Pivot, Pause and Stop. Detailed meanings and consequences remain for later approved rules.
- R06: stack/schema/API/provider proposals explicitly remain subject to ADR review.
- R07: status list corrected to avoid implying automatic transitions; transition policy remains open under O-09.
- R08: progress.md is the user-selected local tracker; B003 recordkeeping status is in progress.md.

The current local-only instruction supersedes earlier remote prerequisites for this selected documentation work. B004 remote checks remain deferred, not completed or silently skipped; any future change to task ordering must be recorded when that boundary is reached. All gates remain pending.

## 3. Gates and release boundary

| Gate | Task | Required decision or evidence |
| --- | --- | --- |
| G0-L Local-only entry (revised G0 scope) | B008 | User-approved local scope/deferrals, sufficiently specified first local slice, task-specific decisions, review limitations and preservation checks; original full-G0 assurance deferred as above |
| G1-L Local foundation milestone | B028 | User-adopted G1-L v0.1 local criteria and preserved deferrals; accepted for local scope only; original full G1 remains Hold |
| G1 Foundation accepted | B028 | Secure signed-in staging UI/API/database, tested adapter mock, real-record dashboard, passing checks and phase acceptance |
| G2 MVP accepted | B056 | Complete idea → analysis → challenge/revision → versioned dossier → export/retrieval → human review journey and failure/access evidence |
| G3 Portfolio accepted | B066 | Product registry, scenarios, critical challenge and human decision history verified |
| G4 Voice and Discovery accepted | B081 | Permissioned saved voice and confidential client workflow, consent and outbound approval verified |
| G5 Advanced capabilities accepted | B099 | Approved scoped/scheduled research, academic analysis and commercial modelling verified with rights/coverage/cost controls |
| G6 Production launch accepted | B104 | Release-specific privacy/security/recovery/operational evidence plus Justice technical and CEO release approval |

**G2 is the MVP completion point.** G3–G5 extend the product through separate scope approvals. G6 is required for any production launch, including an MVP launch; it is not necessary to build Phases 3–5 before releasing an approved MVP. For an earlier approved release, execute the relevant B100–B105 release lane immediately after its accepted phase, documenting skipped/deferred feature scope. Their dependency is the accepted release scope, not mandatory completion of every later feature. Return to the next separately approved phase afterwards. Every future release repeats the applicable release checks.

## 4. Preparation and baseline

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B001 | Inventory current planning files and verified target repository; record source differences, versions and baseline status | Blueprint; feature spec Sections 1/10; D001–D010 | Source/path register exists; Gantt dates, team conflict and missing O-label mapping are explicitly recorded |
| B002 | Obtain/record product and technical decisions on baseline conflicts; align approved requirement references | O-01; blueprint Section 20; D010 | No contradictory rule is silently selected; unresolved items have owners and dependent work remains blocked |
| B003 | Establish authoritative progress, decision and risk records with task/issue links | O-18; D006, D010 | Ledger location and status meanings are documented; no historical completion is fabricated |
| B004 | Verify CPA repository, memberships, MFA, protected branches, reviewer eligibility and actual PR #2 outcome | O-02; handover checklist; D007/D010 | Read-only verification is recorded; unprovisioned access and unresolved review requirements are identified |
| B005 | Review core architecture ADRs: frontend/API/database, identity/roles/tenancy, environments and service boundaries | P1-01; F01/F20; O-03/O-04 | Justice records decisions/options/trade-offs; no provider is selected by assumption |
| B006 | Define initial privacy, secrets, source/IP and client-isolation boundaries for foundation/MVP | F01/F05/F19/F20; O-06/O-12 | Approved allowed-data/test-fixture policy exists; sensitive/live client use remains prohibited until its required review |
| B007 | Refine and approve Phase 1 issues, design scope, operational prerequisites and review cadence | P1-01; O-11/O-16/O-17/O-18; D006 | Issues satisfy Definition of Ready; service costs/actions requiring authority are identified; no invented dates or budgets |
| B008 | **G0-L: Record limited local readiness acceptance** | D006/D010; adopted G0-L v0.1 | User approves local scope and explicit deferrals; first selected local slice has accountable ownership, sufficient approach/checks and preservation plan; unresolved decisions block affected work; original full-G0 assurance remains deferred |

### B010 scoped acceptance and executable verification handoff

On 20 October 2026 UTC the user instructed “Approve and Accept B010” after the proposed revision from full fresh-setup verification to local setup preparation. This adopts that narrower milestone. The original B010 check (fresh setup works with approved runtime versions) is retained as deferred verification, not reported passed. See [acceptance record](docs/evidence/B010-local-setup.md).

| Required verification | Responsible task / checkpoint |
| --- | --- |
| Backend startup, health/API behaviour and approved dependency/runtime compatibility | B011, when separately selected |
| Database connectivity and migrations in an authorised disposable environment | B012, only after user lifts database-setup deferral and approves approach |
| Frontend startup and approved UI/backend sign-in/access integration | B015–B016, when separately selected |
| Repeatable fresh isolated setup walkthrough covering the delivered foundation, locked dependencies, approved configuration and checks | B027 local setup handover; must be evidenced before B028/G1 acceptance |

Justice remains technical authority for these checks; each selected task records its executor and results. Resolve the PowerShell execution-method problem before relying on the script, or document and verify an authorised alternative. No execution-policy change is authorised here. G1's staging requirements are unchanged; a local walkthrough is not staging evidence. Database setup remains deferred, runtimes remain provisional and no install/download or B011 start is implied.

### B020 local-only replan — 21 October 2026

User: “Keep everything local till github comes in later”, selecting the proposed local-only B020 option. B020's completion check is revised to the verified local runner scope. The original check — “Controlled failing check blocks eligible merge; clean checks pass; branch requirements match verified settings” — remains required as [RCI-01](docs/planning/remote-ci-handoff.md) before remote collaboration/merge or release. No remote control is marked verified or waived. B004 stays Blocked for remote verification.

This is the explicit scoped replan required by G0-L for B020. Later local tasks may be separately selected against their own substantive prerequisites; no blanket execution authority, B021 start or staging/release gate approval is implied. The user subsequently said “Approve B020” on 21 October 2026, accepting its verified local deliverable. RCI-01 remains outstanding.

## 5. Phase 1 Foundation

Foundation provides secure infrastructure and a modest dashboard, not an operational global lab. Test fixtures must be labelled; dashboard cards expand only when their underlying modules exist.

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B009 | Prepare approved repository structure and import handover/ADR references at valid paths | P1-02; F20 | Meaningful files and working source links exist; original material is preserved |
| B010 | Prepare Windows-compatible local setup guidance and placeholder configuration | P1-02; F20 | Provisional tooling and local setup guidance recorded; `.env.example` contains placeholders only; known launch/database limitations and later executable-verification checkpoints are explicit |
| B011 | Add FastAPI startup, health contract and initial OpenAPI/error structure | P1-04; F20 | Health and error checks pass; public health response leaks no secrets |
| B012 | Add PostgreSQL connectivity and versioned migration workflow | P1-05; F20 | Apply/reapply checks pass; recovery/rollback implications are demonstrated on disposable data |
| B013 | Implement identity/user references and the approved role/record authorisation boundary | P1-05/P1-06; F01 | Permission tests deny unauthorised records; tenancy assumptions are explicit before client records exist |
| B014 | Implement approved authentication/session validation in the backend | P1-06; F01 | AC-F01-01 passes; invalid/expired credentials cannot obtain protected responses |
| B015 | Build responsive Next.js navigation shell with accurate feature availability | P1-03; F02 | Routes/state labels reflect delivered scope; keyboard/focus checks pass; no fake service availability |
| B016 | Connect sign-in/session and access-denied UI to backend permissions | P1-03/P1-06; F01/F02 | Permitted sign-in journey works; direct API denial remains effective independently of the UI |
| B017 | Implement initial audit events and redacted operational request logging | F19/F20; D007/D009 | Actor/resource/action/time are retained for defined actions; secrets and private payloads are absent from logs |
| B018 | Define AI adapter interface, output/error contracts and mock provider tests | P1-07; F06 | Success, timeout, refusal and malformed fixtures behave predictably; no live call is needed |
| B019 | Implement baseline configuration/usage hooks and fail-closed live-AI enablement | P1-07; F19; O-07 | Missing model/credential/budget configuration cannot trigger an uncontrolled paid call; unknown cost is not reported as zero |
| B020 | Add local syntax/type, test, dependency and limited secret checks | P1-08; F20; RCI-01 deferred | Clean local checks pass; a controlled failure returns nonzero and stops subsequent steps; coverage limits are recorded. Remote merge protection verification is deferred to RCI-01 before remote collaboration/merge or release |
| B021 | Implement approved current-record dashboard queries and filter contracts | P1-10; F02 | Aggregates honour permissions and metric definitions; only meaningful delivered record types are counted |
| B022 | Connect dashboard cards/lists with loading, empty and error states | P1-10; F02 | AC-F02-01–AC-F02-03 pass; fixtures are labelled and query errors do not display invented counts |
| B023 | Prepare reviewed staging service/configuration manifests and deployment instructions | P1-09; F20; O-03/O-16/O-17 | Database, secret, CORS, redirect, worker and cost requirements are reviewable; configuration contains no live secrets |
| B024 | Provision authorised staging resources and deploy the reviewed foundation | P1-09; F20 | Separate approved DB/secrets, HTTPS and access restrictions are verified; actual deployment evidence is recorded |
| B025 | Establish foundation backups, restoration procedure and migration rollback assessment | P1-05/P1-09; F20 | Disposable restore drill succeeds; documented rollback distinguishes app image from database recovery |
| B026 | Verify staging UI/API/DB, direct-record denial and secure configuration | F01/F02/F20; AT-01 | AC-F20-01 and applicable AC-F01-02 pass; issues remain open until resolved or accepted within permitted risk rules |
| B027 | Verify accessible shell/dashboard, operational logs and local setup handover | F02/F19/F20; D005/D008 | Keyboard/screen-reader/responsive evidence exists; staging logs and documented setup are usable |
| B028 | **G1: Demonstrate and accept the foundation** | P1-01–P1-10; D006 | Adopted G1-L v0.1 local milestone accepted; original Justice technical and CEO functional acceptance retained for full G1 (Hold); Phase 2 still requires its scope/issue approval |

## 6. Phase 2 Idea Studio MVP

This phase uses an approved limited research strategy. It does not require broad geography scanning, academic integration, voice or client website intake. Basic retrieval and baseline cost/evidence safeguards are part of the MVP.

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B029 | Resolve Phase 2 workflow, field validation, source strategy, queue, model/budget, scoring and export decisions; approve issues | F03–F10/F18/F19; O-05–O-10/O-12 | Required ADRs/business rules have owners and signed outcomes; no missing rating, transition or source rule is guessed |
| B030 | Add idea schema/migration and ownership constraints | P2-01; F03 | Approved fields/status/archive representation persist correctly; migration and record-denial checks pass |
| B031 | Implement idea create/read/edit/archive API with action-specific validation | P2-01; F03 | AC-F03-01–AC-F03-03 pass at API level; archive cannot bypass permissions or be reported successful on failure |
| B032 | Build idea list/editor and persisted draft workflow | P2-01; F03 | Save/retrieve/edit/archive journey works with field errors, empty states and preserved saved work |
| B033 | Add source/evidence schema and permitted MVP ingestion/parser | P2-03; F05 | Source metadata, rights and claim links survive retrieval; prohibited source use is rejected under policy |
| B034 | Add evidence inspector and hypothesis/no-source presentation | P2-03; F05 | AC-F05-01–AC-F05-03 pass, including untrusted-source fixtures and explicit unsourced warnings |
| B035 | Implement research-run persistence, approved state contract and idempotent job creation | P2-02; F04 | AC-F04-01/AC-F04-03 pass; persisted run ID and duplicate policy are reliable |
| B036 | Implement worker execution, timeout, bounded retry, cancellation and restart recovery | P2-02; F04/F20 | AC-F04-02/AC-F04-04 and AC-F20-04 pass under failure/restart fixtures; idea data is preserved |
| B037 | Implement per-run/user budget enforcement and AI usage metering for the analysis path | P2-04; F19 | AC-F19-01/AC-F19-02 pass, including concurrent/unknown-usage cases required by the approved policy |
| B038 | Implement versioned prompt/schema orchestration and structured assessment validation using mocks | P2-04; F06 | AC-F06-01–AC-F06-03 pass; model text cannot set authoritative human approval |
| B039 | Execute narrowly authorised live-adapter verification in staging, when approved | CPA-AI-001; F06/F19 | Real provider evidence is labelled separately from mocks; configured costs, redaction and error handling verified; no approval means task remains pending |
| B040 | Connect Analyse/progress/result UI to persisted runs and structured output | P2-02/P2-04; F04/F06 | Success/failure/partial states follow contract; model failure does not lose idea or falsely display a valid final dossier |
| B041 | Implement score calculation, validation and scoring-version/risk representation | P2-05; F08 | AC-F08-01–AC-F08-03 pass; complete/incomplete score policies and deterministic calculation are verified |
| B042 | Add scoring rationale, uncertainty, risk and missing-evidence UI | P2-05; F08 | Display agrees with calculation and evidence; no pass threshold or success probability is invented |
| B043 | Add dossier version schema and saved-version API | P2-06; F09 | AC-F09-01 passes; content/run/evidence relationships and historical versions remain retrievable |
| B044 | Implement Challenge assumptions orchestration and relationship to its source assessment | CPA-ID-001; F07 | AC-F07-01/AC-F07-03 pass; challenge failure preserves the saved assessment and review state |
| B045 | Add challenge/revise/save-version interface | F07/F09 | AC-F07-02 passes; reviewer can distinguish original, challenge and revised saved content |
| B046 | Implement review submission, approved transitions and authorised human decisions | P2-07; F09 | AC-F09-02/AC-F09-03 pass; decision actor/time/version retained; dossier review and investment authority remain distinct |
| B047 | Build review queue and approve/return/reject interface | P2-07; F09/F02 | Permitted reviewer can inspect sources and record outcomes; forbidden actions fail through direct API calls too |
| B048 | Implement export generation and private file retrieval for a selected dossier version | P2-08; F10 | AC-F10-01–AC-F10-03 pass; export preserves sources/assumptions and cannot leak through file URLs |
| B049 | Add export status/download interface and version identification | P2-08; F10 | Failed generation shows honest recovery; requested version cannot be confused with an earlier generated file |
| B050 | Implement permission-filtered basic Knowledge Hub/dossier-source retrieval | F18; CPA-KH-001 | AC-F18-01–AC-F18-03 pass for delivered record types; no restricted snippets or counts leak |
| B051 | Extend audit, permitted usage/settings and approved review notifications | P2-07; F19 | AC-F19-03/AC-F19-04 pass; recipients/preferences and content restrictions match the approved channel scope |
| B052 | Extend Command Centre with real idea/run/review/spend data | P1-10 extension; F02 | Lists and metric filters reconcile to stored accessible records; no later-module data is fabricated |
| B053 | Run complete MVP end-to-end and score/evidence/export regression suite | P2-09; F03–F10/F18/F19 | AT-02–AT-06, AT-08 and AT-10 pass; fixtures and any live verification are clearly distinguished |
| B054 | Verify MVP record isolation, injection/refusal handling and recoverable failures in staging | P2-09; F01/F04/F05/F06/F20 | Direct API/file/search denial, restart/failure and no-data-loss evidence recorded; critical defects block exit |
| B055 | Complete MVP accessibility/usability review and technical handover | P2-09; D005/D008/D010 | Keyboard, screen-reader and responsive journeys work; run/setup/support notes, defects and evidence are complete |
| B056 | **G2: Demonstrate and accept the Idea Studio MVP** | P2-01–P2-09; feature spec Section 9.1 | CEO accepts the full useful journey and Justice signs technical acceptance; production still requires the release lane |

## 7. Phase 3 Portfolio and stress testing

Start only after G2 and separate Phase 3 issue/scope approval. Portfolio product names do not establish actual development stage, commercial validation or ownership.

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B057 | Approve product schema/stages, recommendation vocabulary and scenario/review rules | F11/F12; O-09/O-10 | Improve/Continue/Pivot/Pause/Stop conflict resolved; approved issues and decisions recorded |
| B058 | Implement product registry schema/API and idea/evidence relationships | P3-01; F11 | AC-F11-01 passes; unknown product stage remains unknown and record permissions apply |
| B059 | Build portfolio list/detail/editor and review-history display | P3-01; F11 | AC-F11-02/AC-F11-03 pass; saved milestones/stages accurately reflected |
| B060 | Implement product review request and assessment persistence | P3-02; F12 | Review is tracked and linked to the selected product/idea and input/evidence version |
| B061 | Implement optimistic/base/pessimistic scenarios with approved inputs/formulas | P3-03; F12 | AC-F12-01 passes; scenarios disclose assumptions instead of inventing market/financial figures |
| B062 | Add product-specific critical challenge and evidence/counterargument output | P3-04; F12 | AC-F12-02 passes with curated approved product/hypothetical fixtures |
| B063 | Implement recommendation decisions and portfolio review history | P3-05; F11/F12/F09 | AC-F12-03 passes; AI recommendation cannot change investment authority or rewrite historical decisions |
| B064 | Build stress-test results, scenarios and decision panels; extend portfolio/dashboard links | P3-02–P3-05; F02/F12 | Permitted users can inspect evidence/assumptions before decision; unavailable data stays explicit |
| B065 | Run product-specific, permissions, failure and accessibility verification | P3-06; F11/F12 | AC-F11-01–AC-F11-03 and AC-F12-01–AC-F12-03 pass; phase evidence and defects recorded |
| B066 | **G3: Demonstrate and accept portfolio intelligence** | D006 Phase 3 | Existing-product assessment and human decision history accepted by Justice and CEO |

## 8. Phase 4 Voice and Client Discovery

Voice and Discovery have distinct permissions and data risks. A client-facing voice agent is not included automatically. No client response, notification or proposal is sent without the applicable human approval and authorised channel.

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B067 | Approve Phase 4 issues, consent/retention, voice transport and secured website/outbound contracts | F13/F14; O-12/O-13/O-14 | Provider, consent text, approved data, sender/reviewer authority and integration failure/duplicate rules recorded |
| B068 | Implement consent, session/transcript schema and retention/access controls | P4-01; F13 | Consent/history and session links persist; deletion/retention semantics and access checks are verified |
| B069 | Implement approved voice provider transport with permissioned backend integration | P4-02; F13/F19 | Approved mock/live tests show connection, usage and failure handling; no browser secret leakage |
| B070 | Build microphone/session UI and streaming transcript with honest availability states | P4-02; F13 | AC-F13-02 passes for microphone denial/disconnect; interruption only claimed if actually supported |
| B071 | Implement permission-filtered knowledge/project context in voice | P4-03; F13/F18 | AC-F13-03 passes; spoken requests cannot obtain restricted records or confer approval |
| B072 | Implement session summary/actions, project linkage and saved-session retrieval | P4-01/P4-03; F13 | AC-F13-01 passes; retained transcript/summary matches session and consent/retention policy |
| B073 | Implement Discovery client/enquiry/consent/reference schema and secured intake validation | P4-04; F14 | AC-F14-01 passes; reference, consent, duplicate and anti-spam rules follow contract |
| B074 | Connect approved website intake and verify receipt/failure semantics | P4-04; F14 | AC-F14-04 passes; no claimed receipt without persistence or false delivery confirmation |
| B075 | Implement client-isolated enquiry retrieval and internal queue API | P4-05; F01/F14 | AC-F01-03/AC-F14-02 and AT-07 pass before real client data is introduced |
| B076 | Build restricted enquiry queue/detail/triage interface | P4-05; F14 | Only authorised records/actions visible; direct URLs and API remain independently protected |
| B077 | Implement missing-information questions and solution proposal drafts with evidence/IP labels | P4-06; F14 | Draft content remains internal; reusable-product path requires recorded rights review |
| B078 | Implement version-specific human outbound approval and approved channel integration | P4-06; F14/F19 | AC-F14-03 passes; draft creation, retry or model text cannot trigger unapproved client sending |
| B079 | Extend permitted knowledge, notifications and dashboard links for delivered Phase 4 records | F02/F18/F19 | Restricted titles/snippets/notifications and client-private data do not leak across accounts |
| B080 | Verify voice/Discovery security, consent, failure recovery, usability and access | P4-07; F13/F14 | All Phase 4 ACs pass; anti-spam, false receipt, outbound approval and sensitive AI-input controls evidenced |
| B081 | **G4: Demonstrate and accept Voice and Discovery** | P4-01–P4-07 | Saved voice session and secure human-reviewed client journey accepted; unresolved privacy/security defects block exit |

## 9. Phase 5 Advanced research and modelling

Broad scanning requires approved sources, taxonomy, coverage semantics and limits. A Global selection is not a promise of complete world coverage. Academic access and commercial reuse require appropriate rights independently of source visibility.

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B082 | Approve Phase 5 issues, geography/schedule/source rights, modelling formulas and advanced evaluation | F15–F17; O-06/O-07/O-08/O-10/O-15 | Country/region/language/currency policy, quotas, licensed connectors and incomplete-model rules recorded |
| B083 | Implement geography catalogue and explicit region membership | P5-01; F15 | Country ISO references and Wales-within-UK representation verified; supported coverage is explicit |
| B084 | Build scope/sector/window/source/budget selectors | P5-01/P5-02; F15 | Country/multi-country/region/Global requests validate against supported taxonomy and permissions |
| B085 | Implement approved scan source collection/deduplication and actual coverage logs | P5-02; F15/F05 | Requested scope and actual countries/languages/feeds/windows are separately retained, including gaps |
| B086 | Implement scan opportunity extraction and human-review candidate persistence | P5-02; F15/F06/F08 | Candidates retain citations, hypotheses, scores and limitations; no automatic investment approval |
| B087 | Build results/evidence drill-down and candidate-to-idea promotion | P5-02; F15 | AC-F15-01–AC-F15-03 and AT-09 pass; promotion preserves source/run lineage |
| B088 | Implement coverage display and any separately approved heatmap | P5-02; F15/F02 | Colours correspond to approved measurable data; missing coverage cannot appear as low opportunity or full coverage |
| B089 | Implement authorised schedules, recurrence ownership and pause/cancel | P5-03; F15/F04 | Each scheduled run has identity, permissions, timezone and constrained budget; recurrence does not imply unlimited spend |
| B090 | Implement scheduled opportunity alerts with confidentiality/preferences | P5-03; F15/F19 | AC-F15-04 passes; alert rules/recipients are approved and failed/non-actionable results are accurately represented |
| B091 | Implement approved academic connector with rights/provenance persistence | P5-04; F16/F05 | AC-F16-01/AC-F16-02 pass; restricted material is not bypassed or falsely reported analysed |
| B092 | Build academic findings/uncertainty and potential-application review | P5-04; F16 | AC-F16-03 passes; findings and speculative software applications remain distinguishable |
| B093 | Implement commercial assumptions/model schema and deterministic calculation engine | P5-05; F17 | AC-F17-01/AC-F17-02 pass; units/currencies/formula versions and missing inputs are explicit |
| B094 | Build editable business model/scenario interface | P5-05; F17 | Edits recalculate under approved formulas; unknown market/price/cost remains unknown |
| B095 | Implement editable business-plan, investment-memo and pitch-outline generation | P5-06; F17/F10 | AC-F17-03 and export-access/source checks pass; no unsupported number, publication or financial commitment |
| B096 | Extend Knowledge Hub/search to approved academic, scan and modelling records | F18; CPA-KH-001 | Provenance/version links survive search; restricted indexing/retention checks pass |
| B097 | Implement agreed advanced groundedness/citation/contradiction/cost evaluation and guardrails | P5-07; F05/F06/F19 | Approved fixtures and thresholds exercise injection, refusal, schema, source quality, leakage and cost limits |
| B098 | Verify advanced end-to-end, coverage, source licensing, recovery and accessible UI | P5-07; F15–F17/F20 | All Phase 5 ACs and AT-09 pass; permitted mock/live evidence distinguished and operational limits exercised |
| B099 | **G5: Demonstrate and accept advanced capabilities** | P5-01–P5-07 | Approved recurring research, rights-aware academic analysis and editable modelling accepted by Justice and CEO |

## 10. Release lane for the accepted scope

This lane may follow G2, G3, G4 or G5 according to the approved release scope. B100 depends on that gate, not on completion of deferred phases. B101–B105 then run sequentially. All live changes remain subject to the source governance and applicable current authorisation.

| Task | Deliverable and scope | Traceability | Completion check |
| --- | --- | --- | --- |
| B100 | Define candidate version, included/deferred features, defect register and production success/recovery targets | F20; O-16/O-17; D008/D009 | Release scope and numeric performance/RPO/RTO/availability/cost targets are approved; deferred features honestly unavailable |
| B101 | Complete release security/privacy/access review and staging regression | F01/F20; D007/D008 | Applicable feature ACs and source ATs pass; no critical security/client-isolation failure; real-data/source rights reviewed |
| B102 | Demonstrate production backup/restore readiness, migration plan and rollback assessment | F20; D009 | Recovery evidence meets agreed targets; database migration compatibility and rollback/restore actions are reviewable |
| B103 | Finalise production configuration, monitoring/alerts, runbooks, access and support handover | F19/F20; D009 | Approved secrets/quotas/HTTPS/CORS/health controls verified without exposing values; accountable support and incident owners recorded |
| B104 | **G6: Obtain release-specific technical and CEO approval** | D007–D010 | Reviewed release PR/checks, Justice technical sign-off and CEO production release approval recorded; unresolved blockers prevent deployment |
| B105 | Deploy approved release, perform scoped production smoke checks and record handoff | F20; D009 | Approved version/configuration, health/auth/record-access/usage evidence recorded; rollback criteria followed on failure; production result never inferred from staging |

The blueprint's operational cadence remains applicable after handoff: daily error/cost/queue checks; weekly dependency/backup/alert review; monthly restore/access/retention/model-output review. Creating scheduled automations or sending messages is separate work requiring the appropriate explicit instruction; this plan does not create them.

## 11. Acceptance coverage and checkpoints

| Source acceptance scenario | Main implementation/checkpoint tasks |
| --- | --- |
| AT-01 Unauthenticated request rejected | B014, B016, B026; repeated in B101 |
| AT-02 Create/retrieve own idea | B030–B032, B053 |
| AT-03 Tracked analysis and stored output | B035, B038–B040, B053 |
| AT-04 Model failure without idea loss | B036, B040, B054 |
| AT-05 Reproducible score | B041–B042, B053 |
| AT-06 Unsourced claims flagged | B033–B034, B038, B053 |
| AT-07 Cross-client access denied | B075 before real client data; B080, B101 |
| AT-08 Export preserves sources/assumptions | B048–B049, B053; B095 for later outputs |
| AT-09 Actual geography coverage retained | B085, B087–B088, B098 |
| AT-10 Human investment approval | B038, B046–B047, B053; B063/B080 where applicable |

| Feature group | Main task coverage |
| --- | --- |
| F01 Authentication/access | B013–B016, B026, B054, B075, B101 |
| F02 Shell/dashboard | B015–B016, B021–B022, B027, B052 and module extensions |
| F03 Idea management | B029–B032 |
| F04 Run control | B035–B036, B040, B054 |
| F05 Evidence | B033–B034, B054 and later source connectors |
| F06 Structured AI | B018–B019, B038–B040 |
| F07 Challenge/revision | B044–B045 |
| F08 Scoring | B041–B042 |
| F09 Dossiers/review | B043, B045–B047 |
| F10 Exports | B048–B049, B095 |
| F11 Portfolio | B058–B059, B063–B065 |
| F12 Stress testing | B060–B065 |
| F13 Voice | B067–B072, B080 |
| F14 Discovery | B067, B073–B080 |
| F15 Geography/scanning | B082–B090, B098 |
| F16 Academic research | B091–B092, B098 |
| F17 Modelling | B093–B095, B098 |
| F18 Knowledge/search | B050, B071, B079, B096 |
| F19 Usage/audit/settings/notifications | B017–B019, B037, B051, B079, B090, B097, B103 |
| F20 Operations/recovery | Foundation, phase verification tasks and B100–B105 |

## 12. Stop and escalation rules

- Stop dependent work when a required business rule, source right, role grant, credential boundary or paid-service authority is unresolved. Record the precise blocker; continue only independent work within the selected authorised scope.
- Do not bypass protected branches, independent human review, phase acceptance or production approval.
- Do not solve unavailable evidence by inventing market figures, citations, source access, review signatures, live service status or passing test results.
- Preserve unknown financial inputs, scores, product stages and coverage as unknown under the approved policy. Do not interpret an unset cost cap as unlimited.
- Preserve saved ideas/dossiers during error recovery. Unknown submission or deployment outcomes need investigation and an explicit retry policy, not a blind replay.
- Treat provider calls, live client communications, production migrations and releases as distinct actions whose authority and evidence must be established.
- Update the decision register, feature specification and blueprint together when an approved decision changes their requirements. Resolve the source drift identified in Section 2 before claiming a settled baseline.

**Current selected planning task:** B002; see progress.md for its decision and review status.  
**Implementation status:** Not established.  
**All phase and release gates:** Pending.
