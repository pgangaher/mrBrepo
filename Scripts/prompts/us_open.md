# Session: US_OPEN (NASDAQ market open)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. Unattended scheduled session — scheduler is the authorized client.

Permissions: same as the IN_OPEN session (append/create as needed; do not delete; do not overwrite anything except `Dashboard/dashboard_data.js`, which this session does NOT touch — only the CLOSE sessions refresh the dashboard).

## Pre-flight

1. Read `Scripts/strategy_meta.json` for the locked USD NAV ($10,000) and strategy end date. If past `strategy_end`, run maintenance only.
2. Read the most recent `Portfolio/state/US/portfolio_state_*.md`.
3. Read today's Recommendations log (if present from any IN session earlier today).
4. **Read the prefetch snapshot**: `Scripts/cache/snapshot_US_<today>_<HHMM>.json` (newest matching file). Authoritative source for prices, indicators, and signal scores. Fall back per `_preamble.md` if missing or `MRB_PREFETCH_FAILED=1`.

## Routine

Walk the five-layer flow for the US sub-portfolio:

1. **StrategyAdvisor — `MACRO REGIME CHECK US`**: classify the US regime using VIX, S&P 500 trend, 10Y Treasury, DXY, credit spreads, Fed posture. Append a US block to today's strategy memo at `Strategy/frameworks/strategy_memo_<today>.md` (or write a new file with `-v2` suffix if an IN-only memo already exists).
2. **SentimentMonitor — `WATCHLIST PULSE US`**: lightweight sentiment sweep across the US watchlist and all open US positions. Save to `Sentiment/logs/watchlist_pulse_US_<today>.md`.
3. **SignalEngine — `WATCHLIST SCORE US`**: the snapshot already contains a deterministic composite score, signal class, and conviction for every US watchlist + open-position ticker. Compile `Signals/outputs/watchlist_score_US_<today>.md` from the snapshot's `composite_score`, `signal_class`, `conviction` columns — do NOT recompute or override these. Cite the snapshot filename.
4. **Candidate evaluation**: for each HIGH-confidence (`conviction == "HIGH"`, score ≥ 70) and qualifying MEDIUM candidate, run the full five-layer gate, saving:
   - `Research/reports/<TICKER.US>_<today>.md`
   - `Signals/outputs/<TICKER.US>_signal_<today>.md` — quote the snapshot's numbers verbatim, then layer your interpretation
   - `Sentiment/logs/sentiment_<TICKER.US>_<today>.md`
   - `Risk/rules/clearance_<TICKER.US>_<today>.md` — use snapshot's `stop_atr` as the default stop
   Position size is computed against the USD sub-portfolio NAV.
5. **Execute paper fills** for every APPROVED / APPROVED-WITH-MODIFICATION verdict using the snapshot's `quote.open` (NASDAQ open price). Record each in `Logs/TradeLog.md` with the snapshot filename as the price source.
6. **Stops & sentiment overrides** for open positions on URGENT alerts.
7. **Capture verdicts**: append a Recommendation block for each candidate evaluated — trade and no-trade — to `Logs/Recommendations_<today>.md`.
8. **Update PortfolioTracker** with any opens via `PAPER FILL`.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_US_OPEN.md` covering:

- Regime classification + key US macro indicators.
- Watchlist pulse highlights.
- Top 3 signal scores.
- Paper fills executed.
- Rejections / no-trade calls and reasons.
- Open US positions count and USD exposure at session end.

Do NOT update `Dashboard/dashboard_data.js` in this session.

End of session.
