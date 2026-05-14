# Mr.B Scheduler

A long-running Python supervisor that fires Mr.B at every NSE / NASDAQ session
boundary, every Saturday for a weekly review, and once on day 30 of the
paper-trade run for a final report.

No third-party Python dependencies. Requires Python 3.9+ and the `claude` CLI
on `PATH`.

## What it does

| Session | Market | When (IST) | Notes |
|---|---|---|---|
| `IN_OPEN`   | NSE    | Mon–Fri 09:15 | NSE regular open |
| `IN_MIDDAY` | NSE    | Mon–Fri 12:30 | Mid-session check |
| `IN_CLOSE`  | NSE    | Mon–Fri 15:30 | EoD P&L, dashboard refresh |
| `US_OPEN`   | NASDAQ | Mon–Fri 19:00 / 20:00 | 09:30 ET, DST-aware |
| `US_MIDDAY` | NASDAQ | Mon–Fri 22:00 / 23:00 | 12:30 ET, DST-aware |
| `US_CLOSE`  | NASDAQ | Mon–Fri 01:30 / 02:30 next day | 16:00 ET, DST-aware |
| `WEEKEND_REVIEW` | both | Saturday 10:00 | Weekly P&L + framework amendments |
| `MONTH_END` | both | day 30 11:00 | One-shot final paper-trade report |

Trading-day holidays (NSE, NASDAQ) and NYSE half-days are honored via
`holidays.json`.

## Files

```
Scripts/
├── scheduler.py            # the supervisor
├── prompts/                # 8 session prompts (in_open.md, us_close.md, …)
├── holidays.json           # 2026 NSE + NASDAQ calendar
├── strategy_meta.json      # written on first launch — locks start, end, NAVs
└── README.md               # this file
```

## How to run

```bash
# One-off: see the next 8 firings without invoking Mr.B
python3 Scripts/scheduler.py --next

# Dry run: log the next firing but do not invoke claude
python3 Scripts/scheduler.py --dry-run

# Manually fire one session (useful for testing or backfill)
python3 Scripts/scheduler.py --force IN_OPEN

# Run forever (foreground)
python3 Scripts/scheduler.py
```

For unattended operation, install the launchd plist:

```bash
# 1. Edit Scripts/com.parikshit.mrb-scheduler.plist if your python3 path differs.
which python3
# 2. Copy it into LaunchAgents and load.
cp Scripts/com.parikshit.mrb-scheduler.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist
launchctl list | grep mrb-scheduler
```

To stop:

```bash
launchctl unload ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist
```

## Paper-trade contract

On first launch, `strategy_meta.json` is written with:

- `strategy_start`: today (IST)
- `strategy_end`: today + 30 days
- `markets.US.starting_nav`: 10000 USD
- `markets.IN.starting_nav`: 1000000 INR

These are **locked**. Editing them mid-run will corrupt the audit trail.

After `strategy_end`, only `MONTH_END` and `WEEKEND_REVIEW` continue to fire.

## Where things go

- `Logs/scheduler.log` — supervisor lifecycle, one line per event.
- `Logs/sessions/YYYY-MM-DD_HHMM_SESSION_ID.log` — captured stdout/stderr from each `claude -p` invocation.
- `Logs/sessions/<date>_<SESSION>.md` — session summary written by Mr.B during the session.
- `Logs/Recommendations_YYYY-MM-DD.md` — every verdict Mr.B issues, both markets.
- `Logs/daily_pnl_US.md`, `Logs/daily_pnl_IN.md` — append-only daily P&L logs.
- `Logs/Weekly_Reviews/week_NN_YYYY-MM-DD.md` — weekend review output.
- `Logs/Month_End_Report_YYYY-MM-DD.md` — final paper-trade report.
- `Portfolio/state/{US,IN}/portfolio_state_YYYY-MM-DD.md` — snapshots.
- `Dashboard/dashboard_data.js` — refreshed at every CLOSE / weekend / month-end (the one allowed overwrite).

## Troubleshooting

- **`claude: command not found`** in `Logs/sessions/*.log` — install Claude Code and verify `which claude` resolves. If using launchd, the plist needs `PATH` set explicitly (it does not inherit your shell `PATH`).
- **Session log is empty** — Mr.B may have errored before writing anything. Check `Logs/scheduler.log` for the exit code; non-zero exits are flagged there.
- **Wrong US session time** — DST flipped. The scheduler converts ET→IST per day, so this should be automatic. If it isn't, double-check that the host's TZ database is up to date (`/usr/share/zoneinfo/America/New_York`).
- **Holiday skipped that shouldn't have been** — edit `holidays.json` and restart the supervisor.
