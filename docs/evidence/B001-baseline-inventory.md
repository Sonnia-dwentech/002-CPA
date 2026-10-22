# B001 Baseline Inventory

**Date:** 20 October 2026 UTC  
**Task:** B001 only  
**Execution authority:** User instruction to start B001  
**Outcome:** Local baseline inventory accepted by the user on 20 October 2026; B001 Done  
**Formal tracker status:** Done — explicit user acceptance of the local inventory recorded below

## Scope and completion checks

| B001 check | Result |
| --- | --- |
| Inventory current planning files and versions | 22 pre-existing files enumerated below; four current planning Markdown documents inspected |
| Verify target repository identity | GitHub metadata confirms `dwentech-ltd/dwentech-cpa`, private, default branch `main` |
| Distinguish local workspace from repository | `git rev-parse --show-toplevel` reports that this directory is not a Git repository |
| Record Gantt dates, team conflict and missing O-label mapping | Confirmed and recorded in the discrepancy register below |
| Record source paths and baseline status | Full inventory and document register below |
| Local inventory acceptance | Explicitly accepted by the user on 20 October 2026; no code-review, architecture or release approval implied |

B002 decisions/reconciliation and B004 access/protection/PR checks were not executed. No repository was cloned, no application was implemented and no external state was changed.

## Accepted local workspace and historical repository observations

- Accepted working project: `C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA`. Continue in this existing folder and preserve its work.
- Current instruction: all GitHub activity is deferred. Do not access, clone, pull, merge or modify the remote repository. The remote observations below are historical evidence only; no fresh remote verification was performed for acceptance.
- Target confirmed by read-only GitHub query: [dwentech-ltd/dwentech-cpa](https://github.com/dwentech-ltd/dwentech-cpa).
- Visibility: private. Default branch: `main`.
- GitHub description: Dwen Tech's AI Research, Product Innovation, Business Modelling and Investment Intelligence Laboratory.
- Current folder has no Git checkout context. Its documentation must not be treated as a checked-out remote branch.
- A bounded name search of immediate directories under Documents and Desktop/Projects found `002 CPA` and `002 CPA - Copy11` under Documents. The copy was not inspected or adopted as the target checkout. This was not an exhaustive disk search. The user has since selected the existing working folder; locating or cloning another checkout is not required to close B001.
- Remote contents, commit head, membership, MFA, branch protections, `develop`, reviewer eligibility and PR #2 outcome were not verified. The latter governance checks belong to B004 and remain deferred under the local-only instruction.

## Current document register

| Path relative to workspace | Declared version/date | Baseline state |
| --- | --- | --- |
| `blueprint.md` | 1.0; 20 October 2026 | Proposed; CEO approval and Justice review pending; 946 lines at inventory |
| `feature-spec.md` | 0.1 draft; 20 October 2026 | Proposed; 20 features and 65 acceptance criteria; 590 lines |
| `build-order.md` | 0.1 draft; 20 October 2026 | Proposed; 105 tasks, B001–B105; 284 lines |
| `progress.md` | 0.1 draft before B001 update; 20 October 2026 | Initially all tasks Not started; 343 lines at inventory; updated separately in this task |
| `001 — CPA Master Concept & Vision.docx` | 1.0; 17 October 2026 | Proposed standalone vision; contains AI-assistant wording |
| `CPA_Development_Handover_Pack_v1.docx` | 1.0; 17 October 2026 | Proposed consolidated Documents 001–010; explicitly human assistant |
| `CPA_Development_Handover_Pack_v1/docs/001-*` through `010-*` | Pack v1.0; 17 October 2026 | Each declares proposed baseline with approval/review pending |
| `CPA_Development_Handover_Pack_v1/README.md` | Pack v1.0; 17 October 2026 | Source reading order and authority; historical repository claims require verification |
| `CPA_Development_Handover_Pack_v1/AGENTS.md` | No standalone version declared | Working rules, human team and approved-issue boundaries |
| `CPA_Development_Handover_Pack_v1/github/HANDOVER_CHECKLIST.md` | No standalone version declared | Sign-off template; no acceptance inferred |
| `CPA_Development_Handover_Pack_v1/github/PULL_REQUEST_TEMPLATE.md` | No standalone version declared | PR evidence structure |
| `CPA_Development_Handover_Pack_v1.zip` | Pack v1 filename | 14 file entries; all exactly match the extracted files at review |
| `UI.png` | No embedded product version established | Visual reference; not evidence of live metrics or working integrations |

## Source differences and unresolved interpretation

| Ref | Evidence | Required future handling |
| --- | --- | --- |
| R01 Schedule | Blueprint lines 595–610 specify 28 October 2026 and 14/21/28/35-day durations. D006 says dates and story points follow architecture review. | B002 must confirm or qualify the chart; no schedule approval inferred. |
| R02 Decision IDs | Current blueprint has zero `O-nn` labels; feature spec line 38 and Section 10 refer to O-01–O-18 as existing blueprint decisions. | B002 must restore/map the references without inventing decisions. |
| R03 Team | Standalone Word vision body paragraph 4 identifies AI Coding Assistant support; consolidated Word paragraph 4 and D010 explicitly identify a HUMAN assistant developer. | Confirm the team interpretation under B002; AI remains unable to provide independent human approval. Paragraph numbers are XML body-paragraph indices, not page numbers. |
| R04 Paths | Pack AGENTS line 5 refers to `docs/handover-pack-v1/001-*` through `010-*`; actual supplied files are directly under the pack's `docs/`. | Resolve imports/reference paths during approved baseline/repository setup; preserve originals. |
| R05 Recommendations | Standalone vision includes Improve (body paragraph 160); D002/consolidated pack enumerate Continue/Pivot/Pause/Stop. | Agree the final vocabulary before Phase 3 implementation. |
| R06 Proposed design | Blueprint stack, schema, APIs and provider options remain proposed; no approved ADR evidence was supplied. | Justice reviews dependent architecture; B001 does not select providers. |
| R07 State semantics | Blueprint line 187 displays statuses in an arrow sequence; D002 lists statuses and feature spec leaves transition rules open. | Clarify whether arrows imply transitions; do not implement Approved → Rejected → On Hold as an automatic sequence. |
| R08 Tracker filename | Build order permits `build-progress.md` or an authoritative equivalent; user requested `progress.md`. | Use the requested local tracker; formal repository adoption remains B003. This is a naming alignment, not a blocker to local recording. |

The ZIP/extracted duplicate comparison found no byte differences. No broader product, architecture or release acceptance is established by the source planning documents; the user acceptance below closes only the B001 local inventory. UI figures remain illustrative. No reconciliation choice has been made in the source documents during B001.

## Commands and observations

| Check | Actual outcome |
| --- | --- |
| `git rev-parse --show-toplevel` in the working folder | Failed as expected for this folder: not a git repository (or any parent directory). Establishes local boundary only. |
| `gh repo view dwentech-ltd/dwentech-cpa --json nameWithOwner,url,isPrivate,defaultBranchRef,description` in sandbox | Failed because the configured localhost proxy refused the connection. This was not evidence of repository absence or denied membership. |
| Same read-only GitHub query with approved sandbox escalation | Succeeded; returned exact repository identity, URL, private visibility, `main` and description above. |
| `rg` scans of current planning/pack Markdown | Confirmed current versions/status, Gantt values, O-reference mismatch and repository-path/team wording. |
| Python standard-library DOCX XML extraction | Reconfirmed standalone versus consolidated team wording and Improve discrepancy; original files unmodified. |
| Python ZIP byte comparison | 14 entries checked; 14 exact matches against the extracted pack. |
| File enumeration and SHA-256 | 22 pre-existing files captured below before report creation/progress update. |

No runtime tests, provider calls, deployments or branch/PR mutations were performed. File hashes identify the observed input baseline, not approval or authorship. The progress.md hash below deliberately refers to its pre-B001-update content; this report is excluded from its own inventory.

## File inventory

Paths are workspace-relative. All hashes are SHA-256.

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `001 — CPA Master Concept & Vision.docx` | 36167 | `9b9cd59d12e8c1ec3674b2e7d1765a90aeb75267fa7ae1251af2dc87ebdff3ae` |
| `CPA_Development_Handover_Pack_v1.docx` | 48837 | `56e88bf7566005dc01968e87612814fb54c6409c55734050e1a516ac3ab428d0` |
| `CPA_Development_Handover_Pack_v1.zip` | 19400 | `ce4b5dcb6052af93b973ba7dc19871d85213b2129adeb9206fcb0df175763841` |
| `CPA_Development_Handover_Pack_v1/AGENTS.md` | 891 | `30b1af59a8735e17bf874d80e720ecda91cf4f7853453c9394518405ec73aec7` |
| `CPA_Development_Handover_Pack_v1/README.md` | 1168 | `c877647379514cc488894fb8f9b0a40e1ea38817155498ee3fa206fdb5644d24` |
| `CPA_Development_Handover_Pack_v1/docs/001-master-concept-and-vision.md` | 3197 | `a42ff97946f5aadff8e7f0d376d1be973ebc1e81f85dce392d4603443a7050bf` |
| `CPA_Development_Handover_Pack_v1/docs/002-enterprise-product-requirements-specification.md` | 6239 | `e4645f44430125abf4ca95b85488a5ac82e7a546f42b9217fc0ef5649b0a6c8b` |
| `CPA_Development_Handover_Pack_v1/docs/003-system-architecture-and-technology-specification.md` | 3265 | `997fcd86b88467a6607004dcba221d9dc80f403925d6e81c84ba22589b8c2431` |
| `CPA_Development_Handover_Pack_v1/docs/004-ai-agents-and-intelligence-framework.md` | 2993 | `d1959571ea6834bed5ed5efffb9a2823397289c739e19b9ab599f4ce6d71ca90` |
| `CPA_Development_Handover_Pack_v1/docs/005-ui-ux-design-specification.md` | 2741 | `188d6cc66cf8b0897d22e005e46afa10471f305dfbb4bbfa0b0fe647cb98c461` |
| `CPA_Development_Handover_Pack_v1/docs/006-development-roadmap-sprint-backlog.md` | 2813 | `4d88b55db284c51c121598c39d6192c198dba228ede1776afb012bd66efc2a8c` |
| `CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md` | 2282 | `36dad95f80263c48731c22e9a653a4caa63dd676c63df7a5ce2af06dbd3f1d29` |
| `CPA_Development_Handover_Pack_v1/docs/008-testing-and-acceptance-framework.md` | 1916 | `cfc2c4682d7abc0d160e4e89ba1883e05bd9f23460c816426fb8aebf22366eb9` |
| `CPA_Development_Handover_Pack_v1/docs/009-deployment-operations-guide.md` | 1941 | `58d20afd0a74f669aca05c2de5e9e1d579a6acbef70ffc7897508510edc64afe` |
| `CPA_Development_Handover_Pack_v1/docs/010-developer-working-agreement-and-assistant-instructions.md` | 2220 | `44a96f6fa68e0b703249af7abeadb9fd0ceb17328a66607cff7b9cc185cc4dd6` |
| `CPA_Development_Handover_Pack_v1/github/HANDOVER_CHECKLIST.md` | 678 | `438b18d31ca54769cc122bd075fa797d810d1bada409ba8094df6745d361b099` |
| `CPA_Development_Handover_Pack_v1/github/PULL_REQUEST_TEMPLATE.md` | 276 | `c9fda53b0d5e7a3ed0b274f8a0597e2476a47d5030e97765af745ce03a034cb0` |
| `UI.png` | 1783208 | `cfae33967dab0a36fd7806a01a28dde6b7411e1dbaa2ba12cd1b1002b6e11eec` |
| `blueprint.md` | 37518 | `271663780d5d3e1f7ff564e51e2dedf29e74f2a9f710133bb7a4d9cb749a32c9` |
| `build-order.md` | 35494 | `3c9198fecb0f084d85c1faf0067cd51153ad61387690c8127443b8ab32234a3e` |
| `feature-spec.md` | 45420 | `16807ddffae0b44774b5983e6abee1a44ea87d7da3bfe3f9b6006be3075c1fe3` |
| `progress.md` | 29069 | `3a6de91868d6665c749c71c93c1da29f0c2aeb1ae5f3f8bfc9c4b4ea4af882a7` |

## Local acceptance record

**Accepted by:** User, through an explicit instruction in this conversation  
**Acceptance date:** 20 October 2026 UTC  
**Accepted scope:** B001 local baseline inventory and its recorded findings

> I accept the B001 local baseline inventory. Use this existing folder as the working project, keep all GitHub activity deferred, and record the identified conflicts for B002. Update the B001 report and progress.md to mark B001 Done. Do not start B002.

The local recheck confirmed all 22 inventoried files exist, 21 retain their recorded hashes, and progress.md has its documented B001 update. All 14 ZIP entries match the extracted pack; task IDs/titles and local links are consistent. The report itself is the additional twenty-third file. Original hashes remain a historical pre-update snapshot and are not rewritten to conceal subsequent tracker changes.

The user accepted the inventory, not the proposed architecture, schedule, unresolved product rules, phase gates or production release. R01–R07 remain recorded for B002 reconciliation; R08 retains the selected progress.md filename and later B003 workflow work. No B002 decision has been made.

## Handoff

B001 is Done. Continue in the existing local folder. All GitHub activity is deferred; a remote checkout is not a prerequisite for this accepted inventory. B002 remains Not started and must not begin until explicitly selected. All phase/release gates remain pending. Existing source material and historical evidence are preserved.
