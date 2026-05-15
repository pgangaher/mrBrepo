# Session: US_CLOSE (NASDAQ end of day)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. Unattended scheduled session — scheduler is the authorized client.

Permissions: append to logs; create new dated files; **MAY overwrite `Dashboard/dashboard_data.js`** as the final step. Never delete. Never overwrite anything else.

Note: this session typically fires after midnight IST. The session's "today" is the US trading date (the date of the NASDAQ close just completed), not the IST calendar date — use the US date in filenames where the session is about the US market specifically.

## Pre-flight

1. Read `Scripts/strategy_meta.json`.
2. Read the most recent US portfolio state.
3. Read today's Recommendations log (which covers IN sessions from earlier in the same IST date) — if you write new entries here, they remain under that same Recommendations file unless a new IST date has rolled over (in which case start a new file for the new date).
4. **Read the prefetch snapshot**: `Scripts/cache/snapshot_US_<today>_<HHMM>.json`. The `quote.close` field is the authoritative NASDAQ close (yfinance EOD bar). Fall back per `_preamble.md` if missing or `MRB_PREFETCH_FAILED=1`.

## Routine

1. **Use snapshot `quote.close` prices** for every open US position — do not web-search Yahoo Finance separately when the snapshot is present.
2. **`PortfolioTracker PORTFOLIO SNAPSHOT <us_trading_date> US [prices: ...]`** — write `Portfolio/state/US/portfolio_state_<us_trading_date>.md` with USD NAV, peak NAV, drawdown, GICS sector exposure, open positions, realized P&L log.
3. **`PortfolioTracker BENCHMARK UPDATE US [SPY close] <us_trading_date>`** — capture SPY for alpha.
4. **`RiskManager PORTFOLIO RISK CHECK US`** and **`DRAWDOWN CHECK US`**. If US drawdown ≥ 15%, write `DEFENSIVE MODE ACTIVE US` to the active Recommendations log and stop new US long verdicts.
5. **Stop hit reconciliation**: paper-close any US position that breached its stop today. Log as `STOP_HIT` in TradeLog.
6. **Target hit reconciliation**: trim positions that closed above Target 1.
7. **Append today's US P&L line** to `Logs/daily_pnl_US.md`:
   ```
   YYYY-MM-DD | NAV: $X,XXX.XX | Day P&L: $±X.XX (±X.XX%) | Cum return: ±X.XX% | SPY return: ±X.XX% | Alpha: ±X.XX% | Open positions: N
   ```
8. **Finalize the active Recommendations log** with a "US day close summary" block.
9. **Build `Dashboard/dashboard_data.js`** (overwrite allowed). Refresh both US and IN sections — for the IN side, read the latest `Portfolio/state/IN/...` file (do not invent figures). Same schema as documented in `in_close.md`.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_US_CLOSE.md`:

- US sub-portfolio NAV today vs. yesterday.
- Day P&L in USD and percentage.
- Stops / targets triggered.
- Drawdown status vs 15% threshold.
- Confirmation that `Dashboard/dashboard_data.js` was refreshed.

End of session.
