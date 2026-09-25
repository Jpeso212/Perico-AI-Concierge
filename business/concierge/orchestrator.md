# PERICO AI CONCIERGE — ORCHESTRATOR

## 1. PURPOSE

The Orchestrator is the central routing and authority layer of the Perico AI Concierge.

It coordinates:

- Customer conversations
- Product discovery
- Product matching
- Quotes
- Availability
- Reservations
- Payments
- Confirmation
- Human assistance
- Languages
- Sales channels
- Resellers
- Travel agencies
- Virtual reseller agents
- Booking platforms
- Payment providers
- Future integrations

The Orchestrator does NOT replace the specialized Concierge engines.

Its purpose is to determine:

1. Who is interacting with Perico.
2. What they want.
3. Which internal engine should handle the request.
4. Which source has authority.
5. Which external integration may be used.
6. What information may be exposed.
7. What state the transaction is currently in.
8. What the next valid action is.
9. When automation must stop.
10. When Perico Human Assistance is required.

CORE PRINCIPLE:

MANY CHANNELS.
MANY SELLERS.
MANY BOOKING SYSTEMS.
MANY PAYMENT METHODS.
ONE PERICO SOURCE OF TRUTH.

---

# 2. CORE ARCHITECTURE LAYERS AND ENGINES

The Orchestrator coordinates the following authoritative architecture components:

## Global Authority

1. global-rules.md

Defines the highest-level rules that apply across the entire Perico AI Platform.

---

## Brand and Commercial Context

2. brand-commercial-policy-layer.md

Defines:

- brand_id
- Brand isolation
- Brand-specific product access
- Brand offers
- Brand-specific commercial policy
- Brand pricing context
- Brand payment presentation
- Brand channel authorization
- Brand transaction persistence

Brand context must be established before brand-sensitive commercial execution.

---

## Identity and Permissions

3. identity-permissions-engine.md

Determines:

- Actor identity
- Verification level
- Permissions
- Data visibility
- Staff authorization
- Partner authorization
- Virtual agent authorization
- Protected information access

Identity and permission decisions must occur before protected commercial or transactional actions.

---

## Communication and Language

4. language-engine.md
5. channel-layer.md
6. conversation-engine.md

These components control:

- Customer language
- Channel transport
- Conversation behavior
- Context continuity
- Message presentation
- Customer intent

Channel and language must never redefine business truth.

---

## Product Discovery and Commercial Calculation

7. product-matching-engine.md
8. quote-engine.md

These components control:

- Product discovery
- Customer-product matching
- Pricing model selection
- Approved price calculation
- Commercial quote generation

Brand and actor context must be available when they materially affect product access or price.

---

## Availability and Booking

9. availability-engine.md
10. booking-engine.md

These components control:

- Schedule eligibility
- Live availability
- Reservation requirements
- Booking data
- Reservation lifecycle
- Operational booking state

Availability and booking remain separate from payment and final confirmation.

---

## Payment

11. payment-confirmation-engine.md
12. payment-router.md

payment-confirmation-engine.md determines:

- What payment is required
- Deposit/full-payment requirements
- Payment verification
- Balance
- Refund-policy logic
- Payment-related confirmation eligibility

payment-router.md determines:

- Which approved payment method may be used
- Which approved payment provider may execute it
- Routing
- Provider fallback
- Transaction protection

Payment policy and payment execution must remain separate.

---

## Partners and Distribution

13. partner-reseller-engine.md
14. virtual-reseller-agent-layer.md

These components control:

- Partner relationships
- Reseller commercial profiles
- Partner permissions
- Commission structures
- Product access
- Virtual sales-agent specialization
- Sales attribution
- Agent scope

Virtual agents and partners do not create independent business truth.

---

## Integrations

15. integration-registry.md

Defines the standardized adapter and integration architecture for:

- Booking systems
- Inventory systems
- Payment providers
- Messaging platforms
- CRM systems
- Partner systems
- Supplier integrations
- Future external systems

External integrations provide capabilities.

They do not define Perico business policy.

---

## Human Assistance

16. human-handoff-engine.md

Controls escalation from any stage when automation cannot safely continue.

Human Handoff preserves:

- brand_id
- Customer context
- Product context
- Commercial context
- Booking context
- Payment context
- Partner context
- Agent context

The customer remains inside the active Perico-controlled sales environment.

---

The Orchestrator coordinates these components.

It must not duplicate detailed business logic already maintained by the authoritative specialized component.

When two components appear to overlap, the component explicitly assigned authority for that decision must control the result.

If authority cannot be established safely:

DATA CONFLICT
→ PERICO HUMAN ASSISTANCE

---

# 3. GLOBAL RULE AUTHORITY

global-rules.md applies across the entire Concierge.

No channel, reseller, virtual agent, booking platform, payment provider or integration may override a Global Rule unless an explicitly approved Perico rule establishes an authorized exception.

Global Rules include customer sales-channel protection and restrictions against exposing external supplier or competitor booking destinations.

---

# 4. DATA AUTHORITY

Operational decisions must use the most authoritative approved Perico information available.

General authority hierarchy:

1. Explicit current Perico operational override
2. Product-specific or transfer-specific approved Perico master
3. Customer/account-specific approved commercial agreement
4. Approved B2B / reseller commercial rule when applicable
5. Specialized Concierge engine rule
6. Approved Perico global business rule
7. Verified supplier operational information when Perico has not established a conflicting rule
8. Human confirmation when authoritative information is missing or conflicting

Historical catalogs, obsolete files, supplier promotions, previous quotes, competitor information and external marketplace information must not silently override current approved Perico information.

When two authoritative sources conflict and precedence cannot safely resolve the conflict:

DATA CONFLICT
→ PERICO HUMAN ASSISTANCE

Never guess which rule should win.

---

# 5. PRODUCT SOURCE OF TRUTH

Approved product masters under:

business/tours/

are the operational product authority for excursions.

Approved transfer masters under:

business/transfers/

are the operational authority for transfers.

Product identity, pricing model, inclusions, restrictions, transportation rules, supplier identity, capacity and product-specific conditions should be retrieved from the appropriate master.

Do not create product facts inside the Orchestrator.

---

# 6. CUSTOMER LANGUAGE

Language handling is controlled by:

language-engine.md

Language affects communication.

Language must NOT change:

- Product identity
- Selling price
- Availability
- Booking requirements
- Payment requirements
- Cancellation policy
- Safety restrictions
- Operational rules
- Partner permissions
- Commission rules
- Confirmation requirements

The customer may change languages without restarting the workflow.

---

# 7. ACTOR IDENTIFICATION

Before applying commercial or permission-sensitive logic, identify the actor when relevant.

Possible actor types include:

DIRECT_CUSTOMER

B2B_AGENCY

AUTHORIZED_RESELLER

HOTEL_CONCIERGE

AFFILIATE

VIRTUAL_RESELLER

PERICO_STAFF

UNKNOWN_ACTOR

Actor identity must never be assumed merely from language, nationality, communication channel or message style.

If actor type materially affects price, commission, payment terms or data visibility and identity is unresolved:

IDENTITY REQUIRED

or

PERICO HUMAN ASSISTANCE

as appropriate.

---

# 8. PERMISSION PRINCIPLE

Different actors may have access to different information and actions.

Examples:

A direct customer may receive:

- Retail price
- Customer-facing inclusions
- Availability
- Payment instructions
- Booking confirmation

An approved reseller may additionally receive authorized:

- Reseller pricing
- Commission structure
- Commercial booking terms
- Partner-specific payment terms

Perico staff may access authorized internal operational information.

The Concierge must NEVER expose internal information merely because it exists in the knowledge base.

---

# 9. PROTECTED INTERNAL INFORMATION

Unless explicitly authorized for the current actor, never expose:

- Supplier net cost
- Internal Perico cost
- Internal margins
- Internal commissions
- Supplier commission
- Confidential agency rates
- Another agency's rates
- Supplier contact information
- Supplier booking links
- Supplier payment links
- Internal operational notes
- Internal negotiation history
- Private credentials
- API credentials
- Internal system identifiers not intended for customers

Data visibility must be determined before generating the response.

---

# 10. PRIMARY CUSTOMER FLOW

The standard conceptual flow is:

CUSTOMER MESSAGE
→ BRAND CONTEXT
→ CHANNEL CONTEXT
→ LANGUAGE
→ CONVERSATION / INTENT
→ ACTOR / IDENTITY / PERMISSION CONTEXT WHEN REQUIRED
→ VIRTUAL AGENT CONTEXT WHEN APPLICABLE
→ PRODUCT MATCHING
→ BRAND COMMERCIAL CONTEXT
→ QUOTE
→ AVAILABILITY
→ BOOKING
→ PAYMENT REQUIREMENT
→ PAYMENT ROUTING
→ PAYMENT VERIFICATION
→ OPERATIONAL ACCEPTANCE
→ CONFIRMATION
The transaction should preserve, when applicable:

brand_id

channel_id

customer_id

actor_type

partner_id

agent_id

product_id

brand_offer_id

quote_id

booking_id

payment_id

booking_integration_id

payment_provider

These identifiers represent different architectural concepts and must not be treated as interchangeable.

Not every conversation requires every stage.

The Orchestrator should enter the workflow at the stage appropriate to the customer's actual request.

---

# 11. CONTEXT PRESERVATION

Information already provided by the customer must remain available throughout the workflow.

Examples:

- Customer name
- Language
- Product
- Date
- Number of participants
- Participant ages
- Hotel
- Pickup location
- Flight information
- Product configuration
- Private/shared preference
- Quoted price
- Availability state
- Booking state
- Payment state
- Special requests
- Partner/reseller identity

Do not repeatedly ask for information already known and still valid.

---

# 12. PRODUCT DISCOVERY

When the customer has not selected a specific product:

conversation-engine.md
+
product-matching-engine.md

should determine the customer's needs and identify appropriate verified Perico products.

Do not recommend products based primarily on:

- Supplier commission
- Perico margin
- External rankings
- Supplier promotions
- Fake popularity
- Invented scarcity

The customer makes the final decision.

---

# 13. QUOTE ROUTING

Pricing calculations are controlled by:

quote-engine.md

The Orchestrator must determine the correct pricing context before requesting a quote.

Possible contexts include:

RETAIL

B2B

AUTHORIZED_RESELLER

ACCOUNT_SPECIFIC

CUSTOM_QUOTE

The pricing context must not be inferred solely from communication channel.

If the applicable price cannot be established safely:

QUOTE REQUIRED
→ PERICO HUMAN ASSISTANCE

---

# 14. PRICE IS NOT AVAILABILITY

A valid price does not prove availability.

The following are separate:

PRODUCT EXISTS

PRICE AVAILABLE

SCHEDULE ELIGIBLE

LIVE AVAILABILITY CONFIRMED

RESERVATION CREATED

PAYMENT RECEIVED

OPERATIONAL ACCEPTANCE

CONFIRMED

Never collapse these states.

---

# 15. AVAILABILITY ROUTING

Availability logic is controlled by:

availability-engine.md

The Orchestrator may obtain live availability through an approved integration.

Possible availability sources may include:

- Perico-controlled inventory
- Bókun
- Peek Pro
- Rezgo
- Other approved reservation systems
- Approved supplier integrations
- Authorized Perico staff

An integration may report inventory.

It does not automatically control Perico business policy.

If an integration fails:

INTEGRATION FAILURE

does NOT mean:

SOLD OUT

UNAVAILABLE

CANCELLED

or

PAYMENT FAILED

Use another authorized source or Perico Human Assistance.

---

# 16. BOOKING ROUTING

Booking logic is controlled by:

booking-engine.md

A reservation may eventually be created through:

- Perico internal system
- Bókun
- Peek Pro
- Rezgo
- Another approved reservation platform
- Approved supplier integration
- Perico staff workflow

The booking platform is an execution system.

It is not automatically the authority for:

- Perico selling price
- Customer policy
- Reseller permissions
- Payment policy
- Customer communication
- Cross-platform business rules

---

# 17. BOOKING PLATFORM ABSTRACTION

Every booking integration should expose standardized capabilities where possible.

Examples:

CHECK_AVAILABILITY

CREATE_RESERVATION

HOLD_INVENTORY

UPDATE_RESERVATION

CANCEL_RESERVATION

RETRIEVE_RESERVATION

RETRIEVE_PICKUP_INFORMATION

RETRIEVE_VOUCHER

CONFIRM_RESERVATION_STATUS

Not every platform will support every capability.

The Orchestrator must know which capabilities are supported before attempting an action.

---

# 18. MULTIPLE BOOKING SYSTEMS

Perico may use multiple booking platforms simultaneously.

Therefore:

Do not hard-code the Concierge around Bókun.

Do not hard-code the Concierge around Peek Pro.

Do not hard-code the Concierge around Rezgo.

Do not hard-code the Concierge around any future provider.

Instead:

PRODUCT
→ APPROVED INVENTORY SOURCE
→ APPROVED BOOKING ADAPTER
→ STANDARDIZED RESULT

The product master or integration registry should identify the appropriate system when required.

---

# 19. BÓKUN ROLE

Bókun may be used as an approved reservation and availability integration.

Bókun is NOT the Perico AI Concierge brain.

Perico business rules remain controlled by the approved Perico knowledge base and Concierge engines.

---

# 20. RESELLER AND AGENCY NETWORK

Perico may distribute products through:

- Travel agencies
- Tour operators
- Hotels
- Concierges
- Affiliates
- Independent resellers
- Online partners
- Virtual reseller agents
- Other approved distribution partners

Each partner may have its own:

- Identity
- Permission level
- Commercial agreement
- Pricing access
- Commission structure
- Payment terms
- Booking privileges
- Product access
- Reporting requirements

These must not be generalized across all partners.

---

# 21. VIRTUAL RESELLERS

Virtual reseller agents operate on top of the Perico Concierge architecture.

They may specialize in areas such as:

- Direct consumer sales
- B2B sales
- Hotels and concierges
- Transfers
- Excursions
- Groups
- MICE
- Weddings
- Luxury travel
- Multilingual sales
- Destination-specific sales

Virtual reseller agents must use the same authoritative Perico product and operational data.

They may have different:

- Sales style
- Assigned market
- Language
- Customer segment
- Product specialization
- Authorized commercial permissions

They may NOT independently invent:

- Products
- Prices
- Discounts
- Commissions
- Availability
- Payment terms
- Cancellation policies
- Supplier commitments
- Confirmation status

---

# 22. VIRTUAL RESELLER ATTRIBUTION

When technically supported, sales generated by virtual reseller agents should preserve attribution.

Possible fields:

agent_id

agent_type

channel

campaign

partner_id

customer_id

booking_id

product_id

quote_id

payment_id

Attribution must not change the approved customer price unless an authorized commercial rule explicitly permits it.

---

# 23. PAYMENT AUTHORITY

Payment business logic is controlled by:

payment-confirmation-engine.md

The Orchestrator must distinguish:

PAYMENT REQUIREMENT

PAYMENT METHOD

PAYMENT PROVIDER

PAYMENT TRANSACTION

PAYMENT VERIFICATION

BOOKING CONFIRMATION

These are not interchangeable.

---

# 24. PAYMENT ROUTER

Perico may support multiple payment methods and providers.

The architecture must therefore use a Payment Router.

The Payment Router determines which approved payment options are valid for the current transaction.

It may consider:

- Actor type
- Customer/account agreement
- B2C vs B2B
- Product
- Booking total
- Deposit requirement
- Balance requirement
- Currency
- Customer location when legitimately relevant
- Provider availability
- Transaction limits
- Processing fees
- Automation capability
- Payment verification capability
- Refund capability
- Perico operational preference
- Approved commercial terms

The Payment Router must never invent a payment method or fee.

---

# 25. PAYMENT PROVIDER ABSTRACTION

Payment providers should return standardized transaction information where possible.

Possible fields:

payment_provider

payment_method

transaction_id

booking_id

customer_id

partner_id

currency

booking_total

amount_required_now

amount_submitted

amount_verified

balance_remaining

processing_fee

payment_status

verification_status

created_at

verified_at

The exact external provider format may differ.

Adapters should normalize provider responses into the Perico payment model.

---

# 26. PAYMENT STATES

Canonical payment states are controlled by:

payment-confirmation-engine.md

External provider terminology must be mapped into the approved Perico payment states.

An external provider saying:

SUCCESS

CAPTURED

COMPLETED

PAID

or similar

must not automatically create a CONFIRMED reservation.

Payment verification and booking confirmation remain separate.

---

# 27. PAYMENT ROUTING FAILURE

If a payment provider is unavailable:

Do not automatically cancel the reservation.

Do not mark payment as failed unless the transaction actually failed.

Possible state:

PAYMENT METHOD UNAVAILABLE

or

PAYMENT INTEGRATION FAILURE

Then:

- Try another authorized Perico payment method when permitted
or
- Use Perico Human Assistance.

Never redirect the customer to a supplier payment system.

---

# 28. PAYMENT SECURITY

The Concierge must never request or store:

- Full card number
- CVV
- PIN
- Banking password
- Authentication code
- Private payment credentials

Sensitive payment entry should occur only through approved secure Perico payment infrastructure.

---

# 29. PAYMENT LINK PROTECTION

Any customer-facing payment link must be an approved Perico-controlled or Perico-authorized payment destination.

Never send:

- Supplier checkout
- Supplier payment page
- OTA checkout
- Marketplace checkout
- Competitor payment page
- Affiliate payment page not authorized by Perico

If an approved payment destination cannot be generated:

PERICO HUMAN ASSISTANCE

---

# 30. CONFIRMATION AUTHORITY

A reservation becomes CONFIRMED only when all conditions required by the applicable workflow are satisfied.

Possible requirements include:

- Product identified
- Required customer information complete
- Approved price established
- Availability confirmed
- Reservation successfully created when required
- Required payment verified
- Operational acceptance completed when required

Never use the word CONFIRMED merely because:

- Customer accepted the price
- Customer provided information
- Availability existed
- Payment link was sent
- Customer said they paid
- Payment was submitted
- Payment was verified
- Reservation record was created

unless the complete applicable confirmation requirements are satisfied.

---

# 31. OPERATIONAL ACCEPTANCE

Operational acceptance is separate from payment.

Depending on the product or workflow, acceptance may come from:

- Approved automated booking system
- Approved inventory system
- Supplier integration
- Perico operations
- Authorized Perico staff

If operational acceptance is required and unresolved:

PENDING OPERATIONAL ACCEPTANCE

Do not mark the reservation CONFIRMED.

---

# 32. HUMAN HANDOFF

Human escalation is controlled by:

human-handoff-engine.md

Human assistance may be triggered from ANY stage.

Examples:

- Pricing conflict
- Missing approved price
- Availability uncertainty
- Product data conflict
- Booking integration failure
- Payment verification problem
- Refund request
- Large group
- Special request
- B2B exception
- Partner permission issue
- Operational issue
- Safety concern
- Complaint
- Technical failure

The customer remains inside the Perico service environment.

Never solve a handoff by redirecting the customer to a supplier.

---

# 33. HANDOFF CONTEXT

The Orchestrator must pass all relevant known context into Human Handoff.

The human should receive enough information to continue the transaction without forcing the customer to repeat the conversation.

After resolution, automation should resume from the appropriate workflow state whenever possible.

---

# 34. EXTERNAL WEBSITE PROTECTION

External product websites are internal research resources only.

Under no circumstances may the Concierge expose, recommend or redirect customers to:

- Supplier websites
- Supplier booking pages
- Supplier contact pages
- Supplier payment pages
- OTA product pages
- Marketplace product pages
- Competitor websites
- Affiliate booking destinations not authorized by Perico

This applies regardless of:

- Channel
- Language
- Customer type
- Reseller
- Virtual reseller
- Booking platform
- Availability problem
- Payment problem

When automation cannot proceed:

PERICO HUMAN ASSISTANCE

---

# 35. CHANNEL INDEPENDENCE

The core Concierge must remain independent from the communication channel.

Possible channels include:

- WhatsApp
- Website chat
- Website booking assistant
- Social messaging
- Email
- Staff interface
- Reseller portal
- Agency portal
- Future channels

Channel adapters control message delivery.

They do not redefine Perico business logic.

---

# 36. CHANNEL SESSION CONTINUITY

When technically possible, customer context should survive movement between authorized Perico channels.

Example:

Website inquiry
→ WhatsApp continuation
→ Payment
→ Confirmation

The customer should not have to restart merely because the communication channel changed.

---

# 37. INTEGRATION REGISTRY

External integrations should eventually be registered in a centralized Integration Registry.

Each integration should define:

integration_id

provider

integration_type

status

supported_capabilities

supported_products

supported_channels

authentication_reference

availability_support

booking_support

payment_support

refund_support

webhook_support

last_verified

The registry must not expose credentials to customers.

---

# 38. INTEGRATION TYPES

Supported integration categories may include:

CHANNEL

BOOKING

INVENTORY

PAYMENT

CRM

PARTNER

RESELLER

MESSAGING

ANALYTICS

ACCOUNTING

NOTIFICATION

IDENTITY

OTHER

One provider may support multiple integration types.

---

# 39. INTEGRATION FAILURE PRINCIPLE

A technical integration failure describes the system connection.

It does not describe the underlying business reality.

Therefore:

API ERROR ≠ SOLD OUT

TIMEOUT ≠ UNAVAILABLE

PAYMENT API ERROR ≠ PAYMENT DECLINED

BOOKING API ERROR ≠ RESERVATION CANCELLED

WEBHOOK FAILURE ≠ PAYMENT NOT RECEIVED

Use another authorized verification path or Human Assistance.

---

# 40. DUPLICATE TRANSACTION PROTECTION

Before creating a reservation or payment transaction, the Orchestrator should check for an existing matching transaction when technically possible.

Potential duplicate indicators:

- Customer
- Product
- Date
- Time
- Participant configuration
- Existing booking ID
- Existing payment ID
- Recent transaction attempt

Do not create duplicate reservations or duplicate payment requests unnecessarily.

---

# 41. IDEMPOTENCY

External booking and payment actions should use idempotency protection whenever supported.

Repeated webhook delivery, retry or network timeout must not automatically create:

- Duplicate booking
- Duplicate charge
- Duplicate voucher
- Duplicate cancellation
- Duplicate refund

---

# 42. EVENT-DRIVEN UPDATES

Where supported, external systems may update the Concierge through events or webhooks.

Examples:

AVAILABILITY_CHANGED

BOOKING_CREATED

BOOKING_UPDATED

BOOKING_CANCELLED

PAYMENT_SUBMITTED

PAYMENT_VERIFIED

PAYMENT_FAILED

REFUND_PROCESSED

PICKUP_UPDATED

VOUCHER_READY

The Orchestrator must validate the source and map the event into canonical Perico states.

---

# 43. CANONICAL IDENTIFIERS

Where technically possible, maintain Perico-controlled identifiers independent of external provider identifiers.

Examples:

perico_customer_id

perico_product_id

perico_quote_id

perico_booking_id

perico_payment_id

perico_partner_id

perico_agent_id

External identifiers should be stored as mappings.

This prevents Perico from becoming structurally dependent on one external provider.

---

# 44. PLATFORM MAPPING

A Perico product may have different identifiers across external platforms.

Example conceptual mapping:

PERICO PRODUCT
→ Bókun product ID
→ Peek Pro product ID
→ Rezgo product ID
→ Supplier system ID
→ Reseller system ID

These external IDs refer to the same Perico-controlled product only when explicitly mapped.

Never infer mappings from similar product names.

---

# 45. PARTNER-SPECIFIC PRODUCT ACCESS

Not every partner must automatically have access to every Perico product.

Partner permissions may define:

- Allowed products
- Restricted products
- Markets
- Pricing plans
- Commission plans
- Booking permissions
- Payment terms
- Cancellation terms when contractually applicable

If access cannot be established:

PARTNER PERMISSION REQUIRED

Do not expose confidential commercial information.

---

# 46. COMMISSION SEPARATION

Commission is separate from customer price unless an approved commercial model explicitly links them.

The Concierge must distinguish:

CUSTOMER SELLING PRICE

PARTNER NET RATE

PARTNER COMMISSION

SUPPLIER COST

PERICO MARGIN

These values must never be casually substituted for one another.

Customer-facing agents must not expose protected internal economics.

---

# 47. DISCOUNTS AND PROMOTIONS

No reseller, virtual agent, booking platform or payment integration may create an unauthorized discount.

Supplier direct-customer promotions do not automatically apply to Perico.

Any Perico promotion must be explicitly approved and represented in authorized Perico data.

---

# 48. CROSS-PLATFORM CONSISTENCY

The same Perico product should preserve the same core identity across channels.

Channel presentation may differ.

Business truth must not.

The system must avoid situations where:

WhatsApp says one price,
the website says another,
a virtual reseller invents another,
and a booking platform applies an unrelated supplier promotion.

Differences are allowed only when supported by an explicit authorized pricing or commercial rule.

---

# 49. CUSTOMER OWNERSHIP

The Perico customer journey remains inside the Perico sales and service ecosystem.

External providers perform authorized functions for Perico.

They do not become the customer's required destination unless Perico explicitly authorizes a Perico-controlled customer flow.

---

# 50. CUSTOMER RESPONSE GENERATION

Before sending a customer-facing response, validate:

1. Correct customer language.
2. Correct actor permissions.
3. Correct product.
4. Correct approved price if quoted.
5. Correct availability status.
6. Correct booking status.
7. Correct payment status.
8. Correct confirmation status.
9. No protected internal data.
10. No unauthorized external website.
11. No invented fact.
12. No false scarcity.
13. No false confirmation.

Only then generate the customer response.

---

# 51. STANDARD DECISION LOOP

For every meaningful customer action:

UNDERSTAND
→ IDENTIFY CONTEXT
→ CHECK AUTHORITY
→ SELECT ENGINE
→ RETRIEVE DATA
→ VALIDATE
→ EXECUTE AUTHORIZED ACTION
→ UPDATE STATE
→ RESPOND

If validation fails:

DO NOT GUESS
→ HUMAN HANDOFF WHEN REQUIRED

---

# 52. ORCHESTRATOR DOES NOT INVENT

The Orchestrator must never independently invent:

- Product
- Price
- Discount
- Commission
- Availability
- Pickup time
- Capacity
- Payment requirement
- Payment fee
- Cancellation rule
- Refund result
- Booking status
- Confirmation number
- Supplier commitment
- Partner permission

It routes authoritative information.

It does not manufacture it.

---

# 53. FUTURE EXPANSION

The architecture must support adding new:

- Communication channels
- Booking platforms
- Payment providers
- Suppliers
- Resellers
- Travel agencies
- Virtual agents
- CRMs
- Accounting systems
- Analytics platforms
- Countries
- Languages

without rewriting the core Perico business logic.

New systems should connect through adapters and mappings.

---

# 54. NON-NEGOTIABLE ARCHITECTURE RULE

The Perico AI Concierge must remain:

CHANNEL INDEPENDENT

BOOKING-PLATFORM INDEPENDENT

PAYMENT-PROVIDER INDEPENDENT

RESELLER CAPABLE

MULTILINGUAL

PERMISSION AWARE

HUMAN ESCALATION CAPABLE

PERICO CONTROLLED

External systems execute authorized functions.

Perico controls the business logic.

---

# 55. CORE ORCHESTRATION PRINCIPLE

ONE BUSINESS BRAIN.

MANY SALES CHANNELS.

MANY RESELLERS.

MANY VIRTUAL AGENTS.

MANY BOOKING SYSTEMS.

MANY PAYMENT METHODS.

ONE CONTROLLED PERICO CUSTOMER JOURNEY.