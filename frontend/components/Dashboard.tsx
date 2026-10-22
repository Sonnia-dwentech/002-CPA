"use client";
import { useEffect, useId, useRef, useState } from "react";
import { DashboardData, isDashboard, kinds, states, validFilters } from "../lib/dashboard";
import Icon from "./Icon";

type Filters = { kind: string; state: string; owner_id: string };
const emptyFilters: Filters = { kind: "", state: "", owner_id: "" };
export default function Dashboard({ enabled = false, apiBase = "/api", embedded = false }:
  { enabled?: boolean; apiBase?: string; embedded?: boolean }) {
  const [filters, setFilters] = useState<Filters>(emptyFilters);
  const [data, setData] = useState<DashboardData | null>(null);
  const [message, setMessage] = useState("Checking your local session…");
  const [busy, setBusy] = useState(enabled);
  const [signedIn, setSignedIn] = useState(false);
  const [updated, setUpdated] = useState<string | null>(null);
  const sequence = useRef(0);
  const active = useRef<AbortController | null>(null);
  const result = useRef<HTMLParagraphElement>(null);
  const id = useId();
  const connected = apiBase === "/api/reference";
  const Heading = embedded ? "h2" : "h1";
  function notify() { if (connected) window.dispatchEvent(new Event("cpa-reference-session")); }
  function params(values: Filters) {
    const p = new URLSearchParams();
    Object.entries(values).forEach(([key, value]) => { if (value) p.set(key, value); });
    return p;
  }
  function change(key: keyof Filters, value: string) {
    setFilters(current => ({ ...current, [key]: value })); setData(null);
    setMessage("Filters changed. Apply filters to update the references.");
  }
  async function load(p: URLSearchParams, focus = true) {
    const current = ++sequence.current;
    active.current?.abort(); active.current = new AbortController();
    setData(null); setBusy(true); setMessage("Loading references…");
    try {
      if (!validFilters(p)) throw new Error("filters");
      const response = await fetch(`${apiBase}/dashboard?${p}`, { cache: "no-store", credentials: "same-origin", redirect: "error", signal: active.current.signal });
      if (current !== sequence.current) return;
      if (response.status === 401) { setSignedIn(false); notify(); setMessage("Session expired or unavailable. Sign in again to view references."); return; }
      if (response.status === 403) { setMessage("Access denied. Dashboard access is not permitted."); return; }
      if (response.status === 422) throw new Error("filters");
      if (!response.ok) throw new Error("service");
      const value: unknown = await response.json();
      if (current !== sequence.current) return;
      if (!isDashboard(value)) throw new Error("service");
      setSignedIn(true); setData(value);
      setUpdated(new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", second: "2-digit", timeZone: "Atlantic/Reykjavik" }).format(new Date()));
      setMessage(value.status === "unavailable" ? "This reference type is not available. No count can be shown."
        : value.status === "empty" ? "No accessible references match these filters."
        : `${value.total} accessible synthetic ${value.total === 1 ? "reference matches" : "references match"} these filters.`);
    } catch (error) {
      if (current !== sequence.current) return;
      setMessage(error instanceof Error && error.message === "filters" ? "Check the filters. Owner must be a UUID."
        : "Could not load references. Counts are unavailable. Use Retry / refresh when the local service recovers.");
    } finally {
      if (current === sequence.current) { setBusy(false); if (focus) requestAnimationFrame(() => result.current?.focus()); }
    }
  }
  async function session(action: "login" | "logout") {
    const current = ++sequence.current; active.current?.abort(); setData(null); setBusy(true);
    setMessage(action === "login" ? "Signing in…" : "Signing out…");
    try {
      const response = await fetch(`${apiBase}/session/${action}`, { method: "POST", cache: "no-store", credentials: "same-origin", redirect: "error" });
      if (current !== sequence.current) return;
      if (action === "logout" && response.status === 401) {
        setSignedIn(false); setUpdated(null); notify(); setMessage("Session expired. Synthetic references are hidden."); return;
      }
      // The original verification harness may report an already-present session.
      if (action === "login" && response.status === 409) {
        const status = await fetch(`${apiBase}/session/status`, { cache: "no-store", credentials: "same-origin", redirect: "error" });
        if (current !== sequence.current) return;
        if (status.status === 200) { setSignedIn(true); notify(); await load(params(filters)); return; }
        if (status.status === 401) { setSignedIn(false); setMessage("Expired session cleared. Select Sign in again."); return; }
        throw new Error();
      }
      if (!response.ok) throw new Error();
      setSignedIn(action === "login"); notify();
      if (action === "login") { await load(params(filters)); return; }
      setUpdated(null); setMessage("Signed out. Synthetic references are hidden.");
    } catch { if (current === sequence.current) setMessage(action === "logout" ? "Sign-out not confirmed. Retry when the service recovers." : "Sign-in unavailable. Retry when the local service recovers."); }
    finally { if (current === sequence.current) { setBusy(false); requestAnimationFrame(() => result.current?.focus()); } }
  }
  function apply(values: Filters) {
    setFilters(values); setData(null);
    const p = params(values);
    window.history.replaceState(null, "", `${window.location.pathname}${p.size ? `?${p}` : ""}`);
    if (signedIn) void load(p);
    else setMessage("Filters cleared. Sign in to view synthetic references.");
  }
  useEffect(() => {
    if (!enabled) return;
    const p = new URLSearchParams(window.location.search);
    setFilters({ kind: p.get("kind") ?? "", state: p.get("state") ?? "", owner_id: p.get("owner_id") ?? "" });
    const current = ++sequence.current;
    active.current = new AbortController();
    void (async () => {
      try {
        const response = await fetch(`${apiBase}/session/status`, { cache: "no-store", credentials: "same-origin", redirect: "error", signal: active.current!.signal });
        if (current !== sequence.current) return;
        if (response.status === 401) { setSignedIn(false); setMessage("Sign in to view synthetic references."); setBusy(false); notify(); return; }
        if (!response.ok) throw new Error();
        setSignedIn(true); notify(); await load(p, false);
      } catch {
        if (current === sequence.current) { setMessage("Local service unavailable. Try signing in again when it recovers."); setBusy(false); }
      }
    })();
    return () => { ++sequence.current; active.current?.abort(); };
    // The initial URL supplies filters; explicit submissions update them.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [enabled, apiBase]);
  if (!enabled) return <section className="panel"><h2>Reference dashboard</h2><p>Not connected. Sign-in and record queries are available only in the isolated synthetic verification harness.</p></section>;
  return <div className={`dashboard-page ${connected ? "dashboard-connected" : ""}`}>
    <header className="page-heading"><div><p className="eyebrow">{connected ? "LOCAL WORKSPACE · SYNTHETIC DATA" : "ISOLATED LOCAL VERIFICATION · SYNTHETIC DATA ONLY"}</p>
      <Heading>Reference dashboard</Heading><p>Explore the reference metadata you are permitted to view.</p></div>
      <div className="dashboard-session"><span className={`reference-session-pill ${signedIn ? "is-active" : ""}`}>{signedIn ? "Synthetic session active" : busy ? "Checking session…" : "Signed out"}</span>
        {!signedIn && <button className="primary-link" disabled={busy} onClick={() => session("login")}>Sign in to synthetic fixture</button>}
        {signedIn && <button className="secondary-button" disabled={busy} onClick={() => session("logout")}>Sign out</button>}</div></header>
    <div className="reference-notice"><Icon name="shield" /><p>Connected to local synthetic records. Real accounts, business metrics and live AI remain unavailable.</p></div>
    <form className="panel dashboard-filters" onSubmit={event => { event.preventDefault(); apply(filters); }}>
      <div className="reference-filter-field"><label htmlFor={`${id}-kind`}>Reference type</label>
      <select id={`${id}-kind`} disabled={busy || !signedIn} value={filters.kind} onChange={e => change("kind", e.target.value)}>
        <option value="">All enabled types</option>{kinds.map(k => <option key={k} value={k}>{k.replaceAll("_", " ")}</option>)}</select></div>
      <div className="reference-filter-field"><label htmlFor={`${id}-state`}>State</label>
      <select id={`${id}-state`} disabled={busy || !signedIn} value={filters.state} onChange={e => change("state", e.target.value)}>
        <option value="">All states</option>{states.map(s => <option key={s}>{s}</option>)}</select></div>
      <div className="reference-filter-field"><label htmlFor={`${id}-owner`}>Owner UUID <span>(optional)</span></label>
      <input id={`${id}-owner`} disabled={busy || !signedIn} value={filters.owner_id} onChange={e => change("owner_id", e.target.value)} placeholder="All accessible owners" spellCheck={false} autoComplete="off" /></div>
      <div className="reference-filter-actions"><button className="primary-link" disabled={busy || !signedIn}>Apply filters</button>
        <button type="button" className="secondary-button" disabled={busy} onClick={() => apply(emptyFilters)}>Clear filters</button></div>
    </form>
    <div className="reference-quick-filters" aria-label="Quick reference filters">
      <span>Quick view</span>{[["", "All references"], ["idea", "Ideas"], ["dossier", "Dossiers"]].map(([kind, label]) =>
        <button key={label} type="button" className={filters.kind === kind && !filters.state && !filters.owner_id ? "is-selected" : ""} disabled={busy || !signedIn}
          onClick={() => apply({ ...emptyFilters, kind })}>{label}</button>)}
    </div>
    <p ref={result} tabIndex={-1} role="status" aria-live="polite">{message}</p>
    <div className="dashboard-cards" aria-busy={busy}>
      <section className="panel"><h2>Visible references</h2><strong className="dashboard-count">{data?.total ?? "—"}</strong><p>{data?.total === null || !data ? "Count unavailable" : "Accessible records matching the applied filters"}</p></section>
      <section className="panel"><h2>Business metrics</h2><strong>Not available</strong><p>Revenue, research activity and review metrics are not connected.</p></section>
    </div>
    <section className="panel dashboard-list" aria-busy={busy}><div className="reference-list-heading"><h2>Accessible references</h2>
      <button className="secondary-button" disabled={busy || !signedIn} onClick={() => load(params(filters))}><Icon name="arrow" />Retry / refresh</button></div>
      {updated && signedIn && <p className="reference-updated">Last successful refresh {updated} · Reykjavik time</p>}
      {data?.status === "ok" ? <ul>{data.records.map(r => <li key={r.id}><span className="module-icon"><Icon name={r.kind === "dossier" ? "report" : "idea"} /></span>
        <div className="reference-record-body"><strong>{r.kind.replaceAll("_", " ")} reference</strong><span className="quiet-badge">{r.state}</span>
        <span>Reference <code>{r.id}</code></span><span>Owner <code>{r.owner_id}</code></span></div></li>)}</ul>
        : <div className="reference-empty"><Icon name="library" /><p>{busy ? "Loading references…" : !signedIn ? "Sign in to explore the local reference collection." : data?.status === "empty" ? "No matching references. Clear the filters or choose another view." : "No reference list available."}</p></div>}
    </section>
    <section className="reference-deferred"><strong>Foundation preview</strong><p>References are metadata-only synthetic fixtures. Idea editing, research, scanning and voice workflows are planned.</p></section>
  </div>;
}
