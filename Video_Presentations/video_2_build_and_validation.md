---
marp: true
theme: default
paginate: true
title: Netflix: build logic and validation
---

# How I evaluated Netflix

**Video 2 · Alina Mato**

Historical evidence → operating forecast → cash flow → value/share

Five forecast years: 2026–2030
Standalone model; historical January 23 price comparison

---

# Application and visible output

Python standard library · Offline calculation

From the **Project-1 repository root**:

```bash
python3 Project_1_Completion/final/model.py
```

Outputs: `visible_results.md` and `results.json`
Statements/shares: **millions** · Value/share: **dollars**

<!-- Run a temporary copy during recording; executing the original overwrites its outputs. -->

---

# Build logic

1. Historical facts and explicit normalizations
2. Revenue, content and operating-cost assumptions
3. Linked income statement, balance sheet and cash flow
4. Cash available to lenders and shareholders, discounted at WACC
5. Add cash, subtract debt, divide by the share proxy

Code: `forecast()`, `check_statements()`, `value()`

---

# The operating forecast drives cash flow

| Base assumption/result | 2026 | 2030 |
|---|---:|---:|
| Revenue growth | 12% | 6% |
| Content-additions growth | 8% | 4% |
| Revenue, $bn | 50.61 | 68.19 |
| Operating profit, $bn | 16.18 | 24.11 |
| FCFF, $bn | 10.93 | 18.00 |

Growth and improving margins are assumptions to challenge.

Source: `final/visible_results.md`; `final/model.py`

---

# Enterprise value to share value

| Base bridge | $bn |
|---|---:|
| Present value of five forecast years | 56.402 |
| Present value of terminal cash flows | 170.019 |
| Enterprise value | 226.421 |
| Add eligible cash/investments | 9.062 |
| Subtract debt | 14.463 |
| Equity value | 221.021 |

**4.317bn diluted-proxy shares → $51.20/share**

Source: `final/visible_results.md`; share proxy is an approximation

---

# Long-run assumptions and WACC test

Base: **9% WACC · 3% terminal growth · 15% terminal ROIC**
Terminal reinvestment: **20%** · Terminal share of EV: **75.1%**

| WACC only | Estimated value/share |
|---|---:|
| 9% | $51.20 |
| 12% | $33.71 |

**34.17% decline**; identical operating forecasts and other inputs.

AI-assisted sensitivity run; does not establish a locked human prediction.

---

# Checks that can fail

- Historical arithmetic and annual balance-sheet/cash reconciliations
- Synthetic known answer: **$100 / 10% = $1,000**
- Invalid discount/terminal assumptions rejected
- Cash/debt bridge and FCFF/financing reconciliation
- Deliberately corrupted cash or FCFF blocks valuation

Code: `run_checks()` · Source: saved results, Checks

The synthetic check is separate from the official course benchmark.

---

# Validation evidence and remaining requirements

| Evidence | Current presentation status |
|---|---|
| 9% → 12% sensitivity | AI-assisted run reproduced; base unchanged |
| Human locked prediction | Original prediction/precommit still required |
| Official starter answer | Expected/actual comparison still required |
| Fresh-environment run | Text log exists; required recording still needed |

Show actual source and failure-test evidence on screen.

Source: `final/REVISION_AND_VALIDATION.md`; October 17 WACC run

---

# What the model supports

- One financial system produces the forecasts and valuation
- Business scenarios and rate sensitivity answer different questions
- Passing software checks establishes consistency

**The analyst must still defend the assumptions and decision.**

Cutoff/share timing and transaction scope remain material limitations.

Source: revised assumptions; model checks
