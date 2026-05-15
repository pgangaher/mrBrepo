# Mr.B — Operating Guide

A single source of truth for what Mr.B is, how to start it, how it works day-to-day, and where to look for what.

This document covers the 1-month paper-trade run on NASDAQ + NSE with starting NAV of **$10,000 USD** and **₹10,00,000 INR**. The run is locked the first time the scheduler launches.

---

## Table of Contents

1. [Quick start](#1-quick-start)
2. [What Mr.B is](#2-what-mrb-is)
3. [How Mr.B decides — the five-layer gate](#3-how-mrb-decides--the-five-layer-gate)
4. [The six sub-agents](#4-the-six-sub-agents)
5. [The scheduler and the 8 sessions](#5-the-scheduler-and-the-8-sessions)
6. [Paper-trade rules](#6-paper-trade-rules)
7. [File layout — where everything is written](#7-file-layout--where-everything-is-written)
8. [The dashboard](#8-the-dashboard)
9. [Your daily workflow](#9-your-daily-workflow)
10. [Manual control](#10-manual-control)
11. [Stopping, pausing, resetting](#11-stopping-pausing-resetting)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. Quick start

Three commands and you're running.

```bash
# 1. Verify the schedule looks right
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --next

# 2. Install the launchd agent (auto-starts on login, respawns if it crashes)
cp /Users/parikshitgangaher/Codes/workspace-broker/Scripts/com.parikshit.mrb-scheduler.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist

# 3. Confirm it's alive
launchctl list | grep mrb-scheduler
tail -f /Users/parikshitgangaher/Codes/workspace-broker/Logs/scheduler.log
```

To view P&L any time:

```bash
open /Users/parikshitgangaher/Codes/workspace-broker/Dashboard/index.html
```

The dashboard shows "No data yet" until the first market close fires. Your first data point arrives at the next `IN_CLOSE` (15:30 IST) or `US_CLOSE` (~01:30–02:30 IST).

---

## 2. What Mr.B is

Mr.B is a file-based broker agent. It runs on top of Claude Code (`claude -p`) and stores everything it knows and does inside `/Users/parikshitgangaher/Codes/workspace-broker/`. There is no database, no broker API, no real money — it is a paper account whose state lives entirely in markdown and JSON files.

Before each session fires, the scheduler runs a Python prefetch step (`Scripts/prefetch.py`) that pulls market data via yfinance, computes deterministic technical indicators, and scores signals using the locked rubric in `Signals/SignalEngine.md`. The result lands in `Scripts/cache/snapshot_{MARKET}_{DATE}_{HHMM}.json`. The Claude session reads that snapshot as its authoritative source for prices, indicators, and signal scores — it does NOT web-search Yahoo Finance / NSE for prices when the snapshot is present. This makes signal scoring reproducible across sessions and removes the fragility of LLM-parsed web pages.

Two markets, kept structurally separate at every layer:

| Market | Exchanges | Currency | Benchmark | Vol gauge |
|---|---|---|---|---|
| **US** | NASDAQ, NYSE | USD ($) | S&P 500 / SPY | VIX |
| **IN** | NSE | INR (₹) | NIFTY 50 (with NIFTY 500 for breadth, Bank Nifty for financials) | India VIX |

NAV is never converted across currencies. A 15% drawdown in INR does not affect USD deployment, and vice versa.

Every ticker carries an exchange suffix everywhere:
- `.US` — e.g. `NVDA.US`, `AAPL.US`
- `.NS` — e.g. `RELIANCE.NS`, `TCS.NS`, `HDFCBANK.NS`

The root instruction file is **`MrB.md`** — every session reads it first.

---

## 3. How Mr.B decides — the five-layer gate

Every trade recommendation passes through five layers in sequence. If any layer raises a hard block, the trade does not proceed.

```
Client request
      |
      v
   Mr.B
      |
      ├─ [Layer 1] ResearchAnalyst:    RESEARCH [TICKER]
      │      ↓ Fundamental thesis, financials, competitive position, risks
      │
      ├─ [Layer 2] SignalEngine:       MOMENTUM / EARNINGS / BREAKOUT / etc.
      │      ↓ Quant signal class + score 0–100 + confidence (HIGH/MED/LOW)
      │
      ├─ [Layer 3] SentimentMonitor:   SENTIMENT SCAN [TICKER]
      │      ↓ Alert level (URGENT / ELEVATED / NEUTRAL / POSITIVE)
      │
      ├─ [Layer 4] StrategyAdvisor:    sector alignment check
      │      ↓ ALIGNED / MISALIGNED with current regime + rotation
      │
      ├─ [Layer 5] RiskManager:        VALIDATE TRADE [TICKER] [size] [stop]
      │      ↓ APPROVED / APPROVED WITH MODIFICATION / REJECTED
      │
      ├─ Mr.B synthesizes all five → final verdict
      │
      └─ Recommendation logged + (if proceeding) paper fill executed
```

Hard blocks that stop a trade regardless of other layers:

- ResearchAnalyst: thesis broken or insufficient data
- SignalEngine: `NO_SIGNAL` class
- StrategyAdvisor: sector marked AVOID
- SentimentMonitor: URGENT alert against the position
- RiskManager: REJECTED (override requires an explicit `OVERRIDE LOG` entry in TradeLog.md)

**Every verdict** — BUY, ADD, HOLD, TRIM, CLOSE, NO-TRADE, WATCH — is appended to `Logs/Recommendations_<date>.md` with full reasoning, even when no trade was taken.

---

## 4. The six sub-agents

Mr.B never talks to a sub-agent directly in chat. Each is a markdown spec that defines a role; Mr.B references it during a session and writes outputs to that sub-agent's folder.

| Agent | Spec file | Markets | Writes to | What it does |
|---|---|---|---|---|
| ResearchAnalyst | `Research/ResearchAnalyst.md` | US + IN | `Research/reports/` | Fundamentals, technicals, news, competitive landscape; India adds promoter holding/pledge, Ind-AS notes |
| StrategyAdvisor | `Strategy/StrategyAdvisor.md` | US + IN | `Strategy/frameworks/` | Macro regime classification + sector rotation directives (US: VIX/DXY/Fed/10Y; IN: India VIX/USD-INR/RBI/10Y G-Sec/FII flows) |
| SignalEngine | `Signals/SignalEngine.md` | US + IN | `Signals/outputs/` | Momentum / earnings catalyst / breakout / mean reversion / sector relative strength scoring (0–100) |
| RiskManager | `Risk/RiskManager.md` | US + IN | `Risk/rules/` | Hard pre-trade gate: position sizing, stops, R:R, sector concentration, drawdown, beta, cash floor — applied **per sub-portfolio** |
| PortfolioTracker | `Portfolio/PortfolioTracker.md` | US + IN | `Portfolio/state/{US,IN}/`, `Portfolio/performance/{US,IN}/` | Two independent NAV books, sector exposures, alpha vs SPY (US) / NIFTY 50 (IN); FIFO cost basis |
| SentimentMonitor | `Sentiment/SentimentMonitor.md` | US + IN | `Sentiment/logs/` | News, analyst activity, unusual activity, earnings intel; India adds SEBI/BSE/NSE filings, FII/DII flows, CRISIL/ICRA ratings |

Routing is automatic: a ticker's `.US` / `.NS` suffix tells each sub-agent which benchmark, sector taxonomy, news sources, and sub-portfolio to use.

The 3-month framework lives in `Strategy/ThreeMonthFramework.md`. The original 12-week plan is unchanged; the 1-month paper-trade compression and dual-market rules are appended.

---

## 5. The scheduler and the 8 sessions

`Scripts/scheduler.py` is a single long-running Python process. It computes the next firing time (timezone-aware, DST-aware, holiday-aware), runs `Scripts/prefetch.py` to populate `Scripts/cache/` with market data + signal scores, then runs `claude -p` with the right session prompt at the right moment.

The prefetch step is graceful: if it fails (network outage, yfinance rate-limit, etc.), the scheduler still fires the Claude session but exports `MRB_PREFETCH_FAILED=1` so the prompt falls back to web search and flags the data outage at the top of the session summary. `Logs/scheduler.log` shows `PREFETCH_OK` or `PREFETCH_FAIL` before each `FIRE` line.

### The schedule (all times IST)

| Session | Market | When (IST) | Native time | Purpose |
|---|---|---|---|---|
| `IN_OPEN` | NSE | Mon–Fri 09:15 | 09:15 IST | Morning sweep + paper fills |
| `IN_MIDDAY` | NSE | Mon–Fri 12:30 | 12:30 IST | Sentiment + stop review |
| `IN_CLOSE` | NSE | Mon–Fri 15:30 | 15:30 IST | EoD P&L + dashboard refresh |
| `US_OPEN` | NASDAQ | Mon–Fri 19:00 / 20:00 | 09:30 ET | Morning sweep + paper fills |
| `US_MIDDAY` | NASDAQ | Mon–Fri 22:00 / 23:00 | 12:30 ET | Sentiment + stop review |
| `US_CLOSE` | NASDAQ | Mon–Fri 01:30 / 02:30 (next day) | 16:00 ET | EoD P&L + dashboard refresh |
| `WEEKEND_REVIEW` | both | Saturday 10:00 | 10:00 IST | Weekly P&L + framework amendments |
| `MONTH_END` | both | Day 30 (2026-06-13) 11:00 | 11:00 IST | One-shot final paper-trade report |

US session times shift by 1 hour twice a year as US DST flips. The scheduler converts ET → IST on each firing so this is automatic.

Holidays are honored: NSE 2026 + NASDAQ 2026 + NYSE half-days (13:00 ET close) are encoded in `Scripts/holidays.json`. Weekend review fires regardless of holiday status.

### What each session does, in detail

#### `IN_OPEN` — 09:15 IST, NSE open

1. Read `Scripts/strategy_meta.json` to confirm locked NAV and end date.
2. Read latest IN portfolio state and today's recommendations log (if any).
3. **StrategyAdvisor `MACRO REGIME CHECK IN`** — classify India regime (Risk-On Trending / Choppy / Risk-Off / Rate-Sensitive / Stagflation) using India VIX, NIFTY 50 trend, USD/INR, 10Y G-Sec, FII/DII, RBI stance.
4. **SentimentMonitor `WATCHLIST PULSE IN`** — sweep watchlist + open positions.
5. **SignalEngine `WATCHLIST SCORE IN`** — score the whole IN watchlist.
6. For each HIGH-confidence (score ≥ 70) and qualifying MEDIUM candidate, run the full five-layer gate.
7. Execute paper fills for APPROVED verdicts at the NSE open price.
8. Append every verdict (trade and no-trade) to `Logs/Recommendations_<today>.md`.
9. Write a session summary to `Logs/sessions/<today>_IN_OPEN.md`.

#### `IN_MIDDAY` — 12:30 IST

1. `SentimentMonitor NEWS ALERT CHECK` on every open IN position.
2. For each URGENT alert → thesis re-review + stop tightening if warranted.
3. Routine `RiskManager STOP LOSS REVIEW` on every open IN position.
4. New openings only if a morning HIGH candidate has reached its trigger price and Risk re-validates.
5. Session summary at `Logs/sessions/<today>_IN_MIDDAY.md`.

#### `IN_CLOSE` — 15:30 IST

1. Fetch official NSE closes via web search.
2. `PortfolioTracker PORTFOLIO SNAPSHOT <today> IN` → `Portfolio/state/IN/portfolio_state_<today>.md`.
3. `BENCHMARK UPDATE IN` with the NIFTY 50 close.
4. `RiskManager PORTFOLIO RISK CHECK IN` + `DRAWDOWN CHECK IN`. If drawdown ≥ 15%, activate defensive mode for IN (no new IN longs).
5. Reconcile stop hits and target hits — execute paper closes/trims.
6. Append today's IN P&L line to `Logs/daily_pnl_IN.md`.
7. Finalize today's recommendations log.
8. **Rebuild `Dashboard/dashboard_data.js`** — the only file Mr.B ever overwrites. Same schema as documented in the dashboard README; both US and IN sections refreshed (US side reads from latest snapshot).
9. Session summary at `Logs/sessions/<today>_IN_CLOSE.md`.

#### `US_OPEN`, `US_MIDDAY`, `US_CLOSE`

Same structure as the IN sessions but for the US sub-portfolio, using S&P 500 / SPY / VIX / GICS sectors, NASDAQ prices via Yahoo Finance. `US_CLOSE` also refreshes the dashboard.

Note: `US_CLOSE` typically fires after midnight IST, so its session summary filename uses the **US trading date** (the date of the NASDAQ session that just closed), not the IST calendar date.

#### `WEEKEND_REVIEW` — Saturday 10:00 IST

1. `PortfolioTracker WEEKLY P&L REPORT` for both markets → `Portfolio/performance/{US,IN}/weekly_review_<YYYY>-W<NN>.md`.
2. `StrategyAdvisor STRATEGY REVIEW BOTH` → `Strategy/frameworks/strategy_review_<YYYY>-W<NN>.md`.
3. Review every open position for stop trailing; issue `UPDATE STOP` recommendations where appropriate.
4. Write a structured weekly review to `Logs/Weekly_Reviews/week_<NN>_<YYYY-MM-DD>.md` covering: P&L headline, what worked, what didn't, signal-class hit rate, sector shifts, concrete actions for next Monday.
5. **If a lesson materially changes how Mr.B should operate next week**, append a row to the Amendments Log at the bottom of `Strategy/ThreeMonthFramework.md`. The original framework text is never modified.
6. Refresh `Dashboard/dashboard_data.js`.
7. Session summary at `Logs/sessions/<today>_WEEKEND_REVIEW.md`.

#### `MONTH_END` — Day 30, one-shot

The final paper-trade report. Aggregates the whole month:

- Headline US and IN returns + alpha vs SPY / NIFTY 50
- Win rate, average R, max drawdown, peak NAV, sector P&L
- Trade-by-trade ledger
- Signal-class performance breakdown
- Calibration findings: did HIGH signals win? Did URGENT alerts predict moves? Did stops save more than they cost?
- A go / no-go recommendation for live deployment

Written to `Logs/Month_End_Report_<YYYY-MM-DD>.md`. A closing amendment row is appended to `Strategy/ThreeMonthFramework.md`. Dashboard refreshed one last time.

---

## 6. Paper-trade rules

| Parameter | Locked value |
|---|---|
| Mode | Paper trade — no real broker, no real money |
| Strategy start | First-launch date of the scheduler (locked in `Scripts/strategy_meta.json`) |
| Strategy end | Start + 30 days |
| US starting NAV | $10,000 USD |
| IN starting NAV | ₹10,00,000 INR |
| Top-ups | NONE during the run |
| Currency conversion | NEVER. USD stays USD. INR stays INR. |
| Fill price | `*_OPEN` → session-open · `*_MIDDAY` → last print · `*_CLOSE` → official close |
| Price source | Web search: Yahoo Finance (US), NSE site / Moneycontrol (IN) |
| Friction assumed | US ~0.05% round-trip; IN ~0.15% round-trip (STT + GST + brokerage + SEBI + stamp duty) |
| Position size cap | 10% / 6% / 3% of *that market's* NAV for HIGH / MEDIUM / LOW conviction |
| Sector cap | 25% of *that market's* NAV per sector |
| Drawdown trigger | 15% from peak — activates defensive mode for that market only |
| Cash floor | 10% of NAV per market, never deployed |
| Dry powder reserve | 10% of NAV per market, reserved for adding to winners |
| Compressed phases | Week 1 = Phase 1 (recon, ≤40% deployed) · Weeks 2–3 = Phase 2 (≤80%) · Week 4 = Phase 3 (reduce to ≤40%) |

---

## 7. File layout — where everything is written

```
workspace-broker/
├── MrB.md                              # Root orchestrator — read first every session
├── OPERATING_GUIDE.md                  # This file
│
├── Research/
│   ├── ResearchAnalyst.md              # Spec
│   └── reports/                        # [TICKER.US|.NS]_YYYY-MM-DD.md
│
├── Strategy/
│   ├── StrategyAdvisor.md              # Spec
│   ├── ThreeMonthFramework.md          # Master playbook + Amendments Log (append-only)
│   └── frameworks/                     # strategy_memo_YYYY-MM-DD.md, strategy_review_YYYY-WNN.md
│
├── Signals/
│   ├── SignalEngine.md                 # Spec
│   └── outputs/                        # [TICKER]_signal_YYYY-MM-DD.md, watchlist_score_*.md
│
├── Risk/
│   ├── RiskManager.md                  # Spec
│   └── rules/                          # clearance_[TICKER]_YYYY-MM-DD.md, stop_review_*.md
│
├── Portfolio/
│   ├── PortfolioTracker.md             # Spec
│   ├── state/
│   │   ├── US/portfolio_state_YYYY-MM-DD.md
│   │   └── IN/portfolio_state_YYYY-MM-DD.md
│   └── performance/
│       ├── US/weekly_review_YYYY-WNN.md
│       └── IN/weekly_review_YYYY-WNN.md
│
├── Sentiment/
│   ├── SentimentMonitor.md             # Spec
│   └── logs/                           # sentiment_[TICKER]_YYYY-MM-DD.md, watchlist_pulse_*.md
│
├── Logs/
│   ├── TradeLog.md                     # Append-only — every executed paper trade
│   ├── Recommendations_YYYY-MM-DD.md   # Append-only — every Mr.B verdict (trade + no-trade)
│   ├── daily_pnl_US.md                 # Append-only — one line per US trading day
│   ├── daily_pnl_IN.md                 # Append-only — one line per IN trading day
│   ├── Weekly_Reviews/                 # week_NN_YYYY-MM-DD.md
│   ├── Month_End_Report_YYYY-MM-DD.md  # One-shot final report
│   ├── scheduler.log                   # Supervisor lifecycle log
│   ├── scheduler.stdout.log            # launchd-captured stdout
│   ├── scheduler.stderr.log            # launchd-captured stderr
│   └── sessions/                       # YYYY-MM-DD_HHMM_SESSION_ID.log (claude stdout) + summary .md
│
├── Scripts/
│   ├── scheduler.py                    # Long-running supervisor
│   ├── prefetch.py                     # Pre-session data + signals pull (writes cache/)
│   ├── data_feed.py                    # yfinance wrapper (US + IN tickers)
│   ├── indicators.py                   # Pure-math technical indicators
│   ├── signal_engine.py                # Deterministic composite scoring + classification
│   ├── requirements.txt                # Python deps (yfinance, pandas, numpy)
│   ├── watchlist_US.txt                # US watchlist (one .US ticker per line)
│   ├── watchlist_IN.txt                # IN watchlist (one .NS ticker per line)
│   ├── cache/                          # Created at first prefetch run — never edit by hand
│   │   ├── snapshot_US_YYYY-MM-DD_HHMM.json   # Per-session authoritative snapshot
│   │   ├── snapshot_IN_YYYY-MM-DD_HHMM.json
│   │   ├── signals/<TICKER>_YYYY-MM-DD.json   # Per-ticker detail
│   │   └── prices/<TICKER>.csv                # Rolling OHLCV cache
│   ├── prompts/                        # 8 session prompts
│   │   ├── in_open.md
│   │   ├── in_midday.md
│   │   ├── in_close.md
│   │   ├── us_open.md
│   │   ├── us_midday.md
│   │   ├── us_close.md
│   │   ├── weekend_review.md
│   │   ├── month_end.md
│   │   └── _preamble.md                # Shared preamble reference
│   ├── holidays.json                   # 2026 NSE + NASDAQ + NASDAQ_EARLY_CLOSE
│   ├── strategy_meta.json              # Written once at first launch — LOCKED
│   ├── com.parikshit.mrb-scheduler.plist  # launchd bootstrap template
│   └── README.md                       # Scheduler-specific README
│
└── Dashboard/
    ├── index.html                      # Single-file React app (CDN deps)
    ├── dashboard_data.js               # Rebuilt at every close (only allowed overwrite)
    └── README.md                       # Dashboard-specific README
```

### Hard invariants (Mr.B enforces these on itself)

1. **Never delete any file.** Not snapshots, not drafts, not session logs.
2. **Never leave** `/Users/parikshitgangaher/Codes/workspace-broker/`. All reads and writes stay inside.
3. **Never overwrite an existing file** — except `Dashboard/dashboard_data.js`, which is by design a rolling snapshot rebuilt from append-only sources. If a same-date file already exists, Mr.B writes `..._YYYY-MM-DD-v2.md` (then `-v3`, etc.) and notes the supersession.

---

## 8. The dashboard

Open it any time:

```bash
open /Users/parikshitgangaher/Codes/workspace-broker/Dashboard/index.html
```

If your browser blocks the local script-load (rare), serve it locally:

```bash
python3 -m http.server 8000 --directory /Users/parikshitgangaher/Codes/workspace-broker/Dashboard
open http://localhost:8000
```

What you'll see:

- **Two header cards** — one per market — with current NAV, today's P&L, total return %, peak NAV, current drawdown, benchmark return, alpha. INR is formatted with Indian lakhs commas (`₹10,00,000`), USD with western commas (`$10,000.00`).
- **Two NAV history charts** — your portfolio NAV vs benchmark (rebased to your starting NAV) over the run.
- **Two open positions tables** — ticker, sector, shares, entry, current, unrealized P&L (colored), stop, target, conviction badge.
- **Recommendations feed** — last 10 Mr.B verdicts with market badge, ticker, action, conviction, one-line reasoning.

The dashboard refreshes on page reload. Underlying `dashboard_data.js` is rebuilt at every `IN_CLOSE`, `US_CLOSE`, `WEEKEND_REVIEW`, and `MONTH_END`. Until the first close fires, it renders a friendly "No data yet" panel.

---

## 9. Your daily workflow

You don't have to do anything to keep Mr.B running once the launchd agent is installed. A realistic daily rhythm:

| Time (IST) | What's happening | What you might do |
|---|---|---|
| ~09:30 | `IN_OPEN` complete | Skim `Logs/Recommendations_<today>.md` — see what got flagged at the open |
| ~12:45 | `IN_MIDDAY` complete | Quick check if any URGENT alerts fired |
| ~16:00 | `IN_CLOSE` complete | Refresh the dashboard — first NAV data point of the day. Read the IN session summary in `Logs/sessions/<today>_IN_CLOSE.md` |
| ~20:00 | `US_OPEN` complete | If you're up, scan US open recommendations |
| ~02:30 next morning | `US_CLOSE` complete | Dashboard now has full daily data for both markets (yesterday US + today IN) |
| Saturday 10:30 | `WEEKEND_REVIEW` complete | **Read this carefully**. It's the synthesis: what worked, what didn't, lessons, framework amendments, next-Monday action list. File: `Logs/Weekly_Reviews/week_NN_<date>.md` |
| Day 30 ~11:30 | `MONTH_END` complete | Read the final report: `Logs/Month_End_Report_<date>.md`. This contains the go / no-go recommendation for live deployment |

The two files you'll read most:

- **`Logs/Recommendations_<today>.md`** — every verdict, every day, with reasoning.
- **`Logs/Weekly_Reviews/week_NN_<date>.md`** — weekly synthesis with concrete actions.

---

## 10. Manual control

You can talk to Mr.B yourself any time. Open Claude Code in the workspace:

```bash
cd /Users/parikshitgangaher/Codes/workspace-broker
claude
```

Then ask anything natural:

- *"Mr.B, what about RELIANCE.NS right now?"* → runs the five-layer gate manually, logs the verdict.
- *"Mr.B, do a full sentiment pulse on my IN watchlist."*
- *"Mr.B, what's the current US drawdown?"*
- *"Mr.B, why did you not take TCS.NS yesterday?"* → he'll find the entry in `Logs/Recommendations_*.md` and explain.

Manual verdicts are appended to the same daily Recommendations log as the scheduled ones — no separation.

You can also force a session yourself:

```bash
# Re-run IN_CLOSE for today (will not overwrite — writes -v2 if needed)
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --force IN_CLOSE

# Force the weekend review on a weekday
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --force WEEKEND_REVIEW

# Dry run — log the next firing but don't actually invoke claude
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --dry-run

# Show next 8 upcoming firings
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --next
```

---

## 11. Stopping, pausing, resetting

### Pause the scheduler (don't fire sessions for a while)

```bash
launchctl unload ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist
```

To resume:

```bash
launchctl load ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist
```

### Stop permanently

```bash
launchctl unload ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist
rm ~/Library/LaunchAgents/com.parikshit.mrb-scheduler.plist
```

The workspace files remain untouched. You can still use Mr.B manually via `claude` interactively.

### Reset the strategy meta (before the first launch)

If you want a different start date, do this **before** the first launch:

```bash
rm /Users/parikshitgangaher/Codes/workspace-broker/Scripts/strategy_meta.json
```

The supervisor will recreate it on next start with today's date.

⚠️ **Do not reset `strategy_meta.json` mid-run.** It will corrupt the audit trail since all historical entries reference the locked starting NAVs.

---

## 12. Troubleshooting

### `claude: command not found` in `Logs/sessions/*.log`

The launchd plist sets `PATH` explicitly because launchd does not inherit your shell `PATH`. Check that `which claude` resolves and that the path is in the plist's `EnvironmentVariables.PATH`. Current plist includes `/Users/parikshitgangaher/.local/bin` which is where `claude` lives on this machine.

### Session fired but log file is empty

The `claude -p` invocation may have errored before writing. Check `Logs/scheduler.log` for the exit code, and `Logs/scheduler.stderr.log` for any Python traceback from the supervisor.


### A session fired at the wrong IST time

Likely a US DST flip just happened (around early March and early November). The scheduler converts ET → IST per day, so this should be automatic. If it isn't, verify the host's `/usr/share/zoneinfo/America/New_York` is fresh.

### Mr.B skipped a day that should have been a trading day

Open `Scripts/holidays.json` and check whether that date was incorrectly listed under `NSE` or `NASDAQ`. Edit and save; the supervisor reloads the file before each firing.

### Dashboard shows "No data yet" forever

The dashboard reads `Dashboard/dashboard_data.js`, which is rebuilt at every close. If no close has fired yet (or every close has errored), the placeholder stays. Force one:

```bash
python3 /Users/parikshitgangaher/Codes/workspace-broker/Scripts/scheduler.py --force IN_CLOSE
```

Then refresh the browser.

### How do I see what the scheduler is doing right now?

```bash
tail -f /Users/parikshitgangaher/Codes/workspace-broker/Logs/scheduler.log
```

You'll see one line per event: next firing time, FIRE events with session ID, DONE events with exit codes.

### Prefetch failed — what now?

The scheduler logs `PREFETCH_FAIL <SESSION_ID> | exit=... | stderr=...` to `Logs/scheduler.log` and still fires the Claude session with `MRB_PREFETCH_FAILED=1` in the environment. The session prompt then falls back to web search and flags the outage at the top of its summary.

Common causes:

- **yfinance rate-limit (HTTP 429)** — usually clears in 10–15 min. Force-re-run: `python3 Scripts/prefetch.py IN_OPEN` (or whichever session).
- **Network outage** — check connectivity, then re-run prefetch manually.
- **Watchlist has a bad ticker** — `Scripts/cache/snapshot_*.json` will list it under `data_errors`. Fix `Scripts/watchlist_{US,IN}.txt` and re-run.
- **Venv not installed** — `python3 -m venv .venv && source .venv/bin/activate && pip install -r Scripts/requirements.txt`.

### How do I see what Mr.B actually said in a session?

```bash
ls /Users/parikshitgangaher/Codes/workspace-broker/Logs/sessions/
```

Each session produces two artifacts there:

- `<date>_<HHMM>_<SESSION_ID>.log` — raw stdout/stderr from `claude -p`.
- `<date>_<SESSION_ID>.md` — Mr.B's own one-page session summary.

### How do I know if Mr.B is making good calls?

Two views:

- **Daily**: `Logs/Recommendations_<today>.md` — every verdict with reasoning.
- **Weekly**: `Logs/Weekly_Reviews/week_NN_<date>.md` — what worked, what didn't, signal-class hit rates, calibration.

The dashboard gives you the bottom line in numbers; the recommendations log gives you the reasoning behind each call.

---

## What's next after this 1-month run

At day 30, `Logs/Month_End_Report_<date>.md` will contain Mr.B's structured calibration findings and a go / no-go recommendation for live deployment. Use that report to decide whether to:

- Run another paper month with adjusted rules
- Go live with a fraction of the paper-trade capital
- Recalibrate specific signal classes or sectors
- Stop

That decision is yours, not Mr.B's. Mr.B's role here is to give you the data and reasoning to make it.
