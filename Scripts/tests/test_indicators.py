"""Unit tests for Scripts/indicators.py — all pure functions, no I/O."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import indicators


def flat_series(n: int, value: float = 100.0) -> pd.Series:
    return pd.Series([value] * n, dtype=float)


def rising_series(n: int, start: float = 100.0, step: float = 1.0) -> pd.Series:
    return pd.Series([start + i * step for i in range(n)], dtype=float)


class TestRsi:
    def test_flat_series_converges_to_50(self):
        result = indicators.rsi(flat_series(100))
        assert abs(result.iloc[-1] - 50.0) < 1.0

    def test_declining_series_below_50(self):
        # Losing series: occasional small up ticks, but strong downtrend
        # RSI should land below 50 at the end
        prices = [100.0 - i * 0.6 + (0.1 if i % 5 == 0 else 0) for i in range(80)]
        result = indicators.rsi(pd.Series(prices, dtype=float))
        assert result.iloc[-1] < 50.0

    def test_length_preserved(self):
        s = flat_series(30)
        assert len(indicators.rsi(s)) == len(s)


class TestMacd:
    def test_returns_three_series(self):
        s = rising_series(60)
        macd_line, signal_line, hist = indicators.macd(s)
        assert len(macd_line) == len(s)
        assert len(signal_line) == len(s)
        assert len(hist) == len(s)

    def test_hist_is_macd_minus_signal(self):
        s = rising_series(60)
        macd_line, signal_line, hist = indicators.macd(s)
        pd.testing.assert_series_equal(hist, macd_line - signal_line)


class TestReturns:
    def test_correct_calculation(self):
        # 21 bars: price goes from 100 to 110 → return = 0.10
        prices = [100.0] * 21 + [110.0]
        s = pd.Series(prices)
        result = indicators.returns(s, periods=(21,))
        assert abs(result[21] - 0.10) < 1e-9

    def test_insufficient_data_returns_none(self):
        s = pd.Series([100.0] * 10)
        result = indicators.returns(s, periods=(21, 63))
        assert result[21] is None
        assert result[63] is None

    def test_all_periods_returned(self):
        s = flat_series(200)
        result = indicators.returns(s, periods=(21, 63, 126))
        assert set(result.keys()) == {21, 63, 126}


class TestVolumeRatio:
    def test_none_when_insufficient_data(self):
        assert indicators.volume_ratio(pd.Series([1000.0] * 5)) is None

    def test_ratio_of_1_on_flat_volume(self):
        s = pd.Series([1000.0] * 25)
        result = indicators.volume_ratio(s)
        assert result is not None
        assert abs(result - 1.0) < 1e-9

    def test_high_volume_day_above_1(self):
        base = [1000.0] * 21
        s = pd.Series(base + [5000.0])
        result = indicators.volume_ratio(s)
        assert result is not None
        assert result > 1.0


class TestSma:
    def test_none_when_insufficient(self):
        assert indicators.sma(flat_series(10), 200) is None

    def test_sma_flat_series_equals_value(self):
        result = indicators.sma(flat_series(250, value=42.0), 200)
        assert abs(result - 42.0) < 1e-9


class TestNDayHigh:
    def test_none_when_insufficient(self):
        assert indicators.n_day_high(flat_series(5), 20) is None

    def test_returns_max(self):
        highs = pd.Series([float(i) for i in range(30)])
        assert indicators.n_day_high(highs, 20) == 29.0


class TestAtr:
    def test_returns_series_same_length(self):
        n = 30
        s = flat_series(n)
        result = indicators.atr(s, s, s)
        assert len(result) == n

    def test_zero_atr_on_flat_series(self):
        s = flat_series(30)
        result = indicators.atr(s, s, s)
        assert abs(result.iloc[-1]) < 1e-6
