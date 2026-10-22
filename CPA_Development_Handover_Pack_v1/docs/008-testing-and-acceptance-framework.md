# 008 — Testing and Acceptance Framework

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Test pyramid

Unit: scoring, validators, permissions and parsers. Integration: API/DB/OpenAI adapter with mock, source connectors, worker queues. End-to-end: authenticated idea-to-dossier journey and approvals. Security: IDOR, access control, injection, secret leakage. Accessibility and usability: keyboard/screen reader checks.

## Core acceptance scenarios

AT-01 unauthenticated request rejected. AT-02 user creates and retrieves own idea. AT-03 authorised analysis creates tracked job and stores output. AT-04 failed OpenAI call gives retryable error and no lost idea. AT-05 score calculation reproducible. AT-06 unsourced claims flagged. AT-07 unauthorised user cannot access another client enquiry. AT-08 report export retains sources and assumptions. AT-09 scan geography records actual coverage. AT-10 human approval required for investment recommendation status.

## Nonfunctional targets (initial proposed)

API health endpoint; background jobs resilient to restart; logs and traces; staging HTTPS; secure secrets; documented backups; acceptable dashboard response and job timeouts to be measured in testing; cost alerting. Justice to propose quantitative performance and recovery targets before production.

## Evidence required

CI report, test run link, reviewer approval, screenshots/demo, acceptance checklist, migration notes, deployment log and open known defects. Block release on critical security or data isolation failures.

## Release sign-off

Justice signs technical acceptance. CEO signs functional/business acceptance. Record release version, date, known issues, rollback plan and owner. No self-approval of PR by its author.

