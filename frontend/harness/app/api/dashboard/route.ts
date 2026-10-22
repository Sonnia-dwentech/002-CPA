import { NextRequest, NextResponse } from "next/server";
import { isDashboard, validFilters } from "../../../../lib/dashboard";
export const dynamic = "force-dynamic";
const headers = { "Cache-Control": "no-store" };
const error = (status: number) => NextResponse.json({ status }, { status, headers });
export async function GET(req: NextRequest) {
  if (!process.env.CPA_B022_HARNESS) return error(503);
  if (req.headers.get("host") !== "127.0.0.1:3100" || req.headers.get("sec-fetch-site") === "cross-site") return error(403);
  if (req.headers.has("authorization")) return error(400);
  if (!validFilters(req.nextUrl.searchParams)) return error(422);
  const cookies = (req.headers.get("cookie") ?? "").split(";").filter(c => c.trim().split("=", 1)[0] === "cpa_b016_session");
  const token = req.cookies.get("cpa_b016_session")?.value;
  if (cookies.length !== 1 || !token || !/^[A-Za-z0-9_-]{43}$/.test(token)) return error(401);
  try {
    const upstream = await fetch(`http://127.0.0.1:8100/dashboard${req.nextUrl.search}`, {
      headers: { Authorization: `Bearer ${token}` }, cache: "no-store", redirect: "error", signal: AbortSignal.timeout(5000),
    });
    if (!upstream.ok) return error([401, 403, 422, 503].includes(upstream.status) ? upstream.status : 503);
    const data: unknown = await upstream.json();
    if (!isDashboard(data)) return error(503);
    return NextResponse.json({ status: data.status, total: data.total,
      records: data.records.map(({ id, kind, state, owner_id }) => ({ id, kind, state, owner_id })),
      available_kinds: data.available_kinds, data_kind: data.data_kind,
      metric: data.metric, business_metrics_status: data.business_metrics_status }, { headers });
  } catch { return error(503); }
}
