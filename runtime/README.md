# Runtime foundation (work in progress)

This directory begins the Python backend implementation. It is **not** a deployed FastAPI service and does not connect to Bókun, payment processors, WhatsApp, or production data.

`tenant_context.py` supplies a minimal, fail-closed isolation primitive. Context must be built from verified authentication claims by future middleware. Never trust a client-supplied brand ID, customer ID, partner ID, or LLM output as proof of authorization.

Current staff/system requests are intentionally denied until explicit permission grants and action-level checks are implemented. Resource ownership checks alone are not sufficient for booking, payment, refunds, or human handoff.

Run the isolated standard-library tests with:

```bash
python -m unittest discover -s tests -v
```

Next milestones: FastAPI application skeleton, authenticated middleware, persisted tenancy, scoped permission grants, audit events, transaction idempotency, and integration sandbox tests. Existing documents in `business/` remain the source of business policy; do not hard-code prices or deposit rules into this module.
