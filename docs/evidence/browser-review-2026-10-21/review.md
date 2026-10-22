# Local browser functionality review

Date: 21 October 2026 (Atlantic/Reykjavik). Requested by user after B007 completion. No numbered task started or acceptance/gate status changed.

Actual browser controls were used on the existing local services:

- http://127.0.0.1:3000: Command Centre rendered; Idea Studio navigation changed page/title and focused main content; its planned/unavailable state was accurate; return link worked.
- http://127.0.0.1:3100/dashboard: first sign-in attempt succeeded and loaded three accessible synthetic persisted references.
- Combined kind=idea, state=draft, owner UUID ending 002 returned one record.
- Same filters with hidden owner UUID ending 003 returned zero/no matching records.
- Invalid owner input displayed validation feedback, hid counts/list and focused the status result.
- Research type displayed unavailable with no count, rather than a misleading zero.
- Clearing filters restored all three references.
- Sign-out hid protected count/list; Retry/refresh remained unauthenticated and did not reload records.
- A second sign-in succeeded; dashboard was left signed in for user exploration. Both shell and dashboard tabs were marked to remain open.

[Dashboard screenshot](dashboard.png), [shell screenshot](shell.png), [signed-out screenshot](signed-out.png). No application/config change, service restart, fixture/schema edit or cleanup was needed. Only synthetic test sessions were issued/revoked. Existing databases, backups and other previews remain retained.

A strict automation label selector did not match a native select, so the check used the browser's observed settable accessibility controls. That was an automation-target mismatch, not evidence that the user control failed. All listed UI results were observed after the actual control actions.

This review covers the existing foundation shell and isolated synthetic dashboard. Planned modules, real identity, live AI/business workflows and browser-trusted HTTPS operation are not established by it. B026-OBS-01 remains open: successful login in this run does not establish the cause or permanent resolution of its earlier intermittent failure. Spoken-reader verification and original full-G1 deferrals remain.
