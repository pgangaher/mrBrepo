# PortfolioTracker — IN Sub-Portfolio State
## Date: 2026-05-15 | Session: IN_CLOSE (15:30 IST)
## Market: IN (NSE) | Currency: INR
## Supersedes: portfolio_state_2026-05-15.md (midday entry-day snapshot)

---

## EOD Close Prices
Price source: yfinance EOD bar — `Scripts/cache/snapshot_IN_2026-05-15_153033.json` (quote.close)
India VIX at close: 18.80 | NIFTY 50 3m return: −8.53%

---

## NAV Summary

| Field | Value |
|---|---|
| Starting NAV | ₹10,00,000 |
| Cash deployed (cost basis incl. friction) | ₹2,19,071 (21.9%) |
| Cash remaining | ₹7,80,929 (78.1%) |
| Unrealized P&L | −₹1,810.50 |
| Current market value of positions | ₹2,17,260.50 |
| **Current NAV** | **₹9,98,189.50** |
| Peak NAV | ₹10,00,000 |
| Drawdown from peak | 0.18% |
| Phase | Phase 1 (Recon) |
| Benchmark (NIFTY 50 3m) | −8.53% (from close snapshot) |
| Alpha vs NIFTY (since strategy start, Day 2) | N/A — NIFTY daily close not in prefetch snapshot |

---

## Open Positions

| # | Ticker | Sector | Shares | Entry | Entry Date | Close | Unreal. P&L | Unreal. % | Stop | T1 | T2 | Conv |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ONGC.NS | Energy | 332 | ₹301.15 | 2026-05-15 | ₹299.50 | −₹547.80 | −0.55% | ₹290.09 | ₹320.00 | ₹340.00 | HIGH |
| 2 | ADANIPORTS.NS | Industrials | 33 | ₹1,807.90 | 2026-05-15 | ₹1,792.00 | −₹524.70 | −0.88% | ₹1,730.71 | ₹1,950.00 | ₹2,100.00 | HIGH* |
| 3 | HINDALCO.NS | Metals | 55 | ₹1,080.50 | 2026-05-15 | ₹1,067.10 | −₹737.00 | −1.24% | ₹1,038.40 | ₹1,160.00 | ₹1,220.00 | MEDIUM |

*ADANIPORTS: HIGH conviction, position reduced to 6% due to RSI at entry (70.6). Add-on target: RSI <67.

---

## Position Details

| Ticker | Cost Basis | Current Value | Unreal. P&L | % NAV | TradeLog # | Day Low | Stop | Stop Safe? |
|---|---|---|---|---|---|---|---|---|
| ONGC.NS | ₹99,982 | ₹99,434.00 | −₹548 | 10.0% | #1 | ₹298.75 | ₹290.09 | ✓ Yes |
| ADANIPORTS.NS | ₹59,661 | ₹59,136.00 | −₹525 | 6.0% | #2 | ₹1,766.20 | ₹1,730.71 | ✓ Yes |
| HINDALCO.NS | ₹59,428 | ₹58,690.50 | −₹737 | 5.9% | #3 | ₹1,057.80 | ₹1,038.40 | ✓ Yes |
| **TOTAL** | **₹2,19,071** | **₹2,17,260.50** | **−₹1,810** | **21.9%** | | | | |

---

## Stop & Target Reconciliation

**Stops triggered today:** NONE
- ONGC.NS day low (₹298.75) > stop (₹290.09) — no breach ✓
- ADANIPORTS.NS day low (₹1,766.20) > stop (₹1,730.71) — no breach ✓
- HINDALCO.NS day low (₹1,057.80) > stop (₹1,038.40) — no breach ✓

**Targets hit today:** NONE
- ONGC.NS day high (₹304.95) < T1 (₹320.00) — no trim triggered ✓
- ADANIPORTS.NS day high (₹1,823.90) < T1 (₹1,950.00) — no trim triggered ✓
- HINDALCO.NS day high (₹1,098.00) < T1 (₹1,160.00) — no trim triggered ✓

---

## Sector Exposure (at EOD prices)

| Sector | Current Value | % NAV | Cap (25%) |
|---|---|---|---|
| Energy | ₹99,434 | 9.94% | ✓ Under cap |
| Industrials | ₹59,136 | 5.92% | ✓ Under cap |
| Metals | ₹58,690.50 | 5.88% | ✓ Under cap |

---

## RiskManager Check — EOD

| Check | Threshold | Actual | Status |
|---|---|---|---|
| Drawdown from peak | 15% trigger | 0.18% | ✓ SAFE |
| Max sector exposure | 25% | 9.94% (Energy, highest) | ✓ SAFE |
| Max single position | 20% | 9.94% | ✓ SAFE |
| Phase 1 deployment | ≤40% | 21.9% | ✓ Within Phase 1 |
| Max positions | 4 | 3 | ✓ Room for 1 more |
| **DEFENSIVE MODE** | NAV < ₹8,50,000 | NAV ₹9,98,190 | ✗ NOT ACTIVE |

---

## Benchmark Update

| Metric | Value |
|---|---|
| NIFTY 50 3m return (from close snapshot) | −8.53% |
| India VIX at close | 18.80 |
| NIFTY daily close level | Not available in prefetch snapshot |
| Portfolio vs NIFTY since start | Portfolio: −0.18% | NIFTY since start: N/A |

---

## Watchlist — Next Candidates

| Ticker | Score | Current RSI | Trigger | Notes |
|---|---|---|---|---|
| ADANIENT.NS | 87.07 | 75.6 | RSI <70 + price ~₹2,700+ | Top scorer; RSI still elevated at close |
| SUNPHARMA.NS | 69.37 | 64.9 | Full five-layer at next IN_OPEN | Pharma diversifier; MOMENTUM_LONG MEDIUM |
| COALINDIA.NS | — | — | RSI push above 55 | Energy diversifier; Phase 2 candidate |

Note: ADANIENT.NS close ₹2,715.20, RSI 75.6 — still overbought. Entry valid only on RSI cooling below 70 with price holding ₹2,700+.

---

## Phase 1 Deployment Status

| Metric | Limit | Actual | Status |
|---|---|---|---|
| Max deployment | 40% | 21.9% | ✓ Within Phase 1 |
| Max positions | 4 | 3 | ✓ Room for 1 more |
| Cash floor | 10% | 78.1% remaining | ✓ Far above floor |
| Dry powder | 10% reserved | ₹1,00,000 earmarked | ✓ Reserved |

**Available for Phase 1 additions**: ~₹1,80,929 (18.1% NAV, preserving ₹1L dry powder)

---

*PortfolioTracker sub-agent | IN sub-portfolio | IN_CLOSE 2026-05-15 15:30 IST*
*Price source: yfinance EOD bar — snapshot_IN_2026-05-15_153033.json*
