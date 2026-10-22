"use client";
import { useState } from "react";
import { useAccount } from "./AccountContext";
export default function ReferenceSessionBadge() {
  const user = useAccount();
  const [message, setMessage] = useState("");
  const [busy, setBusy] = useState(false);
  async function logout() {
    setBusy(true);
    try {
      const response = await fetch("/api/account/logout", { method: "POST" });
      if (!response.ok) throw new Error();
      window.dispatchEvent(new Event("cpa-account-session"));
    } catch { setMessage("Sign-out failed. Please retry."); }
    finally { setBusy(false); }
  }
  return <><span className="reference-session-link" role="status">{message || user.email}<small className="account-role">{user.role === "admin" ? "Administrator" : "External user"}</small></span><button className="secondary-button" disabled={busy} onClick={logout}>{busy ? "Signing out…" : "Sign out / switch account"}</button></>;
}
