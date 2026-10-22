export const kinds = ["idea", "research", "dossier", "technical", "client_intake", "client_note", "client_response"] as const;
export const states = ["draft", "submitted", "published", "archived"] as const;
export type DashboardData = {
  status: "ok" | "empty" | "unavailable";
  total: number | null;
  records: { id: string; kind: string; state: string; owner_id: string }[];
  available_kinds: string[];
  data_kind: "synthetic_reference_records";
  metric: "visible_reference_count";
  business_metrics_status: "unavailable";
};
const uuid = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
export function validFilters(params: URLSearchParams) {
  return [...params.keys()].every(key => {
    const values = params.getAll(key);
    return values.length === 1 && (key === "kind" ? kinds.some(k => k === values[0])
      : key === "state" ? states.some(s => s === values[0]) : key === "owner_id" && uuid.test(values[0]));
  });
}
export function isDashboard(value: unknown): value is DashboardData {
  if (!value || typeof value !== "object") return false;
  const d = value as DashboardData;
  if (d.data_kind !== "synthetic_reference_records" || d.metric !== "visible_reference_count"
    || d.business_metrics_status !== "unavailable" || !Array.isArray(d.records)
    || !Array.isArray(d.available_kinds) || !d.available_kinds.every(k => kinds.some(v => v === k))) return false;
  if (!d.records.every(r => r && uuid.test(r.id) && uuid.test(r.owner_id)
    && kinds.some(k => k === r.kind) && states.some(s => s === r.state) && d.available_kinds.includes(r.kind))) return false;
  if (new Set(d.records.map(r => r.id)).size !== d.records.length) return false;
  return d.status === "unavailable" ? d.total === null && d.records.length === 0
    : (d.status === "ok" || d.status === "empty") && d.total === d.records.length
      && (d.status === "empty" ? d.total === 0 : d.records.length > 0);
}
