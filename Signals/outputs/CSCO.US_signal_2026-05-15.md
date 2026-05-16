# SignalEngine Report — CSCO.US
## Ticker: CSCO.US | Session: US_OPEN | Date: 2026-05-15
## Snapshot source: `Scripts/cache/snapshot_US_2026-05-15_190032.json` (verbatim)

---

## Snapshot Data (verbatim)

| Field | Value |
|---|---|
| composite_score | **86.46** |
| signal_class | **MOMENTUM_LONG** |
| conviction | **HIGH** |
| stop_atr | **$110.30** |
| Open price (quote.open) | $117.55 |
| Last price (quote.last) | $115.53 |
| RSI_14 | 87.47 |
| MACD line | 5.560 |
| MACD signal | 3.797 |
| MACD histogram | 1.763 (bullish) |
| ATR_14 | $3.484 |
| Return_1m | +40.27% |
| Return_3m | +54.04% |
| Return_6m | +61.11% |
| Volume_ratio_20d | 3.44× (volume surge) |
| RSI zone subscore | 0.0 (penalized for extreme RSI) |
| Momentum_1m subscore | 96 |
| Momentum_3m subscore | 96 |
| Momentum_6m subscore | 96 |
| Rel_strength subscore | 94.22 |
| Volume_confirm subscore | 100 |
| MACD_signal subscore | 100 |

## Interpretation

**Score 86.46 is the highest in the US universe today.** All momentum subscores are at or near 100, and volume confirmation at 100 shows genuine institutional accumulation. However, the RSI zone subscore of 0.0 is a deliberate penalty built into the signal engine — RSI 87.47 is at a statistical extreme that historically precedes corrections in large-cap names.

**Phase 1 Entry Gate:**
- Signal class: MOMENTUM_LONG ✓
- Conviction: HIGH ✓
- stop_atr $110.30 vs open $117.55 → stop distance = (117.55 - 110.30) / 117.55 = **6.17% → FAILS Phase 1 ≤5% rule** ✗
- RSI 87.47 → overbought ELEVATED alert ✗

**Verdict: NO ENTRY. WATCH.** Both the Phase 1 stop width rule AND the overbought RSI screen block entry. Signal strength is extraordinary but entry timing is poor.

Next valid entry window: RSI normalizes to <75 with price holding above $105. Ideal entry at $108–$112 range on a healthy pullback, with stop recalculating to <5% below entry.

---

*SignalEngine sub-agent | CSCO.US | Snapshot: snapshot_US_2026-05-15_190032.json | 2026-05-15 19:05 IST*
