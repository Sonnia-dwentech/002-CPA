# 005 — UI UX Design Specification

**DWEN TECH LTD | CPA DEVELOPMENT HANDOVER PACK v1.0**  
**Classification:** Confidential – Internal  
**Status:** Proposed baseline; CEO approval and Justice technical review pending  
**Date:** 17 October 2026

## Design direction

Professional research laboratory dashboard; light neutral content surfaces, restrained navy navigation and blue accents, legible tables and charts, accessible contrast and keyboard navigation. Data-dense but uncluttered. Desktop-first responsive; no fictional metrics presented as live.

## Navigation map

Command Centre; Opportunity Scanner; Idea Studio; Academic Research; Discovery Enquiries; Stress Testing; Portfolio; Voice Studio; Business Modelling; Reports; Knowledge Hub; Settings.

## Command Centre screen

Header with organisation, current user, notifications and global search. Geography selector (Wales/UK/Ghana/West Africa/selected country/Global) with coverage indicator. KPI cards: research runs, pending reviews, new enquiries, portfolio alerts and AI spend. Main area: opportunity pipeline, recent research, product stress-test summaries, approvals and activity feed.

## Idea Studio screen

Left: idea details and research inputs. Centre: research run progress and evidence-linked analysis tabs. Right: scoring, missing evidence, decision panel. Primary actions: Save draft, Analyse, Challenge assumptions, Export dossier, Submit for review.

## Scanner screen

Scope picker (country/region/global), sector, timeframe, source filters, scan budget and Run Scan. Results table includes problem, location, score, evidence strength, source count, updated date and review status. Drill-down opens evidence and assumptions.

## Other screens

Stress Testing: product selection, scenarios, counterarguments and decision. Discovery: restricted enquiry queue and solution proposal. Business Modelling: editable assumptions, scenarios and document generation. Voice: microphone control, transcript, citations, notes and consent. Knowledge Hub: permission-filtered search with source detail.

## User journeys

UJ-01 CEO reviews pending dossier → opens sources → approve/return/reject. UJ-02 Human CPA creates idea → analyses → challenges → revises → submits. UJ-03 Human CPA selects Ghana → runs limited scan → reviews evidence → promotes opportunity. UJ-04 Client submits Discovery enquiry → authorised staff triages → human approves response.

## States and accessibility

Design loading, empty, partial, error, access denied and stale-source states. WCAG 2.2 AA target; semantic forms, focus states, labelled charts, keyboard access, text alternatives and screen-reader announcements. Every destructive action needs confirmation.

