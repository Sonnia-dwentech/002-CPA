# B025 — Local recovery execution evidence

Date: 21 October 2026 (Atlantic/Reykjavik). **Approved and Done for verified local backup/restore scope.**

User “Start B025” after accepting B024. Continued the explicit local-only staging rehearsal and prior retain-data instruction. Prepared [runbook](../../deployments/local-rehearsal/recovery.md) and executed [recovery runner](../../backend/check_local_recovery.py). No hosted retention duration, RPO/RTO or schedule invented; local snapshot fidelity and measured recovery are the limited success criteria.

## Actual checks

The main runner exited 0 with seven groups; a supplementary check on the same retained restore target passed the audit sequence and restored trigger checks. The reusable runner now includes that check. [Combined eight-group results](B025-local-recovery-checks.json):

- Backup and source fingerprints use the same exported read-only snapshot.
- Archive checksum verified; single-transaction restore into a new empty, separate database.
- All cpa/cpa_meta table counts and hashes match; migration reapplication is a no-op.
- Restored sessions invalidated; new independent credentials and synthetic login/logout work.
- Dashboard permissions/filters preserved; runtime DDL/membership edits denied.
- Failed pending migration rolls back table/data/history, leaving target fingerprints unchanged.
- Original B024 certificate-verified readiness returns 200 after the drill; no source writes or source service restart.
- Restored audit identity returns an ID above existing rows; membership disable/re-enable invalidates an issued target session through the restored trigger.

Backup: 20,959 bytes, 0.703 seconds. Restore/comparison: 0.313 seconds. Initial complete drill: 4.640 seconds; supplementary checks outside that timing. Not workload-scale recovery targets or application switch-over timing. Snapshot digests were compared before destination-only session and sequence tests, so final target session/sequence state intentionally differs.

Full local checks passed: 69 source/config files, dependencies, 68 backend tests, 5 runner tests, dashboard contract checks and three frontend type checks. Application logic was unchanged; only the new recovery runner was added. Original source was selected by recorded name/label/database scope and read-only snapshot. Source secrets were read only within the authorised local execution; no values emitted.

## Retained resources and limits

[Runtime record](B025-runtime.json) identifies the protected backup and new cpa-b025-restore-93b97d5103854c2d8088d75e450de298 container/volume. Source cpa-b024-rehearsal-a26c9d24991042afa32ea1f9b5a20fac is unchanged. Backup, secrets and migration probe remain under user-only ACLs. No data/container cleanup, cloud operation, trust-store change or schedule. The local backup is ACL-restricted, not separately encrypted or off-machine.

No application rollback was executed: only one verified frontend build is recorded. The runbook separates failed-migration transaction rollback, recovery from a committed change and application artifact rollback. Hosted objectives, independent review and real-data policy remain deferred. B025 is approved and Done for local recovery; B026 remains unstarted. [Pre-change records](B025-before.zip).


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.
