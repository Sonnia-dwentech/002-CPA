// Workstation-only account storage. Hosted identity remains a separate deployment.
import { DatabaseSync } from "node:sqlite";
import { createHash, randomBytes, randomUUID, scrypt, timingSafeEqual } from "node:crypto";

type Account = { id: string; email: string; name: string; salt: string; password_hash: string; role: string; enabled: number };
const digest = (value: string) => createHash("sha256").update(value).digest("hex");
const derive = (password: string, salt: string) => new Promise<Buffer>((resolve, reject) => {
  scrypt(password, salt, 64, { N: 32768, r: 8, p: 3, maxmem: 64 * 1024 * 1024 },
    (error, key) => error ? reject(error) : resolve(key));
});
export class AccountError extends Error {
  constructor(public status: number, message: string) { super(message); }
}
export class LocalAccountStore {
  db: DatabaseSync;
  constructor(filename: string) {
    this.db = new DatabaseSync(filename);
    this.db.exec(`PRAGMA foreign_keys=ON; PRAGMA journal_mode=WAL; PRAGMA busy_timeout=5000;
      CREATE TABLE IF NOT EXISTS accounts (
        id TEXT PRIMARY KEY, email TEXT NOT NULL UNIQUE, name TEXT NOT NULL,
        salt TEXT NOT NULL, password_hash TEXT NOT NULL, created_at INTEGER NOT NULL);
      CREATE TABLE IF NOT EXISTS sessions (
        digest TEXT PRIMARY KEY, user_id TEXT NOT NULL REFERENCES accounts(id),
        expires_at INTEGER NOT NULL, last_seen INTEGER NOT NULL);
      CREATE TABLE IF NOT EXISTS attempts (bucket TEXT PRIMARY KEY, count INTEGER NOT NULL, resets_at INTEGER NOT NULL);
      CREATE TABLE IF NOT EXISTS ideas (
        id TEXT PRIMARY KEY, user_id TEXT NOT NULL REFERENCES accounts(id), title TEXT NOT NULL,
        description TEXT NOT NULL, created_at INTEGER NOT NULL);
      CREATE TABLE IF NOT EXISTS admin_setup (digest TEXT PRIMARY KEY, expires_at INTEGER NOT NULL);
      CREATE TABLE IF NOT EXISTS account_audit (id TEXT PRIMARY KEY, actor_id TEXT NOT NULL,
        target_id TEXT NOT NULL, action TEXT NOT NULL, created_at INTEGER NOT NULL);`);
    // Additive migration preserves existing users and their saved work.
    this.db.exec("BEGIN IMMEDIATE");
    try {
      const columns = this.db.prepare("PRAGMA table_info(accounts)").all().map(row => row.name);
      if (!columns.includes("role")) this.db.exec("ALTER TABLE accounts ADD COLUMN role TEXT NOT NULL DEFAULT 'external' CHECK(role IN ('admin','external'))");
      if (!columns.includes("enabled")) this.db.exec("ALTER TABLE accounts ADD COLUMN enabled INTEGER NOT NULL DEFAULT 1 CHECK(enabled IN (0,1))");
      this.db.exec("COMMIT");
    } catch (error) { this.db.exec("ROLLBACK"); throw error; }
  }
  limit(bucket: string, maximum: number, now = Date.now()) {
    const key = digest(bucket);
    this.db.prepare("DELETE FROM attempts WHERE resets_at <= ?").run(now);
    this.db.prepare(`INSERT INTO attempts VALUES (?,1,?) ON CONFLICT(bucket) DO UPDATE SET count=count+1`).run(key, now + 15 * 60_000);
    const row = this.db.prepare("SELECT count FROM attempts WHERE bucket=?").get(key)!;
    if (Number(row.count) > maximum) throw new AccountError(429, "Too many attempts. Please try again in 15 minutes.");
  }
  async authenticate(action: "login" | "signup", input: Record<string, unknown>) {
    const email = typeof input.email === "string" ? input.email.trim().toLowerCase() : "";
    const password = typeof input.password === "string" ? input.password : "";
    const name = typeof input.name === "string" ? input.name.trim() : "";
    const setup = typeof input.adminSetup === "string" ? input.adminSetup : "";
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 254 || password.length > 128 || !password.length)
      throw new AccountError(422, "Enter a valid email and password (up to 128 characters).");
    this.limit("account:" + email, 10);
    this.limit("workstation-auth", 50);
    if (setup && !this.db.prepare("SELECT digest FROM admin_setup WHERE digest=? AND expires_at>?").get(digest(setup), Date.now()))
      throw new AccountError(403, "This administrator setup link has expired or was already used.");
    let user = this.db.prepare("SELECT * FROM accounts WHERE email=?").get(email) as Account | undefined;
    if (action === "signup") {
      if (password.length < 15 || !name || name.length > 80)
        throw new AccountError(422, "Enter your name and a password of 15–128 characters.");
      const salt = randomBytes(16).toString("hex");
      const hash = (await derive(password, salt)).toString("hex");
      if (user) throw new AccountError(409, "Could not create this account. Try logging in if you already registered.");
      user = { id: randomUUID(), email, name, salt, password_hash: hash, role: "external", enabled: 1 };
      try {
        this.db.prepare("INSERT INTO accounts(id,email,name,salt,password_hash,created_at) VALUES (?,?,?,?,?,?)").run(user.id, email, name, salt, hash, Date.now());
      } catch (error) {
        if (this.db.prepare("SELECT id FROM accounts WHERE email=?").get(email))
          throw new AccountError(409, "Could not create this account. Try logging in if you already registered.");
        throw error;
      }
    } else {
      const calculated = await derive(password, user?.salt ?? "00000000000000000000000000000000");
      const expected = user ? Buffer.from(user.password_hash, "hex") : Buffer.alloc(64);
      if (!timingSafeEqual(calculated, expected) || !user || !user.enabled)
        throw new AccountError(401, "Email or password is incorrect.");
    }
    // A local operator issues setup links; signup fields never choose a role.
    // Consume atomically after password verification, including concurrent requests.
    if (setup) {
      this.db.exec("BEGIN IMMEDIATE");
      try {
        const claimed = this.db.prepare("DELETE FROM admin_setup WHERE digest=? AND expires_at>?").run(digest(setup), Date.now());
        if (claimed.changes !== 1) throw new AccountError(403, "This administrator setup link has expired or was already used.");
        this.db.prepare("UPDATE accounts SET role='admin' WHERE id=? AND enabled=1").run(user.id);
        this.db.prepare("DELETE FROM sessions WHERE user_id=?").run(user.id);
        this.db.prepare("INSERT INTO account_audit VALUES (?,?,?,?,?)").run(randomUUID(), user.id, user.id, "administrator_setup", Date.now());
        this.db.exec("COMMIT"); user.role = "admin";
      } catch (error) { this.db.exec("ROLLBACK"); throw error; }
    }
    const token = randomBytes(32).toString("base64url");
    const now = Date.now();
    this.db.prepare("DELETE FROM sessions WHERE expires_at<=? OR last_seen<=?").run(now, now - 30 * 60_000);
    this.db.prepare("INSERT INTO sessions VALUES (?,?,?,?)").run(digest(token), user.id, now + 8 * 3600_000, now);
    return { token, user: { id: user.id, email: user.email, name: user.name, role: user.role } };
  }
  user(token: string | undefined, now = Date.now()) {
    if (!token || !/^[A-Za-z0-9_-]{43}$/.test(token)) throw new AccountError(401, "Please log in.");
    const user = this.db.prepare(`SELECT a.id,a.email,a.name,a.role FROM accounts a JOIN sessions s ON s.user_id=a.id
      WHERE a.enabled=1 AND s.digest=? AND s.expires_at>? AND s.last_seen>?`).get(digest(token), now, now - 30 * 60_000);
    if (!user) throw new AccountError(401, "Your session has ended. Please log in again.");
    this.db.prepare("UPDATE sessions SET last_seen=? WHERE digest=?").run(now, digest(token));
    return user as { id: string; email: string; name: string; role: string };
  }
  issueAdminSetup() {
    const token = randomBytes(32).toString("base64url");
    // Operator-only method; never exposed as an HTTP action.
    this.db.exec("BEGIN IMMEDIATE");
    try {
      this.db.prepare("DELETE FROM admin_setup").run();
      this.db.prepare("INSERT INTO admin_setup VALUES (?,?)").run(digest(token), Date.now() + 24 * 3600_000);
      this.db.exec("COMMIT");
    } catch (error) { this.db.exec("ROLLBACK"); throw error; }
    return token;
  }
  adminUsers(token: string | undefined) {
    if (this.user(token).role !== "admin") throw new AccountError(403, "Administrator access required.");
    return this.db.prepare("SELECT id,email,name,role,enabled,created_at FROM accounts ORDER BY created_at DESC,id DESC").all();
  }
  setAccountEnabled(token: string | undefined, target: unknown, enabled: unknown) {
    if (typeof target !== "string" || typeof enabled !== "boolean") throw new AccountError(422, "Select an account and status.");
    this.db.exec("BEGIN IMMEDIATE");
    try {
      const actor = this.user(token);
      if (actor.role !== "admin") throw new AccountError(403, "Administrator access required.");
      const account = this.db.prepare("SELECT role FROM accounts WHERE id=?").get(target);
      if (!account) throw new AccountError(404, "Account not found.");
      if (account.role === "admin") throw new AccountError(403, "Administrator accounts cannot be suspended here.");
      this.db.prepare("UPDATE accounts SET enabled=? WHERE id=?").run(enabled ? 1 : 0, target);
      this.db.prepare("DELETE FROM sessions WHERE user_id=?").run(target);
      this.db.prepare("INSERT INTO account_audit VALUES (?,?,?,?,?)").run(randomUUID(), actor.id, target, enabled ? "reactivate" : "suspend", Date.now());
      this.db.exec("COMMIT");
    } catch (error) { this.db.exec("ROLLBACK"); throw error; }
  }
  logout(token: string | undefined) {
    if (token) this.db.prepare("DELETE FROM sessions WHERE digest=?").run(digest(token));
  }
  ideas(userId: string) {
    return this.db.prepare("SELECT id,title,description,created_at FROM ideas WHERE user_id=? ORDER BY created_at DESC,id DESC").all(userId);
  }
  addIdea(userId: string, input: Record<string, unknown>) {
    const title = typeof input.title === "string" ? input.title.trim() : "";
    const description = typeof input.description === "string" ? input.description.trim() : "";
    if (!title || title.length > 160 || description.length > 5000)
      throw new AccountError(422, "Add a title up to 160 characters and notes up to 5,000 characters.");
    this.db.prepare("INSERT INTO ideas VALUES (?,?,?,?,?)").run(randomUUID(), userId, title, description, Date.now());
  }
}
