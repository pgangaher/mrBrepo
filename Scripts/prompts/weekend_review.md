# Session: WEEKEND_REVIEW (Saturday 10:00 IST)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. Unattended scheduled session — scheduler is the authorized client.

Permissions: append to logs; create new dated files in `Logs/Weekly_Reviews/`, `Portfolio/performance/{US,IN}/`, `Strategy/frameworks/`; **MAY append rows** to the Amendments Log of `Strategy/ThreeMonthFramework.md`; **MAY overwrite** `Dashboard/dashboard_data.js`. Never delete. Never overwrite anything else.

## Pre-flight

1. Read `Scripts/strategy_meta.json` for strategy start/end dates and starting NAVs.
2. Compute the current ISO week number and the Monday–Friday date range that just concluded.
3. Read this week's daily P&L lines from `Logs/daily_pnl_US.md` and `Logs/daily_pnl_IN.md`.
4. Read this week's portfolio state snapshots from `Portfolio/state/US/` and `Portfolio/state/IN/`.
5. Read this week's Recommendations logs (`Logs/Recommendations_YYYY-MM-DD.md` for each weekday).
6. Read this week's session summaries from `Logs/sessions/`.

## Routine

### Per-market weekly P&L

1. **`PortfolioTracker WEEKLY P&L REPORT [week_number] [start] [end] US [prices: latest US closes]`** → `Portfolio/performance/US/weekly_review_<YYYY>-W<NN>.md`.
2. **`PortfolioTracker WEEKLY P&L REPORT [week_number] [start] [end] IN [prices: latest IN closes]`** → `Portfolio/performance/IN/weekly_review_<YYYY>-W<NN>.md`.
3. For each report, compute and record: starting NAV (Monday open), ending NAV (Friday close), week P&L absolute and %, benchmark week return (SPY for US, NIFTY 50 for IN), week alpha, trade events list (opens / adds / trims / closes), positions that hit Target 1, positions that hit stop.

### Strategy review

4. **`StrategyAdvisor STRATEGY REVIEW [week_number] BOTH`** — produce a single memo at `Strategy/frameworks/strategy_review_<YYYY>-W<NN>.md` with two blocks (US and IN). For each market, verify:
   - Capital deployed vs. phase target.
   - Position count vs. phase cap.
   - Sector rotation alignment with current regime.
   - Whether the framework's phase needs adjustment.

### Stop-trail review per position

5. For every open position in both markets, review whether to trail the stop. Phase-3 rule: lock in at least 30% of unrealized gain on winners. Phase-2 rule: don't let > 50% of unrealized gain give back. Issue `UPDATE STOP` recommendations as needed and append to `Logs/Recommendations_<today>.md`.

### Lessons learned

6. Write a structured Weekly Review file at `Logs/Weekly_Reviews/week_<NN>_<YYYY-MM-DD>.md` with:
   - Headline P&L per market and combined alpha context.
   - What worked this week (best 1–2 calls per market).
   - What didn't (worst 1–2 calls per market, with one-line reason).
   - Stops hit, targets hit, no-trade calls that were right (validation), no-trade calls that were wrong (cost).
   - Signal-class hit rate this week (Momentum / Earnings / Breakout / Mean Reversion).
   - Sector exposure shifts over the week.
   - Concrete actions for next Monday (which positions to add, trim, watch).

### Framework amendment (only if material)

7. If a learning materially changes how Mr.B should operate next week (e.g. "Mean-reversion signals on Indian midcaps underperformed — downweight for now", "US tech regime has shifted from trending to choppy — rotate to quality"), append a new row to the Amendments Log table at the end of `Strategy/ThreeMonthFramework.md`:
   ```
   | YYYY-MM-DD | <one-line description of the change> | <one-line reason citing this week's data> |
   ```
   Also write the full rationale inside the Weekly Review file (step 6). Do NOT modify the original framework text — only append to the Amendments Log table.

### Dashboard refresh

8. **Build `Dashboard/dashboard_data.js`** (overwrite allowed). Use the latest dated portfolio state files in both markets. NAV history should now include the just-completed week's daily series.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_WEEKEND_REVIEW.md`:

- Week P&L per market.
- Cumulative-to-date return per market.
- Cumulative alpha per market.
- Top win and worst loss this week.
- Stops trailed.
- Framework amendments appended (count).
- Next-Monday action list (3–6 bullets).

End of session.
