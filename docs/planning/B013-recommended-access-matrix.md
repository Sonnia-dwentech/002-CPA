# B013 — Recommended Access Matrix for Justice's Approval

**Version:** 0.1 — user-approved local baseline  
**Date:** 20 October 2026 UTC  
**Status:** User-approved for local B013 continuation; formal independent/specialist review and named assignments remain deferred  
**Prepared by:** Codex at the user's request  
**Decision authority:** Justice for technical boundaries and as nominated interim product/scope approver; CEO release/investment authority retained

## Approval recorded — 20 October 2026 UTC

User: “Approve B013 to continue”. Recorded as approval of this version's access-policy recommendations for the requested local implementation using synthetic data. No exceptions were supplied. This is user approval; it is not attributed to Justice personally and does not invent a separate B006 specialist/independent review outcome.

Named real-account bootstrap and actual identity/session configuration remain unset. The local implementation creates no real accounts or providers. Formal reviews remain prerequisites before shared integration, deployment or real-data use. The recommendation/approval worksheet text below is preserved as the reviewed baseline; its earlier “not approved” language is superseded by this entry only for the authorised local scope.

## Recommendation and scope

Use invite-only human accounts, explicit record grants, private-by-default internal records and separate client-organisation boundaries. Client sign-in is included in this design as the user requested. A client may access only their own permitted intake and explicitly published responses. Membership in a client organisation alone does not expose other members' records.

The recommendation derives from [F01 and actor definitions](../../feature-spec.md), [ADR-002](../adr/002-identity-roles-tenancy.md), [O-04](../../decisions.md#o-04) and [B006](../policies/allowed-data-and-test-fixtures.md). The concrete rules below are new recommendations for approval, not assertions that the source documents already grant these permissions.

B012 is accepted and Done. This matrix addresses B013's remaining policy choices. It does not implement B014 sign-in, enable a client portal, accelerate Discovery delivery, select an identity provider or authorise real-client data. Permissions for future resources remain inactive until their feature is separately implemented and accepted.

## 1. Identity and tenancy rules

| ID | Recommended decision |
| --- | --- |
| D1 | Invite-only enrolment for internal and client users; no public self-registration. An authorised administrator issues an invitation following recorded product-authority approval. Invitation redemption must bind the verified identity to the approved membership and be single-use. Exact expiry and identity-provider mechanics are B014 decisions. |
| D2 | Use an application user reference mapped uniquely to a verified `(issuer, subject)` identity. Email is contact information, never the ownership key or evidence of membership. Unlinked, disabled or unverified identities receive no protected access. B013 synthetic tests may inject trusted test identities; production requests cannot inject them. |
| D3 | One internal workspace; separately identified client organisations. A client user belongs to one client organisation initially. Multiple users per client organisation are allowed, but their intake records are private to the submitting user unless a later sharing rule is explicitly approved. Multi-client user membership is deferred. |
| D4 | Internal users and client users have separate account categories. Client accounts cannot acquire internal roles through role stacking. Each client-scoped resource carries a mandatory client-organisation reference; internal-only resources never become client-visible merely by adding an access grant. |
| D5 | Internal staff need explicit case assignment to handle a client's intake and private working material. No role receives automatic access to all clients. Cross-client sharing and moving records between client organisations are denied. |

The logical model needs user identity, enabled status, account category, membership, resource scope, owner, grants and client-case assignments. Exact SQL columns and migrations follow technical approval. Recommend application-enforced scoping in a shared PostgreSQL database for this local foundation; database row-level security is optional later defence, not an assumed control. Every access path must pass negative isolation tests.

## 2. Roles and grant vocabulary

Roles are capabilities, not job-title shortcuts. No named person is assigned an account by this proposal.

| Proposed role | Intended use | Proposed assignment |
| --- | --- | --- |
| Product authority | Approve account/grant changes and review assigned client responses | Justice is the nominated interim authority, but the actual account assignment must be recorded |
| CPA contributor | Create and work on authorised internal records and assigned client cases | Human CPA; other humans only through explicit approved assignment |
| Executive reviewer | Read explicitly shared decision material and record commercial/investment decisions | Founder/CEO, subject to explicit account and record grants |
| Access administrator | Execute approved account/membership changes; suspend access | Named human to be confirmed; no content privilege implied |
| Technical reviewer | Review explicitly shared technical material | Justice or another explicitly assigned human |
| Assistant developer | Development work using synthetic data | Named human to be confirmed; no business/client content entitlement |
| Client user | Own permitted intake and published responses | Verified, invited user within one client organisation |
| Future analyst / AI | No human application role in this initial matrix | Analyst disabled until separately approved; AI cannot receive human approval authority |

**Record grants:** `read` permits viewing; `edit` additionally permits permitted draft changes. Neither permits sharing, approval, deletion, export or background execution. Those require explicit capabilities below. Every grant must match an active membership and resource scope. Account suspension, invalid membership, client-scope mismatch and unavailable features override any allow grant.

## 3. Internal records matrix

“Own” means the server recorded the actor as owner when an authorised creation succeeded. “Shared” means an explicit, current grant on that resource. All omitted combinations are denied.

| Action on internal ideas/research/dossiers/technical material | CPA contributor | Executive reviewer | Technical reviewer | Product authority / Access administrator alone | Client / Assistant developer alone |
| --- | --- | --- | --- | --- | --- |
| Create a draft in an enabled resource type | Allow; creator becomes owner | Deny | Deny | Deny | Deny |
| Read record and permitted attachments | Own or shared `read`/`edit` | Shared `read` | Shared `read`/`edit` | Deny | Deny |
| Edit draft content | Own or shared `edit` | Deny | Shared `edit` on technical material only | Deny | Deny |
| Share `read`/`edit` with an internal user | Owner only; recipient must have a compatible role and active internal membership | Deny | Deny | No unilateral content sharing | Deny |
| Revoke an owner-issued share | Owner | Deny | Deny | Execute a separately approved revocation; may suspend an account | Deny |
| Archive an internal draft | Owner; restore also owner-only | Deny | Deny | Deny | Deny |
| Transfer ownership | Request transfer; cannot execute unilaterally | Deny | Deny | Product authority approves; administrator executes to an eligible active contributor | Deny |
| Export/download a generated dossier | Owner or explicit `export` grant, plus read access | Explicit `export` grant plus read | Explicit `export` grant plus read | Deny | Deny |
| Initiate research/AI/background run | Own/shared `edit` plus explicit `run` capability | Deny | Deny | Deny | Deny |
| Record commercial/investment decision | Deny | Shared readable dossier plus executive decision capability | Deny | Deny | Deny |
| Permanently delete records | Deny pending retention/deletion policy | Deny | Deny | Deny | Deny |

Owner-issued shares are limited to read/edit. Product authority approves export/run capability grants; an administrator applies them. Run permission never bypasses model/source/budget approval or the current prohibition on live provider calls. Recording a decision does not authorise a payment, contract or deployment. Existing lifecycle rules remain prerequisites; this matrix does not make a published/locked record editable.

Read access to an ordinary attachment allows its authorised retrieval; bulk/generated exports require the separate export capability. All derived outputs inherit the source restrictions. A downloaded copy cannot be technically recalled by revoking server access.

## 4. Client intake and response matrix

An **assigned CPA** has both the CPA contributor role and a case assignment approved by product authority. A **response approver** has product-authority capability plus explicit assignment to the case. Assignments are not workspace-wide access grants.

| Action | Client user | Assigned CPA | Assigned response approver | Other internal staff / other clients |
| --- | --- | --- | --- | --- |
| Create intake draft | Allow in own client organisation; server assigns submitting user and organisation | Deny on behalf of a client in this initial scope | Deny | Deny |
| Read intake and client-submitted files | Own submitted/draft intake only | Assigned case | Assigned case | Deny, including another user in the same client organisation |
| Edit intake draft | Own draft before submission | Deny alteration of client's original statement | Deny | Deny |
| Submit intake | Own draft; submission locks original content | Deny | Deny | Deny |
| Add internal analysis / response draft | Deny | Assigned case | Deny unless separately assigned CPA role | Deny |
| Read internal analysis / unpublished response | Deny | Assigned case | Assigned case | Deny |
| Publish a client response | Deny | Deny as author | Assigned case; must be a different human from response author | Deny |
| Read published response and client-approved attachments | Own case only | Assigned case | Assigned case | Deny |
| Share client case or transfer ownership | Deny | Deny | Approve internal case assignment only; no cross-client move | Deny |
| Edit a published response | Deny | Create replacement draft for new review | Approve replacement; preserve earlier version | Deny |
| Permanently delete client material | Deny pending retention/rights policy | Deny | Deny | Deny |

These are proposed workflow restrictions for later Discovery implementation, subject to related lifecycle approval. No outbound email/message is authorised by publication permission. Internal notes must not appear in a client projection, search result, download or generated output. Publication must identify the exact response version and allowed attachments; it must never expose an entire internal case record.

If Justice authors a response while acting as CPA, another explicitly designated human response approver is required. Until that person exists, publication is unavailable. Technical code review and CEO release gates remain separate.

## 5. Access administration and revocation

| Action | Recommended authority and limit |
| --- | --- |
| Approve a new membership, role, sensitive capability or client-case assignment | Product authority; named request, target scope and reason required. Cannot approve their own elevation or new content access. CEO approval is required for changes benefiting the product authority. |
| Execute an approved grant | Access administrator; exact approved scope only. No unilateral role expansion or self-grant. Where Justice holds both roles, self-benefiting changes still require CEO approval. |
| First administrator / authority account bootstrap | Explicitly recorded human approval and one-time local bootstrap procedure before implementation; no public first-user-becomes-admin rule. Named accounts remain unassigned. |
| Suspend an account or revoke access to contain a problem | Access administrator may immediately reduce access; record the reason. Restoration requires product-authority approval and cannot restore unapproved grants. |
| View administrative records | Administrator sees only identity/membership/grant metadata needed to operate access controls; never credentials, tokens or business content through this role. Grant decisions visible to product authority. |
| Change own access, tenancy or account category through a profile request | Deny. Account linking and category changes require separately approved procedures. |

On every protected request, check current account status, membership and grants. Revocation takes effect for the next authorisation check; an already delivered response cannot be recalled. Do not rely solely on long-lived role claims in a token. Queued jobs must check permission before starting and before output delivery; revoked actors cannot retrieve the result. External calls already underway may not be reversible—future job design must address cancellation and cost without promising recall.

Recommend no permission caching initially. B014 must separately define token validation, session expiry/revocation and provider mechanics. B017/B019 must define the audit event and retention implementation; this matrix grants no broad log access.

## 6. Enforcement and verification contract

- Deny by default. Unknown actor/action/resource, missing scope, disabled account, missing grants or policy errors cannot produce an allow.
- Validate trusted identity first. Never trust submitted role, owner, membership or client identifiers.
- Filter collections, counts, search, exports, files and background outputs using the same policy as direct record access.
- Recommend 401 for unauthenticated protected requests; concealed 404 for missing or unreadable records; 403 for a forbidden action on a record the actor may already read. Responses must disclose no internal policy or protected content.
- Database tests use synthetic records only and an explicitly isolated destination. No real client accounts, production dumps or external provider sessions.

| Test | Expected result if this proposal is approved |
| --- | --- |
| Contributor creates an internal draft | Owner can read/edit; another contributor cannot until explicitly shared |
| Reader changes record ID or attempts editing/export/run | Unreadable record concealed; ungranted actions denied |
| CEO, Justice or developer has no applicable content grant | No automatic content access |
| Client A substitutes client B's ID | No content or derived private information disclosed |
| Two clients belong to the same organisation | Neither sees the other's intake merely through membership |
| Client attempts internal-role injection or notes download | Denied, including through search/export/file routes |
| Assigned CPA reads a case, then assignment is revoked | Initial permitted access succeeds; next check and output retrieval deny |
| Response author attempts self-publication | Denied; a different assigned human approver can publish only the reviewed version |
| Administrator attempts self-grant or content access | Denied unless a separate valid approval/content grant exists |
| Account disabled while a job is queued | Job cannot start for that actor or deliver accessible output to them |
| Policy fails or record scope is missing | Deny; no permissive fallback |

Tests for future workflows remain planned until those features are selected. B013 should implement/test the approved core policy and persisted user/scope/grant references; B014 handles real authentication integration. Passing synthetic policy tests alone does not establish full client-portal readiness.

## 7. Justice's decision record

Approval is not recorded yet. Review the entire version, or identify exceptions by section and row. Do not treat approval of a single row as approval of the rest.

| Decision | Response to record |
| --- | --- |
| D1–D5 identity/enrolment/tenancy recommendations | Approve / amend with exact replacement |
| Internal matrix, ownership/sharing and export/run limits | Approve / amend |
| Client matrix, private intake and independent response approval | Approve / amend |
| Administration, bootstrap and revocation controls | Approve / amend; name initial authorised humans separately |
| Shared-database enforcement, denial contract and test plan | Approve / amend; record B006 technical review outcome |
| Approval identity/date/version | Unrecorded; distinguish technical approval from business-grant approval |

**Suggested approval wording:** “I approve B013 access matrix version 0.1, sections 1–6, for local implementation, with these exceptions: [none or specific amendments]. I approve the business access rules in my recorded product-authority capacity and record the B006 technical review outcome as [outcome]. Initial bootstrap assignments are [explicit assignments, or deferred with affected work blocked].”

This is proposed wording, not an approval already given. Provider selection, exact session settings, named bootstrap identities and live configuration remain separate decisions. No secrets or credentials should be entered in this document. B013 remains Blocked until the necessary approval and review outcomes are recorded; B014 remains unstarted.
