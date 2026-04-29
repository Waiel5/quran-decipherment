---
id: H-NEW-55
title: Multi-axis muqaṭṭaʿāt classifier — predict muq vs non-muq from structural features (LOOCV)
phase: B
status: PRE-REGISTERED
date: 2026-04-15
agent: h-new-55-specialist
test: logistic regression with leave-one-out cross-validation; permutation null
rules_tuple: (no-tashkeel; verses 1-3 substring window for book-reference; conservative prophet-named list per H-NEW-49.1)
seed: 20260416
---

# [[h-new-55-classifier|H-NEW-55]] — Pre-registration

## Hypothesis

The 29 muqaṭṭaʿāt-opened surahs differ from the 85 non-muqaṭṭaʿāt-opened surahs along multiple coherent structural axes (length, chronology, book-reference, prophet-named) such that a simple multi-axis classifier should predict muqaṭṭaʿāt-status above chance — and well above any single-axis predictor.

This is a SYNTHESIS test, not a discovery test: cross-finding-006 already documents 8 independent axes. [[h-new-55-classifier|H-NEW-55]] asks: do they CO-OCCUR in a way that yields a strong joint predictor?

## Locked feature set (LOCKED BEFORE TRAINING)

For each of 114 surahs:

- **F1 (length)**: surah verse count (continuous)
- **F2 (period_meccan)**: 1 if Meccan, 0 if Medinan (binary; from data/revelation-order.csv `period` field)
- **F3 (noldeke_order)**: Nöldeke chronological order, integer 1-114 (from data/revelation-order.csv `noldeke_order`)
- **F4 (book_ref_v1_3)**: 1 if any form of root k-t-b OR root q-r-ʾ appears in verses 1-3, 0 otherwise. Substring-match list per [[h-new-53-muqattaat-book-reference|H-NEW-53]]:
  - KITAB_FORMS = {كتاب, كتب, الكتاب, الكتب, كتابك, كتابه, كتابي, كتابهم, كتابا}
  - QURAN_FORMS = {قرآن, القرآن, قرءان, القرءان, قرءن, قرآنا, قرآنه}
- **F5 (prophet_named)**: 1 if surah is in conservative PROPHET_PERSON list per [[h-new-49-1-prophet-enrichment|H-NEW-49.1]]: {10 Yūnus, 11 Hūd, 12 Yūsuf, 14 Ibrāhīm, 19 Maryam, 31 Luqmān, 47 Muḥammad, 71 Nūḥ}, 0 otherwise.
- **F6 (mushaf_index)**: canonical mushaf order, integer 1-114.

All 6 features are derivable from data on disk WITHOUT inspection of muqaṭṭaʿāt status.

## Outcome

**y_i = 1** if surah i is in the locked muqaṭṭaʿāt set:
{2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68} (n=29)
**y_i = 0** otherwise (n=85)

## Procedure

1. Compute the 6-feature design matrix X (114 × 6) with no leakage from y.
2. Standardize continuous features (length, noldeke_order, mushaf_index) by z-score using the FULL training fold (LOOCV: each fold standardizes on n=113).
3. Train scikit-learn LogisticRegression(C=1.0, solver='liblinear', class_weight='balanced') with LOOCV.
4. Compute:
   - Hold-out probabilities (one per surah, from the model trained without that surah).
   - AUC (area under ROC curve, computed on hold-out probabilities vs y).
   - Accuracy at threshold 0.5.
   - Per-class precision and recall.
   - Feature importance: standardized coefficients from a model trained on all 114 surahs (for interpretation only; the LOOCV is the hold-out test).
5. Permutation null: shuffle y 1000 times (seed 20260416), re-run LOOCV, compute AUC each time. p = (1 + count(perm_AUC ≥ observed_AUC)) / 1001.
6. **MW-5 sanity control**: generate a planted-signal dataset with 6 features where 3 features have known design (correlated with planted y), 3 are noise. Confirm classifier achieves >0.95 AUC on this control. If not, the pipeline is broken.

## Pre-committed PASS criterion

- **PASS** iff: observed AUC > 0.80 AND permutation p < 0.01 AND MW-5 control > 0.95 AUC.
- **FAIL** if any of these is unmet.
- **STRONG-PASS** if AUC > 0.90 (well above the pre-committed threshold).

## Garden-of-forking-paths log

Decisions made BEFORE training:
- Feature set = exactly the 6 listed above. No interaction terms; no polynomial expansion; no feature selection. Logistic regression only.
- LOOCV (not k-fold): chosen because n=114 is small; LOOCV uses maximum data per fold.
- class_weight='balanced': because 29:85 is imbalanced; this prevents trivial all-zero classifier.
- C=1.0: scikit-learn default; no tuning.
- Standardization: z-score per fold to prevent leakage.
- Permutation count = 1000.
- Seed = 20260416.

What I will NOT do:
- Add features after seeing the result.
- Try multiple classifier types and report the best.
- Tune hyperparameters.
- Drop features that hurt performance.

## Expected interpretation

If AUC > 0.80, the multi-axis muqaṭṭaʿāt-design picture from cross-finding-006 is empirically validated as a JOINT predictive signal, not just a list of separate marginal correlations.

If AUC ≤ 0.80, the axes are weakly joint-informative and may be partially redundant or weak in combination — which would temper the cross-finding-006 synthesis.

## Integrity

- Feature definitions LOCKED before any training (this document).
- Seed fixed.
- LOOCV with no leakage.
- MW-5 control gates the pipeline.
- Permutation null (1000 perms).
- All features derivable from on-disk CSV/JSON without inspection of muqaṭṭaʿāt status.
