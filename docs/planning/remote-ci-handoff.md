# Deferred remote CI and merge-protection prerequisite — RCI-01

Date: 21 October 2026 (America/Los_Angeles). Status: Deferred, not verified.

The user instructed “Keep everything local till github comes in later”, selecting the proposed local-only B020 replan. B020 now covers verified local checks and failure propagation. Its original remote completion requirements are preserved here, not waived. This is a deferred prerequisite, not an additional numbered build task; the register remains B001–B105.

## Local boundary

Continue separately selected local work under G0-L. Do not access GitHub, initialise remote workflows, push, clone, pull, merge, provision remote services or deploy without a later explicit instruction changing that boundary. This instruction does not automatically start B021 or accept all future work. B004 remains Blocked for its remote scope. Actual staging, live-provider and release gates remain unmet; they are not converted to local-only completion by this replan.

## Required before remote PR collaboration, merging or release

Once GitHub introduction is separately authorised:

1. Resolve applicable B004 evidence: repository identity/access, MFA, protected branches, reviewer eligibility and historical PR outcome. Record what remains unknown and required remediation.
2. Review and adopt CI platform/tool/runtime choices and the actual source layout. Adapt the local runner to the remote checkout; verify clean dependency installation. Assess full linting, dependency advisory and secret scanning availability and coverage.
3. Configure authorised CI checks and required branch checks with matching stable names. Verify review requirements, bypass/direct-push rules and secret permissions. Remote changes need their own authority.
4. Demonstrate a controlled failing check actually blocks an eligible merge, then demonstrate passing checks on the corrected eligible PR. Record commit/PR/check identities and effective branch settings. A local nonzero exit is not this evidence.
5. Obtain the applicable technical and independent review outcomes before declaring RCI-01 complete. Justice remains nominated accountable owner; no personal acceptance or independent review is inferred now.

RCI-01 is a prerequisite for remote collaboration/merge and release, regardless of the B020 local status. Remote staging/provisioning tasks also retain their original authorisation and gate requirements. Track this handoff under O-02 and the progress handoff when GitHub returns.

References: [B020 evidence and coverage limits](../evidence/B020-local-checks.md), [B004 preflight](../evidence/B004-local-preflight.md), [build order](../../build-order.md), [progress](../../progress.md).
