# PERICO AI PLATFORM — BRAND & COMMERCIAL POLICY LAYER

## 1. PURPOSE

The Brand & Commercial Policy Layer allows the Perico AI platform to operate multiple independent customer-facing brands from one centralized business architecture.

Each brand may have its own:

- Name
- Positioning
- Visual identity
- Website
- Domain
- WhatsApp account
- Social channels
- Email addresses
- Customer-facing tone
- Product selection
- Retail pricing strategy
- Approved promotions
- Inclusions
- Commercial terms
- Customer segments
- Virtual sales agents
- Booking presentation
- Payment presentation

while sharing approved backend infrastructure where appropriate.

CORE PRINCIPLE:

MULTIPLE CUSTOMER-FACING BRANDS.

ONE CONTROLLED BUSINESS PLATFORM.

---

# 2. ARCHITECTURAL POSITION

Canonical transaction flow becomes:

BRAND CONTEXT
→ CHANNEL
→ ACTOR / IDENTITY
→ VIRTUAL AGENT
→ ORCHESTRATOR
→ PRODUCT
→ BRAND COMMERCIAL POLICY
→ QUOTE
→ AVAILABILITY
→ BOOKING
→ PAYMENT
→ OPERATIONAL ACCEPTANCE
→ CONFIRMATION

Every transaction should establish brand context as early as possible.

---

# 3. BRAND ID

Every configured brand must have a unique:

brand_id

Example:

PERICO

VALUE_BRAND

PRIVATE_BRAND

Actual IDs must be explicitly configured.

Do not invent a brand identity during a customer transaction.

---

# 4. BRAND PROFILE

Each brand may define:

brand_id

legal_entity_id

brand_name

status

positioning

customer_segment

primary_market

supported_languages

website

approved_domains

customer_service_channels

sales_channels

authorized_products

commercial_policy_id

pricing_profile_id

payment_profile_id

cancellation_profile_id

virtual_agent_profile

branding_profile

contact_profile

booking_profile

created_at

updated_at

Not every field must exist initially.

---

# 5. BRAND STATUS

Possible states:

PLANNED

CONFIGURING

TESTING

ACTIVE

PAUSED

SUSPENDED

RETIRED

Only ACTIVE brands may normally accept new customer transactions.

---

# 6. BRAND VS LEGAL ENTITY

A brand is not automatically a separate legal entity.

Possible architecture:

ONE LEGAL ENTITY
→ MULTIPLE BRANDS

or eventually:

MULTIPLE LEGAL ENTITIES
→ MULTIPLE BRANDS

The system must not infer legal ownership, merchant identity, tax treatment or contractual identity from brand name alone.

These must be explicitly configured.

---

# 7. BRAND CONTEXT IS MANDATORY

Before customer-facing commercial execution, the system should know the applicable:

brand_id

This is particularly important before:

- Quote
- Promotion
- Booking
- Payment
- Voucher
- Confirmation
- Customer support

If brand context cannot be established safely:

DO NOT GUESS.

Resolve context or use Human Assistance.

---

# 8. BRAND RESOLUTION

Brand may be resolved from approved information such as:

- Website/domain
- WhatsApp business account
- Social account
- Email address
- Partner portal
- Campaign
- Authorized reseller configuration
- Staff-selected brand
- Existing transaction
- Existing verified conversation context

Do not determine brand merely from customer preference when the channel belongs to another brand.

---

# 9. BRAND PERSISTENCE

Once a transaction is created, preserve:

brand_id

through:

lead

quote

availability request

booking

payment

voucher

confirmation

refund

support

reporting

Do not silently switch brands during a transaction.

---

# 10. BRAND VS CHANNEL

Never confuse:

brand_id

with:

channel_id.

Example:

brand_id = PERICO

channel = WHATSAPP

Another brand may also use WhatsApp through a different business account.

The channel type alone does not identify the brand.

---

# 11. BRAND VS VIRTUAL AGENT

Virtual agents operate on behalf of an authorized brand.

Possible fields:

agent_id

brand_id

An agent may be:

SINGLE_BRAND

or, if explicitly authorized:

MULTI_BRAND

Customer-facing behavior must always use the active transaction's brand context.

---

# 12. BRAND VS PARTNER

A B2B partner may potentially sell:

- One brand
- Multiple brands
- Selected products from selected brands

Partner authorization does not automatically grant access to every brand.

---

# 13. BRAND VS SUPPLIER

Multiple brands may sell products fulfilled by the same supplier.

Supplier identity and customer-facing brand identity remain separate.

Example:

SUPPLIER PRODUCT
→ BRAND A OFFER
→ BRAND B OFFER

The customer should receive the correct brand experience.

Supplier access information remains protected.

---

# 14. SHARED PRODUCT FOUNDATION

Multiple brands may reference the same operational product master.

Do not duplicate supplier/operational truth unnecessarily.

Conceptually:

CANONICAL PRODUCT
→ BRAND OFFER A
→ BRAND OFFER B
→ BRAND OFFER C

The canonical product may define:

- Supplier
- Operational itinerary
- Capacity
- Safety
- Schedule
- Operational restrictions

Brand offers may define approved commercial differences.

---

# 15. BRAND OFFER

A Brand Offer represents a brand-specific commercial version of a canonical product.

Possible fields:

brand_offer_id

brand_id

product_id

status

customer_facing_name

customer_facing_description

pricing_profile

approved_price

inclusions_override

exclusions_override

commercial_terms

promotion_profile

cancellation_profile

payment_profile

sales_priority

authorized_channels

authorized_markets

Important:

An override may not contradict operational reality.

---

# 16. OPERATIONAL TRUTH VS COMMERCIAL PRESENTATION

Separate:

OPERATIONAL PRODUCT TRUTH

from:

BRAND COMMERCIAL PRESENTATION.

Operational truth includes facts such as:

- Boat capacity
- Departure schedule
- Physical itinerary
- Safety requirements
- Supplier restrictions

Brand commercial presentation may include:

- Customer-facing product name
- Retail price
- Approved inclusions
- Approved extras
- Positioning
- Promotion
- Sales copy

Branding must never rewrite physical reality.

---

# 17. BRAND PRICING

Different brands may have different approved selling prices for the same underlying product.

Example:

CANONICAL PRODUCT X

Brand A:
approved retail price A

Brand B:
approved retail price B

Brand C:
approved retail price C

The Quote Engine must use the pricing authority associated with the active:

brand_id

and applicable commercial context.

---

# 18. NO AUTOMATIC PRICE COPYING

A price change for one brand must not automatically change another brand unless the pricing rule explicitly links them.

Each brand offer requires an approved pricing relationship.

---

# 19. SHARED PRICE RULE

Perico may explicitly configure brands to inherit a common pricing rule.

Possible concept:

pricing_source = CANONICAL_RETAIL

or:

pricing_source = BRAND_SPECIFIC

or:

pricing_source = ACCOUNT_SPECIFIC

Never assume inheritance.

---

# 20. VALUE BRAND

A lower-priced brand may legitimately use a different approved pricing strategy.

Possible strategy:

LOWER_MARGIN

SIMPLIFIED_SERVICE

LIMITED_INCLUSIONS

HIGH_AUTOMATION

VOLUME_FOCUSED

VALUE_POSITIONING

The lower price must come from an approved commercial policy.

The AI may not independently reduce prices to make the brand cheaper.

---

# 21. PREMIUM BRAND

A premium brand may use:

- Higher-touch service
- Additional inclusions
- Private options
- Premium support
- Different approved retail pricing
- Specialized agents

Premium positioning must not create unsupported product claims.

---

# 22. BRAND DIFFERENTIATION

Each brand should have a meaningful commercial position.

Possible differentiation:

- Price
- Service level
- Customer segment
- Product specialization
- Private experiences
- Language/market
- B2B distribution
- Group travel
- Luxury
- Fast automated booking

Do not create artificial factual differences in the underlying experience.

---

# 23. BRAND INCLUSIONS

A brand may include additional approved benefits around a canonical product.

Example:

Brand A:
standard excursion

Brand B:
same excursion + approved private transfer

This must be modeled explicitly.

Do not claim the supplier provides an inclusion that is actually provided separately by Perico.

---

# 24. BRAND EXCLUSIONS

A lower-cost brand may offer fewer commercial extras when operationally and contractually permitted.

The system must clearly preserve what the customer actually receives.

Never remove mandatory safety or legally required components merely to reduce price.

---

# 25. BRAND PRODUCT ACCESS

Each brand may have:

ALL_AUTHORIZED_PRODUCTS

or:

SELECTED_PRODUCTS

Possible reasons for restricted catalog:

- Positioning
- Margin
- Market
- Operational complexity
- Supplier agreement
- Brand strategy

A product existing in Perico's master catalog does not automatically mean every brand sells it.

---

# 26. BRAND-SPECIFIC PRODUCT STATUS

Possible states:

ACTIVE

PAUSED

SEASONAL

INTERNAL_ONLY

DISABLED

RETIRED

Canonical product may remain active while one brand's offer is disabled.

---

# 27. BRAND COMMERCIAL POLICY

Each brand may define a commercial policy containing:

pricing_strategy

discount_authority

promotion_rules

deposit_rules

payment_options

cancellation_policy

refund_policy

service_level

customer_support_model

cross_sell_rules

upsell_rules

partner_rules

Any brand-specific rule must be explicit.

---

# 28. POLICY PRECEDENCE

Commercial policy precedence should be explicit.

Recommended order:

PRODUCT-SPECIFIC APPROVED RULE
→ BRAND + ACCOUNT-SPECIFIC APPROVED RULE
→ BRAND-SPECIFIC APPROVED RULE
→ APPROVED PARTNER/ACCOUNT RULE
→ APPROVED PLATFORM GLOBAL RULE
→ HUMAN ASSISTANCE

More specific approved rules override more general rules.

No engine may invent missing policy.

---

# 29. PRICING CONTEXT

Quote requests should eventually carry:

brand_id

actor_type

customer_id

partner_id

product_id

brand_offer_id

pricing_profile

currency

participant_configuration

applicable_promotion

This prevents cross-brand price contamination.

---

# 30. BRAND PRICE ISOLATION

Never expose another brand's price merely because it is lower or higher.

If customer contacts Brand A:

Use Brand A's approved offer.

Do not say:

"Our other brand sells this cheaper."

unless Perico explicitly creates such a cross-brand sales policy.

---

# 31. BRAND PROMOTIONS

Promotions must belong to an explicit scope.

Possible fields:

promotion_id

brand_id

product_ids

eligible_channels

eligible_markets

start_at

end_at

discount_type

discount_value

eligibility

status

Do not apply a promotion from Brand A to Brand B.

---

# 32. SUPPLIER PROMOTIONS

Supplier direct-customer promotions remain separate from Perico brand promotions.

A supplier promotion does not automatically apply to any Perico-controlled brand.

Never redirect customers to supplier websites to obtain supplier promotions.

---

# 33. CROSS-BRAND PROMOTIONS

A promotion may apply to multiple brands only when explicitly configured.

Do not infer shared eligibility.

---

# 34. BRAND DISCOUNT AUTHORITY

Each brand may define:

discount_permission

maximum_discount

authorized_roles

eligible_products

approval_requirement

If no discount authority exists:

NO DISCOUNT.

Virtual agents may not negotiate beyond approved limits.

---

# 35. BRAND CANCELLATION POLICY

Different customer-facing brand offers may have different cancellation policies only when operationally, contractually and commercially permitted.

Policy hierarchy must remain explicit.

Never promise a refund that Perico cannot honor operationally.

---

# 36. BRAND PAYMENT POLICY

A brand may have different approved customer payment arrangements.

Examples:

Brand A:
full payment or approved deposit

Brand B:
full prepayment

B2B Brand:
approved commercial deposit

The Payment & Confirmation Engine determines the requirement.

The Payment Router determines the approved collection method.

---

# 37. PAYMENT PROVIDERS

Multiple brands may use:

- Same payment provider
- Different payment providers
- Different merchant accounts
- Different payment methods

Provider configuration must explicitly identify brand authorization.

---

# 38. PAYMENT DESTINATION

Customer payment must always go to the approved destination for the active:

brand_id

transaction

payment method

provider

Never send a Brand B customer a Brand A payment destination unless explicitly configured and legally/commercially appropriate.

---

# 39. PAYMENT BRANDING

Where supported, payment presentation should match the active brand.

The customer should not unexpectedly encounter unrelated brand identity during checkout unless required by the legal merchant arrangement.

Legal merchant identity must not be misrepresented.

---

# 40. BOOKING PLATFORM

Different brands may use:

- Same booking platform
- Different booking platforms
- Multiple booking platforms

Examples may include:

Bókun

Peek Pro

Rezgo

future approved systems

Booking platform does not define the brand.

---

# 41. BRAND-TO-BOOKING MAPPING

Possible mapping:

brand_id

brand_offer_id

product_id

booking_integration_id

external_product_id

external_option_id

The Integration Registry should eventually maintain these relationships.

---

# 42. SHARED INVENTORY

Multiple brands may sell from shared underlying inventory.

This creates overselling risk.

Availability must reflect the authoritative inventory source.

Do not create separate imaginary inventory simply because products appear under different brands.

---

# 43. INVENTORY CONCURRENCY

When Brand A and Brand B sell the same limited inventory:

availability and reservation operations must coordinate through the authoritative inventory system.

Brand separation must not cause duplicate capacity.

---

# 44. BRAND BOOKING

Every booking should preserve:

brand_id

brand_offer_id when applicable

product_id

customer_id

partner_id when applicable

agent_id

channel

sales_source

booking_platform

This allows correct operations and reporting.

---

# 45. BRAND CONFIRMATION

Customer confirmation should use the correct:

- Brand name
- Customer service contact
- Product name
- Booking reference
- Payment information
- Voucher presentation

Do not leak another brand into the confirmation.

---

# 46. BRAND CUSTOMER SERVICE

Support should identify the booking's original brand.

If centralized Perico staff serves multiple brands internally:

Customer-facing communication should still use the appropriate active brand identity.

---

# 47. CROSS-BRAND CUSTOMER

The same person may legitimately be a customer of multiple brands.

Do not assume:

same customer = same commercial terms.

Customer identity may be shared internally when permitted.

Brand transactions remain separate.

---

# 48. CUSTOMER RECORD

A canonical customer may have:

customer_id

with relationships to:

Brand A transactions

Brand B transactions

Brand C transactions

Access must follow privacy and permission rules.

---

# 49. CROSS-BRAND DATA PRIVACY

Do not expose to a customer:

- Their activity with another brand
- Another brand's quote
- Another brand's booking

unless the workflow explicitly requires it and the identity/permission rules permit it.

---

# 50. CROSS-BRAND RECOGNITION

Internal systems may recognize the same verified customer across brands when permitted.

Customer-facing behavior should not unexpectedly reveal cross-brand ownership or history.

---

# 51. BRAND INDEPENDENCE

A brand may appear operationally independent to the customer while using shared backend infrastructure.

The system must preserve:

- Correct branding
- Correct commercial terms
- Correct customer communication
- Correct payment presentation
- Correct support identity

Do not make false statements about legal ownership or corporate independence.

---

# 52. BRAND CONTACT INFORMATION

Each brand may define its own approved:

phone

WhatsApp

email

website

social accounts

support channel

Customer communication must use the correct brand contact profile.

---

# 53. EXTERNAL WEBSITE PROTECTION

The existing no-external-product-website rule applies across all brands.

Do not redirect customers to:

- Suppliers
- Supplier booking pages
- Supplier payment pages
- OTAs
- Competitors
- Unauthorized marketplaces

The customer remains inside the active brand's approved sales environment.

---

# 54. CROSS-BRAND REDIRECTION

Do not automatically redirect customers between Perico-controlled brands.

If Perico later authorizes cross-brand referral:

It must be explicit.

Possible fields:

cross_brand_referral_allowed

eligible_brands

eligible_products

disclosure_rule

attribution_rule

Until configured:

NO AUTOMATIC CROSS-BRAND REDIRECTION.

---

# 55. BRAND CHANNELS

Each channel instance should map to a brand when appropriate.

Example:

WhatsApp Account A
→ Brand A

WhatsApp Account B
→ Brand B

Instagram Account A
→ Brand A

Website Domain B
→ Brand B

Channel Layer remains transport.

Brand Layer controls commercial identity.

---

# 56. BRAND DOMAIN

Each customer-facing domain should have an explicit brand mapping.

Never infer that all domains belong to Perico's primary brand.

---

# 57. BRAND EMAIL

Incoming email address may help establish brand context.

Example:

sales@brand-a...

bookings@brand-b...

Exact addresses must be configured.

Do not invent them.

---

# 58. BRAND SOCIAL ACCOUNTS

Social accounts should map to:

brand_id

channel_id

integration_id

A customer entering through one brand's social account should remain in that brand context unless an approved workflow changes it.

---

# 59. VIRTUAL AGENT BRAND ASSIGNMENT

Every active Virtual Reseller Agent must know which brand it represents for a customer-facing conversation.

Possible configuration:

agent_id

allowed_brand_ids

default_brand_id

If an agent supports multiple brands:

active brand must be transaction-specific.

---

# 60. NO BRAND PERSONALITY LEAKAGE

A virtual agent representing a value brand must not accidentally use:

- Perico branding
- Perico slogan
- Perico email
- Perico website
- Perico-specific commercial promise

unless those elements are explicitly shared.

Likewise, Perico should not accidentally use another brand's identity.

---

# 61. BRAND LANGUAGE

Brands may support different language sets.

Language Engine remains responsible for translation and multilingual behavior.

Brand configuration determines whether a language is officially supported for that brand.

---

# 62. BRAND SALES STYLE

Each brand may define a customer-facing style.

Examples:

PREMIUM_HUMANIZED

FAST_VALUE

LUXURY_CONCIERGE

ADVENTURE_YOUTH

B2B_PROFESSIONAL

Style changes communication.

It does not change facts.

---

# 63. BRAND CLAIMS

Marketing claims must be approved for the applicable brand.

Do not automatically transfer:

- Review counts
- Years in business
- Awards
- Ratings
- Testimonials
- Certifications
- Reputation claims

from one brand to another.

---

# 64. REVIEWS

Reviews belonging to one brand should not automatically be presented as reviews of another brand.

Shared operational experience does not make brand-specific reviews interchangeable.

---

# 65. BRAND SEO

Each brand should maintain distinct:

- Search positioning
- Content
- Brand voice
- Landing pages
- Value proposition

Avoid unnecessary duplication of customer-facing website content across brands.

The backend product truth may be shared.

Public marketing content should be intentionally differentiated.

---

# 66. BRAND CONTENT

Brand-specific website content may reference canonical product facts.

However:

Marketing copy should be stored separately from operational product truth where practical.

This prevents SEO/branding changes from modifying booking logic.

---

# 67. BRAND CATALOG

A brand catalog is a filtered commercial view of the master product inventory.

Conceptually:

MASTER PRODUCT CATALOG
→ BRAND FILTER
→ BRAND OFFER
→ CUSTOMER CATALOG

Do not create a completely independent operational catalog for every brand unless genuinely necessary.

---

# 68. BRAND PRODUCT NAME

The same canonical product may have different customer-facing names across brands.

Preserve:

product_id

as the stable operational identity.

Use:

brand_offer_id

for brand-specific commercial identity.

---

# 69. BRAND REPORTING

Reporting should support:

brand_id

channel

agent_id

partner_id

product_id

brand_offer_id

booking_platform

payment_provider

sales_source

revenue

refunds

cancellations

This allows Perico to evaluate each brand independently.

---

# 70. BRAND PROFITABILITY

Future internal analytics may compare:

- Revenue
- Gross margin
- Acquisition cost
- Conversion
- Refund rate
- Support cost
- Channel performance

These are internal.

Do not expose cross-brand financial information to customers or unauthorized partners.

---

# 71. BRAND ATTRIBUTION

Every lead and sale should preserve original brand attribution when possible.

Possible fields:

origin_brand_id

current_brand_id

If cross-brand transfer is ever permitted, preserve both.

---

# 72. BRAND CAMPAIGN ATTRIBUTION

Campaigns should identify:

brand_id

campaign_id

channel

source

medium

agent_id

This prevents marketing performance from being mixed across brands.

---

# 73. PARTNER + BRAND AUTHORIZATION

Partner permissions may include:

partner_id

authorized_brand_ids

authorized_product_ids

commercial_profile

A partner approved for Brand A is not automatically approved for Brand B.

---

# 74. B2B BRANDING

Perico may eventually operate:

consumer brands

and:

B2B/distribution brands.

The Partner & Reseller Engine remains responsible for commercial partner relationships.

The Brand Layer determines which brand relationship applies.

---

# 75. WHITE LABEL

A future partner may require white-label presentation.

White label must be modeled explicitly.

Do not treat every reseller as a separate brand.

Possible distinction:

PERICO-OWNED BRAND

PARTNER BRAND

WHITE-LABEL PRESENTATION

RESELLER IDENTITY

These are different concepts.

---

# 76. BRAND OPERATIONS

Multiple brands may share:

- Staff
- Vehicles
- Suppliers
- Guides
- Booking platforms
- Payment infrastructure
- Customer support systems

Shared operations must not cause customer-facing brand contamination.

---

# 77. OPERATIONAL NOTES

Internal operational staff should be able to see the brand associated with a booking.

This helps ensure:

- Correct signage
- Correct voucher
- Correct customer greeting
- Correct contact details
- Correct service expectations

---

# 78. BRAND-SPECIFIC SERVICE LEVEL

A brand may define service-level differences when operationally approved.

Examples:

STANDARD

VALUE

PREMIUM

PRIVATE_CONCIERGE

The system must know exactly what each service level means.

Do not infer service reductions merely from lower price.

---

# 79. BRAND-SPECIFIC ADD-ONS

Add-ons may differ by brand.

Possible examples:

Professional photos

Private transportation

Premium beverages

Celebration setup

Exact availability and pricing must be approved.

---

# 80. CROSS-SELL WITHIN BRAND

Default cross-sell should remain inside the active brand.

Example:

Brand B Saona customer
→ Brand B airport transfer

Do not silently cross-sell Brand A.

---

# 81. UPSELL WITHIN BRAND

Upsell should normally use products available within the active brand.

If a premium option does not exist within that brand:

Do not automatically move the customer to another brand.

---

# 82. BRAND AVAILABILITY

Brand offer availability depends on:

CANONICAL PRODUCT AVAILABILITY

plus:

BRAND OFFER STATUS

plus:

BRAND-SPECIFIC RESTRICTIONS

A canonical product may be available operationally but unavailable for sale through a particular brand.

---

# 83. BRAND-SPECIFIC CAPACITY

Do not create artificial capacity per brand unless the inventory arrangement explicitly allocates capacity.

Shared capacity must remain shared.

---

# 84. BRAND HUMAN HANDOFF

Human Handoff must preserve:

brand_id

Customer-facing human support should continue under the correct brand identity.

Do not force the customer to restart.

---

# 85. BRAND COMPLAINTS

Complaint records should preserve:

brand_id

booking_id

product_id

customer_id

agent_id

channel

This allows accurate service recovery and reporting.

---

# 86. BRAND REFUNDS

Refunds must remain associated with:

original brand

original booking

original payment transaction

applicable cancellation/refund policy

Do not move a refund to another brand merely because payment infrastructure is shared.

---

# 87. BRAND SECURITY

Brand separation must not weaken:

- Identity verification
- Customer privacy
- Partner privacy
- Payment security
- Staff permissions

A staff user with access to Brand A does not automatically require access to Brand B.

---

# 88. BRAND PERMISSIONS

Identity & Permissions should eventually support:

allowed_brand_ids

for:

staff

partners

virtual agents

integrations

API clients

---

# 89. INTEGRATION BRAND SCOPE

Integration Registry should eventually support:

allowed_brand_ids

An integration may serve:

ONE BRAND

MULTIPLE BRANDS

ALL AUTHORIZED BRANDS

This must be explicit.

---

# 90. PROVIDER LOCK-IN PROTECTION

No brand should become architecturally dependent on one:

- Messaging provider
- Booking system
- Payment processor
- CRM
- Reseller platform

Brand logic remains above the adapter layer.

---

# 91. NEW BRAND CREATION

Future brand onboarding should follow:

DEFINE BRAND
→ DEFINE POSITIONING
→ DEFINE LEGAL / COMMERCIAL IDENTITY
→ DEFINE CUSTOMER SEGMENT
→ DEFINE CATALOG
→ DEFINE BRAND OFFERS
→ DEFINE PRICING
→ DEFINE POLICIES
→ DEFINE CHANNELS
→ DEFINE VIRTUAL AGENTS
→ DEFINE BOOKING MAPPINGS
→ DEFINE PAYMENT MAPPINGS
→ DEFINE SUPPORT
→ TEST
→ APPROVE
→ ACTIVATE

---

# 92. BRAND TESTING

Before activation, test:

- Brand resolution
- Product catalog
- Product names
- Prices
- Promotions
- Availability
- Booking
- Payment
- Cancellation
- Refund
- Confirmation
- Customer support
- Language
- Channel mapping
- Virtual agents
- Partner permissions
- Brand isolation
- External website protection
- Shared inventory
- Human handoff

---

# 93. BRAND ISOLATION TEST

Before launch, explicitly test that Brand A cannot accidentally expose:

- Brand B prices
- Brand B promotions
- Brand B contact information
- Brand B payment destination
- Brand B customer records
- Brand B partner terms
- Brand B internal configuration

Repeat in both directions.

---

# 94. BRAND TRANSACTION VALIDATION

Before customer-facing transactional action, verify:

1. brand_id established.
2. Brand is active.
3. Channel authorized for brand.
4. Agent authorized for brand.
5. Actor/partner authorized when required.
6. Product authorized for brand.
7. Brand offer active.
8. Correct brand pricing used.
9. Correct promotion used.
10. Correct availability state.
11. Correct booking mapping.
12. Correct payment rule.
13. Correct payment destination.
14. Correct customer-facing identity.
15. Correct cancellation/refund rule.
16. No other brand's protected data exposed.
17. No supplier sales destination exposed.
18. Transaction retains brand attribution.

If any critical element cannot be established:

DO NOT GUESS.

Use the appropriate engine or Human Assistance.

---

# 95. NON-NEGOTIABLE RULE

NEVER CONFUSE:

BRAND
WITH
LEGAL ENTITY.

NEVER CONFUSE:

BRAND
WITH
SUPPLIER.

NEVER CONFUSE:

BRAND
WITH
CHANNEL.

NEVER CONFUSE:

BRAND
WITH
VIRTUAL AGENT.

NEVER CONFUSE:

BRAND
WITH
BOOKING PLATFORM.

NEVER CONFUSE:

BRAND
WITH
PAYMENT PROVIDER.

NEVER ALLOW ONE BRAND'S COMMERCIAL POLICY
TO LEAK INTO ANOTHER BRAND
WITHOUT EXPLICIT AUTHORIZATION.

---

# 96. CORE PRINCIPLE

ONE CENTRAL BUSINESS PLATFORM.

ONE AUTHORITATIVE OPERATIONAL PRODUCT FOUNDATION.

MULTIPLE BRANDS.

MULTIPLE COMMERCIAL STRATEGIES.

MULTIPLE PRICE POINTS.

MULTIPLE WEBSITES.

MULTIPLE WHATSAPP ACCOUNTS.

MULTIPLE VIRTUAL SALES TEAMS.

MULTIPLE BOOKING SYSTEMS.

MULTIPLE PAYMENT PROVIDERS.

SHARED INFRASTRUCTURE WHERE APPROPRIATE.

STRICT BRAND ISOLATION WHERE REQUIRED.

THE BRANDS CAN COMPETE.

THE PLATFORM STAYS CENTRALIZED.