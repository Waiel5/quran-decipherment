---
id: H-NEW-263
title: Divine-name surah-overlap network
phase: B
status: PRE-REGISTERED 2026-04-18
date: 2026-04-18
agent: codex
seed: 20260418
bonferroni_family: h-new-263-divine-name-surah-network
bonferroni_k: 2
alpha_bon: 0.025
n_perm: 300
n_perm_mw5: 120
accepted_swaps_per_perm: 500
rules_tuple: "(repo divine-name detections from findings/phase-b-hypotheses/divine-names-by-verse.csv; surah x distinct-name binary incidence; attested names only; weighted projection W=B·Bᵀ with diagonal zeroed; fixed-margin bipartite double-edge-swap null; conservative hub graph defined by W>=2)"
disclosure_preinspection: "Quick exploratory probes on the existing divine-name incidence table were used to reject a trivial W>=1 degree graph dominated by Allah-links and to settle on a conservative 2-cell design before final execution. This prereg therefore locks the final executable test, but it is not discovery-pure."
amendment_runtime_2026-04-18: "Initial execution with 1000 accepted swaps per permutation proved too slow to land promptly in this environment. Swap depth was reduced to 500 before the successful run. Null family, statistics, and decision rules were unchanged."
---

# [[h-new-263-divine-name-surah-network|H-NEW-263]] — Divine-name surah-overlap network

## Question

Using the repo's existing divine-name detections, do surahs that share divine-name repertoires form a non-random network once surah-level and name-level margins are held fixed, and do any surahs emerge as genuinely distinctive hubs in that incidence network?

## Data source

- Primary data: `findings/phase-b-hypotheses/divine-names-by-verse.csv`
- Canonical 99-name reference only for denominator/context: `data/asma-al-husna.txt`

The operative dataset is the repo's already-built per-verse divine-name table. I do **not** rematch raw Quran text in this study.

## Locked construction

### Step 1 — Surah x name incidence

Build binary matrix `B[s, n]` where:

- `s` ranges over the 114 surahs
- `n` ranges over the **attested** divine names appearing in `divine-names-by-verse.csv`
- `B[s, n] = 1` iff surah `s` contains at least one verse tagged with divine name `n`

This is a **distinct-name repertoire** matrix, not a token-count matrix. Repetition inside a surah does not increase `B[s, n]`.

### Step 2 — Weighted surah projection

Compute

`W = B · Bᵀ`

with diagonal zeroed. Then `W[i, j]` is the number of distinct divine names shared by surahs `i` and `j`.

### Step 3 — Conservative hub graph

Define binary adjacency

`A₂[i, j] = 1[W[i, j] >= 2]`

This threshold is locked for one reason only: `W >= 1` is too heavily driven by the ubiquitous `Allah` backbone and is therefore not a conservative hub screen. Requiring at least two shared names asks for repertoire overlap beyond a single-name link.

## Null model

Primary null is a **fixed-margin bipartite randomization** of `B`:

- preserve every surah's row-sum exactly
- preserve every name's surah-incidence count exactly
- randomize arrangement by accepted 2x2 double-edge swaps
- `accepted_swaps_per_perm = 500`
- `n_perm = 300`
- seed = `20260418`

This is intentionally conservative: any global structure or hub effect must survive after controlling both for "name-rich surahs" and for "popular names."

## Inferential cells

### Cell A — Global network structure

Statistic:

`H = Σ_{i<j} W[i, j]^2`

This is the projection-weight concentration statistic. Under fixed row/column margins, total overlap mass `Σ_{i<j} W[i, j]` is largely constrained by column sizes, but `Σ W^2` increases when overlap is concentrated into repeated surah-surah channels rather than spread diffusely.

Direction:

- one-sided upper tail: `H_obs > H_null`

Decision:

- PASS if permutation `p < alpha_bon = 0.025`

### Cell B — Distinctive hub existence

Hub strength is measured on the conservative graph:

`S₂[i] = Σ_j W[i, j] * 1[W[i, j] >= 2]`

For each surah `i`, compute

`Z₂[i] = (S₂[i] - mean_null_i) / sd_null_i`

using the same permutation family.

Existence statistic:

`Z_max = max_i Z₂[i]`

Calibrate `Z_max` against the permutation distribution of `max_i Z₂_null[i]`.

Decision:

- PASS if `p(Z_max_null >= Z_max_obs) < alpha_bon = 0.025`
- If Cell B fails, **no individual surah is promoted as a distinctive hub**
- If Cell B passes, individual hub promotions use the same max-null distribution for family-wise adjusted `p_adj`

## Bonferroni family

| Cell | Claim | Test | Direction | Alpha |
|---|---|---|---|---:|
| A | network structure is non-random | `H = Σ W²` permutation test | upper tail | 0.025 |
| B | at least one distinctive hub exists | `Z_max` permutation test | upper tail | 0.025 |

Family size `k = 2`, so `alpha_bon = 0.05 / 2 = 0.025`.

## MW-5 positive control

Before interpreting the observed corpus:

- build a synthetic `114 x N_name` incidence matrix with 3 planted surah blocks and 1 planted cross-block hub
- run the same Cell A and Cell B machinery on that synthetic matrix
- expected:
  - Cell A PASS strongly
  - Cell B PASS strongly

If the MW-5 control fails, the observed run is treated as **PIPELINE-BROKEN** and no substantive verdict is promoted.

## Decision matrix

| Cell A | Cell B | Final verdict |
|---|---|---|
| PASS | PASS | PASS-STRUCTURE-AND-HUB |
| PASS | FAIL | PASS-STRUCTURE-NO-HUB |
| FAIL | PASS | HUB-ONLY |
| FAIL | FAIL | NULL |

MW-5 failure overrides all four and forces `PIPELINE-BROKEN`.

## Garden of forking paths

Locked choices before final execution:

1. Use the repo's existing `divine-names-by-verse.csv` instead of re-parsing Arabic text.
2. Use binary surah-repertoire incidence rather than within-surah token counts.
3. Use the full weighted projection `W` for Cell A rather than thresholding away information.
4. Use `W >= 2` only for hub screening, because `W >= 1` is dominated by the ubiquitous single-name backbone.
5. Use fixed-margin double-edge swaps as the sole observed-data null.
6. Use `Σ W²` as the structure statistic, not raw edge count or raw density.
7. Use `Z_max` over surah-specific null-standardized `S₂` as the hub-existence statistic, not post-hoc cherry-picking of a single surah.
8. All observed descriptive rankings are reported regardless of inferential outcome.

## Deliverables

- Script: `scripts/h_new_263_divine_name_surah_network.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-263.json`
- Findings: `findings/phase-b-hypotheses/h-new-263-divine-name-surah-network.md`
- Journal: `journal/h-new-263-run-1.md`
