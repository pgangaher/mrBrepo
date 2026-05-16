#!/usr/bin/env python3
"""Delete cache files older than CUTOFF_DAYS days. Run manually or via cron."""
from __future__ import annotations

from pathlib import Path
from datetime import datetime

CACHE_DIR = Path(__file__).resolve().parent / "cache"
CUTOFF_DAYS = 30


def main() -> None:
    cutoff = datetime.now().timestamp() - CUTOFF_DAYS * 86400
    removed = 0
    for f in CACHE_DIR.rglob("*"):
        if f.is_file() and f.stat().st_mtime < cutoff:
            f.unlink()
            removed += 1
    print(f"Removed {removed} cache files older than {CUTOFF_DAYS} days")


if __name__ == "__main__":
    main()
