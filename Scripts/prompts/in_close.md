# Session: IN_CLOSE (NSE end of day)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. Unattended scheduled session — scheduler is the authorized client.

Permissions: append to logs; create new dated files; **MAY overwrite `Dashboard/dashboard_data.js`** as the final step. Never delete. Never overwrite anything else.

## Pre-flight

1. Read `Scripts/strategy_meta.json` for the locked INR NAV (₹10,00,000) and strategy end date.
2. Read the most recent IN portfolio state.
3. Read today's Recommendations log and all session summaries from earlier today.
4. **Read the prefetch snapshot** for this session: `Scripts/cache/snapshot_IN_<today>_<HHMM>.json`. The `quote.close` field is the authoritative NSE close (yfinance EOD bar). Fall back to web search only if the snapshot is missing or `MRB_PREFETCH_FAILED=1` is set.

## Routine

1. **Use snapshot `quote.close` prices** for every open IN position. This is yfinance's official EOD bar — do not web-search NSE separately when the snapshot is present.
2. **`PortfolioTracker PORTFOLIO SNAPSHOT <today> IN [prices: ...]`** — write `Portfolio/state/IN/portfolio_state_<today>.md` with current NAV, peak NAV, drawdown, sector exposure (IN taxonomy), open positions table with unrealized P&L, and realized P&L log.
3. **`PortfolioTracker BENCHMARK UPDATE IN [NIFTY50 close] <today>`** — capture NIFTY 50 level for alpha computation.
4. **`RiskManager PORTFOLIO RISK CHECK IN`** and **`DRAWDOWN CHECK IN`** — flag any rule violations. If the IN drawdown ≥ 15%, write `DEFENSIVE MODE ACTIVE IN` to today's Recommendations log and stop new IN long verdicts going forward.
5. **Stop hit reconciliation**: if any open IN position closed below its stop today, execute a paper `CLOSE POSITION` at the stop price (or the day's low if it gapped through the stop, whichever is worse) and log a TradeLog entry with `STOP_HIT` reason. Append a TRIM/CLOSE recommendation to the day's log.
6. **Target hit reconciliation**: if any open IN position closed above Target 1, recommend trimming half the position (Phase 1/2 rule) and execute the paper trim. Log it.
7. **Append today's IN P&L line** to `Logs/daily_pnl_IN.md` (append-only):
   ```
   YYYY-MM-DD | NAV: ₹X,XX,XXX | Day P&L: ₹±X (±X.XX%) | Cum return: ±X.XX% | NIFTY return: ±X.XX% | Alpha: ±X.XX% | Open positions: N
   ```
8. **Finalize today's Recommendations log** by appending a "Day close summary" block: number of recommendations, splits by Action type, total INR P&L on the day.
9. **Build `Dashboard/dashboard_data.js`** (this is the one allowed overwrite). Read:
   - `Portfolio/state/US/portfolio_state_<latest>.md` and `Portfolio/state/IN/portfolio_state_<latest>.md`
   - `Logs/daily_pnl_US.md` and `Logs/daily_pnl_IN.md` for the NAV history
   - `Logs/Recommendations_<today>.md` (and recent days') for the recommendations feed
   
   Write `Dashboard/dashboard_data.js` with the following structure:
   ```js
   window.DATA = {
     updated_at: "<ISO timestamp with IST offset>",
     strategy_start: "<from strategy_meta.json>",
     strategy_end: "<from strategy_meta.json>",
     markets: {
       US: { label, currency: "USD", currency_symbol: "$", starting_nav, current_nav, todays_pnl, todays_pnl_pct, total_return_pct, peak_nav, drawdown_pct, benchmark_return_pct, alpha_pct, nav_history: [...], open_positions: [...] },
       IN: { label, currency: "INR", currency_symbol: "₹", starting_nav, current_nav, todays_pnl, todays_pnl_pct, total_return_pct, peak_nav, drawdown_pct, benchmark_return_pct, alpha_pct, nav_history: [...], open_positions: [...] }
     },
     recent_recommendations: [ {timestamp, ticker, market, verdict, action, conviction, reasoning_one_line}, … up to 10 newest ]
   };
   ```
   If the US side has not had a CLOSE session yet today, keep yesterday's US figures in `markets.US` (read them from `Portfolio/state/US/portfolio_state_<latest>.md`); do NOT zero them out.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_IN_CLOSE.md` covering:

- IN sub-portfolio NAV today vs. yesterday.
- Day P&L in INR and percentage.
- Stops triggered (if any).
- Targets hit (if any).
- Drawdown status (current vs. 15% threshold).
- Confirmation that `Dashboard/dashboard_data.js` was refreshed.

End of session.
