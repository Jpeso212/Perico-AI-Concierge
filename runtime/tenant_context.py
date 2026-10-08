"""Fail-closed tenant and actor context for future concierge services.

Identity must come from authenticated middleware, never from AI-generated text.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class AuthorizationError(PermissionError):
    """Raised when a request cannot access a resource."""


class ActorType(str, Enum):
    CUSTOMER = "customer"
    STAFF = "staff"
    PARTNER = "partner"
    SYSTEM = "system"


@dataclass(frozen=True)
class RequestContext:
    brand_id: str
    actor_id: str
    actor_type: ActorType
    customer_id: Optional[str] = None
    partner_id: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.brand_id.strip() or not self.actor_id.strip():
            raise AuthorizationError("Authenticated brand and actor are required")
        if self.actor_type == ActorType.CUSTOMER and not self.customer_id:
            raise AuthorizationError("Customer actor requires authenticated customer_id")
        if self.actor_type == ActorType.PARTNER and not self.partner_id:
            raise AuthorizationError("Partner actor requires authenticated partner_id")


@dataclass(frozen=True)
class ResourceScope:
    brand_id: str
    customer_id: Optional[str] = None
    partner_id: Optional[str] = None


def authorize_scope(context: RequestContext, resource: ResourceScope) -> None:
    """Minimum isolation boundary; staff/system need separate action-level grants."""
    if not resource.brand_id or context.brand_id != resource.brand_id:
        raise AuthorizationError("Resource not accessible")
    if context.actor_type == ActorType.CUSTOMER:
        if not resource.customer_id or context.customer_id != resource.customer_id:
            raise AuthorizationError("Resource not accessible")
    elif context.actor_type == ActorType.PARTNER:
        if not resource.partner_id or context.partner_id != resource.partner_id:
            raise AuthorizationError("Resource not accessible")
    else:
        # Never interpret brand membership alone as staff/system permission.
        raise AuthorizationError("Explicit action-level authorization is required")
