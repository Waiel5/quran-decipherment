---
id: H-NEW-283
title: Divine-name surah max-edge under fixed-margin null
phase: B
status: MAX-EDGE-NO-PASS
date: 2026-04-18
agent: codex
parent_hypothesis: H-NEW-263
follow_up: H-NEW-276
prereg: findings/phase-b-hypotheses/h-new-283-divine-name-max-edge-prereg.md
prereg_sha256: c189e547921bd400e8cca72713da2c8397b9f413e5478cca5ad630f2c2293bdc
script: scripts/h_new_283_divine_name_max_edge.py
json: findings/phase-b-hypotheses/csv/h-new-283.json
seed: 20260694
alpha: 0.025
n_perm: 10000
accepted_swaps_per_perm: 500
verdict: MAX-EDGE-NO-PASS
---

# [[h-new-283-divine-name-max-edge|H-NEW-283]] — Divine-name surah max-edge under fixed-margin null

## Headline

The strongest observed pairwise overlap in the divine-name surah network is
`M = 10`, achieved uniquely by `Q 2 ↔ Q 3`, but the corpus-level max-edge is
not unusual under the same fixed-margin swap null used in [[h-new-263-divine-name-surah-network|H-NEW-263]]/H-NEW-276.

- Observed `M_obs = 10`
- Null mean `= 9.7615`
- Null sd `= 0.8430`
- `p_adj = P_null(M >= M_obs) = 0.600040`
- Decision at `alpha = 0.025`: **FAIL**

So the max-edge result is descriptive, not inferentially strong.

## Data and construction

- Source table: `findings/phase-b-hypotheses/divine-names-by-verse.csv`
- Same binary surah x attested-name matrix as [[h-new-263-divine-name-surah-network|H-NEW-263]]/H-NEW-276
- Same weighted projection `W = B·Bᵀ` with diagonal zeroed
- Same fixed-margin bipartite double-edge-swap null family
- Same swap depth: `500` accepted swaps per permutation
- Same seed: `20260694`

The inferential object was the corpus-level maximum shared-name edge:

`M = max_{i<j} shared_names(i,j)`

This is the adjusted statistic; the p-value is the upper-tail permutation
probability of that max under the null.

## Results

| Quantity | Value |
|---|---:|
| `M_obs` | **10** |
| `M_null_mean` | 9.7615 |
| `M_null_sd` | 0.8430 |
| `M_p_upper` | **0.600040** |
| `M_ge_count` | 6000 / 10000 |
| `mc_se_p_M` | 0.004899 |

Top observed edges:

| Pair | Shared names |
|---|---:|
| `Q 2 - Q 3` | **10** |
| `Q 2 - Q 5` | 9 |
| `Q 2 - Q 40` | 9 |
| `Q 5 - Q 6` | 9 |
| `Q 6 - Q 10` | 9 |
| `Q 40 - Q 42` | 9 |

`Q 2 ↔ Q 3` is the unique max-edge achiever, but it is not null-extreme at
the family level.

## MW-5 positive control

The cheap parent-line control was retained, but retargeted to the new max-edge
statistic with a synthetic planted-pair matrix.

| Check | Value | Result |
|---|---:|---|
| Control `M_obs` | 20 | PASS |
| Control `M_p_upper` | 0.0082645 | PASS |

This confirms the pipeline can recover a planted max-edge when one is present.

## Interpretation

The divine-name network does contain a clear strongest pair, namely Q 2 and
Q 3, but the fixed-margin null says that a max edge of 10 is ordinary in this
matrix family.

That means the [[h-new-263-divine-name-surah-network|H-NEW-263]]/H-NEW-276 story remains unchanged:

1. There is real structure in the network.
2. There is no corpus-level max-edge anomaly strong enough to clear the
   inherited `0.025` threshold.
3. The Q 2/Q 3 edge is descriptive only.

## Honest limits

1. The study uses the repo's existing per-verse divine-name detections and the
   attested-name subset already encoded in the source CSV.
2. The max-edge test is intentionally conservative because it asks for the
   strongest pair in the whole network, not a targeted pairwise comparison.
3. A larger permutation count would sharpen the Monte Carlo error bars, but it
   is not likely to change the verdict materially.

