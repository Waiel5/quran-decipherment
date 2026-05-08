---
surah: 11
test_id: Q011-F-01
title: wa-ilā-[TRIBE]-akhāhum-[PROPHET] formulaic-lattice corpus-share
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_family: Q011-F-01
bonferroni_k: 1
alpha_bon: 0.05
n_perm: 0
---

# Q011-F-01 — Pre-registration: wa-ilā-akhāhum corpus-share

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, direction LOCKED):** Of all corpus-wide instantiations of the
exact 4-word abstracted formula `وإلى [TRIBE] أخاهم [PROPHET]` (where the slot
fillers are any tribe-ethnonym + prophet-name), **at least 50 % occur in
Q 11 Hūd**, AND Q 11 contains **≥ 3 instantiations**.

**H0:** Q 11's share of corpus instantiations is < 50 %, OR Q 11 has < 3
instantiations.

**Direction:** Q 11 share ≥ 50 %; Q 11 count ≥ 3 (LOCKED).

## 2. Operational definition

- **Corpus**: `quran-text/quran-no-tashkeel.json`, all 114 surahs.
- **Tokenization**: split on whitespace + Arabic punctuation marks
  `۞ ۚ ۗ ۖ ۘ ۙ` (consistent with H-NEW-270's regex extractor).
- **Slot-abstracter**:
  - TRIBE ∈ {`عاد`, `ثمود`, `مدين`}
  - PROPHET ∈ {`هودا`, `صالحا`, `شعيبا`} (the orthographic-token forms)
  - These are the H-NEW-270-locked slot fillers (no extension).
- **Match definition**: a verse contains a match iff some 4-token contiguous
  sub-window of the verse equals `[وإلى, TRIBE, أخاهم, PROPHET]` after token
  normalization.
- **Per-surah count** = number of distinct verses in that surah containing
  ≥ 1 match. **Corpus total** = sum over all surahs.
- **Q 11 share** = Q 11 count / corpus total.

## 3. Test statistic

**Primary**: Q 11 share (fraction). **Secondary**: Q 11 raw count.
**Tertiary**: corpus distribution (which surahs contribute, ranked).

## 4. Success / Failure

| Outcome | Verdict |
|:--|:--|
| Q 11 count ≥ 3 AND Q 11 share ≥ 50 % | **CONFIRMED** |
| Q 11 count ≥ 3 AND 33 % ≤ share < 50 % | DIRECTIONAL |
| Q 11 count < 3 OR share < 33 % | NULL |
| Q 11 count strongly low (≤ 1) | Pre-commit violation; published NULL with full prominence |

## 5. Bonferroni context

- This is a 1-cell test (k=1): single descriptive claim.
- Conventional α=0.05, no permutation null required (the claim is descriptive
  about exact-form counts, not a comparison with a randomization).
- The H-NEW-270 within-Hūd matched-null already established the *non-randomness*
  of the within-surah lattice; this test asks the orthogonal **corpus-share**
  question.

## 6. Honest limits known a priori

- The 4-word formula could appear in surahs other than Q 11 and Q 7 (per
  H-NEW-270 we know Q 7 also has 3 matches at 7:65/73/85). The expected outcome
  given H-NEW-270 priors is: corpus total = 6 (3 in Q 11 + 3 in Q 7); Q 11
  share = 50 %. The hypothesis is locked at the boundary; published as PASS
  iff Q 11 share **≥** 50 %.
- The slot-filler list is restricted to the 3 tribes / 3 prophets attested
  in the H-NEW-270 lattice. Hypothetical extensions (e.g., Q 41 alludes to
  ʿĀd / Thamūd but not in this exact pre-vocative form) are correctly
  excluded by the locked filler list.
- The claim is exact-form lexical, not lemma/root level. A different
  rules-tuple (lemma-collapse) might fold cognate vocative forms together.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, exact-string-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Computed at run-time. Embedded in `scripts/Q011_F_01_wa_ila_akhahum_corpus_share.py`.
