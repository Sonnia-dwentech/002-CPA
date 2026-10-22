"""Read-only B023 draft checks. Never authorizes or executes deployment."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(document, template):
    errors = []
    if document.get("format") != "cpa-staging-review-v1" or document.get("environment") != "staging":
        errors.append("unexpected manifest format/environment")
    if document.get("status") != "draft-not-deployable" or document.get("deployment_authorized") is not False:
        errors.append("draft must remain non-deployable")
    for group in ("decisions_required", "cost_review"):
        values = document.get(group)
        if not isinstance(values, dict) or not values or any(value is not None for value in values.values()):
            errors.append(group + " must contain unresolved placeholders only")
    proposal = document.get("proposal", {})
    for group in ("worker", "live_ai", "storage", "identity"):
        if proposal.get(group, {}).get("enabled") is not False:
            errors.append(group + " must stay disabled")
    if proposal.get("test_harness_deployable") is not False:
        errors.append("test harness must not be deployable")
    security = proposal.get("browser_security", {})
    if security.get("cors_allowed_origins") != [] or security.get("cors_allow_credentials") is not False:
        errors.append("CORS must remain unconfigured and deny cross-origin access")
    for key in ("cookie_secure_required", "cookie_http_only_required", "exact_origin_csrf_check_required"):
        if security.get(key) is not True:
            errors.append("required browser protection missing")
    identity = proposal.get("identity", {})
    if identity.get("callback_urls") != [] or identity.get("logout_redirect_urls") != []:
        errors.append("identity redirects must remain unset")
    for service in ("frontend", "api"):
        for key in ("build_command", "start_command", "runtime_version"):
            if proposal.get(service, {}).get(key, "missing") is not None:
                errors.append("unverified runtime command/version populated")
    db = proposal.get("database", {})
    if db.get("persistent_storage") is not True or any(db.get(k, "missing") is not None for k in ("runtime_secret_ref", "migration_secret_ref")):
        errors.append("database storage/secret placeholders invalid")
    migration = proposal.get("migration", {})
    if migration.get("run_automatically_on_boot") is not False or migration.get("command", "missing") is not None:
        errors.append("migration must not execute from draft")
    exclusions = document.get("promotion_exclusions", [])
    if not {"frontend/harness/**", "backend/check_local_*.py", "docs/evidence/**", "**/.env", "**/.env.*"} <= set(exclusions):
        errors.append("promotion exclusions incomplete")
    if not document.get("unresolved_implementation"):
        errors.append("implementation blockers missing")
    values = {}
    for line in template.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if "=" not in line:
            errors.append("invalid template line")
            continue
        key, value = line.split("=", 1)
        if key in values:
            errors.append("duplicate environment key")
        values[key] = value
    expected = dict(APP_ENV="staging", LOG_LEVEL="INFO", LIVE_AI_ENABLED="false",
                    DATABASE_URL="", FRONTEND_ORIGIN="", AUTH_SECRET="", OPENAI_API_KEY="",
                    OPENAI_MODEL="", STORAGE_BUCKET="", MAX_AI_RUN_COST="")
    if values != expected:
        errors.append("template must contain only reviewed defaults and empty placeholders")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-ready", action="store_true", help="Return 2 for this intentionally blocked staging draft.")
    args = parser.parse_args()
    try:
        folder = ROOT / "deployments/staging"
        errors = validate(json.loads((folder / "review-manifest.json").read_text()),
                          (folder / "staging.env.example").read_text())
    except (OSError, ValueError, TypeError, AttributeError):
        print("Staging draft validation failed; file details withheld")
        return 1
    if errors:
        print("Staging draft invalid: " + "; ".join(errors))
        return 1
    print("PASS: local draft structure, disabled services and empty-value template")
    print("BLOCKED: provider/values/owners/budget, runtime integration, technical review and deployment authority remain unresolved")
    return 2 if args.require_ready else 0


if __name__ == "__main__":
    raise SystemExit(main())
