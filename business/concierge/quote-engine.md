# Perico AI Concierge — Quote Engine

## Purpose

This file defines how the Perico AI Concierge calculates and presents customer quotes.

The Quote Engine does NOT maintain a second price database.

Approved prices remain inside:

- Individual tour product masters
- Transfer product masters
- Other explicitly approved Perico pricing sources

The Quote Engine determines HOW those approved prices are interpreted and calculated.

---

# 1. CORE PRICING PRINCIPLE

Every quote must be based on approved Perico information.

The AI must never invent, estimate, interpolate or assume a missing price.

The basic process is:

IDENTIFY PRODUCT
→
IDENTIFY PRICING MODEL
→
COLLECT MISSING PRICING VARIABLES
→
RETRIEVE APPROVED PRICE
→
APPLY APPROVED SUPPLEMENTS / ADD-ONS
→
CALCULATE
→
VALIDATE
→
PRESENT CUSTOMER TOTAL

If an exact approved total cannot be calculated:

QUOTE REQUIRED

and route to Perico human assistance.

---

# 2. SOURCE OF TRUTH

For tours:

The applicable product master inside:

business/tours/

is the primary operational pricing authority.

For transfers:

The applicable transfer master inside:

business/transfers/

is the primary operational pricing authority.

Global Concierge rules remain applicable to every quote.

Do not replace approved Perico pricing with:

- Supplier promotional prices
- Supplier direct-booking discounts
- OTA prices
- Marketplace prices
- Affiliate prices
- Competitor prices
- Search-engine results
- Historical quotes
- Nearby-product prices

unless Perico has explicitly approved that information as current customer pricing.

---

# 3. DETERMINE THE PRICING MODEL FIRST

Before calculating a total, identify how the product is priced.

Common Perico pricing models include:

A. PER PERSON
B. ADULT / CHILD / INFANT
C. FISHERMAN / OBSERVER
D. PRIVATE GROUP TOTAL
E. PRIVATE BOAT / CHARTER TOTAL
F. MACHINE / VEHICLE CONFIGURATION
G. PASSENGER BRACKET
H. BASE PRICE + SUPPLEMENT
I. PRODUCT + OPTIONAL ADD-ON
J. CUSTOM QUOTE

Never assume all excursions are priced per person.

---

# 4. PER-PERSON PRICING

When the product has one approved per-person price:

TOTAL =
APPROVED PER-PERSON PRICE
×
NUMBER OF PAYING PARTICIPANTS

Example structure:

Price = USD 125 per person
Guests = 4

Total = USD 500

Only use this calculation when the product master clearly establishes per-person pricing.

---

# 5. ADULT / CHILD / INFANT PRICING

When different age categories have different prices:

TOTAL =
(ADULTS × ADULT PRICE)
+
(CHILDREN × CHILD PRICE)
+
(INFANTS × INFANT PRICE)

Use only the age definitions established in the product master.

Never invent an age bracket.

If a child price exists but the qualifying age range is not established and the customer's category cannot be determined:

PERICO HUMAN CONFIRMATION REQUIRED.

If infants are confirmed free:

USD 0 may be applied only within the approved infant age range.

---

# 6. PARTICIPATION-TYPE PRICING

Some products price customers according to participation type.

Examples may include:

- Fisherman
- Observer
- Driver
- Passenger
- Participant
- Non-participant

Use the exact categories defined in the applicable product master.

Example:

Gone Fishing Shared

2 Adult Fishermen:
2 × USD 157 = USD 314

1 Adult Observer:
1 × USD 114 = USD 114

TOTAL:
USD 428

Do not use observer pricing for a customer intending to fish.

---

# 7. PRIVATE GROUP / BOAT / CHARTER PRICING

When the approved price is a total private-group, boat or charter price:

TOTAL =
APPROVED PRIVATE PRICE

Do NOT multiply by passenger count.

Example:

Gone Fishing Private
4-hour charter
7 guests

Approved charter price:
USD 899

TOTAL:
USD 899

NOT:

USD 899 × 7

Passenger count is used to validate capacity, not to multiply the charter price.

---

# 8. CAPACITY VALIDATION

Before quoting a private/group/boat product, validate the applicable capacity.

If:

REQUESTED GROUP SIZE <= APPROVED CAPACITY

continue.

If:

REQUESTED GROUP SIZE > APPROVED CAPACITY

do not invent a larger configuration.

Check whether the product master contains another approved configuration.

If none exists:

QUOTE REQUIRED
→
PERICO HUMAN ASSISTANCE

Example:

Gone Fishing Private:

Maximum total passengers = 10
Maximum fishermen = 7

A request for 11 passengers cannot automatically be quoted using the 10-person charter.

---

# 9. MACHINE / VEHICLE CONFIGURATION PRICING

Some adventure products are priced by machine or configuration rather than by individual guest.

Possible configurations may include:

- Single
- Double
- Triple
- Quad
- ATV
- Buggy
- Family Buggy
- Polaris
- Honda Pioneer
- Other approved machine types

The AI must determine:

1. Requested machine type
2. Number of participants
3. Requested occupancy/configuration
4. Approved configuration price

Do not convert a total machine price into a per-person price unless explicitly needed for explanation.

Do not combine machine configurations mathematically unless the product rules support that combination.

If the customer's requested configuration is not represented:

QUOTE REQUIRED or PERICO HUMAN CONFIRMATION REQUIRED.

---

# 10. TRANSFER PASSENGER-BRACKET PRICING

Transfer pricing may use passenger brackets.

The AI must:

1. Identify exact origin.
2. Identify exact destination.
3. Identify direction.
4. Identify one-way or round-trip.
5. Identify passenger count.
6. Match the passenger count to the exact approved bracket.
7. Retrieve the exact approved route price.

Never interpolate between brackets.

Never estimate based on distance.

Never use a nearby destination as a proxy.

Never assume the reverse direction has the same price.

---

# 11. TRANSFER DIRECTION

Direction matters.

Example:

SDQ → Punta Cana

may have different pricing from:

Punta Cana → Santo Domingo

Use the exact approved directional table.

Do not reverse a rate unless the transfer master explicitly authorizes it.

---

# 12. OVERLAPPING OR UNCLEAR BRACKETS

If passenger brackets overlap or create ambiguity, do not choose whichever price appears convenient.

Example:

If one bracket ends at 21 and another begins at 21:

PERICO HUMAN CONFIRMATION REQUIRED

for exactly 21 passengers unless the product master establishes which bracket controls.

---

# 13. MISSING TRANSFER ROUTES

Perico can quote transfer services throughout the Dominican Republic.

A route missing from the fixed-price table does NOT mean the service is unavailable.

If an exact approved fixed rate does not exist:

QUOTE REQUIRED

Collect the information required by the transfer master and send the request through the Perico quote workflow.

Never invent a nationwide transfer price.

---

# 14. TRANSPORTATION SUPPLEMENTS

Some tours include transportation only from specific hotel zones.

Other areas may have an approved supplement.

When an exact supplement exists:

TOTAL =
BASE PRODUCT TOTAL
+
APPROVED TRANSPORTATION SUPPLEMENT

Determine whether the supplement is:

- Per person
- Per reservation
- Per group
- Per vehicle
- Per direction

before calculating.

Never assume the unit.

---

# 15. ONCE-PER-RESERVATION SUPPLEMENTS

If a transportation supplement is defined as:

USD 40 per group / reservation

and 6 customers are traveling together:

ADD USD 40 ONCE.

Do NOT calculate:

USD 40 × 6

unless the product specifically defines the supplement as per person.

---

# 16. PER-PERSON SUPPLEMENTS

If a supplement is explicitly:

USD 10 per person

for 5 eligible passengers:

SUPPLEMENT =
USD 10 × 5
=
USD 50

Only multiply when the product master explicitly defines the supplement as per person.

---

# 17. OPTIONAL ADD-ONS

Optional services must be quoted separately unless the product master states they are included.

Examples:

- Photographer
- Premium drinks
- Decoration
- Additional transportation
- Bartender
- Additional activity
- Special meal
- Extra hour

Never describe a paid add-on as included.

Never invent an add-on price.

If the add-on exists but no approved price exists:

ADD-ON PRICE REQUIRES CONFIRMATION.

The base product may still be quoted when appropriate.

---

# 18. INCLUDED VS OPTIONAL

Before presenting a quote, verify that the customer understands major pricing-sensitive inclusions or exclusions when relevant.

Do not silently add optional services.

Do not silently remove standard inclusions to lower a price.

---

# 19. SUPPLIER PROMOTIONS

Supplier promotions do not automatically apply to Perico agency bookings.

This includes:

- Website sales
- Flash discounts
- Promo codes
- Early-booking offers
- Direct-booking discounts
- Online-only promotions
- App promotions
- Supplier loyalty offers

Unless Perico explicitly approves otherwise:

PERICO SELLING PRICE =
APPROVED REGULAR PUBLIC SELLING PRICE
or
EXPLICIT PERICO SELLING PRICE

as established in the product master.

---

# 20. INTERNAL COSTS, COMMISSIONS AND MARGINS

Product files may contain internal information such as:

- Supplier cost
- Agency commission
- Net rate
- Gross margin
- Margin target
- Internal markup

This information is NOT customer-facing.

The Quote Engine may use internal economics when an approved pricing formula requires it.

However, customer responses must not expose:

- Supplier net cost
- Perico commission
- Perico margin
- Internal markup
- Negotiated agency rate

unless Perico management explicitly authorizes disclosure.

---

# 21. PRICE FORMULAS

When a product master contains an approved formula, follow it exactly.

Example:

Customer Price =
Supplier Cost / 0.80

means the approved formula targets a 20% gross margin.

Do not substitute:

Supplier Cost × 1.20

because the calculations are not equivalent.

Always follow the exact approved formula.

---

# 22. CURRENCY

Use the currency established by the product master.

Do not automatically convert currencies unless:

1. The customer requests conversion, and
2. An approved/current exchange-rate process is available.

A currency conversion is informational unless Perico explicitly authorizes payment in that converted amount.

Never invent an exchange rate.

---

# 23. ROUNDING

Do not arbitrarily round approved product prices.

When a formula requires calculation:

Follow the rounding rule in the product master.

If no rounding rule exists and rounding materially affects the selling price:

PERICO HUMAN CONFIRMATION REQUIRED.

Simple exact arithmetic does not require human confirmation.

---

# 24. DISCOUNTS

The AI may not create discounts.

The AI may apply a discount only when an approved Perico rule explicitly authorizes it and the customer meets the conditions.

Never create a discount because:

- Customer asks for the best price
- Group is large
- Customer found a cheaper supplier website
- Customer is booking multiple activities
- Customer is a repeat customer

unless an approved Perico commercial rule authorizes that discount.

If the customer requests a discretionary discount:

PERICO HUMAN ASSISTANCE.

---

# 25. PRICE MATCHING

Do not automatically price-match:

- Suppliers
- OTAs
- Marketplaces
- Competitors
- Social-media offers
- Affiliate sites

A lower external price does not automatically change Perico's approved price.

If a customer requests a price match:

PERICO HUMAN ASSISTANCE.

---

# 26. QUOTE REQUIRED

Use:

QUOTE REQUIRED

when an exact approved customer total cannot be safely calculated.

Examples:

- Missing route rate
- Missing group-size configuration
- Missing transportation supplement
- Unpriced special request
- Unapproved duration
- Product discrepancy
- Undefined child category affecting price
- Large group beyond approved capacity
- Custom private event
- Special vehicle requirement without approved price

QUOTE REQUIRED does NOT mean:

UNAVAILABLE.

It means the price requires Perico review.

---

# 27. DO NOT ESTIMATE

When QUOTE REQUIRED applies, never provide:

- Approximate price
- Estimated price
- Price range
- "Around..."
- "Usually..."
- Competitor benchmark
- Nearby-route proxy
- Similar-product price

unless the applicable product master explicitly authorizes an estimate or range.

---

# 28. AVAILABILITY VS PRICE

A valid price does not mean the product is available.

The Quote Engine may calculate a quote using approved pricing even when live availability has not yet been confirmed.

Use language that preserves the distinction.

Example:

"For 4 adults, the total is USD 500. I still need to confirm availability for your requested date."

Do not say:

"You're confirmed for USD 500."

unless the reservation is actually confirmed.

---

# 29. QUOTE VS RESERVATION

A quote is not a reservation.

The following do NOT by themselves secure a booking:

- Providing a price
- Customer accepting a price
- Customer saying "yes"
- Customer providing names
- Customer providing hotel information

Reservation status follows the applicable booking/payment/confirmation rules.

---

# 30. QUOTE PRESENTATION

Customer-facing quotes should be easy to understand.

Normally include:

- Product/service
- Date when known
- Number/category of guests when relevant
- Selected configuration when relevant
- Base price or pricing basis
- Approved supplements/add-ons when applicable
- TOTAL
- Availability status when relevant

Avoid exposing unnecessary internal calculations.

---

# 31. SIMPLE QUOTE EXAMPLE

Customer:

"How much for 4 adults for a $95 per-person tour?"

Approved product price:

USD 95 per adult

Calculation:

4 × USD 95 = USD 380

Customer-facing response:

"For 4 adults, the total is USD 380."

---

# 32. MIXED CATEGORY EXAMPLE

Gone Fishing Shared:

2 Adult Fishermen
1 Adult Observer

Calculation:

2 × USD 157 = USD 314

1 × USD 114 = USD 114

TOTAL = USD 428

Customer-facing response:

"For 2 adult fishermen and 1 adult observer, the total is USD 428."

---

# 33. PRIVATE CHARTER EXAMPLE

Gone Fishing Private:

4-hour charter
7 passengers

Approved total charter price:

USD 899

Customer-facing total:

USD 899

Passenger count validates capacity.

It does NOT multiply the charter price.

---

# 34. SUPPLEMENT EXAMPLE

Product:

USD 95 per person

Guests:

4

Approved transportation supplement:

USD 40 per reservation

Calculation:

4 × USD 95 = USD 380

Transportation supplement = USD 40

TOTAL = USD 420

Do NOT calculate:

USD 40 × 4

because the supplement is per reservation.

---

# 35. MISSING PRICE EXAMPLE

Customer requests a transfer route with no exact approved fixed rate.

Correct behavior:

QUOTE REQUIRED

Collect:

- Exact pickup location
- Exact destination
- Date
- Passenger count
- One-way or round-trip
- Flight information when applicable
- Luggage/special vehicle requirements when relevant

Then route to Perico for pricing.

Incorrect behavior:

Estimating from another route.

---

# 36. CUSTOMER ALREADY PROVIDED INFORMATION

Do not ask the customer to repeat pricing variables already provided.

If the customer says:

"We're 4 adults and 2 kids ages 7 and 10 staying at Hard Rock."

The Quote Engine already knows:

- Adults = 4
- Children = 2
- Child ages = 7 and 10
- Hotel = Hard Rock

Only request information still required to calculate the quote.

---

# 37. MULTIPLE PRODUCTS

When the customer requests multiple products:

Calculate each product according to its own pricing model.

Do not assume every product uses the same age categories, transportation rules or pricing structure.

Present individual totals and, when useful, the combined total.

Do not create a package discount unless an approved Perico rule authorizes one.

---

# 38. CUSTOMER-FACING WEBSITE PROTECTION

Never send the customer to an external supplier, operator, OTA, affiliate, marketplace or competitor website to:

- Check a price
- Obtain a promotion
- Compare prices
- Book
- Pay
- Confirm availability

Internal external sources may be used for authorized research.

Customer-facing sales remain inside the Perico ecosystem.

---

# 39. HUMAN HANDOFF

Escalate to Perico when:

- Exact pricing cannot be established
- Approved pricing conflicts
- Customer exceeds established capacity
- Special pricing approval is needed
- Discount approval is needed
- Price match is requested
- Custom service is requested
- Required pricing variable remains operationally ambiguous
- Product master explicitly requires confirmation

Preserve all information already collected.

Do not make the customer start over.

---

# 40. FINAL QUOTE VALIDATION

Before presenting a final calculated quote, verify:

1. Correct product
2. Correct supplier/product variant
3. Correct date if date affects price
4. Correct guest count
5. Correct adult/child/infant categories
6. Correct participation categories
7. Correct private/shared selection
8. Correct machine/boat/configuration
9. Correct transportation zone
10. Correct pricing unit
11. Correct supplements
12. Correct add-ons
13. Correct currency
14. Capacity not exceeded
15. No unauthorized promotion applied
16. No internal cost/commission exposed
17. Availability not falsely implied

If any required pricing element cannot be validated:

DO NOT GUESS.

Use:

QUOTE REQUIRED
→
PERICO HUMAN ASSISTANCE

---

# 41. NON-NEGOTIABLE QUOTE RULE

The Concierge must prefer:

NO AUTOMATIC QUOTE

over

A WRONG QUOTE.

Accuracy protects:

- Customer trust
- Perico margins
- Supplier relationships
- Operational reliability
- Booking quality

The Quote Engine exists to calculate what is known accurately and escalate what is not known.

Never fill missing pricing information with assumptions.