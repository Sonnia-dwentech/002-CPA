-- Synthetic local verification only; no audit HTTP reader or production grants.
CREATE TABLE cpa.audit_events (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    occurred_at timestamptz NOT NULL DEFAULT clock_timestamp(),
    actor_id uuid,
    resource_id uuid,
    action text NOT NULL,
    outcome text NOT NULL,
    CHECK (
        (action = 'session.issue' AND outcome IN ('issued','denied','unavailable'))
        OR (action = 'session.logout' AND outcome IN ('revoked','denied','unavailable'))
        OR (action = 'record.read' AND outcome IN ('allowed','denied','unavailable'))
        OR (action = 'privileged.check' AND outcome IN ('denied','unavailable'))
    )
);
REVOKE ALL ON cpa.audit_events FROM PUBLIC;
