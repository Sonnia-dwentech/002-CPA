# ADR-002 — Application identity, roles and tenancy

**Updated:** 21 October 2026 (Atlantic/Reykjavik)  
**Status:** Accepted for the local synthetic baseline; listed deferrals remain binding  
**Prepared by:** Codex under the user's B005 selection  
**Decision owner:** Justice; product owner also required for business permissions  
**Approval/date:** 21 October 2026 (Atlantic/Reykjavik); user confirms Justice approval: “Justice approves the four local ADR decisions and listed deferrals”. See [acceptance record](../evidence/B005-local-architecture-acceptance.md).

This revision replaces the 20 October proposal's descriptions of unbuilt local work. The original is preserved in [the pre-review snapshot](../evidence/B005-before-current-review.zip). Tested implementation is evidence for review, not retrospective technical approval. No remote alignment is claimed.

## Accepted local decision

Retain the user-approved [B013 matrix v0.1](../planning/B013-recommended-access-matrix.md), [B014 session policy](../planning/B014-local-session-policy.md), and shared-schema PostgreSQL with application-enforced record/client scope for synthetic local use. Deny access by default and load authoritative membership/grants from storage for each protected operation. Business permissions remain those already approved for this synthetic slice; technical acceptance creates no new real-account grants.

## Options, rationale and consequences

| Option | Rationale / trade-off | Recommended outcome |
| --- | --- | --- |
| Synthetic fixture identity and opaque server-side sessions | Supports repeatable positive/negative checks without managing human passwords; cannot establish a real person's identity | Select for the local baseline only |
| Managed identity vs application-managed credentials | Either requires enrolment, recovery, MFA, contracts, support and integration decisions absent from this fixture | Deliberately defer provider/real identity choice |
| Shared schema with application checks | Matches the tested permission model and common migrations; every API, query, worker and output path must enforce scope | Select locally; no database-level tenant isolation claim |
| Database row policies or separate client schemas/databases | Additional storage boundaries need policy/bypass/migration/recovery design and tests | Defer the real-client tenancy choice before affected implementation |

## As built and evidence

[B013](../evidence/B013-local-authorisation.md), [B014](../evidence/B014-local-authentication.md) and the [connected dashboard](../evidence/main-dashboard-connection.md) cover synthetic permission/session boundaries. Backend sessions use opaque random tokens stored as hashes, 30-minute idle and 8-hour absolute expiry, revocation checks and privileged denial pending MFA. CEO/technical roles do not imply unrestricted record access. Client category/ownership/assignment and approval separation remain explicit.

The rehearsal runtime database role can SELECT all CPA tables. There are no database row policies protecting tenants. Application filtering is therefore essential; hiding UI entries is insufficient. Future writes, exports, jobs and files need their own checked enforcement paths.

The main loopback HTTP dashboard uses an HttpOnly, SameSite=Strict, host-only cookie scoped to /api/reference; Secure is false for that explicit HTTP origin. Its bridge uses certificate-validated HTTPS to the local rehearsal. This local exception is not an internet cookie/TLS policy or a real sign-in system.

## Deliberate deferrals and checkpoints

Justice and the product owner must decide real identity, enrolment/recovery, MFA, final business grants, tenant isolation and named access before real users/client data or affected shared/client workflows. B006 policy and independent review remain separate. No identity vendor, named user, live MFA or client portal is approved here. Access-store and session test success does not establish all F01 paths or compliance.

[Decision summary](../evidence/B005-current-architecture-review.md) · [ADR-001](001-core-stack.md) · [ADR-004](004-service-boundaries.md)
