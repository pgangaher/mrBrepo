# Session: IN_MIDDAY (NSE mid-session)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. Unattended scheduled session — scheduler is the authorized client.

Permissions: same as IN_OPEN (append to logs / Recommendations / TradeLog; create new dated files; do not delete; do not overwrite except `Dashboard/dashboard_data.js`, which this session does NOT touch).

## Pre-flight

1. Read the most recent IN portfolio state and today's Recommendations log.
2. Read this morning's `Sentiment/logs/watchlist_pulse_IN_<today>.md` for context.

## Routine

1. **SentimentMonitor — `NEWS ALERT CHECK [TICKER.NS]`** for every open IN position. For each, log a short sentiment note into `Sentiment/logs/sentiment_<TICKER.NS>_<today>.md` (or `..._<today>-v2.md`).
2. For any URGENT alert (FDA-like equivalents: SEBI action, results miss disclosed mid-session, promoter pledge increase, large block-deal exit, RBI banking-sector action), immediately:
   - Run a thesis re-review reading the existing research report.
   - Run `RiskManager STOP LOSS REVIEW [TICKER.NS]` — if the recommendation is to tighten the stop, execute a paper `UPDATE STOP` in PortfolioTracker and log the verdict in `Logs/Recommendations_<today>.md`.
3. **`RiskManager STOP LOSS REVIEW`** for every open IN position regardless of sentiment level (routine trail check). Save the bundle to `Risk/rules/stop_review_IN_<today>.md`.
4. **No new openings** in this session unless a HIGH-confidence opportunity from the morning Watchlist Score has reached its entry trigger zone — and only if RiskManager re-validates with current price.
5. Append every verdict to `Logs/Recommendations_<today>.md`.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_IN_MIDDAY.md` covering:

- URGENT/ELEVATED alerts surfaced.
- Stops adjusted (which positions, old → new).
- Any mid-session paper fills (rare).
- Open IN positions and unrealized P&L snapshot at session time.

End of session.
