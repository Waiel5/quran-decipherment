---
finding_id: H-NEW-6
title: Spectral clustering of 114-surah root-Jaccard graph recovers the classical 4-part mushaf partition beyond what length alone predicts; Fiedler split does NOT recover Meccan/Medinan; spectral gap is SMALLER than null (graph is more gradual than random)
date: 2026-04-12
rules_tuple:
  orthography: no-tashkeel
  word_definition: QAC STEM lemma (LEM) aggregated to ROOT sets per surah
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
null_model:
  primary: length-preserving root-set shuffle (within length quartiles), 500 draws
  secondary: random-weight-shuffle of upper triangle (degree-non-preserving), 1000 draws
acceptance_criterion: Bonferroni-corrected p < 0.005 for positive direction on ANY of 3 sub-claims
verdict: PARTIAL — sub-claim (b) CONFIRMED beyond length confound; sub-claim (a) REFUTED; sub-claim (c) REFUTED but directionally opposite (gap smaller, not larger).
---

## Claim

Build G = (V = 114 surahs, W = Jaccard(root_set_i, root_set_j)). Compute the normalized graph Laplacian spectrum.

(a) Fiedler (sign of 2nd eigenvector) should recover Meccan/Medinan (2-way).
(b) K-means on top-4 non-trivial eigenvectors should recover the classical 4-part partition (sabʿ ṭiwāl / miʾūn / mathānī / mufaṣṣal), beyond length confound.
(c) Observed spectral gap should exceed null (i.e. the Quran graph is MORE cleanly clustered than random).

## Method

1. Per surah, extract root set from QAC v0.4 root-index. 114 sets.
2. Build 114×114 weighted Jaccard adjacency matrix W. Normalized Laplacian L = I − D^{-1/2} W D^{-1/2}.
3. Compute eigen-decomposition. Report spectral gap λ_2 − λ_1.
4. Fiedler: sign pattern of v_2 → 2-way labels.
5. K-means-4 on eigvecs[:, 1:5].
6. Null: random upper-triangle weight shuffle (1000 draws, degree-non-preserving); length-quartile-preserving root-set shuffle (500 draws; stringent test for (b)).

## Results

### Spectral gap
| Statistic | Value |
|---|---|
| Observed gap λ_2 − λ_1 | 0.740 |
| Random-shuffle null mean | 0.868 ± 0.0036 |
| **z** | **−35.2** |
| Direction | gap is SMALLER than null |

**Interpretation**: the Quran's root-overlap graph is LESS cleanly clusterable than a random weight-shuffled graph. There is no dominant bottleneck; connectivity is gradual. This **refutes (c)** as stated but reveals a real structural property: the graph has continuous, not modular, community structure.

### Fiedler vs Meccan/Medinan
| Statistic | Value |
|---|---|
| Cluster A: 64 surahs (51 Meccan, 13 Medinan) | — |
| Cluster B: 50 surahs (35 Meccan, 15 Medinan) | — |
| Overall purity | 0.754 |
| ARI(Fiedler, M/M) | **0.015** |
| Null ARI | 0.0003 ± 0.010 |
| z | 1.46, p_ge = 0.075 |

**Interpretation**: Fiedler split does NOT recover Meccan/Medinan. The two clusters are ~75% Meccan each — essentially the majority class in both. **Refutes (a)**.

### K-means-4 vs classical sabʿ ṭiwāl / miʾūn / mathānī / mufaṣṣal

| Statistic | Value |
|---|---|
| ARI(spectral-4, classical) observed | **0.451** |
| ARI(length-quartile, classical) | 0.315 |
| ARI(spectral-4, length-quartile) | 0.357 |
| Length-preserving null mean ARI | 0.226 ± 0.053 |
| **z vs length-preserving null** | **+4.25** |
| p_ge | 0.0 (0/500 exceeded observed) |

**Interpretation**: spectral clustering recovers the classical partition at ARI = 0.45. Length alone accounts for ARI = 0.315 (length-quartile → classical). But the residual — specifically the 0.45 vs null-mean 0.226 — is statistically significant at z = 4.25. **Confirms (b)**: there is genuine root-topology information recovering the classical partition beyond length confound.

Corrected p under Bonferroni k=3: threshold 0.005/3 ≈ 0.0017. p_ge = 0 < 0.0017. **Survives correction.**

## Verdict: PARTIAL

- **(a) REFUTED**: Fiedler does not recover Meccan/Medinan. ARI ~0.015.
- **(b) CONFIRMED** (after length-confound control): spectral-4 recovers classical 4-partition at ARI 0.45, z=+4.25 under length-preserving null. Survives Bonferroni.
- **(c) REFUTED but with an interesting reverse signal**: spectral gap is SMALLER than null (z = −35). The Quran graph is more gradual/continuous in its connectivity than random — a property worth its own investigation.

## Substantive interpretation

The classical al-Dānī partition (ṭiwāl 2-9, miʾūn 10-35, mathānī 36-49, mufaṣṣal 50-114), traditionally explained as based on surah-length thresholds, appears to reflect **thematic-vocabulary clustering** in addition to length. Under length-preserving shuffles, the spectral clustering becomes MORE confused about boundaries: which surahs belong to which partition shifts. Under the *actual* root-binding, the spectral partition aligns better with the classical scheme.

This is consistent with al-Zarkashī's observation (*Burhān* 1:251) that the 4-part scheme was motivated by thematic as well as length considerations — legal/narrative content concentrates in ṭiwāl and miʾūn, while mufaṣṣal is dominated by eschatology and hymnic register.

However, the effect is **modest** beyond length (ARI 0.226 → 0.451 under real roots, z=4.25). Length alone explains ~70% of the partition recovery; root-topology explains ~30%. Not a revolutionary finding, but honest.

## Garden of forking paths disclosure

### Choices made after seeing the data
- Ran the length-preserving confound check AFTER seeing the raw ARI=0.45 was suspiciously correlated with length-quartile (0.315). This is the correct defensive analysis, not a rescue.

### Alternative rule tuples considered
- Word-level (tokens) instead of roots: not run; roots are more semantically stable.
- Weighted vs unweighted Jaccard graph: weighted used (thresholding at Jaccard>0 vs Jaccard>threshold would be a knob).
- Number of spectral dimensions: k=4 is classical-theory-motivated, not data-derived.

### Sibling hypotheses
- k=2 (Fiedler) vs M/M: tested, refuted.
- k=3, k=5: not tested. k=4 is the pre-committed value matching classical partition.

### Why this one and not those
- Committed to k=4 a priori because the classical partition IS 4-way. Testing k=5 would be post-hoc.

## Seed
`random.seed(20260413)`. Raw: `scratch/team-discovery/result-005.json`, `result-005-confound.json`.
