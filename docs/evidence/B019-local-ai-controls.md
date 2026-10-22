# B019 — Local AI configuration and usage controls

Date: 21 October 2026 (America/Los_Angeles). Status: Done; user approved the local scope on 21 October 2026.

Authority: user “Start B019”, after B018 approval and acceptance. Codex implemented the local baseline under G0-L; Justice remains nominated accountable owner. No independent review is claimed. [Pre-change records](B019-before.zip) preserve the prior tracker, decisions, guides, template and work-item pack.

## Implementation and contract

[ai_controls.py](../../backend/app/ai_controls.py) accepts an explicit settings mapping and a trusted B018 mock adapter. It never loads `.env`, constructs a live provider, reads credentials from the machine or modifies the normal HTTP application. No packages were added.

| Setting | Local contract |
| --- | --- |
| LIVE_AI_ENABLED | Missing defaults to `false`; only exact strings `true` and `false` are valid. Other values reject the request before the mock transport. |
| OPENAI_MODEL | For requested live mode: required, 1–128 characters, restricted identifier syntax. Presence/syntax does not establish an approved or available model. |
| OPENAI_API_KEY | For requested live mode: required nonblank string without whitespace. This is a presence check, not credential verification. No real key is supplied or retained by the configuration result. |
| MAX_AI_RUN_COST | For requested live mode: required positive finite decimal string, at most 12 integer and 8 fractional digits. Zero, negatives, exponents, nonfinite and malformed values reject. No currency, actual ceiling or pricing policy is selected. |

Invalid settings produce `configuration_invalid` without calling the adapter. Complete live settings produce `live_unavailable`, also without calling it. **Live AI remains unconditionally disabled** in this baseline. No setting can authorise spend. The numeric format limit is input validation, not an approved business budget. Actual model choice, credential authority, budget currency/ceiling, pricing, per-user quotas, concurrency reservations, retry limits and alerts remain O-07 decisions before future live enablement. No paid transport exists here.

With live mode false, only the explicitly injected mock adapter runs. There is no live-to-mock fallback after refusal or configuration failure. Test injection is trusted code, not a security sandbox for arbitrary Python transports. Settings are inspected at construction and raw values discarded; configuration changes require a new controls instance.

## Usage hook

Each returned result carries an ephemeral `UsageRecord`: UUID actor/request/resource IDs, fixed purpose `synthetic_assessment`, UTC timestamp, elapsed monotonic seconds, outcome, synthetic model and token counts when known. Blocked calls have unavailable model/tokens. Cost is always `None` with `cost_status=unknown`, including successful mock results; no fabricated price or actual-billing claim is made.

Provider failure, timeout, refusal and malformed outcomes carry safe usage metadata without raw exceptions, prompt text, provider content or credentials. Successful draft content remains in the separate B018 outcome; callers must not log whole result objects. IDs are sensitive metadata and must remain within trusted access boundaries. There is no new logging sink, database store, UI or retention period. Usage exists only for the caller's in-memory result lifetime. Invalid caller input raises a fixed error; caller cancellation propagates without producing a completed usage record. Persistent audit integration and cancellation accounting are future work.

## Verification

From `backend`:

```powershell
.\.venv312\Scripts\python.exe -B -m unittest discover -s tests -v
```

Result: **54 tests passed**, exit code 0, on the existing Python 3.12.14 environment. This includes 42 previous backend tests and [12 new control tests](../../backend/tests/test_ai_controls.py).

New checks cover each missing live requirement, malformed switches, invalid budgets/model/credential fields, complete configuration remaining blocked, zero transport calls on denial, mock labelling, usage IDs/timing/token metadata, unknown cost, unavailable usage, failure outcomes, secret/prompt exclusion and settings snapshot behaviour. The complete-live-settings test patches network connection to fail and asserts it was unused. Existing loopback startup/shutdown also passed; no server was left running. PostgreSQL integration checks were not rerun because this change has no database path.

## Acceptance boundary

The B019 completion check is demonstrated for this local, always-disabled live baseline. This does not deliver operational quota/budget enforcement for an enabled provider, retained production telemetry or full AC-F19-01/02. O-07 remains open; no actual model, budget, secret, currency or live-call approval is inferred. No GitHub activity, deployment, real-client data or external provider call occurred. B019 is approved for this local scope. B020 remains Not started and its remote prerequisites remain unresolved.


## Local approval — 21 October 2026

User: “Approve B019”. The tested local configuration/usage baseline is accepted and B019 is Done. Retained evidence: 54 backend tests passed, including 12 B019 tests. No tests rerun for this documentation-only update. Live AI remains disabled; O-07 live model/budget/quota/enablement decisions remain Open. No independent review or deployment sign-off inferred. B020 remains Not started. [Pre-approval records](B019-before-acceptance.zip) preserve the previous state.
