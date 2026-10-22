"use client";
import { useEffect, useRef, useState } from "react";
import { usePathname, useRouter } from "next/navigation";
import { AccountContext } from "./AccountContext";
import { accountDestination, dashboardFor, type AccountUser } from "../lib/account-navigation";

export default function EntryJourney({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const [intro, setIntro] = useState(true);
  const [admitted, setAdmitted] = useState(false);
  const [user, setUser] = useState<AccountUser | null>(null);
  const [mode, setMode] = useState<"login" | "signup">("login");
  const [busy, setBusy] = useState(false);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [adminSetup, setAdminSetup] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [checking, setChecking] = useState(true);
  const [message, setMessage] = useState("");
  const heading = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    const setup = new URLSearchParams(window.location.hash.slice(1)).get("admin-setup");
    if (setup && /^[A-Za-z0-9_-]{43}$/.test(setup)) { setAdminSetup(setup); setAdmitted(false); }
  }, []);
  useEffect(() => {
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const timer = window.setTimeout(() => setIntro(false), reduced ? 0 : 2200);
    return () => window.clearTimeout(timer);
  }, []);
  useEffect(() => {
    if (pathname === "/sign-in" || pathname === "/sign-up") {
      setAdmitted(false);
      setMode(pathname === "/sign-up" ? "signup" : "login");
    }
  }, [pathname]);
  useEffect(() => {
    if (!intro && !admitted) heading.current?.focus();
  }, [intro, admitted, mode]);
  useEffect(() => {
    let alive = true;
    void fetch("/api/account/status", { cache: "no-store" }).then(async response => {
      if (response.ok) {
        const data = await response.json();
        if (alive && pathname !== "/sign-in" && pathname !== "/sign-up" && !window.location.hash.includes("admin-setup=")) {
          setUser(data.user); setAdmitted(true);
        }
      }
    }).catch(() => {}).finally(() => { if (alive) setChecking(false); });
    return () => { alive = false; };
    // Restore only on initial load; explicit navigation to sign-in stays there.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  useEffect(() => {
    if (!admitted) return;
    let controller: AbortController | undefined;
    const check = async () => {
      controller?.abort();
      controller = new AbortController();
      const signal = controller.signal;
      try {
        const response = await fetch("/api/account/status", { cache: "no-store", signal });
        if (!signal.aborted && !response.ok) {
          setAdmitted(false);
          setUser(null);
          setEmail(""); setPassword(""); setConfirm(""); setName(""); setMode("login");
          setMessage(response.status === 401 ? "You’re signed out. Log in to continue." : "The local session service is unavailable. Please retry.");
        } else if (!signal.aborted) {
          const data = await response.json();
          if (!signal.aborted) setUser(data.user);
        }
      } catch { if (!signal.aborted) { setAdmitted(false); setUser(null); setMessage("Could not verify your session. Please retry."); } }
    };
    window.addEventListener("cpa-account-session", check);
    window.addEventListener("focus", check);
    return () => { controller?.abort(); window.removeEventListener("cpa-account-session", check); window.removeEventListener("focus", check); };
  }, [admitted]);
  const destination = user ? accountDestination(pathname, user.role) : pathname;
  useEffect(() => {
    if (admitted && user && destination !== pathname) router.replace(destination);
  }, [admitted, user, destination, pathname, router]);

  async function enter() {
    if (busy) return;
    if (mode === "signup" && password !== confirm) { setMessage("Your passwords do not match."); return; }
    setBusy(true); setMessage("");
    try {
      const response = await fetch(`/api/account/${mode}`, {
        method: "POST", cache: "no-store", credentials: "same-origin", redirect: "error",
        headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email, password, name, adminSetup }),
      });
      const data = await response.json();
      if (!response.ok) { setMessage(data.message ?? "Sign-in failed. Please retry."); return; }
      setPassword(""); setConfirm("");
      setAdminSetup("");
      setUser(data.user);
      router.replace(dashboardFor(data.user.role));
      setAdmitted(true);
    } catch { setMessage("Could not reach the account service. Please try again."); }
    finally { setBusy(false); }
  }

  if (intro || checking) return <main className="entry-splash" aria-label="Welcome to CPA">
    <div className="entry-orbit" aria-hidden="true"><span /><span /></div>
    <div className="entry-splash-content"><div className="entry-monogram" aria-hidden="true">C<span>·</span></div>
      <p className="entry-wordmark">DwenTech <strong>CPA</strong></p>
      <p className="entry-tagline">Ideas into possibility.</p>
      <div className="entry-progress" aria-hidden="true"><span /></div>
    </div>
    <button className="entry-skip" onClick={() => setIntro(false)}>Skip introduction →</button>
    <noscript>JavaScript is needed to open this local workspace.</noscript>
  </main>;

  if (admitted && user) {
    if (destination !== pathname) return <main className="entry-splash"><p role="status">Opening your dashboard…</p></main>;
    return <AccountContext.Provider value={user}>{children}</AccountContext.Provider>;
  }
  return <main className="entry-page">
    <section className="entry-story" aria-label="About CPA">
      <a className="entry-wordmark" href="/">DwenTech <strong>CPA</strong></a>
      <div className="entry-story-body"><p className="entry-kicker">CHIEF PRODUCT ARCHITECT</p>
        <h2>Every great product <br />starts with <br /><em>an idea.</em></h2>
        <p>Your space to explore, shape and build what comes next.</p>
        <div className="entry-story-line" /><span className="entry-story-caption">One workspace. A world of possibilities.</span>
      </div><small>Dwen Tech Ltd · CPA laboratory</small>
    </section>
    <section className="entry-access" aria-label="Workspace access">
      <div className="entry-card">
        <p className="entry-kicker">{adminSetup ? "ONE-TIME ADMINISTRATOR SETUP" : "CPA ACCOUNT ACCESS"}</p>
        <h1 ref={heading} tabIndex={-1}>{mode === "login" ? "Welcome back." : "Start your journey."}</h1>
        <p className="entry-subtitle">{mode === "login" ? "Log in to open your Command Centre." : "Create your account and start saving your ideas."}</p>
        {adminSetup && <p className="account-hint">Choose the email for your administrator account. Sign up for a new account, or log in to upgrade your existing account. This setup link can be used once.</p>}
        {!adminSetup && mode === "signup" && <p className="account-hint">New accounts have external-user access to their own workspace. Administrator access is assigned separately.</p>}
        <div className="entry-modes" aria-label="Choose access method">
          <button aria-pressed={mode === "login"} disabled={busy} onClick={() => { setMode("login"); setMessage(""); }}>Log in</button>
          <button aria-pressed={mode === "signup"} disabled={busy} onClick={() => { setMode("signup"); setMessage(""); }}>Sign up</button>
        </div>
        <form onSubmit={event => { event.preventDefault(); void enter(); }} aria-busy={busy}>
          {mode === "signup" && <div className="account-field"><label htmlFor="account-name">Your name</label><input id="account-name" autoComplete="name" required maxLength={80} value={name} onChange={e => setName(e.target.value)} disabled={busy} /></div>}
          <div className="account-field"><label htmlFor="account-email">Email</label><input id="account-email" type="email" autoComplete="username" required maxLength={254} value={email} onChange={e => setEmail(e.target.value)} disabled={busy} /></div>
          <div className="account-field"><label htmlFor="account-password">Password</label><input id="account-password" type="password" autoComplete={mode === "signup" ? "new-password" : "current-password"} required minLength={mode === "signup" ? 15 : 1} maxLength={128} value={password} onChange={e => setPassword(e.target.value)} disabled={busy} aria-describedby={mode === "signup" ? "password-hint" : undefined} /></div>
          {mode === "signup" && <><p id="password-hint" className="account-hint">Use at least 15 characters. A memorable passphrase works well.</p><div className="account-field"><label htmlFor="account-confirm">Confirm password</label><input id="account-confirm" type="password" autoComplete="new-password" required maxLength={128} value={confirm} onChange={e => setConfirm(e.target.value)} disabled={busy} /></div></>}
          <p className="entry-error" role="status">{message}</p>
          <button className="entry-submit" disabled={busy}>{busy ? "Opening workspace…" : mode === "login" ? "Log in →" : "Create account →"}</button>
        </form>
        <p className="entry-footnote">Your account and work are saved on this computer.<br />Online sync, email verification and password recovery are not connected yet.</p>
      </div>
      <p className="entry-access-footer">EXPLORE. SHAPE. BUILD.</p>
    </section>
  </main>;
}
