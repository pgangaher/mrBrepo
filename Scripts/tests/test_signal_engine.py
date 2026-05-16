"""Unit tests for Scripts/signal_engine.py — all pure functions, no I/O."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import signal_engine


class TestComposite:
    def test_all_none_returns_zero(self):
        subs = {k: None for k in signal_engine.WEIGHTS}
        assert signal_engine.composite(subs) == 0.0

    def test_all_100_returns_100(self):
        subs = {k: 100.0 for k in signal_engine.WEIGHTS}
        assert abs(signal_engine.composite(subs) - 100.0) < 1e-9

    def test_renormalizes_missing_components(self):
        # Only one component present — result should be that component's score
        subs = {k: None for k in signal_engine.WEIGHTS}
        subs["momentum_3m"] = 80.0
        result = signal_engine.composite(subs)
        assert abs(result - 80.0) < 1e-9

    def test_partial_missing(self):
        subs = {k: 50.0 for k in signal_engine.WEIGHTS}
        subs["earnings_cat"] = None
        result = signal_engine.composite(subs)
        assert abs(result - 50.0) < 1e-9


class TestConviction:
    def test_high_at_70(self):
        assert signal_engine.conviction(70.0) == "HIGH"

    def test_medium_at_40(self):
        assert signal_engine.conviction(40.0) == "MEDIUM"

    def test_low_below_40(self):
        assert signal_engine.conviction(39.9) == "LOW"

    def test_boundary_69(self):
        assert signal_engine.conviction(69.9) == "MEDIUM"


class TestStopAtr:
    def test_none_when_inputs_none(self):
        assert signal_engine.stop_atr(None, 2.0) is None
        assert signal_engine.stop_atr(100.0, None) is None

    def test_floor_at_8_percent(self):
        # ATR so large the ATR-stop would be < 92% of close
        result = signal_engine.stop_atr(100.0, 100.0, multiplier=1.5)
        # floor_stop = 92.0; atr_stop = 100 - 150 = -50 → max is 92.0
        assert result is not None
        assert abs(result - 92.0) < 1e-9

    def test_atr_stop_when_tighter_than_floor(self):
        # ATR-stop = 100 - 1.5*0.5 = 99.25 > floor 92.0
        result = signal_engine.stop_atr(100.0, 0.5, multiplier=1.5)
        assert result is not None
        assert abs(result - 99.25) < 1e-9


class TestMomentumSubscore:
    def test_none_return_value_returns_none(self):
        assert signal_engine.momentum_subscore(None, [0.1, 0.2]) is None

    def test_empty_peers_returns_50(self):
        assert signal_engine.momentum_subscore(0.1, []) == 50.0

    def test_best_in_peers_returns_near_100(self):
        peers = [0.01, 0.02, 0.03, 0.04]
        result = signal_engine.momentum_subscore(0.05, peers)
        assert result == 100.0

    def test_worst_in_peers_returns_0(self):
        peers = [0.02, 0.03, 0.04, 0.05]
        result = signal_engine.momentum_subscore(0.01, peers)
        assert result == 0.0


class TestRsiZoneSubscore:
    def test_none_input_returns_none(self):
        assert signal_engine.rsi_zone_subscore(None) is None

    def test_oversold_returns_zero(self):
        assert signal_engine.rsi_zone_subscore(30.0) == 0.0

    def test_overbought_returns_zero(self):
        assert signal_engine.rsi_zone_subscore(85.0) == 0.0

    def test_peak_at_60(self):
        assert abs(signal_engine.rsi_zone_subscore(60.0) - 100.0) < 1e-9

    def test_midpoint_between_30_and_60(self):
        result = signal_engine.rsi_zone_subscore(45.0)
        assert result is not None
        assert 0 < result < 100


class TestClassify:
    _base = dict(
        composite_score=50.0,
        subscores={k: 50.0 for k in signal_engine.WEIGHTS},
        rsi_value=55.0,
        close_today=100.0,
        n_day_high_20=110.0,
        sma_200=90.0,
        momentum_3m=0.05,
        momentum_6m=0.10,
        peer_3m=[0.01, 0.02, 0.03],
        peer_6m=[0.05, 0.06, 0.07],
    )

    def test_no_signal_baseline(self):
        result = signal_engine.classify(**self._base)
        # With score=50, subscores all 50, no special conditions → NO_SIGNAL or SECTOR_ROTATION
        assert result in ("NO_SIGNAL", "SECTOR_ROTATION", "MOMENTUM_LONG", "BREAKOUT")

    def test_breakout_when_at_20d_high_with_volume(self):
        kwargs = {**self._base}
        kwargs["close_today"] = 110.0  # at 20d high
        kwargs["subscores"] = {**self._base["subscores"], "volume_confirm": 100.0}
        result = signal_engine.classify(**kwargs)
        assert result == "BREAKOUT"

    def test_mean_reversion_conditions(self):
        kwargs = {**self._base}
        kwargs["rsi_value"] = 30.0  # oversold (< 35)
        kwargs["composite_score"] = 55.0
        kwargs["close_today"] = 100.0  # above sma_200=90
        result = signal_engine.classify(**kwargs)
        assert result == "MEAN_REVERSION"
