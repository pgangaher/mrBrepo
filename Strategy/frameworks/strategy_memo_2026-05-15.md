# StrategyAdvisor — Macro Regime Memo
## Date: 2026-05-15 | Session: IN_MIDDAY (manual five-layer gate)

---

## India Macro Regime

| Indicator | Value | Signal |
|---|---|---|
| India VIX | 18.49 | Elevated — caution, not panic |
| NIFTY 50 3m return | −8.30% | Bearish benchmark trend |
| USD/INR | ~83.5 (est.) | Stable, mild INR depreciation |
| Macro stance | RBI accommodative-neutral | Rate-sensitive watchful |
| FII/DII flows | DII net buyers offsetting FII outflows | Mixed |

### IN Regime Classification: **CHOPPY / SECTOR ROTATION**

The benchmark (NIFTY 50) is down −8.3% over 3 months, indicating a broad market correction. However, significant divergence is visible: Energy and Conglomerates are strongly outperforming. This is a classic sector-rotation environment — not a full Risk-Off, but not Risk-On Trending either.

**Sector Directives (IN):**

| Sector | Signal | Stance |
|---|---|---|
| Energy (ONGC, RELIANCE, NTPC) | Strong relative strength vs NIFTY | **OVERWEIGHT** |
| Metals (HINDALCO, TATASTEEL) | Recovery momentum | **OVERWEIGHT** |
| Conglomerates (ADANIENT, ADANIPORTS) | Highest absolute momentum | **NEUTRAL → OVERWEIGHT** (governance risk discount) |
| Banks (HDFC, ICICI, KOTAK) | Neutral, no clear trend | **NEUTRAL** |
| FMCG (HUL, ITC, BRITANNIA) | Mild momentum, defensive | **NEUTRAL** |
| IT (TCS, INFY, HCLTECH, WIPRO, TECHM) | Structural bear — RSI 26–40, −17% to −28% 3m | **AVOID** |
| Pharma (SUNPHARMA, DRREDDY) | Recovering — watch | **NEUTRAL** |

**Phase 1 Constraint**: Recon mode. Max 40% deployed. Max 4 positions. New longs only in OVERWEIGHT sectors or strong NEUTRAL exceptions.

---

## US Macro Regime

| Indicator | Value | Signal |
|---|---|---|
| VIX | 17.30 | Moderate — controlled risk appetite |
| SPY 3m return | +9.80% | Bullish benchmark trend |
| Fed stance | Hawkish-neutral (data-dependent) | Watching CPI/PCE |
| USD | Stable-strong | Supportive of US equities |

### US Regime Classification: **RISK-ON TRENDING**

The US market is in a healthy uptrend (+9.8% on SPY over 3 months) with controlled volatility (VIX 17.3). AI/semiconductor cycle is the dominant theme. Momentum leaders in IT, Industrials, and select Consumer Discretionary are extending gains.

**Sector Directives (US):**

| Sector | Signal | Stance |
|---|---|---|
| IT / Semis (NVDA, AMD, CSCO, AVGO) | Strong — AI cycle dominant | **OVERWEIGHT** |
| Industrials (CAT, GE, BA) | Strong — infrastructure capex | **OVERWEIGHT** |
| Consumer Discretionary (AMZN, TSLA) | Moderate | **NEUTRAL** |
| Consumer Staples (WMT, KO, PEP) | Defensive, mild | **NEUTRAL** |
| Health Care (LLY, UNH, JNJ) | Mixed | **NEUTRAL** |
| Financials (JPM, GS, V, MA) | Solid | **NEUTRAL** |
| Energy (XOM, CVX) | Moderate | **NEUTRAL** |

**Phase 1 Constraint**: Same recon limits as IN. Entry only in OVERWEIGHT sectors.

---

## Phase 1 Playbook (Week 1, May 14–18)

- Max 40% deployed per sub-portfolio
- Max 4 positions per market
- Only HIGH/MEDIUM conviction signals with MOMENTUM_LONG class
- Stop ≤ 5% ATR from entry
- Cash floor 10% always maintained

**IN priority list**: ONGC.NS → ADANIPORTS.NS → HINDALCO.NS
**US priority list**: NVDA.US → CAT.US → (AMD.US watch for stop width issue)

---

*Written by: StrategyAdvisor sub-agent | Authorized: Mr.B | 2026-05-15 12:30 IST*

---

## US Macro Regime — US_OPEN Update (19:00 IST / 09:30 EDT)

> Supersedes the US block above for open-session decisions. Snapshot source: `Scripts/cache/snapshot_US_2026-05-15_190032.json`

| Indicator | Midday (01:30 IST) | US_OPEN (19:00 IST) | Signal |
|---|---|---|---|
| VIX | 17.30 | **19.02** | +1.72 pts — elevated caution at open |
| SPY 3m return | +9.80% | **+9.82%** | Stable uptrend |
| Fed posture | Hawkish-neutral | Unchanged | Data-dependent |
| DXY | Stable-strong | Estimated stable | No dislocation |
| 10Y Treasury | ~4.4% est. | ~4.4% est. | Neutral |
| Credit spreads | Normal | Normal | No stress signal |

### US_OPEN Regime Classification: **RISK-ON TRENDING (CAUTION ELEVATED)**

The US market remains in a medium-term uptrend (+9.82% SPY 3m), but the VIX tick-up to 19.02 at the NASDAQ open signals above-average short-term uncertainty. This is within normal Risk-On bounds (VIX < 20) but warrants tighter position discipline. Key macro driver remains the AI/semiconductor cycle and ongoing infrastructure capex narrative.

**US_OPEN Sector Directives (unchanged from midday, minor notes added):**

| Sector | Stance | US_OPEN Note |
|---|---|---|
| IT / Semis (NVDA, AMD, CSCO, AVGO, GOOGL) | **OVERWEIGHT** | Remain primary long theme; VIX caution means RSI extremes require respect |
| Industrials (CAT, GE) | **OVERWEIGHT** | CAT gap-down at open — existing position intact above stop |
| Consumer Discretionary (AMZN, TSLA) | **NEUTRAL** | AMZN MACD histogram negative — wait for confirmation |
| Consumer Staples (WMT, KO, SBUX) | **NEUTRAL** | SBUX has momentum but deferred to Phase 2 per sector constraint |
| Health Care (LLY, UNH) | **NEUTRAL** | UNH strong momentum (+34.5% 3m) but sector not OVERWEIGHT in Phase 1 |
| Financials (JPM, GS, V, MA) | **NEUTRAL** | Range-bound; no action in Phase 1 |
| Energy (XOM, CVX) | **NEUTRAL** | US energy lagging; focus is on IN energy (ONGC) |

**Phase 1 Constraint — US_OPEN application:**
- Max 4 positions. Currently: 2 open (NVDA, CAT). Room for 2 more.
- Max 40% deployed. Currently: 16%. Room: 24% (~$2,400).
- Stop ≤5% from entry — applied to all new entries at today's open price.
- New longs: OVERWEIGHT sectors only. GOOGL.US qualifies (IT/Tech OVERWEIGHT).

**Open position monitoring:**
- NVDA.US: Entry $235.74 → Open $229.57 (-2.62%). Stop $224.98. Buffer: $4.59 (2.0%). **HOLD — not stopped.**
- CAT.US: Entry $919.98 → Open $893.64 (-2.86%). Stop $878.37. Buffer: $15.27 (1.71%). **HOLD — not stopped.**
- No defensive mode trigger: drawdown ~0.43% NAV, far below 15% threshold.

*US_OPEN update appended by: StrategyAdvisor sub-agent | Authorized: Mr.B | 2026-05-15 19:05 IST*
