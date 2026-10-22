# B018 local AI adapter contract

Date: 21 October 2026 (America/Los_Angeles). Status: local contract and implementation approved and accepted by user on 21 October 2026; B018 Done.

Authority: the user selected “Start B018”. Codex is the executor; Justice remains the nominated accountable owner. This selection authorises the local adapter definition and mock tests under G0-L. The user subsequently said “Approve and accept B018”, accepting these local implementation choices; no independent technical sign-off is claimed. B017 is accepted. Broad architecture and live-provider decisions remain deferred.

## Contract

- `AssessmentRequest`: UUID request, actor and resource identifiers plus a nonempty prompt of at most 8,000 characters. Context must already be authorised by the caller; identifiers are traceability, not proof of permission. There is no HTTP entry point.
- `Provider.generate(request)`: asynchronous transport interface returning a `ProviderReply`. B018 supplies wholly synthetic implementations in tests. There is no SDK, provider factory, environment credential lookup, live transport or fallback.
- `MockAdapter(provider, timeout_seconds=...)`: explicitly mock-labelled composition. Timeout must be positive and finite; tests choose their own short deadline. Cancellation-cooperative asynchronous transports are required. Blocking or cancellation-suppressing transports cannot be bounded by this wrapper and are outside its contract. No production deadline or retry policy is selected.
- `Outcome`: preserves caller IDs, mock provider/model identifiers, prompt version, synthetic token usage when known, and unknown cost as `None`. Missing tokens stay `None`. Counts must be nonnegative integers; booleans are rejected.
- Outcomes are `draft`, `timeout`, `refused`, `malformed_output` or `provider_error`. Only `draft` carries validated content. Refusal overrides any accompanying body. Invalid requests raise a fixed `ValueError` before calling the transport. Caller cancellation propagates.

## Versioned synthetic output

`cpa.synthetic-assessment.v1` is a foundation fixture schema, not the final F06 dossier schema. Exactly four JSON fields are accepted:

| Field | Rule |
| --- | --- |
| schema_version | Exactly `cpa.synthetic-assessment.v1` |
| summary | Nonblank string, at most 2,000 characters |
| assumptions | List of at most 20 nonblank strings, each at most 500 characters |
| evidence_kind | Exactly `synthetic` |

The body is limited to 16,384 UTF-8 bytes. Duplicate fields, unknown fields, invalid types, unsupported versions and invalid provenance fail validation. Partially valid output is rejected as a whole; no salvage or automatic retry is implemented. Prompt identifier `cpa.synthetic-prompt.v1` names the synthetic test instruction in source, not a production assessment prompt.

Validated content always has `status=draft`. Model text claiming approval remains untrusted text; an approval field is rejected. The adapter cannot write a human decision or mutate a saved idea because it has no persistence dependency. Future renderers must safely render untrusted text; no browser rendering is added here.

## Disclosure and scope

The adapter emits no logs and returns fixed error codes without provider bodies, refusal explanations, exception strings or prompts. Payload fields are omitted from dataclass representations. Successful content is intentionally available to its authorised caller and must not be indiscriminately serialised into logs. Test injection is trusted code, not a sandbox for arbitrary transports.

Fixtures are wholly synthetic source-code test data, maintained with the test suite; there is no runtime fixture store or database cleanup requirement. No real research or client records are used. Full F06 fields, evidence grading, evaluation thresholds, actual OpenAI implementation and stored-idea integration remain later work. O-07 live models/budgets/configuration remains open at B019 and later checkpoints. B018 does not establish full AC-F06-01/02 end-to-end completion, live safety, deployed readiness or formal review.
