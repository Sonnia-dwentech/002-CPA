# 007 — Security Data and AI Governance

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Threat model

Assets: company IP, research dossiers, client Discovery submissions, user accounts, API keys and model usage budget. Threats: unauthorised access, prompt injection from external sources, secret exposure, data leakage across clients, abusive API costs, poisoned research, insecure deployment and accidental deletion.

## Identity and access

MFA for GitHub and privileged accounts; least-privilege GitHub teams; protected main/develop; feature branches; independent PR review; production deploy rights limited to Justice and CEO-authorised administrators. App RBAC and server-side object-level authorisation. No shared developer logins.

## Data protection

Create data inventory, purposes, lawful basis, retention schedules and access controls. Review UK GDPR obligations and DPIA triggers before handling personal/sensitive client data. Minimise stored prompts, anonymise analytics, encrypt transit/at rest, define deletion and DSAR process.

## AI safety and quality

Model outputs are drafts; label uncertainty and unverifiable claims. External pages and files are untrusted; never execute instructions embedded in research content. Avoid passing sensitive client information to third-party models without contractual/legal review and configured data controls.

## Academic and client IP

Respect publisher licences, university permissions, research copyright, confidentiality and client ownership clauses. Never repurpose confidential client enquiries as product IP without review and rights.

## Operational controls

Secrets in Render/GitHub secrets managers, not repository; dependency scanning, secret scanning where available, pinned dependencies, audit events, backup/restore drills, incident escalation, service status monitoring, per-run AI spending limits.

## Human approvals

CEO: investment, commercial commitments, production release approval. Justice: technical design and code quality. Assistant developer: no unilateral release/privileged credential changes. Keep evidence of sign-off.

