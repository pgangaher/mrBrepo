# SignalEngine — US Watchlist Score
## Date: 2026-05-15 | Session: US_CLOSE (May 14 close) | Market: US (NASDAQ/NYSE)
## Snapshot: Scripts/cache/snapshot_US_2026-05-15_0130.json

---

## Ranked Universe (50 names, sorted by composite score)

| Rank | Ticker | Score | Class | Conv | RSI | 1m Ret | 3m Ret | ATR Stop | Stop% |
|---|---|---|---|---|---|---|---|---|---|
| 1 | CSCO.US | 86.2 | MOMENTUM_LONG | HIGH | 87.5 | +40.3% | +54.1% | $110.32 | −4.5% |
| 2 | AMD.US | 76.1 | MOMENTUM_LONG | HIGH | 76.8 | +74.4% | +118.6% | $415.80 | −7.8% |
| 3 | NVDA.US | 74.1 | MOMENTUM_LONG | HIGH | 76.7 | +18.5% | +26.1% | $224.98 | −4.6% |
| 4 | CAT.US | 69.7 | MOMENTUM_LONG | MEDIUM | 66.4 | +19.4% | +21.3% | $878.37 | −4.5% |
| 5 | GOOGL.US | 67.8 | MOMENTUM_LONG | MEDIUM | 74.2 | — | — | — | — |
| 6 | UNH.US | 65.4 | MOMENTUM_LONG | MEDIUM | 83.1 | — | — | — | — |
| 7 | LIN.US | 64.7 | NO_SIGNAL | MEDIUM | 58.1 | — | — | — | — |
| 8 | AVGO.US | 64.0 | MOMENTUM_LONG | MEDIUM | 66.1 | — | — | — | — |
| 9 | GS.US | 63.8 | NO_SIGNAL | MEDIUM | 66.1 | — | — | — | — |
| 10 | SBUX.US | 62.0 | MOMENTUM_LONG | MEDIUM | 64.6 | +8.2% | +10.0% | $102.46 | −3.7% |
| 11 | FCX.US | 61.5 | NO_SIGNAL | MEDIUM | 58.7 | — | — | — | — |
| 12 | WMT.US | 61.1 | NO_SIGNAL | MEDIUM | 60.1 | — | — | — | — |
| 13 | COST.US | 59.9 | NO_SIGNAL | MEDIUM | 63.3 | — | — | — | — |
| 14 | AMZN.US | 59.6 | SECTOR_ROTATION | MEDIUM | 62.9 | — | — | — | — |
| 15 | XOM.US | 58.8 | NO_SIGNAL | MEDIUM | 51.8 | — | — | — | — |

---

## Phase 1 Decisions

### EXECUTE:
| Ticker | Score | Entry | Stop | Size | Rationale |
|---|---|---|---|---|---|
| **NVDA.US** | 74.1 | $235.74 | $224.98 | 10% = $1,000 | Stop 4.6% ≤5% ✓; AI thesis dominant |
| **CAT.US** | 69.7 | $919.98 | $878.37 | 6% = $600 | Stop 4.5% ≤5% ✓; infrastructure theme |

### WATCH (blockers):
| Ticker | Score | Blocker | Action |
|---|---|---|---|
| CSCO.US | 86.2 | RSI 87.5 — dangerously overbought | Wait for RSI pullback <75 |
| AMD.US | 76.1 | ATR stop 7.8% > Phase 1 ≤5% limit | RiskManager REJECTED; revisit if stop tightens |
| GOOGL.US | 67.8 | RSI 74.2 — elevated | Wait for entry at lower RSI |

---

*SignalEngine sub-agent | Benchmark: SPY 3m = +9.80% | VIX: 17.30*
