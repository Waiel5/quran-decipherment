# H-NEW-245 — Run 1 journal

**Date**: 2026-04-17
**Specialist**: autonomous agent (H-NEW-245 lane)
**Seed**: 20260419
**Parent**: H-NEW-222 (additional chronologies Fisher-Rao)

## Hypothesis tested

If the mushaf reflects Ibn Taymiyya's moderated-tawqīfī (chronology + thematic
consensus), a cross-chronology CONSENSUS ordering should be CLOSER-TO-mushaf
(Kendall τ) and/or SHORTER on Fisher-Rao roots than any individual chronology.

## Inputs

5 de-duplicated chronologies (primary Weighting-A), reading H-NEW-222 §3.1–3.2:
- Nöldeke 1860 (= Watt-Bell 1970 numerically; 114/114 match)
- Egyptian Standard 1924 (= Tanzil = Suyūṭī-Itqān numerically; identical lists)
- Bell 1937 (Fr. Wikipedia; 1 imputation s15, 2 ties)
- Blachère 1947 (Fr. Wikipedia; 1 tie)
- Ibn ʿAbbās / ʿAbd al-Kāfī transmission

Raw 7-slot Weighting-B (Egyptian/Suyūṭī/Tanzil triple-counted) reported as
secondary.

## Method

- Borda-count consensus (primary).
- Kemeny local-search (3 sweeps, adjacent-swap, init from Borda; heuristic).
- Cell A: Kendall τ vs mushaf; chronology-rank-shuffle null (10K perms).
- Cell B: FR-roots path length; uniform-perm null (10K perms, reuses H-NEW-212 null).
- Cell C: pairwise Kendall τ matrix (descriptive).
- MW-5: shuffled-chronology-input negative control.

## Execution

Script: `scripts/h_new_245_consensus_ordering.py`
Pre-reg: `findings/phase-b-hypotheses/h-new-245-chronology-consensus-prereg.md`
Output: `findings/phase-b-hypotheses/csv/h-new-245.json`

Pre-reg SHA-256 embedded in script stderr and in output JSON.
H-NEW-111 D-matrix SHA-256 and H-NEW-222 chronology SHA-256 also embedded.

Runtime: ~7 minutes (dominated by 10,000-perm chronology-shuffle null for Cell A;
each perm recomputes a Borda consensus + O(N²) Kendall-τ computation).

Assertion checks passed (script ran to completion with no assertion errors):
- Suyūṭī == Tanzil (H-NEW-222 claim)
- Tanzil == Egyptian (H-NEW-222 §3.2 claim)

## Primary results

### Cell A — Kendall τ vs mushaf
- τ(Borda-A, mushaf) = **−0.3718**
- max_c τ = **−0.2451** at egyptian_1924
- Gap: −0.127 (consensus is 0.127 τ units MORE anti-correlated with mushaf)
- **FAIL** (consensus FARTHER from mushaf, not closer)
- Chronology-shuffle null: null τ mean = +0.004, SD = 0.063; z = −5.94
- p_twosided(|τ| ≥ null) = 0.0001 — real consensus is MORE anti-mushaf than random

### Cell B — Fisher-Rao path length
- L_consensus_borda_A = **90.2989**
- min_c L = **87.2321** (Nöldeke)
- L_mushaf = 85.7597
- **FAIL** vs best chronology (gap 3.07 FR units, 1.88 null-SDs)
- **FAIL** vs mushaf (gap 4.54 FR units, 2.79 null-SDs)
- Against uniform-perm null: z = −8.63, p_1sided_lower = 0.0001 (still beats random)

### Cell C — Pairwise τ (descriptive)
Two clusters confirmed:
- Cluster 1 (Western style-sorted): Nöldeke/Bell, internal τ = +0.875
- Cluster 2 (length/classical/French): Egyptian/Blachère/Ibn ʿAbbās,
  all pairwise τ ∈ [+0.93, +0.98]
- Inter-cluster τ ≈ +0.52–0.58
- Ibn ʿAbbās is NOT a Kendall-τ outlier — clusters tightly with Egyptian
  (τ = +0.978). H-NEW-222's "outlier" framing was Spearman-ρ-weighted by
  the al-Fātiḥa 1-position shift; under τ, Ibn ʿAbbās is a cluster-2 member.

### MW-5 negative control
- τ_shuffled_consensus = −0.0070 (expected ≈ 0) ✓
- L_shuffled_consensus = 105.36 (expected ≈ null mean 104.35, 0.62 SD away) ✓

## Interpretation

Per pre-registered rules:
- Cell A FAIL + Cell B FAIL → **uniquely-tawqīfī** supported.
- Cell A FAIL + Cell B FAIL (+ consensus LONGER than mushaf) → strong
  uniquely-tawqīfī signal.

The mushaf's ordering is NOT a weighted average of classical/modern
chronologies. Combining chronologies DILUTES coherence (L lengthens;
|τ| vs mushaf grows). This is consistent with cross-finding-021 §6 and
tightens the claim: the mushaf is not even a *linear combination* of
chronologies, let alone any single one.

## Deviations from pre-reg

None. Executed exactly as pre-registered.

## Honest limits

1. Only 5 de-duplicated chronologies; Weil/Muir/Nöldeke-Schwally-1909 not
   included. Extension would be H-NEW-245.1.
2. Kendall τ only; position-weighted τ or Ulam distance might read differently.
3. Kemeny is heuristic (local optimum, not global); 3 sweeps converged from
   dist 3588 → 3363. Global Kemeny unlikely to close the 0.127 τ gap.
4. One feature-set (FR-roots). char-4-gram and verse-length FR matrices
   not tested.
5. Theological vs mechanistic interpretation not discriminable from this test.

## Follow-up candidates

- **H-NEW-245.1**: Repeat consensus test on char-4-gram and verse-length
  D-matrices (H-NEW-111b/c); is the verdict feature-independent?
- **H-NEW-245.2**: Add Weil 1844, Muir 1858, Nöldeke-Schwally 1909 inputs.
- **H-NEW-245.3**: Test weighted-consensus with cluster-prior weights
  (e.g., weight Cluster 2 higher, or weight by scholarly-authority).
- **H-NEW-245.4**: Kemeny-exact via integer programming (gurobi/cbc)
  for definitive ordering.

## Files written

- `findings/phase-b-hypotheses/h-new-245-chronology-consensus-prereg.md`
- `findings/phase-b-hypotheses/h-new-245-chronology-consensus.md`
- `findings/phase-b-hypotheses/csv/h-new-245.json`
- `scripts/h_new_245_consensus_ordering.py`
- `journal/h-new-245-run-1.md` (this file)

## Verdict

**FAIL BOTH CELLS → uniquely-tawqīfī (not moderated-tawqīfī) EMPIRICALLY SUPPORTED.**
