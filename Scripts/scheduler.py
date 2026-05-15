#!/usr/bin/env python3
"""
Mr.B scheduler — long-running supervisor that fires session prompts at
market open / mid-day / close for NSE and NASDAQ, plus a weekend review
and a one-shot month-end report.

Design notes are in /Users/parikshitgangaher/.claude/plans/check-the-mr-b-file-delegated-dewdrop.md
and in MrB.md (`Unattended Mode` section).

Usage:
    python3 Scripts/scheduler.py                # run forever
    python3 Scripts/scheduler.py --force IN_OPEN   # fire one session now
    python3 Scripts/scheduler.py --next         # print next firing and exit
    python3 Scripts/scheduler.py --dry-run      # show schedule, do not invoke claude

Requires Python 3.9+ (zoneinfo). No third-party dependencies.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, date, time as dtime
from pathlib import Path
from zoneinfo import ZoneInfo

WORKSPACE = Path("/Users/parikshitgangaher/Codes/workspace-broker")
SCRIPTS_DIR = WORKSPACE / "Scripts"
PROMPTS_DIR = SCRIPTS_DIR / "prompts"
LOGS_DIR = WORKSPACE / "Logs"
SESSIONS_DIR = LOGS_DIR / "sessions"
SCHEDULER_LOG = LOGS_DIR / "scheduler.log"
META_PATH = SCRIPTS_DIR / "strategy_meta.json"
HOLIDAYS_PATH = SCRIPTS_DIR / "holidays.json"

IST = ZoneInfo("Asia/Kolkata")
ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")

STARTING_NAV_USD = 10000
STARTING_NAV_INR = 1000000
PAPER_TRADE_DAYS = 30

# Session definitions ─ each entry is (session_id, market, kind, time_in_native_tz, tz)
#   kind:    OPEN | MIDDAY | CLOSE | WEEKEND | MONTH_END
#   tz:      ZoneInfo to interpret the time
# NSE hours: 09:15–15:30 IST; we fire OPEN at 09:15, MIDDAY at 12:30, CLOSE at 15:30.
# NASDAQ hours: 09:30–16:00 ET; we fire OPEN at 09:30 ET, MIDDAY at 12:30 ET, CLOSE at 16:00 ET.
# Weekend: Saturday 10:00 IST.
# Month end: one-shot, day +30 from strategy start, 11:00 IST.
SESSIONS = [
    ("IN_OPEN",   "IN", "OPEN",   dtime(9, 15), IST),
    ("IN_MIDDAY", "IN", "MIDDAY", dtime(12, 30), IST),
    ("IN_CLOSE",  "IN", "CLOSE",  dtime(15, 30), IST),
    ("US_OPEN",   "US", "OPEN",   dtime(9, 30), ET),
    ("US_MIDDAY", "US", "MIDDAY", dtime(12, 30), ET),
    ("US_CLOSE",  "US", "CLOSE",  dtime(16, 0), ET),
    ("WEEKEND_REVIEW", "BOTH", "WEEKEND", dtime(10, 0), IST),
    ("MONTH_END", "BOTH", "MONTH_END", dtime(11, 0), IST),
]


@dataclass(frozen=True)
class Firing:
    when_utc: datetime
    session_id: str
    market: str


def log_line(msg: str) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S %z")
    line = f"[{ts}] {msg}\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    with SCHEDULER_LOG.open("a") as f:
        f.write(line)


def load_holidays() -> dict:
    if not HOLIDAYS_PATH.exists():
        log_line(f"holidays.json missing at {HOLIDAYS_PATH}; treating all weekdays as trading days")
        return {"NSE": [], "NASDAQ": [], "NASDAQ_EARLY_CLOSE": []}
    with HOLIDAYS_PATH.open() as f:
        return json.load(f)


def load_or_init_meta() -> dict:
    if META_PATH.exists():
        with META_PATH.open() as f:
            return json.load(f)
    today = datetime.now(IST).date()
    end = today + timedelta(days=PAPER_TRADE_DAYS)
    meta = {
        "mode": "paper_trade",
        "strategy_start": today.isoformat(),
        "strategy_end": end.isoformat(),
        "duration_days": PAPER_TRADE_DAYS,
        "markets": {
            "US": {"starting_nav": STARTING_NAV_USD, "currency": "USD", "currency_symbol": "$"},
            "IN": {"starting_nav": STARTING_NAV_INR, "currency": "INR", "currency_symbol": "₹"},
        },
        "notes": "Hard-cap paper trade. No top-ups. Locked at first scheduler launch.",
    }
    META_PATH.parent.mkdir(parents=True, exist_ok=True)
    with META_PATH.open("w") as f:
        json.dump(meta, f, indent=2)
    log_line(f"wrote strategy_meta.json: start={meta['strategy_start']} end={meta['strategy_end']}")
    return meta


def is_trading_day(d: date, market: str, holidays: dict) -> bool:
    if d.weekday() >= 5:
        return False
    iso = d.isoformat()
    if market == "IN":
        return iso not in holidays.get("NSE", [])
    if market == "US":
        return iso not in holidays.get("NASDAQ", [])
    return True


def early_close_time(d: date, holidays: dict) -> dtime | None:
    iso = d.isoformat()
    early = holidays.get("NASDAQ_EARLY_CLOSE", [])
    if iso in early:
        return dtime(13, 0)  # NYSE half-day close at 13:00 ET
    return None


def next_firings(now_utc: datetime, meta: dict, holidays: dict, lookahead_days: int = 7) -> list[Firing]:
    out: list[Firing] = []
    strategy_end = date.fromisoformat(meta["strategy_end"])
    month_end_date = date.fromisoformat(meta["strategy_end"])

    for delta in range(lookahead_days + 1):
        d = (now_utc.astimezone(IST) + timedelta(days=delta)).date()
        for sid, market, kind, t, tz in SESSIONS:
            if kind == "WEEKEND":
                if d.weekday() != 5:
                    continue
                fire_local = datetime.combine(d, t, tzinfo=tz)
            elif kind == "MONTH_END":
                if d != month_end_date:
                    continue
                fire_local = datetime.combine(d, t, tzinfo=tz)
            else:
                if market in ("US", "IN") and not is_trading_day(d, market, holidays):
                    continue
                effective_t = t
                if market == "US" and kind == "CLOSE":
                    ec = early_close_time(d, holidays)
                    if ec is not None:
                        effective_t = ec
                fire_local = datetime.combine(d, effective_t, tzinfo=tz)
            fire_utc = fire_local.astimezone(UTC)
            if fire_utc <= now_utc:
                continue
            if d > strategy_end and kind != "MONTH_END":
                continue
            out.append(Firing(when_utc=fire_utc, session_id=sid, market=market))
    out.sort(key=lambda f: f.when_utc)
    return out


def prompt_path(session_id: str) -> Path:
    return PROMPTS_DIR / f"{session_id.lower()}.md"


def session_log_path(session_id: str, when: datetime) -> Path:
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    return SESSIONS_DIR / f"{when.astimezone(IST).strftime('%Y-%m-%d_%H%M')}_{session_id}.log"


def run_prefetch(session_id: str) -> bool:
    """Run Scripts/prefetch.py to populate Scripts/cache/ before the Claude session.
    Returns True on success, False on any failure (Claude session still fires either way).
    """
    prefetch_path = SCRIPTS_DIR / "prefetch.py"
    if not prefetch_path.exists():
        log_line(f"PREFETCH_SKIPPED {session_id} | prefetch.py not found")
        return False
    # Prefer venv python if present, fall back to system python3.
    venv_py = WORKSPACE / ".venv" / "bin" / "python3"
    py = str(venv_py) if venv_py.exists() else sys.executable or "python3"
    try:
        proc = subprocess.run(
            [py, str(prefetch_path), session_id],
            cwd=str(WORKSPACE),
            timeout=10 * 60,  # 10 min cap
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0:
            snaps = [l for l in proc.stdout.splitlines() if l.strip()]
            log_line(f"PREFETCH_OK {session_id} | snapshots={','.join(snaps) if snaps else '(none)'}")
            return True
        log_line(f"PREFETCH_FAIL {session_id} | exit={proc.returncode} | stderr={proc.stderr.strip()[:500]}")
        return False
    except subprocess.TimeoutExpired:
        log_line(f"PREFETCH_TIMEOUT {session_id} after 10min")
        return False
    except Exception as e:
        log_line(f"PREFETCH_ERROR {session_id} | {type(e).__name__}: {e}")
        return False


def invoke_claude(session_id: str, dry_run: bool = False) -> int:
    pp = prompt_path(session_id)
    if not pp.exists():
        log_line(f"PROMPT MISSING for {session_id} at {pp}; skipping invocation")
        return 2
    when = datetime.now(UTC)
    log_path = session_log_path(session_id, when)

    # Run prefetch first. Graceful degradation: if prefetch fails, fire Claude
    # anyway but set MRB_PREFETCH_FAILED=1 so the session prompt knows to fall
    # back to web search and flag the outage at the top of its summary.
    prefetch_ok = run_prefetch(session_id) if not dry_run else True

    log_line(f"FIRE {session_id} | prompt={pp.name} | log={log_path.name} | prefetch={'ok' if prefetch_ok else 'FAILED'}")
    if dry_run:
        return 0
    prompt_text = pp.read_text()
    cmd = ["claude", "-p"]
    env = os.environ.copy()
    if not prefetch_ok:
        env["MRB_PREFETCH_FAILED"] = "1"
    try:
        with log_path.open("w") as logf:
            logf.write(f"# session={session_id} fired_at={when.astimezone(IST).isoformat()}\n")
            logf.write(f"# prefetch={'ok' if prefetch_ok else 'FAILED'}\n\n")
            logf.flush()
            proc = subprocess.run(
                cmd,
                input=prompt_text,
                stdout=logf,
                stderr=subprocess.STDOUT,
                cwd=str(WORKSPACE),
                env=env,
                timeout=60 * 60,  # 1h max per session
                text=True,
            )
        log_line(f"DONE {session_id} | exit={proc.returncode}")
        return proc.returncode
    except FileNotFoundError:
        log_line(f"ERROR claude CLI not found in PATH; install Claude Code or update PATH in launchd plist")
        return 127
    except subprocess.TimeoutExpired:
        log_line(f"TIMEOUT {session_id} after 60min")
        return 124


def run_forever(dry_run: bool = False) -> None:
    meta = load_or_init_meta()
    log_line(f"scheduler start | strategy_start={meta['strategy_start']} strategy_end={meta['strategy_end']}")
    while True:
        holidays = load_holidays()
        meta = load_or_init_meta()
        firings = next_firings(datetime.now(UTC), meta, holidays, lookahead_days=14)
        if not firings:
            log_line("no upcoming firings within 14 days; sleeping 1h")
            time.sleep(3600)
            continue
        nxt = firings[0]
        wait = (nxt.when_utc - datetime.now(UTC)).total_seconds()
        log_line(f"next: {nxt.session_id} at {nxt.when_utc.astimezone(IST).strftime('%Y-%m-%d %H:%M %Z')} (in {int(wait)}s)")
        # Sleep in chunks so we re-check holidays/meta periodically.
        while wait > 0:
            chunk = min(wait, 300)
            time.sleep(chunk)
            wait = (nxt.when_utc - datetime.now(UTC)).total_seconds()
        invoke_claude(nxt.session_id, dry_run=dry_run)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", metavar="SESSION_ID", help="Fire a single session now and exit")
    ap.add_argument("--next", action="store_true", help="Print next firing and exit")
    ap.add_argument("--dry-run", action="store_true", help="Show schedule, do not invoke claude")
    args = ap.parse_args()

    if args.force:
        sid = args.force.upper()
        if sid not in {s[0] for s in SESSIONS}:
            print(f"unknown session: {sid}", file=sys.stderr)
            return 2
        load_or_init_meta()
        return invoke_claude(sid, dry_run=args.dry_run)

    if args.next:
        meta = load_or_init_meta()
        holidays = load_holidays()
        firings = next_firings(datetime.now(UTC), meta, holidays, lookahead_days=14)
        for f in firings[:8]:
            print(f"{f.when_utc.astimezone(IST).strftime('%Y-%m-%d %H:%M %Z')}  {f.session_id}")
        return 0

    run_forever(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
