# PERICO AI PLATFORM — POLICY AUTHORITY MATRIX

## 1. PURPOSE

This file defines how the Perico AI Platform resolves competing or overlapping business policies.

It exists to prevent different engines, brands, partners, accounts, products, agents or integrations from independently deciding which rule wins.

CORE PRINCIPLE:

MORE SPECIFIC APPROVED POLICY
OVERRIDES
MORE GENERAL APPROVED POLICY

ONLY WITHIN ITS AUTHORIZED SCOPE.

No policy may override Global Rules unless an explicitly authorized Global Rule permits that exception.

---

# 2. HIGHEST AUTHORITY

The highest platform authority is:

global-rules.md

Global Rules apply across:

- Brands
- Products
- Customers
- Partners
- Resellers
- Virtual agents
- Channels
- Booking platforms
- Payment providers
- Integrations

Lower-level policies must remain compatible with Global Rules.

---

# 3. OPERATIONAL TRUTH

Canonical product and transfer masters remain authoritative for operational facts.

Examples:

- Actual itinerary
- Capacity
- Safety requirements
- Supplier identity
- Operational restrictions
- Vehicle rules
- Product configuration
- Approved fixed route prices where defined directly in the master

A brand policy may change commercial presentation.

It may not rewrite physical or operational reality.

---

# 4. POLICY DIMENSIONS

Policy must not be treated as one universal hierarchy.

Different policy dimensions may have different specific scopes.

The platform should resolve each dimension independently.

Primary dimensions include:

- PRODUCT ACCESS
- PRICING
- PROMOTIONS
- PAYMENT REQUIREMENT
- PAYMENT METHOD
- CANCELLATION
- REFUND
- PARTNER COMMERCIAL TERMS
- BRAND PRESENTATION
- AVAILABILITY
- BOOKING
- PERMISSIONS
- CUSTOMER COMMUNICATION

---

# 5. GENERAL AUTHORITY PRINCIPLE

For any policy dimension:

1. Identify the active brand when required.
2. Identify the product or transfer.
3. Identify the actor.
4. Identify the customer/account/partner when applicable.
5. Identify all approved policies that apply.
6. Reject policies outside their authorized scope.
7. Apply the most specific valid approved policy.
8. Preserve Global Rules.
9. If two equally specific approved policies conflict and no explicit precedence exists:

DATA / POLICY CONFLICT
→ PERICO HUMAN ASSISTANCE

Never guess which policy should win.

---

# 6. PRICING AUTHORITY

Recommended pricing precedence:

1. Explicit product + brand + account/partner-specific approved price
2. Explicit product + account/partner-specific approved price
3. Explicit product + brand-specific approved price
4. Explicit canonical product approved selling price
5. Approved brand pricing formula or pricing profile
6. Approved account/partner commercial pricing rule
7. Approved platform pricing rule
8. Human Assistance

The exact applicable order may be narrowed by an explicit commercial agreement.

No layer may create a price merely because a higher-priority price is missing.

---

# 7. BRAND PRICE ISOLATION

A price belonging to:

Brand A

must never be used for:

Brand B

unless the price rule explicitly authorizes both brands.

A lower-cost brand does not change the canonical operational product.

It creates an approved commercial offer associated with its own brand context.

---

# 8. SUPPLIER PUBLIC PRICE RULE

Where an approved Perico product uses the supplier's regular public website price as its selling-price reference:

Use the supplier's approved REGULAR PUBLIC PRICE.

Do not automatically use:

- Promotional price
- Flash sale
- Promo code
- Direct-booking discount
- Website-only discount
- Temporary campaign

Supplier promotional pricing does not automatically apply to Perico-controlled brands.

Internal supplier research does not authorize customer redirection.

---

# 9. PROMOTION AUTHORITY

Promotion precedence:

1. Explicit product + brand + customer/account promotion
2. Explicit product + brand promotion
3. Explicit brand promotion
4. Explicit account/partner promotion
5. Explicit platform promotion
6. No promotion

A promotion must satisfy:

- Brand scope
- Product scope
- Channel scope when applicable
- Customer/partner eligibility
- Start date
- End date
- Usage conditions
- Status

Never infer promotion eligibility.

---

# 10. DISCOUNT AUTHORITY

No discount exists unless explicitly authorized.

Discount permission should identify:

- Authorized brand
- Authorized product
- Authorized actor/role
- Maximum amount or percentage
- Approval requirement
- Valid period when applicable

Virtual agents may not independently negotiate outside approved authority.

---

# 11. PAYMENT REQUIREMENT AUTHORITY

Payment requirement determines:

WHAT MUST BE PAID
AND
WHEN THE PAYMENT CONDITION IS SATISFIED.

Recommended precedence:

1. Product + brand + account-specific approved payment rule
2. Product-specific approved payment rule
3. Brand + account/partner-specific approved payment rule
4. Account/partner-specific approved payment rule
5. Brand-specific approved payment rule
6. Approved B2B commercial rule
7. Approved platform/global payment rule
8. Human Assistance

The Payment & Confirmation Engine owns payment requirement interpretation.

---

# 12. CURRENT DIRECT TRANSFER RULE

For direct-customer transfers:

Either:

100% full payment

or:

minimum 15% deposit

may satisfy the currently approved general payment requirement for securing/formalizing the reservation, subject to operational acceptance.

A quote alone does not secure the transfer.

Providing booking details alone does not secure the transfer.

---

# 13. CURRENT B2B RULE

For approved B2B agency reservations:

40% payment/deposit

is the currently approved general rule unless an applicable product-specific or account-specific approved policy overrides it.

The remaining balance does not automatically have to be cash.

Do not invent:

- Balance deadline
- Payment method
- Processing charge

when not established.

---

# 14. NO UNIVERSAL EXCURSION DEPOSIT

No universal direct-customer excursion deposit percentage exists unless explicitly approved.

Do not automatically apply:

15%

30%

40%

50%

or any other percentage to excursions.

If no applicable payment rule exists:

PAYMENT TERMS PENDING
→ PERICO HUMAN ASSISTANCE

---

# 15. PAYMENT METHOD AUTHORITY

Payment requirement and payment method are separate.

Payment & Confirmation Engine determines:

WHAT IS OWED.

Payment Router determines:

HOW AN APPROVED PAYMENT MAY BE COLLECTED.

The Payment Router may select only methods/providers authorized for the active:

- Brand
- Account
- Partner
- Product
- Currency
- Amount
- Channel
- Transaction

A payment provider may not change the underlying payment requirement.

---

# 16. PROCESSING FEES

A processing fee may be customer-facing only when explicitly approved.

Internal provider cost does not automatically become a customer fee.

Never invent or estimate a payment-processing charge.

---

# 17. CANCELLATION AUTHORITY

Recommended cancellation precedence:

1. Product + brand + account-specific approved cancellation policy
2. Product-specific approved cancellation policy
3. Brand + account/partner-specific approved cancellation policy
4. Account/partner-specific approved cancellation policy
5. Brand-specific approved cancellation policy
6. Approved B2B cancellation policy
7. Approved platform fallback cancellation policy
8. Human Assistance

A more specific policy applies only within its authorized scope.

---

# 18. GENERAL CANCELLATION FALLBACK

When no more specific approved policy applies:

More than 48 hours before service:
100% of applicable deposit refundable.

24–48 hours before service:
50% of applicable deposit refundable.

Less than 24 hours:
No refund.

No-show or missed pickup:
No refund.

After activity begins:
No refund.

Operator/safety cancellation:
Follow applicable product/operational policy.

This fallback never overrides a verified product-specific policy.

---

# 19. REFUND AUTHORITY

Cancellation eligibility and refund execution are separate.

Applicable policy determines:

REFUND ELIGIBILITY.

Authorized business logic or staff determines:

REFUND APPROVAL.

Payment Router/provider determines:

REFUND EXECUTION.

A refund request does not equal approval.

A successful provider refund does not rewrite the cancellation policy.

---

# 20. PRODUCT ACCESS AUTHORITY

A product may exist in the canonical catalog while being unavailable for sale through a particular brand, partner or channel.

Product access may depend on:

- Brand
- Partner
- Account
- Market
- Channel
- Product status
- Commercial agreement

Canonical product existence does not automatically grant commercial access.

---

# 21. AVAILABILITY AUTHORITY

Availability is controlled by:

availability-engine.md

using approved authoritative inventory/operational sources.

Commercial policy may determine whether a product MAY BE SOLD through a brand.

Commercial policy may not manufacture physical availability.

---

# 22. BOOKING AUTHORITY

Booking workflow is controlled by:

booking-engine.md

Booking policy may depend on:

- Product
- Brand
- Actor
- Partner/account
- Participant configuration
- Operational requirements

Payment state remains separate.

Availability state remains separate.

---

# 23. PERMISSION AUTHORITY

Permissions are controlled by:

identity-permissions-engine.md

Commercial policy may define an entitlement.

Identity & Permissions determines whether the current actor is authorized to use that entitlement.

A customer or partner claiming a special rate does not establish authorization.

---

# 24. PARTNER COMMERCIAL AUTHORITY

Partner relationships are controlled by:

partner-reseller-engine.md

Partner-specific commercial terms may include:

- Net rates
- Commission
- Account-specific pricing
- Product access
- Payment terms
- Booking permissions

Partner terms do not automatically apply to direct customers.

One partner's terms never apply to another partner.

---

# 25. BRAND AUTHORITY

Brand commercial behavior is controlled by:

brand-commercial-policy-layer.md

Brand policy may define:

- Product catalog
- Customer-facing product name
- Approved retail price
- Approved promotions
- Commercial presentation
- Payment presentation
- Support identity

Brand policy may not violate:

- Global Rules
- Operational truth
- Safety requirements
- Legal identity accuracy
- Permissions

---

# 26. CHANNEL AUTHORITY

Channel Layer controls communication transport and presentation capability.

Channel does not independently determine:

- Price
- Product truth
- Availability
- Payment requirement
- Cancellation
- Refund eligibility
- Booking confirmation

A channel-specific commercial policy applies only when explicitly approved.

---

# 27. VIRTUAL AGENT AUTHORITY

Virtual Reseller Agents may operate only within authorized scope.

They may:

- Discover
- Qualify
- Explain
- Recommend
- Present approved quotes
- Guide booking
- Guide approved payment

They may not independently create:

- Prices
- Discounts
- Promotions
- Availability
- Payment requirements
- Cancellation rules
- Refund approval
- Supplier access
- Confirmation

---

# 28. INTEGRATION AUTHORITY

External systems provide capabilities and data.

They do not automatically define Perico policy.

Integration Registry determines:

- Which system is authorized
- Which capabilities it provides
- Which brands/products/accounts it may serve
- How external states map into canonical Perico states

API success does not automatically mean business success.

API failure does not automatically mean business failure.

---

# 29. HUMAN OVERRIDES

Authorized Perico staff may issue a scoped override.

An override should identify, where practical:

- Actor/staff member
- Transaction
- Brand
- Product
- Policy dimension
- Previous value
- Approved override
- Reason
- Timestamp
- Scope

A transaction-specific override does not become global policy.

---

# 30. POLICY CONFLICT

When two applicable policies conflict:

First:
compare scope and specificity.

Then:
apply explicit precedence.

If still unresolved:

DO NOT:

- Choose the cheaper rule
- Choose the more profitable rule
- Choose the newest-looking rule
- Choose the external platform's rule
- Average the values
- Guess

Instead:

POLICY CONFLICT
→ PERICO HUMAN ASSISTANCE

---

# 31. POLICY VERSIONING

Future structured policies should support:

policy_id

version

status

effective_from

effective_until

brand_scope

product_scope

account_scope

partner_scope

channel_scope

created_at

updated_at

approved_by

This allows future policy changes without silently rewriting historical transactions.

---

# 32. TRANSACTION POLICY SNAPSHOT

Where technically practical, important transactions should preserve the policy context used at the time of execution.

Examples:

pricing_policy_id

payment_policy_id

cancellation_policy_id

promotion_id

brand_id

partner_id

This allows later auditing when policies change.

---

# 33. EXISTING BOOKINGS

A new policy does not automatically rewrite an existing confirmed booking.

Changes to existing transactions must follow:

- Applicable contract
- Existing booking terms
- Approved modification workflow
- Authorized human decision when necessary

---

# 34. POLICY EFFECTIVE DATES

A policy with a future effective date must not apply early.

An expired policy must not apply to new transactions unless explicitly preserved for an existing booking/account agreement.

---

# 35. NO SILENT FALLBACK

If a required policy is missing:

Do not silently substitute an unrelated policy.

Examples:

Missing Brand B payment rule
does not mean
use Brand A payment rule.

Missing excursion deposit rule
does not mean
use transfer 15%.

Missing B2B account rate
does not mean
invent a net rate.

Use Human Assistance when required.

---

# 36. FINAL POLICY VALIDATION

Before applying a policy to a customer transaction, validate:

1. Global Rules are satisfied.
2. brand_id is correct when required.
3. product_id is correct.
4. actor type is correct.
5. partner/account identity is verified when required.
6. Policy is active.
7. Policy is within effective dates.
8. Policy applies to the active brand.
9. Policy applies to the product.
10. Policy applies to the account/partner when applicable.
11. Policy applies to the channel when channel scope exists.
12. No more-specific approved policy supersedes it.
13. Operational truth is preserved.
14. No unauthorized discount is created.
15. No external supplier sales destination is exposed.

If validation fails:

DO NOT APPLY THE POLICY.

---

# 37. NON-NEGOTIABLE RULE

NEVER ALLOW DIFFERENT ENGINES TO INDEPENDENTLY DECIDE WHICH COMMERCIAL POLICY WINS.

POLICY PRECEDENCE MUST BE CENTRALIZED.

MORE SPECIFIC DOES NOT MEAN MORE POWERFUL THAN GLOBAL RULES.

MORE SPECIFIC MEANS:

MORE SPECIFIC WITHIN AN AUTHORIZED SCOPE.

---

# 38. CORE PRINCIPLE

GLOBAL RULES
PROTECT THE PLATFORM.

PRODUCT MASTERS
DEFINE OPERATIONAL TRUTH.

BRANDS
DEFINE AUTHORIZED COMMERCIAL PRESENTATION.

PARTNERS AND ACCOUNTS
DEFINE AUTHORIZED COMMERCIAL RELATIONSHIPS.

SPECIALIZED ENGINES
EXECUTE THEIR OWN BUSINESS DIMENSIONS.

INTEGRATIONS
PROVIDE CAPABILITIES.

HUMANS
RESOLVE AUTHORIZED EXCEPTIONS AND TRUE CONFLICTS.

ONE POLICY AUTHORITY MODEL.

NO GUESSING.

NO CROSS-BRAND LEAKAGE.

NO UNAUTHORIZED DISCOUNTS.

NO POLICY CREATED BY THE AI.