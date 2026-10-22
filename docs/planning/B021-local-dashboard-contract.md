# B021 local dashboard contract proposal

Date: 21 October 2026 (America/Los_Angeles). Status: local baseline approved by user “Approve this local baseline” on 21 October 2026; implementation delivered, actual database verification outstanding.

User selected B021 after approving B020's local scope. Work remains local; GitHub is deferred. B021 requires agreed metric definitions and persisted record types. The existing `cpa.access_records` table is permission-reference metadata, not delivered idea/research/dossier business content. No business schema will be added solely to populate a dashboard.

## Proposed limited baseline

- Implement a backend query service for an explicitly enabled synthetic local harness, labelled `synthetic_reference_records`. Normal application business metrics remain unavailable. No frontend cards or wiring in B021; those belong to B022 after separate selection.
- Count only access-reference rows visible through the existing B013 access policy. Use its current enabled-kind whitelist, ownership, explicit grants and client/case checks. Internal callers only, matching F02; client callers denied. Do not treat an executive or administrator title as universal read permission.
- Return one total and a metadata-only list derived from the identical authorised, filtered dataset. A reference is counted once; grants cannot multiply it. Stable UUID ordering; no invented titles, progress percentages or financial values.
- Allow optional exact `kind`, `state` and UUID `owner_id` filters, combined with AND. Omitted state includes all permitted states including archived; explicitly requested state filters exactly. Unsupported kinds/states, malformed owner IDs and unknown filter keys produce a generic validation error. Do not accept raw SQL/sort fragments.
- Only explicitly enabled reference kinds may be queried; an unavailable capability must not be converted to a zero count. Owner filters narrow already-visible data and cannot grant access. A valid inaccessible owner filter returns an empty result without confirming owner existence.
- Date, geography, title search, research-run status, pending approvals, spend and portfolio metrics remain unavailable: the required business fields/services do not exist. Do not reinterpret reference states as product-review KPIs.
- Distinguish `ok`, `empty` and `unavailable`. Successful available queries with no visible matching rows return zero and an empty list. Database or permission-loading failures return a safe error, never a successful zero or partial count. Unknown actors and inactive membership deny access.
- Scope any counts/list consistency to a single database snapshot; do not promise immediate cancellation of an already-running query when a grant changes. The next query must re-read permissions and reflect revocation.

## Planned verification

Synthetic fixtures should cover owner access, explicit sharing, revocation, unrelated internal users, assigned client-case references, cross-client denial, disabled membership, role-only denial, filtering, counts matching lists, duplicate grants, empty/unavailable distinction and query failure without payload leakage. Reuse the existing access rules, not a competing dashboard permission policy.

The current workstation has no Docker executable on PATH or at the usual Docker Desktop location. Actual disposable PostgreSQL verification is not yet available here. No installation, service start, alternative database or mock-as-real evidence is implied. Unit/fake-repository tests can verify contract behaviour but cannot establish PostgreSQL execution correctness; record that distinction explicitly if implementation proceeds.

## Decision recorded

The user approved this limited synthetic-reference baseline. No actual business metric definitions, new role grants, data retention, live service or B022 scope are approved by this proposal.


Current B021 update — 21 October 2026: actual PostgreSQL 17.11 verification passed all 15 harness checks after Docker recovery and approved image download; full local checks passed. Earlier unavailable-runtime statements are historical. B021 is approved and Done for local scope; B022 unstarted. The test container was already removed before the user requested no cleanup; retain future test containers and adjust the automatic-cleanup harness before reuse. See the B021 evidence and progress tracker.


## B021 local deliverable approved — 21 October 2026

User: “Approve B021”. B021 is Done for the verified local synthetic-reference dashboard queries and filters. Existing 68 backend tests, 15 actual PostgreSQL checks and full local check runner passed; no tests rerun for this documentation-only acceptance. Earlier blocked/pending-acceptance wording is historical and superseded. B022 remains unstarted. Business metrics and frontend/API exposure remain outside this accepted scope; GitHub/RCI-01 remains deferred. Retain future test containers unless the user asks otherwise and keep approvals in chat. Pre-approval records: docs/evidence/B021-before-acceptance.zip.
