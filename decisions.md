# CPA Decision Register

**Version:** 3.6 · **Updated:** 21 October 2026 (Atlantic/Reykjavik) · **Status:** Local record structure and workflow accepted under B003

This is the authoritative current decision register. [Progress](progress.md) owns task status; [build order](build-order.md) owns scope and order; [risks](risks.md) owns risk records. [B002](docs/evidence/B002-baseline-reconciliation.md) preserves conflict dispositions and explicit user answers. Roles below identify required authority, not accepted personal assignments. Dates and named assignees remain unset.

## Maintenance

Use Open, Partly resolved, Resolved or Superseded. Record the exact decision, authority, date, evidence, affected tasks and consequences before marking Resolved. Preserve superseded outcomes in dated history and link replacement ADRs. Unknown values are not unlimited or approved. Review dependent task readiness after changes; drafting a decision never grants approval.

## Current decisions

<a id="o-01"></a>
### O-01 — Scope, team clarification and priorities

- **State:** Partly resolved; scope/priorities open.
- **Required authority:** CEO/product owner and Justice.
- **Checkpoint / affected tasks:** [B002](build-order.md), [B007](build-order.md)–[B008](build-order.md).
- **Evidence / limits:** User confirmed human developer with AI assistance in B002.

<a id="o-02"></a>
### O-02 — Repository access, protections and reviewer workflow

- **State:** Open.
- **Required authority:** Justice.
- **Checkpoint / affected tasks:** [B004](build-order.md).
- **Evidence / limits:** User defers all GitHub activity; B004 local preflight is complete but current controls remain unverified. B004 is Blocked pending explicit read-only access authority or an approved recorded local-only replan; see [B004 report](docs/evidence/B004-local-preflight.md).

<a id="o-03"></a>
### O-03 — Architecture and hosting boundaries

- **State:** Partly resolved; local architecture adopted, hosting and future choices deferred.
- **Required authority:** Justice.
- **Checkpoint / affected tasks:** [B005](build-order.md).
- **Evidence / limits:** Local B005 review prepared: [ADR-001 stack](docs/adr/001-core-stack.md), [ADR-003 environments](docs/adr/003-environments.md) and [ADR-004 boundaries](docs/adr/004-service-boundaries.md). Refreshed [current review](docs/evidence/B005-current-architecture-review.md) proposes four concrete local selections with D005-01–D005-09 deliberate deferrals. User subsequently confirmed Justice approves all four local decisions and listed deferrals; see [technical acceptance](docs/evidence/B005-local-architecture-acceptance.md). Remote alignment unverified; hosting/operational choices stay open.

<a id="o-04"></a>
### O-04 — Identity, role grants and client/record isolation

- **State:** Partly resolved for approved synthetic B013/B014/B016 policies; real identity, tenancy and operational assignments remain open.
- **Required authority:** Justice; product owner for business access.
- **Checkpoint / affected tasks:** [B005](build-order.md), [B013](build-order.md)–[B016](build-order.md).
- **Evidence / limits:** Local B005 [ADR-002 identity, roles and tenancy](docs/adr/002-identity-roles-tenancy.md) prepared. Approved synthetic policies are recorded below; real identity/tenancy and named grants remain open. [Current architecture review](docs/evidence/B005-current-architecture-review.md) proposes local technical acceptance without expanding those grants.
- **20 October 2026 proposal scope:** User selected “Include client sign-in in the proposal” for [B013](docs/evidence/B013-local-authorisation.md). Include client identity/enrolment/membership and isolation in local design. O-04 remains Open: no provider, grants, tenancy design, client-portal implementation or release enablement approved.

- **Recommended matrix:** [B013 access matrix v0.1](docs/planning/B013-recommended-access-matrix.md), drafted at user request for Justice approval. Invite-only identity, explicit grants, private client intake, scoped administration and revocation are recommendations only. O-04 remains Open; no grants or named assignments approved.

- **20 October 2026 local implementation authority:** User “Approve B013 to continue” adopts matrix v0.1 for local synthetic implementation. Core identity/record permissions implemented and tested; [B013 execution evidence](docs/evidence/B013-local-authorisation.md) is In review. Earlier proposed/unapproved entries above are historical. No approval is attributed to Justice personally; formal B006/independent reviews, named real-account bootstrap and B014 session/MFA/provider choices remain deferred. No live operation or external access inferred.

- **B014 policy proposal — 20 October 2026:** [Local session policy v0.1](docs/planning/B014-local-session-policy.md) is ready for decision. Opaque server-stored sessions and expiry/MFA restrictions are proposed only; user answer pending. B013 remains accepted; no identity provider or password system selected.

- **B014 local policy approved — 20 October 2026:** User answered “Approve this local baseline”. Adopted v0.1 opaque server-stored sessions, 30-minute idle/8-hour absolute expiry, no refresh, immediate revocation checks and privileged denial pending MFA. [B014 execution evidence](docs/evidence/B014-local-authentication.md) is In review: 26 unit/API tests and 33 PostgreSQL/HTTP groups passed. Earlier session-policy-pending wording above is superseded for this local scope. Provider integration, real login/browser/session UI, live MFA and named assignments remain open; O-04 stays Partly resolved.

- **B016 local integration approved — 20 October 2026:** User approved the isolated synthetic journey and local cookie baseline. Adopted HttpOnly/SameSite=Strict host-only cookie, same-origin server-side Bearer forwarding and origin checks solely for loopback testing. [B016 evidence](docs/evidence/B016-local-sign-in.md) is In review. Real human login/provider, live MFA, production Secure-cookie/TLS configuration and formal reviews remain deferred. Earlier browser-integration-pending wording is superseded only for this approved local scope.

<a id="o-05"></a>
### O-05 — Jobs, recovery, cancellation and idempotency

- **State:** Open.
- **Required authority:** Justice.
- **Checkpoint / affected tasks:** [B029](build-order.md), [B035](build-order.md)–[B036](build-order.md).
- **Evidence / limits:** Not recorded.

<a id="o-06"></a>
### O-06 — Sources, licences, evidence grades and freshness

- **State:** Partly resolved; limited local policy user-approved, specialist and use-specific reviews open.
- **Required authority:** Product/research owner and Justice.
- **Checkpoint / affected tasks:** [B006](build-order.md), [B029](build-order.md), [B082](build-order.md).
- **Evidence / limits:** [B006 policy v0.2](docs/policies/allowed-data-and-test-fixtures.md) records user approval for limited local scope. Specialist review is deferred before affected implementation/data use; no source-specific rights, live-data permission or retention duration approved.

<a id="o-07"></a>
### O-07 — Model routing, credentials, budgets, quotas and limits

- **State:** Open.
- **Required authority:** Justice and authorised budget owner.
- **Checkpoint / affected tasks:** [B019](build-order.md), [B029](build-order.md), [B037](build-order.md)–[B039](build-order.md).
- **Local B019 evidence:** User selected B019 on 21 October 2026. [Local controls](docs/evidence/B019-local-ai-controls.md) validate settings but unconditionally deny live calls; mock usage cost remains unknown. Actual model, budget, currency, quotas, pricing, concurrency and live enablement policy remain Open. User “Approve B019” accepted the tested local implementation on 21 October 2026; actual live policy remains open.

<a id="o-08"></a>
### O-08 — Export formats and private storage

- **State:** Open.
- **Required authority:** Product owner and Justice.
- **Checkpoint / affected tasks:** [B029](build-order.md), [B048](build-order.md), [B082](build-order.md).
- **Evidence / limits:** Not recorded.

<a id="o-09"></a>
### O-09 — Lifecycle, archive, versioning and review permissions

- **State:** Open.
- **Required authority:** Product owner and Justice.
- **Checkpoint / affected tasks:** [B029](build-order.md), [B043](build-order.md)–[B047](build-order.md), [B057](build-order.md).
- **Evidence / limits:** Not recorded.

<a id="o-10"></a>
### O-10 — Scoring, incomplete ratings and recommendation vocabulary

- **State:** Partly resolved; scoring/semantics open.
- **Required authority:** Product owner and Justice.
- **Checkpoint / affected tasks:** [B029](build-order.md), [B041](build-order.md), [B057](build-order.md), [B082](build-order.md).
- **Evidence / limits:** User confirmed Continue, Improve, Pivot, Pause, Stop in B002.

<a id="o-11"></a>
### O-11 — Navigation, design tokens/assets and phased content

- **State:** Partially resolved for B015 local shell; full product/service design remains open.
- **Required authority:** Product owner and Justice.
- **Checkpoint / affected tasks:** [B007](build-order.md), [B015](build-order.md).
- **Evidence / limits:** On 20 October 2026 the user approved offline-only dependency installation, a derived local colour/spacing/type baseline, D005 navigation labels and visible “Not available yet” states. [B015 report](docs/evidence/B015-local-navigation.md) records values and checks. No live dashboard metrics, search, notifications, sign-in or provider readiness approved. Independent review remains separate.

- **B007 preparation:** [Design/operations approval worksheet](docs/planning/phase-1-design-operations.md) records proposed scope, prerequisites and unresolved choices. No design, numeric limit, named assignment or schedule approved by drafting.

- **B007 current reconciliation — 21 October 2026:** B015 local tokens/navigation/unavailable states and B021/B022 synthetic reference count/filter contract are user-approved and implemented. [Current worksheet](docs/planning/phase-1-design-operations.md) no longer treats these local decisions as unanswered. Business KPIs/full product design and spoken-reader verification remain open. This is evidence reconciliation, not new design approval.

<a id="o-12"></a>
### O-12 — Privacy, consent, rights, retention and sensitive inputs

- **State:** Partly resolved; limited local policy user-approved, specialist and use-specific reviews open.
- **Required authority:** CEO-designated policy owner and Justice.
- **Checkpoint / affected tasks:** [B006](build-order.md), [B067](build-order.md), [B101](build-order.md).
- **Evidence / limits:** [B006 policy v0.2](docs/policies/allowed-data-and-test-fixtures.md) records user approval for limited local scope. Specialist review is deferred before affected implementation/data use; no source-specific rights, live-data permission or retention duration approved.

- **B017 local baseline approved — 20 October 2026:** User approved the local event baseline and disposable storage baseline. [Approved contract](docs/planning/B017-local-audit-baseline.md) limits capture to synthetic events and minimum request metadata, runner-only disposable storage and end-of-run deletion. [Executed evidence](docs/evidence/B017-local-audit.md) is In review. No persistent/production retention, audit-viewer grant, live-data use or formal review inferred; O-12 remains partly resolved.

<a id="o-13"></a>
### O-13 — Voice provider, supported interactions and transcript rules

- **State:** Open.
- **Required authority:** Product owner and Justice.
- **Checkpoint / affected tasks:** [B067](build-order.md).
- **Evidence / limits:** Not recorded.

<a id="o-14"></a>
### O-14 — Website intake, outbound channels and approval flow

- **State:** Open.
- **Required authority:** Product owner and Justice.
- **Checkpoint / affected tasks:** [B067](build-order.md).
- **Evidence / limits:** Not recorded.

<a id="o-15"></a>
### O-15 — Geography, languages, regions, coverage and maps

- **State:** Open.
- **Required authority:** Product/research owner and Justice.
- **Checkpoint / affected tasks:** [B082](build-order.md).
- **Evidence / limits:** Not recorded.

<a id="o-16"></a>
### O-16 — Performance, recovery targets, sizing and operating ceiling

- **State:** Open.
- **Required authority:** Justice and CEO.
- **Checkpoint / affected tasks:** [B007](build-order.md), [B023](build-order.md), [B100](build-order.md)–[B102](build-order.md).
- **Evidence / limits:** Not recorded.

- **B007 preparation:** [Design/operations approval worksheet](docs/planning/phase-1-design-operations.md) records proposed scope, prerequisites and unresolved choices. No design, numeric limit, named assignment or schedule approved by drafting.

- **B007 current reconciliation — 21 October 2026:** B025 manual local backup/separate restore and B027 isolated setup/build/rehearsal evidence are available. Their measured fixture timings do not resolve agreed workload, capacity, sizing, spending or RPO/RTO targets. Required role/trigger checkpoints are explicit in the current worksheet; no numeric target or price selected.

<a id="o-17"></a>
### O-17 — Domain, support/incident ownership and release process

- **State:** Open.
- **Required authority:** CEO and Justice.
- **Checkpoint / affected tasks:** [B007](build-order.md), [B100](build-order.md)–[B104](build-order.md).
- **Evidence / limits:** Not recorded.

- **B007 preparation:** [Design/operations approval worksheet](docs/planning/phase-1-design-operations.md) records proposed scope, prerequisites and unresolved choices. No design, numeric limit, named assignment or schedule approved by drafting.

- **B007 current reconciliation — 21 October 2026:** Local setup/support/recovery instructions exist under B025/B027; resources are retained by user instruction. Named incident/support/rollback ownership, domains and hosted release process remain open before affected reliance. No assignment acceptance inferred.

<a id="o-18"></a>
### O-18 — Estimates, assignments, cadence and success measures

- **State:** Partly resolved.
- **Required authority:** Justice and CEO.
- **Checkpoint / affected tasks:** [B003](build-order.md), [B007](build-order.md).
- **Evidence / limits:** Local record structure and maintenance workflow accepted by the user under B003 on 20 October 2026 UTC; local interim-owner acceptance and task/chat cadence are now user-confirmed; estimates, future allocations, calendar/team cadence and broader operational success targets remain open.

- **B007 preparation:** [Design/operations approval worksheet](docs/planning/phase-1-design-operations.md) records proposed scope, prerequisites and unresolved choices. No design, numeric limit, named assignment or schedule approved by drafting.

- **User clarification (20 October 2026 UTC):** Justice nominated as interim implementation owner and product/scope approver; assignment acceptance not recorded. Carry forward source cadence as a proposal; operating details and approval remain open. No GitHub connection permitted.

- **B007 current reconciliation — 21 October 2026:** Justice remains nominated; personal role acceptance is not recorded. Actual local executor/task approval history is now explicit. A concrete task-by-task local cadence is prepared for decision, with no calendar schedule/reminder or outbound action. Estimates/dates remain unset; they are not additional fields in D006's nine-field Ready definition. Formal team cadence/review assignments remain separate.

- **B007 decisions completed — 21 October 2026:** User answered “Yes” confirming Justice accepted the interim implementation-owner/product-scope role and explicitly approved the task-by-task local cadence. This is user-reported acceptance, not user identity or a Justice/independent/CEO technical signature. Earlier pending local-role/cadence wording is superseded; future assignments/formal reviews/calendar commitments remain separate. [B007 completion](docs/evidence/B007-local-completion.md).

## History

| Date | Authority | Outcome |
| --- | --- | --- |
| 20 October 2026 UTC | User B001 acceptance | Existing folder selected; GitHub deferred. See [B001](docs/evidence/B001-baseline-inventory.md). |
| 20 October 2026 UTC | User B002 answers | Human developer with AI assistance; Continue, Improve, Pivot, Pause, Stop. Broader scope/scoring rules remain open. See [B002](docs/evidence/B002-baseline-reconciliation.md). |
| 20 October 2026 UTC | User: “I have accepted B002” | Local reconciliation accepted; no architecture or gate approval inferred. |
| 20 October 2026 UTC | User: “Start B003” | Local records prepared for review; O-18 broader choices remain open. |

| 20 October 2026 UTC | User: “I accept the B003 local record structure and maintenance workflow.” | B003 Done; O-18 remains partly resolved because estimates, assignments, cadence and success measures remain open. |

| 20 October 2026 UTC | User: “Start B004” | Local preflight recorded; O-02 remains Open and B004 Blocked because the explicit GitHub deferral has not been lifted. No dependency replan made. |

| 20 October 2026 UTC | User controlled B005 exception | Local independent architecture review authorised while B004 stays Blocked. Four proposed ADRs prepared; O-03/O-04 remain Open. No Justice technical acceptance, provider adoption or gate approval inferred. |

| 20 October 2026 UTC | User: “I accept B005” | Local review accepted by user; Justice review evidence remains outstanding. O-03/O-04 remain Open; no architecture option or grant selected. |

| 20 October 2026 UTC | User: “Start B006” | Local policy draft prepared; O-06/O-12 remain Open. Earlier B004/B005 review requirements are retained; no live-data approval inferred. |

| 20 October 2026 UTC | User: “Approve B006” | Limited local policy accepted; B006 Done. Specialist reviews and architecture-dependent controls remain deferred, not approved by attribution. O-06/O-12 partly resolved only. |

| 20 October 2026 UTC | User: “Start B007” | Local Phase 1 refinement prepared. O-11/O-16/O-17 remain Open; remaining O-18 choices remain open. No estimate, owner assignment or approval fabricated. |

| 20 October 2026 UTC | User B007 answers | Carry forward cadence as proposal; no GitHub connection. Justice nominated provisionally for implementation ownership and product/scope approval. No scope/technical sign-off or independent reviewer eligibility inferred. |

| 20 October 2026 UTC | User: “Approve B007” | Local planning pack approved. Unanswered O-11/O-16/O-17 and remaining O-18 choices remain open; no technical outcome, assignment acceptance, budget or gate approval inferred. B007 In review pending Definition of Ready evidence. |

| 20 October 2026 UTC | User: “Start B008”; local evidence assessment | G0 Hold, B008 Blocked. [Assessment](docs/evidence/B008-g0-readiness-assessment.md) records unresolved evidence and authority requirements; no substantive open decision or phase gate approved. |

| 20 October 2026 UTC | Explicit user approval of G0-L v0.1 and B009 local scope | Adopted revised local gate; [reassessment](docs/evidence/B008-g0-local-reassessment.md) passed. B008 Done for local scope only. Original governance and technical choices remain deferred; B009 not started. No substantive O-02/O-03/O-04 resolution inferred. |

## 20 October 2026 UTC — B012 local execution selection

User explicitly approved a usable local PostgreSQL destination, migration approach, initial schema and actual migration/recovery checks. Recorded task-level choice: existing offline Docker PostgreSQL 17 image; installed psycopg 3.3.6; ordered SQL with transactional migration history/checksums; initial `cpa_meta.schema_migrations` bookkeeping and empty `cpa` namespace. Temporary synthetic recovery fixtures are removed after checks. This supersedes the database-setup deferral only for this disposable local scope. Nine actual database checks passed on PostgreSQL 17.11; [evidence](docs/evidence/B012-local-database.md).

O-03 remains open for broad architecture/hosting approval; O-04 remains open for identity, grants and tenancy. No business schema, runtime role grants, GitHub, downloads, installs, cloud, real-client data or deployment approved. B012 acceptance of the executed deliverable remains pending.

### B012 acceptance — 20 October 2026 UTC

User: “I accept B012”. Executed local scope accepted; B012 Done. The preceding pending-acceptance statement is superseded. O-03/O-04 remain open for their broader architecture/access decisions; no further implementation or external activity implied.

### B013 local acceptance — 20 October 2026 UTC

User: “i accept B013”. Executed local identity/reference and permission-boundary deliverable accepted; B013 Done. The earlier In review status is superseded. O-04 remains partly resolved: local policy is approved, while B014 identity/session/MFA choices and named operational assignments remain open. Formal specialist/independent review and deployment assurances remain deferred.

### B014 local acceptance — 20 October 2026 UTC

User: “Approve B014”. Executed local backend session validation accepted; B014 Done. The earlier In review status is superseded. O-04 remains Partly resolved: provider integration, real login/browser flow, live MFA and named operational assignments are still deferred. No formal independent/specialist or deployment sign-off is inferred.

### 20 October 2026 UTC — B015 local choices approved

User approved offline-only installation and the local design baseline. O-11 resolved only for the delivered shell; B015 awaits acceptance and B016 is unstarted. No GitHub/download authority granted.

### 20 October 2026 UTC — B016 local deliverable accepted

User: “Accept B016”. B016 Done for the verified isolated synthetic browser/session/permission scope. Earlier In review wording is superseded. Real human identity/provider integration, deployed Secure-cookie/TLS configuration, live MFA and formal reviews remain deferred. O-04 remains partly resolved. B017 is not started; no external activity authorised.

### 20 October 2026 UTC — B017 local deliverable accepted

User: “Accept B017”. Verified local synthetic audit/redaction scope accepted; B017 Done. Earlier In review wording is superseded. O-12 remains partly resolved: persistent/production retention, audit-viewer grants, live-data handling and formal reviews remain deferred. B018 not started; no external operation authorised.


### B018 local contract implementation — 21 October 2026 (America/Los_Angeles)

User: “Start B018”. Codex implemented the selected local contract and synthetic tests under G0-L. [Contract](docs/planning/B018-local-ai-contract.md) defines a minimal versioned synthetic draft, fixed errors, caller-selected finite timeout, all-or-nothing validation and mock-labelled usage with unknown cost. These are reviewable implementation choices, not claimed Justice or independent approval. [Evidence](docs/evidence/B018-local-ai-adapter.md): 15 tests passed; existing backend packages are absent in this machine's Python runtime, so broader regression was not rerun. B018 In review. O-07 remains Open for live models/budgets/configuration; full F06 schema and provider integration remain deferred. B019 not started.


### Dependency installation follow-up — 21 October 2026

User explicitly requested Python dependency installation. Network installation was authorised for this local setup. Python 3.15 lacked a wheel for pinned pydantic-core; existing bundled Python 3.12.14 was used in `backend/.venv312`. Original direct pins were preserved, with `psycopg-binary==3.3.6` added for Windows libpq support. Installed versions are saved in `backend/requirements-installed-py312.txt`. All 42 backend tests passed and pip check found no broken requirements. This supersedes the earlier missing-dependency regression limitation for this environment. PostgreSQL integration checks were not rerun. B018 acceptance and B019 selection remain pending; live-provider and deployment boundaries are unchanged.


### B018 approved and accepted — 21 October 2026

User: “Approve and accept B018”. The local mock adapter contract and verified implementation are accepted; B018 Done. Earlier pending-acceptance wording is superseded. Retained evidence: 42 backend tests passed (including 15 adapter tests), pip check clean. No tests rerun for documentation-only acceptance. O-07 live model/budget/configuration decisions remain Open; no independent review or deployment sign-off inferred. B019 remains Not started. Pre-acceptance records: `docs/evidence/B018-before-acceptance.zip`.


### B019 local baseline — 21 October 2026

User “Start B019” authorises the local configuration and usage implementation after accepted B018. Codex implemented reviewable validation rules and ephemeral usage metadata; all live requests remain disabled, even with complete settings. No live model/budget/currency/credential policy selected; O-07 remains Open. All 54 backend tests passed, including 12 B019 cases. B019 In review; B020 Not started. See `docs/evidence/B019-local-ai-controls.md` for contract and limitations. No independent review, provider or deployment approval inferred.


### B019 approved — 21 October 2026

User: “Approve B019”. B019 Done for the verified local configuration/usage baseline. Earlier pending-acceptance wording is superseded. Retained evidence: 54 passing backend tests, including 12 B019 tests; no tests rerun for this documentation-only update. Live AI remains unconditionally disabled. O-07 actual model, budget, currency, quotas and live enablement remain Open. No independent review or deployment acceptance inferred. B020 remains Not started; GitHub activity remains deferred. Prior records: `docs/evidence/B019-before-acceptance.zip`.


### B020 local-only preparation — 21 October 2026

User “Start B020”, followed by “Keep GitHub deferred; prepare locally”. This confirms local tooling scope and retains the remote deferral. Codex prepared an offline runner: syntax/limited secret patterns, dependency consistency, backend/runner tests and frontend/harness types pass; deliberate failure propagates exit 1. These are not verified GitHub merge controls. B020 remains Blocked under unchanged acceptance criteria until separately authorised remote governance and CI verification. B004 remains Blocked; no independent review, workflow adoption, remote access or B021 execution inferred. Evidence: `docs/evidence/B020-local-checks.md`.


### B020 local-only replan approved — 21 October 2026

User: “Keep everything local till github comes in later”, selecting the proposed local-only scope. Revised B020 to verified local checks and failure propagation; it is In review pending local deliverable acceptance. Original remote CI/merge-protection requirements are preserved under [RCI-01](docs/planning/remote-ci-handoff.md), mandatory before remote collaboration/merge or release. B004 remains Blocked and O-02 remains Open; no remote verification is claimed. Continue only separately selected local tasks under G0-L; B021 not started. No blanket gate waiver, independent sign-off, remote activity or deployment authority inferred. Earlier B020 remote-blocked status is superseded for its revised local scope only.


### B020 local deliverable approved — 21 October 2026

User: “Approve B020”. B020 Done for the revised, verified local scope. Earlier pending-acceptance wording is superseded. Existing test/check evidence retained; no tests rerun. RCI-01 remains deferred and mandatory before remote collaboration/merge or release; B004 and O-02 remain unresolved. No GitHub activity, remote verification, independent sign-off or B021 start authorised. Prior records: `docs/evidence/B020-before-acceptance.zip`.


### B021 local dashboard baseline approved — 21 October 2026

User selected B021 and answered “Approve this local baseline”: permission-filtered synthetic reference counts, kind/state/owner filters and unavailable business metrics. [Contract](docs/planning/B021-local-dashboard-contract.md) records the local scope. Codex implemented the service and prepared actual PostgreSQL checks; 68 backend tests pass but Docker is unavailable, so persisted-query verification remains outstanding and B021 is Blocked. No new business metrics, grants, database installation, live data or independent review approved by this decision. B022 remains unstarted. O-11 business KPI definitions remain open beyond this reference-only slice.


## B021 local deliverable approved — 21 October 2026

User: “Approve B021”. B021 is Done for the verified local synthetic-reference dashboard queries and filters. Existing 68 backend tests, 15 actual PostgreSQL checks and full local check runner passed; no tests rerun for this documentation-only acceptance. Earlier blocked/pending-acceptance wording is historical and superseded. B022 remains unstarted. Business metrics and frontend/API exposure remain outside this accepted scope; GitHub/RCI-01 remains deferred. Retain future test containers unless the user asks otherwise and keep approvals in chat. Pre-approval records: docs/evidence/B021-before-acceptance.zip.


### B022 local execution — 21 October 2026

User “Start B022” after B021 acceptance. Continued existing B015 styling, B016 isolated synthetic session transport and B021 reference metrics/filters; no new business metric definition inferred. UI/API connection exists only in the isolated harness; normal app remains disconnected. Verified implementation is In review for local acceptance. Containers are retained by default per user instruction, with explicit future user cleanup trigger; preview remains running. GitHub and B023 remain unstarted. See docs/evidence/B022-local-dashboard-ui.md.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.


### B023 local preparation selected — 21 October 2026

User “Start B023” authorises local staging service/configuration and deployment preparation. Provider-neutral draft delivered in deployments/staging; In review for local preparation. Proposed same-origin frontend/BFF → private API → separate persistent PostgreSQL, with migration/runtime credentials separated; worker/live AI/storage/real identity remain disabled. No provider, company account, region, domain, owner assignment, budget or technical sign-off inferred. O-03/O-04/O-16/O-17 remain unresolved for staging. Normal-runtime composition, target-platform commands, secrets loading and readiness gaps are documented before deployment. GitHub/RCI-01 and B024 external actions remain deferred. Existing preview/database left untouched. See docs/evidence/B023-staging-preparation.md.


## B023 local preparation approved — 21 October 2026

User: “Approve B023”. The local staging preparation pack is accepted; B023 Done for that scope. Existing draft validation and eight rejection checks retained; no tests rerun for documentation-only acceptance. Earlier pending-review wording is superseded for local preparation. Provider, exact configuration, ownership/budget, target runtime integration and independent review remain unresolved before deployment. Manifest stays draft-not-deployable and deployment_authorized=false; no spending, secret population, GitHub, provisioning or B024 authority is inferred. B024 remains unstarted. Preview/database were left untouched. Prior records: docs/evidence/B023-before-acceptance.zip.


### B024 local rehearsal scope selected — 21 October 2026

User “Start B024”, followed by “Keep it local: build and verify a separate staging rehearsal”. Authorises isolated local synthetic deployment rehearsal, dedicated retained PostgreSQL storage/secrets, production-mode frontend and loopback HTTPS. No cloud/GitHub, provider/budget/real-identity or global certificate trust authority inferred. Six actual rehearsal groups and full local runner passed; B024 In review for local acceptance. B022 stays untouched. Hosted requirements from B023/RCI-01 remain deferred, not waived. See docs/evidence/B024-local-rehearsal.md. B025 remains unstarted.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.


### B025 local recovery selected — 21 October 2026

User “Start B025” authorises local backup and isolated restoration against the accepted B024 synthetic rehearsal. Codex completed a read-only consistent snapshot and fresh separate restore, with eight recovery/control groups and the full local runner passing. B025 In review; acceptance pending. Existing user retention instruction applies to the protected manual snapshot, restore target and services; no cleanup or source database restore occurred. Observed local durations do not establish hosted RPO/RTO or backup cadence. Hosted policy, off-machine recovery, real identity and independent review remain deferred. Application rollback is documented separately; only one deployed local build exists, so no prior-release rollback was exercised. See [evidence](docs/evidence/B025-local-recovery.md) and [runbook](deployments/local-rehearsal/recovery.md). B026 unstarted.


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.


## B026 local verification

User “Start with B026” selected verification of the retained local rehearsal. [Evidence](docs/evidence/B026-local-foundation.md) records six passing HTTPS/API/database groups, the passing full local runner and supplemental shared-dashboard browser checks. B026 approved and Done for local scope; B027 unstarted. Initial browser sign-in failure recovered after explicit logout/retry; B026-OBS-01 remains open with cause unproven. No risk acceptance, hosted staging, remote CI, real identity or independent review inferred. Existing services, backups and databases retained; no cleanup.


## B026 local verification approved — 21 October 2026

User: “Approve B026”. B026 is Done for the verified local foundation scope. Six live check groups, the full local runner and supplemental browser evidence are retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. B026-OBS-01 remains open with cause unproven; approval does not resolve it. Hosted staging, trusted-browser HTTPS, real identity, remote CI and independent review remain deferred. Existing previews, backups and database resources were left untouched; no cleanup. B027 remains unstarted. Prior records: docs/evidence/B026-before-acceptance.zip.


## B027 local setup/accessibility/support execution — 21 October 2026

User “Start B027” authorises the local handover checks. When the isolated npm cache-only install failed, the user explicitly chose “Allow exact locked dependency downloads”. This permits the exact frontend lock resolution for that setup, with scripts disabled; no GitHub/cloud/live-AI authority or dependency upgrades inferred. Python remained offline. New dependency installs, source copy, full checks/build and separate retained database/rehearsal succeeded after correcting the setup runner's missing public template. Existing service ports/data remained untouched. Added safe allowlisted logging and alternate loopback ports to the explicit rehearsal; actual redaction/failure logs verified. Keyboard/mobile/accessibility-tree evidence is recorded; spoken screen-reader walkthrough remains outstanding. B027 In review for local scope, B026-OBS-01 open, B028 unstarted. Hosted staging, independent review and G1 approvals remain deferred. See [evidence](docs/evidence/B027-accessibility-setup.md). No cleanup; all attempts and resources retained.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.


## B028 foundation gate assessment — 21 October 2026

User “Start B028” authorises the local demonstration and review preparation. [Review pack](docs/evidence/B028-foundation-review.md) records current passing local controls and the original G1 Hold for missing required human decisions and full-scope assurance. B028 In review. [G1-L v0.1](docs/planning/G1-local-foundation-proposal.md) is proposed only; no criteria amendment, original G1 acceptance, personal reviewer attribution or Phase 2 authority inferred. Generic earlier task approvals do not sign the Justice/CEO fields. Existing local-only, retain-data and no-GitHub instructions persist. B029 unstarted.


## G1-L v0.1 adopted — 21 October 2026

User: “Adopt G1-L v0.1 and accept B028 for local scope only”. B028 Done for the demonstrated local milestone; [adoption/reassessment](docs/evidence/B028-g1-local-adoption.md) preserves original full G1 Hold and every stated deferral. No named Justice/CEO or independent review is inferred. Spoken-reader verification and B026-OBS-01 remain open. B029 unstarted; later local tasks need separate selection and substantive decisions. Documentation-only adoption; no tests rerun or resource changes. All services/data retained; no cleanup. Pre-adoption records: docs/evidence/B028-before-local-adoption.zip.


## B007 planning reconciliation revisited — 21 October 2026

User “Let's work on B007” selected reconciliation of the pending pack with completed B009–B028 local slices/G1-L. Current cards, local decision evidence and external cost/action checkpoints refreshed. B007 remains In review for actual Justice interim-role acceptance and cadence decision; B005 and full G1 not closed. Existing task approvals are preserved, not backdated into initial Ready. No changed criteria, new assignment, schedule, budget, Phase 2 or external action inferred. See [reassessment](docs/evidence/B007-foundation-reconciliation.md). All services/data retained.


## B007 local planning completed — 21 October 2026

User confirmed Justice interim-role acceptance and approved local task-by-task/chat review cadence. Earlier B007 pack approval remains valid; reconciled local DoR/decisions and the current answers complete the approved local planning scope. B007 Done; B005 review and full G1 Hold unchanged. No user identity, direct Justice/CEO/independent sign-off, calendar schedule or external authority inferred. B029 unstarted; all resources retained. See docs/evidence/B007-local-completion.md.


## Main reference dashboard connection — 21 October 2026

User “Improve the functionalities and connect the reference dashboard” explicitly supersedes the earlier disconnected-normal-frontend restriction for this local synthetic reference/session slice. Main port 3000 now embeds/browses permitted fixture metadata through a restricted same-origin bridge to existing B027 HTTPS 3543. Public CA exported for scoped server-side verification only; no system/browser trust change or private-key/database-secret copy. HTTP preview cookie baseline is host-only, HttpOnly/SameSite=Strict and path /api/reference; it is not hosted session authority. Added quick views, filters reset, refresh feedback, restored/idempotent/stale session handling and accurate header state. Tests/build/browser evidence: docs/evidence/main-dashboard-connection.md. No real identity, new role grants, business metrics, AI/model calls, external actions or B029 authority. Numbered task statuses/full-G1 deferrals unchanged; all services/data retained.


### 21 October 2026 (Atlantic/Reykjavik) — B005 refreshed technical choices pending

User “Let's sort out B005” authorises the local architecture review refresh. [Four ADR decisions](docs/evidence/B005-current-architecture-review.md) now identify the actual stack, access/session boundary, isolated local environments and service split, with reasons, alternatives and D005-01–D005-09 deferrals. No outcome attributed to Justice yet. O-03 stays Open; O-04 stays Partly resolved. A future explicit technical confirmation may resolve the local architecture review while hosted/real identity/job/operational choices remain gated. B004 Blocked, B029 unstarted and original full G1 Hold; all resources retained.


### 21 October 2026 (Atlantic/Reykjavik) — B005 technical decision adopted

User answered “Justice approves the four local ADR decisions and listed deferrals” to the explicit question covering ADR-001–004 and D005-01–D005-09 with their checkpoints. Record this as user-confirmed Justice approval, not inferred user identity or direct signature. The four local selections, rationale/options/trade-offs and deliberate deferrals are adopted. B005 Done for this approved local review. O-03 becomes Partly resolved; O-04 remains Partly resolved; broader hosting/identity/job/operations/remote choices stay gated. No new business grants, external authority, independent/CEO review or full G1 acceptance. See [acceptance record](docs/evidence/B005-local-architecture-acceptance.md). B029 unstarted; all resources retained.


### B005 — Explicit user acceptance confirmed

User: “Approve B005”. Acceptance of the completed local architecture review is recorded in the [acceptance record](docs/evidence/B005-local-architecture-acceptance.md). Earlier user-confirmed Justice approval and the four adopted local ADRs remain valid. D005-01–D005-09 retain their checkpoints; O-03/O-04 remain Partly resolved. B005 remains Done, B004 Blocked, full G1 Hold and B029 unstarted. No external activity or cleanup.
