# SentimentMonitor — Watchlist Pulse US (US_OPEN)
## Date: 2026-05-15 | Session: US_OPEN (19:00 IST / 09:30 EDT)
## Market: US (NASDAQ / NYSE)
## Supersedes: `Sentiment/logs/watchlist_pulse_US_2026-05-15.md` (pre-open reference)
## Snapshot source: `Scripts/cache/snapshot_US_2026-05-15_190032.json`

---

## Summary Dashboard

| Metric | Value |
|---|---|
| VIX at open | 19.02 (elevated but sub-20) |
| Tickers scanned | 50 |
| URGENT alerts | 0 |
| ELEVATED alerts | 2 (CSCO.US overbought, AVGO.US gap-down) |
| POSITIVE alerts | 1 (GOOGL.US — AI momentum intact) |
| NEUTRAL alerts | 47 |

---

## Open Position Pulse

### NVDA.US (Open position — entry $235.74)
- **Alert Level: NEUTRAL**
- Open: $229.57 — down 2.62% from entry. Volume: intraday 1m bar at open (non-zero volume).
- RSI 76.72 slightly overbought but within NVDA's historical momentum range.
- MACD histogram +2.22 (bullish). Trend intact.
- No negative news catalysts in snapshot. Blackwell demand narrative ongoing.
- **Action: HOLD. Stop $224.98 intact (buffer 2.0%).**

### CAT.US (Open position — entry $919.98)
- **Alert Level: NEUTRAL**
- Open: $893.64 — down 2.86% from entry. Volume: 0 volume on the 1m bar (market just opened, gap-down print).
- RSI 60.25 healthy. MACD histogram -1.11 (slightly negative — mild weakness).
- Stop $878.37 intact (buffer $15.27 / 1.71%). Not triggered.
- Infrastructure spending narrative unchanged. No fundamental deterioration.
- **Action: HOLD. Stop $878.37 intact. CAT stop at 1.71% buffer — watch intraday closely.**

---

## High-Priority Watchlist Pulse

### CSCO.US — ELEVATED ALERT (Overbought)
- RSI: 87.47 (dangerously overbought — same as prior session ~87.5)
- 1m return: +40.3% | 3m: +54.0% | 6m: +61.1% — extended on all timeframes
- Volume_ratio_20d: 3.44 (volume surge confirms breakout but also confirms overbought risk)
- MACD histogram +1.76 (bullish but decelerating from prior session)
- **Sentiment: ELEVATED — overbought RSI at extreme levels; statistically precedes near-term correction**
- Status: WATCH continued. Entry requires RSI pullback to <75.

### AMD.US — NEUTRAL (Momentum intact, stop issue persists)
- RSI: 76.70 (elevated, not extreme)
- 1m return: +74.2% | 3m: +118.4% | 6m: +89.3% — strongest absolute momentum in universe
- Open: $440.60, last close $449.70 — opened below prior close (mild gap-down)
- ATR $22.90 — stop_atr $415.35 = 5.73% below open. Phase 1 ≤5% stop rule still violated.
- Volume ratio 0.53 (below average — reduced conviction at open)
- **Sentiment: NEUTRAL — no negative catalyst, stop issue is purely mechanical**
- Status: No entry until ATR contracts or Phase 2 relaxes stop constraint.

### AVGO.US — ELEVATED ALERT (Gap-down concern)
- Prior close: $439.79. Open: $416.73 — gap-down of $23.06 (-5.25%)
- RSI 66.12 — still healthy post gap-down
- ATR: $15.60. Stop_atr (from prior close): $416.39 = effectively AT open price (0.08% buffer)
- Recalculated stop from open: 416.73 - 1.5×15.60 = $393.33 = 5.58% below open → exceeds Phase 1 limit
- Volume_ratio: 1.02 — normal. Not a volume-driven capitulation gap.
- MACD histogram: -1.73 (negative — bearish momentum in short term)
- **Sentiment: ELEVATED — material gap-down at open, ATR stop either useless or too wide**
- Status: Gap-down likely caused by sector rotation or sympathy move. NO ENTRY. Watch for stabilization.

### GOOGL.US — POSITIVE (Strong momentum, AI theme intact)
- RSI: 74.16 (elevated but within manageable range for GOOGL momentum runs)
- 1m return: +19.0% | 3m: +29.8% | 6m: +37.7% — consistent multi-timeframe alpha vs SPY
- MACD histogram: +1.17 (bullish, stable)
- Volume_ratio: 0.75 (below 20d average — mildly low; not a volume-exhaustion concern yet)
- No negative news catalysts. Gemini AI momentum, Google Cloud growth, strong Q1 2026 earnings in the rearview.
- No upcoming earnings for ~10 weeks (Q2 results expected late July).
- Antitrust overhang is known and priced.
- **Sentiment: POSITIVE — clean momentum, no near-term event risk**

### SBUX.US — NEUTRAL (Momentum building, sector constraint applies)
- RSI 64.59 (healthy, not overbought)
- 1m: +8.2%, 3m: +10.0%, 6m: +23.1% — recovery momentum building
- MACD histogram +0.12 (bullish but very thin — early crossover)
- Volume_ratio 1.29 (above average — accumulation signal)
- **Sentiment: NEUTRAL — improving but Consumer Staples sector is NEUTRAL in Phase 1 playbook**
- Status: Phase 2 candidate. Not actionable today under Phase 1 constraints.

### UNH.US — NEUTRAL (Strong momentum but sector NEUTRAL)
- RSI 77.44 (approaching overbought zone)
- 1m: +24.6%, 3m: +34.5% — exceptional healthcare momentum (UnitedHealth specific catalyst)
- MACD histogram +0.94 (bullish)
- Volume_ratio 0.047 (extremely low — thin volume at open, price gap may normalize)
- **Sentiment: NEUTRAL — strong fundamental momentum but sector stance NEUTRAL; thin volume caution**
- Status: Monitor for Phase 2 consideration.

---

## Sector Sentiment Summary (US)

| Sector | Tickers | Avg Score | Sentiment |
|---|---|---|---|
| IT/Semis | NVDA, CSCO, AMD, AVGO, MSFT, ORCL | 57–86 | OVERWEIGHT; caution on overbought names |
| Mega-cap Internet | GOOGL, META, AMZN | 27–68 | Mixed; GOOGL standout |
| Industrials | CAT, BA, GE, HON | 29–65 | CAT leading; others neutral-weak |
| Healthcare | UNH, LLY, JNJ, PFE, MRK | 24–66 | UNH exceptional; sector otherwise neutral |
| Consumer | SBUX, WMT, COST, HD, NKE | 7–68 | SBUX leading; HD/NKE in structural bear |
| Financials | JPM, GS, BAC, V, MA | 26–57 | Range-bound; no action |
| Energy | XOM, CVX | 56–59 | Moderate; IN energy preferred |
| Materials | FCX, LIN | 62–64 | Mild momentum; no Phase 1 priority |
| REIT/Utilities | PLD, AMT, NEE | 27–43 | Defensive; no action |

---

## URGENT Alert Summary
**No URGENT alerts across the US watchlist.** 
All open US positions (NVDA, CAT) are below stop levels on the upside — stops are intact. No forced position reviews required.

---

*SentimentMonitor sub-agent | US session | Snapshot: snapshot_US_2026-05-15_190032.json | 2026-05-15 19:05 IST*
