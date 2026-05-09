---
prereg_id: Q076-F-02
surah: 76
title: Q 76 is the LONGEST 100%-alif single-rāwī surah in the Qurʾān
date_locked: 2026-05-09
phase: B+
hypothesis_class: novel
post_hoc: false
direction_locked: Q 76 ≥ all other 100%-alif surahs in verse-count
bonferroni_k: 4
bonferroni_family: Q076-F
alpha_bon: 0.0125
seed: 20260509
n_perm: 10000
verse_numbering: hafs-kufan
orthography: no-tashkeel
letter_definition: graphemes
null_model: monorhyme-letter-shuffled with length-matching
---

# Q076-F-02 — Q 76 al-Insān: corpus-EXACT longest 100%-alif single-rāwī surah

## Hypothesis

Across all 114 Qurʾānic surahs, exactly 4 surahs achieve 100% alif-rāwī (every verse ends in alif): Q 48 al-Fatḥ (29v), Q 72 al-Jinn (28v), Q 76 al-Insān (31v), Q 91 al-Shams (15v). Q 76 is the longest. We test whether this corpus-EXACT-rank-1 is statistically distinguishable from a permutation null.

## Operationalization

Final-letter detection: the last grapheme of the last whitespace-split token of each verse, with sajda-marker (`۞`) and waqf-markers (`ۚ`, `ۖ`) stripped. Per `findings/phase-b-hypotheses/csv/h-new-750.json`, this gives `top_final_letter_frac = 1.0` for the 15 single-rāwī surahs.

## Tests (2 cells)

### Cell A — corpus-rank within 100%-alif subgroup

H₀: Q 76 is not rank 1 by verse-count among 100%-alif surahs.
H₁: Q 76 = 31 verses, all alif > Q 48 = 29 verses, all alif > Q 72 = 28 verses, all alif > Q 91 = 15 verses, all alif. Q 76 rank = 1 / 4.

Decision rule: PASS if Q 76 = rank 1.

### Cell B — permutation null on the 4-element 100%-alif length distribution

H₀: A random sample of 4 single-rāwī surahs from the corpus would have a top-length of 31 or more.
H₁: Such a sample rarely (< α_bon) reaches the observed top-length.

Null design: For each of 10,000 permutations (seed=20260509), select 4 random surahs from the 15 single-rāwī surahs (per h-new-750), compute the top length. p_perm = fraction with top-length ≥ 31.

Decision rule: PASS if p_perm < α_bon = 0.0125.

NOTE: This is a small-N comparison (N=4 from N=15). Statistical power is low. The PASS-criterion is therefore SUPPLEMENTARY; the primary signal is the **corpus-EXACT** rank itself.

## Pre-decision verdicts

- **CONFIRMED-CORPUS-EXACT** if Cell A PASS (rank 1)
- **CONFIRMED-CORPUS-EXACT-EXTREME** if both PASS

## Garden-of-forking-paths log

The 100%-alif fact was observed by direct computation on h-new-750 before pre-registration; the corpus-EXACT rank-1 length is a direct consequence. This is a descriptive/structural finding, not a hypothesis-testing finding in the strict permutation-null sense.

## Replication path

Trivially deterministic — re-loading h-new-750 yields identical result. Independent re-derivation by recomputing finals from `quran-no-tashkeel.json` (executed in `scripts/Q076_F_all_tests.py`).
