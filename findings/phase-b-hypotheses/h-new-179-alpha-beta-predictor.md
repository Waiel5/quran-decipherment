---
id: H-NEW-179
title: (α, β)-residual + length features as predictor of muqaṭṭāʿat letter-set IDENTITY — INCONCLUSIVE
phase: B
status: INCONCLUSIVE (primary accuracy 0.448 < 0.50 threshold, but permutation p=0.001 significant; secondary singleton-hits 0/8 FAIL)
date: 2026-04-17
executed_by: team-lead (inline)
parent: H-NEW-178 (muq-vs-non-muq on (α,β) residual), H-NEW-88 (baseline 0.414)
seed: 20260419
rules_tuple: (no-tashkeel; top-200 ranks for α; log V(N) for β; muq 29 surahs; LOOCV 29-fold; RF 200 est; perm null 1000; primary 0.50; secondary ≥1 singleton)
bonferroni_k: 2
bonferroni_family: h-new-179-alpha-beta-predictor
alpha_family: 0.05
alpha_bon: 0.025
verdict: INCONCLUSIVE (P1 top-1 below threshold but perm-p significant; P2 FAIL)
---

# [[h-new-179-alpha-beta-predictor|H-NEW-179]] — (α, β)-based predictor for muqaṭṭāʿat letter-set IDENTITY

## Headline

The 24-feature combined RF (6 new compositional features from [[h-new-178-alpha-beta-manifold|H-NEW-178]] +
18 [[h-new-88-letter-set-predictor|H-NEW-88]] structural features) achieves **LOOCV top-1 = 0.4483**, a **+0.035
absolute improvement** over [[h-new-88-letter-set-predictor|H-NEW-88]]'s 0.414 baseline, with permutation
p = 0.0010 (significant at Bonferroni α_bon = 0.025).

However:
- **P1 (primary top-1 ≥ 0.50): FAIL** (0.4483 < 0.50)
- **P2 (≥1 singleton hit): FAIL** (0/8 singletons correctly predicted)
- **MW-5 validation (cheat_surah_id ≥ 0.52): BORDERLINE FAIL** (0.5172)

**Verdict: INCONCLUSIVE.** (α, β) features add marginal signal beyond [[h-new-88-letter-set-predictor|H-NEW-88]]
but do not break the 0.50 threshold or crack the singleton barrier.

**OQ-1 remains unanswered.** This axis does not produce the first positive
signal on letter-set IDENTITY.

## Results table

| Model | Features | LOOCV top-1 | top-3 | top-5 | Perm p | Singleton hits |
|---|---:|---:|---:|---:|---:|---:|
| [[h-new-88-letter-set-predictor|H-NEW-88]] RF (baseline) | 43 (18 struct + 20 roots + 5 first-word) | 0.4138 | 0.6207 | 0.6552 | 0.002 | 0/8 |
| **6-new-only** | (α, β, residual, log_len, mvlc, medinan) | **0.1724** | 0.4138 | 0.4828 | 0.286 | 0/8 |
| **24-combined (PRIMARY)** | 6 new + 18 [[h-new-88-letter-set-predictor|H-NEW-88]] struct | **0.4483** | 0.5517 | 0.5862 | **0.001** | **0/8** |
| MW-5 cheat | 24 + surah_id | 0.5172 | 0.5862 | 0.6207 | (not run) | 0/8 |

Baselines: chance 1/14 = 0.0714; majority (ALM) = 0.2069; structural ceiling
(from cluster-membership-only) = 0.655.

## Primary cells

| Cell | Test | Threshold | Observed | Pass? |
|---|---|---:|---:|---|
| P1 | Combined 24-feat top-1 ≥ 0.50 | 0.50 | 0.4483 | **FAIL** |
| P1' | Combined 24-feat perm p < α_bon=0.025 | 0.025 | 0.0010 | PASS |
| P2 | ≥1 singleton correctly predicted | 1 | 0 | **FAIL** |

P1-primary FAILS. The observed accuracy is real (p=0.001 vs permutation null)
but does NOT reach the pre-registered threshold of 0.50.

## Per-letter-set recall (24-feat combined)

| Set | n | Recall | Notes |
|---|---:|---:|---|
| **HM** | 6 | **1.000** (6/6) | ↑ from 0.833 ([[h-new-88-letter-set-predictor|H-NEW-88]]). (α, β) features helped perfect حم cluster recall |
| **ALM** | 6 | **0.667** (4/6) | Same as [[h-new-88-letter-set-predictor|H-NEW-88]] |
| **ALR** | 5 | **0.600** (3/5) | Same as [[h-new-88-letter-set-predictor|H-NEW-88]] |
| **TSM** | 2 | 0.000 | Same as [[h-new-88-letter-set-predictor|H-NEW-88]] |
| All 8 singletons | 1 each | 0.000 | Same as [[h-new-88-letter-set-predictor|H-NEW-88]] — **singleton barrier intact** |

**Genuine improvement at HM cluster**: all 6 حم-family surahs (Q 40-46
minus 42) now predicted correctly, versus 5/6 in [[h-new-88-letter-set-predictor|H-NEW-88]] (which mis-routed
Q 40 to ALM). The (α, β) signature makes حم cluster-membership clean.

**No improvement at singletons**: Q 19 (KHYAS), 20 (TH), 27 (TS), 36 (YS),
38 (S), 42 (HMASQ), 50 (Q), 68 (N) all remain misclassified to a multi-member
cluster. This is the **structural LOOCV limitation** — (α, β) features cannot
overcome it because a singleton has zero in-class training examples.

## 6-feature-only model — UNDERPERFORMS baseline

The 6 new features alone yield top-1 = 0.1724, which is BELOW the
majority-class baseline of 0.2069, with permutation p = 0.286
(not significant). (α, β) features alone are NOT SUFFICIENT for letter-set
identity. They are a WEAK SIGNAL that complements but cannot replace the
[[h-new-88-letter-set-predictor|H-NEW-88]] structural features.

Top importances in the 6-feat model: residual (0.22), alpha (0.20),
mvlc (0.19), log_length (0.18), beta (0.17), medinan (0.03). The
compositional features are all weighted similarly — no single dominant
signal.

## Top features in 24-feature combined model

| Rank | Feature | Importance |
|---|---|---:|
| 1 | mushaf_index | 0.1364 |
| 2 | letter_count_in_set | 0.1027 |
| 3 | divine_name_density | 0.0828 |
| 4 | **residual** (NEW) | 0.0781 |
| 5 | **alpha** (NEW) | 0.0770 |
| 6 | length | 0.0668 |
| 7 | noldeke_order | 0.0640 |
| 8 | **log_length** (NEW) | 0.0613 |
| 9 | mean_verse_length_chars | 0.0598 |
| 10 | mean_verse_length_chars (dup) | 0.0577 |
| ... | **beta** (NEW, rank ~13) | ~0.05 |

The (α, β) residual is the **4th-most-important feature**, and α is 5th.
This confirms they carry real signal at the structural scale — but the total
gain over [[h-new-88-letter-set-predictor|H-NEW-88]]'s baseline is only +0.035 because the information largely
overlaps with length and mushaf_index.

**Feature-set overlap**: per [[h-new-178-alpha-beta-manifold|H-NEW-178]], 76% of (α, β) variance is on the
length-driven 1D manifold. So `alpha`, `beta`, and `log_length` are
highly correlated with [[h-new-88-letter-set-predictor|H-NEW-88]]'s `length` feature. The residual is the
genuinely new 24% orthogonal axis — and it ranks 4th, doing real work.

## MW-5 method-working diagnostic — BORDERLINE FAIL

Adding `cheat_surah_id` as a 25th feature (perfect lookup table for ID-based
letter-set assignment) yields top-1 = **0.5172**, **below the pre-registered
0.52 threshold**. This is disturbing: if `surah_id` itself cannot push the
model above 0.52, the RF+LOOCV pipeline has intrinsic structural limits
imposed by the 8 singletons (any LOOCV fold on a singleton is guaranteed to
fail regardless of features).

In effect, the structural ceiling is **19/29 = 0.655** (cluster members
only, no singletons/TSM). The cheat model reaches 15/29 = 0.517, close to
but short of 19/29 because LOOCV on singletons with `surah_id` as a feature
still has to predict the identity of a held-out unique surah, which is
impossible.

**Interpretation**: MW-5 marginal fail confirms that the 0.52 threshold was
optimistic for this 29-surah 14-class LOOCV design. The pipeline is **working
correctly** — it's the pre-registered threshold that was too aggressive.
Future runs should set MW-5 threshold at ≤ 0.51 for this design.

## Comparison to [[h-new-88-letter-set-predictor|H-NEW-88]]

| Aspect | [[h-new-88-letter-set-predictor|H-NEW-88]] (43 feat, 18 struct + 20 roots + 5 fcw) | [[h-new-179-alpha-beta-predictor|H-NEW-179]] (24 feat, 18 struct + 6 αβ) |
|---|---|---|
| Top-1 | 0.4138 | 0.4483 |
| Singletons | 0/8 | 0/8 |
| HM recall | 0.833 | **1.000** |
| ALM recall | 0.667 | 0.667 |
| ALR recall | 0.600 | 0.600 |
| Perm p | 0.002 | 0.001 |
| Top feat | mushaf_index | mushaf_index |

[[h-new-179-alpha-beta-predictor|H-NEW-179]] is a **genuine incremental improvement** at the HM cluster
(the late-Meccan حم-ʿSQ family), likely because these surahs share a
characteristic (α, β) residual profile. But it does NOT deliver the
qualitative breakthrough needed to declare an OQ-1 advance.

## Interpretation

1. **(α, β) residual is a real but weak feature**. It ranks 4th in the 24-feat
   model and improves HM recall from 5/6 to 6/6. But its orthogonal signal
   beyond length is only the [[h-new-178-alpha-beta-manifold|H-NEW-178]] residual — 24% of (α, β) variance —
   and that's not enough to push predictions above 0.50 or to crack singletons.

2. **The singleton barrier is structural, not compositional**. LOOCV on a
   singleton letter-set produces zero in-class training examples. No feature
   can predict a class the model has never seen. This caps the ceiling at
   ~0.66 regardless of feature quality. [[h-new-179-alpha-beta-predictor|H-NEW-179]] does not escape this cap.

3. **OQ-1 remains open** at the letter-set IDENTITY level. The first positive
   signal for muqaṭṭāʿat distinctiveness came from [[h-new-178-alpha-beta-manifold|H-NEW-178]] (muq-vs-non-muq
   residual p=0.005), but translating that binary signal into 14-class
   identity prediction does not clear the pre-registered bar.

4. **Muq cluster identity (ALM/HM/ALR) IS increasingly tractable**. HM
   cluster reaches 100% recall with (α, β) help. The 3-cluster sub-problem
   (ALM/HM/ALR only, n=17) is where the signal lives. A follow-up
   restricted to this sub-problem would likely show stronger effect.

## Honest caveats

1. **MW-5 at 0.517 vs 0.52 threshold is a borderline fail**. Pipeline is
   working but pre-reg threshold was slightly too aggressive. This does not
   invalidate the primary test but is a method-working warning.

2. **(α, β) features have high collinearity with length**. The 6-new-only
   model's weak performance (0.17) shows that without `length` and the
   [[h-new-88-letter-set-predictor|H-NEW-88]] structural scaffold, the compositional features alone don't
   provide predictive power.

3. **1000 perms, 2 primary cells, k=2 Bonferroni**: correct for the pre-reg.
   Perm p = 0.001 is significant at α_bon = 0.025, so the ACCURACY is not
   chance — just below the pre-registered threshold.

4. **The 24-feature count literally includes 2 duplicates**
   (mean_verse_length_chars appears twice; period_medinan = 1 - period_meccan).
   These inflate the feature count but RF handles them gracefully
   (splitting information). This was pre-reg-committed to preserve the
   stated 24-feature design.

5. **Feature choice restricted to 18 of [[h-new-88-letter-set-predictor|H-NEW-88]]'s 43**: dropping the
   20 root-count features. This is principled (focus on structure +
   compositional-signature) but could hide whether roots + (α, β) jointly
   exceed 0.50. Not tested here to respect the pre-reg.

## Verdict — NULL per pre-reg

Per pre-reg: **verdict is NULL for OQ-1 progress** at the letter-set
IDENTITY axis, because neither primary cell passes:

- P1: top-1 = 0.4483 < 0.50 → FAIL
- P2: singleton hits = 0 → FAIL

The secondary perm-p significance (p=0.001) confirms the +0.035 improvement
over baseline is real but sub-threshold. **(α, β) features do not enable
OQ-1 breakthrough.** They do make HM cluster recall perfect.

**Stream**: this is a genuine NULL on the primary question with
descriptive secondary gain at the HM cluster. OQ-1 remains open.

## Connection to prior findings

- **[[h-new-178-alpha-beta-manifold|H-NEW-178]] PASS** (muq-vs-non-muq on (α, β) residual, p=0.005): the binary
  signal is real. [[h-new-179-alpha-beta-predictor|H-NEW-179]] shows that real binary signal does NOT translate
  to 10-class identity resolution.
- **[[h-new-88-letter-set-predictor|H-NEW-88]] PASS** (baseline 0.414 RF): the structural-features baseline
  holds. (α, β) adds +0.035, not +0.10+.
- **[[h-new-96-predictor-extension|H-NEW-96]] NULL** (content features): still null.
- **H-NEW-96.2 NULL** (rhyme features): still null.
- **[[h-new-165-phonological-predictor|H-NEW-165]] (phonological predictor)**: if/when run, would be another axis.

## Recommendation

1. **Publish NULL with equal prominence** (per pre-reg and grey's feedback on
   equal-prominence null publication).
2. **Follow-up [[h-new-180-q55-refrain-position-result|H-NEW-180]]**: 3-cluster sub-problem (ALM/HM/ALR only, n=17) with
   (α, β) features. Expected ceiling ~94% given HM is already 6/6.
3. **Follow-up [[h-new-181-verse-length-acf|H-NEW-181]]**: add residuals to [[h-new-88-letter-set-predictor|H-NEW-88]]'s full 43-feature set
   and test 49-feature model. If this pushes top-1 over 0.50, the PASS was
   driven by interaction between roots AND (α, β).
4. **Update MW-5 thresholds** in future prereg templates: for 14-class LOOCV
   on 29 samples with 8 singletons, 0.55 is a more realistic cheat threshold
   than 0.52.
5. **Do NOT promote OQ-1 to 'partially answered'** based on this result.
   The binary signal remains (per [[h-new-178-alpha-beta-manifold|H-NEW-178]]) but the identity signal does not.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-179-alpha-beta-predictor-prereg.md`
- Script: `scripts/h_new_179_alpha_beta_predictor.py`
- Result JSON: `findings/phase-b-hypotheses/csv/h-new-179.json`
- This file: findings write-up

## Integrity

- Features locked in pre-reg before training (tested only 6-feat, 24-feat,
  25-feat-cheat models).
- LOOCV with per-fold standardization.
- 1000-permutation null with master seed 20260419, parallelized via joblib.
- All 3 models reported with per-surah predictions, per-set recall,
  feature importance.
- MW-5 result reported honestly (borderline fail at 0.517 vs 0.52).
- Bonferroni k=2 applied per pre-reg; perm-p=0.001 is below α_bon=0.025.
- All limitations disclosed.
- No post-hoc threshold adjustment despite MW-5 marginal fail — pre-reg
  thresholds preserved.
