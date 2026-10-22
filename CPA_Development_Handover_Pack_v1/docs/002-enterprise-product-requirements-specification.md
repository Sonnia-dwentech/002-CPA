# 002 — Enterprise Product Requirements Specification

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Personas and access

CEO: all strategic reports, approval and portfolio overview. Human CPA: submit/review ideas, initiate scans, prepare dossiers. Technical lead: technical settings, deployments, audit and access as authorised. Assistant developer: development/staging access, no production secrets by default. Client: own Discovery intake and approved responses only. Enforce tenant/record-level checks on server; never rely solely on hidden UI.

## CPA-AI-001 — OpenAI Intelligence Integration

All CPA intelligence-generation features must route through a company-controlled, server-side OpenAI integration; no browser-exposed API keys. Every AI request must have an actor, purpose, model, token/cost telemetry, request ID, error state and retained output subject to retention policy. Not every scan needs a model call: scheduling, retrieval, source collection, filtering and calculations should use deterministic services; OpenAI interprets, compares, reasons and drafts. ChatGPT subscriptions are separate from API billing. Provide timeouts, retries, rate limits, spending caps and graceful failure.

## CPA-CORE-001 — Command Centre

Dashboard cards: active research runs, ideas awaiting review, new Discovery enquiries, portfolio risk alerts, AI usage spend, approvals due. Lists must reflect real stored records; sample data clearly labelled. Filters by date, region, status and owner. Role-sensitive actions.

## CPA-GEO-001 — Geography selector

Human CPA can select one or multiple countries, region(s), or Global. Include explicit location taxonomy, source availability indicators, language and currency context, scan time window and sector. Global means multi-region source coverage with coverage limitations clearly displayed; do not imply exhaustive world surveillance. Store country ISO codes and region definitions; include Wales as a subnational selection within UK.

## CPA-MI-001 — Opportunity Scanner

User chooses scope, sector, date range and scan objective. System creates research run; collects permitted sources; deduplicates; extracts evidence; asks OpenAI to identify problems and solution hypotheses; scores with source quality; stores citations and timestamps; routes candidates to human review. Scheduled runs later. No fabricated live access.

## CPA-ID-001 — Idea Studio

Create/edit/archive idea; enter problem, affected group, geography, known evidence and hypotheses. Trigger structured AI assessment; show assumptions, competitors, alternatives, risks, pricing hypotheses, opportunity score, missing evidence, citations and recommended validation experiments. Save versioned dossiers; status: Draft, Researching, Review, Validate, Approved, Rejected, On Hold.

## CPA-ST-001 — Stress Testing

Select portfolio product or idea; assess severity, willingness to pay, competitors, technical, regulatory, growth, business model and strategic fit. Produce optimistic/base/pessimistic scenarios and Continue/Pivot/Pause/Stop recommendation with evidence, counterarguments and human decision log.

## CPA-RI-001 — Academic Research

Search approved open-access repositories and licensed sources; store metadata, licence and DOI/URL; extract findings with uncertainty; map findings to real-world problems and potential software applications. Restricted articles/datasets require explicit rights; no automatic copying or commercialisation of university IP.

## CPA-CD-001 — Client Discovery

Receive website enquiry through authenticated integration, webhook or secured API; validate input, anti-spam, consent, reference number and notifications. Separate client confidentiality; allow follow-up questions; create internal proposal; human approve before any outbound communication. Track bespoke versus potentially reusable product path only with contractual/IP review.

## CPA-VOICE-001 — Voice Studio

Authenticated push-to-talk or realtime voice; streaming transcript, interruption where supported, project linkage, consent/retention controls, session summary and action items. Voice uses same permissioned knowledge and AI workflows. Deliver incrementally after text workflows.

## CPA-BM-001 — Business Modelling

From validated opportunity: customer segments, value proposition, business model canvas, competitor positioning, price assumptions, TAM/SAM/SOM methodology, revenue drivers, unit economics, operating/development costs, funding need, sensitivity/scenarios, risks, milestones. Generate editable business plan, investment memo, pitch deck outline and financial-model assumptions. No unsupported numbers: label inputs and calculations.

## CPA-PM-001 and CPA-KH-001

Portfolio: product stages, owners, assessments, decision history, milestones and dependencies. Knowledge Hub: indexed authorised sources, dossier versions, research logs, evidence citations, access control, provenance, retention and retrieval.

## Opportunity scoring

Default weights: problem severity 20%; willingness to pay 20%; market size 15%; AI differentiation 15%; commercial accessibility 10%; feasibility 10%; strategic fit 10%. Rate each 0–5 with rationale and evidence strength; weighted total = sum(weight × rating/5). Display as heuristic, never probability of success. Red-flag risks may override numeric score.

## Cross-cutting requirements

Search, filters, accessible responsive UI, audit log, role-based access, versioning, export, background task status, cancel/retry, provenance, UTC timestamps and timezone display, privacy controls, notification preferences, usage analytics, API and UI error states.

## MVP acceptance journey

Given a signed-in authorised user, when they create an idea and request analysis, system persists idea, queues a run, records AI model/cost, produces structured result with source references or explicit no-source warning, allows review/edit and saves a retrievable version. Unauthorised users cannot access records; failed model calls show recoverable error without data loss.

