"""Pure-math technical indicators. No I/O, no network. Unit-testable."""
from __future__ import annotations

import numpy as np
import pandas as pd


def rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1.0 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, np.nan)
    return (100.0 - 100.0 / (1.0 + rs)).fillna(50.0)


def macd(
    close: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9
) -> tuple[pd.Series, pd.Series, pd.Series]:
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    hist = macd_line - signal_line
    return macd_line, signal_line, hist


def bbands(
    close: pd.Series, period: int = 20, num_std: float = 2.0
) -> tuple[pd.Series, pd.Series, pd.Series]:
    mid = close.rolling(period).mean()
    std = close.rolling(period).std()
    return mid + num_std * std, mid, mid - num_std * std


def atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat(
        [(high - low).abs(), (high - prev_close).abs(), (low - prev_close).abs()],
        axis=1,
    ).max(axis=1)
    return tr.ewm(alpha=1.0 / period, adjust=False).mean()


def returns(close: pd.Series, periods: tuple[int, ...] = (21, 63, 126)) -> dict[int, float | None]:
    out: dict[int, float | None] = {}
    for p in periods:
        if len(close) > p:
            out[p] = float(close.iloc[-1] / close.iloc[-1 - p] - 1.0)
        else:
            out[p] = None
    return out


def relative_strength(close: pd.Series, bench_close: pd.Series, period: int = 63) -> float | None:
    """Ratio slope: (last / first - 1) of the ticker/benchmark ratio over period."""
    if len(close) < period + 1 or len(bench_close) < period + 1:
        return None
    n = min(len(close), len(bench_close))
    ratio = (close.iloc[-n:].reset_index(drop=True) / bench_close.iloc[-n:].reset_index(drop=True))
    window = ratio.iloc[-period:]
    if window.iloc[0] == 0:
        return None
    return float(window.iloc[-1] / window.iloc[0] - 1.0)


def beta(close: pd.Series, bench_close: pd.Series, period: int = 63) -> float | None:
    if len(close) < period + 1 or len(bench_close) < period + 1:
        return None
    r = close.pct_change().iloc[-period:].dropna().to_numpy()
    rb = bench_close.pct_change().iloc[-period:].dropna().to_numpy()
    n = min(len(r), len(rb))
    if n < 5:
        return None
    cov = np.cov(r[-n:], rb[-n:])
    if cov.shape[0] < 2 or cov[1, 1] == 0:
        return None
    return float(cov[0, 1] / cov[1, 1])


def n_day_high(high: pd.Series, n: int) -> float | None:
    if len(high) < n:
        return None
    return float(high.iloc[-n:].max())


def n_day_low(low: pd.Series, n: int) -> float | None:
    if len(low) < n:
        return None
    return float(low.iloc[-n:].min())


def volume_ratio(volume: pd.Series, period: int = 20) -> float | None:
    if len(volume) < period + 1:
        return None
    mean = volume.iloc[-period - 1:-1].mean()
    if mean == 0:
        return None
    return float(volume.iloc[-1] / mean)


def sma(close: pd.Series, period: int) -> float | None:
    if len(close) < period:
        return None
    return float(close.rolling(period).mean().iloc[-1])
