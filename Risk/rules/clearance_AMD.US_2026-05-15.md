# RiskManager — Clearance Decision: AMD.US
## Date: 2026-05-15 | Session: US_OPEN | Market: US (NASDAQ)

---

## Proposed Trade
- Direction: LONG
- Entry (snapshot open): $440.60
- Stop (stop_atr from snapshot): $415.35
- Phase: Phase 1 (Reconnaissance)

## Risk Parameter Check

| Parameter | Rule | Actual | Pass? |
|---|---|---|---|
| Stop width (Phase 1) | ≤5% below entry | (440.60 - 415.35)/440.60 = **5.73%** | **❌ FAIL** |
| RSI screen | Acceptable | 76.70 (elevated, acceptable) | ✓ |
| Signal class | MOMENTUM_LONG | MOMENTUM_LONG | ✓ |
| Conviction | HIGH or MEDIUM | HIGH | ✓ |
| Sector alignment | OVERWEIGHT | IT/Semis OVERWEIGHT | ✓ |
| Sentiment | Not URGENT | NEUTRAL | ✓ |
| Position count | Max 4 in Phase 1 | Currently 2 + proposed = 3 | ✓ |
| Deployment | Max 40% deployed | 16% + proposed 8% = 24% | ✓ |

## Verdict: **REJECTED (Second consecutive session)**

**Reason:** Phase 1 hard stop rule requires stop ≤5% below entry. AMD's ATR ($22.90) creates a stop 5.73% below the open price of $440.60. This is an improvement from yesterday's 7.76% but still above threshold.

**Improvement noted:** Stop distance has narrowed from 7.76% (prior session) to 5.73% today. The convergence toward the 5% threshold is positive. If AMD consolidates near current levels and ATR contracts:
- ATR contracts to ~$20 → stop = 440.60 - 1.5 × 20 = $410.60 = 6.8% — still failing
- For stop to be ≤5%: (entry - stop)/entry ≤ 0.05 → stop ≥ 0.95 × entry. At entry $440.60, stop ≥ $418.57. Gap to $415.35 is $3.22 — needs about 2 more days of consolidation + ATR contraction.

**Override available?** Phase 2 (Week 2+) allows Mr.B discretion. Minimum: May 21 for Phase 2 entry under stop-width relaxation.

---

*RiskManager sub-agent | AMD.US | 2026-05-15 19:05 IST*
