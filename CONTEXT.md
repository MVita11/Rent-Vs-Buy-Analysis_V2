Project: Rent-Vs-Buy Analysis (UK)

Overview
--------
A UK-focused rent-vs-buy decision assistant aimed at first-time homebuyers and first-time renters. The tool provides clear, UK-specific financial calculations and a simple recommendation (rent vs buy) for multiple planning horizons (5, 10, 15, 20, 25 years). An AI assistant explains results in plain English, flags unrealistic inputs, and suggests local research; richer features (location-based defaults, saved profiles, downloadable spreadsheets) are planned for later phases.

Target users
------------
- Primary: First-time homebuyers and first-time renters in the UK.
- Secondary: People unfamiliar with housing finance who want a clear, guided comparison.

MVP goals
---------
- Implement accurate UK financial calculations for buying and renting.
- Present a single, easy-to-understand recommendation plus numeric comparisons at 5/10/15/20/25/30-year horizons.
- Surface both a concise summary and an optional detailed breakdown of costs.
- Provide AI-driven plain-language explanations and input validation (flag unrealistic values).

UK-specific model (key cost components)
---------------------------------------
One-off buying costs:
- Stamp Duty Land Tax (SDLT) / Scotland equivalent
- Solicitor and conveyancing fees
- Survey costs
- Mortgage arrangement / product fees
- Mortgage valuation fee
- Land registration fee

Ongoing buying costs:
- Mortgage interest
- Building insurance
- Service charge / ground rent
- Repairs & maintenance reserve
- Council tax

Renting costs:
- Deposit
- Rent (ongoing)

User experience & AI role
------------------------
- AI acts as an assistant (not an authoritative advisor): explains calculations, asks clarifying questions, suggests local research (e.g., typical mortgage rates in Manchester), and flags unrealistic inputs.
- Default view: a clean dashboard with a summary recommendation and clear graphs; users can drill down into a detailed line-item breakdown.
- Users can toggle planning horizon; comparisons are shown for 5, 10, 15, 20, and 25 years.

User stories
------------
See `docs/user-stories.md` for the full set of detailed user stories across core calculation, assumptions, inputs, AI layer, results, output, and non-functional requirements.

Next steps
----------
- Review this `CONTEXT.md` and request edits or approval.
- After approval: implement the financial model and basic UI, then add AI prompt flows and input validation.
