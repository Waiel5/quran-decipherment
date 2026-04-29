---
finding_id: h-new-245
title: Cross-chronology consensus ordering vs mushaf (Borda + Kemeny)
parent: h-new-222 (additional chronologies Fisher-Rao)
date: 2026-04-17
seed: 20260419
bonferroni_k: 3
alpha_bon: 0.01667
specialist: autonomous agent (H-NEW-245 lane)
classical_anchor: Ibn Taymiyya Majmūʿ al-Fatāwā (moderated tawqīfī); al-Suyūṭī Itqān (dual positions); Farāhī-Iṣlāḥī naẓm (chronology + theme blend)
---

# [[h-new-245-chronology-consensus|H-NEW-245]] — Cross-chronology consensus ordering vs mushaf

## Hypothesis

If the mushaf reflects a **moderated-tawqīfī** logic (Ibn Taymiyya) — i.e., divinely-fixed but informed by classical chronological + thematic consensus — then a CONSENSUS ordering built from multiple independent classical/modern chronologies should approximate mushaf better than any single chronology.

Concretely:

- **H-245-A**: Kendall τ(consensus, mushaf) > max_c Kendall τ(c, mushaf) across c ∈ {Nöldeke, Bell, Blachère, Egyptian, Suyūṭī-Itqān=Tanzil, Ibn ʿAbbās, Watt-Bell=Nöldeke}.
- **H-245-B**: L_FR(consensus) < min_c L_FR(c) across c in the same family.
- **H-245-C** (descriptive): confirm chronology clustering from [[h-new-222-more-chronologies|H-NEW-222]] — Nöldeke/Suyūṭī/Egyptian tight cluster; Ibn ʿAbbās outlier.

## Direction committed BEFORE execution

- H-245-A: consensus EXPECTED CLOSER to mushaf than best individual chronology.
- H-245-B: consensus EXPECTED SHORTER on FR-roots than best individual chronology.
- H-245-C: EXPECT Ibn ʿAbbās to be Kendall-τ-outlier relative to Nöldeke/Suyūṭī/Egyptian cluster.

## Method (frozen BEFORE execution)

### Input chronologies (6 distinct orderings; Watt-Bell ≡ Nöldeke per [[h-new-222-more-chronologies|H-NEW-222]] §3.1; Suyūṭī Itqān ≡ Tanzil per §3.2)

After de-duplication, 6 numerically distinct chronologies:
1. Nöldeke 1860 (= Watt-Bell 1970)
2. Egyptian Standard 1924
3. Bell 1937
4. Blachère 1947
5. Suyūṭī Itqān = Tanzil (**numerically identical to Egyptian 1924 in our instrument per [[h-new-222-more-chronologies|H-NEW-222]]** §3.2)
6. Ibn ʿAbbās (ʿAbd al-Kāfī)

Since Suyūṭī-Itqān ≡ Tanzil ≡ Egyptian numerically, the consensus family has effectively **5 numerically distinct chronologies** plus the Egyptian/Suyūṭī/Tanzil block weighted once. The pre-reg commits to two weighting schemes:

- **Weighting-A (de-duplicated)**: 5 distinct lists, each weighted 1.
  Inputs = {Nöldeke, Egyptian=Suyūṭī=Tanzil, Bell, Blachère, Ibn ʿAbbās}.
- **Weighting-B (raw-6)**: 6 lists including the duplicate, weight 1 each.
  Inputs = {Nöldeke, Egyptian, Suyūṭī, Tanzil, Bell, Blachère, Ibn ʿAbbās} — but Suyūṭī = Tanzil = Egyptian so effectively Egyptian tradition is triple-weighted.

Both are reported. **Primary decision uses Weighting-A** (de-duplicated; honest). Weighting-B is a secondary robustness check.

### Consensus algorithm

- **Borda-count primary**: For each surah s, compute the sum of its rank across all input chronologies (lower = earlier). Re-rank to get the consensus.
  - Rank 1 = earliest revelation in that chronology.
  - Consensus rank of s = rank of Σ_c rank_c(s) in ascending order; tie-break by mushaf-order ascending (inherited from [[h-new-212-alt-chronology-fisher-rao|h-new-212]] convention).
- **Kemeny-optimal secondary**: Minimize Σ_c Kendall-τ-distance(consensus, chronology_c). Kemeny over 114! is NP-hard; with only 5–6 inputs we use a local-search heuristic starting from the Borda solution and iteratively swapping adjacent pairs if they reduce total τ-distance. Report local optimum (acknowledge suboptimality honestly).

### Cells

- **Cell A** — Kendall τ(consensus, mushaf) vs max_c Kendall τ(c, mushaf) vs mean_c Kendall τ(c, mushaf). PASS iff τ(consensus) > max_c τ(c).
- **Cell B** — L_FR(consensus) on the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix vs {L_FR(c) : c ∈ inputs}. PASS iff L_FR(consensus) < min_c L_FR(c). Also compare to L_FR(mushaf) = 85.7597.
- **Cell C** — pairwise Kendall τ matrix across all 6 chronologies + mushaf + consensus. Descriptive only; confirm clustering.

### Bonferroni

- **k = 3** (Cells A, B, C), α_bon = 0.05/3 = 0.01667.
- Cell A uses a one-sided permutation null: randomly shuffle each chronology's ranks and recompute consensus + τ(consensus, mushaf); p = fraction of null τ ≥ observed τ. N = 10,000 perms, seed 20260419.
- Cell B uses a one-sided permutation null: the consensus's FR path length vs random permutation null from [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] (null mean 104.35, null SD 1.63). p_1sided_lower.
- Cell C is descriptive (no inferential p).

### MW-5 (negative control)

Shuffled-chronology input: for each input chronology, randomize ranks uniformly. Expected: consensus collapses toward random; τ(shuffled_consensus, mushaf) ≈ 0; L_FR(shuffled_consensus) ≈ null mean.

### Interpretation rules (frozen BEFORE execution)

- **If PASS both Cell A AND Cell B**: consensus > any individual chronology → supports **moderated-tawqīfī** (Ibn Taymiyya): mushaf emerges from chronological-plus-thematic consensus.
- **If PASS Cell A, FAIL Cell B** (or vice versa): split verdict; report honestly.
- **If FAIL both**: mushaf is EQUIDISTANT or FARTHER from all chronology combinations simultaneously → supports **uniquely-tawqīfī** (not a chronology blend).
- **If L_FR(consensus) > L_FR(mushaf)**: mushaf beats even the composite consensus on FR coherence — strong uniquely-tawqīfī signal regardless of Cell-A outcome.

## Garden-of-forking-paths log (choices committed BEFORE execution)

1. **Input family is 6 chronologies** — we do NOT add Wansbrough, Lüling, or revisionist schemes; they do not produce surah-rank lists.
2. **De-duplication rule**: Watt-Bell = Nöldeke (per [[h-new-222-more-chronologies|H-NEW-222]] §3.1, 114/114 match); Suyūṭī = Tanzil = Egyptian (per [[h-new-222-more-chronologies|H-NEW-222]] §3.2, identical numeric lists). Primary uses 5-distinct; Weighting-B reports 6-raw as robustness.
3. **Borda over Kemeny as primary**: Borda is tractable + interpretable; Kemeny is NP-hard, we use it only as heuristic check. If Kemeny disagrees with Borda on Cell A/B direction, report honestly.
4. **Tie-break in Borda**: mushaf-order ascending (inherited from [[h-new-212-alt-chronology-fisher-rao|h-new-212]] convention).
5. **Kendall τ variant**: standard (not τ-b or τ-c). No ties in any chronology rank vector, so τ-b collapses to τ.
6. **FR distance matrix**: inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]], same D matrix as [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]/222.
7. **Null type**: Cell A uses a **chronology-rank-shuffle null** (not the uniform-perm null), since the test is whether real-chronology-consensus beats random-chronology-consensus.
8. **10,000 perms**: matches [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]/222 precedent.
9. **Seed 20260419**: matches [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]/222 precedent.
10. **Interpretation rules pre-committed above** — no post-hoc drift.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-245.json`
- `findings/phase-b-hypotheses/h-new-245-chronology-consensus.md`
- `journal/h-new-245-run-1.md`
- `scripts/h_new_245_consensus_ordering.py`

## Pre-reg integrity

SHA-256 of this pre-reg file is computed and emitted to stderr by the script, and stored in the output JSON.
