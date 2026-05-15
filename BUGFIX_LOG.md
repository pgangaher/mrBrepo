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
