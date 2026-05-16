# RiskManager — Pre-Trade Clearance
## Ticker: NVDA.US | Date: 2026-05-15 | Market: US

---

## Trade Parameters Submitted

| Field | Value |
|---|---|
| Direction | LONG |
| Entry price | $235.74 (May 14 US close) |
| Stop loss | $224.98 |
| Target 1 | $255.00 |
| Target 2 | $270.00 |
| Proposed size | 10% of US NAV (HIGH conviction) |
| Shares | 4.24 (paper fractional) |
| Notional | $1,000.00 |

---

## Risk Checks

| Check | Threshold | Actual | Pass? |
|---|---|---|---|
| Stop width | ≤5% Phase 1 | 4.56% | ✓ PASS (just within limit) |
| Position size | ≤10% (HIGH) | 10.0% | ✓ PASS |
| Sector concentration (IT/Semis) | ≤25% NAV | 10.0% | ✓ PASS |
| Phase 1 total deployment | ≤40% | 10.0% (this trade) | ✓ PASS |
| R:R ratio (Target 1) | ≥1.5:1 | ($19.26 / $10.76) = **1.79:1** | ✓ PASS |
| R:R ratio (Target 2) | ≥2.5:1 | ($34.26 / $10.76) = **3.19:1** | ✓ PASS |
| Cash floor after trade | ≥10% | 90.0% remaining | ✓ PASS |
| Portfolio drawdown | <15% | 0% (Day 2) | ✓ PASS |
| Earnings within 14 days | WATCH | NVDA earnings ~May 28 | ⚠ FLAGGED |

---

## Earnings Alert

**NVDA Q1 FY2027 earnings expected ~May 28, 2026** — within 14 days. Per MrB rules, all three monitors (ResearchAnalyst EARNINGS WATCH, SignalEngine EARNINGS SIGNAL, SentimentMonitor EARNINGS MONITOR) should be triggered within 7 days of the report. Plan: run the triple-check on May 21 IN_OPEN session.

**Earnings risk mitigation**: At 10% position (Phase 1 entry), risk is limited. If pre-earnings momentum is strong (RSI trending up, no ELEVATED sentiment), hold through earnings. If URGENT alert fires before earnings, trim to 5% (half size) before report.

---

## Friction

- Estimated cost (0.025% one-way): $0.25
- Breakeven price: $235.80

---

## Verdict

**APPROVED** — with earnings watch flag.

NVDA.US cleared for Phase 1 LONG at $235.74. Stop $224.98 (−4.56%). Targets $255 and $270. 4.24 paper shares, $1,000 notional. Earnings flag active: run triple earnings check ~May 21.

---

*RiskManager sub-agent | US sub-portfolio | 2026-05-15*
