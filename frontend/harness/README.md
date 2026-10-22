# B016 isolated synthetic sign-in verification

This is a separate Next.js application. It is never mounted by the normal frontend. It shares `components/SessionJourney.tsx` with the normal `/sign-in` unavailable page, but only this harness enables the synthetic journey and supplies cookie/server routes.

No real login, password, MFA, client data or identity provider is present. The cookie configuration is approved for loopback HTTP testing only. It is not a deployment template.

## Run all automated integration checks

Use the existing installed dependencies and local `postgres:17` image. No package installation or image pull is required or allowed:

```powershell
Set-Location 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\backend'
python -B check_local_browser.py
```

The runner checks that ports 3100 and 8100 are free, creates a new disposable PostgreSQL container, applies existing migrations and runs B012–B014 checks. It starts an isolated backend at 127.0.0.1:8100 and this frontend at 127.0.0.1:3100, then verifies cookie/session/permission behaviour. A random harness key is passed through process environment only. The fixture-issuance endpoint requires that key and always selects one fixed synthetic client; no browser-supplied role/account is trusted.

The normal frontend at port 3000 and backend at port 8000 are separate. The runner does not stop existing listeners to take their ports. Docker named-pipe access and Next child-process spawning require appropriate local execution permission on this Windows host.

## Browser review

```powershell
python -B check_local_browser.py --serve
```

After the automated checks pass, open **http://127.0.0.1:3100/**. Use:

1. **Sign in to synthetic fixture**.
2. **Open own fixture** — displays labelled authorised synthetic content.
3. **Check other-client denial** — generic unavailable record, no restricted data.
4. **Check privileged denial** — denied pending approved MFA.
5. **Sign out**, then **Check session** — session is revoked.

Keyboard activation and focus on each result are supported. A service outage hides protected content and reports unverified access; failed sign-out is explicitly unconfirmed.

To finish from a second PowerShell window:

```powershell
New-Item -ItemType File -Force 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA\docs\evidence\B016-stop'
```

The runner stops only its own child process tree and backend thread, removes its container and discards tmpfs data. It also stops automatically after 20 minutes. Avoid force-killing the runner: its `finally` cleanup needs to execute. Raw credentials are not printed or saved.

Strict type checking:

```powershell
Set-Location 'C:\Users\hp.DESKTOP-KVH15G5\Documents\002 CPA'
node frontend/node_modules/typescript/bin/tsc --noEmit -p frontend/harness
```

## Limits

Real sign-in remains unavailable at http://127.0.0.1:3000/sign-in. The normal app has no synthetic login/API proxy routes. B016 tests actual persisted sessions and backend permissions, but synthetic identity issuance cannot establish human authentication. Future deployment needs an approved identity adapter, account lifecycle, Secure cookies over HTTPS, production connection lifecycle, MFA and independent review.


## B022 local dashboard preview

B022 is approved and Done for verified local synthetic reference metadata. Preview: http://127.0.0.1:3100/dashboard. It connects the isolated session harness to B021 stored queries; the normal app stays disconnected. Evidence: docs/evidence/B022-local-dashboard-ui.md (project root). The retained container and preview remain running by user preference. Future database checks retain containers by default; tmpfs contents are not durable across container stop/reboot. The B022-stop marker ends preview servers only when requested. B023 has not started.


## B022 local deliverable approved — 21 October 2026

User: “Approve B022”. B022 is Done for the verified local synthetic-reference dashboard UI and isolated query connection. Existing full local runner, PostgreSQL/BFF and browser verification evidence is retained; no tests rerun for this documentation-only approval. Earlier pending-acceptance wording is superseded. B023 remains unstarted. Preview processes and retained database were left untouched; no cleanup performed. Business metrics, normal application data integration, GitHub/RCI-01 and deployment remain deferred. This records user acceptance, not independent code review. Pre-approval records: docs/evidence/B022-before-acceptance.zip.
