---
surah: 78
test_id: Q078-F-03
title: Corpus-EXACT 2-pair-match — Q 78:4-5 / Q 102:3-4 *kallā sa-yaʿlamūn / thumma kallā sa-yaʿlamūn*
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q078-F-03-kalla-formula
alpha_bon: 0.05
---

# Q078-F-03 — Pre-registration: *kallā sa-yaʿlamūn / thumma kallā sa-yaʿlamūn* corpus-EXACT pair-match test

## 1. Hypothesis (locked before observation)

**H1 (corpus-EXACT count, single-test):** The 2-verse formula sequence "كلا سيعلمون" (v) followed by "ثم كلا سيعلمون" (v+1) — both as exact verse-text matches after no-tashkeel normalization — occurs in EXACTLY 2 corpus locations: Q 78:4-5 AND Q 102:3-4.

**H0:** any count ≠ 2.

**Direction**: corpus-EXACT 2.

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Match-strict**: exact regex `^كلا سيعلمون$` for v; exact regex `^ثم كلا سيعلمون$` for v+1; consecutive-verse pair within a single surah.
- **No-tashkeel + alif-variant + final-yāʾ normalization** is unnecessary because the regex matches the exact orthographic-token form of the 2-3 word verse.

## 3. Test statistic

- N_pair_matches = corpus count of consecutive-verse-pairs satisfying the match-strict criteria.
- Pre-locked: N = 2.

## 4. Null

This is a corpus-EXACT-count claim (single-test). The null is "any count ≠ 2." No permutation test; the count is observable directly.

## 5. Success / Failure

- **CONFIRMED-EXACT**: N_pair_matches = 2.
- **DIRECTIONAL**: N_pair_matches > 2 (more pairs than expected, in the direction of "Q 78 has the formula but it's NOT corpus-EXACT 2-pair").
- **NULL**: N_pair_matches < 2 OR ≠ 2.

## 6. Honest limits known a priori

- The Q 78:4-5 formula and Q 102:3-4 formula are both already known from pre-flight inspection. This pre-reg formalizes the corpus-EXACT count claim, not a discovery claim.
- Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol": single-test α=0.05 cap applies. Verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION (e.g., character-n-gram replication; verb-tense variation).
- Single-formula occurrences (each formula alone, NOT in the consecutive-pair) are documented as auxiliary data, NOT as primary test outcomes.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, exact-match-regex, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 1 (single-test). α_bon = 0.05.

## 9. Coordination

No prior surah specialist has tested this exact pair-match. No duplication.

## 10. SHA256 lock

Computed at write-time; embedded into `scripts/Q078_F_03_kalla_formula.py`; verified at runtime.
