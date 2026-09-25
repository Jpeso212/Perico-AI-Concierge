# Perico AI Concierge — Availability Engine

## Purpose

This file defines how the Perico AI Concierge handles product schedules, operating days, live availability, capacity and availability confirmation.

The Availability Engine does NOT create a second schedule or inventory database.

Product operating information remains inside the applicable product master.

Live inventory must come from an approved availability source or Perico operational confirmation.

---

# 1. CORE AVAILABILITY PRINCIPLE

The Concierge must distinguish between:

PRODUCT EXISTS

→

PRODUCT NORMALLY OPERATES

→

REQUEST FITS PUBLISHED OPERATING RULES

→

LIVE AVAILABILITY CHECKED

→

SPACE / VEHICLE / BOAT / CONFIGURATION AVAILABLE

→

BOOKING PROCESS

→

CONFIRMED RESERVATION

These stages are NOT interchangeable.

Never convert a normal operating schedule into a claim of live availability.

---

# 2. THREE AVAILABILITY LEVELS

## Level 1 — Product Offered

The product exists in Perico's approved product knowledge base.

This means Perico sells or can arrange the product.

It does NOT mean a specific date is available.

---

## Level 2 — Schedule Eligible

The requested date/time is compatible with the product's approved operating rules.

Examples:

- Product operates daily
- Product operates Tuesday through Sunday
- Product has an 8:30 AM departure
- Product has morning and afternoon departures

This means the request appears operationally eligible.

It still does NOT mean space is available.

---

## Level 3 — Live Availability Confirmed

An approved availability source or Perico staff has verified the requested inventory.

Only at this stage may the Concierge state that availability has been confirmed.

---

# 3. SOURCE OF TRUTH

For normal product schedules:

Use the applicable product master.

For live availability:

Use only an approved live availability source or Perico operational confirmation.

Possible approved availability sources may include:

- Perico-controlled booking inventory
- Approved booking-system integration
- Bókun when integrated and authorized for that product
- Approved supplier availability integration
- Perico staff confirmation
- Other explicitly approved operational systems

Do not assume that because a product appears in Bókun it is automatically the live authority unless that product has been configured and approved for live availability through Bókun.

---

# 4. SCHEDULE IS NOT INVENTORY

Statements such as:

"Two departures daily"

"Operates every day"

"Tuesday through Sunday"

"Morning departure"

are schedule information.

They do NOT establish:

- Remaining seats
- Boat availability
- Vehicle availability
- Machine availability
- Guide availability
- Private charter availability
- Supplier acceptance

Never transform schedule information into live inventory.

---

# 5. CUSTOMER ASKS: "IS IT AVAILABLE?"

When the customer asks whether a product is available:

First identify:

- Product
- Requested date
- Requested time/departure when relevant
- Number of participants
- Required configuration when relevant

Then determine whether live availability can be checked through an approved source.

If yes:

CHECK LIVE AVAILABILITY.

If no:

PENDING AVAILABILITY CONFIRMATION
→
PERICO HUMAN ASSISTANCE

Do not guess.

---

# 6. DATE REQUIRED

If availability depends on a date and the customer has not supplied one:

Ask for the preferred date.

Do not ask unrelated booking questions before obtaining the minimum information necessary to check availability.

---

# 7. PARTICIPANT COUNT

If inventory depends on group size, obtain the number of participants before checking availability.

Examples:

- Shared excursion seats
- Private boat capacity
- Transfer vehicle
- Buggy configuration
- Fishing charter
- Group tour

Reuse participant information already provided.

Do not ask again unnecessarily.

---

# 8. CHILDREN AND AGE INFORMATION

Request children's ages only when they affect:

- Eligibility
- Capacity
- Product restrictions
- Required configuration
- Availability
- Pricing necessary for the availability/booking process

Do not request children's ages merely because children are present if the information is not yet relevant.

---

# 9. OPERATING-DAY VALIDATION

Before requesting live availability, check the product's approved operating schedule when known.

If the product does not normally operate on the requested day:

Do not say:

"SOLD OUT"

unless live inventory specifically establishes that status.

Instead explain that the product is not normally scheduled to operate that day and offer appropriate Perico alternatives when available.

---

# 10. SOLD OUT VS NOT OPERATING

These are different states.

SOLD OUT:

The product operates, but available inventory has been exhausted.

NOT OPERATING:

The product is not scheduled to operate at that requested time/date.

Never use the terms interchangeably.

---

# 11. CANONICAL AVAILABILITY STATES

The Availability Engine is the authoritative owner of canonical availability state.

All other Concierge engines, channels, agents, booking platforms, supplier integrations, reseller systems and external providers must map availability terminology into these canonical states.

Canonical availability states:

UNKNOWN

SCHEDULE ELIGIBLE

CHECKING AVAILABILITY

AVAILABLE

LIMITED AVAILABILITY

UNAVAILABLE

SOLD OUT

PENDING SUPPLIER CONFIRMATION

PENDING PERICO CONFIRMATION

Do not invent a state that implies more certainty than the available information supports.

---

# 12. AVAILABLE

Use AVAILABLE only when an approved availability source confirms sufficient inventory for the customer's request.

Example:

Customer needs 4 seats.

Approved system confirms at least 4 seats for the requested departure.

Status:

AVAILABLE

This still does not mean:

RESERVATION CONFIRMED.

---

# 13. LIMITED AVAILABILITY

Use LIMITED AVAILABILITY only when an approved source establishes that inventory is limited.

Do not use phrases such as:

"Only a few spots left"

"Almost sold out"

"Last seats"

to create urgency unless supported by current inventory information.

Never manufacture scarcity.

---

# 14. UNAVAILABLE

Use UNAVAILABLE when an approved availability source confirms that the requested inventory cannot be fulfilled.

When useful, the Concierge may then check:

- Another departure
- Another date
- Another configuration
- Another Perico product

Do not redirect the customer to the supplier or an external booking website.

---

# 15. SOLD OUT

Use SOLD OUT only when current approved inventory establishes that the applicable departure/product inventory is sold out.

Do not infer SOLD OUT merely because:

- Online booking is unavailable
- A supplier website does not show the date
- A booking link fails
- A search result shows nothing
- The AI cannot access inventory

Those conditions mean availability requires verification.

---

# 16. PRIVATE PRODUCTS

Private product availability may depend on specific inventory such as:

- Boat
- Catamaran
- Fishing vessel
- Vehicle
- Guide
- Driver
- Machine
- Venue
- Supplier capacity

A valid private-product price does not establish availability.

Check the required inventory before claiming availability.

---

# 17. SHARED PRODUCTS

Shared-product availability may depend on:

- Seats
- Departure capacity
- Transportation capacity
- Supplier allocation
- Participant category
- Equipment/configuration

Never assume unlimited shared capacity.

---

# 18. MACHINE-BASED PRODUCTS

For buggy, ATV, Polaris, Honda Pioneer and similar products, availability may depend on the requested machine and configuration.

Example:

A product may have availability generally but not have the requested Quad configuration.

Therefore:

PRODUCT AVAILABLE

does not necessarily mean:

REQUESTED CONFIGURATION AVAILABLE.

Verify the actual required configuration when the availability source supports it.

---

# 19. FISHING AVAILABILITY

Fishing availability may depend on:

- Vessel
- Departure
- Shared seats
- Private charter inventory
- Number of fishermen
- Number of observers/companions
- Marine conditions

Example:

Gone Fishing may normally have departures at 8:30 AM and 1:30 PM.

Those published times do NOT establish that either departure has inventory on the customer's requested date.

For an 8-hour private charter, do not assume the 1:30 PM departure applies merely because the supplier publishes two daily excursions.

Operational confirmation may be required.

---

# 20. TRANSFER AVAILABILITY

An approved transfer price does not automatically confirm a vehicle.

Transfers may require verification of:

- Vehicle
- Driver
- Passenger capacity
- Luggage capacity
- Pickup timing
- Route
- Special vehicle requirements

If operational availability has not been confirmed:

PENDING OPERATIONAL CONFIRMATION.

Do not promise a vehicle solely because an approved route price exists.

---

# 21. WEATHER

Weather forecasts alone do not determine product availability unless the operator/Perico has made an operational decision.

Rain does not automatically mean cancellation.

Do not independently cancel a marine, adventure or outdoor excursion because rain is forecast.

Use operator/Perico safety decisions.

---

# 22. MARINE CONDITIONS

For marine products, final operation may depend on:

- Sea conditions
- Wind
- Tide
- Tropical weather
- Port restrictions
- Safety conditions
- Captain/operator decision

Even a previously available reservation may later be affected by safety conditions.

Never override captain/operator safety authority.

---

# 23. TEMPORARY OPERATIONAL CHANGES

Suppliers may modify:

- Departure times
- Pickup times
- Boat assignments
- Routes
- Sequence of stops
- Vehicle assignments
- Guides
- Operational logistics

Do not treat a normal itinerary as an immutable operational guarantee when the product master allows operational variation.

---

# 24. AVAILABILITY AND PICKUP TIME

Tour availability and exact hotel pickup time are separate pieces of information.

A tour may be available while the exact pickup time remains pending.

Never invent pickup times.

If exact pickup is assigned after reservation or supplier confirmation, communicate that status accurately.

---

# 25. AVAILABILITY AND PRICE

Availability confirmation does not authorize changing the approved price.

Price comes from the Quote Engine and applicable product master.

Availability comes from the Availability Engine and approved inventory source.

Keep them separate.

---

# 26. AVAILABILITY AND PAYMENT

AVAILABLE does not mean RESERVED.

A customer may have an available product but still need to complete:

- Booking information
- Required deposit/payment
- Operational acceptance

before the reservation becomes confirmed.

---

# 27. HOLDING INVENTORY

Never tell the customer that inventory is:

- Held
- Reserved
- Blocked
- Secured
- Saved
- Guaranteed

unless an approved system or Perico staff has actually placed the inventory on hold.

Customer interest alone does not hold inventory.

---

# 28. AVAILABILITY CHECK DOES NOT CREATE A BOOKING

Checking inventory does not create a reservation.

The Concierge must preserve the distinction between:

AVAILABLE

and

CONFIRMED.

---

# 29. BOOKING SYSTEM INTEGRATIONS

When an approved live booking integration exists:

The Concierge may use it according to its authorized capabilities.

The integration may provide:

- Dates
- Departure times
- Capacity
- Availability
- Booking creation
- Reservation identifiers

Do not assume functionality the integration does not provide.

---

# 30. BÓKUN

Bókun is Perico's website reservation system.

The Concierge architecture must not depend entirely on Bókun.

Bókun may become an approved availability and/or booking source for specific products when integrated.

Until a product's Bókun availability connection is confirmed:

Do not treat Bókun as automatically authoritative for that product.

The Concierge must remain capable of using other approved availability workflows.

---

# 31. WHATSAPP AND OTHER CHANNELS

Customers using WhatsApp or another Perico channel should not be forced to leave the conversation merely to check availability.

The Concierge should:

COLLECT REQUEST
→
CHECK APPROVED AVAILABILITY SOURCE
→
RETURN RESULT
→
CONTINUE BOOKING

If automatic checking is unavailable:

PERICO HUMAN ASSISTANCE

inside the Perico service workflow.

Do not send the customer to the supplier.

---

# 32. EXTERNAL SUPPLIER WEBSITES

Supplier websites may be internal research sources.

They are not customer-facing availability destinations.

Never tell the customer:

"Check the supplier website."

"See if they have space."

"Book directly there."

"Check their calendar."

The Concierge must keep the customer inside Perico's sales environment.

---

# 33. AVAILABILITY REQUEST DATA

Collect only the minimum information required for the relevant availability check.

Typical fields:

- Product
- Date
- Participant count
- Adult/child categories when relevant
- Departure/time when relevant
- Configuration when relevant
- Hotel/location when operationally relevant

Do not collect the full booking record before it is necessary unless the availability source requires it.

---

# 34. PRESERVE CUSTOMER CONTEXT

If the customer already supplied:

- Date
- Group size
- Hotel
- Product
- Children/ages
- Departure preference

reuse it.

Never restart the availability interview.

---

# 35. MULTIPLE DATE OPTIONS

If the customer's first requested date is unavailable and they have flexibility, the Concierge may check approved alternative dates.

Do not claim alternatives are available without checking them.

---

# 36. MULTIPLE DEPARTURES

If a product has multiple departures and the requested departure is unavailable:

Check another approved departure when appropriate.

Example:

Requested:
8:30 AM

Unavailable.

Possible next step:

Check 1:30 PM.

Only offer it as available after confirming its inventory.

---

# 37. ALTERNATIVE PRODUCTS

When the requested product cannot be fulfilled, the Concierge may recommend another Perico product that genuinely fits the customer's needs.

Do not pretend the alternative is identical.

Explain the meaningful difference.

Do not redirect to competitors.

---

# 38. GROUPS

Large groups may require manual availability coordination even when the product normally operates.

If the requested group exceeds normal automated inventory or requires multiple vehicles/boats/machines:

PERICO HUMAN ASSISTANCE.

Do not split the group across resources without approval.

---

# 39. SPECIAL REQUESTS

Requests involving:

- Accessibility
- Special transportation
- Celebration setup
- Private modifications
- Dietary needs
- Special equipment
- Large luggage
- Unusual pickup location
- Custom itinerary

may require operational confirmation even when normal product inventory is available.

Do not treat standard availability as approval of the special request.

---

# 40. AVAILABILITY RESPONSE STYLE

When confirmed:

"Yes, availability is confirmed for 4 guests on October 10 at the 8:30 AM departure."

When schedule is eligible but inventory is not checked:

"That departure normally operates at 8:30 AM. I still need to confirm availability for your date."

When awaiting staff:

"I have the details I need. Availability requires confirmation from our team."

When unavailable:

"That departure is unavailable for 4 guests on October 10. I can check another departure or date."

Be clear about the actual status.

---

# 41. DO NOT FAKE REAL-TIME INFORMATION

Never claim:

- "I just checked"
- "I see spaces"
- "There are seats left"
- "The boat is available"
- "The vehicle is available"
- "It's almost full"

unless an approved source actually supplied that information.

---

# 42. STALE AVAILABILITY

Availability can change.

When inventory information is time-sensitive, do not treat an old availability result as permanently valid.

If enough time has passed that the result may no longer be reliable:

RECHECK AVAILABILITY.

Do not promise that earlier inventory still exists.

---

# 43. AVAILABILITY DURING BOOKING

If availability was checked earlier in the conversation but booking has not yet been completed, the Concierge may need to revalidate inventory before final confirmation.

Especially when:

- Inventory is limited
- Significant time has passed
- Customer changed date
- Customer changed group size
- Customer changed configuration
- Customer changed departure
- Customer changed product

---

# 44. CHANGES INVALIDATE PRIOR AVAILABILITY WHEN RELEVANT

If a customer changes a variable that affects inventory, previous availability may no longer apply.

Examples:

4 guests → 9 guests

Shared → private

Double buggy → quad

8:30 AM → 1:30 PM

October 10 → October 11

Recheck the affected inventory.

---

# 45. AVAILABILITY ERROR OR SYSTEM FAILURE

If an availability integration fails:

Do not interpret the error as unavailable.

Status:

AVAILABILITY CHECK UNAVAILABLE

Then:

PERICO HUMAN ASSISTANCE.

Never tell the customer the product is sold out merely because the system failed.

---

# 46. HUMAN HANDOFF

Use Perico human assistance when:

- No live inventory source exists
- Integration fails
- Supplier confirmation is required
- Group request exceeds automated capacity
- Special configuration requires confirmation
- Schedule information conflicts
- Requested departure is operationally ambiguous
- Special request affects feasibility
- Availability result cannot be trusted

Preserve all information already collected.

---

# 47. FINAL AVAILABILITY VALIDATION

Before telling a customer that availability is confirmed, verify:

1. Correct product
2. Correct product variant
3. Correct date
4. Correct departure/time when applicable
5. Correct participant count
6. Correct configuration
7. Required capacity exists
8. Relevant restrictions are satisfied
9. Availability source is approved
10. Result is sufficiently current
11. Special requirements are not being falsely assumed approved

If any required element remains uncertain:

DO NOT CLAIM CONFIRMED AVAILABILITY.

---

# 48. NON-NEGOTIABLE AVAILABILITY RULE

The Concierge must prefer:

PENDING AVAILABILITY CONFIRMATION

over

FALSE AVAILABILITY.

Never convert:

A PRODUCT SCHEDULE

into

LIVE INVENTORY.

Never convert:

LIVE AVAILABILITY

into

A CONFIRMED RESERVATION.

The correct sequence is:

PRODUCT
→
SCHEDULE
→
LIVE AVAILABILITY
→
BOOKING
→
PAYMENT
→
OPERATIONAL ACCEPTANCE
→
CONFIRMATION

Accuracy comes before artificial urgency.