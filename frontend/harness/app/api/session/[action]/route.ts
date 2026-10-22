import { NextRequest, NextResponse } from "next/server";
export const dynamic = "force-dynamic";
const cookieName = "cpa_b016_session";
const origin = "http://127.0.0.1:3100";
const routes: Record<string, [string, string]> = {
  login: ["POST", "/fixture-login"], logout: ["POST", "/logout"],
  status: ["GET", "/session"], own: ["GET", "/records/00000000-0000-0000-0000-00000000012d"],
  other: ["GET", "/records/00000000-0000-0000-0000-00000000012e"],
  privileged: ["POST", "/privileged"],
};
function reply(status: number) {
  return NextResponse.json({ status }, { status, headers: { "Cache-Control": "no-store" } });
}
function clear(response: NextResponse) {
  response.cookies.set(cookieName, "", { httpOnly: true, sameSite: "strict", secure: false, path: "/", maxAge: 0 });
}
async function handle(req: NextRequest, context: { params: Promise<{ action: string }> }) {
  const { action } = await context.params;
  const route = routes[action];
  if (!route) return reply(404);
  if (req.method !== route[0]) return reply(405);
  if (req.headers.get("host") !== "127.0.0.1:3100") return reply(403);
  if (req.method !== "GET" && req.headers.get("origin") !== origin) return reply(403);
  if (req.headers.get("sec-fetch-site") === "cross-site") return reply(403);
  if (req.nextUrl.search || req.headers.has("authorization")) return reply(400);
  const rawCookies = (req.headers.get("cookie") ?? "").split(";")
    .filter(value => value.trim().split("=", 1)[0] === cookieName);
  if (rawCookies.length > 1) return reply(401);
  const credentials = req.cookies.getAll(cookieName);
  if (credentials.length > 1) return reply(401);
  const token = credentials[0]?.value;
  if (token && !/^[A-Za-z0-9_-]{43}$/.test(token)) {
    const response = reply(401); clear(response); return response;
  }
  if (action === "login" && token) return reply(409); // never silently replace a possibly live session
  if (action !== "login" && !token) { const response = reply(401); clear(response); return response; }
  const key = process.env.CPA_B016_HARNESS_KEY;
  if (!key) return reply(503);
  try {
    const upstream = await fetch(`http://127.0.0.1:8100${route[1]}`, {
      method: route[0], cache: "no-store", redirect: "error",
      signal: AbortSignal.timeout(5000),
      headers: action === "login" ? { "X-B016-Harness-Key": key } : { Authorization: `Bearer ${token}` },
    });
    const status = [200, 401, 403, 404, 503].includes(upstream.status) ? upstream.status : 503;
    const response = reply(status);
    if (action === "login" && status === 200) {
      const payload = await upstream.json();
      if (typeof payload.token !== "string" || !/^[A-Za-z0-9_-]{43}$/.test(payload.token)) return reply(503);
      response.cookies.set(cookieName, payload.token, {
        httpOnly: true, sameSite: "strict", secure: false, path: "/", maxAge: 8 * 60 * 60,
      });
    }
    if (status === 401 || (action === "logout" && status === 200)) clear(response);
    return response;
  } catch { return reply(503); }
}
export const GET = handle;
export const POST = handle;
