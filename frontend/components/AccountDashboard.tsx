"use client";
import { useEffect, useState } from "react";
import { useAccount } from "./AccountContext";
type Idea = { id: string; title: string; description: string; created_at: number };
export default function AccountDashboard() {
  const user = useAccount();
  const [ideas, setIdeas] = useState<Idea[] | null>(null);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(false);
  async function load() {
    setMessage(""); setIdeas(null);
    try {
      const response = await fetch("/api/account/ideas", { cache: "no-store" });
      if (response.status === 401) window.dispatchEvent(new Event("cpa-account-session"));
      if (!response.ok) throw new Error();
      const data = await response.json(); setIdeas(data.ideas);
    } catch { setMessage("Could not load your work. Please retry."); }
  }
  useEffect(() => { void load(); }, []);
  async function save(event: React.FormEvent) {
    event.preventDefault(); if (busy) return; setBusy(true); setMessage("");
    try {
      const response = await fetch("/api/account/ideas", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ title, description }) });
      const data = await response.json();
      if (response.status === 401) window.dispatchEvent(new Event("cpa-account-session"));
      if (!response.ok) { setMessage(data.message ?? "Could not save. Please retry."); return; }
      setIdeas(data.ideas); setTitle(""); setDescription(""); setMessage("Your idea is saved.");
    } catch { setMessage("Save could not be confirmed. Refresh your list before retrying."); }
    finally { setBusy(false); }
  }
  return <div className="account-dashboard">
    <div className="page-heading"><div><p className="eyebrow">YOUR PERSONAL WORKSPACE</p><h1>My dashboard</h1><p>Welcome, {user.name}. Your ideas, saved and ready to develop.</p></div><span className="preview-pill">External user</span></div>
    <section className="panel account-summary"><div><p className="eyebrow">SAVED IDEAS</p><strong>{ideas === null ? "—" : ideas.length}</strong><p>Ideas in your account</p></div><div><h2>A place for your next idea</h2><p>Capture a title and some notes. Your dashboard updates from the work you save.</p></div></section>
    <div className="account-work-grid"><form className="panel" onSubmit={save} aria-busy={busy}><h2>Capture an idea</h2>
      <div className="account-field"><label htmlFor="idea-title">Title</label><input id="idea-title" value={title} onChange={e => setTitle(e.target.value)} maxLength={160} required disabled={busy} placeholder="What would you like to build?" /></div>
      <div className="account-field"><label htmlFor="idea-description">Notes</label><textarea id="idea-description" rows={6} value={description} onChange={e => setDescription(e.target.value)} maxLength={5000} disabled={busy} placeholder="The problem, who it helps, or a first thought…" /></div>
      <button className="primary-link" disabled={busy}>{busy ? "Saving…" : "Save idea"}</button>
    </form><section className="panel"><div className="account-list-heading"><h2>Your ideas</h2><button className="secondary-button" disabled={busy} onClick={load}>Refresh</button></div>
      {ideas === null ? <p>{message ? "Your work is unavailable right now." : "Loading your work…"}</p> : ideas.length === 0 ? <div className="account-empty"><h3>Your first idea starts here.</h3><p>Save an idea to see it in your dashboard. Only your own work appears here.</p></div> : <ul className="account-ideas">{ideas.map(idea => <li key={idea.id}><h3>{idea.title}</h3><p>{idea.description}</p><small>Saved {new Date(idea.created_at).toLocaleDateString("en-GB")}</small></li>)}</ul>}
    </section></div><p role="status" className="account-status">{message}</p>
  </div>;
}
