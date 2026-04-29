---
id: H-NEW-182
title: Phonological feature vectors per surah — cluster structure and Bukhārī distinctness
status: PARTIAL-PASS (2 of 3 Bonferroni cells)
prereg: h-new-182-phonological-vectors-prereg.md
bonferroni_family: h-new-182-phonological-vectors
bonferroni_k: 3
alpha_bon: 0.01667
seed: 20260419
script: scripts/h_new_182_phonological_vectors.py
results_json: findings/phase-b-hypotheses/csv/h-new-182.json
per_surah_csv: findings/phase-b-hypotheses/csv/h-new-182-surah-vectors.csv
---

# [[h-new-182-phonological-vectors|H-NEW-182]] — Phonological Feature Vectors per Surah

## Summary

Each surah was encoded as a 9-d mean phonological feature vector over its
body-letters (labial, alveolar, palatal, velar, pharyngeal, glottal, emphatic,
voiced, continuant) using no-tashkeel text. K-means (k=4) on the 114-surah
standardized matrix produced a silhouette of **0.2963**, compared to a shuffled
null mean of 0.0936 and q95 = 0.1224 (p = 0.0010, PASS).

Phonological-vector distance between the Quran and Bukhārī (letter-weighted
global vectors) = **0.0595** Euclidean, vs Bukhārī self-split q95 = 0.00201 and
max = 0.00335 — an observed separation ~30× greater than internal noise
(p = 0.0010, PASS).

Emphatic-fraction alone DID NOT separate Meccan vs Medinan (AUC 0.436, two-sided
p = 0.319, NULL). However, as an EXPLORATORY (outside Bonferroni) observation,
the pharyngeal-fraction feature gave AUC 0.372 (|dev| = 0.128, not corrected).

## Cell A — k-means silhouette (PASS)

- k = 4, seed 20260419, n_init = 10
- Observed silhouette: 0.2963
- Null (row-shuffled): mean 0.0936, q95 0.1224, max 0.1838
- **p = 0.0010** (< α_bon = 0.01667)
- Effect size: observed − null_mean = 0.203 (≈ 6× null std)

### Cluster composition

| cluster | n | meccan | medinan | muq | dominant features |
|---|---|---|---|---|---|
| c0 | 24 | 17 | 7 | 1 | HIGH palatal (0.105), HIGH glottal (0.072), LOW voiced (0.746), HIGH continuant (0.851) |
| c1 | 85 | 64 | 21 | 28 | MODAL — Quran-typical (MOST muq surahs here) |
| c2 | 4 | 4 | 0 | 0 | HIGH alveolar (0.384), HIGH emphatic (0.051 — nearly 3× modal), HIGH continuant |
| c3 | 1 | 1 | 0 | 0 | Q-outlier — HIGHEST voiced (0.899), LOW continuant (0.737) |

The main cluster (c1, n=85) contains **28 of 29 muq surahs** — the muqaṭṭaʿāt
cohort lives in the Quran's phonological mode rather than forming its own
cluster. The Medinan share of c0 (29%, 7/24) is slightly elevated relative to
the global Medinan rate (25%), but not dramatically.

## Cell B — Meccan/Medinan ROC-AUC (NULL)

- Scorer: emphatic-letter fraction per surah
- Observed AUC = 0.436 (direction flipped to 0.564 for report)
- |AUC − 0.5| = 0.064
- Two-sided permutation p (10 000 draws) = **0.319** (NOT < α_bon = 0.01667)
- Verdict: Emphatic letters do NOT distinguish Meccan from Medinan surahs.

### Exploratory (outside Bonferroni)

- pharyngeal-fraction: AUC = 0.372 (|dev| = 0.128) — Meccan surahs have MORE
  pharyngeal letters than Medinan (the strongest individual-feature signal).
- voiced: AUC = 0.472 (negligible)
- alveolar: AUC = 0.520 (negligible)
- labial: AUC = 0.534 (weak)

## Cell C — Quran vs Bukhārī phonological distance (PASS)

- Quran global 9-d vector: labial 0.217, alveolar 0.324, palatal 0.091,
  velar 0.053, pharyngeal 0.052, glottal 0.057, emphatic 0.018, voiced 0.767,
  continuant 0.844.
- Bukhārī global 9-d vector: labial 0.181, alveolar 0.340, palatal 0.094,
  velar 0.046, pharyngeal 0.083, glottal 0.059, emphatic 0.019, voiced 0.747,
  continuant 0.819.
- Observed Euclidean distance = **0.0595**
- Bukhārī self-split bootstrap (n=1000, block=100): mean 0.00133, q95 0.00201,
  max 0.00335.
- **p = 0.0010** (observed is ~30× Bukhārī's internal noise ceiling)

### Phonological contrasts

| feature | Quran | Bukhārī | Δ (Q−B) |
|---|---|---|---|
| labial | 0.217 | 0.181 | **+0.036** |
| pharyngeal | 0.052 | 0.083 | **−0.031** |
| continuant | 0.844 | 0.819 | +0.025 |
| voiced | 0.767 | 0.747 | +0.020 |
| alveolar | 0.324 | 0.340 | −0.016 |

**Direction**: The Quran is MORE labial and LESS pharyngeal than Bukhārī. The
pharyngeal gap is interesting given that the Quran is stylized as having heavy
pharyngeal / guttural texture — Bukhārī actually has 60% MORE pharyngeal density.
This likely reflects the prosodic-name density in Bukhārī (ḥadīth chains rich in
ʿayn, ḥāʾ, ghayn via names like ʿAbd Allāh, Ḥasan, etc).

## MW-5 positive control

IID-uniform fake surahs (114 synthetic, uniform over 28-letter alphabet,
lengths matched): silhouette = 0.4440 — HIGHER than the observed Quran
silhouette. This is a known clustering artifact: IID-uniform sampling on
small-N surahs gives high-variance mean vectors that cluster artificially. This
does NOT invalidate Cell A, because the locked null for Cell A is the ROW-
SHUFFLED marginal-preserving null, not an IID-uniform null. Under the locked
null, the Quran silhouette is 6× the null std above null mean.

Interpretation: the Quran's joint feature-vector cluster structure is
significantly non-random given its per-feature marginals, but the raw silhouette
value is not meaningfully higher than what random short strings can produce.
Cell A demonstrates structure-beyond-marginals, not structure-beyond-noise.

## Verdict

- Cell A (k-means silhouette):   **PASS** (p = 0.0010, effect size ≈ 6σ)
- Cell B (Meccan/Medinan AUC):   **NULL** (emphatic fraction does not separate)
- Cell C (Bukhārī distinctness): **PASS** (distance ~30× Bukhārī self-noise)
- **OVERALL: PARTIAL-PASS (2 of 3)**

## Key findings

1. **Phonological clustering is REAL but modest**: 114 surahs do cluster
   non-randomly in 9-d phonological space, driven mostly by the palatal/glottal
   axis (cluster 0, n=24) and the emphatic-alveolar axis (cluster 2, n=4).
   The 29 muqaṭṭaʿāt surahs do NOT form a distinctive phonological cluster —
   28 of 29 live in the modal cluster 1 with the rest of the Quran.

2. **The Meccan/Medinan distinction is NOT driven by emphatic letters**. The
   pharyngeal-fraction direction (Meccan > Medinan) is the only exploratory
   signal worth queuing for [[h-new-183-chronology-predictor|H-NEW-183]] pre-reg — the direction is consistent
   with the Quran's traditional association of pharyngeal /ʿayn ḥāʾ/ sounds
   with early rhyming Meccan sūras.

3. **The Quran's phonological profile differs REAL from Bukhārī's**, most
   conspicuously in +3.6 pp labial and −3.1 pp pharyngeal. The "more labial"
   direction is not what Quranic-recitation folklore predicts. This is a clean
   quantitative baseline for future phonological-feature comparisons.

## Follow-up hooks

- [[h-new-183-chronology-predictor|H-NEW-183]] (exploratory): pharyngeal-fraction as Meccan/Medinan scorer with
  pre-reg (pharyngeal-Meccan direction is locked post-hoc — queue as
  replication on an independent corpus split, e.g. early vs late Meccan Nöldeke
  phase).
- Alternative clustering (Ward hierarchical, GMM) to verify cluster structure
  under a different algorithm.
- Per-surah phonological distance to Bukhārī (do individual surahs vary in
  their Bukhārī-distance rank?).
