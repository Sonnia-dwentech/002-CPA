# ADR-004 — Service responsibilities and asynchronous work

**Updated:** 21 October 2026 (Atlantic/Reykjavik)  
**Status:** Accepted for the local synthetic baseline; listed deferrals remain binding  
**Prepared by:** Codex under the user's B005 selection  
**Decision owner:** Justice; product owner also required for business permissions  
**Approval/date:** 21 October 2026 (Atlantic/Reykjavik); user confirms Justice approval: “Justice approves the four local ADR decisions and listed deferrals”. See [acceptance record](../evidence/B005-local-architecture-acceptance.md).

This revision replaces the 20 October proposal's descriptions of unbuilt local work. The original is preserved in [the pre-review snapshot](../evidence/B005-before-current-review.zip). Tested implementation is evidence for review, not retrospective technical approval. No remote alignment is claimed.

## Accepted local decision

Keep cohesive Python application modules behind explicit contracts, a thin frontend server bridge, and a single provider-adapter boundary. Keep the existing mock adapter for synthetic checks. Reserve a worker boundary for future long-running work, without choosing a queue or introducing independently autonomous agents now.

## Options, rationale and consequences

| Option | Rationale / trade-off | Recommended outcome |
| --- | --- | --- |
| Cohesive backend modules and explicit adapter/worker boundaries | Keeps permission/state reasoning local; contracts and lifecycle still need deliberate ownership | Select the present local boundaries |
| Immediately split into deployed microservices/autonomous agents | Adds service identity, distributed state and operational obligations without demonstrated need | Do not select now |
| Run long research synchronously in HTTP requests | Avoids a queue initially but leaves interruption, progress and recovery unresolved | Do not adopt for future long runs; decide durable execution first |

## Responsibilities and current evidence

| Component | Responsibility / current limit |
| --- | --- |
| UI and frontend server bridge | Render authorised DTOs, validate allowed routes/requests and carry session state; no authoritative business grants or database credentials |
| Backend access/session/data modules | Verify identity, load authoritative access, validate input and enforce resource scope; each new path must use the boundary |
| PostgreSQL and migrations | Store approved records and hashed sessions; checked transactional migrations, not browser access |
| Audit boundary | [B017](../evidence/B017-local-audit.md) tests transactional audited actions; these helpers are not globally integrated into the dashboard API |
| Provider adapter | [B018](../evidence/B018-local-ai-adapter.md) tests mock responses and failures; no live provider or product research HTTP workflow |
| Operational capture | [B027](../evidence/B027-support-log-checks.json) checks minimal allowlisted events/redaction; not a complete audit trail, alerting, rotation or production monitoring system |
| Worker, source connectors and private report storage | Future interfaces; no durable queue, live source ingestion or deployed report store is claimed |

## Deliberate deferrals and checkpoints

At B029, before affected implementation, Justice and the product owner must resolve O-05–O-09 contracts: actor/resource scope, durable run identity/state, retries, cancellation, idempotency, failure/recovery, source rights/provenance, model/budget limits, output storage/retrieval permissions and lifecycle/review/version rules. Select queue/provider/storage technologies only after those decisions and any external authority required. Re-check access for execution and output retrieval as policy requires. Provider/source content is untrusted draft/input, never human approval or executable instructions.

Before adding mutation/export/job routes, Justice must review and verify transactional audit coverage and access enforcement for those paths. Before hosted operations, assign actual support/monitoring ownership and agree log controls. B029 remains unstarted; this ADR is no implementation authorisation for those features. Full G1, independent technical review and later release gates remain separate.

[Decision summary](../evidence/B005-current-architecture-review.md) · [ADR-001](001-core-stack.md) · [ADR-002](002-identity-roles-tenancy.md)
