---
surah: 89
test_id: Q089-F-04
title: Q 89 H-NEW-1070 oath-cluster centrality + 2-tier structure verification
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q089-F-04-oath-cluster-centrality
alpha_bon: 0.025
---

# Q089-F-04 — Pre-registration: Q 89 oath-cluster centrality and 2-tier structure verification

## 1. Hypothesis (locked before observation)

H-NEW-1070 (CONFIRMED, p=0.0004) established the strict-15 *wa-l-* oath-opener cluster as FR-cohesive: {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}. Q037-F-04 (NULL on individual extension) showed that Q 37 sits at rank 15/15 in cluster centrality — the LEAST-central member — and proposed a 2-tier structure: TIER 1 (CORE) short-Meccan-tail {Q 85, 86, 89, 91, 92, 93, 95, 100, 103} and TIER 2 (PERIPHERY) mid-mushaf {Q 37, 51, 52, 53, 77, 79}.

Q 89 sits at the BOUNDARY between TIER 1 and TIER 2: it's the largest short-Meccan-tail surah (30 verses) and the FIRST H-NEW-1070 cluster member by mushaf order on the short-tail side (Q 89, 91-103 form a contiguous arc; Q 79, 77, 85, 86 are scattered earlier).

**H1 (locked direction, primary)**: Q 89's mean FR distance to the OTHER 14 oath-cluster members (D_oath_q89) is **LOWER** than its mean FR distance to a corpus-random 14-surah sample, at α_bon = 0.025 over 10,000 random-14-subsamples.

**H2 (locked direction, secondary, exploratory)**: Q 89 sits in TIER 1 (CORE) — operationalized as: Q 89's mean distance to TIER 1 members (excluding self) is LOWER than to TIER 2 members. This tests whether Q 89 is genuinely a CORE oath-cluster member or whether (like Q 37) it has divergent FR-affinity.

**H0**: Q 89 has no preferential FR-affinity to the oath cluster, OR Q 89 sits with TIER 2 mid-mushaf surahs in FR space.

## 2. Operational definitions

- **Source**: H-NEW-111 FR distance matrix (D_matrix_upper_triangular in `findings/phase-b-hypotheses/csv/h-new-111.json`).
- **Strict-15 oath cluster**: O = {37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}.
- **TIER 1 (core)** (locked from Q037-F-04 finding): T1 = {85, 86, 89, 91, 92, 93, 95, 100, 103} (9 surahs, including Q 89 itself).
- **TIER 2 (periphery)**: T2 = {37, 51, 52, 53, 77, 79} (6 surahs).
- **D_oath_q89** = mean over s ∈ O \ {89} of FR(89, s).
- **D_random_null**: 10,000 trials, draw uniform-random 14-subset R from {1..114} \ {89}; compute D_R = mean(FR(89, s) for s in R). Permutation p = fraction with D_R ≤ D_oath_q89.
- **TIER 1 vs TIER 2 diagnostic**: M_t1 = mean FR(89, s) for s ∈ T1 \ {89} (8 surahs); M_t2 = mean FR(89, s) for s ∈ T2 (6 surahs). H2 PASS if M_t1 < M_t2.

## 3. Test statistic

- **H1**: D_oath_q89, D_random distribution, perm-p (one-tailed: D_oath_q89 ≤ random).
- **H2**: M_t1, M_t2; signed-difference M_t2 − M_t1 (PASS if positive).

## 4. Success / Failure

- **CONFIRMED**: H1 perm-p ≤ α_bon = 0.025 AND H2 PASS.
- **DIRECTIONAL**: only one of H1/H2 passes.
- **NULL**: both fail.
- **Pre-commit violation**: D_oath_q89 > corpus-mean (Q 89 ACTIVELY REPELLED from the cluster); OR M_t1 > M_t2 + 0.10 (Q 89 sits with periphery, not core).

## 5. Honest limits known a priori

- Empirical-anchor extraction (DISCLOSED): inspecting Q 89's FR-row from H-NEW-111 matrix shows top-15 nearest are dominated by short-tail surahs ({Q 108, 105, 106, 113, 100, 93, 94, 112, 110, 114, 107, 97, 103, 111, 99}), of which 4 are H-NEW-1070 oath-cluster members (Q 100, 93, 103, 92 in extended top-20). Q 89 mean dist to corpus = 0.894 (BELOW corpus mean 0.923). This suggests Q 89 is itself near-central in the short-tail FR-region, which BIAS-supports H1.
- Per HANDOFF/04-DISCIPLINE.md, this empirical observation is disclosed; the test is run with locked direction. If H1 passes at extreme p (< 10⁻¹⁰), the verdict ceiling extends; otherwise PASS-DIRECTED.
- This is the COMPLEMENT TEST to Q037-F-04 (which found Q 37 at rank 15/15 in cluster centrality). If Q 89 ranks high (e.g., top-5 of 15 in centrality), it would CONFIRM the 2-tier structure proposed by Q037-F-04 from the OTHER direction.

## 6. Rules-tuple

`(no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (H1 perm-test, H2 tier-diagnostic). α_bon = 0.025.

## 8. SHA256 lock

Embedded in `scripts/Q089_F_04_oath_centrality.py`; verified at runtime.
