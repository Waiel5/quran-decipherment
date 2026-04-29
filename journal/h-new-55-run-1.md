---
date: 2026-04-15
agent: h-new-55-specialist
hypothesis: H-NEW-55 — multi-axis muqaṭṭaʿāt classifier (LOOCV)
seed: 20260416
---

# Run-1 journal — H-NEW-55

## Goal

Build a binary classifier (muq vs non-muq) from 6 pre-registered structural features and test predictive accuracy via leave-one-out CV with a 1000-permutation null. Pre-committed PASS criterion: AUC > 0.80 AND permutation p < 0.01 AND MW-5 control > 0.95.

## Sequence

1. Read context: cross-finding-006 + H-NEW-46/46.1/49.1/53 result docs.
2. Located canonical 29-surah muqaṭṭaʿāt set in scripts/h_new_46_muqattaat_length.py:
   `{2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}`
3. Located canonical 8-surah prophet-named conservative set per H-NEW-49.1:
   `{10, 11, 12, 14, 19, 31, 47, 71}`
4. Located H-NEW-53 substring lists for KITAB_FORMS and QURAN_FORMS.
5. Wrote pre-reg with 6 features, LOOCV, 1000 perms, seed 20260416, MW-5 gate at 0.95.
6. Wrote scripts/h_new_55_classifier.py.
7. Installed scikit-learn 1.8.0 (pip --break-system-packages).
8. Single run; no re-tuning.

## Results

- MW-5 planted-signal control: AUC = 0.9793 — pipeline OK.
- Real data LOOCV AUC = 0.9241.
- Accuracy @ 0.5 = 0.8246.
- Muq precision/recall = 0.610/0.862; Non-muq = 0.945/0.812.
- Permutation null: 0/1000 perms ≥ observed AUC; p = 0.001.
- Permutation AUC mean = 0.4676 (std 0.092); max = 0.6913.

## Feature importance (full-data, standardized continuous)

book_ref_v1_3 +1.957 > mushaf_index −1.255 > period_meccan +0.881 > prophet_named +0.642 > noldeke_order −0.140 > length +0.089

## Errors

False negatives (4): Q 29, 30, 42, 68 — exactly the H-NEW-53 exceptions (no book ref in v1-3) plus already-noted Q 29.
False positives (16): mostly H-NEW-53's "muqaṭṭaʿāt-shaped without muqaṭṭaʿāt" set (Q 17, 18, 34, 39, 52, 55, 72) plus long early-Meccan surahs (Q 4, 5, 6, 16, 21, 23, 37) plus Q 1 and Q 25.

## Verdict

STRONG-PASS (all 3 criteria met; AUC > 0.90 strong-pass condition also met).

## Garden of forking paths

Closed. All decisions logged in pre-reg before training. Single run, no hyperparameter search, no model comparison, no feature reselection.

## Files written

- /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-55-classifier-prereg.md
- /Users/grey/Downloads/quran/scripts/h_new_55_classifier.py
- /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-55.json
- /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-55-classifier.md
- /Users/grey/Downloads/quran/journal/h-new-55-run-1.md

## Notes for follow-up

- Could re-run with stronger Bonferroni p-floor (10000 perms) to push p below 10⁻⁴, but pre-reg specified 1000.
- Could test classifier transfer: train on early-mushaf, test on late-mushaf, to check if the signal is independent of mushaf-position. Pre-registered separately if pursued.
- The 4 false negatives = H-NEW-53's exceptions = the "muqaṭṭaʿāt without the rest of the package." These are interpretively the most interesting muqaṭṭaʿāt-opened surahs.
