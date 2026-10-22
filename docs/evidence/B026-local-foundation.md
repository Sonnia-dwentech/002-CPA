# B026 — Local foundation verification

**Status:** Approved and Done for the verified existing synthetic local rehearsal scope on 21 October 2026. User selected “Start with B026” after B025 approval. No hosted staging or release acceptance is claimed.

## Executed evidence

[Reusable runner](../../backend/check_local_foundation.py) exited 0; [six live check groups](B026-local-foundation-checks.json) record execution time and scope. No application behavior changed.

- Production HTML and all referenced JavaScript assets returned 200 through hostname-verified HTTPS with the explicit private CA. Default trust rejected that CA. Security headers and database readiness passed.
- Anonymous dashboard/session/record requests returned 401 (AT-01). Incorrect Host/Origin and cross-site requests were rejected.
- Synthetic authentication returned a Secure, HttpOnly, SameSite=Strict host-only cookie. Dashboard returned three permitted records; owned and shared direct records returned 200. Hidden and nonexistent record requests returned identical 404 responses.
- Hidden-owner filtering returned zero without leaking the hidden record. Unsupported file/search routes and direct frontend record paths returned 404. These checks establish no implemented file/search capability.
- Valid combined filters, honest zero/unavailable results, malformed and duplicate query rejection, duplicate cookies and spoofed authorization checks passed. Errors exposed no counts or traceback. Logout replay returned 401.
- Read-only database inspection confirmed four retained fixtures, the expected database/runtime identity, and denial of schema creation, record deletion and membership changes. Only this runner's session was issued/validated/revoked; no schema or fixture mutation, restart or cleanup occurred.

Full offline local runner exited 0: 70 source/config files, dependency checks, 68 backend tests, 5 runner tests, dashboard contract and normal/harness/rehearsal TypeScript checks.

## Browser verification and observation

The shared Dashboard component was exercised in the retained B022 browser harness at http://127.0.0.1:3100/dashboard. A first sign-in displayed “Sign-in unavailable”. Explicit Sign out succeeded; subsequent sign-in displayed three accessible synthetic references. Filtering owner 00000000-0000-0000-0000-000000000003 displayed zero and no matching records. Sign out hid the count/list. [Authenticated screenshot](B026-browser-dashboard.png).

The exact cause of the initial sign-in failure was not established. The existing session route deliberately rejects login when a cookie is present, but no response capture proves this was that case. Keep this as an open usability/diagnostic observation (B026-OBS-01); do not infer a new authentication defect or silently claim a clean first-attempt journey. Explicit logout/retry recovered in this check.

The browser check used B022's HTTP harness and separate database. It is supplemental shared-component evidence, not an authenticated browser journey on B024 HTTPS. B024 production HTML/assets and API/database integration were verified with TLS programmatically. Browser certificate trust was neither installed nor bypassed.

## Acceptance mapping and limits

- AC-F01-02: applicable synthetic direct-record and filtered-list/count isolation passed. File/search endpoints are unavailable and reject requests; future real file/search/content paths require their own checks.
- AC-F20-01: local production asset/API/database operation, agreed local CI and secure-configuration checks passed. Observable invalid-request errors were exercised now. Actual database-outage/readiness recovery evidence is carried forward from [B024](B024-local-rehearsal.md), not re-executed against the retained running database.
- Full hosted staging, real identity/MFA, remote CI RCI-01, independent review and a browser-trusted HTTPS end-to-end journey remain deferred. The complete original staging criterion is not claimed passed.
- B026-OBS-01 remains open for review; no risk acceptance inferred. B027 remains unstarted.

All previews, backups, database containers and volumes are retained. Prior tracking files: B026-before.zip.


## B026 local verification approved — 21 October 2026

User: “Approve B026”. B026 is Done for the verified local foundation scope. Six live check groups, the full local runner and supplemental browser evidence are retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded for local scope. B026-OBS-01 remains open with cause unproven; approval does not resolve it. Hosted staging, trusted-browser HTTPS, real identity, remote CI and independent review remain deferred. Existing previews, backups and database resources were left untouched; no cleanup. B027 remains unstarted. Prior records: docs/evidence/B026-before-acceptance.zip.
