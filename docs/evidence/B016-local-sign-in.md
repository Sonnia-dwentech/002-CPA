# B016 — Local sign-in/session and access-denied integration

**Date:** 20 October 2026 UTC  
**Status:** Done — user accepted the verified isolated local scope on 20 October 2026 UTC  
**Authority:** User “Start B016”, followed by “Approve isolated synthetic journey” and “Approve local cookie baseline”  
**Executor:** Codex; no independent review or real-identity assurance inferred

## Approved scope and delivered result

The user approved an isolated synthetic sign-in journey backed by actual PostgreSQL sessions/permissions and an HttpOnly, SameSite=Strict cookie with same-origin server forwarding and origin checks. This resolves the two local preparation blockers. No identity provider, real accounts, password/recovery system, downloads, GitHub or deployment was approved.

- [Shared session UI](../../frontend/components/SessionJourney.tsx): checking, unauthenticated, signed-in synthetic fixture, permitted record, concealed record denial, privileged denial, unavailable service and logout states. Previous protected content is removed while a request is pending. Results receive focus and a polite status announcement. Browser return-to-page triggers revalidation; every protected action is revalidated by the backend. No localStorage credential use.
- [Separate Next.js harness](../../frontend/harness/README.md): own application root and API routes on loopback port 3100, outside the normal app's route tree. The server forwards to a fixed loopback backend at port 8100; it does not accept arbitrary destinations or follow redirects. Exact Host/Origin checks, method restrictions, malformed/duplicate cookie rejection, no-store responses and no raw token responses to client JavaScript.
- Cookie: host-only `cpa_b016_session`, HttpOnly, SameSite=Strict, Path=/, maximum age 8 hours. Secure=false is solely the approved loopback HTTP test configuration. Future HTTPS deployment requires Secure cookies and separately verified controls. Backend idle/absolute expiry remains authoritative and is not extended by the cookie.
- [Runner and HTTP checks](../../backend/check_local_browser.py): reuses B012–B014 migrations, checks, SessionStore and AccessStore. A random server-only harness key protects fixed synthetic fixture issuance. No browser-selected identity or role. Existing 30-minute idle/8-hour absolute limits, revocation and privileged denial are retained.
- Normal frontend `/sign-in` explicitly says sign-in is unavailable and collects no credentials. Normal frontend API session/login routes and normal backend fixture/session/record routes are absent. Existing normal servers remain separate on ports 3000/8000.

## Executed verification

- `python -B -m unittest discover -s tests -v` from backend: **27 tests passed**.
- `python -B check_local_browser.py --serve`: actual disposable PostgreSQL, backend and Next.js server checks passed, then browser inspection performed and cleanup confirmed.
- Final `python -B check_local_browser.py` after duplicate-cookie rejection: **41 groups passed** (33 existing migration/access/session groups plus 8 B016 integration groups). Covers login/cookie attributes, own access, other-client 404, privileged 403, missing/malformed/duplicate credentials, direct API denial and spoofed headers, origin/method rejection, fixed protected fixture issuance, logout replay, idle/absolute expiry, membership revocation, unavailable validation, unconfirmed logout and normal-app route absence. Captured frontend logs contained no harness key or issued automated-test tokens.
- PostgreSQL **17.11**, existing local image `sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3`, `--pull=never`, loopback binding and tmpfs data. Both runs removed their disposable containers. Final checks confirmed ports 3100 and 8100 closed.
- Frontend `npm run typecheck`, strict harness TypeScript check and normal `npm run build` passed. Production build generated 15 static pages including `/sign-in`; no harness API routes appeared in the normal build. No new dependencies installed.
- In-app browser: synthetic login succeeded; keyboard Enter opened authorised fixture content. Other-client denial removed prior content and showed the generic unavailable message; privileged denial showed access denied. Results received focus. Keyboard logout showed revoked session and removed signed-in actions. [Denial screenshot](B016-denied.png).
- Narrow responsive browser check used a temporary same-origin 320px iframe. Document client/scroll widths were both 320px; controls wrapped without horizontal overflow. [Narrow screenshot](B016-narrow.png). Harness fixture HTML was removed. This is browser reflow evidence, not physical-device or full screen-reader certification.
- [Normal-app checks](B016-normal-app-checks.json): `/sign-in` HTTP 200 with unavailable wording; POST `/api/session/login` and GET `/api/session/status` both 404. Normal dev server restored after build. Temporary test tab closed.

The first automated run passed before duplicate-cookie validation was added; the complete final suite was rerun after that change. Initial read-only file probes used an incorrect working-directory prefix and were corrected; no test success is attributed to those failed reads.

## Preservation and acceptance

[Pre-implementation snapshot](B016-before-implementation.zip) and [input hashes](B016-input-hashes.json) preserve changed existing records/source. Original source pack, UI reference, migrations, backend permission/session implementations and build-order definitions remain unchanged. The existing disposable-check runner only adds B016 to its permitted task labels. No production database, real account, provider or remote repository was touched.

**Acceptance recorded — 20 October 2026 UTC:** User “Accept B016” accepts the approved isolated local browser/session/permission integration, retaining real human sign-in, provider integration, deployed cookie/TLS configuration, live MFA and formal independent reviews as deferred. The permitted synthetic journey and independent direct API denial have executed evidence. This is not completion of real human identity verification or unrestricted AC-F01-01 assurance.

B016 is Done. [Pre-acceptance snapshot](B016-before-acceptance.zip) preserves prior records. This acceptance changes documentation only; no code, runtime or database changes and no new tests. B017 is Not started. B004 remains Blocked and B005/B007 retain their existing review boundaries. To repeat browser review use the harness guide; the disposable harness is intentionally stopped after checks.

---

## Historical preparation — superseded by approvals and execution above

### Initial preparation

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B016”; existing local-only restrictions  
**Status:** Blocked for implementation pending the two local scope/transport decisions below  
**Executor:** Codex; Justice remains nominated technical authority

## Scope and dependency review

The unchanged build-order completion check is: **“Permitted sign-in journey works; direct API denial remains effective independently of the UI.”** See [build order](../../build-order.md), [work item](../planning/phase-1-work-items.md#b016) and F01/F02 in the [feature specification](../../feature-spec.md).

B015 is accepted and Done. B013 permissions and B014 opaque server-stored sessions are accepted for their local scopes. B014 explicitly deferred real human login, browser cookies/storage, sign-in UI and provider integration to a separately approved approach. O-04 remains partly resolved. Starting B016 selects the task; it does not select an identity provider or custom password/recovery system.

Local source inspection confirms:

- The normal FastAPI app exposes status, health and OpenAPI only. It has no login/session/record endpoints.
- `backend/app/sessions.py` validates persisted opaque Bearer sessions and delegates record permissions to B013. Missing store wiring fails closed. Session issuance is internal and requires verified identity; it must not become an unauthenticated normal-app login endpoint.
- B014's isolated test harness supplies actual PostgreSQL stores and synthetic identities; it tests direct HTTP denial independently of UI.
- The B015 shell currently shows “Not signed in” as static preview context. It reads no session and loads no protected records.
- No persistent application PostgreSQL destination is retained. Existing disposable-database tooling can support a separately approved local integration harness.

## Decisions requested

1. **Local scope:** approve a clearly labelled synthetic sign-in journey available only in an isolated local test harness, backed by actual PostgreSQL sessions and permissions. Real login remains unavailable in the normal app. Alternative: prepare the proposal only.
2. **Browser transport:** approve a same-origin server layer using an HttpOnly, SameSite=Strict cookie, server-side Bearer forwarding and origin checks on state-changing requests. No localStorage tokens. Loopback HTTP is test-only; future HTTPS deployment requires Secure cookies and separate deployment verification.

Both answers are pending. These questions are needed because the approved [B014 policy](../planning/B014-local-session-policy.md) explicitly leaves browser integration unapproved. Neither question grants GitHub, downloads, cloud/provider calls, real-account creation or live-client data use.

## Concrete implementation proposal

After approval, keep synthetic identity issuance in a separate test harness, absent from normal application routes and startup. Do not add a normal-app mock-login toggle or trust a browser-supplied user/role/client header. Use disposable synthetic accounts and records with the existing approved matrix; no new business grants.

Use a same-origin server boundary to keep credentials out of client JavaScript. Forward only the required credential to a fixed trusted loopback backend, with no arbitrary proxy destination. Do not follow backend redirects or expose backend token responses to the browser. Protect state-changing requests with exact origin checks; use POST for login/logout, no-store responses and a host-only cookie. Do not introduce wildcard CORS.

The UI should distinguish unauthenticated, authenticated synthetic fixture, session expired/revoked, access denied/not found, and service unavailable. Do not render restricted content before permission checks. Preserve B013's 403/404 disclosure rules. Use a fixed internal return path rather than accepting arbitrary redirects. A service outage must not appear as successful logout or a signed-in fallback.

Keep B014's 30-minute idle and 8-hour absolute expiry, no refresh and immediate revocation semantics. Browser cookie lifetime must not extend backend lifetime. Logout should revoke the current backend session and clear the local cookie; expiry/revocation must remove protected UI state. Privileged operations remain denied pending MFA.

## Planned verification — not executed

- Run existing backend contract, permissions and session checks as relevant to changed code.
- Exercise actual browser → same-origin server → backend → disposable PostgreSQL session/permission flow.
- Verify valid synthetic sign-in and permitted synthetic record access, logout/replay, expired/revoked session and disabled membership.
- Verify direct API calls without credentials, with malformed credentials and with another client's valid session fail independently of UI visibility.
- Verify 403/404 states disclose no restricted record title/content; 503 shows unavailable, not empty or authenticated success.
- Check cookie attributes, no raw credential in HTML/client state/URLs/logs, origin rejection, safe return navigation and no normal-app synthetic issuance endpoint.
- Check keyboard focus and responsive sign-in/denial states; compile/typecheck the frontend.
- Clean up disposable database/server fixtures and record actual results and limitations.

## Acceptance and boundary

No B016 acceptance check has passed. A synthetic journey would establish local browser/session/permission integration only; it cannot prove real human identity verification. Acceptance of that limited deliverable would need to state its local scope explicitly, with real sign-in and full AC-F01-01 assurance deferred.

[Pre-edit snapshot](B016-before.zip) preserves the tracker and documentation index. No application source, dependencies, running service or database changed during preparation. B004 remains Blocked; B005/B007 retain their review boundaries. B017 is Not started.
