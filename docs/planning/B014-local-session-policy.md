# B014 — Proposed Local Session Policy

**Version:** 0.1 — user-approved local baseline  
**Date:** 20 October 2026 UTC  
**Status:** User approved this local baseline on 20 October 2026 UTC; executed local implementation accepted; B014 Done  
**Purpose:** Give B014 a concrete local backend validation approach after accepted B013

## Approval recorded — 20 October 2026 UTC

User answered “Approve this local baseline” to the explicit session-policy question. This adopts the opaque bearer session, 30-minute idle/8-hour absolute expiry, no-refresh, current-state revocation and privileged-denial baseline for local synthetic implementation. The proposal text below preserves the approved detail; its earlier pending-approval statements are historical. [Execution evidence](../evidence/B014-local-authentication.md) records actual checks and limits. Provider integration, real login/browser storage and live MFA remain excluded.

## Proposed decision

Implement server-stored opaque bearer sessions for the local backend, tested with synthetic users in disposable PostgreSQL. Validate real random session credentials against stored hashes and session state. Do not select an external identity provider or implement passwords, invitation redemption or account recovery in this step.

The user has been asked to approve this baseline or request changes. The exact durations below are proposals for this project, not values already approved or claims of universal security requirements.

| Area | Proposed rule |
| --- | --- |
| Credential | Cryptographically random opaque token with 32 bytes of entropy; store only its SHA-256 digest. Never accept user/role/client IDs as a credential. |
| Transport | Exactly one `Authorization: Bearer <token>` header. No credentials in URL/query/body, cookies or logs. Reject malformed or ambiguous credentials. |
| Identity | Session maps to the existing B013 application user. Check enabled account, active membership and current permissions from server state; never create an account merely because a token is presented. |
| Absolute expiry | Eight hours from issuance. Authenticated activity never extends it. |
| Idle expiry | Thirty minutes since issuance or last successful validation. An authenticated request may update activity, subject to the absolute limit. |
| Boundary times | Expired when current server time is equal to or later than either deadline. Use UTC server/database time. No grace period. |
| Refresh | No refresh tokens or automatic renewal in this local baseline. Expiry requires a new approved sign-in flow, which is not yet implemented. |
| Logout | Revoke the presented session; subsequent replay fails. No implicit logout of every other session. |
| Account/session revocation | Validate stored revocation on every request. Account suspension or removal of membership denies every associated session. Reactivation must not silently resurrect revoked sessions. |
| Permission changes | B013 continues rechecking grants and assignments; no cached role claims in the credential. |
| MFA | No MFA bypass or invented assurance. Access administration, grant changes, response publication and commercial/investment decisions remain denied through the authentication boundary until an approved MFA integration is available. Existing feature-unavailability gates remain in force. |
| Failures | Generic 401 for missing/malformed/unknown/expired/revoked credential or inactive identity; generic 503 if validation storage is unavailable; no protected content in either case. Then use B013's approved 403/404 rules for resource authorisation. |
| Browser | No browser token persistence, cookie-based login, CORS expansion or sign-in UI in this step. B016 must approve the browser integration; do not treat this proposal as approval to store tokens in localStorage. |

## Why this is a bounded local option

Installed psycopg and PostgreSQL can provide the required persisted session validation and revocation checks. Python's standard library supplies random-token and hashing primitives; no new package is needed for this approach.

Local package metadata inspection found no PyJWT, cryptography or Authlib in the default Python environment. That is a tooling observation, not a reason to invent a signed-token verifier. Existing itsdangerous/Argon2 packages do not select an account/password design. External identity integration remains a separate decision.

Opaque sessions require server-side storage and a lookup for each request. They do not establish that a human successfully signed in. A later approved identity integration must authenticate the human before issuing a session. The local test harness can create synthetic sessions; the application must have no unauthenticated token-minting route or mock-login flag.

## Implementation boundary if approved

1. Add a new versioned migration for session digest, user reference, issuance/activity timestamps, fixed absolute deadline and revocation state. Preserve migrations 0001–0002.
2. Implement a session validator and a FastAPI authentication dependency. Link verified session state to B013 and keep credentials out of error responses.
3. Verify behaviour through a protected test-only route plus the actual dependency. Normal public health stays unchanged. No public business endpoint or real login is added by the test harness.
4. Implement logout/revocation semantics at the service boundary. Test replay and disabled identities without inventing an administrator or real-account bootstrap.
5. Prevent privileged operations until MFA is configured. Do not count blocked MFA as verified multi-factor authentication.

Any issuance helper is a server-internal interface only, callable after a later approved identity verification; the tests use synthetic identities exclusively. Revocation and expiry must be tested against actual PostgreSQL state, not solely mocked return values.

## Verification required before acceptance

- Valid synthetic session reaches an authorised B013 record through the backend dependency.
- Missing, malformed, duplicate, unknown, expired and revoked credentials cannot obtain protected responses.
- Idle and absolute expiry are tested immediately before and at their boundaries; activity cannot extend absolute lifetime.
- Logout replay fails; account suspension/membership removal denies access; restoration cannot revive a revoked session.
- Forged role/client/user headers do not alter identity or grants.
- A valid session cannot access another owner's/client's record.
- Required-MFA actions remain denied even with a valid session.
- Validation database failure returns the approved generic failure and never bypasses authentication.
- Raw tokens are absent from persisted session rows, returned error bodies and captured application diagnostics.
- Existing API/permission checks and migration recovery checks still pass; disposable containers and data are cleaned up.

All checks are planned. None has run for B014.

## Approval and remaining boundaries

**Decision requested:** Approve this local baseline, amend the policy, or select a real identity approach first.

Approval would select the local backend session policy for implementation. It would not approve an identity provider, real-account enrolment, password/recovery system, browser credential handling, live MFA, real-client data, GitHub, downloads, installations or deployment.

B014's unchanged backend criterion requires actual invalid/expired-credential rejection. Full AC-F01-01 also includes the sign-in interface, which remains B016 work. Evidence must state that distinction; successful synthetic local tests cannot be presented as an end-to-end real sign-in demonstration.

Until this policy is approved, B014 remains Blocked. B013 is Done; B015 remains unstarted.

## Executed deliverable accepted — 20 October 2026 UTC

User: “Approve B014”. Local backend implementation and its verification evidence accepted. Earlier pending-acceptance statements are historical; B014 is Done for this local scope. All provider, real sign-in, browser and live-MFA exclusions above remain in force. B015 remains unstarted.
