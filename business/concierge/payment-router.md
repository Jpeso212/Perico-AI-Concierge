# PERICO AI CONCIERGE — PAYMENT ROUTER

## 1. PURPOSE

The Payment Router determines which approved Perico payment method and payment provider may be used for a transaction.

It does NOT determine:

- Product price
- Deposit percentage
- Amount due
- Cancellation policy
- Refund entitlement
- Whether a reservation is confirmed

Those rules remain controlled by the appropriate Perico engines.

The Payment Router answers:

HOW CAN THIS APPROVED PAYMENT BE COLLECTED?

CORE PRINCIPLE:

PAYMENT POLICY DETERMINES WHAT IS OWED.

PAYMENT ROUTER DETERMINES HOW AN APPROVED PAYMENT MAY BE COLLECTED.

---

# 2. ARCHITECTURAL POSITION

Conceptual flow:

QUOTE
→ AVAILABILITY
→ BOOKING REQUIREMENTS
→ PAYMENT REQUIREMENT
→ PAYMENT ROUTER
→ APPROVED PAYMENT METHOD
→ PAYMENT PROVIDER ADAPTER
→ PAYMENT RESULT
→ PAYMENT VERIFICATION
→ BOOKING / OPERATIONAL ACCEPTANCE
→ CONFIRMATION

The Payment Router operates after the required payment amount and applicable payment terms are known.

---

# 3. SOURCE OF PAYMENT POLICY

Payment policy is controlled by:

payment-confirmation-engine.md

The Payment Router must not override that engine.

Applicable payment-rule precedence remains:

PRODUCT-SPECIFIC APPROVED PAYMENT RULE
→ CUSTOMER/ACCOUNT-SPECIFIC APPROVED COMMERCIAL RULE
→ APPROVED B2B COMMERCIAL RULE
→ APPROVED PERICO GLOBAL RULE
→ PERICO HUMAN ASSISTANCE

The Payment Router begins only after the applicable payment requirement has been established.

---

# 4. PAYMENT ROUTER RESPONSIBILITIES

The Payment Router may determine:

- Which payment methods are permitted
- Which payment providers support those methods
- Whether the provider is operational
- Whether the transaction amount is supported
- Whether the currency is supported
- Whether automatic verification is available
- Whether a processing fee applies under an approved rule
- Whether the method is allowed for the actor/account
- Whether the method supports deposit or full payment
- Whether the method supports refunds
- Which approved method should be presented first
- Which approved fallback may be used

It must not invent missing commercial rules.

---

# 5. PAYMENT METHOD VS PAYMENT PROVIDER

Always distinguish:

PAYMENT METHOD

from:

PAYMENT PROVIDER

Examples of payment methods:

CREDIT_CARD

DEBIT_CARD

BANK_TRANSFER

PAYMENT_LINK

CASH

DIGITAL_WALLET

ACCOUNT_CREDIT

AGENCY_SETTLEMENT

OTHER_APPROVED_METHOD

A provider is the system or company that executes or facilitates an approved method.

One provider may support multiple methods.

One method may be available through multiple providers.

---

# 6. CANONICAL PAYMENT METHODS

Possible canonical methods include:

CREDIT_CARD

DEBIT_CARD

PAYMENT_LINK

BANK_TRANSFER

CASH

DIGITAL_WALLET

ACCOUNT_BALANCE

AGENCY_CREDIT

PERIODIC_SETTLEMENT

MANUAL_PAYMENT

OTHER_APPROVED_METHOD

The existence of a canonical method does not mean Perico currently offers it.

A method becomes usable only after it is explicitly configured and approved.

---

# 7. PAYMENT PROVIDER PROFILE

Each payment provider may eventually have:

payment_provider_id

provider_name

integration_id

status

supported_methods

supported_currencies

minimum_amount

maximum_amount

supported_countries_if_relevant

supports_deposit

supports_full_payment

supports_partial_payment

supports_refund

supports_partial_refund

supports_webhook

supports_automatic_verification

supports_payment_link

processing_fee_rule

settlement_currency

priority

environment

last_verified

Do not invent missing provider capabilities.

---

# 8. PAYMENT PROVIDER STATUS

Possible states:

PLANNED

CONFIGURING

TESTING

ACTIVE

DEGRADED

DISABLED

SUSPENDED

FAILED

RETIRED

Only appropriately operational providers may be selected for automated production payment.

---

# 9. PAYMENT METHOD STATUS

Possible method states:

AVAILABLE

TEMPORARILY_UNAVAILABLE

ACCOUNT_RESTRICTED

PRODUCT_RESTRICTED

CHANNEL_RESTRICTED

AMOUNT_RESTRICTED

CURRENCY_RESTRICTED

REQUIRES_HUMAN_ASSISTANCE

NOT_AVAILABLE

Do not present an unavailable method as an option.

---

# 10. ROUTING INPUTS

The Payment Router may consider:

actor_type

customer_id

partner_id

account_id

product_id

booking_id

booking_total

amount_required_now

balance_remaining

currency

payment_requirement_type

channel

country_when_legitimately_relevant

commercial_profile

payment_terms

provider_status

method_availability

processing_fee_rule

automatic_verification_support

refund_support

transaction_limits

existing_payment_attempts

Not every transaction requires every input.

---

# 11. ACTOR CONTEXT

Payment routing may differ for:

DIRECT_CUSTOMER

B2B_AGENCY

AUTHORIZED_RESELLER

HOTEL_CONCIERGE

AFFILIATE

PERICO_STAFF_ASSISTED

VIRTUAL_RESELLER_CUSTOMER

The actor type does not itself create payment terms.

Applicable payment terms must already be established.

---

# 12. DIRECT CUSTOMER PAYMENTS

Direct customers should receive only approved Perico customer payment methods.

Never expose:

- Supplier payment methods
- Supplier bank details
- Supplier checkout
- Supplier payment links
- OTA checkout
- Competitor payment destination

The payment remains within the approved Perico payment environment.

---

# 13. B2B PAYMENT ROUTING

Approved agencies and resellers may have different payment methods based on their commercial profile.

Possible examples:

- Card
- Bank transfer
- Approved payment link
- Account credit
- Periodic settlement
- Other approved commercial arrangement

Do not assume every B2B partner has access to every method.

---

# 14. CURRENT GENERAL B2B PAYMENT REQUIREMENT

For approved Perico B2B agency reservations:

40% payment/deposit is generally required to reserve/confirm the service,

unless a product-specific or account-specific approved rule overrides it.

The Payment Router does not calculate this rule.

It receives:

amount_required_now

from the Payment & Confirmation / Quote workflow.

The remaining balance does not automatically have to be cash.

---

# 15. DIRECT CUSTOMER TRANSFER PAYMENT REQUIREMENT

For direct-customer transfer reservations, the approved rule is:

- 100% full payment

OR

- Minimum 15% deposit

subject to applicable operational acceptance.

The Payment Router determines which approved methods may collect that payment.

It does not change the 15% minimum.

---

# 16. NO UNIVERSAL EXCURSION DEPOSIT

Do not assume a universal direct-customer excursion deposit.

For excursions:

retrieve the applicable approved payment rule first.

If none exists:

PAYMENT TERMS PENDING
→ PERICO HUMAN ASSISTANCE

The Payment Router must not create a deposit percentage.

---

# 17. PAYMENT REQUIREMENT TYPES

Possible canonical payment requirements:

FULL_PAYMENT

MINIMUM_DEPOSIT

FIXED_DEPOSIT

PERCENTAGE_DEPOSIT

BALANCE_PAYMENT

PARTIAL_PAYMENT

ACCOUNT_SETTLEMENT

NO_PAYMENT_REQUIRED_NOW

CUSTOM

These describe what is owed.

They do not identify how it will be paid.

---

# 18. ROUTING PROCESS

Standard routing process:

RECEIVE PAYMENT REQUIREMENT
→ IDENTIFY ACTOR / ACCOUNT
→ IDENTIFY CURRENCY
→ IDENTIFY TRANSACTION AMOUNT
→ LOAD AUTHORIZED PAYMENT METHODS
→ FILTER RESTRICTED METHODS
→ LOAD OPERATIONAL PROVIDERS
→ VALIDATE LIMITS
→ VALIDATE FEES
→ VALIDATE VERIFICATION CAPABILITY
→ SELECT APPROVED OPTION
→ PRESENT CUSTOMER-APPROPRIATE METHOD
→ EXECUTE THROUGH PAYMENT ADAPTER

---

# 19. METHOD FILTERING

Remove payment methods that are not authorized for:

- Actor
- Account
- Product
- Currency
- Transaction amount
- Channel
- Commercial agreement
- Current provider status

Never present a method first and discover afterward that the customer cannot use it when the restriction was already known.

---

# 20. PROVIDER SELECTION

When multiple providers support the same approved payment method, routing may consider:

1. Business authorization
2. Provider status
3. Currency support
4. Transaction amount support
5. Account eligibility
6. Automatic verification
7. Processing cost
8. Reliability
9. Refund support
10. Operational preference

No single factor automatically controls selection unless Perico explicitly defines that rule.

---

# 21. CUSTOMER CHOICE

When multiple approved methods are valid, the customer may be offered a reasonable selection.

The AI should not overwhelm the customer with unnecessary payment options.

Preferred presentation:

Offer the most appropriate approved options.

Allow the customer to choose when appropriate.

---

# 22. DEFAULT PAYMENT METHOD

Do not invent a universal default payment method.

A default may exist only when Perico explicitly configures one for the applicable:

- Customer type
- Partner
- Product
- Currency
- Channel
- Market

---

# 23. PAYMENT METHOD PRIORITY

Perico may eventually assign method priorities.

Example:

priority = 1
priority = 2
priority = 3

Priority affects routing preference.

It does not authorize an otherwise prohibited method.

---

# 24. CURRENCY

Never assume the payment currency.

Use the approved currency for the quote or commercial agreement.

If the selected provider does not support the required currency:

Try another approved provider or method.

If none exists:

PERICO HUMAN ASSISTANCE.

---

# 25. CURRENCY CONVERSION

Do not automatically convert currency unless Perico has approved:

- Conversion mechanism
- Exchange-rate source
- Applicable fee
- Rounding rule

If conversion is not established:

Use the original approved transaction currency.

---

# 26. PROCESSING FEES

Processing fees may apply only when an approved rule establishes them.

The Payment Router must never invent:

- Percentage
- Fixed fee
- Card surcharge
- Currency fee
- International fee

If a provider charges Perico internally, that does not automatically mean the fee may be passed to the customer.

---

# 27. FEE AUTHORITY

Before showing a customer fee, verify:

1. Fee exists.
2. Fee may legally and commercially be passed to this transaction.
3. Exact amount or formula is known.
4. Correct payment method/provider is being used.

If unresolved:

Do not invent the fee.

---

# 28. TRANSACTION LIMITS

A payment provider may have:

minimum_amount

maximum_amount

daily_limit

transaction_limit

account_limit

Method selection must respect known limits.

Do not split a payment merely to bypass provider restrictions unless an approved Perico workflow explicitly permits it.

---

# 29. DEPOSIT SUPPORT

A provider may support:

FULL_PAYMENT_ONLY

or:

PARTIAL_PAYMENT_ALLOWED

The provider capability must match the applicable payment requirement.

If the customer owes a 40% deposit and the provider cannot collect partial payment:

Select another approved method or use Human Assistance.

Do not change the required deposit simply to fit the provider.

---

# 30. CUSTOMER PAYS MORE THAN MINIMUM

When the payment policy defines a minimum deposit, the customer may pay more than the minimum or the full amount when the applicable workflow allows it.

Example:

Transfer total = $200

Minimum 15% = $30

Valid payment may be:

$30

$50

$100

$200

when supported by the applicable payment workflow.

The router must not treat payment above the minimum as an error merely because it exceeds the minimum.

---

# 31. CUSTOMER PAYS LESS THAN REQUIRED

If verified payment is below the required minimum:

PAYMENT REQUIREMENT NOT SATISFIED.

Record:

amount_required

amount_received

balance_to_requirement

Do not mark the payment requirement complete.

---

# 32. PAYMENT LINK

An approved Payment Link is a method of collecting payment.

A payment link must be:

- Generated by an approved Perico provider
- Authorized for the transaction
- Associated with the correct amount/currency
- Associated with the correct booking/customer when supported

Never fabricate a payment URL.

---

# 33. PAYMENT LINK EXPIRATION

If a payment provider supports expiration:

Track the provider's verified expiration status.

Do not invent a payment-link expiration deadline.

An expired payment link does not automatically mean the booking is cancelled.

Booking state must be evaluated separately.

---

# 34. BANK TRANSFER

Bank transfer may be offered only when approved Perico banking instructions exist for the applicable transaction.

Never invent:

- Bank
- Account number
- SWIFT
- Routing number
- Beneficiary
- Transfer instructions

Payment proof does not automatically equal verified settlement.

---

# 35. CASH

Cash may be used only when allowed by the applicable Perico workflow.

Do not assume:

BALANCE = CASH.

B2B remaining balances do not automatically require cash.

If cash is allowed, exact collection instructions must come from approved Perico operational rules.

---

# 36. ACCOUNT CREDIT

Agency or reseller credit may be used only when the partner has an approved credit arrangement.

Never create credit because the partner is B2B.

Partner credit eligibility belongs to:

partner-reseller-engine.md

---

# 37. PERIODIC SETTLEMENT

Periodic settlement may be available for approved partners.

Examples may eventually include:

WEEKLY

BIWEEKLY

MONTHLY

CUSTOM

Do not invent settlement schedules.

Only use an approved partner commercial agreement.

---

# 38. MANUAL PAYMENT

Some payments may require manual Perico processing.

Possible state:

MANUAL_PAYMENT_REQUIRED

The customer remains within the Perico workflow.

Do not redirect them to a supplier.

---

# 39. AUTOMATIC VERIFICATION

Providers supporting automatic verification are preferred when appropriate because they can return verified payment state directly.

Automatic verification may use:

- API
- Webhook
- Provider transaction lookup
- Other approved integration

Provider verification must map into canonical Perico payment states.

---

# 40. MANUAL VERIFICATION

Some methods may require Perico staff verification.

Examples may include certain:

- Bank transfers
- Cash payments
- Manual transactions

Possible state:

PAYMENT VERIFICATION PENDING

Do not claim payment received until verification is complete.

---

# 41. CUSTOMER PAYMENT CLAIM

If the customer says:

"I paid."

Record the claim appropriately.

Do not automatically mark:

PAYMENT RECEIVED

or:

FULL PAYMENT RECEIVED.

Verify through an approved source.

---

# 42. PROOF OF PAYMENT

Customer-provided proof may support verification.

Proof of payment does not automatically prove:

- Settlement
- Correct amount
- Correct currency
- Correct booking
- Successful transaction

Use the applicable verification workflow.

---

# 43. PAYMENT PROVIDER RESULT

Provider result should normalize into fields such as:

payment_provider

payment_method

transaction_id

currency

booking_total

amount_required_now

amount_submitted

amount_verified

balance_remaining

processing_fee

payment_status

verification_status

booking_id

customer_id

partner_id

timestamp

---

# 44. PAYMENT STATUS

Canonical payment states remain defined by:

payment-confirmation-engine.md

The Payment Router must not create competing payment states.

Provider-specific terminology must be mapped through the payment adapter.

---

# 45. PAYMENT SUCCESS VS BOOKING CONFIRMATION

Never treat:

PAYMENT SUCCESS

as automatically equal to:

BOOKING CONFIRMED.

After payment, the workflow may still require:

- Payment verification
- Reservation creation
- Availability validation
- Operational acceptance
- Supplier acceptance
- Other product-specific requirement

---

# 46. PAYMENT AUTHORIZATION VS CAPTURE

If a provider distinguishes:

AUTHORIZED

from:

CAPTURED

the adapter must preserve the distinction.

Do not tell the customer funds were received merely because a card authorization exists unless Perico's approved payment workflow treats that state as received.

---

# 47. PENDING PAYMENT

Some providers may return:

PENDING

The router must preserve this state.

Do not retry immediately through another provider if the original transaction may still complete.

This could create duplicate payment.

---

# 48. FAILED PAYMENT

A verified provider decline or failure may result in:

PAYMENT FAILED

The customer may then be offered another approved method when appropriate.

Do not expose unnecessary provider error details.

---

# 49. TECHNICAL PAYMENT FAILURE

A technical failure is different from a declined payment.

Examples:

- API timeout
- Provider unavailable
- Connection failure
- Webhook delay

Possible internal state:

PAYMENT RESULT UNKNOWN

or:

PAYMENT INTEGRATION FAILURE

Do not tell the customer their payment was declined unless the provider actually established that result.

---

# 50. UNKNOWN PAYMENT RESULT

When payment submission occurred but the result is unknown:

DO NOT IMMEDIATELY RETRY.

First:

CHECK EXISTING TRANSACTION

using:

- transaction reference
- idempotency key
- booking reference
- provider lookup

This protects against duplicate charges.

---

# 51. IDEMPOTENCY

Payment creation should use idempotency protection whenever supported.

Repeated:

- Click
- Message
- API retry
- Timeout retry
- Webhook

must not create duplicate charges.

---

# 52. DUPLICATE PAYMENT DETECTION

Before creating another payment request, check when technically possible for:

- Existing pending payment
- Existing verified payment
- Same booking
- Same amount
- Same customer
- Recent transaction
- Existing provider transaction ID

Potential duplicate:

STOP
→ VERIFY EXISTING PAYMENT

---

# 53. OVERPAYMENT

If verified amount exceeds the amount due:

Do not automatically refund the difference.

State:

OVERPAYMENT REVIEW REQUIRED

→ PERICO HUMAN ASSISTANCE

unless an approved automatic overpayment rule exists.

---

# 54. PARTIAL PAYMENT

For valid partial payments, track:

booking_total

amount_required_now

amount_received

balance_remaining

minimum_requirement_satisfied

Do not lose the original total.

---

# 55. BALANCE PAYMENT

When a balance remains:

The router may later select an approved method for collecting the balance.

Do not assume the same provider must be used unless required.

Do not invent the balance due date.

---

# 56. MULTIPLE PAYMENT METHODS

A booking may potentially contain multiple payment transactions.

Example:

Deposit by payment link

Balance by approved card method

or another approved combination.

This is permitted only when the applicable Perico workflow allows it.

The system must reconcile all verified payments against the same booking.

---

# 57. PAYMENT ALLOCATION

Every verified payment should be associated with the correct:

customer

booking

partner when applicable

currency

amount

transaction

Do not leave successful payments without a booking/customer relationship when avoidable.

---

# 58. MULTIPLE BOOKINGS

If the customer is purchasing multiple products:

The payment workflow may use:

SEPARATE PAYMENTS

or

CONSOLIDATED PAYMENT

only when the applicable system and business rules support it.

Do not automatically combine unrelated bookings.

---

# 59. PAYMENT PROVIDER FALLBACK

If the primary provider is unavailable:

1. Determine whether a transaction may already exist.
2. Avoid duplicate charge.
3. Check authorized fallback.
4. Validate method/currency/amount.
5. Present fallback only when safe.

Fallback must not change the payment requirement.

---

# 60. PROVIDER OUTAGE

Provider outage does not mean:

PAYMENT DECLINED.

Possible customer-facing behavior:

Offer another approved method when safe.

or:

PERICO HUMAN ASSISTANCE.

Never send the customer to the supplier.

---

# 61. REFUNDS

Payment routing for refunds must use the provider or approved refund path associated with the verified payment when required.

Refund entitlement is not determined by the Payment Router.

Refund policy and approval remain governed by:

payment-confirmation-engine.md

---

# 62. REFUND CAPABILITY

Before automated refund execution, verify:

- Refund approved
- Original payment verified
- Provider supports refund
- Amount approved
- Currency correct
- Transaction reference valid
- Actor authorized

If any required condition fails:

DO NOT EXECUTE AUTOMATIC REFUND.

---

# 63. PARTIAL REFUND

Partial refunds may be executed only when:

- Approved by applicable policy/authority
- Provider supports partial refund
- Exact amount is established

Never invent the refund amount.

---

# 64. REFUND DESTINATION

Refund should normally follow the approved payment/provider workflow.

Do not independently ask the customer for alternative financial credentials unless Perico has an approved process requiring it.

---

# 65. CHARGEBACK

Chargeback is not the same as:

REFUND.

A chargeback may require:

PAYMENT DISPUTE REVIEW
→ PERICO HUMAN ASSISTANCE

Do not automatically cancel the booking solely because a chargeback event appears without checking operational context.

---

# 66. PAYMENT DISPUTE

Possible disputes:

- Customer says charged twice
- Customer disputes amount
- Payment appears missing
- Wrong booking credited
- Provider reports reversal
- Agency disputes settlement

Preserve evidence and transaction references.

Use Human Assistance when automatic reconciliation cannot safely resolve it.

---

# 67. CUSTOMER-FACING PAYMENT INFORMATION

Customer-facing payment communication should include only information necessary to complete the payment.

Examples:

- Amount due now
- Currency
- Approved payment method
- Approved payment destination/instructions
- Applicable approved fee
- Payment status

Do not expose internal provider routing logic.

---

# 68. INTERNAL PAYMENT INFORMATION

Internal fields may include:

provider priority

provider fee

settlement cost

internal merchant account

routing rule

integration ID

retry history

These should not automatically be exposed to customers.

---

# 69. PAYMENT SECURITY

Never request or store in ordinary Concierge conversation:

- Full card number
- CVV
- PIN
- Banking password
- One-time authentication code
- Private wallet key
- Security answers

Sensitive payment entry belongs in approved secure payment infrastructure.

---

# 70. PAYMENT TOKENIZATION

When providers support secure tokenization, Perico systems may use provider tokens according to the approved integration.

Never expose tokens to customers.

Never treat payment tokens as general identity credentials.

---

# 71. PAYMENT LINKS AND CUSTOMER CHANNELS

An approved payment destination may be delivered through:

- WhatsApp
- Website
- Email
- Partner portal
- Other approved Perico channel

Channel selection does not change the payment amount or payment policy.

---

# 72. VIRTUAL RESELLER PAYMENT BEHAVIOR

Virtual resellers may:

- Explain approved payment requirement
- Present approved payment methods
- Request creation of approved payment link
- Check payment state when authorized
- Continue booking after verified payment

Virtual resellers may NOT:

- Invent payment account
- Invent payment link
- Change required deposit
- Waive payment
- Invent processing fee
- Mark unverified payment as received
- Approve refund without authority

---

# 73. PARTNER PAYMENT BEHAVIOR

Partner payment options depend on the verified partner commercial profile.

A partner may not receive another partner's:

- Payment terms
- Credit arrangement
- Settlement method
- Processing fee agreement

---

# 74. PAYMENT ROUTING AND LANGUAGE

Language Engine controls customer-facing payment communication.

Translation must not change:

- Amount
- Currency
- Deposit requirement
- Fee
- Balance
- Deadline
- Payment status
- Refund status

---

# 75. PAYMENT ROUTING AND CHANNEL

Channel limitations may affect presentation.

Example:

A channel may not support payment buttons.

The same approved payment workflow may instead provide an authorized payment link.

Channel limitation must not change business policy.

---

# 76. AUDITABILITY

When technically supported, payment routing should record:

routing_id

booking_id

customer_id

partner_id

actor_id

amount

currency

payment_requirement

eligible_methods

selected_method

selected_provider

processing_fee

routing_reason

timestamp

Do not record secret payment credentials.

---

# 77. PAYMENT ROUTING REASON

For internal audit, routing may record why a method/provider was selected.

Examples:

DEFAULT_APPROVED_PROVIDER

ACCOUNT_SPECIFIC_METHOD

CURRENCY_REQUIREMENT

AMOUNT_LIMIT

AUTOMATIC_VERIFICATION

PRIMARY_PROVIDER_UNAVAILABLE

CUSTOMER_SELECTED_APPROVED_METHOD

Do not expose internal routing reasons unnecessarily.

---

# 78. PROVIDER HEALTH

Routing may consider provider health when technically available.

Possible states:

HEALTHY

DEGRADED

UNAVAILABLE

UNKNOWN

Do not route new transactions to a known unavailable provider when an authorized alternative exists.

---

# 79. RECONCILIATION

Payment records should eventually support reconciliation between:

PERICO BOOKING
↔ PAYMENT ROUTER
↔ PAYMENT PROVIDER
↔ ACCOUNTING

Reconciliation should detect:

- Missing payment
- Duplicate payment
- Incorrect amount
- Incorrect currency
- Unmatched transaction
- Refund mismatch
- Settlement discrepancy

---

# 80. ACCOUNTING INTEGRATION

Accounting systems may receive verified financial transaction data through an approved integration.

Accounting systems do not determine:

- Product availability
- Booking confirmation
- Customer cancellation entitlement

unless an explicit Perico business rule says otherwise.

---

# 81. HUMAN HANDOFF

Use:

human-handoff-engine.md

when:

- No approved payment method is available
- Payment terms are missing
- Fee is unclear
- Currency is unsupported
- Payment result is unknown
- Duplicate charge suspected
- Overpayment occurs
- Payment cannot be verified
- Partner credit is unclear
- Refund requires approval
- Chargeback occurs
- Provider records conflict
- Payment integration fails without safe fallback

Preserve all transaction context.

---

# 82. ROUTING FAILURE

If no approved method can complete the transaction:

PAYMENT ROUTING FAILED
→ PERICO HUMAN ASSISTANCE

Do not:

- Invent a payment method
- Change the amount
- Reduce the deposit
- Send supplier payment instructions
- Mark booking confirmed

---

# 83. FINAL ROUTING VALIDATION

Before presenting or executing a payment method, verify:

1. Payment requirement established.
2. Exact amount required now established.
3. Currency established.
4. Actor/account identified when relevant.
5. Method authorized.
6. Provider approved.
7. Provider operational.
8. Transaction amount supported.
9. Currency supported.
10. Applicable fee established.
11. Customer-facing destination authorized.
12. Duplicate-payment risk checked.
13. Booking/payment identifiers available when required.
14. No supplier payment destination exposed.
15. No protected credentials exposed.

If validation fails:

DO NOT EXECUTE.

---

# 84. NON-NEGOTIABLE RULE

NEVER CONFUSE:

PAYMENT POLICY
WITH
PAYMENT METHOD.

NEVER CONFUSE:

PAYMENT METHOD
WITH
PAYMENT PROVIDER.

NEVER CONFUSE:

PAYMENT SUBMITTED
WITH
PAYMENT VERIFIED.

NEVER CONFUSE:

PAYMENT VERIFIED
WITH
BOOKING CONFIRMED.

NEVER CHANGE A BUSINESS RULE
JUST TO FIT A PAYMENT PROVIDER.

---

# 85. CORE PRINCIPLE

ONE PAYMENT POLICY FRAMEWORK.

MULTIPLE APPROVED PAYMENT METHODS.

MULTIPLE APPROVED PAYMENT PROVIDERS.

ONE NORMALIZED PAYMENT STATE.

NO DUPLICATE CHARGES.

NO INVENTED FEES.

NO SUPPLIER PAYMENT REDIRECTION.

PERICO REMAINS IN CONTROL.