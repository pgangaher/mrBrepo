# Session: US_MIDDAY (NASDAQ mid-session)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. Unattended scheduled session — scheduler is the authorized client.

Permissions: append/create as needed; never delete; never overwrite (the dashboard is not touched here).

## Pre-flight

1. Read the most recent US portfolio state and today's Recommendations log.
2. Read this evening's `Sentiment/logs/watchlist_pulse_US_<today>.md` for context.
3. **Read the prefetch snapshot**: `Scripts/cache/snapshot_US_<today>_<HHMM>.json`. Use `quote.last_price` for any mid-session decision. Fall back per `_preamble.md` if missing.

## Routine

1. **SentimentMonitor — `NEWS ALERT CHECK [TICKER.US]`** for every open US position. Log each into `Sentiment/logs/sentiment_<TICKER.US>_<today>.md` (or `..._<today>-v2.md` if one exists).
2. For any URGENT alert (earnings pre-announcement, FDA action, SEC investigation, CEO departure, M&A offer):
   - Thesis re-review.
   - `RiskManager STOP LOSS REVIEW [TICKER.US]` — execute a paper `UPDATE STOP` if tightened.
   - Append the verdict to `Logs/Recommendations_<today>.md`.
3. **`RiskManager STOP LOSS REVIEW`** for every open US position (routine trail check). Save to `Risk/rules/stop_review_US_<today>.md`.
4. **No new openings** unless a HIGH-confidence morning candidate has reached its trigger price (compare snapshot `quote.last_price` to the morning's trigger) and RiskManager re-validates.
5. Append every verdict to `Logs/Recommendations_<today>.md`.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_US_MIDDAY.md`:

- URGENT/ELEVATED alerts surfaced.
- Stops adjusted.
- Any mid-session paper fills.
- Open US positions and unrealized USD P&L at session time.

End of session.
