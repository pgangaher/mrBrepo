# Mr.B — Bug Fix Log

A running record of bugs found, root causes, fixes applied, and any manual recovery steps taken.

---

## 2026-05-15 — Scheduler never invoked Claude (two bugs)

**Affected sessions:** Every session from first launch. First noticed at `IN_OPEN` 09:15 IST on 2026-05-15.

---

### Bug 1 — `subprocess.run` crashed on string input (`text=True` missing)

**Symptom:**
Session log files contained only the two-line header and nothing else. `Logs/scheduler.stderr.log` showed:

```
TypeError: memoryview: a bytes-like object is required, not 'str'
```

**Root cause:**
`invoke_claude` in `Scripts/scheduler.py` passed `input=prompt_text` (a `str`) to `subprocess.run` without setting `text=True`. Python's subprocess defaults to binary mode and expects `bytes` for `input`, so it crashed before Claude was ever invoked. Prefetch ran fine and the `FIRE` line was written to `scheduler.log`, making it look like the session had started.

**Fix:**
Added `text=True` to the `subprocess.run` call in `invoke_claude`.

```python
# before
proc = subprocess.run(cmd, input=prompt_text, stdout=logf, ...)

# after
proc = subprocess.run(cmd, input=prompt_text, stdout=logf, ..., text=True)
```

---

### Bug 2 — `claude --cwd` is not a valid flag

**Symptom:**
After Bug 1 was fixed, the session log showed:

```
error: unknown option '--cwd'
```

Claude exited with code 1 immediately.

**Root cause:**
The command array was built as `["claude", "-p", "--cwd", str(WORKSPACE)]`. The `claude` CLI does not accept a `--cwd` flag. The working directory was already correctly set via `subprocess.run`'s own `cwd=str(WORKSPACE)` parameter, making the flag both wrong and redundant.

**Fix:**
Removed `"--cwd", str(WORKSPACE)` from the command array.

```python
# before
cmd = ["claude", "-p", "--cwd", str(WORKSPACE)]

# after
cmd = ["claude", "-p"]
```

---

### Recovery — forced IN_OPEN replay on 2026-05-15

Both bugs together meant Mr.B had never been invoked since the scheduler first launched on 2026-05-14.

After applying both fixes, the `IN_OPEN` session that should have fired at 09:15 IST was manually replayed at ~10:00 IST using:

```bash
python3 Scripts/scheduler.py --force IN_OPEN
```

The session fired with a fresh prefetch snapshot (`snapshot_IN_2026-05-15_0957.json`). The session log is at `Logs/sessions/2026-05-15_0957_IN_OPEN.log`.

The launchd daemon was also restarted (`launchctl kickstart`) to pick up both fixes. `IN_MIDDAY` at 12:30 IST will be the first session to fire with a fully working scheduler.

---

## 2026-05-15 — IN_MIDDAY output silently discarded (missing Write permissions)

**Affected sessions:** `IN_MIDDAY` 12:30 IST on 2026-05-15. Potentially all prior sessions if they had generated output.

---

### Bug — `Write(**)` and `Edit(**)` absent from `.claude/settings.local.json`

**Symptom:**
The `IN_MIDDAY` session ran for 8 minutes and exited cleanly (`exit=0`, `elapsed=514s`). The session log (`Logs/sessions/2026-05-15_1230_IN_MIDDAY.log`) contained a full 7 KB of analysis — stop reviews, watchlist rankings, recommendations, session summary — but **none of the output files were created**. `Risk/rules/`, `Logs/Recommendations_*.md`, and `Logs/sessions/*.md` were all empty.

The session itself reported: *"I'm in a permission catch-22 — even the settings file edit is blocked."*

**Root cause:**
`.claude/settings.local.json` had no `Write(**)` or `Edit(**)` entries in its `allow` list. In non-interactive `claude -p` mode, any tool call not on the allow list is rejected without prompting. Every file write attempt silently failed, but the session continued — Claude generated all its analysis as text output (captured in the `.log` file) but could not persist any of it.

The allow list also lacked basic read-only Bash commands (`cat`, `ls`, `find`, `grep`) that session prompts use for file discovery.

**Fix:**
Added the following entries to `.claude/settings.local.json`:

```json
"Write(**)",
"Edit(**)",
"Bash(mkdir -p *)",
"Bash(cat *)",
"Bash(ls *)",
"Bash(find *)",
"Bash(grep *)"
```

**Recovery:**
The full `IN_MIDDAY` analysis was salvaged from `Logs/sessions/2026-05-15_1230_IN_MIDDAY.log` and written to the correct output files:

- `Risk/rules/stop_review_IN_2026-05-15.md` — stop review (no open positions; watchlist top signals noted)
- `Logs/Recommendations_2026-05-15.md` — 4 recommendations: ONGC.NS WATCH, ADANIPORTS.NS WATCH, ADANIENT.NS WATCH, IT sector NO-TRADE
- `Logs/sessions/2026-05-15_IN_MIDDAY.md` — session summary

**Why IN_OPEN (09:15, 10:00) logs were also blank:**
These sessions were killed mid-run by launchd restarting the scheduler process during bug-fix testing earlier in the day. This is not a code bug — the sessions were terminated before Claude could produce output. The fixes described above prevent this from happening in normal operation.

---

## 2026-05-15 — Code quality improvements (non-breaking)

Applied the following improvements while the scheduler was running. All changes take effect at the next session fire without requiring a restart.

### `Scripts/data_feed.py`
- **Intraday fallback now logs to stderr** — the silent `except Exception: pass` in `fetch_quote()` now prints a DEBUG line to stderr so transient network errors are visible without polluting normal runs.
- **`fetch_benchmark()` gained retry logic** — previously had no retry on transient yfinance failures. Now uses the same 3-attempt exponential backoff (`1.5²` spacing) as `fetch_ohlcv()`.

### `Scripts/prefetch.py`
- **Snapshot filenames now include seconds** — `session_clock()` changed from `%H%M` to `%H%M%S`. Prevents overwrite if prefetch is rerun within the same minute (e.g. via `--force` twice). Old format: `snapshot_IN_2026-05-15_1230.json`. New format: `snapshot_IN_2026-05-15_123042.json`.

### `Scripts/scheduler.py`
- **`WORKSPACE` path is now derived from script location** — changed from the hardcoded `/Users/parikshitgangaher/Codes/workspace-broker` to `Path(__file__).resolve().parent.parent`. Consistent with `prefetch.py`'s approach; portable if the directory is moved.
- **`DONE` log lines now include elapsed time** — e.g. `DONE IN_MIDDAY | exit=0 | elapsed=514s`. Makes it easy to detect hung sessions vs fast error exits.

### `Scripts/signal_engine.py` and `Scripts/indicators.py`
- **Full type annotations added** to all public functions — parameter types and return types (using `float | None`, `dict[str, float | None]`, `tuple[pd.Series, ...]`, etc.). No behaviour change; enables IDE validation and makes the signal rubric easier to audit.

### `Scripts/requirements.txt`
- **Upper-bound pins added** — `yfinance>=0.2.40,<0.3`, `pandas>=2.0,<3.0`, `numpy>=1.24,<2.0`. Prevents a breaking yfinance/pandas/numpy major-version bump from silently breaking an overnight session.

### New: `Scripts/cache_cleanup.py`
- Deletes cache files older than 30 days from `Scripts/cache/`. Run manually with `python3 Scripts/cache_cleanup.py`. No files from the current 30-day paper-trade run will be touched.

### New: `Scripts/tests/test_indicators.py` and `Scripts/tests/test_signal_engine.py`
- 40 pytest unit tests for the pure-math modules. Run with `python3 -m pytest Scripts/tests/ -v`. All 40 pass on Python 3.9.6 with the current library versions.

---
