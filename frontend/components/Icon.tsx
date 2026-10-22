const paths: Record<string, string> = {
  home: "M3 10 12 3l9 7M5 9v12h5v-7h4v7h5V9",
  scan: "M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M8 12a4 4 0 1 0 8 0 4 4 0 1 0-8 0",
  idea: "M9 18h6m-6 3h6M8 15c-6-6 2-15 8-9 3 3 1 6-1 9v1H9v-1",
  book: "M3 4h7l2 2 2-2h7v15h-7l-2 2-2-2H3V4m9 2v15",
  message: "M3 4h18v13H9l-6 4V4m4 5h10M7 13h7",
  shield: "M12 3 3 7v5c0 5 9 9 9 9s9-4 9-9V7l-9-4m-4 9 3 3 5-6",
  grid: "M3 3h7v7H3V3m11 0h7v7h-7V3M3 14h7v7H3v-7m11 0h7v7h-7v-7",
  voice: "M9 5a3 3 0 0 1 6 0v7a3 3 0 0 1-6 0V5m-4 6v1a7 7 0 0 0 14 0v-1m-7 8v3m-4 0h8",
  chart: "M4 21V11h4v10m2 0V7h4v14m2 0V3h4v18",
  report: "M5 3h10l4 4v14H5V3m10 0v5h4M8 12h8m-8 4h8",
  library: "M3 4h4v17H3V4m7 0h4v17h-4V4m7 0 4 1-1 16-4-1 1-16",
  settings: "M9 3h6l1 4 4 1v7l-4 1-1 5H9l-1-5-4-1V8l4-1 1-4m0 9a3 3 0 1 0 6 0 3 3 0 1 0-6 0",
  arrow: "M5 12h14m-6-6 6 6-6 6",
  lock: "M6 10h12v11H6V10m3 0V6a3 3 0 0 1 6 0v4",
  menu: "M4 6h16M4 12h16M4 18h16",
};
export default function Icon({ name, className = "" }: { name: string; className?: string }) {
  return <svg className={className} width="20" height="20" viewBox="0 0 24 24" fill="none"
    stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"
    aria-hidden="true" focusable="false"><path d={paths[name] ?? paths.home} /></svg>;
}
