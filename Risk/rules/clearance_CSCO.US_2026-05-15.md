# RiskManager — Clearance Decision: CSCO.US
## Date: 2026-05-15 | Session: US_OPEN | Market: US (NASDAQ)

---

## Proposed Trade
- Direction: LONG
- Entry (snapshot open): $117.55
- Stop (stop_atr from snapshot): $110.30
- Phase: Phase 1 (Reconnaissance)

## Risk Parameter Check

| Parameter | Rule | Actual | Pass? |
|---|---|---|---|
| Stop width (Phase 1) | ≤5% below entry | (117.55 - 110.30)/117.55 = **6.17%** | **❌ FAIL** |
| RSI screen | <85 preferred for new entry | **87.47** | **❌ ELEVATED** |
| Signal class | MOMENTUM_LONG required | MOMENTUM_LONG | ✓ |
| Conviction | HIGH or MEDIUM | HIGH | ✓ |
| Sector alignment | OVERWEIGHT | IT/Semis OVERWEIGHT | ✓ |
| Sentiment | Not URGENT | ELEVATED | Soft fail |
| Position count | Max 4 in Phase 1 | Currently 2 + proposed = 3 | ✓ |
| Deployment | Max 40% deployed | 16% + proposed 8% = 24% | ✓ |

## Verdict: **REJECTED**

**Reason:** Phase 1 hard stop rule requires stop ≤5% below entry price. At open price $117.55, the ATR stop of $110.30 is 6.17% below entry — exceeds the Phase 1 limit. Additionally, RSI 87.47 is at an extreme level that statistically precedes corrections; entering at this RSI level violates sound risk management practice.

**Override available?** Not in Phase 1. Override only permitted in Phase 2+ with explicit Mr.B notation in TradeLog.

**Re-evaluate conditions:**
1. RSI pulls back to <75
2. Price holds above $105 (prior consolidation support)
3. ATR stop recalculates to <5% below entry (requires price ~$116–$118 with reduced ATR)

---

*RiskManager sub-agent | CSCO.US | 2026-05-15 19:05 IST*
