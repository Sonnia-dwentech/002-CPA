# B005 Architecture Review Pack

**Version:** 0.4 · **Updated:** 21 October 2026 (Atlantic/Reykjavik)  
**Current state:** Accepted local architecture; user confirmed Justice approval on 21 October 2026

Start with the [current decision summary](../evidence/B005-current-architecture-review.md): four concrete selections, their trade-offs, evidence and nine deliberate deferrals with authorities/checkpoints. The four ADR files now describe the implemented synthetic foundation. User confirmed Justice approves the four decisions and listed deferrals. See the [acceptance record](../evidence/B005-local-architecture-acceptance.md).

| ADR | Accepted local decision | State |
| --- | --- | --- |
| [ADR-001](001-core-stack.md) | Retain local Next.js/FastAPI/PostgreSQL and checked SQL migrations | Accepted locally |
| [ADR-002](002-identity-roles-tenancy.md) | Retain approved synthetic sessions/grants and application-scoped shared schema | Accepted locally |
| [ADR-003](003-environments.md) | Retain isolated local environments; require separated hosted environments later | Accepted locally |
| [ADR-004](004-service-boundaries.md) | Retain cohesive modules, thin bridge/mock adapter; defer durable worker technology | Accepted locally |

## Historical review index — 20 October 2026

The following record describes the initial preparation, before later local build approvals. Its stop-before-B006 and unbuilt-work statements are historical; current authority and status are in the summary and progress tracker. Original ADR text is preserved in the [snapshot](../evidence/B005-before-current-review.zip).

# B005 Local Architecture Review Pack

**Version:** 0.2 draft · **Date:** 20 October 2026 UTC  
**Review state:** Local review deliverable accepted by user; Justice review outcome pending

User authority: “Start B005 as a controlled exception while B004 remains blocked and should work on B005 that is independent of B004”. This permits local review despite the default numeric order. It does not lift GitHub deferral, authorise implementation/provisioning or provide Justice's technical sign-off. B004 remains Blocked; stop before B006.

## Review index

| ADR | B005 coverage | Decision authority | State |
| --- | --- | --- | --- |
| [ADR-001](001-core-stack.md) | Frontend/API/database | Justice / O-03 | Proposed |
| [ADR-002](002-identity-roles-tenancy.md) | Application identity, roles and tenancy | Justice and product owner / O-04 | Proposed |
| [ADR-003](003-environments.md) | Environment/configuration separation | Justice; relevant business/budget authority for commitments | Proposed |
| [ADR-004](004-service-boundaries.md) | API/worker/provider/source/storage boundaries | Justice / O-03; later O-05–O-09 decisions retained | Proposed |

## Review action

For each ADR, record Accept, Revise or Defer, the selected option (if any), rationale, consequences, required authority and actual decision date. Business access grants need product-owner input. No signature, named account, provider choice, version, price or operational limit is inferred. These documents use supplied local sources and architectural reasoning only; no current external product capabilities or remote compatibility have been verified.

B005's full completion check remains: Justice records decisions/options/trade-offs; no provider selected by assumption. The local review pack is ready for that review, not an approved architecture. If a decision depends on missing remote facts, keep that part explicitly deferred. G0 access/reviewer requirements remain intact; no successor is automatically authorised.

## Dependency split

- **Satisfied for this review:** accepted B001–B003 local baseline/records and the explicit user sequencing exception.
- **Independent of B004:** logical stack alternatives, application permissions/tenancy, environment separation and service responsibilities.
- **Still dependent on B004:** assertions about actual remote code/branches, protections, developer repository access, PR #2 outcome and eligible repository review.
- **Separate outstanding inputs:** product permission choices, Justice ADR decisions, data policy B006, phase refinement B007, and later queue/source/model/storage/recovery choices. B004 completion alone resolves none of these.

[Build order](../../build-order.md) · [Progress](../../progress.md) · [Decision register](../../decisions.md) · [B005 report](../evidence/B005-local-architecture-review.md)

## User acceptance record

20 October 2026 UTC — User: “I accept B005”. Local review acceptance recorded; no Justice identity, technical sign-off or selected architecture option inferred. Explicitly justified deferrals can remain after technical review; dependent implementation stays gated. See the [B005 evidence report](../evidence/B005-local-architecture-review.md).
