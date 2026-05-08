---
surah: 15
test_id: Q015-F-01
title: Iblīs-rebellion-discourse lexical analysis (Q 15:28-44)
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q015-F-family-2026-05-08
alpha_bon: 0.0167
---

# Q015-F-01 — Pre-registration: Iblīs-rebellion-discourse lexical analysis

## 1. Hypothesis (locked before observation)

**Background**: Q 15:28-44 contains the corpus's most-extended pre-creation Iblīs-rebellion narrative (17 verses, 119 words). Classical tafsir (al-Ṭabarī, al-Rāzī, Ibn Kathīr) treats this block as the canonical pre-creation rebellion-discourse, with paralels in Q 7:11-25, Q 17:61-65, Q 18:50, Q 20:115-126, Q 38:71-85.

**H1 (direction-locked)**: Q 15:28-44 contains **≥3 corpus-hapax tokens** (single-corpus-attestation tokens of length > 2). The classical attention to this block's distinctive vocabulary is empirically anchored at corpus-rare lexical concentration.

**H1-extended (descriptive, not direction-locked but reported)**: Q 15:28-44's hapax + near-hapax token count (n_total) is comparable to or higher than parallel Iblīs-rebellion blocks.

**H0 (null)**: Q 15:28-44 has < 3 hapax tokens.

**Direction LOCKED**: ≥3 hapax. Sign-flip prohibited.

## 2. Operational definition

**Block**: Q 15:28-44 (verses 28 through 44 inclusive, 17 verses).

**Token**: orthographic token (word) per the no-tashkeel JSON, after stripping punctuation marks `۞۩.،,!?:;()[]`. Tokens of length ≤ 2 are EXCLUDED (to avoid 1-2-letter prepositions counting as hapax).

**Corpus**: full no-tashkeel Quran (`quran-text/quran-no-tashkeel.json`).

**Hapax (single-corpus-attestation)**: a token T is hapax if exactly **1 verse** in the corpus contains T as a substring.

**Near-hapax (corpus-rare-attestation)**: a token T is near-hapax if 2 ≤ n_attestations ≤ 5 verses in the corpus contain T as a substring.

**Per-block stats**: count of unique tokens in block; count of hapax tokens (n=1); count of near-hapax tokens (n≤5).

## 3. Test statistic

**Primary (direction-locked)**: count of hapax tokens (n=1) in Q 15:28-44.

**Secondary** (descriptive, reported for context): comparison vs Q 7:11-25, Q 17:61-65, Q 18:50, Q 20:115-126, Q 38:71-85.

## 4. Success / Failure thresholds

- **CONFIRMED**: ≥3 hapax tokens AND Q 15:28-44 has higher hapax-count than ≥3 of the 5 comparison blocks.
- **PASS-DIRECTED**: ≥3 hapax tokens (primary direction met).
- **NULL**: < 3 hapax tokens.
- **PRE-COMMIT VIOLATION**: 0 hapax tokens (vocabulary not corpus-rare at all).

## 5. Honest limits known a priori

- The corpus-search uses substring-match — this could overcount if a longer hapax-token contains a shorter common token. We accept this limitation; the substring-match is conservative for the *uniqueness* claim (a hapax via substring is at least as rare as a hapax via exact match).
- The "hapax" definition is substring-attestation in unique verses; it is NOT the strict philological hapax-legomenon (which requires unique verbal-form attestation). The substring-method is a coarser proxy.
- Comparison blocks are heterogeneous in length (Q 18:50 = 1 verse vs Q 7:11-25 = 15 verses); per-block hapax-count is correlated with length. The PRIMARY test is direction-locked at the absolute hapax-count, not the density.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, substring-corpus-attestation, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

Not applicable for a corpus-rank/count statistic — the test is descriptive (corpus-hapax count). At α_bon = 0.0167, the test is direction-locked: ≥3 hapax PASSES; <3 FAILS.

## 8. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q015_F_all_tests.py`.
