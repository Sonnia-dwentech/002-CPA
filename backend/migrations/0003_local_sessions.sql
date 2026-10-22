CREATE TABLE cpa.sessions (
    token_digest text PRIMARY KEY CHECK (token_digest ~ '^[0-9a-f]{64}$'),
    user_id uuid NOT NULL REFERENCES cpa.users(id),
    issued_at timestamptz NOT NULL,
    last_seen_at timestamptz NOT NULL,
    expires_at timestamptz NOT NULL,
    revoked_at timestamptz,
    CHECK (expires_at = issued_at + interval '8 hours'),
    CHECK (last_seen_at >= issued_at AND last_seen_at < expires_at)
);
CREATE INDEX sessions_user_id ON cpa.sessions(user_id);

-- Removing access invalidates sessions even when no request arrives while the
-- account is disabled. Restoring membership never restores revoked sessions.
CREATE FUNCTION cpa.revoke_sessions_after_user_change() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NOT NEW.enabled OR NOT NEW.membership_active
       OR NEW.issuer IS DISTINCT FROM OLD.issuer
       OR NEW.subject IS DISTINCT FROM OLD.subject
       OR NEW.category IS DISTINCT FROM OLD.category
       OR NEW.client_id IS DISTINCT FROM OLD.client_id THEN
        UPDATE cpa.sessions SET revoked_at = COALESCE(revoked_at, clock_timestamp())
        WHERE user_id = NEW.id AND revoked_at IS NULL;
    END IF;
    RETURN NEW;
END;
$$;
CREATE TRIGGER users_revoke_sessions
AFTER UPDATE OF enabled, membership_active, issuer, subject, category, client_id
ON cpa.users FOR EACH ROW EXECUTE FUNCTION cpa.revoke_sessions_after_user_change();
