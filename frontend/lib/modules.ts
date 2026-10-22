export const modules = [
  { slug: "", name: "Command Centre", icon: "home", description: "An overview of your product workspace." },
  { slug: "dashboard", name: "Your dashboard", icon: "grid", description: "Your saved ideas and personal workspace.", phase: "Foundation" },
  { slug: "opportunity-scanner", name: "Opportunity Scanner", icon: "scan", description: "Explore problems and opportunities against a defined research scope.", phase: "Advanced research" },
  { slug: "idea-studio", name: "Idea Studio", icon: "idea", description: "Develop an idea, examine the evidence and prepare a product dossier.", phase: "Idea Studio MVP" },
  { slug: "academic-research", name: "Academic Research", icon: "book", description: "Connect research findings with potential product applications.", phase: "Advanced research" },
  { slug: "discovery-enquiries", name: "Discovery Enquiries", icon: "message", description: "Review client enquiries and prepare responses for human approval.", phase: "Voice & Discovery" },
  { slug: "stress-testing", name: "Stress Testing", icon: "shield", description: "Challenge product assumptions and examine alternative scenarios.", phase: "Portfolio & stress testing" },
  { slug: "portfolio", name: "Portfolio", icon: "grid", description: "Follow products, decisions and evidence across their lifecycle.", phase: "Portfolio & stress testing" },
  { slug: "voice-studio", name: "Voice Studio", icon: "voice", description: "Capture a conversation with consent and review its transcript.", phase: "Voice & Discovery" },
  { slug: "business-modelling", name: "Business Modelling", icon: "chart", description: "Explore commercial assumptions and compare modelled scenarios.", phase: "Advanced research" },
  { slug: "reports", name: "Reports", icon: "report", description: "Review and export evidence-backed dossiers as reporting becomes available.", phase: "Phased delivery" },
  { slug: "knowledge-hub", name: "Knowledge Hub", icon: "library", description: "Find permitted sources, research and reusable knowledge.", phase: "Phased delivery" },
  { slug: "settings", name: "Settings", icon: "settings", description: "Manage approved preferences and access controls when connected.", phase: "Foundation integration" },
] as const;
export type Module = (typeof modules)[number];
