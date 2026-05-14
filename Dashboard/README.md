# Mr.B Dashboard

A single-file React dashboard that visualizes the paper-trade book for both
markets side-by-side: NAV, today's P&L, NAV vs benchmark over the run, open
positions, and a feed of recent Mr.B recommendations.

No build step. No `npm install`. Dependencies load from public CDNs at page
load.

## Open it

```bash
open /Users/parikshitgangaher/Codes/workspace-broker/Dashboard/index.html
```

If your browser blocks the local script-load (rare on macOS but possible), run
a local static server:

```bash
python3 -m http.server 8000 --directory /Users/parikshitgangaher/Codes/workspace-broker/Dashboard
open http://localhost:8000
```

## How it updates

The dashboard renders whatever is in `dashboard_data.js`. That file is rebuilt
by Mr.B at the end of every:

- `IN_CLOSE` session (~15:30 IST)
- `US_CLOSE` session (~01:30 / 02:30 IST the next morning)
- `WEEKEND_REVIEW` (Saturday 10:00 IST)
- `MONTH_END` (one-shot on day 30)

So the dashboard is current as of the most recent close in either market.
Refresh the browser page after a close to pick up the latest data.

## Data file shape

```js
window.DATA = {
  updated_at: "2026-05-14T15:30:00+05:30",
  strategy_start: "2026-05-14",
  strategy_end: "2026-06-13",
  markets: {
    US: { label, currency: "USD", currency_symbol: "$", starting_nav, current_nav,
          todays_pnl, todays_pnl_pct, total_return_pct, peak_nav, drawdown_pct,
          benchmark_return_pct, alpha_pct,
          nav_history: [ { date, nav, benchmark } ],
          open_positions: [ { ticker, sector, shares, entry, current,
                              unrealized_pnl, unrealized_pct, stop, target1, conviction } ] },
    IN: { same shape, currency "INR" }
  },
  recent_recommendations: [
    { timestamp, ticker, market: "US"|"IN", verdict, action, conviction, reasoning_one_line }
  ]
};
```

## Force a refresh manually

If you want to see fresh numbers without waiting for the next scheduled close:

```bash
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --force IN_CLOSE
# or
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --force US_CLOSE
```

Either invocation will rebuild `dashboard_data.js` once Mr.B finishes the
session.

## Currency display

USD always renders as `$` with Western-style commas (`$10,000.00`).
INR always renders as `₹` with the Indian numbering system (`₹10,00,000`).
Values are never converted across currencies.
