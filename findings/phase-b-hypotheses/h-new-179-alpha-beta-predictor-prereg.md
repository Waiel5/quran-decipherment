---
id: H-NEW-179
title: (α, β)-residual + length features as predictor of muqaṭṭāʿat letter-set IDENTITY (10-class)
phase: B
status: PRE-REG
date: 2026-04-17
parent: H-NEW-178 (muq-vs-non-muq on (α,β) residual, p=0.005), H-NEW-88 (18-feature structural baseline, top-1 0.414)
seed: 20260419
rules_tuple: (no-tashkeel; top-200 ranks for α; log V(N) checkpoints for β; muq 29 surahs; LOOCV 29-fold; RF primary; perm null 1000; primary top-1 ≥ 0.50; secondary ≥1 singleton hit)
bonferroni_k: 2
bonferroni_family: h-new-179-alpha-beta-predictor
alpha_family: 0.05
alpha_bon: 0.025
---

# [[h-new-179-alpha-beta-predictor|H-NEW-179]] — (α, β)-based predictor for muqaṭṭāʿat letter-set IDENTITY

## Motivation

OQ-1 (why specific letter-set per muqaṭṭāʿat surah?) has been ANSWERED-NULL at content
([[h-new-96-predictor-extension|H-NEW-96]]) and rhyme (H-NEW-96.2). [[h-new-88-letter-set-predictor|H-NEW-88]] achieved top-1 0.414 on the 10-class
problem (14 letter-sets, 8 of which are singletons) using 43 structural/content
features, ceiling ≈ 0.65 due to 8 singletons.

[[h-new-178-alpha-beta-manifold|H-NEW-178]] found (α, β) residual distinguishes muq from non-muq at p=0.005 — a new
non-content axis. This test asks: **do (α, β) features help predict letter-set
IDENTITY (10-class) beyond [[h-new-88-letter-set-predictor|H-NEW-88]]'s 0.414 baseline?**

If PASS (top-1 ≥ 0.50), this would be the first OQ-1 progress since project
inception.

## Features

### New-feature vector (6 features per surah)

Computed per [[h-new-172-zipf-per-chapter|H-NEW-172]] methodology (top-200 ranks for α; log V(N) checkpoints for β).

1. `alpha` — Zipf exponent from rank-frequency log-log fit (top-200 ranks per [[h-new-172-zipf-per-chapter|H-NEW-172]])
2. `beta` — Heap exponent from log V(N) fit per [[h-new-172-zipf-per-chapter|H-NEW-172]] (same per-surah β)
3. `residual` — residual from linear (α, β) regression fit to 93 surahs with N≥50
4. `log_length` — log of total token count N per surah
5. `mean_verse_length` — mean chars per verse (same as [[h-new-88-letter-set-predictor|H-NEW-88]] F11)
6. `period_medinan` — 1 if Medinan, 0 if Meccan (same as [[h-new-88-letter-set-predictor|H-NEW-88]] F2 inverted)

### Combined-feature vector (24 features)

6 new features + **18 [[h-new-88-letter-set-predictor|H-NEW-88]] structural features**:
- F1 length (verse count)
- F2 period_meccan
- F3 noldeke_order
- F4 mushaf_index
- F5 book_ref_v1_3
- F6 prophet_named
- F7 name_class one-hot (9 classes)
- F8 divine_name_density
- F11 mean_verse_length_chars
- F12 letter_count_in_set

(18 = 6 structural + 9 name_class + 1 divine_name + 1 mean_verse_len + 1 letter_count)

**Note**: The 20 root-count features from [[h-new-88-letter-set-predictor|H-NEW-88]] F10 and the 5 first-word
one-hot from F9 are **excluded** to keep dimensionality tractable and focus on
structure+compositional-signature features.

## Procedure

- **Classifier**: Random Forest (200 estimators, seed 20260419)
- **CV**: 29-fold LOOCV (per [[h-new-88-letter-set-predictor|H-NEW-88]])
- **Standardization**: train-fold only (z-score)
- **Target**: 14-class letter-set (10 unique, 8 singletons)
- **Null**: 1000-permutation of y labels, seed 20260419

## Primary cells (Bonferroni k=2)

- **P1**: LOOCV top-1 accuracy of 24-feature combined model ≥ **0.50**
  (baseline [[h-new-88-letter-set-predictor|H-NEW-88]]: 0.414; structural ceiling: 0.655)
- **P2**: At least **1 singleton letter-set correctly predicted** at top-1
  ([[h-new-88-letter-set-predictor|H-NEW-88]] got 0/8 singletons; any singleton hit = qualitative advance)

α_family = 0.05, k=2 → α_bon = 0.025 per cell.

## Secondary (descriptive only)

- 6-feature-only model top-1 accuracy (is (α,β) alone enough?)
- Which singletons (if any) become predictable?
- Feature importance rankings
- Per-cluster recall comparison (ALM/HM/ALR)

## MW-5 Method Working Test

**cheat_surah_id**: add surah_id as a feature. Model should reach top-1 ≥ 0.52
(lookup-table proxy). If not, pipeline is broken. **This validates LOOCV is
working and RF can exploit strong features.**

## Garden-of-forking-paths log (PRE-RUN)

Decisions made BEFORE seeing results:

1. **Primary classifier = RF** (not logistic). Rationale: [[h-new-88-letter-set-predictor|H-NEW-88]] RF outperformed
   logistic substantively (0.414 vs 0.276), interactions likely among length/α/β.
2. **Top-200 rank cutoff for α**: locked from [[h-new-172-zipf-per-chapter|H-NEW-172]] existing CSV.
3. **Residual = residual from linear (α,β) fit on 93 surahs ≥50 tokens**: same as
   [[h-new-178-alpha-beta-manifold|H-NEW-178]], using Quran-only regression line (not cross-corpus).
4. **24 = 6 new + 18 [[h-new-88-letter-set-predictor|H-NEW-88]] structural**: drop roots (20) and first_word (5) from
   [[h-new-88-letter-set-predictor|H-NEW-88]]; keep all other locked features. Choice pre-committed.
5. **Primary threshold = 0.50** (not 0.45 or 0.55): midpoint between baseline
   (0.414) and ceiling (0.655).
6. **Secondary = ≥1 singleton** (not top-3 improvement): qualitative OQ-1 advance
   would require cracking the singleton barrier.
7. **1000 perms**: standard from [[h-new-88-letter-set-predictor|H-NEW-88]] pre-reg.
8. **Bonferroni k=2** not k=3 or more — primary and secondary are distinct
   claims; we don't correct for exploratory descriptive diagnostics.
9. **Seed 20260419** per session standard.

## Expected null

Under null (α, β residual has no letter-set signal beyond [[h-new-88-letter-set-predictor|H-NEW-88]] 18 features),
combined model top-1 ≈ 0.414 (same as [[h-new-88-letter-set-predictor|H-NEW-88]] RF). Permutation distribution
q95 ≈ 0.28 per [[h-new-88-letter-set-predictor|H-NEW-88]].

## Exit criteria

- **PASS** (both cells): report first OQ-1 positive. Document which singletons
  became predictable. Stream to MASTER-FINDINGS-LEDGER as Tier-A promotion.
- **PASS primary only**: predictor improves but no singleton breakthrough.
- **PASS secondary only**: singleton hit(s) but overall accuracy unchanged
  (unusual — probably data quirk).
- **NULL**: report with equal prominence. (α, β) features do NOT meaningfully
  help letter-set identity beyond [[h-new-88-letter-set-predictor|H-NEW-88]] baseline. Close OQ-1 on this axis.

## Files

- Script: `scripts/h_new_179_alpha_beta_predictor.py`
- Pre-reg: this file
- Result: `findings/phase-b-hypotheses/h-new-179-alpha-beta-predictor.md`
- JSON: `findings/phase-b-hypotheses/csv/h-new-179.json`
