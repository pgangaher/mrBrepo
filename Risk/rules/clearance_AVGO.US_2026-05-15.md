# RiskManager — Clearance Decision: AVGO.US
## Date: 2026-05-15 | Session: US_OPEN | Market: US (NASDAQ)

---

## Proposed Trade
- Direction: LONG
- Entry (snapshot open): $416.73
- Stop option A (snapshot stop_atr verbatim): $416.39
- Stop option B (recalculated from today's open, 1.5×ATR): $393.33
- Phase: Phase 1 (Reconnaissance)

## Risk Parameter Check

| Parameter | Rule | Option A | Option B | Pass? |
|---|---|---|---|---|
| Stop width (Phase 1) | ≤5% below entry | 0.08% — unusable | **5.58%** — exceeds 5% | **❌ FAIL both options** |
| Gap-down assessment | No material gap-down at entry | −5.25% gap from prior close | Same | **❌ ELEVATED concern** |
| MACD | Bullish preferred | Histogram −1.73 (bearish) | Same | Soft fail |
| Earnings timeline | >30 days preferred for new entries | ~3 weeks away | Same | ⚠️ CAUTION |
| Signal class | MOMENTUM_LONG | ✓ | ✓ | ✓ |
| Conviction | MEDIUM | ✓ | ✓ | ✓ |
| Sector | OVERWEIGHT | IT/Semis ✓ | IT/Semis ✓ | ✓ |
| Sentiment | Not URGENT | ELEVATED | ELEVATED | Soft fail |

## Verdict: **REJECTED**

**Primary reason:** Both stop options fail Phase 1's ≤5% stop width rule:
- Snapshot stop_atr ($416.39) is 0.08% below entry — not a valid risk-management stop.
- Recalculated stop (1.5×ATR from open, $393.33) is 5.58% below entry — exceeds Phase 1 limit.

**Secondary concerns:** MACD histogram negative (short-term bearish momentum), gap-down at open (ELEVATED sentiment), and earnings in ~3 weeks make this a poor Phase 1 entry on multiple dimensions.

**Re-evaluate conditions:**
1. Post-earnings (Q2 FY2026, expected early June 2026) with gap-fill recovery
2. ATR contracts and recalculated stop ≤5% from entry
3. MACD histogram turns positive (bullish momentum restoration)

---

*RiskManager sub-agent | AVGO.US | 2026-05-15 19:05 IST*
