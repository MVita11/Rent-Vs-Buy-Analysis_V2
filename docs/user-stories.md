# User stories

## Core calculation
- As a first-time buyer or renter, I want the system to compute total cost-to-occupy for both renting and buying so I can compare net cash flows over time.
- As a user, I want the comparator to show totals at 5, 10, 15, 20, and 25 years so I can evaluate different planning horizons.
- As a user, I want the calculation to include both one-off purchase costs and ongoing costs so I can see where money is spent.

## Assumptions
- As a user, I want the tool to list key assumptions (inflation, house price growth, maintenance rate, mortgage amortization) so I understand the model limits.
- As a user, I want sensible default assumptions for UK markets that I can override so I can get a quick answer without deep input.

## Inputs
- As a user, I want to enter core inputs (purchase price, down payment, mortgage rate, mortgage term, monthly rent, deposit) so the model reflects my situation.
- As a user, I want optional inputs (council tax band, service charge, insurance, planned move horizon) to refine results when available.
- As a user, I want the UI to provide UK-specific helper text (what is SDLT, what is a conveyancing fee) so I can enter accurate values.

## AI layer
- As a user, I want the AI assistant to explain the recommendation in plain language so I can understand why renting or buying is better.
- As a user, I want the AI to flag unrealistic inputs (e.g., impossible mortgage rates) and suggest plausible ranges so my analysis is realistic.
- As a user, I want the AI to suggest local research (typical mortgage rates, local market trends) when I choose a location so I can refine inputs.

## Results
- As a user, I want a one-line recommendation (Rent / Buy / Indeterminate) with confidence notes so I can act quickly.
- As a user, I want a side-by-side numeric summary (cumulative costs, net equity, opportunity cost) for each horizon so I can compare alternatives.
- As a user, I want clear graphs showing cumulative costs and break-even points so I can visualise when buying becomes preferable.

## Output
- As a user, I want an expandable detailed breakdown that lists every cost line (SDLT, solicitor, survey, interest, maintenance, council tax, rent) so I can audit the math.
- As a user, I want an export option (CSV/XLS) so I can run my own analyses in a spreadsheet.

## Non-functional / UX
- As a user, I want the app to be mobile responsive so I can use it on my phone.
- As a user, I want to save and reload scenarios (with an account) so I don't re-enter data and can compare locations.
- As a user, I want input validation and friendly error messages so I don’t submit impossible scenarios.
- As a user, I want reasonable performance for typical inputs so calculations and visualisations appear instantly.
- As a product owner, I want telemetry on feature usage (e.g., which horizons viewed, export downloads) to prioritise improvements.

## Cross-cutting
- As a user concerned about privacy, I want clear information about how saved data is stored and used so I can opt in or out.
- As a developer, I want automated tests that validate core financial calculations so regressions are caught early.
