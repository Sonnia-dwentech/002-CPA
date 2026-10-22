# CPA Documentation Index

The root [progress ledger](../progress.md) owns current task status and handoff. This index provides local navigation, not a second tracker. Original source requirements remain proposed unless the decision/acceptance records explicitly approve them.

## Planning and governance

| Document | Purpose |
| --- | --- |
| [Blueprint](../blueprint.md) | Product concept, proposed architecture and scope |
| [Feature specification](../feature-spec.md) | F01–F20 behaviour and acceptance criteria |
| [Build order](../build-order.md) | B001–B105 definitions, dependencies and gates |
| [Progress](../progress.md) | Authoritative task status, checks and handoff |
| [Decisions](../decisions.md) | O-01–O-18 authorities, choices and deferrals |
| [Risks](../risks.md) | Potential risks, mitigation requirements and history |
| [Local-only G0](planning/G0-local-only-proposal.md) | Adopted local entry scope and deferred assurance |
| [B014 local session policy](planning/B014-local-session-policy.md) | User-approved local session policy and accepted backend verification; B014 Done |
| [B013 recommended access matrix](planning/B013-recommended-access-matrix.md) | User-approved local internal/client policy; formal reviews and named assignments deferred |
| [Phase 1 work items](planning/phase-1-work-items.md) | Local B009–B028 cards; not proof of execution readiness |
| [Design and operations](planning/phase-1-design-operations.md) | Scope, operational prerequisites and review arrangements |
| [Data/test-fixture policy](policies/allowed-data-and-test-fixtures.md) | Approved limited local policy and deferred specialist reviews |
| [ADR review index](adr/README.md) | Proposed architecture decisions; actual approvals remain in records |
| [Local backend](../backend/README.md) | B011 loopback API contract, launch and test instructions |
| [Local setup preparation](local-setup.md) | Provisional tooling, public configuration template and incomplete-setup evidence |
| [Project layout](project-layout.md) | Existing structure, preserved sources and future layout boundaries |

## Original handover documents

The actual source location is `CPA_Development_Handover_Pack_v1/docs/`. The historical `docs/handover-pack-v1/` location mentioned inside original files does not exist here and must not be assumed. Sources are linked in place rather than copied or moved.

| Source | Title |
| --- | --- |
| [D001](../CPA_Development_Handover_Pack_v1/docs/001-master-concept-and-vision.md) | 001 — Master Concept & Vision |
| [D002](../CPA_Development_Handover_Pack_v1/docs/002-enterprise-product-requirements-specification.md) | 002 — Enterprise Product Requirements Specification |
| [D003](../CPA_Development_Handover_Pack_v1/docs/003-system-architecture-and-technology-specification.md) | 003 — System Architecture & Technology Specification |
| [D004](../CPA_Development_Handover_Pack_v1/docs/004-ai-agents-and-intelligence-framework.md) | 004 — AI Agents & Intelligence Framework |
| [D005](../CPA_Development_Handover_Pack_v1/docs/005-ui-ux-design-specification.md) | 005 — UI UX Design Specification |
| [D006](../CPA_Development_Handover_Pack_v1/docs/006-development-roadmap-sprint-backlog.md) | 006 — Development Roadmap Sprint Backlog |
| [D007](../CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md) | 007 — Security Data and AI Governance |
| [D008](../CPA_Development_Handover_Pack_v1/docs/008-testing-and-acceptance-framework.md) | 008 — Testing and Acceptance Framework |
| [D009](../CPA_Development_Handover_Pack_v1/docs/009-deployment-operations-guide.md) | 009 — Deployment Operations Guide |
| [D010](../CPA_Development_Handover_Pack_v1/docs/010-developer-working-agreement-and-assistant-instructions.md) | 010 — Developer Working Agreement and Assistant Instructions |

Supporting originals: [pack README](../CPA_Development_Handover_Pack_v1/README.md), [working rules](../CPA_Development_Handover_Pack_v1/AGENTS.md), [handover checklist](../CPA_Development_Handover_Pack_v1/github/HANDOVER_CHECKLIST.md), [PR template](../CPA_Development_Handover_Pack_v1/github/PULL_REQUEST_TEMPLATE.md). These are local files; linking them does not contact GitHub or imply any checklist item passed.

Original binary sources: [standalone vision](<../001 — CPA Master Concept & Vision.docx>), [consolidated handover](../CPA_Development_Handover_Pack_v1.docx), [source archive](../CPA_Development_Handover_Pack_v1.zip), [illustrative UI](../UI.png). Preserve them byte-for-byte; the UI image is not evidence of operational metrics.

## Evidence navigation

| Task | Evidence |
| --- | --- |
| B001 | [Baseline inventory](evidence/B001-baseline-inventory.md) |
| B002 | [Reconciliation](evidence/B002-baseline-reconciliation.md) |
| B003 | [Record setup](evidence/B003-records-setup.md) |
| B004 | [Local preflight and missing remote evidence](evidence/B004-local-preflight.md) |
| B005 | [Local architecture review](evidence/B005-local-architecture-review.md) |
| B006 | [Policy review/approval](evidence/B006-policy-review.md) |
| B007 | [Phase 1 refinement](evidence/B007-phase-1-refinement.md) |
| B008 | [Original full-G0 Hold assessment](evidence/B008-g0-readiness-assessment.md); [adopted G0-L reassessment](evidence/B008-g0-local-reassessment.md) |
| B009 | [Local structure/reference work](evidence/B009-local-structure.md) |
| B010 | [Local setup preflight and blockers](evidence/B010-local-setup.md) |
| B011 | [Local API startup/contract evidence](evidence/B011-local-api.md) |
| B012 | [Local database prerequisites and execution plan](evidence/B012-local-database.md) |
| B013 | [Local identity/permission implementation and verification](evidence/B013-local-authorisation.md) |
| B014 | [Local session implementation and verification](evidence/B014-local-authentication.md) |
| B015 | [Responsive local navigation shell and verification](evidence/B015-local-navigation.md) |
| B016 | [Isolated local sign-in integration and verification](evidence/B016-local-sign-in.md) |
| B017 | [Local audit/redaction implementation and verification](evidence/B017-local-audit.md) |

Snapshots and input-hash manifests sit beside their reports in `docs/evidence/`. They record historical inputs; a later authorised ledger change does not invalidate the original snapshot. Preserve original reports and append dated outcomes rather than silently rewriting past approvals.
