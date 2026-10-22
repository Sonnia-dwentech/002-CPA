import Link from "next/link";
import { notFound } from "next/navigation";
import { modules } from "../../lib/modules";
import Icon from "../../components/Icon";
export const dynamicParams = false;
export function generateStaticParams() { return modules.filter(m => m.slug && m.slug !== "dashboard").map(m => ({ section: m.slug })); }
export async function generateMetadata({ params }: { params: Promise<{ section: string }> }) {
  const { section } = await params;
  return { title: modules.find(m => m.slug === section)?.name ?? "Page not found" };
}
export default async function ModulePage({ params }: { params: Promise<{ section: string }> }) {
  const { section } = await params;
  const item = modules.find(m => m.slug === section);
  if (!item || !item.slug) notFound();
  return <>
    <div className="page-heading"><div><p className="eyebrow">PLANNED WORKSPACE</p><h1>{item.name}</h1>
      <p className="page-description">{item.description}</p></div></div>
    <section className="panel unavailable-panel" aria-labelledby="unavailable-title">
      <span className="unavailable-icon"><Icon name={item.icon} /></span><span className="quiet-badge">Not available yet</span>
      <h2 id="unavailable-title">This workspace is still to come</h2>
      <p>You can explore its place in the navigation, but its workflow is not implemented. No records are loaded and no service is started from this page.</p>
      <div className="delivery-note"><span>Planned delivery</span><strong>{"phase" in item ? item.phase : "Foundation"}</strong><small>A scope label, not a scheduled release date.</small></div>
      <Link href="/" className="primary-link">Return to Command Centre <Icon name="arrow" /></Link>
    </section>
  </>;
}
