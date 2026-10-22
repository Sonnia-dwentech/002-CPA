-- Reference/permission metadata only: no application content or live accounts.
CREATE TABLE cpa.client_organisations (
    id uuid PRIMARY KEY
);
CREATE TABLE cpa.users (
    id uuid PRIMARY KEY,
    issuer text NOT NULL CHECK (length(issuer) > 0),
    subject text NOT NULL CHECK (length(subject) > 0),
    category text NOT NULL CHECK (category IN ('internal', 'client')),
    client_id uuid REFERENCES cpa.client_organisations(id),
    enabled boolean NOT NULL DEFAULT false,
    membership_active boolean NOT NULL DEFAULT false,
    UNIQUE (issuer, subject),
    UNIQUE (id, category),
    CHECK ((category = 'client' AND client_id IS NOT NULL)
        OR (category = 'internal' AND client_id IS NULL))
);
CREATE TABLE cpa.user_roles (
    user_id uuid NOT NULL,
    category text NOT NULL,
    role text NOT NULL,
    PRIMARY KEY (user_id, role),
    FOREIGN KEY (user_id, category) REFERENCES cpa.users(id, category),
    CHECK ((category = 'client' AND role = 'client_user') OR
           (category = 'internal' AND role IN
            ('cpa', 'executive', 'technical', 'product_authority', 'access_admin', 'developer')))
);
CREATE TABLE cpa.access_records (
    id uuid PRIMARY KEY,
    kind text NOT NULL CHECK (kind IN
        ('idea','research','dossier','technical','client_intake','client_note','client_response')),
    owner_id uuid NOT NULL REFERENCES cpa.users(id),
    client_id uuid REFERENCES cpa.client_organisations(id),
    case_id uuid,
    author_id uuid REFERENCES cpa.users(id),
    state text NOT NULL CHECK (state IN ('draft','submitted','published','archived')),
    UNIQUE (id, client_id),
    FOREIGN KEY (case_id, client_id) REFERENCES cpa.access_records(id, client_id),
    CHECK (
        (kind IN ('idea','research','dossier','technical') AND client_id IS NULL AND case_id IS NULL)
        OR (kind = 'client_intake' AND client_id IS NOT NULL AND case_id IS NULL)
        OR (kind IN ('client_note','client_response') AND client_id IS NOT NULL AND case_id IS NOT NULL)
    ),
    CHECK (kind <> 'client_response' OR author_id IS NOT NULL)
);
CREATE TABLE cpa.record_grants (
    record_id uuid NOT NULL REFERENCES cpa.access_records(id),
    user_id uuid NOT NULL REFERENCES cpa.users(id),
    permission text NOT NULL CHECK (permission IN ('read','edit','export','run','decision')),
    PRIMARY KEY (record_id, user_id, permission)
);
CREATE TABLE cpa.case_assignments (
    case_id uuid NOT NULL REFERENCES cpa.access_records(id),
    user_id uuid NOT NULL REFERENCES cpa.users(id),
    assignment text NOT NULL CHECK (assignment IN ('cpa','approver')),
    PRIMARY KEY (case_id, user_id, assignment)
);
-- No seeds or public grant mutation functions. Approved bootstrap/administration
-- must precede creating any non-test account or assignment.
