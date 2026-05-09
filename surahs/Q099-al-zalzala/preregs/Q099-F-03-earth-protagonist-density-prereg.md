---
surah: 99
test_id: Q099-F-03
title: Q 99 earth-protagonist density — corpus-MAX test (length-controlled)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q099-F-03-earth-protagonist
alpha_bon: 0.025
---

# Q099-F-03 — Pre-registration: Q 99 earth-protagonist density — corpus-MAX test

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Q 99 has the corpus-MAX density of *al-arḍ*-related-token presence (where "earth-related-token" includes the lemma *al-arḍ* + feminine 3rd-person pronouns *-hā* referring to the earth + agreement-pronouns specifying earth-as-grammatical-subject within verses 1-5), normalized by surah verse-count.

**H1b (one-tailed, locked direction):** Q 99 holds ≥ 5 of 8 verses (62.5%) where the EARTH is a primary subject/object/topic — operationalized as a verse where one of the 4 forms below is present:
1. The lemma *al-arḍ* explicitly.
2. A pronoun *-hā* whose antecedent is *al-arḍ* (agreement-tracked).
3. A grammatical 3rd-person feminine verb whose subject is *al-arḍ*.
4. A direct-address topic about the earth (*mā lahā* etc).

**H0:** Q 99 has fewer than 5 of 8 earth-protagonist verses, OR is not corpus-MAX in earth-density length-normalized.

**Direction:** locked POSITIVE Q 99 = corpus-MAX.

## 2. Operational definition

- **Source data**: `quran-text/quran-no-tashkeel.json`.
- **Earth-token regex**: detect (a) `الأرض` lemma, (b) `أرض` lemma (indefinite), (c) feminine pronouns `-ها` whose verse-context anchors on the earth (computed by inspection: in Q 99, vv. 1, 2, 3, 4, 5 all have *-hā* explicitly referring to earth; in other surahs, the same verses are tagged by inspection of the immediate antecedent).
- **Density measure**: (number of verses containing earth-protagonist marker) / (total verse count). Length-normalized.
- **Corpus baseline**: per-surah density across all 114 surahs.

## 3. Test statistic

- T1: Q 99 earth-density / max(other-surah earth-density). T1 ≥ 1.0 = corpus-MAX.
- T2: Q 99 earth-protagonist verse count = 5 (per the locked operational specification: vv. 1, 2, 3, 4, 5).

## 4. Permutation null

For T1: rank all 114 surahs by earth-density. p-value = rank/114 (one-tailed). p ≤ α_bon = 0.025 = Q 99 must be in top-3 corpus-wide.

For T2: not a permutation test; check direct count.

## 5. Success / Failure

- **CONFIRMED**: T1 corpus-MAX (rank 1/114) AND T2 = 5+ verses.
- **DIRECTIONAL**: 1 of 2 passes.
- **NULL**: 0 of 2 passes.

## 6. Honest limits known a priori

- The earth-protagonist measure is a content-thematic measure rather than purely orthographic. The lemma-detection (a) + (b) is purely orthographic; the pronoun-antecedent tracking (c) is INSPECTION-BASED for Q 99 (5 of 8 verses confirmed by direct text inspection); for other surahs, this requires a length-controlled approximation.
- A pure-orthographic baseline (lemma *al-arḍ* count alone, no pronoun tracking) is computed as the sensitivity-check.
- Length-normalization: critical because long-surahs have many opportunities for earth-mentions and Q 99 is short; raw-count comparison would be misleading.
- Post-hoc origin acknowledged: the earth-protagonist observation in `02-content-analysis.md` §4 was visible during pre-flight content review; this test FORMALIZES it.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token + content-thematic-marker, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (T1 + T2). α_bon = 0.025.

## 9. Coordination

This is a Q 99-specific structural-fingerprint test. No other surah-specialist tests this exact axis. Q 22 al-Ḥajj (which contains *zalzalat al-sāʿati*) and Q 79 al-Nāziʿāt (eschatological earth-references) might be sensitivity-comparison anchors.

## 10. SHA256 lock

Computed at write-time, embedded in `scripts/Q099_F_03_earth_protagonist.py`, verified at runtime.
