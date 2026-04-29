---
id: H-NEW-88-PREREG
title: Multi-class predictive model for muqaṭṭaʿāt LETTER-SET (14 classes, 29 surahs)
phase: B
status: PRE-REGISTERED
date: 2026-04-15
agent: h-new-88-specialist
test: multi-class classifier (multinomial logistic regression + random forest); leave-one-out CV; permutation null
rules_tuple: (no-tashkeel; canonical 14 distinct letter-sets across 29 muqaṭṭaʿāt-opened surahs; hafs-kufan; locked feature set per pre-reg)
seed: 20260416
---

# [[h-new-88-letter-set-predictor|H-NEW-88]] — PRE-REGISTRATION

## Question

[[h-new-55-classifier|H-NEW-55]] demonstrated that we can PREDICT which surahs are muqaṭṭaʿāt-opened (binary, AUC=0.92, perm p=0.001).

The OPEN QUESTION (per cross-finding-008): why does each surah get its specific letter-set (الم vs الر vs حم etc.)? Is there ANY content-based signal that predicts WHICH set, or are letter-sets independent of all content features?

[[h-new-88-letter-set-predictor|H-NEW-88]] tests the harder question: among the 29 muqaṭṭaʿāt-opened surahs, can we predict the specific letter-set from content/structural features alone?

## Hypothesis

H1 (signal): A locked feature set predicts muqaṭṭaʿāt letter-set with LOOCV accuracy significantly above the chance baseline.
H0 (null): The letter-set assignment is independent of these structural/content features.

## Sample

- **N = 29** muqaṭṭaʿāt-opened surahs (locked per [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]/49/55).
- **K = 14** distinct letter-sets:
  - الم (n=6): Q 2, 3, 29, 30, 31, 32
  - المص (n=1): Q 7
  - الر (n=5): Q 10, 11, 12, 14, 15
  - المر (n=1): Q 13
  - كهيعص (n=1): Q 19
  - طه (n=1): Q 20
  - طسم (n=2): Q 26, 28
  - طس (n=1): Q 27
  - يس (n=1): Q 36
  - ص (n=1): Q 38
  - حم (n=6): Q 40, 41, 43, 44, 45, 46
  - حم عسق (n=1): Q 42 (treated as separate set per canonical convention)
  - ق (n=1): Q 50
  - ن (n=1): Q 68

## Locked feature set (specified BEFORE training)

Same family as [[h-new-55-classifier|H-NEW-55]] + extensions for content:

| # | Feature | Description | Source |
|---|---------|-------------|--------|
| F1 | length | total verse count | quran-no-tashkeel.json |
| F2 | period_meccan | 1=Meccan, 0=Medinan | revelation-order.csv |
| F3 | noldeke_order | Nöldeke chronological 1–114 | revelation-order.csv |
| F4 | mushaf_index | canonical mushaf order | trivial |
| F5 | book_ref_v1_3 | k-t-b or q-r-ʾ form in v1–3 | per [[h-new-53-muqattaat-book-reference|H-NEW-53]] substring lists |
| F6 | prophet_named | conservative PROPHET_PERSON list | per [[h-new-49-1-prophet-enrichment|H-NEW-49.1]] |
| F7 | name_class | one-hot encoding of 9-class taxonomy | per [[h-new-49-surah-name-class|H-NEW-49]] |
| F8 | divine_name_density | count of 99-names tokens / total tokens | per H-NEW-59 list |
| F9 | first_content_word_class | binary categories: book-ref / oath / address / narrative-particle / other | derived from v1 first content word post-muqaṭṭaʿāt |
| F10 | top_root_distribution | count of top-K roots (K=20) appearing | derived (consonant skeleton freq from text) |
| F11 | mean_verse_length_chars | mean character length per verse | derived |
| F12 | letter_count_in_set | size of muqaṭṭaʿāt set itself (1–5) | trivial |

For one-hot F7 we expand to 9 binary columns (one per class), not selected.
For F10 we use the top-20 most frequent roots across the 29 muqaṭṭaʿāt surahs (locked from full corpus, not letter-set-stratified) — this avoids leakage.

**No interactions, no polynomial expansion, no per-class feature selection, no hyperparameter tuning.**

## Procedure

1. Build design matrix X (29 × ~36 features after one-hot expansion + 20 root counts).
2. Train two locked classifiers (compared on LOOCV):
   - Multinomial logistic regression (sklearn `LogisticRegression(multi_class='multinomial', solver='lbfgs', C=1.0)`)
   - Random forest (sklearn `RandomForestClassifier(n_estimators=200, random_state=20260416)`)
3. **Leave-one-out CV**: for each of 29 surahs, hold out, train on 28, predict the held-out letter-set, score top-1 and top-3 accuracy.
4. **Permutation null**: 1000 shuffles of letter-set labels y; rerun the SAME LOOCV pipeline; record per-shuffle accuracy. p = (1 + #(perm_acc ≥ obs)) / (1+N_perm).
5. **Feature importance**: fit a single full-data model (logistic + RF), report standardized coefficients (logistic) and permutation importance (RF).
6. **Confusion matrix**: 14×14 LOOCV confusion of true-vs-predicted letter-sets.

## PASS criteria (locked)

- **PASS** if LOOCV top-1 accuracy ≥ 0.30 (vs chance baseline of ~6/29 if always-predicting الم = 0.207, or 1/14 ≈ 0.071 if uniform) AND permutation p < 0.05.
- **STRONG-PASS** if top-1 accuracy ≥ 0.50 AND permutation p < 0.01.
- **NULL** if top-1 accuracy ≤ majority-class baseline (0.207) OR permutation p ≥ 0.05.

## Baseline reference

- Chance (uniform random over 14): 1/14 ≈ 0.071
- Always predict الم (majority): 6/29 ≈ 0.207
- Always predict from {الم, حم}: oracle of two top classes alone covers 12/29 ≈ 0.414
- The PASS threshold of 0.30 is between always-الم (0.207) and the 2-class oracle (0.414).

## Honest expectations

This is a **harder problem than [[h-new-55-classifier|H-NEW-55]]**. Of the 14 letter-sets, 8 are SINGLETONS (one surah each), so the classifier cannot learn their pattern from training data — they will be missed in LOOCV by design. The realistic upper bound is essentially the multi-member sets: الم (6), حم (6), الر (5), طسم (2). Together those cover 19/29 = 65.5% of the data. If the classifier matches those well, top-1 accuracy could plausibly reach 0.45–0.55.

If letter-sets are essentially random with respect to all content features, top-1 accuracy will be near majority-class baseline (~0.207).

## Garden of forking paths declaration

- Two classifiers (logistic + RF) reported jointly; primary verdict uses logistic. RF is exploratory.
- Feature set locked above; no substitution after training.
- One-hot expansion of F7 is mechanical; not data-driven.
- F10 (top-20 roots) selected on full muqaṭṭaʿāt corpus before fold splits — this is acknowledged leakage of "which roots are common" but NOT of the letter-set labels.
- Top-3 accuracy reported as secondary informativeness measure (chance ≈ 3/14 = 0.214).
- Confusion matrix and per-letter-set recall reported for descriptive purposes — not used in PASS decision.

## Mechanism interpretation guide (post-hoc only)

If signal exists, possible mechanisms:
- **Position-based**: the الم-cluster (Q 2–3, 29–32) and حم-cluster (Q 40–46) reflect mushaf adjacency.
- **Length-based**: very long surahs (Q 2, 3) get الم; medium-long get حم.
- **Content-based**: book-ref + prophet-named might predict الر (Q 10–15 are nearly all prophet-named book-intros).
- **Random within constraint**: letter-sets cluster but specific assignment is contingent.

If null, then letter-set assignment is genuinely independent of these structural features — leaving the question OPEN as before.

## Outputs

- `/Users/grey/Downloads/quran/scripts/h_new_88_letter_set_predictor.py` — script
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-88.json` — full results
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-88-letter-set-predictor.md` — write-up
