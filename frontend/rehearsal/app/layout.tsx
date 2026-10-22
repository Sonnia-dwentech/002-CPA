import "../../app/globals.css";
export const metadata = { title: "CPA local staging rehearsal — synthetic only", robots: { index: false, follow: false } };
export default function Layout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body><main><p style={{padding:"16px 32px",margin:0,background:"#172944",color:"white"}}>LOCAL STAGING REHEARSAL · Synthetic sign-in only · No cloud services</p>{children}</main></body></html>;
}
