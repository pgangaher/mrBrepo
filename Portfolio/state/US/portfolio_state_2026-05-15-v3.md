# PortfolioTracker — US Sub-Portfolio State (v3 — US_CLOSE)
## Date: 2026-05-15 | Session: US_CLOSE (01:30 IST May 16 / 15:58 EDT)
## Market: US (NASDAQ/NYSE) | Currency: USD
## Supersedes: `Portfolio/state/US/portfolio_state_2026-05-15-v2.md` (US_OPEN snapshot)
## Price reference: NASDAQ close from snapshot_US_2026-05-16_013028.json (quote.close / yfinance-intraday-1m last bar)

---

## EOD Close Prices (Authoritative)

| Ticker | Close | High | Low | Open | Source |
|---|---|---|---|---|---|
| NVDA.US | $225.30 | $231.50 | $224.25 | $229.75 | snapshot_US_2026-05-16_013028.json |
| CAT.US | $888.74 | $899.73 | $880.20 | $898.75 | snapshot_US_2026-05-16_013028.json |
| GOOGL.US | $396.46 | $399.54 | $393.18 | $396.28 | snapshot_US_2026-05-16_013028.json |

VIX at close: 18.13 | SPY 3m return (benchmark_return_3m): +8.43%

---

## NAV Summary

| Field | Value |
|---|---|
| Starting NAV | $10,000.00 |
| Cash deployed (cost basis incl. friction) | $2,396.52 (24.0%) |
| Cash remaining | $7,603.48 (76.0%) |
| Unrealized P&L (vs entry prices) | −$66.22 (−0.66% on deployed) |
| Current market value of positions | $2,329.83 |
| **Current NAV** | **$9,933.32** |
| Day P&L (vs May 14 baseline $10,000) | −$66.68 (−0.67%) |
| Cumulative return | −0.67% |
| Peak NAV | $10,000.00 |
| Drawdown from peak | 0.67% |
| Phase | Phase 1 (Recon) — Day 2 |
| SPY 3m return | +8.43% (from snapshot benchmark_return_3m) |
| SPY day return | N/A (SPY not in snapshot universe) |
| Alpha vs SPY | N/A (day return not available) |
| **DEFENSIVE MODE** | **NOT ACTIVE** (0.67% < 15% threshold) |

---

## Open Positions

| # | Ticker | Sector | Shares | Entry | Entry Date | Close | Unreal. P&L | Unreal. % | Stop | T1 | T2 | Conv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA.US | IT/Semis | 4.24 | $235.74 | 2026-05-15 | $225.30 | −$44.27 | −4.43% | $224.98 | $255.00 | $270.00 | HIGH |
| 2 | CAT.US | Industrials | 0.65 | $919.98 | 2026-05-15 | $888.74 | −$20.31 | −3.40% | $878.37 | $982.00 | $1,030.00 | MEDIUM |
| 3 | GOOGL.US | IT/Tech | 2.01 | $397.28 | 2026-05-15 | $396.46 | −$1.65 | −0.21% | $386.30 | $419.24 | $441.20 | MEDIUM |

---

## Position Details

| Ticker | Cost Basis | Market Value | Unreal. P&L | % NAV | TradeLog # | Day Low | Stop | Stop Safe? |
|---|---|---|---|---|---|---|---|---|
| NVDA.US | $1,000.00 | $955.27 | −$44.27 | 9.6% | #4 | $224.25 | $224.98 | ⚠️ **CRITICAL** — low breached stop intraday; close $225.30 > stop, position maintained |
| CAT.US | $597.99 | $577.68 | −$20.31 | 5.8% | #5 | $880.20 | $878.37 | ⚠️ ELEVATED — $1.83 above stop at day low |
| GOOGL.US | $798.53 | $796.88 | −$1.65 | 8.0% | #6 | $393.18 | $386.30 | ✓ Standard monitoring |
| **TOTAL** | **$2,396.52** | **$2,329.83** | **−$66.68** | **23.5%** | | | | |

*Note: Market value NAV percentages calculated on $9,933.32 current NAV.

---

## Stop & Target Reconciliation — 2026-05-15 US_CLOSE

**Stops triggered:** NONE
- NVDA.US: Day low $224.25 breached paper stop $224.98 INTRADAY by $0.73. However, paper-trade CLOSE rule uses official session close price ($225.30 > $224.98) → **NO STOP-HIT. Position maintained.**
  - This is the second consecutive intraday breach (same as US_MIDDAY). Stop remains at $224.98.
  - **Next session watch: If open OR close falls below $224.98 → paper close immediately.**
- CAT.US: Day low $880.20 > stop $878.37 — buffer $1.83 / 0.21% at worst → **No breach. Position maintained.**
- GOOGL.US: Day low $393.18 > stop $386.30 — comfortable $6.88 / 1.73% buffer → **No breach. Position maintained.**

**Targets hit:** NONE
- NVDA.US: Day high $231.50 << T1 $255.00 — no trim
- CAT.US: Day high $899.73 << T1 $982.00 — no trim
- GOOGL.US: Day high $399.54 < T1 $419.24 — no trim

---

## Sector Exposure (at EOD close prices)

| Sector | Tickers | Market Value | % NAV | Cap (25%) |
|---|---|---|---|---|
| IT/Semis | NVDA.US | $955.27 | 9.6% | ✓ Under cap |
| Industrials | CAT.US | $577.68 | 5.8% | ✓ Under cap |
| IT/Tech (Internet) | GOOGL.US | $796.88 | 8.0% | ✓ Under cap |
| **IT Total** | NVDA + GOOGL | $1,752.15 | 17.6% | ✓ Under 25% IT cap |

---

## RiskManager Check — US_CLOSE

| Check | Threshold | Actual | Status |
|---|---|---|---|
| Drawdown from peak | 15% → DEFENSIVE | 0.67% | ✓ SAFE — **DEFENSIVE MODE NOT ACTIVE** |
| Max sector exposure | 25% | 17.6% (IT combined) | ✓ SAFE |
| Max single position | 20% | 9.6% (NVDA) | ✓ SAFE |
| Phase 1 deployment | ≤40% | 24.0% of starting NAV | ✓ Within Phase 1 |
| Max positions (Phase 1) | 4 | 3 | ✓ 1 slot remaining |
| NVDA stop buffer | — | $0.32 / 0.14% | ⚠️ CRITICAL — flag for next session |
| CAT stop buffer | — | $10.37 / 1.17% | ⚠️ ELEVATED monitoring |
| GOOGL stop buffer | — | $10.16 / 2.56% | ✓ Standard monitoring |

---

## Benchmark Update

| Metric | Value |
|---|---|
| VIX at US_CLOSE | 18.13 (↑ from 18.37 at midday) |
| SPY 3m return (from snapshot) | +8.43% |
| SPY day return | Not available (SPY not in snapshot tickers) |
| Portfolio day return | −0.67% |
| Alpha today | N/A |

---

## Phase 1 Deployment Status

| Metric | Limit | Actual | Status |
|---|---|---|---|
| Max deployment | 40% | 24.0% (starting NAV basis) | ✓ Within Phase 1 |
| Max positions | 4 | 3 | ✓ Room for 1 more Phase 1 slot |
| Cash floor | 10% | 76.0% | ✓ Far above floor |
| Drawdown from peak | <15% | 0.67% | ✓ Not triggered |

**Available for Phase 1 additions**: ~$1,600 remaining (16% starting NAV) for 1 final Phase 1 slot.

---

## Watchlist — US_CLOSE Signal Update

| Ticker | Close Score | Signal | RSI | Stop_ATR | Stop % | Phase 1 Entry? | Notes |
|---|---|---|---|---|---|---|---|
| AMD.US | 80.09 | MOMENTUM_LONG | 67.29 | $390.16 | 8.01% | ❌ Exceeds 5% limit | Phase 2 target (May 21+). Price pulled back from $440→$424. |
| CSCO.US | 81.38 | MOMENTUM_LONG | 88.47 | $112.87 | 4.44% | ❌ RSI extreme | Stop technically clears 5% limit but RSI 88.47 overrides. Entry only RSI <75. |
| SBUX.US | 64.23 | MOMENTUM_LONG | 65.49 | $102.80 | 3.76% | ❌ Sector NEUTRAL | Consumer Staples deferred to Phase 2 |
| UNH.US | 66.48 | SECTOR_ROTATION | 76.52 | $379.49 | 3.58% | ❌ Sector NEUTRAL | Healthcare deferred to Phase 2; RSI still elevated |
| AVGO.US | 64.40 | MOMENTUM_LONG | 58.61 | $401.50 | 5.64% | ❌ Exceeds 5% limit; earnings risk | Post-Q2 FY26 earnings entry window (early June) |

---

## Key Watch Items — Next US Session

1. **NVDA.US ⚠️ CRITICAL STOP WATCH**: Close $225.30 is $0.32 / 0.14% above stop $224.98. Any session where open or close falls below $224.98 → execute paper close at that session's reference price. This is the top priority for the next US_OPEN review.
2. **CAT.US ⚠️ ELEVATED**: 1.17% buffer above stop. Monitor pre-market.
3. **AMD.US Phase 2 Evaluation**: On May 21 (Phase 2 start), run fresh full five-layer with wider stop allowance.
4. **NVDA Earnings Watch**: Triple-layer earnings check required on May 21 (7 days pre-earnings ~May 28).

---

*PortfolioTracker sub-agent | US sub-portfolio | US_CLOSE | 2026-05-15 (01:30 IST May 16)*
*Price source: yfinance-intraday-1m last bar — snapshot_US_2026-05-16_013028.json*
