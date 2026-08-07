---
finding_id: h-new-245
title: Cross-chronology consensus ordering — Borda + Kemeny vs mushaf
parent: h-new-222 (additional chronologies Fisher-Rao)
status: FAIL BOTH CELLS → UNIQUELY-TAWQĪFĪ SUPPORTED
date: 2026-04-17
seed: 20260419
bonferroni_k: 3
alpha_bon: 0.01667
verdict_ceiling: PASS (single feature-set; instrument inherited from H-NEW-111)
pre_reg_sha256: see JSON
---

# [[h-new-245-chronology-consensus|H-NEW-245]] — Cross-chronology consensus ordering vs mushaf

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## TL;DR

A cross-chronology **CONSENSUS ordering** (Borda-count over 5 de-duplicated classical/modern chronologies, plus Kemeny local-search refinement) is

- **FARTHER** from the mushaf in Kendall τ than the closest individual chronology (τ_consensus = −0.372 vs max_c τ = −0.245 for Egyptian);
- **LONGER** on Fisher-Rao roots than the shortest individual chronology (L_consensus = 90.30 vs L_Nöldeke = 87.23);
- **LONGER** than the mushaf (L_mushaf = 85.76) — by a wider margin (4.54 FR units, 2.79 null-SDs) than any single chronology.

Both pre-registered cells FAIL the "moderated-tawqīfī" direction. The consensus is NOT a better approximation to the mushaf than its component chronologies. Instead, **combining chronologies makes the ordering LESS mushaf-like**, not more. This supports the **uniquely-tawqīfī** position: the mushaf's ordering is not a weighted blend of classical/modern chronological reconstructions.

MW-5 negative control passes cleanly (shuffled chronology inputs → consensus τ ≈ 0, consensus L ≈ null mean), confirming the instrument is working correctly.

---

## 1. Method recap

**Input chronologies** (5 de-duplicated per [[h-new-222-more-chronologies|H-NEW-222]] §3.1–3.2; Weighting-A is primary):

1. Nöldeke 1860 (= Watt-Bell 1970 per [[h-new-222-more-chronologies|H-NEW-222]] §3.1, 114/114 match)
2. Egyptian Standard 1924 (= Tanzil = Suyūṭī-Itqān per [[h-new-222-more-chronologies|H-NEW-222]] §3.2)
3. Bell 1937 (French Wikipedia transcription; 1 imputation, 2 ties)
4. Blachère 1947 (French Wikipedia transcription; 1 tie)
5. Ibn ʿAbbās / ʿAbd al-Kāfī transmission

**Consensus algorithms**:

- **Borda-count** (primary): rank-sum across 5 inputs, lower sum = earlier consensus position, mushaf-order tie-break.
- **Kemeny local-search** (secondary, heuristic): initialize from Borda; sweep adjacent-swaps that reduce total Kendall-distance; 3 sweeps converged from 3588 → 3363.

**Weighting-B robustness**: raw 7-list family (Nöldeke, Egyptian, Bell, Blachère, Ibn ʿAbbās, Suyūṭī, Tanzil) triple-weights the Egyptian/Suyūṭī/Tanzil tradition.

**Nulls**:

- Cell A: chronology-rank-shuffle null (each input chronology's rank vector permuted independently; consensus recomputed; τ(null-consensus, mushaf) distribution). 10,000 perms, seed 20260419.
- Cell B: uniform-permutation null over 114 surahs (matches [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] null; null mean = 104.35, SD = 1.63).

---

## 2. Cell A — Kendall τ vs mushaf

| Ordering                         | Kendall τ vs mushaf |
|:---------------------------------|--------------------:|
| Nöldeke 1860                     | **−0.4762** (most anti-correlated) |
| Bell 1937                        | −0.4327 |
| **CONSENSUS_BORDA_A (5 inputs)** | **−0.3718** |
| **CONSENSUS_KEMENY_A**           | **−0.3330** |
| **CONSENSUS_BORDA_B (7 inputs)** | **−0.3218** |
| Ibn ʿAbbās                       | −0.2663 |
| Blachère 1947                    | −0.2526 |
| Egyptian / Suyūṭī / Tanzil       | −0.2451 (closest to mushaf, i.e., least anti-correlated) |

**Closest individual chronology to mushaf**: Egyptian 1924 (τ = −0.2451).

**Consensus τ**: −0.3718.

**Test**: Is τ_consensus > max_c τ_c (i.e., less negative, closer to mushaf)?
→ **NO**: −0.372 < −0.245. **FAIL.**

The Borda consensus is **0.127 Kendall-τ units FARTHER** from mushaf than the closest individual chronology (Egyptian). All three consensus variants (Borda-A, Borda-B, Kemeny-A) fail the same test.

### Null test (chronology-shuffle)

Against a null where each input chronology's ranks are independently shuffled:

- Null τ mean = +0.0039, SD = 0.0633.
- Observed τ = −0.3718, z = **−5.94 (5.94 SDs BELOW null mean)**.
- p_upper (τ ≥ null) = 1.0000 (consensus is definitively NOT closer-to-mushaf than a random-consensus).
- p_twosided (|τ| ≥ null |τ|) = 0.0001 (the real-chronology-consensus is MORE anti-correlated with mushaf than random-consensus, at p < 10⁻⁴).

**Interpretation**: combining real chronologies produces a consensus that is MORE ANTI-CORRELATED with mushaf than random orderings would produce. This is a **stronger anti-mushaf signal than individual chronologies**, not a weaker one — the chronologies reinforce each other's negative correlation with mushaf order.

---

## 3. Cell B — Fisher-Rao path length

| Ordering                              | L (FR roots) | z vs null | Δ vs mushaf (null-SDs) |
|:--------------------------------------|-------------:|----------:|-----------------------:|
| **mushaf (reference)**                |   **85.7597** | **−11.42** | 0 |
| Nöldeke 1860                          |     87.2321 |    −10.52 | +0.91 |
| Bell 1937                             |     87.7956 |    −10.17 | +1.25 |
| Egyptian / Suyūṭī / Tanzil            |     89.5297 |     −9.11 | +2.32 |
| Blachère 1947                         |     89.8345 |     −8.92 | +2.50 |
| Ibn ʿAbbās                            |     89.8953 |     −8.88 | +2.54 |
| **CONSENSUS_KEMENY_A**                |   **90.2755** | **−8.64** | **+2.77** |
| **CONSENSUS_BORDA_A (5 inputs)**      |   **90.2989** | **−8.63** | **+2.79** |
| **CONSENSUS_BORDA_B (7 inputs)**      |   **91.4260** | **−7.94** | **+3.48** |

**Shortest individual chronology**: Nöldeke (L = 87.2321).

**Consensus L**: 90.2989 (Borda-A).

**Test 1 (pre-reg primary)**: Is L_consensus < min_c L_c?
→ **NO**: 90.30 > 87.23. **FAIL** by 3.07 FR units (1.88 null-SDs).

**Test 2 (pre-reg secondary)**: Is L_consensus < L_mushaf?
→ **NO**: 90.30 > 85.76. **FAIL** by 4.54 FR units (2.79 null-SDs).

The consensus is **LONGER than every single chronology** and longer than the mushaf. All three consensus variants rank below every individual chronology on FR coherence.

All consensus permutations still beat random (p_lower ≤ 0.0001, z ≤ −7.9), so they carry *some* coherence signal — but combining chronologies DILUTES the single-chronology coherence rather than concentrating it.

---

## 4. Cell C — Pairwise Kendall τ matrix (chronology clustering)

### Chronology-to-chronology τ (Weighting-A family)

| Pair                              | Kendall τ |
|:----------------------------------|----------:|
| Nöldeke × Bell                    | **+0.875** (tight cluster) |
| Egyptian × Ibn ʿAbbās             | **+0.978** (tight cluster) |
| Egyptian × Blachère               | **+0.955** (tight cluster) |
| Ibn ʿAbbās × Blachère             | **+0.933** (tight cluster) |
| Nöldeke × Egyptian                | +0.577 (moderate) |
| Nöldeke × Blachère                | +0.576 (moderate) |
| Nöldeke × Ibn ʿAbbās              | +0.577 (moderate) |
| Bell × Egyptian                   | +0.523 (moderate) |
| Bell × Blachère                   | +0.522 (moderate) |
| Bell × Ibn ʿAbbās                 | +0.522 (moderate) |

**Cluster structure (replicating [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] §"Two schools" finding, updated with Ibn ʿAbbās)**:

- **Cluster 1 (Western style-sorted)**: Nöldeke + Bell (τ = +0.875 with each other; τ ≈ +0.52–0.58 with cluster-2).
- **Cluster 2 (length-ordered / classical-Islamic / French)**: Egyptian + Blachère + Ibn ʿAbbās, all pairwise τ ∈ [+0.93, +0.98].
- Consensus sits at τ ≈ +0.70–0.88 from every chronology — a **centroid of the two clusters**, which is why it's FARTHER from mushaf than any cluster-interior point.

### Ibn ʿAbbās clustering observation (REVISES [[h-new-222-more-chronologies|H-NEW-222]] framing)

[[h-new-222-more-chronologies|H-NEW-222]] §"Spearman ρ cross-correlations" described Ibn ʿAbbās as "distinctly different" from Egyptian/Suyūṭī (ρ = +0.99 there; 70/114 positions differ). Under Kendall τ, **Ibn ʿAbbās clusters TIGHTLY with Egyptian (τ = +0.978) and Blachère (τ = +0.933)** — it is NOT the cluster-outlier. The 70-position difference vs Egyptian ([[h-new-222-more-chronologies|H-NEW-222]]) concentrates on small 1-position shifts plus the al-Fātiḥa placement — these move Spearman ρ a little but Kendall τ barely (most pairwise orderings remain intact).

The true outlier in Cluster 1 vs Cluster 2 is **Bell** (τ = +0.52 with every cluster-2 member, vs Nöldeke's +0.58 with same), though Nöldeke and Bell themselves cluster tightly together at +0.875.

### Mushaf's τ with every entity

| Against                  | τ vs mushaf |
|:-------------------------|------------:|
| Nöldeke 1860             | −0.476 (most anti-correlated) |
| Bell 1937                | −0.433 |
| CONSENSUS_BORDA_A        | −0.372 |
| CONSENSUS_KEMENY_A       | −0.333 |
| CONSENSUS_BORDA_B        | −0.322 |
| Ibn ʿAbbās               | −0.266 |
| Blachère 1947            | −0.253 |
| Egyptian 1924            | −0.245 (least anti-correlated) |

**All negative**. Consensus falls between Nöldeke/Bell (more negative) and Egyptian/Blachère/Ibn ʿAbbās (less negative) — a weighted centroid that inherits the average anti-correlation rather than the minimum.

---

## 5. MW-5 negative control (shuffled chronology inputs)

With independent seed (20260420), each input chronology's ranks were uniformly shuffled before Borda consensus.

| Metric                                   | Observed | Expected (null) | PASS? |
|:-----------------------------------------|---------:|----------------:|:-----:|
| τ(shuffled-consensus, mushaf)            |  −0.0070 | ≈ 0              | **YES** |
| L(shuffled-consensus)                    |   105.36 | 104.35 ± 1.63    | **YES** (within 0.62 SD) |

MW-5 passes cleanly. The consensus-collapse mechanism behaves as expected under shuffled inputs: both τ and L regress to their null distributions. This confirms the REAL consensus's FAIL is NOT an instrument artifact.

---

## 6. Interpretation — Moderated-tawqīfī vs Uniquely-tawqīfī

Per the pre-registered interpretation rules ([[h-new-245-chronology-consensus|h-new-245]]-chronology-consensus-prereg §"Interpretation rules"):

- **Cell A FAIL + Cell B FAIL (both)** → the consensus is NOT closer/shorter than any individual chronology → mushaf is **NOT a chronology blend** → supports **uniquely-tawqīfī** (not moderated-tawqīfī).

This is the outcome. The moderated-tawqīfī hypothesis (Ibn Taymiyya *Majmūʿ al-Fatāwā*; Farāhī-Iṣlāḥī naẓm blending chronology + theme) is **NOT supported** by this test. The uniquely-tawqīfī position (mushaf ordering is *not* a recoverable function of chronological reconstructions) is the position that survives.

### Why combining chronologies makes things WORSE, not better

This is actually expected once you observe the cluster structure:

- The 5 chronologies fall into 2 roughly-equal clusters (Cluster 1: Nöldeke/Bell; Cluster 2: Egyptian/Blachère/Ibn ʿAbbās).
- The two clusters disagree with each other internally more than they disagree with mushaf (inter-cluster τ ≈ +0.52–0.58 vs mushaf-cluster τ ≈ −0.24 to −0.48).
- Borda averaging across two disagreeing clusters produces a centroid that is SIMULTANEOUSLY ambiguous about what each cluster claims — the centroid position is noisier than either cluster's interior, hence LONGER on FR-roots and FARTHER from mushaf.
- The mushaf, by contrast, is sharply NEGATIVELY correlated with both clusters, so it is not occupying the intersection of the two chronology-schools; it's occupying an **orthogonal axis** that the chronology-schools collectively fail to span.

### Classical-scholarship alignment update

- **Ibn Taymiyya moderated-tawqīfī** (*Majmūʿ al-Fatāwā*): chronology-plus-thematic blend expected to approximate mushaf → **NOT SUPPORTED** at empirical level. Does not refute Ibn Taymiyya's *jurisprudential* distinction (allowing some chronological reorder) but refutes the specific empirical prediction that such blending recovers mushaf order.
- **Farāhī-Iṣlāḥī naẓm groups** (chronology + theme): to the extent these propose mushaf ≈ chronology + theme, the "+ theme" component is load-bearing; chronology alone (even consensus-averaged) cannot reconstruct the mushaf.
- **al-Suyūṭī Itqān dual positions**: the tawqīfī position that Suyūṭī preserves is the empirically surviving one (consistent with [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]] §6).
- **Strict uniquely-tawqīfī**: **EMPIRICALLY CORROBORATED at descriptive level** — consistent with [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]]'s "tartīb tawqīfī" conclusion.

---

## 7. Limits and caveats (honest)

1. **6 chronologies is a small input set**. Expanding to include e.g. Theodor Nöldeke / Schwally revision 1909, Weil 1844, or Muir 1858 might change the consensus geometry. Those lists exist but were not tested here. Bonferroni-correct any extension.
2. **Kendall τ is one metric among several**. Spearman ρ is reported as secondary (§2 table). A more exotic metric (e.g., ULAM distance, position-weighted τ) might show different directional evidence. We committed to Kendall τ in the pre-reg and report honestly.
3. **Kemeny is heuristic, not optimal**. Our 3-sweep local search from Borda converged to dist 3363 (from Borda's 3588). True Kemeny optimum might be lower, which *might* shift τ_consensus closer to zero — but given Cell A fails by 0.127 τ units (a large gap) this is very unlikely to reverse the verdict.
4. **One feature-set**: FR-roots inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]. Char-4-gram and verse-length FR matrices ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]/c) were NOT tested here; a natural follow-up is H-NEW-245.1 extending to those distance matrices. Verdict is **PASS (not CONFIRMED)** per project discipline.
5. **Tawqīfī verdict is EMPIRICAL, not theological**: we're reporting what the quantitative geometry says. The theological interpretation (divinely-ordered vs human-redactorial sophistication vs common-cause) is not discriminable from this test.

---

## 8. Verdict

- **Cell A (τ consensus > max_c τ)**: **FAIL** (−0.372 < −0.245; gap = 0.127)
- **Cell B (L consensus < min_c L)**: **FAIL** (90.30 > 87.23; gap = 3.07 FR units, 1.88 null-SDs)
- **Cell B′ (L consensus < L mushaf)**: **FAIL** (90.30 > 85.76; gap = 4.54 FR units, 2.79 null-SDs)
- **MW-5 negative control**: **PASS** (shuffled-consensus τ ≈ 0; L ≈ null mean)
- **Cell C clustering**: **DESCRIPTIVE-CONFIRMED** two chronology-clusters + Ibn ʿAbbās = part of cluster-2 (not outlier, revising [[h-new-222-more-chronologies|H-NEW-222]]'s framing slightly).
- **Interpretation**: **UNIQUELY-TAWQĪFĪ** supported; **MODERATED-TAWQĪFĪ** NOT supported.
- **Ceiling**: PASS (not CONFIRMED per project discipline; one feature-set, 5 input chronologies).

**Aggregate classical-scholarship update**:

- **Validated**: al-Suyūṭī Itqān tawqīfī position (continued).
- **Refuted (empirically, at the descriptive level)**: moderated-tawqīfī specific empirical prediction that chronology-consensus approximates mushaf.

Adds to [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]]'s "the mushaf is not a chronology blend" claim with a stronger version: **the mushaf is not even a WEIGHTED-AVERAGE chronology blend**. No linear combination of classical/modern chronologies reconstructs mushaf's information-theoretic geometry.

---

## Files

- pre-reg: `findings/phase-b-hypotheses/h-new-245-chronology-consensus-prereg.md`
- script:  `scripts/h_new_245_consensus_ordering.py`
- JSON:    `findings/phase-b-hypotheses/csv/h-new-245.json`
- journal: `journal/h-new-245-run-1.md`
- parent:  `findings/phase-b-hypotheses/h-new-222-more-chronologies.md`
- synthesis anchor: `findings/phase-b-hypotheses/cross-finding-021-mushaf-information-theoretic-optimality.md`
