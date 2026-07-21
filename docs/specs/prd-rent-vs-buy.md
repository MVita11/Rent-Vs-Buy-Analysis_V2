## PRD: Rent-vs-Buy Analysis — MVP (UK)

## Problem Statement

First-time renters and first-time homebuyers in the UK struggle to make an informed decision between renting and buying because existing tools are either too technical (spreadsheets) or too shallow (single-metric calculators). Users need a clear, UK-specific comparison that explains which option is likely better for them over multiple planning horizons and why.

## Solution

Provide a UK-focused rent-vs-buy decision assistant that computes and compares the total cost-to-occupy for renting and buying across multiple horizons (5, 10, 15, 20, 25 years). The product will present a one-line recommendation (Rent / Buy / Indeterminate), a side-by-side numeric comparison, clear graphs (cumulative costs and break-even), and an optional expandable line-item breakdown. An AI assistant explains results in plain English, flags unrealistic inputs, and suggests local research.

## User Stories

(Extensive list capturing MVP and near-term features)

1. As a first-time buyer or renter, I want the system to compute total cost-to-occupy for both renting and buying so I can compare net cash flows over time.
2. As a user, I want the comparator to show totals at 5, 10, 15, 20, and 25 years so I can evaluate different planning horizons.
3. As a user, I want the calculation to include both one-off purchase costs and ongoing costs so I can see where money is spent.
4. As a user, I want the tool to list key assumptions (inflation, house price growth, maintenance rate, mortgage amortization) so I understand model limits.
5. As a user, I want sensible default assumptions for UK markets that I can override so I can get a quick answer without deep input.
6. As a user, I want to enter core inputs (purchase price, down payment, mortgage rate, mortgage term, monthly rent, deposit) so the model reflects my situation.
7. As a user, I want optional inputs (council tax band, service charge, insurance, planned move horizon) to refine results when available.
8. As a user, I want the UI to provide UK-specific helper text (what is SDLT, conveyancing fee) so I can enter accurate values.
9. As a user, I want the AI assistant to explain the recommendation in plain language so I can understand why renting or buying is better.
10. As a user, I want the AI to flag unrealistic inputs (e.g., impossible mortgage rates) and suggest plausible ranges so my analysis is realistic.
11. As a user, I want the AI to suggest local research (typical mortgage rates, local market trends) when I choose a location so I can refine inputs.
12. As a user, I want a one-line recommendation (Rent / Buy / Indeterminate) with confidence notes so I can act quickly.
13. As a user, I want a side-by-side numeric summary (cumulative costs, net equity, opportunity cost) for each horizon so I can compare alternatives.
14. As a user, I want clear graphs showing cumulative costs and break-even points so I can visualise when buying becomes preferable.
15. As a user, I want an expandable detailed breakdown that lists every cost line (SDLT, solicitor, survey, interest, maintenance, council tax, rent) so I can audit the math.
16. As a user, I want an export option (CSV/XLS) so I can run my own analyses in a spreadsheet (near-term/phase-2).
17. As a user, I want the app to be mobile responsive so I can use it on my phone.
18. As a user, I want to save and reload scenarios (with an account) so I don't re-enter data and can compare locations (phase-2).
19. As a user, I want input validation and friendly error messages so I don’t submit impossible scenarios.
20. As a user, I want reasonable performance for typical inputs so calculations and visualisations appear instantly.
21. As a product owner, I want telemetry on feature usage (e.g., which horizons viewed, export downloads) to prioritise improvements.
22. As a user concerned about privacy, I want clear information about how saved data is stored and used so I can opt in or out.
23. As a developer, I want automated tests that validate core financial calculations so regressions are caught early.
24. As a user, I want the option to select UK region (England, Scotland, Northern Ireland, Wales) so the tool applies appropriate taxes and fees.
25. As a user, I want the AI to offer clarifying questions when inputs are incomplete so the result quality improves.

## Implementation Decisions

Seams and modules (high-level)
- Core calculation module: pure, deterministic finance functions that accept input parameters and return a full time-series of costs and key aggregates (cumulative costs, net equity, break-even time). This module must be pure and fully unit-tested.
- Presentation layer: UI component(s) for input form, summary recommendation, numeric table, and graphs.
- AI assistant layer: metadata + prompt orchestration layer that inspects the calculation output and produces a plain-language explanation, flags unrealistic inputs, and suggests local research. The assistant is a thin service that calls an LLM; keep prompts and templates versioned.
- Persistence layer (phase-2 opt-in): user scenarios and saved profiles; not required in MVP but designed as a small, isolated module behind an interface.
- Data layer for UK defaults: a small read-only configuration that maps regions to default values (mortgage-rate estimates, council tax heuristics, typical service-charge ranges). This is a configuration artefact, not a heavy dependency.

Seams (testing and integration points)
- Preferred seam: the project should expose the core calculation module as a single public API that the UI and AI layers call. Tests target this API only.
- Secondary seam: the AI assistant interacts with the calculation output through a simple DTO (calculation summary) — keep the DTO stable and minimal.
- Avoid scattering calculation logic across UI; keep finance logic centralized.

APIs & contracts (prose)
- Core calculation API signature: accepts user inputs + assumptions; returns time-series and aggregates (per-horizon cumulative costs, net equity, break-even indicator, line-item breakdowns).
- AI assistant contract: accepts calculation summary and user inputs, returns explanation text, flagged-input warnings, and optionally suggested defaults/research pointers.

Security & privacy
- Saved profiles (phase-2) must be opt-in and stored encrypted at rest; design for selective field redaction.

Operational
- Telemetry: record which horizons users view and when they export; store minimal, aggregated usage metrics.

## Testing Decisions

What makes a good test
- Unit tests for the core calculation must assert deterministic outputs for known inputs (fixtures). Tests validate aggregates and line-item breakdowns, not internal steps.
- Integration tests ensure the UI renders a calculation summary for a full example input and that the AI assistant returns a well-formed explanation (syntactic checks, not semantic correctness).
- Edge-case tests: extreme inputs (very high/low mortgage rates, zero down payment), missing optional inputs, and typical UK scenarios for multiple regions.

Modules to test
- Core calculation module: full coverage of arithmetic, tax rules (SDLT / regional variants), and amortization.
- Validation module: input sanity checks.
- AI prompt layer: unit tests for prompt assembly and a small integration smoke test (mocked LLM).

Prior art
- Use example fixtures in `tests/fixtures/` containing representative UK scenarios (London flat, Manchester terraced, rural Wales) and expected aggregates.

## Out of Scope (MVP)

- Real-time location-based market scraping or integration with external property APIs (phase-2).
- Full account system and multi-user sharing flows (phase-2).
- Advanced tax optimisation or legal advice — product provides educational explanation only.
- Automatic mortgage rate fetching and loan offers (phase-2 research-only suggestion).

## Further Notes

- UK specifics: ensure SDLT vs Scotland differences are encoded in the tax logic and surfaced in helper text.
- Keep the core calculation module small and language-agnostic so it can be reused across web and CLI front-ends.
- Prefer simple, testable deterministic defaults and let the AI recommend research links rather than embedding uncertain live data.


---

*Spec generated from repo context and prior planning conversation.*
