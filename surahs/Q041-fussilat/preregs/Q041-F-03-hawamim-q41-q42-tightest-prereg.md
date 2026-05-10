---
prereg_id: Q041-F-03
title: Q 41 ↔ Q 42 al-Shūrā — tightest ḥawāmīm pair on Fisher-Rao test
date: 2026-05-09
seed: 20260509
locked_at: 2026-05-09T23:05:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q041-F-03 — Q 41 ↔ Q 42 tightest HM-7 pair on FR

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Among the 21 pairwise Fisher-Rao distances within the ḥawāmīm cluster {Q 40, Q 41, Q 42, Q 43, Q 44, Q 45, Q 46}, the pair **(Q 41, Q 42)** is the **TIGHTEST** (= smallest FR distance) pair.

**Rationale**: al-Suyūṭī (*al-Itqān*, nawʿ 51 *al-Munāsaba*) identifies Q 41 and Q 42 as "two cousins" — both ḥawāmīm-opener-tanzīl, both HM-A sub-block, with strong thematic munāsabah (Q 41 → Q 42 continues the apologetic close-block into the universal-prophetology). The empirical prediction: FR distance between Q 41 ↔ Q 42 is the smallest in HM-7.

## 2. Null

**H0**: A pair other than (Q 41, Q 42) is the tightest HM-7 pair.

## 3. Operationalization

- Distance source: Fisher-Rao root-distribution distance from H-NEW-111 (`findings/phase-b-hypotheses/csv/h-new-111.json`, field `D_matrix_upper_triangular`).
- Pairs: 21 pairs from {40, 41, 42, 43, 44, 45, 46}.
- Tightest = minimum FR distance.

## 4. Direction lock

Pre-committed: pair (Q 41, Q 42) = rank 1 of 21 tightest. Any other pair at rank 1 = NULL (pre-commit violation if direction reversed).

## 5. Bonferroni

Single test on a pre-committed pair; k = 1.

## 6. Success / failure criteria

- **VINDICATION**: pair (Q 41, Q 42) is the minimum of the 21 HM-7 pairwise distances.
- **NULL**: any other pair is the minimum.
- If NULL, publish prominently per protocol §1.3 (equal NULL prominence) and §1.8 (honest pre-commit violations).

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q041-F-03.json`: SHA, full HM-7 pair ranking, Q 41-Q 42 rank, verdict.

## 9. Rationale (extended)

The HM-7 cluster is one of the most-discussed surah-clusters in classical *munāsaba* literature. al-Biqāʿī (*Naẓm al-durar*) treats Q 41 → Q 42 as a tight semantic continuation. al-Suyūṭī catalogs the cluster as a coherent unit. The Fisher-Rao test of root-distribution distance is the strongest available empirical proxy for content-level cluster cohesion. If the classical "two cousins" claim is empirically valid, the FR distance should be minimum within the cluster.

**Important note**: This pre-reg is direction-locked BEFORE running the test. The honest verdict (whatever it is) is recorded.

## 10. Cross-references

- [[h-new-111-mushaf-fr-information-geodesic|H-NEW-111]] — FR distance matrix
- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]
- [[Q042-al-shura/00-overview|Q 42 al-Shūrā]] — the partner surah
- al-Suyūṭī *al-Itqān*, nawʿ 51 *al-Munāsaba bayna al-suwar*
- al-Biqāʿī *Naẓm al-durar*, ad Q 41 → Q 42 transition
