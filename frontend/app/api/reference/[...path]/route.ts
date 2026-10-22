import { NextRequest } from "next/server";
import { referenceRequest } from "../../../../lib/reference-server";
export const dynamic = "force-dynamic";
export const runtime = "nodejs";
async function handle(req: NextRequest, context: { params: Promise<{ path: string[] }> }) {
  return referenceRequest(req, (await context.params).path);
}
export const GET = handle;
export const POST = handle;
