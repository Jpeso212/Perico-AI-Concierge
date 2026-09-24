# PERICO AI CONCIERGE — PARTNER & RESELLER ENGINE

## 1. PURPOSE

The Partner & Reseller Engine controls Perico's commercial distribution relationships.

It governs how Perico works with:

- Travel agencies
- Tour operators
- Hotels
- Hotel concierges
- Independent resellers
- Affiliates
- Corporate partners
- Destination partners
- Online partners
- B2B accounts
- Virtual reseller agents
- Future distribution partners

This engine determines the commercial relationship.

Identity and access control remain governed by:

identity-permissions-engine.md

Pricing calculations remain governed by:

quote-engine.md

Booking execution remains governed by:

booking-engine.md

Payment rules remain governed by:

payment-confirmation-engine.md

CORE PRINCIPLE:

ONE PERICO PRODUCT NETWORK.
MULTIPLE AUTHORIZED SELLERS.
CONTROLLED COMMERCIAL TERMS.
COMPLETE SALES ATTRIBUTION.

---

# 2. PARTNER IS NOT CUSTOMER

A partner and the traveler are separate entities.

Example:

ABC Travel sells a Saona excursion to Maria.

PARTNER:
ABC Travel

CUSTOMER:
Maria

The system must preserve both identities.

Do not replace customer information with agency information.

Do not treat the agency as the traveler.

---

# 3. CANONICAL PARTNER TYPES

Supported partner types may include:

TRAVEL_AGENCY

TOUR_OPERATOR

AUTHORIZED_RESELLER

HOTEL

HOTEL_CONCIERGE

AFFILIATE

CORPORATE_PARTNER

DESTINATION_PARTNER

ONLINE_RESELLER

VIRTUAL_RESELLER_NETWORK

OTHER_APPROVED_PARTNER

Partner type alone does not determine commercial terms.

Each partner may have an individual commercial profile.

---

# 4. PARTNER IDENTIFIER

Every approved partner should eventually receive a unique Perico-controlled identifier.

Example:

partner_id

External system identifiers should map to this Perico identifier.

Example:

PERICO PARTNER ID
→ CRM ACCOUNT
→ Bókun reseller ID
→ Peek Pro reseller ID
→ Rezgo reseller ID
→ payment/accounting mapping

Never use company name alone as the permanent system identifier.

---

# 5. PARTNER PROFILE

A partner profile may contain:

partner_id

partner_type

legal_name

trade_name

status

country

market

preferred_language

authorized_contacts

authorized_channels

authorized_products

pricing_plan

commission_plan

payment_terms

booking_permissions

cancellation_terms

credit_terms

currency

contract_start

contract_end

sales_owner

special_conditions

created_at

updated_at

Do not invent missing partner information.

---

# 6. PARTNER STATUS

Canonical partner states:

PROSPECT

PENDING_VERIFICATION

PENDING_APPROVAL

ACTIVE

SUSPENDED

EXPIRED

TERMINATED

BLOCKED

Only ACTIVE partners receive normal active partner commercial privileges.

---

# 7. PROSPECT PARTNERS

A PROSPECT is not yet an approved commercial partner.

Prospects may receive authorized public or recruitment information.

They must not automatically receive:

- Confidential net rates
- Commission tables
- Account-specific pricing
- Partner booking access
- Customer records
- Other partner information

Approval is required before protected commercial access.

---

# 8. PARTNER VERIFICATION

A partner claiming an existing Perico relationship must be verified according to:

identity-permissions-engine.md

Company name alone is not sufficient.

Verification may eventually use:

- Partner account
- Authorized email
- Authorized phone
- Partner ID
- CRM record
- Contract record
- Secure portal
- Perico staff verification

---

# 9. AUTHORIZED CONTACTS

A partner may have multiple authorized contacts.

Possible fields:

contact_id

partner_id

name

role

email

phone

language

permissions

status

One employee leaving an agency must not automatically invalidate the agency itself.

Likewise, agency authorization does not automatically authorize every person claiming to work there.

---

# 10. COMMERCIAL PROFILE

Each partner may have a commercial profile.

Possible components:

PRICING_PLAN

COMMISSION_PLAN

PAYMENT_TERMS

CREDIT_TERMS

CANCELLATION_TERMS

PRODUCT_ACCESS

BOOKING_PERMISSIONS

MARKET_RESTRICTIONS

CHANNEL_RESTRICTIONS

SPECIAL_CONDITIONS

Never assume one partner's commercial agreement applies to another.

---

# 11. COMMERCIAL MODELS

Perico may support different partner commercial models.

Examples:

COMMISSION_MODEL

NET_RATE_MODEL

RETAIL_REFERRAL_MODEL

ACCOUNT_SPECIFIC_RATE

PACKAGE_RATE

CUSTOM_CONTRACT

HYBRID_MODEL

The commercial model must be explicitly established.

Do not infer it from partner type.

---

# 12. COMMISSION MODEL

Under a commission model:

CUSTOMER SELLING PRICE
→ APPROVED COMMISSION
→ PARTNER COMMISSION
→ PERICO REVENUE

Exact calculations must use approved commercial rules.

Do not invent commission percentages.

---

# 13. NET RATE MODEL

Under a net-rate model:

PERICO NET RATE
→ PARTNER RECEIVES AUTHORIZED NET PRICE

The partner's resale behavior must follow the applicable agreement.

The Concierge must not automatically expose Perico's internal supplier cost merely because a partner receives a net rate.

PARTNER NET RATE ≠ SUPPLIER COST.

---

# 14. RETAIL REFERRAL MODEL

Under a retail referral model:

Perico may control the customer selling price and attribute the sale to the referring partner.

Partner compensation follows the approved referral agreement.

The partner does not automatically receive net-rate access.

---

# 15. ACCOUNT-SPECIFIC RATE

Some partners may have negotiated pricing.

These prices apply only to the authorized account and applicable products.

Never generalize an account-specific rate into:

- Global B2B rate
- Customer retail rate
- Another agency's rate
- Supplier cost

---

# 16. HYBRID COMMERCIAL MODEL

A partner may use different commercial models for different products.

Example:

Transfers
→ NET RATE

Excursions
→ COMMISSION

Private charters
→ CUSTOM QUOTE

This is valid when explicitly approved.

Do not force one commercial model across the entire partner account.

---

# 17. PRODUCT ACCESS

A partner may have access to:

ALL_APPROVED_PRODUCTS

SELECTED_PRODUCTS

PRODUCT_CATEGORY

SPECIFIC_PRODUCTS

QUOTE_ONLY_PRODUCTS

Access must be explicitly defined when restrictions exist.

---

# 18. PRODUCT AUTHORIZATION STATES

Possible product authorization states:

AUTHORIZED

RESTRICTED

QUOTE_ONLY

BOOKING_REQUIRES_APPROVAL

NOT_AUTHORIZED

If unclear:

PARTNER PERMISSION REQUIRED
→ PERICO HUMAN ASSISTANCE

---

# 19. PARTNER PRICING CONTEXT

Before generating a partner quote, determine:

1. Verified partner identity
2. Active partner status
3. Product authorization
4. Applicable commercial model
5. Applicable pricing plan
6. Applicable commission plan
7. Applicable account-specific rules

Then send the pricing request to:

quote-engine.md

This engine does not independently calculate product prices.

---

# 20. COMMISSION PLAN

A commission plan may contain:

commission_plan_id

partner_id

product_id_or_category

commission_type

commission_value

currency_if_fixed

effective_date

expiration_date

special_conditions

Commission types may eventually include:

PERCENTAGE

FIXED_AMOUNT

PRODUCT_SPECIFIC

CUSTOM

Do not invent missing commission rules.

---

# 21. COMMISSION IS NOT CUSTOMER DISCOUNT

Partner commission belongs to the commercial relationship.

It must not automatically become a customer discount.

Example:

20% commission

does NOT mean:

20% customer discount.

Any customer discount requires separate authorization.

---

# 22. SUPPLIER COMMISSION IS INTERNAL

Supplier commission received by Perico is not automatically the same as reseller commission paid by Perico.

Never expose supplier commission to a reseller unless specifically authorized.

Never use supplier commission as the automatic reseller commission.

---

# 23. SUPPLIER PROMOTIONS

Supplier promotions, direct-booking discounts, promotional codes and flash sales do not automatically apply to Perico agency or reseller bookings.

Perico pricing follows approved Perico commercial rules.

Never redirect a partner or customer to the supplier to obtain a supplier promotion.

---

# 24. PARTNER MARKUP

Some commercial models may permit a reseller to determine its own customer markup.

This must be explicitly authorized.

If markup authority is not established:

DO NOT ASSUME IT.

Perico-controlled customer channels must continue using approved Perico selling prices.

---

# 25. PARTNER DISCOUNTS

A partner must not create a Perico-funded discount unless authorized.

Possible states:

NO_DISCOUNT_AUTHORITY

PROMOTION_ONLY

LIMITED_DISCOUNT_AUTHORITY

CUSTOM_APPROVAL_REQUIRED

Any discount authority must define its limits.

---

# 26. PARTNER PAYMENT TERMS

Partner payment rules may differ from direct-customer rules.

Possible commercial arrangements may include:

DEPOSIT_REQUIRED

FULL_PREPAYMENT

BALANCE_LATER

CREDIT_TERMS

PAY_PER_BOOKING

PERIODIC_SETTLEMENT

CUSTOM_TERMS

Only approved arrangements may be used.

---

# 27. CURRENT GENERAL B2B RESERVATION RULE

For approved Perico B2B agency reservations, the currently approved general rule is:

40% payment/deposit required to reserve/confirm the service,

unless a product-specific or account-specific approved rule overrides it.

The remaining balance does NOT automatically have to be paid in cash.

Available approved Perico payment methods may be used according to the applicable booking terms.

Applicable processing charges may apply when specifically established.

Never invent:

- Balance deadline
- Required payment method
- Processing charge
- Credit term

when not established.

---

# 28. PAYMENT RULE PRECEDENCE

For partner transactions:

PRODUCT-SPECIFIC APPROVED PAYMENT RULE
→ ACCOUNT-SPECIFIC APPROVED COMMERCIAL RULE
→ APPROVED B2B COMMERCIAL RULE
→ APPROVED PERICO GLOBAL RULE
→ PERICO HUMAN ASSISTANCE

Payment calculations and payment states remain controlled by:

payment-confirmation-engine.md

---

# 29. CREDIT TERMS

Credit terms must never be assumed.

Possible examples:

PREPAID_ONLY

NET_7

NET_15

NET_30

CUSTOM

These states may exist only when formally approved for the partner.

If no approved credit term exists:

Do not extend credit.

---

# 30. BOOKING OWNERSHIP

Every partner-generated booking should preserve both:

CUSTOMER OWNERSHIP CONTEXT

and

SALES ATTRIBUTION

Possible fields:

booking_id

customer_id

partner_id

agent_id

channel

product_id

booking_platform

created_by

sales_source

This allows Perico to know who is traveling and who generated the sale.

---

# 31. CUSTOMER RELATIONSHIP

Partner-generated customers remain travelers receiving Perico services.

Customer service must not be degraded because the booking originated through a reseller.

The system should know when communication must:

- Go directly to traveler
- Go through partner
- Go to both

according to the applicable commercial workflow.

---

# 32. CUSTOMER CONTACT PERMISSIONS

Partner agreements may define whether Perico may communicate directly with the traveler.

Possible states:

DIRECT_CONTACT_ALLOWED

PARTNER_ONLY

OPERATIONAL_CONTACT_ONLY

EMERGENCY_CONTACT_ALLOWED

CUSTOM

Do not invent a communication restriction.

---

# 33. CUSTOMER DATA PRIVACY

A partner may access customer information only when authorized and relevant to its bookings.

A partner must never receive another partner's customer records.

Customer data must not be exposed merely because two reservations use the same hotel, product or travel date.

---

# 34. PARTNER BOOKING PERMISSIONS

Possible permissions:

CAN_REQUEST_QUOTE

CAN_CHECK_AVAILABILITY

CAN_CREATE_BOOKING

CAN_MODIFY_BOOKING

CAN_CANCEL_BOOKING

CAN_VIEW_VOUCHER

CAN_VIEW_PAYMENT_STATUS

CAN_REQUEST_REFUND

CAN_VIEW_COMMISSION

CAN_VIEW_NET_RATE

CAN_MANAGE_CONTACTS

CAN_VIEW_REPORTS

Permissions must follow identity-permissions-engine.md.

---

# 35. PARTNER BOOKING FLOW

Typical partner booking flow:

VERIFY PARTNER
→ VERIFY PRODUCT ACCESS
→ IDENTIFY CUSTOMER/TRAVELER
→ COLLECT BOOKING DETAILS
→ APPLY PARTNER COMMERCIAL CONTEXT
→ QUOTE
→ CHECK AVAILABILITY
→ CREATE RESERVATION
→ APPLY PARTNER PAYMENT TERMS
→ PAYMENT / ACCOUNT SETTLEMENT
→ OPERATIONAL ACCEPTANCE
→ CONFIRMATION
→ ATTRIBUTE SALE

---

# 36. PARTNER QUOTE

A partner quote should distinguish internally:

CUSTOMER SELLING PRICE

PARTNER NET RATE

PARTNER COMMISSION

PERICO RECEIVABLE

only when the applicable commercial model requires those fields.

Do not expose unnecessary internal economics.

---

# 37. PARTNER RESERVATION STATUS

Partner-facing reservation states should map to canonical Perico booking states.

Do not create a completely separate booking truth for agencies.

Partner portal terminology may differ visually.

Underlying Perico state remains canonical.

---

# 38. VOUCHERS

A partner booking may generate:

CUSTOMER VOUCHER

PARTNER VOUCHER

INTERNAL OPERATIONS RECORD

depending on workflow.

A voucher must not expose protected internal pricing unless specifically intended for that audience.

---

# 39. WHITE-LABEL SALES

Perico may eventually support authorized white-label partners.

White-label presentation does not change:

- Product truth
- Operational requirements
- Safety rules
- Availability
- Booking requirements
- Payment obligations
- Internal Perico attribution

White-label behavior requires explicit authorization.

---

# 40. RESELLER PORTAL

A future reseller portal may allow authorized partners to:

- Browse approved products
- View authorized rates
- Check availability
- Create bookings
- View their bookings
- Retrieve vouchers
- View authorized commission
- Submit payment
- View account status
- Request modifications
- Request cancellations
- Download authorized commercial materials

Portal access must use Identity & Permissions.

---

# 41. PARTNER API

Perico may eventually provide API access to selected partners.

API access does not automatically grant access to all Perico products or data.

Each API partner must have:

partner_id

credentials

allowed_capabilities

allowed_products

rate_limit

commercial_profile

data_permissions

status

---

# 42. PARTNER API ACTIONS

Possible API capabilities:

SEARCH_PRODUCTS

GET_PRODUCT

GET_PRICE

CHECK_AVAILABILITY

CREATE_BOOKING

GET_BOOKING

MODIFY_BOOKING

CANCEL_BOOKING

GET_VOUCHER

GET_PAYMENT_STATUS

REQUEST_REFUND

GET_COMMISSION

Capabilities must be explicitly authorized.

---

# 43. PLATFORM RESELLERS

External reservation platforms may function as distribution partners.

Examples may include approved connections involving:

- Bókun
- Peek Pro
- Rezgo
- Other reseller networks
- Other booking marketplaces

Their role must be classified.

A booking platform is not automatically a reseller.

A reseller is not automatically the booking platform.

One provider may perform multiple roles.

---

# 44. EXTERNAL MARKETPLACE BOOKINGS

When Perico receives a booking through an approved external marketplace:

The marketplace may be the SALES SOURCE.

Perico still maintains its own canonical booking record or mapped booking identity when technically possible.

Preserve:

external_booking_id

external_product_id

partner_id

perico_booking_id

customer_id

payment_context

commission_context

operational_status

---

# 45. EXTERNAL PLATFORM PRICES

An external platform may contain its own configured retail price.

Do not automatically treat that platform price as the universal Perico price.

Price authority depends on the approved channel and commercial configuration.

Cross-platform price differences must be intentional and authorized.

---

# 46. BOOKING PLATFORM VS COMMERCIAL PARTNER

Always distinguish:

BOOKING PLATFORM

from:

COMMERCIAL PARTNER

Example:

An agency may sell the product.

Bókun may execute the reservation.

A payment provider may collect the payment.

These are three separate roles.

---

# 47. VIRTUAL RESELLER NETWORK

Perico may operate a network of virtual reseller agents.

Each virtual reseller should have:

agent_id

agent_profile

authorized_languages

authorized_channels

authorized_products

authorized_customer_segments

commercial_permissions

sales_attribution

supervision_rules

Virtual reseller permissions are controlled by:

identity-permissions-engine.md

---

# 48. VIRTUAL RESELLER SALES ATTRIBUTION

Every virtual reseller-generated transaction should preserve attribution when technically possible.

Possible fields:

agent_id

virtual_team_id

channel

campaign

customer_id

quote_id

booking_id

payment_id

product_id

partner_id_if_applicable

This enables performance reporting without changing customer business rules.

---

# 49. VIRTUAL RESELLER + PARTNER

A virtual reseller may operate on behalf of:

PERICO DIRECT

or

AN AUTHORIZED PARTNER

when explicitly configured.

If operating for a partner:

The virtual reseller inherits only the commercial permissions explicitly delegated to it.

It does not automatically inherit all partner account permissions.

---

# 50. VIRTUAL RESELLER COMPENSATION

Virtual reseller compensation, if used, must remain separate from:

Customer price

Partner commission

Supplier commission

Perico margin

Do not alter customer pricing merely to calculate virtual reseller performance.

---

# 51. LEAD ATTRIBUTION

The system may track leads before booking.

Possible fields:

lead_id

customer_id

partner_id

agent_id

channel

campaign

product_interest

created_at

last_activity

status

Lead attribution rules must eventually define how competing claims are handled.

Do not invent attribution ownership when unresolved.

---

# 52. SALES ATTRIBUTION

Possible sales-source categories:

PERICO_DIRECT

B2B_AGENCY

AUTHORIZED_RESELLER

HOTEL_CONCIERGE

AFFILIATE

VIRTUAL_RESELLER

WEBSITE

WHATSAPP

SOCIAL

EXTERNAL_PLATFORM

STAFF_ASSISTED

CUSTOM

Sales source and communication channel are separate.

Example:

SALES SOURCE:
B2B Agency

CHANNEL:
WhatsApp

---

# 53. ATTRIBUTION DOES NOT CHANGE BUSINESS TRUTH

Tracking who generated a sale must not change:

- Product identity
- Safety requirements
- Availability
- Capacity
- Booking requirements
- Cancellation rules

unless an authorized commercial agreement specifically changes an applicable commercial condition.

---

# 54. COMMISSION CALCULATION

Commission calculations should use explicit approved rules.

Possible basis:

SELLING_PRICE

NET_REVENUE

FIXED_AMOUNT

PRODUCT_SPECIFIC_AMOUNT

CUSTOM

The commission basis must not be guessed.

---

# 55. COMMISSION STATUS

Possible states:

NOT_APPLICABLE

PENDING

EARNED

APPROVED

PAYABLE

PAID

REVERSED

DISPUTED

Exact transition rules should eventually be defined by Perico accounting policy.

Do not promise a commission payout merely because a booking exists.

---

# 56. CANCELLATION AND COMMISSION

Cancellation may affect partner commission.

Do not invent the result.

Commission impact should follow the applicable:

- Partner agreement
- Product cancellation policy
- Payment/refund result
- Accounting rule

If unresolved:

PERICO HUMAN ASSISTANCE.

---

# 57. REFUNDS

A reseller may request a refund when authorized.

Refund request ≠ refund approval.

Refund approval and payment handling remain governed by:

payment-confirmation-engine.md

Partner commercial consequences must follow the applicable agreement.

---

# 58. CHARGEBACKS AND PAYMENT DISPUTES

Chargebacks and payment disputes require controlled handling.

Do not automatically:

- Cancel partner
- Cancel booking
- Reverse commission
- Refund customer
- Accuse customer or partner

Use the verified payment status and Perico Human Assistance when required.

---

# 59. PARTNER SUSPENSION

When a partner becomes SUSPENDED:

Do not automatically delete existing bookings.

Existing reservations must continue according to their valid operational status unless Perico determines otherwise.

New commercial privileges may be blocked.

---

# 60. PARTNER TERMINATION

TERMINATED partner status blocks future partner privileges unless Perico explicitly restores the relationship.

Historical transaction records should remain available internally for audit and operational purposes according to applicable policy.

---

# 61. CONTRACT EXPIRATION

If a partner contract expires:

Do not silently continue expired commercial terms.

Possible state:

PARTNER TERMS EXPIRED
→ PERICO HUMAN ASSISTANCE

unless a valid replacement agreement exists.

---

# 62. COMMERCIAL RULE CHANGES

When Perico changes a partner's:

- Rate
- Commission
- Payment terms
- Product access
- Booking permissions

the effective date should be preserved when technically possible.

Do not automatically apply new terms retroactively to completed transactions.

---

# 63. EXISTING BOOKING PROTECTION

Commercial rule changes should not silently rewrite already confirmed reservations.

If a confirmed booking requires modification because of a contractual or operational change:

PERICO HUMAN ASSISTANCE

unless an explicit automated rule exists.

---

# 64. PARTNER-SPECIFIC CANCELLATION TERMS

A partner may have approved cancellation terms different from Perico's general customer fallback.

Applicable hierarchy:

PRODUCT-SPECIFIC APPROVED CANCELLATION RULE
→ ACCOUNT/PARTNER-SPECIFIC APPROVED RULE
→ APPROVED B2B RULE
→ PERICO GLOBAL FALLBACK

When unresolved:

PERICO HUMAN ASSISTANCE.

---

# 65. LARGE GROUPS

Partner group bookings may require:

- Custom quote
- Custom transportation
- Supplier confirmation
- Deposit arrangement
- Payment schedule
- Group coordinator
- Multiple vehicles
- Multiple guides
- Special itinerary
- Contract

Do not force standard small-booking automation onto complex group requests.

---

# 66. COURTESY EXCURSIONS

Perico may authorize courtesy excursions for selected partners or commercial purposes.

Courtesy service must be explicitly approved.

Do not interpret:

"agency partner"

as automatically entitled to a free excursion.

Possible state:

COURTESY REQUEST
→ PERICO APPROVAL REQUIRED

---

# 67. FAMILIARIZATION TRIPS

If Perico later establishes FAM-trip programs, they should use explicit:

- Eligibility
- Product access
- Dates
- Capacity
- Costs
- Companion rules
- Booking process

Do not invent FAM benefits.

---

# 68. MARKETING MATERIAL ACCESS

Partners may receive authorized:

- Product photos
- Videos
- Descriptions
- Sales sheets
- Rate sheets
- Brand assets
- Destination information

Access to marketing material does not automatically authorize access to confidential commercial data.

---

# 69. BRAND REPRESENTATION

Partners must not be treated as Perico employees unless they actually are.

Virtual reseller agents operating directly for Perico may represent Perico according to their authorized role.

Third-party partners remain separate commercial entities.

---

# 70. CUSTOMER EXPERIENCE

Regardless of sales source, the Concierge should preserve Perico's service principles:

- Clear communication
- Accurate information
- Honest pricing
- Attention to detail
- No invented promises
- No false availability
- No false confirmation
- Human assistance when required

---

# 71. EXTERNAL WEBSITE PROTECTION

Partner and reseller workflows must obey:

global-rules.md

The Concierge must not redirect customers to supplier websites, supplier booking pages, supplier payment systems, competitors, OTAs or unauthorized external marketplaces.

Approved external systems may operate behind Perico workflows without being exposed as customer alternatives.

---

# 72. INTERNAL SUPPLIER RELATIONSHIP

A partner sells Perico-authorized inventory.

The partner does not automatically gain access to Perico's supplier relationship.

Do not expose:

- Supplier net cost
- Supplier commission
- Supplier negotiation
- Supplier contact
- Supplier payment arrangements
- Internal supplier notes

unless explicitly authorized.

---

# 73. PARTNER REPORTING

Future reporting may include:

- Leads
- Quotes
- Bookings
- Gross sales
- Cancellations
- Refunds
- Commission
- Outstanding balance
- Products sold
- Sales by market
- Sales by channel
- Sales by virtual reseller

Reporting visibility must follow permissions.

---

# 74. PARTNER SETTLEMENT

Future settlement systems may reconcile:

BOOKINGS
→ PAYMENTS
→ REFUNDS
→ COMMISSIONS
→ BALANCE
→ PAYOUT

Accounting calculations must use verified transaction data.

The Concierge must not invent financial settlement results.

---

# 75. MULTI-CURRENCY PARTNERS

If Perico later supports multiple partner currencies:

Do not perform unauthorized automatic currency conversion.

The applicable:

- Contract currency
- Selling currency
- Payment currency
- Settlement currency
- Exchange-rate source

must be explicitly established.

---

# 76. MULTILINGUAL PARTNERS

Partner communication may use any language supported by:

language-engine.md

Translation does not change commercial terms.

A Spanish agreement and an English explanation must represent the same approved business rule.

---

# 77. PARTNER HUMAN HANDOFF

Use:

human-handoff-engine.md

for situations including:

- New agency approval
- Identity conflict
- Account verification
- Missing commercial terms
- Custom commission
- Special pricing
- Credit request
- Contract issue
- Large group
- Courtesy request
- Refund dispute
- Commission dispute
- Account suspension
- Permission conflict
- Technical integration failure

Preserve the partner and booking context.

---

# 78. AUTOMATION BOUNDARY

The Partner & Reseller Engine may automate a transaction only when:

1. Partner identity is sufficiently verified.
2. Partner status permits transaction.
3. Product access is authorized.
4. Applicable commercial model is known.
5. Applicable price can be determined.
6. Applicable payment terms are known.
7. Required permissions exist.
8. Availability can be established.
9. No unresolved conflict exists.
10. Required integrations are functioning or an approved alternative exists.

Otherwise:

PERICO HUMAN ASSISTANCE.

---

# 79. FINAL PARTNER VALIDATION

Before completing a partner transaction, validate:

- Correct partner
- Correct customer
- Correct product
- Correct commercial profile
- Correct price
- Correct commission when applicable
- Correct payment terms
- Correct booking permissions
- Correct availability
- Correct reservation status
- Correct attribution
- Correct data visibility
- No protected internal information exposed
- No unauthorized external website
- No invented commercial condition

---

# 80. NON-NEGOTIABLE RULE

NEVER ASSUME:

ALL AGENCIES HAVE THE SAME RATE.

ALL RESELLERS HAVE THE SAME COMMISSION.

ALL PARTNERS HAVE THE SAME PAYMENT TERMS.

ALL PARTNERS CAN SELL EVERY PRODUCT.

ALL PARTNERS CAN MODIFY BOOKINGS.

ALL PARTNERS CAN ACCESS CUSTOMER DATA.

ALL SALES CHANNELS ARE COMMERCIAL PARTNERS.

EVERY BOOKING PLATFORM IS A RESELLER.

EVERY RESELLER IS A BOOKING PLATFORM.

---

# 81. CORE PRINCIPLE

ONE PERICO DISTRIBUTION NETWORK.

INDIVIDUAL PARTNER AGREEMENTS.

CONTROLLED PRODUCT ACCESS.

CONTROLLED COMMERCIAL TERMS.

CONTROLLED DATA ACCESS.

COMPLETE SALES ATTRIBUTION.

NO INVENTED PRIVILEGES.