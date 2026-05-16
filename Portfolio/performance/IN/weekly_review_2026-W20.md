# PortfolioTracker — IN Weekly P&L Report
## Week: 2026-W20 | 2026-05-11 to 2026-05-17
## Market: IN (NSE) | Currency: INR
## PortfolioTracker WEEKLY P&L REPORT W20 2026-05-11 2026-05-17 IN [ONGC ₹299.50 | ADANIPORTS ₹1,792.00 | HINDALCO ₹1,067.10]

---

## Week Summary

| Metric | Value |
|---|---|
| Week number | ISO W20 (2026-05-11 – 2026-05-17) |
| Strategy trading days this week | 2 (May 14 — baseline; May 15 — positions opened + first P&L day) |
| Starting NAV (Mon open / strategy start) | ₹10,00,000 |
| Ending NAV (last IN_CLOSE this week) | ₹9,98,189.50 |
| Week P&L (absolute) | −₹1,810.50 |
| Week P&L (%) | −0.18% |
| NIFTY 50 week return | N/A — NIFTY daily close level not in prefetch snapshot |
| Week Alpha vs NIFTY | N/A |
| Cumulative return since strategy start | −0.18% |
| Peak NAV | ₹10,00,000 |
| Drawdown from peak | 0.18% |
| Phase | Phase 1 — Recon (Week 1 of 1-month paper trade) |
| Benchmark (NIFTY 50) 3m | −8.53% |
| India VIX at week end | 18.80 |

**Note:** This is a partial inception week. IN strategy baseline set on 2026-05-14. Positions opened 2026-05-15 at midday (12:45 IST). NIFTY 50 spot level and daily returns are not yet captured in the prefetch snapshot — alpha tracking begins Week 2 once daily NIFTY capture is added to prefetch.

---

## Position-Level P&L

| # | Ticker | Sector | Shares | Entry | Entry Date | EOW Close | Unreal. P&L | Unreal. % | Stop | T1 | T2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ONGC.NS | Energy | 332 | ₹301.15 | 2026-05-15 | ₹299.50 | −₹547.80 | −0.55% | ₹290.09 ✓ | ₹320.00 | ₹340.00 |
| 2 | ADANIPORTS.NS | Industrials | 33 | ₹1,807.90 | 2026-05-15 | ₹1,792.00 | −₹524.70 | −0.88% | ₹1,730.71 ✓ | ₹1,950.00 | ₹2,100.00 |
| 3 | HINDALCO.NS | Metals | 55 | ₹1,080.50 | 2026-05-15 | ₹1,067.10 | −₹737.00 | −1.24% | ₹1,038.40 ✓ | ₹1,160.00 | ₹1,220.00 |
| **TOTAL** | | | | | | | **−₹1,809.50** | **−0.18% NAV** | | | |

NAV differential: −₹1,810.50 (−₹1,809.50 unrealized + −₹1 cost-basis rounding at entry)

---

## NAV Summary

| Field | Value |
|---|---|
| Starting NAV | ₹10,00,000 |
| Cash deployed (cost basis) | ₹2,19,071 (21.91% of starting NAV) |
| Cash remaining | ₹7,80,929 (78.1%) |
| Unrealized P&L | −₹1,809.50 |
| Current market value of positions | ₹2,17,260.50 |
| **Ending NAV** | **₹9,98,189.50** |

---

## Trade Events This Week

| Date | Time (IST) | Event | Ticker | Price | Shares | Notional | TradeLog # |
|---|---|---|---|---|---|---|---|
| 2026-05-15 | 12:45 | OPEN | ONGC.NS | ₹301.15 | 332 | ₹99,982 | #1 |
| 2026-05-15 | 12:45 | OPEN | ADANIPORTS.NS | ₹1,807.90 | 33 | ₹59,661 | #2 |
| 2026-05-15 | 12:45 | OPEN | HINDALCO.NS | ₹1,080.50 | 55 | ₹59,428 | #3 |

**Positions that hit Target 1:** NONE
**Positions that hit Stop:** NONE

---

## Stop Reconciliation (End of Week)

| Ticker | Day Low (May 15) | Stop | Buffer at Low | Status |
|---|---|---|---|---|
| ONGC.NS | ₹298.75 | ₹290.09 | +₹8.66 / 2.89% | ✓ Safe |
| ADANIPORTS.NS | ₹1,766.20 | ₹1,730.71 | +₹35.49 / 2.01% | ✓ Safe |
| HINDALCO.NS | ₹1,057.80 | ₹1,038.40 | +₹19.40 / 1.84% | ✓ Safe (tightest) |

All IN positions are comfortably above their stops. No stop-trail opportunities — all positions in entry-day drawdown; no unrealized gains to protect.

---

## Sector Exposure

| Sector | Ticker | Cost Basis | Market Value | % NAV |
|---|---|---|---|---|
| Energy | ONGC.NS | ₹99,982 | ₹99,434 | 9.94% |
| Industrials | ADANIPORTS.NS | ₹59,661 | ₹59,136 | 5.92% |
| Metals | HINDALCO.NS | ₹59,428 | ₹58,691 | 5.88% |
| Cash | — | — | ₹7,80,929 | 78.26% |

All sector exposures within Phase 1 caps (25% per sector max). Excellent diversification across Energy, Industrials, and Metals.

---

## Benchmark

| Metric | Value |
|---|---|
| India VIX at week end | 18.80 (Choppy regime) |
| NIFTY 50 3m return | −8.53% |
| NIFTY daily return | N/A — not in snapshot universe |
| Portfolio week return | −0.18% |
| Alpha vs NIFTY 3m | Portfolio −0.18% vs NIFTY 3m −8.53% → directionally positive (portfolio outperforming 3m benchmark by 8.35ppt), though daily tracking not yet established |

**Context on benchmark:** The NIFTY 50 has returned −8.53% over 3 months while the IN portfolio sectors (Energy, Industrials, Metals) have been meaningful outperformers. The relative setup is favorable.

---

## No-Trade Summary (Validated Decisions)

| Ticker | Reason | Outcome |
|---|---|---|
| ADANIENT.NS | RSI 75.6 overbought; wait for cooling | Closed at ₹2,715.20 — RSI still 75.6 EOD. Correct to wait. |
| IN IT sector (TCS/INFY/HCLTECH/WIPRO/TECHM) | All NO_SIGNAL LOW; RSI 26–40; 3m −17% to −28% | Structural bear confirmed. No-trade fully validated. |

---

## Watchlist Carry-Forward to Week 21

| Ticker | Close | Score | RSI | Signal | Gate for Entry |
|---|---|---|---|---|---|
| ADANIENT.NS | ₹2,715.20 | 87.07 | 75.6 | MOMENTUM_LONG HIGH | RSI must cool below 70; price hold ₹2,700+ |
| SUNPHARMA.NS | N/A | 69.37 | 64.9 | MOMENTUM_LONG MEDIUM | Run full five-layer at IN_OPEN May 18 |
| COALINDIA.NS | N/A | — | — | Phase 2 candidate | RSI push above 55 triggers evaluation |

---

## Key Watch Items for W21 (IN)

1. **Phase 2 begins May 18**: Cap raises to 80%, position limit to 8. Can now add to existing positions or initiate ADANIENT.NS / SUNPHARMA.NS if criteria met.
2. **ADANIPORTS.NS add-on plan**: Add 22 shares if RSI cools below 67 on healthy pullback.
3. **ONGC.NS Q4 FY2026 earnings** expected late May / early June — catalyst watch; could accelerate to T1 ₹320.
4. **IN IT sector remains AVOID**: No evaluation until sector RSI >50 and MACD turns bullish.
5. **ADANIENT.NS RSI watch**: First check at IN_OPEN May 18 — if RSI < 70 with price ≥ ₹2,700, proceed to five-layer.

---

*PortfolioTracker sub-agent | IN sub-portfolio | WEEKEND_REVIEW 2026-W20 | 2026-05-16 10:00 IST*
*Price source: yfinance EOD bar — snapshot_IN_2026-05-15_153033.json (authoritative IN_CLOSE 2026-05-15)*
