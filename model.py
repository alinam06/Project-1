"""Offline Netflix standalone FCFF model; all money/shares in USD millions.

Run: python3 model.py. Writes visible_results.md and results.json beside script.
AI-assisted Edition B revision, not a locked human prediction or course benchmark.
"""
from copy import deepcopy
from dataclasses import dataclass, replace, asdict
from datetime import datetime, timezone
from pathlib import Path
import json
import math
import sys

ROOT = Path(__file__).resolve().parent
VALUATION_DATE = "2026-01-23"
PRICE = 86.12
BASIC_SHARES = 4222.162150
DILUTION_ALLOWANCE = 94.351
SHARES = BASIC_SHARES + DILUTION_ALLOWANCE
INVESTMENTS = 28.678
OPENING = dict(revenue=45183.036, cash=9033.681, content_assets=32778.392,
               ppe=2004.350, other_assets=11780.570,
               content_liabilities=5664.330, debt=14462.836,
               other_liabilities=8854.339, equity=26615.488)
FY25 = dict(revenue=45183.036, cost=23275.329, amort=16422.166,
            additions=17096.617, da=333.389, opex=8581.104,
            ebit=13326.603, interest=776.510, other_income=172.459,
            pretax=12722.552, tax=1741.351, net_income=10981.201,
            cfo=10149.273, capex=688.220, brazil_charge=619.0)
NORMALIZED_OTHER_COST_RATIO = (FY25['cost']-FY25['amort']-FY25['brazil_charge'])/FY25['revenue']
CONTENT_LIABILITY_RATIO = OPENING['content_liabilities']/OPENING['content_assets']
DA_RATE = FY25['da']/1593.756
RF, BETA, ERP, CREDIT_SPREAD, MARGINAL_TAX = .0424, 1., .05, .0125, .21
MARKET_EQUITY = PRICE*BASIC_SHARES
DEBT_WEIGHT = OPENING['debt']/(MARKET_EQUITY+OPENING['debt'])
CALCULATED_WACC = (1-DEBT_WEIGHT)*(RF+BETA*ERP)+DEBT_WEIGHT*(RF+CREDIT_SPREAD)*(1-MARGINAL_TAX)


@dataclass(frozen=True)
class Assumptions:
    growth: tuple = (.12,.10,.08,.07,.06)
    content_growth: tuple = (.08,.07,.06,.05,.04)
    amort_growth: tuple = (.08,.07,.06,.05,.04)
    opex_gp: tuple = (.375,.365,.355,.350,.345)
    other_cost_ratio: float = NORMALIZED_OTHER_COST_RATIO
    tax: float = .21
    capex: float = 700.
    other_asset_growth: float = .05
    debt_repayment: float = 1000.
    interest_rate: float = 776.510/(1784.453+13798.351)
    distribution: float = 6000.
    brazil_deposit: float = 700.
    minimum_cash: float = 5000.
    wacc: float = .09
    terminal_g: float = .03
    terminal_roic: float = .15


BASE = Assumptions()
CASES = {
    'low': replace(BASE, growth=(.10,.08,.06,.05,.04),
                   content_growth=(.10,.09,.08,.07,.06),
                   opex_gp=(.395,.385,.375,.370,.365)),
    'base': BASE,
    'high': replace(BASE, growth=(.14,.12,.10,.09,.08),
                    opex_gp=(.355,.345,.335,.330,.325)),
    'structural_impairment': replace(BASE, growth=(.02,.01,.00,.00,.00),
                    content_growth=(.10,.09,.08,.07,.06),
                    opex_gp=(.42,.42,.42,.42,.42),
                    other_cost_ratio=NORMALIZED_OTHER_COST_RATIO+.01,
                    distribution=0., wacc=.10, terminal_g=.02, terminal_roic=.07)
}


def close(actual, expected, label, tol=1e-6):
    if not math.isfinite(actual) or abs(actual-expected)>tol:
        raise ValueError(f'{label}: {actual} != {expected}')


def gap(r):
    return sum(r[k] for k in ('cash','content_assets','ppe','other_assets'))-sum(r[k] for k in ('content_liabilities','debt','other_liabilities','equity'))


def validate(a):
    for key in ('growth','content_growth','amort_growth','opex_gp'):
        seq=getattr(a,key)
        if len(seq)!=5 or not all(math.isfinite(x) for x in seq):
            raise ValueError(f'{key}: exactly five finite inputs required')
    if any(x<=-1 for seq in (a.growth,a.content_growth,a.amort_growth) for x in seq):
        raise ValueError('growth must exceed -100%')
    if not 0<=a.tax<1 or not 0<=a.terminal_g<min(a.wacc,a.terminal_roic):
        raise ValueError('require 0 <= terminal g < WACC and ROIC; valid tax')
    if not all(0<=x<1 for x in a.opex_gp):
        raise ValueError('opex/gross profit outside [0,1)')
    if min(a.capex,a.distribution,a.debt_repayment,a.brazil_deposit)<0:
        raise ValueError('investment/distribution/repayment inputs must be nonnegative')


def forecast(a=BASE):
    validate(a)
    old=dict(OPENING)
    additions, amort=FY25['additions'], FY25['amort']
    rows=[]
    for i,year in enumerate(range(2026,2031)):
        r={'year':year, 'opening_cash':old['cash']}
        r['revenue']=old['revenue']*(1+a.growth[i])
        additions*=1+a.content_growth[i]
        amort*=1+a.amort_growth[i]
        r.update(additions=additions,amort=amort)
        r['other_cost']=r['revenue']*a.other_cost_ratio
        r['cost']=amort+r['other_cost']
        r['gross_profit']=r['revenue']-r['cost']
        r['opex']=r['gross_profit']*a.opex_gp[i]
        # D&A is already embedded in these GAAP-based functional expenses.
        r['ebit']=r['gross_profit']-r['opex']
        r['da']=old['ppe']*DA_RATE
        r['interest']=old['debt']*a.interest_rate
        r['pretax']=r['ebit']-r['interest']
        r['tax']=max(0.,r['pretax'])*a.tax
        r['net_income']=r['pretax']-r['tax']
        r['content_assets']=old['content_assets']+additions-amort
        r['content_liabilities']=r['content_assets']*CONTENT_LIABILITY_RATIO
        r['change_content_liabilities']=r['content_liabilities']-old['content_liabilities']
        r['ppe']=old['ppe']+a.capex-r['da']
        r['deposit']=a.brazil_deposit if i==0 else 0.
        r['change_other_assets']=a.other_asset_growth*(r['revenue']-old['revenue'])+r['deposit']
        r['other_assets']=old['other_assets']+r['change_other_assets']
        r['debt_repayment']=min(a.debt_repayment,old['debt'])
        r['net_borrowing']=-r['debt_repayment']
        r['debt']=old['debt']+r['net_borrowing']
        r['other_liabilities']=old['other_liabilities']
        # Cash replacement of SBC is assumed; no SBC add-back or future dilution benefit.
        r['distribution']=a.distribution
        r['equity']=old['equity']+r['net_income']-r['distribution']
        r['cfo']=r['net_income']+r['da']+amort-additions-r['change_other_assets']+r['change_content_liabilities']
        r['cfi']=-a.capex
        r['cff']=r['net_borrowing']-r['distribution']
        r['cash']=old['cash']+r['cfo']+r['cfi']+r['cff']
        r['fcfe']=r['cfo']-a.capex+r['net_borrowing']
        r['nopat']=r['ebit']-max(0.,r['ebit'])*a.tax
        r['fcff']=r['nopat']+r['da']+amort-additions-a.capex-r['change_other_assets']+r['change_content_liabilities']
        # Exact bridge also works when interest tax shields cannot be used immediately.
        r['interest_after_tax']=r['interest']-(max(0.,r['ebit'])*a.tax-r['tax'])
        rows.append(r)
        old=r
    check_statements(rows,a)
    return rows


def check_statements(rows,a=BASE):
    close(gap(OPENING),0,'opening balance sheet')
    for r in rows:
        close(gap(r),0,f"{r['year']} balance sheet")
        close(r['cash']-r['opening_cash'],r['cfo']+r['cfi']+r['cff'],f"{r['year']} cash tie")
        close(r['fcff'],r['fcfe']-r['net_borrowing']+r['interest_after_tax'],f"{r['year']} FCFF/FCFE bridge")
        if r['cash']<a.minimum_cash or min(r['content_assets'],r['ppe'],r['debt'])<0:
            raise ValueError(f"{r['year']} liquidity/asset/debt constraint")


def discount_cashflows(cashflows, terminal_cashflow, wacc, growth):
    if not math.isfinite(wacc) or not math.isfinite(growth) or wacc<=growth or wacc<=-1:
        raise ValueError('invalid discount rates')
    if not cashflows or not all(math.isfinite(x) for x in (*cashflows,terminal_cashflow)):
        raise ValueError('finite cash flows required')
    pv=sum(cf/(1+wacc)**t for t,cf in enumerate(cashflows,1))
    terminal_value=terminal_cashflow/(wacc-growth)
    return pv,terminal_value,terminal_value/(1+wacc)**len(cashflows)


def value(rows,a=BASE, cash_adjustment=0., debt_adjustment=0.):
    validate(a)
    check_statements(rows,a)
    # Terminal operating earnings grow at g; incremental investment earns ROIC.
    terminal_nopat=rows[-1]['nopat']*(1+a.terminal_g)
    terminal_fcff=terminal_nopat*(1-a.terminal_g/a.terminal_roic)
    if terminal_fcff<=0:
        raise ValueError('terminal FCFF must be positive; explicit negative FCFF is allowed')
    pv,tv,pv_tv=discount_cashflows([r['fcff'] for r in rows],terminal_fcff,a.wacc,a.terminal_g)
    ev=pv+pv_tv
    eligible_cash=OPENING['cash']+INVESTMENTS+cash_adjustment
    debt=OPENING['debt']+debt_adjustment
    equity=ev+eligible_cash-debt
    return dict(pv_explicit=pv,terminal_nopat=terminal_nopat,terminal_fcff=terminal_fcff,
                terminal_value=tv,pv_terminal=pv_tv,ev=ev,eligible_cash=eligible_cash,
                debt=debt,equity=equity,shares=SHARES,price=equity/SHARES,
                terminal_share=pv_tv/ev)


def reverse_dcf():
    # Solve a uniform revenue-growth shift, not a free-standing FCF growth override.
    low,high=-.02,.15
    def evaluate(shift):
        a=replace(BASE,growth=tuple(g+shift for g in BASE.growth))
        return value(forecast(a),a)['price']
    if not evaluate(low)<=PRICE<=evaluate(high):
        raise ValueError('reverse DCF target outside bracket')
    for _ in range(80):
        mid=(low+high)/2
        if evaluate(mid)<PRICE: low=mid
        else: high=mid
    shift=(low+high)/2
    a=replace(BASE,growth=tuple(g+shift for g in BASE.growth))
    rows=forecast(a)
    return dict(shift=shift,growth=a.growth,price=value(rows,a)['price'],
                revenue_2030=rows[-1]['revenue'],fcff_2030=rows[-1]['fcff'])


def peer_reference():
    # One qualified peer. Pre-existing business policy retained; no post-Jan EPS.
    # Disney cover shares: November 5, 2025; latest verified pre-cutoff snapshot.
    dis=dict(price=110.98,shares_snapshot=1785.288846,cash=5695.,debt=42026.,nci=4743.,
             revenue=94425.,eps=6.85)
    ev=dis['price']*dis['shares_snapshot']+dis['debt']+dis['nci']-dis['cash']
    ev_sales=ev/dis['revenue']
    pe=dis['price']/dis['eps']
    target_ev=ev_sales*FY25['revenue']
    return dict(disney=dis,ev=ev,ev_sales=ev_sales,pe=pe,
                pe_implied=pe*2.53,
                ev_sales_implied=(target_ev+OPENING['cash']+INVESTMENTS-OPENING['debt'])/SHARES,
                netflix_pe=PRICE/2.53,
                netflix_ev_sales=(PRICE*BASIC_SHARES+OPENING['debt']-OPENING['cash']-INVESTMENTS)/FY25['revenue'])


def base_reconciliation():
    close(FY25['revenue']-FY25['cost']-FY25['opex'],FY25['ebit'],'reported EBIT')
    close(FY25['ebit']-FY25['interest']+FY25['other_income'],FY25['pretax'],'reported pretax')
    close(FY25['pretax']-FY25['tax'],FY25['net_income'],'reported NI')
    cfo=FY25['net_income']-FY25['additions']-610.838+FY25['amort']+FY25['da']+368.449+72.348+577.451-442.056-790.661-8.039+881.218+254.917-793.655
    close(cfo,FY25['cfo'],'reported CFO')
    close(10149.273+1041.688-10345.623+386.519,1231.857,'reported cash movement incl restricted cash/FX')
    close(7807.337+1231.857,9039.194,'reported closing cash incl restricted')
    close(gap(OPENING),0,'reported BS')
    normalized_ebit=FY25['ebit']+619.
    # Apply a consistent normalized operating tax, not the reported NI tax rate.
    norm_nopat=normalized_ebit*(1-BASE.tax)
    normalized_fcff=norm_nopat+FY25['da']+FY25['amort']-FY25['additions']-FY25['capex']-610.838
    # Non-content working capital/noncash historical adjustments shown explicitly.
    residual=FY25['cfo']-(FY25['net_income']+FY25['da']+FY25['amort']-FY25['additions']-610.838)
    return dict(reported_ebit=FY25['ebit'],normalized_ebit=normalized_ebit,
                normalized_nopat=norm_nopat,normalized_fcff_reference=normalized_fcff,
                reported_cfo=FY25['cfo'],other_cfo_adjustments=residual,
                reported_fcf=FY25['cfo']-FY25['capex'],
                normalized_other_cost_ratio=NORMALIZED_OTHER_COST_RATIO)


def run_checks():
    checks=[]
    base_reconciliation(); checks.append('PASS: reported FY2025 IS/BS/CF arithmetic and cash/FX reconciliation')
    rows=forecast(); v=value(rows)
    checks.append('PASS: five annual BS balances, cash ties, FCFF/FCFE bridges')
    # Independent synthetic perpetuity: five 100 cash flows and 1000 terminal EV.
    pv,_,pv_tv=discount_cashflows([100]*5,100,.10,0.)
    synthetic=pv+pv_tv
    close(synthetic,1000.,'synthetic perpetuity'); checks.append('PASS: synthetic known answer $1,000 EV (not the official course benchmark)')
    for g in (.02,.03,.04):
        prices=[value(rows,replace(BASE,wacc=w,terminal_g=g))['price'] for w in (.08,.09,.10)]
        if not prices[0]>prices[1]>prices[2]: raise ValueError('WACC monotonicity')
    for w in (.08,.09,.10):
        prices=[value(rows,replace(BASE,wacc=w,terminal_g=g))['price'] for g in (.02,.03,.04)]
        if not prices[0]<prices[1]<prices[2]: raise ValueError('growth monotonicity')
    checks.append('PASS: WACC/growth monotonicity over the 3x3 valid grid')
    for kwargs in ({'terminal_g':.09},{'wacc':float('nan')},{'terminal_roic':.02}):
        try: value(rows,replace(BASE,**kwargs))
        except ValueError: pass
        else: raise AssertionError('boundary not rejected')
    checks.append('PASS: invalid terminal/rate boundary inputs rejected')
    for broken_key in ('cash','fcff'):
        broken=deepcopy(rows); broken[0][broken_key]+=100
        try: value(broken)
        except ValueError: pass
        else: raise AssertionError(f'{broken_key} corruption not rejected')
    checks.append('PASS: cash corruption and FCFF corruption each block valuation')
    close((value(rows,debt_adjustment=100)['equity']-v['equity']),-100,'debt bridge')
    close((value(rows,cash_adjustment=100)['equity']-v['equity']),100,'cash bridge')
    financing=replace(BASE,debt_repayment=0.,distribution=0.)
    close(value(forecast(financing),financing)['ev'],v['ev'],'financing invariance')
    checks.append('PASS: +$100m debt/cash bridge; FCFF EV invariant to financing distributions')
    unnormalized=replace(BASE,other_cost_ratio=(FY25['cost']-FY25['amort'])/FY25['revenue'])
    if value(forecast(unnormalized),unnormalized)['price']>=v['price']: raise AssertionError('normalization direction')
    checks.append('PASS: retaining Brazil charge reduces value; normalization does not manufacture cash')
    for name,a in CASES.items(): value(forecast(a),a)
    checks.append('PASS: all four named scenarios articulate and satisfy liquidity constraints')
    close(reverse_dcf()['price'],PRICE,'reverse DCF',1e-6)
    checks.append('PASS: revenue-driven reverse DCF reaches dated target')
    p=peer_reference()
    close(p['pe'],110.98/6.85,'peer EPS definition')
    close(p['ev'],110.98*1785.288846+42026+4743-5695,'peer EV definition')
    checks.append('PASS: peer price/EPS and equity+debt+NCI-cash definitions (dated cover shares; book NCI proxy)')
    return checks


def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(x) for x in row)+' |' for row in rows])


def main():
    checks=run_checks()
    results={name:dict(assumptions=asdict(a),statements=forecast(a),valuation=value(forecast(a),a)) for name,a in CASES.items()}
    base=results['base']; rows=base['statements']; v=base['valuation']
    grid=[dict(wacc=w,g=g,price=value(rows,replace(BASE,wacc=w,terminal_g=g))['price']) for g in (.02,.03,.04) for w in (.08,.09,.10)]
    report=['# Netflix revised standalone FCFF results',
      '\nValuation/information boundary: January 23, 2026. Historical standalone case; not an October 2026 trade recommendation. USD millions except USD/share. Annual year-end discount convention t=1…5 for FY2026–2030; 23-day date approximation disclosed. Prepared with AI assistance.',
      '\n## Decision and cases',
      '\nWorking committee action: WATCH–DEFER. Do not initiate at the $86.12 dated close from this standalone evidence. The pending WBD transaction is excluded and separately blocks a consolidated investment conclusion.',
      table(['Case','FY2030 revenue','FY2030 EBIT','FY2030 FCFF','Value/share','Terminal share'],[[name,*[f"{r['statements'][-1][k]:,.2f}" for k in ('revenue','ebit','fcff')],f"${r['valuation']['price']:.2f}",f"{r['valuation']['terminal_share']:.1%}"] for name,r in results.items()]),
      '\nLow/base/high use the same 9% WACC, 3% terminal growth, 15% terminal ROIC. Structural impairment also changes WACC to 10%, growth to 2%, ROIC to 7%, and stops distributions; it is a separate thesis-break case, not the range endpoint of the ordinary operating cases.',
      '\n## Base enterprise-to-equity bridge',
      table(['Item','Value'],[[k,f'{x:,.4f}'] for k,x in v.items()]),
      f'\nCalculated WACC: {CALCULATED_WACC:.4%}; used 9.0% rounded to nearest 0.5 percentage point. Rf 4.24% verified Treasury; beta 1.0, ERP 5.0%, spread 1.25% are analyst assumptions. Debt weight {DEBT_WEIGHT:.2%}.',
      f'\nDiluted proxy: {BASIC_SHARES:,.6f}m year-end basic + {DILUTION_ALLOWANCE:,.3f}m FY2025 incremental diluted awards = {SHARES:,.6f}m. Not a reported point-in-time diluted count. Basic-only price: ${v["equity"]/BASIC_SHARES:.2f}.',
      '\n## Five-year statements',
      table(['Line']+[str(r['year']) for r in rows],[[key]+[f'{r[key]:,.3f}' for r in rows] for key in ('revenue','cost','gross_profit','opex','ebit','interest','pretax','tax','net_income','cash','content_assets','ppe','other_assets','content_liabilities','debt','other_liabilities','equity','additions','amort','da','deposit','change_other_assets','change_content_liabilities','cfo','cfi','cff','opening_cash','distribution','fcfe','nopat','fcff')]),
      '\n## Sensitivity; value/share',
      table(['Terminal g','WACC 8%','WACC 9%','WACC 10%'],[[f'{g:.0%}']+[f"${value(rows,replace(BASE,wacc=w,terminal_g=g))['price']:.2f}" for w in (.08,.09,.10)] for g in (.02,.03,.04)]),
      '\n## Reverse DCF',json.dumps(reverse_dcf(),indent=2),
      '\nUniform percentage-point shift to all five revenue-growth assumptions. Content, operating-cost ratios, taxes, WACC, terminal assumptions and bridge are held fixed. This becomes increasingly optimistic as content does not accelerate with revenue; not a probability or management forecast.',
      '\n## Peer cross-check',json.dumps(peer_reference(),indent=2),
      '\nDisney-only qualified reference: EV/revenue includes debt and book NCI; excludes operating lease liabilities with lease costs in operating earnings. Investments/equity affiliates are not netted from either EV/revenue calculation. P/E uses reported FY2025 diluted GAAP EPS; Disney tax benefit and business mix weaken it. Disney shares are the November 5, 2025 cover count, not January 23 shares; book NCI approximates its market value. No peer range or averaging is defensible. WBD FY2025 EPS was not available at this cutoff and its transaction exposure further disqualifies it as a clean standalone anchor.',
      '\n## Historical reconciliation',json.dumps(base_reconciliation(),indent=2),
      '\nNormalized FCFF reference excludes residual non-content CFO adjustments and assumes zero normalized incremental non-content working capital; it is a disclosed diagnostic, not reported FCFF. Forecast cash flows are built separately from statements. Brazil deposit $700m is deducted once in 2026 and held in other assets; no refund is assumed.',
      '\n## Checks',*checks,
      '\n## Still missing course evidence',
      '\nOfficial starter-answer comparison; original Brightspace receipt; human-authored AI-off locked record; actual partner challenge; screen recording of clean-run demonstration; final videos/transcripts and access check. These cannot be inferred from passing software tests.',
      '\n## Material limitations',
      '\nStandalone WBD exclusion; annual timing approximation; no January cash/debt roll-forward; carrying debt as fair-value proxy; all unrestricted cash treated as additive (excluding $5,000m operating reserve would reduce value by $'+f'{5000/SHARES:.2f}'+'); fixed diluted share proxy; cash replacement of future SBC; aggregate operating assets and fixed non-content liabilities; simplified content roll-forward omits FX/noncash historical movements; terminal ROIC judgment; one dated diversified peer. Legacy September values are research history only.'
    ]
    text='\n\n'.join(report)+'\n'
    (ROOT/'visible_results.md').write_text(text)
    payload=dict(valuation_date=VALUATION_DATE,market_price=PRICE,calculated_wacc=CALCULATED_WACC,
                 cases=results,grid=grid,reverse=reverse_dcf(),peers=peer_reference(),
                 base_reconciliation=base_reconciliation(),checks=checks,
                 run_utc=datetime.now(timezone.utc).isoformat(),python=sys.version)
    (ROOT/'results.json').write_text(json.dumps(payload,indent=2,allow_nan=False)+'\n')
    print(text)


if __name__=='__main__':
    main()
