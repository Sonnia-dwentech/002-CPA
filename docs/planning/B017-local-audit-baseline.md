# B017 approved local audit baseline

**Date:** 20 October 2026 UTC  
**Authority:** User “Approve local event baseline” and “Approve disposable storage baseline”

Only synthetic local test activity is authorised. Audit rows live in a newly created disposable PostgreSQL database and are discarded with that run. Operational events are captured in test-runner memory. The runner is the sole intended reader; no application audit endpoint, viewer role, exporter or production retention schedule is introduced.

## Event contract

| Action | Outcomes | Identifiers |
| --- | --- | --- |
| `session.issue` | issued, denied, unavailable | User UUID resolved from server-verified synthetic identity; no session token/digest |
| `session.logout` | revoked, denied, unavailable | User UUID from validated session; no session token/digest |
| `record.read` | allowed, denied, unavailable | Validated user and database-resolved record UUIDs |
| `privileged.check` | denied, unavailable | Validated user UUID; privileged operations remain denied pending MFA |

Unknown IDs are null. Audit metadata contains only event ID, timezone-aware database timestamp, actor/resource UUIDs and fixed action/outcome codes. Timestamps come from PostgreSQL, not request input. There is no free-text payload field. A denied record's ID is retained only if resolved in trusted storage, and never returned to the unauthorised client.

Operational events contain a new server-generated request UUID, allowlisted route name, bounded HTTP method/status and duration in milliseconds. Unmatched URLs become `unmatched`. No raw path, query, body, header, cookie, credential, IP address, user agent or exception text is captured.

## Failure and access behaviour

Successful audited session changes and the audit insert share one outer transaction. A missing/unwritable audit table returns generic 503 and rolls back issuance/logout; it does not claim successful logout or return an issued token. Handled permission denials are audited before their generic HTTP denial is returned. Validation-store failure can record `unavailable` if audit storage still works, without inventing an actor.

Audit-store failure cannot record itself in the failed store. It produces minimal operational status evidence only; no fallback file or queued payload is created. Persistent delivery/retry policy remains deferred. This implementation does not claim tamper-proof storage, production database-role separation or protection from the machine/database owner.

Migration 0004 revokes PUBLIC table privileges. Only the disposable runner's existing database owner connection reads/writes the table; no real user is granted audit access. The audit wrapper is explicitly wired in the B017 test application. Normal application startup and the existing B016 browser harness do not silently enable persistent logging.

## Run and cleanup

```powershell
Set-Location 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B -m unittest discover -s tests -v
python -B check_local_audit.py
```

Requires the already installed local PostgreSQL Docker image and Python packages. The runner uses `--pull=never`, a random container name, loopback-only binding and tmpfs data. Docker access needs local execution permission on this host. The runner stops its test HTTP server and removes the disposable container in cleanup; do not force-kill it.

No raw audit rows, synthetic secrets or session credentials are saved in project evidence. Retain only redacted result summaries. Production retention, viewer grants, live-data handling, log collectors, deployment and independent reviews remain deferred. B018 is outside this work.
