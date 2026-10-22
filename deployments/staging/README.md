# B023 — Staging preparation and deployment review

Date: 21 October 2026 (client date; Atlantic/Reykjavik). **Local preparation pack; not an executable deployment.** User selected B023 after accepting B022. No provider, account, domain, spend or external action has been approved by this pack. GitHub stays deferred.

## Review artifacts

- [Service/configuration manifest](review-manifest.json): provider-neutral review format, not Render/Terraform/Compose syntax and not consumed by a deployment tool.
- [Environment template](staging.env.example): empty sensitive values and disabled live AI. Current application does not load this file.
- [Validator](../../scripts/check_staging_draft.py): local structural checks; success means draft consistency only. `--require-ready` returns 2 because this draft cannot be deployed.
- [Evidence](../../docs/evidence/B023-staging-preparation.md), [decisions](../../decisions.md), [RCI-01](../../docs/planning/remote-ci-handoff.md).

## Proposed topology for review

Restricted HTTPS access → Next.js frontend and same-origin backend-for-frontend → private FastAPI API → separate private PostgreSQL database. A separately authorised migration job uses its own database role. Browser access to database credentials and direct public database access are excluded.

This continues the local stack as a candidate; it does not settle O-03 or accept ADR-001/003/004. Source D009 names Render, but no provider is selected here. No vendor compatibility or price claim is made. Choose the provider and target OS before producing its executable manifest and verifying its current documentation. Review geography, company account ownership, access restrictions, service availability, networking and backup capabilities then.

| Component | Available now | Staging requirement / current gap |
| --- | --- | --- |
| Frontend | Next.js local shell and disconnected dashboard | Portable production build/start and approved private API routing; current launcher explicitly requires Windows x64 and loopback port 3000 |
| API | FastAPI `app.main:app`, liveness and safe errors | Normal application has no configured database/session/dashboard composition; do not copy test routes into staging |
| Database | Versioned migrations and local synthetic verification | Separate staging database on persistent storage; selected version/size/region; TLS validation and separate migration/runtime credentials |
| Identity | Local synthetic session mechanics | Real identity provider and account verification unresolved; no usable callback or logout routes configured |
| Worker / queue | No durable job implementation | Disabled and unprovisioned; queue, concurrency, retries and idempotence remain O-05 / later work |
| AI / report storage | Mock adapter; no live transport or report store | Disabled and unprovisioned; no keys, buckets or paid calls needed for this pack |

`/health` proves only process liveness. It does not prove database connectivity, migration state, identity or dashboard readiness. A readiness route and acceptance probes must be implemented and tested before any staging-ready claim.

## Configuration and secret ownership worksheet

All values remain unset. `null` and empty strings mean unresolved, not automatic defaults. Justice is the nominated accountable technical owner, not an assumed secret custodian or billing authority.

| Item | Intended handling | Decision / evidence needed |
| --- | --- | --- |
| APP_ENV / LOG_LEVEL | Staging / INFO proposed; validate at boot | Environment loader and validation are not implemented |
| DATABASE_URL | API-only secret reference from company-managed secret store | Exact staging DB identity, TLS policy, least-privilege runtime role and named custodian |
| Migration connection | Separate migration-role secret, never browser/runtime role | Named executor, release window, migration ownership and grants |
| FRONTEND_ORIGIN | One exact HTTPS origin, scheme/host/port | Approved domain; no wildcard or localhost fallback |
| Private API origin | Server-side BFF configuration only | Provider network identity, port and authentication policy; new config key/composition to implement |
| Identity settings / AUTH_SECRET | Provider-specific settings only after decision | Exact callback/logout URLs, issuer/audience, secret owner and rotation/revocation method; do not invent AUTH_SECRET usage |
| OPENAI_API_KEY / model / cost ceiling | Empty, live transport disabled | Separate live-model/budget decision later; unknown cost is not zero |
| STORAGE_BUCKET | Empty, capability disabled | Private retrieval/retention policy later |
| Platform deployment credentials | Company account with approved least privilege | Operator/reviewer access and protected release process; never placed in this folder |

Never populate example files with credentials. Separate local/staging/production secrets, database roles and eventual API projects. Do not use retained B022 containers, tmpfs volumes, fixture passwords or synthetic session issuance as staging infrastructure. Record secret references and owners in operational records; never copy secret values into source, evidence or logs. A private environment file must not be created until ignore/packaging controls are established; no active root .gitignore was found during this review.

## CORS, redirects and browser sessions

The proposal uses a same-origin BFF, so browser cross-origin API requests are not enabled: the draft has an empty CORS allowlist and credentials disabled. These are review requirements, not applied configuration. If cross-origin browser access is later selected, approve exact HTTPS origins and credential behavior, test preflight and rejected origins, and implement that explicitly. Never use a wildcard with credentials.

Real sign-in remains disabled. Callback/logout allowlists stay empty until an identity provider and exact environment URLs are approved; an arbitrary redirect target must not be accepted. Staging cookies require Secure, HttpOnly and host-only scope plus approved SameSite/CSRF behavior. Strict is the local starting proposal, but validate provider redirect flows before adopting it for staging. The loopback B016 cookie has Secure=false and hard-coded local host/origin checks: it is test-only and must not be promoted unchanged. Backend authorization remains authoritative regardless of browser state.

## Capacity, cost and operations worksheet

Select actual plans only after a workload and budget decision. Estimate frontend/API/database compute, persistent storage, backups, logs/monitoring, build usage, egress, domain/DNS and taxes. Record quantity/unit price, region/currency, estimate date and official pricing source for each; then sum the recurring and usage-based totals and compare with an approved monthly ceiling. Worker/AI/report storage are excluded from initial provisioning, not assumed free. The manifest leaves every estimate blank; no price lookup was performed without a selected provider.

| Decision | Required outcome | Checkpoint |
| --- | --- | --- |
| Workload / sizing | Concurrent users, request volume, dataset size and performance objective; chosen frontend/API/DB plans | O-16 before executable manifest |
| Budget | Named billing owner, currency, monthly ceiling, usage alerts and response authority | O-16 before any paid action |
| Recovery | RPO/RTO, backup retention/location, restore isolation, approved drill | O-16/B025 before reliance on staging data |
| Logs / test data | Retention, redaction, access and user-approved deletion triggers | O-12/O-17 before persistent hosted data |
| Incident / rollback | Named operator, escalation contact/channel, decision authority and response coverage | O-17 before deployment |
| Technical review | Selected topology, secret/cross-origin/identity boundaries, target build proof | O-03/B005/B023 |
| Independent review | Eligible reviewer and recorded outcome | Existing gate/review requirements |

## Conditional deployment instructions — not commands to run now

1. Resolve the worksheet and record technical/provider/budget outcomes. Refresh provider documentation and pricing at selection time. B023 draft acceptance alone does not authorize B024 provisioning.
2. Implement and verify the identified normal-runtime gaps under separately selected work. Keep the normal API/frontend free of fixture issuance and test-only identities. Establish target-OS locked dependencies and production commands; the existing Windows launcher and local Python package inventory are not a portable staging build. Do not run development servers or the B022 harness as hosted services.
3. Produce the selected provider's manifest using reviewed service IDs, exact private connections, constrained ingress and secret references. Validate its schema with the appropriate provider tooling only when available/authorised. Define deployment artifact exclusions before upload: no private environment files, local environments/build caches, harnesses, evidence archives, retained database data or original handover materials. No upload package is produced here.
4. Resolve B004/RCI-01 and obtain explicit GitHub/release authority before any remote source or CI operation. Identify the reviewed release artifact/revision and the prior recoverable release. Local testing does not establish remote checks or branch protection.
5. Under explicit B024 provisioning/deployment authority and approved ceiling, verify company account permissions, create the isolated resources and configure secrets through the approved channel. Verify separate DB identity and private reachability before migration. Nothing in this pack performs this step.
6. Back up any nonempty staging database and test restoration to a separate approved destination before risky migrations. Run reviewed migrations once with the migration role, verify checksum/history and restart behavior, and revoke temporary privileges. The current migration helper is wired to loopback test credentials; a reviewed staging entry point is still required. Do not assume automatic down-migrations are safe.
7. Deploy the reviewed API/frontend artifacts using the selected platform commands. Confirm process liveness separately from readiness. Verify exact HTTPS origin, restricted access, Secure cookies, identity callbacks, CSRF checks and direct unauthorized-record denial independently of UI visibility.
8. B024/B026 record actual UI/API/DB integration and denial evidence; B025 records restore outcomes against agreed RPO/RTO; B027 covers setup/accessibility/operations; B028 evaluates G1. Keep unanswered criteria open. Staging is not production release approval.

## Rollback and incident preparation

Before deploying, nominate an operator and record last verified artifact, schema compatibility and recovery destination. On failed readiness or broken permissions, halt rollout and restrict access through the approved mechanism. Revert application artifact only if compatible with the current schema; otherwise use the reviewed restore/forward-repair plan. Never point local or staging code at production as a recovery shortcut. Preserve redacted failure evidence, notify through the authorised channel and document follow-up; no notifications or credential rotations are performed by this pack. No blanket migration rollback command is safe to invent.

## Local validation

From the project root:

```powershell
& .\backend\.venv312\Scripts\python.exe -B scripts/check_staging_draft.py
& .\backend\.venv312\Scripts\python.exe -B scripts/check_staging_draft.py --require-ready
```

Expected exits: 0 for a valid review draft; 2 for the readiness request; 1 for malformed or unsafe draft/template content. The validator is not a provider schema validator, credential scanner or deployment permission system. Actual readiness requires human review and execution evidence; editing a flag cannot create authorization.

References: [B023 work item](../../docs/planning/phase-1-work-items.md#b023), [ADR-003](../../docs/adr/003-environments.md), [D009](../../CPA_Development_Handover_Pack_v1/docs/009-deployment-operations-guide.md), [B006](../../docs/policies/allowed-data-and-test-fixtures.md). Earlier source deployment descriptions are proposals; current local-only instructions govern.


## B023 local preparation approved — 21 October 2026

User: “Approve B023”. The local staging preparation pack is accepted; B023 Done for that scope. Existing draft validation and eight rejection checks retained; no tests rerun for documentation-only acceptance. Earlier pending-review wording is superseded for local preparation. Provider, exact configuration, ownership/budget, target runtime integration and independent review remain unresolved before deployment. Manifest stays draft-not-deployable and deployment_authorized=false; no spending, secret population, GitHub, provisioning or B024 authority is inferred. B024 remains unstarted. Preview/database were left untouched. Prior records: docs/evidence/B023-before-acceptance.zip.
