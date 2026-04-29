---
finding_id: Q044-F-03
title: Q 44's FR-roots nearest neighbors are short eschatological mufaṣṣal surahs (NOT its HM-7 sub-cluster)
date_locked: 2026-04-28
seed: 20260428
phase: B+
test_family: per-surah cluster-cohesion
---

# Q044-F-03 pre-registration: Q 44's FR-roots nearest neighbors

## Hypothesis (direction-locked)

Q 44's top-7 Fisher-Rao-distance nearest neighbors (per the FR distance matrix at `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json`, the canonical 114×114 FR-roots metric) are NOT primarily its HM-7 sub-cluster siblings (Q 40-46 minus Q 44), but instead are **short eschatological mufaṣṣal surahs**.

**Pre-committed direction**: of Q 44's top-7 FR-nearest neighbors, ≥ 4 fall in the **eschatological-mufaṣṣal class** (defined as: Meccan + verse-count ≤ 60 + eschatological-content register per classical exegesis; the registered candidate set is {Q 51, 52, 53, 54, 55, 56, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 32}).

## Why this pre-reg matters

If TRUE: Q 44, despite being in HM-7, sits content-cohesively with the SHORT-MUFAṢṢAL ESCHATOLOGICAL register, NOT with its HM-7 cluster siblings (Q 40 has 85 verses, Q 41 has 54, Q 42 has 53, Q 43 has 89, Q 45 has 37, Q 46 has 35). This would explain:
- Q 44's UAS rank 97 (HM-7 minimum).
- Q 44's compression-tail-like properties (6.17 words/verse — the densest in HM-7).
- Q 44's two-rhyme-letter monorhyme (mufaṣṣal-style prosody).

It would also empirically demonstrate that **letter-family clusters (HM-7) and content-cohesion clusters can be ORTHOGONAL** at the per-surah level — replicating [[h-new-600-letter-families|H-NEW-600]]'s NULL on letter-family content cohesion at the within-cluster-member level.

## Null hypothesis

H₀: Q 44's top-7 FR-nearest neighbors are MAJORITY HM-7 siblings (≥ 4 of 7 from Q 40-46 minus Q 44).

## Operationalization

- **Source**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- **Metric**: Fisher-Rao on QAC v0.4 stem-root distributions (the canonical project FR distance).
- **Top-K**: K=7 (matching the HM-7 cluster size for symmetric comparison).

## Verdict criteria

- **VINDICATED** if ≥ 4 of top-7 are eschatological-mufaṣṣal class AND ≤ 1 is HM-7 sibling.
- **DIRECTIONAL** if ≥ 3 of top-7 are eschatological-mufaṣṣal class.
- **NULL** if < 3 are eschatological-mufaṣṣal class.
- **PRE-COMMIT VIOLATION** if ≥ 4 of top-7 are HM-7 siblings (the H₀ winning).

## Garden-of-forking-paths log (BEFORE running)

- K locked at 7 (not 5 or 10).
- Eschatological-mufaṣṣal class locked at the {Q 32, Q 51-114} surface enumeration above.
- HM-7 sibling set locked at {Q 40, 41, 42, 43, 45, 46}.
- Direction-of-effect locked: eschatological-mufaṣṣal-majority over HM-7-majority.

## Bonferroni

Single direction-test, k=1, α=0.05.

## Run script

`/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/scripts/Q044_F_03_fr_nearest.py`.

## Output

`/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-03.json`.
