# PortfolioTracker — US Sub-Portfolio State (v2)
## Date: 2026-05-15 | Session: US_OPEN (19:00 IST / 09:30 EDT)
## Market: US (NASDAQ/NYSE) | Currency: USD
## Supersedes: `Portfolio/state/US/portfolio_state_2026-05-15.md` (pre-open, 2 positions)
## Price reference: NASDAQ open prices from snapshot_US_2026-05-15_190032.json

---

## NAV Summary

| Field | Value |
|---|---|
| Starting NAV | $10,000.00 |
| Cash deployed | $2,396.52 (24.0%) |
| Cash remaining | $7,603.48 (76.0%) |
| Unrealized P&L (at open) | −$43.28 (−0.43%) |
| Estimated Current NAV | $9,956.72 |
| Peak NAV | $10,000.00 |
| Drawdown from peak | 0.43% |
| Phase | Phase 1 (Recon) |
| Benchmark (SPY 3m) | +9.82% |
| Alpha vs SPY (since start) | −0.43% (Day 2, open-price snapshot) |

---

## Open Positions

| # | Ticker | Sector | Shares | Entry | Entry Date | Open 2026-05-15 | Unreal. P&L | Stop | T1 | T2 | Conv |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA.US | IT/Semis | 4.24 | $235.74 | 2026-05-15 | $229.57 | −$26.16 | $224.98 | $255.00 | $270.00 | HIGH |
| 2 | CAT.US | Industrials | 0.65 | $919.98 | 2026-05-15 | $893.64 | −$17.12 | $878.37 | $982.00 | $1,030.00 | MEDIUM |
| 3 | GOOGL.US | IT/Tech | 2.01 | $397.28 | 2026-05-15 | $397.28 | $0.00 | $386.30 | $419.24 | $441.20 | MEDIUM |

---

## Position Details

| Ticker | Notional | % NAV | TradeLog # | Risk ($) | Max Risk % NAV | Buffer to Stop |
|---|---|---|---|---|---|---|
| NVDA.US | $1,000.00 | 10.0% | #4 | $45.62 | 0.46% | 2.00% ($4.59) |
| CAT.US | $597.99 | 6.0% | #5 | $27.05 | 0.27% | 1.71% ($15.27) |
| GOOGL.US | $798.53 | 8.0% | #6 | $22.07 | 0.22% | 2.76% ($10.98) |
| **TOTAL** | **$2,396.52** | **24.0%** | | **$94.74** | **0.95%** | — |

---

## Stop Monitoring (Priority Order)

| Ticker | Current Open | Stop | Buffer $ | Buffer % | Action Threshold |
|---|---|---|---|---|---|
| CAT.US | $893.64 | $878.37 | $15.27 | 1.71% | **Monitor intraday** — thin buffer |
| NVDA.US | $229.57 | $224.98 | $4.59 | 2.00% | **Monitor intraday** — thin buffer |
| GOOGL.US | $397.28 | $386.30 | $10.98 | 2.76% | Standard monitoring |

> Both NVDA and CAT are down from entry and have thinning stop buffers. No forced action yet — stops not triggered. If either approaches stop intraday, SentimentMonitor URGENT review is required before any manual intervention.

---

## Sector Exposure

| Sector | Tickers | Exposure | % NAV | Cap (25%) |
|---|---|---|---|---|
| IT/Semis | NVDA.US | $1,000 | 10.0% | ✓ Under cap |
| Industrials | CAT.US | $598 | 6.0% | ✓ Under cap |
| IT/Tech (Internet) | GOOGL.US | $799 | 8.0% | ✓ Under cap |
| **IT Total** | NVDA + GOOGL | $1,799 | 18.0% | ✓ Under 25% cap |

---

## Phase 1 Deployment Status

| Metric | Limit | Actual | Status |
|---|---|---|---|
| Max deployment | 40% | 24.0% | ✓ Within Phase 1 |
| Max positions | 4 | 3 | ✓ Room for 1 more |
| Cash floor | 10% | 76.0% remaining | ✓ Far above floor |
| Drawdown from peak | <15% (defensive trigger) | 0.43% | ✓ Not triggered |

**Available for Phase 1 additions**: ~$1,600 (16% NAV) for 1 final Phase 1 position slot.

---

## Watchlist — Next Candidates (Priority Order for Phase 1 / Phase 2)

| Ticker | Score | Status | Entry Condition |
|---|---|---|---|
| AMD.US | 76.12 | Phase 1 WATCH — stop 5.73% | Consolidation → ATR contracts → stop <5%; OR Phase 2 May 21+ |
| CSCO.US | 86.46 | Phase 2 WATCH — RSI 87.47 overbought | RSI pullback <75, price holds $105+ |
| AVGO.US | 69.58 | WATCH post-gap — earnings in 3 wks | Post-Q2 earnings (early June) with stable ATR |
| SBUX.US | 67.56 | Phase 2 candidate | Phase 2 entry (May 21+); Consumer Staples |
| UNH.US | 65.61 | Phase 2 monitor | Phase 2 healthcare entry consideration |

---

## Upcoming Earnings Watch

| Ticker | Expected Earnings | Action Required |
|---|---|---|
| NVDA.US | ~May 28, 2026 | Run triple earnings check May 21 (7 days pre) |
| AVGO.US | ~early June 2026 | Post-earnings entry evaluation |
| GOOGL.US | ~late July 2026 | Initiate earnings watch ~July 8 (3 weeks pre) |

---

*PortfolioTracker sub-agent | US sub-portfolio | Session: US_OPEN | 2026-05-15 19:15 IST*
