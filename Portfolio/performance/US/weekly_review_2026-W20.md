# PortfolioTracker — US Weekly P&L Report
## Week: 2026-W20 | 2026-05-11 to 2026-05-17
## Market: US (NASDAQ/NYSE) | Currency: USD
## PortfolioTracker WEEKLY P&L REPORT W20 2026-05-11 2026-05-17 US [NVDA $225.30 | CAT $888.74 | GOOGL $396.46]

---

## Week Summary

| Metric | Value |
|---|---|
| Week number | ISO W20 (2026-05-11 – 2026-05-17) |
| Strategy trading days this week | 2 (May 14 — baseline; May 15 — first live P&L day) |
| Starting NAV (Mon open / strategy start) | $10,000.00 |
| Ending NAV (Fri close / last US_CLOSE) | $9,933.32 |
| Week P&L (absolute) | −$66.68 |
| Week P&L (%) | −0.67% |
| SPY week return | N/A — SPY daily return not in prefetch universe |
| Week Alpha vs SPY | N/A |
| Cumulative return since strategy start | −0.67% |
| Peak NAV | $10,000.00 |
| Drawdown from peak | 0.67% |
| Phase | Phase 1 — Recon (Week 1 of 1-month paper trade) |
| Benchmark (SPY) 3m | +8.43% |

**Note:** This is a partial inception week. The US strategy baseline was set on 2026-05-14 (Wednesday). Positions were opened on May 15. SPY daily returns are not currently captured in the prefetch snapshot — alpha will be computed from Week 2 onwards when daily benchmark tracking is established.

---

## Position-Level P&L

| # | Ticker | Sector | Shares | Entry | Entry Date | EOW Close | Unreal. P&L | Unreal. % | Stop | T1 | T2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NVDA.US | IT/Semis | 4.24 | $235.74 | 2026-05-15 | $225.30 | −$44.27 | −4.43% | $224.98 ⚠️ CRITICAL | $255.00 | $270.00 |
| 2 | CAT.US | Industrials | 0.65 | $919.98 | 2026-05-15 | $888.74 | −$20.31 | −3.40% | $878.37 ⚠️ ELEVATED | $982.00 | $1,030.00 |
| 3 | GOOGL.US | IT/Tech | 2.01 | $397.28 | 2026-05-15 | $396.46 | −$1.65 | −0.21% | $386.30 ✓ | $419.24 | $441.20 |
| **TOTAL** | | | | | | | **−$66.23** | **−0.66% deployed** | | | |

NAV differential: −$66.68 (−$66.23 unrealized + −$0.45 GOOGL entry friction)

---

## NAV Summary

| Field | Value |
|---|---|
| Starting NAV | $10,000.00 |
| Cash deployed (cost basis) | $2,396.52 (23.97% of starting NAV) |
| Cash remaining | $7,603.48 (76.0%) |
| Unrealized P&L | −$66.23 |
| Current market value of positions | $2,329.83 |
| **Ending NAV** | **$9,933.32** |

---

## Trade Events This Week

| Date | Time (IST) | Event | Ticker | Price | Shares | Notional | TradeLog # |
|---|---|---|---|---|---|---|---|
| 2026-05-15 | 13:00 | OPEN | NVDA.US | $235.74 | 4.24 | $1,000.00 | #4 |
| 2026-05-15 | 13:00 | OPEN | CAT.US | $919.98 | 0.65 | $597.99 | #5 |
| 2026-05-15 | 19:15 | OPEN | GOOGL.US | $397.28 | 2.01 | $798.53 | #6 |

**Positions that hit Target 1:** NONE
**Positions that hit Stop:** NONE

---

## Stop Reconciliation

| Ticker | Day Low (Fri) | Stop | Buffer at Low | Status |
|---|---|---|---|---|
| NVDA.US | $224.25 | $224.98 | −$0.73 (intraday breach, close $225.30 > stop) | ⚠️ CRITICAL — 2 consecutive intraday breaches; position maintained per CLOSE price rule |
| CAT.US | $880.20 | $878.37 | +$1.83 / 0.21% | ⚠️ ELEVATED — dangerously thin at worst point |
| GOOGL.US | $393.18 | $386.30 | +$6.88 / 1.73% | ✓ Standard monitoring |

---

## Sector Exposure

| Sector | Tickers | Cost Basis | Market Value | % NAV |
|---|---|---|---|---|
| IT/Semis | NVDA.US | $1,000.00 | $955.27 | 9.6% |
| IT/Tech | GOOGL.US | $798.53 | $796.88 | 8.0% |
| Industrials | CAT.US | $597.99 | $577.68 | 5.8% |
| IT Combined | NVDA + GOOGL | $1,798.53 | $1,752.15 | 17.6% |
| Cash | — | — | $7,603.48 | 76.5% |

All sector exposures within Phase 1 caps. IT combined below 25% cap.

---

## Benchmark

| Metric | Value |
|---|---|
| VIX at week end | 18.13 (Risk-On Choppy range) |
| SPY 3m return | +8.43% |
| SPY week return | N/A — not in snapshot universe |
| Portfolio week return | −0.67% |
| Cumulative alpha | N/A (benchmark daily not tracked yet) |

---

## Watchlist Carry-Forward to Week 21

| Ticker | Close | Score | Signal | Status | Gate for Entry |
|---|---|---|---|---|---|
| AMD.US | $424.16 | 80.09 | MOMENTUM_LONG HIGH | Phase 2 candidate | ATR stop 8.01% — needs to contract to ≤5% |
| CSCO.US | $118.12 | 81.38 | MOMENTUM_LONG HIGH | Phase 2 candidate | RSI 88.47 extreme; entry on RSI < 75 |
| AVGO.US | $425.46 | 64.40 | MOMENTUM_LONG MEDIUM | Phase 2 candidate | Post-Q2 earnings (early June) |
| SBUX.US | $106.81 | 64.23 | MOMENTUM_LONG MEDIUM | Phase 2 candidate | Consumer Staples NEUTRAL — Phase 1 excluded |
| UNH.US | $393.60 | 66.48 | SECTOR_ROTATION MEDIUM | Phase 2 candidate | Healthcare NEUTRAL — Phase 1 excluded |

---

## Key Watch Items for W21

1. **NVDA.US CRITICAL**: Open/close below $224.98 → execute paper close at session reference price. Also: NVDA earnings triple-check on May 21 (7 days pre-earnings ~May 28).
2. **Phase 2 begins W21 (May 18)**: CAP raises to 80%, position limit to 8. Evaluate AMD.US and CSCO.US with Phase 2 stop-width latitude.
3. **CAT.US ELEVATED**: Monitor at US_OPEN May 18 — stop buffer thin.
4. **No additional Phase 1 slots needed**: Phase 2 begins Monday.

---

*PortfolioTracker sub-agent | US sub-portfolio | WEEKEND_REVIEW 2026-W20 | 2026-05-16 10:00 IST*
*Price source: snapshot_US_2026-05-16_013028.json (authoritative US_CLOSE 2026-05-15)*
