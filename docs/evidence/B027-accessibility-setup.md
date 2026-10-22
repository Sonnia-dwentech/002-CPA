# B027 — Accessibility, operational logs and local setup handover

**Date:** 21 October 2026 (Atlantic/Reykjavik). **Status:** Approved and Done for verified local scope on 21 October 2026. User “Start B027” after B026 acceptance; subsequent explicit approval permits exact locked npm downloads for the isolated setup. B028 remains unstarted.

## Delivered

- [Current Windows setup guide](../local-setup.md), replacing obsolete current instructions while preserving the earlier guide in B027-before.zip.
- [Fresh setup runner](../../scripts/check_fresh_local_setup.py): separate retained source/dependency/build folder, Python pins installed offline from cached wheels, npm lock installation with scripts disabled, complete local CI, separate PostgreSQL/dashboard checks and production frontend build.
- Rehearsal launcher now supports distinct loopback ports and explicitly wires the existing OperationalCapture to a protected JSON-lines file. Defaults remain 3200/3443. No existing service was restarted.
- [Log verifier](../../scripts/check_local_support_logs.py) checks actual response/failure logs and redaction without printing credentials.

## Fresh setup and integrated verification

[Setup results](B027-setup-checks.json) record completion and retain failed as well as passing step outcomes. Successful workspace: `.local/b027/4ad0f577510342bcb2ae551e37e343c2/workspace`. Python 3.12.14; observed Node 24.22.0 and npm 11.19.1. Earlier Node/npm observations in historical reports are not this run's inventory.

1. Created a new virtual environment and installed all 17 Python distribution pins with --no-index from recovered cached wheels. Wheel names/hashes are recorded; no independent provenance review is claimed.
2. Initial cache-only frontend install failed on missing locked packages, including undici-types 7.24.6. Repeating with approved cache access confirmed the miss. User then explicitly authorised exact package-lock dependencies from npm; npm ci succeeded with scripts/audit/funding disabled and lock integrity checks intact. No working dependency install or lockfile was replaced.
3. Fresh CI initially failed because the source-copy runner omitted public .env.example. Added that copy and resumed the retained run; CI passed. No successful install was discarded. Earlier cached-body scanning also needed to ignore non-ZIP HTTP cache entries; corrected before installation. All attempts are retained.
4. Fresh local CI passed: source/config/dependency consistency, **70 backend tests**, 5 runner tests, dashboard contract and all three TypeScript projects. The copied snapshot scanned 72 files; the final working-tree suite scanned 73 after adding the log verifier and also exited 0.
5. Fresh real PostgreSQL migration/dashboard harness passed and retained `cpa-b021-check-e07a5882cb174ea69c1afb6901e17abd`. Its tmpfs data are not durable across stop/reboot; no stop/removal occurred.
6. Normal frontend production build passed from fresh dependencies. A separate rehearsal production build and new persistent database then ran all six HTTPS/database/access/failure/recovery groups successfully. The rehearsal remains at https://127.0.0.1:3543, with internal frontend 3300. [Runtime metadata](B027-rehearsal-runtime.json) identifies the retained container/volume and protected paths. Main B024/B025 metadata and resources were not reused.

[Verified source hashes](B027-verified-source-hashes.json) match the launched rehearsal/backend and shared UI/lock inputs to working source. This is a fresh application dependency setup on the same Windows machine, not an independent clean OS, other platform or hosted deployment qualification. The resumed copy retains its earlier setup-runner source; current runner fixes are in the working project. Application/launcher/shared UI inputs matched exactly.

## Keyboard, semantics and responsive evidence

[Observed checks](B027-accessibility-checks.json), [shell accessibility tree](B027-shell-accessibility.txt), [dashboard accessibility tree](B027-dashboard-accessibility.txt), [desktop shell](B027-shell-desktop.png), [mobile shell](B027-shell-mobile.png), [mobile dashboard](B027-dashboard-mobile.png).

- First shell Tab exposed Skip to content; Enter focused main-content. Keyboard Idea Studio navigation changed the page title and focused main-content, with its unavailable state exposed.
- At 390 px, keyboard Enter expanded Menu, Tab reached Command Centre and Escape collapsed Menu and returned focus to its button. The screenshot shows visible focus.
- Dashboard keyboard login succeeded. Invalid owner input submitted by keyboard exposed “Check the filters. Owner must be a UUID.” and focused the role=status element. Keyboard sign-out hid count and list.
- Accessibility tree exposed descriptive titles/headings, named navigation, unavailable labels, labelled native controls and a polite live status. DOM inspection confirmed aria-live=polite, role=status and tabindex=-1. This provides screen-reader-facing semantic evidence; actual Narrator/NVDA speech, announcement timing and reading order were not heard/tested.
- Measured no horizontal document overflow: shell 390/375 px viewport/document and desktop 1440/1425; dashboard 390/375 and 320/305. Dashboard form controls were at least 44 px high. Mobile screenshots were visually inspected. The attempted tablet screenshot retained a desktop viewport, so it is excluded from claimed responsive results.
- Browser verification used the existing normal shell at 3000 and shared dashboard on B022 at 3100. It does not establish a trusted-browser HTTPS journey on the new rehearsal. No certificate warning bypass or global trust change occurred. Temporary viewport overrides were reset.
- B026-OBS-01 remains open: this clean-session keyboard login passed, but that does not establish the cause or resolution of the earlier initial login failure.

## Actual support-log evidence

[Log verification](B027-support-log-checks.json) passed on **24 real events**, including HTTP **200, 400, 401, 403, 404 and 503**. The 503 events were generated by the new isolated launcher's controlled database fault and recovery. [Redacted event records](B027-operational-events.jsonl) contain exactly request_id, allowlisted route name, normalized method, status and duration_ms. No raw URL/path/query, request body, headers, cookies, token, SQL or exception text is captured. Canary path/query/header/cookie values and both database passwords were absent. Random request IDs are not yet propagated to client responses; client-to-server correlation and timestamps/rotation/retention/alerting are not completed production monitoring.

Original B024 has not been restarted to load the new logging wiring, and no historical access events are fabricated. This is live local rehearsal support-log evidence. Hosted staging log access remains deferred; the B017 audit-event contract stays separate.

## Remaining human checks and acceptance boundary

Before claiming spoken screen-reader usability, a human should run their supported reader (for example Narrator or NVDA) through the shell skip link, menu expansion/collapse, page title/headings, dashboard filter labels, loading/error/zero results and sign-out. Confirm announcement order, one understandable result announcement and no keyboard trap; record actual tool/version and outcome. No conformance certification is claimed from these checks.

Original hosted-staging requirements, real identity, independent code review, remote CI and G1 technical/functional sign-offs remain deferred. B027's local setup/log/keyboard/responsive scope is approved and Done, with spoken-reader verification explicitly outstanding. User approval of this local pack must not be represented as independent review or hosted readiness. B028 has not started.

Every prior preview, setup attempt, container, volume and backup remains retained. No cleanup was performed. The new rehearsal is an additional local service; its private stop marker is documented for use only when requested.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.
