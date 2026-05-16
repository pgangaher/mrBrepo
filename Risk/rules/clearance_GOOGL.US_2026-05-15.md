# RiskManager — Clearance Decision: GOOGL.US
## Date: 2026-05-15 | Session: US_OPEN | Market: US (NASDAQ)

---

## Proposed Trade
- Direction: LONG
- Entry (snapshot open): $397.28
- Stop (stop_atr from snapshot): $386.30
- Position size: 8% of US NAV = $800
- Phase: Phase 1 (Reconnaissance)

## Risk Parameter Check

| Parameter | Rule | Actual | Pass? |
|---|---|---|---|
| Stop width (Phase 1) | ≤5% below entry | (397.28 - 386.30)/397.28 = **2.76%** | ✅ PASS |
| RSI screen | Acceptable (<85 for new entry) | 74.16 | ✅ PASS |
| Signal class | MOMENTUM_LONG or SECTOR_ROTATION | MOMENTUM_LONG | ✅ PASS |
| Conviction | HIGH or MEDIUM | MEDIUM | ✅ PASS |
| Sector alignment (Layer 4) | OVERWEIGHT sector | IT/Tech OVERWEIGHT | ✅ PASS |
| Sentiment (Layer 3) | Not URGENT or ELEVATED | POSITIVE | ✅ PASS |
| Research thesis (Layer 1) | Intact, not broken | BULLISH — strong moat | ✅ PASS |
| Position count | Max 4 in Phase 1 | Currently 2 + GOOGL = 3 | ✅ PASS |
| Deployment | Max 40% in Phase 1 | 16% + 8% = 24.0% | ✅ PASS |
| Cash floor | ≥10% at all times | 76% remaining after fill | ✅ PASS |
| Max risk per trade | ≤2% NAV | 0.22% NAV ($22.07) | ✅ PASS |
| MACD | Bullish preferred | +1.17 histogram | ✅ PASS |
| Earnings timeline | >2 weeks preferred | ~10 weeks (late July) | ✅ PASS |
| No gap-down at entry | Preferred | No gap-down (open $397.28 vs close $401.07 — minor) | ✅ PASS |

## Position Sizing

| Parameter | Calculation | Value |
|---|---|---|
| US NAV (starting) | Locked per strategy_meta.json | $10,000.00 |
| Position size | 8% | $800.00 |
| Entry price | Snapshot open | $397.28 |
| Paper shares | $800 / $397.28 | **2.01 shares** |
| Notional | 2.01 × $397.28 | **$798.53** |
| Stop | Snapshot stop_atr | $386.30 |
| Risk per share | $397.28 − $386.30 | $10.98 |
| Total position risk | 2.01 × $10.98 | **$22.07** |
| % NAV at risk | $22.07 / $10,000 | **0.22%** |

## Risk:Reward Analysis

| Target | Price | Gain from Entry | R:R Ratio |
|---|---|---|---|
| Target 1 | $419.24 | +5.52% (+$21.96) | **2.00:1** |
| Target 2 | $441.20 | +11.07% (+$43.92) | **4.00:1** |
| Stop | $386.30 | −2.76% (−$10.98) | — |

R:R is favorable at 2:1 minimum (T1) and 4:1 (T2). Acceptable for MEDIUM conviction.

## Portfolio Impact After Fill

| Metric | Before | After |
|---|---|---|
| Positions | 2 (NVDA, CAT) | 3 (NVDA, CAT, GOOGL) |
| Deployed | $1,597.99 (16.0%) | $2,396.52 (24.0%) |
| Cash remaining | $8,402.01 | $7,603.48 |
| Sector concentration IT/Semis+Tech | 10.0% | 18.0% |
| Phase 1 limit (40%) | ✓ | ✓ |
| Phase 1 max positions (4) | ✓ | ✓ |

## Verdict: **APPROVED**

All five layers pass. RiskManager approves GOOGL.US LONG at $397.28 (snapshot open). No modifications required.

**Stop management note:** With NVDA and CAT already showing early losses at open (combined -$43.28 unrealized), adding GOOGL at 8% does not materially change portfolio risk profile (NAV drawdown still <1%). No defensive mode trigger.

**Earnings flag:** No action required. Q2 FY2026 earnings ~late July. Initiate earnings watch on approximately July 8, 2026 (3 weeks before expected report).

---

*RiskManager sub-agent | GOOGL.US | 2026-05-15 19:08 IST*
