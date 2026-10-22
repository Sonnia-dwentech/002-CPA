"use client";
import { useEffect, useState } from "react";
import { useAccount } from "./AccountContext";
type Account = { id: string; name: string; email: string; role: string; enabled: number; created_at: number };
export default function Administration() {
  const user = useAccount();
  const [accounts, setAccounts] = useState<Account[] | null>(null);
  const [message, setMessage] = useState("Checking administrator access…");
  const [busy, setBusy] = useState(false);
  const [query, setQuery] = useState("");
  const [status, setStatus] = useState("all");
  const counts = accounts ? {
    total: accounts.length,
    external: accounts.filter(account => account.role === "external").length,
    active: accounts.filter(account => account.enabled).length,
    suspended: accounts.filter(account => !account.enabled).length,
  } : null;
  const visible = accounts?.filter(account => `${account.name} ${account.email}`.toLowerCase().includes(query.toLowerCase())
    && (status === "all" || (status === "active" ? !!account.enabled : !account.enabled)));
  async function load() {
    setAccounts(null); setBusy(true); setMessage("Loading accounts…");
    try {
      const response = await fetch("/api/account/users", { cache: "no-store" });
      const data = await response.json();
      if (!response.ok) { setMessage(data.message ?? "Could not load accounts."); return; }
      setAccounts(data.users); setMessage("");
    } catch { setMessage("Could not load accounts. Please retry."); }
    finally { setBusy(false); }
  }
  useEffect(() => { void load(); }, []);
  async function update(account: Account) {
    setBusy(true); setMessage("");
    try {
      const response = await fetch("/api/account/users", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ userId: account.id, enabled: !account.enabled }) });
      const data = await response.json();
      if (!response.ok) { setMessage(data.message ?? "Could not update account."); if (response.status === 401 || response.status === 403) setAccounts(null); return; }
      setAccounts(data.users); setMessage(account.enabled ? "Account suspended. Its sessions have ended." : "Account reactivated. The user can log in again.");
    } catch { setMessage("Update could not be confirmed. Refresh before retrying."); }
    finally { setBusy(false); }
  }
  return <div className="administrator-dashboard"><div className="page-heading admin-console-heading"><div><p className="eyebrow">CPA ADMINISTRATION CONSOLE</p><h1>Administrator dashboard</h1><p>Welcome, {user.name}. Oversee accounts and control workspace access.</p><a className="admin-console-action" href="#account-management">Manage users →</a></div><span className="admin-access-badge">Administrator access</span></div>
    <section id="account-overview" className="admin-summary-grid" aria-label="Account overview">
      {[["Total accounts", counts?.total], ["External users", counts?.external], ["Active accounts", counts?.active], ["Suspended accounts", counts?.suspended]].map(([label, count]) => <div className="panel admin-summary-card" key={label}><p>{label}</p><strong>{count ?? "—"}</strong></div>)}
    </section>
    <section id="account-management" className="panel"><div className="account-list-heading"><div><p className="eyebrow">USER MANAGEMENT</p><h2>Accounts and permissions</h2><p>Find a user, review their role, or change their access.</p></div><button className="secondary-button" disabled={busy} onClick={load}>Refresh accounts</button></div>
    <div className="admin-filters"><div className="account-field"><label htmlFor="admin-search">Find account</label><input id="admin-search" type="search" placeholder="Name or email" value={query} onChange={event => setQuery(event.target.value)} /></div><div className="account-field"><label htmlFor="admin-status">Account status</label><select id="admin-status" value={status} onChange={event => setStatus(event.target.value)}><option value="all">All accounts</option><option value="active">Active</option><option value="suspended">Suspended</option></select></div></div>
    <p role="status">{message}</p>
    {visible && <><p className="account-hint">{visible.length} {visible.length === 1 ? "account" : "accounts"} shown</p><ul className="account-ideas">{visible.map(account => <li key={account.id}><div className="account-list-heading"><div><h3>{account.name}{account.id === user.id && <span className="quiet-badge">You</span>}</h3><p>{account.email}</p><small>{account.role === "admin" ? "Administrator" : "External user"} · {account.enabled ? "Active" : "Suspended"}</small></div>{account.role !== "admin" && <button className="secondary-button" disabled={busy} onClick={() => update(account)}>{account.enabled ? "Suspend" : "Reactivate"}</button>}</div></li>)}</ul>{visible.length === 0 && <p>No accounts match your search.</p>}</>}
  </section></div>;
}
