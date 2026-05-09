---
surah: 59
test_id: Q059-F-03
title: Q 59 ↔ Q 62 al-Jumuʿah pair cohesion (Khawātim-bridge testing)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q059-F-03-q59-q62-pair-cohesion
alpha_bon: 0.025
post_hoc_origin: NO — pre-committed in the Q 59 specialist brief.
---

# Q059-F-03 — Pre-registration: Q 59 ↔ Q 62 pair cohesion via root/token overlap

## 1. Hypothesis (brief-derived, locked)

**H1 (one-tailed):** Q 59 and Q 62 share more surah-level orthographic-token overlap than random pairs of length-matched Medinan surahs. Specifically, Q 59 ↔ Q 62 token-set Jaccard > pool-mean of length-matched-Medinan-pair Jaccards at p < α_bon = 0.025.

**Substantive motivation:** Q 62:1 is the [[h-new-95-khawatim-extension|H-NEW-95]] external Khawātim echo (4 of 14 Khawātim-window names). At the verse level, Q 62:1 is the second-highest divine-name surah after Q 59. The brief asks whether this verse-level bridge is reflected at the surah-token-bag level — i.e., do Q 59 and Q 62 share substantively MORE total-token-overlap than random Medinan pairs?

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` ornament-stripped.
- **Token-set**: bag of distinct orthographic tokens per surah (whitespace-split).
- **Jaccard**: `|A ∩ B| / |A ∪ B|`.
- **Length matching**: pairs whose harmonic-mean-word-count falls within [0.7×, 1.5×] of the Q 59 ↔ Q 62 harmonic mean (with widening to [0.5×, 2.0×] if the tight pool < 30).

## 3. Permutation null

The 28-Medinan-surah corpus has C(28,2) = 378 pairs. Restrict to pairs whose harmonic mean word-count matches the Q 59 ↔ Q 62 harmonic. The pool serves as the natural empirical null distribution. p = fraction of pool pairs with Jaccard ≥ observed Q 59 ↔ Q 62 Jaccard.

## 4. Test statistics

- obs_jaccard = J(Q 59, Q 62).
- pool_mean_jaccard.
- p_one_sided = (count of pool pairs with J ≥ obs) / pool_size.
- Q 62 rank among Q 59's 27 Medinan partners by Jaccard.

## 5. Success / Failure

- **PASS**: p_one_sided < 0.05 AND Q 62 in top-quartile (rank ≤ 7) of Q 59's Medinan partners.
- **PARTIAL**: one of the two passes.
- **NULL**: neither.

## 6. Honest limits

- **No root-extraction**: orthographic-token Jaccard is a coarse proxy for root-overlap. Full QAC root extraction would tighten the test but requires external data not in scope here.
- **Length matching is asymmetric**: Q 62 (W=177) is much shorter than Q 59 (W=447), with harmonic mean 253.6. The pool is sensitive to the matching window; widening the pool yields more null statistical power but reduces the length-control.
- **High-frequency stopwords dominate**: tokens like الله, من, في, لا, الذين are likely to inflate Jaccard. The Khawātim-name overlap (e.g., "العزيز", "الحكيم") is a sub-fraction of total overlap. A future refinement should isolate divine-name-specific overlap.

## 7. Rules-tuple

`(no-tashkeel, ornament-stripped, whitespace-tokenized, surah-as-bag-of-orthographic-tokens, harmonic-mean-length-matching)`.

## 8. Bonferroni

k = 2 (J test + rank test). α_bon = 0.025.

## 9. Authored by

Waiel Al-Shujaa, 2026-05-09.
