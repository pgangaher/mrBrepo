# Trade Log — workspace-broker

> **APPEND-ONLY**: This file is a permanent record. Entries are never deleted, edited, or overwritten. New events are appended at the bottom. Each entry is numbered sequentially.

---

## Header

| Field | Value |
|---|---|
| Strategy Start Date | 2026-05-14 |
| IN Starting NAV | ₹10,00,000 INR |
| US Starting NAV | $10,000.00 USD |
| IN Benchmark | NIFTY 50 (^NSEI) from 2026-05-14 |
| US Benchmark | S&P 500 / SPY from 2026-05-14 |
| SPY Start Level (approx) | ~$568 (2026-05-14 close reference) |

---

## Trade Entry Format

Each trade event (OPEN, ADD, TRIM, CLOSE, OVERRIDE) uses the block below. Copy the template and append at the bottom of this file.

```
---
## Trade #[N] — [TICKER] — [EVENT TYPE]
Date: [YYYY-MM-DD]
Event: OPEN | ADD | TRIM | CLOSE | OVERRIDE LOG

### Position Details
Ticker: [TICKER]
Company: [Full company name]
Direction: LONG | SHORT
Shares this action: [X]
Price: $[X.XX]
Total shares held after action: [X]
Cost basis this lot: $[X]

### Risk Parameters (for OPEN and ADD)
Stop Loss: $[X.XX] ([X]% below entry)
Target 1: $[X.XX] ([X:1] R)
Target 2: $[X.XX] ([X:1] R)

### Signal Context (for OPEN and ADD)
SignalEngine class: [class]
SignalEngine confidence: HIGH | MEDIUM | LOW
SignalEngine score: [0–100]
RiskManager verdict: APPROVED | APPROVED WITH MODIFICATION | REJECTED + OVERRIDE
StrategyAdvisor sector: OVERWEIGHT | NEUTRAL | UNDERWEIGHT (alignment status)
SentimentMonitor alert: URGENT | ELEVATED | NEUTRAL | POSITIVE

### Thesis (for OPEN and ADD)
[2–4 sentences: why this trade, what is the expected catalyst, what would invalidate the thesis]

### P&L (for TRIM and CLOSE)
Average entry price: $[X.XX]
Exit price: $[X.XX]
Shares exited: [X]
Gross P&L this action: $[X] ([+/-X]%)
Cumulative realized P&L all trades: $[X]
Exit reason: TARGET_1_HIT | TARGET_2_HIT | STOP_HIT | SENTIMENT_CHANGE | STRATEGY_ROTATION | THESIS_BROKEN | FORCED_TRIM | PHASE_3_HARVEST

### Override Details (for OVERRIDE LOG only)
RiskManager original verdict: REJECTED
Override reason: [Mr.B's stated reason for proceeding]
Risk acknowledged: YES

### Mr.B Notes
[Any qualitative observation — what worked, what surprised, what to watch]
---
```

---

## Live Trade Log

> Entries begin here. Append new trades below this line.

---
## Trade #1 — ONGC.NS — OPEN
Date: 2026-05-15
Event: OPEN

### Position Details
Ticker: ONGC.NS
Company: Oil and Natural Gas Corporation Ltd
Direction: LONG
Shares this action: 332
Price: ₹301.15
Total shares held after action: 332
Cost basis this lot: ₹99,982 (incl. ₹75 friction @ 0.075%)
Fill session: IN_MIDDAY (last print at 12:30 IST)
Fill source: yfinance snapshot_IN_2026-05-15_1230.json

### Risk Parameters
Stop Loss: ₹290.09 (−3.67% below entry)
Target 1: ₹320.00 (+6.27%, R:R 1.70:1)
Target 2: ₹340.00 (+12.89%, R:R 3.51:1)

### Signal Context
SignalEngine class: MOMENTUM_LONG
SignalEngine confidence: HIGH
SignalEngine score: 74.86/100
RiskManager verdict: APPROVED
StrategyAdvisor sector: OVERWEIGHT (Energy, Choppy/Sector-Rotation regime)
SentimentMonitor alert: NEUTRAL

### Thesis
ONGC is India's dominant upstream E&P with deep value (P/E ~8x), massive outperformance vs NIFTY (NIFTY −8.3% 3m vs ONGC +10.6%), and clean RSI 62.8 momentum without overbought risk. The Energy sector is the primary rotation beneficiary in the current Choppy regime. ATR stop at 3.67% keeps Phase 1 risk tight. Thesis invalidated by crude oil sustained below $68/bbl or policy reinstatement of upstream subsidy burden.

### Mr.B Notes
First trade of the paper run. Cleanest Phase 1 setup in the 50-name IN universe by risk-adjusted profile. RSI momentum healthy, not extended. Chosen as anchor of the IN sub-portfolio.
---

---
## Trade #2 — ADANIPORTS.NS — OPEN
Date: 2026-05-15
Event: OPEN

### Position Details
Ticker: ADANIPORTS.NS
Company: Adani Ports and Special Economic Zone Ltd
Direction: LONG
Shares this action: 33
Price: ₹1,807.90
Total shares held after action: 33
Cost basis this lot: ₹59,661 (incl. ₹45 friction)
Fill session: IN_MIDDAY (last print at 12:30 IST)
Fill source: yfinance snapshot_IN_2026-05-15_1230.json

### Risk Parameters
Stop Loss: ₹1,730.71 (−4.27% below entry)
Target 1: ₹1,950.00 (+7.86%, R:R 1.84:1)
Target 2: ₹2,100.00 (+16.18%, R:R 3.79:1)

### Signal Context
SignalEngine class: MOMENTUM_LONG
SignalEngine confidence: HIGH
SignalEngine score: 78.59/100
RiskManager verdict: APPROVED WITH MODIFICATION (6% position, not 10%, due to RSI 70.6)
StrategyAdvisor sector: NEUTRAL→OVERWEIGHT (Infrastructure/Ports)
SentimentMonitor alert: NEUTRAL

### Thesis
India's largest port operator with 25%+ market share, 60%+ EBITDA margins, and strong cargo volume growth driven by India's $1T export target. Adani governance narrative has normalized post-2023. RSI 70.6 near overbought — position sized at 6% (not full 10%). Add-on planned if RSI cools to <67 on a healthy pullback.

### Mr.B Notes
Second trade. RiskManager approved with modification — position haircut to 6%. Strong absolute score (78.59) and momentum story intact. Watch for Adani group-level news closely.
---

---
## Trade #3 — HINDALCO.NS — OPEN
Date: 2026-05-15
Event: OPEN

### Position Details
Ticker: HINDALCO.NS
Company: Hindalco Industries Ltd
Direction: LONG
Shares this action: 55
Price: ₹1,080.50
Total shares held after action: 55
Cost basis this lot: ₹59,428 (incl. ₹45 friction)
Fill session: IN_MIDDAY (last print at 12:30 IST)
Fill source: yfinance snapshot_IN_2026-05-15_1230.json

### Risk Parameters
Stop Loss: ₹1,038.40 (−3.90% below entry)
Target 1: ₹1,160.00 (+7.36%, R:R 1.89:1)
Target 2: ₹1,220.00 (+12.92%, R:R 3.31:1)

### Signal Context
SignalEngine class: MOMENTUM_LONG
SignalEngine confidence: MEDIUM
SignalEngine score: 65.9/100
RiskManager verdict: APPROVED
StrategyAdvisor sector: OVERWEIGHT (Metals)
SentimentMonitor alert: NEUTRAL

### Thesis
Hindalco is a diversified global aluminium + copper play: Novelis (world's largest recycled aluminium maker) gives structural EV tailwind exposure; copper from Birla Copper benefits from energy transition infra build. RSI 61.4 healthy, 3m return +11.5% vs NIFTY −8.3%. Diversifies IN portfolio away from pure Energy/Ports.

### Mr.B Notes
Third trade. MEDIUM conviction at 6% NAV. Chosen for sector diversification. Novelis is the long-term value driver here — watch Novelis quarterly metrics when available.
---

---
## Trade #4 — NVDA.US — OPEN

Date: 2026-05-15
Event: OPEN

### Position Details
Ticker: NVDA.US
Company: NVIDIA Corporation
Direction: LONG
Shares this action: 4.24 (paper fractional)
Price: $235.74
Total shares held after action: 4.24
Cost basis this lot: $1,000.00 (incl. $0.25 friction)
Fill session: US reference price (May 14 US close)
Fill source: yfinance snapshot_US_2026-05-15_0130.json

### Risk Parameters
Stop Loss: $224.98 (−4.56% below entry)
Target 1: $255.00 (+8.17%, R:R 1.79:1)
Target 2: $270.00 (+14.53%, R:R 3.19:1)

### Signal Context
SignalEngine class: MOMENTUM_LONG
SignalEngine confidence: HIGH
SignalEngine score: 74.1/100
RiskManager verdict: APPROVED (with earnings watch flag for ~May 28)
StrategyAdvisor sector: OVERWEIGHT (IT/Semis, Risk-On Trending regime)
SentimentMonitor alert: POSITIVE

### Thesis
NVDA is the dominant AI infrastructure play: CUDA moat, Blackwell GPU demand with multiyear hyperscaler backlog, sovereign AI expansion. 1m return +18.5%, 3m +26.1% vs SPY +9.8%. RSI 76.7 elevated but historically sustained at this level during NVDA momentum cycles. Earnings ~May 28 is the key near-term event — triple check scheduled May 21. Thesis invalidated by AI capex slowdown signal, major export restriction expansion, or RSI >85 with bearish divergence.

### Mr.B Notes
Anchor US position. Stop 4.56% is just within Phase 1 limit. Earnings flag active — will reassess May 21 whether to hold through or trim pre-earnings.
---

---
## Trade #5 — CAT.US — OPEN
Date: 2026-05-15
Event: OPEN

### Position Details
Ticker: CAT.US
Company: Caterpillar Inc.
Direction: LONG
Shares this action: 0.65 (paper fractional)
Price: $919.98
Total shares held after action: 0.65
Cost basis this lot: $597.99 (incl. $0.15 friction)
Fill session: US reference price (May 14 US close)
Fill source: yfinance snapshot_US_2026-05-15_0130.json

### Risk Parameters
Stop Loss: $878.37 (−4.52% below entry)
Target 1: $982.00 (+6.74%, R:R 1.53:1) [revised from $975 per RiskManager T1 adjustment]
Target 2: $1,030.00 (+11.96%, R:R 2.64:1)

### Signal Context
SignalEngine class: MOMENTUM_LONG
SignalEngine confidence: MEDIUM
SignalEngine score: 69.7/100
RiskManager verdict: APPROVED WITH MODIFICATION (T1 revised to $982)
StrategyAdvisor sector: OVERWEIGHT (Industrials)
SentimentMonitor alert: NEUTRAL

### Thesis
Caterpillar sits at the intersection of the US infrastructure boom (IIJA spending), AI data center construction (massive earthmoving/construction for hyperscaler campuses), and critical mineral mining (copper, lithium). RSI 66.4 clean, 3m return +21.3% vs SPY +9.8%. No earnings concern until late July. Diversifies US portfolio away from pure semiconductor exposure.

### Mr.B Notes
Second US position. Provides industrial/infrastructure sector diversification vs NVDA's semiconductor weight. CAT's data center construction angle is underappreciated by the market.
---

---
## Trade #6 — GOOGL.US — OPEN
Date: 2026-05-15
Event: OPEN

### Position Details
Ticker: GOOGL.US
Company: Alphabet Inc. (Class A)
Direction: LONG
Shares this action: 2.01 (paper fractional)
Price: $397.28
Total shares held after action: 2.01
Cost basis this lot: $798.53 (incl. ~$0.20 friction)
Fill session: US_OPEN (snapshot open price, 09:30 EDT)
Fill source: yfinance snapshot_US_2026-05-15_190032.json

### Risk Parameters
Stop Loss: $386.30 (−2.76% below entry)
Target 1: $419.24 (+5.52%, R:R 2.00:1)
Target 2: $441.20 (+11.07%, R:R 4.01:1)

### Signal Context
SignalEngine class: MOMENTUM_LONG
SignalEngine confidence: MEDIUM
SignalEngine score: 68.14/100
RiskManager verdict: APPROVED
StrategyAdvisor sector: OVERWEIGHT (IT/Tech, Risk-On Trending regime)
SentimentMonitor alert: POSITIVE

### Thesis
Alphabet offers the most durable moat in technology (Google Search 91% market share) combined with a cloud business growing 28% YoY with genuine AI differentiation (Gemini + TPU). At 22x forward P/E with $100B net cash and 29.8% 3m alpha vs SPY (+20ppt), GOOGL represents the highest-quality risk-adjusted entry available in the US universe today. RSI 74.16 elevated but within GOOGL's historical momentum range. No earnings event for ~10 weeks. Adds meaningful portfolio diversification — consumer internet + cloud vs pure semiconductor (NVDA) and industrial (CAT). Thesis invalidated by adverse DOJ search divestiture ruling, sustained Search market share loss >5ppt to AI competitors, or Google Cloud growth deceleration below 15%.

### Mr.B Notes
Third US position (Trade #6 overall in paper run). Clean five-layer pass: all layers APPROVED/POSITIVE. The 2.76% ATR stop is the tightest of the three US positions — good risk management. Portfolio now 24% deployed, 3/4 Phase 1 slots filled. One position slot remaining for Phase 1.
---
