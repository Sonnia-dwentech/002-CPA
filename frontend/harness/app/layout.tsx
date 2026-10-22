import "../../app/globals.css";
export const metadata = { title: "CPA isolated synthetic verification", robots: { index: false, follow: false } };
export default function Layout({ children }: { children: React.ReactNode }) {
  return <html lang="en" data-scroll-behavior="smooth"><body><main>{children}</main></body></html>;
}
