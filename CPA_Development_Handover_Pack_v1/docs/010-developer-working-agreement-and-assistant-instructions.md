# 010 — Developer Working Agreement and Assistant Instructions

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Team structure

Founder/CEO = product owner and final commercial sign-off. Justice = technical lead and reviewer. Justice’s assistant = HUMAN assistant developer, accountable to Justice for assigned work. ChatGPT may provide guidance, but is not a repository member or substitute reviewer.

## Day-to-day workflow

Justice creates/refines issue with acceptance criteria, assigns assistant, approves approach. Assistant creates feature branch from develop, implements with tests, opens PR referencing issue, documents change. Justice reviews; independent reviewer requirement must be satisfied by eligible non-author. Merge to develop, test staging, report demo to CEO. Production release requires separate approval.

## Branch conventions

main = approved production; develop = integration; feature/CPA-###-short-name; fix/CPA-###-short-name. PR template includes summary, issue, screenshots, tests, risks, migration and rollback. No direct push to protected branches.

## Working rules

Never commit credentials, private client data or licensed full-text research. Ask when requirements conflict. Avoid undocumented architecture changes. Do not fabricate market data or citations. All generated outputs need evidence labels and review. Tests must accompany functional changes. Maintain README and ADRs.

## Justice oversight

Weekly issue review and planning; daily lightweight blocker updates during active sprints; mandatory PR review; staging demonstrations; code-quality and cost oversight; record approvals in GitHub. The assistant should have Write access only to required repositories, not organisation Owner or Render billing/admin rights.

## Handover sign-off

CEO confirms scope and phase priorities; Justice confirms architecture and risk register; assistant confirms access and task understanding; all confirm review policy and communication channel. No assumption that accounts or credentials are already provisioned.

