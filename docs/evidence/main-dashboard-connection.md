# Main application — connected reference dashboard

Date: 21 October 2026 (Atlantic/Reykjavik). Authority: user “Improve the functionalities and connect the reference dashboard”. Delivered for user review; no B029 selection, numbered task status or gate outcome changed.

## Delivered behavior

The Command Centre at http://127.0.0.1:3000 now embeds the functioning reference dashboard. The sidebar includes an available Reference dashboard route at http://127.0.0.1:3000/dashboard. Both use the same shared component and same-origin local API; future workspaces keep their unavailable labels.

Added explicit session restoration before enabling sign-in, an accurate session indicator in the page/header, quick All references/Ideas/Dossiers views, Clear filters, manual refresh with last-successful-check time, improved reference rows and explicit accessible input labels. Filters, empty/error/unavailable results and login/logout are integrated into the main shell. Embedded home heading is h2; dedicated dashboard has one h1. No business metrics, record-content editing, real login or AI workflow invented.

## Connection and security boundary

The new /api/reference route accepts only dashboard and session login/logout/status. It verifies exact 127.0.0.1:3000 Host/Origin, rejects cross-site and caller Bearer headers, validates filters, denies unknown routes/methods and rejects duplicate/malformed cookies. Responses are no-store and backend failures return a generic unavailable result.

The server talks only to the retained synthetic B027 HTTPS API at https://127.0.0.1:3543, verifying hostname/certificate using its exported public CA at deployments/local-rehearsal/reference-dashboard-ca.pem. No system/browser trust change, private key export, insecure TLS skip or external target. Timeout and response-size limits are enforced. Existing B027 database/runtime permissions and fixed synthetic identity remain the authority.

Browser cookie cpa_reference_session is HttpOnly, SameSite=Strict, host-only and limited to /api/reference. Its non-Secure setting is limited to the explicitly HTTP loopback preview; this is not a hosted cookie configuration. Upstream uses its original Secure cookie through verified TLS. Cookie values and private responses are not exposed to JavaScript or error bodies. Only the public CA is stored with local configuration; no database passwords or server keys copied.

Repeated login with a valid session reuses it. An explicit login may replace only a session the upstream confirms is invalid; an upstream outage does not silently replace an existing session. Logout revokes server state before clearing the cookie; replay is denied. The shared legacy harness also checks an existing session after its 409 response and directs the user to retry after a confirmed invalid cookie is cleared. This improves the previously observed stale-cookie behavior without asserting the original B026-OBS-01 root cause or global closure.

The connection depends on the retained B027 rehearsal and its valid local certificate. If that service stops or its certificate expires/changes, the main dashboard fails closed with an unavailable result; do not bypass TLS or create a replacement database. Restore/review that exact local service and public-CA configuration. Existing B024/B025 resources remain separate.

## Verification

[Real main-API checks](main-dashboard-checks.json) passed all four groups: home/dashboard rendering, anonymous/origin/host/cross-site/method/route denial; scoped cookie and permitted stored queries; filter/empty/unavailable/malformed-query and duplicate-cookie cases; logout replay and stale-session recovery. Synthetic own sessions only; no fixture/schema edits.

The complete local runner exited 0 after final code changes: **79 source/config files, 70 backend tests, 5 runner tests**, dashboard contract and all three TypeScript projects passed. [Separate production build](main-dashboard-build.json) exited 0 with static home/dashboard and dynamic API route. The copy's active frontend source hashes match the working source, including final CSS. It uses a retained dependency junction to the existing installed packages, not a new dependency installation. Current dev/rehearsal build directories were not replaced. Dynamic planned-page generation excludes /dashboard to avoid conflicting with its actual page.

Actual browser on port 3000 verified: signed-out state; login with three permitted references; sidebar navigation to /dashboard preserving session; Dossiers quick view returning one; Clear filters restoring three; accessible Owner input validation with no count; reset/manual refresh; reload session restoration; logout removing records/updating header; re-login success. The earlier strict label selector issue is addressed with explicit htmlFor/id labels; current owner-field lookup worked.

Desktop 1440/1425 and mobile 390/375 viewport/document widths showed no horizontal overflow. Main controls are at least 44 px high on mobile and the dedicated page has one h1. [Desktop](main-dashboard-desktop.png), [mobile](main-dashboard-mobile.png). Screenshots visually inspected; an inherited reference-icon flex style was corrected and the final production copy rebuilt. No spoken-reader or independent code-review claim. Temporary viewport override reset; the dashboard is left open with the synthetic session active.

## Preservation

[Pre-change snapshot](main-dashboard-before.zip). Original backend status at port 8000 and all databases, volumes, backups and rehearsal services are retained. No cleanup, GitHub/cloud/model/source call or package installation. Application behavior changed only for the explicitly requested local frontend connection and shared reference component; backend permissions/business features unchanged. Historical reports describing the main frontend as disconnected are superseded by this dated connection record for this scope. All full-G1/real-identity/remote/independent-review deferrals persist.
