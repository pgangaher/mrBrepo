#!/usr/bin/env python3
"""Mr.B prefetch — pulls market data, computes deterministic indicators + signal
scores, writes a session snapshot JSON the Claude session reads instead of
web-searching for prices.

Usage:
    python3 Scripts/prefetch.py <SESSION_ID>

SESSION_ID ∈ {
    IN_OPEN, IN_MIDDAY, IN_CLOSE,
    US_OPEN, US_MIDDAY, US_CLOSE,
    WEEKEND_REVIEW, MONTH_END
}

Outputs:
    Scripts/cache/snapshot_{MARKET}_{YYYY-MM-DD}_{HHMM}.json   (one per market)
    Scripts/cache/signals/{TICKER}_{YYYY-MM-DD}.json           (per-ticker detail)
    Scripts/cache/prices/{TICKER}.csv                          (rolling history)

Exit code: 0 if at least one market snapshot wrote successfully, 1 otherwise.
"""
from __future__ import annotations

import json
import re
import sys
import traceback
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = SCRIPT_DIR.parent
CACHE_DIR = SCRIPT_DIR / "cache"
PRICES_DIR = CACHE_DIR / "prices"
SIGNALS_DIR = CACHE_DIR / "signals"

sys.path.insert(0, str(SCRIPT_DIR))
import indicators  # noqa: E402
import signal_engine  # noqa: E402
from data_feed import (  # noqa: E402
    DataFeedError,
    fetch_benchmark,
    fetch_ohlcv,
    fetch_quote,
    fetch_vol_gauge,
)

IST = ZoneInfo("Asia/Kolkata")

SESSION_MARKETS = {
    "IN_OPEN": ["IN"],
    "IN_MIDDAY": ["IN"],
    "IN_CLOSE": ["IN"],
    "US_OPEN": ["US"],
    "US_MIDDAY": ["US"],
    "US_CLOSE": ["US"],
    "WEEKEND_REVIEW": ["IN", "US"],
    "MONTH_END": ["IN", "US"],
}

TICKER_RE = re.compile(r"\b([A-Z][A-Z0-9.&-]*\.(?:US|NS|BO))\b")


def today_str() -> str:
    return datetime.now(IST).strftime("%Y-%m-%d")


def session_clock() -> str:
    return datetime.now(IST).strftime("%H%M%S")


def load_watchlist(market: str) -> list[str]:
    path = SCRIPT_DIR / f"watchlist_{market}.txt"
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


def load_open_positions(market: str) -> list[str]:
    state_dir = WORKSPACE / "Portfolio" / "state" / market
    if not state_dir.exists():
        return []
    files = sorted(state_dir.glob("portfolio_state_*.md"))
    if not files:
        return []
    text = files[-1].read_text()
    suffix = "US" if market == "US" else "NS"
    tickers = set()
    for m in TICKER_RE.finditer(text):
        t = m.group(1)
        if t.endswith(f".{suffix}"):
            tickers.add(t)
    return sorted(tickers)


def compute_for_ticker(
    ticker: str,
    df: pd.DataFrame,
    peer_returns_by_period: dict,
    bench_df: pd.DataFrame | None,
) -> dict:
    close = df["Close"]
    high = df["High"]
    low = df["Low"]
    volume = df["Volume"]

    try:
        quote = fetch_quote(ticker)
    except DataFeedError:
        last = df.iloc[-1]
        quote = {
            "last_price": float(last["Close"]),
            "open": float(last["Open"]),
            "high": float(last["High"]),
            "low": float(last["Low"]),
            "close": float(last["Close"]),
            "volume": float(last["Volume"]),
            "as_of": str(last["Date"]),
            "source": "yfinance-history-only",
        }

    rsi_series = indicators.rsi(close)
    macd_line, macd_signal_line, hist = indicators.macd(close)
    atr_series = indicators.atr(high, low, close)

    rsi_value = float(rsi_series.iloc[-1])
    hist_today = float(hist.iloc[-1])
    hist_prev = float(hist.iloc[-2]) if len(hist) > 1 else None
    atr_value = float(atr_series.iloc[-1])

    rets = indicators.returns(close, periods=(21, 63, 126))
    n20 = indicators.n_day_high(high, 20)
    sma_200 = indicators.sma(close, 200)
    vol_ratio = indicators.volume_ratio(volume)
    bbu, bbm, bbl = indicators.bbands(close)

    bench_3m = None
    if bench_df is not None and not bench_df.empty:
        bench_rets = indicators.returns(bench_df["Close"], periods=(63,))
        bench_3m = bench_rets.get(63)

    subs = {
        "momentum_1m": signal_engine.momentum_subscore(rets.get(21), peer_returns_by_period.get(21, [])),
        "momentum_3m": signal_engine.momentum_subscore(rets.get(63), peer_returns_by_period.get(63, [])),
        "momentum_6m": signal_engine.momentum_subscore(rets.get(126), peer_returns_by_period.get(126, [])),
        "rel_strength": signal_engine.rel_strength_subscore(rets.get(63), bench_3m),
        "volume_confirm": signal_engine.volume_confirm_subscore(vol_ratio, rets.get(21)),
        "rsi_zone": signal_engine.rsi_zone_subscore(rsi_value),
        "macd_signal": signal_engine.macd_signal_subscore(hist_today, hist_prev),
        # Earnings calendar via yfinance is unreliable; left None — composite
        # re-normalizes remaining weights. SignalEngine.md amendment notes this.
        "earnings_cat": None,
    }

    score = signal_engine.composite(subs)
    cls = signal_engine.classify(
        composite_score=score,
        subscores=subs,
        rsi_value=rsi_value,
        close_today=float(close.iloc[-1]),
        n_day_high_20=n20,
        sma_200=sma_200,
        momentum_3m=rets.get(63),
        momentum_6m=rets.get(126),
        peer_3m=peer_returns_by_period.get(63, []),
        peer_6m=peer_returns_by_period.get(126, []),
    )
    stop = signal_engine.stop_atr(float(close.iloc[-1]), atr_value)

    return {
        "ticker": ticker,
        "quote": quote,
        "indicators": {
            "rsi_14": rsi_value,
            "macd_line": float(macd_line.iloc[-1]),
            "macd_signal": float(macd_signal_line.iloc[-1]),
            "macd_hist": hist_today,
            "atr_14": atr_value,
            "return_1m": rets.get(21),
            "return_3m": rets.get(63),
            "return_6m": rets.get(126),
            "high_20d": n20,
            "sma_200": sma_200,
            "volume_ratio_20d": vol_ratio,
            "bb_upper": float(bbu.iloc[-1]) if not pd.isna(bbu.iloc[-1]) else None,
            "bb_lower": float(bbl.iloc[-1]) if not pd.isna(bbl.iloc[-1]) else None,
            "benchmark_return_3m": bench_3m,
        },
        "subscores": subs,
        "composite_score": round(score, 2),
        "signal_class": cls,
        "conviction": signal_engine.conviction(score),
        "stop_atr": round(stop, 4) if stop is not None else None,
        "history_rows": int(len(df)),
    }


def build_market_snapshot(market: str, session_id: str) -> dict:
    watchlist = load_watchlist(market)
    positions = load_open_positions(market)
    universe = sorted(set(watchlist) | set(positions))
    errors: list[dict] = []

    if not universe:
        return {
            "market": market,
            "session_id": session_id,
            "generated_at": datetime.now(IST).isoformat(),
            "universe_size": 0,
            "watchlist": watchlist,
            "open_positions": positions,
            "tickers": [],
            "data_errors": [{"ticker": None, "error": "empty universe (no watchlist + no open positions)"}],
        }

    bench_df = None
    try:
        bench_df = fetch_benchmark(market, period="1y")
    except DataFeedError as e:
        errors.append({"ticker": f"benchmark_{market}", "error": str(e)})

    vix = fetch_vol_gauge(market)

    # Pass 1: fetch all OHLCV (so we have peer return distributions for momentum subscore)
    per_ticker_df: dict[str, pd.DataFrame] = {}
    for t in universe:
        try:
            df = fetch_ohlcv(t, period="1y")
            per_ticker_df[t] = df
            PRICES_DIR.mkdir(parents=True, exist_ok=True)
            df.to_csv(PRICES_DIR / f"{t}.csv", index=False)
        except Exception as e:
            errors.append({"ticker": t, "error": f"fetch_ohlcv: {type(e).__name__}: {e}"})

    peer_returns_by_period: dict[int, list[float]] = {21: [], 63: [], 126: []}
    for t, df in per_ticker_df.items():
        rets = indicators.returns(df["Close"], periods=(21, 63, 126))
        for p in (21, 63, 126):
            v = rets.get(p)
            if v is not None:
                peer_returns_by_period[p].append(v)

    # Pass 2: compute per-ticker entries
    tickers_out: list[dict] = []
    for t in universe:
        df = per_ticker_df.get(t)
        if df is None:
            continue
        try:
            entry = compute_for_ticker(t, df, peer_returns_by_period, bench_df)
            tickers_out.append(entry)
            SIGNALS_DIR.mkdir(parents=True, exist_ok=True)
            (SIGNALS_DIR / f"{t}_{today_str()}.json").write_text(
                json.dumps(entry, indent=2, default=str)
            )
        except Exception as e:
            errors.append({
                "ticker": t,
                "error": f"compute: {type(e).__name__}: {e}",
                "trace": traceback.format_exc(),
            })

    return {
        "market": market,
        "session_id": session_id,
        "generated_at": datetime.now(IST).isoformat(),
        "universe_size": len(universe),
        "watchlist": watchlist,
        "open_positions": positions,
        "benchmark_symbol": {"US": "SPY", "IN": "^NSEI"}.get(market),
        "vol_gauge_value": vix,
        "tickers": tickers_out,
        "data_errors": errors,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: prefetch.py <SESSION_ID>", file=sys.stderr)
        return 2
    session_id = sys.argv[1].upper()
    markets = SESSION_MARKETS.get(session_id)
    if markets is None:
        print(f"unknown session: {session_id}", file=sys.stderr)
        return 2

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    written: list[str] = []

    for market in markets:
        try:
            snap = build_market_snapshot(market, session_id)
            path = CACHE_DIR / f"snapshot_{market}_{today_str()}_{session_clock()}.json"
            path.write_text(json.dumps(snap, indent=2, default=str))
            written.append(str(path.relative_to(WORKSPACE)))
            err_count = len(snap.get("data_errors", []))
            ok_count = len(snap.get("tickers", []))
            print(f"{market}: wrote {path.name} (tickers={ok_count}, errors={err_count})", file=sys.stderr)
        except Exception as e:
            print(f"{market}: snapshot failed: {type(e).__name__}: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

    for p in written:
        print(p)

    return 0 if written else 1


if __name__ == "__main__":
    sys.exit(main())
