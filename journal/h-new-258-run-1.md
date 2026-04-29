# H-NEW-258 run log 1

## Date

2026-04-18

## Scope

Cross-corpus replication of the Quran `H-NEW-236.1b` preserved-adjacency
scaffold logic on the inherited `H-NEW-147` Bukhari retained-segment
instrument.

## Commands

```bash
python3 -m py_compile scripts/h_new_258_bukhari_mh_replication.py
python3 scripts/h_new_258_bukhari_mh_replication.py
```

## Control

- Recomputed inherited `L_canonical = 108.16400419493601` exactly.
- Recomputed inherited best-of-10 `L_2opt = 90.22845190401614` vs parent
  `90.40959540817704`.
- Both within the pre-registered `0.5` Fisher-Rao-unit tolerance.
- Control PASS.

## Primary result

- `K=0`: OPEN-HIGH
  - sim mean `103.724376`
  - sim 95% CI `[102.302357, 104.998505]`
  - empirical percentile `100.0`
- `K=15`: CLOSED
  - sim mean `107.535164`
  - sim 95% CI `[106.036570, 108.904334]`
  - empirical percentile `78.0`
  - closure vs `K=0` mean-gap: `85.84%`
- `K=30`: CLOSED
  - sim mean `108.693318`
  - empirical percentile `16.0`
- `K=50`: CLOSED
  - sim mean `109.015250`
  - empirical percentile `9.7`
- `K=100`: CLOSED
  - sim mean `108.534028`
  - sim 95% CI `[108.116820, 109.315074]`
  - empirical percentile `8.3`

## Verdict

- `overall_verdict = LOOSE-ANALOGUE`
- `first_closing_k = 15`
- `k100_closes = true`

## Interpretation note

The dense Quran-side `top-100` closure does not replicate at comparable
density on the inherited Bukhari instrument. The Bukhari path-only
analogue exists, but it is already present at `K=15`; heavier K values
close less centrally and increasingly push the simulator above the
empirical canonical path.
