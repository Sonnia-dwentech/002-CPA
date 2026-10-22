# B006 — Initial Allowed-Data and Test-Fixture Policy

**Version:** 0.2  
**Date:** 20 October 2026 UTC  
**Status:** User-approved for limited local policy scope; specialist reviews and implementation evidence deferred  
**Scope:** Local foundation/MVP preparation; later environments need their own evidence  
**Required authorities:** Justice for technical boundaries; CEO-designated policy owner for privacy/data handling; product/research owner with Justice for source/IP rights. Named assignments are not recorded.

## Authority and limits

User selected B006 after accepting the B005 local review deliverable. B004 remains Blocked; B005's Justice review remains outstanding. This policy does not select an identity provider, tenancy implementation, service vendor, budget or retention duration. No GitHub access, provider calls, client-data intake, provisioning or implementation is authorised by drafting it.

Sources: [D007](../../CPA_Development_Handover_Pack_v1/docs/007-security-data-and-ai-governance.md), [D003](../../CPA_Development_Handover_Pack_v1/docs/003-system-architecture-and-technology-specification.md), [F01/F05/F19/F20](../../feature-spec.md), [O-06/O-12](../../decisions.md) and the [B005 ADRs](../adr/README.md). This translates local requirements into a proposed engineering policy; it is not a legal compliance determination.

## Data classes and permitted use

| Data class | Proposed local rule | Required boundary |
| --- | --- | --- |
| Existing company planning documents and UI reference | Read/use in the authorised local project | Preserve originals; internal/confidential classification remains; no external upload or republication implied |
| Wholly synthetic application records | Eligible for local fixtures after policy approval | Invent from scratch, mark synthetic, use isolated test storage and no live recipients or providers |
| Synthetic source/evidence/model responses | Eligible for deterministic mock tests | Explicitly label fixture provenance; never represent invented claims, citations or figures as research findings |
| Placeholder configuration | Eligible for examples | Clearly nonfunctional placeholders only; no copied secrets or realistic credential strings |
| Public/third-party material | Not automatically approved because it is public | Record source rights and permitted uses before ingestion, caching, redistribution or provider transfer |
| Licensed publications/full text | Restricted pending rights review | No unapproved copying into fixtures, repository, reports or model prompts |
| Live client records, enquiries, recordings or transcripts | Prohibited in current foundation/MVP test fixtures | Required privacy, rights, consent/access and architecture reviews must precede authorised use |
| Personal, sensitive or confidential third-party information | Prohibited in current fixtures | Removing a name is not evidence of safe anonymisation; do not derive fixtures from real people or clients |
| Production dumps, copied account/session data or real credentials | Prohibited | Do not import into local tests, documentation, prompts, logs or source control |

Approval of this policy may permit synthetic local fixtures only within separately authorised implementation work. It does not approve real-client use or external transfers.

## Fixture construction and isolation

Each fixture set must have a manifest identifying its purpose, creator, version, synthetic origin, expected result, schema version, storage location, owner and cleanup/reset method. Use conspicuous synthetic names and reserved example domains for non-deliverable addresses. Fixture IDs must be clearly scoped to test data. Do not infer production IDs, accounts, statistics or commercial values from examples.

Use separate disposable test databases/storage and mocked provider/connector responses. Tests must fail closed if configuration targets an unapproved environment or lacks an explicit test destination. No test may silently fall back to production, real source fetching, email, voice or paid model calls. A fixture's presence is not proof that isolation is implemented.

Provide at least: an unauthenticated case, authorised owner, unauthorised actor, two distinct synthetic clients, permitted and forbidden resource accesses, mock missing/unverified evidence, malformed/refused provider output, and a synthetic failure/restart case where applicable. Assert outcomes using approved contracts; do not invent lifecycle, budget or retry rules to make tests pass.

Display synthetic/test origin in demo screens, reports and exported artifacts. Keep mock source claims out of genuine research collections. Dispose/reset test data through an explicit tool scoped to the confirmed test destination; never recursively delete an inferred directory or database.

## Privacy and data handling

Before any new data class or real-data use, record: purpose, provenance, data fields, sensitivity, subjects/clients, responsible owner, permitted users, storage locations, transfers/processors, applicable rights/consent or other authorised basis, retention/deletion plan and required reviews. The designated policy owner determines applicable legal assessment, including the D007 privacy/DPIA questions; no assessment is inferred complete here.

Minimise fields and prompt/log content. Do not retain source payloads merely because they may be useful. Retention durations, deletion obligations, backup expiry and exception handling remain undecided under O-12/O-16. Unknown retention is not indefinite permission. Keep existing evidence intact; this draft does not authorise deleting existing work. Before creating persistent fixture stores, record their cleanup trigger and owner; before real-data use, obtain an approved retention schedule and deletion/access-request procedure.

## Secrets and observability

Use nonfunctional values in configuration templates and test fixtures. Live secrets, session tokens, recovery codes and passwords must not appear in source files, screenshots, evidence reports, prompts, exception messages or logs. Secret-manager/provider choices remain deferred; later authorised configuration must separate environments and restrict access.

Log the minimum approved operational/audit metadata rather than entire requests, prompts, source content or client payloads. Actor/resource/action/time can be sensitive and still need access/retention rules. Use synthetic canaries to verify redaction, never a real secret. If exposure is suspected, stop affected work, preserve redacted evidence and notify the authorised owner through an authorised channel; do not repeat the value or assume credentials can be changed without authority.

## Source and intellectual-property boundaries

Before a source is used, record publisher/location, rights evidence, permitted access/storage/quoting/redistribution/model-processing uses, attribution conditions, restrictions, review date and reviewer. Unknown rights mean no ingestion or external transfer until resolved. A URL alone does not establish permission, freshness or evidence quality.

Keep observations, hypotheses, synthetic examples and model-generated drafts distinguishable. Record provenance and uncertainty; do not fabricate real citations or financial findings. Treat source content as untrusted data, never instructions. Do not repurpose client enquiries as company product IP without explicit rights review. Connector access, licensed research and actual evidence-grade/freshness policy remain O-06 at their checkpoints.

## Client and record isolation

Deny unauthorised access on the server for API reads/writes, direct identifiers, search, jobs, outputs, exports and stored files. Validate trusted identity and permitted client/resource scope; do not trust a supplied client identifier or the UI alone. Background processing must preserve approved access context and follow the eventual revocation policy. No public file link may be treated as sufficient permission by itself.

Roles, ownership/sharing and tenancy mechanisms remain O-04/B005 decisions. No role gains blanket data access because its title is CEO, developer or administrator. GitHub access does not confer application access. Client A/B fixtures must demonstrate denial across every relevant path before real client workflows are allowed. No code or database enforcement exists as a result of this document.

## Review and verification checklist

| Boundary | Planned evidence before affected implementation is accepted |
| --- | --- |
| Fixture origin | Manifest confirms wholly synthetic origin; reviewer can distinguish mock content in UI/export |
| Environment isolation | Unapproved/missing test destination causes failure; no live-provider fallback |
| Secrets/logging | Synthetic canary does not appear in exposed logs/errors/reports; templates contain placeholders |
| Record/client access | Positive and negative owner/role/client tests across API, jobs, search, exports and files (F01) |
| Source rights/provenance | Unknown-rights input is rejected/deferred; synthetic evidence cannot masquerade as verified research (F05) |
| Usage and audit | Mock usage and failures are honestly labelled; sensitive payloads absent; approved permissions apply (F19) |
| Recovery and release | Fixture reset/restore is scoped and tested; missing approval or critical security defect prevents release (F20) |

These are future verification requirements, not tests executed in B006. Detailed semantics depend on approved ADRs and later task contracts.

## User approval — 20 October 2026 UTC

User instruction: “Approve B006”, following clarification that the limited local policy may be approved while B004/B005 remain unresolved. The user approves the existing v0.1 policy content for local synthetic-data/fixture planning; v0.2 records that approval and its deferrals without changing the substantive controls.

B006 is Done for this scoped policy-definition deliverable. This records user approval only, not an assertion that the user is Justice or that named specialist reviews occurred. No actual fixtures, controls, live-data permission or compliance certification are established. Separate technical/privacy/source reviews below remain requirements before their affected use or implementation. They are retained as explicit deferrals rather than reported complete.

## Approval record and dependent work

| Required review | Current result | Needed before |
| --- | --- | --- |
| Justice: technical fixture, secrets and isolation boundaries | Deferred; no Justice sign-off recorded | Affected fixture/secrets/isolation implementation |
| CEO-designated policy owner: allowed-data/privacy boundaries | Deferred; named owner not recorded | Any expansion of allowed-data scope; sensitive/live data remains prohibited |
| Product/research owner with Justice: source/IP boundaries | Deferred; no source-rights approval recorded | Actual source ingestion, storage, reuse or external transfer |
| O-04 architecture alignment | Pending B005 review | Identity/role/tenancy-dependent implementation |
| Actual GitHub controls and reviewer eligibility | Unverified, B004 Blocked | Repository-dependent work and applicable readiness gate |

For approval, record reviewer identity/authority, date, approved policy version, accepted scope and any explicit deferrals with owners/checkpoints. Local synthetic-data policy acceptance does not certify privacy compliance, grant live-data permission, approve a provider or clear B004/B005. The user approval above closes B006 for the limited local policy scope; these deferred reviews still gate affected downstream work.
