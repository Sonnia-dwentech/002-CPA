# CPA Risk Register

**Version:** 0.8 · **Updated:** 20 October 2026 UTC · **Status:** Local record structure and workflow accepted under B003

Authoritative local risk record. All risks below are **Open** potential risks, not observed application defects. Likelihood, impact ratings and dates are unassessed; named assignments are not recorded. Roles identify required authorities. Mitigations are planned and require evidence, not claimed implemented controls. RK IDs are separate from B002 source-conflict R IDs.

[Progress](progress.md) owns actual blockers/status; [decisions](decisions.md) owns pending choices. Task links refer to build definitions; none authorise execution.

| ID | Risk | Responsible role | Decision / tasks | Source | Mitigation / closure evidence required |
| --- | --- | --- | --- | --- | --- |
| RK-01 | Scope expands before MVP acceptance | CEO/product owner and Justice | [O-01](decisions.md#o-01); [B007](build-order.md), [B008](build-order.md), [B056](build-order.md) | [D006](CPA_Development_Handover_Pack_v1/docs/006-development-roadmap-sprint-backlog.md) | Approve included/deferred scope and verify gate compliance. |
| RK-02 | Unsupported claims or false research coverage | Product/research owner and Justice | [O-06](decisions.md#o-06); [B029](build-order.md), [B040](build-order.md), [B082](build-order.md) | [D004](CPA_Development_Handover_Pack_v1/docs/004-ai-agents-and-intelligence-framework.md) | Verify provenance, freshness and missing-evidence labels with reviewed outputs. |
| RK-03 | Bias or unjustified scoring precision | Product owner and Justice | [O-10](decisions.md#o-10); [B029](build-order.md), [B041](build-order.md), [B057](build-order.md) | [D004](CPA_Development_Handover_Pack_v1/docs/004-ai-agents-and-intelligence-framework.md) | Approve scoring and missing-rating rules; verify scenarios and human review. |
| RK-04 | Uncontrolled model or worker costs | Justice and budget owner | [O-07](decisions.md#o-07); [B019](build-order.md), [B029](build-order.md), [B037](build-order.md) | [D007](CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md) | Approve limits and verify enforcement/retry handling before live calls. |
| RK-05 | Source licence or client IP misuse | Product/research owner and Justice | [O-06](decisions.md#o-06); [B006](build-order.md), [B029](build-order.md), [B082](build-order.md) | [D007](CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md) | Record rights and verify permitted ingestion, storage and use. |
| RK-06 | Secrets or sensitive information exposure | Justice | [O-12](decisions.md#o-12); [B006](build-order.md), [B017](build-order.md), [B101](build-order.md) | [D007](CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md) | Verify secrets handling, redaction and privacy boundaries. |
| RK-07 | Cross-client or unauthorised record access | Justice and product owner | [O-04](decisions.md#o-04); [B005](build-order.md), [B013](build-order.md), [B016](build-order.md), [B101](build-order.md) | [D007](CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md) | Approve access rules; verify negative authorisation and isolation cases. |
| RK-08 | Prompt injection from untrusted content | Justice | [O-06](decisions.md#o-06); [B029](build-order.md), [B037](build-order.md), [B073](build-order.md) | [D004](CPA_Development_Handover_Pack_v1/docs/004-ai-agents-and-intelligence-framework.md) | Test content/instruction separation and tool permission boundaries. |
| RK-09 | Premature service/agent complexity | Justice | [O-03](decisions.md#o-03); [B005](build-order.md), [B029](build-order.md) | [D003](CPA_Development_Handover_Pack_v1/docs/003-system-architecture-and-technology-specification.md) | Approve minimal ADR boundaries; verify maintainability in review. |
| RK-10 | Missing independent review or inferred release approval | Justice and CEO | [O-02](decisions.md#o-02); [B004](build-order.md), [B008](build-order.md), [B104](build-order.md) | [D010](CPA_Development_Handover_Pack_v1/docs/010-developer-working-agreement-and-assistant-instructions.md) | Record eligible human reviews and explicit gate acceptance. |
| RK-11 | Data loss or failed recovery | Justice | [O-16](decisions.md#o-16); [B023](build-order.md), [B100](build-order.md), [B102](build-order.md) | [D009](CPA_Development_Handover_Pack_v1/docs/009-deployment-operations-guide.md) | Approve recovery targets and demonstrate restore/rollback. |
| RK-12 | Illustrative UI metrics appear operational | Product owner and Justice | [O-11](decisions.md#o-11); [B007](build-order.md), [B015](build-order.md), [B056](build-order.md) | [D005](CPA_Development_Handover_Pack_v1/docs/005-ui-ux-design-specification.md) | Verify truthful unavailable/draft states and rendered journeys. |
| RK-13 | Document drift or unsupported completion claims | Justice; executor maintains evidence | [O-18](decisions.md#o-18); [B003](build-order.md), [B007](build-order.md) | [D006](CPA_Development_Handover_Pack_v1/docs/006-development-roadmap-sprint-backlog.md) | Verify linked records, counts and preserved history on handoff. |
| RK-14 | Remote activity contrary to user deferral | Justice and user | [O-02](decisions.md#o-02); [B004](build-order.md) | [D010](CPA_Development_Handover_Pack_v1/docs/010-developer-working-agreement-and-assistant-instructions.md) | Keep B004 deferred until explicit changed authority or recorded approved replan. |

## Maintenance and history

Review relevant risks before each selected task and at handoff. Use Open, Mitigating, Accepted or Closed. Record date, assessment, authority/owner, action and evidence for changes. Accepted requires explicit residual-risk acceptance; Closed requires demonstrated closure evidence. Reopen if later evidence invalidates closure. An actual blocker belongs in progress with task, impact, authority and unblock condition. Regular cadence remains O-18/B007.

20 October 2026 UTC: RK-01–RK-14 registered Open from linked source requirements; RK-14 also reflects the user's current local-only instruction. No mitigation verified. See [B003 report](docs/evidence/B003-records-setup.md).

20 October 2026 UTC: User accepted the B003 local record structure and maintenance workflow. This accepts the register process; all RK risks remain Open and mitigations unverified.

20 October 2026 UTC: B004 local preflight recorded the actual authority blocker in [progress](progress.md) and [B004 report](docs/evidence/B004-local-preflight.md). RK-10/RK-14 remain Open; no GitHub controls verified and no remote activity performed.

20 October 2026 UTC: Under the explicit B005 local exception, [four proposed ADRs](docs/adr/README.md) document design options relevant to RK-06/RK-07/RK-09/RK-10/RK-11/RK-14. This is review preparation, not implemented mitigation or risk acceptance. All risks remain Open; remote alignment and eligible repository review remain unverified.

20 October 2026 UTC: [B006 draft policy](docs/policies/allowed-data-and-test-fixtures.md) documents proposed boundaries relevant to RK-02/RK-05/RK-06/RK-07/RK-08/RK-11/RK-12. No controls implemented or verified; all risks remain Open.

20 October 2026 UTC: B007 [work-item pack](docs/planning/phase-1-work-items.md) and [operations worksheet](docs/planning/phase-1-design-operations.md) expose readiness gaps relevant to RK-01/RK-04/RK-09/RK-10/RK-11/RK-12/RK-13/RK-14. Planned actions are not verified mitigations; risk states unchanged.

20 October 2026 UTC: [B008 G0 assessment](docs/evidence/B008-g0-readiness-assessment.md) records Hold for actual prerequisite/sign-off gaps relevant to RK-09/RK-10/RK-13/RK-14. Gate remains closed; no risk closure or residual-risk acceptance inferred.

20 October 2026 UTC: User adopted G0-L v0.1 with explicit deferred assurance limitations. [Reassessment](docs/evidence/B008-g0-local-reassessment.md) passes only local entry, not original full-G0 assurance. RK-09/RK-10/RK-13/RK-14 remain Open; no controls or reviewer eligibility verified. B009 not started.


21 October 2026 (Atlantic/Reykjavik): B028 [foundation assessment](docs/evidence/B028-foundation-review.md) consolidates local mitigation evidence relevant to RK-01/RK-06/RK-07/RK-10/RK-11/RK-12/RK-13/RK-14. Full G1 remains Hold: required human review/sign-offs and original-scope assurance are absent. Local tests and approved task slices do not close these risks or establish residual-risk acceptance. B026-OBS-01 and spoken-reader verification remain open. Proposed G1-L v0.1 is unadopted; no waiver/phase/release authority. Risk states unchanged, all resources retained.


## G1-L v0.1 adopted — 21 October 2026

User: “Adopt G1-L v0.1 and accept B028 for local scope only”. B028 Done for the demonstrated local milestone; [adoption/reassessment](docs/evidence/B028-g1-local-adoption.md) preserves original full G1 Hold and every stated deferral. No named Justice/CEO or independent review is inferred. Spoken-reader verification and B026-OBS-01 remain open. B029 unstarted; later local tasks need separate selection and substantive decisions. Documentation-only adoption; no tests rerun or resource changes. All services/data retained; no cleanup. Pre-adoption records: docs/evidence/B028-before-local-adoption.zip.


21 October 2026 (Atlantic/Reykjavik): B007 reconciliation addresses documentation drift (RK-13) by linking accepted local outcomes instead of stale blanket readiness/test statements. Justice nomination, actual Codex execution, user local acceptance and absent independent/formal approvals are distinguished (RK-10). Cost/action authorities and checkpoints remain explicit (RK-01/RK-04/RK-14). No risk closure or residual-risk acceptance inferred; states unchanged. All resources retained.


21 October 2026 (Atlantic/Reykjavik): B007 local planning completed after user-confirmed interim owner acceptance and approved local review cadence. This resolves those local planning gaps; RK-10/RK-13 and other risk states are not automatically closed. B005, independent/CEO/full-G1 outcomes remain absent; no risk waiver or external authority. All resources retained. See [completion record](docs/evidence/B007-local-completion.md).


21 October 2026 (Atlantic/Reykjavik): B005 refreshed ADR review identifies local application-only tenant enforcement, privileged migration bootstrap/runtime locking write grant, manual same-machine recovery/certificate lifecycle, incomplete global audit integration and deferred real identity/durable jobs/hosted operations. [D005-01–D005-09](docs/evidence/B005-current-architecture-review.md) assign required decision authorities and checkpoints. These are explicit review findings, not newly discovered incidents or accepted/closed risks. No technical risk acceptance inferred; existing risk states and retained resources unchanged.


21 October 2026 (Atlantic/Reykjavik): User confirms Justice approval of the four B005 local architecture decisions and D005-01–D005-09 deliberate deferrals/checkpoints. The review decision is now recorded; it does not close operational/security risks or certify deferred controls. Required authorities/checkpoints persist; risk states unchanged. See [technical acceptance](docs/evidence/B005-local-architecture-acceptance.md).
