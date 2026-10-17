# Netflix Project 1 — revised standalone FCFF application

## Project Overview

This project evaluates whether an investment fund should
initiate a position in Netflix (NASDAQ: NFLX) based on
financial information available as of January 23, 2026.

I developed an AI-assisted corporate finance application
that integrates five-year financial statement projections,
discounted cash flow (DCF) valuation, comparable-company
analysis, scenario testing, and model validation.

The objective is to provide an evidence-based investment
recommendation while maintaining independent financial
judgment over assumptions and model outputs.

### Investment Recommendation: WATCH–DEFER

My analysis estimates Netflix's standalone intrinsic
value between $42.13 and $60.33 per share, with a
base-case valuation of $51.20.

Netflix's January 23, 2026 closing price was $86.12,
approximately 68% above my base-case estimate.

Even under the high operating scenario, the estimated
intrinsic value remains below the historical market price.

Based on these results, I recommend that the investment
committee place Netflix on its watchlist rather than
initiate a position at the historical market price.

This recommendation is conditional on the assumptions
used in the model. The potential Warner Bros. Discovery
acquisition is excluded and requires separate analysis
before an initiation decision.

### Key Valuation Results

| Scenario | Estimated Value Per Share |
|---|---:|
| Low Operating Case | $42.13 |
| Base Operating Case | $51.20 |
| High Operating Case | $60.33 |
| January 23 Market Price | $86.12 |

**Valuation Date:** January 23, 2026  
**Forecast Period:** FY2026–FY2030  
**Currency:** USD  
**Investment Recommendation:** WATCH–DEFER

## Decision boundary

- User: fund investment committee, no current NFLX position.
- Historical valuation date and information cutoff: January 23, 2026 close.
- Proposed investment horizon: 2026–2030.
- USD millions for statements and share counts; USD/share for price/value.
- Valuation denominator: 4,222.162150m reported year-end basic shares + 94.351m FY2025 incremental diluted awards = 4,316.513150m diluted proxy. This is an analyst approximation, not reported spot diluted shares.
- Standalone Netflix only. Pending WBD acquisition, synergies, financing, dilution, integration costs and subsequent deal outcomes excluded. This is a material reason to defer full initiation underwriting.
- Annual year-end discount convention, periods 1–5 for 2026–2030; explicit 23-day approximation to January 23. December cash/debt are latest annual snapshots, not rolled to January 23.
- Not a current October 2026 trade recommendation.

The historical date was chosen to align with Edition A and remove the old mixed-date inputs. Rebuilding the same system for a later valuation date would require contemporaneous interim history, market data and transaction underwriting; do not relabel this result as a later-date value.

## Run from the course folder

```bash
python3 model.py
python3 build_communications.py
```

Python 3.10+; standard library only; no API keys, network calls or downloads. The actual interpreter version is saved in `results.json`. First command runs checks and writes `visible_results.md` and `results.json` beside the script. The second refreshes the slide plan/scripts and memo from those saved results. **Both commands overwrite generated outputs**; save any personal edits before regeneration. Edit assumptions in `model.py`, not generated result tables.

To produce a log:

```bash
python3 model.py > run_log.txt
```

Failures produce a nonzero exit and prevent a new successful result from being written. Existing generated files can remain from a previous run; check exit status and timestamps before using them. The runner does not require the old lab scripts, PDFs or a network connection; source references remain separately visible for audit.

## What changed

1. New application preserves legacy lab engines and Edition A; it integrates the operating forecast and FCFF/WACC DCF.
2. Removes duplicate depreciation expense. Functional GAAP-based costs include D&A; cash flow adds back noncash D&A once.
3. Separates $619m Brazil expense normalization from the $700m expected deposit cash outflow.
4. Uses a documented 21% operating-tax judgment, January WACC calculation and a consistent share proxy.
5. Normalizes terminal reinvestment using growth/ROIC instead of extending an unusually high final-year cash conversion forever.
6. Produces causal operating cases, an additional structural stress, a WACC–growth grid and revenue-driven reverse DCF.
7. Adds January Disney EV/revenue and P/E references, with a real dated cover share count and NCI claim. No mechanical peer average.
8. Adds historical reconciliation, cash/FCFF articulation, boundary/monotonicity, claim-bridge, corruption and financing-invariance checks.

The separately edited old `md files/lab10_netflix.md` changes only two mislabeled historical units. No earlier AI-off receipt or student verification was reconstructed.

## Scope of validation

`model.py` runs all software checks each time. `SOURCES_AND_ASSUMPTIONS.md` records primary-source/definition checks and an AI-output correction. Synthetic $1,000 perpetuity exercises the same discount function used in the valuation; it does **not** claim a match to instructor starter answers.

`cold_run_log.txt`, if present, records an isolated fresh-venv execution and result comparison. It is a text execution record, not a screen recording. Capture the actual demonstration required for Video 2 separately.

The financial statements can balance while the economics remain wrong. Review content economics, future working capital, tax, cash availability, terminal returns, share dilution, pending transaction and the forward expense ratios before endorsing the output. Full limitations and the value/basis/challenge/change-evidence driver record are in `SOURCES_AND_ASSUMPTIONS.md`.

## AI Use and Analyst Responsibility

AI-assisted tools, including Codex, were used to
support Python development, financial modeling,
data organization, validation procedures, and
drafting of supporting documentation.

The financial assumptions, valuation methods,
and investment recommendation require independent
analyst review.

AI-generated outputs are not treated as
independent evidence of financial accuracy.

The project includes financial reconciliation,
sensitivity analysis, and model validation
procedures to evaluate calculation consistency.

Additional validation and course-specific evidence
requirements are documented in the project files.

The final investment recommendation reflects
the analyst's evaluation of the financial
evidence, assumptions, and model limitations.