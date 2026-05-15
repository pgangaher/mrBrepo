# Session: IN_OPEN (NSE market open)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. This is an unattended scheduled session — the scheduler is acting as the authorized client.

Permissions: create new dated files in any sub-agent's artifact folder; append to `Logs/Recommendations_<today>.md`, `Logs/TradeLog.md`, `Logs/daily_pnl_IN.md`, and `Logs/scheduler.log` adjacent files; append to the Amendments Log section of `Strategy/ThreeMonthFramework.md`; overwrite `Dashboard/dashboard_data.js` (only this file). Never delete. Never overwrite anything else — if a same-date file exists, use a `-v2` suffix.

## Pre-flight

1. Read `Scripts/strategy_meta.json` to confirm the locked INR starting NAV (₹10,00,000) and strategy end date. If today is past `strategy_end`, do not open new positions; only run a maintenance pass (stop reviews, P&L update).
2. Read the most recent `Portfolio/state/IN/portfolio_state_*.md` if any exists.
3. Read today's `Logs/Recommendations_<today>.md` if it exists (to know what's already been said today).
4. Confirm NSE is open today (the scheduler already checked the holiday calendar).
5. **Read the prefetch snapshot** for this session: `Scripts/cache/snapshot_IN_<today>_<HHMM>.json` (newest matching file). This is the authoritative source for prices, indicators, and signal scores. If the file is missing or `MRB_PREFETCH_FAILED=1` is set, fall back per `_preamble.md`.

## Routine

Walk the five-layer flow for the IN sub-portfolio:

1. **StrategyAdvisor — `MACRO REGIME CHECK IN`**: classify the India regime using India VIX, NIFTY 50 trend, USD/INR, India 10Y G-Sec, FII/DII flows, RBI stance. Save a strategy memo (single-market IN block) to `Strategy/frameworks/strategy_memo_<today>.md` (or `..._<today>-v2.md` if one already exists from a US session today).
2. **SentimentMonitor — `WATCHLIST PULSE IN`**: lightweight sentiment sweep across the IN watchlist (and all open IN positions). Save to `Sentiment/logs/watchlist_pulse_IN_<today>.md`. Escalate any URGENT items immediately to step 5.
3. **SignalEngine — `WATCHLIST SCORE IN`**: the snapshot already contains a deterministic composite score, signal class, and conviction tier for every IN watchlist + open-position ticker. Compile a `Signals/outputs/watchlist_score_IN_<today>.md` summary that tabulates `composite_score`, `signal_class`, and `conviction` from the snapshot (do NOT recompute or override these numbers — they are the locked formula's output). Rank candidates by composite score. Cite the snapshot filename.
4. **Candidate evaluation**: for each HIGH-confidence (snapshot `conviction == "HIGH"`, score ≥ 70) and qualifying MEDIUM candidate (40–69 with a clear catalyst), run the full five-layer gate:
   - `ResearchAnalyst RESEARCH [TICKER.NS]` — full report saved to `Research/reports/<TICKER.NS>_<today>.md` if not already present this week.
   - `SignalEngine` single-stock signal report saved to `Signals/outputs/<TICKER.NS>_signal_<today>.md` — quote the snapshot's `composite_score`, `subscores`, `indicators`, and `signal_class` verbatim; add your interpretation but do not change the numbers.
   - StrategyAdvisor sector alignment check from step 1's memo.
   - `SentimentMonitor SENTIMENT SCAN [TICKER.NS]` if not covered by the pulse.
   - `RiskManager VALIDATE TRADE` — saved to `Risk/rules/clearance_<TICKER.NS>_<today>.md`. Position size is computed against the INR sub-portfolio NAV; the suggested stop is the snapshot's `stop_atr` (override only with a documented reason in the clearance file).
5. **Execute paper fills** for every APPROVED or APPROVED-WITH-MODIFICATION verdict from step 4. Use the snapshot's `quote.open` (NSE open price) for the fill. Record in `Logs/TradeLog.md` as a new entry with the snapshot filename as the price source.
6. **Stops & sentiment overrides**: for any URGENT alert on an open position from step 2, run a thesis review and trigger a stop adjustment via `RiskManager STOP LOSS REVIEW`.
7. **Capture verdicts**: append a Recommendation block to `Logs/Recommendations_<today>.md` for every candidate evaluated in step 4 — including those that produced NO-TRADE or REJECTED-by-Risk verdicts. Use the template from `MrB.md`.
8. **Update PortfolioTracker** with any opens via `PAPER FILL` task (records the price source).

## Wrap-up

Write a session summary to `Logs/sessions/<today>_IN_OPEN.md` covering:

- Regime classification chosen and key indicators.
- Watchlist pulse highlights (URGENT/ELEVATED items).
- Top 3 signal scores.
- Number of paper fills executed, with tickers.
- Any rejections / no-trade calls and why.
- Open IN positions count and total INR exposure at end of session.

Do NOT update `Dashboard/dashboard_data.js` in this session — only `IN_CLOSE` and `US_CLOSE` refresh the dashboard.

End of session.
