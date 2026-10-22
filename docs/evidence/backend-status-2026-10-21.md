# Backend status link repair

Date: 21 October 2026 (Atlantic/Reykjavik). User: “Let backend status work”. No numbered task started or gate acceptance changed.

The frontend status link already targeted http://127.0.0.1:8000/, but no local API listener was running. Started the existing backend/run_local.py using backend/.venv312, binding 127.0.0.1 only. Corrected obsolete status-page copy saying the frontend had not been built; the page now accurately describes a separate frontend and backend process liveness. Updated the existing page-content assertion and ran tests.test_api: all 10 tests passed.

Restarted only the API process launched for this repair to load the copy change; it remains running. Browser clicked “Open local backend status” from the Command Centre and displayed “The backend is running”; its Check backend health link displayed {"status":"ok"}. Returned to the status page and left it visible. [Screenshot](backend-status-2026-10-21.png).

This endpoint checks process liveness; database/identity/provider readiness is not claimed. Existing dashboard/rehearsal services, databases, volumes and backups were untouched and retained. No cleanup, package installation, GitHub or external activity.
