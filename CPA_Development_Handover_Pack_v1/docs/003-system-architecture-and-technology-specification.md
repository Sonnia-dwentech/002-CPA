# 003 — System Architecture & Technology Specification

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Architecture decision baseline

Proposed frontend Next.js/TypeScript; backend FastAPI/Python; PostgreSQL with migrations; OpenAI API via backend; background jobs for scans; object storage for generated reports; Render for hosting; GitHub Actions CI. Justice must issue Architecture Decision Records (ADRs) before committing production design.

## Logical components

Browser → Next.js UI → FastAPI service → PostgreSQL. API service → OpenAI adapter; Research Source connectors → ingestion queue → evidence store → analysis orchestration; report generator → private object storage. Worker handles asynchronous research runs. Authentication provider or secure managed identity validates sessions; backend authorises every operation.

## Repository layout

frontend/ (Next.js), backend/app/api, backend/app/models, backend/app/services/ai, backend/app/services/research, backend/app/workers, backend/tests, database/migrations, docs/handover-pack-v1, docs/adr, .github/workflows, .env.example, AGENTS.md. Avoid creating empty folders without meaningful files.

## Data model minimum

users(id,role,status); ideas(id,owner_id,title,problem,geography,status,created_at); research_runs(id,idea_id,scope,status,started_at,finished_at,cost); sources(id,url,title,publisher,published_at,licence,accessed_at); evidence(id,run_id,source_id,claim,confidence); dossiers(id,idea_id,version,content,approved_by); product_reviews(id,product_id,decision); discovery_enquiries(id,client_id,consent,status); ai_usage(id,actor,model,tokens,cost); audit_events(id,actor,action,resource,timestamp). Add row-level isolation for client data.

## API contracts (illustrative)

POST /api/v1/ideas; GET /api/v1/ideas/{id}; POST /api/v1/ideas/{id}/analyse → 202 + run_id; GET /api/v1/research-runs/{id}; GET /api/v1/dossiers/{id}; POST /api/v1/opportunity-scans; GET /api/v1/geographies; POST /api/v1/discovery-enquiries; GET /api/v1/usage. Define OpenAPI schemas, validation, pagination, idempotency for job creation, structured errors and authentication.

## AI adapter

One server-side abstraction with model selection config, prompt templates under version control, JSON schema output validation, refusal/error handling, logging with sensitive-field redaction, token/cost metering and test doubles. Tool responses are untrusted inputs; guard against prompt injection and citation laundering.

## Deployment environments

Local, staging, production with separate databases, credentials, API projects and spending limits. Render web services and worker as appropriate. Database backups and restore testing. HTTPS, restricted CORS, least privilege, no secrets in logs or repository.

## Architecture decisions required

Identity solution, tenancy boundaries, source licensing, job queue, document/object storage, AI model routing, voice provider, web Discovery integration, backup retention, Render service sizing and cost ceiling. Each decision recorded with options, trade-offs, owner and date.

