# B021 — Local dashboard queries and verification gap

Date: 21 October 2026 (America/Los_Angeles). Status: **Done for verified local scope; user approved 21 October 2026.**

Authority: user “Start B021”, followed by “Approve this local baseline” for synthetic permission-reference counts, kind/state/owner filters and unavailable business metrics. [Contract](../planning/B021-local-dashboard-contract.md). B020 is accepted. Codex executed; Justice remains nominated accountable owner, without inferred independent review.

## Delivered

- [Dashboard query service](../../backend/app/dashboard.py), isolated from normal HTTP and frontend routes.
- [14 synthetic contract tests](../../backend/tests/test_dashboard.py), using repository doubles and the existing B013 pure permission function.
- [Actual PostgreSQL verification harness](../../backend/check_local_dashboard.py), prepared but not executed. Existing disposable database runner now recognises B021; no database schema changes.
- [Pre-change records](B021-before.zip).

The service accepts only a trusted `VerifiedIdentity`, checks current active internal membership and delegates row visibility to B013 `AccessStore`. Exact kind/state/owner filters narrow visible records; they cannot confer permission. It deduplicates by UUID, returns a matching total/list, includes archived references unless filtered, and exposes only id/kind/state/owner metadata. It requests a read-only REPEATABLE READ transaction on an idle dedicated connection; all permission reads and row selection belong to that snapshot. The next query reloads grants.

Empty available queries return zero; disabled kinds return `unavailable` with `total=None`. Unsupported filters return 422; invalid identity returns 401; client dashboard access returns 403; database or busy-connection failure returns generic 503 rather than zero. All result objects identify `synthetic_reference_records`; business metrics remain unavailable. No production-scale pagination, service availability claim, business schema or B022 frontend work is included.

## Verification performed

`backend/.venv312/Scripts/python.exe -B -m unittest discover -s tests -v`, from backend: **68 tests passed**, including 14 new dashboard tests.

The local runner additionally passed source/config checks (52 files), dependency consistency, 5 runner tests and frontend/harness type checks. No dependencies installed or remote calls made. Test servers shut down normally.

New unit tests cover matching count/list, AND filters, hidden-owner non-disclosure, next-query grant revocation, inactive/unknown actors, client denial, role-only denial, client-case assignment restrictions, unavailable versus empty, strict filter validation, failure without fabricated zero, snapshot command/idle connection requirements and duplicate-count prevention.

These tests use doubles for repository access. They do **not** verify actual SQL execution, PostgreSQL snapshot behaviour, database integrity checks inside AccessStore or concurrency under a real database. No passing database integration result is claimed.

## Outstanding verification and handoff

Read-only availability checks found no `docker` on PATH and no executable at the usual Docker Desktop location. The existing verification runner depends on an installed Docker engine and offline PostgreSQL image. No service, container, download or install was attempted. Database verification remains necessary before full B021 acceptance.

Once a suitable local disposable PostgreSQL runtime is available, from backend run:

```powershell
.\.venv312\Scripts\python.exe -B check_local_dashboard.py
```

The prepared harness uses the established isolated Docker workflow, applies existing migrations, seeds synthetic records, checks persisted permission/filter/revocation behaviour, forces a query failure and recovery, and cleans up its disposable container. It must actually run successfully; code presence is not evidence. No existing or real-client database may be substituted silently.

B021 remains Blocked solely on executing the required persisted-query verification; the proposed metric baseline is approved. B022 remains Not started. Work stays local, GitHub/RCI-01 deferred, live AI disabled. No independent review, full F02 delivery or deployment acceptance inferred.


## Docker installation prerequisite check — 21 October 2026

User requested “Install Docker”. Authorised read-only checks outside the sandbox found Windows 11 Pro 64-bit version 10.0.22000. WinGet offers Docker Desktop 4.96.0 from Docker Inc. Official Docker documentation requires Windows 11 build 22631 (23H2) or higher and modern WSL (https://docs.docker.com/desktop/setup/install/windows-install/). The installed WSL command returned legacy usage rather than version details. No Docker package was installed and no OS upgrade, WSL installation or reboot was performed. A supported Windows upgrade is required before proceeding with the current Docker Desktop installer. B021's actual PostgreSQL verification remains blocked. GitHub/project remote access remains deferred.


## Docker recheck and Windows prerequisites — 21 October 2026

User: “Check if docker has been installed and use it”. Docker Desktop is now installed at `C:/Program Files/Docker/Docker`; CLI version 29.9.1, Desktop log identifies 4.96.0. Started Desktop. Engine queries failed with HTTP 500; startup logs identify Virtual Machine Platform not enabled. These observations supersede the earlier absence of Docker.

The initial feature-enable attempt lacked administrator elevation. Subsequent approved UAC-elevated DISM commands enabled VirtualMachinePlatform and Microsoft-Windows-Subsystem-Linux with /All /NoRestart; both returned 3010 (success, restart required). No reboot performed. Docker Desktop remains launched; no test container, database or image pull was performed. Existing PostgreSQL image availability is still unknown because engine inspection failed.

Next: user restarts Windows, then recheck Docker/WSL readiness and run B021 disposable PostgreSQL verification when usable. Windows still reports build 22000 and WSL lacks modern version reporting; further compatibility/update work may remain after reboot. B021 remains Blocked; no passing database result or acceptance inferred.


## Successful PostgreSQL verification — 21 October 2026

This result supersedes earlier missing-runtime and unexecuted-harness observations. After the user-confirmed reboot, Docker Desktop restart restored engine readiness (29.9.1). Approved download supplied official postgres:17, image sha256:a63c1ea3f6a3a5a1621f97d2aba3b30faecfab4224c1b0000cc85ced57bb1939. PostgreSQL reports 17.11 (Debian 17.11-1.pgdg13+2).

The unchanged check_local_dashboard.py exited 0 with 15 passing checks: loopback connectivity; migration application and idempotence; changed/missing history rejection; failed migration rollback; corrected migration recovery; failed transaction preservation; synthetic rollback; owner/shared counts and hidden-record exclusion; combined filters/archived/empty/unavailable; next-query revocation; inactive/unknown identity denial; unsupported filters and busy-transaction rejection; actual SQL failure and recovery without false zero. This establishes tested persisted-query behavior, not concurrent-load or production-scale assurance.

The runner confirmed disposable container removal and tmpfs data disposal. This completed before the user said “Do not clean it up”. Docker and postgres:17 remain installed. Retain future test containers unless asked otherwise; do not reuse the automatic-cleanup harness unchanged. No existing database was selected.

Full local check runner also exited 0: 52 source/config files, dependency pins/consistency, backend tests, runner tests and frontend/harness types passed. No implementation changes were needed. B021 is approved and Done for local scope; B022 remains unstarted and remote work deferred.


## B021 local deliverable approved — 21 October 2026

User: “Approve B021”. B021 is Done for the verified local synthetic-reference dashboard queries and filters. Existing 68 backend tests, 15 actual PostgreSQL checks and full local check runner passed; no tests rerun for this documentation-only acceptance. Earlier blocked/pending-acceptance wording is historical and superseded. B022 remains unstarted. Business metrics and frontend/API exposure remain outside this accepted scope; GitHub/RCI-01 remains deferred. Retain future test containers unless the user asks otherwise and keep approvals in chat. Pre-approval records: docs/evidence/B021-before-acceptance.zip.
