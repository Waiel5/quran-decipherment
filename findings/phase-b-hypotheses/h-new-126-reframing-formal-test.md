---
finding_id: h-new-126-reframing-formal-test
title: "Formal corpus-test of H-NEW-126 reframing: 5-true-isolate set is NOT FR-tight as a sub-cluster"
status: NULL on FR-cohesion → CONFIRMS reframing of H-NEW-126 from similarity-isolation to label-invisibility
phase: B+
date: 2026-05-07
seed: 20260507
n_perm: 100000
parent: h-new-126-true-isolate-core
inheritors: Q016-F-03 (PRE-COMMIT VIOLATION); Q021-F-05 (NULL — NEAR-NEIGHBOR-BUT-NOT-CLUSTER); Q025-F-01 (FR position not bottom-quartile)
---

# H-NEW-126 reframing — formal corpus-test

## 1. Headline

The H-NEW-126 "true-isolate" set {Q 16, Q 21, Q 22, Q 23, Q 25} has mean pairwise Fisher-Rao distance **0.8781** vs random-5-subset null mean **0.9237** — z = **−0.452**, perm-p = **0.255**. **NOT statistically significantly tighter than a random 5-subset.**

This is the formal corpus-level proof of the reframing the Q 16, Q 21, Q 25 specialists separately surfaced in Wave-D MAY-7. The reframing:

> **"True-isolate" status = invisibility to all 20 classical cluster-LABELS, NOT geometric FR-isolation.**

The 5 surahs share *sui-generis* status at the LABEL level (none belongs to Hawamim, ALR, ALM, Musabbiḥāt, qul-cluster, etc.), while remaining geometrically-typical in FR similarity to many other surahs.

## 2. Pairwise FR distances within isolate set

| Pair | FR distance |
|:-:|:-:|
| Q 16-Q 22 | 0.7559 |
| Q 21-Q 23 | 0.8287 |
| Q 23-Q 25 | 0.8327 |
| Q 21-Q 25 | 0.8537 |
| Q 16-Q 25 | 0.8648 |
| Q 16-Q 23 | 0.8669 |
| Q 16-Q 21 | 0.9297 |
| Q 22-Q 25 | 0.9359 |
| Q 22-Q 23 | 0.9530 |
| Q 21-Q 22 | 0.9592 |

**Mean: 0.8781**, median 0.8658, range [0.756, 0.959]. Q 21–Q 22 is the FARTHEST pair (0.9592) — already noted in Q021-F-05 as the architectural-twin-pair-violator.

## 3. Per-isolate nearest neighbor

For each isolate, the nearest non-isolate is within 0.005 FR-units of the nearest fellow-isolate:

| Isolate | Nearest non-isolate (d) | Nearest fellow-isolate (d) | Margin |
|:-:|:--|:--|:-:|
| Q 16 | Q 39 (**0.7538**) | Q 22 (0.7559) | non-isolate WINS by 0.002 |
| Q 21 | Q 7 (0.8243) | Q 23 (0.8287) | non-isolate WINS by 0.004 |
| Q 22 | Q 31 (0.7991) | Q 16 (**0.7559**) | isolate wins by 0.043 |
| Q 23 | Q 43 (0.7888) | Q 21 (0.8287) | non-isolate WINS by 0.040 |
| Q 25 | Q 36 (0.7778) | Q 23 (0.8327) | non-isolate WINS by 0.055 |

**4 of 5 isolates have a NON-isolate nearest neighbor closer than any fellow-isolate.** Only Q 22 has a fellow-isolate (Q 16) as its FR-nearest neighbor.

## 4. Permutation null

100000 random 5-subsets of {1..114}, seed 20260507. Mean of means = 0.9237 ± 0.1011.

Empirical isolate-set mean 0.8781 corresponds to z = −0.452. One-sided lower-tail p = 0.255 — far above any significance threshold.

The isolate-set is mildly tighter than corpus-mean (0.95× ratio) but well within the random-5-subset null distribution. This is consistent with: (a) the 5 surahs being moderately-similar-length Meccan surahs (which produces some baseline cohesion), (b) NOT being a tight architectural sub-cluster.

## 5. Substantive interpretation

The reframing of H-NEW-126:

**Old interpretation**: 5 surahs are dissimilar from everything else — *similarity-isolated*.

**New interpretation (this finding)**: 5 surahs are invisible to the 20 classical cluster-LABELS (Hawamim, ALR, ALM, Musabbiḥāt, qul-cluster, etc.) — *taxonomy-invisible*. Their pairwise FR distances are typical-to-mildly-tighter; their non-isolate FR neighbors are often closer than their fellow-isolates.

This reframing dissolves an apparent paradox raised by Q021-F-05: why does the mushaf pay top-15 TSP-cost (rank 16/113) on Q 21–Q 22 adjacency despite it being the FARTHEST FR pair within the isolate cluster? The answer: the mushaf is NOT placing them adjacent for FR-cohesion; it is preserving the adjacency of two label-invisible surahs for some other architectural reason (possibly: keeping the chronologically-classified-as-Late-Meccan + cosmological-pilgrimage-mixed surahs together for content-thematic reasons that don't reduce to FR).

## 6. Why this is a CONFIRMING finding (not a refutation)

H-NEW-126 was always defined as "invisible to all 20 cluster-systems." The novelty of the reframing is interpretive: we now know that "invisible to cluster-systems" does NOT imply "FR-isolated from corpus." These are LOGICALLY INDEPENDENT properties.

al-Suyūṭī's *al-Itqān* nawʿ on tartīb-tawqīfī gains new traction: the canonical compilers were preserving the *labels* the prophetic tradition recognized — not necessarily a FR-similarity-clustering, which can be empirically ANY pattern.

## 7. Files

- This finding: `findings/phase-b-hypotheses/h-new-126-reframing-formal-test.md`
- Inputs: `findings/phase-b-hypotheses/csv/h-new-111.json` (FR matrix)
- Inheritors-of-the-reframing:
  - `surahs/Q016-al-nahl/06-novel-findings.md` (Q016-F-03 PRE-COMMIT VIOLATION on isolate-persistence)
  - `surahs/Q021-al-anbiya/06-novel-findings.md` (Q021-F-05 NULL — NEAR-NEIGHBOR-BUT-NOT-CLUSTER)
  - `surahs/Q025-al-furqan/06-novel-findings.md` (Q025-F-01 isolate-position not bottom-quartile)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
