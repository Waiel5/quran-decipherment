---
surah: 14
test_id: Q014-F-01
title: Abrahamic Mecca-prayer corpus-MAX prayer-vocative density (Q 14:35-41)
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q014-F-family-2026-05-08
alpha_bon: 0.0167
---

# Q014-F-01 — Pre-registration: Mecca-prayer corpus-MAX prayer-vocative density

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, direction-locked)**: The 7-verse window Q 14:35-41 contains the **highest prayer-vocative density per 100 words** among all 7-verse windows in the Quran corpus. The classical attention to vv. 35-41 as a structural-iʿjāz Abrahamic-prayer-block (al-Bāqillānī, *Iʿjāz al-Qurʾān*; al-Rāzī, *Mafātīḥ al-ghayb*) corresponds empirically to the surah's verse-block being maximally prayer-saturated.

**H0 (null)**: Q 14:35-41 ranks no better than top-5%ile (≥ rank 279 of ~5569 7-verse windows) on prayer-vocative density.

**Direction LOCKED**: Q 14:35-41 has **MAXIMUM** density (rank 1/N_windows). Sign-flip prohibited (PRE-REG-STANDARD-01).

## 2. Operational definition

**Prayer-vocative-cluster lemmas (Arabic, no-tashkeel, token-level matching)**:
- Vocatives to the Lord: `رب`, `ربنا`, `ربي`, `اللهم`
- Petition imperatives (root+prefix coverage): tokens starting with `اجعل`, `فاجعل`, `ارزق`, `وارزق`, `اغفر`, `فاغفر`, `اهد`, `فاهد`, `وهب`, `تقبل`, `سميع` only when in `سميع الدعاء` context.
- Note: tokens are matched in their stem-prefix-stripped form via Python startswith for compound prefixes; bare matches for the vocative tokens.

**Per-window metric**: 
`density(window) = count_prayer_tokens(window) / count_words(window) × 100`

**Corpus-window enumeration**: For each surah s with ≥ 7 verses, slide a 7-verse window from start=0 to start=N-7. The corpus has 5,569 such 7-verse windows.

**Per-surah whole-surah metric** (secondary): density at the surah level for context.

## 3. Test statistic

**Primary (direction-locked)**: rank of Q 14:35-41 among all 7-verse windows in the corpus, sorted by density descending.

**Secondary** (descriptive, not direction-locked): rank of Q 14 in whole-surah prayer-density distribution.

## 4. Success / Failure thresholds

- **CONFIRMED (strict)**: Q 14:35-41 ranks **1 / N_windows** on prayer-vocative density.
- **PASS-DIRECTED**: Q 14:35-41 ranks in top-5 of 5569 windows (≥ 99.91%ile).
- **DIRECTIONAL**: Q 14:35-41 ranks in top-1% (top 56 windows).
- **NULL**: rank 56 < r ≤ 279 (top-5% but not top-1%).
- **PRE-COMMIT VIOLATION**: rank > 279 (below 95th percentile).

## 5. Honest limits known a priori

- The pre-test scan (informational only, NOT result-viewing for this primary test) computed Q 14:35-41 density. The pre-reg locks the test infrastructure BEFORE re-running with the formal SHA-locked script.
- Lemma family is small and curated. Prayer-discourse markers in classical Arabic are richer than this regex captures (e.g., *yā Rabbī*, *yā ʾIlāhī*, *yā Mawlāy* are missed if not in the cluster). The cluster errs CONSERVATIVE (under-counts true prayers) — bias is AGAINST H1.
- Short verses can produce inflated densities at the window level. Mitigated by the 7-verse window length (≥ 50 words typically).
- Very short surahs (<7 verses, e.g., Q 105, 106, 108, 110, 111, 112, 113, 114) are excluded from window-rank ranking but are reported in the whole-surah scoring.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, token-level-stem-prefix-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

Not applicable for a corpus-rank statistic. The test is descriptive (corpus-MAX vs. all candidate 7-verse windows). At α_bon = 0.0167, the threshold for CONFIRMED is rank 1; for PASS-DIRECTED, rank ≤ 5.

## 8. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q014_F_all_tests.py`.
