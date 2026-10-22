"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { modules } from "../lib/modules";
import Icon from "./Icon";
import ReferenceSessionBadge from "./ReferenceSessionBadge";
import { useAccount } from "./AccountContext";
import { dashboardFor } from "../lib/account-navigation";

export default function Shell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const user = useAccount();
  const dashboard = { slug: dashboardFor(user.role).slice(1), name: user.role === "admin" ? "Administrator dashboard" : "My dashboard", icon: "grid" as const };
  const navigation = user.role === "admin" ? [dashboard] : [dashboard, ...modules.filter(item => item.slug && item.slug !== "dashboard")];
  const [open, setOpen] = useState(false);
  const toggle = useRef<HTMLButtonElement>(null);
  const previous = useRef(pathname);
  useEffect(() => {
    if (previous.current !== pathname) {
      previous.current = pathname;
      setOpen(false);
      document.getElementById("main-content")?.focus();
    }
  }, [pathname]);
  const current = navigation.find(m => `/${m.slug}` === pathname);
  return <div className={`workspace ${user.role === "admin" ? "workspace-admin" : "workspace-personal"}`}>
    <a className="skip-link" href="#main-content">Skip to content</a>
    <aside className="sidebar" onKeyDown={event => {
      if (event.key === "Escape" && open) {
        setOpen(false); toggle.current?.focus();
      }
    }}>
      <div className="brand">
        <span className="brand-mark" aria-hidden="true">C</span>
        <div><strong>DwenTech <span>CPA</span></strong><small>{user.role === "admin" ? "Administration console" : "Chief Product Architect"}</small></div>
        <button ref={toggle} className="menu-toggle" aria-expanded={open} aria-controls="primary-navigation"
          onClick={() => setOpen(!open)}><Icon name="menu" /><span>Menu</span></button>
      </div>
      <div className={`navigation-panel ${open ? "is-open" : ""}`} id="primary-navigation">
        <p className="nav-heading">{user.role === "admin" ? "Administration" : "Your workspace"}</p>
        <nav aria-label="Main navigation">
          {navigation.map(item => <Link href={`/${item.slug}`} key={item.slug}
            aria-current={pathname === `/${item.slug}` ? "page" : undefined}
            onClick={() => {
              if (pathname === `/${item.slug}`) {
                setOpen(false);
                document.getElementById("main-content")?.focus();
              }
            }}>
            <Icon name={item.icon} />
            <span className="nav-label"><span>{item.name}</span>{item.slug !== dashboard.slug && <small>Not available yet</small>}</span>
          </Link>)}
          {user.role === "admin" && <>
            <Link href="/admin#account-management"><Icon name="settings" /><span className="nav-label">User management</span></Link>
            <Link href="/admin#account-overview"><Icon name="shield" /><span className="nav-label">Access overview</span></Link>
          </>}
        </nav>
        <div className="sidebar-note"><Icon name="lock" /><div><strong>{user.role === "admin" ? "Administrator access" : "Personal workspace"}</strong>
          <p>{user.role === "admin" ? "Manage accounts and user access." : "Your saved ideas are private to your account."}</p></div></div>
      </div>
    </aside>
    <div className="workspace-body">
      <header className="topbar">
        <div className="breadcrumb"><span>{user.role === "admin" ? "Admin console" : "Workspace"}</span><span aria-hidden="true">/</span><strong>{current?.name ?? (pathname === "/admin" ? "Administration" : pathname === "/sign-in" ? "Sign in" : "Page not found")}</strong></div>
        <div className="session-state"><span className="preview-pill">Local account</span><ReferenceSessionBadge /></div>
      </header>
      <main id="main-content" tabIndex={-1}>{children}</main>
      <footer>Dwen Tech Ltd <span aria-hidden="true">·</span> CPA laboratory <span className="footer-right">Personal workspace · Saved locally</span></footer>
    </div>
  </div>;
}
