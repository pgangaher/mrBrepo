// Mr.B paper-trade dashboard data.
//
// This file is rebuilt by the scheduler at every IN_CLOSE, US_CLOSE,
// WEEKEND_REVIEW, and MONTH_END session. It is the single allowed overwrite
// target (the underlying history lives in Portfolio/state/, Logs/daily_pnl_*,
// and Logs/Recommendations_* — all append-only).
//
// Until the first close session fires, this file is the placeholder below and
// the dashboard renders a "No data yet" panel.

window.DATA = null;
