---
surah: 99
test_id: Q099-F-04
title: zalzala-root corpus-EXACT distribution: Q 99 share + corpus-token-count
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q099-F-04-zalzala-root
alpha_bon: 0.01667
---

# Q099-F-04 — Pre-registration: zalzala-root corpus-EXACT distribution

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** The corpus-EXACT count of the root *z-l-l* in its reduplicated quadriliteral form *zalzala* (regex pattern: `زلزل` after tashkeel-strip) is exactly **6 tokens distributed across 4 verses in 4 distinct surahs**: Q 2:214 (1), Q 22:1 (1), Q 33:11 (2), Q 99:1 (2).

**H1b (one-tailed, locked direction):** Q 99 holds the corpus-MAX share of *zalzala*-root tokens by length-normalized density: tokens / surah-words.

**H1c (one-tailed, locked direction):** Q 99 contains the highest single-verse density of the root: 2 tokens in v. 1 (4-word verse) = 50% per-word density at v. 1.

**H0**: Failure of any of the 3 hypotheses.

**Direction:** locked POSITIVE Q 99 = corpus-MAX on density.

## 2. Operational definition

- **Source data**: `quran-text/quran-no-tashkeel.json`.
- **Detection regex**: `زلزل` (tashkeel already stripped in source data).
- **Token-counting**: raw regex match count per verse.
- **Surah-density**: tokens / surah-words.
- **Verse-density**: tokens / verse-words.

## 3. Test statistic

- T1: corpus-EXACT count of zalzala-root tokens (locked = 6).
- T2: Q 99 surah-density rank in the 4-host-surah set.
- T3: Q 99:1 verse-density rank in the 4-host-verse set.

## 4. Permutation null (not applicable — direct count test)

This is a deterministic-count test, not a statistical-inference test. The locked numbers must match the corpus-extracted numbers EXACTLY for PASS.

## 5. Success / Failure

- **CONFIRMED**: T1 = 6 AND Q 99 surah-density rank-1 of 4 AND Q 99:1 verse-density rank-1 of 4.
- **DIRECTIONAL**: 2 of 3 conditions match.
- **NULL**: 1 or fewer conditions match.

## 6. Honest limits known a priori

- The pre-locked count of 6 was derived from a corpus-search BEFORE this pre-reg lock; per HANDOFF/04-DISCIPLINE.md "post-hoc protocol" the result is PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.
- The independent-replication question: does the count hold under the alt-text Uthmani-consonantal corpus? Future test.
- Sensitivity check: the regex `زلزل` may not capture all morphological derivatives of the geminate-quadriliteral. Sensitivity-check via QAC `data/morphology/quranic-arabic-corpus.json` if available.

## 7. Rules-tuple

`(no-tashkeel, regex-orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 3 (T1, T2, T3). α_bon = 0.01667.

## 9. Coordination

This is a Q 99-specific root-distribution test. Q 22 al-Ḥajj specialist (when developed) will note its single token at Q 22:1; Q 33 al-Aḥzāb specialist will note the doublet at Q 33:11. Coordinated cross-surah root-table.

## 10. SHA256 lock

Computed at write-time, embedded in `scripts/Q099_F_04_zalzala_root.py`, verified at runtime.
