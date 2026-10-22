# 009 — Deployment Operations Guide

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Environment topology

Local → Render staging → Render production. Separate Postgres databases, OpenAI API credentials and quotas. Stage on develop, production from approved main release. Use GitHub Actions checks before merges and protected deployment environment where supported.

## Setup checklist

Confirm organisation membership; repository roles; open PRs; branch rules; billing owner; domain plan; Render organisation/team access; staging web/API/worker services; PostgreSQL; secret manager; CORS and redirect URLs; migrations; HTTPS; health checks; logging; alerts; backups.

## Configuration template

OPENAI_API_KEY (secret), OPENAI_MODEL (configured model), DATABASE_URL (secret), APP_ENV, FRONTEND_ORIGIN, AUTH_SECRET or identity-provider settings (secret), STORAGE_BUCKET, MAX_AI_RUN_COST, LOG_LEVEL. Never store live values in .env.example.

## CI/CD policy

Feature → PR to develop → independent review + checks → staging deployment and tests → release PR develop to main → independent review and CEO release approval → production deploy. Rollback to last verified image; migration rollback assessed individually.

## Operations runbook

Daily: monitor errors, costs and queues. Weekly: dependencies, backups and alerts. Monthly: restore drill, access review, retention review and model output sampling. Incidents: contain, revoke compromised credentials, preserve logs, notify responsible people, recover, record postmortem.

## Launch gate

No production launch without working authentication, least privilege, audit trail, tested backups, budget guardrails, privacy review, documented support owner, security test results and acceptance signatures.

