---
finding_id: h-new-203
title: "Full 30-juzʾ partition analysis — do classical recitation-balance juzʾ boundaries align with Fisher-Rao structural jumps, and are juzʾ segments internally coherent?"
specialist: autonomous-quran-test
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-203
alpha_bon: 0.025
alpha_raw: 0.05
parent_findings: [h-new-111, h-new-127, h-new-130, h-new-64]
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan, 30-juzʾ canonical partition)"
---

# [[h-new-203-fisher-rao-juz|H-NEW-203]] — Full 30-juzʾ partition against Fisher-Rao structural geometry

## Motivation

The classical 30-juzʾ partition of the Quran is conventionally described
as a RECITATION-BALANCE device (roughly equal-length parts for one-month
recitation during Ramadan). [[h-new-64-juz-boundaries|H-NEW-64]] already tested whether the 29
internal juzʾ boundaries align with four axes of content shift
(lexical, rhyme, proper-noun, length). This hypothesis asks a
COMPLEMENTARY question in the Fisher-Rao geometric framework established
by [[h-new-111-fisher-rao-mushaf|H-NEW-111]] / [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] / [[h-new-130-fisher-rao-residuals|H-NEW-130]]:

1. Do the 29 juzʾ-internal cuts preferentially land on positions of
   HIGH Fisher-Rao jump (windowed-verse root-distribution discontinuity)?
2. Are juzʾ SEGMENTS internally coherent, i.e., do verses within a
   juzʾ have a tighter root-distribution than verses in random
   contiguous segmentations of the same verse-count pattern?

The underlying question: is "recitation balance" the ONLY function of
the juzʾ partition, or does it also track information-geometric
structure?

## Data and locked parameters

- Corpus: 6236 verses, Hafs-Kufan, no-tashkeel, basmala-counted-only-in-surah-1.
  (Matches [[h-new-64-juz-boundaries|H-NEW-64]] convention.)
- Feature: QAC v0.4 STEM root tokens per verse (from
  `data/morphology/quranic-corpus-morphology-0.4.txt`, same parse as
  [[h-new-111-fisher-rao-mushaf|H-NEW-111]]/127).
- Top-K roots: K = 500 globally (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).
- Dirichlet smoothing α = 0.5 (Jeffreys), same as [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]].
- Fisher-Rao angular distance: d(p,q) = 2·arccos(Σ √(p_i q_i)).
- Window half-width W = 20 verses on each side of a cut (symmetric,
  truncated at corpus edges). Rationale: median juzʾ length ≈ 208
  verses; W=20 → 40-verse windows are ~19% of a juzʾ, giving local
  scale without dragging in the next juzʾ.
- Juzʾ-start table locked, copied from [[h-new-64-juz-boundaries|H-NEW-64]] pre-reg (no re-derivation).
- Seed: 20260419.
- n_perm = 10000 for both permutation tests.

## Hypotheses and locked thresholds

### Test 1 (Primary — boundary concentration). α_bon = 0.025.

Let J = 29 juzʾ-internal cut positions (between verse p-1 and verse p,
1-indexed global position). For each of the 6235 possible cut positions,
compute `D(p)` = FR-distance between window-before and window-after
root-distributions.

Test statistic:  T1 = Σ_{p ∈ J} D(p).

Null: 10000 random samples of 29 cut positions drawn uniformly without
replacement from the 6235 possible positions.

p_1 = (1 + #{T1_perm ≥ T1_obs}) / (n_perm + 1), one-sided upper.

**PASS-1** iff p_1 < 0.025.
**NULL-1** iff p_1 ≥ 0.025.

### Test 2 (Primary — juzʾ-segment internal coherence). α_bon = 0.025.

For a partition of 6236 verses into 30 contiguous segments, define the
COHERENCE statistic as the mean FR-distance from each verse's
windowed-root-distribution to its segment's centroid root-distribution
(computed as L1-normalized smoothed pooled root counts across the
segment). Lower = tighter segment coherence.

Test statistic:  T2 = Σ_{s=1..30} Σ_{v ∈ s} D(p_v, q_s) / 6236
where p_v is verse v's windowed (W=20 each side, within-segment-clipped)
root distribution and q_s is segment s's pooled root distribution.

Observed: T2 computed using the canonical 30-juzʾ partition.

Null: 10000 random partitions of 6236 verses into 30 contiguous
segments with the SAME segment-length vector as the canonical
partition (permute segment-length vector uniformly to preserve
multiset of juzʾ lengths; place 29 cuts at cumulative-sum positions).

p_2 = (1 + #{T2_perm ≤ T2_obs}) / (n_perm + 1), one-sided lower.

**PASS-2** iff p_2 < 0.025.
**NULL-2** iff p_2 ≥ 0.025.

### Joint verdict

| Test 1 | Test 2 | Label |
|---|---|---|
| PASS | PASS | STRONG-PASS (juzʾ is BOTH a boundary-jump partition AND a coherent segmentation) |
| PASS | NULL | BOUNDARY-ONLY (jumps align, but segments not internally distinctive) |
| NULL | PASS | COHERENCE-ONLY (segments are tight, but classical boundaries weren't uniquely jump-like) |
| NULL | NULL | NULL-JUZʾ-NOT-GEOMETRIC (pure recitation-balance, no information-geometric alignment) |

## Secondary / descriptive (not bonferroni-counted)

- S1. Per-boundary rank: for each of 29 juzʾ cuts, its percentile rank
  among all 6235 cuts' D(p) values. Report mean rank and #{rank ≥ 90th
  percentile}.
- S2. Surah-seam-matched null for Test 1: repeat Test 1 with the
  constraint that exactly 7 of 29 sampled cuts fall on surah seams
  (matching the observed juzʾ split: juzʾ 14, 15, 17, 18, 26, 29, 30 are
  surah-aligned). Reports p_1_matched. DESCRIPTIVE only.
- S3. Per-juzʾ coherence: report each juzʾ's mean D(p_v, q_s) value,
  ranked from most- to least-coherent.
- S4. Sanity controls:
  - MW-5 (discriminativeness): compute T1 for a RANDOM permutation of the
    corpus (scramble verse order globally, re-derive windowed distributions,
    recompute D(p) for juzʾ positions). If the scrambled T1 is NOT
    meaningfully lower than observed (e.g., Δ > 20% of null SD), the
    instrument is broken.
  - MW-1 (length residualization): verse-count per juzʾ is
    approximately balanced by construction (164..259 verses); confound
    minimal. Not adjusted.

## Pre-committed failure modes

| Scenario | Report |
|---|---|
| PASS-1 + PASS-2 | STRONG-PASS |
| PASS-1 only | BOUNDARY-ONLY — boundaries are structural, segments not |
| PASS-2 only | COHERENCE-ONLY — juzʾ segments track topic, but boundary choice is under-determined (many equally-good cuts) |
| NULL-1 + NULL-2 | NULL — juzʾ is purely recitation-balance |
| MW-5 scrambled corpus passes | INSTRUMENT-BROKEN; primaries inadmissible |

## Garden of forking paths

- Window W=20 is a judgment call. Alternatives: W=5, W=10 ([[h-new-64-juz-boundaries|H-NEW-64]]'s
  choice), W=50. I am locking W=20 BEFORE running. If PASS, I will
  report robustness across W ∈ {10, 20, 30} as secondary.
- Top-K=500 is inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] global selection. Not changed.
- FR distance vs. cosine vs. KL: FR is the natural distance on the
  probability simplex and is what [[h-new-111-fisher-rao-mushaf|H-NEW-111]]/127/130 have been using;
  no ambiguity.
- Segment coherence could be measured as mean pairwise intra-segment
  D vs. centroid D. I'm using centroid D because it is O(n) per
  segment rather than O(n²), and because the centroid IS the
  segment's natural Fisher-Rao summary. Locked before running.
- Null for Test 2: matched segment-length vector (permuted) is the
  stringent choice. Alternatives (random cut points, equal-length
  segments) were considered and rejected as less fair.

## Deliverables

1. Pre-reg (this file), SHA-256 emitted.
2. Script: `scripts/h_new_203_juz_fisher_rao.py` (seed 20260419,
   deterministic).
3. JSON: `findings/phase-b-hypotheses/csv/h-new-203.json`.
4. Findings md: `findings/phase-b-hypotheses/h-new-203-fisher-rao-juz.md`.
5. Journal: `journal/h-new-203-run-1.md`.
