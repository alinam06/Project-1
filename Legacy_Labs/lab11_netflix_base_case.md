# Lab 11 - Netflix Unchanged Base-Case Record

**Purpose:** Preserve the unchanged Lab 10 base case as the comparison point for Lab 11 and document the two selected input ranges before the formal sensitivity runs. No changed-input results or student prediction are included here.

**Model rerun:** `python3 netflix_proforma.py`

## Preservation note

The existing `netflix_proforma.py` and `lab10_netflix.md` files were read and rerun without modification. This document is a separate Lab 11 baseline record.

## Inputs used in the unchanged base case

All monetary inputs are USD millions unless otherwise stated.

| Model input | Unchanged base value | Units / basis |
|---|---:|---|
| Revenue growth | 12%, 10%, 8%, 7%, 6% | Annual growth, FY2026E-FY2030E |
| Content-additions growth | 8%, 7%, 6%, 5%, 4% | Annual growth, FY2026E-FY2030E |
| Content-amortization growth | 8%, 7%, 6%, 5%, 4% | Annual growth, FY2026E-FY2030E |
| Other cost of revenues / revenue | 15.17% | FY2025 historical ratio |
| Operating expenses / gross profit | 37.5%, 36.5%, 35.5%, 35.0%, 34.5% | Annual ratio, FY2026E-FY2030E |
| Depreciation / opening PP&E | 20.92% | FY2025 historical ratio |
| Capital spending | $700.0 each year | USD millions |
| Other-asset investment / revenue increase | 5.0% | Ratio |
| Content liabilities / content assets | 17.28% | FY2025 historical ratio |
| Tax rate | 14.0% | Effective rate assumption |
| Interest rate | 4.98% | Applied to opening term debt |
| Term-debt repayment | $1,000.0 each year | USD millions |
| Share buybacks | $6,000.0 each year | USD millions |
| Minimum cash | $5,000.0 | USD millions |
| Cost of equity | 9.0% | FCFE discount rate |
| Terminal growth | 3.0% | Perpetual growth rate |
| Shares outstanding | 4,222.162150 | Millions of shares; held fixed |

### FY2025 opening balances used by the model

| Opening input | FY2025 value |
|---|---:|
| Revenue | $45,183.036 |
| Cash | $9,033.681 |
| Content assets, net | $32,778.392 |
| PP&E, net | $2,004.350 |
| Other assets | $11,780.570 |
| Content liabilities | $5,664.330 |
| Term debt | $14,462.836 |
| Other liabilities | $8,854.339 |
| Stockholders' equity | $26,615.488 |

### Historical anchors used to calculate base ratios and schedules

| Historical input | Value |
|---|---:|
| FY2025 content additions | $17,096.617 |
| FY2025 content amortization | $16,422.166 |
| FY2025 cost of revenues | $23,275.329 |
| FY2025 depreciation and amortization of PP&E and intangibles | $333.389 |
| FY2024 PP&E | $1,593.756 |
| Interest-expense numerator used for the interest rate | $776.510 |
| Debt denominator used for the interest rate | $15,582.804 |

## Two independent operating inputs selected for Lab 11

The inputs are still named `REVENUE_GROWTH` and `SGA_TO_GROSS_PROFIT` in `netflix_proforma.py`.

| Input and units | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| `REVENUE_GROWTH` (annual %) | 12.0% | 10.0% | 8.0% | 7.0% | 6.0% |
| `SGA_TO_GROSS_PROFIT` (% of gross profit) | 37.5% | 36.5% | 35.5% | 35.0% | 34.5% |

### How `REVENUE_GROWTH` affects the statements

The model calculates each year's revenue as opening revenue multiplied by one plus that year's growth rate. It therefore affects the income statement first through revenue. It also changes other cost of revenues, which is modeled as a percentage of revenue, and then gross profit, operating expenses, operating income, taxes, and net income. On the balance sheet and cash-flow statement, revenue growth changes the required investment in other assets because that investment equals 5% of the annual revenue increase. Through net income and working investment, it changes operating cash flow, FCFE, cash, retained equity, terminal cash flow, and equity value.

### How `SGA_TO_GROSS_PROFIT` affects the statements

Despite the variable's abbreviated name, the Lab 10 presentation calls this line operating expenses: sales and marketing, technology and development, and general and administrative expenses. The model calculates operating expenses as gross profit multiplied by the annual ratio. The input therefore changes operating expenses directly, then operating income, pretax income, taxes, net income, operating cash flow, FCFE, cash, retained equity, terminal cash flow, and equity value. It does not directly change revenue, content additions, content amortization, or gross profit.

The two inputs are independent model assumptions: revenue growth sets the top-line path, while the operating-expense ratio sets the amount of gross profit consumed by operating expenses.

## Visible results from the unchanged rerun

### Income statement

| Line item | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Revenue | $50,605.0 | $55,665.5 | $60,118.7 | $64,327.1 | $68,186.7 |
| Content amortization | $17,735.9 | $18,977.5 | $20,116.1 | $21,121.9 | $21,966.8 |
| Other cost of revenues | $7,675.5 | $8,443.1 | $9,118.5 | $9,756.8 | $10,342.3 |
| Cost of revenues | $25,411.5 | $27,420.6 | $29,234.6 | $30,878.8 | $32,309.0 |
| Gross profit | $25,193.5 | $28,244.9 | $30,884.1 | $33,448.3 | $35,877.6 |
| Operating expenses | $9,447.6 | $10,309.4 | $10,963.9 | $11,706.9 | $12,377.8 |
| Depreciation | $419.3 | $478.0 | $524.4 | $561.2 | $590.2 |
| Operating income | $15,326.7 | $17,457.5 | $19,395.8 | $21,180.2 | $22,909.6 |
| Interest | $720.7 | $670.9 | $621.0 | $571.2 | $521.4 |
| Pretax income | $14,606.0 | $16,786.7 | $18,774.8 | $20,609.0 | $22,388.3 |
| Tax | $2,044.8 | $2,350.1 | $2,628.5 | $2,885.3 | $3,134.4 |
| Net income | $12,561.1 | $14,436.5 | $16,146.3 | $17,723.8 | $19,253.9 |

### Balance sheet

| Line item | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Cash | $13,440.5 | $19,757.3 | $27,821.9 | $37,478.9 | $48,683.8 |
| Content assets, net | $33,506.8 | $34,286.2 | $35,112.4 | $35,979.8 | $36,882.0 |
| PP&E, net | $2,285.1 | $2,507.1 | $2,682.6 | $2,821.5 | $2,931.3 |
| Other assets | $12,051.7 | $12,304.7 | $12,527.4 | $12,737.8 | $12,930.8 |
| Content liabilities | $5,790.2 | $5,924.9 | $6,067.7 | $6,217.6 | $6,373.5 |
| Term debt | $13,462.8 | $12,462.8 | $11,462.8 | $10,462.8 | $9,462.8 |
| Other liabilities | $8,854.3 | $8,854.3 | $8,854.3 | $8,854.3 | $8,854.3 |
| Stockholders' equity | $33,176.6 | $41,613.2 | $51,759.5 | $63,483.2 | $76,737.1 |

### Cash-flow statement

| Line item | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Net income | $12,561.1 | $14,436.5 | $16,146.3 | $17,723.8 | $19,253.9 |
| Content additions | $18,464.3 | $19,756.9 | $20,942.3 | $21,989.4 | $22,868.9 |
| Content amortization | $17,735.9 | $18,977.5 | $20,116.1 | $21,121.9 | $21,966.8 |
| Operating cash flow | $12,106.8 | $14,016.8 | $15,764.7 | $17,356.9 | $18,904.9 |
| Investing cash flow | $(700.0) | $(700.0) | $(700.0) | $(700.0) | $(700.0) |
| Financing cash flow | $(7,000.0) | $(7,000.0) | $(7,000.0) | $(7,000.0) | $(7,000.0) |
| Change in cash | $4,406.8 | $6,316.8 | $8,064.7 | $9,656.9 | $11,204.9 |
| Opening cash | $9,033.7 | $13,440.5 | $19,757.3 | $27,821.9 | $37,478.9 |
| Ending cash | $13,440.5 | $19,757.3 | $27,821.9 | $37,478.9 | $48,683.8 |
| FCFE before share buybacks | $10,406.8 | $12,316.8 | $14,064.7 | $15,656.9 | $17,204.9 |
| Share buybacks | $(6,000.0) | $(6,000.0) | $(6,000.0) | $(6,000.0) | $(6,000.0) |

## Accounting and model checks from the unchanged rerun

| Check | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Assets - liabilities - equity | $0.0 | $0.0 | $0.0 | $0.0 | $0.0 |
| Ending cash | $13,440.5 | $19,757.3 | $27,821.9 | $37,478.9 | $48,683.8 |
| $5,000 minimum-cash test | PASS | PASS | PASS | PASS | PASS |
| FCFE sign test | Positive | Positive | Positive | Positive | Positive |

The model's existing intentional failure test also worked: resetting FY2026E cash to the FY2025 opening balance on a separate copy stopped valuation with a balance-sheet gap of negative $4,406.8 million. The unchanged model itself remained intact.

## Unchanged valuation result

| Valuation output | Result |
|---|---:|
| PV of forecast FCFE | $53,048.59 million |
| Terminal value at FY2030 | $312,516.98 million |
| PV of terminal value | $203,114.60 million |
| Equity value | $256,163.18 million |
| Terminal value / equity value | 79.29% |
| Value per share | **$60.67** |

## Cash-flow classification and valuation review

The modeled free cash flow is **FCFE, not FCFF**. It begins with net income after interest expense, adds noncash depreciation and content amortization, subtracts content additions, other-asset investment, capital spending, and the $1,000 million annual debt repayment, and adds the change in content liabilities. Because financing costs are already reflected in net income and net debt repayment is reflected in the cash flow, the residual belongs to common equity holders.

The valuation is structurally defensible as a simplified FCFE model because it:

- discounts FCFE at the 9% cost of equity rather than at WACC;
- produces equity value directly and therefore does not subtract net debt again;
- excludes share repurchases from FCFE because repurchases are distributions of FCFE, not operating investments required to generate it;
- verifies that the balance sheet balances, cash stays above the stated minimum, and FCFE remains positive before calculating value; and
- removes the fixed $1,000 million debt repayment from the terminal cash-flow base, consistent with the explicit comment that this repayment is not assumed to continue forever.

It remains a simplified and assumption-dependent valuation rather than a precise estimate. In particular, 79.29% of equity value comes from the terminal value; the terminal treatment assumes the fixed debt repayment stops after FY2030; shares outstanding are held fixed even though the statements include annual buybacks; and the large forecast cash balance is not separately distributed or normalized. Those limitations do not change the model's FCFE classification, but they should be considered when interpreting the existing $60.67 per-share result.

## Lab 11 - Selected ranges (documented before any sensitivity run)

No changed-input sensitivity was run as part of this Lab 11 range-selection step, and no changed-input results are included here. Each formal Lab 11 test will change only one named input while holding every other model input at its unchanged base value.

### Driver 1: `REVENUE_GROWTH`

**Units:** Annual percent growth in revenue. Differences from the base case are stated in **percentage points**.

**Years affected:** FY2026E, FY2027E, FY2028E, FY2029E, and FY2030E. No historical year changes.

| Revenue-growth path | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Lower | 10.0% | 8.0% | 6.0% | 5.0% | 4.0% |
| Base | 12.0% | 10.0% | 8.0% | 7.0% | 6.0% |
| Higher | 14.0% | 12.0% | 10.0% | 9.0% | 8.0% |
| Lower change from base | -2.0 pp | -2.0 pp | -2.0 pp | -2.0 pp | -2.0 pp |
| Higher change from base | +2.0 pp | +2.0 pp | +2.0 pp | +2.0 pp | +2.0 pp |

**Reason and evidence:** Netflix's reported revenue growth was 6.67% in 2023, 15.65% in 2024, and 15.85% in 2025. The Netflix research file also records management's July 2026 expectation of 13%-14% full-year revenue growth, driven by memberships, pricing, and advertising. The 14% FY2026E higher value is therefore tied to management's stated 2026 range, while 10% represents a material downside to that outlook without assuming revenue contraction. The later-year lower and higher values are explicitly **analyst judgment**: both retain the base model's declining-growth pattern as Netflix becomes larger, but place a consistent two-percentage-point band around it. The historical evidence supports uncertainty around the growth rate; it does not guarantee either path.

**Statement path:** Revenue growth changes revenue directly. Because other cost of revenues equals a fixed percentage of revenue, it then changes gross profit. Operating expenses are calculated from gross profit, so operating income, pretax income, tax, and net income also change. Revenue growth additionally changes other-asset investment through the model's 5% of revenue-increase formula. Those effects flow into operating cash flow, FCFE, ending cash, equity, terminal cash flow, and value per share.

### Driver 2: `SGA_TO_GROSS_PROFIT`

**Units:** Operating expenses as a percent of gross profit. Differences from the base case are stated in **percentage points**.

**Years affected:** FY2026E, FY2027E, FY2028E, FY2029E, and FY2030E. No historical year changes.

| Operating-expense path | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|
| Lower | 35.5% | 34.5% | 33.5% | 33.0% | 32.5% |
| Base | 37.5% | 36.5% | 35.5% | 35.0% | 34.5% |
| Higher | 39.5% | 38.5% | 37.5% | 37.0% | 36.5% |
| Lower change from base | -2.0 pp | -2.0 pp | -2.0 pp | -2.0 pp | -2.0 pp |
| Higher change from base | +2.0 pp | +2.0 pp | +2.0 pp | +2.0 pp | +2.0 pp |

**Reason and evidence:** The comparable historical ratio—sales and marketing plus technology and development plus general and administrative expense, divided by gross profit—declined from 50.36% in 2023 to 42.00% in 2024 and 39.17% in 2025. The higher FY2026E value of 39.5% is close to the 2025 actual ratio and represents less operating leverage than the base case. The lower values are explicitly **analyst judgment** and represent stronger operating leverage as Netflix uses its existing global technology, brand, and administrative structure across a larger gross-profit base. A symmetric two-percentage-point band keeps the test interpretable while acknowledging that the historical improvement may be faster or slower than the base forecast.

`SGA_TO_GROSS_PROFIT` is the model's variable name, but the modeled line is broader than conventional SG&A: it includes sales and marketing, technology and development, and general and administrative expenses. This test does **not** change operating margin directly because operating margin is an output calculated from the model's other inputs.

**Statement path:** The ratio changes operating expenses directly but does not directly change revenue, content additions, content amortization, cost of revenues, or gross profit. The expense change then flows through operating income, pretax income, tax, net income, operating cash flow, FCFE, ending cash, equity, terminal cash flow, and value per share. A lower ratio is favorable to those profit and cash-flow outputs; a higher ratio is unfavorable, all else equal.

## Student-locked prediction - complete after closing AI

This section is intentionally blank. The prediction must be written and timestamped by the student before any sensitivity run.

**Date/time:**  
**Driver and affected years:**  
**Old input -> new input, with units:**  
**Expected direction and rough size of the output change:**  
**Why, tracing input -> statements -> output:**  

## Partner discussion - complete only after it occurs

Do not fill this section from an assumed or invented conversation.

**Partner's name:**  
**Date/time discussed:**  
**Range and locked prediction shown to partner:**  
**Partner confirmation that units are percentage points:**  
**Partner confirmation that only one independent input changes:**  
**Partner's question:**  
**My response:**  
**Roles swapped and partner's driver reviewed:**  
