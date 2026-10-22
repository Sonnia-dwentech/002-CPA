# CPA Feature Specification

**Organisation:** Dwen Tech Ltd  
**Product:** Chief Product Architect AI Laboratory  
**Version:** 0.3 draft  
**Date:** 20 October 2026  
**Classification:** Confidential — Internal  
**Status:** Proposed for product owner approval and Justice's technical review

This document specifies the intended features of CPA: a secure internal platform for researching problems, assessing product ideas, challenging assumptions and preparing evidence-labelled recommendations for human decisions. The MVP comprises the application foundation and the complete idea-to-dossier workflow. Later phases extend it to portfolio reviews, voice, client Discovery and advanced research and modelling.

**Current local working instruction:** Use this existing `002 CPA` folder and `progress.md`. All GitHub activity is deferred: no remote access, clone, pull, merge or modification. References to GitHub issues, branches, PRs and remote checks below describe the deferred delivery workflow, not a prerequisite for the currently selected local documentation task. B001 was accepted by the user; later tasks and gates need their own evidence.

## 1. Specification basis

Read this document with [blueprint.md](blueprint.md). The blueprint supplies strategic context, architecture proposals, source reconciliation, roadmap and open decisions. This specification describes observable feature behaviour and acceptance criteria; it is not implementation evidence or approval to build every phase.

Primary source documents, under `CPA_Development_Handover_Pack_v1/docs/`, are:

| Reference | File | Use |
| --- | --- | --- |
| D001 | `001-master-concept-and-vision.md` | Purpose and MVP |
| D002 | `002-enterprise-product-requirements-specification.md` | Product requirements and original CPA identifiers |
| D003 | `003-system-architecture-and-technology-specification.md` | Data, API and integration proposals |
| D004 | `004-ai-agents-and-intelligence-framework.md` | AI execution, evidence and output contracts |
| D005 | `005-ui-ux-design-specification.md` | Screens, actions, journeys and states |
| D006 | `006-development-roadmap-sprint-backlog.md` | Phase boundaries and source backlog identifiers |
| D007 | `007-security-data-and-ai-governance.md` | Access, confidentiality, rights and authority |
| D008 | `008-testing-and-acceptance-framework.md` | Source acceptance scenarios AT-01–AT-10 |
| D009 | `009-deployment-operations-guide.md` | Environment, configuration and release controls |
| D010 | `010-developer-working-agreement-and-assistant-instructions.md` | Delivery and human review responsibilities |

The standalone vision Word document, combined handover Word document, `UI.png`, README, repository working rules and handover/PR templates are accounted for in the blueprint's source register. The supplied image is a visual reference; its records, counts, dates, article claims, heatmap colours and service availability are not verified product data.

### 1.1 Requirement notation

- **F01–F20:** Local specification feature IDs, not existing GitHub issues.
- **AC-Fxx-nn:** Local acceptance criteria. None is marked passed.
- **CPA-…:** Original requirement IDs retained from D002.
- **O-01–O-18:** Stable open-decision labels aligned with blueprint Section 20 and progress.md during B002; these labels are not approved decisions.
- **Must:** Required behaviour within this proposed specification, subject to approval.
- **Proposed detail:** Additional interpretation offered for review; dependent work needs confirmation before implementation.

All features remain draft. Acceptance criteria clarify the source intent; they do not settle the open business rules listed in Section 10. No dates, budgets, providers, thresholds or performance values are invented here.

## 2. Actors and authority

| Actor | Intended capabilities and boundaries |
| --- | --- |
| Founder / CEO | Strategy, portfolio oversight, human investment/commercial decisions, functional acceptance and release approval |
| Human CPA / Product Innovation Lead | Create ideas, initiate authorised research, challenge results, prepare dossiers and submit recommendations |
| Justice / Technical Lead | Architecture, implementation supervision, technical review, access/settings as authorised and technical acceptance |
| Human assistant developer | Assigned implementation with required development/staging access; no production secrets or unilateral release authority by default |
| Future analyst | Research contribution under a permission model still to be defined |
| Discovery client | Own permitted intake and approved responses only; no internal intelligence or other-client access |
| AI | Drafting, analysis and recommendations; no approval, investment, contractual or production release authority |

An actor's business role does not automatically confer every application or infrastructure privilege. Exact grants, tenancy boundaries and reviewer assignments require O-04 and O-09. The user confirmed in B002 that Justice’s assistant is a human developer with AI assistance. This resolves the team-definition conflict under O-01 without assigning a specific person or privileges.

## 3. Release scope and dependencies

| Phase | Included features | Required outcome |
| --- | --- | --- |
| 1 Foundation | F01, F02, F06 adapter/mock foundation, F19 foundational controls, F20 operational foundation | Secure signed-in staging application, working API/database and real-record dashboard |
| 2 Idea Studio MVP | F03–F10, F18 basic retrieval, F19–F20 supporting controls | Create → analyse → challenge/revise → version/save → retrieve/export → human review |
| 3 Portfolio intelligence | F11–F12, corresponding F02/F18/F19 extensions | Evidence-based product review with scenarios and recorded human decision |
| 4 Voice and Discovery | F13–F14, corresponding shared-feature extensions | Permissioned saved voice sessions and confidential client enquiry review |
| 5 Advanced research/modelling | F15–F17, extended F10/F18/F19/F20 | Approved scoped/scheduled research, academic analysis and editable commercial models |

F18's full search design and F19's notification channels need issue-level phasing. Shared controls apply before the first feature that depends on them. Phase 5's advanced cost/evaluation work does not defer MVP budget guardrails or evidence checks.

The source backlog IDs remain defined in D006 and the blueprint. Features may span several issues; this document does not prescribe sprint estimates or claim issue creation.

## 4. Feature catalogue

| ID | Feature | Original requirement / main sources |
| --- | --- | --- |
| F01 | Authentication and record access | D002 personas; D007; P1-06 |
| F02 | Application shell and Command Centre | CPA-CORE-001; D005; P1-03, P1-10 |
| F03 | Idea capture and management | CPA-ID-001; P2-01 |
| F04 | Analysis request and run control | CPA-ID-001; D003–D004; P2-02 |
| F05 | Sources, claims and provenance | CPA-ID-001, CPA-KH-001; P2-03 |
| F06 | Structured AI assessment | CPA-AI-001, CPA-ID-001; P1-07, P2-04 |
| F07 | Assumption challenge and revision | CPA-ID-001; D004–D005 |
| F08 | Opportunity scoring and risk flags | D002 scoring; P2-05 |
| F09 | Versioned dossiers and human review | CPA-ID-001, CPA-KH-001; P2-06, P2-07 |
| F10 | Dossier and report export | D002 cross-cutting/export; P2-08; P5-06 |
| F11 | Product portfolio | CPA-PM-001; P3-01 |
| F12 | Product stress testing | CPA-ST-001; P3-02–P3-06 |
| F13 | Voice Studio | CPA-VOICE-001; P4-01–P4-03 |
| F14 | Client Discovery | CPA-CD-001; P4-04–P4-07 |
| F15 | Geography and opportunity scanning | CPA-GEO-001, CPA-MI-001; P5-01–P5-03 |
| F16 | Academic research | CPA-RI-001; P5-04 |
| F17 | Business modelling and investor outputs | CPA-BM-001; P5-05–P5-06 |
| F18 | Knowledge Hub and search | CPA-KH-001; D002, D005 |
| F19 | Usage, settings, audit and notifications | CPA-AI-001; D002 cross-cutting; D004, D007, D009 |
| F20 | Operational readiness and recovery | D003, D007–D010; P1-04, P1-05, P1-08, P1-09 |

## 5. MVP features

### F01 Authentication and record access

**Purpose:** Permit authorised staff to use CPA while protecting internal and client records.  
**Actors:** All roles, subject to approved grants.  
**Dependencies:** O-04 identity, sessions, role matrix and tenancy; O-12 data policy.

**Behaviour**

- Require authentication for internal application data and protected actions.
- Authorise role and specific record access on the server for API requests, background outputs, search, exports and files.
- Apply client isolation before any real client record is introduced.
- Keep API credentials outside browser code, responses and logs. Developer access must follow approved infrastructure roles.
- Show sign-in/session and access-denied states without disclosing restricted record content.

**Acceptance**

- **AC-F01-01:** Given no valid authentication, a protected API request is rejected and the interface offers the approved sign-in path without returning protected content. Maps to AT-01.
- **AC-F01-02:** Given an authenticated actor without access to a record, direct URL/API/file requests and search cannot expose its content or derived private information.
- **AC-F01-03:** Given two separate clients, neither can retrieve the other's enquiry or approved response by changing an identifier. Maps to AT-07 when Discovery is delivered.

**Open:** Identity provider, session lifecycle, role grants, record ownership/sharing and tenancy implementation. Error-code detail belongs in the approved API contract.

### F02 Application shell and Command Centre

**Purpose:** Show current work and available actions from real records.  
**Actors:** Authorised internal users.  
**Dependencies:** F01, persisted records, O-11 design/navigation and metric definitions.

**Behaviour**

- Provide organisation/user context, navigation, search entry and notification access as delivered.
- Show relevant counts and lists for research runs, pending reviews, enquiries, portfolio risk alerts, AI spend and approvals as their modules become available.
- Support date, geography, status and owner filters where applicable, preserving permission boundaries.
- Distinguish an empty dataset, a failed query and an unavailable capability. Label demonstration data.
- Use the supplied navy/blue/light-surface visual direction with accessible responsive layouts. Do not infer active integrations from mockup badges.

**Acceptance**

- **AC-F02-01:** Given stored accessible records and an agreed metric definition, cards and lists match those records and selected filters.
- **AC-F02-02:** Given no records, the dashboard shows an honest empty state; given a failed query, it shows an error rather than fabricated counts.
- **AC-F02-03:** Given a deferred scanner or voice feature, any visible entry accurately communicates its availability and cannot start an unavailable service.

**Open:** Final labels, token/asset specification, KPI definitions, full search phase and deferred-navigation treatment.

### F03 Idea capture and management

**Purpose:** Preserve rough product ideas and problem statements for assessment.  
**Actors:** Human CPA and other authorised staff.  
**Dependencies:** F01; O-09 workflow and validation rules.

**Inputs and records:** Title, problem, affected group, geography, known evidence, hypotheses, owner, status and timestamps. Distinguish unknown evidence from a claim of validation.

**Behaviour**

- Create, edit, retrieve and archive ideas within permissions.
- Allow draft development before analysis; approved validation rules determine which fields are required for saving and for analysing.
- Display the source-defined statuses: Draft, Researching, Review, Validate, Approved, Rejected and On Hold. Do not implement an invented transition matrix.
- Confirm destructive actions. A failed operation must not falsely report success or erase existing saved content.

**Acceptance**

- **AC-F03-01:** Given a permitted idea meeting draft-save validation, saving persists it and an authorised later retrieval shows the saved values. Maps to AT-02.
- **AC-F03-02:** Given invalid or missing input required for the requested action, show actionable field validation and do not claim the action succeeded.
- **AC-F03-03:** Given a saved idea and a failed update/archive request, previously saved content remains retrievable and the failure is visible.

**Open:** Field lengths, required fields by action, archive semantics, edit conflicts, sharing and transition permissions. No hard-delete requirement is inferred from CRUD wording.

### F04 Analysis request and run control

**Purpose:** Execute accountable research without losing the underlying idea.  
**Actors:** Authorised researcher; background worker.  
**Dependencies:** F01, F03, F05, F06, F19; O-05 queue/retry design and O-07 budgets.

**Behaviour**

- Persist the idea and tracked request before exposing a run as accepted. Record requestor, objective, jurisdiction/scope, authorised tools, input sources, budget and timeout.
- Return a run identifier and expose background progress and outcomes. The illustrative analysis contract returns `202` with `run_id`.
- Offer cancellation and bounded retry within permissions and limits. Worker restart recovery and job creation idempotency must be designed explicitly.
- Keep run state separate from idea/review state. Proposed run states are queued, running, succeeded, failed and cancelled; partial-result semantics remain open.
- Surface timeout, refusal, provider, source and worker failures without losing the saved idea or mislabelling the run as successful.

**Acceptance**

- **AC-F04-01:** Given an authorised valid analysis request, the system provides a persisted run ID whose status can be retrieved only by authorised actors. Maps to AT-03.
- **AC-F04-02:** Given a failed provider call, the saved idea remains intact and the run exposes an actionable recovery state. Maps to AT-04.
- **AC-F04-03:** Given a repeated creation request with the same approved idempotency identity, the system follows the agreed duplicate-prevention contract rather than silently creating duplicate chargeable work.
- **AC-F04-04:** Given cancellation or worker restart, status and retained output follow the approved recovery policy; a stopped local task must not imply a confirmed reversal of provider charges.

**Open:** Queue, timeout values, limits, retries/backoff, duplicate identity, cancellation boundaries and partial-result handling.

### F05 Sources, claims and provenance

**Purpose:** Make externally derived analysis inspectable and distinguish it from hypotheses.  
**Actors:** Authorised researchers and reviewers.  
**Dependencies:** F01, permitted input strategy, O-06 sources/rights/evidence policy.

**Behaviour**

- Record URL/DOI, title, publisher, publication/access dates, source type, applicable licence and quotation/summary boundaries.
- Associate material external claims with source references and retain confidence, contradictions, gaps and limitations.
- Label unsupported statements as hypotheses or unverified claims; show an explicit no-source warning where applicable.
- Treat source content as untrusted. It cannot authorise tool actions, change access rules or override application instructions.
- Respect licensing, terms, permissions and collection limits. Do not claim access to material that was not retrieved.

**Acceptance**

- **AC-F05-01:** Given a sourced assessment claim, an authorised reviewer can trace it to its recorded source and provenance metadata.
- **AC-F05-02:** Given an assessment without sources, the UI and retained dossier explicitly show the absence and do not describe its claims as verified. Maps to AT-06.
- **AC-F05-03:** Given an injected instruction in source text, processing cannot grant privileges, expose secrets or bypass review.

**Open:** Approved MVP connectors/input types, evidence grades, source-quality checks, date/metadata gaps, stale-source rules and permitted content retention.

### F06 Structured AI assessment

**Purpose:** Produce consistent, evidence-labelled product analysis through a controlled backend integration.  
**Actors:** Authorised staff; backend OpenAI adapter.  
**Dependencies:** F04–F05, F19; O-07 model and budget configuration.

**Behaviour**

- Route intelligence generation through the company-controlled server-side OpenAI adapter with version-controlled prompts and schema validation.
- Begin with a single controlled orchestration. Specialist research, market, competitor, architecture, feasibility, commercial, risk, challenge, evidence-audit and report functions do not require autonomous agents.
- Show problem/users/geography, demand evidence, competitors and alternatives, proposed solution, AI advantage, pricing hypotheses, market assumptions, feasibility, risks, evidence grade, score breakdown, recommendation and validation experiments.
- Use deterministic services for collection/filtering/calculation; the model must not invent evidence or calculation inputs.
- Treat outputs as drafts. Refusal or invalid schema must produce an honest failure/partial state under the approved policy, never a silently accepted final assessment.

**Acceptance**

- **AC-F06-01:** Given a valid successful fixture, the result meets the versioned structured-output schema and records actor, request/model and usage metadata. Maps to AT-03.
- **AC-F06-02:** Given malformed or refused output, the interface does not present it as a valid completed dossier; the saved idea survives and the error is recorded safely.
- **AC-F06-03:** Given model text purporting to approve investment, no authoritative human approval is created.

**Open:** Model IDs/routing, full schema, prompt versions, evaluation thresholds and treatment of partially valid output. The authoritative human decision is written through F09.

### F07 Assumption challenge and revision

**Purpose:** Help researchers identify weaknesses and improve or reject ideas.  
**Actors:** Human CPA and authorised reviewers.  
**Dependencies:** F05–F06, F09; O-09 revision rules.

**Behaviour**

- Offer Challenge assumptions on an assessment with its evidence context.
- Surface disconfirming evidence, alternative explanations/solutions, adoption barriers, commercial weaknesses, risk and missing validation.
- Allow human review/edit and preserve the relationship between original analysis, challenge and revised dossier.
- Do not replace a human judgement with an AI recommendation or describe a proposed experiment as completed validation.

**Acceptance**

- **AC-F07-01:** Given an assessment, a successful challenge exposes counterarguments and validation questions linked to that assessment.
- **AC-F07-02:** Given a revised saved dossier, an authorised reviewer can distinguish the earlier assessment and challenge from the revised content under the approved version policy.
- **AC-F07-03:** Given a failed challenge request, the existing saved assessment remains available and its approval state is not changed by the failure.

**Open:** Challenge storage/version model, edit provenance and which revisions require renewed review.

### F08 Opportunity scoring and risk flags

**Purpose:** Provide a reproducible comparison aid alongside evidence and uncertainty.  
**Actors:** Authorised researchers and reviewers.  
**Dependencies:** F05–F06; O-10 rating/missing-data policy.

| Criterion | Weight |
| --- | ---: |
| Problem severity/significance | 20% |
| Willingness to pay/economic value | 20% |
| Market size/growth | 15% |
| AI differentiation/solution advantage | 15% |
| Commercial accessibility | 10% |
| Technical/operational feasibility | 10% |
| Strategic fit | 10% |

Ratings are 0–5 with rationale and evidence strength. With weights expressed as percentage points, total out of 100 is `Σ(weight × rating / 5)`. Display research gaps, confidence limits, critical assumptions, red flags and recommended validation alongside it. A red flag can override numeric ranking; the override policy is not yet defined.

**Acceptance**

- **AC-F08-01:** Given all ratings are 5, the default total is 100; given all are 0, it is 0; given all are 3, it is 60. Maps to AT-05.
- **AC-F08-02:** Given a missing rating, do not silently replace it with zero, redistribute weights or assert a complete score; follow the approved incomplete-score policy.
- **AC-F08-03:** Given a high total and a material risk, display both; the score cannot automatically approve investment or claim a probability of success.

**Open:** Anchored rating rubric, rounding, incomplete-score presentation, weight-change/version rules and risk overrides. No pass threshold is approved.

### F09 Versioned dossiers and human review

**Purpose:** Preserve assessments and record accountable review decisions.  
**Actors:** Dossier author, authorised reviewer and CEO for investment decisions.  
**Dependencies:** F01, F03–F08, F19; O-09 lifecycle/versioning.

**Behaviour**

- Save and retrieve versioned dossier content with its idea, run, evidence, assumptions, scores and recommendation.
- Submit a defined dossier version for review. Permit authorised approval, return or rejection and record actor, outcome, time and applicable content/version.
- Distinguish dossier acceptance, investment approval and production release approval. A dossier's Approved label cannot silently authorise spending or deployment.
- Preserve review history and prevent later edits from falsely appearing to have been approved as part of an earlier version.
- Support validation, rejection and hold outcomes under the approved transition policy.

**Acceptance**

- **AC-F09-01:** Given a saved version, later authorised retrieval returns that version and its evidence/assumption context.
- **AC-F09-02:** Given a user or model lacking approval authority, attempted approval cannot create an investment decision. Maps to AT-10.
- **AC-F09-03:** Given an authorised decision, history identifies the human actor, time, outcome and dossier version; subsequent revision does not rewrite that history.

**Open:** Reviewer assignment, delegation, reasons required per decision, self-review business rules, allowed transitions, revision invalidation and version immutability mechanics. Independent code review remains mandatory separately.

### F10 Dossier and report export

**Purpose:** Share authorised assessments while retaining evidence and limitations.  
**Actors:** Authorised internal users.  
**Dependencies:** F01, F09; O-08 export formats/storage; F17 for advanced investor outputs.

**Behaviour**

- Generate exports for an identifiable saved dossier/version.
- Preserve sources, assumptions, evidence limitations, score meaning and human-review status.
- Protect generated files with approved access and retention controls; apply authorisation to retrieval as well as generation.
- Show progress and recoverable errors for background exports. Never substitute an earlier file while presenting it as the requested version.

**Acceptance**

- **AC-F10-01:** Given an exported dossier, its sources, assumptions and limitations remain inspectable and match the requested version. Maps to AT-08.
- **AC-F10-02:** Given a user without record access, neither export generation nor file retrieval returns its protected content.
- **AC-F10-03:** Given generation failure, the saved dossier survives and no successful download is falsely reported.

**Open:** Formats, templates, editable-output requirements per format, file expiry and storage provider. Outbound publication or client sending is a separate human-approved action.

## 6. Later-phase features

### F11 Product portfolio

**Phase:** 3. **Actors:** Authorised internal users; CEO oversight.  
**Dependencies:** F01, F09, F18–F19; approved product schema and stages.

Maintain product objectives, problem, intended customers, owner, stage, research/commercial assessments, risks, milestones, dependencies, decisions, historical reviews and next actions. Support OnCallX, Krommu, Meznja and approved future products without inventing their development status. Link products to related approved opportunity records where defined.

**Acceptance**

- **AC-F11-01:** Given an authorised saved product record, its declared stage, owner and linked reviews can be retrieved accurately.
- **AC-F11-02:** Given multiple reviews, authorised users can inspect historical decisions rather than only the latest recommendation.
- **AC-F11-03:** Given no entered milestone or stage, the portfolio does not manufacture progress from product names or mockup counts.

**Open:** Product stages, relation to ideas, milestone rules, risk alert rules and edit permissions.

### F12 Product stress testing

**Phase:** 3. **Actors:** Human CPA, authorised reviewers and CEO.  
**Dependencies:** F05–F09, F11; O-10 recommendation vocabulary.

Select a product or idea and assess problem severity, user demand, willingness to pay, competition, differentiation, technical feasibility, operational complexity, regulatory exposure, adoption, growth, economics, investment risk and strategic fit. Present optimistic/base/pessimistic scenarios, counterarguments, supporting evidence and a human decision log. The user confirmed all five recommendations during B002: Continue, Improve, Pivot, Pause and Stop. This resolves the vocabulary conflict; scenario definitions and investment/status consequences still need their own approved rules.

**Acceptance**

- **AC-F12-01:** Given a successful review, each scenario identifies its inputs/assumptions and material risks rather than inventing supporting market figures.
- **AC-F12-02:** Given a recommendation, authorised users can inspect evidence, counterarguments and missing validation before recording a decision.
- **AC-F12-03:** Given a Stop/Pivot or other recommendation, product investment status changes only through an approved human workflow.

**Open:** Recommendation definitions, scenario calculations, evaluation rubric and portfolio-stage consequences. The five recommendation labels were confirmed in B002; implementation and technical acceptance remain future work.

### F13 Voice Studio

**Phase:** 4. **Actors:** Authenticated authorised internal users.  
**Dependencies:** F01, F05–F06, F18–F19; O-12/O-13 consent, retention and provider.

Provide incrementally delivered push-to-talk or realtime conversation with spoken responses, streaming transcript and interruption where supported. Link sessions to the relevant project/idea, preserve summaries/actions and use the same authorised knowledge and workflows as text. Apply consent, retention and deletion controls. A client-facing conversational Discovery interface is a later possibility, not included automatically.

**Acceptance**

- **AC-F13-01:** Given the required consent and an authorised session, permitted conversation can be captured and later retrieved as transcript/summary linked to the correct record.
- **AC-F13-02:** Given microphone denial or connection failure, show the actual state; do not claim recording or a saved transcript that does not exist.
- **AC-F13-03:** Given a spoken request for restricted knowledge or an investment approval, voice cannot bypass record permissions or human decision gates.

**Open:** Voice provider/transport, supported interruptions, languages, audio storage, consent interaction and retention/deletion periods.

### F14 Client Discovery

**Phase:** 4. **Actors:** Client submitter, authorised internal staff and approved outbound reviewer.  
**Dependencies:** F01, F05–F06, F09/F10 as applicable, F19; O-12/O-14 integration and privacy.

Accept website enquiries through an approved authenticated integration/webhook/API with validation, anti-spam, consent and a unique reference. Store the problem, client/sector context and status in a restricted queue. Support missing-information questions, feasibility/risk analysis, draft proposals and notifications. Human approval is required before any outbound communication. A bespoke or reusable-product path requires contractual/IP review before client material is repurposed.

**Acceptance**

- **AC-F14-01:** Given valid permitted intake, persist the enquiry with consent/reference and make it available only to authorised parties.
- **AC-F14-02:** Given forged integration credentials or another client's identifier, reject unauthorised access and do not disclose client content. Maps to AT-07.
- **AC-F14-03:** Given an AI proposal/follow-up draft, no client communication occurs until the approved human workflow authorises the outbound action.
- **AC-F14-04:** Given an unavailable intake integration, show an honest unavailable state and do not claim receipt or delivery without persistence/provider confirmation.

**Open:** Intake fields, consent wording, authentication, duplicate submissions, statuses, spam policy, delivery channels, approval roles and IP permissions.

### F15 Geography and opportunity scanning

**Phase:** 5. **Actors:** Authorised Human CPA/researchers.  
**Dependencies:** F04–F06, F08–F09, F19; O-06/O-07/O-15 sources, budgets and geography.

Support one/multiple countries, regions and Global with sector, time window, objective, source filters, language/currency context, source availability and budget. Store country ISO codes and explicit region definitions; include Wales as a UK subnational selection. Collect permitted sources, deduplicate, extract evidence, identify problems/solution hypotheses and route candidates to human review.

Results show problem, geography, score, evidence strength, source count, update date and review status. Coverage logs record actual countries, languages, sectors, feeds and windows, plus gaps and bias. Global is limited multi-region coverage. Add schedules and alerts only after manual scan behaviour and safeguards are accepted. Heatmaps require a defined metric and coverage basis.

**Acceptance**

- **AC-F15-01:** Given a Ghana-scoped run, the result preserves requested scope and actual source coverage without claiming unsupported wider coverage. Maps to AT-09.
- **AC-F15-02:** Given Global scope with unavailable feeds/regions, show coverage gaps and partial/failure status according to policy, rather than exhaustive-world claims.
- **AC-F15-03:** Given a candidate promoted for evaluation, the receiving record retains its originating run/evidence links; promotion does not authorise investment.
- **AC-F15-04:** Given an approved schedule, each execution is tracked and constrained by permissions, quotas and budgets; recurrence does not imply unlimited spending.

**Open:** Region membership, language/currency lists, source availability, schedule ownership/timezone, alert thresholds, duplicate-candidate policy and coverage/heatmap definitions.

### F16 Academic research

**Phase:** 5. **Actors:** Authorised researchers.  
**Dependencies:** F05–F06, F18–F19; O-06 licensing and approved connectors.

Search approved open-access repositories and licensed sources. Preserve DOI/URL, metadata, licence, findings and uncertainty, then relate findings to real-world problems and possible software interventions. Distinguish an interesting application hypothesis from demonstrated commercial feasibility. Restricted articles/datasets and university IP require appropriate rights before access, retention or reuse.

**Acceptance**

- **AC-F16-01:** Given an accessible permitted publication, a saved finding retains source identity, rights context and uncertainty.
- **AC-F16-02:** Given restricted content without rights, the system does not bypass access or claim a full-text analysis it could not perform.
- **AC-F16-03:** Given a proposed application, output distinguishes research findings from product hypotheses and further validation needs.

**Open:** Repositories, licences, full-text retention, metadata gaps, permissions evidence and partnership scope.

### F17 Business modelling and investor outputs

**Phase:** 5. **Actors:** Authorised internal researchers/commercial reviewers; CEO.  
**Dependencies:** F05, F09–F10, F19; O-08/O-10 model and output rules.

For validated opportunities, maintain editable customer segments, value proposition, business model canvas, competitors, pricing assumptions, TAM/SAM/SOM method, acquisition/distribution, revenue drivers, unit economics, operating/development costs, funding, sensitivity/scenarios, risks and milestones. Generate editable business plans, investment memos, pitch-deck outlines and financial-model assumptions. Show evidence, estimates, input units/currencies and calculations distinctly.

**Acceptance**

- **AC-F17-01:** Given a changed assumption, affected calculations follow the approved formula/version and outputs identify the applicable assumptions.
- **AC-F17-02:** Given unknown price, market size or costs, the system marks gaps and does not silently fill them with purported facts or label incomplete projections as validated.
- **AC-F17-03:** Given generated investor material, sources, scenarios, limitations and human approval status remain visible; generation cannot commit funds or publish the document automatically.

**Open:** Model formulas, supported units/currencies/time periods, validation-readiness rules, scenario defaults and editable formats. No market or financial figures are preapproved.

## 7. Shared features

### F18 Knowledge Hub and search

**Phase:** Basic dossier/source retrieval in Phase 2; expands with delivered modules.  
**Actors:** Authorised internal users and any separately permitted client-facing retrieval.  
**Dependencies:** F01, F05, F09 and relevant module records; O-04/O-12 access/retention.

Index authorised source records, research logs, dossier versions, specifications, decisions and later voice summaries/client records under their respective restrictions. Provide search/filtering and source/version drill-down. Global search must not mix inaccessible client records into internal or client-visible results. PostgreSQL search is proposed; vector retrieval is justified only when needed and approved.

**Acceptance**

- **AC-F18-01:** Given an authorised stored dossier/source, permitted retrieval opens the corresponding record/version and provenance.
- **AC-F18-02:** Given inaccessible client material, titles, snippets, result counts and generated answers do not expose its private information.
- **AC-F18-03:** Given an empty index or failed search, show the appropriate state without fabricating matches or implying successful source retrieval.

**Open:** Index fields, ranking, indexing freshness, full-search phase, deletion propagation and any vector approach.

### F19 Usage, settings, audit and notifications

**Phase:** Foundation onward; advanced controls in Phase 5.  
**Actors:** Authorised users for own permitted information; authorised technical/budget administrators for privileged configuration.  
**Dependencies:** F01; O-07/O-12 budgets, access and retention.

Record AI actor, purpose, request ID, model, tokens, latency, cost estimate and error state with redaction. Expose authorised usage analytics, per-run budgets, user quotas, source/retry limits and monthly alerts. Distinguish estimated/unknown cost from actual confirmed billing; unavailable usage is not zero.

Audit important changes, approvals, privileged operations and usage within the agreed event catalogue. Provide settings and notification preferences appropriate to roles. Notifications must respect record access and client confidentiality. Channel, delivery and trigger definitions remain open. Settings must never expose secret values through ordinary UI or API responses.

**Acceptance**

- **AC-F19-01:** Given a completed or failed model request, retained telemetry identifies the actor/request/model and available usage or an explicit unavailable state without leaking secrets.
- **AC-F19-02:** Given a request beyond configured permission/quota/budget limits, reject or stop new work according to the approved enforcement policy and record the outcome.
- **AC-F19-03:** Given a human review decision, its audit event identifies the actor, resource/version, action and UTC time.
- **AC-F19-04:** Given a notification about restricted content, recipients and message content comply with the approved permissions/preferences and do not disclose private records.

**Open:** Exact budgets/quotas, estimate method, concurrent-run enforcement, alert channels/thresholds, audit event schema/retention and administrative role grants.

### F20 Operational readiness and recovery

**Phase:** Foundation onward. **Actors:** Justice and authorised operators.  
**Dependencies:** Architecture ADRs, approved environments; O-03/O-05/O-16/O-17.

Provide API health/OpenAPI, migrations, CI checks, redacted logs, job observability and separate local/staging/production configuration. Use separate databases, secrets, company API projects and quotas. Require HTTPS, approved CORS, tested backups, restore procedures, rollback assessment and support ownership before production.

Feature branches go through independent review/checks to `develop`, staging verification, then a reviewed release to `main` with CEO approval. No automatic rollback assumption may override migration compatibility assessment. Queue/restart recovery must retain consistent visible outcomes.

**Acceptance**

- **AC-F20-01:** Given a staging deployment, evidence demonstrates authenticated UI/API/database operation, passing agreed CI checks, secure configuration and observable failures.
- **AC-F20-02:** Given a backup/restore drill, authorised operators can demonstrate restoration under the agreed retention and recovery targets; having a backup file alone is insufficient.
- **AC-F20-03:** Given critical security/isolation defects or missing technical/business sign-off, the release fails the launch gate.
- **AC-F20-04:** Given a worker/service restart, runs recover according to the approved recovery contract without silently reporting lost work as successful.

**Open:** Numeric performance/RPO/RTO/availability targets, Render sizing, backup retention, domain/support/incident ownership and migration rollback rules.

## 8. Shared interaction, data and API rules

### 8.1 UI and accessibility

All delivered features must support loading, empty, partial, error, access-denied and relevant stale-source states. Distinguish persisted success from an unknown/unconfirmed result. Preserve saved data on failures; proposed additional detail is to retain unsaved form values during recoverable request errors, subject to the approved client data policy.

Target WCAG 2.2 AA with semantic fields, labels, keyboard/focus support, accessible contrast, chart alternatives and screen-reader announcements. Show UTC-backed timestamps with clear timezone context. Confirm destructive actions. The desktop-first layout must remain usable on smaller screens. Exact breakpoints/tokens are open under O-11.

### 8.2 Data contracts

Minimum concepts are users, ideas, research runs, sources, evidence, dossier versions, product reviews, client enquiries, AI usage and audit events. Product/client entities, geography definitions, voice sessions, generated files, consent and approval history require completed schemas. These conceptual records do not constitute approved migrations.

Preserve links between idea, input version, run, evidence, output and human decision. Exact concurrency, immutability, deletion, archive and retention mechanics remain to be designed. Personal/sensitive client data use requires the governance review in D007; this specification does not determine legal compliance.

### 8.3 API contracts

D003 illustrates `/api/v1/ideas`, idea detail/analysis, research-run detail, dossier detail, opportunity scans, geographies, Discovery enquiries and usage. Treat these as proposed contracts. Define OpenAPI schemas, validation, pagination, authentication, record permissions, structured errors and idempotency for job creation before building dependent clients.

Cancellation, review, export, edits/archive, portfolio, voice and search need additional approved contracts. API design must enforce the same rules as UI actions. A disabled button alone cannot enforce authority or budget limits.

### 8.4 Nonfunctional acceptance

| Area | Required evidence | Unresolved values |
| --- | --- | --- |
| Access/security | Direct-record/API/file and cross-client denial tests; secret/prompt injection checks | Provider/session/tenancy details |
| Evidence quality | Citation, groundedness, contradiction, refusal and schema evaluation | Quality rubric and thresholds |
| Reliability | Recoverable failures, worker restart and job consistency tests | Timeouts, retry/recovery limits |
| Performance | Measured dashboard/API/job behaviour in staging | Latency, throughput and availability targets |
| Costs | Run/user limits, usage records and alerts exercised | Model, prices, caps and estimate policies |
| Recovery | Backup restoration and assessed rollback demonstration | RPO/RTO, retention and restore cadence targets |
| Privacy/rights | Data inventory, retention/access design and source/client rights review | Detailed policies and consent text |
| Accessibility | Keyboard, screen-reader and responsive state verification | Final components/design tokens |

## 9. Acceptance and delivery traceability

| Source scenario | Specification coverage | Delivery |
| --- | --- | --- |
| AT-01 Unauthenticated request rejected | AC-F01-01 | Phase 1 onward |
| AT-02 Create/retrieve own idea | AC-F03-01 | Phase 2 |
| AT-03 Tracked analysis and stored output | AC-F04-01, AC-F06-01 | Phase 2 |
| AT-04 Recoverable model failure/no idea loss | AC-F04-02 | Phase 2 |
| AT-05 Reproducible score | AC-F08-01 | Phase 2 |
| AT-06 Unsourced claims flagged | AC-F05-02 | Phase 2 |
| AT-07 Cross-client access denied | AC-F01-03, AC-F14-02 | Before/at Phase 4 client-data introduction |
| AT-08 Sources/assumptions preserved in export | AC-F10-01 | Phase 2 and later exports |
| AT-09 Actual scan coverage retained | AC-F15-01 | Phase 5 |
| AT-10 Human investment approval required | AC-F09-02 | Phase 2 onward |

### 9.1 MVP demonstration

Use approved synthetic data and mocked AI fixtures for deterministic automated checks; separately record any authorised live-provider validation. Do not imply that mocked output verifies live sourcing or production readiness.

1. Sign in as an authorised user; demonstrate denial as an unauthenticated/unauthorised actor.
2. Create and retrieve a saved idea containing a problem, hypotheses and permitted evidence inputs under the approved validation rules.
3. Request analysis; show run identity, progress, structured result and usage metadata.
4. Inspect source links, uncertainty and an explicit unsourced fixture warning.
5. Challenge assumptions, revise and save a retrievable dossier version.
6. Verify default scoring with controlled ratings; demonstrate incomplete-score behaviour once approved.
7. Submit the selected version; record the authorised human review and reject an unauthorised approval attempt.
8. Export the selected version with sources and assumptions intact.
9. Exercise provider failure and prove the saved idea/dossier survives with an honest recovery state.

### 9.2 Completion evidence

Each approved issue needs scope, dependencies, acceptance criteria, security implications, owner and test plan before work starts. Completion requires an issue-linked PR, independent human review, relevant tests/lint, updated docs/migrations, secrets scanning, staging demonstration and recorded acceptance/known defects. Justice signs technical acceptance; CEO signs phase business acceptance and production release approval. AI tools do not approve their own work.

## 10. Decisions required before dependent implementation

Labels map to blueprint Section 20; current authority and states are in [decisions.md](decisions.md). Reference alignment does not resolve the underlying decisions. See [B002 reconciliation](docs/evidence/B002-baseline-reconciliation.md) for correction status and pending human choices.

| Blueprint decisions | Specification impact |
| --- | --- |
| O-01 scope/team clarification; O-02 repository/review verification | Baseline authority and all implementation work |
| O-03 architecture | F01–F20 component and integration choices |
| O-04 identity/roles/tenancy | F01 and every record, search, export and client boundary |
| O-05 jobs/recovery/idempotency | F04 and later long-running features |
| O-06 sources/licences/evidence grades | F05–F07, F12, F15–F18 |
| O-07 model/budgets/limits | F04, F06, F13, F15–F17, F19 |
| O-08 exports/storage | F10, F17 and private generated files |
| O-09 lifecycle/version/review | F03, F07, F09, F11–F12 |
| O-10 scoring/recommendation vocabulary | F08, F12, F17 |
| O-11 UI/navigation/assets | F02 and all delivered screens |
| O-12 privacy/retention/consent | All personal/client/source data and particularly F13–F14/F18–F19 |
| O-13 voice | F13 |
| O-14 website/communications | F14 |
| O-15 geography/coverage/heatmaps | F15 |
| O-16 performance/recovery/sizing; O-17 support/release ownership | F20 and production launch |
| O-18 estimates/success measures | Sprint planning and outcome measurement |

Detailed validation limits, state transitions, notification behaviour and incomplete-data policies should be decided in the corresponding approved issues/ADRs rather than inferred from this document. External commercialisation, a client-facing voice agent, autonomous investment decisions and unrestricted global scraping remain outside the approved-first-release proposition.

## 11. Review record

| Review | Status |
| --- | --- |
| Product scope and feature acceptance by CEO/product owner | Pending |
| Technical/architecture and security review by Justice | Pending |
| Blocking business rules resolved for selected implementation scope | Pending |
| Test execution and staging evidence | Not supplied; no acceptance criterion claimed passed |
| Production release approval | Not established |

After review, record decisions against the existing open-decision labels, update this specification and the blueprint together where their requirements change, and create/refine only the approved current-phase issues.
