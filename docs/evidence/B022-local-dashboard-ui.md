# B022 — Local synthetic dashboard UI

Date: 21 October 2026 (client date; Atlantic/Reykjavik). Status: **Done for verified local scope; user approved 21 October 2026.**

## Authority and scope

User “Start B022” after accepting B021. Continues approved B015 styling, B016 isolated synthetic session transport, and B021 reference metric/filter definitions. Codex executed; Justice remains accountable owner. This does not establish independent review or production acceptance. GitHub remains deferred; stop before B023.

Delivered a reusable reference dashboard with visible-count card and matching metadata list, exact kind/state/owner filters, URL-retained selections, loading, empty, unavailable and safe error states. Counts/list clear before refresh or filter changes. Request sequencing and cancellation prevent outdated responses replacing later results. Malformed payloads cannot fabricate counts. Business metrics, scanner and voice remain explicitly unavailable. The normal app renders the dashboard as disconnected; only the separately launched harness connects to PostgreSQL.

## Files

- `frontend/components/Dashboard.tsx`: UI and state handling.
- `frontend/lib/dashboard.ts`: payload and filter validation.
- `frontend/harness/app/dashboard/page.tsx`, `frontend/harness/app/api/dashboard/route.ts`: isolated page and cookie-authenticated proxy. Reuses existing B016 session transport, rejects duplicate cookies and unexpected request headers/filters, uses no-store and safe error bodies, forwards only allowed fields.
- `backend/check_local_dashboard_ui.py`: new synthetic-only backend routes, session validation and B021 DashboardStore, actual database/BFF verification and optional persistent preview process.
- `backend/check_local_database.py`: retains created test containers by default per user instruction; no automatic removal. Added B022 task identifier.
- `scripts/test_dashboard_contract.mjs`: rejects count/list mismatch, duplicate records, malformed metadata and filters, and false unavailable zeroes; included in local CI runner.
- `frontend/app/page.tsx`, `frontend/app/globals.css`: shared component and existing visual tokens; normal app remains disconnected.

## Executed verification

Full local runner exited 0: 58 source/config files, installed dependency pins/consistency, all 68 backend tests, 5 runner tests, dashboard contract checks and both frontend type checks passed. A subsequent singular/plural message correction was confirmed by the running frontend; no logic changed.

Actual PostgreSQL/HTTP/BFF harness reported six passing groups while remaining alive in --serve mode:

1. Card/list data match three persisted owner/shared references; the fourth inaccessible reference and credentials are absent.
2. AND filters, empty versus unavailable, duplicate filters/cookies, cross-site and spoofed requests.
3. Actual table-unavailability query failure returns 503 without counts or SQL details; recovery succeeds.
4. Grant revocation and sign-out replay denial through the frontend proxy.
5. Normal backend still rejects dashboard and synthetic-issuance routes.
6. Captured frontend logs omit the harness key and issued token.

The shared migration/recovery assertions completed before these checks. The server process deliberately remains running, so no completed-process exit code is claimed for --serve.

Browser checks through the in-app browser: unauthenticated no-count view; synthetic login; loading with disabled controls and cleared counts; three records/card agreement; submitted filter gives honest zero and empty list; reload retains the selected filter; research gives unavailable with no count; idea/draft/owner filters produce one record; real database failure gives an error with no counts; restore plus Retry recovers the filtered count; keyboard Tab/Enter submits and result focus returns; sign-out immediately hides records. Scanner/voice have no launch controls. Final populated preview: [screenshot](B022-dashboard.png); actual error: [screenshot](B022-browser-error.png).

AC-F02-01–03 verified only for approved synthetic-reference scope. No live business metrics, real account, production pagination/load, staging, complete mobile or screen-reader audit is claimed. Responsive CSS is provided; broader accessibility/setup evidence remains B027.

## Running preview and retained storage

Preview: http://127.0.0.1:3100/dashboard (backend 127.0.0.1:8100). The browser is left signed into a synthetic fixture. No real account exists. Preview is held by the active check_local_dashboard_ui.py --serve process.

Retained container: `cpa-b022-check-2c4e5c7f77664a28b9e8b6ffd419522d`, official PostgreSQL 17 image already downloaded. No database container was stopped or removed. Data is in tmpfs: retaining this running container is not a durable backup across container stop/reboot. User controls eventual cleanup; owner Justice; cleanup trigger is explicit user instruction. No background cleanup or scheduled deletion.

To end preview servers when requested, create `docs/evidence/B022-stop`; the runner leaves the database container running. Inspect/remove that marker before a later launch. A new launch creates a new isolated database rather than adopting any existing one. Credentials are process-local and are not written to evidence. The table temporarily renamed for browser error verification was restored successfully; normal queries pass.

Fixture manifest: B022 v1, invented entirely by Codex for local verification; users 1/2/3, references 11/12/13/14, owner/shared/hidden states; schema uses unchanged existing migrations. Three visible results initially, two ideas and one archived dossier, one hidden idea. No real user/client data, providers or external recipients. Pre-change files: B022-before.zip.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.
