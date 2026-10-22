import assert from 'node:assert/strict';
import { accountDestination, dashboardFor } from '../lib/account-navigation.ts';
for (const role of ['admin','external']) {
  const expected = role === 'admin' ? '/admin' : '/dashboard';
  assert.equal(dashboardFor(role), expected);
  for (const entry of ['/','/sign-in','/sign-up','/dashboard','/admin']) {
    assert.equal(accountDestination(entry, role), expected, `${role} entering ${entry}`);
  }
  assert.equal(accountDestination('/reports', role), '/reports');
}
console.log('PASS: admin/external login, signup, root, dashboard, direct admin links and planned-route navigation.');
