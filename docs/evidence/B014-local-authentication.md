# B014 — Local Authentication and Session Preparation

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B014”, under G0-L and existing local-only restrictions  
**Status:** Done — user approved the verified local backend deliverable on 20 October 2026 UTC  
**Executor:** Codex; Justice remains nominated technical authority

## Acceptance recorded — 20 October 2026 UTC

User: “Approve B014”. Marked B014 Done for the approved, executed local backend session-validation scope under G0-L. Retained evidence of 26 unit/API tests and 33 PostgreSQL/HTTP verification groups. This acceptance updates documentation only; no code changed or tests rerun.

Real human login, identity-provider integration, browser sign-in/storage, live MFA, named-account bootstrap and deployment remain deferred. Privileged operations remain denied pending MFA. The sign-in interface portion of AC-F01-01 remains B016 work. No formal independent/specialist sign-off is inferred and B015 is not started.

[Pre-acceptance snapshot](B014-before-acceptance.zip) preserves the previous records. Earlier In review/Blocked statements below are historical; this acceptance governs current B014 status.

## Current approved implementation — 20 October 2026 UTC

User answered “Approve this local baseline” to the explicit policy question. [Session policy v0.1](../planning/B014-local-session-policy.md) is adopted for local synthetic implementation. B013 is accepted. Earlier blocked/pending entries below describe historical preparation snapshots, not current authority.

### Delivered

- [Migration 0003](../../backend/migrations/0003_local_sessions.sql): hashed session references, fixed expiry/activity and revocation; trigger invalidation on disabled account, removed membership or changed identity/scope. No previous migration edited.
- [Session service and HTTP dependencies](../../backend/app/sessions.py): 32-byte opaque tokens stored as SHA-256 digests; exact Bearer parsing; 30-minute idle and 8-hour absolute expiry; no refresh; current account checks; logout/revocation; B013 record integration and fail-closed privileged actions pending MFA.
- [Unit checks](../../backend/tests/test_sessions.py), [database/HTTP integration checks](../../backend/check_local_sessions.py), [run guide/fixture manifest](../../backend/README.md). The existing API error handler now supplies a constant Bearer challenge on 401 responses. The ASGI test helper accepts explicit test headers; existing API contract tests still pass.

### Actual results

Run from the backend directory:

- `python -B -m unittest discover -s tests -v`: **26 tests passed** (existing 21 plus 5 session contract tests). Exact idle/absolute expiry boundaries are checked at equality and just before expiry.
- `python -B check_local_sessions.py`: **33 verification groups passed**: 9 migration/recovery, 10 persisted B013 permission, 14 session/HTTP. Actual PostgreSQL rejects expired/revoked sessions; validation links real stored sessions to B013 protected references. Tests cover tampered/unknown/malformed/ambiguous credentials, query/cookie rejection, no absolute extension, future timestamps, logout replay, inactive/restored accounts, cross-client access, spoofed role/MFA headers, missing MFA, storage outage and no raw credentials in session rows/captured diagnostics.
- An actual loopback HTTP server returned 401 without credentials and 200 for a valid synthetic session; it was stopped and joined after checks. Missing credentials received the Bearer challenge and no-store response. Protected test-only routes were used; the normal application routes remain unchanged.
- PostgreSQL **17.11**, psycopg **3.3.6**, installed offline image `sha256:2d2b8998d31037bf721cfdf764d76ba74171b4fab3431b7f72c27c56ddbdf9e3`. Elevated execution was required for local Docker named-pipe access. Every run used a new disposable container with loopback port and tmpfs data; cleanup confirmed removal. No pull/install, GitHub or provider operation occurred.

An initial unit-test invocation from the project root failed because `app` was not importable from that working directory; no check passed from that invocation. Rerunning the documented command from backend passed. After adding the HTTP challenge/tampered-token/MFA-spoof checks, both final suites were rerun and passed as reported above.

### Scope, acceptance and remaining work

B014 is **In review**, ready for acceptance of this approved local backend session-validation scope. Invalid/expired credentials cannot obtain the exercised protected responses. The tests exercise actual session hashes, database state and HTTP processing rather than a validator stub that simply returns a chosen actor.

No real human login, identity provider, password/recovery flow, browser storage, live MFA or named-account bootstrap is delivered. Privileged access is denied; that is not a claim of successful MFA verification. The normal app exposes no session-minting/mock-login route. A future approved identity adapter must verify the human before using the internal issuance interface; future routes must supply trusted request-scoped database connections and enforce the session/record dependencies. Public health remains liveness only.

The sign-in interface part of AC-F01-01 remains B016 work; it has not been demonstrated here. Full-stack readiness, deployed roles/TLS, session-retention cleanup, provider integration and concurrency/load assurance remain separate future work. Formal specialist/independent review and shared integration/deployment approvals remain deferred under G0-L. B015 was not started.

[Pre-implementation snapshot](B014-before-implementation.zip) and [input hashes](B014-implementation-input-hashes.json) preserve prior state. Original source material, migrations 0001–0002 and B013 policy implementation remain unchanged. No persistent application database was retained. The existing startup test regenerated the ignored `backend/app/__pycache__/main.cpython-314.pyc` cache after the API error-handler change; this generated file is the only additional pre-existing file changed beyond the documented source/navigation records.

## Scope and dependency findings

[B014](../../build-order.md) requires approved backend authentication/session validation. Its unchanged completion check is: “AC-F01-01 passes; invalid/expired credentials cannot obtain protected responses.”

The [work item](../planning/phase-1-work-items.md#b014) depends on B013 and decisions about identity/session validation, expiry/revocation and privileged MFA. B012 is accepted and Done. B013's [recommended matrix](../planning/B013-recommended-access-matrix.md) is proposed, not approved. [O-04](../../decisions.md#o-04) and [ADR-002](../adr/002-identity-roles-tenancy.md) leave the identity approach and session policy open.

The user selected B014, permitting this independent local preparation. That selection does not approve the B013 matrix, choose an identity provider or authorise external identity calls. No authentication implementation, account creation, credential generation or new database work occurred. B015 remains unstarted.

## Decisions Justice needs to record

| Decision | Concrete outcome required | Current state |
| --- | --- | --- |
| B013 policy and user-reference boundary | Approve/amend identity mapping, membership, enabled status and access rules; record applicable B006 review | Awaiting review of access matrix v0.1 |
| Identity approach | Managed identity integration or application-managed identity; selected authority and account lifecycle | Unselected; no vendor or custom password/recovery system adopted |
| Credential validation | Accepted credential type and transport, trusted issuer/audience or server session lookup, validation configuration and failure handling | Unselected; request headers cannot supply trusted user/role/client fields |
| Session lifetime | Exact idle/absolute expiry policy, refresh/rotation behaviour, clock handling and reauthentication requirements | Unset; no invented durations |
| Logout and revocation | Which sessions logout ends; effect of account suspension, membership removal and password/security changes | B013 proposes current-state checks; implementation policy unapproved |
| Privileged MFA | Which actions/roles require MFA, how assurance is verified and when fresh authentication is needed | Unselected; GitHub MFA is not application MFA |
| Browser/session protections | Cookie or bearer approach, applicable request-forgery protection, allowed origins and local-to-deployed differences | Unselected; no wildcard origins or browser credential storage chosen |
| Failure and disclosure contract | Public status/error behaviour for invalid credentials and unavailable validation; safe diagnostics | Proposal below; technical approval needed |
| Local verification boundary | Isolated synthetic validator fixtures and a protected test-only route; later actual identity integration evidence | Proposed; no mock login added to the application |

These decisions can be reviewed without GitHub. If the selected implementation needs downloads, new packages, external discovery/key retrieval or provider accounts, identify that requirement separately before proceeding. Local-only does not silently permit those operations.

## Proposed backend boundary for review

Keep credential verification distinct from record authorisation:

1. A validator accepts only the approved credential form. It validates the credential using the approved method before creating any trusted identity context.
2. Resolve the verified identity to the B013 application user reference and check that the account and required membership remain active.
3. Pass a minimal trusted context to B013's permission evaluator. Successful authentication alone never grants access to a resource.
4. Enforce the boundary on protected requests regardless of UI state. Public B011 `/health` remains process liveness and cannot be used as proof that protected requests are authenticated.
5. Invalid, expired, revoked or unverifiable credentials never return protected content. Validation infrastructure failure must fail closed; there is no fallback actor or administrator.
6. Never log or echo credential values, identity-provider secrets or submitted private payloads. The approved application logging policy governs diagnostic events.

Proposed public response distinction: generic 401 for missing/invalid/expired/revoked credentials; generic 503 when the selected validation dependency is unavailable, with no protected response; apply B013's approved 403/404 rules only after successful authentication. This is a proposed contract, not existing behaviour or a claimed vendor capability.

The actual adapter must follow the selected method's complete verification rules. A session lookup and a signed-token verifier are alternatives, not interchangeable pseudovalidation. Do not implement a stub that accepts any token, a debug login, a trusted user-ID header or a mock validator accessible through normal application configuration.

## Local preparation versus execution

This report prepares the contract and test cases independently of B013. Implementation of identity-to-user mapping and account/membership checks needs B013's approved references and rules. Full authentication-to-record enforcement needs its implemented policy boundary.

After task-level approval, isolated test fixtures may exercise denial and context-mapping behaviour without contacting a provider. Fixtures must be available only through the test harness; the normal app must not expose a switch to authenticate as an arbitrary user.

Mocked tests alone cannot establish real signature verification, session revocation, MFA or provider integration. Record any selected-method checks separately and do not mark the unchanged acceptance criteria passed from mocks alone.

## Planned verification — none executed

| Case | Required evidence after the contract is approved |
| --- | --- |
| Missing credential | Protected request denied; response contains no protected data |
| Malformed, wrong-type or tampered credential | Denied before trusted identity context is produced |
| Wrong issuer/audience/key or unknown session, as applicable | Denied by the selected validation method |
| Expired or not-yet-valid credential, as applicable | Boundary cases checked against the approved time rules |
| Revoked credential/session or disabled account | Denied despite a previously successful sign-in |
| Valid credential with unmapped user | Denied; no automatic privileged account creation |
| Valid, mapped, active user | Correct trusted context, followed by B013 record permission checks |
| Forged role/client/user fields | No privilege or membership change |
| Privileged action without required MFA assurance | Denied or requires the approved reauthentication path |
| Validation dependency unavailable | Fail closed; generic approved failure response |
| Refresh/logout replay | Behaviour matches the approved invalidation/rotation policy |
| Credential/error canaries | No token/private payload exposed through responses or diagnostic output |
| Direct API request bypasses UI | Same authentication and permission enforcement |

Fixture requirements: wholly synthetic identities and non-live credentials; manifest recording the selected method, schema, version, creator, expected outcomes, isolated storage and cleanup. Use test-generated signing keys only if that method is selected. No real sessions or client data. No fixtures or persistent stores were created in this preparation.

AC-F01-01 also mentions the approved sign-in interface. Backend denial belongs here; the sign-in/access-denied UI is integrated at B016. Backend checks cannot claim that future UI journey passed. The final acceptance record must state this component boundary explicitly.

## Completion path and preservation

1. Record Justice's B013 matrix decision and relevant technical review.
2. Record B014's identity/session/MFA choices above.
3. Implement the approved backend adapter and user-policy integration using an authorised local test destination.
4. Run actual selected-method validation and negative tests, then review evidence against the unchanged B014 completion check.

B014 is started but Blocked for implementation. No requirement is waived and no task is marked Done by this preparation. B013 remains Blocked; B012 remains Done; B015 is not started.

[Pre-edit snapshot](B014-before.zip) and [input hashes](B014-input-hashes.json) preserve existing records. Only progress.md and the documentation index change; this report and preservation files are new. Existing code, source documents, prior evidence and task definitions remain unchanged. No GitHub, installs, external services or database execution occurred.

## B013 continuation update — 20 October 2026 UTC

User approved the B013 matrix for local continuation. Its core boundary and persisted references were implemented and tested; [B013](B013-local-authorisation.md) is now In review pending acceptance. This supersedes the earlier statement that the access matrix lacks user approval for local work. B014 remains Blocked by its unselected identity/session validation, expiry/revocation and MFA choices, plus B013 acceptance. No B014 code or live authentication implemented. Formal B006/independent review and named real-account assignments remain deferred prerequisites for affected operation.

## B013 acceptance update — 20 October 2026 UTC

User accepted B013's verified local deliverable. B013 is Done; its local acceptance dependency is satisfied. B014 remains Blocked by its own identity/session validation, expiry/revocation and privileged MFA choices. Earlier references to pending B013 acceptance are historical. No B014 implementation, provider connection or B015 work occurred in this update.

## Concrete session-policy proposal — 20 October 2026 UTC

User: “Let's fix B014”. B013 is accepted. Prepared [local session policy v0.1](../planning/B014-local-session-policy.md) to resolve the remaining implementation choices: server-stored opaque bearer sessions, proposed 30-minute idle/8-hour absolute expiry, no refresh, current-state revocation, and privileged actions denied pending MFA. Asked the user to approve the baseline, change it or choose a real identity approach first; decision remains pending.

Default Python metadata showed psycopg available; PyJWT, cryptography and Authlib absent; itsdangerous 2.2.0 and argon2-cffi 25.1.0 present. No package installed or external service consulted. The proposal does not select those libraries for a password or signed-token system.

B014 remains Blocked pending the policy decision. No session schema/code/credentials created and no authentication check claimed passed. [Pre-proposal snapshot](B014-before-session-proposal.zip) and [input hashes](B014-session-proposal-input-hashes.json) preserve the starting state.
