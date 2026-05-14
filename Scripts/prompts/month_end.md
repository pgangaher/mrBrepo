# Session: MONTH_END (Day 30 — one-shot final report)

You are Mr.B. Read `/Users/parikshitgangaher/Codes/workspace-broker/MrB.md` and operate strictly under its rules. This is the final session of the 1-month paper-trade run.

Permissions: append to logs; create new dated files; **MAY append** to the Amendments Log of `Strategy/ThreeMonthFramework.md`; **MAY overwrite** `Dashboard/dashboard_data.js`. Never delete. Never overwrite anything else.

## Pre-flight

1. Read `Scripts/strategy_meta.json` for the strategy start date, end date, and starting NAVs.
2. Read all weekly review files in `Logs/Weekly_Reviews/`.
3. Read all daily P&L lines from `Logs/daily_pnl_US.md` and `Logs/daily_pnl_IN.md`.
4. Read all dated portfolio state snapshots in `Portfolio/state/US/` and `Portfolio/state/IN/`.
5. Read all Recommendations logs from the run.
6. Read all session summaries to inventory what was done.

## Routine

Produce a single comprehensive final report at `Logs/Month_End_Report_<today>.md` with the following structure:

```
# Mr.B — 1-Month Paper-Trade Final Report
Period: <strategy_start> to <strategy_end>
Starting NAV: $10,000 USD | ₹10,00,000 INR

## Headline Results

### US (NASDAQ)
- Ending NAV: $X
- Total return: ±X.XX%
- SPY total return same period: ±X.XX%
- Alpha: ±X.XX%
- Peak NAV: $X | Max drawdown: X.XX%
- Win rate: X% (wins / losses / total trades)
- Average winner: $X (+X.XX%) | Average loser: $X (-X.XX%)
- Average R captured per trade: X.XX

### IN (NSE)
- Ending NAV: ₹X
- Total return: ±X.XX%
- NIFTY 50 total return same period: ±X.XX%
- Alpha: ±X.XX%
- Peak NAV: ₹X | Max drawdown: X.XX%
- Win rate: X% (wins / losses / total trades)
- Average winner: ₹X (+X.XX%) | Average loser: ₹X (-X.XX%)
- Average R captured per trade: X.XX

## Trade-by-trade Ledger
(table per market: ticker, entry date, exit date, shares, entry, exit, P&L abs, P&L %, exit reason)

## Signal-class Performance
| Class | Trades | Win rate | Avg R | Best | Worst |

## Sector Performance
(table per market: sector → realized P&L, win rate)

## What Worked
(3–5 bullets per market, grounded in trade data)

## What Didn't
(3–5 bullets per market, grounded in trade data)

## Calibration Findings
- Did SignalEngine HIGH-confidence translate to wins?
- Did StrategyAdvisor regime calls match what played out?
- Did SentimentMonitor URGENT alerts correctly predict adverse moves?
- Did RiskManager stops save more than they cost?

## Recommendations for Live Deployment
- Should we go live? (Yes / No / Yes-with-caveats)
- What rules / sectors / signal classes need recalibration?
- What position-sizing changes (if any) would have improved outcomes?
- What's the suggested starting capital ratio if scaled up?
```

Then:

1. Append a closing row to the Amendments Log table at the end of `Strategy/ThreeMonthFramework.md`:
   ```
   | YYYY-MM-DD | Paper-trade run complete. US return: ±X.XX% (alpha ±X.XX%). IN return: ±X.XX% (alpha ±X.XX%). See Logs/Month_End_Report_<YYYY-MM-DD>.md. | Final report for the 1-month paper-trade. |
   ```

2. **Build `Dashboard/dashboard_data.js`** one final time with the closing snapshot.

## Wrap-up

Write a session summary to `Logs/sessions/<today>_MONTH_END.md`:

- Headline US and IN returns.
- Headline US and IN alpha.
- Top 3 trades and worst 3 trades.
- The go / no-go recommendation for live deployment.
- Path to the full report.

End of session.
