# B028 — Foundation review and acceptance record

**Date:** 21 October 2026 (Atlantic/Reykjavik). **Executor:** Codex. **Task:** Done for adopted G1-L v0.1 only; see [adoption](B028-g1-local-adoption.md). Earlier assessment below is preserved; original full G1 remains Hold. **Original G1 outcome:** HOLD — required human decisions and original-scope assurance are not recorded. User “Start B028” authorises assessment/demonstration, not acceptance or a criteria change.

## Demonstration for the reviewers

[Current executed demo](B028-foundation-demo.json), [reusable runner](../../backend/check_foundation_demo.py): exit 0 on 21 October 2026 UTC. No new dependency download, GitHub/cloud action, fixture/schema mutation, service restart or cleanup. Only the demo's own synthetic session was issued and revoked.

- Existing B027 production UI HTML, health and database readiness returned 200 at https://127.0.0.1:3543 with explicit private CA and hostname verification.
- Anonymous dashboard 401; synthetic login; three permitted persisted reference rows; hidden direct record 404; hidden-owner count zero; logout and replay 401. The references are real database rows containing wholly synthetic metadata; no business idea content or metrics are implied.
- Direct Python mock adapter returned a schema-checked synthetic draft with unknown cost. Malformed output was rejected. Fully shaped live configuration was blocked before invoking the adapter. No provider transport/network call occurred and no AI HTTP workflow exists.
- Current complete local check runner exited 0: **74 source/config files, 70 backend tests, 5 runner tests**, dashboard contract and normal/harness/rehearsal TypeScript checks. These are local checks, not remote CI or independent review.

Browser evidence is carried from B022/B026/B027: signed-in shared dashboard, counts/filters, keyboard, mobile, error and sign-out behavior. This demonstration does not claim a new browser-rendered authenticated HTTPS journey or install/bypass browser certificate trust. B027's original six groups provide real isolated database fault/recovery and redacted log evidence; B028 did not repeat that fault against the retained service. B025 restore evidence remains a separate actual drill, not rerun at this gate.

## B009–B027 traceability

| Tasks | Accepted local result | Evidence and preserved limits |
| --- | --- | --- |
| B009 | Structure and references | [Report](B009-local-structure.md); remote alignment deferred |
| B010 | Setup preparation, later fulfilled by B027 executable walkthrough | [B010](B010-local-setup.md), [current guide](../local-setup.md), [B027](B027-accessibility-setup.md); same workstation, not fresh OS certification |
| B011 | Minimal API health/OpenAPI/errors | [Report](B011-local-api.md); normal API not the synthetic composition |
| B012 | PostgreSQL/migrations | [Report](B012-local-database.md); isolated local database checks |
| B013–B014 | Synthetic access/session boundaries | [Access](B013-local-authorisation.md), [sessions](B014-local-authentication.md); real identity/MFA deferred |
| B015–B016 | Honest navigation and synthetic sign-in UI | [Shell](B015-local-navigation.md), [journey](B016-local-sign-in.md); unavailable future modules stay labelled |
| B017 | Audit and operational-capture primitives | [Report](B017-local-audit.md); audit not globally wired into normal startup |
| B018–B019 | Mock adapter, structured outcomes and live-mode block | [Adapter](B018-local-ai-adapter.md), [controls](B019-local-ai-controls.md); no live provider/production billing ledger |
| B020 | Local syntax/type/test/dependency/limited secret checks | [Report](B020-local-checks.md), [RCI-01](../planning/remote-ci-handoff.md); remote enforcement deferred |
| B021–B022 | Permission-filtered stored reference dashboard and shared UI | [Queries](B021-local-dashboard.md), [UI](B022-local-dashboard-ui.md); synthetic reference metadata, no revenue/research metrics |
| B023–B024 | Local staging preparation and selected separate HTTPS rehearsal | [Preparation](B023-staging-preparation.md), [rehearsal](B024-local-rehearsal.md); hosted deployment not performed |
| B025 | Actual consistent snapshot and separate restore | [Report](B025-local-recovery.md); manual local fixture timing, not recovery SLA/PITR/off-machine proof |
| B026 | Actual local security/config integration checks | [Report](B026-local-foundation.md); B026-OBS-01 remains open |
| B027 | Fresh dependency setup/build, keyboard/responsive/semantic evidence, real redacted logs | [Report](B027-accessibility-setup.md); spoken-reader walkthrough outstanding |

All 19 task approvals are local and scoped. Their Done statuses do not transform a deferred original criterion into a verified one.

## Gate assessment against original G1

| Requirement | Result | Outstanding evidence/disposition |
| --- | --- | --- |
| Secure signed-in staging UI/API/database | Partial local evidence | Programmatic TLS/API/database and separate shared-component browser journey pass. Hosted staging, real identity/MFA and trusted-browser authenticated HTTPS journey not established. Current authority remains local only. |
| Tested adapter mock | Local evidence passes | B018 suite and current direct component demo; no live-provider capability claimed. |
| Accurate real-record dashboard | Local synthetic slice passes | Counts/list/filters operate on actual permitted stored fixture rows; business metrics/content workflows are out of scope. |
| Passing agreed checks | Local evidence passes | Full local runner/fresh build; RCI-01 remains a separate prerequisite before remote collaboration/merge/release. |
| Recovery/logs/setup/supportability | Local evidence available | B025/B027 actual drills/logs/setup; operational policy for hosted/live reliance still undecided. |
| Unresolved-defect/control disposition | Open | B026-OBS-01, spoken-reader check, architecture/access/operations and original-G0/full-scope gaps require recorded review outcomes; no risk severity or acceptance inferred. |
| Justice technical acceptance | **Pending** | Actual named technical reviewer, review scope, decision/date and conditions are absent. |
| CEO functional acceptance | **Pending** | Actual named functional reviewer, review scope, decision/date and conditions are absent. |
| Eligible independent review where required | **Pending** | Prior user task approvals and Codex checks do not supply independent review. If Justice authors changes, the eligible reviewer must be a different human. |

G0-L explicitly preserved G1 unchanged. See [G0-L reassessment](B008-g0-local-reassessment.md) and build-order.md Sections 1.1/3. No full-G1 Pass or B028 Done is inferred from “Start B028”.

## Human decision record — not yet signed

| Decision | Named reviewer / role | Outcome | Date / conditions |
| --- | --- | --- | --- |
| Technical review and original G1 acceptance | Justice — actual reviewer confirmation pending | Pending | Not recorded |
| Functional review and original G1 acceptance | CEO — actual reviewer confirmation pending | Pending | Not recorded |
| Independent review, where applicable | Eligible human not identified | Pending | Not recorded |
| Any revised local milestone | User; [G1-L v0.1 proposal](../planning/G1-local-foundation-proposal.md) | Adopted for local scope only | 21 October 2026; full G1 Hold, all deferrals retained |

A reviewer should record who reviewed what, the explicit decision, the remaining conditions and any permitted risk disposition. A document template or Codex-authored status is not their signature. Do not copy a generic user approval into Justice/CEO fields without explicit role/decision attribution.

## Review walkthrough

1. Open http://127.0.0.1:3000 for available shell/navigation and explicit planned modules. Open http://127.0.0.1:3100/dashboard for the synthetic browser journey; allow its initial session check to settle, sign in, inspect the three references, apply owner/type/state filters and sign out. B026-OBS-01 remains open if an initial attempt fails; do not erase its history after a retry.
2. Review B028's current TLS/API/database demo results, B027's production build/log/fault evidence, and B025's exact snapshot/restore comparison. The private HTTPS CA is explicitly trusted by test clients; no browser warning bypass is part of the walkthrough.
3. Review the mock-only adapter and fail-closed live controls, current test output and handover. No button claims a live AI workflow.
4. Record the named technical/functional outcomes and independent-review state, or explicitly select the proposed limited local milestone while retaining the full-G1 Hold. Do not treat unknowns as approvals.

The [G1-L v0.1 proposal](../planning/G1-local-foundation-proposal.md) is concrete and reviewable but unadopted. It would preserve full G1 and permit only separately selected local work under stated limits. No changes to build-order.md, G1 criteria or Phase 2 authority have been made.

## Preservation and next boundary

[Pre-change snapshot](B028-before.zip). Existing previews, setup attempts, secrets, containers, volumes and backups are retained. No cleanup. B029 has not started and still requires separate selection and substantive Phase 2 decisions even after any gate outcome.


## Subsequent local adoption

User “Adopt G1-L v0.1 and accept B028 for local scope only” adopts the concrete proposal. [Reassessment](B028-g1-local-adoption.md) records PASS for G1-L and B028 Done for that local scope. Earlier unadopted/no-criteria-change wording is historical and superseded only for this limited milestone. Original full-G1 criteria and Hold, all missing human reviews and every deferral remain. B029 unstarted. No runtime/source/service/data changes or cleanup.
