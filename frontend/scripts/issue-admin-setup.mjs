// Explicit local operator action; prints the one-use setup URL for the user.
import path from 'node:path';
import { LocalAccountStore } from '../lib/local-account-store.ts';
const store = new LocalAccountStore(path.resolve('../.local/accounts/accounts.sqlite'));
try {
  console.log('http://127.0.0.1:3000/sign-up#admin-setup=' + store.issueAdminSetup());
} finally { store.db.close(); }
