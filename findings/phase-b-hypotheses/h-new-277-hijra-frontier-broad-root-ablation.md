---
id: H-NEW-277
title: "Hijra lexical frontier broad-root ablation"
status: PASS-DIRECTED — 3/3 Bonferroni cells still pass after removing the 5 broadest mass-shift roots
date: 2026-04-18
parent: H-NEW-267
prereg: findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation-prereg.md
script: scripts/h_new_277_hijra_frontier_broad_root_ablation.py
json: findings/phase-b-hypotheses/csv/h-new-277.json
journal: journal/h-new-277-run-1.md
seed: 20260418
n_perm: 3000
mw5_n_perm: 1000
bonferroni_k: 3
alpha_bon: 0.0166667
rules_tuple: "(H-NEW-267 scorer + split rule + nulls, but with fixed exclusion of {Alh, Amn, qwl, rbb, Ayy} from the root space)"
---

# [[h-new-277-hijra-frontier-broad-root-ablation|H-NEW-277]] — Hijra lexical frontier broad-root ablation

## Headline

The [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] Hijra lexical frontier is **not reducible** to the five
obvious broad mass-shift roots

- `Alh`
- `Amn`
- `qwl`
- `rbb`
- `Ayy`

Those five roots account for **5,264 rooted tokens** in the parent
Late-Meccan/Medinan pool, yet after removing them the same three locked
frontier cells still pass:

- train A -> test B AUC stays at **1.000**
- train B -> test A AUC stays at **1.000**
- split-weight rho stays high at **0.452**

MW-5 also remains alive. The correct reading is therefore:

**the Hijra lexical frontier is broad-root-robust, not just a handful of
common-root movers in disguise.**

## Frozen ablation set

The excluded roots were frozen from [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]'s published descriptive
`top_abs_delta_mean_density` table:

- `Alh`
- `Amn`
- `qwl`
- `rbb`
- `Ayy`

No alternative ablation family was tested.

## Primary results

### Bonferroni family (`k = 3`, `alpha_bon = 0.0166667`)

| Cell | Observed | Null mean | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---:|---|
| Train A -> test B AUC | **1.000000** | 0.510225 | 0.700000 | **0.000333** | **PASS** |
| Train B -> test A AUC | **1.000000** | 0.508750 | 0.696970 | **0.000333** | **PASS** |
| Split-weight Spearman rho | **0.452289** | -0.038090 | 0.103089 | **0.000333** | **PASS** |

Overall verdict: **PASS-DIRECTED**.

### What changed relative to [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]

The frontier weakens only slightly:

- AUC_A->B: **1.000000 -> 1.000000** (no change)
- AUC_B->A: **1.000000 -> 1.000000** (no change)
- split-weight rho: **0.457673 -> 0.452289**
- held-out score gap A->B: **0.105421 -> 0.072133**
- held-out score gap B->A: **0.090290 -> 0.083068**
- support roots: **434 -> 429**

So the ablation trims the margin, but it does not alter the basic
geometry of the split. The two held-out sides still remain cleanly
separated.

## MW-5 positive control

The same ablated root space was applied to the broader Meccan vs
Medinan control.

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Train A -> test B AUC | **0.897010** | 0.659551 | **0.000999** | **PASS** |
| Train B -> test A AUC | **0.855482** | 0.667774 | **0.000999** | **PASS** |
| Split-weight Spearman rho | **0.509789** | 0.092749 | **0.000999** | **PASS** |

MW-5 therefore stays fully alive. The surviving primary result is
interpretable.

## Interpretation

[[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] already showed the Hijra boundary is a real lexical frontier.
[[h-new-277-hijra-frontier-broad-root-ablation|H-NEW-277]] sharpens that result mechanistically:

- the frontier is **not** only `Alh` and `Amn` rising
- it is **not** only `qwl`, `rbb`, and `Ayy` falling
- once those broad high-mass roots are removed, the same held-out split
  still separates perfectly in both directions

That means the frontier is being carried by a wider band of roots,
including the sharper stable markers already highlighted in [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]
such as `nfq`, `qtl`, `nsw`, `mwl`, `wHy`, `fry`, and `jrm`.

The broad roots matter. They just do **not** exhaust the signal.

## Honest limits

- This tests one fixed ablation family only.
- The excluded roots were chosen from the parent's published descriptive
  table, so this is a mechanistic child test, not an independent blind
  discovery.
- Surah remains the unit; passage-level frontier structure could behave
  differently.
- A surviving ablation does not make the remaining roots equally
  important. It only shows the frontier is not reducible to these five.

## Bottom line

`[[h-new-277-hijra-frontier-broad-root-ablation|H-NEW-277]]` lands as **PASS-DIRECTED**.

After removing the five broadest absolute density-shift roots from
[[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]], the Hijra boundary still shows:

- **AUC = 1.000** in both held-out directions
- **rho = 0.452**
- **MW-5 PASS 3/3**

So the Late-Meccan -> Medinan lexical frontier is **broad-root-robust**.
