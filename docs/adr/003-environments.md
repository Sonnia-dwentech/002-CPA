# ADR-003 — Local, staging and production separation

**Updated:** 21 October 2026 (Atlantic/Reykjavik)  
**Status:** Accepted for the local synthetic baseline; listed deferrals remain binding  
**Prepared by:** Codex under the user's B005 selection  
**Decision owner:** Justice; product owner also required for business permissions  
**Approval/date:** 21 October 2026 (Atlantic/Reykjavik); user confirms Justice approval: “Justice approves the four local ADR decisions and listed deferrals”. See [acceptance record](../evidence/B005-local-architecture-acceptance.md).

This revision replaces the 20 October proposal's descriptions of unbuilt local work. The original is preserved in [the pre-review snapshot](../evidence/B005-before-current-review.zip). Tested implementation is evidence for review, not retrospective technical approval. No remote alignment is claimed.

## Accepted local decision

Keep development, disposable verification, persistent local rehearsals and restored recovery targets separately configured. Retain synthetic data, loopback-only services and disabled live providers. Hosted staging and production must have separate databases, secrets, storage and provider projects/limits if later authorised. Shared staging/production data or credentials are not an acceptable shortcut.

## Options, rationale and consequences

| Option | Rationale / trade-off | Recommended outcome |
| --- | --- | --- |
| Separate local verification/rehearsal/restore state | Provides contained migration/failure/recovery evidence; multiple services and credentials need careful runbooks | Select for the local baseline |
| Separated hosted environments using source-proposed hosting or another provider | Logical boundary is useful, but account ownership, capability, cost and operating evidence are missing | Keep the boundary; deliberately defer vendor/provisioning |
| Reuse staging/production databases or credentials | Reduces configuration but defeats the required separation | Reject |

## As built and evidence

- [B024](../evidence/B024-local-rehearsal.md): isolated persistent synthetic rehearsal, separate runtime/migration credentials and local HTTPS.
- [B025](../evidence/B025-local-recovery.md): actual consistent snapshot, isolated restore and comparison. This is manual same-machine recovery evidence, not off-machine backup, PITR or agreed recovery targets.
- [B027](../evidence/B027-accessibility-setup.md): a second setup/rehearsal and scoped support checks. The [main dashboard](../evidence/main-dashboard-connection.md) now depends on its retained service on 3543.

The private local state uses user ACLs. The current local CA is short lived; only its public certificate is exported for the dashboard's fixed upstream. Certificate and hostname validation remain enabled; the CA is not installed as Windows/browser trust. Renewal/pin updates remain manual. Existing services, volumes and backups must be retained under the user's instruction; no retention/deletion schedule is adopted.

## Deliberate deferrals and operational checkpoints

The Docker bootstrap/migration role is privileged; the runtime role is separate and non-superuser. Runtime SELECT covers all CPA tables; session writes and UPDATE(id) on users support the current lock path. UPDATE(id) is a real write grant. Justice must review a least-privilege locking/migration design before hosted use. This is not a production privilege certification.

Before any hosted staging or release, Justice and the relevant business/budget authority must settle hosting/account ownership, region, domains, origins, secret loading/rotation, database transport TLS, least privilege, certificates, operators, spending ceilings, retention, backup location, agreed RPO/RTO and restore evidence. No numerical service target, provider or operator is invented. B004/RCI-01 and release review remain separate requirements; GitHub stays deferred.

[Decision summary](../evidence/B005-current-architecture-review.md) · [ADR-001](001-core-stack.md) · [ADR-002](002-identity-roles-tenancy.md)
