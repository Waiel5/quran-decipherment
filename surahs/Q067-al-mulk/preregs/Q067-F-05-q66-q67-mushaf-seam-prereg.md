---
finding_id: Q067-F-05
title: Q 66 → Q 67 canonical-adjacency cost — is the long-Medinan→short-Meccan-tail seam a high-cost boundary?
date_locked: 2026-05-09
phase: B+
seed: 20260509
n_perm: 10000
rules_tuple: (no-tashkeel, QAC-stem-roots, K=500, Dirichlet α=0.5, FR-distance, Hafs-Kufan)
---

# Q067-F-05 — Pre-registration

## Hypothesis

Q 67 al-Mulk opens the Quran's "short-Meccan tail" segment (Q 67 onwards is dominated by Meccan-mufaṣṣal-awsāṭ/qiṣār surahs, in contrast to the long-Medinan block Q 47-Q 66). If the canonical mushaf order encodes a structural-architectural boundary at this position, then the Q 66 → Q 67 adjacency should incur an elevated Fisher-Rao traversal cost relative to the empirical distribution of the 113 canonical adjacency-costs in `findings/phase-b-hypotheses/csv/h-new-720.json`.

## Pre-registered direction (LOCKED)

**HIGH-cost seam**: Q 66 → Q 67 raw delta (`delta_raw` field from `h-new-720.json`'s `per_adjacency` array) sits in the top decile (rank ≤ 12 of 113, descending order by `delta_raw`).

## Success criterion

**PASS-DIRECTED** if:
- Q 66 → Q 67 rank (descending by `delta_raw`) ≤ 12 (top decile of 113).

**NULL** if:
- Q 66 → Q 67 rank > 12.

## MW protections

- **MW-1 (instrument-prior)**: Instrument is the pre-locked `h-new-720` adjacency-cost map; no new metric introduced.
- **MW-2 (corpus-prior)**: 10000 bootstrap resamples over the 113 adjacency-cost distribution.
- **MW-3 (alternative-models)**: Re-test under `fraction_residual` field (alternative normalization).
- **MW-5 (replication)**: Compare Q 66 → Q 67 rank to Q 65 → Q 66 and Q 67 → Q 68 (neighbours).
- **MW-6 (instrument-control)**: Report distribution stats for context.
- **MW-7 (post-hoc cap)**: pre-reg locks rank threshold ≤ 12 = top-decile. Pre-commit fixed.

## Failure conditions

- Rank > 12 (descending): NULL — Q 66 → Q 67 is NOT a high-cost seam.
- Rank between 12 and 50: NULL-DIRECTIONAL — neither high nor low.

## Honest-limits note

The H-NEW-720 cost is computed under a single rules-tuple (`no-tashkeel, QAC-stem-roots, K=500, Dirichlet α=0.5`). Rules-tuple sensitivity is not tested here; the rank is rules-tuple-conditional.

## Output

`/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-05.json`
