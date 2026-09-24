# PERICO AI CONCIERGE — INTEGRATION REGISTRY & ADAPTER LAYER

## 1. PURPOSE

The Integration Registry & Adapter Layer defines how external systems connect to the Perico AI Concierge.

It supports current and future integrations including:

- Booking platforms
- Inventory systems
- Payment providers
- Communication channels
- CRM systems
- Reseller platforms
- Agency systems
- Accounting systems
- Analytics systems
- Notification systems
- Identity systems
- Supplier systems
- Internal Perico services
- Future APIs

Examples may include:

- Bókun
- Peek Pro
- Rezgo
- WhatsApp providers
- Payment processors
- CRM platforms
- Reseller networks
- Future Perico applications

CORE PRINCIPLE:

EXTERNAL SYSTEMS PROVIDE CAPABILITIES.

PERICO CONTROLS BUSINESS LOGIC.

---

# 2. ARCHITECTURAL ROLE

External platforms must connect through adapters whenever technically practical.

Conceptual architecture:

PERICO BUSINESS LOGIC
→ ORCHESTRATOR
→ INTEGRATION REGISTRY
→ APPROVED ADAPTER
→ EXTERNAL PLATFORM

Responses return through:

EXTERNAL PLATFORM
→ ADAPTER
→ NORMALIZED PERICO RESULT
→ ORCHESTRATOR
→ APPROPRIATE ENGINE

External provider-specific terminology should not become the core Perico business model.

---

# 3. INTEGRATION REGISTRY

The Integration Registry maintains information about approved external systems.

Each integration may contain:

integration_id

provider

integration_type

status

environment

supported_capabilities

supported_products

supported_partners

supported_channels

authentication_reference

webhook_support

availability_support

booking_support

payment_support

refund_support

last_verified

configuration_version

notes

Sensitive credentials must not be stored directly in ordinary registry documentation.

---

# 4. INTEGRATION TYPES

Canonical integration types may include:

CHANNEL

BOOKING

INVENTORY

PAYMENT

CRM

PARTNER

RESELLER

MESSAGING

ACCOUNTING

ANALYTICS

NOTIFICATION

IDENTITY

SUPPLIER

INTERNAL_SERVICE

OTHER

A provider may support more than one integration type.

---

# 5. INTEGRATION STATUS

Canonical integration states:

PLANNED

CONFIGURING

TESTING

ACTIVE

DEGRADED

DISABLED

SUSPENDED

FAILED

RETIRED

Only integrations in an appropriate operational state should be used for automated production actions.

---

# 6. ENVIRONMENTS

Where applicable, integrations should distinguish:

DEVELOPMENT

SANDBOX

STAGING

PRODUCTION

Test transactions must not be treated as real customer bookings or payments.

Production customer data must not be sent to test environments unless explicitly authorized and appropriately protected.

---

# 7. ADAPTER PRINCIPLE

Each external provider may use different:

- APIs
- Field names
- Statuses
- Product IDs
- Booking IDs
- Payment IDs
- Error codes
- Webhook formats
- Authentication methods

The adapter translates between:

PROVIDER-SPECIFIC FORMAT

and

PERICO CANONICAL FORMAT

Core Concierge engines should use canonical Perico data whenever possible.

---

# 8. PROVIDER INDEPENDENCE

Do not design core business logic specifically around:

Bókun

Peek Pro

Rezgo

or any other provider.

Instead:

PERICO REQUEST
→ REQUIRED CAPABILITY
→ APPROVED INTEGRATION
→ PROVIDER ADAPTER
→ NORMALIZED RESULT

This allows providers to be added, changed or replaced without rewriting Perico's business rules.

---

# 9. CAPABILITY-BASED ROUTING

The Orchestrator should request capabilities rather than specific providers whenever possible.

Examples:

CHECK_AVAILABILITY

CREATE_RESERVATION

MODIFY_RESERVATION

CANCEL_RESERVATION

CREATE_PAYMENT

VERIFY_PAYMENT

PROCESS_REFUND

SEND_MESSAGE

LOOKUP_CUSTOMER

SYNC_PARTNER

The Integration Registry determines which approved integration can perform the capability.

---

# 10. CANONICAL CAPABILITIES

Possible capabilities include:

SEARCH_PRODUCTS

GET_PRODUCT

GET_PRICE_REFERENCE

CHECK_SCHEDULE

CHECK_AVAILABILITY

HOLD_INVENTORY

RELEASE_INVENTORY

CREATE_RESERVATION

GET_RESERVATION

MODIFY_RESERVATION

CANCEL_RESERVATION

GET_PICKUP_INFORMATION

GET_VOUCHER

CREATE_PAYMENT

GET_PAYMENT

VERIFY_PAYMENT

CANCEL_PAYMENT

PROCESS_REFUND

GET_REFUND

SEND_MESSAGE

RECEIVE_MESSAGE

LOOKUP_CUSTOMER

CREATE_CUSTOMER

UPDATE_CUSTOMER

LOOKUP_PARTNER

SYNC_PARTNER

CREATE_WEBHOOK

RECEIVE_WEBHOOK

GET_REPORT

Additional capabilities may be introduced later.

---

# 11. CAPABILITY DOES NOT EQUAL AUTHORITY

An integration being technically capable of an action does not mean it is authorized to perform it.

Example:

A booking platform may support cancellation through its API.

That does not mean the Concierge may cancel every booking automatically.

Authorization must still pass:

- Identity
- Permissions
- Product rules
- Cancellation rules
- Commercial rules
- Booking state
- Human approval when required

TECHNICAL CAPABILITY ≠ BUSINESS AUTHORIZATION.

---

# 12. INTEGRATION SELECTION

Integration selection may depend on:

- Product
- Supplier
- Booking source
- Partner
- Channel
- Required capability
- Integration status
- Existing reservation location
- Payment method
- Commercial agreement
- Operational configuration

Do not choose an integration merely because it is available.

Use the integration authorized for the transaction.

---

# 13. PRODUCT-TO-INTEGRATION MAPPING

A Perico product may map to one or more external systems.

Possible mapping:

perico_product_id

integration_id

external_product_id

external_option_id

external_rate_id

external_schedule_id

external_supplier_id

mapping_status

last_verified

Never infer a mapping solely from similar product names.

Mappings must be explicit.

---

# 14. PARTNER-TO-INTEGRATION MAPPING

Partner identities may also map across systems.

Example:

perico_partner_id
→ Bókun reseller ID
→ Peek Pro account ID
→ Rezgo partner ID
→ CRM account ID

External IDs must not replace the canonical Perico partner identity.

---

# 15. CUSTOMER-TO-INTEGRATION MAPPING

Where needed:

perico_customer_id
→ CRM customer ID
→ booking-platform customer ID
→ payment-provider customer reference
→ messaging-platform contact ID

Only create mappings when operationally useful.

Avoid unnecessary duplication of customer data.

---

# 16. BOOKING IDENTIFIER MAPPING

A reservation may have multiple identifiers.

Example:

perico_booking_id

external_booking_id

booking_platform

supplier_booking_id

partner_booking_reference

customer_confirmation_reference

The canonical Perico booking ID should remain independent of external provider identifiers when technically possible.

---

# 17. PAYMENT IDENTIFIER MAPPING

Payment integrations may produce:

payment_provider

external_transaction_id

external_payment_id

external_refund_id

merchant_reference

These should map to:

perico_payment_id

and the applicable:

perico_booking_id

Never use external payment IDs as the only business identity when Perico can maintain its own identifier.

---

# 18. STANDARDIZED REQUEST ENVELOPE

Where technically practical, integration requests should include a standardized internal envelope.

Possible fields:

request_id

timestamp

actor_id

actor_type

channel

partner_id

customer_id

product_id

booking_id

payment_id

required_capability

integration_id

correlation_id

idempotency_key

Not every request requires every field.

---

# 19. STANDARDIZED RESULT ENVELOPE

Adapter responses should be normalized.

Possible fields:

request_id

integration_id

provider

capability

result_status

business_status

external_reference

perico_reference

data

error_type

error_code

error_message_internal

retryable

timestamp

Provider-specific responses may be retained internally when useful.

---

# 20. TECHNICAL STATUS VS BUSINESS STATUS

Always separate:

TECHNICAL STATUS

from:

BUSINESS STATUS

Examples:

Technical status:
SUCCESS

Business status:
NO_AVAILABILITY

Technical status:
FAILED

Business status:
UNKNOWN

Technical status:
SUCCESS

Business status:
PAYMENT_DECLINED

Technical status:
TIMEOUT

Business status:
UNKNOWN

Never convert a technical failure into an unsupported business conclusion.

---

# 21. CANONICAL TECHNICAL RESULTS

Possible technical results:

SUCCESS

PARTIAL_SUCCESS

FAILED

TIMEOUT

UNAUTHORIZED

FORBIDDEN

RATE_LIMITED

INVALID_REQUEST

PROVIDER_UNAVAILABLE

CONNECTION_ERROR

UNKNOWN_ERROR

These describe integration execution.

They do not automatically describe booking, availability or payment state.

---

# 22. AVAILABILITY NORMALIZATION

External systems may use statuses such as:

AVAILABLE

OPEN

BOOKABLE

SOLD_OUT

CLOSED

FULL

WAITLIST

UNAVAILABLE

Adapters should map them into canonical states defined by:

availability-engine.md

Do not invent availability when provider response is ambiguous.

---

# 23. BOOKING NORMALIZATION

External booking platforms may use different reservation states.

Adapters should map provider states into canonical Perico booking states defined by:

booking-engine.md

Provider state names must not silently redefine Perico confirmation logic.

---

# 24. PAYMENT NORMALIZATION

Payment providers may return:

AUTHORIZED

CAPTURED

PAID

SETTLED

PENDING

FAILED

DECLINED

CANCELLED

REFUNDED

or other terminology.

Adapters must map these into the canonical payment states defined by:

payment-confirmation-engine.md

External "PAID" does not automatically mean Perico booking "CONFIRMED."

---

# 25. PROVIDER ERROR NORMALIZATION

Provider errors should be classified.

Possible categories:

AUTHENTICATION_ERROR

AUTHORIZATION_ERROR

VALIDATION_ERROR

RATE_LIMIT

NETWORK_ERROR

TIMEOUT

PROVIDER_ERROR

PRODUCT_MAPPING_ERROR

PARTNER_MAPPING_ERROR

CUSTOMER_MAPPING_ERROR

BOOKING_MAPPING_ERROR

PAYMENT_MAPPING_ERROR

WEBHOOK_ERROR

UNKNOWN_ERROR

Errors should not be exposed raw to customers unless intentionally transformed into safe customer-facing language.

---

# 26. RETRY LOGIC

Retry may be appropriate for some technical failures.

Possible retryable conditions:

- Timeout
- Temporary network failure
- Provider temporary unavailable
- Rate limit after appropriate delay

Do not automatically retry actions that may create duplicates unless idempotency protection exists.

---

# 27. IDEMPOTENCY

Use idempotency protection whenever supported for actions such as:

CREATE_RESERVATION

CREATE_PAYMENT

PROCESS_REFUND

CANCEL_RESERVATION

Repeated execution caused by:

- Timeout
- Network retry
- Webhook duplication
- User double-click
- System retry

must not automatically create duplicate business transactions.

---

# 28. CORRELATION ID

A correlation ID should connect related events across systems when technically possible.

Example:

Customer request
→ Quote
→ Availability check
→ Booking
→ Payment
→ Confirmation

A shared correlation reference can improve troubleshooting and auditability.

---

# 29. WEBHOOKS

Approved integrations may send events through webhooks.

Possible events:

AVAILABILITY_CHANGED

RESERVATION_CREATED

RESERVATION_UPDATED

RESERVATION_CANCELLED

PAYMENT_CREATED

PAYMENT_SUBMITTED

PAYMENT_VERIFIED

PAYMENT_FAILED

REFUND_CREATED

REFUND_COMPLETED

PICKUP_UPDATED

VOUCHER_READY

PARTNER_UPDATED

CUSTOMER_UPDATED

Every webhook must be validated before changing Perico state.

---

# 30. WEBHOOK AUTHENTICATION

Webhook authenticity should be verified using the provider's approved security mechanism when available.

Possible mechanisms:

- Signature
- Shared secret
- Token
- Certificate
- Provider verification method

Never trust an incoming webhook merely because its payload looks correct.

---

# 31. WEBHOOK DUPLICATION

Providers may deliver the same webhook multiple times.

The system should detect duplicate events when technically possible.

Duplicate webhook delivery must not create:

- Duplicate reservation
- Duplicate payment
- Duplicate refund
- Duplicate cancellation
- Duplicate notification

---

# 32. WEBHOOK ORDERING

Events may arrive out of order.

Example:

PAYMENT_VERIFIED

may arrive before:

PAYMENT_SUBMITTED

The system should use timestamps, provider references and canonical state logic rather than blindly applying events in arrival order.

---

# 33. POLLING

When webhook support is unavailable or insufficient, approved integrations may require polling.

Polling frequency should respect:

- Provider limits
- Operational need
- Cost
- Rate limits
- Customer urgency

Do not treat lack of webhook support as lack of automation capability.

---

# 34. SOURCE FRESHNESS

Integration data should preserve freshness when relevant.

Possible fields:

retrieved_at

provider_updated_at

expires_at

cache_status

Availability information may become stale quickly.

Never present stale inventory as confirmed live availability when freshness requirements are not satisfied.

---

# 35. CACHING

Caching may improve performance for:

- Product descriptions
- Static schedules
- Destination information
- Non-sensitive reference data

Use caution when caching:

- Availability
- Price
- Payment status
- Booking status
- Pickup time
- Partner permissions

Dynamic information should respect appropriate freshness rules.

---

# 36. PRICE DATA FROM EXTERNAL SYSTEMS

External platforms may contain prices.

Those prices are reference data unless the approved Perico pricing architecture designates that system as authoritative for that specific pricing context.

Do not automatically overwrite Perico product pricing from:

- Supplier website
- OTA
- Marketplace
- Booking platform
- Reseller system
- Promotion feed

Quote Engine remains responsible for customer quote logic.

---

# 37. SUPPLIER PROMOTION PROTECTION

If an external system returns:

PROMOTIONAL_PRICE

DISCOUNT_CODE

FLASH_SALE

DIRECT_BOOKING_PRICE

EARLY_BOOKING_DISCOUNT

do not automatically apply it.

Supplier promotions do not automatically apply to Perico agency bookings.

Use approved Perico pricing rules.

---

# 38. EXTERNAL WEBSITE PROTECTION

Integration data may contain URLs.

Possible examples:

supplier_url

checkout_url

booking_url

product_url

support_url

customer_portal_url

The existence of a URL in integration data does NOT authorize customer exposure.

Customer-facing URL decisions must obey:

global-rules.md

Supplier and competitor destinations remain protected.

---

# 39. CUSTOMER-FACING PAYMENT DESTINATIONS

A payment adapter may generate an approved customer-facing payment destination only when:

- It is approved by Perico
- It is authorized for the transaction
- It belongs to an approved Perico payment workflow
- The applicable Payment Router selects it

Never expose supplier checkout as a substitute.

---

# 40. BOOKING PLATFORM CUSTOMER PAGES

An external booking platform may generate:

- Voucher URL
- Booking-management URL
- Customer portal URL

These must not automatically be sent to the customer.

Customer exposure requires explicit Perico authorization.

---

# 41. CHANNEL ADAPTERS

Communication platforms should connect through channel adapters.

Possible channels:

WHATSAPP

WEBSITE_CHAT

WEB_FORM

EMAIL

INSTAGRAM

FACEBOOK

SMS

PARTNER_PORTAL

STAFF_INTERFACE

FUTURE_CHANNEL

Channel adapters should normalize incoming messages into the Perico conversation model.

---

# 42. CHANNEL INBOUND MESSAGE

A normalized inbound message may contain:

message_id

channel

channel_account

customer_reference

partner_reference

timestamp

language_hint

message_type

text

attachments

reply_to

conversation_id

metadata

Do not treat unverified metadata as trusted identity.

---

# 43. CHANNEL OUTBOUND MESSAGE

A normalized outbound message may contain:

conversation_id

channel

recipient

language

message_type

content

attachments

booking_reference

payment_reference

metadata

The final content remains controlled by Perico business logic and Language Engine.

---

# 44. CHANNEL CAPABILITIES

Different channels may support:

TEXT

IMAGE

VIDEO

AUDIO

DOCUMENT

BUTTONS

QUICK_REPLIES

PAYMENT_BUTTON

LOCATION

TEMPLATE_MESSAGE

RICH_CARD

Do not make core business logic depend on one channel feature.

If a feature is unavailable, use an appropriate fallback presentation.

---

# 45. CRM ADAPTERS

CRM integrations may support:

LOOKUP_CUSTOMER

CREATE_CUSTOMER

UPDATE_CUSTOMER

CREATE_LEAD

UPDATE_LEAD

LOOKUP_PARTNER

UPDATE_PARTNER

CREATE_ACTIVITY

GET_ACTIVITY

CRM data must obey Identity & Permissions.

CRM data is not automatically authoritative for product pricing or availability.

---

# 46. RESELLER SYSTEM ADAPTERS

Reseller platforms may support:

GET_PARTNER

GET_PARTNER_TERMS

GET_PARTNER_BOOKINGS

CREATE_PARTNER_BOOKING

GET_COMMISSION

SYNC_SALE

Commercial authority remains controlled by:

partner-reseller-engine.md

and

identity-permissions-engine.md

---

# 47. PAYMENT ADAPTERS

Payment provider adapters may support:

CREATE_PAYMENT

GET_PAYMENT

VERIFY_PAYMENT

CANCEL_PAYMENT

PROCESS_REFUND

GET_REFUND

Provider-specific payment execution should remain separate from payment business policy.

Payment method selection belongs to the future Payment Router.

---

# 48. BOOKING ADAPTERS

Booking adapters may support:

CHECK_AVAILABILITY

HOLD_INVENTORY

CREATE_RESERVATION

GET_RESERVATION

MODIFY_RESERVATION

CANCEL_RESERVATION

GET_PICKUP_INFORMATION

GET_VOUCHER

The applicable product determines which booking source is authorized.

---

# 49. MULTIPLE SOURCES FOR ONE PRODUCT

A product may theoretically be available through multiple approved systems.

The Orchestrator must not query or book randomly.

Routing rules may consider:

- Primary integration
- Secondary integration
- Partner source
- Existing booking location
- Supplier
- Channel
- Availability
- Commercial rule
- Operational configuration

---

# 50. PRIMARY AND FALLBACK INTEGRATIONS

A capability may have:

PRIMARY_INTEGRATION

and approved:

FALLBACK_INTEGRATION

Fallback is permitted only when business rules allow it.

Do not use fallback merely to bypass:

- Product restriction
- Partner restriction
- Price rule
- Payment rule
- Availability rule

---

# 51. EXISTING RESERVATION PLATFORM

Once a reservation is created in a particular booking system, subsequent actions should normally route to the system holding that reservation unless an approved synchronization or migration workflow exists.

Do not create a second reservation in another platform merely because the first platform temporarily fails.

---

# 52. INTEGRATION FAILURE

If an integration fails:

1. Preserve transaction context.
2. Determine whether the action may have completed.
3. Check idempotency/reference data.
4. Retry only when safe.
5. Use approved fallback when permitted.
6. Otherwise use Perico Human Assistance.

Never assume failure means the business action did not occur.

---

# 53. UNCERTAIN TRANSACTION RESULT

A timeout after submitting a booking or payment may create:

TRANSACTION_RESULT_UNKNOWN

Before retrying:

CHECK EXISTING TRANSACTION.

This prevents duplicate bookings and duplicate charges.

---

# 54. CIRCUIT BREAKER

Repeated provider failures should eventually prevent repeated automated attempts when technically supported.

Possible state:

INTEGRATION DEGRADED

or

INTEGRATION TEMPORARILY DISABLED

This protects customer experience and prevents cascading failures.

---

# 55. RATE LIMITS

External providers may impose rate limits.

Adapters should respect provider limits.

Rate limiting must not be communicated to the customer as:

SOLD OUT

PAYMENT FAILED

BOOKING REJECTED

unless that business result was independently established.

---

# 56. AUTHENTICATION

Integration authentication may use:

API key

OAuth

Access token

Client credentials

Signed request

Certificate

Other approved mechanism

Credentials must be stored securely outside normal business documentation.

---

# 57. SECRET MANAGEMENT

Never store active secrets directly in:

- Product Markdown
- Customer conversations
- Public repository files
- Logs intended for ordinary viewing
- Prompt text

Use secure secret-management infrastructure.

Registry documentation should store only a safe:

authentication_reference

when needed.

---

# 58. ACCESS SCOPE

Integration credentials should use the minimum required scope.

Example:

A booking adapter needing reservation creation should not automatically receive administrative account permissions.

Use least privilege.

---

# 59. DATA MINIMIZATION

Send only necessary data to external providers.

Do not send:

- Entire customer conversation
- Supplier costs
- Unrelated customer records
- Partner commission
- Internal notes

unless operationally required and authorized.

---

# 60. CUSTOMER DATA

Customer data sent to external systems must be limited to what is required for the approved transaction.

Identity and privacy rules remain controlled by:

identity-permissions-engine.md

---

# 61. LOGGING

Integration activity should be auditable when technically supported.

Possible fields:

request_id

integration_id

capability

actor_id

customer_id

partner_id

booking_id

payment_id

timestamp

technical_result

business_result

duration

retry_count

Do not log secret credentials.

---

# 62. OBSERVABILITY

Future operational monitoring should be able to identify:

- Integration availability
- Error rate
- Response time
- Failed bookings
- Unknown transaction results
- Payment verification delays
- Webhook failures
- Mapping errors
- Repeated retries

Monitoring must not redefine business status.

---

# 63. ALERTING

Critical integration failures may generate internal Perico alerts.

Examples:

- Booking provider unavailable
- Payment provider unavailable
- Webhook authentication failures
- High booking failure rate
- Mapping failure
- Repeated unknown payment state

Customer notification should follow the applicable customer workflow rather than exposing raw technical errors.

---

# 64. TEST MODE

Integrations should support safe testing where possible.

Test data should be clearly distinguishable from production data.

Possible marker:

environment = SANDBOX

or

is_test = true

Test booking must never become a real operational reservation accidentally.

---

# 65. INTEGRATION CERTIFICATION

Before an integration becomes ACTIVE, Perico should verify:

- Authentication
- Required capabilities
- Product mapping
- Partner mapping when applicable
- Availability mapping
- Booking state mapping
- Payment state mapping when applicable
- Error handling
- Retry behavior
- Idempotency
- Webhooks
- Data visibility
- Customer-facing behavior
- External website protection

---

# 66. VERSIONING

Provider APIs may change.

Integration configuration should preserve:

api_version

adapter_version

configuration_version

when technically relevant.

Do not assume an integration remains correct forever after initial setup.

---

# 67. DEPRECATION

When a provider or API version is being retired:

Mark the integration appropriately.

Example:

DEPRECATED

MIGRATION_REQUIRED

RETIRED

Do not silently route new transactions through unsupported integrations.

---

# 68. MIGRATION

Moving from one provider to another must preserve:

- Perico product identity
- Existing booking identity
- Customer history
- Partner attribution
- Payment references
- Operational obligations

Do not duplicate existing bookings during migration.

---

# 69. BÓKUN

Bókun may be used as an approved integration for applicable Perico products and website reservations.

Its exact capabilities depend on the implemented connection.

Bókun remains:

AN INTEGRATION

not:

THE PERICO BUSINESS BRAIN.

---

# 70. PEEK PRO

Peek Pro may be integrated when approved by Perico.

Its supported capabilities must be recorded in the Integration Registry.

Do not assume Peek Pro functionality before the actual integration is implemented and verified.

---

# 71. REZGO

Rezgo may be integrated when approved by Perico.

Its supported capabilities must be recorded in the Integration Registry.

Do not assume Rezgo functionality before the actual integration is implemented and verified.

---

# 72. FUTURE PROVIDERS

Adding a new provider should normally require:

1. Register integration.
2. Define integration type.
3. Define capabilities.
4. Configure authentication.
5. Create adapter.
6. Map applicable products/partners.
7. Map provider statuses.
8. Implement error handling.
9. Implement idempotency where applicable.
10. Test.
11. Approve.
12. Activate.

Core Perico engines should not require redesign merely because a new provider is added.

---

# 73. HUMAN HANDOFF

Use:

human-handoff-engine.md

when:

- Integration fails and no safe fallback exists
- Transaction result is unknown
- Product mapping is missing
- Partner mapping is missing
- Provider response conflicts with Perico data
- Booking cannot be safely retried
- Payment cannot be safely verified
- Refund state is uncertain
- External platform reports contradictory status
- Required capability is unavailable

Preserve all transaction context.

---

# 74. CUSTOMER COMMUNICATION DURING FAILURE

Do not expose unnecessary technical details.

Instead of:

"Rezgo API returned HTTP 503."

Use customer-appropriate language such as:

"I'm checking the reservation status with our operations system."

Only claim that Perico staff is actively reviewing when a handoff has actually been submitted.

---

# 75. INTEGRATION SECURITY RULE

Never allow external provider data to override:

- Global Rules
- Identity permissions
- Product safety rules
- Approved pricing authority
- Payment policy
- Confirmation requirements
- Customer data protections

without an explicitly authorized Perico rule.

---

# 76. FINAL INTEGRATION VALIDATION

Before executing an external action, verify:

1. Required capability identified.
2. Integration approved.
3. Integration operational.
4. Correct environment.
5. Actor authorized.
6. Product mapped.
7. Partner mapped when required.
8. Required data complete.
9. Business rules satisfied.
10. Idempotency applied when appropriate.
11. No protected data unnecessarily exposed.
12. Customer-facing destination authorized.
13. Result will map into canonical Perico state.

If not:

DO NOT EXECUTE UNSAFELY.

---

# 77. NON-NEGOTIABLE RULE

NEVER CONFUSE:

API SUCCESS
WITH
BUSINESS SUCCESS.

NEVER CONFUSE:

API FAILURE
WITH
BUSINESS FAILURE.

NEVER CONFUSE:

PLATFORM DATA
WITH
PERICO BUSINESS AUTHORITY.

NEVER CONFUSE:

TECHNICAL CAPABILITY
WITH
BUSINESS PERMISSION.

---

# 78. CORE PRINCIPLE

ONE PERICO BUSINESS BRAIN.

STANDARDIZED ADAPTERS.

MULTIPLE BOOKING PLATFORMS.

MULTIPLE PAYMENT PROVIDERS.

MULTIPLE COMMUNICATION CHANNELS.

MULTIPLE RESELLER SYSTEMS.

NO PLATFORM LOCK-IN.