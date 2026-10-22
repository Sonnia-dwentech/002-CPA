# B025 — Local backup, restore and rollback runbook

Date: 21 October 2026 (Atlantic/Reykjavik). Scope: user-selected local foundation after B024 acceptance. **In review for local acceptance.** No cloud backup policy, production recovery objective or scheduled automation is established.

## Retention and recovery baseline

The earlier instruction to retain test data applies: keep the snapshot, protected credentials, original B024 database and new B025 restore database until explicit user direction. Justice is the existing nominated accountable owner; no other operator assignment is inferred. Backup and restore state are wholly synthetic and use the same user-only filesystem ACL restriction as B024. Do not upload them or put them in ordinary evidence files/source control. The .local directory is ignored by the root .gitignore.

This is one manual snapshot and a measured restore drill, not a recurring backup schedule. Recovery point is the exported PostgreSQL snapshot; later transactions are outside it. No point-in-time/WAL archive recovery is configured. Hosted retention, backup cadence, RPO/RTO, off-machine copy, encryption/key ownership and alerting remain undecided. Keeping backup and database on this workstation does not cover loss of the workstation/disk. No automatic cleanup or alerts are scheduled.

## Verified result

[Machine-readable results](../../docs/evidence/B025-local-recovery-checks.json) record archive checksum, bytes, snapshot time, table row counts/digests and measured durations. [Runtime record](../../docs/evidence/B025-runtime.json) identifies exact retained resources and protected paths without credentials.

The 20,959-byte PostgreSQL custom archive was taken from the recorded B024 container using a read-only REPEATABLE READ exported snapshot. Table fingerprints were collected from that same snapshot. `pg_dump --snapshot` produced a consistent archive while B024 stayed running. Source access was read-only; no source service restart, destructive drill or role/session change was performed.

Restoration used a newly created B025-labelled container, separate database cpa_b025_restore, named persistent volume and independent credentials. `pg_restore --single-transaction --exit-on-error --no-owner --no-acl` restored into an empty destination after checksum validation. No --clean option and no restore into B024. Role/password globals were not backed up; target ownership and runtime grants are established independently.

All application/migration table counts and digests matched the captured source snapshot before destination-only safety tests. Applying the existing migration set was a no-op. Restored sessions were then revoked before any restored runtime was used, preventing captured session state from becoming reusable access in a different environment. A fresh synthetic session was issued/tested/revoked only on the restore target. Dashboard visibility and filters, runtime permission limits, audit identity generation and membership-trigger revocation passed.

Measured backup duration: 0.703 seconds. Restore plus table comparison/migration verification: 0.313 seconds. Initial full drill: 4.640 seconds, excluding the later supplementary sequence/trigger check. These observations are for this small local fixture set and include no application switch-over; they are not guaranteed RPO/RTO or larger-dataset capacity evidence.

## Repeat the protected local drill

1. Verify B024-runtime.json identifies the intended synthetic rehearsal. The runner requires its exact B024 name pattern, label, database and credential scope. Docker must be running and the source's image already local. No image download is attempted.
2. From backend, run `.\.venv312\Scripts\python.exe -B check_local_recovery.py` with the installed Docker CLI on PATH. The tool requires permission to read protected local state and operate Docker. No password belongs in command arguments or chat.
3. Each invocation produces a new protected backup directory and a new retained restore container/volume. Do not repeat just to view the existing result. Preserve the current records before a deliberate new drill; runtime/check JSON files describe the latest attempt.
4. Inspect the exit status and recorded checks. A failed run retains partial archive/target state; an existing file or container is not success evidence. Resolve the cause without restoring into the source or deleting retained resources automatically.
5. For a later recovery from an older saved archive, first select its manifest, verify the SHA-256, authorise a new empty target and establish matching PostgreSQL/runtime/schema compatibility. Reapply the same role/credential/session isolation and comparison checks; do not assume this latest-snapshot runner is an arbitrary restore selector.

The runner stores the dump and snapshot manifest under user-only ACLs before creating the destination. Runtime credentials stay in protected private state. Ordinary evidence contains resource names, digests and counts only. PostgreSQL custom archives are not independently encrypted by this procedure; ACL access control is the implemented local boundary. Do not treat this as an approved hosted backup security design.

## Migration rollback assessment

The verified restore target was given a copied migration directory with an additional synthetic migration that creates a probe table and inserts duplicate primary keys. The expected error rolled back the new schema/data/history transaction. No probe table remained and all pre-probe table fingerprints remained identical. The failing SQL file is retained in protected drill state as evidence. No B024/source migration was executed.

This proves transactional rollback of a failed pending migration in this runner. It does not prove arbitrary committed schema changes can be undone. For an already committed migration, review forward repair versus recovery into another database. Record data loss since the chosen backup, schema/application compatibility, writer handling and switching authority before changing a running service. Never delete migration history to hide a committed change and never invent a generic down-migration.

## Application rollback is separate

B024 has one verified production frontend build, identified in B024-runtime.json. There is no demonstrated previous deployed release to roll back to. No application artifact rollback, database switch-over or service outage was performed in B025.

Before an actual application rollback: retain a separately identified previous artifact and source/runtime manifest; verify compatibility with the current database schema; test that artifact on separate ports against an approved isolated restore; obtain the existing release authority; switch only the intended service and verify readiness/authentication/direct denial. Do not rebuild or overwrite the running .next directory as a rollback method. If incompatible with the current schema, stop and choose an approved forward repair or database recovery plan rather than assuming application rollback also restores data.

## Handoff

B025's local backup/restore and rollback assessment are approved and Done for the verified local scope. B026 has not started. Source rehearsal and B022 remain retained; the B025 target is for recovery verification, not connected to either running application. Global TLS trust is unchanged. Hosted backup/release/operations requirements remain deferred under existing ledgers.


## B025 local recovery approved — 21 October 2026

User: “Approve B025”. B025 is Done for the verified local backup/restore and rollback assessment. Existing eight recovery/control groups and full local-runner evidence retained; no tests rerun for documentation-only acceptance. Earlier pending-acceptance wording is superseded for this scope. Hosted backup policy, cadence and recovery targets, off-machine recovery and independent review remain deferred. Backup, restored database, secrets and existing services were left untouched; no cleanup performed. B026 remains unstarted. Prior records: docs/evidence/B025-before-acceptance.zip.
