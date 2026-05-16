# SignalEngine Report — AMD.US
## Ticker: AMD.US | Session: US_OPEN | Date: 2026-05-15
## Snapshot source: `Scripts/cache/snapshot_US_2026-05-15_190032.json` (verbatim)

---

## Snapshot Data (verbatim)

| Field | Value |
|---|---|
| composite_score | **76.12** |
| signal_class | **MOMENTUM_LONG** |
| conviction | **HIGH** |
| stop_atr | **$415.35** |
| Open price (quote.open) | $440.60 |
| Last price (quote.last) | $449.70 |
| RSI_14 | 76.70 |
| MACD line | 52.846 |
| MACD signal | 45.920 |
| MACD histogram | 6.926 (strongly bullish) |
| ATR_14 | $22.90 |
| Return_1m | +74.22% |
| Return_3m | +118.36% |
| Return_6m | +89.33% |
| Volume_ratio_20d | 0.533 (below average at open) |
| RSI zone subscore | 33.19 |
| Momentum_1m subscore | 98 |
| Momentum_3m subscore | 98 |
| Momentum_6m subscore | 98 |
| Rel_strength subscore | 100.0 |
| MACD_signal subscore | 50 |

## Interpretation

**Score 76.12 is the #2 score in the US universe (after CSCO 86.46).** AMD has the strongest relative strength in the universe (subscore 100) and near-perfect momentum scores on all timeframes — 1m/3m/6m subscores are 98/98/98. This is one of the highest-quality momentum signals in the universe.

**Phase 1 Entry Gate:**
- Signal class: MOMENTUM_LONG ✓
- Conviction: HIGH ✓
- stop_atr $415.35 vs open $440.60 → stop distance = (440.60 - 415.35) / 440.60 = **5.73% → FAILS Phase 1 ≤5% rule** ✗
- Volume below 20d average (0.53) — caution on open-print volume

**Comparison with prior session (snapshot_US_2026-05-15_0130.json):**
- Prior score: 76.1 | Today: 76.12 — essentially unchanged
- Prior stop: $415.80 (7.76% from $450.81 prior close) | Today: $415.35 (5.73% from $440.60 open)
- **Improvement**: Stop distance has narrowed from 7.76% to 5.73% as the stock opened below prior close. However, still above 5% threshold.
- **Trend**: Convergence toward 5% threshold — if AMD consolidates at current levels, ATR may contract below 5% threshold within 1–2 sessions.

**Verdict: REJECTED again (Phase 1 ≤5% stop rule). Monitor daily.**

Watch for: AMD close within $440–$445 range for 1–2 days → ATR contracts → stop_atr potentially below 5% from entry. Phase 2 entry possible as early as Week 2 (May 21+).

---

*SignalEngine sub-agent | AMD.US | Snapshot: snapshot_US_2026-05-15_190032.json | 2026-05-15 19:05 IST*
