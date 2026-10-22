# 006 — Development Roadmap Sprint Backlog

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Governance and cadence

Justice is technical owner; assistant developer implements assigned issues; CEO accepts product scope. Weekly planning/demo, short written progress update, code review per PR, phase-end acceptance. Estimate story points and dates only after architecture review.

## Phase 1 — Foundation

P1-01 architecture ADRs; P1-02 repository structure and local setup; P1-03 Next.js shell/navigation; P1-04 FastAPI health endpoint and OpenAPI; P1-05 PostgreSQL migrations; P1-06 authentication and RBAC; P1-07 OpenAI adapter with mocked test; P1-08 CI lint/test; P1-09 Render staging; P1-10 dashboard with real DB records. Exit: signed-in staging app, API, DB, tests, logs and secrets secure.

## Phase 2 — Idea Studio MVP

P2-01 idea CRUD; P2-02 analysis request/job; P2-03 source ingestion and provenance; P2-04 structured OpenAI analysis; P2-05 weighted scoring and risk flags; P2-06 dossier versioning; P2-07 human approval and audit; P2-08 report export; P2-09 end-to-end tests. Exit: complete idea-to-saved-dossier journey.

## Phase 3 — Portfolio & Stress Testing

P3-01 product registry; P3-02 review workflow; P3-03 optimistic/base/pessimistic scenarios; P3-04 critical challenge; P3-05 recommendation approval history; P3-06 product-specific tests.

## Phase 4 — Voice & Discovery

P4-01 consent and transcript storage; P4-02 voice MVP; P4-03 knowledge-linked conversations; P4-04 Discovery website integration; P4-05 secure enquiry queue; P4-06 proposal draft and approval; P4-07 security and privacy tests.

## Phase 5 — Advanced research and modelling

P5-01 geography catalogue; P5-02 country/global scans with coverage logs; P5-03 scheduler/alerts; P5-04 licensed academic connectors; P5-05 commercial model editor; P5-06 business plan and pitch outline exports; P5-07 advanced evaluation and cost controls.

## Definition of Ready

Issue has user value, scope, non-goals, acceptance criteria, dependencies, test plan, security implications, owner and design reference. Unclear issues return to Ready/Backlog for clarification.

## Definition of Done

PR linked to issue; reviewed by eligible independent reviewer; tests and lint pass; migrations and docs updated; secrets scan passes; staging demonstration; acceptance criteria checked; CEO accepts product functionality for phase milestone.

## Immediate repository task

Open PR #2 for frontend README should be reviewed by Justice (or another eligible reviewer) before merge into protected develop. Do not bypass protections or assume it is already merged.

