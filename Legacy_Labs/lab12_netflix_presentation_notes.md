# Lab 12 - Netflix Presentation Notes

## 15-minute speaking guide

These notes use the saved Netflix project only. Dollar amounts are U.S. dollars. Historical and forecast financial-statement amounts are generally shown in USD millions unless a table says billions; market prices and valuation conclusions are USD per split-adjusted share.

## Opening: current conclusion — 0:45

### Say

- My current conclusion remains **watch-defer**, not buy or sell. Netflix is a scaled, profitable entertainment platform with growing revenue, margins, and cash flow, but the saved base valuations do not provide a clear margin of safety at the dated market prices.
- The latest dedicated DCF gives **$60.94 per diluted share**, compared with a **$78.05 reference price dated September 8, 2026**. The Lab 10 linked FCFE model gives **$60.67 per share**, compared with a **$71.36 close on September 23, 2026**.
- The peer median is much higher at **$142.55**, but it is too unstable to override the DCF evidence because it is based on only Disney and a qualified WBD observation.
- My main research priority is the durability of revenue growth. In Lab 11, revenue growth was the largest driver over the tested ranges.

### Show

- [`Netflix_DCF_Analysis.md`](Netflix-research/Netflix_DCF_Analysis.md), “Conditional call” and “Overall conclusion.”
- [`lab08_netflix_comparables.md`](md%20files/lab08_netflix_comparables.md), sections 6-8.
- [`lab11_netflix.md`](lab11_netflix.md), “Conclusion and interpretation.”

### Plain-language terms

- **Watch-defer:** keep researching, but do not initiate based on the current evidence.
- **Margin of safety:** a meaningful gap between estimated value and price that allows for forecast error.

### Verify or decide myself

- Decide whether “watch-defer” is still the conclusion I personally support before presenting.
- The dedicated DCF does not state one formal valuation date. It uses a September 8 reference price, Q2 2026 balance-sheet inputs, and September 2026 discount-rate inputs. State this limitation rather than assigning a date that is not documented.

## Stop 1: target selection — 1:15

### Say

- I selected Netflix as the target company. My saved initial thesis described it as a high-quality, scaled entertainment platform whose 2025 revenue growth converted into faster operating-income and operating-cash-flow growth.
- Netflix was suitable for analysis because its SEC filings provide revenue, operating costs, content assets and additions, debt, cash flow, and split-adjusted per-share data. Those disclosures support a linked forecast, DCF, and peer comparison.
- Netflix is also analytically interesting because content cash spending occurs before all related expense is recognized. That makes the connection between accounting profit and cash generation important.
- My documented initial view was **watch-defer while completing valuation and risk underwriting**. A strong business was not automatically a good investment without a verified price and valuation range.

### Show

- [`Project_1_Edition_A.md`](md%20files/Project_1_Edition_A.md), “Decision and user,” “Initial thesis,” and “Consequential assumptions.”
- [`lab10_netflix.md`](lab10_netflix.md), “The line that makes Netflix different.”

### Plain-language terms

- **Target company:** the company being analyzed and valued.
- **Content amortization:** recognition of capitalized content cost as an expense over the period viewers are expected to consume it.

### Verify or decide myself

- A personal reason for choosing Netflix—such as interest in streaming, familiarity with the service, or another motivation—is **not documented**. Add it only if it is true.

## Stop 2: company and evidence — 2:00

### Say

- Netflix provides series, films, games, and live programming. In 2025 it earned revenue primarily from monthly streaming membership fees. Advertising and other activities contributed to growth but were not material individually in the 2023-2025 filing periods.
- The principal source is Netflix's Form 10-K for the year ended **December 31, 2025**, filed **January 23, 2026**. The later DCF also uses Netflix's Q2 2026 Form 10-Q and shareholder letter.
- In 2025, revenue was **$45.183 billion**, operating income was **$13.327 billion**, net income was **$10.981 billion**, and operating cash flow was **$10.149 billion**.
- Content is central to both operations and cash flow. Netflix recorded **$17.097 billion** of content additions and **$16.422 billion** of content amortization in 2025. It also disclosed **$24.039 billion** of content obligations.
- Netflix reported **$9.034 billion** of cash and cash equivalents and **$14.463 billion** of debt carrying value at December 31, 2025.
- The 2025 diluted weighted-average share count was **4.344 billion**, and all share data were retroactively adjusted for the November 2025 ten-for-one split.

### Show

- [`Netflix_2026-09-03_report.md`](Netflix-research/Netflix_2026-09-03_report.md), “Company and filing overview,” “2025 financial performance,” “Cost structure and content economics,” and “Cash flow, liquidity, and debt.”
- [`Netflix_2026-09-03_sources.md`](Netflix-research/Netflix_2026-09-03_sources.md) for the saved source trail.
- Local filing: [`nflx-20251231 10K.pdf`](Netflix%2010-K/nflx-20251231%2010K.pdf).

### Plain-language terms

- **Operating cash flow:** cash produced by the core business before investing and financing activities.
- **Carrying value:** the debt amount recorded on the balance sheet after accounting adjustments such as discounts and issuance costs.
- **Content obligation:** a contractual commitment to pay for content; some obligations are not yet recognized as balance-sheet liabilities.

### Verify or decide myself

- Keep billions and millions consistent when speaking. The report often uses billions; the pro-forma tables use USD millions.
- Do not describe the 2025 weighted-average diluted shares as the same share basis used in every valuation; the project uses different dated share counts.

## Stop 3: pro-forma — 3:00

### Say

- I used 2023-2025 filing history to anchor the forecast. Revenue growth was 6.67%, 15.65%, and 15.85%; the comparable operating-expense-to-gross-profit ratio declined from 50.36% to 42.00% to 39.17%.
- My base revenue-growth assumptions decline from **12% in FY2026E to 6% in FY2030E**. This is judgment: Netflix can still grow through membership, pricing, and advertising, but maintaining the same percentage growth becomes harder as the company becomes larger.
- Content additions and content amortization grow from **8% to 4%**. My reasoning is that Netflix can spread content across a larger global revenue base, and pricing and advertising do not require equal growth in content spending.
- Operating expenses fall from **37.5% to 34.5% of gross profit**. The variable name is `SGA_TO_GROSS_PROFIT`, but it includes sales and marketing, technology and development, and general and administrative expenses—not only conventional SG&A.
- The linked model works in this order: revenue and content assumptions produce gross profit; operating expenses, depreciation, interest, and tax produce net income; content additions, amortization, other assets, capital spending, and debt repayment produce cash flow; cash and equity then update the balance sheet.
- The modeled free cash flow is **FCFE**, or cash available to common shareholders after interest, capital investment, and net debt repayment. It is not FCFF.
- The base forecast reaches FY2030E revenue of **$68,186.7 million**, operating income of **$22,909.6 million**, and FCFE before buybacks of **$17,204.9 million**.
- Every forecast-year balance-sheet gap was **$0.0**, cash remained above the **$5,000 million** minimum, and FCFE was positive. The intentional error test stopped valuation when FY2026E cash was changed without a balancing entry.

### Show

- [`lab10_netflix.md`](lab10_netflix.md), “Three-year history,” “Historical ratios,” “Base-case assumption set,” “Five-year model results,” and “Check block and failure test.”
- [`netflix_proforma.py`](netflix_proforma.py), the base assumptions and `build_model()` if asked how the statements link.

### Plain-language terms

- **Pro-forma:** a forecast of future financial statements based on explicit assumptions.
- **FCFE:** free cash flow to equity, meaning residual cash attributable to common shareholders after debt-related cash flows.
- **Linked model:** changing an input recalculates all dependent statement lines instead of manually changing the final answer.
- **Accounting check:** assets must equal liabilities plus equity; a zero gap confirms that identity.

### Verify or decide myself

- The Lab 10 share count stays fixed even though the model includes annual buybacks. Mention this as a simplification.
- Ending cash reaches **$48,683.8 million** by FY2030E. Decide whether to call out the need to normalize or distribute excess cash in a more advanced model.

## Stop 4: valuation — 4:15

### Say: dedicated five-year DCF

- The dedicated DCF is an intrinsic valuation: it estimates value from forecast cash flow rather than from another company's trading multiple.
- It starts with **$10.204 billion of normalized 2026 free cash flow**, then applies growth of **12%, 10%, 8%, 6%, and 5% for 2027-2031**.
- It uses an **8.0% WACC** and **3.0% perpetual growth**. WACC means the blended return required by debt and equity investors. Perpetual growth is the assumed long-run growth after the explicit forecast.
- The present value of explicit cash flow is **$53.000 billion** and the present value of terminal value is **$211.860 billion**, giving enterprise value of approximately **$264.860 billion**.
- The enterprise-to-equity bridge subtracts approximately **$5.178 billion of net debt**: $14.309 billion of debt less $9.131 billion of cash and investments. That gives equity value of approximately **$259.7 billion**, or **$60.94 per diluted share** on **4.261 billion weighted-average diluted shares**.
- About **80.0% of enterprise value** comes from terminal value, so the result is highly sensitive to WACC and terminal growth.

### Say: dated valuation table

| Saved method or market observation | Date and information boundary | Value | Currency and share basis |
|---|---|---:|---|
| Dedicated five-year DCF | Formal valuation date **not explicitly labeled**; uses Q2 2026 balance-sheet data and September 2026 discount-rate inputs | **$60.94** | USD per diluted share; 4.261 billion weighted-average diluted shares |
| DCF reverse-DCF reference price | September 8, 2026, as identified by the peer-comparison file | **$78.05** | USD per share |
| Peer P/E median | September 10, 2026 comparison date | **$142.55** | USD per split-adjusted NFLX share; applies peer median P/E to FY2025 NFLX diluted EPS of $2.53 |
| NFLX market close used with peers | September 10, 2026 | **$76.01** | USD per split-adjusted share |
| Lab 10 linked FCFE valuation | Compared with market on September 23, 2026; model uses FY2025 opening data and FY2026E-FY2030E forecast | **$60.67** | USD per share; fixed 4,222.162150 million FY2025 period-end shares |
| NFLX market close used in Lab 10 | September 23, 2026 | **$71.36** | USD per split-adjusted share |

### Say: reverse DCF and held-fixed inputs

- A reverse DCF asks what performance is required to justify a market price; it does not predict that performance.
- To reach **$78.05**, the model adds **5.85 percentage points** to every explicit annual FCF growth rate. The implied rates are 17.8%, 15.8%, 13.8%, 11.8%, and 10.8% for 2027-2031.
- That raises the five-year FCF CAGR from **8.2% to about 14.0%** and produces 2031 FCF of **$19.662 billion**.
- The reverse DCF holds fixed normalized 2026 FCF of **$10.204 billion**, WACC of **8.0%**, terminal growth of **3.0%**, cash and investments of **$9.131 billion**, debt of **$14.309 billion**, and diluted shares of **4.261 billion**.

### Say: peers and method differences

- Disney was used because it has a substantial paid-video direct-to-consumer business and positive annual GAAP EPS, although parks, sports, networks, and other operations reduce comparability.
- WBD was only qualified. Its streaming exposure is relevant, but its $0.29 EPS includes a $2.945 billion debt-extinguishment gain and its price was merger-influenced.
- The two-peer median implies **$142.55**, but removing WBD leaves **$39.08** and removing Disney leaves **$246.02**. A $103.47 change when either peer is removed shows that the peer result is not stable.
- The methods differ because the DCF values Netflix's own future cash flow, the peer method applies market P/E ratios to Netflix's reported EPS, and the Lab 10 model discounts linked FCFE directly at the cost of equity. They also use different dates, cash-flow definitions, and share counts.
- I do **not** average them because averaging would hide those differences and create false precision.

### Show

- [`Netflix_DCF_Analysis.md`](Netflix-research/Netflix_DCF_Analysis.md), base case, sensitivity, reverse DCF, and reasonableness review.
- [`dcf.py`](Netflix-research/dcf.py), if asked for the calculation or held-fixed inputs.
- [`lab08_netflix_comparables.md`](md%20files/lab08_netflix_comparables.md), source table, peer decisions, DCF/peer comparison, and limitations.
- [`lab10_netflix.md`](lab10_netflix.md), valuation table and dated market comparison.

### Plain-language terms

- **DCF:** present value of forecast future cash flows.
- **WACC:** discount rate for cash flow available to both debt and equity investors.
- **Terminal value:** estimated value of all cash flows after the explicit forecast period.
- **Enterprise value:** value of the operating business available to capital providers.
- **Equity value:** value attributable to shareholders after the cash/debt bridge.
- **P/E:** share price divided by earnings per share.

### Verify or decide myself

- **Missing evidence:** confirm the formal valuation date of the dedicated $60.94 DCF before presenting it as a same-date comparison.
- **Internal DCF version conflict:** an older research follow-up reports approximately $61.01 using 8.5% WACC and 4.164 billion shares. Use the latest dedicated $60.94 DCF and state that the older version was not combined.
- The DCF calls its starting cash flow a practical FCFF proxy. Verify whether the instructor expects it to be presented strictly as FCFF; the Lab 10/Lab 11 model is clearly FCFE.
- The dated price pages are secondary market-data sources. If required, independently verify the September 8, 10, and 23 closes before final delivery.

## Stop 5: sensitivity — 2:30

### Say

- One-at-a-time sensitivity changes one independent input while holding every other independent assumption at its base value. Linked quantities still recalculate.
- Driver one was annual revenue growth for FY2026E-FY2030E. The lower path was **10%, 8%, 6%, 5%, 4%**; the base was **12%, 10%, 8%, 7%, 6%**; and the higher path was **14%, 12%, 10%, 9%, 8%**. Each changed year is two percentage points below or above base.
- Driver two was operating expenses as a percentage of gross profit. The lower path was **35.5%, 34.5%, 33.5%, 33.0%, 32.5%**; the base was **37.5%, 36.5%, 35.5%, 35.0%, 34.5%**; and the higher path was **39.5%, 38.5%, 37.5%, 37.0%, 36.5%**.

| Driver | FY2030E operating-profit span | FY2030E FCFE span | Value-per-share span |
|---|---:|---:|---:|
| Revenue growth | $6,985.0 million | $5,849.9 million | $18.14 |
| Operating expenses / gross profit | $1,435.1 million | $1,234.2 million | $4.22 |

- **Over these tested ranges**, revenue growth was the main driver for operating profit, FCFE, and value per share.
- For a traceable example, compare the base with higher revenue growth. FY2030E revenue rises from **$68,186.7 million to $74,703.5 million**. Gross profit rises from **$35,877.6 million to $41,406.1 million**. Operating profit rises by **$3,621.2 million**, FCFE rises by **$3,030.4 million**, and value per share rises from **$60.67 to $70.05**, a **$9.38** increase.
- All six cases passed the one-input isolation, balance-sheet, and minimum-cash checks. FCFE stayed positive, so valuation remained available.
- These scenarios do not establish probabilities. They show conditional model outputs if an assumption changes; they do not say how likely any path is.

### Show

- [`lab11_netflix.md`](lab11_netflix.md), “Exact selected ranges,” “Scenario results and signed changes,” “Visible accounting checks,” and “Statement-detail appendix.”
- [`lab11_netflix_sensitivity.py`](lab11_netflix_sensitivity.py), if asked how fresh base copies and one-input isolation were enforced.

### Plain-language terms

- **Percentage point:** the direct difference between percentages; moving from 12% to 14% is +2 percentage points.
- **Output span:** highest valid output minus lowest valid output across the tested cases.
- **Sensitivity is not probability:** it measures conditional impact, not likelihood.

### Verify or decide myself

- The saved “prediction” was recorded retrospectively after results were viewed. Do not describe it as a valid pre-run locked prediction.
- The Lab 11 report still has incomplete partner-verification fields. Do not claim that a partner checked the results unless that review occurs.

## Stop 6: interpretation — 1:15

### Say

- The evidence supports a conditional **watch-defer** conclusion. Netflix's operating performance is strong, but the $60.94 dedicated DCF and $60.67 linked FCFE model are below their respective dated market prices.
- The DCF can support approximately $78 only if Netflix delivers roughly 14% five-year FCF CAGR or benefits from a lower discount rate or higher terminal growth than the base case.
- The peer median does not overturn the conclusion because the peer set is small, diversified, and highly sensitive to WBD's weak recurring-earnings denominator.
- This is consistent with my initial view: the company merits further research, but valuation and risk evidence do not yet support initiation.
- Evidence that could change the conclusion includes stronger sustainable revenue and FCFE growth, better evidence that margin gains are durable, a more reliable peer set, a lower required return, or a market price that provides a clearer margin of safety.
- My next research priority is revenue-growth durability: membership and engagement, pricing power, advertising growth, churn, regional performance, and foreign exchange. I would also investigate normalized content cash spending because content commitments can limit flexibility.

### Show

- [`Project_1_Edition_A.md`](md%20files/Project_1_Edition_A.md), initial thesis and unknowns.
- [`Netflix_DCF_Analysis.md`](Netflix-research/Netflix_DCF_Analysis.md), conditional call.
- [`lab11_netflix.md`](lab11_netflix.md), interpretation and limitations.

### Plain-language terms

- **Conditional conclusion:** the conclusion holds only if the stated assumptions and evidence remain reasonable.
- **Research priority:** the uncertainty most worth investigating because it could change the decision.

### Verify or decide myself

- Decide which single next evidence item I would actually investigate first. The saved work supports revenue durability as the main priority, with content cash requirements as a second candidate.

## Timing check

| Segment | Time |
|---|---:|
| Opening conclusion | 0:45 |
| 1. Target selection | 1:15 |
| 2. Company and evidence | 2:00 |
| 3. Pro-forma | 3:00 |
| 4. Valuation | 4:15 |
| 5. Sensitivity | 2:30 |
| 6. Interpretation | 1:15 |
| **Total** | **15:00** |

## Preparation gaps to resolve

1. Confirm or explicitly label the formal valuation date for the dedicated $60.94 DCF.
2. Independently verify dated market closes if the assignment requires primary or approved price evidence.
3. Decide whether to add a truthful personal reason for selecting Netflix; none is documented.
4. Decide how to describe the dedicated DCF's cash flow: the saved file calls it normalized FCF used as a practical FCFF proxy, while Lab 10 and Lab 11 are clearly FCFE.
5. Do not present the retrospective Lab 11 prediction as a pre-run prediction.
6. Complete real partner verification and reflection separately; the saved partner fields are incomplete.
7. Add GitHub URLs after the final files are committed and pushed. No Git repository or remote was detected in the current course folder during earlier work.

## Files to link in the GitHub checkout

### Required Lab 12 files

- `lab12_netflix_presentation_notes.md`
- `lab12_netflix_review.md`

### Core evidence and reproducibility files

- `md files/Project_1_Edition_A.md`
- `Netflix-research/Netflix_2026-09-03_report.md`
- `Netflix-research/Netflix_2026-09-03_sources.md`
- `Netflix-research/Netflix_DCF_Analysis.md`
- `Netflix-research/dcf.py`
- `md files/lab08_netflix_comparables.md`
- `lab08_netflix_comparables.py`
- `lab10_netflix.md`
- `netflix_proforma.py`
- `lab11_netflix.md`
- `lab11_netflix_sensitivity.py`

