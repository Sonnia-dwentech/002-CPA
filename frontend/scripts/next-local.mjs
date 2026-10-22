import { createRequire } from "node:module";
import { spawn } from "node:child_process";
const require = createRequire(import.meta.url);
const command = process.argv[2];
if (!["dev", "build", "start"].includes(command)) throw new Error("Use dev, build or start");
// Refuse startup if the installed native compiler is unavailable. Never rely on
// Next's missing-compiler download fallback.
if (process.platform !== "win32" || process.arch !== "x64") {
  throw new Error("This verified local launcher requires Windows x64.");
}
require("@next/swc-win32-x64-msvc");
const child = spawn(process.execPath, [
  require.resolve("next/dist/bin/next"), command,
  ...(command === "build" ? ["--webpack"] :
    ["--hostname", "127.0.0.1", "--port", "3000", ...(command === "dev" ? ["--webpack"] : [])]),
], {
  stdio: "inherit",
  env: { ...process.env, NEXT_TELEMETRY_DISABLED: "1" },
  windowsHide: true,
});
child.on("exit", (code) => { process.exitCode = code ?? 1; });
for (const signal of ["SIGINT", "SIGTERM"]) process.on(signal, () => child.kill(signal));
