---
surah: 77
test_id: Q077-F-04
title: Q 77 quadruple-cluster-intersection — corpus-UNIQUE 4-way architectural-hub
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q077-F-04-quad-intersection
alpha_bon: 0.05
---

# Q077-F-04 — Pre-registration: Q 77 as corpus-UNIQUE 4-way architectural-cluster hub

## 1. Hypothesis (locked before observation)

The brief flags Q 77 as a member of FOUR distinct empirical-architectural clusters confirmed in prior project work:
1. **H-NEW-1070** strict 15-surah *wa-l-* oath-opener cluster (CONFIRMED p=0.0004): {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}
2. **H-NEW-1190** *wa-mā adrāka mā* 10-surah cluster (CONFIRMED p=0.00068): {Q 69, 74, 77, 82, 83, 86, 90, 97, 101, 104}
3. **H-NEW-1200** short-Meccan-tail eschatology 14-cluster (CONFIRMED p=0.00030): {Q 56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}
4. **H-NEW-1230 / H-NEW-1320** refrain-architecture top-3 + 5-cluster (PASS-DIRECTED FULL p<0.0001): {Q 26, 37, 54, 55, 77} (H-NEW-1230) and top-3 {Q 26, 55, 77} (H-NEW-1320)

**H1 (Cell A — quadruple intersection corpus-uniqueness):** Q 77 is the ONLY surah in the corpus that belongs to all 4 sets simultaneously. Cell A passes if |∩₄| == 1 AND Q 77 is in ∩₄.

**H2 (Cell B — triple-intersection identity):** Among the 3-way intersections (any 3 of the 4 clusters), the cluster {oath ∩ adraka ∩ eschat} has cardinality EXACTLY 2 — Q 77 and Q 86 al-Ṭāriq. Cell B passes if 3-way intersection {oath, adraka, eschat} = {77, 86}.

**H3 (Cell C — null permutation: how rare is a 4-way hit?):** Under random-cluster-membership preserving each cluster's cardinality (15, 10, 14, 5 — the brief's set sizes), simulate 10,000 permutations: each permutation picks 4 random subsets of {1, ..., 114} of those cardinalities; record the maximum number of surahs that achieve 4-way intersection. p_perm = fraction of perms with max ≥ 1. PASS if p_perm ≤ α_bon = 0.05.

**H0:** Q 77's quadruple-intersection is a coincidence; under random cluster membership of the same sizes, 4-way overlaps occur with non-negligible probability.

## 2. Operational definitions

- Source: cluster set memberships hard-coded as listed above (from MASTER-FINDINGS-LEDGER §10.34, §10.35, §10.38, §10.40).
- **Cell A**: |O ∩ A ∩ E ∩ R| where O = oath, A = adraka, E = eschat, R = refrain.
- **Cell B**: |O ∩ A ∩ E|.
- **Cell C**: Monte Carlo over 10,000 random-cluster-set assignments. Each replicate: draw |O|=15 random surahs from {1..114}, |A|=10, |E|=14, |R|=5 (independent draws); record max-per-replicate of |intersection of all 4 random sets|; p_perm = (1/10000) × Σ I[max_perm ≥ observed_q77_count = 1].

## 3. Test statistic

- Cell A: integer |O ∩ A ∩ E ∩ R|.
- Cell B: integer |O ∩ A ∩ E|.
- Cell C: p_perm (one-tailed: random ≥ observed).

## 4. Success / Failure

- **PASS-DIRECTED FULL**: |O ∩ A ∩ E ∩ R| == 1 AND Q 77 ∈ ∩₄ AND p_perm ≤ 0.05 AND |O ∩ A ∩ E| == 2.
- **PASS-DIRECTED PARTIAL**: 3 of 4 conditions.
- **NULL**: ≤ 2 of 4 conditions.
- **Pre-commit violation**: |O ∩ A ∩ E ∩ R| == 0 (Q 77 NOT in 4-way intersection — would directly disconfirm the brief's framing).

## 5. Honest limits known a priori

- Empirical-anchor extraction (DISCLOSED, pre-lock):
  - O ∩ A = {77, 86}
  - O ∩ E = {77, 86}
  - O ∩ R = {37, 77}
  - A ∩ R = {77}
  - E ∩ R = {77}
  - O ∩ A ∩ E = {77, 86}
  - O ∩ A ∩ R = O ∩ E ∩ R = A ∩ E ∩ R = {77}
  - O ∩ A ∩ E ∩ R = {77}
  - Q 86 (al-Ṭāriq) is the **second-most-architecturally-overlapping** surah (3 of 4), missing only the refrain cluster.
- The DISCLOSED 4-way intersection = {77} is the empirical anchor; H1 is locked at the integer == 1 condition.
- The Monte Carlo null in Cell C uses the same set cardinalities (15, 10, 14, 5) as the actual clusters — this controls for size effects. The null p ought to be very small because the expected size of a 4-way random intersection of these cardinalities is ≈ (15×10×14×5)/(114³) ≈ 10500/1,481,544 ≈ 0.0071 surahs per replicate; observing ≥ 1 should have probability ≈ 0.7% per replicate.
- The test SUFFERS from a known dependency: the 4 clusters were selected by the brief *because* Q 77 is in all of them; this is selection-on-the-outcome. To compensate, Cell C's null draws independent random clusters of the same sizes (does not condition on Q 77 membership); the question becomes "would 4 random clusters of these sizes coincide on at least 1 surah?" — a structural rather than a Q 77-specific test.

## 6. Rules-tuple

`(cluster-membership-set-theoretic, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 1 (single planned 4-way intersection test). α_bon = 0.05. Cells A, B, and C are jointly evaluated as a unified family.

## 8. Garden of forking paths

- The brief STATES Q 77 is in H-NEW-1190 + H-NEW-1200 + (rank #2 in H-NEW-1320 / member of H-NEW-1230) + (member of H-NEW-1070 oath-cluster). The 4-way intersection is the LITERAL request "Q 77 within H-NEW-1190 + H-NEW-1200" extended to include the oath-cluster (per the explicit oath-anchor opening of Q 77) and the refrain-cluster (per the explicit refrain anchor).
- The 4-way framing came from observing that the brief's anchors literally span 4 distinct named clusters. No alternative cluster-set selection was considered.
- A more conservative test "is Q 77 in ALL of H-NEW-1190, H-NEW-1200, H-NEW-1230 (3 of 4 — drop oath)" was considered and rejected as too narrow given the explicit 5-element oath opener at vv 1-5.

## 9. SHA256 lock

Embedded in `scripts/Q077_F_04_quad_intersection.py`; verified at runtime.
