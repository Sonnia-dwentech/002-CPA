# CPA Local Project Layout

**Date:** 20 October 2026 UTC  
**Scope:** B009 local structure/reference slice under accepted G0-L v0.1

## Existing structure and ownership

| Path | Actual purpose / editing rule |
| --- | --- |
| `README.md` | Project entry point; links to the authoritative records |
| Root blueprint/spec/build order | Product requirements and task definitions; change only in authorised scope |
| Root progress/decisions/risks | Current status, decisions and risks respectively |
| `CPA_Development_Handover_Pack_v1/` | Original extracted source pack, preserved in place |
| Original root Word/ZIP/UI files | Preserve supplied artifacts; no re-export, move or replacement needed |
| `docs/README.md` | Local source/planning/evidence navigation |
| `docs/adr/` | Proposed local ADRs; no accepted technical decision inferred from file existence |
| `docs/planning/` | G0-L scope and Phase 1 work-item/design planning |
| `docs/policies/` | Local data policy and deferred review requirements |
| `backend/` | B011 local API, loopback launcher, observed dependency versions and tests; see [backend guide](../backend/README.md) |
| `frontend/` | B015 local Next.js navigation shell; [frontend guide](../frontend/README.md); no live sign-in/data integration |
| `docs/evidence/` | Dated task reports, pre-edit snapshots and hash manifests |

[Documentation index](README.md) resolves original source documents and current records. No `docs/handover-pack-v1/` duplicate is created. No source files are imported from a remote repository; B009's approved local interpretation is reference organisation, not remote import.

## Proposed application layout — B009 historical plan; B011 update below

D003 suggests the paths below. They are recorded only for future review, not instructions to create empty folders or choose a stack.

| Proposed path | Source intent | Decision/checkpoint before creation |
| --- | --- | --- |
| `frontend/` | Proposed Next.js UI | B005 stack decision; B010 setup and later UI task selection |
| `backend/app/api/` | Proposed API endpoints | Approved backend/contract approach before B011 |
| `backend/app/models/` | Proposed persisted model definitions | Approved schema/ownership design before B012/B013 |
| `backend/app/services/ai/` | Server-side adapter boundary | Approved mocked adapter scope before B018 |
| `backend/app/services/research/` | Research orchestration/connector services | Phase 2 scope and source/rights decisions before affected implementation |
| `backend/app/workers/` | Background work | Approved job/recovery contracts before B035/B036 |
| `backend/tests/` | Application tests | Approved runtime/test approach and synthetic fixtures with each affected task |
| `database/migrations/` | Versioned migrations | Approved migration workflow before B012 |
| `.github/workflows/` | Remote CI workflows | B020 scope and explicit authority; GitHub remains deferred |
| `.env.example` | Nonfunctional configuration template | B010-approved configuration contract; placeholders only |

Exact framework/runtime versions, package manager, migration tool and executable setup remain unresolved. Existing ADRs do not by themselves approve these paths. No application manifests, entrypoints or empty scaffold are added by this slice.

## Change and review boundary

The user selected B009 after approving G0-L and this local scope. Justice remains nominated accountable owner; Codex is the executor of this documentation slice. No Justice acceptance or independent technical review is claimed. The work is reviewable as three new navigation/layout documents plus the evidence report and progress update.

Check local file links and source preservation against the B009 input hashes. No real secrets, client records, copied research or provider credentials are needed. Recover earlier progress content from the B009 snapshot if an authorised rollback is needed; do not delete source material. Removing new documents is not performed automatically.

Remote layout, repository compatibility and eventual import remain unverified and deferred. Stop before B010; setup needs its own selection and task-specific decisions.

References: [D003](../CPA_Development_Handover_Pack_v1/docs/003-system-architecture-and-technology-specification.md), [G0-L scope](planning/G0-local-only-proposal.md), [ADR index](adr/README.md), [progress](../progress.md).

## B011 implementation update — 20 October 2026 UTC

The separately selected B011 task adds `backend/app/main.py`, a loopback-only launcher and focused tests. It does not create the remaining proposed API/model/worker/frontend/migration tree. B009’s original no-application-work statements describe that earlier task. Current launch/test details are in [backend README](../backend/README.md); current status is in progress.md.

## B015 update

The separately selected and approved B015 task creates `frontend/` with a responsive local shell and offline dependency lockfile. The proposed-layout table above is retained as B009 history. Use the frontend guide for port 3000; backend port 8000 remains separate. B016 has not started.
