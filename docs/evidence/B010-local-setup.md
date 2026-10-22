# B010 — Local Setup Preparation and Blockers

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B010”; subsequent provisional-tooling approval and database deferral  
**Status:** Done — user accepted revised local setup-preparation scope; executable setup remains unverified  
**Executor:** Codex; Justice remains nominated accountable owner

## Scoped acceptance — 20 October 2026 UTC

User: “Approve and Accept B010”. This follows the proposal to revise B010 to setup preparation and demonstrate runnable components at B011/B012/B015–B016, with a final fresh-setup walkthrough. The revised check is recorded in build-order.md; B010 is Done for preparation only.

Existing local inventory, provisional runtime approval, placeholder template, setup guide and honest recorded limitations satisfy that scope. The original fresh-setup check has not passed: B011 retains backend verification, B012 database verification after explicit authorisation, B015–B016 frontend/integration verification, and B027 the full fresh isolated setup walkthrough before B028/G1. Justice remains technical authority; task executors record actual results when selected.

The PowerShell launch failure is not resolved by acceptance. Database remains deferred, runtimes provisional, and no install/download, GitHub connection, policy change or B011 execution is authorised. [Pre-acceptance snapshot](B010-before-scoped-acceptance.zip) preserves the original blocked assessment. Sections below describe that historical preparation/check evidence; this acceptance supersedes only the task completion scope/status.

## Delivered

- [Windows setup guide](../local-setup.md), distinguishing inventory from working setup and retaining network restrictions.
- [Public configuration template](../../.env.example) with empty sensitive/undecided values, local defaults and a proposed false live-AI switch; no application consumes it yet.
- [Read-only PowerShell preflight](../../scripts/check-local-setup.ps1), syntax checked but not successfully launched due to execution policy. Never reads a private .env or contacts services.
- Project/documentation navigation and current progress updated. No application scaffolding or later-task code created.

## User decisions

User answered “Approve provisional local tooling”: Python 3.14.8, Node 24.21.0 and npm 11.19.0 approved provisionally for the proposed FastAPI/Next.js stack; application compatibility unverified, no installs/downloads authorised. This does not approve B005 architecture or particular dependency versions.

User answered “Defer database setup; document blocker”. No native or Docker PostgreSQL approach selected, no database started, and no image pulled.

## Observations and commands

| Local check | Actual result |
| --- | --- |
| `Get-Command` for tools | python/node/npm/docker resolved; psql not found on PATH |
| `python --version` | Python 3.14.8 |
| `node --version` | v24.21.0 |
| Explicit local `npm.cmd --version` | 11.19.0 |
| `docker --version` | CLI 29.8.2; no daemon/image/database check |
| `py -0p` | Python 3.14 listed; no other launcher runtime shown |
| Optional conventional PostgreSQL folder listing | No entries returned; not proof of global absence. Combined shell command returned 1 for the unavailable lookup, not for the successful version probes |
| `powershell.exe -NoProfile -File .\scripts\check-local-setup.ps1` | Failed: running scripts disabled on system, UnauthorizedAccess. No policy override/change attempted |
| PowerShell Parser.ParseFile | No syntax errors; parsing is not execution verification |

## Completion assessment and blockers

B010 requires fresh setup steps working with approved runtime versions and a placeholder-only `.env.example`. Template preparation and provisional-tool inventory are complete; full application setup is not proven.

| Blocker | Owner / required action | Boundary |
| --- | --- | --- |
| Database explicitly deferred | User selects later setup scope; Justice approves approach and disposable destination | Do not infer PostgreSQL unavailable everywhere or pull/start/install anything |
| Script execution policy | User/local administrator approves a permitted execution method if needed | Do not change machine policy or call the preflight successful |
| No approved locked dependencies or runnable scaffold | Justice/task authority agrees versions and setup artifacts, or explicit revised B010 local scope/dependency plan | Do not invent run commands, download packages or begin B011/B012 implicitly |
| Provisional runtimes not compatibility-tested | Verify against actual approved application dependencies and fresh isolated setup | Installed versions alone do not establish support |

The build order places API/database implementation at B011/B012. If executable verification depends on those later artifacts, obtain a specific recorded scope/dependency adjustment. Until then B010 stays Blocked rather than claiming the original completion check passed.

## Preservation and verification

[B010-before.zip](B010-before.zip) retains pre-edit progress/README/index. [Input hashes](B010-input-hashes.json) cover all pre-existing files. No private .env, secrets, client data, application manifests, services or Git metadata were created. No GitHub/web/registry access, download, install, provider call or deployment occurred. B011 remains Not started.

- PASS: all 64 pre-existing files other than the three intentionally edited records remain unchanged; build task definitions preserved.
- PASS: static configuration validation found exactly the expected 10 placeholder/default keys, no duplicate entries and no actual credentials.
- PASS: 105 task rows; 6 Done, 2 Blocked, 2 In review, 95 Not started; changed-document file links resolve.
- LIMITED: PowerShell syntax parses; documented launch failed due to execution policy. No fresh application installation/startup or database check passed.

Acceptance-update verification: only B010 status changed; 105 tasks total 7 Done, 1 Blocked, 2 In review, 95 Not started. B011–B105 remain Not started. No runtime execution or external action performed for acceptance.
