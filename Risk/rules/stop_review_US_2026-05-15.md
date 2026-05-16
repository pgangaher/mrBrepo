# RiskManager — Stop Loss Review: US Sub-Portfolio
## Date: 2026-05-15 | Session: US_MIDDAY (22:00 IST / 12:30 EDT)
## Market: US (NASDAQ / NYSE) | Type: Routine Mid-Session Trail Check
## Snapshot source: `Scripts/cache/snapshot_US_2026-05-15_220028.json`

---

## Portfolio State at Review Time

| Ticker | Entry | Entry Date | Midday Price | Stop (Current) | Buffer $ | Buffer % | P&L $ | Status |
|---|---|---|---|---|---|---|---|---|
| NVDA.US | $235.74 | 2026-05-15 | $228.40 | $224.98 | $3.42 | 1.50% | −$31.12 | ELEVATED |
| CAT.US | $919.98 | 2026-05-15 | $885.44 | $878.37 | $7.07 | 0.80% | −$22.45 | ELEVATED |
| GOOGL.US | $397.28 | 2026-05-15 | $397.16 | $386.30 | $10.86 | 2.73% | −$0.24 | NORMAL |

**VIX midday:** 18.37 (improving from 19.02 at open)
**Total unrealized P&L:** −$53.81 (−0.54% NAV)
**Drawdown from peak:** 0.54% — DEFENSIVE MODE: NOT ACTIVE (threshold: 15%)

---

## Individual Stop Reviews

---

### 1. NVDA.US — ELEVATED ⚠️

**Intraday stop breach event:**
- Paper stop: $224.98
- Intraday low: $224.25 ← **$0.73 below stop**
- Recovery to midday last_price: $228.40
- In live trading, stop order at $224.98 would have executed at $224.98 (or next available print)

**Paper trade ruling:**
Per `_preamble.md`, midday session fills use `quote.last_price`. Since the midday last_price ($228.40) is ABOVE the stop ($224.98), no paper fill is executed at this session. The intraday breach is logged as a **material risk event** requiring elevated monitoring through US_CLOSE.

**Stop trail assessment:**
- Position is −3.11% below entry → trailing UP is NOT applicable
- Existing stop $224.98 (−4.56% from entry) provides tighter protection than ATR stop ($217.23 = −7.69% from entry)
- **Verdict: MAINTAIN stop at $224.98. Do NOT widen.**

**Risk metrics:**
| Metric | Value |
|---|---|
| Max risk if stop triggers | 4.24 × ($235.74 − $224.98) = **−$45.62** |
| Max risk % NAV | **0.46%** |
| Current buffer from stop | $3.42 / 1.50% |
| ATR midday ($7.50) | Stop provides 0.46× ATR cushion — thin but valid |

**RiskManager verdict: MAINTAIN STOP $224.98. ELEVATED WATCH through US_CLOSE.**

If US_CLOSE price is below $224.98 → paper close at close price, log Trade #4 close.
If US_CLOSE price is above $224.98 → position continues with same stop into next session.

---

### 2. CAT.US — ELEVATED ⚠️

**Near-stop event:**
- Paper stop: $878.37
- Intraday low: $880.20 — buffer at worst: $1.83 / 0.21%
- Recovery to midday last_price: $885.44

**Stop trail assessment:**
- Position is −3.75% below entry → trailing UP is NOT applicable
- Existing stop $878.37 (−4.52% from entry) is tighter than ATR stop ($841.97 = −8.48% from entry)
- ATR has widened intraday ($28.61 today vs ~$22 at open) — this is what makes the ATR stop so much wider
- **Verdict: MAINTAIN stop at $878.37. Do NOT widen to $841.97 ATR stop.**

**Risk metrics:**
| Metric | Value |
|---|---|
| Max risk if stop triggers | 0.65 × ($919.98 − $878.37) = **−$27.05** |
| Max risk % NAV | **0.27%** |
| Current buffer from stop | $7.07 / 0.80% |
| Tightest intraday buffer | $1.83 / 0.21% at low $880.20 |
| ATR midday ($28.61) | Stop is 0.25× ATR from current price — very tight |

**RiskManager verdict: MAINTAIN STOP $878.37. ELEVATED WATCH through US_CLOSE.**

If US_CLOSE price is below $878.37 → paper close at close price, log Trade #5 close.
If US_CLOSE price is above $878.37 → position continues with same stop into next session.

---

### 3. GOOGL.US — NORMAL ✓

**Standard review:**
- Intraday low $393.18 — stop buffer at worst: $393.18 − $386.30 = $6.88 / 1.73%
- Recovery to midday last_price: $397.16

**Stop trail assessment:**
- Position is −0.03% below entry (essentially flat) → trailing UP is NOT applicable
- Existing stop $386.30 (−2.76% from entry) is tighter than ATR stop ($382.60 = −3.70% from entry)
- **Verdict: MAINTAIN stop at $386.30.**

**Risk metrics:**
| Metric | Value |
|---|---|
| Max risk if stop triggers | 2.01 × ($397.28 − $386.30) = **−$22.07** |
| Max risk % NAV | **0.22%** |
| Current buffer from stop | $10.86 / 2.73% |

**RiskManager verdict: MAINTAIN STOP $386.30. Standard monitoring.**

---

## Portfolio-Level Risk Summary

| Metric | Value | Limit | Status |
|---|---|---|---|
| Total unrealized P&L | −$53.81 | — | — |
| Max total risk (all stops) | −$94.74 | — | 0.95% NAV |
| Drawdown from peak NAV | 0.54% | 15% | ✓ SAFE |
| Positions at ELEVATED risk | 2 (NVDA, CAT) | — | Monitor |
| Defensive mode trigger | 15% drawdown | Not active | — |
| Positions with intraday stop breach | 1 (NVDA) | — | Log event |
| Positions near-stop (≤1% buffer) | 1 (CAT at 0.80%) | — | Monitor |

---

## Stop Actions Taken This Session

| Ticker | Action | New Stop | Reason |
|---|---|---|---|
| NVDA.US | NO CHANGE | $224.98 | Intraday breach logged; midday price above stop; maintain |
| CAT.US | NO CHANGE | $878.37 | Near-stop event logged; position above stop; maintain |
| GOOGL.US | NO CHANGE | $386.30 | Healthy; standard review confirms stop appropriate |

**No stops were adjusted this session.**

---

## Intraday Breach Log

| Ticker | Stop | Intraday Low | Breach Amount | Recovery Price | Paper Action |
|---|---|---|---|---|---|
| NVDA.US | $224.98 | $224.25 | −$0.73 | $228.40 | NO CLOSE — midday price above stop; logged as material event |

---

*RiskManager sub-agent | US_MIDDAY | US sub-portfolio | 2026-05-15 22:00 IST*
