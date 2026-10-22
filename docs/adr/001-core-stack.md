# ADR-001 — Frontend, API and database boundary

**Updated:** 21 October 2026 (Atlantic/Reykjavik)  
**Status:** Accepted for the local synthetic baseline; listed deferrals remain binding  
**Prepared by:** Codex under the user's B005 selection  
**Decision owner:** Justice; product owner also required for business permissions  
**Approval/date:** 21 October 2026 (Atlantic/Reykjavik); user confirms Justice approval: “Justice approves the four local ADR decisions and listed deferrals”. See [acceptance record](../evidence/B005-local-architecture-acceptance.md).

This revision replaces the 20 October proposal's descriptions of unbuilt local work. The original is preserved in [the pre-review snapshot](../evidence/B005-before-current-review.zip). Tested implementation is evidence for review, not retrospective technical approval. No remote alignment is claimed.

## Accepted local decision

Retain Next.js/TypeScript and React for the UI, FastAPI/Python for application services, and PostgreSQL for relational persistence. Retain the current checked, numbered SQL migration runner for the local baseline. The backend owns identity verification, permission decisions and data access; the frontend's server bridge transports only the explicitly allowed dashboard/session requests. The browser receives no database or provider credentials.

## Options, rationale and consequences

| Option | Rationale / trade-off | Recommended outcome |
| --- | --- | --- |
| Retain the separate UI/API/PostgreSQL stack | Existing local contracts, migrations, access/session checks and browser journey provide concrete evidence; two runtimes require coordinated configuration and contract checks | Select for the local baseline |
| Consolidate into one application runtime | Could reduce runtime boundaries, but requires rewriting the tested Python application boundary without a demonstrated local need | Do not select now; reconsider on evidence |
| Replace PostgreSQL | Requires new concurrency, schema, isolation and recovery evidence; no unmet local requirement is recorded | Do not select now |
| Retain checked SQL migrations vs adopt a migration framework | Current runner hashes applied migrations, validates history order and applies pending migrations transactionally under an advisory lock; it requires transaction-compatible SQL and deliberate review | Retain locally; reassess before non-transactional or complex hosted migrations |

These are architectural judgments from local code and checks, not performance or vendor comparisons. Version pins in [frontend package.json](../../frontend/package.json) and [Python local requirements](../../backend/requirements-local.txt) describe the tested setup; accepting this decision would not freeze them indefinitely or certify hosted compatibility.

## As built and evidence

- [Migration runner](../../backend/app/database.py) and [B012 checks](../evidence/B012-local-database.md) provide apply/reapply and failure evidence.
- [Access policy](../../backend/app/access.py) owns application checks. [Main dashboard evidence](../evidence/main-dashboard-connection.md) records the UI/server bridge to the retained B027 synthetic HTTPS service, production build and browser checks.
- The normal API on port 8000 exposes liveness; it is not the synthetic reference API. The working dashboard depends on the separate local rehearsal on 3543, through the server bridge on 3000. This is not a self-contained production composition.

## Deliberate deferrals and checkpoints

Justice must review normal-runtime composition, version/support compatibility and configuration before any hosted staging or release. The B027 fresh-setup evidence predates the main dashboard bridge; the later production build is separate evidence, not a repeated fresh-machine setup. Hosting, database service, costs and remote repository compatibility remain deferred under ADR-003/B004. No replacement stack or provider is selected by assumption.

[Decision summary](../evidence/B005-current-architecture-review.md) · [ADR-002](002-identity-roles-tenancy.md) · [ADR-003](003-environments.md)
