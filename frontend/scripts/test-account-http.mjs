import assert from 'node:assert/strict';
import { randomBytes, randomUUID } from 'node:crypto';
const origin = 'http://127.0.0.1:3000';
const password = randomBytes(24).toString('hex');
const email = `check-${randomUUID()}@example.test`;
let cookie = '';
async function call(action, body, headers = {}) {
  return fetch(`${origin}/api/account/${action}`, {
    method: body === undefined ? 'GET' : 'POST',
    headers: { Origin: origin, ...(body === undefined ? {} : { 'Content-Type': 'application/json' }), ...(cookie ? { Cookie: cookie } : {}), ...headers },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }), redirect: 'error',
  });
}
assert.equal((await call('ideas')).status, 401);
assert.equal((await call('login', {email,password}, {Origin: 'https://untrusted.example'})).status, 403);
assert.equal((await call('login')).status, 405);
let result = await call('signup', {name: 'Isolated HTTP test',email,password});
assert.equal(result.status, 200);
const setCookie = result.headers.get('set-cookie');
assert.match(setCookie, /HttpOnly/i); assert.match(setCookie, /SameSite=strict/i);
cookie = setCookie.split(';')[0];
assert.equal((await call('status')).status, 200);
assert.equal((await call('users')).status, 403);
assert.equal((await call('users', {userId:'forged',enabled:false})).status, 403);
assert.equal((await (await call('ideas')).json()).ideas.length, 0);
assert.equal((await call('ideas', {title: 'HTTP test record', description: 'Synthetic verification only.'})).status, 200);
assert.equal((await (await call('ideas')).json()).ideas.length, 1);
assert.equal((await call('logout', {})).status, 200);
assert.equal((await call('status')).status, 401);
cookie = '';
assert.equal((await call('login', {email, password: 'wrong password for test'})).status, 401);
result = await call('login', {email,password});
assert.equal(result.status, 200); cookie = result.headers.get('set-cookie').split(';')[0];
assert.equal((await (await call('ideas')).json()).ideas.length, 1);
await call('logout', {});
cookie = '';
result = await call('signup', {name:'Second isolated HTTP test',email:`check-${randomUUID()}@example.test`,password});
assert.equal(result.status, 200); cookie = result.headers.get('set-cookie').split(';')[0];
assert.equal((await (await call('ideas')).json()).ideas.length, 0);
await call('logout', {});
console.log('PASS: real HTTP signup/login, password rejection, cookie flags, protected data, origin denial, persistence, logout replay and second-account isolation. Test accounts retained separately from user work.');
