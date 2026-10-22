import Link from "next/link";
export default function NotFound() {
  return <section className="panel unavailable-panel"><p className="eyebrow">PAGE NOT FOUND</p>
    <h1>This page is not part of the workspace</h1><p>Use the navigation or return to the Command Centre.</p>
    <Link className="primary-link" href="/">Return to Command Centre</Link></section>;
}
