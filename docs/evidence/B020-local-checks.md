# B020 — Local check preparation and remote blocker

Date: 21 October 2026 (America/Los_Angeles). Status: **Done for the user-revised local scope, approved 21 October 2026; remote requirements deferred to RCI-01.**

Authority: user “Start B020”, followed by “Keep GitHub deferred; prepare locally”. Codex prepared and verified local checks. B019 is accepted. Justice remains nominated accountable owner; no independent review or remote control approval is inferred.

## Delivered

- [Offline check runner](../../scripts/check_local_ci.py).
- [Runner verification tests](../../scripts/tests/test_local_ci.py).
- [Pre-change records](B020-before.zip).

From the project root:

```powershell
.\backend\.venv312\Scripts\python.exe -B scripts/check_local_ci.py
```

The runner uses the installed Python environment and Node on PATH. It installs nothing, fetches no advisory feeds, reads no live credentials, and makes no remote requests. The existing backend test suite briefly uses loopback HTTP and stops its test server.

## Actual results

| Check | Result |
| --- | --- |
| Active source/config syntax and limited secret patterns | PASS, 49 files inspected |
| Installed Python direct/resolved pins | PASS |
| Frontend manifest/lock agreement and installed direct versions | PASS |
| Python dependency consistency (`pip check`) | PASS |
| Backend suite | PASS, existing 54 tests |
| Runner tests | PASS, 5 tests |
| Frontend TypeScript | PASS, no emit or incremental write |
| Isolated browser harness TypeScript | PASS, no emit or incremental write |
| Complete local runner | Exit code 0 |
| Deliberate failure command below | Exit code 1, as expected |

```powershell
.\backend\.venv312\Scripts\python.exe -B scripts/check_local_ci.py --self-test-failure
```

The deliberate failure runs a harmless child that exits 7; the runner reports `controlled_failure: FAIL` and exits 1. Runner tests additionally prove later steps are not invoked following a failed child. Synthetic token fixtures verify detection and that reported findings contain only file/line/category, not matched values. Subprocess output is withheld because it may include private payloads; to investigate a trusted local failure, rerun the named underlying command separately. Exceptions/timeouts fail the runner with a fixed diagnostic. This proves local failure propagation, **not GitHub merge blocking**.

## Coverage limits

The syntax pass parses Python and JSON. It is not a full Python style or semantic linter. TypeScript checks cover the current application and separate harness. No Ruff or Gitleaks executable was found on PATH, and no such tools were installed.

The built-in scan detects selected private-key, GitHub-token, provider-key and AWS access-key signatures. Scope is code/config files under backend, frontend and scripts plus the root `.env.example`. Dependency directories, Python environments, generated Next output, Git internals and caches are excluded; original handover material, archives, backups, documentation, binary files and actual `.env` files are outside this scan. Symlinks within traversed scope fail closed. This is a limited local pattern scan, not a complete secret audit or Git-history scan. No real secret was discovered or displayed.

Dependency checks compare installed Python versions against both recorded requirement files, compare frontend manifests with the lockfile, and check installed direct frontend versions. They do not verify package provenance, every transitive frontend package or current vulnerability advisories. No dependency download, vulnerability service or clean-machine installation is exercised. PostgreSQL integration, frontend production builds and browser checks were not repeated for this tooling-only preparation.

## Original remote blocker — history; superseded by local replan below

The local project root has no `.git` marker. The user's GitHub deferral remains explicit. No repository was initialised, cloned, inspected remotely or modified; no Actions workflow, PR, branch rule or remote required check was created. Local commands are preparation for a later reviewed CI integration.

The unchanged B020 acceptance check requires a controlled failing check to block an eligible merge, passing checks, and required checks matching verified branch settings. Before that can be claimed, obtain separately authorised remote access, complete the applicable B004 verification, review runner/platform/tool choices, install the intended CI tooling, adopt protected-branch check names, and demonstrate failed/passing runs against an eligible PR without bypassing rules. Dependency advisory and full secret-scanning tool availability must also be assessed there.

B020 remains **Blocked**, not Done or In review for full completion. B004 remains Blocked; B005/B007 remain In review. B021 is Not started. Local success does not authorise remote activity or change gate/merge requirements.


## User-approved local-only replan — 21 October 2026

User: “Keep everything local till github comes in later”, selecting the proposed local-only option. B020 now covers passing local syntax/type/test/dependency/limited secret checks, controlled nonzero failure propagation and documented coverage limits. Existing results meet that local completion check; B020 is In review pending deliverable acceptance. No tests were rerun for this documentation-only change.

The original remote merge/branch verification criteria are preserved as [RCI-01](../planning/remote-ci-handoff.md), mandatory before remote collaboration/merge or release. They have not passed and are not waived. B004 remains Blocked, B021 remains unstarted, and GitHub stays deferred. [Pre-replan snapshot](B020-before-local-replan.zip) preserves the original scope/status.


## Local deliverable approval — 21 October 2026

User: “Approve B020”. The revised local deliverable is accepted; B020 Done. Earlier pending-acceptance wording is superseded. Existing 54 backend tests, 5 runner tests, source/dependency/type checks and expected failure-path evidence are retained; no tests rerun for this documentation-only update. Original remote requirements remain mandatory under RCI-01 and unverified. B004 remains Blocked, B021 remains Not started, and all work stays local. No remote CI or independent review approval is inferred. [Pre-approval records](B020-before-acceptance.zip) preserved.
