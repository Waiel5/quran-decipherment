---
finding_id: Q050-F-08
date_locked: 2026-05-09
phase: B+
direction: LOCKED
seed: 20260509
---

# Q050-F-08 — Pre-registration: Q 49 → Q 50 universal hinge re-verification (H-NEW-1262 replication)

## Hypothesis

The **Q 49 → Q 50 mushaf adjacency** is a "universal hinge" — i.e., it appears in the **top-15 most-extreme adjacency entries on ALL THREE independent feature sets**:

- **H-NEW-130** (QAC-root residuals)
- **H-NEW-130b** (character-4-gram residuals)
- **H-NEW-130c** (verse-length residuals)

This was originally established as H-NEW-1262 / Q049-F-03 with `in_all_three: True` (Q 49 al-Ḥujurāt specialist landing, 2026-05-08). The Q 50 specialist re-verifies on disk that the result holds without modification — a "verify your dependencies" check before incorporating the hinge into Q 50's cross-references.

## Pre-registered direction

**REPLICATION**: the disk JSON `surahs/Q049-al-hujurat/csv/Q049-F-03.json` must satisfy ALL the following:

1. `in_h130_top15_root` == True
2. `in_h130b_top15_char4gram` == True
3. `in_h130c_top15_verselen` == True
4. `primary_all_three` == True
5. The Q 49-Q 50 pair is `[49, 50]` (mushaf-adjacency, not transposed).

If ALL 5 conditions hold → REPLICATED (Q 49 → Q 50 universal hinge VERIFIED). Q 50 inherits the cross-reference to H-NEW-1262.

If ANY condition fails → REPLICATION-FAILED — investigate whether (a) the Q049 specialist's JSON was misreported, or (b) underlying H-NEW-130/130b/130c top-15 sets have changed since the original Q049-F-03 run. Publish as NULL-REPLICATION with full prominence.

## Independent check

In addition to the JSON cross-read, compute the Q 49 → Q 50 entry from h-new-130.json, h-new-130b.json, h-new-130c.json **directly** (not via Q049-F-03 JSON):

- For each of the 3 H-NEW JSONs, extract the top-15 highest-distance adjacency pairs from the relevant `per_pair` or equivalent ranking.
- Check whether (49, 50) appears in the top-15.

If the direct re-extraction AGREES with the JSON cross-read → STRONG-REPLICATION.
If the direct re-extraction DISAGREES → flag the disagreement; publish both results with full prominence; mark Q049-F-03 as questionable.

## Data and rules-tuple

- Primary source: `surahs/Q049-al-hujurat/csv/Q049-F-03.json` (the Q049 specialist's locked result).
- Cross-verification sources:
  - `findings/phase-b-hypotheses/csv/h-new-130.json` (root residuals)
  - `findings/phase-b-hypotheses/csv/h-new-130b.json` (char-4-gram residuals)
  - `findings/phase-b-hypotheses/csv/h-new-130c.json` (verse-length residuals)
- Rules-tuple: (cross-feature replication, no parameter change from Q049-F-03 source).
- Seed: 20260509 (irrelevant for deterministic JSON cross-read; recorded for reproducibility).
- n_perm: N/A (this is a replication check, not a new permutation null).
- Bonferroni: N/A (single replication question).

## SHA lock

Compute SHA256 of THIS file after writing; embed in `scripts/Q050_F_08_q49_q50_hinge_reverify.py`. Verify at runtime; fail-fast on mismatch.

## Output

- JSON: `surahs/Q050-qaf/csv/Q050-F-08.json` with:
  - finding_id, prereg_sha256, seed, rules_tuple
  - q049_f_03_in_all_three: bool
  - q049_f_03_pair: [int, int]
  - direct_h130_top15_contains_49_50: bool
  - direct_h130b_top15_contains_49_50: bool
  - direct_h130c_top15_contains_49_50: bool
  - verdict (STRONG-REPLICATION / REPLICATED-JSON-ONLY / NULL-REPLICATION)
  - pre_commit_violation flag

## Honest limits

- This is a "trust but verify" check on a dependency finding. Most likely outcome: REPLICATED (Q049-F-03 was a CONFIRMED-CROSS-FEATURE landing).
- Direct re-extraction from h-new-130*.json requires inferring the top-15 ranking from the underlying data structure. If h-new-130 stores residuals differently from the Q049 specialist's read, the direct check may produce a different top-15 — this is a methodological artifact, NOT a real disagreement with Q049-F-03.
- The pre-commit-direction-locked verdict is REPLICATED. If the direct re-extraction disagrees, the JSON-only verdict still stands as the headline; the disagreement is logged for follow-up.
- Q050-F-08 is intentionally LOW-NOVELTY (it is a verification, not a new claim) — its value is method-discipline, not new science.
