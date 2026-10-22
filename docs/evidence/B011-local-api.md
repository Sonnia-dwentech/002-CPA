# B011 — Local API Startup, Health and Error Contract

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B011”; accepted G0-L and provisional Python tooling; no authority for remote/live-service work  
**Status:** Done — user accepted local API scope on 20 October 2026 UTC  
**Executor:** Codex; Justice remains nominated accountable owner; no formal technical/independent review recorded

## Acceptance recorded — 20 October 2026 UTC

User: “I accept B011’s local API deliverable”. B011 is Done for the local startup/health/OpenAPI/error scope tested under G0-L. No independent human technical review, general architecture approval, authentication/database readiness or deployment sign-off is inferred.

Database setup remains explicitly deferred and B012 has not started. [Pre-acceptance snapshot](B011-before-acceptance.zip) preserves the earlier tracker/report. The verification counts below describe the original execution snapshot; no code or test result changed during acceptance.

## Delivered and scope

[Backend guide](../../backend/README.md) documents launch/test commands and limitations. [Application](../../backend/app/main.py) exposes `GET /health` and `/openapi.json`. The [launcher](../../backend/run_local.py) binds only to 127.0.0.1, suppresses access/error-detail logging and disables proxy-header trust/server-version header. Browser docs are disabled to avoid external asset requests.

Health returns only `{"status":"ok"}` and no-store; it is process liveness, not database/provider/full-product readiness. Structured 404/405/422/500 responses use generic messages; HTTP and validation details are not echoed. The 405 Allow header is retained. Unknown HTTP errors also use generic messages. No authentication or data/business endpoints are provided; test-only validation/error routes exist only inside isolated tests.

The selected task explicitly names FastAPI. This is a bounded local implementation of that named component, not a broad approval of the proposed stack or B005 architecture. No database service, model, identity provider or frontend was introduced. No .env is loaded. Operational redacted logging remains B017 work, so the launcher is not suitable evidence of production observability.

## Runtime evidence

Observed and exercised Python 3.14.8 with installed FastAPI 0.143.0, Uvicorn 0.54.0, Pydantic 2.13.5 and Starlette 1.7.0. These versions are recorded in requirements-local.txt as tested local pins, not a complete transitive lock or production approval. pytest/httpx were not installed; standard-library unittest/HTTP tools suffice. No packages downloaded or installed.

Initial inventory commands encountered shell quoting and terminal encoding errors; corrected bounded metadata queries succeeded. No application check was counted passed from those failed probes.

## Verification

Command, run in backend: `python -B -m unittest discover -s tests -v`.

**Result: 9 tests passed.**

- Liveness stays minimal with synthetic environment/query canaries.
- Missing route does not echo a private path.
- Wrong method returns a structured 405 with Allow.
- Invalid input returns generic 422 without submitted values.
- HTTP exception detail/private header suppressed.
- Unhandled exception returns generic 500.
- OpenAPI matches implemented route and response schemas; test routes absent.
- Browser docs endpoints disabled.
- Actual loopback launcher starts, answers health without server header, stops in cleanup and does not log the synthetic query canary.

Only local loopback networking was used. The child test server was stopped; no background application remains intentionally running. No GitHub/web/provider/database access, installation, staging or deployment occurred. Application-wide security, authentication, concurrency/load and full end-to-end checks remain future work.

## B010 verification handoff

B011 backend startup evidence is now recorded. The earlier PowerShell preflight remains execution-policy blocked; Python launch/test commands succeeded without changing that policy. A fresh isolated installation from locked dependencies, database setup and complete foundation walkthrough remain unverified. B012 database deferral is unchanged and B012 was not started.

## Preservation

[B011-before.zip](B011-before.zip) retains the five edited navigation/ledger files; [input hashes](B011-input-hashes.json) cover all pre-existing files. Original sources, task definitions, ADRs, policy, earlier evidence, .env.example and PowerShell preflight are unchanged. New backend files are local source/tests/docs plus Python-generated cache files, ignored by backend/.gitignore. No Git repository was initialised.

- PASS: five archived files match input hashes; all 69 other pre-existing files unchanged, including build-order task definitions.
- PASS: 105 tasks; totals 7 Done, 1 Blocked, 3 In review, 94 Not started. B012–B105 remain Not started.
- PASS: local file links and Markdown fences verified; no .git or private .env created.

## Handoff

User acceptance is recorded above for B011's local API startup, health, OpenAPI and error-contract deliverable. Formal architecture/independent-review and deployment approval remain separate requirements. Do not start B012 until separately selected and its database deferral/technical decisions are explicitly addressed.

Acceptance update verified: 105 task rows, 8 Done, 1 Blocked, 2 In review, 94 Not started. Only B011 changed status; backend source/tests and all other pre-existing files outside progress/report remain unchanged.
