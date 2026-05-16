"""Market data fetching via yfinance. Thin wrapper with retry + ticker mapping.

Mr.B suffixes:
  .US → strip suffix (NVDA.US → NVDA, yfinance expects bare US tickers)
  .NS → keep as-is (RELIANCE.NS, yfinance supports the .NS suffix natively)
"""
from __future__ import annotations

import sys
import time

import pandas as pd
import yfinance as yf


class DataFeedError(Exception):
    pass


BENCHMARKS = {"US": "SPY", "IN": "^NSEI"}
VOL_GAUGES = {"US": "^VIX", "IN": "^INDIAVIX"}


def _yf_symbol(ticker: str) -> str:
    if ticker.endswith(".US"):
        return ticker[:-3]
    return ticker


def fetch_ohlcv(ticker: str, period: str = "1y", retries: int = 3) -> pd.DataFrame:
    sym = _yf_symbol(ticker)
    last_err = None
    for attempt in range(retries):
        try:
            df = yf.Ticker(sym).history(period=period, auto_adjust=False)
            if df.empty:
                raise DataFeedError(f"empty history for {ticker} ({sym})")
            return df.rename_axis("Date").reset_index()
        except DataFeedError:
            raise
        except Exception as e:
            last_err = e
            time.sleep(1.5 ** attempt)
    raise DataFeedError(f"failed to fetch {ticker} after {retries} retries: {last_err}")


def fetch_quote(ticker: str) -> dict:
    """Best-effort current quote. Tries intraday 1m bars, falls back to last daily bar."""
    sym = _yf_symbol(ticker)
    try:
        intraday = yf.Ticker(sym).history(period="1d", interval="1m", auto_adjust=False)
        if not intraday.empty:
            last = intraday.iloc[-1]
            return {
                "last_price": float(last["Close"]),
                "open": float(intraday.iloc[0]["Open"]),
                "high": float(intraday["High"].max()),
                "low": float(intraday["Low"].min()),
                "close": float(last["Close"]),
                "volume": float(intraday["Volume"].sum()),
                "as_of": str(intraday.index[-1]),
                "source": "yfinance-intraday-1m",
            }
    except Exception as e:
        print(f"DEBUG fetch_quote intraday fail for {sym}: {type(e).__name__}: {e}", file=sys.stderr)

    try:
        daily = yf.Ticker(sym).history(period="5d", auto_adjust=False)
        if daily.empty:
            raise DataFeedError(f"no quote available for {ticker}")
        last = daily.iloc[-1]
        return {
            "last_price": float(last["Close"]),
            "open": float(last["Open"]),
            "high": float(last["High"]),
            "low": float(last["Low"]),
            "close": float(last["Close"]),
            "volume": float(last["Volume"]),
            "as_of": str(daily.index[-1]),
            "source": "yfinance-daily-fallback",
        }
    except DataFeedError:
        raise
    except Exception as e:
        raise DataFeedError(f"quote fetch failed for {ticker}: {e}")


def fetch_benchmark(market: str, period: str = "1y", retries: int = 3) -> pd.DataFrame:
    sym = BENCHMARKS.get(market)
    if not sym:
        raise DataFeedError(f"unknown market: {market}")
    last_err = None
    for attempt in range(retries):
        try:
            df = yf.Ticker(sym).history(period=period, auto_adjust=False)
            if df.empty:
                raise DataFeedError(f"empty benchmark history for {market} ({sym})")
            return df.rename_axis("Date").reset_index()
        except DataFeedError:
            raise
        except Exception as e:
            last_err = e
            time.sleep(1.5 ** attempt)
    raise DataFeedError(f"failed to fetch benchmark {market} ({sym}) after {retries} retries: {last_err}")


def fetch_vol_gauge(market: str) -> float | None:
    sym = VOL_GAUGES.get(market)
    if not sym:
        return None
    try:
        df = yf.Ticker(sym).history(period="5d", auto_adjust=False)
        if df.empty:
            return None
        return float(df.iloc[-1]["Close"])
    except Exception:
        return None
