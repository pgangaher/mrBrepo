// Mr.B paper-trade dashboard data.
//
// This file is rebuilt by the scheduler at every IN_CLOSE, US_CLOSE,
// WEEKEND_REVIEW, and MONTH_END session. It is the single allowed overwrite
// target (the underlying history lives in Portfolio/state/, Logs/daily_pnl_*,
// and Logs/Recommendations_* — all append-only).
//
// Last updated: 2026-05-16T10:00:00+05:30 (WEEKEND_REVIEW — Week 20)
// US price source: yfinance-intraday-1m — Scripts/cache/snapshot_US_2026-05-16_013028.json (US_CLOSE 2026-05-15)
// IN price source: yfinance EOD bar — Scripts/cache/snapshot_IN_2026-05-15_153033.json (IN_CLOSE 2026-05-15)

window.DATA = {
  updated_at: "2026-05-16T10:00:00+05:30",
  session: "WEEKEND_REVIEW",
  week: "2026-W20",
  strategy_start: "2026-05-14",
  strategy_end: "2026-06-13",

  week_summary: {
    week_number: "W20",
    week_start: "2026-05-11",
    week_end: "2026-05-17",
    trading_days_active: 2,
    phase_entering_next_week: "Phase 2 — Conviction Deployment (Week 2 of 4)",
    next_monday_priority: "NVDA.US CRITICAL stop check at US_OPEN. ADANIENT.NS RSI check at IN_OPEN. AMD.US Phase 2 five-layer. NVDA earnings triple-check May 21.",
    framework_amendments_this_week: 1,
    amendment_summary: "IN IT sector (TCS/INFY/HCLTECH/WIPRO/TECHM) formally downgraded to AVOID until cohort RSI >50 and MACD bullish on 3 of 5 names."
  },

  markets: {
    IN: {
      label: "India (NSE)",
      currency: "INR",
      currency_symbol: "₹",
      starting_nav: 1000000,
      current_nav: 998190,
      week_pnl: -1810.50,
      week_pnl_pct: -0.18,
      todays_pnl: -1810,
      todays_pnl_pct: -0.18,
      total_return_pct: -0.18,
      peak_nav: 1000000,
      drawdown_pct: 0.18,
      benchmark: "NIFTY 50",
      benchmark_return_3m_pct: -8.53,
      benchmark_return_since_start_pct: null,
      alpha_pct: null,
      phase: "Phase 2 — Conviction Deployment (begins 2026-05-18)",
      deployed_pct: 21.9,
      cash_pct: 78.1,
      india_vix: 18.80,
      defensive_mode: false,
      stop_trail_actions_this_week: 0,
      nav_history: [
        { date: "2026-05-14", nav: 1000000, benchmark_rebased: 1000000, session: "baseline" },
        { date: "2026-05-15", nav: 998190, benchmark_rebased: null, session: "IN_CLOSE" }
      ],
      open_positions: [
        {
          ticker: "ONGC.NS",
          company: "Oil & Natural Gas Corp Ltd",
          sector: "Energy",
          shares: 332,
          entry_price: 301.15,
          entry_date: "2026-05-15",
          current_price: 299.50,
          unrealized_pnl: -548,
          unrealized_pnl_pct: -0.55,
          stop: 290.09,
          stop_status: "SAFE",
          stop_buffer_pct: 3.14,
          target1: 320.00,
          target2: 340.00,
          conviction: "HIGH",
          signal_score: 74.86,
          notional_cost: 99982,
          current_value: 99434,
          pct_nav: 10.0,
          add_on_plan: "Add-on in Phase 2 if RSI cools below 67; earnings catalyst late May/early June"
        },
        {
          ticker: "ADANIPORTS.NS",
          company: "Adani Ports & SEZ Ltd",
          sector: "Industrials",
          shares: 33,
          entry_price: 1807.90,
          entry_date: "2026-05-15",
          current_price: 1792.00,
          unrealized_pnl: -525,
          unrealized_pnl_pct: -0.88,
          stop: 1730.71,
          stop_status: "SAFE",
          stop_buffer_pct: 3.42,
          target1: 1950.00,
          target2: 2100.00,
          conviction: "HIGH*",
          signal_score: 78.59,
          notional_cost: 59661,
          current_value: 59136,
          pct_nav: 6.0,
          add_on_plan: "Add 22 shares if RSI < 67 — takes position from ₹59,661 to ~₹99,000 (10% NAV)"
        },
        {
          ticker: "HINDALCO.NS",
          company: "Hindalco Industries Ltd",
          sector: "Metals",
          shares: 55,
          entry_price: 1080.50,
          entry_date: "2026-05-15",
          current_price: 1067.10,
          unrealized_pnl: -737,
          unrealized_pnl_pct: -1.24,
          stop: 1038.40,
          stop_status: "SAFE",
          stop_buffer_pct: 2.69,
          target1: 1160.00,
          target2: 1220.00,
          conviction: "MEDIUM",
          signal_score: 65.90,
          notional_cost: 59428,
          current_value: 58691,
          pct_nav: 5.9
        }
      ],
      watchlist_priority: [
        { ticker: "ADANIENT.NS", score: 87.07, rsi: 75.6, signal: "MOMENTUM_LONG HIGH", gate: "RSI < 70 AND price ≥ ₹2,700 → five-layer" },
        { ticker: "SUNPHARMA.NS", score: 69.37, rsi: 64.9, signal: "MOMENTUM_LONG MEDIUM", gate: "Full five-layer at IN_OPEN May 18" },
        { ticker: "COALINDIA.NS", score: null, rsi: null, signal: "Phase 2 candidate", gate: "RSI push above 55" }
      ]
    },

    US: {
      label: "United States (NASDAQ/NYSE)",
      currency: "USD",
      currency_symbol: "$",
      starting_nav: 10000,
      current_nav: 9933.32,
      week_pnl: -66.68,
      week_pnl_pct: -0.67,
      todays_pnl: -66.68,
      todays_pnl_pct: -0.67,
      total_return_pct: -0.67,
      peak_nav: 10000,
      drawdown_pct: 0.67,
      benchmark: "SPY",
      benchmark_return_3m_pct: 8.43,
      benchmark_return_since_start_pct: null,
      alpha_pct: null,
      phase: "Phase 2 — Conviction Deployment (begins 2026-05-18)",
      deployed_pct: 24.0,
      cash_pct: 76.0,
      vix: 18.13,
      defensive_mode: false,
      stop_trail_actions_this_week: 0,
      nav_history: [
        { date: "2026-05-14", nav: 10000, benchmark_rebased: 10000, session: "baseline" },
        { date: "2026-05-15", nav: 9933.32, benchmark_rebased: null, session: "US_CLOSE" }
      ],
      open_positions: [
        {
          ticker: "NVDA.US",
          company: "NVIDIA Corporation",
          sector: "IT/Semiconductors",
          shares: 4.24,
          entry_price: 235.74,
          entry_date: "2026-05-15",
          current_price: 225.30,
          unrealized_pnl: -44.27,
          unrealized_pnl_pct: -4.43,
          stop: 224.98,
          stop_status: "CRITICAL",
          stop_buffer_pct: 0.14,
          target1: 255.00,
          target2: 270.00,
          conviction: "HIGH",
          signal_score: 67.10,
          notional_cost: 1000.00,
          current_value: 955.27,
          pct_nav: 9.6,
          stop_watch: "CRITICAL — $0.32 / 0.14% above stop; intraday breach 2 consecutive days. Next session: if open or close < $224.98 → PAPER CLOSE.",
          earnings_watch: "~2026-05-28 — triple-check May 21 (ResearchAnalyst + SignalEngine + SentimentMonitor)"
        },
        {
          ticker: "CAT.US",
          company: "Caterpillar Inc",
          sector: "Industrials",
          shares: 0.65,
          entry_price: 919.98,
          entry_date: "2026-05-15",
          current_price: 888.74,
          unrealized_pnl: -20.31,
          unrealized_pnl_pct: -3.40,
          stop: 878.37,
          stop_status: "ELEVATED",
          stop_buffer_pct: 1.17,
          target1: 982.00,
          target2: 1030.00,
          conviction: "MEDIUM",
          signal_score: 64.68,
          notional_cost: 597.99,
          current_value: 577.68,
          pct_nav: 5.8,
          stop_watch: "ELEVATED — $10.37 / 1.17% above stop. Monitor at US_OPEN May 18."
        },
        {
          ticker: "GOOGL.US",
          company: "Alphabet Inc (Class A)",
          sector: "IT/Tech (Internet)",
          shares: 2.01,
          entry_price: 397.28,
          entry_date: "2026-05-15",
          current_price: 396.46,
          unrealized_pnl: -1.65,
          unrealized_pnl_pct: -0.21,
          stop: 386.30,
          stop_status: "SAFE",
          stop_buffer_pct: 2.56,
          target1: 419.24,
          target2: 441.20,
          conviction: "MEDIUM",
          signal_score: 70.04,
          notional_cost: 798.53,
          current_value: 796.88,
          pct_nav: 8.0
        }
      ],
      watchlist_priority: [
        { ticker: "AMD.US", score: 80.09, rsi: 67.29, signal: "MOMENTUM_LONG HIGH", close: 424.16, gate: "Phase 2 — evaluate with wider stop latitude; ATR stop was 8.01% at close" },
        { ticker: "CSCO.US", score: 81.38, rsi: 88.47, signal: "MOMENTUM_LONG HIGH", close: 118.12, gate: "RSI must cool below 75; stop 4.44% qualifies mechanically" },
        { ticker: "AVGO.US", score: 64.40, rsi: 58.61, signal: "MOMENTUM_LONG MEDIUM", close: 425.46, gate: "Post-Q2 earnings entry (early June)" },
        { ticker: "SBUX.US", score: 64.23, rsi: 65.49, signal: "MOMENTUM_LONG MEDIUM", close: 106.81, gate: "Phase 2 — Consumer Staples evaluate" },
        { ticker: "UNH.US", score: 66.48, rsi: 76.52, signal: "SECTOR_ROTATION MEDIUM", close: 393.60, gate: "Phase 2 — Healthcare evaluate; RSI elevated" }
      ]
    }
  },

  weekly_stats: {
    "2026-W20": {
      us_week_pnl: -66.68,
      us_week_pnl_pct: -0.67,
      in_week_pnl_inr: -1810.50,
      in_week_pnl_pct: -0.18,
      trades_opened: 6,
      trades_closed: 0,
      stops_hit: 0,
      targets_hit: 0,
      no_trade_correct: 4,
      stop_trail_updates: 0,
      framework_amendments: 1
    }
  },

  recent_recommendations: [
    {
      timestamp: "2026-05-16T10:00:00+05:30",
      ticker: "ALL_POSITIONS",
      market: "BOTH",
      verdict: "BULLISH",
      action: "HOLD",
      conviction: "HIGH",
      reasoning_one_line: "Weekend stop-trail review: no unrealized gains on any position — all stops maintained. NVDA CRITICAL watch for Mon open."
    },
    {
      timestamp: "2026-05-16T01:30:00+05:30",
      ticker: "NVDA.US",
      market: "US",
      verdict: "BULLISH",
      action: "HOLD",
      conviction: "HIGH",
      reasoning_one_line: "CRITICAL: close $225.30 only $0.32 above stop $224.98. Intraday breach day 2. Thesis intact — next session immediate review."
    },
    {
      timestamp: "2026-05-16T01:30:00+05:30",
      ticker: "CAT.US",
      market: "US",
      verdict: "BULLISH",
      action: "HOLD",
      conviction: "MEDIUM",
      reasoning_one_line: "ELEVATED: $10.37 above stop. Consolidating after +21% 3m run. Stop $878.37 maintained."
    },
    {
      timestamp: "2026-05-16T01:30:00+05:30",
      ticker: "GOOGL.US",
      market: "US",
      verdict: "BULLISH",
      action: "HOLD",
      conviction: "MEDIUM",
      reasoning_one_line: "Stable at −0.21% from entry. Best risk-adjusted US position. Stop $386.30, buffer 2.56%."
    },
    {
      timestamp: "2026-05-15T22:05:00+05:30",
      ticker: "AMD.US",
      market: "US",
      verdict: "BULLISH",
      action: "NO-TRADE",
      conviction: "HIGH",
      reasoning_one_line: "Stop ATR 8.01% (close $424.16) — Phase 1 ≤5% rule violated 3rd consecutive session. Phase 2 window: May 18+."
    },
    {
      timestamp: "2026-05-15T19:15:00+05:30",
      ticker: "GOOGL.US",
      market: "US",
      verdict: "BULLISH",
      action: "BUY",
      conviction: "MEDIUM",
      reasoning_one_line: "Search + Cloud moat. Score 68.14. Stop 2.76%. Clean five-layer pass. Executed at $397.28."
    },
    {
      timestamp: "2026-05-15T13:00:00+05:30",
      ticker: "NVDA.US",
      market: "US",
      verdict: "BULLISH",
      action: "BUY",
      conviction: "HIGH",
      reasoning_one_line: "AI GPU dominance, CUDA moat. Score 74.1. Earnings watch May 28. Executed at $235.74."
    },
    {
      timestamp: "2026-05-15T13:00:00+05:30",
      ticker: "CAT.US",
      market: "US",
      verdict: "BULLISH",
      action: "BUY",
      conviction: "MEDIUM",
      reasoning_one_line: "Infrastructure + AI data center construction. Score 69.7. Stop 4.52%. Executed at $919.98."
    },
    {
      timestamp: "2026-05-15T12:45:00+05:30",
      ticker: "ONGC.NS",
      market: "IN",
      verdict: "BULLISH",
      action: "BUY",
      conviction: "HIGH",
      reasoning_one_line: "Deep-value E&P, P/E ~8x. Score 74.86. RSI 62.8. Cleanest Phase 1 setup. Executed at ₹301.15."
    },
    {
      timestamp: "2026-05-15T12:45:00+05:30",
      ticker: "ADANIPORTS.NS",
      market: "IN",
      verdict: "BULLISH",
      action: "BUY",
      conviction: "HIGH",
      reasoning_one_line: "India's largest port operator. Score 78.59. RSI 70.6 — position haircut to 6%. Executed at ₹1,807.90."
    },
    {
      timestamp: "2026-05-15T12:45:00+05:30",
      ticker: "HINDALCO.NS",
      market: "IN",
      verdict: "BULLISH",
      action: "BUY",
      conviction: "MEDIUM",
      reasoning_one_line: "Novelis EV tailwind, metals diversification. Score 65.9. RSI 61.4. Executed at ₹1,080.50."
    }
  ]
};
