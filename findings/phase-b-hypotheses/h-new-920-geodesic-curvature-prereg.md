# [[h-new-920-geodesic-curvature-prereg|H-NEW-920 — pre-registration]] — Discrete geodesic curvature of the mushaf path

**Finding ID**: h-new-920
**Specialist**: geodesic-curvature-specialist
**Date**: 2026-05-07
**Seed**: 20260507
**Parent**: [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (114×114 Fisher-Rao distance matrix on QAC stem-roots)
**Anchors**: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (mushaf is FR information-geodesic optimal: L_mushaf/L_2opt = 1.107); [[h-new-130-fisher-rao-residuals|H-NEW-130]] (15 top-jumps coincide 100% with classical block-boundaries); [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] (M1.3 structural hinges close 73% of the 4-principle simulator residual); [[cross-finding-020-the-complete-equation|cross-finding-020]] (the complete equation context).
**Rules-tuple (inherited from H-NEW-111, NOT reset)**: `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, Fisher-Rao arccos-Bhattacharyya per-surah-distribution, K_top_roots=500, dirichlet_alpha=0.5, mushaf order, Hafs-Kūfan)`. **This finding inherits all of these analytical choices from H-NEW-111. Any rules-tuple sensitivity is downstream of H-NEW-111.**

---

## 1. Motivation

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] established that the mushaf traces a **near-geodesic path** through the Fisher-Rao information manifold: L_mushaf / L_2opt ≈ 1.107 (11% from TSP-optimum on TOTAL length). [[h-new-130-fisher-rao-residuals|H-NEW-130]] characterised the 11% residual *by edge length*: the 15 LARGEST consecutive-pair distances all land on classical block-boundaries.

But total path length and per-edge length say nothing about **path-direction stability**. A geodesic of length 113 can be near-length-optimal yet have **sharp turning points** — positions where the manifold-direction inverts abruptly. These are "structural hinges in the curvature sense": positions where the previous-arrival vector and the next-departure vector disagree most.

Curvature is the **second-order** feature of the mushaf path. Edge-length is first-order. To our knowledge no prior analysis (in this project or in classical scholarship) has computed it for the mushaf.

**Why this matters**: a curvature peak at position i means s_{i-1} → s_i and s_i → s_{i+1} occupy substantively different regions of the FR manifold. If curvature peaks coincide with thematic / chronological / structural boundaries (Mufaṣṣal-onset at Q 50, the ḥawāmīm-cluster boundary at Q 39 → Q 40, the early Medinan onset around Q 2), this provides an INDEPENDENT confirmation of those boundaries that does NOT reduce to either edge-length (H-NEW-130) or total-path-length (H-NEW-111). Curvature is a triangle-inequality slack: small if the path "passes through" s_i straight, large if it "bends" there.

---

## 2. Hypothesis (DIRECTION-LOCKED before computation)

### 2.1 H1a — boundary-co-incidence of top-10 curvature positions

Three pre-committed thematic boundaries (selected from classical scholarship + prior findings, BEFORE looking at curvature spectrum):

| label | boundary | ±2 surah-position window |
|:--|:--|:--|
| **B1** Mufaṣṣal-onset | Q 50 (al-Zarkashī *al-Burhān* nawʿ 1; al-Suyūṭī *al-Itqān* nawʿ 18 *al-mufaṣṣal*) | interior positions i ∈ {48, 49, 50, 51, 52} |
| **B2** Ḥawāmīm-cluster boundary | Q 39 → Q 40 (entry into the seven Ḥā-Mīm surahs) | i ∈ {38, 39, 40, 41, 42} |
| **B3** Medinan-block-onset | Q 2 (al-Suyūṭī Meccan/Medinan chronology; first long Medinan block after Q 1) | i ∈ {2, 3, 4} (lower bound at i=2 since interior positions start at 2) |

(Note: interior positions are i ∈ {2, …, 113}; B3's window naturally clips at 2.)

**H1a primary**: of the **top-10 curvature positions** (by primary metric `turn_cost`, see §4), **at least 4** fall inside the union B1 ∪ B2 ∪ B3 (i.e., within ±2 of at least one of Q 2, Q 40, Q 50).

**Direction-lock**: ≥4 hits is the PASS direction. <4 hits is NULL or DIRECTIONAL. NEVER reversible.

**Bonferroni-3** on the family of three boundary-cluster sub-tests:

  - **H1a.B1**: of top-10, at least 2 hit B1 (window 48-52). Null hypergeometric (N=112 interior, K=5 boundary slots, n=10): expected 0.446, P(≥2) = exact-tail.
  - **H1a.B2**: of top-10, at least 2 hit B2 (window 38-42). Same null shape (5 slots).
  - **H1a.B3**: of top-10, at least 1 hit B3 (window 2-4, 3 slots given interior-clip). Null P(≥1) under hypergeometric.
  - **Joint**: at least 4 hit any of B1 ∪ B2 ∪ B3 (windows union; account for overlap if any — none here since |2−40|, |40−50|, |2−50| all > 4).

α_bon = 0.05 / 3 = **0.01667** per sub-test. Joint test reported separately at α = 0.05 (it is the headline summary of the three sub-tests, not a 4th independent test).

**Permutation null (10000 perms)**: shuffle the 114 surah-indices uniformly random; recompute the 112 turn-costs on the shuffled path through the SAME H-NEW-111 FR matrix; record top-10 positions and count hits in the same boundary-windows. Empirical p-value = #{perms with ≥ k_obs hits} / 10000. Report this p-value alongside the hypergeometric exact-tail p (which assumes all interior positions are exchangeable — the perm-null is the gold standard).

### 2.2 H1b — corpus-mean turning angle vs uniform-random null

**H1b**: the empirical mushaf's mean `turn_cost` (averaged over the 112 interior positions) is **strictly LESS** than the perm-null mean. Equivalently: the mushaf is *locally smoother* than expected at random along its FR path, beyond what total-length optimisation alone (H-NEW-111's L-statistic) can guarantee.

**Direction-lock**: empirical mean < perm-null 5th percentile = PASS. Empirical mean > perm-null 95th percentile = REVERSED → publish as PRE-COMMIT VIOLATION (NULL with prominence). Empirical mean inside [5%, 95%] = NULL-NEUTRAL.

α = 0.05 (two-sided perm, but DIRECTION-LOCKED below; one-tailed lower lookup).

### 2.3 No 4th hypothesis sneak

These two hypotheses (H1a ternary + H1b mean) are the ENTIRE pre-reg. We will report descriptive statistics (e.g., top-10 list, distribution shape) but no further pre-registered tests in this run. Any post-hoc observation is α = 0.05 single-test ceiling per MW-7.

---

## 3. Null distribution design (10000 permutations, seed = 20260507)

For each permutation r ∈ {1, …, 10000}:
1. Draw a uniform-random permutation π_r of (1, 2, …, 114) using `random.Random(20260507 + r)`.
2. Compute the 112 turn-costs along the permuted path s_{π_r(1)}, s_{π_r(2)}, …, s_{π_r(114)} using the H-NEW-111 FR distance matrix.
3. Record:
   - mean turn-cost (for H1b)
   - top-10 position-indices (in the path-ordering, i.e., the positions 2..113 of the permutation that have the highest turn-cost)
4. For H1a, the position-indices in the perm-null are tested against the SAME canonical interior-position windows B1∪B2∪B3 (because what we are measuring is whether *the path-order positions* land at the canonical mushaf positions 2-4, 38-42, 48-52). This means we ask: when a random ordering's curvature spectrum is computed, do its top-10 positions ALSO land near the canonical mushaf indices? This is the correct null for testing whether the empirical mushaf's curvature peaks have a structural reason to land where they do.

(Equivalent framing: under H_0, top-10 positions are uniformly distributed over {2,…,113}; the perm-null operationalises this by re-running the entire computation on shuffled paths.)

---

## 4. Curvature computation (DISCRETE, primary + secondary metric)

For path P = [s_1, s_2, …, s_114] (mushaf or permutation):

For each interior position i ∈ {2, …, 113}:
- d_in(i) = FR_distance(s_{i-1}, s_i) per H-NEW-111
- d_out(i) = FR_distance(s_i, s_{i+1}) per H-NEW-111
- d_skip(i) = FR_distance(s_{i-1}, s_{i+1}) per H-NEW-111

**Primary metric — `turn_cost(i)` (triangle-inequality slack)**:

  turn_cost(i) = d_in(i) + d_out(i) − d_skip(i)

Range: 0 (perfectly straight, equality in triangle inequality) to 2·max(d_in, d_out) (pathological reversal). FR-distances satisfy the triangle inequality (FR is a metric on the simplex), so turn_cost(i) ≥ 0 always.

**Secondary metric — `turning_angle(i)`** (Euclidean-pseudo, for diagnostic only; PRE-REGISTERED but NOT used for verdict):

  cos θ(i) = (d_in(i)² + d_out(i)² − d_skip(i)²) / (2 · d_in(i) · d_out(i))
  turning_angle(i) = arccos(clip(cos θ(i), -1, 1))

This treats the three pairwise distances as if embedded in a Euclidean triangle (which is an approximation since FR is not Euclidean, only metric). We compute and report turning_angle for replication, but **PRIMARY VERDICT IS BASED ON `turn_cost`** per pre-reg.

Top-10 by `turn_cost` (descending) = candidate curvature peaks.

---

## 5. Decision rule (locked)

### H1a (Bonferroni-3 family on top-10 boundary co-incidence):
- B1 hits ≥ 2 AND perm-p ≤ 0.01667 → B1 PASS
- B2 hits ≥ 2 AND perm-p ≤ 0.01667 → B2 PASS
- B3 hits ≥ 1 AND perm-p ≤ 0.01667 → B3 PASS
- Joint: union-hits ≥ 4 AND perm-p ≤ 0.05 → JOINT PASS (descriptive; not Bonferroni-counted)

Family verdict:
- ≥ 2 of 3 sub-cells PASS at α_bon → **PASS-DIRECTED** (replication needed for CONFIRMED)
- 1 of 3 sub-cells PASS → **DIRECTIONAL**
- 0 PASS → **NULL** for H1a
- Direction reversed (top-10 actively AVOIDS boundaries beyond random) → PRE-COMMIT VIOLATION, publish with prominence per Protocol §1.8

### H1b (mean turn-cost):
- emp_mean < perm-null 5th pct AND one-tailed perm-p ≤ 0.05 → PASS (mushaf is locally smoother than random)
- emp_mean ∈ [5%, 95%] → NULL-NEUTRAL
- emp_mean > perm-null 95th pct → PRE-COMMIT VIOLATION (mushaf is LOCALLY ROUGHER than random; reverse-direction; publish as NULL per §1.8)

### Overall verdict:
- H1a JOINT PASS + H1b PASS → CONFIRMED (curvature spectrum is structurally non-random AND lower-mean)
- H1a JOINT PASS + H1b NEUTRAL → PASS-DIRECTED (boundaries-aligned but no global smoothness gain)
- H1a NULL + H1b PASS → PASS-DIRECTED (smoother than random globally, but peaks not boundary-aligned)
- Both NULL → NULL FINDING (publish with full prominence)

Replication is NOT pre-registered for this run. Promotion to CONFIRMED requires a follow-up run on either: (a) char-4-gram FR matrix from H-NEW-130b (cross-feature replication), or (b) a different boundary set (e.g., al-Suyūṭī Meccan-phase transitions per H-NEW-130). Either is a separate pre-reg.

---

## 6. Inputs (file paths)

- FR matrix: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular`, 6441 entries, 114-surah pair-list).
- This pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-920-geodesic-curvature-prereg.md`.

---

## 7. Outputs (locked)

- Script: `/Users/grey/Downloads/quran/scripts/h_new_920_geodesic_curvature.py` (with embedded SHA256 of THIS FILE).
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-920.json` — full 112 turn-costs (and 112 turning-angles), top-10 list, perm-null summary (mean, std, percentiles, top-10-position-distribution), p-values, verdicts.
- Findings markdown: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-920-geodesic-curvature.md`.
- Journal: `/Users/grey/Downloads/quran/journal/h-new-920-run-1.md`.
- Ledger update: row appended to `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` after the H-NEW-910 row.

---

## 8. MW-1..MW-7 protections

- **MW-1 (instrument-prior)**: turn_cost = d_in + d_out − d_skip is locked here, BEFORE running. Secondary turning_angle computed but not used for verdict.
- **MW-2 (corpus-prior)**: 10000 permutations (seed 20260507).
- **MW-3 (alternative-models)**: turn_cost (primary) AND turning_angle (secondary) BOTH computed and reported. If they disagree on top-10 set, this is flagged in the findings.
- **MW-4 (over-fitting)**: no fitted parameters. Pure descriptive computation on a fixed FR matrix.
- **MW-5 (replication-positive-control)**: random-permutation null IS the MW-5 control.
- **MW-6 (instrument-control)**: deferred. Cross-feature replication (e.g., H-NEW-130b char-4-gram D-matrix) is a separate pre-reg.
- **MW-7 (post-hoc cap)**: any observation in this run beyond H1a/H1b carries α = 0.05 single-test ceiling.

---

## 9. Honest limits (PRE-COMMITTED)

1. **Inheritance from H-NEW-111**: turn_cost is a derived quantity from the FR matrix. If H-NEW-111's choice of (K_top_roots=500, Dirichlet α=0.5, QAC-STEM tokens) materially changes, our spectrum changes. We are NOT auditing those choices here.
2. **FR is metric, not Euclidean**: turn_cost is the natural triangle-slack and is the primary metric. turning_angle treats the three FR-distances AS-IF Euclidean and is approximate. The two metrics will not agree perfectly; PRIMARY VERDICT uses turn_cost.
3. **Boundaries-list is finite**: B1/B2/B3 were chosen from classical scholarship + prior findings BEFORE looking at curvature. We did not optimise for boundary placement. If a curvature peak lands on a non-pre-committed boundary (e.g., al-sabʿ-al-ṭiwāl→mathānī transition at Q 9→Q 10), it counts AGAINST H1a unless we pre-committed it. We did not.
4. **No causal claim**: a curvature peak at position i means the FR path bends at s_i. It does NOT mean classical scholars consciously placed s_i to bend the path. It means classical block-boundaries CO-INCIDE with FR-curvature peaks IF H1a passes — a structural correlation, not a generative claim.

---

## 10. SHA256-locking instructions

After writing this file, compute its SHA256 and embed at the head of the run script. Verify at runtime; fail-fast on mismatch. This pre-reg file is FROZEN at the moment of SHA computation; any subsequent edit invalidates the SHA and requires a new pre-reg.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
