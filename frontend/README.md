# CPA local frontend

The main Command Centre at **http://127.0.0.1:3000/** now embeds the connected synthetic reference dashboard; **/dashboard** provides its dedicated sidebar route. Sign in to the fixed synthetic fixture, apply type/state/owner filters, use quick views, clear filters and refresh. The header reflects the local session and page reload restores a valid session. Port 8000 remains the separate process-status API.

The main same-origin /api/reference routes verify the retained B027 service at https://127.0.0.1:3543 with its dedicated public CA. No browser trust installation or certificate bypass is needed for the HTTP loopback frontend. See [connection evidence and boundaries](../docs/evidence/main-dashboard-connection.md). Real identity, business metrics and future module workflows remain unavailable. The legacy B016/B022 harness at 3100 remains separate; its source shares the improved Dashboard component. Earlier disconnected-main notes below are milestone history superseded by this record.

From PowerShell:

```powershell
Set-Location 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\frontend'
npm run dev
```

Stop this server with Ctrl+C in its terminal. The launcher binds to 127.0.0.1:3000 only, disables Next telemetry and checks the installed Windows x64 native compiler before starting. It deliberately fails if that compiler is absent, rather than allowing Next to fetch a fallback.

Installed and verified locally: Node 24.21.0, npm 11.19.0, Next 16.3.8, React/React DOM 19.3.0, TypeScript 6.0.3, Node types 24.19.1 and React/React DOM types 19.3.0. This is a local compatibility result, not production qualification.

```powershell
npm run typecheck
npm run build
npm run start
```

Stop the development server before building because both use `.next`. `start` serves the completed production build on the same loopback port. On this host, sandboxed Next worker creation returned `spawn EPERM`; the same command succeeded with approved local execution permission.

## Offline dependencies

The user approved cache-only installation with lifecycle scripts disabled. `.npmrc` enforces offline mode, no install scripts, no audit/funding calls and project-local logs. Exact tarball URLs in `package.json` identify already-cached artifacts; they do not authorise downloads. `package-lock.json` records the resolved dependency tree.

To restore dependencies from a sufficiently populated local cache:

```powershell
npm ci --offline --ignore-scripts --no-audit --no-fund
```

Stop on a cache miss. Do not remove the offline flag or download missing packages. The initial install required permission to write npm's cache temporary files. Fresh-machine reproducibility remains a later B027 check.

## Design and evidence

See [B015 report](../docs/evidence/B015-local-navigation.md) for approved scope, token values, route/keyboard/responsive checks and remaining acceptance. Source labels come from D005; colours and spacing were derived locally from `UI.png` with user approval. System fonts and inline SVG/CSS decoration require no asset downloads.


## B022 local dashboard preview

B022 is approved and Done for verified local synthetic reference metadata. Preview: http://127.0.0.1:3100/dashboard. It connects the isolated session harness to B021 stored queries; the normal app stays disconnected. Evidence: docs/evidence/B022-local-dashboard-ui.md (project root). The retained container and preview remain running by user preference. Future database checks retain containers by default; tmpfs contents are not durable across container stop/reboot. The B022-stop marker ends preview servers only when requested. B023 has not started.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.


## B024 separate local rehearsal

The user selected a local staging rehearsal; it is approved and Done for the verified local scope. HTTPS endpoint: https://127.0.0.1:3443, with separate production frontend and persistent PostgreSQL volume. The private CA was validated explicitly in tests; browser/system trust was not modified. Existing B022 preview/data remain untouched. See deployments/local-rehearsal/README.md and docs/evidence/B024-local-rehearsal.md from project root for operation, scope and retained-state details. Cloud deployment and B025 remain unstarted.


## B024 local rehearsal approved — 21 October 2026

User: “Approve B024”. B024 is Done for the verified user-selected local staging rehearsal. Existing six real HTTPS/database/access/recovery groups, production-build and full local-runner evidence retained; no tests rerun for documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. Hosted deployment, real identity, provider/budget, remote CI and independent review requirements remain deferred. Browser/system certificate trust was not changed. Preview processes, secrets, database containers and volumes were left untouched; no cleanup performed. B025 remains unstarted. Prior records: docs/evidence/B024-before-acceptance.zip.


## B027 current setup and support handover

Use the [current setup guide](../docs/local-setup.md) for the delivered Windows foundation, isolated setup, alternate rehearsal ports and safe operational logs. B027 local checks passed and the verified local scope is approved and Done; spoken screen-reader verification remains outstanding. The additional B027 rehearsal runs at https://127.0.0.1:3543, with separate persistent data and protected redacted logs. Original services and all resources remain retained. B028 unstarted.


## B027 local scope approved — 21 October 2026

User: “Approve B027”. B027 is Done for the verified local setup, keyboard/responsive/semantic accessibility evidence and operational-log handover. Existing verification evidence retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for this scope. Spoken screen-reader verification remains outstanding and B026-OBS-01 remains open. Hosted staging, real identity, remote CI, independent review and G1 sign-offs remain deferred. All services, setup attempts, containers, volumes and backups are retained; no cleanup performed. B028 remains unstarted. Prior records: docs/evidence/B027-before-acceptance.zip.

## Personal accounts — 22 October 2026

The main frontend now offers local email/password signup and login, then an account-owned ideas dashboard. Open http://127.0.0.1:3000/sign-up to create your account. Passwords must be 15–128 characters. Existing demo sessions do not grant personal-account access. No password recovery/email verification is available yet; online hosting remains unfinished.

The interim account database is .local/accounts/accounts.sqlite at the project root, separate from retained PostgreSQL fixtures. Keep its SQLite database/WAL files and owner-only ACL intact; do not upload .local. A .prepared marker is required before API startup. The current workstation directory has been prepared. A new machine needs explicit private directory/ACL preparation before accepting passwords. This adapter supports only http://127.0.0.1:3000 and must not be forwarded to the internet. Future hosted work must select its durable database/authentication configuration and migrate personal work deliberately.

Checks: node --experimental-transform-types scripts/test-local-accounts.mjs (isolated temporary database) and node scripts/test-account-http.mjs (running loopback server; creates reserved example.test accounts, retains them). Neither command uses the user's credentials.

## Administrator / external roles

Ordinary signup creates an external account; neither role fields nor the email address grant administration. Local operator script `node --experimental-transform-types scripts/issue-admin-setup.mjs` issues a one-use setup URL valid for 24 hours, invalidating previous unused setup URLs. Treat its fragment as a temporary credential; do not publish it. At that URL, the user signs up or logs in with the email they choose. Never put their password in chat or shell arguments. No email verification or hosted claim is made.

Administration at /admin is enforced by the API and supports account listing, external-account suspension/reactivation and audited session revocation. Private idea content remains owner-scoped. Sign out / switch account before using another email. Core role tests: `node --experimental-transform-types scripts/test-account-roles.mjs` (in-memory only). Database migration defaults existing accounts to external and preserves saved work.

## Role-based dashboards

Successful login/signup and restored sessions direct administrators to /admin and external users to /dashboard. Opening / or the other dashboard's URL resolves to the signed-in role's destination. Header and navigation share the verified account context; switching accounts discards the previous dashboard before another account opens. Administrator overview/search/status controls use stored account metadata; external ideas remain owner-scoped. API authorization remains authoritative. Verify navigation with `node --experimental-transform-types scripts/test-account-navigation.mjs`.
