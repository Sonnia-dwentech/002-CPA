export type AccountRole = "admin" | "external";
export type AccountUser = { id: string; name: string; email: string; role: AccountRole };
export function dashboardFor(role: AccountRole) {
  return role === "admin" ? "/admin" : "/dashboard";
}
export function accountDestination(pathname: string, role: AccountRole) {
  if (["/", "/sign-in", "/sign-up", "/dashboard", "/admin"].includes(pathname)) return dashboardFor(role);
  return pathname;
}
