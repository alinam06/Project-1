# Sources, definitions, and challenges

AI-assisted revision prepared October 16, 2026. **Historical comparison price: January 23, 2026 close ($86.12). Claimed information cutoff: January 23 close — requires reconciliation with the after-close filing time.** This choice aligns with Edition A and avoids combining January financials with September discount-rate/price inputs. It is not an October 2026 recommendation. The available January information includes a pending WBD acquisition; standalone exclusion is a material condition, not a conclusion that the acquisition has zero value or risk. No subsequent termination fee or July guidance enters this valuation.

## Source register

| ID | Source | Period / evidence date | Use |
|---|---|---|---|
| N25 | [Netflix FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm) | FY ended Dec. 31, 2025; SEC accepted Jan. 23, 2026 **16:06:33 ET (after close)** | Item 8 statements, Notes 3/4/9/13; reported and normalized base |
| NE | [Netflix January 2026 earnings filing search](https://www.sec.gov/edgar/browse/?CIK=1065280&owner=exclude) | Jan. 20, 2026 earnings disclosure; precise source/values to verify | Potential pre-cutoff substitute for FY2025 figures (not assumed equivalent) |
| NR | Local `md files/Netflix_Latest_10-K.md`, `md files/lab10_netflix.md`, and 2023–2025 local filings | Historical research | Cross-reference to pre-existing extraction; original checked boxes are student records, not new manual verification by Alina |
| NP | [Yahoo NFLX history](https://finance.yahoo.com/quote/NFLX/history/), [FinanceCharts NFLX](https://www.financecharts.com/stocks/NFLX/summary/price) | Jan. 23, 2026 closing price; retrieved Oct. 16 | Both show $86.12; use close, not open |
| T | [US Treasury daily par curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026) | Jan. 23, 2026, 10-year column | 4.24% risk-free proxy; confirmed maturity heading, not a Treasury-bill rate |
| D25 | [Disney FY2025 results](https://thewaltdisneycompany.com/app/uploads/2025/11/q4-fy25-earnings.pdf) | Fiscal year ended Sept. 27, 2025; Nov. 13, 2025 release | pp. 14–15: annual EPS/revenue and cash/debt/NCI; report page numbering |
| DA | [Disney FY2025 annual report](https://investors.thewaltdisneycompany.com/files/doc_financials/2025/ar/2025-Annual-Report.pdf) | Cover: Nov. 5, 2025 share snapshot | 1,785,288,846 outstanding shares; dated share basis, not January count |
| DP | [Yahoo DIS history](https://finance.yahoo.com/quote/DIS/history/?p=DIS), [FinanceCharts DIS](https://www.financecharts.com/stocks/DIS/summary/price) | Jan. 23, 2026 close; retrieved Oct. 16 | $110.98 unadjusted close; Yahoo adjusted close $110.14 is a different field |

The financial facts and definition checks were checked by this AI assistant against primary issuer/Treasury sources. This is independent of the old model’s arithmetic, but it is **not a student AI-off check**. Market prices use named secondary providers. Their definitions were reconciled, and conflicting share estimates from market-cap providers were not imported. Preserve retrieved evidence/links in the final submission; public pages can change. No credentials or private account data are required. Sources are public; the repository need not redistribute copyrighted full third-party reports.

## Information-cutoff reconciliation — REQUIRED BEFORE FINALIZING

The SEC confirms that Netflix's FY2025 Form 10-K was accepted on **January 23, 2026 at 16:06:33 ET**, after the regular 4 p.m. market close. Thus, although the model compares its value with the **January 23 closing price of $86.12**, the 10-K cannot automatically be treated as information available *at* that close. Source: [SEC filing detail](https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/0001065280-26-000034-index.htm).

**Proposed remedy:** preserve the Edition A historical price/date, and build a dated disclosure matrix showing which material model inputs were published before the close (for example, from the January 20 earnings release) and which first appear in the after-close 10-K. Do **not** assume every detailed balance-sheet, content or tax figure was in the earlier release. If any material input was unavailable, either reconstruct a true close-of-day model using only pre-cutoff information **and rerun the results**, or clearly redefine this as a **post-filing retrospective analysis compared with the earlier January 23 close**, not an investable real-time 4 p.m. decision. Keep both versions distinguishable from unchanged Edition A. Do not silently relabel the cutoff.

### Historical Information-Cutoff Verification

**Valuation date:** January 23, 2026
**Information cutoff:** January 23, 2026, 4:00 p.m. ET

| Material input | First verified public source and publication time | Public by Jan. 23, 4 p.m. ET? | Decision / revised model location |
|---|---|---|---|
| FY2025 revenue and EBIT | Netflix Q4 2025 Financial Statements, January 20, 2026. Earnings release scheduled for approximately 4:01 p.m. ET; SEC 8-K accepted at 4:07:54 p.m. ET. | YES | Retain reported revenue of $45,183.036m and EBIT of $13,326.603m. Reference the January 20 earnings materials as the pre-cutoff source. |
| Brazil tax charge of $619m | Previously disclosed in Netflix's Q3 2025 reporting. Exact original disclosure and date require confirmation. | YES for the previously disclosed charge, subject to checking its exact definition. | Retain the existing normalization provisionally. Verify that the $619m adjustment matches the original disclosure and document why the full amount is removed. |
| Year-end cash and debt | Netflix Q4 2025 Financial Statements, January 20, 2026. SEC 8-K accepted at 4:07:54 p.m. ET. | YES | Retain December 31 cash of $9,033.681m and debt of $14,462.836m. Clearly identify these as December balances rather than January 23 balances. |
| Share counts | January 20 earnings materials disclose weighted-average basic and diluted shares. The FY2025 10-K supplies additional year-end share information on January 23 after 4 p.m. ET. | PARTIALLY VERIFIED | Review the 4,316.513150m diluted-share proxy. Confirm that its components were available before the cutoff or substitute a defensible pre-cutoff denominator. |
| Content assets and liabilities | Netflix Q4 2025 Financial Statements, January 20, 2026. | YES | Retain content assets of $32,778.392m and total content liabilities of $5,664.330m. Reference the January 20 balance sheet. |
| Content additions and amortization | Netflix Q4 2025 Financial Statements, January 20, 2026. | YES | Retain FY2025 content additions of $17,096.617m and content amortization of $16,422.166m. Reference the January 20 cash flow statement. |
| Expected FY2026 Brazil deposits | Netflix Q4 2025 Shareholder Letter, January 20, 2026. | YES | Retain the approximately $700m expected deposit in FY2026 cash flow. Confirm the accounting treatment and avoid treating the deposit as a second expense. |
| Disney financial metrics | Disney FY2025 earnings release, November 2025, and annual report published before January 2026. | YES | Retain as historical comparable-company information, subject to consistent share counts, definitions, and enterprise-value calculations. |
| Treasury yield | U.S. Treasury daily par yield curve, January 23, 2026. | VERIFY PUBLICATION TIME | Retain 4.24% as the model's dated 10-year Treasury input, but verify when the rate was published relative to the cutoff. |
| January 23 closing prices | Yahoo Finance and FinanceCharts historical closing-price records. | NO, not strictly before 4:00 p.m. ET | Retain NFLX $86.12 and DIS $110.98 as official-date closing-price references, with an explicit close-of-day pricing convention. |

### Information-Cutoff Assessment

The original financial model relied heavily on Netflix's
FY2025 Form 10-K, filed January 23, 2026, at 4:06:33 p.m. ET.

Although the filing occurred after the stated information cutoff,
Netflix had previously published its Q4 and FY2025 financial
statements on January 20, 2026.

The January 20 materials support the principal reported
financial statement figures, including revenue, EBIT,
cash, debt, content balances, additions, and amortization.

Therefore, these figures do not necessarily introduce
look-ahead bias, even though the revised model originally
referenced the later 10-K.

However, the diluted-share proxy and detailed disclosures
that first appeared in the 10-K require additional review.

The model also uses January 23 closing prices as its
historical pricing reference. These are close-of-day
observations rather than information available before
4:00 p.m. ET.

**Remaining verification:**
- Confirm the original disclosure of the $619m Brazil charge.
- Reconcile the diluted-share proxy to pre-cutoff information.
- Check whether any other model inputs rely exclusively on
  disclosures first published in the January 23 Form 10-K.
- Verify the publication timing of the Treasury yield.
- Confirm the final information and pricing convention.

**Model status:** Retain existing outputs provisionally
until the remaining timing and source checks are completed.
Any material input changes require rerunning the model
and updating the investment memorandum.| Disney metrics, Treasury yield, January closing prices | Listed source records; verify timestamps where needed | [VERIFY] | [YOUR INPUT] |

> **Analyst sign-off needed:** I reviewed the information available as of January 23, 2026. Inputs were available and I retained the information. 

## Input ledger

Amounts below are USD millions unless noted. N25 raw financial-statement amounts are USD thousands, divided by 1,000. Share data require their own stated units.

| Input group | Values used | Definition / transformation | Type / source |
|---|---|---|---|
| Operating history | Revenue 45,183.036; cost of revenues 23,275.329; operating expenses 8,581.104; EBIT 13,326.603 | Opex = marketing + technology/development + G&A; D&A embedded in functional expenses | Fact/derived, N25 p.39 |
| Content and D&A | Additions 17,096.617; amortization 16,422.166; other D&A 333.389 | Additions and content-liability changes determine cash content investment; content amortization remains an operating expense | Fact, N25 p.41 and Note 13 |
| Normalization | Brazil historical charge 619.0; expected deposit 700.0 | Remove only identified cumulative charge from recurring costs; model deposit separately in 2026 other assets/cash flow | Approximate filing amounts and analyst treatment, N25 Note 9 |
| Normalized cost driver | (23,275.329 − 16,422.166 − 619.0) / 45,183.036 = 13.7976% | Other operating costs/revenue; do not remove the entire annual increase in other costs | Derived |
| Opening assets | Cash 9,033.681; content 32,778.392; PP&E 2,004.350; other assets 11,780.570 | Other assets = reported total 55,596.993 less separately modeled categories | Fact/derived, N25 p.42 |
| Opening claims | Content liabilities 5,664.330; debt 14,462.836; other liabilities 8,854.339; equity 26,615.488 | Aggregate residual liabilities; debt is carrying value, used as a fair-value approximation | Fact/derived, N25 p.42 |
| Valuation cash | 9,033.681 + short-term investments 28.678 = 9,062.359 | Excludes restricted cash. Investment stays frozen within aggregate other assets in the pro-forma; no forecast investment income | Fact/analyst convention, N25 Note 4 |
| Share basis | 4,222.162150 basic + 94.351 incremental dilution = 4,316.513150 million | Year-end basic plus FY2025 weighted-average dilutive awards; a disclosed proxy, not a reported diluted spot count | Fact plus analyst construction, N25 cover/Note 3 |
| Historical income/cash reconciliation | See executable `base_reconciliation()` | Historical NI and CFO include reported interest/other income, deferred tax, SBC, working capital and FX; forecast is separately normalized | Fact/derived, N25 pp.39–42 |
| Disney reference | Revenue 94,425; EPS $6.85; cash 5,695; debt 42,026; book NCI 4,743; dated shares 1,785.288846m | FY2025 annual reported figures; full consolidated revenue requires a claim for NCI in EV | Fact, D25 and DA |
| Prices | NFLX $86.12; DIS $110.98 | Common Jan. 23, 2026 unadjusted closes; NFLX is already split-adjusted | Market facts, NP/DP |

The executable opening data are aggregate reported amounts, not a normalized balance-sheet restatement. The Brazil normalization changes recurring forecast costs; it does not erase existing liabilities or restore historical cash. Forecast operating cash assumes the expected deposit is paid in FY2026 and never refunded during the forecast; it is excluded from terminal investment as a one-time item. Recoverability and classification remain judgment risks.

## Major normalization and enterprise-to-equity judgments

### Brazil tax charge versus cash deposit

The model removes the **$619m cumulative Brazil-related charge** from the recurring FY2025 cost base, increasing normalized operating income, but does not rewrite the reported financial statements or erase opening liabilities. The model separately projects approximately **$700m in FY2026 deposits** as a cash outflow and corresponding other-asset movement, with no assumed refund. The accounting charge and deposit must not be casually added together as two independent permanent losses. Their precise classification, recoverability and subsequent treatment remain uncertain.

I removed the identified $619 million Brazil-related
charge from normalized operating income because it
represents a cumulative tax assessment rather than
an expense expected to recur at the same magnitude
each year.

However, part of the charge relates to FY2025,
and Netflix may incur additional related expenses.
The adjustment is therefore a normalization
assumption rather than a conclusion that all
Brazil-related tax costs are nonrecurring.

I retained approximately $700 million in expected
FY2026 deposits in projected cash flow to recognize
the anticipated cash requirement.

### Operating tax versus reported effective tax

I used a normalized operating tax rate of 21%
rather than Netflix's reported FY2025 effective
tax rate of approximately 13.69%.

The 21% assumption reflects the U.S. federal
statutory corporate income tax rate and serves
as a conservative normalized proxy.

Netflix's reported effective tax rate may
reflect geographic differences, tax credits,
and temporary or unusual tax effects.

I recognize that 21% does not incorporate
all company-specific tax characteristics.

The model's sensitivity analysis indicates
that reducing the operating tax rate to 14%
increases estimated value from $51.20 to
$55.95 per share.

### Cash availability in the equity bridge

The enterprise-to-equity bridge adds $9.062
billion in cash and eligible investments
and subtracts approximately $14.463 billion
in debt.

I recognize that not all unrestricted cash
may be economically available to shareholders
because Netflix requires liquidity to fund
ongoing operations and content investment.

The model separately maintains a $5 billion
liquidity floor.

Excluding $5 billion from the equity bridge
would reduce the estimated value by
approximately $1.16 per share.

This sensitivity does not change my
WATCH–DEFER recommendation.

## Driver record: value · basis · challenge · evidence that changes it

Every future value is an analyst proposal for Alina to review. Historical support is an anchor, not proof of the forecast.

| Driver and value | Basis | Strongest challenge | Evidence that changes it |
|---|---|---|---|
| Revenue growth 12/10/8/7/6% | Preserves existing lab judgment; FY2025 growth about 16%; larger scale makes sustained percentage growth harder | Advertising and pricing may not offset slower customer growth | Subsequent reported growth, price/retention evidence and disclosed monetization; re-underwrite below 10% in first forecast year |
| Content additions 8/7/6/5/4%; amortization same path | Preserves lab schedule; tests spreading content over a larger revenue base | Lower investment growth may weaken the slate; additions and amortization need not move together | Content cash payments, slate/engagement evidence, actual amortization and liability changes |
| Other costs/revenue 13.7976% | Normalized historical ratio after $619m charge | Brazil taxes could recur; residual costs may scale differently | New assessments or recurring expenses above normalized ratio |
| Opex/gross profit 37.5/36.5/35.5/35/34.5% | Existing forecast; reported FY2025 about 39.17% | Assumes substantial operating leverage while content also gains scale | Marketing/technology/G&A growth persistently above the forecast; use sticky-cost low case |
| D&A/opening PP&E 20.9184%; capex $700m/year | Historical D&A ratio; capex near $688.220m historical spending | D&A includes intangibles; flat capex may understate future infrastructure needs | Actual capex plans, asset mix/useful-life changes; rebuild schedule rather than merely adjusting value |
| Other-asset investment 5% of revenue change | Preserves prior simplification; adds explicit $700m Brazil deposit | Aggregate assets hide working-capital and tax movements; liabilities held flat | Cash conversion and detailed working-capital/tax disclosures |
| Content liabilities/content assets 17.2807% approximately | Opening reported ratio; exact code uses unrounded ratio | Supplier payment terms or FX change the ratio | Actual content-payment timing and liability roll-forward |
| Operating tax 21% | US statutory rate as transparent normalized proxy | Reported FY2025 effective rate is about 13.69%; geographic mix and credits matter | Sustainable tax reconciliation/cash taxes. At 14% forecast tax, model value is $55.95, not $51.20 |
| Interest about 4.9831%; debt repayment $1bn/year | Historical interest/opening debt; retained illustrative repayment policy | Refinancing, maturity schedule and acquisition financing differ | Dated debt schedules; financing does not change unlevered EV under the model's tax convention |
| Distributions $6bn/year | Replaces old buyback assumption with a generic cash payout so fixed shares do not imply free repurchase gains | Not an actual capital-return forecast | Adopt an explicit buyback-price/share schedule if buybacks are modeled; do not retain fixed shares and claim accretion |
| Cash floor $5bn; all unrestricted cash additive in bridge | Retains liquidity check; shows optimistic cash availability explicitly | Some cash is necessary to operate | Reserve cash evidence; excluding $5bn lowers all values by about $1.16/share |
| SBC treated as cash replacement compensation | Expense retained, no SBC cash add-back, no future dilution benefit | Cash forecast differs from actual share-based compensation mechanics | Build award issuance/exercise and dilution schedules if material |
| WACC 9%, grid 8–10% | CAPM-style cost of equity 4.24% + 1.0×5%=9.24%; debt cost 4.24%+1.25%=5.49%; 21% interest tax shield; actual basic market-equity weight gives 9.0524%, rounded | Beta 1, ERP 5%, spread 1.25% are assumptions, not verified company market estimates | Independent dated beta/ERP/bond evidence; retain the grid while unresolved |
| Terminal growth 3%, terminal ROIC 15% | Nominal maturity assumption plus explicit reinvestment: g/ROIC = 20% of terminal NOPAT | No guarantee of durable 15% incremental returns or immediate transition | Long-run reinvestment economics. ROIC 10% gives $46.28, 20% gives $53.67 at base WACC/g |
| Diluted proxy 4,316.513150m | Adds existing award allowance to latest year-end basic shares | Weighted-average award dilution is not spot dilution | Actual dated diluted cap table; basic-only value is $52.35 |

Exact ratios are calculated in `model.py`; rounded prose is for speaking. Five-year operating case ranges and cost assumptions are analyst-selected challenges, not confidence intervals. The separate structural case assumes growth 2/1/0/0/0%, continued elevated content investment, 42% opex/gross profit, higher other costs, 10% WACC/2% g/7% terminal ROIC, and no payouts. This is a thesis-break illustration, not an assigned probability.

## Additional valuation-parameter rationale

### Revenue and operating leverage

The forecast **12/10/8/7/6%** annual revenue growth path preserves prior lab judgment and moderates from approximately **16% FY2025 growth**. Increasing scale is a plausible reason for deceleration, but is **not independent evidence** for exact percentages. Revenue growing faster than content additions and declining opex/gross-profit ratios together imply considerable margin expansion to **35.4% EBIT margin in FY2030**. [YOUR INPUT: cite pre-cutoff guidance and historical growth; explain the 2026 assumption and subsequent fade.] [YOUR INPUT: explain what advertising, pricing, customer retention and content economics would cause a base-case change.]

### WACC assumptions

**CAPM-style cost of equity:** 4.24% 10-year Treasury proxy + **1.0 beta × 5% assumed ERP** = **9.24%**. **Pretax borrowing cost:** 4.24% + **1.25% assumed debt spread** = **5.49%**. With approximately **96.17% equity / 3.83% debt** and a **21% interest tax shield**, the saved calculation gives **9.0524%**, rounded to **9%**. The Treasury yield is a dated market observation; **beta, ERP and spread are deliberately assumed, not Netflix-specific estimates independently verified at cutoff**.

### Additional Beta Research — Yahoo Finance

As part of my review of the model's WACC assumptions,
I consulted Yahoo Finance's Netflix statistics.

Yahoo Finance displayed a five-year monthly beta
of 1.61 when accessed on October 17, 2026.

This is higher than the beta of 1.00 originally
assumed in my financial model.

Using the model's existing 4.24% risk-free rate
and 5% equity risk premium, a beta of 1.61
produces a CAPM cost of equity of 12.29%,
compared with 9.24% using beta of 1.00.

Holding the existing financing weights, debt
cost, and tax assumptions constant, estimated
WACC would increase from approximately
9.05% to 11.99%.

However, the currently displayed Yahoo Finance
beta may incorporate information after the
January 23, 2026 valuation cutoff.

For this reason, I do not treat 1.61 as a
verified historical beta for January 23, 2026.

I will use this observation as evidence that
the valuation is sensitive to systematic-risk
assumptions and will seek a beta estimate based
only on data available by the historical cutoff.

Source: Yahoo Finance, Netflix (NFLX), Beta (5Y Monthly).
https://finance.yahoo.com/quote/NFLX/

Accessed: October 17, 2026.

### Terminal growth and ROIC

A **3% nominal perpetual growth** assumption represents a mature-state scenario, not a reported company forecast. **15% terminal ROIC** implies reinvestment = `3% / 15% = 20%` of terminal NOPAT, so terminal growth is not free. A 15% incremental return forever requires sustained franchise economics; it is a consequential judgment given the large terminal-value share. At base WACC/g, modeled terminal ROIC **10% → $46.28**, **15% → $51.20**, **20% → $53.67** per share. [YOUR INPUT: calculate/locate historical ROIC with a consistent invested-capital denominator, describe the relevance to *incremental* terminal ROIC, and justify or revise 15%.] [YOUR INPUT: justify 3% nominal growth relative to long-run economy/inflation assumptions without treating it as certain.]

## Peer policy and definitions

Retain the existing preselection business policy: substantial paid-video/DTC exposure, public issuer, available positive annual GAAP EPS, with diversification qualified. This revision applies the January cutoff consistently. The record does not claim the expanded EV calculation policy was historically precommitted; it is an Edition B extension to the existing policy.

- Disney: qualified due to parks, sports, linear networks, and tax effects. Annual periods differ from Netflix. The cover share snapshot is dated November 5; balance-sheet figures are September 27. These are lagged public observations, not January measurements.
- WBD: exclude from the revised January P/E calculation because FY2025 EPS used in the September lab was not public at the January cutoff. Transaction exposure also weakens ordinary trading comparisons. The old $142.55 median remains prior work only.
- EV/revenue = (dated price × latest verified basic shares + carrying debt + book NCI − cash − short-term investments) / annual consolidated revenue. Disney has no separate short-term investment subtraction in the extracted balance sheet; its long-term investments are not netted. Netflix's target EV/revenue also uses basic shares for consistency; diluted intrinsic value still uses the disclosed diluted proxy.
- Operating leases stay in operating costs and are excluded from financing debt consistently. NCI is included at book as a proxy, not independently measured fair value. Other non-operating investments are not netted; this limits interpretation.
- P/E uses closing price / reported annual diluted GAAP EPS. It is an equity multiple: do not apply a second cash/debt bridge.
- There is one qualified peer, so show separate references, not a peer median/range. EV/revenue ignores margin differences; P/E inherits tax and earnings-quality differences. Do not average them with the DCF.

No transaction multiple is offered. Control, synergy, financing and pending-deal context are not sufficiently underwritten here to use acquisition terms as valuation evidence.

### Dated original peer-selection record — analyst to complete
- **Criteria demonstrably written before choosing peers:** Lab 08
- **Edition B changes:** consistent January cutoff, qualified Disney multiples and the expanded EV/revenue bridge.

## AI output evaluated against evidence

**Output qualified/corrected:** the earlier standalone model called management FCF a practical FCFF proxy and applied WACC; the linked lab separately valued FCFE.

**Independent evidence used:** N25 separately presents operating cash flow, capital purchases, and interest expense; its operating cash is not an unlevered operating-profit measure. Note 13's operating-cost presentation also reconciles EBIT without an additional separate D&A deduction.

**Disposition in this revision:** replace the proxy with an operating FCFF schedule, verify FCFF against FCFE less net borrowing plus after-tax interest, and retain depreciation inside functional costs while adding noncash D&A once in cash flow. This is an AI-assisted correction documented October 16, not a claim that Alina independently completed this review. She should explain and verify it herself before the defense.


### Student review of the AI-assisted FCFF correction — pending

The documented earlier error was treating management-reported FCF as an FCFF proxy while applying WACC, and separately mixing FCFE treatment. The revised model uses an operating FCFF construction, adds back embedded noncash depreciation/amortization once and maintains an explicit financing bridge. The technical explanation is **not** a substitute for a genuine student check.

| Review item | Student-completed evidence |
|---|---|
| Verification Item | Analyst Response |
|---|---|
| What I examined without relying solely on Codex | I reviewed the revised FCFF calculation in `model.py` and compared its methodology with the corporate finance formulas covered in class. I examined how the model calculates operating income, accounts for depreciation, and converts operating earnings into free cash flow. 
| Independent source or calculation | I used Netflix's FY2025 Form 10-K, specifically the consolidated income statement and statement of cash flows, to examine reported operating income, depreciation, capital expenditures, and interest expense. I compared the model's methodology with the FCFF formula: FCFF = EBIT × (1 − Tax Rate) + D&A − Capital Expenditures − Change in Net Working Capital. 
| Result and any discrepancy |  The revised methodology is consistent with an unlevered FCFF approach because it begins with after-tax operating income rather than treating management-reported free cash flow as FCFF. I also checked that depreciation was not deducted twice. However, the accuracy of the final valuation still depends on the model's assumptions regarding content investment, working capital, and taxes. 
| Changes made to model or memo | No additional model changes were made following my review. The previously documented AI-assisted correction was retained. I added this independent verification explanation to `SOURCES_AND_ASSUMPTIONS.md`. 
| Remaining uncertainty | Although the FCFF methodology is conceptually appropriate, the forecast relies on estimates of future content spending, working capital, tax rates, and operating efficiency. These assumptions could materially affect projected cash flows and the resulting intrinsic valuation. 
**Integrity note:** Do not label this AI-off or independently verified unless that is what actually occurred. Preserve original Edition A, genuine pre-run predictions, partner challenges and recorded cold runs as separate evidence; this ledger does not reconstruct them.

## Final analyst review checklist

- [ ] Resolve **after-close 10-K** versus January 23 close cutoff and reconcile model outputs.
- [ ] Approve/revise Brazil full-charge normalization and corresponding cash deposit treatment.
- [ ] Provide dated support for forecast growth, the 21% tax proxy and WACC inputs.
- [ ] Defend 3% terminal growth, 15% ROIC and opening cash/debt treatment.
- [ ] Locate original **dated** comparable selection rule; disclose later additions.
- [ ] Complete genuine student verification of the FCFF correction and document actual evidence.
- [ ] Check that `model.py`, `results.json`, `visible_results.md`, memo and scripts agree after any revisions.
