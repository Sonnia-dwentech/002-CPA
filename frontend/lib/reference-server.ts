import { readFile } from "node:fs/promises";
import { request } from "node:https";
import path from "node:path";
import { NextRequest, NextResponse } from "next/server";
import { isDashboard, validFilters } from "./dashboard";

const origin = "http://127.0.0.1:3000";
const upstreamOrigin = "https://127.0.0.1:3543";
const cookieName = "cpa_reference_session";
const cookiePath = "/api/reference";
const tokenPattern = /^[A-Za-z0-9_-]{43}$/;
const cookieOptions = { httpOnly: true, sameSite: "strict" as const, secure: false, path: cookiePath };

function reply(status: number, value: object = { status }, clear = false) {
  const response = NextResponse.json(value, { status, headers: {
    "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "no-referrer",
  } });
  if (clear) response.cookies.set(cookieName, "", { ...cookieOptions, maxAge: 0 });
  return response;
}

async function upstream(endpoint: string, method: "GET" | "POST", token?: string) {
  // Trust this local rehearsal's public CA only for this fixed loopback request.
  const ca = await readFile(path.resolve(process.cwd(), "../deployments/local-rehearsal/reference-dashboard-ca.pem"));
  return new Promise<{ status: number; body: string; cookies: string[] }>((resolve, reject) => {
    const call = request(upstreamOrigin + endpoint, {
      method, ca, rejectUnauthorized: true, minVersion: "TLSv1.2",
      headers: { Origin: upstreamOrigin, ...(token ? { Cookie: `cpa_b024_session=${token}` } : {}) },
    }, response => {
      const chunks: Buffer[] = [];
      let length = 0;
      response.on("data", (chunk: Buffer) => {
        length += chunk.length;
        if (length > 131072) { call.destroy(new Error("Upstream response limit")); return; }
        chunks.push(chunk);
      });
      response.on("error", reject);
      response.on("end", () => resolve({ status: response.statusCode ?? 503,
        body: Buffer.concat(chunks).toString("utf8"), cookies: response.headers["set-cookie"] ?? [] }));
    });
    call.setTimeout(5000, () => call.destroy(new Error("Upstream timeout")));
    call.on("error", reject);
    call.end();
  });
}

export async function referenceRequest(req: NextRequest, segments: string[]) {
  if (req.headers.get("host") !== "127.0.0.1:3000" || req.headers.get("sec-fetch-site") === "cross-site"
      || (req.headers.get("origin") !== null && req.headers.get("origin") !== origin)) return reply(403);
  if (req.method === "POST" && req.headers.get("origin") !== origin) return reply(403);
  if (req.headers.has("authorization")) return reply(400);
  const endpoint = segments.join("/");
  const dashboard = endpoint === "dashboard";
  if (!dashboard && !["session/login", "session/logout", "session/status"].includes(endpoint)) return reply(404);
  const expectedMethod = dashboard || endpoint === "session/status" ? "GET" : "POST";
  if (req.method !== expectedMethod) return reply(405);
  if (dashboard ? !validFilters(req.nextUrl.searchParams) : !!req.nextUrl.search) return reply(422);
  const cookies = (req.headers.get("cookie") ?? "").split(";")
    .map(value => value.trim()).filter(value => value.split("=", 1)[0] === cookieName);
  if (cookies.length > 1) return reply(401, { status: 401 }, true);
  const token = cookies[0]?.slice(cookieName.length + 1);
  if (cookies.length && (!token || !tokenPattern.test(token))) return reply(401, { status: 401 }, true);
  if (endpoint === "session/logout" && !token) return reply(200, { logged_out: true }, true);
  if (endpoint !== "session/login" && !token) return reply(401, { status: 401 }, true);
  try {
    if (endpoint === "session/login") {
      if (token) {
        const current = await upstream("/api/session/status", "GET", token);
        // Reuse an active session. Only replace a confirmed invalid/expired one.
        if (current.status === 200) return reply(200, { authenticated: true, synthetic: true });
        if (current.status !== 401) return reply(503);
      }
      const issued = await upstream("/api/session/login", "POST");
      if (issued.status !== 200) return reply(issued.status === 403 ? 403 : 503);
      const sessionCookies = issued.cookies.filter(value => value.startsWith("cpa_b024_session="));
      const newToken = sessionCookies[0]?.split(";", 1)[0].slice("cpa_b024_session=".length);
      if (sessionCookies.length !== 1 || !newToken || !tokenPattern.test(newToken)) return reply(503);
      const response = reply(200, { authenticated: true, synthetic: true });
      // HTTP cookie is limited to this explicitly loopback-only preview.
      response.cookies.set(cookieName, newToken, { ...cookieOptions, maxAge: 28800 });
      return response;
    }
    const result = await upstream("/api/" + endpoint + (dashboard ? req.nextUrl.search : ""),
      expectedMethod as "GET" | "POST", token);
    if (result.status !== 200) {
      const status = [400, 401, 403, 404, 422, 503].includes(result.status) ? result.status : 503;
      return reply(status, { status }, status === 401);
    }
    if (dashboard) {
      const data: unknown = JSON.parse(result.body);
      return isDashboard(data) ? reply(200, data) : reply(503);
    }
    return endpoint === "session/logout" ? reply(200, { logged_out: true }, true)
      : reply(200, { authenticated: true, synthetic: true });
  } catch {
    // Do not expose upstream exceptions, certificates, tokens or response text.
    return reply(503);
  }
}
