# Revision and validation status

## Revision History

| Revision | Original approach | Revised approach | Reason for change | Effect on valuation |
|---|---|---|---|---|
| FCFF methodology | Earlier work used management-reported free cash flow as an approximation for FCFF | Integrated operating FCFF forecast using projected financial statements | FCFF must represent cash available to debt and equity investors before financing distributions | Material; exact isolated effect not yet established |
| Depreciation | Earlier model separately deducted D&A despite functional operating expenses already including it | D&A remains in operating expenses and is added back once when calculating operating cash flow | Prevents double-counting a noncash expense | Requires isolated comparison |
| Brazil normalization | Historical operating costs included the cumulative $619m tax charge | Removed the identified charge from recurring forecast costs while retaining expected deposits | Avoids assuming the cumulative charge recurs annually | Requires isolated comparison |
| Operating tax rate | Prior assumption needs confirmation | 21% normalized operating-tax assumption | Transparent forecasting judgment rather than direct use of reported effective tax rate | 14% alternative gives $55.95/share versus $51.20 base |
| WACC | Previous model assumptions need confirmation | 9% base WACC | Uses a dated risk-free rate plus documented capital-cost assumptions | WACC sensitivity reported separately |
| Terminal reinvestment | Earlier approach did not explicitly incorporate sustainable terminal reinvestment | Terminal growth of 3% and ROIC of 15% imply 20% reinvestment of terminal NOPAT | Ensures continued growth requires reinvestment | 10% ROIC gives $46.28/share; 20% gives $53.67/share |
| Share count | Earlier denominator needs confirmation | 4,316.513150m diluted-share proxy | Separates reported shares from estimated dilution | Basic-only value is $52.35/share |

**Important:** The revisions above are not all error corrections.
Some are forecasting and valuation judgments that require
independent review.

The isolated valuation effect of each revision should only
be reported if the old and revised models can be compared
while holding all other assumptions constant.

October 16, 2026; AI-assisted. The recommendation and assumptions remain for Alina's personal review. This document does not certify the full assignment complete.

| Item | Status and evidence |
|---|---|
| Preserve baseline | Original `md files/Project_1_Edition_A.md` not edited. Match to actual submitted checkpoint/receipt still needed. A current file hash cannot prove the original receipt. |
| Integrated FCFF | Implemented in `model.py`; five-year operating forecast drives valuation; FCFF independently ties to FCFE and financing. |
| Depreciation | Corrected in new model: reported revenue less reported cost of revenues less functional opex equals reported EBIT without subtracting D&A again. Old lab engine preserved as history. |
| Normalization | Identified $619m cumulative Brazil charge removed from recurring cost driver; $700m expected deposit deducted once in 2026 cash flow. Not all annual cost growth is excluded. |
| Tax / WACC / terminal | New judgments explicitly documented, not represented as mechanical error corrections. 21% operating tax, 9% WACC, 3% terminal growth, 15% terminal ROIC. Alternative tax/ROIC values and effects disclosed. |
| Statements | Opening reported BS and all forecast BS balances pass; cash flows tie to cash; reported FY2025 NI/CFO/cash arithmetic reconciles. Forecast simplified cash compensation/operating assets differs explicitly from reported GAAP adjustments. |
| Synthetic known answer | $100 perpetual cash flow at 10% and zero growth = $1,000 EV; test uses actual shared discount function. Official training-starter answer comparison not available. |
| Independent definition/source check | Primary Netflix statement/Note 13 operating-cost presentation, content accounting, cash/debt/share definitions and Treasury maturity/row checked against old inputs. AI-assisted; not claimed as Alina's AI-off work. |
| Direction / boundary checks | 3×3 base WACC–g grid passes directional ordering; invalid g/WACC/ROIC and NaN WACC rejected. Statements/FCFF corruptions fail loudly. |
| Highest-risk test | Add $100m to FCFF without changing operating/financing cash flows: FCFF/FCFE reconciliation fails before valuation. This protects against a plausible but wrongly defined enterprise cash flow. Cash-cell corruption independently fails BS reconciliation. |
| EV/equity bridge | +$100m debt lowers equity $100m; +$100m cash raises it $100m. Removing modeled repayments/distributions leaves unlevered EV unchanged under consistent taxes. |
| Cases and reverse DCF | Low/base/high plus structural stress all articulate. Reverse DCF solves revenue-growth requirements for $86.12 while holding other assumptions fixed. |
| Multiple definitions | P/E and EV/revenue implemented; dated Disney cover shares verified, NCI included at book proxy. One qualified peer, no median. WBD later EPS excluded at January cutoff. Expanded EV policy is a disclosed Edition B extension, not backdated precommitment. |
| AI output evaluated | Old proxy FCFF and duplicate depreciation qualified/corrected against primary financial definitions; see source/assumption record. |
| Fresh-environment execution | Fresh Python venv with no pip/packages, isolated run from clean staging copy, all saved numerical results matched exactly. See `cold_run_log.txt`. This is a real text log; a screen recording was not made. |
| Communication | Revised eight-slide content plan and three scripts use one saved result set; a committee memo draft is included. They require Alina's review and actual recordings/transcripts. |

## Model Validation Results

The following tests evaluate calculation consistency,
financial statement articulation, and the model's
response to changes in key inputs.

| Validation Test | Expected Result | Reported Actual Result | Status |
|---|---|---|---|
| Synthetic perpetuity | $100 / 10% = $1,000 | $1,000 | Reported PASS |
| Historical EBIT reconciliation | Revenue - cost of revenue - operating expenses = reported EBIT | $13,326.603m | Reported PASS |
| Forecast balance sheet | Assets = liabilities + equity each year | All forecast years reconcile | Reported PASS |
| Cash flow reconciliation | Ending cash equals balance-sheet cash | All forecast years reconcile | Reported PASS |
| FCFF/FCFE reconciliation | Unlevered and levered cash flows reconcile under financing adjustments | Reconciliation reported successful | Reported PASS |
| WACC sensitivity | Higher WACC decreases estimated value | Directional ordering passes | Reported PASS |
| Terminal growth sensitivity | Higher terminal growth increases estimated value, holding other assumptions constant | Directional ordering passes | Reported PASS |
| FCFF corruption test | Artificial $100m FCFF increase causes reconciliation failure | Failure detected before valuation | Reported PASS |
| Cash corruption test | Artificial cash change causes balance-sheet reconciliation failure | Failure detected | Reported PASS |
| Enterprise-to-equity bridge | $100m more debt reduces equity value by $100m, holding EV constant | Expected change reported | Reported PASS |
| Official training-case comparison | Match instructor's published expected answers | Not completed | OUTSTANDING |

## Locked Changed-Input Record — WACC Test

**Test Date:** October 17, 2026 
**Original WACC:** 9%  
**Test WACC:** 12%  
**Other Assumptions:** Held constant

### Pre-Test Prediction (Human-Authored, AI-Off)

**Original prediction:** Increasing WACC will decrease the valuation of the stock. 

### Actual Results

| Metric | 9% WACC | 12% WACC |
|---|---:|---:|
| Intrinsic Value/Share | $51.20 | $33.71 |
| Enterprise Value | $226.42B | $150.89B |
| Terminal Value | $261.60B | $174.40B |
| PV of Terminal Value | $170.02B | $98.96B |
| Recommendation | WATCH–DEFER | WATCH–DEFER |

### Interpretation

Increasing WACC from 9% to 12% reduced Netflix's estimated
intrinsic value by $17.49 per share, or 34.2%.

A higher discount rate reduces the present value of future
cash flows and terminal value. This demonstrates that Netflix's
valuation is highly sensitive to cost-of-capital assumptions.

### Investment Decision

The recommendation remains **WATCH–DEFER** because both
valuations are below Netflix's January 23, 2026 market
price of $86.12.

The higher WACC strengthens the decision to defer investment
but does not change the recommended action.

### Test Evidence

- **Prediction commit:** [INSERT HASH]
- **Execution date/time:** [INSERT]
- **Execution log:** [INSERT PATH]
- **12% results saved:** [INSERT PATH]
- **9% WACC restored and verified:** [YES/NO]

### Conclusion

The test confirms that WACC is a material valuation driver.
Although intrinsic value declined significantly, the
investment recommendation remained unchanged.


**Evidence locations:**
- `model.py` — executable model and testing functions.
- `results.json` — saved numerical model outputs.
- `run_log.txt` — execution results.
- `cold_run_log.txt` — isolated execution record.

The reported passing results are based on the
existing AI-assisted model and validation records.

## Items the assistant cannot truthfully manufacture

1. First successful Brightspace checkpoint receipt and exact original Edition A submission.
2. Instructor's official training-case answers, shared filename checklist and video limits, if not supplied.
3. A human-authored, AI-off prediction made before its test and preserved with actual timestamp/commit evidence. Existing observed outcomes cannot be reclassified as unseen predictions.
4. Real partner dialogue, credit, review and student reflection.
5. Alina's acceptance of new financial assumptions and committee judgment.
6. Screen recordings, corrected transcripts of actual speech, external publication/access tests and final submission receipt.

## Interpretation to defend

The new $51.20 is not “the old $60.94 with one bug fixed.” It reflects an integrated cash-flow definition plus choices about normalization, forecast taxes, discount rate, diluted denominator and terminal reinvestment. Those changes should be explained and challenged individually. The alternative assumptions in the driver record help show that the resulting range is conditional.

The January analysis cannot be presented as an October investment recommendation. Pending-transaction exclusion remains a substantive underwriting gap. A low modeled value can support not initiating at the dated price, but an acquisition-adjusted conclusion requires additional analysis.
