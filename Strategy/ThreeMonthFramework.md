# Three-Month Investment Framework — Mr.B's Master Playbook

> This document is the strategic anchor for all decisions in the 3-month trading window. Mr.B references it before every new trade and every weekly review. StrategyAdvisor uses it to report framework progress. It is never deleted and never overwritten — updates are appended as versioned amendments.

---

## Strategy Header

| Field | Value |
|---|---|
| Strategy Period | [Fill in: start date] to [Fill in: end date — 12 weeks later] |
| Starting NAV | $[Fill in before first trade] |
| Return Target | 20–30% net over 3 months (aggressive growth) |
| Benchmark | S&P 500 total return (SPY) from strategy start date |
| Alpha Target | Outperform S&P 500 by at least 10% over the period |
| Max Drawdown Tolerance | 15% from peak NAV (triggers defensive mode per RiskManager rules) |

---

## The Five-Layer Decision Gate

Every new trade must pass all five layers before Mr.B finalizes it. No shortcuts.

```
Layer 1 → ResearchAnalyst: Fundamental thesis confirmed
Layer 2 → SignalEngine: HIGH or MEDIUM confidence signal (≥40 score)
Layer 3 → StrategyAdvisor: Sector aligned with current rotation priorities
Layer 4 → SentimentMonitor: Alert level NEUTRAL or POSITIVE
Layer 5 → RiskManager: Risk Clearance = APPROVED or APPROVED WITH MODIFICATION
```

A trade fails if ANY layer raises a hard block (broken thesis, NO_SIGNAL class, sector AVOID, URGENT sentiment against position, or REJECTED risk clearance).

---

## Three-Phase Structure

### Phase 1: Reconnaissance and Foundation (Weeks 1–3)

**Objective**: Build the watchlist. Deploy capital selectively into 2–3 highest-conviction names only. Get all sub-agents calibrated.

| Parameter | Limit |
|---|---|
| Max capital deployed | 40% of NAV |
| Max open positions | 4 |
| Risk posture | CONSERVATIVE |
| Position sizing | Half of RiskManager recommended size |
| Stop tightness | Tighter — max 5% from entry (not 8%) |

**Priority tasks for this phase**:
1. Run `MACRO REGIME CHECK` via StrategyAdvisor before the first trade.
2. Build and vet a watchlist of 10–15 names using ResearchAnalyst.
3. Run `WATCHLIST SCORE` via SignalEngine to rank the list.
4. Open 2–3 positions only in HIGH-signal, highest-conviction names.
5. Start `TradeLog.md` with the first trade entry.
6. Set first `BENCHMARK UPDATE` in PortfolioTracker with strategy start NAV and S&P 500 level.

**Phase 1 exit criteria**: 3 vetted positions open, watchlist populated, all sub-agents tested, weekly review cadence established.

---

### Phase 2: Conviction Deployment (Weeks 4–8)

**Objective**: Scale into winners. Add 2–3 new positions. Push to 65–80% deployment. Pursue alpha through momentum and earnings catalysts.

| Parameter | Limit |
|---|---|
| Max capital deployed | 80% of NAV (with 10% cash floor + 10% dry powder) |
| Max open positions | 8 |
| Risk posture | MODERATE TO AGGRESSIVE |
| Position sizing | Full RiskManager recommended size for HIGH conviction |
| Stop tightness | Trail stops on winners — do not allow > 50% of unrealized gains to give back |

**Priority tasks for this phase**:
1. Weekly Monday sweep: StrategyAdvisor WEEKLY BRIEF + SignalEngine WATCHLIST SCORE.
2. Add to positions that have confirmed momentum (price > entry, signal still HIGH).
3. Run EARNINGS SIGNAL for any name with earnings within 30 days.
4. Biweekly STRATEGY REVIEW via StrategyAdvisor to check alpha and phase alignment.
5. First monthly performance report at the end of Month 1.

**Key question for every new trade this phase**: "Is this trade improving portfolio quality or just adding noise?"

**Phase 2 exit criteria**: Alpha positive vs. S&P 500, at least 3 closed trades with logged P&L, portfolio generating positive realized gains.

---

### Phase 3: Harvest and Protect (Weeks 9–12)

**Objective**: Realize profits. Protect the gains built in Phase 2. Do not give back the quarter chasing new ideas.

| Parameter | Limit |
|---|---|
| Max capital deployed | 60% by Week 11, 40% by Week 12 |
| Max open positions | 6 (trimming toward quarter close) |
| Risk posture | DEFENSIVE — tighten all stops |
| Stop tightness | Max 4% from current price (not entry) on all winners |
| New positions | NONE after Week 10 (exceptional conviction only, max 3% size) |

**Priority tasks for this phase**:
1. Trim at Target 1 for all positions that haven't already.
2. Close positions where thesis has weakened or SentimentMonitor flagged ELEVATED/URGENT.
3. Tighten stops to lock in at minimum 30% of each position's unrealized gains.
4. Reduce position count weekly.
5. Final performance report at end of Week 12: portfolio return vs. S&P 500, alpha, win rate, lessons.

**Non-negotiable rule for Phase 3**: Do not open a new position just because cash is available. Cash is protection, not a problem.

---

## Market Regime Playbooks

StrategyAdvisor classifies the regime each week. Mr.B uses the matching playbook:

### Risk-On Trending (VIX < 18, S&P uptrend, yields stable)
- Posture: Full offensive.
- Sectors: Technology, Consumer Discretionary, Industrials, High-beta growth.
- Position sizing: Full Kelly per RiskManager.
- New positions: Approved in all phases within position count limits.

### Risk-On Choppy (VIX 18–25, mixed signals)
- Posture: Selective — quality names only.
- Sectors: Sector leaders, Quality growth, Earnings plays.
- Position sizing: 75% of RiskManager recommended.
- New positions: Only HIGH-signal names (score ≥ 70).

### Risk-Off (VIX > 25, S&P downtrend, spreads widening)
- Posture: Defensive — max 3 positions, move to cash.
- Sectors: Healthcare, Utilities, Consumer Staples.
- Position sizing: 50% of RiskManager recommended.
- New positions: NONE unless explicitly Defensive sector.
- Mandatory: Tighten all stops to 5% from current price immediately.

### Rate-Sensitive (Fed hiking, yields rising sharply)
- Posture: Rotate out of duration.
- Sectors: Value, Energy, Financials — avoid high-multiple growth.
- Position sizing: 75% of RiskManager recommended for value names.
- Avoid: Any position with P/E > 40 or negative free cash flow.

### Stagflation (high inflation + slowing growth + rising yields)
- Posture: Hard commodities and real assets only.
- Sectors: Energy, Materials, Gold proxies.
- Avoid: Consumer Discretionary, high-multiple Technology.
- Cash target: Raise to 30% of NAV minimum.

---

## Sector Rotation Priority Table

Updated weekly by StrategyAdvisor. Mr.B uses this before any new position.

| Sector | Priority | Max Allocation | Current Rationale |
|--------|----------|----------------|-------------------|
| [Fill in at strategy start — updated each week by StrategyAdvisor] | | | |

---

## Signal Priority Stack

When multiple factors conflict, use this priority order:

1. **ResearchAnalyst fundamental thesis** — must be present. A broken thesis overrides everything.
2. **RiskManager verdict** — REJECTED is a hard stop. No trade without APPROVED.
3. **StrategyAdvisor sector alignment** — AVOID sector = no trade, even with HIGH signal.
4. **SignalEngine confidence** — HIGH required for full size; MEDIUM → half size.
5. **SentimentMonitor alert** — URGENT against a position → immediate thesis review.

---

## Performance Review Cadence

| Frequency | When | Owner | Action |
|---|---|---|---|
| Weekly | Every Friday | Mr.B + PortfolioTracker | P&L report, stop trail review, signal refresh |
| Biweekly | Every 2nd Monday | Mr.B + StrategyAdvisor | Strategy alignment check, rotation update |
| Month 1 end | End of Week 4 | Mr.B | Full performance report vs. S&P 500, phase review |
| Month 2 end | End of Week 8 | Mr.B | Full performance report, Phase 2 → Phase 3 transition review |
| Month 3 end | End of Week 12 | Mr.B | Final report: total return, alpha, win rate, lessons learned |

---

## Hard Stops and Override Rules

- **15% drawdown from peak NAV**: Defensive mode activated immediately. No overrides.
- **SentimentMonitor URGENT on an open position**: Mr.B must review the same session. Stop review is mandatory.
- **StrategyAdvisor marks regime as Risk-Off**: Close weakest position within 2 sessions. No new longs.
- **Mr.B overrides RiskManager REJECTED verdict**: Must log via `OVERRIDE LOG [TICKER] [reason]` in TradeLog.md before proceeding.

---

## Dual-Market Capital Rules (Appended)

This framework was originally written for a single US portfolio. It now applies to **two independent sub-portfolios**, US (NASDAQ/NYSE, USD NAV) and IN (NSE, INR NAV). The rules below clarify how the framework's parameters apply across both markets:

- Each sub-portfolio has its own NAV, its own peak NAV, its own drawdown, and its own phase counters.
- The capital-deployment ladder (Phase 1 ≤40%, Phase 2 ≤80%, Phase 3 reducing to 40%) applies **per sub-portfolio** — not summed across the two.
- The position-count caps (Phase 1 ≤4, Phase 2 ≤8, Phase 3 ≤6) apply **per sub-portfolio**.
- The 15% max drawdown trigger is evaluated **per sub-portfolio**. A 15% drawdown in IN does not force defensive mode in US, and vice versa.
- The Five-Layer Decision Gate is identical for both markets; each layer routes through the correct market's context based on the ticker's exchange suffix (`.US` / `.NS`).
- StrategyAdvisor produces a single weekly memo containing **both** market sections side-by-side (`## US Strategy Memo` then `## IN Strategy Memo`).
- Sector Rotation Priority Table below is maintained twice — once with the US (GICS) sector taxonomy, once with the IN (NIFTY-sector) taxonomy.

### Paper-trade compression (1-month run)

For the current 1-month paper-trade run (locked in `Scripts/strategy_meta.json`), the 12-week phases compress as follows. The original 12-week parameters above remain authoritative for live trading.

| Phase | Paper-trade window | Max deployed (per market) | Max positions (per market) |
|---|---|---|---|
| Phase 1 (Recon) | Week 1 | 40% | 4 |
| Phase 2 (Deployment) | Weeks 2–3 | 80% | 8 |
| Phase 3 (Harvest) | Week 4 | reducing to 40% | reducing to 6 |

---

## Amendments Log

> All future amendments to this framework are appended here with a date. The original text above is never modified.

| Date | Amendment | Reason |
|------|-----------|--------|
| 2026-05-14 | Extend framework to dual-market (US NASDAQ + India NSE). Each sub-portfolio operates the framework independently; sector taxonomies, benchmarks, regime indicators, NAV, and drawdown are tracked per market. | User requirement: Mr.B should work on NASDAQ as well as NSE. |
| 2026-05-14 | 1-month paper-trade run started. Starting NAV locked: $10,000 USD for US sub-portfolio, ₹10,00,000 INR for IN sub-portfolio. No top-ups. 12-week phases compressed to 4 weeks per `Dual-Market Capital Rules` section above. | User requested a 1-month paper-trade to evaluate Mr.B before live deployment. |
| 2026-05-16 | IN IT sector (TCS, INFY, HCLTECH, WIPRO, TECHM) formally downgraded to AVOID until sector RSI recovers above 50 across the cohort AND MACD turns bullish on at least 3 of 5 names. Do not evaluate any IN IT name for entry during this period regardless of individual signal score. | W20 data: all five major IN IT names scored NO_SIGNAL LOW; RSIs 26–40; 3-month returns −17% to −28% vs NIFTY −8.3%. Structural bear confirmed — entering any name would require catching a falling knife against clear quantitative contraindication. |
