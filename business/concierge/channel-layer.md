# PERICO AI CONCIERGE — CHANNEL LAYER

## 1. PURPOSE

The Channel Layer defines how customers, partners, resellers, virtual agents and Perico staff communicate with the Perico AI Concierge across different communication channels.

Possible channels include:

- WhatsApp
- Website chat
- Website booking assistant
- Instagram messaging
- Facebook Messenger
- Email
- SMS
- Partner portal
- Reseller portal
- Staff interface
- API-driven interfaces
- Future communication channels

The Channel Layer controls communication transport and presentation.

It does NOT control:

- Product truth
- Pricing
- Availability
- Booking rules
- Payment requirements
- Cancellation policy
- Partner permissions
- Confirmation rules

CORE PRINCIPLE:

ONE CONCIERGE BRAIN.

MANY COMMUNICATION CHANNELS.

---

# 2. ARCHITECTURAL POSITION

Conceptual inbound flow:

CUSTOMER / PARTNER
→ CHANNEL
→ CHANNEL ADAPTER
→ NORMALIZED MESSAGE
→ IDENTITY / SESSION CONTEXT
→ ORCHESTRATOR
→ APPROPRIATE CONCIERGE ENGINE

Conceptual outbound flow:

CONCIERGE ENGINE
→ ORCHESTRATOR
→ LANGUAGE ENGINE
→ CHANNEL PRESENTATION
→ CHANNEL ADAPTER
→ CUSTOMER / PARTNER

The communication channel must not redefine Perico business logic.

---

# 3. CHANNEL TYPES

Canonical channel types may include:

WHATSAPP

WEBSITE_CHAT

WEBSITE_BOOKING_ASSISTANT

INSTAGRAM

FACEBOOK_MESSENGER

EMAIL

SMS

PARTNER_PORTAL

RESELLER_PORTAL

STAFF_INTERFACE

API_CHANNEL

VOICE_CHANNEL

OTHER_APPROVED_CHANNEL

The existence of a canonical channel type does not mean the channel is currently active.

---

# 4. CHANNEL STATUS

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

Only appropriately active channels should receive normal automated production traffic.

---

# 5. CHANNEL PROFILE

Each channel integration may eventually define:

channel_id

channel_type

provider

integration_id

status

environment

account_reference

supported_message_types

supports_inbound

supports_outbound

supports_media

supports_buttons

supports_templates

supports_payment_links

supports_location

supports_handoff

supports_delivery_status

supports_read_status

session_behavior

last_verified

Do not invent unsupported capabilities.

---

# 6. CHANNEL IS NOT IDENTITY

A communication channel does not establish actor identity.

Examples:

WhatsApp user ≠ automatically direct customer.

Email sender ≠ automatically travel agency.

Partner portal session ≠ automatically authorized unless authenticated.

Instagram account ≠ automatically verified customer.

Identity and authorization remain controlled by:

identity-permissions-engine.md

---

# 7. CHANNEL IS NOT SALES SOURCE

Communication channel and sales source are separate.

Example:

CHANNEL:
WhatsApp

SALES SOURCE:
B2B Agency

Another example:

CHANNEL:
Website Chat

SALES SOURCE:
Virtual Reseller

Another:

CHANNEL:
WhatsApp

SALES SOURCE:
Perico Direct

Preserve both independently.

---

# 8. CHANNEL IS NOT BOOKING PLATFORM

Never confuse:

WHATSAPP

with:

BÓKUN

WhatsApp may be the communication channel.

Bókun may be the booking execution system.

Similarly:

Instagram may be the communication channel.

Peek Pro may be the reservation platform.

A reseller portal may be the sales channel.

Rezgo may be the booking system.

These are separate architectural roles.

---

# 9. CHANNEL IS NOT PAYMENT PROVIDER

A customer may receive payment instructions through WhatsApp.

That does not make WhatsApp the payment provider.

The Payment Router determines the approved payment method/provider.

The Channel Layer only delivers the approved customer-facing payment experience.

---

# 10. NORMALIZED INBOUND MESSAGE

Incoming messages should be normalized where technically practical.

Possible fields:

message_id

conversation_id

channel_id

channel_type

channel_account

sender_reference

actor_id_if_known

customer_id_if_known

partner_id_if_known

agent_id_if_known

timestamp

message_type

text

attachments

language_hint

reply_to_message_id

location_data

metadata

Do not treat unverified channel metadata as verified identity.

---

# 11. MESSAGE TYPES

Possible normalized message types:

TEXT

IMAGE

VIDEO

AUDIO

VOICE_NOTE

DOCUMENT

LOCATION

CONTACT

BUTTON_RESPONSE

QUICK_REPLY

FORM_RESPONSE

SYSTEM_EVENT

OTHER

Different channels may support different types.

---

# 12. ATTACHMENTS

Attachments may include:

- Images
- Videos
- Audio
- Documents
- Payment proof
- Booking documents
- Flight information
- Screenshots

Attachments should be associated with the correct conversation and actor.

Do not automatically trust the factual content of an attachment without appropriate validation.

---

# 13. NORMALIZED OUTBOUND MESSAGE

Possible fields:

message_id

conversation_id

channel_id

recipient_reference

language

message_type

content

attachments

buttons

quick_replies

payment_reference

booking_reference

template_reference

metadata

The business content must already be authorized before channel delivery.

---

# 14. MESSAGE PRESENTATION

The Channel Layer may adapt presentation.

Examples:

WhatsApp:
Short conversational messages.

Website:
Structured cards or buttons.

Email:
Longer formatted summaries.

Partner portal:
Structured transaction details.

Presentation may change.

Business meaning must not.

---

# 15. CHANNEL CAPABILITIES

Possible channel capabilities:

TEXT

IMAGE

VIDEO

AUDIO

DOCUMENT

BUTTON

QUICK_REPLY

FORM

LOCATION

CONTACT

PAYMENT_LINK

RICH_CARD

TEMPLATE_MESSAGE

DELIVERY_RECEIPT

READ_RECEIPT

THREADING

The Orchestrator should not assume every channel supports every capability.

---

# 16. CAPABILITY FALLBACK

If a channel does not support a desired feature, use an appropriate fallback.

Example:

Preferred:
Interactive booking button.

Fallback:
Plain text response with approved next step.

Preferred:
Rich product cards.

Fallback:
Concise text comparison.

The fallback must preserve business meaning.

---

# 17. LANGUAGE

Customer-facing language is controlled by:

language-engine.md

The Channel Layer may provide:

language_hint

but the channel must not independently redefine customer language.

Language switching must preserve the same conversation context.

---

# 18. SESSION

A channel session represents an active conversational context.

Possible fields:

conversation_id

channel_id

customer_id

actor_id

partner_id

agent_id

language

current_intent

current_product

quote_id

booking_id

payment_id

handoff_id

last_activity

session_status

Not every conversation requires every field.

---

# 19. SESSION STATUS

Possible states:

ACTIVE

WAITING_CUSTOMER

WAITING_SYSTEM

WAITING_PAYMENT

WAITING_AVAILABILITY

WAITING_HUMAN

COMPLETED

EXPIRED

CLOSED

Session state does not replace canonical booking or payment states.

---

# 20. CONTEXT PRESERVATION

The Channel Layer must preserve conversation context.

Known information should not disappear simply because the conversation contains multiple messages.

Examples:

Customer already provided:

- Date
- Hotel
- Party size
- Product
- Child ages
- Flight
- Language

Do not ask again unless:

- Information changed
- Information became stale
- Clarification is required
- Verification is required

---

# 21. CROSS-CHANNEL CONTINUITY

When identity can be safely linked, Perico may continue a transaction across authorized channels.

Example:

Website Chat
→ WhatsApp
→ Payment
→ Confirmation

Another:

Agency Portal
→ Email
→ Perico Operations
→ Portal Confirmation

The customer should not need to restart unnecessarily.

---

# 22. CROSS-CHANNEL IDENTITY SAFETY

Do not merge two conversations solely because:

- Names match
- Hotel matches
- Product matches
- Phone looks similar
- Email display name matches

Cross-channel linking must use appropriate verified identifiers.

---

# 23. CANONICAL CONVERSATION ID

When technically possible, maintain a Perico-controlled:

conversation_id

independent of channel-specific thread identifiers.

External thread IDs should map to the canonical conversation.

---

# 24. CHANNEL THREAD MAPPING

Possible mapping:

perico_conversation_id

channel_id

external_thread_id

external_contact_id

customer_id

partner_id

last_message_id

This allows conversation continuity without making Perico dependent on one messaging provider.

---

# 25. WHATSAPP

WhatsApp is expected to be a major Perico customer communication and booking channel.

The Concierge should support a customer journey such as:

QUESTION
→ PRODUCT DISCOVERY
→ QUOTE
→ AVAILABILITY
→ BOOKING
→ PAYMENT
→ CONFIRMATION
→ SUPPORT

without unnecessarily sending the customer outside the Perico environment.

---

# 26. WHATSAPP BOOKING

Perico intends to support direct booking through WhatsApp.

WhatsApp booking must use:

- Perico product truth
- Quote Engine
- Availability Engine
- Booking Engine
- Payment Router
- Payment & Confirmation Engine
- Human Handoff when necessary

WhatsApp must not become dependent on TRYTN.

---

# 27. WHATSAPP + BOOKING PLATFORM

A WhatsApp customer may communicate entirely through WhatsApp while an approved booking platform performs reservation actions behind the scenes.

Possible examples:

WhatsApp
→ Perico Concierge
→ Bókun

WhatsApp
→ Perico Concierge
→ Peek Pro

WhatsApp
→ Perico Concierge
→ Rezgo

The customer-facing conversation remains controlled by Perico.

---

# 28. WEBSITE CHAT

Website chat should use the same Perico Concierge logic.

Do not create separate website-only:

- Product prices
- Booking rules
- Cancellation rules
- Payment rules

Website presentation may differ.

Business truth remains shared.

---

# 29. WEBSITE BOOKING ASSISTANT

A website booking assistant may provide more structured interaction than chat.

Possible features:

- Product cards
- Date selector
- Participant selector
- Hotel selector
- Availability display
- Booking form
- Payment action
- Confirmation display

These are presentation capabilities.

The underlying transaction must still use canonical Perico engines.

---

# 30. SOCIAL MESSAGING

Social channels may include:

Instagram

Facebook Messenger

and future approved social messaging systems.

Customers should be able to:

- Ask product questions
- Receive recommendations
- Request quotes
- Begin booking

When the social channel cannot safely complete a required step, the transaction may continue through another approved Perico channel.

Do not redirect to a supplier.

---

# 31. EMAIL

Email may support:

- Quotes
- B2B communication
- Group requests
- Booking summaries
- Confirmation
- Vouchers
- Payment instructions
- Human follow-up

Email should preserve the same canonical booking and payment state.

---

# 32. PARTNER PORTAL

A partner portal may provide authenticated B2B access.

Possible functions:

- Product search
- Partner pricing
- Availability
- Booking
- Payment
- Voucher retrieval
- Booking history
- Commission reporting
- Modification request
- Cancellation request

Partner permissions remain controlled by:

identity-permissions-engine.md

and:

partner-reseller-engine.md

---

# 33. RESELLER PORTAL

Reseller portal behavior may differ from direct-customer channels.

The portal may expose authorized commercial information.

It must not expose:

- Supplier cost
- Another reseller's rates
- Another reseller's customers
- Unauthorized internal notes
- Secret credentials

---

# 34. STAFF INTERFACE

Perico staff may use an internal interface connected to the same architecture.

Possible functions:

- Review handoffs
- Check bookings
- Confirm availability
- Verify payments
- Resolve exceptions
- Approve special requests
- Apply authorized overrides
- Manage partners
- Review customer conversations

Staff permissions remain role-based.

---

# 35. VIRTUAL RESELLER CHANNELS

Virtual reseller agents may operate through:

- WhatsApp
- Website chat
- Social messaging
- Partner portal
- Other approved channels

The virtual reseller identity and the communication channel must remain separate.

Example:

agent_id = VR-001

channel = WHATSAPP

sales_source = VIRTUAL_RESELLER

---

# 36. MULTIPLE VIRTUAL RESELLERS

Multiple virtual reseller agents may operate simultaneously.

They must share the same:

- Product truth
- Pricing authority
- Availability logic
- Booking rules
- Payment rules
- Safety rules

They may differ in:

- Language
- Market
- Channel
- Product specialization
- Sales style
- Authorized customer segment

---

# 37. VIRTUAL RESELLER HANDOFF

When a virtual reseller requires human assistance:

Preserve:

- Customer
- Conversation
- Agent
- Channel
- Product
- Quote
- Booking
- Payment
- Reason for handoff

The human should continue without restarting the sale.

---

# 38. CHANNEL-SPECIFIC SALES STYLE

Channels may use different communication styles.

Example:

WhatsApp:
Short, natural, conversational.

Email:
Structured and complete.

Website:
Concise with interactive options.

B2B portal:
Operational and transactional.

Style may change.

Facts must not.

---

# 39. RESPONSE LENGTH

The Concierge should adapt response length to the channel and customer need.

Avoid sending unnecessarily long blocks through conversational channels when a shorter response would work.

Do not remove important:

- Restrictions
- Payment conditions
- Safety information
- Booking requirements

merely to shorten a message.

---

# 40. CUSTOMER QUESTIONS

Direct questions should receive direct answers.

Do not force customers through a scripted funnel when they ask a simple question.

Example:

Customer:
"Does this include transportation?"

Answer the question using verified product information.

Then continue naturally if appropriate.

---

# 41. SALES FLOW

The channel experience should support progression from:

DISCOVERY
→ INTEREST
→ QUOTE
→ AVAILABILITY
→ BOOKING INTENT
→ PAYMENT
→ CONFIRMATION

Do not force progression before the customer is ready.

---

# 42. BUTTONS AND QUICK REPLIES

When supported, buttons may simplify choices.

Examples:

CHECK AVAILABILITY

BOOK NOW

PRIVATE OPTION

SHARED OPTION

PAY DEPOSIT

SPEAK WITH PERICO

Buttons must trigger authorized actions.

Button labels must not falsely imply:

- Availability
- Reservation
- Payment success
- Confirmation

before those states exist.

---

# 43. "BOOK NOW" BUTTON

A BOOK NOW action means:

START OR CONTINUE BOOKING WORKFLOW.

It does not automatically mean:

BOOKING CONFIRMED.

---

# 44. "PAY NOW" BUTTON

A PAY NOW action means:

START APPROVED PAYMENT WORKFLOW.

It does not mean:

PAYMENT RECEIVED.

---

# 45. "CHECK AVAILABILITY" BUTTON

A CHECK AVAILABILITY action initiates:

availability-engine.md

It does not mean inventory is available.

---

# 46. CUSTOMER LOCATION

Some channels may provide location information.

Do not use location metadata to infer sensitive or unnecessary personal information.

Use customer location only when relevant to:

- Pickup
- Transfer
- Hotel
- Operational service

and permitted.

---

# 47. MEDIA

Customers may send:

- Hotel screenshot
- Flight screenshot
- Payment receipt
- Tour photo
- Voucher
- Booking confirmation
- Location image

Media may support the workflow.

Do not invent information that cannot be reliably established from the media.

---

# 48. VOICE NOTES

Voice notes may be converted into normalized customer intent when supported.

The system should preserve:

- Customer language
- Dates
- Numbers
- Names
- Hotel
- Product
- Participant information

Critical ambiguity must be clarified.

---

# 49. CHANNEL DELIVERY STATUS

Possible delivery states:

QUEUED

SENT

DELIVERED

READ

FAILED

UNKNOWN

Delivery status describes communication delivery.

It does not describe:

- Booking status
- Payment status
- Availability
- Confirmation

---

# 50. FAILED MESSAGE

If an outbound message fails:

Do not automatically assume the customer rejected the offer.

Possible actions:

- Retry when safe
- Use approved alternative channel when authorized
- Flag for Human Assistance when important

Do not spam the customer across multiple channels.

---

# 51. DUPLICATE MESSAGES

Provider retries or webhook duplication may produce duplicate events.

The system should avoid sending duplicate:

- Quotes
- Payment links
- Confirmations
- Cancellation notices
- Vouchers

when technically possible.

---

# 52. MESSAGE IDEMPOTENCY

Outbound transactional messages should use message identifiers or idempotency protection when supported.

This is especially important for:

- Payment requests
- Booking confirmations
- Cancellation notices
- Refund notices

---

# 53. CHANNEL TIMEOUT

A customer not responding does not automatically mean:

BOOKING CANCELLED.

Conversation inactivity and booking status are separate.

Any reservation expiration must follow the actual booking/payment rules.

---

# 54. SESSION EXPIRATION

Channel sessions may expire technically.

Technical session expiration must not delete:

- Booking
- Payment
- Customer record
- Partner attribution
- Confirmation

Persistent business state belongs outside the temporary channel session.

---

# 55. RE-ENTRY

A customer returning later should be able to continue when identity and context can be safely restored.

Example:

"Hi, I'm back about the Saona trip for Friday."

Use available verified context.

Do not unnecessarily restart discovery.

---

# 56. CUSTOMER OPT-OUT

Communication channels may have opt-out or messaging consent requirements.

Approved channel integrations should respect applicable messaging permissions.

Opting out of marketing does not automatically cancel an existing reservation.

Operational communication requirements should follow applicable policy.

---

# 57. MARKETING VS TRANSACTIONAL COMMUNICATION

Distinguish:

MARKETING

from:

TRANSACTIONAL

Examples of transactional communication:

- Booking update
- Pickup information
- Payment status
- Confirmation
- Operational change

Marketing permissions must not be assumed merely because a customer booked a tour.

---

# 58. TEMPLATE MESSAGES

Some channels may require approved templates.

Templates should use variables rather than hard-coded business facts where possible.

Example variables:

customer_name

product_name

date

pickup_time

booking_reference

amount_due

Templates must not contain outdated prices or policies.

---

# 59. CUSTOMER-FACING LINKS

Any link delivered through a channel must comply with:

global-rules.md

The Concierge must not send customers to:

- Supplier websites
- Supplier booking pages
- Supplier payment pages
- Competitor websites
- Unauthorized OTA pages
- Unauthorized marketplace pages

Approved Perico-controlled destinations may be used.

---

# 60. PAYMENT LINKS

Payment links delivered through any channel must come from:

payment-router.md

The Channel Layer must never invent or substitute payment destinations.

---

# 61. BOOKING LINKS

If Perico later uses customer-facing booking links, they must be explicitly approved.

The existence of an external booking URL inside an integration response does not authorize customer exposure.

---

# 62. HUMAN HANDOFF

Human handoff is controlled by:

human-handoff-engine.md

The Channel Layer must support:

HANDOFF REQUIRED
→ HANDOFF PREPARED
→ HANDOFF SUBMITTED
→ HUMAN ASSIGNED
→ HUMAN RESPONDED
→ RESOLVED
→ RETURNED TO AUTOMATION

when supported by the actual infrastructure.

---

# 63. HUMAN HANDOFF DELIVERY

Do not tell the customer:

"A team member is reviewing this"

unless the handoff was actually submitted or assigned according to the Human Handoff Engine.

If the system can only prepare the handoff:

Use accurate language.

---

# 64. HUMAN TAKEOVER

When a human takes control of a conversation:

Automation should avoid competing responses.

Possible state:

HUMAN_CONTROLLED

Automation may continue supporting the staff member internally if authorized.

---

# 65. RETURN TO AUTOMATION

After human resolution, the conversation may return to automation.

Preserve:

- Human decision
- Approved override
- Updated booking state
- Updated payment state
- Customer context

Do not make the customer repeat resolved information.

---

# 66. CHANNEL ESCALATION

A channel limitation may require moving the customer to another approved Perico channel.

Example:

Social DM cannot safely complete payment.

The customer may continue through an approved Perico payment or communication path.

This is not external supplier redirection.

---

# 67. CHANNEL SWITCH COMMUNICATION

When moving channels, explain only what the customer needs.

Example:

"I can continue the reservation with you on WhatsApp."

Do not expose internal architecture.

---

# 68. CHANNEL SECURITY

Channel adapters should validate provider events when supported.

Examples:

- Webhook signature
- Token
- Provider verification
- Authenticated session

Do not trust inbound system events merely because they resemble a valid payload.

---

# 69. SENSITIVE DATA

Do not request sensitive payment credentials through conversational channels.

Never request:

- Full card number
- CVV
- PIN
- Banking password
- Authentication code

Use approved secure payment infrastructure.

---

# 70. CUSTOMER PRIVACY

Do not expose one customer's:

- Booking
- Payment
- Phone
- Email
- Hotel
- Flight
- Special requests

to another customer.

Channel errors must not bypass Identity & Permissions.

---

# 71. PARTNER PRIVACY

Do not expose one partner's:

- Rates
- Commission
- Customers
- Bookings
- Payment terms
- Commercial agreement

to another partner.

---

# 72. INTERNAL INFORMATION

Do not expose through customer channels:

- Supplier costs
- Perico margins
- Internal commission
- Supplier contacts
- Integration credentials
- Internal routing logic
- Private operational notes

unless explicitly authorized for the actor.

---

# 73. CHANNEL ANALYTICS

Future analytics may track:

- Conversations
- Leads
- Quotes
- Bookings
- Conversion
- Response time
- Handoffs
- Revenue attribution
- Channel source
- Virtual reseller performance

Analytics must not change transaction truth.

---

# 74. CHANNEL ATTRIBUTION

Track separately where possible:

channel

sales_source

partner_id

agent_id

campaign

customer_id

booking_id

Example:

channel = INSTAGRAM

sales_source = VIRTUAL_RESELLER

agent_id = VR-004

booking_platform = BOKUN

payment_provider = APPROVED_PROVIDER

These are separate dimensions.

---

# 75. MULTI-CHANNEL DUPLICATE LEADS

The same customer may contact Perico through multiple channels.

Do not automatically create multiple customer records or multiple bookings.

When identity can be safely linked:

Merge or associate context according to approved data rules.

---

# 76. CONCURRENT CONVERSATIONS

A customer may have multiple active requests.

Example:

Saona booking

and

airport transfer

Do not mix:

- Dates
- Participant counts
- Payments
- Booking IDs

Maintain transaction-level context.

---

# 77. CONVERSATION VS TRANSACTION

One conversation may contain multiple transactions.

One transaction may span multiple conversations/channels.

Therefore:

conversation_id

must remain separate from:

quote_id

booking_id

payment_id

---

# 78. ERROR COMMUNICATION

Translate technical errors into useful customer communication.

Do not expose raw messages such as:

HTTP 500

API timeout

OAuth failure

Webhook signature error

Database exception

Use the actual business state.

If business state is unknown:

Say it is being verified through Perico's process.

Do not claim human review unless submitted.

---

# 79. CHANNEL FAILURE

If a channel provider fails:

Preserve business state outside the channel.

When service returns, the customer transaction should still exist.

Channel failure must not automatically:

- Cancel booking
- Reverse payment
- Remove availability
- Delete customer
- Lose partner attribution

---

# 80. PROVIDER REPLACEMENT

Perico should be able to replace a channel provider without rewriting the Concierge.

Example:

WHATSAPP
→ Provider A

later:

WHATSAPP
→ Provider B

The canonical channel remains WHATSAPP.

Only the adapter changes.

---

# 81. FUTURE VOICE CHANNEL

A future voice agent may connect through the same Channel Layer.

Voice must use the same:

- Product data
- Quote logic
- Availability logic
- Booking logic
- Payment logic
- Permissions
- Human handoff

Voice must not become a separate business brain.

---

# 82. FUTURE MOBILE APP

A future Perico mobile app may operate as another channel.

The application should use the same Concierge and transaction architecture.

Do not duplicate business rules inside the mobile application.

---

# 83. FUTURE PARTNER APPLICATION

A future agency/reseller application may use:

partner-reseller-engine.md

identity-permissions-engine.md

and the same Orchestrator.

Partner-specific presentation may differ.

Business truth remains centralized.

---

# 84. CHANNEL CONFIGURATION

Channel-specific configuration should eventually be stored separately from business policy.

Possible configuration:

channel_id

provider

credentials_reference

business_account

supported_features

message_limits

template_configuration

webhook_configuration

status

Do not hard-code these into product files.

---

# 85. TESTING

Each channel should be tested for:

- Inbound message
- Outbound message
- Language
- Context preservation
- Product recommendation
- Quote
- Availability
- Booking
- Payment delivery
- Confirmation
- Handoff
- Media
- Error handling

A successful text message alone does not prove the channel is ready for full transaction automation.

---

# 86. CHANNEL ACTIVATION

Before production activation, verify:

1. Integration is approved.
2. Authentication is secure.
3. Incoming messages normalize correctly.
4. Outgoing messages deliver correctly.
5. Identity behavior works.
6. Language works.
7. Context persists.
8. Payment links remain approved.
9. External website protection works.
10. Human handoff works.
11. Duplicate message protection works.
12. Business state survives channel failure.

---

# 87. HUMAN ASSISTANCE

Use:

human-handoff-engine.md

when:

- Channel cannot complete required action
- Identity cannot be verified
- Message content is critically ambiguous
- Media cannot be interpreted reliably
- Channel integration fails
- Customer requests a human
- Customer complaint requires staff
- Payment issue requires staff
- Booking issue requires staff
- Operational emergency requires staff

The channel should preserve all available context.

---

# 88. CUSTOMER REQUESTS HUMAN

If the customer clearly asks to speak with a person:

Do not trap them in automation.

Initiate the appropriate Perico Human Handoff when the infrastructure supports it.

Preserve conversation context.

---

# 89. AUTOMATION SHOULD NOT FIGHT THE CUSTOMER

The Concierge should not repeatedly force menus or automated questions when the customer is clearly communicating their need.

Understand natural language first.

Use structured controls only when they improve the experience.

---

# 90. FINAL CHANNEL VALIDATION

Before sending a customer-facing message, verify:

1. Correct conversation.
2. Correct customer/actor context.
3. Correct language.
4. Correct transaction.
5. Correct product.
6. Correct authorized price.
7. Correct availability state.
8. Correct booking state.
9. Correct payment state.
10. Correct confirmation state.
11. Correct data visibility.
12. Correct customer-facing link.
13. No supplier redirect.
14. No protected internal information.
15. No duplicate transactional message.
16. No invented business fact.

---

# 91. NON-NEGOTIABLE RULE

NEVER CONFUSE:

CHANNEL
WITH
CUSTOMER IDENTITY.

NEVER CONFUSE:

CHANNEL
WITH
SALES SOURCE.

NEVER CONFUSE:

CHANNEL
WITH
BOOKING PLATFORM.

NEVER CONFUSE:

CHANNEL
WITH
PAYMENT PROVIDER.

NEVER CREATE SEPARATE BUSINESS TRUTH
FOR EACH COMMUNICATION CHANNEL.

---

# 92. CORE PRINCIPLE

ONE PERICO CONCIERGE.

ONE PRODUCT TRUTH.

ONE TRANSACTION LOGIC.

WHATSAPP.

WEBSITE.

SOCIAL.

EMAIL.

PARTNER PORTALS.

STAFF INTERFACES.

FUTURE CHANNELS.

THE CHANNEL CHANGES.

THE PERICO BUSINESS BRAIN DOES NOT.