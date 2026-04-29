---
id: H-NEW-96
title: Multi-class muqaṭṭaʿāt LETTER-SET predictor — NEW feature extension (OQ-1 singleton probe)
phase: B
status: PRE-REGISTERED (locked)
date: 2026-04-17
agent: h-new-96-specialist
parent: H-NEW-88 (RF LOOCV top-1 = 0.414, perm p = 0.002)
open_question: OQ-1 (why does each muqaṭṭaʿāt surah get its specific letter-set?)
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-96-predictor-extension
alpha_bon: 0.025
direction_primary: "top-1 LOOCV > 0.50 (strictly > H-NEW-88's 0.414)"
direction_secondary: "≥1 of the 8 singletons correctly predicted"
acceptance_window: "permutation p < 0.025 for primary AND observed top-1 > 0.50"
rules_tuple: "(no-tashkeel; canonical 14 distinct letter-sets; hafs-kufan; locked feature set before training; LOOCV on 29 surahs; seed 20260417)"
---

# [[h-new-96-predictor-extension|H-NEW-96]] — Predictor extension: can NEW features crack the 8 singletons?

## Classical / project anchor

- **Parent**: [[h-new-88-letter-set-predictor|H-NEW-88]] multi-class classifier (RF top-1 = 0.4138, perm p = 0.002). The 3 multi-member clusters (ALM / HM / ALR) are predicted at 60-83% recall. The 8 singletons (ص, ق, ن, طه, يس, طس, كهيعص, حمعسق) are NOT predictable because LOOCV holds out the only example of each class.
- **OQ-1** asks: can DEEPER features (opening-word category, formulaic-opening template, top-K root distribution, divine-name pattern, content classification) make the singletons predictable — even partially?
- **[[h-new-61-opening-words|H-NEW-61]]** provides the 9-class opening-word taxonomy and the top-10 repeated-incipit formulas.
- **[[h-new-57-formulaic-openings|H-NEW-57]]** documented the "tilka āyāt al-kitāb" / "wa-l-qurʾān" formulaic-opening exclusivity (13/13 muqaṭṭaʿāt, p = 1.6 × 10⁻⁹).
- **[[h-new-86-surah-name-as-key-root|H-NEW-86]]** provides the surah-name-as-key-root concentration counts.
- **[[h-new-49-surah-name-class|H-NEW-49]]** provides the 9-class surah-name taxonomy (already used in [[h-new-88-letter-set-predictor|H-NEW-88]]; retained).

## Hypothesis (pre-registered)

**H1 (primary)**: Adding the NEW features (enumerated below) will lift LOOCV top-1 accuracy to >0.50 — strictly better than [[h-new-88-letter-set-predictor|H-NEW-88]]'s 0.414. This corresponds to capturing at least ~15 of 29 surahs correctly.

**H2 (secondary)**: With richer features capturing opener-specific signatures, at least 1 of the 8 singleton letter-sets (ص, ق, ن, طه, يس, طس, كهيعص, حمعسق) will be predicted correctly (it would be mis-routed to its single class in a LOOCV fold by the model; i.e., top-1 prediction for that held-out surah matches its true set).

## Feature space (LOCKED before any model training, before viewing any result)

Features partitioned into **BASELINE** (from [[h-new-88-letter-set-predictor|H-NEW-88]]) and **NEW** (from the task spec).

### BASELINE (retained from [[h-new-88-letter-set-predictor|H-NEW-88]])

- F1: `length` (verse count)
- F2: `period_meccan` (1/0)
- F3: `noldeke_order` (integer chronology rank)
- F4: `mushaf_index` (surah id, 1-114)
- F5: `book_ref_v1_3` ([[h-new-53-muqattaat-book-reference|H-NEW-53]]; 1 if kitāb/qurʾān root in v1-3)
- F6: `prophet_named` ([[h-new-49-1-prophet-enrichment|H-NEW-49.1]]; 1 if surah-name = prophet name)
- F7: `name_class_*` one-hot over [[h-new-49-surah-name-class|H-NEW-49]]'s 9 classes
- F8: `divine_name_density` (99-names tokens / total tokens)
- F9: `mean_verse_length_chars`
- F10: `letter_count_in_set` (1-5)

### NEW (this study; locked)

**G1 — Opening-word class ([[h-new-61-opening-words|H-NEW-61]] 9-class taxonomy)** — one-hot, 9 features
- OATH_PARTICLE, OTHER_CONTENT, REPORT_ASSERTIVE, PRAISE, VOCATIVE,
  DEMONSTRATIVE_PRONOMINAL, CONDITIONAL_TEMPORAL, IMPERATIVE, INTERROGATIVE_NEGATIVE
- Derived from the first word AFTER the muqaṭṭaʿāt-token-run AND after basmala,
  using the [[h-new-61-opening-words|H-NEW-61]] extractor (reimplemented here, validated against [[h-new-61-opening-words|H-NEW-61]] JSON).

**G2 — Formulaic-opening template ([[h-new-57-formulaic-openings|H-NEW-57]]/61)** — one-hot, 8 features
  (binary presence flags; a surah may be tagged at most one)
- FORMULA_tilka_ayat_al_kitab (*tilka āyāt al-kitāb*, 7 surahs)
- FORMULA_tanzil_al_kitab (*tanzīl al-kitāb / mina-llāh*, 4 surahs)
- FORMULA_wa_l_quran (*wa-l-qurʾān*, Q 36, 38, 50 — 3 surahs)
- FORMULA_wa_l_kitab_al_mubin (Q 43, 44 — 2 surahs)
- FORMULA_ha_mim_tanzil (*ḥm tanzīl*, ḥm surahs with tanzīl in v2-3)
- FORMULA_ya_ayyuha_l_nabi (Q 33/65/66)
- FORMULA_other_named (any of the other [[h-new-61-opening-words|H-NEW-61]] top-10 repeated incipits)
- FORMULA_none (default fallback)

**G3 — Top-30 root distribution** — 30 features (EXTENDED from [[h-new-88-letter-set-predictor|H-NEW-88]]'s top-20)
- Top-30 most-frequent 3-character consonant skeletons across the 29 muqaṭṭaʿāt
  corpus (same extraction rule as [[h-new-88-letter-set-predictor|H-NEW-88]] `lock_top_roots_from_muq_corpus`;
  K = 30 instead of 20). Per-surah count of each.

**G4 — Divine-name presence (top-20 names)** — 20 binary features
- For the 20 most-frequently-occurring divine names across the muqaṭṭaʿāt
  corpus (derived from `data/asma-al-husna.txt`, counts computed across the
  29 muqaṭṭaʿāt surahs once; locked set), presence/absence per surah (≥1 vs 0).

**G5 — Name-root concentration ([[h-new-86-surah-name-as-key-root|H-NEW-86]])** — 1 continuous + 1 binary = 2 features
- `name_root_count_in_surah`: occurrences of the surah's name lemma/root
  inside the surah (from `[[h-new-86-surah-name-as-key-root|h-new-86]]-per-surah.csv` field `hits_in`)
- `name_root_sig_bon`: 1 if that surah is Bonferroni-114 sig per [[h-new-86-surah-name-as-key-root|H-NEW-86]]
  (`sig_bon` field), else 0

**G6 — Content-classification (narrative / legal / eschatological / wisdom / polemic)** — 5-way one-hot, 5 features
- DERIVED from [[h-new-49-surah-name-class|H-NEW-49]] name-class mapping for muqaṭṭaʿāt surahs,
  with a small LOCKED mapping table for the 29 muqaṭṭaʿāt surahs
  (see block below). NO result-viewed-based assignments.
- Classes: NARRATIVE (prophet-stories dominant), LEGAL (ethical/social norms),
  ESCHATOLOGICAL (day-of-judgment dominant), WISDOM (reflection/discourse),
  POLEMIC (argument-against-deniers dominant)

The 29-surah content-class mapping is pre-committed HERE based on standard
tafsir synopses (Ṣābūnī's Ṣafwat al-Tafāsīr headers + Wherry/Yusuf Ali
Surah intros — a classical-consensus summary, not a post-hoc re-reading):

| Surah | Letter-set | Content-class (pre-committed) |
|---|---|---|
| 2 al-Baqarah | ALM | LEGAL |
| 3 Āl-ʿImrān | ALM | LEGAL |
| 7 al-Aʿrāf | ALMS | NARRATIVE |
| 10 Yūnus | ALR | NARRATIVE |
| 11 Hūd | ALR | NARRATIVE |
| 12 Yūsuf | ALR | NARRATIVE |
| 13 al-Raʿd | ALMR | POLEMIC |
| 14 Ibrāhīm | ALR | NARRATIVE |
| 15 al-Ḥijr | ALR | NARRATIVE |
| 19 Maryam | KHYAS | NARRATIVE |
| 20 Ṭāhā | TH | NARRATIVE |
| 26 al-Shuʿarāʾ | TSM | NARRATIVE |
| 27 al-Naml | TS | NARRATIVE |
| 28 al-Qaṣaṣ | TSM | NARRATIVE |
| 29 al-ʿAnkabūt | ALM | POLEMIC |
| 30 al-Rūm | ALM | POLEMIC |
| 31 Luqmān | ALM | WISDOM |
| 32 al-Sajdah | ALM | ESCHATOLOGICAL |
| 36 Yā-Sīn | YS | ESCHATOLOGICAL |
| 38 Ṣād | S | NARRATIVE |
| 40 Ghāfir | HM | POLEMIC |
| 41 Fuṣṣilat | HM | POLEMIC |
| 42 al-Shūrā | HMASQ | POLEMIC |
| 43 al-Zukhruf | HM | POLEMIC |
| 44 al-Dukhān | HM | ESCHATOLOGICAL |
| 45 al-Jāthiyah | HM | ESCHATOLOGICAL |
| 46 al-Aḥqāf | HM | NARRATIVE |
| 50 Qāf | Q | ESCHATOLOGICAL |
| 68 al-Qalam | N | POLEMIC |

(This is committed ONCE and locked. No reassignment based on model feedback.)

**G7 — Cheat positive control (MW-5)** — 1 feature, used ONLY for positive-control test
- `cheat_surah_id` — when used as the sole feature, LOOCV top-1 must equal 1.0
  by structural-memorization (each held-out surah has a unique id). This is
  the MW-5 positive control. NOT included in the primary feature matrix.

### Final feature count (primary matrix)

- Baseline: 6 + 9 + 1 + 1 + 1 = 18
- NEW G1-G6: 9 + 8 + 30 + 20 + 2 + 5 = 74
- **TOTAL: 92 features × 29 surahs**

The primary matrix has p >> n (92 > 29). Random Forest and L2-regularized
logistic regression both handle p >> n; sparse lasso logistic is added as a
sanity check (but PRIMARY reporting uses RF, matching [[h-new-88-letter-set-predictor|H-NEW-88]]).

## Procedure (locked)

1. Build design matrix X (29 × 92), label vector y (14 classes, 29 samples)
2. Run LOOCV with both RandomForestClassifier (n_estimators=200, random_state=20260417)
   and LogisticRegression (C=1.0, L2, solver='lbfgs', max_iter=2000)
3. Compute top-1, top-3, top-5 LOOCV accuracy
4. Compute per-class recall (14 entries)
5. **Per-singleton accuracy**: separately report whether each of the 8
   singleton-class surahs (Q 38, 50, 68, 20, 36, 27, 19, 42) was correctly
   predicted
6. Permutation null: shuffle y 1000×, redo LOOCV (same RF hyperparameters),
   compute top-1 distribution
7. Feature-importance: RF built-in + logistic |coef| averaged over classes
8. **MW-5 positive control**: train on cheat_surah_id alone; verify LOOCV top-1 = 1.0
9. Report all of the above BEFORE interpretation

## Verdict decision rule (locked)

Primary test: **RF LOOCV top-1 > 0.50 AND permutation p < 0.025**
  → PASS-STRONG

Primary: **RF LOOCV top-1 > 0.414 AND permutation p < 0.05**
  → PASS-WEAK (modest improvement over [[h-new-88-letter-set-predictor|H-NEW-88]])

Secondary test (independent of primary): **≥1 singleton correctly predicted**
  → OQ-1-PROGRESS

- If primary = PASS-STRONG AND OQ-1-PROGRESS: **JOINT-PASS** (OQ-1 partially answered)
- If primary = PASS-STRONG alone: PASS (no singleton-level progress)
- If primary fails and no singleton hit: **NULL** — publish with same prominence
- MW-5 positive control MUST pass (LOOCV top-1 = 1.0) for any other verdict to stand

## Bonferroni correction

- `bonferroni_k = 2` (primary top-1 threshold + secondary singleton-hit)
- `alpha_bon = 0.025`
- `bonferroni_family = [[h-new-96-predictor-extension|h-new-96]]-predictor-extension`

The secondary (≥1 singleton) is not a traditional p-value test — it is a
deterministic LOOCV outcome; we report permutation p for the singleton-hit
event (probability that random-label-shuffle would produce ≥1 singleton hit).

## Garden-of-forking-paths log

1. **Feature selection pre-committed**: all 92 features listed above are
   locked BEFORE any model training. No post-hoc feature pruning.
2. **Classifier choice**: RF (primary) matches [[h-new-88-letter-set-predictor|H-NEW-88]] for direct
   comparability. Logistic (secondary) for sanity check.
3. **Hyperparameter**: RF n_estimators=200, random_state=20260417 — same as
   [[h-new-88-letter-set-predictor|H-NEW-88]] modulo seed (20260417 per handoff discipline for this session).
   This is a MINOR divergence from [[h-new-88-letter-set-predictor|H-NEW-88]]'s seed 20260416 and is disclosed.
4. **Content-class mapping**: the 5-way NARRATIVE/LEGAL/ESCHAT/WISDOM/POLEMIC
   assignment is committed ONCE in this document, based on standard tafsir
   synopses. It is NOT revised after seeing any model output.
5. **Formulaic-opening template (G2)**: derived DIRECTLY from the [[h-new-61-opening-words|H-NEW-61]]
   incipit list in the published finding file; no re-classification.
6. **Top-20 divine names (G4)**: derived from `asma-al-husna.txt` by counting
   raw occurrences in the 29 muqaṭṭaʿāt surahs and taking top-20. This IS
   leakage of "which names are common in muqaṭṭaʿāt surahs" but NOT of the
   letter-set labels — same leakage profile as [[h-new-88-letter-set-predictor|H-NEW-88]]'s top-20 roots,
   acknowledged.
7. **Top-30 roots (G3)**: same extraction as [[h-new-88-letter-set-predictor|H-NEW-88]] but K=30 instead of K=20.
8. **Singleton secondary**: chosen because singleton-prediction is the
   substantive OQ-1 question. Pre-registered BEFORE running.
9. **Permutation null**: 1000 shuffles, same seed family.
10. **Sensitivity reporting**: if primary fails, we additionally report what
    happens without G3 (top-30 roots) to test whether ROOT noise suppressed
    the other features — this is a DISCLOSED sensitivity cell, not a cherry-pick.

## Expected outcome (pre-committed)

Given that:
- The 8 singletons have NO other training examples of their own class (LOOCV
  holds the only one out, so the model cannot output that class label)
- The 3 multi-member clusters already achieve 60-83% recall in [[h-new-88-letter-set-predictor|H-NEW-88]]

The STRUCTURAL CEILING for LOOCV top-1 without cross-class confusion is:
  - Perfect multi-member: 6 ALM + 6 HM + 5 ALR + 2 TSM = 19/29 = 0.655
  - Singletons cannot be correctly assigned (no class to vote for them)
  - Unless the classifier learns to vote a singleton class for a held-out
    multi-member surah (very unlikely given class imbalance)

Therefore **the best H1 could achieve** is ~0.655. We predict PASS-STRONG
(>0.50) is plausible with ~17/29 correct; PASS-WEAK (>0.414) is very likely;
singleton-hit (H2) is UNLIKELY because the LOOCV structural constraint
normally forces singleton-held-out surahs to be predicted as the nearest
multi-member class.

**Honest default expectation**: mild improvement (maybe 0.45-0.48),
possibly PASS-WEAK, likely no singleton hits. Report the full result either way.

## MW-5 positive control

Fit the RF on [cheat_surah_id] alone, LOOCV → expected top-1 = 1.0 (each
surah id is unique, so the tree can memorize). Report actual result.

If MW-5 positive control FAILS (acc < 1.0 on cheat), the entire pipeline is
broken and we report NULL-BROKEN-PIPELINE.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_96_predictor_extension.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-96.json`
- Findings: `findings/phase-b-hypotheses/h-new-96-predictor-extension.md`
- Journal: `journal/h-new-96-run-1.md`

## Cross-references

- Parent: [[h-new-88-letter-set-predictor|H-NEW-88]] (current best)
- [[h-new-61-opening-words|H-NEW-61]] (opening-word taxonomy, G1 / G2 source)
- [[h-new-57-formulaic-openings|H-NEW-57]] (formulaic-opening exclusivity)
- [[h-new-86-surah-name-as-key-root|H-NEW-86]] (surah-name root concentration)
- [[h-new-49-surah-name-class|H-NEW-49]] (name-class taxonomy)
- [[h-new-53-muqattaat-book-reference|H-NEW-53]] (book-reference)
- OQ-1 (open question being probed)
