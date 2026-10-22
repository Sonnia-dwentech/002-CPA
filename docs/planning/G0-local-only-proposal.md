# Proposed Revision — G0 Local-Only Readiness

**Version:** 0.1 draft  
**Date:** 20 October 2026 UTC  
**Status:** Version 0.1 scope adopted by user; G0-L passed on reassessment — see [adoption record](../evidence/B008-g0-local-reassessment.md)  
**Requested by:** User: “I want to continue locally, Draft a revised local-only G0”  
**Current state:** B008 Done for G0-L only; B004 Blocked; B005/B007 In review; B009 Not started. Original full-G0 Hold conditions remain deferred. The proposal wording below preserves the approved scope; the linked adoption record governs current status.

## 1. Purpose and proposed gate wording

Replace the all-or-nothing entry to foundation work with a limited local implementation gate, while retaining a separate checkpoint before remote integration, shared staging or release. This is a proposed change to the acceptance scope, not a claim that the original G0 checks have passed.

**Proposed B008 completion check:**

> The user approves the local-only scope, evidence and explicit deferrals. The selected first local work item has an accountable owner, bounded scope, sufficiently specified technical approach, checks and preservation plan. No unresolved decision needed for that work item is assumed. GitHub, external services, real client data and deployment remain prohibited. Local review and unreviewed-code handling are documented. Remote governance, formal technical acceptance and deployment readiness remain separately gated.

Call this limited decision **G0-L (local work only)** in evidence. It is a scope label for B008, not a new numbered build task. If adopted and accepted, B008 may be recorded Done **for G0-L only**, with the original full-foundation readiness conditions preserved under the deferred checkpoint below. Do not describe original G0 as fully satisfied.

## 2. What an accepted G0-L would permit

Only separately selected local tasks or local portions of tasks in the existing folder:

- Meaningful project structure and documentation, preserving original handover files and planning evidence.
- Local application development and tests using an explicitly approved task-level approach and synthetic data.
- Mocked AI/source interfaces and honest unavailable states; no fallback to live services.
- Local technical documentation, inspection, diffs and review evidence.

Gate acceptance does not itself start B009 or authorise a batch. Each task still needs explicit selection, a bounded scope and checks. No clone, new remote checkout or migration of the project is needed. No Git initialisation is required by this proposal; any local version-control setup would be separately selected work.

**Still excluded:** all GitHub connections (including read-only checks), clone/pull/push/merge/PR activity, cloud provisioning, live APIs/models/research ingestion, email/voice/outbound messaging, real credentials, production/live-client datasets and staging/production deployment. A local server, if later authorised, must not be exposed publicly. Package downloads and other network-dependent setup are not silently permitted by “local-only”; surface their need and obtain the relevant authority first, or use available local dependencies.

## 3. Acceptance evidence for G0-L

| Requirement | Current evidence | Action needed for local acceptance |
| --- | --- | --- |
| Existing folder and preserved baseline | B001–B003 accepted | Carry forward their accepted local scope; preserve original sources |
| Allowed data | B006 local policy approved | Keep synthetic-only rules and prohibition on sensitive/live data; apply relevant specialist checks before affected implementation |
| Local scope and exclusions | This proposal | User explicitly approves this revised scope and deferral arrangement |
| Accountable work owner | Justice nominated interim implementation owner and product/scope approver | Retain nomination; record actual executor on the selected task. Do not invent Justice's acceptance or availability |
| First work item | B009 card exists in B007 pack | Narrow to the local layout/reference slice described below, record its checks and needed decisions |
| Technical decisions | Four B005 ADRs proposed | Resolve decisions needed by the selected slice, or exclude the affected part. Do not require unrelated future decisions to be final |
| Local review workflow | Proposed below | User accepts the distinction between reviewable local drafts and formal technical acceptance |
| Preservation and stopping conditions | Existing snapshots/ledgers | Record pre-edit evidence, actual checks and rollback/recovery notes relevant to each change |

No live runtime, CI or infrastructure evidence is needed merely to open this limited gate. Future implementation acceptance requires actual checks; the gate is not a substitute for them.

## 4. First proposed slice: B009 local structure and references

**Value:** Organise the accepted local project for subsequent work without needing repository access.

**Scope:** Prepare meaningful local documentation/source-layout references, using approved source paths; preserve supplied assets and reports; record any proposed application folder structure before adding functional code. Avoid empty scaffolding.

**Non-goals:** No remote imports, code migration, package installation, provider selection, credentials, application implementation or GitHub verification. No claim that local layout matches unseen remote contents.

**Acceptance:** Meaningful files and working local source links exist; original material remains unchanged; changed paths and any deferred remote-alignment requirement are recorded. Confirm this local interpretation of B009 explicitly at selection. If application files require a stack/layout decision not yet approved, leave that part out rather than selecting a stack implicitly.

**Checks:** Verify file/link structure, preservation hashes and that no credentials or restricted content were introduced. Record outcomes and the exact reviewed file set.

**Owner/executor:** Justice remains user-nominated accountable owner; executor is recorded when work is selected. Codex can prepare authorised changes but cannot claim Justice's review.

This slice can proceed after G0-L acceptance and explicit B009 selection without deciding every identity, tenancy, hosting or later-phase question.

## 5. B005/B007 dependencies become task-specific

The revised gate would permit local preparation to proceed while B005/B007 remain In review. It would not mark them Done or declare every Phase 1 item Ready.

| Upcoming work | Decision or evidence required before that work |
| --- | --- |
| B009 local layout/reference slice | Approved local layout scope and preservation plan; no assertion of remote compatibility |
| B010 setup | Runtime/tooling choices, test destination, local dependencies and safe setup instructions |
| B011–B012 API/database | Selected stack and contract/schema/migration approach; sufficient local technical authority for implementation |
| B013–B016 identity/access/UI | Identity/session/roles/tenancy and required business grants; local design scope/tokens; relevant B006 technical review |
| B017 logging | Approved events/redaction/access and required retention treatment |
| B018 mocked adapter | Approved mock input/output/error contracts; synthetic fixtures; no live fallback |
| B019 configuration/usage | Approved fail-closed behaviour; unset live model/budget/credentials must prevent live calls |
| B021–B022 dashboard | Approved meaningful metrics, available record types and permission/filter contracts; honest empty/error states |
| B023 configuration planning | Approved logical topology and explicit unresolved costs/values; placeholders only; no deployment |

Detailed implementation choices may be proposed by the executor, but must receive the required authority before being treated as approved. Justice's formal technical-review role remains; if the user wants a different temporary technical authority, that requires an explicit separate designation. User approval of this gate alone does not select an identity provider, stack alternative, role grant or spending limit.

## 6. Local review without GitHub

For each selected local change:

1. Record task ID, scope, executor and pre-edit evidence in the local ledger/report.
2. Present changed files or local diffs and the exact checks/results. Keep failed checks and limitations visible.
3. Record the actual human reviewer, review date, reviewed snapshot/version and disposition when review occurs. The user may accept local deliverables without that being attributed to Justice or an independent code reviewer.
4. Until required technical/independent review is recorded, label functional code as an unreviewed local draft. The user may authorise further local iteration that does not depend on unresolved safety or business choices; do not claim independent assurance or mark a task Done when its own required checks/review remain missing.
5. If Justice authors code, another eligible human is needed for independent review before shared integration/deployment acceptance. AI is not that reviewer.

An available independent code reviewer is **not proposed as a prerequisite to opening G0-L for local draft work**. The absence remains an explicit limitation and a blocker to the later assurance checkpoint. No review messages or meetings are scheduled by this document.

## 7. Deferred checkpoint before remote integration or deployment

Retain all original governance requirements. Before any GitHub connection, remote integration, shared staging/deployment or release, require the relevant explicit user authorisation and reassess:

- B004's repository/access/MFA/protection/reviewer/PR outcome evidence; unknowns are not treated as compliant.
- Justice's substantive ADR review and technical-readiness confirmation.
- Sufficiently approved work-item scope, assignment acceptance, business permissions and independent human review evidence for the actual change set.
- CEO scope/phase approval and any required budget, external-service or release approval.
- Applicable B006 specialist/data controls, environment separation, verification and recovery requirements.

This checkpoint is **not passed** and cannot be bypassed by G0-L acceptance. B004 stays Blocked under the current no-GitHub instruction. Existing G1–G6 definitions and their requirements remain unchanged; a local demo cannot satisfy a staging or production criterion.

## 8. Later sequence boundaries

G0-L would remove B004/B005/B007 completion as a blanket prerequisite only for explicitly selected, sufficiently specified local slices. It would not silently skip the later numeric order.

B020 needs actual remote CI/merge-control evidence; local configuration/testing alone cannot complete it. B024 requires authorised staging provisioning/deployment. B025–B028 contain recovery/staging/acceptance requirements that local drafts cannot automatically satisfy. If the project reaches one of these boundaries while remote work remains deferred, record the blocker and request a specific local-slice/reordering decision before proceeding beyond it. B023 draft preparation does not authorise B024. No blanket execution of B009–B028 is granted.

## 9. Adoption and acceptance record

| Record | State |
| --- | --- |
| User adoption of revised G0-L scope | Explicit user approval on 20 October 2026 UTC |
| First local slice and approach accepted | B009 local structure/reference scope approved; execution explicitly not started |
| Accepted limitations / deferred original controls | User explicitly retained all stated restrictions and deferred reviews |
| Approver/date and evidence version | User, 20 October 2026 UTC; G0-L version 0.1; [reassessment](../evidence/B008-g0-local-reassessment.md) |
| Gate outcome | G0-L PASS; B008 Done for local scope only; original full-G0 conditions deferred |

Suggested adoption wording, if the user agrees:

> I approve G0-L version 0.1 for local-only work. Keep all GitHub, live-service, real-client-data and deployment activity deferred. Permit separately selected local tasks with task-specific technical decisions and checks. Retain missing formal technical and independent-review evidence as explicit limitations before integration/deployment, without claiming those approvals occurred. Reassess B008 against this revised scope and record the outcome before starting B009.

That wording authorises adoption and reassessment, not fabricated results or automatic B009 execution. If reassessment still finds a blocker to the selected local slice, record it rather than passing the gate automatically.

## 10. Proposed document changes upon adoption

Update build-order.md with the bounded G0-L exception and local B008 completion wording while preserving the original full-gate criteria as the deferred checkpoint. Update progress.md and the B008 report only after evidence reassessment. Cross-reference B005/B007 deferred decisions without changing their statuses or claiming technical approval. Add affected decision/risk history. Keep the original B008 Hold assessment and prior snapshots as historical evidence.

**Adoption update:** These bounded changes were applied after explicit user approval. Original proposal scope/version retained; see the reassessment for evidence and current status.

References: [current build order](../../build-order.md), [B008 Hold assessment](../evidence/B008-g0-readiness-assessment.md), [B005 ADRs](../adr/README.md), [B006 policy](../policies/allowed-data-and-test-fixtures.md), [B007 work items](phase-1-work-items.md), [decision register](../../decisions.md), [progress](../../progress.md).
