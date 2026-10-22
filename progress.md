# CPA Progress Tracker

**Organisation:** Dwen Tech Ltd  
**Product:** Chief Product Architect AI Laboratory  
**Version:** 7.4 draft  
**Last updated:** 21 October 2026 (Atlantic/Reykjavik)  
**Classification:** Confidential — Internal  
**Current stage:** Main reference dashboard connected and verified under direct user request; B007 local planning completed; G0-L accepted; B012–B014 Done; B015 local shell Done; B016 local integration Done; B017 local audit implementation Done; B018 local adapter Done; B019 local controls Done; B020 revised local scope Done; B021 verified local scope approved and Done; B022 verified local dashboard UI approved and Done; B023 local staging preparation approved and Done; B024 local rehearsal approved and Done; B025 local recovery approved and Done; B026 local verification approved and Done; B027 local support/accessibility approved and Done; B028 Done for adopted G1-L v0.1, original G1 Hold; remote CI deferred under RCI-01; B004 Blocked; B005 Done for approved local architecture

This file records task status, evidence, decisions, phase gates and handoffs against [build-order.md](build-order.md). Read [blueprint.md](blueprint.md) for product context and [feature-spec.md](feature-spec.md) for feature behaviour and acceptance criteria. The build order owns task definitions, dependencies and completion checks; this tracker owns recorded progress for this folder.

The user requested `progress.md`, so this is the selected tracker filename rather than the optional `build-progress.md` name mentioned in the build order. B003 establishes the local record workflow below with decisions.md and risks.md. The existing folder remains the working project; remote adoption is deferred.

**Current operating instruction — 20 October 2026:** The user accepted the B001 local inventory and selected `C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA` as the working project. All GitHub activity is deferred: do not access, clone, pull, merge or modify the remote repository. Historical remote evidence is retained only as history. This direct instruction governs current work where earlier repository/PR wording differs. The user accepted B002 and B003, then explicitly authorised B005 as a controlled exception limited to work independent of B004. B004 remains Blocked and GitHub activity deferred. The subsequent “Start B006” authorises local policy preparation with B005 review still pending. The user subsequently selected B007 for local refinement. The user subsequently selected B008 for local gate assessment. The user subsequently adopted G0-L v0.1; reassessment passed for limited local scope only. The user subsequently selected B009 for the approved local structure/reference slice. The user subsequently selected B010, approved provisional installed tooling and deferred database setup. The user subsequently selected B011 for local API startup/health/OpenAPI/error work. The user subsequently selected B012 for local database prerequisite review; the user subsequently confirmed the database deferral and selected read-only native PostgreSQL inspection first. The user subsequently selected B013; local access-boundary preparation only while database setup remains deferred and O-04 is unresolved. The user subsequently authorised disposable local PostgreSQL setup and actual B012 migration/recovery checks, superseding the earlier setup deferral for that scope. The user subsequently selected B014 for local authentication/session preparation; B013 and session-policy decisions remain unresolved. The user subsequently approved B013 to continue, authorising local synthetic implementation of matrix v0.1. The user subsequently approved B014 local session policy v0.1 for synthetic local implementation. The user subsequently selected B015 and approved offline-only installation and a derived local design baseline; implementation and local verification are complete. The user subsequently said “Accept B015”, accepting the local responsive navigation shell. The user subsequently selected B016 and approved the isolated synthetic journey and local cookie baseline. The user subsequently said “Accept B016”, accepting the verified isolated local integration. Real human login remains deferred. The user subsequently selected B017 and approved the local event and disposable storage baselines. The user subsequently said “Accept B017”, accepting its verified local audit/redaction scope. The user subsequently selected B018, authorised dependency installation, and said “Approve and accept B018” on 21 October 2026, accepting the tested local adapter scope. The user subsequently selected “Start B019”, authorising the local configuration/usage baseline with live calls still disabled. The user subsequently said “Approve B019”, accepting the verified local baseline on 21 October 2026. The user subsequently selected “Start B020” and answered “Keep GitHub deferred; prepare locally”. Local check preparation is authorised; remote verification remains deferred. The user subsequently instructed “Keep everything local till github comes in later”, approving a local-only B020 scope with original remote requirements preserved under RCI-01. The user subsequently said “Approve B020”, accepting the verified revised local scope on 21 October 2026. The user subsequently selected “Start B021” and approved the local synthetic-reference dashboard baseline. The user subsequently said “Approve B021”, accepting its verified local scope on 21 October 2026. The user subsequently said “Start B022”, authorising local dashboard connection to the approved B021 reference slice using existing styling and isolated session harness. The user subsequently said “Approve B022”, accepting its verified local scope on 21 October 2026. The user subsequently selected “Start B023”; local staging preparation is authorised, with external/provider decisions and deployment still deferred. The user subsequently said “Approve B023”, accepting the local preparation pack on 21 October 2026; deployment readiness and external authority remain unresolved. The user subsequently selected “Start B024” and chose “Keep it local: build and verify a separate staging rehearsal”. This authorises the separate synthetic local rehearsal, not cloud/GitHub deployment. The user subsequently said “Approve B024”, accepting the verified local rehearsal on 21 October 2026. The user subsequently selected “Start B025”, authorising a local backup and isolated restore drill within the retained synthetic rehearsal scope. The user subsequently said “Approve B025”, accepting the verified local recovery scope on 21 October 2026. The user subsequently selected “Start with B026”, authorising verification of the retained local rehearsal. The user subsequently said “Approve B026”, accepting the verified local scope on 21 October 2026 with B026-OBS-01 retained as an open observation. The user subsequently selected “Start B027” and authorised exact locked npm downloads for its isolated setup after cache-only installation failed. The user subsequently said “Approve B027”, accepting the verified local scope on 21 October 2026; spoken screen-reader verification remains outstanding. The user subsequently selected “Start B028”, authorising the foundation demonstration and gate review. Original G1 criteria remain unchanged; G1-L v0.1 is proposed only. The user subsequently chose “Adopt G1-L v0.1 and accept B028 for local scope only”, accepting the local milestone with full G1 held and every deferral preserved. The user subsequently requested “Let's work on B007”, reopening its pending planning review without reopening accepted local tasks or starting Phase 2. The user then confirmed Justice interim-role acceptance and approved the local task-by-task review cadence, resolving the remaining local B007 decisions. Stop before B029.

## 1. Current snapshot

| Measure | Recorded state |
| --- | --- |
| Build tasks | 105, B001–B105 |
| Done | 27 |
| In review | 0 |
| In progress | 0 |
| Ready | 0 |
| Blocked tasks | 1 — B004 remote verification deferred; RCI-01 also deferred |
| Not started | 77 |
| Recorded task completion | 27 / 105; task count is not a measure of effort or delivered product value |
| Active build task | None; B005 local architecture approved and Done |
| Next candidate | B029 awaits separate selection; deferred checkpoints remain binding |
| Approved issue / owner / branch | User approved B013 local continuation; Codex implemented/tested synthetic scope; formal reviews deferred; no remote activity |
| Phase approvals | G0-L and G1-L accepted for local scope only; original full-G0 assurance deferred; full G1 Hold; G2–G6 pending |
| Runtime, CI or acceptance results | Main dashboard follow-up: 79 source/config files, 70 backend tests, 5 runner tests, contract/types and separate production build passed; four real main-API groups and browser login/filter/navigation/reload/logout checks passed. |
| Staging / production | Local B024 and separate B027 rehearsals verified for scoped checks; hosted staging/production deferred |
| Approved schedule / budget | Not recorded |

**Evidence boundary:** The local planning files exist. Their existence establishes draft documentation, not approved requirements, completed build tasks or a working application. Repository membership, branch protection, PR #2, credentials and deployment statements from the handover pack remain unverified historical context. No external systems were checked at initialisation. During B001, a read-only GitHub metadata query verified the target repository identity, private visibility and default branch; membership/protection/PR checks remain unverified.

## 2. Planning documents and evidence

| Artifact | Local state | Approval / scope note |
| --- | --- | --- |
| [blueprint.md](blueprint.md) | Present; proposed baseline, version 1.2 draft | CEO product approval and Justice technical review pending in the document |
| [feature-spec.md](feature-spec.md) | Draft present, version 0.3; F01–F20 and 65 acceptance criteria | No criterion is claimed passed; B002 reference reconciliation accepted |
| [build-order.md](build-order.md) | Draft present, version 1.1; 105 tasks; G0-L/G1-L local scope adopted; original full-G1 checkpoint retained | Sequence and gates proposed; all build tasks initially unverified |
| [progress.md](progress.md) | Tracker updated for connected main dashboard follow-up, version 7.4 | Authoritative local status ledger; B003 workflow accepted; remote adoption deferred |
| [Original handover README](CPA_Development_Handover_Pack_v1/README.md) | Present | Source baseline, not completion evidence |
| [Original handover checklist](CPA_Development_Handover_Pack_v1/github/HANDOVER_CHECKLIST.md) | Present | Sign-off still needs actual evidence; no checkboxes inferred complete |

## 3. Status and update rules

| Status | Meaning |
| --- | --- |
| Not started | No task execution is recorded; prerequisites may still be unresolved |
| Ready | Approved issue, owner, scope, dependencies, decisions and test plan are sufficient to begin |
| In progress | The selected authorised task is being executed; record the current scope and evidence |
| Blocked | A specific impediment prevents the task proceeding; record impact, owner/required authority and unblock condition |
| In review | Required implementation/checks are available for the eligible human reviewer; acceptance is still pending |
| Done | Build-order completion checks and applicable independent review/acceptance are evidenced |

Update the task row, phase counts, detailed task record and handoff together. Record the actual UTC date/time when known; do not invent earlier activity dates. Preserve prior decisions, failed checks and superseded evidence through dated entries. If a task is reopened, change its status and record why rather than deleting its earlier history.

Complete only the selected task or authorised batch. Do not automatically start the next task, resolve an open business rule by assumption, call a paid provider or deploy because this tracker names a future action. Relevant tests accompany functional work; later verification tasks do not defer them.

Gate tasks require recorded technical/business sign-off. AI-generated drafts and successful local checks do not replace independent human review or release authority. Keep credentials, private client records and restricted research out of this file.

### 3.1 Authoritative local workflow

- build-order.md owns task definitions/order; progress.md owns current status/blockers; [decisions.md](decisions.md) owns decisions; [risks.md](risks.md) owns risks; docs/evidence holds task reports. Product documents are not alternative status ledgers.
- B001–B105 are local work-item IDs. Each register row maps by the identical ID/title to its build-order definition and links its report. No GitHub issue numbers or URLs are invented. For selected local documentation, the user's instruction is the authorisation reference; remote issue creation remains deferred.
- Before work, record scope, executor, dependencies/gates, decisions, risks and planned checks. Ready requires adequate approved scope and prerequisites. Selection alone does not bypass blockers.
- During work, record In progress or a specific Blocked condition with evidence, authority and unblock action. Preserve prior source files, failed checks and acceptance history.
- At review, update the task row, phase counts, report, relevant decision/risk changes and handoff together. In review means checks complete and human acceptance pending; Done needs applicable acceptance evidence. Document acceptance does not approve architecture or gates.
- Stop after the selected task. Reopen with dated reasons if needed. Cadence, named assignments and schedule commitments remain O-18/B007 decisions.

## 4. Phase summary

| Stage | Tasks | Total | Done | Not started | Exit |
| --- | --- | ---: | ---: | ---: | --- |
| Preparation | B001–B008 | 8 | 7 | 0 | G0-L accepted only; B004 Blocked; B005 local architecture Done |
| Phase 1 Foundation | B009–B028 | 20 | 20 | 0 | B009–B028 local scopes Done; G1-L accepted; original full G1 Hold |
| Phase 2 Idea Studio MVP | B029–B056 | 28 | 0 | 28 | G2 pending |
| Phase 3 Portfolio / stress testing | B057–B066 | 10 | 0 | 10 | G3 pending |
| Phase 4 Voice / Discovery | B067–B081 | 15 | 0 | 15 | G4 pending |
| Phase 5 Advanced research / modelling | B082–B099 | 18 | 0 | 18 | G5 pending |
| Release lane | B100–B105 | 6 | 0 | 6 | G6 pending; deployment unverified |
| **Total** | **B001–B105** | **105** | **26** | **77** | **1 Blocked, 1 In review; G0-L/G1-L local only accepted** |

G2 is the MVP completion point. The release lane may follow an accepted G2, G3, G4 or G5 scope, as described in the build order; deferred later features need not be built before an approved MVP release. Each release needs its own version, evidence and sign-off. G6 approval does not by itself prove that B105 deployment succeeded.

## 5. Build task register

Task titles are copied from the current build order for navigation. Consult that file for full scope, traceability and completion checks. Owners, issue links, PRs and evidence are unassigned/unrecorded for every row unless a detailed entry below says otherwise. No row is marked Ready solely because it appears next numerically.

### Preparation and baseline

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B001 | Inventory current planning files and verified target repository; record source differences, versions and baseline status | Done | [B001 inventory](docs/evidence/B001-baseline-inventory.md); user acceptance on 20 October 2026; local-only scope |
| B002 | Obtain/record product and technical decisions on baseline conflicts; align approved requirement references | Done | [B002 reconciliation](docs/evidence/B002-baseline-reconciliation.md); user acceptance 20 October 2026 |
| B003 | Establish authoritative progress, decision and risk records with task/issue links | Done | [B003 records setup](docs/evidence/B003-records-setup.md); user acceptance 20 October 2026 |
| B004 | Verify CPA repository, memberships, MFA, protected branches, reviewer eligibility and actual PR #2 outcome | Blocked | [B004 local preflight](docs/evidence/B004-local-preflight.md); GitHub verification deferred |
| B005 | Review core architecture ADRs: frontend/API/database, identity/roles/tenancy, environments and service boundaries | Done | [Technical acceptance](docs/evidence/B005-local-architecture-acceptance.md); user confirms Justice approves four local ADR decisions and D005-01–D005-09 deferrals |
| B006 | Define initial privacy, secrets, source/IP and client-isolation boundaries for foundation/MVP | Done | [B006 policy report](docs/evidence/B006-policy-review.md); user-approved limited local scope; specialist reviews deferred |
| B007 | Refine and approve Phase 1 issues, design scope, operational prerequisites and review cadence | Done | [Local completion](docs/evidence/B007-local-completion.md); prior pack approval, user-confirmed Justice role acceptance and approved local cadence |
| B008 | **G0-L: Record limited local readiness acceptance** | Done | [G0-L reassessment](docs/evidence/B008-g0-local-reassessment.md); user-approved limited scope only |

### Phase 1 Foundation

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B009 | Prepare approved repository structure and import handover/ADR references at valid paths | Done | [Local structure/reference report](docs/evidence/B009-local-structure.md); user accepted local slice on 20 October 2026 |
| B010 | Prepare Windows-compatible local setup guidance and placeholder configuration | Done | [Scoped acceptance](docs/evidence/B010-local-setup.md); executable verification carried forward, not passed |
| B011 | Add FastAPI startup, health contract and initial OpenAPI/error structure | Done | [Local API evidence](docs/evidence/B011-local-api.md); 9 tests passed; user accepted local scope on 20 October 2026 |
| B012 | Add PostgreSQL connectivity and versioned migration workflow | Done | [B012 executed checks](docs/evidence/B012-local-database.md); user accepted verified local scope on 20 October 2026 |
| B013 | Implement identity/user references and the approved role/record authorisation boundary | Done | [B013 executed local boundary](docs/evidence/B013-local-authorisation.md); user accepted verified local scope on 20 October 2026 |
| B014 | Implement approved authentication/session validation in the backend | Done | [B014 executed local sessions](docs/evidence/B014-local-authentication.md); user approved verified local scope on 20 October 2026 |
| B015 | Build responsive Next.js navigation shell with accurate feature availability | Done | [B015 implementation and acceptance](docs/evidence/B015-local-navigation.md); user accepted local shell on 20 October 2026; verified scope retained |
| B016 | Connect sign-in/session and access-denied UI to backend permissions | Done | [Local integration and acceptance](docs/evidence/B016-local-sign-in.md); user accepted isolated local scope on 20 October 2026; real login deferred |
| B017 | Implement initial audit events and redacted operational request logging | Done | [Audit/redaction evidence and acceptance](docs/evidence/B017-local-audit.md); user accepted verified local scope on 20 October 2026 |
| B018 | Define AI adapter interface, output/error contracts and mock provider tests | Done | [Local adapter evidence](docs/evidence/B018-local-ai-adapter.md); user approved and accepted 21 October 2026; 42 backend tests passed, including 15 adapter tests |
| B019 | Implement baseline configuration/usage hooks and fail-closed live-AI enablement | Done | [Local controls and evidence](docs/evidence/B019-local-ai-controls.md); user approved 21 October 2026; 54 backend tests passed; live mode always disabled |
| B020 | Add local syntax/type, test, dependency and limited secret checks | Done | [Local checks](docs/evidence/B020-local-checks.md); user approved 21 October 2026; remote requirements remain deferred under RCI-01 |
| B021 | Implement approved current-record dashboard queries and filter contracts | Done | [Local implementation and PostgreSQL verification](docs/evidence/B021-local-dashboard.md); 68 backend tests and 15 real database checks pass; user approved local scope 21 October 2026 |
| B022 | Connect dashboard cards/lists with loading, empty and error states | Done | [Local dashboard UI evidence](docs/evidence/B022-local-dashboard-ui.md); full runner and real database/BFF/browser checks passed; user approved local scope 21 October 2026 |
| B023 | Prepare reviewed staging service/configuration manifests and deployment instructions | Done | [Local staging preparation](docs/evidence/B023-staging-preparation.md); user approved local preparation 21 October 2026; technical/provider/cost decisions and implementation gaps remain before deployment |
| B024 | Provision authorised staging resources and deploy the reviewed foundation | Done | [User-selected local staging rehearsal](docs/evidence/B024-local-rehearsal.md); user approved verified local scope 21 October 2026; hosted deployment remains deferred |
| B025 | Establish foundation backups, restoration procedure and migration rollback assessment | Done | [Local recovery evidence](docs/evidence/B025-local-recovery.md); user approved verified local scope on 21 October 2026 |
| B026 | Verify staging UI/API/DB, direct-record denial and secure configuration | Done | [Local verification](docs/evidence/B026-local-foundation.md); user approved local scope; B026-OBS-01 open |
| B027 | Verify accessible shell/dashboard, operational logs and local setup handover | Done | [Local support/accessibility evidence](docs/evidence/B027-accessibility-setup.md); user approved verified local scope; spoken-reader check outstanding |
| B028 | **G1: Demonstrate and accept the foundation** | Done | [G1-L v0.1 adoption](docs/evidence/B028-g1-local-adoption.md); local milestone accepted; original full G1 Hold |

### Phase 2 Idea Studio MVP

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B029 | Resolve Phase 2 workflow, field validation, source strategy, queue, model/budget, scoring and export decisions; approve issues | Not started | Not recorded |
| B030 | Add idea schema/migration and ownership constraints | Not started | Not recorded |
| B031 | Implement idea create/read/edit/archive API with action-specific validation | Not started | Not recorded |
| B032 | Build idea list/editor and persisted draft workflow | Not started | Not recorded |
| B033 | Add source/evidence schema and permitted MVP ingestion/parser | Not started | Not recorded |
| B034 | Add evidence inspector and hypothesis/no-source presentation | Not started | Not recorded |
| B035 | Implement research-run persistence, approved state contract and idempotent job creation | Not started | Not recorded |
| B036 | Implement worker execution, timeout, bounded retry, cancellation and restart recovery | Not started | Not recorded |
| B037 | Implement per-run/user budget enforcement and AI usage metering for the analysis path | Not started | Not recorded |
| B038 | Implement versioned prompt/schema orchestration and structured assessment validation using mocks | Not started | Not recorded |
| B039 | Execute narrowly authorised live-adapter verification in staging, when approved | Not started | Not recorded |
| B040 | Connect Analyse/progress/result UI to persisted runs and structured output | Not started | Not recorded |
| B041 | Implement score calculation, validation and scoring-version/risk representation | Not started | Not recorded |
| B042 | Add scoring rationale, uncertainty, risk and missing-evidence UI | Not started | Not recorded |
| B043 | Add dossier version schema and saved-version API | Not started | Not recorded |
| B044 | Implement Challenge assumptions orchestration and relationship to its source assessment | Not started | Not recorded |
| B045 | Add challenge/revise/save-version interface | Not started | Not recorded |
| B046 | Implement review submission, approved transitions and authorised human decisions | Not started | Not recorded |
| B047 | Build review queue and approve/return/reject interface | Not started | Not recorded |
| B048 | Implement export generation and private file retrieval for a selected dossier version | Not started | Not recorded |
| B049 | Add export status/download interface and version identification | Not started | Not recorded |
| B050 | Implement permission-filtered basic Knowledge Hub/dossier-source retrieval | Not started | Not recorded |
| B051 | Extend audit, permitted usage/settings and approved review notifications | Not started | Not recorded |
| B052 | Extend Command Centre with real idea/run/review/spend data | Not started | Not recorded |
| B053 | Run complete MVP end-to-end and score/evidence/export regression suite | Not started | Not recorded |
| B054 | Verify MVP record isolation, injection/refusal handling and recoverable failures in staging | Not started | Not recorded |
| B055 | Complete MVP accessibility/usability review and technical handover | Not started | Not recorded |
| B056 | **G2: Demonstrate and accept the Idea Studio MVP** | Not started | Not recorded |

### Phase 3 Portfolio and stress testing

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B057 | Approve product schema/stages, recommendation vocabulary and scenario/review rules | Not started | Not recorded |
| B058 | Implement product registry schema/API and idea/evidence relationships | Not started | Not recorded |
| B059 | Build portfolio list/detail/editor and review-history display | Not started | Not recorded |
| B060 | Implement product review request and assessment persistence | Not started | Not recorded |
| B061 | Implement optimistic/base/pessimistic scenarios with approved inputs/formulas | Not started | Not recorded |
| B062 | Add product-specific critical challenge and evidence/counterargument output | Not started | Not recorded |
| B063 | Implement recommendation decisions and portfolio review history | Not started | Not recorded |
| B064 | Build stress-test results, scenarios and decision panels; extend portfolio/dashboard links | Not started | Not recorded |
| B065 | Run product-specific, permissions, failure and accessibility verification | Not started | Not recorded |
| B066 | **G3: Demonstrate and accept portfolio intelligence** | Not started | Not recorded |

### Phase 4 Voice and Discovery

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B067 | Approve Phase 4 issues, consent/retention, voice transport and secured website/outbound contracts | Not started | Not recorded |
| B068 | Implement consent, session/transcript schema and retention/access controls | Not started | Not recorded |
| B069 | Implement approved voice provider transport with permissioned backend integration | Not started | Not recorded |
| B070 | Build microphone/session UI and streaming transcript with honest availability states | Not started | Not recorded |
| B071 | Implement permission-filtered knowledge/project context in voice | Not started | Not recorded |
| B072 | Implement session summary/actions, project linkage and saved-session retrieval | Not started | Not recorded |
| B073 | Implement Discovery client/enquiry/consent/reference schema and secured intake validation | Not started | Not recorded |
| B074 | Connect approved website intake and verify receipt/failure semantics | Not started | Not recorded |
| B075 | Implement client-isolated enquiry retrieval and internal queue API | Not started | Not recorded |
| B076 | Build restricted enquiry queue/detail/triage interface | Not started | Not recorded |
| B077 | Implement missing-information questions and solution proposal drafts with evidence/IP labels | Not started | Not recorded |
| B078 | Implement version-specific human outbound approval and approved channel integration | Not started | Not recorded |
| B079 | Extend permitted knowledge, notifications and dashboard links for delivered Phase 4 records | Not started | Not recorded |
| B080 | Verify voice/Discovery security, consent, failure recovery, usability and access | Not started | Not recorded |
| B081 | **G4: Demonstrate and accept Voice and Discovery** | Not started | Not recorded |

### Phase 5 Advanced research and modelling

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B082 | Approve Phase 5 issues, geography/schedule/source rights, modelling formulas and advanced evaluation | Not started | Not recorded |
| B083 | Implement geography catalogue and explicit region membership | Not started | Not recorded |
| B084 | Build scope/sector/window/source/budget selectors | Not started | Not recorded |
| B085 | Implement approved scan source collection/deduplication and actual coverage logs | Not started | Not recorded |
| B086 | Implement scan opportunity extraction and human-review candidate persistence | Not started | Not recorded |
| B087 | Build results/evidence drill-down and candidate-to-idea promotion | Not started | Not recorded |
| B088 | Implement coverage display and any separately approved heatmap | Not started | Not recorded |
| B089 | Implement authorised schedules, recurrence ownership and pause/cancel | Not started | Not recorded |
| B090 | Implement scheduled opportunity alerts with confidentiality/preferences | Not started | Not recorded |
| B091 | Implement approved academic connector with rights/provenance persistence | Not started | Not recorded |
| B092 | Build academic findings/uncertainty and potential-application review | Not started | Not recorded |
| B093 | Implement commercial assumptions/model schema and deterministic calculation engine | Not started | Not recorded |
| B094 | Build editable business model/scenario interface | Not started | Not recorded |
| B095 | Implement editable business-plan, investment-memo and pitch-outline generation | Not started | Not recorded |
| B096 | Extend Knowledge Hub/search to approved academic, scan and modelling records | Not started | Not recorded |
| B097 | Implement agreed advanced groundedness/citation/contradiction/cost evaluation and guardrails | Not started | Not recorded |
| B098 | Verify advanced end-to-end, coverage, source licensing, recovery and accessible UI | Not started | Not recorded |
| B099 | **G5: Demonstrate and accept advanced capabilities** | Not started | Not recorded |

### Release lane

| Task | Deliverable | Status | Evidence / issue |
| --- | --- | --- | --- |
| B100 | Define candidate version, included/deferred features, defect register and production success/recovery targets | Not started | Not recorded |
| B101 | Complete release security/privacy/access review and staging regression | Not started | Not recorded |
| B102 | Demonstrate production backup/restore readiness, migration plan and rollback assessment | Not started | Not recorded |
| B103 | Finalise production configuration, monitoring/alerts, runbooks, access and support handover | Not started | Not recorded |
| B104 | **G6: Obtain release-specific technical and CEO approval** | Not started | Not recorded |
| B105 | Deploy approved release, perform scoped production smoke checks and record handoff | Not started | Not recorded |

## 6. Gate and approval register

| Gate | Task | Required acceptance | Status | Evidence / date |
| --- | --- | --- | --- | --- |
| G0-L Local-only entry | B008 | Adopted local scope, slice readiness, review limitations and preservation | Accepted for local scope only | [Reassessment](docs/evidence/B008-g0-local-reassessment.md); original full-G0 conditions deferred |
| G1-L Local foundation | B028 | Adopted v0.1 local scope, verified demonstration and explicit deferrals | Accepted — local only | [Adoption and reassessment](docs/evidence/B028-g1-local-adoption.md) |
| G1 Foundation | B028 | Secure signed-in staging application, API/DB, checks, logs and real-record dashboard | Hold | [Assessment and pending human decisions](docs/evidence/B028-foundation-review.md); [G1-L v0.1 adopted separately](docs/evidence/B028-g1-local-adoption.md) |
| G2 MVP | B056 | Full idea-to-reviewed-dossier journey with retrieval/export and failure/access evidence | Pending | Not recorded |
| G3 Portfolio | B066 | Product assessment, scenarios, critical challenge and human decision history | Pending | Not recorded |
| G4 Voice / Discovery | B081 | Saved permissioned voice session and secure human-reviewed client workflow | Pending | Not recorded |
| G5 Advanced capabilities | B099 | Rights-aware scoped/scheduled research, academic analysis and editable modelling | Pending | Not recorded |
| G6 Production launch | B104 | Release-specific technical acceptance and CEO production approval | Pending | Not recorded |

CEO product/business approval, Justice technical acceptance and eligible independent PR review must be evidenced in their relevant contexts. No signature, reviewer identity, GitHub link or approval date is fabricated here.

## 7. Open prerequisites and decision register

### 7.1 Source reconciliation

B001’s findings are preserved in its accepted report. B002 dispositions are recorded in [the reconciliation report](docs/evidence/B002-baseline-reconciliation.md); broader implementation decisions remain gated.

| Reference | Disposition | Remaining action / authority | Status |
| --- | --- | --- | --- |
| R01 Schedule | Chart marked illustrative, not approved | Justice/CEO estimate after architecture review, O-18 | Documentation corrected; estimates open |
| R02 Decision IDs | O-01–O-18 restored/aligned across current documents | Underlying authorities/decisions in B002 report | References aligned |
| R03 Team | User: human developer with AI assistance | Justice assigns actual person/access later | User decision recorded |
| R04 Source paths | Actual local pack paths indexed; originals preserved | B009 local reference slice; remote alignment deferred | Local references verified |
| R05 Recommendations | User: Continue, Improve, Pivot, Pause, Stop | Product owner/Justice define scenario semantics at B057 | User decision recorded |
| R06 Proposed design | Explicitly subject to ADRs | Justice at B005 and relevant later tasks | Deferred with dependencies |
| R07 Status arrows | Unordered idea statuses; dossier versions separate | Product owner/Justice approve transitions at B029 | Documentation corrected; rules open |
| R08 Tracker filename | progress.md selected by user | B003 local process formalisation | Naming aligned |

### 7.2 Decision tracking labels

O-label meanings now align with blueprint Section 20 and feature-spec Section 10. The B002 report names responsible roles and dependent tasks. This mapping is not an approved ADR or personal assignment; only the explicit user choices below are resolved.

Current states, authorities, checkpoints and evidence: [decisions.md](decisions.md#current-decisions). Potential risks: [risks.md](risks.md). The B003 pre-edit snapshot preserves the prior table.

### 7.3 Blockers and defects

B002 and B003 are accepted and Done. Decisions and risks retain required authorities and affected tasks in their canonical registers. B004 remains remote-deferred; implementation defects are unassessed.

B001 has no remaining completion blocker; the user accepted the local inventory on 20 October 2026. The initial sandbox proxy failure was resolved through approved read-only escalation. Implementation defects remain unassessed. The user selected this existing folder as the working project; another checkout is not required for B001. All GitHub activity is deferred. Open prerequisites above must be resolved before dependent tasks become Ready. Future blocker entries should identify task, impact, required authority/owner, evidence, unblock condition and resolution date.

**B004 blocker:** Current remote governance evidence cannot be obtained under the user's GitHub deferral. User authority clarification is needed; Justice owns verification/replanning. See [preflight and exact gaps](docs/evidence/B004-local-preflight.md). The user subsequently authorised the narrow B005 exception in build-order.md; the B004 blocker remains unchanged.

## 8. Verification and release evidence

| Area | Current evidence state |
| --- | --- |
| Document structure | Initial tracker generated from 105 build-order task rows; task identity/status/count checks described in the initial activity entry |
| AT-01–AT-10 | Not run; original acceptance scenarios remain in the feature spec/build order |
| AC-F01 through AC-F20 criteria | Not run; no criterion claimed passed |
| Unit / integration / end-to-end tests | B011: 8 ASGI contract tests and 1 real loopback startup test passed; broader E2E not run |
| Security / record and client isolation | Not verified |
| Accessibility / usability | Not verified |
| Provider mocks | No execution results recorded |
| Live model / source / voice / website integrations | Not verified; no live provider action authorised by this file |
| CI / independent PR review | Not recorded |
| Backups / restoration / migrations / rollback | Not verified |
| Staging deployment / smoke checks | Not verified |
| Production release / approval / smoke checks | Not recorded / not verified |

For future releases, record release version/commit, included and deferred features, required gate, checks/defects, migration and restore evidence, rollback owner/criteria, Justice acceptance, CEO approval, deployment outcome and production verification. Separate each release record; repeating B100–B105 requires new evidence rather than reusing an earlier sign-off.

## 9. Detailed task evidence template

B001 evidence is recorded below and in the linked inventory. Copy this template for subsequent selected tasks; placeholders are not evidence.

```text
Task ID and title:
Linked approved issue:
Status:
Owner / authorised scope:
Start / last update / completion time in UTC:
Dependencies and gate evidence:
Decision / ADR references:
Repository / branch / commit / PR:
Changes and relevant files:
Checks run, exact commands and actual outcomes:
Acceptance criteria verified and evidence links:
Mocked versus live-provider evidence:
Migration / backup / restore / rollback evidence, if applicable:
Independent reviewer and review outcome:
Technical / business acceptance, if required:
Defects / blockers / unresolved risks:
Next eligible task and handoff:
```

### B001 execution record

Historical check counts and next-step notes describe the B001 handoff; current register status takes precedence.

- **Scope/authority:** User explicitly instructed “Start B001”; inventory and read-only target-repository identity check only.
- **Status:** Done. Executor: Codex; accepted by the user on 20 October 2026 through the explicit instruction quoted in the report. No code-review/phase approval is implied.
- **Evidence:** [B001 baseline inventory](docs/evidence/B001-baseline-inventory.md), including 22 source paths/versions/hashes, 14 matching ZIP files, command outcomes and eight interpretation/path findings.
- **Working project:** Existing local folder selected by the user. Earlier remote identity/private visibility/main observations are historical; all GitHub activity, including B004 remote checks, is deferred.
- **Changes:** Added inventory report; updated this tracker. Source requirements and B002 decisions unchanged.
- **Verification:** PASS — 105 task identities; B001 In review and 104 Not started; 22 baseline records; all 21 input hashes other than the intentionally updated progress.md unchanged; local links valid; 65 feature acceptance criteria confirmed. No runtime test or deployment claim.
- **Acceptance:** Explicit user acceptance recorded for B001 local inventory only; all gates remain pending. Identified conflicts remain for B002.
- **Next:** B002 requires a separate explicit selection and remains Not started. B003 remains Not started.

### B002 execution record

- **Authority:** User instruction “Start B002”; existing local-only/GitHub-deferred instruction retained.
- **Status:** Done. User: “I have accepted B002”, 20 October 2026 UTC.
- **User decisions:** “Human developer with AI assistance”; “Yes, include all” for Continue, Improve, Pivot, Pause and Stop.
- **Evidence:** [B002 reconciliation](docs/evidence/B002-baseline-reconciliation.md), [pre-edit snapshot](docs/evidence/B002-before.zip), [input hashes](docs/evidence/B002-input-hashes.json).
- **Changes:** Blueprint 1.1, feature spec 0.2, build order 0.2 and tracker 0.4. Original handover assets and accepted B001 report preserved.
- **Remaining decisions:** Responsible roles and dependent tasks recorded for O-01–O-18. No Justice technical/phase signature invented.
- **Verification:** PASS — pre-edit archive matches original hashes; original sources and B001 report unchanged; all 105 task definitions preserved; 1 Done / 1 In review / 103 Not started; 18 decision rows aligned; 65 acceptance criteria retained; local links and Markdown fences valid. No runtime or deployment claims.
- **Boundary at initial review:** B003 had not started. Subsequently selected by user; GitHub still deferred.

### B003 execution record

- **Authority:** User “Start B003”; dependency B002 accepted by “I have accepted B002”. Executor: Codex. Date: 20 October 2026 UTC; exact times not recorded.
- **Status:** Done; user accepted the local record structure and maintenance workflow on 20 October 2026 UTC.
- **Scope:** Linked progress, decision and risk records; preserve existing work. No application, remote or B004 work.
- **Evidence:** [B003 report](docs/evidence/B003-records-setup.md), [snapshot](docs/evidence/B003-before.zip), [input hashes](docs/evidence/B003-input-hashes.json).
- **Limits:** Documentation checks only; no runtime or gate approval. O-18 broader choices remain open.

### B004 execution record

- **Authority/date:** User “Start B004”; 20 October 2026 UTC. B003 prerequisite Done. Executor: Codex.
- **Scope:** Local preflight only; current GitHub prohibition retained. No remote action or successor work.
- **Status:** Blocked. User must clarify read-only access authority or retain deferral and arrange approved replanning with Justice.
- **Evidence:** [B004 preflight](docs/evidence/B004-local-preflight.md) and [register snapshot](docs/evidence/B004-before.zip). Local .git marker absent; remote controls and PR outcome unverified.
- **Checks:** 105 task rows; 3 Done, 1 Blocked, 101 Not started; original sources, build definitions and prior evidence preserved.

### B005 execution record

- **Authority:** User explicitly selected B005 as a controlled exception, limited to work independent of blocked B004. Date: 20 October 2026 UTC. Executor: Codex; technical decision owner: Justice.
- **Scope/status:** Done for approved local architecture review. User confirmed Justice approves ADR-001–004 and D005-01–D005-09 deferrals on 21 October 2026. [Acceptance record](docs/evidence/B005-local-architecture-acceptance.md). O-03/O-04 remain Partly resolved for their broader future choices.
- **Evidence:** [B005 report](docs/evidence/B005-local-architecture-review.md), [ADR index](docs/adr/README.md), [pre-edit snapshot](docs/evidence/B005-before.zip), [input hashes](docs/evidence/B005-input-hashes.json).
- **Review limits:** This architecture review performs no remote alignment, account/MFA/branch/reviewer/PR checks, runtime implementation, provider selection, provisioning or live calls. B004 remains Blocked. The original stop-before-B006 handoff was later superseded by separate task authorisations; no gate or successor-task approval follows from this review.

- **Current outcome:** The user-confirmed technical decision supersedes earlier pending-review statements; original reports retain historical context. All deferred checkpoints remain binding. Independent code review, CEO/full-G1 review and external authority are separate.

### B006 execution record

- **Authority/date:** User “Start B006”, 20 October 2026 UTC; local drafting only. Executor: Codex. B004/B005 completion is not inferred.
- **Status:** Done for user-approved limited local scope. [Policy](docs/policies/allowed-data-and-test-fixtures.md) covers permitted/restricted data, synthetic fixtures, secrets, source/IP, privacy and client boundaries.
- **Evidence:** [B006 report](docs/evidence/B006-policy-review.md), [snapshot](docs/evidence/B006-before.zip), [input hashes](docs/evidence/B006-input-hashes.json).
- **Remaining:** Justice and designated policy/source authorities must record approval. O-04 implementation decisions, O-06/O-12 details and all gates remain open as applicable.
- **Boundary:** No live-data use, implementation, external access or B007 start.

### B007 execution record

- **Authority/date:** User “Start B007”, 20 October 2026 UTC. Executor: Codex; local documentation only.
- **Status:** In review. [20 Phase 1 work-item cards](docs/planning/phase-1-work-items.md) and [design/operations worksheet](docs/planning/phase-1-design-operations.md) prepared; Definition of Ready not yet satisfied.
- **Evidence:** [B007 report](docs/evidence/B007-phase-1-refinement.md), [snapshot](docs/evidence/B007-before.zip), [input hashes](docs/evidence/B007-input-hashes.json).
- **Remaining:** Justice’s acceptance of the interim owner nomination, scope/design choices, relevant architecture decisions, operational authority and agreed cadence details. Estimates/dates unset. No fabricated sign-off.
- **Boundary:** B004/B005 unchanged; B008 and all Phase 1 implementation tasks remain Not started. No remote action or provisioning.

### B008 execution record — original full-G0 assessment (historical)

- **Authority/date:** User “Start B008”, 20 October 2026 UTC. Codex assessed local evidence only.
- **Status/outcome:** Blocked; G0 Hold, not accepted. No technical/CEO signature inferred from prior local document approvals.
- **Evidence:** [Gate assessment and closure requirements](docs/evidence/B008-g0-readiness-assessment.md), [snapshot](docs/evidence/B008-before.zip), [input hashes](docs/evidence/B008-input-hashes.json).
- **Blockers:** B004 access/review evidence; B005 technical review; B007 planning readiness; eligible independent reviewer; CEO scope/Justice readiness confirmations.
- **Boundary:** No external access or implementation; B009 remains Not started. Assessment completion does not mean gate completion.

### B008 G0-L adoption and reassessment

- **Authority:** User explicitly approved G0-L v0.1 and B009 local structure/reference scope, retained restrictions/deferrals and instructed no B009 start.
- **Outcome:** B008 Done for G0-L only. The [reassessment](docs/evidence/B008-g0-local-reassessment.md) records evidence against each local criterion; original full-G0 controls/sign-offs are not claimed satisfied.
- **Owners:** Justice's existing interim nomination retained; no new personal acceptance inferred. Executor for later B009 is recorded at selection.
- **Boundary:** B004 Blocked; B005/B007 In review; B009–B105 Not started. No technical/provider/business decision or remote/deployment approval inferred.

### B009 local execution record

- **Authority/date:** User “Start B009”, 20 October 2026 UTC; G0-L and local B009 scope already accepted. Justice remains nominated accountable owner; Codex executed this local slice.
- **Status:** Done; user accepted the local structure and source-reference deliverable on 20 October 2026 UTC.
- **Changes:** Root README, docs index, actual/proposed layout guide and evidence report; progress update only among existing files.
- **Evidence:** [B009 report](docs/evidence/B009-local-structure.md), [input hashes](docs/evidence/B009-input-hashes.json), [progress snapshot](docs/evidence/B009-before.zip).
- **Boundary:** No remote import/compatibility claim, application code, install, Git initialisation or provider activity. B010 remains Not started.

### B010 local execution record — original preparation/check results

- **Authority/date:** User “Start B010”, 20 October 2026 UTC; provisional Python 3.14.8/Node 24.21.0/npm 11.19.0 approved; database explicitly deferred.
- **Status:** Blocked. Setup guide, placeholder template and read-only preflight prepared. Script launch rejected by execution policy; syntax and manual inventory checks completed.
- **Evidence:** [B010 report](docs/evidence/B010-local-setup.md), [guide](docs/local-setup.md), [input hashes](docs/evidence/B010-input-hashes.json), [snapshot](docs/evidence/B010-before.zip).
- **Remaining:** Authorised execution method, database scope, approved dependencies/artifacts and actual fresh-setup verification or explicit scoped replan. No B011 work or external action.

### B011 local execution record

- **Authority/date:** User “Start B011”, 20 October 2026 UTC; G0-L local draft scope. Codex executor; Justice remains nominated accountable owner and formal technical authority.
- **Status:** Done for the user-accepted local API deliverable; no independent technical approval inferred.
- **Implementation:** Minimal FastAPI app, loopback-only launcher, health/OpenAPI/generic errors, local documentation and standard-library tests. No data/business endpoints or database/provider integration.
- **Checks:** `python -B -m unittest discover -s tests -v` from backend: 9 passed, including actual local server startup. Child server stopped. Synthetic privacy/error cases passed.
- **Evidence:** [B011 report](docs/evidence/B011-local-api.md), [backend guide](backend/README.md), [snapshot](docs/evidence/B011-before.zip), [input hashes](docs/evidence/B011-input-hashes.json).
- **Limits:** Installed package versions exercised only; no clean install/full lock/staging proof. B010 PowerShell preflight issue unchanged. Stop before B012; database still deferred.

### B012 local prerequisite review

- **Authority:** User selected B012 under G0-L; earlier explicit database setup deferral subsequently confirmed by user.
- **Evidence:** [B012 report](docs/evidence/B012-local-database.md); installed package metadata and bounded local tool/service inspection only.
- **Status:** Blocked. Migration tool, initial schema, destination and recovery approach remain unapproved; no database connection or migration attempted.
- **Acceptance:** PostgreSQL apply/reapply and disposable-data recovery evidence still required; no completion claim.
- **Boundary:** Backend unchanged; no installs, GitHub or external services; B013 not started.

### B013 local preparation record

- **Authority:** User “Start B013”; local-only restrictions and database setup deferral retained.
- **Delivered:** [Approval worksheet, server-contract proposal and permission-test plan](docs/evidence/B013-local-authorisation.md).
- **Status:** Blocked for implementation by B012 persistence and O-04 grants/ownership/tenancy decisions, plus deferred B006 technical review.
- **Checks:** Documentation and preservation checks only; no permission tests or implementation claimed. User subsequently requested client sign-in in the proposal; implementation decisions remain open.
- **Boundary:** No database, identity provider, invented grants, GitHub or successor work.

### B014 local preparation record

- **Authority:** User “Start B014”; local-only restrictions retained.
- **Deliverable:** [Authentication/session decision worksheet, proposed backend contract and test plan](docs/evidence/B014-local-authentication.md).
- **Status:** Blocked for implementation by B013's unapproved boundary and identity/session/expiry/revocation/MFA decisions.
- **Checks:** Documentation/preservation checks only; no authentication tests, credentials or provider integration performed.
- **Boundary:** B012 remains Done. No B015 work, GitHub, installs, external services or database changes.

### B015 local implementation record

- **Authority:** User “Start B015”, then approved offline-only installation and derived design baseline.
- **Delivered:** [Responsive shell, twelve source-labelled routes and verification evidence](docs/evidence/B015-local-navigation.md); frontend on 127.0.0.1:3000.
- **Status:** Done; user “Accept B015” on 20 October 2026 accepts the verified local shell scope. Formal deferred reviews and live integration remain outside this acceptance.
- **Checks:** Cache-only install, typecheck, production build, 12 routes plus 404, keyboard/skip/focus, mobile toggle/Escape and 320px/390px browser reflow passed. See report for tool limits.
- **Boundary:** Backend preserved; no downloads/GitHub/external services; B016 not started.

### B016 local implementation record

- **Authority:** User “Start B016”, “Approve isolated synthetic journey” and “Approve local cookie baseline”.
- **Delivered:** [Shared UI, separate cookie/server harness and real PostgreSQL permission checks](docs/evidence/B016-local-sign-in.md).
- **Status:** Done; user “Accept B016” on 20 October 2026 accepted the verified isolated local scope. Real human login/provider, deployment and formal reviews remain deferred.
- **Checks:** 27 backend tests; 41 database/HTTP groups; strict frontend/harness types; production build; browser permitted/denied/logout/focus and 320px reflow checks passed.
- **Boundary:** Disposable database/servers cleaned up, normal application has no fixture-login route. No installs/downloads/GitHub/provider activity. B017 not started.

### B017 local implementation record

- **Authority:** User approved local event and disposable storage baselines after selecting B017.
- **Delivered:** [Constrained audit migration/writer, transactional session/permission wrapper and redacted request capture](docs/evidence/B017-local-audit.md).
- **Status:** Done; user “Accept B017” on 20 October 2026 accepts the verified synthetic local scope. Persistent/production retention, audit viewers and formal reviews remain deferred.
- **Checks:** 27 backend tests and 39 database/HTTP groups passed, including canaries, direct access denial, audit-write rollback/recovery and session-storage failure.
- **Boundary:** Test HTTP server and disposable PostgreSQL cleaned up. No frontend, live logging, installs, GitHub or provider changes. B018 not started.

### B018 local implementation record

- **Authority:** User “Start B018” on 21 October 2026 (America/Los_Angeles) supersedes earlier stop-before-B018 wording for the selected local scope. Current workspace is `C:/Users/Win11/Documents/002 CPA`; earlier machine paths are historical.
- **Scope/executor:** Codex defines the mock-only contract and tests under G0-L following accepted B017. Justice remains nominated accountable owner; independent review is unrecorded.
- **Delivered:** [Adapter, versioned synthetic schema and safe outcomes](docs/evidence/B018-local-ai-adapter.md), with [contract and limits](docs/planning/B018-local-ai-contract.md).
- **Status:** Done. User “Approve and accept B018” on 21 October 2026 accepts the local contract and tested implementation. No final dossier schema, live model/budget selection, independent review or live-provider authority inferred.
- **Checks:** 15 adapter tests passed on installed Python 3.15. Existing backend/database regressions were not rerun: FastAPI/Uvicorn/psycopg are absent in this runtime. Initial Windows Python alias failure is retained in evidence.
- **Boundary:** No downloads, live calls, database/HTTP wiring or frontend changes. B019 remains Not started.

### B019 local implementation record

- **Authority/executor:** User “Start B019”; Codex implements the local baseline under G0-L after accepted B018. Justice remains nominated accountable owner; independent review is unrecorded.
- **Delivered:** [Configuration validation, unconditional live denial and ephemeral usage hooks](docs/evidence/B019-local-ai-controls.md). Invalid/missing live settings cannot reach the adapter; complete settings also remain denied. Mock cost is unknown, never zero.
- **Status:** Done; user “Approve B019” on 21 October 2026 accepts the tested local baseline. O-07 actual model/budget/quota/enablement policy remains open; no live spending configuration chosen.
- **Checks:** 54 backend tests passed, including 12 new B019 tests. No dependency changes or PostgreSQL integration run.
- **Boundary:** No HTTP wiring, persistent telemetry, provider calls, GitHub or B020 work.

### B020 local preparation record

- **Authority/executor:** User “Start B020”, then “Keep GitHub deferred; prepare locally”. Codex prepared local tooling after accepted B019; Justice remains nominated accountable owner.
- **Delivered:** [Offline check runner, tests and coverage limits](docs/evidence/B020-local-checks.md). No .git marker exists at the project root; no remote actions performed.
- **Status:** Done for user-revised local scope; user “Approve B020” on 21 October 2026 accepts the verified local pass/failure checks. Original remote criteria remain [RCI-01](docs/planning/remote-ci-handoff.md), required before remote collaboration/merge or release. B004 remains Blocked.
- **Checks:** Runner exits 0: 49 source/config files, installed dependency pins, pip check, 54 backend tests, 5 runner tests, frontend and harness types pass. Deliberate failure exits 1 as expected; subsequent steps stop. Limited secret patterns are not a full secret audit; syntax parsing is not a full style linter; no vulnerability advisory scan.
- **Next:** Remote verification and CI adoption require separate authority while GitHub remains deferred. B021 Not started. No code product behaviour, dependencies, original sources or remote settings changed.

### B021 local implementation record

- **Authority:** User “Start B021” then “Approve this local baseline”. [Synthetic-reference metric/filter contract](docs/planning/B021-local-dashboard-contract.md) approved; business metrics remain unavailable.
- **Delivered:** [Read-only dashboard service, unit tests and prepared PostgreSQL harness](docs/evidence/B021-local-dashboard.md). Reuses B013 permissions and scopes filters to authorised references.
- **Checks:** 68 backend tests pass including 14 dashboard unit tests; full local runner also passes. Repository doubles do not prove real SQL/snapshot behaviour.
- **Status:** Blocked on actual disposable PostgreSQL verification. Docker absent from PATH and usual install location; no install or database execution performed. No full B021 acceptance or independent review claimed.
- **Boundary:** No normal HTTP/frontend wiring, live metrics, schema changes, GitHub or B022 work. Existing database runner only extended to recognise B021.

## 10. Activity log

### 20 October 2026 UTC — Initial tracker draft

- Request: draft `progress.md` for the existing CPA planning documents.
- Read the current build order and local file inventory; initialise all 105 task rows as Not started with no issue/evidence references.
- Carry forward the build order's source discrepancies and pending decisions for review; do not resolve them by assumption.
- Record planning-document drafting separately from implementation completion. No build task, gate, test, external access check or deployment is claimed complete.
- Document checks: generation verified the ordered B001–B105 input sequence. Final consistency checks cover unique task IDs, copied titles, initial statuses, phase totals, gate/task references and local links.
- Scope of change: create this tracker only. No blueprint, feature specification, build-order definition, source document or application file is modified.

### 20 October 2026 UTC — B001 inventory executed

- Verified 22 pre-existing local files and their hashes; confirmed all 14 ZIP entries match extracted sources.
- Confirmed target repository via read-only GitHub metadata after a sandbox proxy failure and successful approved escalation.
- Recorded the working folder's non-Git status and source conflicts; no source requirements reconciled.
- Set B001 to In review, with 104 tasks Not started and 0 Done; human acceptance has not been recorded.
- Added the B001 report and updated this ledger only. Stopped before B002.

### 20 October 2026 UTC — B001 accepted for local continuation

- User explicitly accepted the B001 local baseline inventory and instructed that it be marked Done.
- Selected the existing folder as the working project and deferred all GitHub activity, including access, clone, pull, merge and remote modification.
- Updated only the B001 report and this tracker; preserved the inventory hashes, earlier execution history and source material.
- Carried identified conflicts forward to B002 without resolving them. B002 remains Not started by explicit instruction.
- Current totals: 1 Done, 0 In review, 104 Not started; all phase/release gates pending.

### 20 October 2026 UTC — B002 reconciliation prepared

- User selected B002, then confirmed human developer with AI assistance and all five recommendation labels.
- Preserved pre-edit planning files; corrected references, schedule qualification, actual source paths, unordered statuses and local workflow wording.
- Recorded remaining decision authorities and dependent-task blocks; kept original source files and B001 history intact.
- B002 In review; totals 1 Done, 1 In review, 103 Not started. B003 not started; all gates pending.

### 20 October 2026 UTC — B002 accepted; B003 prepared

- Recorded user acceptance of B002 and marked Done; preserved review history.
- Continued selected B003: linked canonical records, local work-item mapping and maintenance rules.
- B003 In review; 2 Done, 1 In review, 102 Not started. All gates pending.

### 20 October 2026 UTC — B003 accepted

- User: “I accept the B003 local record structure and maintenance workflow.”
- Marked B003 Done; local record structure/workflow accepted. Open decisions, risk controls and all phase gates retain their separate approval requirements.
- Totals: 3 Done, 0 In review, 102 Not started. B004 remains unstarted; all GitHub activity deferred.
- Verified all 105 task rows and totals; preserved prior review-stage verification and activity history.

### 20 October 2026 UTC — B004 local preflight

- User selected B004. Reviewed local requirements and historical evidence without accessing GitHub.
- Recorded six verification gaps and the authority blocker; no control marked verified or unprovisioned without evidence.
- Totals: 3 Done, 1 Blocked, 101 Not started. No gate accepted; B005 not started.

### 20 October 2026 UTC — B005 controlled local exception

- User explicitly authorised B005 work independent of B004. Recorded the exception without changing task definitions, B004 status or gates.
- Prepared four proposed ADRs with options, trade-offs, decision authorities and explicit deferred inputs. No provider or business grant selected by assumption.
- B005 In review for the local independent scope; totals 3 Done, 1 Blocked, 1 In review, 100 Not started. Justice's decisions and product-owner access choices remain outstanding.

### 20 October 2026 UTC — B005 user acceptance recorded

- User stated: “I accept B005”. Recorded acceptance of the local review deliverable under the controlled exception.
- This statement does not identify the user as Justice or record Justice's substantive ADR review. No technical sign-off or waiver of the named completion requirement is inferred.
- B005 remains In review pending that review outcome. Pending choices may be explicitly deferred with rationale, owner and checkpoint; not every implementation choice must be settled to accept the review.
- B004 remains Blocked; B006 not started; task totals unchanged.

### 20 October 2026 UTC — B006 local policy prepared

- User selected B006 after accepting the B005 local review deliverable. Recorded the later local preparation authority without clearing B004/B005 or claiming Justice approval.
- Drafted allowed-data/test-fixture policy and review checklist. Sensitive/live client data remains prohibited pending required reviews.
- Totals: 3 Done, 1 Blocked, 2 In review, 99 Not started. No gate accepted; B007 not started.

### 20 October 2026 UTC — B006 scoped policy approved

- User: “Approve B006”. Marked B006 Done for the limited local policy-definition scope described in the preceding acceptance clarification.
- Recorded user approval without attributing specialist sign-offs. Justice technical review and designated policy/source reviews remain explicit downstream prerequisites in policy version 0.2.
- Totals: 4 Done, 1 Blocked, 1 In review, 99 Not started. B004/B005 unchanged; all gates pending; B007 not started.

### 20 October 2026 UTC — B007 local refinement prepared

- User selected B007. Prepared 20 local work-item cards with value, scope, non-goals, unchanged acceptance checks, dependencies, test/security plans, owner gaps and design references.
- Added Phase 1 design/operations/cadence proposal and approval worksheet. Asked user about cadence and named assignments; unanswered choices remain pending.
- Totals: 4 Done, 1 Blocked, 2 In review, 98 Not started. No work item declared Ready; no gate approved.

### 20 October 2026 UTC — B007 user clarifications

- User confirmed cadence option 1 as a proposal and reiterated no GitHub connection.
- User nominated Justice “for the meantime” for Phase 1 implementation ownership and product/scope approval. Recorded the interim roles without inferring acceptance or technical/scope sign-off.
- If Justice authors work, independent human review needs another eligible reviewer. CEO gate/release authority retained.
- Statuses unchanged; no meetings, messages, external connections or B008 work.

### 20 October 2026 UTC — B007 local pack user-approved

- User: “Approve B007”. Recorded approval of the local planning pack, preserving unselected decisions and outstanding authority/readiness evidence.
- B007 remains In review: work-item Definition of Ready is not yet evidenced. No Justice technical review, assignment acceptance, budget or G0 approval inferred.
- Status totals unchanged; no GitHub activity, scheduling, messages or successor work.

### 20 October 2026 UTC — B008 G0 assessed locally

- User selected B008. Reviewed baseline/ADR/policy/work-item evidence and original gate requirements.
- Recorded Hold with five explicit closure actions. Prior approvals retained; no prerequisite status silently upgraded.
- Totals: 4 Done, 2 Blocked, 2 In review, 97 Not started. G0 not accepted; B009–B105 Not started.

### 20 October 2026 UTC — G0-L adopted and accepted

- User approved revised local gate and proposed first local scope while retaining restrictions/deferred reviews.
- Reassessment passed G0-L; B008 marked Done only for local entry. Original full-G0 assessment preserved, with deferred assurance checkpoint explicit.
- Totals: 5 Done, 1 Blocked, 2 In review, 97 Not started. B009 explicitly not started.

### 20 October 2026 UTC — B009 local structure prepared

- User selected B009. Added meaningful project/documentation entry points and a layout guide; linked the original handover in place.
- Preserved original materials and all prior evidence; remote alignment remains unverified and deferred.
- Totals: 5 Done, 1 Blocked, 3 In review, 96 Not started. No runtime implementation or B010 work.

### 20 October 2026 UTC — B009 accepted

- User: “I accept B009’s local structure and source-reference deliverable”.
- Marked B009 Done for the G0-L local slice only; preserved original execution evidence and source files.
- Totals: 6 Done, 1 Blocked, 2 In review, 96 Not started. B010 remains unstarted; no external activity or new technical approval inferred.

### 20 October 2026 UTC — B010 preparation and blocker recorded

- User selected B010 and approved provisional installed tooling with application compatibility unverified; database setup deferred by explicit answer.
- Added safe public template, setup guide and read-only preflight; script launch blocked by machine policy, parser accepted syntax. Recorded results without claiming runnable setup.
- Totals: 6 Done, 2 Blocked, 2 In review, 95 Not started. B011–B105 remain Not started.

### 20 October 2026 UTC — B010 revised scope approved and accepted

- User: “Approve and Accept B010”. Adopted setup-preparation milestone and marked B010 Done for that scope only.
- Preserved failed script-launch evidence and database deferral. Provisional runtimes are not verified application compatibility.
- Backend/database/frontend checks remain at B011/B012/B015–B016; complete fresh isolated setup walkthrough required at B027 before B028/G1.
- Totals: 7 Done, 1 Blocked, 2 In review, 95 Not started. B011 remains unstarted; no external action or implementation.

### 20 October 2026 UTC — B011 local API prepared and tested

- Selected B011 implemented with existing local FastAPI/Uvicorn packages; no download/install or external calls.
- Nine tests passed, including loopback startup and non-disclosure checks. Public health is liveness only; no dependency readiness claim.
- Totals: 7 Done, 1 Blocked, 3 In review, 94 Not started. B012–B105 remain Not started.

### 20 October 2026 UTC — B011 local API accepted

- User: “I accept B011’s local API deliverable”. Marked B011 Done for the tested local startup/health/OpenAPI/error scope under G0-L.
- Existing nine-test evidence retained. No Justice/independent review, broad architecture approval or deployment readiness inferred.
- Totals: 8 Done, 1 Blocked, 2 In review, 94 Not started. Database remains deferred; B012 not started.

### 20 October 2026 UTC — B012 selected and prerequisites reviewed

- User: “Start B012”. Inspected local requirements and available package/tool metadata; prepared decision and verification plan.
- Requested clarification of the prior database deferral and local destination approach. No setup authority or technical choice inferred from an unanswered question.
- Totals: 8 Done, 2 Blocked, 2 In review, 93 Not started. B012 Blocked; B013–B105 Not started.
- Preserved existing code, original sources, previous evidence and unchanged B012 acceptance criteria.

### 20 October 2026 UTC — B012 setup deferral confirmed

- User retained the setup deferral and selected native PostgreSQL inspection first. Read-only checks found no standard native installation or matching service; CIM inspection was access-denied and no elevation attempted.
- No database destination/version verified; no setup, connection, install or migration performed. Details and limitations recorded in the B012 report.
- Status totals unchanged: 8 Done, 2 Blocked, 2 In review, 93 Not started. B013 remains unstarted.

### 20 October 2026 UTC — B012 local report approved

- User: “Approve B012”. Recorded approval of the local prerequisite review, native inspection findings and execution plan.
- B012 remains Blocked under its unchanged acceptance criteria: database setup remains explicitly deferred; actual PostgreSQL apply/reapply/recovery evidence and task-specific technical decisions are outstanding.
- No scope revision, database setup authority, technical-option selection or successor work inferred. Totals unchanged: 8 Done, 2 Blocked, 2 In review, 93 Not started.

### 20 October 2026 UTC — B013 selected and local design prepared

- Reviewed task dependencies, F01, ADR-002, O-04 and B006. Prepared an explicit approval worksheet and planned positive/negative permission cases without inventing business grants.
- B012 remains Blocked with database setup deferred. B013 implementation is Blocked; independent local design preparation is delivered.
- Totals: 8 Done, 3 Blocked, 2 In review, 92 Not started. B014–B105 remain Not started.

### 20 October 2026 UTC — B013 client sign-in proposal scope

- User: “Include client sign-in in the proposal”. Expanded the local design worksheet to cover client enrolment, membership, access grants and negative isolation checks.
- Recorded the choice under O-04 without approving a provider, permissions, client portal implementation or Phase 1 release enablement.
- Statuses unchanged; B012/B013 remain Blocked; database setup deferred; B014 not started.

### 20 October 2026 UTC — B012 database execution authorised and verified

- User lifted the setup deferral for usable local PostgreSQL, migration approach, initial schema and actual checks. Selected an existing offline PostgreSQL image, psycopg and transactional ordered SQL; no business/user/client schema invented.
- Started the installed Docker engine with required local permissions. Nine actual PostgreSQL checks passed, including apply/reapply, history rejection, failure rollback, recovery and synthetic rollback; nine existing API tests passed.
- Test container removed and tmpfs data discarded; Docker Desktop left running. No pulls, installs or GitHub commands.
- Totals: 8 Done, 2 Blocked, 3 In review, 92 Not started. B012 In review for executed scope; B013 policy decisions remain unresolved; B014 not started.

### 20 October 2026 UTC — B012 executed deliverable accepted

- User: “I accept B012”. Marked B012 Done for the verified local PostgreSQL/migration/recovery scope; retained nine database checks and nine API tests as execution evidence.
- B013 access decisions remain unresolved; no broader architecture, independent review, persistent database or deployment acceptance inferred.
- Totals: 9 Done, 2 Blocked, 2 In review, 92 Not started. B014 remains unstarted; no code changes or external activity.

### 20 October 2026 UTC — B013 access matrix proposed

- User requested a recommended matrix for Justice approval. Drafted version 0.1 covering internal and client access, identity/membership, ownership/sharing, administration, revocation and verification cases.
- Linked the proposal under O-04. No choices adopted, accounts assigned or task statuses changed; B013 remains Blocked pending decisions and technical review.
- Documentation only; existing backend and database workflow preserved. No GitHub or B014 work.

### 20 October 2026 UTC — B014 selected and prepared locally

- Reviewed the unchanged task definition, F01 and identity ADR. Prepared the B014 decision worksheet, proposed validator-to-user-to-permission contract and negative test matrix.
- B014 implementation remains Blocked pending B013 and session-policy decisions. No identity provider or session settings selected by assumption.
- Totals: 9 Done, 3 Blocked, 2 In review, 91 Not started. B015–B105 remain Not started.

### 20 October 2026 UTC — B013 approved to continue and implemented locally

- User: “Approve B013 to continue”. Adopted matrix v0.1 as local policy authority; no Justice identity or separate independent/specialist sign-off invented.
- Added migration 0002 for user/scope/grant references, server-side record checks and synthetic permission tests. No real accounts, live authentication, administration or business endpoints enabled.
- 21 policy/API tests and 19 actual PostgreSQL verification groups passed. Disposable B013 container removed; original sources and prior migration preserved.
- Totals: 9 Done, 2 Blocked, 3 In review, 91 Not started. B013 In review for executed scope; B014 session decisions remain blocked; B015 not started.

### 20 October 2026 UTC — B013 executed local deliverable accepted

- User: “i accept B013”. Marked B013 Done for the verified local identity references and permission boundary; existing 21 policy/API tests and 19 PostgreSQL verification groups retained as evidence.
- B014's B013 acceptance prerequisite is satisfied; identity/session/MFA choices remain unresolved. No formal specialist/independent review or live operation inferred.
- Totals: 10 Done, 2 Blocked, 2 In review, 91 Not started. No code changes, database execution, external activity or B015 work.

### 20 October 2026 UTC — B014 concrete policy prepared

- User requested to fix B014. Prepared local session policy v0.1 and requested a decision on opaque bearer sessions, expiry, revocation and fail-closed privileged access pending MFA.
- Checked local package metadata; no implementation, installs or external services. B014 remains Blocked awaiting the policy answer; B013 remains Done.
- Task statuses unchanged: 10 Done, 2 Blocked, 2 In review, 91 Not started.

### 20 October 2026 UTC — B014 session baseline approved and implemented

- User answered “Approve this local baseline”. Implemented opaque server-stored sessions, fixed 30-minute idle/8-hour absolute expiry, logout/revocation and privileged denial pending MFA.
- Added migration 0003, backend dependencies, synthetic HTTP/database checks and Bearer 401 challenge. No real login, provider, browser storage or public mock-login route.
- Final checks: 26 unit/API tests and 33 PostgreSQL/HTTP verification groups passed. Disposable database removed and test HTTP server stopped; initial wrong-directory test invocation retained in report as failed evidence.
- Totals: 10 Done, 1 Blocked, 3 In review, 91 Not started. B014 In review for approved local scope; B015 not started.

### 20 October 2026 UTC — B014 executed local deliverable accepted

- User: “Approve B014”. Marked B014 Done for the verified local backend session scope; retained 26 unit/API tests and 33 PostgreSQL/HTTP verification groups as evidence.
- Real sign-in/provider integration, browser flow, live MFA, named assignments and formal reviews remain deferred. No code changes, database execution or external activity.
- Totals: 11 Done, 1 Blocked, 2 In review, 91 Not started. B015 remains unstarted.

### 20 October 2026 UTC — Localhost root status page fixed

- User reported the root URL showing a JSON 404. Added a small backend-only HTML status page at `/`; `/health` remains the unchanged JSON liveness contract.
- 27 unit/API tests passed. Restarted the selected local backend and verified root HTTP 200 and health `ok` on port 8000.
- Existing numbered-task statuses unchanged; B015 remains unstarted. No GitHub, provider or database activity. Pre-edit source/navigation snapshot: [localhost-status-before.zip](docs/evidence/localhost-status-before.zip).

### 20 October 2026 UTC — B015 selected and prepared

- Inspected D005, the UI reference, F02 and local npm cache. Prepared twelve source-labelled routes with honest unavailable-feature treatment and a responsive/keyboard verification plan.
- Asked for offline-only installation authority and a derived local token/navigation baseline. Answers pending; no dependencies installed or frontend code created.
- Totals: 11 Done, 2 Blocked, 2 In review, 90 Not started. B016 remains unstarted.

### 20 October 2026 UTC — B015 implemented under approved offline/design scope

- User approved cache-only installation and the locally derived design baseline. Installed exact cached dependencies with scripts/network disabled; created the twelve-route responsive Next.js shell.
- Type checking, production build, route/404 and browser keyboard/responsive checks passed. B015 In review for user acceptance; no live sign-in, metrics, service calls or B016 work.
- Corrected the stale phase-summary total to match task rows: 11 Done, 1 Blocked, 3 In review, 90 Not started. Existing unrelated task statuses unchanged.

### 20 October 2026 UTC — B015 accepted

- User: “Accept B015”. Marked B015 Done for the verified local responsive navigation shell. Existing build, route, keyboard and responsive evidence retained; no tests rerun for this documentation-only acceptance.
- B016 remains Not started. B004 remains Blocked, B005/B007 remain In review; all local-only and deferred-review restrictions retained.
- Totals: 12 Done, 1 Blocked, 2 In review, 90 Not started. Pre-acceptance records preserved in [B015-before-acceptance.zip](docs/evidence/B015-before-acceptance.zip). No code, runtime, database or GitHub changes.

### 20 October 2026 UTC — B016 selected and prepared

- Reviewed build-order/F01/F02, the work item and approved B013–B015 scope. Real login and browser transport remain explicitly deferred by B014.
- Asked for a separate synthetic local journey and HttpOnly same-origin cookie baseline; answers pending. Prepared concrete failure/denial and browser/backend verification cases.
- Totals: 12 Done, 2 Blocked, 2 In review, 89 Not started. B017 remains unstarted. Existing application work preserved.

### 20 October 2026 UTC — B016 approved local implementation verified

- User approved isolated synthetic journey and local cookie baseline. Implemented shared UI plus a separate Next.js/server/PostgreSQL harness, retaining real-login unavailability in the normal app.
- 27 backend tests, 41 integration groups, type/build and browser checks passed. Both disposable runs cleaned up; normal frontend restored. No dependency install or remote operation.
- Totals: 12 Done, 1 Blocked, 3 In review, 89 Not started. B016 awaits local-scope acceptance; B017 remains unstarted.

### 20 October 2026 UTC — B016 accepted

- User: “Accept B016 and let me see the current progress”. Marked B016 Done for the approved isolated local browser/session/permission integration. Existing verification evidence retained; no tests rerun for this documentation-only acceptance.
- Totals: 13 Done, 1 Blocked, 2 In review, 89 Not started. Phase 1: 8 of 20 tasks Done for their accepted local scopes. B017 remains Not started.
- Real human login, provider integration, deployed cookie/TLS configuration, live MFA and formal reviews remain deferred. No application code, runtime, database or GitHub changes. [Pre-acceptance snapshot](docs/evidence/B016-before-acceptance.zip) preserves prior records.

### 20 October 2026 UTC — B017 selected and prepared

- Reviewed B017, F19/F20, D007, B006 and current session/harness boundaries. Proposed fixed local audit events, minimal request metadata and runner-only disposable storage with end-of-run cleanup.
- Asked for the two required baseline decisions; answers pending. No persistent retention duration or audit-viewer grant invented.
- Totals: 13 Done, 2 Blocked, 2 In review, 88 Not started. B018 remains unstarted. No code or external changes.

### 20 October 2026 UTC — B017 local implementation verified

- User approved the local event and disposable-storage baselines. Implemented audit metadata and operational capture only through explicit test wiring.
- Final checks: 27 backend tests and 39 database/HTTP groups passed. Canary exclusion, transactional audit-write failure/recovery and cleanup verified.
- Totals: 13 Done, 1 Blocked, 3 In review, 88 Not started. B017 awaits scoped acceptance; B018 unstarted. No external operations.

### 20 October 2026 UTC — B017 accepted

- User: “Accept B017”. Marked B017 Done for its verified local synthetic audit and redacted operational-capture scope. Retained 27 backend tests and 39 database/HTTP verification groups as evidence; no tests rerun for this documentation-only acceptance.
- Totals: 14 Done, 1 Blocked, 2 In review, 88 Not started. Phase 1: 9 of 20 tasks Done for accepted local scopes. B018 remains Not started.
- Persistent logging, production retention, audit-viewer grants, live data and formal reviews remain deferred. No code, runtime, database or GitHub changes. [Pre-acceptance snapshot](docs/evidence/B017-before-acceptance.zip) preserves prior records.

### 21 October 2026 (America/Los_Angeles) — B018 local adapter implemented

- User selected B018. Defined explicit mock-only input/output/error contracts, versioned synthetic output and prompt, draft-only results and unknown-cost handling.
- 15 tests passed covering required outcomes plus validation, cancellation, safe errors and no network fallback. Existing backend regression unavailable in current runtime; no install attempted.
- Totals: 14 Done, 1 Blocked, 3 In review, 87 Not started. B018 awaits local acceptance; B019 unstarted. [Pre-change records](docs/evidence/B018-before.zip) preserved.

### 21 October 2026 — Python dependencies installed at user request

- User: “Install pythons dependencies”. This authorises package downloads for the local backend setup, superseding the earlier no-install boundary for this work only.
- Initial sandbox network denial was followed by approved network execution. Python 3.15 lacked the pinned Pydantic core wheel; used locally bundled Python 3.12.14 in `backend/.venv312`, preserving direct pins and adding matching psycopg binary support.
- Installed versions recorded in `backend/requirements-installed-py312.txt`. All 42 backend tests passed, including B018 and loopback startup/shutdown. `pip check` reports no broken requirements. Earlier missing-package regression limitation is resolved in this environment; PostgreSQL integration checks were not rerun.
- Task statuses unchanged: B018 remains In review; B019 Not started. No live AI or database operation; no persistent server started.

### 21 October 2026 — B018 approved and accepted

- User: “Approve and accept B018”. Marked B018 Done for its local mock adapter, versioned synthetic draft and safe error contracts.
- Retained evidence of 42 passing backend tests, including 15 adapter tests, and clean pip check. No tests rerun for this documentation-only acceptance; PostgreSQL integration checks were not rerun in this session.
- Totals: 15 Done, 1 Blocked, 2 In review, 87 Not started. Phase 1: 10 of 20 Done for accepted local scopes. B019 remains Not started.
- Preserved [pre-acceptance records](docs/evidence/B018-before-acceptance.zip). No code/runtime changes, live-provider authority, independent review or deployment acceptance inferred.

### 21 October 2026 — B019 local controls implemented

- User selected B019. Implemented explicit settings validation, live denial even with complete configuration, and safe ephemeral usage with unknown cost.
- All 54 backend tests passed. [Evidence and scope](docs/evidence/B019-local-ai-controls.md); [pre-change records](docs/evidence/B019-before.zip).
- Totals: 15 Done, 1 Blocked, 3 In review, 86 Not started. B019 awaits local acceptance; B020 not started. O-07 live policy decisions remain open.

### 21 October 2026 — B019 approved

- User: “Approve B019”. Marked B019 Done for the tested local configuration/usage baseline; live AI remains unconditionally disabled.
- Retained 54 passing backend tests, including 12 B019 tests. No tests rerun for this documentation-only approval; PostgreSQL integration checks were not rerun during B019.
- Totals: 16 Done, 1 Blocked, 2 In review, 86 Not started. Phase 1: 11 of 20 Done for accepted local scopes. B020 remains Not started.
- [Pre-approval records](docs/evidence/B019-before-acceptance.zip) preserved. No code/runtime changes, live spend authority, independent review or deployment sign-off inferred. O-07 live policy decisions remain open.

### 21 October 2026 — B020 prepared locally; remote completion blocked

- User selected B020 and explicitly retained the GitHub deferral. Built the local offline runner and its verification tests without downloads or remote activity.
- Complete local runner passed; controlled child failure produced exit 1 as expected. Actual merge blocking and branch settings remain unverified.
- Totals: 16 Done, 2 Blocked, 2 In review, 85 Not started. B020 Blocked for full completion; B021 remains unstarted. [Pre-change records](docs/evidence/B020-before.zip) preserved.

### 21 October 2026 — B020 local-only scope adopted

- User selected “Keep everything local till github comes in later”. Revised B020's build-order/work-item scope to verified local checks; moved original remote criteria into mandatory RCI-01 before remote collaboration/merge or release.
- B020 is now In review for the local deliverable, not Blocked on remote work. Scope selection is recorded separately from deliverable acceptance. Existing check evidence retained; no tests rerun for documentation-only replan.
- Totals: 16 Done, 1 Blocked, 3 In review, 85 Not started. B004 remains Blocked; B021 remains unstarted. [Pre-replan records](docs/evidence/B020-before-local-replan.zip) preserved.

### 21 October 2026 — B020 local scope approved

- User: “Approve B020”. Marked B020 Done for the revised local syntax/type/test/dependency/limited secret checks and verified failure propagation.
- Retained passing evidence: 54 backend tests, 5 runner tests, dependency and frontend/harness type checks; controlled failure returned 1. No tests rerun for this documentation-only approval.
- Totals: 17 Done, 1 Blocked, 2 In review, 85 Not started. Phase 1: 12 of 20 Done for accepted local scopes. B021 remains Not started.
- [Pre-approval records](docs/evidence/B020-before-acceptance.zip) preserved. RCI-01 remains deferred and mandatory before remote collaboration/merge or release. No GitHub activity, remote verification or independent sign-off inferred.

### 21 October 2026 — B021 local implementation delivered

- User selected B021 and approved the synthetic-reference baseline. Implemented permission-filtered count/list queries and strict kind/state/owner filters, with explicit empty/unavailable/error semantics.
- 68 backend tests and full local runner pass. Actual PostgreSQL harness prepared but not executed because Docker is unavailable; this remains a completion blocker.
- Totals: 17 Done, 2 Blocked, 2 In review, 84 Not started. B021 Blocked; B022 not started. [Pre-change records](docs/evidence/B021-before.zip) preserved.

### 21 October 2026 — Docker installation prerequisite blocked

- User requested Docker installation. WinGet identified Docker Desktop 4.96.0; system inspection found Windows 11 Pro build 22000, below Docker's documented minimum build 22631. WSL lacks modern version reporting.
- Docker was not installed. A supported Windows upgrade is needed before installation; no OS upgrade or reboot attempted. [B021 evidence](docs/evidence/B021-local-dashboard.md) records findings. Task totals unchanged.

### 21 October 2026 — Docker installed; required Windows features enabled

- Rechecked at user request: Docker Desktop installed, CLI 29.9.1; launched Desktop. Engine returned HTTP 500 and logs identify disabled Virtual Machine Platform.
- UAC-elevated DISM enabled VirtualMachinePlatform and Microsoft-Windows-Subsystem-Linux with no restart; both returned 3010. A user restart is now required. No database/container/image operation succeeded or was started.
- Docker absence is superseded by installed-but-not-ready status. B021 remains Blocked on engine readiness and actual PostgreSQL verification. Windows/WSL compatibility must be rechecked after restart. Task totals unchanged.

### 21 October 2026 — B021 PostgreSQL verification passed after restart

- User confirmed Windows restart and authorised continuation. Docker engine recovered after Desktop restart; downloaded the official postgres:17 image with approval.
- Actual PostgreSQL 17.11 harness passed 15 migration/recovery/dashboard checks. Container removal and tmpfs disposal confirmed before the later user instruction not to clean it up. Docker and image remain installed.
- Full local runner passed source/config, dependencies, backend/runner tests and frontend/harness types. B021 moves to In review; acceptance not inferred. Totals: 17 Done, 1 Blocked, 3 In review, 84 Not started.
- User requests approvals here in chat and no cleanup. Retain future test containers unless explicitly instructed otherwise; adjust the automatic-cleanup runner before reuse. No B022 work started.

### 21 October 2026 — B021 approved

- User: “Approve B021”. Accepted the verified local synthetic-reference dashboard query/filter scope; B021 Done.
- Existing 68 backend tests, 15 PostgreSQL checks and full local runner pass retained; no tests rerun for this documentation-only approval.
- Totals: 18 Done, 1 Blocked, 2 In review, 84 Not started. Phase 1: 13 of 20 Done for local scopes. B022 unstarted.
- Preserve future test containers and request approvals in chat. GitHub/RCI-01 deferred. Pre-approval records saved in docs/evidence/B021-before-acceptance.zip.

### 21 October 2026 — B022 local dashboard UI delivered

- User “Start B022”. Reused approved reference metric/filter scope, shell styling and isolated session pattern. Dashboard cards/list/filter states connected to PostgreSQL only in the harness.
- Full local runner passed including new dashboard payload/filter checks. Actual backend/BFF checks passed six groups; browser loading/empty/unavailable/error/retry/filter retention/sign-out/keyboard checks passed. [Evidence](docs/evidence/B022-local-dashboard-ui.md).
- Preview at http://127.0.0.1:3100/dashboard remains running. Retained container cpa-b022-check-2c4e5c7f77664a28b9e8b6ffd419522d; no container cleanup. Runner now retains containers by default.
- Totals: 18 Done, 1 Blocked, 3 In review, 83 Not started. B022 In review for local acceptance; B023 not started.

### 21 October 2026 — B022 local deliverable approved

- User “Approve B022” accepts the verified local synthetic-reference dashboard UI; B022 Done.
- Existing local runner, database/BFF and browser evidence retained. Documentation-only approval; no tests rerun or runtime cleanup performed.
- Totals: 19 Done, 1 Blocked, 2 In review, 83 Not started. Phase 1: 14 of 20 Done for accepted local scopes. B023 unstarted.
- Pre-approval records: docs/evidence/B022-before-acceptance.zip. Preview/database left untouched; keep approvals in chat and retain test containers.

### 21 October 2026 — B023 staging preparation delivered

- User “Start B023”. Prepared provider-neutral non-deployable manifest, environment example, secret/origin/redirect/worker/cost requirements, conditional deployment and rollback guide.
- Valid draft exit 0, readiness exit 2 and eight unsafe-edit rejection cases passed; syntax and limited secret-pattern checks passed. No application changes or full-suite rerun.
- Source gaps and unresolved O-03/O-04/O-16/O-17 decisions remain explicit. No GitHub, cloud, secrets, spending, deployment or runtime cleanup.
- Totals: 19 Done, 1 Blocked, 3 In review, 82 Not started. B023 In review for local preparation; B024 unstarted.

### 21 October 2026 — B023 local preparation approved

- User “Approve B023” accepts the reviewed local staging preparation pack. B023 Done for this local scope; no executable staging configuration or deployment readiness inferred.
- Existing draft/negative-case validation retained; documentation-only acceptance, no tests rerun. Review manifest remains draft-not-deployable with deployment_authorized=false and unresolved choices unchanged.
- Totals: 20 Done, 1 Blocked, 2 In review, 82 Not started. Phase 1: 15 of 20 Done for accepted local scopes. B024 unstarted.
- Pre-approval records: docs/evidence/B023-before-acceptance.zip. Preview and database left untouched; GitHub/cloud actions remain deferred.

### 21 October 2026 — B024 local staging rehearsal delivered

- User selected B024 then chose a separate local staging rehearsal. Created dedicated persistent PostgreSQL and protected credentials, production frontend and loopback HTTPS application with synthetic sign-in.
- Fixed restart port rediscovery and Windows build-log encoding; resumed the same retained container. Six actual HTTPS/DB/access groups passed; full local runner passed. [Evidence](docs/evidence/B024-local-rehearsal.md).
- Rehearsal remains running at https://127.0.0.1:3443. Tests explicitly trust its local CA; no global/browser trust installed. B022 still returns HTTP 200. No container/volume cleanup.
- Totals: 20 Done, 1 Blocked, 3 In review, 81 Not started. B024 In review for user-selected local scope; hosted prerequisites deferred; B025 unstarted.

### 21 October 2026 — B024 local rehearsal approved

- User “Approve B024” accepts the verified separate local staging rehearsal; B024 Done for that scope.
- Existing six HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained. Documentation-only acceptance; no tests rerun and no service/data changes.
- Totals: 21 Done, 1 Blocked, 2 In review, 81 Not started. Phase 1: 16 of 20 Done for accepted local scopes. B025 unstarted.
- Pre-approval records: docs/evidence/B024-before-acceptance.zip. Hosted deployment, real identity, remote CI and independent review remain deferred. Keep services/data retained and approvals in chat.

### 21 October 2026 — B025 local recovery delivered

- User “Start B025” authorises the local synthetic backup and isolated restore drill. Pre-change records: docs/evidence/B025-before.zip.
- Read-only consistent B024 snapshot restored to a fresh retained PostgreSQL container/volume; exact table fingerprints matched before destination-only session checks. Eight recovery/control groups passed, including migration failure rollback, runtime restrictions, audit sequence and session revocation.
- Full local runner passed: 68 backend tests, 5 runner tests, source/dependency checks, dashboard contract and all three TypeScript checks. Source readiness returned HTTPS 200.
- Backup 0.703 seconds; restore plus comparison 0.313 seconds for 20,959 bytes. These are fixture observations, not recovery guarantees. Runbook separates app rollback, transactional migration failure and database recovery; no prior deployed app release was available for an app rollback drill.
- Backup, secrets, restore target and existing services retained. Hosted retention/cadence, RPO/RTO, off-machine recovery and independent review remain unresolved. No cleanup or cloud/GitHub activity.
- Totals: 21 Done, 1 Blocked, 3 In review, 80 Not started. B025 In review for local acceptance; B026 unstarted.

### 21 October 2026 — B025 local recovery approved

- User “Approve B025” accepts the verified local backup/restore and rollback assessment; B025 Done for that scope.
- Existing eight recovery/control groups and full local-runner evidence retained. Documentation-only approval; no tests rerun or service/data changes.
- Totals: 22 Done, 1 Blocked, 2 In review, 80 Not started. Phase 1: 17 of 20 Done for accepted local scopes. B026 unstarted.
- Pre-approval records: docs/evidence/B025-before-acceptance.zip. Hosted recovery policy/targets, off-machine recovery and independent review remain deferred. Backup, restored database and existing services retained; no cleanup.

### B026 local foundation verification delivered

- User “Start with B026” selected verification of the retained local rehearsal after B025 approval. Six real HTTPS/API/database groups and the full local check runner passed.
- Shared dashboard browser check on B022 showed three accessible references, hidden-owner zero and successful logout. Initial sign-in failed and recovered after explicit logout/retry; cause unproven, B026-OBS-01 remains open for review.
- [Evidence](docs/evidence/B026-local-foundation.md) distinguishes programmatic B024 TLS integration from B022 browser checks and carried-forward B024 database-failure evidence. Hosted/real-identity/remote-CI/independent-review requirements remain deferred.
- No source application changes, service restart, fixture/schema mutation or cleanup. Totals: 22 Done, 1 Blocked, 3 In review, 79 Not started. B026 In review; B027 unstarted.

### 21 October 2026 — B026 local verification approved

- User “Approve B026” accepts the verified local foundation scope; B026 Done for that scope.
- Six live HTTPS/API/database groups, full local runner and supplemental browser evidence retained. Documentation-only acceptance; no tests rerun, service changes or cleanup.
- B026-OBS-01 remains open: initial browser sign-in failure recovered after explicit logout/retry, cause unproven. Approval does not close the observation or establish hosted staging, trusted-browser HTTPS, real identity, remote CI or independent review.
- Totals: 23 Done, 1 Blocked, 2 In review, 79 Not started. Phase 1: 18 of 20 Done for accepted local scopes. B027 unstarted.
- Pre-approval records: docs/evidence/B026-before-acceptance.zip. All previews, backups and database resources retained.

### 21 October 2026 — B027 local support/accessibility delivered

- User “Start B027” selected local verification/handover. Exact locked npm downloads were explicitly approved after confirmed offline cache misses. Prior records: B027-before.zip.
- Fresh source copy, new Python/npm installs, full local CI, PostgreSQL checks and production build passed. Fixed the copy runner's missing public template and retained the failed/resumed evidence.
- Added alternate loopback ports and safe operational capture to the explicit rehearsal launcher. New independent persistent rehearsal at https://127.0.0.1:3543 passed six real HTTPS/database/failure/recovery groups; 24 actual log events passed allowlist/redaction checks.
- Keyboard, semantic accessibility-tree and mobile/desktop evidence recorded. Spoken screen-reader walkthrough remains outstanding; no conformance/hosted staging claim. B026-OBS-01 remains open. Existing services/data untouched; additional setup folders/databases/rehearsal retained.
- Final working local runner: 73 source/config files, 70 backend tests, 5 runner tests, dashboard contract and all three TypeScript checks passed. B027 In review for local scope; B028 unstarted. Totals: 23 Done, 1 Blocked, 3 In review, 78 Not started.

### 21 October 2026 — B027 local scope approved

- User “Approve B027” accepts the verified local setup, keyboard/responsive/semantic evidence and operational-log handover; B027 Done for that scope.
- Existing fresh-install/build, 70 backend/5 runner tests, six integrated rehearsal groups and 24 redacted log-event checks retained. Documentation-only acceptance; no tests rerun, service changes or cleanup.
- Spoken screen-reader walkthrough remains outstanding. B026-OBS-01 stays open; hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. Approval does not establish accessibility conformance or G1 acceptance.
- Totals: 24 Done, 1 Blocked, 2 In review, 78 Not started. Phase 1: 19 of 20 Done for accepted local scopes. B028 unstarted.
- Pre-approval records: docs/evidence/B027-before-acceptance.zip. All services, setup attempts, containers, volumes and backups retained.

### 21 October 2026 — B028 foundation demonstration and review prepared

- User “Start B028” authorises gate assessment, not acceptance. [Review pack](docs/evidence/B028-foundation-review.md) traces all 19 accepted B009–B027 local scopes and distinguishes evidence from original criteria.
- Current retained rehearsal demo passed verified TLS/UI delivery/readiness, synthetic login, three permitted stored references, hidden record/owner denial and logout replay. Direct mock component produced a draft, rejected malformed output and blocked live mode before adapter invocation. No external provider calls.
- Full local runner passed: 74 source/config files, 70 backend tests, 5 runner tests, dashboard contract and all three TypeScript checks. Existing recovery/browser/failure/log evidence carried forward with dates/limits; no repeated database fault or cleanup.
- Original G1 Hold: named Justice technical and CEO functional decisions, independent review and original-scope staging/identity assurance remain absent. Spoken-reader walkthrough/B026-OBS-01 and other scoped deferrals remain open. No criteria silently changed.
- [G1-L v0.1](docs/planning/G1-local-foundation-proposal.md) is a concrete proposed local milestone only; adoption requires an explicit user decision. Full G1 would stay held. No B029/Phase 2 execution authority inferred.
- B028 In review. Totals: 24 Done, 1 Blocked, 3 In review, 77 Not started. Phase 1: 19 Done, 1 In review. All services/resources retained. Pre-change records: B028-before.zip.

### 21 October 2026 — G1-L v0.1 adopted; B028 accepted for local scope

- User “Adopt G1-L v0.1 and accept B028 for local scope only” explicitly adopts the reviewed milestone and retained deferrals. [Reassessment](docs/evidence/B028-g1-local-adoption.md) passes adopted local criteria; B028 Done for G1-L only.
- Full G1 remains Hold. No Justice/CEO/independent sign-off, hosted/real-identity/remote-CI assurance or issue closure inferred. Spoken-reader walkthrough and B026-OBS-01 remain open.
- Documentation-only adoption; existing demo/check/recovery/log evidence retained, no tests rerun or source/service/data changes. Pre-adoption records: B028-before-local-adoption.zip.
- Totals: 25 Done, 1 Blocked, 2 In review, 77 Not started. Phase 1: 20 of 20 Done for accepted local scopes. B029 unstarted; no automatic Phase 2 execution or release authority.

### 21 October 2026 — B007 planning reconciliation revisited

- User “Let's work on B007” authorises documentation reconciliation. Preserved [pre-change records](docs/evidence/B007-before-foundation-reconciliation.zip); original task criteria and accepted statuses unchanged.
- Reconciled 20 B009–B028 cards with actual accepted local evidence, owner/executor distinctions and test results. Removed stale blanket current Not Ready/no-tests assertions without backdating initial readiness. Nine D006 fields structurally present for all 20 cards; no estimate/date invented.
- Refreshed [design/operations worksheet](docs/planning/phase-1-design-operations.md) identifies already-approved local design/metric/tooling/rehearsal choices and required authorities/triggers before external/full-scope actions.
- [B007 reassessment](docs/evidence/B007-foundation-reconciliation.md) keeps B007 In review: Justice's personal interim-role acceptance and a local cadence decision remain pending. B005/full-G1 reviews, spoken-reader check and B026-OBS-01 remain open. No silent criteria change.
- Documentation-only checks; no runtime tests repeated, source changes, GitHub/network activity, service changes or cleanup. Totals unchanged: 25 Done, 1 Blocked, 2 In review, 77 Not started. B029 unstarted.

### 21 October 2026 — B007 local planning completed

- User answered “Yes” to the explicit Justice interim-role acceptance question and “Approve this task-by-task local cadence”. Record acceptance as user-confirmed, not a claim that the user is Justice or that formal reviews were signed.
- Earlier pack approval plus the reconciled local scope/design/dependencies and these decisions complete B007 for approved local planning. [Completion record](docs/evidence/B007-local-completion.md). No original/full-scope criterion silently waived; B005/full-G1 reviews and operational checkpoints remain.
- Twenty card titles/scopes/acceptance checks and nine-field/evidence coverage verified. Documentation-only update; no runtime tests rerun, source/config/service changes or cleanup. Pre-update records: B007-before-owner-cadence-acceptance.zip.
- Totals: 26 Done, 1 Blocked, 1 In review, 77 Not started. B004 Blocked; B005 In review. B029 unstarted; all resources retained.

### 21 October 2026 — main reference dashboard connected on user request

- User “Improve the functionalities and connect the reference dashboard” authorises this local follow-up; not B029. Replaced disconnected home panel and added /dashboard/sidebar entry, same-origin restricted API bridge to retained B027 HTTPS with dedicated public CA and no trust bypass.
- Improved restored/repeated/stale sessions, accurate header state, quick views, Clear filters, refresh/time, reference rows and accessible labels. Synthetic fixed identity/permissions preserved; future business modules remain unavailable.
- [Main-API groups](docs/evidence/main-dashboard-checks.json), actual browser journeys/mobile layout and full local runner passed (79 source/config, 70 backend/5 runner tests, contract/types). Separate production build/source-copy hashes passed after visual CSS refinement; no running build replaced.
- [Evidence](docs/evidence/main-dashboard-connection.md), [snapshot](docs/evidence/main-dashboard-before.zip). No package install, database fixture/schema changes, existing service restart or cleanup. All retained resources preserved. Numbered task states unchanged; B029 unstarted and full G1 Hold.

### 21 October 2026 (Atlantic/Reykjavik) — B005 current architecture review

- User “Let's sort out B005” selected the pending architecture review. Refreshed all four ADRs against the built synthetic foundation and current dashboard bridge; prepared explicit selections, rejected alternatives, rationale and consequences.
- [Current review](docs/evidence/B005-current-architecture-review.md) records D005-01–D005-09 deliberate deferrals with authorities/checkpoints. No real identity/provider/hosting choice or technical outcome inferred from existing implementation.
- [Snapshot](docs/evidence/B005-before-current-review.zip) retains original inputs. Documentation/link/count/preservation checks recorded; no runtime rerun for this documentation-only change.
- B005 remains In review pending Justice's technical outcome. Totals unchanged: 26 Done, 1 Blocked, 1 In review, 77 Not started. B029 unstarted; original full G1 Hold; all resources retained.

### 21 October 2026 (Atlantic/Reykjavik) — B005 technical acceptance recorded

- User answered “Justice approves the four local ADR decisions and listed deferrals” to the explicit ADR-001–004/D005-01–D005-09 question. Recorded as user-confirmed Justice technical approval, without inferring personal identity or a direct signature.
- [Acceptance record](docs/evidence/B005-local-architecture-acceptance.md): B005 Done for approved local architecture. O-03 Partly resolved for the local baseline; O-04 Partly resolved. Hosted/real identity/operational/job choices retain their stated authorities and checkpoints.
- Totals: 27 Done, 1 Blocked (B004), 0 In review, 77 Not started. Original full G1 Hold; independent/CEO reviews separate. B029 unstarted; all services/data retained.

### B005 — Explicit user acceptance confirmed

- User “Approve B005” confirms acceptance of the completed local architecture review. [Acceptance record](docs/evidence/B005-local-architecture-acceptance.md) updated; earlier user-confirmed Justice technical approval preserved.
- B005 remains Done for the approved local scope. Counts unchanged: 27 Done, 1 Blocked, 0 In review, 77 Not started. All deferrals remain binding; full G1 Hold, B029 unstarted and all resources retained.

## 11. Current handoff

**Current browser work:** [Connected main dashboard](http://127.0.0.1:3000/dashboard), [verification](docs/evidence/main-dashboard-connection.md). Delivered for user review; G1 restrictions preserved.  
**Architecture review:** [B005 technical acceptance](docs/evidence/B005-local-architecture-acceptance.md), local architecture adopted with explicit deferrals.  
**Deliverable:** [B007 local completion](docs/evidence/B007-local-completion.md), [approved local workflow](docs/planning/phase-1-design-operations.md), [20 reconciled cards](docs/planning/phase-1-work-items.md) and [checks](docs/evidence/B007-readiness-reconciliation-checks.json).  
**Status:** B007 Done for approved local planning; B005 Done for approved local architecture; B004 Blocked. 27 Done, 0 In review, 77 Not started. B009–B028 local scopes Done; G1-L accepted; original full G1 Hold.  
**Next:** B029 awaits separate user selection. Preserve [D005-01–D005-09 checkpoints](docs/evidence/B005-current-architecture-review.md). Independent/CEO acceptance and Phase 2 decisions remain separate; B029 unstarted.  
**Boundary:** Existing local-only restrictions, full-scope review/operational checkpoints and every G1-L deferral persist. Spoken-reader verification and B026-OBS-01 remain open. No external/release authority.  
**Retention:** All previews, setup attempts, containers, volumes and backups preserved; no cleanup.

## 22 October 2026 — Local opening and access flow

User requested opening animation, login/sign-up, then homepage. Added EntryJourney around the main shell: 2.2-second branded opening, Skip, reduced-motion bypass, login/sign-up views, explicit demo acknowledgement for sign-up, existing synthetic session login, and home entry after success. Session invalidation/sign-out returns to access. Added /sign-up and replaced obsolete /sign-in unavailable content. Real registration remains deferred and the UI states that no personal account is created; no credentials collected.

Verification: main TypeScript check passed. Browser verified login/sign-up switching, disabled/enabled demo consent control and recoverable failed-login feedback. Homepage transition could not be verified because the retained session service at port 3543 was unavailable. Main frontend started at http://127.0.0.1:3000 for review. Existing data/services were not removed or rebuilt. Numbered task status and real identity/hosting deferrals unchanged.

### 22 October 2026 — Demo sign-in restored

User: “Allow me to sign in.” Resumed the exact retained B027 reference HTTPS API using backend/resume_reference_service.py. It checks the retained container label, loopback database binding, runtime identity scope, migration count and matching public CA. It uses existing runtime credentials and TLS files without printing them. No seed, migration, database restart, trust bypass or container replacement. Operational capture retained. Browser login succeeded and Command Centre displayed an active synthetic session with all three permitted reference records. Screenshot: docs/evidence/entry-signin-restored.png. This supersedes the unavailable-service verification limit above. API and main preview left running for the user.

## 22 October 2026 — Personal local accounts and saved ideas

User requested working standalone sign-in after selecting online CPA email/password accounts, then asked “Let the sign in process work.” Implemented a workstation-only interim account flow; the online objective remains outstanding pending hosting/account access and budget. No cloud deployment or verified email ownership is claimed.

Main frontend now uses /api/account for signup/login/status/logout and account-owned saved ideas. It no longer admits the shared demo identity or displays fixture counts in the normal homepage. Name/email/password/confirmation form, session restoration, idle expiry, logout and personal empty dashboard are connected. User must enter their own password; dev1@dwentech.com is only prefilled, not provisioned by the agent.

Implementation choice: isolated SQLite at .local/accounts/accounts.sqlite under an owner-only Windows ACL, using installed Node sqlite and scrypt (N=32768,r=8,p=3), random salts, hashed opaque sessions, 30-minute idle/8-hour absolute expiry, request limits, persisted attempt throttling, exact loopback Host/Origin checks and account-scoped data queries. This is a local interim store, not a replacement hosted architecture decision. Existing PostgreSQL fixtures and retained services remain intact. Real email verification, recovery, hosted HTTPS, online sync and multi-device use remain unfinished. The local adapter rejects other origins.

Verification: frontend typecheck and complete local runner passed. scripts/test-local-accounts.mjs passed password, duplicate/weak signup, persistence, isolation, expiry, logout and throttle checks in a separate retained temporary database. scripts/test-account-http.mjs passed actual HTTP signup/login, bad password, cookie flags, protected routes, origin denial, saved idea reload, logout replay and two-account isolation. Reserved example.test test accounts are retained separately; no user's account/password was created. Browser verified labelled real signup fields, password guidance, honest local-only notice. Screenshot: docs/evidence/personal-account-signup.png.

## 22 October 2026 — Administrator and external-user access

User requested administrative access plus a separate external-user login, and said they would enter the emails themselves. Added persisted server-owned admin/external roles and enabled state through an additive local SQLite migration. Existing/new ordinary accounts default to external. No personal email was promoted automatically.

Prepared a one-use administrator setup link valid for 24 hours. Its token is stored only as a digest; no HTTP endpoint issues setup links. The user chooses an email and signs up, or logs in to upgrade their existing account. Redemption follows password verification, atomically consumes the token, records an audit event and revokes prior sessions. The user enters their own password and completes account setup. Ordinary signup cannot set role via request fields.

Administrator UI at /admin lists account name/email/role/status and allows suspending/reactivating external users. Server enforces admin permission and revokes affected sessions; suspended users cannot authenticate. Admin accounts cannot be suspended through this screen. Administrator visibility does not include another user's saved-idea content. External users retain their own dashboard/ideas only. Header shows actual role and provides Sign out / switch account; login email no longer prefilled. No external email is reserved or invented.

Verification: role tests passed (privilege-field injection denied, hashed/single-use setup, new signup and existing-account promotion, old-session revocation, metadata-only admin listing, external denial, suspend/reactivate, audit, content isolation). Existing account tests and actual HTTP checks passed, including GET/POST admin denial for external users. TypeScript passed. All test data retained; no personal password created or collected by the agent. Online hosting still outstanding; these roles apply to the current local application.

## 22 October 2026 — Dashboards follow the signed-in role

User requested administrator dashboard for administrators and personal dashboard for other users. Added a verified-account context shared by entry gate, header and navigation; login/signup/session restore route admin to /admin and external to /dashboard. Root and incorrect dashboard URLs resolve to the same role destination before rendering dashboard children. Role refresh checks update the common account state; logout unmounts all account-specific UI before switching.

Administrator dashboard now displays live account counts (total/external/active/suspended), name/email search, account-status filters and suspension/reactivation controls. External dashboard welcomes the signed-in user and loads only that account's stored ideas. Sidebar dashboard label/URL and role badge follow the server account role. Existing API administrator checks and owner-scoped idea queries retained.

Validation: navigation matrix and role/authorization tests passed; full local runner passed (94 source/config files, dependency consistency, backend/runner tests, dashboard contract and all three frontend TypeScript projects). Browser verification uses a clearly named reserved example.test account; no user password accessed and the user's pending administrator setup link preserved. Test identity will be disabled after browser checks, with sessions revoked. These dashboards remain in the local application; online hosting is still outstanding.

### Role-dashboard browser verification completed

Reserved browser-check account verified administrator login -> /admin, account overview/search, and administrator direct /dashboard -> /admin. The same reserved account was switched to external with sessions revoked, then verified login -> /dashboard, external-only navigation, own idea creation/count and saved list. Screenshots: docs/evidence/role-admin-dashboard.png and docs/evidence/role-user-dashboard.png. Existing personal accounts and the pending administrator setup token were not modified. Browser-check sessions are revoked and its synthetic account disabled after verification; retained idea data is preserved.

## 22 October 2026 — Correct administrator assignment and distinct console

User reported their admin dashboard still matched a normal user. Diagnosis: both actual registered accounts (dev1@dwentech.com and dappahsonnia@gmail.com) still had the external role, and the one-use administrator setup was pending. User explicitly selected dev1@dwentech.com for administrator access in chat. Applied that exact role change transactionally, recorded administrator_assigned in account_audit, revoked that account's existing sessions and invalidated pending setup tokens. dappahsonnia@gmail.com remains enabled/external. No password was accessed or changed.

Admin sidebar now contains Administrator dashboard, User management and Access overview instead of the normal user's planned workspace navigation. Added a distinct green/navy administration console header, administrator-access badge, management shortcut and overview styling. Account counts and access controls continue using authorized persisted data; external user's own ideas dashboard remains separate.

Validation: database readback confirmed dev1 admin and dappahsonnia external; role/navigation tests and frontend typecheck passed. User must sign in again as dev1@dwentech.com to obtain the administrator session. This supersedes the earlier assumption that providing a setup link had completed the user's administrator assignment.
