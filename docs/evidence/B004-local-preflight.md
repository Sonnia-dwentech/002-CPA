# B004 Local Preflight and Verification Gaps

**Date:** 20 October 2026 UTC  
**Status:** Blocked — current GitHub verification deferred by standing user instruction  
**Authority:** User “Start B004”; this selects the task but does not explicitly lift the earlier prohibition on all GitHub access.  
**Executor:** Codex; existing local folder only. B003 prerequisite accepted.

## Scope and local evidence

B004 requires read-only verification of repository identity, memberships, MFA, protected branches, independent reviewer eligibility and actual PR #2 outcome. Reviewed [build order](../../build-order.md), [B001 historical inventory](B001-baseline-inventory.md), [handover checklist](../../CPA_Development_Handover_Pack_v1/github/HANDOVER_CHECKLIST.md), [D007](../../CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md), [D010](../../CPA_Development_Handover_Pack_v1/docs/010-developer-working-agreement-and-assistant-instructions.md), working rules and the current local registers.

Local `Test-Path -LiteralPath .git` returned False. This is a folder-marker check, not remote verification. The original checklist remains unchecked and is not evidence of provisioned access or approval. No remote request, clone, pull, merge, repository modification, credential inspection or provider call occurred.

## Evidence required to finish

| Check | Evidence available locally | Missing current evidence / required authority |
| --- | --- | --- |
| Repository | B001 historically observed dwentech-ltd/dwentech-cpa, private, default main | Current identity/visibility/default branch and relevant branch existence; Justice verifies |
| Memberships / least privilege | D010 requires assistant access limited to required repositories; human assistant confirmed in B002 | Actual human accounts, effective repository/team permissions, accepted invitations and excess-access assessment; Justice/admin |
| MFA | D007 requires MFA; checklist has no confirmation | Authorised account/admin evidence for both developers; lack of visibility must be recorded as unknown, not disabled; never collect secrets or recovery codes |
| Protected main/develop | Required by D007/D010 | Current effective protection/rulesets, review/check requirements and bypass/direct-push permissions; Justice assesses policy compliance |
| Independent reviewer | D010 requires an eligible non-author; AI is not a substitute | Named human reviewers, actual permissions, authorship conflict and applicable review rules; Justice |
| PR #2 | Historical pack identifies it as unresolved review work | Actual current state, author, base/head, reviews, checks and final outcome (open/closed/merged); do not infer merged from closed |

Unprovisioned access cannot yet be distinguished from provisioned-but-unverified access. Do not mark any account/control as missing or compliant without evidence. Record observation date, source, scope/visibility limitations, gaps and accountable authority when verification becomes possible. B004's completion check allows documented unresolved access/review requirements; it does not allow claiming that unperformed verification occurred.

## Blocker and next action

- **Blocker:** The standing user instruction prohibits all GitHub access while B004 requires current remote governance verification.
- **Owner/authority:** User controls the local-only instruction; Justice owns technical access/review assessment and any dependency replan.
- **Impact:** B004 cannot meet its present completion check. Under the unchanged numeric build order, B005 must not start.
- **Unblock paths:** Explicitly authorise read-only GitHub checks for B004 (no clone, pull, merge or modifications), or retain the deferral and approve a recorded local-only replan through the required authority. No replan has been made.
- **Status:** Blocked, not In review or Done. Prior accepted tasks remain Done; all gates remain pending.

## Preservation and verification

[B004-before.zip](B004-before.zip) preserves the three registers before this update. The report and registers record the preflight and blocker only. No build definition, product requirement, original source file or prior evidence report was edited.
