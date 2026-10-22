# Phase 1 Design, Operations and Review Decisions — B007

**Version:** 0.5 · **Reconciled:** 21 October 2026 (Atlantic/Reykjavik)  
**Status:** B007 Done for approved local planning. User confirmed Justice interim-role acceptance and approved the local task/chat cadence; full-scope reviews remain open.

The earlier 20 October worksheet is preserved in [snapshot](../evidence/B007-before-foundation-reconciliation.zip). The old blanket “unset/not started” statements no longer describe current local evidence. [Current reassessment](../evidence/B007-foundation-reconciliation.md) and [20 reconciled cards](phase-1-work-items.md) govern this review. No earlier Ready or human approval is backdated.

## Local decisions already recorded

| Area | Current adopted local boundary | Evidence / remaining limit |
| --- | --- | --- |
| Phase 1 scope | Foundation only; all B009–B028 local slices accepted, G1-L v0.1 adopted | [G1-L adoption](../evidence/B028-g1-local-adoption.md). Original full G1 held; Phase 2 unstarted. |
| UI/navigation/tokens | D005 labels, derived navy/blue/neutral baseline, unavailable future modules; no fake account/metrics | [B015](../evidence/B015-local-navigation.md). Full product design remains open. |
| Dashboard | Count/list from identical permitted persisted synthetic reference set; exact kind/state/owner AND filters; zero/error/unavailable distinct | [B021 contract](B021-local-dashboard-contract.md), [B022 UI](../evidence/B022-local-dashboard-ui.md). No business KPIs, research/financial metrics or operational search. |
| Sign-in/session/access | Synthetic local identities, stored opaque sessions, expiry/revocation and server-side record checks | [B013 matrix](B013-recommended-access-matrix.md), [B014 policy](B014-local-session-policy.md), [B026](../evidence/B026-local-foundation.md). Real identity/MFA deferred; B026-OBS-01 open. |
| Runtime/setup | Python 3.12.14, Node 24.22.0/npm 11.19.1 observed in fresh same-workstation setup, pinned dependencies, local PostgreSQL, isolated source/install/build | [B027](../evidence/B027-accessibility-setup.md), [current setup](../local-setup.md). No fresh-OS or hosted qualification. |
| Local data | Wholly synthetic; no client data; retained local resources until explicit cleanup request | [B006 policy](../policies/allowed-data-and-test-fixtures.md), later user retention instruction. No hosted data-retention policy selected. |
| AI | Mock-only structured draft/error contract, live requests blocked, unknown cost remains unknown | [B018](B018-local-ai-contract.md), [B019](../evidence/B019-local-ai-controls.md). No provider/model/budget/source strategy chosen. |
| Checks | Passing local runner, dependency/source/limited-secret scan, backend/runner tests, dashboard contract and three type checks | [B028 review](../evidence/B028-foundation-review.md). RCI-01 and independent review deferred. |
| Rehearsal/config/logs | Separate loopback HTTPS, production frontend, persistent database/runtime credential; explicit test-CA trust; redacted operational events | [B024](../evidence/B024-local-rehearsal.md), [B027 logs](../evidence/B027-support-log-checks.json). No browser trust bypass or hosted deployment. |
| Recovery/accessibility | Actual manual snapshot/separate restore; keyboard/responsive/accessibility-tree evidence | [B025](../evidence/B025-local-recovery.md), [B027](../evidence/B027-accessibility-setup.md). No RPO/RTO/SLA; spoken screen-reader check outstanding. |

## Costs, external actions and binding checkpoints

| Unresolved action/value | Required authority and trigger | Current permitted boundary |
| --- | --- | --- |
| GitHub access, protections and remote CI | Explicit user change of authority, then Justice/reviewer workflow; before remote collaboration/merge/release | B004 blocked and [RCI-01](remote-ci-handoff.md) deferred; no connection. |
| Architecture/identity/tenancy decisions beyond local baselines | Justice technical and product authority for business grants; before affected implementation/shared or real-client use | B005 In review; no adoption of all ADRs inferred. |
| Hosting provider/account/region/domain/sizing/fees | Justice plus CEO/authorised budget owner; reviewed actual plan and ceiling before provisioning/spending | Local rehearsal only; costs/ceiling remain unknown, not zero/unlimited. |
| Real credentials, redirects, public origins and hosted secret loading | Approved technical/operational owners and exact target configuration before real identity or deployment | Protected local fixtures only. No credential change/population authorised here. |
| Live AI/model/worker/storage/source services | Task-specific technical/product decisions and spending/data authority before enabling/calling | Live AI blocked. Queue/source/model/scoring/export decisions belong to selected B029 work. |
| Package installation/network | Exact action authority before download/install | B027 exact npm lock download exception is historical and specific; not a general network permission. |
| Retention/cadence/RPO/RTO/off-machine recovery | Justice plus relevant policy/CEO authority before hosted/live reliance | Local resources retained until explicit user request; observed fixture timings are not targets. |
| Capacity/performance workload/targets | Justice and CEO before sizing/reliance | No invented numeric target or price. |
| Support, incident, escalation and rollback owners | Justice/CEO assignment acceptance before shared/hosted operation or release | Required roles identified; no named operational acceptance inferred. |
| Formal gate/release acceptance | Justice technical, CEO functional and eligible independent review where required | G0-L/G1-L local only; full G1 Hold, no release/deployment authority. |

These are explicit restrictions/checkpoints, not service orders or blanket risk acceptance. Role names do not imply personal assignment acceptance. Nothing is purchased, scheduled, sent, deployed or connected by this worksheet.

## Ownership decision recorded

| Responsibility | Recorded fact | Missing decision |
| --- | --- | --- |
| Interim accountable Phase 1 implementation owner/product-scope approver | User nominated Justice: “Keep Justice for the meantime” | User answered ‘Yes’ confirming Justice accepted this interim role on 21 October 2026. No user identity, direct technical signature or availability commitment inferred. |
| Actual local executor | Codex performed the selected local changes; user approved each bounded task | No human-assistant appointment or eligible independent-review claim is made. Future executor allocation is task-specific. |
| Technical/independent review | Justice retains technical authority; eligible independent human outcome remains absent | Named reviewer/eligibility and actual ADR/review outcomes before affected full-scope work. Another human must independently review Justice-authored changes. |
| CEO/full-gate/release | Required authority preserved | No CEO identity/signature inferred from ordinary user task approvals. |

## Review cadence — current practice and concrete choice

Observed local practice is explicit selection of one task, implementation and relevant checks, evidence/status update, then user approval in this chat. Approval requests stay in chat; blockers are surfaced when encountered. This is already how work has proceeded, not proof of a signed calendar agreement.

**Approved local operating cadence — 21 October 2026:** Continue that task-by-task review workflow, with an update when a blocker/decision requires attention and a milestone review at each local gate. No daily/weekly calendar commitment, scheduled reminder, SLA, meeting or outbound message is created. The source weekly-planning/daily-blocker cadence remains a future team proposal, to be agreed when named participants and an operating timetable exist. PR review stays deferred until GitHub authority is separately granted.

**Decision:** User selected “Approve this task-by-task local cadence”. Calendar/team weekly/daily commitments remain a future proposal. Formal human reviews and approvals retain their required authority.

## B007 completion boundary

The original check remains: issues satisfy Definition of Ready; service costs/actions requiring authority are identified; no invented dates/budgets. The cards' nine D006 fields and execution links are verified, and later local scope decisions are reconciled. This does not certify unrecorded original/full-scope readiness or human review. The user confirmed Justice interim-role acceptance and approved the local cadence, resolving the remaining local planning decisions. B007 is Done for the approved local planning scope, relying on the earlier pack approval and the current decisions; [completion record](../evidence/B007-local-completion.md). B005/full-G1 decisions retain their checkpoints. B029 has not started.

Estimates/dates are unset. D006's Ready list does not require inventing them; any future schedule commitment needs real agreement. [Source D006](../../CPA_Development_Handover_Pack_v1/docs/006-development-roadmap-sprint-backlog.md), [source D010](../../CPA_Development_Handover_Pack_v1/docs/010-developer-working-agreement-and-assistant-instructions.md). All resources retained; no cleanup.
