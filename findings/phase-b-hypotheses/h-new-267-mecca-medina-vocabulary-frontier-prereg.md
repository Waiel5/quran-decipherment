---
id: H-NEW-267
title: Mecca-Medina vocabulary frontier test
status: PRE-REGISTERED (locked before production run)
date_prereg: 2026-04-18
seed: 20260418
bonferroni_family: h-new-267-mecca-medina-vocabulary-frontier
bonferroni_k: 3
alpha: 0.05
alpha_bon: 0.016666666666666666
n_perms: 5000
mw5_n_perms: 1000
rules_tuple: "(QAC v0.4 STEM roots via surah-root-graph.json; Late Meccan vs Medinan pool from revelation-order.csv Noldeke phases; alternating split-halves by Noldeke rank within phase; Dirichlet-0.5 pooled log-odds scorer; held-out AUC cells; root-localizer support rule >=10 pooled tokens and >=2 surahs per side; Hafs-Kufan)"
direction_primary: "POSITIVE - a held-out root-log-odds scorer trained on one Late-Meccan/Medinan half separates the other half in both directions, and the split-half root weights replicate with positive rank correlation."
verdict_ceiling: "PASS-DIRECTED only; the scorer family was feasibility-checked before this production lock."
---

# [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] - Mecca-Medina vocabulary frontier test (pre-registration)

## Question

Is there a **reproducible lexical frontier** at the Hijra transition when
the Quran is represented only by **per-surah QAC STEM-root profiles**?

More concretely:

1. If a root-weight vector is learned on one half of the **Late Meccan**
   surahs versus one half of the **Medinan** surahs, does it separate the
   held-out halves?
2. Do the learned root weights replicate across the two split-halves?
3. Which roots carry the sharpest stable shift, if the boundary is real?

This is a deliberately bounded question. It does **not** claim that the Hijra
is the only chronological frontier in the corpus, nor that roots by themselves
recover the full historical process. It tests one conservative instrument:
split-half, held-out root-log-odds separation on the Late-Meccan/Medinan pool.

## Motivation

The project already contains multiple Meccan/Medinan signals:

- verse-length and density differences are strong at the period level,
- some lexical fields clearly drift by phase,
- but the specific question of a **root-level frontier right at the
  Late-Meccan -> Medinan boundary** has not yet been locked as a formal,
  reproducibility-oriented test.

The key risk is over-reading a single pooled contrast. A frontier worth
reporting should survive a stricter standard:

- learn on one half,
- test on the other half,
- swap halves,
- and check whether the root-weight ranking itself is reproducible.

That is the standard used here.

## Data lock

### Root counts

- `data/morphology/surah-root-graph.json`
- Interpretation: QAC v0.4 STEM-root counts per surah

For each surah `s`, let `c_s(r)` be the count of root `r`, and let
`d_s(r) = c_s(r) / sum_r c_s(r)` be the surah-level root-density vector.

### Chronology

- `data/revelation-order.csv`
- Phase field: `noldeke_phase`
- Rank field: `noldeke_order`

Locked 4-phase schema:

- `Early Meccan`
- `Middle Meccan`
- `Late Meccan`
- `Medinan`

The **primary pool** for [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] is the union of the
`Late Meccan` and `Medinan` surahs only.

### Pool size (locked by source file)

Expected from the chronology CSV:

- `Late Meccan = 21 surahs`
- `Medinan = 24 surahs`

Total primary pool size: `45`.

## Split rule (locked)

Within each of the two primary phases separately:

1. sort surahs by `noldeke_order`,
2. assign alternating surahs to split `A` and split `B`.

So:

- `Late Meccan -> (Late_A, Late_B)`
- `Medinan -> (Med_A, Med_B)`

No random split is allowed in the primary run. The alternating split is fixed
and deterministic from the chronology file.

## Root-log-odds scorer (locked)

For any training contrast `later` vs `earlier`, define pooled root counts:

- `C_later(r) = sum_{s in later} c_s(r)`
- `C_earlier(r) = sum_{s in earlier} c_s(r)`

Use symmetric additive smoothing with locked `alpha = 0.5` over the full root
vocabulary of `surah-root-graph.json`.

Define smoothed root probabilities:

- `p_later(r) = (C_later(r) + alpha) / (sum_r C_later(r) + alpha * R)`
- `p_earlier(r) = (C_earlier(r) + alpha) / (sum_r C_earlier(r) + alpha * R)`

and the learned weight vector:

- `w(r) = log(p_later(r) / p_earlier(r))`

For a held-out surah `s`, define its frontier score:

- `score(s) = sum_r d_s(r) * w(r)`

Higher scores indicate stronger alignment with the **later** side of the
contrast.

## Primary Bonferroni family

There are exactly **3 inferential cells**.

### Cell A - Train A, test B

Train `w_A` on:

- positive class = `Med_A`
- negative class = `Late_A`

Test on the held-out pool:

- positives = `Med_B`
- negatives = `Late_B`

Statistic:

- `A_obs = AUC(score_wA(Med_B), score_wA(Late_B))`

Direction: **upper-tail**.

### Cell B - Train B, test A

Train `w_B` on:

- positive class = `Med_B`
- negative class = `Late_B`

Test on the held-out pool:

- positives = `Med_A`
- negatives = `Late_A`

Statistic:

- `B_obs = AUC(score_wB(Med_A), score_wB(Late_A))`

Direction: **upper-tail**.

### Cell C - Root-weight reproducibility

The boundary is not considered reproducible only because surah scores separate.
The learned **root weights** should also replicate.

Support set for Cell C is locked as roots satisfying, on the full
Late-Meccan/Medinan pool:

1. pooled token count `>= 10`, and
2. present in `>= 2` Late-Meccan surahs, and
3. present in `>= 2` Medinan surahs.

Let this support set be `R_support`.

Statistic:

- `C_obs = Spearman( w_A(r), w_B(r) )` over `r in R_support`

Direction: **upper-tail**.

This cell is inferential. Root rankings reported later are descriptive only.

## Null model (locked)

The primary null is a **within-pool label shuffle** on the 45-surah
Late-Meccan/Medinan pool.

For each permutation draw:

1. keep the 45 surahs fixed,
2. shuffle the labels `Late Meccan` and `Medinan` across them,
3. preserve the exact observed counts `21 / 24`,
4. re-split each permuted phase by the same alternating-by-rank rule,
5. recompute Cells A-C.

Repeat `N_PERMS = 5000` with seed `20260418`.

This null asks the exact question of interest:

> if the 45-surah transition pool were not lexically partitioned at the
> observed Hijra boundary, would the same held-out separation and root-weight
> replication still appear?

## MW-5 positive control (same instrument, easier boundary)

Because the primary is a narrow boundary test, MW-5 uses the same scorer on a
broader, easier split that should be recoverable if the instrument is working:

- positive class = all `Medinan` surahs
- negative class = all `Meccan` surahs

Use the same machinery:

1. alternating split by `noldeke_order` within each period,
2. reciprocal held-out AUC cells,
3. split-half root-weight Spearman on the support rule
   `>=10 pooled tokens and >=2 surahs per side`,
4. null = label shuffle across all 114 surahs preserving the exact
   `Meccan / Medinan` counts.

Run `MW5_N_PERMS = 1000`.

### MW-5 pass rule

MW-5 passes only if all 3 control cells pass at `alpha_bon`.

If MW-5 fails, the finding is reported as `NULL-BROKEN`.

## Bonferroni discipline

Family size:

- `k = 3`

Cells:

- A: train A -> test B AUC
- B: train B -> test A AUC
- C: split-half root-weight Spearman

Per-cell threshold:

- `alpha_bon = 0.05 / 3 = 0.0166666667`

No additional inferential cells are allowed inside [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]].

Descriptive comparisons to `Early -> Middle` and `Middle -> Late` may be
reported, but they are **not** part of the family and will not be promoted to
extra significance claims.

## Decision rule

Per cell:

- PASS iff observed statistic exceeds the null 95th percentile **and**
  `p_perm < alpha_bon`
- else NULL

Overall verdict:

- `NULL-BROKEN` if MW-5 fails
- `PASS-DIRECTED` if Cells A-C all pass and MW-5 passes
- `MIXED` if MW-5 passes but only 1-2 of Cells A-C pass
- `NULL` if MW-5 passes and 0 of Cells A-C pass

Verdict ceiling is **PASS-DIRECTED**, not `CONFIRMED`, because the exact
held-out scorer family was chosen only after feasibility checking.

## Descriptive outputs (not extra inferential cells)

The script may report the following descriptively only:

- observed adjacent-boundary mean AUCs for
  `Early|Middle`, `Middle|Late`, `Late|Medinan`
- held-out score ranges and no-overlap gaps for Cells A and B
- full-pool Late-Meccan vs Medinan log-odds weights
- top stable roots ranked by
  `min(abs(w_A), abs(w_B))` with sign agreement
- top absolute mean-density shifts on the full pool

These are localization aids, not new hypothesis tests.

## Honest limits (pre-committed)

1. The chronology labels come from a **Noldeke reconstruction**, not directly
   observed historical timestamps.
2. The analysis is **root-level only**. Phraseology, syntax, and semantics may
   shift differently.
3. Surah is the unit. A perfect or near-perfect surah-level held-out AUC would
   still not imply a verse-level cliff or a single historical cause.
4. Cell C's support rule is a stability filter, not an ontological statement
   that lower-support roots are unimportant.
5. The scorer family was chosen after exploratory feasibility checks on
   2026-04-18. This file locks the final production run **after** that
   feasibility stage but **before** the production execution and reporting.
6. A positive result shows a reproducible lexical partition under this
   instrument; it does **not** prove the Hijra boundary is the unique or
   globally largest chronological frontier in every feature space.

## Deliverables

1. `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier-prereg.md`
2. `scripts/h_new_267_mecca_medina_vocabulary_frontier.py`
3. `findings/phase-b-hypotheses/csv/h-new-267.json`
4. `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier.md`
5. `journal/h-new-267-run-1.md`
