# RiskManager — Pre-Trade Clearance
## Ticker: ADANIPORTS.NS | Date: 2026-05-15 | Market: IN

---

## Trade Parameters Submitted

| Field | Value |
|---|---|
| Direction | LONG |
| Entry price | ₹1,807.90 |
| Stop loss | ₹1,730.71 |
| Target 1 | ₹1,950.00 |
| Target 2 | ₹2,100.00 |
| Proposed size | 6% of IN NAV (reduced from 10% due to RSI 70.6) |
| Shares | 33 |
| Notional | ₹59,661 |

---

## Risk Checks

| Check | Threshold | Actual | Pass? |
|---|---|---|---|
| Stop width | ≤5% Phase 1 | 4.27% | ✓ PASS |
| Position size | ≤10% (HIGH) / used 6% | 6.0% | ✓ PASS (modification) |
| Sector concentration (Industrials) | ≤25% NAV | 6.0% | ✓ PASS |
| Phase 1 total deployment | ≤40% | 16.0% cumulative | ✓ PASS |
| R:R ratio (Target 1) | ≥1.5:1 | (₹142.1 / ₹77.19) = **1.84:1** | ✓ PASS |
| R:R ratio (Target 2) | ≥2.5:1 | (₹292.1 / ₹77.19) = **3.79:1** | ✓ PASS |
| Cash floor after trade | ≥10% | 84.0% remaining | ✓ PASS |
| Portfolio drawdown | <15% | 0% (Day 2) | ✓ PASS |
| Earnings within 7 days | None | Q4 results >2 weeks away | ✓ PASS |

---

## Modification Note

**RSI 70.6** is at the overbought boundary. Rule: when RSI is between 68–72, RiskManager applies position size haircut to 60% of conviction-based allocation.
- Original allocation (HIGH conviction): 10% = ₹1,00,000
- Modified allocation: 6% = ₹60,000 → 33 shares at ₹1,807.90

When RSI cools below 67 on a pullback, the ADD action can bring position to full 10% (add ~22 more shares).

---

## Friction

- Estimated cost (0.075% one-way): ₹45
- Breakeven price: ₹1,809.26

---

## Verdict

**APPROVED WITH MODIFICATION** — 6% position (33 shares), not the full 10%.

All checks pass at modified size. ADANIPORTS.NS cleared for LONG entry at ₹1,807.90. Stop ₹1,730.71 (−4.27%). Targets ₹1,950 and ₹2,100. Add-on target: if RSI cools <67, add 22 shares to bring to full 10% (requires fresh five-layer check at that time).

---

*RiskManager sub-agent | IN sub-portfolio | 2026-05-15*
