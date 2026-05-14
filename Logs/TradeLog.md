# Trade Log — workspace-broker

> **APPEND-ONLY**: This file is a permanent record. Entries are never deleted, edited, or overwritten. New events are appended at the bottom. Each entry is numbered sequentially.

---

## Header

| Field | Value |
|---|---|
| Strategy Start Date | [Fill in before first trade] |
| Starting NAV | $[Fill in before first trade] |
| Benchmark | S&P 500 / SPY from strategy start date |
| Benchmark Start Level | $[Fill in SPY price on strategy start date] |

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

*(No trades yet — log starts with first trade)*
