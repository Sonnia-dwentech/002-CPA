import type { Metadata } from "next";
import Shell from "../components/Shell";
import EntryJourney from "../components/EntryJourney";
import "./globals.css";
export const metadata: Metadata = {
  title: { default: "Command Centre · CPA", template: "%s · CPA" },
  description: "CPA personal workspace. Save and develop your ideas.",
  robots: { index: false, follow: false },
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en" data-scroll-behavior="smooth"><body><EntryJourney><Shell>{children}</Shell></EntryJourney></body></html>;
}
