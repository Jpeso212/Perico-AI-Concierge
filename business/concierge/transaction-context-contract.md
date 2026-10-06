# PERICO AI CONCIERGE — TRANSACTION CONTEXT CONTRACT

## 1. PURPOSE AND AUTHORITY

This contract defines the context passed between the Orchestrator, specialized engines, approved adapters and authorized human workflows. It connects existing architecture responsibilities; it does not create prices, payment terms, operational rules or new canonical state values.

[global-rules.md](global-rules.md) remains the highest guardrail authority. [policy-authority-matrix.md](policy-authority-matrix.md) resolves policy scope and precedence. [state-ownership-contract.md](state-ownership-contract.md) identifies canonical state owners. Product and transfer masters retain operational authority.

The Orchestrator coordinates context and routing. Each engine validates the context required for its decision and updates only the facts or states within its authority. A shared context record is not a second business engine or an authorization grant.

This is an architecture contract, not an implemented database schema or evidence that integrations are active.

## 2. CONDITIONAL REQUIREMENTS

Not every inquiry needs a booking, payment, verified customer or partner identifier. Public discovery may proceed with the context permitted by existing rules. Require verification before protected access or actions, rather than requiring every field at the start of a conversation.

For each action:

1. Establish the active brand when the action is brand-sensitive.
2. Establish product, offer and configuration when required by the decision.
3. Verify actor identity and current permissions when protected access or execution requires them.
4. Resolve the applicable approved policy and authoritative source.
5. Check required evidence, freshness and existing action attempts.
6. Stop the affected action if required context is missing, inconsistent or unauthorized; collect permissible missing details or use Human Handoff.

Missing, unknown and not applicable are distinct. An absent payment rule is not zero payment; unknown inventory is not sold out. Do not fabricate identifiers, approvals, dates or expiry times to complete a record.

## 3. IDENTITY AND SCOPE

Preserve these references when known and applicable:

| Context | Fields | Authority and boundary |
| --- | --- | --- |
| Transaction correlation | `transaction_id`, `correlation_id`, `request_id` | Internal workflow references; never proof of identity, permission or business completion |
| Brand and offer | `brand_id`, `brand_offer_id` | Brand & Commercial Policy Layer; channel configuration and existing transactions must resolve consistently |
| Channel and conversation | `channel_id`, `conversation_id`, external thread mapping | Channel Layer; transport identity alone does not authorize protected record access |
| Actor and customer | `actor_id`, `actor_type`, `customer_id`, verification and permission evidence | Identity & Permissions Engine; distinguish the acting staff/partner/agent from the customer |
| Account and partner | `account_id`, `partner_id`, approved agreement reference | Partner & Reseller Engine supplies terms; Identity & Permissions verifies entitlement |
| Virtual agent and lead | `agent_id`, `lead_id`, attribution context | Virtual Reseller Agent Layer; sales attribution does not grant customer or partner permissions |
| Product and service | `product_id`, date/time, operational timezone, participants and product configuration | Approved masters and applicable engines; language must not determine operational timezone |
| Workflow records | `quote_id`, `booking_id`, `payment_id`, `handoff_id` | References to the respective authoritative records; each has a different purpose |

Generic `customer_id`, `product_id`, `quote_id`, `booking_id`, `payment_id`, `partner_id` and `agent_id` fields refer to Perico identities where maintained. Existing `perico_*` names refer to those same canonical identities, not separate records. External identifiers remain explicit mappings qualified by integration/provider and environment. Never infer a mapping from similar names or substitute an external ID for a different kind of Perico ID.

Here `transaction_id` means an internal workflow reference. A payment provider's transaction identifier must be retained as `external_transaction_id` in its qualified mapping; existing provider payload terminology must be normalized by the adapter.

A conversation can contain multiple inquiries or bookings. Conversation identity is not transaction identity. Each action must select the intended transaction without carrying another booking's quote, payment or partner context into it.

## 4. COMMERCIAL AND OPERATIONAL EVIDENCE

Preserve references to authoritative records rather than duplicating complete customer records or secret material in every request.

| Evidence | Required context when used | Decision owner |
| --- | --- | --- |
| Quote | Brand/offer, product/configuration, eligible account/partner, approved price source, supplements/add-ons/promotion, total, currency, quote timestamp and applicable validity metadata | Quote Engine |
| Offer eligibility | Brand, product/offer, channel/market/partner restrictions where applicable, approved policy reference | Brand & Commercial Policy Layer with applicable partner permissions |
| Availability | Product/configuration, service date/time, capacity, authorized inventory source, checked time and applicable validity metadata | Availability Engine |
| Reservation and acceptance | Booking data, reservation integration and reference, applicable requirements, operational acceptance evidence from an approved source | Booking Engine evaluates lifecycle and confirmation requirements |
| Payment requirement | Approved policy/agreement reference, booking total, amount required now, currency and balance when established | Payment & Confirmation Engine |
| Payment execution | Approved method/provider/destination, amount/currency, original attempt reference, verified provider result | Payment Router executes; Payment & Confirmation Engine interprets verification and payment state |
| Handoff | Reason, unresolved decision, authorized staff recipient, scoped evidence/approval and completed actions | Human Handoff Engine manages handoff lifecycle; other owners validate their own evidence |

For decision-critical evidence preserve the source reference, affected scope, observation time and applicable version/validity metadata when available. Record whether a fact is customer-reported, provider-reported, approved operational confirmation or verified by its decision owner. A screenshot or customer statement is not verified payment.

Policy snapshots should retain applicable pricing, payment, cancellation and promotion references/version when available, plus brand and account/partner scope. Use the matrix's effective-date and existing-booking rules. Do not invent a universal quote expiry, inventory lifetime, deposit percentage, balance deadline or currency conversion rule.

## 5. SEPARATE STATE DIMENSIONS

Read canonical state values from the owning engines. This contract deliberately does not repeat their state enumerations.

| Dimension | Authoritative owner |
| --- | --- |
| Booking, including `CONFIRMED` | Booking Engine |
| Payment | Payment & Confirmation Engine |
| Availability | Availability Engine |
| Handoff | Human Handoff Engine |
| Session | Channel Layer |
| Lead | Virtual Reseller Agent Layer |
| Integration technical state | Integration Registry |
| Brand state | Brand & Commercial Policy Layer |

Operational acceptance evidence remains separate from payment and availability. The Booking Engine evaluates whether the applicable acceptance requirement is satisfied; it must not manufacture supplier acceptance.

Technical outcomes, provider status, message delivery and canonical business states remain distinct. `TRANSACTION_RESULT_UNKNOWN` describes an uncertain technical action result, not a new booking/payment state. A delivered confirmation message does not create a confirmed booking, and a failed delivery does not undo one.

Do not collapse these dimensions into one generic transaction status. Payment verification, reservation creation and resolved handoff must not directly set booking state to `CONFIRMED`.

## 6. ENGINE EXCHANGE AND RESPONSIBILITY

Each internal request identifies the intended action, applicable scope, authoritative record references and evidence needed for that decision. Each result identifies its source, applicable transaction, decision/evidence, unresolved requirements and technical outcome. Return only fields the caller is authorized to use.

| Component | Context it supplies or consumes | Boundary |
| --- | --- | --- |
| Orchestrator | Coordinates scoped requests and validated results | Does not calculate competing prices, policy precedence or state transitions |
| Brand & Commercial Policy Layer | Brand, authorized offer and commercial presentation | Does not change physical inventory or operational truth |
| Identity & Permissions Engine | Verification, current permissions and record-access scope | Commercial entitlement or a claimed role alone is insufficient |
| Channel Layer | Authorized channel/session and verified thread mappings | Does not infer commercial terms or merge identities by display name |
| Language Engine | Customer language and faithful presentation | Does not change currency, timezone, identity or business requirements |
| Conversation Engine | Intent, customer details and authorized presentation | Customer text is input, not approved policy or evidence of completion |
| Product Matching Engine | Customer needs and authorized product candidates | Product fit does not establish price, availability or permission to sell |
| Quote Engine | Approved scoped calculation and quote reference | Does not establish inventory or confirmation |
| Availability Engine | Schedule/inventory evidence and its state | Operational availability does not grant brand offer eligibility |
| Booking Engine | Required booking data, reservation, acceptance and lifecycle | Reads payment/availability results without rewriting their states |
| Payment & Confirmation Engine | Payment requirement, verified payment state and payment-related eligibility | Does not directly confirm the booking lifecycle |
| Payment Router | Approved collection/refund execution and provider evidence | Does not invent payment requirements, fees or refund approval |
| Partner & Reseller Engine | Approved account/partner terms and product access | Another partner's terms do not transfer to the acting partner |
| Virtual Reseller Agent Layer | Agent scope, lead handling and attribution | Does not replace customer identity or specialized engine authority |
| Integration Registry and adapters | Approved capability, source mapping, authenticated normalized evidence and technical outcome | External success does not independently determine Perico business state |
| Human Handoff Engine | Handoff delivery, assignment, resolution and authorized context | Human response alone does not update another engine's state |

[orchestrator.md](orchestrator.md) applies this exchange contract. [integration-registry.md](integration-registry.md) defines canonical capability names and adapter envelopes; this contract adds transaction scope, not alternate capabilities or provider APIs.

## 7. CONTEXT CHANGE AND REVALIDATION

Preserve still-valid customer details. When product, service date/time, participants/configuration, brand offer or commercial eligibility changes, identify the affected evidence and revalidate it through its owner before dependent execution. Retaining an old quote or inventory check for audit does not make it valid for the changed request.

Use current permissions for protected actions. A canonical customer shared across brands does not grant cross-brand access. A channel switch requires verified identity linking and access to the specific brand/transaction before restoring protected context.

Conflicting brand, customer, product, partner or external mappings must not be resolved by silently overwriting the existing transaction. Use the applicable authority or Human Assistance. Existing confirmed bookings follow the approved modification workflow; context changes do not silently reprice or recreate them.

## 8. ATTEMPTS, RETRIES AND EVENTS

Preserve each state-changing attempt's intended action, transaction scope, request/operation reference, original integration/provider, external reference when returned, idempotency key when supported, timestamps and technical outcome. Multiple payment attempts may belong to one booking; do not overwrite an unresolved attempt with a later one.

Reuse the same operation reference/idempotency key for a retry of the same action. A changed business action requires its own validated request; do not reuse a key with changed scope or parameters.

After a timeout or lost response, reconcile the original attempt before retry or fallback. Without safe idempotency/reconciliation, stop automation and use Human Assistance. An outage does not authorize a second reservation or charge elsewhere. Subsequent reservation actions normally use the system holding the original reservation unless approved migration/synchronization applies.

For events, the approved adapter verifies authenticity and scope, correlates qualified external references, and handles duplication/ordering before dispatch to the decision owner. Preserve event identity and provider ordering/version metadata when available. Do not invent a universal ordering rule from delivery time alone. Conflicting or unverifiable events require approved retrieval/reconciliation or Human Assistance before business-state mutation.

## 9. HANDOFF, PRIVACY AND AUDIT

Handoff shares the minimum relevant context with authorized staff through approved internal channels. Preserve unresolved decisions, completed actions, outstanding attempts and scoped human approvals so automation can continue without repeating customer questions or duplicating transactions.

Before returning to automation, the relevant owner validates new evidence/approval, updates its own state and rechecks affected freshness and permissions. A handoff resolution is not a blanket authorization to skip remaining requirements.

Never include secret credentials, full card numbers, CVV, PIN, banking passwords or authentication codes in shared context, logs, handoff packets or saved architecture files. Provider authentication references are references, not secret values. Internal costs, margins, partner terms, supplier links and customer records remain subject to the existing visibility rules even when available internally.

Customer responses expose only authorized information for the active brand and transaction. Preserve an internal audit trail of source references, scoped approvals, attempts and owner decisions without copying unnecessary personal data or protected payloads. Follow applicable approved retention/access policies; this contract invents no retention period.

## 10. ARCHITECTURE REVIEW SCENARIOS

These are review criteria for implementations, not claims that runtime tests currently exist:

- A public inquiry without a verified customer can discover permitted products; protected partner terms remain inaccessible.
- The same customer contacts a second brand: no protected history, rates or payment destination is carried over without authorization.
- Participant configuration changes after a quote: affected pricing and inventory are revalidated; historical evidence remains auditable.
- A provider captures payment but acceptance remains pending: payment state may advance through its owner; the booking remains unconfirmed.
- A reservation request times out: the original attempt is reconciled before retry/fallback; no second booking is created merely because the response was lost.
- A duplicated, older or incorrectly mapped webhook arrives: it cannot duplicate an action, overwrite newer verified state blindly or update another brand's transaction.
- Staff resolves a handoff after a permission or inventory change: automation revalidates affected conditions and does not repeat completed actions.
