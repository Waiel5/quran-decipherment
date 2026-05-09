---
surah: 35
test_id: Q035-F-03
title: Q 35 v.1 corpus-unique al-malāʾika opener test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q035-F-03-malaika-opener
alpha_bon: 0.025
---

# Q035-F-03 — Pre-registration: Q 35 v.1 al-malāʾika opener corpus-uniqueness

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** Q 35 is the **only surah in the corpus** that mentions the explicit word *al-malāʾika* (الملائكة or ملائكة, in the named-angels sense, NOT the homonym *al-mulk* which uses the same root mlk for "sovereignty / kingship") in its **first verse (v.1)**.

**H1b (secondary direction):** Q 35 is the only surah whose v.1 contains the lemma *malak* (LEM:malak per QAC v0.4).

**H0 (joint):** there exists at least one OTHER surah whose v.1 contains explicit angels-vocabulary.

**Direction:** Q 35 is corpus-UNIQUE in v.1 al-malāʾika placement.

## 2. Operational definition

- **Source**: `quran-text/quran-no-tashkeel.json` (text) + `data/morphology/quranic-corpus-morphology-0.4.txt` (lemma).
- **Surface-form test (H1)**: regex search for "الملائكة" or "ملائكة" in v.1 of all 114 surahs.
- **Lemma test (H1b)**: search for LEM:malak in v.1 across all 114 surahs.

## 3. Test statistic

- n_v1_surface = number of surahs whose v.1 contains the surface form *al-malāʾika*.
- n_v1_lemma = number of surahs whose v.1 contains LEM:malak.

## 4. Permutation null

For surface form: under the null, malāʾika tokens are distributed across verses proportional to verse-length (longer verses ⇒ more chance to contain rare phrase). Compare random-distribution probability to observed.

n_perm = 10000, seed = 20260509.

## 5. Success / Failure

- **CONFIRMED**: n_v1_surface = 1 (only Q 35) AND n_v1_lemma = 1.
- **DIRECTIONAL**: only one of H1/H1b passes.
- **NULL**: n_v1_surface > 1.
- **Pre-commit violation**: Q 35 v.1 does NOT contain the malāʾika token (impossible per direct verification, but pre-registered as a check).

## 6. Honest limits known a priori

- **Pre-flight observation**: confirmed at session-start that Q 35 is the only v.1 with explicit *al-malāʾika*. Q 62/64/67 have *al-mulk* (sovereignty) which is the SAME ROOT mlk but a DIFFERENT LEMMA. Per HANDOFF/04-DISCIPLINE.md, post-hoc origin disclosed: verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION.
- **Sūrat al-Malāʾika dual-name basis**: this test directly validates the empirical basis for the secondary canonical name (al-Malāʾika) of Q 35. The corpus-unique v.1 placement is the structural fingerprint that motivates the dual-name tradition.
- **Density vs. position**: Q 35's overall angel-token COUNT is low (1 LEM:malak instance, 2 broad-count). This test is about POSITIONAL SALIENCE (v.1 placement), not density. Q 35 is NOT a high-density angel-vocabulary surah — but it IS the unique v.1-positioning.
- **Alternative homonym filter**: must EXCLUDE *al-mulk* (kingship), *malik* (king), *Mālik* (proper name) from the v.1 search. The QAC lemma `malak` cleanly excludes these (root mlk is shared but lemma differs).

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, mashriqi)` for surface; `(QAC v0.4, lemma=malak)` for lemma test.

## 8. Bonferroni

k = 2 (surface form + QAC lemma). α_bon = 0.025.

## 9. Coordination

This test is unique to Q 35 — no other specialist has run it.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q035_F_03_malaika_opener.py`, verified at runtime.
