import { NextRequest, NextResponse } from "next/server";
import path from "node:path";
import { existsSync } from "node:fs";
import { AccountError, LocalAccountStore } from "../../../../lib/local-account-store";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";
const cookie = "cpa_local_account";
const cookieOptions = { httpOnly: true, sameSite: "strict" as const, secure: false, path: "/" };
let store: LocalAccountStore | undefined;
function response(value: object, status = 200) {
  return NextResponse.json(value, { status, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
}
async function handle(req: NextRequest, context: { params: Promise<{ action: string }> }) {
  // This adapter cannot be exposed on a hosted origin or through a reverse proxy.
  const origin = "http://127.0.0.1:3000";
  if (req.headers.get("host") !== "127.0.0.1:3000" || req.headers.has("x-forwarded-for") && req.headers.get("x-forwarded-for") !== "127.0.0.1"
    || req.headers.get("sec-fetch-site") === "cross-site"
    || (req.headers.get("origin") !== null && req.headers.get("origin") !== origin)
    || (req.method === "POST" && req.headers.get("origin") !== origin)) return response({ message: "Local access only." }, 403);
  const { action } = await context.params;
  const methods: Record<string, string[]> = { status: ["GET"], login: ["POST"], signup: ["POST"], logout: ["POST"], ideas: ["GET", "POST"], users: ["GET", "POST"] };
  if (!methods[action]) return response({ message: "Not found." }, 404);
  if (!methods[action].includes(req.method)) return response({ message: "Method not allowed." }, 405);
  try {
    const directory = path.resolve(process.cwd(), "../.local/accounts");
    if (!existsSync(path.join(directory, ".prepared"))) return response({ message: "Local account storage has not been prepared." }, 503);
    store ??= new LocalAccountStore(path.join(directory, "accounts.sqlite"));
    const cookies = req.cookies.getAll(cookie);
    if (cookies.length > 1) throw new AccountError(401, "Please log in again.");
    const token = cookies[0]?.value;
    if (action === "logout") {
      store.logout(token);
      const result = response({ ok: true }); result.cookies.set(cookie, "", { ...cookieOptions, maxAge: 0 }); return result;
    }
    let input: Record<string, unknown> = {};
    if (req.method === "POST") {
      if (!req.headers.get("content-type")?.startsWith("application/json")) throw new AccountError(415, "JSON required.");
      // Read incrementally so a chunked body cannot bypass the size cap.
      const reader = req.body?.getReader();
      if (!reader) throw new AccountError(422, "Invalid request.");
      const chunks: Uint8Array[] = []; let length = 0;
      while (true) {
        const next = await reader.read(); if (next.done) break;
        length += next.value.length;
        if (length > 32768) { await reader.cancel(); throw new AccountError(413, "Request too large."); }
        chunks.push(next.value);
      }
      try { input = JSON.parse(Buffer.concat(chunks).toString("utf8")); }
      catch { throw new AccountError(422, "Invalid request."); }
      if (!input || Array.isArray(input) || typeof input !== "object") throw new AccountError(422, "Invalid request.");
    }
    if (action === "signup" || action === "login") {
      const account = await store.authenticate(action, input);
      store.logout(token);
      const result = response({ user: account.user });
      result.cookies.set(cookie, account.token, { ...cookieOptions, maxAge: 8 * 3600 });
      return result;
    }
    const user = store.user(token);
    if (action === "status") return response({ user });
    if (action === "users") {
      if (req.method === "POST") store.setAccountEnabled(token, input.userId, input.enabled);
      return response({ users: store.adminUsers(token) });
    }
    if (req.method === "POST") { store.limit("ideas:" + user.id, 100); store.addIdea(user.id, input); }
    return response({ user, ideas: store.ideas(user.id) });
  } catch (error) {
    if (error instanceof AccountError) return response({ message: error.message }, error.status);
    return response({ message: "The account service is unavailable. Please retry." }, 503);
  }
}
export const GET = handle;
export const POST = handle;
