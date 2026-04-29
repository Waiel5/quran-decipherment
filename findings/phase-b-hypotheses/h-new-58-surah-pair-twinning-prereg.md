---
id: H-NEW-58
title: Empirical structural twinning of classically-paired surahs
phase: B
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running pair similarity computation against null)
parent: H-NEW-8 (twin-opener Lock at L≥30 chars: Q 2:149-150 and Q 59:22-23)
bonferroni_family: 2026-04-15-Wave-Pair-Twinning
bonferroni_k: 20  (4 classical pairs × 5 axes; full grid pre-declared)
alpha_bon: 0.0025  (= 0.05 / 20)
seed: 20260416
rules_tuple: (no-tashkeel; QAC morphology v0.4 STEM-tokens for roots/lemmas; basmala-only-in-Q1)
---

# [[h-new-58-surah-pair-twinning|H-NEW-58]] — Surah-Pair Twinning (Pre-registration)

## Question

Do classically-paired surahs (canonically described by tradition as "twins"
or as having a special structural relationship) show structural similarity
on multiple axes that exceeds the similarity of randomly-chosen surah
pairs from the corpus?

## Locked test set — 4 classical pairs

Locked **before any computation on these pairs** is run:

1. **P_zahrawan** — Q 2 al-Baqara + Q 3 Āl ʿImrān ("al-Zahrāwān", "the
   two luminous ones"; both open with الم).
2. **P_anfal_tawba** — Q 8 al-Anfāl + Q 9 al-Tawba (al-Tawba lacks
   basmala; some classical readers treat as a continuation pair).
3. **P_muawwidhatan** — Q 113 al-Falaq + Q 114 al-Nās ("al-muʿawwidhatān";
   the two refuge-seeker surahs).
4. **P_muzz_mudd** — Q 73 al-Muzzammil + Q 74 al-Muddaththir (prophet-
   encounter pair; closely-similar opening epithet).

## Locked similarity axes — 5 axes

Locked **before any computation on these pairs** is run. For a surah pair
(A, B) compute on each axis a similarity statistic in [0, 1], where higher =
more similar. Definitions are pre-committed:

### Axis 1 — Lexical (root-set Jaccard)

Build the set of QAC STEM root tokens present in each surah. Similarity =
|R_A ∩ R_B| / |R_A ∪ R_B| (Jaccard index over roots).

### Axis 2 — Mean verse-length similarity (no-tashkeel char count)

Mean character length per verse. Similarity = 1 − |μ_A − μ_B| / max(μ_A,
μ_B). Range in [0, 1].

### Axis 3 — Rhyme-class entropy similarity

For each surah compute the distribution over the last 2-character (no-
tashkeel) suffix of each verse — this is the *rhyme class*. Compute Shannon
entropy H of the distribution. Similarity = 1 − |H_A − H_B| / max(H_A, H_B,
1e-9). Range in [0, 1]. Lower entropy = more rhyme-uniform.

### Axis 4 — Divine-name density similarity

Use the existing `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-by-verse.csv`
to compute per-surah divine-name density = (sum of `num_names`) / (verse
count). Similarity = 1 − |d_A − d_B| / max(d_A, d_B, 1e-9).

### Axis 5 — Hapax (surah-internal lexical concentration) density similarity

For each surah, compute the fraction of distinct STEM-roots in that surah
that occur exactly once *across the whole Quran* (i.e. corpus-level hapax
roots). Similarity = 1 − |h_A − h_B| / max(h_A, h_B, 1e-9).

## Null distribution

For each axis, draw 10,000 random *adjacent* surah pairs (i, i+1) where
1 ≤ i ≤ 113, with the EXACT classical pair excluded from each pair's null
draw to avoid a tautology. (Random adjacent pairs match the structural
fact that 3/4 classical pairs in this study are adjacent (Q2-Q3, Q8-Q9,
Q113-114, Q73-74). All 4 classical pairs are adjacent.)

For each pair × axis cell, p = (1 + |{null sims ≥ observed sim}|) / (1 +
N_null). One-sided test: enrichment = "observed sim is unusually HIGH".

Seed for null shuffle: 20260416.

## Bonferroni declaration (locked)

Family size k = 20 (= 4 pairs × 5 axes). α_bon = 0.05 / 20 = 0.0025.

A pair × axis cell is declared **significant under Bonferroni** iff
its one-sided p ≤ 0.0025.

## PASS criterion (declared before null draw)

The [[h-new-58-surah-pair-twinning|H-NEW-58]] hypothesis is declared **PASS** iff at least 2 of the 4
classical pairs show enrichment on at least 2 of the 5 axes at α_bon =
0.0025.

Otherwise **NULL**.

The cell-level table will be published in full regardless (no cherry-pick).

## Method-witness — MW-5 positive control

The pair P_muawwidhatan (Q 113 + Q 114) is the obvious "must-pass" check:
they are both 5-6 verses, both open with `qul aʿūdhu bi-rabbi…`, share a
near-identical opening formula and brevity. Pre-committed expectation:
**P_muawwidhatan must show similarity p < 0.001 on at least 2 axes**
(verse-length is the obvious one; rhyme-class entropy is the second-most
obvious). If MW-5 fails, the procedure itself is broken and we log a NULL
+ instrument-fail and do not declare [[h-new-58-surah-pair-twinning|H-NEW-58]] itself as either PASS or
NULL until the instrument is fixed.

## Garden-of-forking-paths disclosure

Choices fixed *before* seeing the four pair similarity vectors:
- Adjacent-only null (matches the empirical pattern that all 4 classical
  pairs are adjacent surahs; not chosen post-hoc to disadvantage non-
  adjacent random comparisons).
- 5 axes chosen because all 5 are computable from existing tools and
  cover lexical, prosodic-length, prosodic-rhyme, theological-density,
  and lexical-rarity dimensions. Iltifāt rate, qasam frequency, and
  muqaṭṭaʿāt overlap considered but rejected as orthogonal to the
  twinning question or as too narrow a basis (only 1 of 4 pairs has
  shared muqaṭṭaʿāt).
- Bonferroni k = 20 (full grid) chosen rather than k = 4 (per-pair axis-
  pooled) because cell-level reporting is the headline output. A loosening
  to k = 4 would require ratification per the
  bonferroni_tightening_vs_loosening rule.
- Similarity definition uses the SYMMETRIC normalization 1 − |Δ| / max(·).
  Rejected: |Δ| / σ_null (would couple null and statistic), and
  cosine on log-density (overkill for 1-D scalars).

## Data + outputs

- Input corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Input morphology: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
- Input divine-names: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-by-verse.csv`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_58_surah_pair_twinning.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-58.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-58-surah-pair-twinning.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-58-run-1.md`

## Status

PRE-REGISTERED 2026-04-15. Spec locked before running pair-vs-null script.
