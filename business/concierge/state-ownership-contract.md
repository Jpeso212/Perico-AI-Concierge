# PERICO AI CONCIERGE — STATE OWNERSHIP CONTRACT

## 1. AUTHORITY

Each canonical state dimension has one owner. The Orchestrator coordinates requests and results; it does not maintain a competing lifecycle. Apply [global-rules.md](global-rules.md), [policy-authority-matrix.md](policy-authority-matrix.md) and [transaction-context-contract.md](transaction-context-contract.md) for guardrails, policy scope and evidence exchanges.

## 2. EXISTING STATE OWNERS

BOOKING STATE
owner → Booking Engine

PAYMENT STATE
owner → Payment & Confirmation Engine

AVAILABILITY STATE
owner → Availability Engine

HANDOFF STATE
owner → Human Handoff Engine

SESSION STATE
owner → Channel Layer

LEAD STATE
owner → Virtual Reseller Agent Layer

INTEGRATION TECHNICAL STATE
owner → Integration Registry

BRAND STATE
owner → Brand & Commercial Policy Layer

## 3. OWNER REFERENCES

- Booking: [booking-engine.md](booking-engine.md), including the CONFIRMED booking transition.
- Payment: [payment-confirmation-engine.md](payment-confirmation-engine.md), including payment-related confirmation eligibility.
- Availability: [availability-engine.md](availability-engine.md).
- Handoff: [human-handoff-engine.md](human-handoff-engine.md).
- Session: [channel-layer.md](channel-layer.md).
- Lead: [virtual-reseller-agent-layer.md](virtual-reseller-agent-layer.md).
- Integration technical state: [integration-registry.md](integration-registry.md).
- Brand: [brand-commercial-policy-layer.md](brand-commercial-policy-layer.md).

Canonical values and transition conditions remain in these documents. This contract does not repeat or extend their state enumerations.

## 4. TRANSITION BOUNDARY

Approved adapters normalize and authenticate external evidence. Authorized staff may supply scoped facts or approvals. Neither source directly changes another engine’s canonical state: the owner validates transaction scope, evidence, policy and transition requirements before recording the change.

Other engines read the authoritative result and must not independently reinterpret, promote, downgrade or overwrite it. Missing, stale, ambiguous or conflicting evidence requires the applicable verification or Human Handoff path. Duplicate and out-of-order events follow the Registry and transaction-context rules before owner validation.

Keep booking, payment, availability, handoff, session, lead, brand and integration technical state separate. Operational acceptance evidence and channel message delivery are separate from those states; an outage, expired session or failed message does not by itself cancel a booking or fail a payment.

CONFIRMED remains a booking state. Verified payment supplies payment evidence; resolved handoff supplies a handoff result. Neither alone creates booking confirmation.

Technical uncertainty, review flags and customer-facing wording are not additional canonical state values. Preserve the relevant owner’s state while resolving the actual uncertainty; do not create a generic transaction status that replaces all dimensions.
