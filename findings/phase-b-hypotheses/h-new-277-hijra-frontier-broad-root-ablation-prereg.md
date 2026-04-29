---
id: H-NEW-277
title: "Hijra lexical frontier broad-root ablation"
phase: B
status: PRE-REGISTERED
registered: 2026-04-18
parent: H-NEW-267
script: scripts/h_new_277_hijra_frontier_broad_root_ablation.py
data_out: findings/phase-b-hypotheses/csv/h-new-277.json
bonferroni_k: 3
alpha: 0.05
alpha_bon: 0.0166666667
seed: 20260418
n_perms_primary: 3000
n_perms_mw5: 1000
rules_tuple: "(QAC v0.4 STEM roots via surah-root-graph.json; exact H-NEW-267 split rule and scorer; EXCLUDE fixed broad-shift roots {Alh, Amn, qwl, rbb, Ayy}; Late Meccan vs Medinan held-out AUC + split-weight rho; MW-5 broad Meccan vs Medinan control)"
direction_primary: "POSITIVE — the H-NEW-267 Hijra frontier survives removal of the five broadest mass-shift roots."
---

# [[h-new-277-hijra-frontier-broad-root-ablation|H-NEW-277]] — Hijra lexical frontier broad-root ablation

## Motivation

[[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] showed that the Late-Meccan -> Medinan boundary is a clean
held-out lexical frontier, with perfect held-out separation in both
split directions and a positive split-weight replication.

That result still leaves one mechanistic question:

**Is the frontier broad, or is it mostly being carried by a few
high-mass roots such as `Alh`, `Amn`, `qwl`, `rbb`, and `Ayy`?**

This follow-up does not re-ask whether the frontier exists in the full
space. It asks whether the same frontier survives when those broadest
mass-shift roots are removed.

## Frozen ablation set

The excluded roots are fixed from [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]'s published descriptive
table `top_abs_delta_mean_density`, taking the top five rows exactly:

- `Alh`
- `Amn`
- `qwl`
- `rbb`
- `Ayy`

No alternative or expanded ablation family is permitted in this run.

## Inherited instrument

Everything else is inherited from [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]:

- QAC STEM-root counts from `surah-root-graph.json`
- Nöldeke chronology from `revelation-order.csv`
- Late-Meccan vs Medinan primary pool
- alternating split-halves by Nöldeke rank within side
- Dirichlet-0.5 pooled log-odds scorer
- held-out AUC in both split directions
- split-half Spearman rho on learned root weights
- same support rule: pooled tokens `>= 10` and `>= 2` surahs per side

Only the five frozen broad-shift roots are removed from the root space
before all scoring and null generation.

## Primary family (Bonferroni k = 3)

Family-wise alpha = `0.05`. Per-cell alpha:

- `alpha_bon = 0.0166666667`

### Cell A — train A -> test B AUC

Statistic:

- held-out AUC on the Late-Meccan vs Medinan boundary after root
  ablation

Direction:

- higher than the permutation null

### Cell B — train B -> test A AUC

Statistic:

- held-out AUC on the reverse split after root ablation

Direction:

- higher than the permutation null

### Cell C — split-weight rho

Statistic:

- Spearman rho of the learned split-half root-log-odds weights after
  ablation

Direction:

- higher than the permutation null

## Nulls

### Primary null

- `n_perms = 3000`
- same 45-surah Late-Meccan/Medinan pool as [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]
- preserve exact class sizes `21 / 24`
- same split procedure after relabeling

### MW-5 positive control

- exact [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] Meccan-vs-Medinan control
- same ablated root space
- `n_perms = 1000`
- pass rule: all 3 cells must pass at `alpha_bon`

If MW-5 fails, verdict ceiling becomes `NULL-BROKEN`.

## Verdict mapping

- MW-5 fail: **NULL-BROKEN**
- 3/3 primary PASS with MW-5 alive: **PASS-DIRECTED**
- 1-2/3 primary PASS with MW-5 alive: **MIXED**
- 0/3 primary PASS with MW-5 alive: **NULL**

## Descriptive outputs allowed

The script may additionally report:

- new support-set size after ablation
- held-out score gaps
- comparison against the parent [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] observed cells
- top stable roots in the reduced space

These descriptives are not extra inferential cells.

## Garden-of-forking-paths log

- The ablation set is fixed from the already-published [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]
  descriptive table, not re-estimated during this run.
- I am not testing multiple ablation families in parallel.
- I am not changing the scorer, split rule, chronology source, or null.
- This is a mechanistic child test, so the verdict ceiling is
  `PASS-DIRECTED`, not `CONFIRMED`.

## Honest limits

- Removing only five roots cannot prove the frontier is fully diffuse.
- The ablation set is driven by broad mass shifts, not by stable
  log-odds magnitude.
- Root-space dependence remains; phraseology and syntax are still out of
  scope.
- A surviving result would show the frontier is not reducible to these
  five roots, not that every remaining root is equally important.

## Deliverables

1. This pre-reg
2. `scripts/h_new_277_hijra_frontier_broad_root_ablation.py`
3. `findings/phase-b-hypotheses/csv/h-new-277.json`
4. `findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation.md`
5. `journal/h-new-277-run-1.md`
