# SignalEngine Report — AVGO.US
## Ticker: AVGO.US | Session: US_OPEN | Date: 2026-05-15
## Snapshot source: `Scripts/cache/snapshot_US_2026-05-15_190032.json` (verbatim)

---

## Snapshot Data (verbatim)

| Field | Value |
|---|---|
| composite_score | **69.58** |
| signal_class | **MOMENTUM_LONG** |
| conviction | **MEDIUM** |
| stop_atr | **$416.39** |
| Open price (quote.open) | $416.73 |
| Last price (quote.last) | $439.79 |
| RSI_14 | 66.12 |
| MACD line | 16.838 |
| MACD signal | 18.569 |
| MACD histogram | −1.731 (negative — bearish short-term) |
| ATR_14 | $15.60 |
| Return_1m | +10.86% |
| Return_3m | +32.80% |
| Return_6m | +24.95% |
| Volume_ratio_20d | 1.019 (normal) |
| RSI zone subscore | 75.54 |
| Momentum_1m subscore | 80 |
| Momentum_3m subscore | 90 |
| Rel_strength subscore | 72.98 |
| MACD_signal subscore | 0.0 (bearish MACD cross) |

## Interpretation

**Score 69.58 is #4 in the US universe.** Strong multi-timeframe momentum (+32.8% 3m), but the MACD histogram has turned negative (-1.73) indicating short-term bearish momentum. The volume ratio is normal (not confirming the gap-down as capitulation).

**Critical Issue — Gap-Down:**
AVGO gapped down from prior close $439.79 to open $416.73 (-$23.06 / -5.25%). This gap-down has two consequences:
1. **Snapshot stop_atr ($416.39) is essentially at open price**: Distance = (416.73 - 416.39)/416.73 = **0.08%** — functionally zero. Not a valid stop.
2. **Recalculated stop from today's open**: Using 1.5× ATR: 416.73 - 1.5 × 15.60 = 416.73 - 23.40 = **$393.33** = **5.58% below open → FAILS Phase 1 ≤5% rule** ✗

**Phase 1 Entry Gate:**
- Signal class: MOMENTUM_LONG ✓
- Conviction: MEDIUM ✓
- Stop_atr (verbatim): 0.08% below open — not a usable stop ✗
- Recalculated stop: 5.58% below open ✗
- MACD histogram negative (bearish short-term momentum) ✗
- Earnings in ~3 weeks: Event risk ✗

**Verdict: REJECTED — both stop options fail Phase 1; additional concerns from gap-down and negative MACD.**

Post-earnings entry is the preferred window (early June 2026).

---

*SignalEngine sub-agent | AVGO.US | Snapshot: snapshot_US_2026-05-15_190032.json | 2026-05-15 19:05 IST*
