# [[h-new-162-beta-as-predictor|H-NEW-162]] — Per-surah β as predictor of period and muqaṭṭāʿat-status

**Finding ID**: [[h-new-162-beta-as-predictor|h-new-162]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent**: [[h-new-159-heap-beta-per-chapter|H-NEW-159]] (per-chapter β differs Quran vs Bukhārī; Quran more variable)
**Verdict**: **PASS for Meccan/Medinan prediction (strong); PASS for muq-status (weak)**

## Headline

**Per-surah Heap's β combined with mean-verse-length predicts Meccan vs Medinan at 75% LOOCV accuracy** (vs null 51% ± 8%, p = 0.001, ~3σ). β + verse-length are a genuine, learnable feature pair for period classification.

**Per-surah β predicts muqaṭṭāʿat-status at 62% LOOCV accuracy** (vs null 51% ± 9%, p = 0.037). Weak-but-significant at α=0.05 single-test ceiling.

## Numbers

### Class means

| Class | n | mean β | mean verse-length |
|---|---:|---:|---:|
| Meccan | 73 | 0.914 | 9.27 |
| Medinan | 27 | 0.878 | 18.63 |
| Muq-opened | 29 | 0.876 | 13.91 |
| Non-muq | 71 | 0.916 | 10.94 |

Meccan surahs have HIGHER β (more vocabulary growth) and SHORTER verses than Medinan. Muq surahs have LOWER β than non-muq surahs — muq surahs tend to be longer and more repetitive vocabulary.

### Nearest-centroid LOOCV

**Predict Meccan vs Medinan** (2-class):
- Accuracy: **0.750** (n=100)
- Null mean (1000 shuffles): 0.509 ± 0.080
- p_one-sided: **0.001**
- Effect size: 3σ above null

**Predict muq-opened vs non-muq** (2-class):
- Accuracy: **0.620** (n=100)
- Null mean: 0.510 ± 0.085
- p_one-sided: **0.037**
- Effect size: 1.3σ above null

## Interpretation

### Period prediction is non-trivial

75% accuracy with n=100 and a 2-feature simple-centroid model (β + mean-verse-length) is substantial. Meccan vs Medinan classification is a classical Quranic-studies question with many competing criteria (content, style, pronoun-use, etc.). This result says: **a 2-number summary of each surah's vocabulary-growth + prosody gives 75% Meccan/Medinan accuracy**.

The direction makes sense:
- Medinan surahs are longer (mean verse-length 19) — settled legal discourse.
- Meccan surahs are shorter (mean verse-length 9) — proclamatory / eschatological.
- Medinan surahs are more repetitive (β 0.878) — legal terminology cycles.
- Meccan surahs grow vocabulary faster (β 0.914) — more varied imagery/narrative.

### Muq prediction is weak

62% muq-vs-non-muq accuracy is only 1.3σ above null. Muq surahs do have distinct β profile (lower average) but it's not a strong classifier. This is consistent with [[h-new-96-predictor-extension|H-NEW-96]] (parent predictor findings NULL on detailed muq letter-set prediction).

### Practical implication

Per-surah β + verse-length could be used as:
1. Cross-checking chronology labels in ambiguous cases (where traditional criteria disagree)
2. Outlier detection (surahs whose β+vl profile does NOT fit their assigned period)
3. Feature engineering for more sophisticated predictors (H-NEW-96.2 or similar)

## Honest limits

1. **Nearest-centroid is a simple classifier**. A proper ML model (logistic regression, RF) might improve accuracy further. Compute budget limited.
2. **Short surahs excluded** (< 30 tokens). Selection bias toward longer surahs (mostly Meccan short-mufaṣṣal).
3. **Period labels are from Tanzil Egyptian Standard + Wikipedia Nöldeke reconstruction**. Not ground-truth; classification accuracy is bounded by label-quality.
4. **β is a single numerical summary**; multi-dimensional features (full Heap-curve slope + intercept, bigram stats, etc.) would richer.
5. **muq prediction at p=0.037 is single-test α=0.05**; would not survive Bonferroni-2 across the two classification tasks. Reporting as weak-descriptive.

## Connections

- **[[h-new-159-heap-beta-per-chapter|H-NEW-159]] (parent)**: per-chapter β distinguishes Quran from Bukhārī; distributions are genre-informative.
- **[[h-new-96-predictor-extension|H-NEW-96]] / H-NEW-96.2**: muq letter-set predictor context; β could be an additional feature.
- **[[h-new-125-chronology-content|H-NEW-125]]**: chronology-content axes; β + vl add a compact 2D summary.
- **M3 / [[cross-finding-014-five-principle-unified-equation|cross-finding-014]]**: β as an additional corpus-internal axis.

## Verdict

**PASS** on period prediction (75% LOOCV, p = 0.001; 3σ).
**WEAK-PASS** on muq-status prediction (62% LOOCV, p = 0.037; 1.3σ).

β + mean-verse-length are compactly informative features for surah classification. Per-surah β contains genuine corpus-internal signal beyond its corpus-level value ([[h-new-123-heap-law|H-NEW-123]]).
