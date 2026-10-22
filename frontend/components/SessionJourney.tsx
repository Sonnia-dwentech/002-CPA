"use client";
import { useEffect, useRef, useState } from "react";

// Only the separately launched harness supplies enabled=true. The normal app
// has no issuance route, backend fixture configuration or synthetic-login flag.
export default function SessionJourney({ enabled = false }: { enabled?: boolean }) {
  const [signedIn, setSignedIn] = useState(false);
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState("Checking session…");
  const [record, setRecord] = useState(false);
  const result = useRef<HTMLParagraphElement>(null);
  const sequence = useRef(0);

  async function run(action: string, focus = true) {
    const current = ++sequence.current;
    setBusy(true);
    setRecord(false);
    try {
      const response = await fetch(`/api/session/${action}`, {
        method: action === "status" || action === "own" || action === "other" ? "GET" : "POST",
        credentials: "same-origin", cache: "no-store", redirect: "error",
      });
      if (current !== sequence.current) return;
      if (response.status === 401) {
        setSignedIn(false);
        setMessage("No valid session. Sign in to the synthetic fixture to continue. An expired or revoked session requires a new sign-in.");
      } else if (response.status === 403) {
        setMessage("Access denied. This action is not permitted.");
      } else if (response.status === 404) {
        setMessage("Record unavailable. It may not exist or you may not have access.");
      } else if (!response.ok) {
        setSignedIn(false);
        setMessage(action === "logout"
          ? "Sign-out not confirmed. The service is unavailable; retry sign-out when it recovers."
          : "Session service unavailable. Access cannot be verified. Try again.");
      } else {
        // Only fixed presentation messages are rendered, never backend text.
        setSignedIn(action !== "logout");
        setRecord(action === "own");
        setMessage(action === "logout" ? "Signed out. This session has been revoked."
          : action === "own" ? "Access allowed to your synthetic record."
          : "Signed in as the synthetic client fixture. This is not a real account.");
      }
    } catch {
      if (current !== sequence.current) return;
      setSignedIn(false);
      setMessage(action === "logout" ? "Sign-out not confirmed. Check the local service and retry."
        : "Session service unavailable. Access cannot be verified. Try again.");
    } finally {
      if (current === sequence.current) {
        setBusy(false);
        if (focus) requestAnimationFrame(() => result.current?.focus());
      }
    }
  }
  useEffect(() => {
    if (!enabled) return;
    void run("status", false);
    // Recheck on return to the page. Protected content is removed while checking.
    const check = () => { if (document.visibilityState === "visible") void run("status", false); };
    document.addEventListener("visibilitychange", check);
    return () => { ++sequence.current; document.removeEventListener("visibilitychange", check); };
  }, [enabled]);

  if (!enabled) return <section className="panel unavailable-panel">
    <h1>Sign-in is not available yet</h1>
    <p>Real account sign-in has not been configured. No credentials are collected by this preview.</p>
    <a className="primary-link" href="/">Return to Command Centre</a>
  </section>;

  return <section className="panel" style={{ maxWidth: 650, margin: "24px auto" }}>
    <p className="eyebrow">Isolated local verification · Synthetic data only</p>
    <h1>Session and access check</h1>
    <p>This separate test harness uses disposable PostgreSQL sessions and backend permissions.
      No password, provider or real account is used.</p>
    <p ref={result} tabIndex={-1} role="status" aria-live="polite">{busy ? "Checking access…" : message}</p>
    <p><strong>{!busy && signedIn ? "Synthetic session active" : "No verified session displayed"}</strong></p>
    {record && !busy && <div className="panel"><h2>Synthetic record</h2><p>Authorised fixture content. No client information.</p></div>}
    <div style={{ display: "flex", flexWrap: "wrap", gap: 16 }} aria-busy={busy}>
      {!signedIn && <button className="primary-link" disabled={busy} onClick={() => run("login")}>Sign in to synthetic fixture</button>}
      <button className="primary-link" disabled={busy} onClick={() => run("status")}>Check session</button>
      {signedIn && <>
        <button className="primary-link" disabled={busy} onClick={() => run("own")}>Open own fixture</button>
        <button className="primary-link" disabled={busy} onClick={() => run("other")}>Check other-client denial</button>
        <button className="primary-link" disabled={busy} onClick={() => run("privileged")}>Check privileged denial</button>
      </>}
      <button className="primary-link" disabled={busy} onClick={() => run("logout")}>Sign out</button>
    </div>
  </section>;
}
