import Dashboard from "../../../components/Dashboard";
export default function Page() { return <Dashboard enabled={process.env.CPA_B022_HARNESS === "1"} />; }
