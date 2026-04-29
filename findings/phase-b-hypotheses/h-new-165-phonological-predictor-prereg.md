---
id: H-NEW-165
title: Classical-Arabic phonological-feature predictor for muqaṭṭaʿāt letter-set identity (OQ-1 attack)
phase: B
status: PRE-REGISTERED (locked)
date: 2026-04-17
agent: h-new-165-autonomous
parent: H-NEW-88 (RF LOOCV top-1 = 0.4138 content-feature baseline)
parent_null_1: H-NEW-96 (92-feature content extension NULL; 0.379 < 0.414)
parent_null_2: H-NEW-96.2 (14-feature rhyme predictor NULL; 0.310 < 0.414)
open_question: OQ-1 (why does each muqaṭṭaʿāt surah get its specific letter-set?)
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-165-phonological-predictor
alpha_bon: 0.025
direction_primary: "RF LOOCV top-1 > 0.50 (strong-signal threshold, strictly > H-NEW-88 baseline 0.414)"
direction_secondary: "≥ 1 of 8 singletons correctly predicted (OQ-1 phonological-axis progress)"
acceptance_window: "permutation p < 0.025 for primary AND observed top-1 > 0.50 (Bonferroni-2 for 2-family)"
rules_tuple: "(no-tashkeel; canonical 14 distinct letter-sets; hafs-kufan; locked classical tajwīd feature codebook; LOOCV on 29 surahs; RF primary, logistic secondary; seed 20260419)"
---

# [[h-new-165-phonological-predictor|H-NEW-165]] — Classical-Arabic phonological-feature predictor for muqaṭṭaʿāt letter-set identity

## Classical / project anchor

The muqaṭṭaʿāt discourse in classical Arabic grammar and tajwīd has long distinguished these letters by their *phonological profile* (makhraj, ṣifa, tafkhīm), not only by their lexical/semantic use. E.g.,
- Al-Khalīl b. Aḥmad organised Kitāb al-ʿAyn by makhraj (place of articulation), the pharyngeal letters first.
- Ibn Jinnī (*Sirr Ṣināʿat al-Iʿrāb* I.46ff.) catalogues the ṣifāt (manner-features) of each letter.
- The 14 muqaṭṭaʿāt letters are exactly HALF the 28-letter alphabet; classical writers (al-Suyūṭī *Itqān* III, §36) noted that the 14 include all SEVEN mustaʿliya (emphatic/raised letters).
- Modern phonological coding (Watson 2002, *Phonology & Morphology of Arabic*) supplies a consistent feature-bundle per letter.

[[h-new-88-letter-set-predictor|H-NEW-88]] showed content/surface features predict muq letter-set at 0.414 (permutation p = 0.002, well above chance 0.071). [[h-new-96-predictor-extension|H-NEW-96]] (content extension to 92 features) and H-NEW-96.2 (rhyme features, 14 one-hot) both came in BELOW the 0.414 baseline — NULL. OQ-1 remains open.

**This hypothesis**: the muqaṭṭaʿāt letter-set assignment is determined not by content, not by rhyme alone, but by the *phonological profile* of the surah's letter-set when summarised as a mean feature-vector. If classical tajwīd classification has any predictive power over muq assignment, a phonologically-coded feature-vector should beat content baselines.

## Hypothesis (pre-registered)

**H1 (primary)**: A surah-level mean classical-phonological feature vector (aggregated over its muq letter-set) predicts letter-set identity at RF LOOCV top-1 > 0.50. This would be the FIRST positive OQ-1 phonological signal.

**H2 (secondary)**: With phonological features, ≥ 1 of 8 singleton letter-sets (ص=S, ق=Q, ن=N, طه=TH, يس=YS, طس=TS, كهيعص=KHYAS, حمعسق=HMASQ) will be correctly predicted in LOOCV.

## Feature codebook (LOCKED before any training)

For each of the 14 muqaṭṭaʿāt letters, encode classical tajwīd phonological features as numerical columns. Features are grounded in Ibn Jinnī / al-Jurjānī / modern Semitic-phonology standard tables (Watson 2002, Holes 2004).

### Per-letter feature vector (one row per muq letter)

| Letter | makhraj | voice | manner | emphatic | pharyngealized | sonorant | continuant | idhlāq | vowel_carrier |
|--------|---------|-------|--------|----------|----------------|----------|------------|--------|---------------|
| ا      | 8 (glottal/vowel) | 0 | 0 (vowel) | 0 | 0 | 1 | 1 | 0 | 1 |
| ل      | 3 (alveolar) | 1 | 4 (lateral) | 0 | 0 | 1 | 1 | 1 | 0 |
| م      | 1 (labial) | 1 | 5 (nasal) | 0 | 0 | 1 | 1 | 1 | 0 |
| ر      | 3 (alveolar) | 1 | 6 (trill) | 0 | 0 | 1 | 1 | 1 | 0 |
| ص      | 3 (alveolar) | 0 | 2 (fricative) | 1 | 1 | 0 | 1 | 0 | 0 |
| ك      | 5 (velar) | 0 | 1 (stop) | 0 | 0 | 0 | 0 | 0 | 0 |
| ه      | 8 (glottal) | 0 | 2 (fricative) | 0 | 0 | 0 | 1 | 0 | 0 |
| ي      | 4 (palatal) | 1 | 3 (glide) | 0 | 0 | 1 | 1 | 0 | 1 |
| ع      | 7 (pharyngeal) | 1 | 2 (fricative) | 0 | 1 | 0 | 1 | 0 | 0 |
| ط      | 3 (alveolar) | 1 | 1 (stop) | 1 | 1 | 0 | 0 | 0 | 0 |
| س      | 3 (alveolar) | 0 | 2 (fricative) | 0 | 0 | 0 | 1 | 0 | 0 |
| ح      | 7 (pharyngeal) | 0 | 2 (fricative) | 0 | 1 | 0 | 1 | 0 | 0 |
| ن      | 3 (alveolar) | 1 | 5 (nasal) | 0 | 0 | 1 | 1 | 1 | 0 |
| ق      | 6 (uvular) | 0 | 1 (stop) | 0 | 1 | 0 | 0 | 0 | 0 |

Where:
- `makhraj` ∈ {1..8} = {labial, labio-dental, alveolar, palatal, velar, uvular, pharyngeal, glottal} (classical 8-tier al-Khalīl scheme, numeric ordinal ~ "back-ness")
- `voice` ∈ {0,1} = jahr (voiced) vs hams (voiceless). Note classical ṣād is sometimes classified ambiguously; we follow Ibn Jinnī's majhūra = jahr for consistency with modern phonetics: actually ṣ is hams (voiceless). Correction: ṣ = 0 (hams/voiceless), ṭ = classically majhūra but modern voicing disputed → we code by classical jahr/hams table: majhūr (1) = {ا, ل, م, ر, ي, ع, ط, ن, ظ, ب, د, ذ, ز, ض, غ, و, ء}; mahmūs (0) = {ص, ك, ه, س, ح, ق, ش, ث, ف, ت, خ, ه}. We apply this to the 14 muq letters.
- `manner` ∈ {0..6} = {0=vowel/carrier, 1=stop, 2=fricative, 3=glide, 4=lateral, 5=nasal, 6=trill}
- `emphatic` ∈ {0,1} = one of the 7 ḥurūf al-tafkhīm {خ, ص, ض, ط, ظ, غ, ق} (of muq letters: ص ط ق)
- `pharyngealized` ∈ {0,1} = mustaʿliya (raised tongue-body) subset: {خ, ص, ض, ط, ظ, غ, ق} ∪ pharyngeals {ع, ح}. For muq letters: {ص, ط, ق, ع, ح}
- `sonorant` ∈ {0,1} = {ا, ل, م, ر, ي, ن, و} and semivowels (traditional "soft" letters)
- `continuant` ∈ {0,1} = opposed to stops {ك, ط, ق, ب, د, ت, ء}
- `idhlāq` ∈ {0,1} = classical 6 "fluent" letters of al-Khalīl: {ف, ر, م, ن, ل, ب} (of muq: ر م ن ل)
- `vowel_carrier` ∈ {0,1} = {ا, ي, و} (weak/vowel-bearers)

### Surah-level aggregation

For each of 29 muq surahs with letter-set L_s = {letter_i, ...}:

  `feature_vector(s)_j = mean over letter_i in L_s of feature_j(letter_i)`

→ 9-dim feature vector per surah. Example: Q2 (ALM = {ا, ل, م}):
  makhraj_mean = (8+3+1)/3 = 4.0
  voice_mean = (0+1+1)/3 = 0.667 (NB: ا voice coded 0 per above correction)
  emphatic_mean = 0
  pharyngealized_mean = 0
  etc.

Additional aggregate features (also locked):
- `letter_count` (size of letter-set, already in [[h-new-88-letter-set-predictor|H-NEW-88]], retained for comparability): 1..5
- `frac_emphatic`: fraction of set-letters that are ḥurūf al-tafkhīm
- `frac_pharyngeal`: fraction that are pharyngeal/emphatic (mustaʿliya)
- `frac_sonorant`: fraction that are sonorants
- `frac_idhlāq`: fraction that are idhlāq letters
- `has_qalqala_letter`: 1 if set contains {ق, ط} (classical qalqala letters {ق, ط, ب, ج, د} intersected with muq alphabet)

**Total locked feature dimension**: 9 (per-letter means) + 1 (letter_count) + 4 (fractions) + 1 (has_qalqala) = **15 features**.

## Procedure (locked)

1. Build 29 × 15 design matrix X (phonological aggregates), label vector y (14 muq letter-set classes).
2. LOOCV with RandomForestClassifier(n_estimators=200, random_state=20260419) as PRIMARY.
3. LOOCV with LogisticRegression(C=1.0, L2, lbfgs, max_iter=2000) as SECONDARY.
4. Compute top-1, top-3, top-5 accuracy.
5. Per-class recall (14 entries); per-singleton accuracy (8 entries).
6. Permutation null: shuffle y 1000×, redo LOOCV; compute top-1 distribution.
7. **MW-5 positive control**: cheat_surah_id alone → expected LOOCV top-1 ≈ 0.517 ([[h-new-96-predictor-extension|H-NEW-96]] structural ceiling under LOOCV; NOT 1.0 because singletons can't vote their own class).
8. Report all metrics BEFORE interpretation.

## Verdict decision rule (locked)

Per Bonferroni-2 on the 2-test family (primary top-1 > 0.50, secondary any-singleton-hit):
- **PASS-STRONG (joint)**: top-1 > 0.50 AND perm p < 0.025 AND ≥ 1 singleton correctly predicted
- **PASS-PRIMARY**: top-1 > 0.50 AND perm p < 0.025 (but no singleton hit)
- **PASS-SECONDARY**: ≥ 1 singleton hit (but top-1 ≤ 0.50) — weak OQ-1 progress signal only
- **PASS-WEAK**: top-1 > 0.414 (beats [[h-new-88-letter-set-predictor|H-NEW-88]]) AND perm p < 0.05 (standard uncorrected)
- **NULL**: top-1 ≤ 0.414 OR perm p ≥ 0.025 (under Bonferroni-2) — phonology also doesn't predict letter-set

MW-5 positive control MUST yield top-1 ≥ 0.45 (close to [[h-new-96-predictor-extension|H-NEW-96]]'s 0.517 structural ceiling) for any other verdict to stand; else report NULL-BROKEN-PIPELINE.

## Bonferroni correction

- `bonferroni_k = 2` (primary top-1 + secondary singleton-hit)
- `alpha_bon = 0.025`
- `bonferroni_family = [[h-new-165-phonological-predictor|h-new-165]]-phonological-predictor`

## Garden-of-forking-paths log

1. **Feature codebook pre-committed**: 15 features (9 per-letter means + letter_count + 4 fractions + has_qalqala). NO post-hoc addition of n-gram, bigram, or word-level features.
2. **Classical feature sources**: al-Khalīl makhraj scheme (8-tier ordinal), Ibn Jinnī ṣifāt, standard modern Semitic phonology tables. No feature tuning to improve accuracy.
3. **Aggregation**: MEAN over letter-set for ordinal features, FRACTION for binary features. No alternate aggregations (max, sum) tested.
4. **Primary classifier = RF** (matches [[h-new-88-letter-set-predictor|H-NEW-88]] / [[h-new-96-predictor-extension|H-NEW-96]] for direct comparability). Logistic secondary.
5. **Seed 20260419** (locked; distinct from parent 20260417 to avoid correlated-seed cherry-pick).
6. **Letter-set size is included** as a redundant feature-overlap with [[h-new-88-letter-set-predictor|H-NEW-88]]. Not a circularity violation (it was in both parents).
7. **LOOCV structural ceiling is 0.655** for multi-member classes; singletons structurally UNPREDICTABLE in LOOCV (disclosed).
8. **Permutation null**: 1000 shuffles, seed 20260419.
9. **No per-fold feature recomputation needed**: the phonological features are letter-set-intrinsic (no surah-text-derived leakage).
10. **No post-hoc threshold change**: primary > 0.50 is locked per task-spec; PASS-WEAK at 0.414 is reported for continuity but NOT treated as primary.

## Expected outcome (pre-committed)

Given that:
- [[h-new-88-letter-set-predictor|H-NEW-88]] content features got 0.414 — better than chance but unable to beat the mushaf-adjacency structural bias.
- [[h-new-96-predictor-extension|H-NEW-96]] and H-NEW-96.2 both NULL.
- The phonological feature space has only 9 ordinal + 5 binary = 14 dimensions (vs. 92 in [[h-new-96-predictor-extension|H-NEW-96]]), so is LESS overfittable.
- Classical tafsīr (e.g., Ibn Taymiyya, Rāshid Riḍā) has speculated phonological patterns in muq letters without quantitative test.

**Honest default expectation**: top-1 ≈ 0.35–0.50 (comparable to rhyme-null H-NEW-96.2's 0.310, possibly pushed slightly higher by the `letter_count` feature which survived [[h-new-88-letter-set-predictor|H-NEW-88]]). Singleton hits UNLIKELY under LOOCV because they can't vote their own class.

**PASS would be genuinely novel**: first positive OQ-1 signal on the phonological axis, consistent with classical tajwīd intuition.

**NULL is the equal-weight outcome** and narrows the OQ-1 search space (content, rhyme, phonology all NULL → OQ-1 letter-set assignment may be arbitrary-by-design or require a fundamentally different feature space, e.g., intra-surah root-letter distribution).

## Files

- Pre-reg: this file
- Script: `scripts/h_new_165_phonological_predictor.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-165.json`
- Findings: `findings/phase-b-hypotheses/h-new-165-phonological-predictor.md`
- Journal: `journal/h-new-165-run-1.md`

## Cross-references

- Parent baseline: [[h-new-88-letter-set-predictor|H-NEW-88]] (content features, top-1 = 0.414)
- Parent NULL 1: [[h-new-96-predictor-extension|H-NEW-96]] (92-feature content extension NULL, 0.379)
- Parent NULL 2: H-NEW-96.2 (14-feature rhyme NULL, 0.310)
- OQ-1 phonological-axis attack; queued after result: H-NEW-165.1 (per-letter one-hot as fall-back)
