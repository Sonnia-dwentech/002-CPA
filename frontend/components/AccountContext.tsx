"use client";
import { createContext, useContext } from "react";
import type { AccountUser } from "../lib/account-navigation";
export const AccountContext = createContext<AccountUser | null>(null);
export function useAccount() {
  const user = useContext(AccountContext);
  if (!user) throw new Error("Verified account required.");
  return user;
}
