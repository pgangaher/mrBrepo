"""Deterministic signal scoring. Pure functions of indicator inputs.

Locks the rubric from Signals/SignalEngine.md: each component normalized to
0..100, weighted average → composite score in 0..100. Missing components are
dropped and remaining weights re-normalize.
"""
from __future__ import annotations

import numpy as np

WEIGHTS = {
    "momentum_1m":    0.15,
    "momentum_3m":    0.20,
    "momentum_6m":    0.15,
    "rel_strength":   0.15,
    "volume_confirm": 0.10,
    "rsi_zone":       0.10,
    "macd_signal":    0.10,
    "earnings_cat":   0.05,
}


def momentum_subscore(return_value: float | None, peer_returns: list[float]) -> float | None:
    """Cross-sectional percentile rank of return vs peers (0..100)."""
    if return_value is None:
        return None
    peers = [r for r in peer_returns if r is not None]
    if not peers:
        return 50.0
    rank = sum(1 for r in peers if r < return_value)
    return 100.0 * rank / len(peers)


def rel_strength_subscore(ticker_3m: float | None, bench_3m: float | None) -> float | None:
    """100 × (ticker_3m − bench_3m + 0.5) clipped to [0, 100]."""
    if ticker_3m is None or bench_3m is None:
        return None
    raw = (ticker_3m - bench_3m + 0.5) * 100.0
    return float(max(0.0, min(100.0, raw)))


def volume_confirm_subscore(vol_ratio: float | None, price_change: float | None) -> float | None:
    if vol_ratio is None:
        return None
    if vol_ratio >= 1.5 and price_change is not None and price_change > 0:
        return 100.0
    if vol_ratio >= 1.0:
        return 50.0
    return 0.0


def rsi_zone_subscore(rsi_value: float | None) -> float | None:
    """Triangular: peaks at RSI=60. 0 at RSI≤30 or RSI≥85, ramping linearly."""
    if rsi_value is None:
        return None
    if rsi_value <= 30 or rsi_value >= 85:
        return 0.0
    if rsi_value <= 60:
        return 100.0 * (rsi_value - 30) / 30.0
    return 100.0 * (85 - rsi_value) / 25.0


def macd_signal_subscore(hist_today: float | None, hist_prev: float | None) -> float | None:
    if hist_today is None:
        return None
    if hist_today > 0:
        if hist_prev is not None and hist_today > hist_prev:
            return 100.0
        return 50.0
    return 0.0


def earnings_subscore(days_to_earnings: int | None) -> float | None:
    """Peaks at |d|≤5, decays linearly to 0 by |d|≥20."""
    if days_to_earnings is None:
        return None
    d = abs(days_to_earnings)
    if d <= 5:
        return 100.0
    if d >= 20:
        return 0.0
    return 100.0 * (20 - d) / 15.0


def composite(subscores: dict[str, float | None]) -> float:
    total_w = 0.0
    total = 0.0
    for k, w in WEIGHTS.items():
        v = subscores.get(k)
        if v is None:
            continue
        total += v * w
        total_w += w
    if total_w == 0:
        return 0.0
    return total / total_w


def conviction(score: float) -> str:
    if score >= 70:
        return "HIGH"
    if score >= 40:
        return "MEDIUM"
    return "LOW"


def _top_quartile(value, peers):
    if value is None:
        return False
    peers = [p for p in peers if p is not None]
    if not peers:
        return False
    threshold = float(np.percentile(peers, 75))
    return value >= threshold


def classify(
    *,
    composite_score,
    subscores,
    rsi_value,
    close_today,
    n_day_high_20,
    sma_200,
    momentum_3m,
    momentum_6m,
    peer_3m,
    peer_6m,
):
    earnings = subscores.get("earnings_cat")
    if earnings is not None and earnings >= 80 and composite_score >= 55:
        return "EARNINGS_PLAY"

    vol_conf = subscores.get("volume_confirm")
    if (
        close_today is not None
        and n_day_high_20 is not None
        and close_today >= n_day_high_20
        and vol_conf is not None
        and vol_conf >= 50
    ):
        return "BREAKOUT"

    if (
        composite_score >= 60
        and _top_quartile(momentum_3m, peer_3m)
        and _top_quartile(momentum_6m, peer_6m)
    ):
        return "MOMENTUM_LONG"

    if (
        rsi_value is not None
        and rsi_value < 35
        and composite_score >= 50
        and sma_200 is not None
        and close_today is not None
        and close_today > sma_200
    ):
        return "MEAN_REVERSION"

    rs = subscores.get("rel_strength")
    if rs is not None and rs >= 70:
        return "SECTOR_ROTATION"

    return "NO_SIGNAL"


def stop_atr(close_today: float | None, atr_value: float | None, multiplier: float = 1.5) -> float | None:
    """ATR-based stop, floored at 8% loss (entry × 0.92)."""
    if close_today is None or atr_value is None:
        return None
    atr_stop = close_today - multiplier * atr_value
    floor_stop = close_today * 0.92
    return float(max(atr_stop, floor_stop))
