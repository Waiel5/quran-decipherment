---
id: H-NEW-263
title: Divine-name surah-overlap network
phase: B
status: PASS-STRUCTURE-NO-HUB
date: 2026-04-18
agent: codex
prereg: findings/phase-b-hypotheses/h-new-263-divine-name-surah-network-prereg.md
prereg_sha256: 0aa9d2097bcba6c8b7ffd34cebd4c56645a6b6758fbdf274059c34bfc57f30c7
script: scripts/h_new_263_divine_name_surah_network.py
json: findings/phase-b-hypotheses/csv/h-new-263.json
seed: 20260418
bonferroni_family: h-new-263-divine-name-surah-network
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: "(repo divine-name detections from findings/phase-b-hypotheses/divine-names-by-verse.csv; 114 surahs x 58 attested names binary incidence; weighted projection W=B·Bᵀ with diagonal zeroed; conservative hub graph W>=2; fixed-margin bipartite double-edge-swap null; 300 permutations; 500 accepted swaps/perm)"
verdict: PASS-STRUCTURE-NO-HUB
---

# [[h-new-263-divine-name-surah-network|H-NEW-263]] — Divine-name surah-overlap network

## Headline

Using the repo's existing divine-name table, the surah-level overlap network shows a **non-random global structure** but **no family-wise-significant distinctive hub**.

- **Cell A PASS**: `H = Σ_{i<j} W[i,j]^2 = 17282`, versus null mean `16614.34`, null sd `244.25`, permutation `p = 0.0066445 < 0.025`.
- **Cell B FAIL**: `Z_max = 2.1972`, with `p_exist = 0.0431894 > 0.025`.
- **MW-5 PASS**: synthetic planted-structure positive control passes both structure and hub checks (`p = 0.0082645` for each).

The locked result category therefore stays **PASS-STRUCTURE-NO-HUB**.

## Data and construction

- Source table: `findings/phase-b-hypotheses/divine-names-by-verse.csv`
- Canonical reference list: `data/asma-al-husna.txt`
- Canonical names: 99
- Attested names in the repo table: **58**
- Surah incidence matrix: `114 x 58`, binary by distinct name-presence within each surah
- Weighted surah projection: `W = B·Bᵀ`, diagonal zeroed
- Conservative hub graph: `W >= 2`

## Results

### Cell A — Global structure

The preregistered structure statistic was the weighted-overlap concentration

`H = Σ_{i<j} W[i,j]^2`

with a fixed-margin bipartite swap null preserving both surah repertoire sizes and name popularity.

Observed versus null:

| Statistic | Observed | Null mean | Null sd | p_upper | Decision |
|---|---:|---:|---:|---:|---|
| `H = Σ W²` | **17282** | 16614.34 | 244.25 | **0.0066445** | PASS |

Descriptive network size:

| Quantity | Value |
|---|---:|
| Edges with `W >= 1` | 3603 |
| Edges with `W >= 2` | 1372 |
| Max shared names on a single edge | 10 |

The `W >= 2` graph is not more triangle-dense than null:

- observed transitivity = `0.821518`
- null mean transitivity = `0.823722`
- null sd = `0.008976`

So the Cell A pass is coming from **concentrated high-weight overlap**, not from an unusual excess of binary clustering at the conservative threshold.

### Cell B — Distinctive hub existence

Hubness was tested on the conservative graph with

`S₂[i] = Σ_j W[i,j] * 1[W[i,j] >= 2]`

and surah-specific null-standardized scores

`Z₂[i] = (S₂[i] - mean_null_i) / sd_null_i`.

The preregistered existence statistic was `Z_max = max_i Z₂[i]`.

| Statistic | Observed | p_exist | Decision |
|---|---:|---:|---|
| `Z_max` | **2.1972** | **0.0431894** | FAIL |

Top descriptive hub candidates from the final JSON:

| Rank | Surah | `S₂_obs` | Null mean | Null sd | `Z₂` | `p_raw` | `p_adj_fwer` |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | Q 27 | 232 | 177.76 | 24.69 | **2.1972** | 0.0033223 | **0.0431894** |
| 2 | Q 45 | 147 | 99.15 | 28.20 | 1.6966 | 0.0332226 | 0.7607973 |
| 3 | Q 41 | 194 | 149.12 | 28.44 | 1.5784 | 0.0365449 | 0.9102990 |
| 4 | Q 30 | 204 | 164.61 | 27.62 | 1.4264 | 0.0664452 | 0.9867110 |
| 5 | Q 29 | 205 | 166.34 | 27.83 | 1.3891 | 0.0598007 | 0.9966777 |

Q 27 is the strongest descriptive hub candidate, but its family-wise adjusted `p` remains above the Bonferroni threshold, so **no individual surah is promoted as a distinctive hub**.

Raw conservative-strength leaders are slightly different:

| Rank | Surah | `strength_ge2` | `degree_ge2` |
|---|---:|---:|---:|
| 1 | Q 2 | 282 | 63 |
| 2 | Q 42 | 241 | 58 |
| 3 | Q 5 | 239 | 60 |
| 4 | Q 40 | 239 | 56 |
| 5 | Q 6 | 233 | 57 |

These raw totals are informative descriptively, but the hub cell is governed by null-standardized `Z₂`, not raw size.

## Strongest observed surah pairs

Top overlap edges in the final JSON:

| Rank | Pair | Shared names |
|---|---|---:|
| 1 | Q 2 - Q 3 | **10** |
| 2 | Q 2 - Q 5 | 9 |
| 2 | Q 2 - Q 40 | 9 |
| 2 | Q 5 - Q 6 | 9 |
| 2 | Q 6 - Q 10 | 9 |
| 2 | Q 40 - Q 42 | 9 |

The highest-weight edge in the corpus is therefore **Q 2 with Q 3**, at 10 shared attested divine names.

## MW-5 positive control

The script's synthetic 3-block-plus-hub control passes both preregistered inferential cells:

| Check | p | Result |
|---|---:|---|
| Structure cell on MW-5 | 0.0082645 | PASS |
| Hub cell on MW-5 | 0.0082645 | PASS |

This keeps the observed verdict admissible: the null machinery can recover planted structure and planted hubness when those are present.

## Interpretation

The final JSON supports a narrow conclusion:

1. The surah-level divine-name overlap network is **more concentrated than a fixed-margin randomization would produce**.
2. That concentration does **not** resolve into a Bonferroni-protected hub claim for any one surah.
3. Q 27 is the closest thing to a hub candidate in the final run, but it remains a **descriptive near-miss**, not a promoted finding.

## Honest limits

1. The study uses the repo's existing per-verse divine-name detections and does not rematch raw Quran text.
2. The surah matrix is **binary by distinct repertoire**, not frequency-weighted by token count.
3. Only **58 of the canonical 99 names** are attested in the operative data table.
4. `n_perm = 300` is enough for the present verdict, but Cell B sits in the near-miss zone and could be refined by a larger rerun without changing the current category.
5. The prereg discloses preinspection and the runtime amendment from `1000` to `500` accepted swaps per permutation; the final JSON, prereg, and script are now aligned on the successful `500`-swap run.
