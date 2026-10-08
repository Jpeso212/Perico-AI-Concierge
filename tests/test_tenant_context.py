import unittest

from runtime.tenant_context import (
    ActorType, AuthorizationError, RequestContext, ResourceScope, authorize_scope
)


class TenantContextTests(unittest.TestCase):
    def test_customer_can_access_owned_resource(self):
        ctx = RequestContext("brand-a", "actor-1", ActorType.CUSTOMER, customer_id="cust-1")
        authorize_scope(ctx, ResourceScope("brand-a", customer_id="cust-1"))

    def test_cross_brand_denied(self):
        ctx = RequestContext("brand-a", "actor-1", ActorType.CUSTOMER, customer_id="cust-1")
        with self.assertRaises(AuthorizationError):
            authorize_scope(ctx, ResourceScope("brand-b", customer_id="cust-1"))

    def test_cross_customer_denied(self):
        ctx = RequestContext("brand-a", "actor-1", ActorType.CUSTOMER, customer_id="cust-1")
        with self.assertRaises(AuthorizationError):
            authorize_scope(ctx, ResourceScope("brand-a", customer_id="cust-2"))

    def test_missing_owner_denied(self):
        ctx = RequestContext("brand-a", "actor-1", ActorType.CUSTOMER, customer_id="cust-1")
        with self.assertRaises(AuthorizationError):
            authorize_scope(ctx, ResourceScope("brand-a"))

    def test_partner_is_scoped(self):
        ctx = RequestContext("brand-a", "actor-1", ActorType.PARTNER, partner_id="partner-1")
        authorize_scope(ctx, ResourceScope("brand-a", partner_id="partner-1"))
        with self.assertRaises(AuthorizationError):
            authorize_scope(ctx, ResourceScope("brand-a", partner_id="partner-2"))

    def test_staff_cannot_assume_authority(self):
        ctx = RequestContext("brand-a", "staff-1", ActorType.STAFF)
        with self.assertRaises(AuthorizationError):
            authorize_scope(ctx, ResourceScope("brand-a"))

    def test_missing_identity_denied(self):
        with self.assertRaises(AuthorizationError):
            RequestContext("", "actor-1", ActorType.CUSTOMER, customer_id="cust-1")
        with self.assertRaises(AuthorizationError):
            RequestContext("brand-a", "actor-1", ActorType.PARTNER)


if __name__ == "__main__":
    unittest.main()
