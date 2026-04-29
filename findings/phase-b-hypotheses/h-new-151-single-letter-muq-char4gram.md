---
id: H-NEW-151
title: Single-letter muqaṭṭāʿat sub-cluster under char-4-gram — replication test
phase: B
status: NULL at α=0.05; direction-consistent but signal weaker than root feature space
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [h-new-146 (Cell C root FR p=0.031), h-new-111b (char-4-gram FR D-matrix)]
seed: 20260417
rules_tuple: "(114 surahs Hafs-Kūfan; char-4-gram features per H-NEW-111b; Fisher-Rao arccos-Bhattacharyya)"
bonferroni: k=1 α=0.05 family=h-new-151-single-letter-muq-char4gram
pre_reg: findings/phase-b-hypotheses/h-new-151-single-letter-muq-char4gram-prereg.md
script: scripts/h_new_151_single_letter_muq_char4gram.py
output_json: findings/phase-b-hypotheses/csv/h-new-151.json
verdict: NULL — replication direction is CORRECT (within-singleton < between) but magnitude at char-4-gram is weaker (z=-1.06) than at root FR (z=-2.06), failing to reach single-test α=0.05 (p=0.15). Parent claim (single-letter-muq sub-cluster) remains descriptively suggestive but NOT cross-feature-robust.
---

# [[h-new-151-single-letter-muq-char4gram|H-NEW-151]] — Single-letter muq sub-cluster under char-4-gram

## Summary

[[h-new-146-q50-qaf-hub|H-NEW-146]] Cell C found that the three single-letter muq surahs
(Q 38 ص, Q 50 ق, Q 68 ن) are mutually closer in FR-root space than to
other 26 muq surahs, at p=0.031. This cross-feature replication under
char-4-gram ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] D-matrix) **FAILS to reach single-test α=0.05**
but the direction is **consistent**.

## Result

| Quantity | Root FR ([[h-new-146-q50-qaf-hub|H-NEW-146]]) | Char-4-gram FR ([[h-new-151-single-letter-muq-char4gram|H-NEW-151]]) |
|---|---:|---:|
| Mean within-singleton dist | 0.850 | 0.934 |
| Mean between singletons-vs-others | 0.992 | 0.981 |
| Delta (within − between) | **−0.142** | **−0.046** |
| Null SD | 0.069 | 0.044 |
| z-score | **−2.06** | **−1.06** |
| p (1-sided lower) | **0.031** | **0.15** |
| Verdict | near-miss | **NULL** (direction-consistent) |

**The direction of the effect is PRESERVED** (delta negative in both)
but the **magnitude is ~1/3 under char-4-gram** (−0.046 vs −0.142).
This suggests the single-letter-muq sub-cluster is ROOT-FEATURE-SPECIFIC
rather than a generic feature-space-invariant structural fact.

## Pairwise char-4-gram distances

| Pair | FR-char4gram distance |
|---|---:|
| Q 38 ↔ Q 50 | 0.889 |
| Q 50 ↔ Q 68 | 0.945 |
| Q 38 ↔ Q 68 | 0.968 |

All three pairs below the muq-average of ~0.98, but only marginally.
Q 38-Q 50 is the shortest singleton-pair.

## Interpretation

The single-letter-muq sub-cluster hypothesis is WEAKLY ROOT-SPECIFIC.
Under char-4-gram features, the Q 38/50/68 triad is directionally
closer-to-each-other-than-to-other-muq, but the magnitude fails to
reach statistical significance at α=0.05.

This pattern (direction preserved, magnitude reduced) is typical of
feature-specific signals. The root feature space captures thematic
content (which roots appear); char-4-gram captures surface-orthographic
patterns. The single-letter muq surahs share MORE at the thematic level
than at the orthographic level.

**Honest null**: the parent [[h-new-146-q50-qaf-hub|H-NEW-146]] Cell C finding (p=0.031) is
REINFORCED as a near-miss in its own feature space but NOT extended
by this char-4-gram replication.

## Pre-reg compliance

Bonferroni k=1, α=0.05. Direction locked negative (replication). 1-sided
lower-tail. Seed 20260417. Pre-reg SHA committed. No deviations.

## Connections

- Parent [[h-new-146-q50-qaf-hub|H-NEW-146]] Cell C: ratified as "root-feature-specific weak
  tendency"
- [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (char-4-gram Fisher-Rao): confirmed as cross-feature
  replication ANCHOR; replication of this particular sub-test NULL
- Relates to [[h-new-150-liturgical-hub|H-NEW-150]]'s WEAK-LINK verdict for liturgical-hub: similar
  pattern of "parent claim weakened under alternative-feature / alternative-
  regressor test"

## Honest limits

1. Sample size (n=3 singletons) inherently low-power. Near-significance
   at any reasonable single-test threshold would be surprising.
2. Char-4-gram captures ORTHOGRAPHIC patterns; may be orthogonal to the
   THEMATIC content captured by roots. Both are valid features but not
   interchangeable.
3. [[h-new-146-q50-qaf-hub|H-NEW-146]]'s near-miss was never Bonferroni-3-passable; this
   replication doesn't help push it there.

## Follow-ups queued

- **H-NEW-151.1**: replicate under surface-word FR ([[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] scratch
  feature space) as a third feature space.
- **H-NEW-151.2**: test direct phonological similarity of the three
  letters ص, ق, ن — they are all coronal/uvular consonants; is there
  a phonological-feature-based sub-cluster claim?

## Honest null reporting

Published with equal prominence. The direction-consistency is a genuine
observation but the strict inferential test fails.
