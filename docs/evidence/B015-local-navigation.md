# B015 — Local Responsive Navigation Shell

**Date:** 20 October 2026 UTC  
**Status:** Done — user accepted the verified local responsive navigation shell on 20 October 2026 UTC  
**Authority:** Start B015 plus explicit approval of offline-only installation and the derived local design baseline. G0-L restrictions retained.  
**Executor:** Codex; independent review is not inferred.

## Delivered scope

The [frontend](../../frontend/README.md) runs at **http://127.0.0.1:3000/**. The separate backend remains at port 8000. All twelve D005 navigation labels are implemented; the eleven unfinished workspaces have explanatory “Not available yet” pages. The Command Centre states that records are not connected and queries no metrics. Unknown routes return 404 with a return-home action.

The shell has desktop navigation, a narrow-screen menu, current-page indication, descriptive titles, semantic navigation/main landmarks, a skip link and focus management. No sign-in control, fabricated user/count, operational research/voice action, session storage or provider call was added. B016 remains Not started.

## Approved local design baseline

User answers: **“Approve offline-only installation”** and **“Approve this local design baseline.”** These resolve the two B015 preparation blockers; they do not approve a live identity provider, full product design, deployment or formal deferred reviews.

Values are locally derived, not exact source-supplied tokens: navy `#0c1c31`, secondary navy `#162c47`, blue `#155bd7`, pale blue `#eaf1ff`, canvas `#f3f6fb`, white surfaces, ink `#17263c`, muted text `#52647c`, borders `#dce4ee`, navigation text `#dce7f5` and muted navigation text `#afc1d8`. Focus rings are blue on light surfaces and amber `#ffbf47` on dark surfaces. Spacing scale: 4/8/12/16/24/32/48px; panel radius 12px. Arial/Helvetica/system sans-serif avoids downloads. Inline SVG icons and CSS geometry are decorative, not copied operational data or official brand assets. Layout breakpoints: 1180/800/440px.

## Installation and verification evidence

- Offline installation succeeded from the existing cache with `--offline --ignore-scripts --no-audit --no-fund`: 27 packages added. The first version-spec attempt failed because cached `@types/node` metadata was absent. Exact cached tarball URLs resolved that issue. A sandbox cache-temp write failed with EPERM; the same offline operation succeeded with approved local execution permission. No online fallback was used.
- Installed: Node 24.21.0; npm 11.19.0; Next 16.3.8; React/React DOM 19.3.0; TypeScript 6.0.3; Node types 24.19.1; React/React DOM types 19.3.0. Windows x64 native SWC resolution passed. The launcher checks that package before Next starts and disables telemetry. `.npmrc` retains offline/script restrictions; lockfile retained.
- `npm run typecheck` passed. Production build passed, including TypeScript and 14 static pages. Sandboxed Next worker creation initially failed with `spawn EPERM`; permitted local execution succeeded. Final build repeated after focus/scroll configuration changes.
- [HTTP route results](B015-route-checks.json): all 12 known routes returned 200, with unavailable copy on all 11 unfinished pages; unknown route returned 404.
- In-app browser desktop inspection at approximately 975px viewport: navigation and content rendered. Tab reached the visible skip link; Enter focused main content. Selecting Idea Studio changed title/content and focused main.
- Responsive browser checks used temporary same-origin iframes of 320px and 390px because the browser tool exposes no viewport resizing API. Both rendered with readable wrapping. Document client/scroll widths matched (305/305 and 375/375 after scrollbars), so no horizontal overflow was observed. This is browser reflow evidence, not physical-device verification.
- Mobile Menu expanded/collapsed with accurate accessibility state. Tab then Escape closed it and restored button focus. Enter on the menu and Idea Studio link navigated, collapsed the menu and focused main. The temporary harness was removed after checking.
- [Desktop screenshot](B015-desktop.png) and [narrow screenshot](B015-narrow.png) retain browser evidence. Keyboard focus colours were adjusted for light/dark backgrounds. A Next smooth-scroll warning was addressed with the documented HTML attribute. No full assistive-technology or cross-browser audit is claimed.
- Next generated frontend AGENTS.md/CLAUDE.md during first startup. These newly generated files were removed and generation disabled with `agentRules: false`; original source instructions remain intact.

## Preservation, acceptance and handoff

[Pre-implementation snapshot](B015-before-implementation.zip) and [input hashes](B015-implementation-input-hashes.json) preserve prior planning files. Original source pack, UI reference, build definitions and backend remain unchanged. Only B015 documentation/current-ledger entries and the new frontend/evidence are in scope. No GitHub, downloads, external provider, database or deployment operation occurred.

[Final preservation check](B015-preservation-check.json) confirmed 124 pre-existing files unchanged, no missing files, and only the six intended planning/navigation documents modified. Final restarted frontend returned HTTP 200 and rendered in a fresh browser tab; its warning/error log was empty. The desktop screenshot was refreshed from that tab.

**Acceptance recorded — 20 October 2026 UTC:** The user said “Accept B015”. B015 is Done for the verified local responsive navigation shell described above. This acceptance does not approve B016, live sign-in/data/services, deployment or deferred formal reviews. B004 remains Blocked and B005/B007 review boundaries remain unchanged. B016 remains Not started. This acceptance updates records only; no code or GitHub activity occurred. [Pre-acceptance snapshot](B015-before-acceptance.zip) retains the previous report and tracker.

---

## Historical preparation record — superseded by the approved implementation above

### Initial B015 preparation

**Date:** 20 October 2026 UTC  
**Authority:** User “Start B015”; G0-L and local-only restrictions  
**Status:** Blocked pending offline-install and local design-baseline choices  
**Executor:** Codex; no independent review inferred

## Scope and findings

[B015](../../build-order.md) requires a responsive Next.js navigation shell. Its completion check is: “Routes/state labels reflect delivered scope; keyboard/focus checks pass; no fake service availability.”

B014 is accepted and Done. [O-11](../../decisions.md#o-11) and the [design worksheet](../planning/phase-1-design-operations.md) leave final route labels, design tokens/assets and unavailable-navigation treatment unresolved. The user has been asked to approve:

1. Dependency installation using the existing local npm cache only, with network access and install scripts disabled.
2. A small documented token set derived from the supplied UI reference, source-document navigation labels and visible “Not available yet” labels.

Both answers are pending. No dependency installation or frontend implementation has occurred. The current backend remains available at port 8000; it is not the Next.js frontend.

## Read-only local tooling evidence

- Node 24.21.0 and npm 11.19.0 reported their versions; these were previously approved provisional tooling.
- npm cache lists Next.js 16.3.8, React/React DOM 19.3.0, TypeScript 6.0.3 and 7.0.2, React types 19.3.0 and Node types 24.19.1 tarballs.
- Cache entries are not proof of a complete compatible install. A targeted SWC cache query returned no entries; native compiler availability remains unverified.
- No registry request, package download, install, GitHub or external provider operation was performed. An approved offline install must fail rather than fall back to fetching missing dependencies.

## Proposed route and availability plan

Use [D005](../../CPA_Development_Handover_Pack_v1/docs/005-ui-ux-design-specification.md) for labels. The mockup's alternate labels, counts, user photo and operational badges are illustrative and do not establish actual data or service readiness.

| Route | Source label | Proposed content/state |
| --- | --- | --- |
| `/` | Command Centre | Local shell introduction and explicit unavailable-data state; no fabricated metrics |
| `/opportunity-scanner` | Opportunity Scanner | Not available yet; no scan action |
| `/idea-studio` | Idea Studio | Not available yet; no save/analyse action |
| `/academic-research` | Academic Research | Not available yet; no source fetching |
| `/discovery-enquiries` | Discovery Enquiries | Not available yet; no client data or intake action |
| `/stress-testing` | Stress Testing | Not available yet; no scenario execution |
| `/portfolio` | Portfolio | Not available yet; no invented portfolio |
| `/voice-studio` | Voice Studio | Not available yet; no microphone access |
| `/business-modelling` | Business Modelling | Not available yet; no calculated figures |
| `/reports` | Reports | Not available yet; no generated export |
| `/knowledge-hub` | Knowledge Hub | Not available yet; no operational search |
| `/settings` | Settings | Not available yet; no credential, membership or configuration changes |

Links may navigate to explanatory unavailable pages; their labels must not imply the underlying service works. The active Command Centre route is a shell view, not an operational dashboard. An unknown URL should produce a useful not-found state.

Header context: organisation/product name and “Local preview — not signed in”. Do not invent a current user, unread-notification badge or connected-account state. Search, geography and notifications have no implemented service and should not look operational. Real sign-in/access-denied integration remains B016.

## Proposed design and interaction baseline

- Preserve `UI.png` in place as reference; no crop of its fake metrics, logo recreation or external image/font requests.
- Derive explicit CSS tokens for navy navigation, blue active/focus state, neutral background, white panels, text/borders, spacing, radius and system typography. Record chosen values with the implementation after approval; do not claim they were supplied as exact source tokens.
- Desktop sidebar and light main content; on narrow screens use an accessible navigation toggle with an accurate expanded state, Escape dismissal and sensible focus return.
- Semantic navigation/main landmarks, a skip link, descriptive page titles, visible keyboard focus and current-page indication.
- No button starts an unavailable service. No mock record counts or “all systems operational” claims.

## Verification after approval and implementation

1. Resolve the local dependency set offline; if incomplete, report the missing package without downloads or script execution.
2. Verify Next.js startup and route/state rendering at a loopback-only frontend port. Keep the accepted backend separate.
3. Check each known route and unknown-route handling, availability labels and absence of fabricated data/provider controls.
4. Check keyboard navigation, skip link, focus visibility, mobile toggle and Escape/focus restoration.
5. Inspect desktop and narrow viewport layouts for clipping/overflow and readable labels. Record the actual tool/browser used and limits; static source inspection alone does not prove interactive checks passed.
6. Record results, exact local versions and clean stopping instructions. Do not claim B016 session integration or a full Command Centre implementation.

## Preservation and handoff

[Pre-edit snapshot](B015-before.zip) and [input hashes](B015-input-hashes.json) preserve existing records. Original source pack/UI reference and backend implementation remain unchanged. Only the tracker and documentation index are updated, with this report and preservation artifacts added.

B015 is started but implementation is awaiting the two explicit choices above. No acceptance check is claimed passed. B016 remains Not started.
