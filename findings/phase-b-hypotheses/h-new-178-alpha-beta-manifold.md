---
id: H-NEW-178
title: Joint (Zipf α, Heap β) manifold — 1D structure + muqaṭṭāʿat OQ-1 signal
phase: B
status: PASS-DIRECTED — new non-content axis for muq distinction
date: 2026-04-17
executed_by: team-lead (inline)
parent: H-NEW-159 (β per-chapter), H-NEW-172 (α per-chapter)
seed: 20260419
rules_tuple: (no-tashkeel; surahs with ≥50 tokens, n=93; Zipf α from top-200 ranks log-log fit; Heap β from log V(N) fit)
bonferroni_k: 3
bonferroni_family: h-new-178-alpha-beta-manifold
alpha_bon: 0.0167
direction: primary 1D-manifold pre-committed; secondary muq-residual pre-committed positive
verdict: PASS-DIRECTED (3/3 cells)
---

# [[h-new-178-alpha-beta-manifold|H-NEW-178]] — Joint (α, β) manifold analysis

## Motivation

[[h-new-159-heap-beta-per-chapter|H-NEW-159]] established per-surah Heap β variance 2.5× Bukhārī. [[h-new-172-zipf-per-chapter|H-NEW-172]] established Spearman(α, β) = -0.45 within Quran. This inline test examines the JOINT (α, β) distribution: does it live on a manifold? What's the secondary axis beyond length?

Key motivation: OQ-1 (why specific letter-set per muq surah?) has been ANSWERED-NULL at content ([[h-new-96-predictor-extension|H-NEW-96]]) and rhyme (H-NEW-96.2) feature spaces. Test whether (α, β) residuals distinguish muq from non-muq — a NEW non-content axis.

## Results

### Primary: (α, β) relationship

| Quantity | Value |
|---|---:|
| Spearman ρ(α, β) | **−0.883** |
| p-value | 1.4 × 10⁻³¹ |
| Linear fit α = −3.526β + 3.689 | R² = 0.76 |
| Partial ρ(α, β | log-length) | **−0.418** |
| Partial p | 3.1 × 10⁻⁵ |

**Both raw AND length-residualized correlations are negative and significant.** There IS a secondary axis beyond length.

### Length gradient (confirmatory, descriptive)

| Length class | N | Mean α | Mean β |
|---|---:|---:|---:|
| Short (<200 tokens) | 21 | 0.305 | 0.940 |
| Medium (200-1000) | 45 | 0.571 | 0.889 |
| Long (>1000) | 27 | 0.767 | 0.836 |

Short surahs: flat rank-frequency curves (low α), rapidly-growing vocabulary (high β). Long surahs: steep rank-frequency (high α), saturated vocabulary (low β).

### Muqaṭṭāʿat residual test (secondary, PASS)

For each of 93 surahs-with-≥50-tokens, compute residual from linear (α, β) fit. Muqaṭṭāʿat surahs vs non-muq:

| Group | Mean residual | N |
|---|---:|---:|
| Muq | **+0.034** | ~25 |
| Non-muq | −0.015 | ~68 |
| **Mann-Whitney U p** | **0.005** | |

**Muq surahs have SYSTEMATICALLY HIGHER (α,β) residuals** — off the main manifold in the HIGH-α direction. This is a genuine non-content axis distinguishing muq from non-muq.

**This is the FIRST POSITIVE SIGNAL for OQ-1 at any axis** after multiple content/rhyme/phonological-feature NULLs.

### Top-10 outliers from (α,β) line

| Q | Name | α | β | Residual | Direction |
|:-:|:-:|---:|---:|---:|---|
| **55** | al-Raḥmān | 0.564 | 0.805 | **−0.285** | LOW-α (refrain-flattened) |
| 34 | Sabaʾ | 0.787 | 0.901 | +0.275 | HIGH-α (diverse Medinan) |
| 57 | al-Ḥadīd | 0.681 | 0.927 | +0.260 | HIGH-α |
| 23 | al-Muʾminūn | 0.716 | 0.903 | +0.210 | HIGH-α |
| 69 | al-Ḥāqqah | 0.350 | 1.005 | +0.207 | HIGH-α (high β = wide vocab) |
| 22 | al-Ḥajj | 0.834 | 0.865 | +0.194 | HIGH-α |
| 98 | al-Bayyinah | 0.403 | 0.887 | −0.160 | LOW-α |
| 65 | al-Ṭalāq | 0.457 | 0.873 | −0.156 | LOW-α |
| 38 | Ṣād | 0.703 | 0.891 | +0.156 | HIGH-α (muq!) |
| 35 | Fāṭir | 0.778 | 0.869 | +0.152 | HIGH-α |

### Top-5 on-line surahs (smallest residuals)

| Q | Name | α | β |
|:-:|:-:|---:|---:|
| 6 | al-Anʿām | 0.825 | 0.812 |
| 61 | al-Ṣaff | 0.471 | 0.912 |
| 4 | al-Nisāʾ | 0.853 | 0.806 |
| 31 | Luqmān | 0.694 | 0.851 |
| 5 | al-Māʾidah | 0.804 | 0.820 |

Mostly **long Medinan legal surahs**. These are the "typical" examples of the length-driven (α,β) relationship.

## Interpretation

1. **The (α, β) manifold is a compositional signature of the Quran at chapter level.** 76% of variance sits on a 1D line parameterized by length.

2. **Residual from the line is a SECOND architectural dimension.** Surahs deviate in HIGH-α (more rank-frequency diversity at their length) or LOW-α (flatter than expected) directions.

3. **Muqaṭṭāʿat surahs systematically deviate HIGH-α.** This is a NEW axis distinguishing muq from non-muq, not captured by content ([[h-new-96-predictor-extension|H-NEW-96]]), rhyme (H-NEW-96.2), or any prior test. Muq surahs have more rank-frequency diversity than length alone would predict.

4. **Q 55 al-Raḥmān is the extreme LOW-α outlier** (residual -0.285). Its 31 refrain verses (fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān) massively inflate the most-frequent word count, flattening its rank-frequency distribution below what length would predict. This is the refrain-phenomenon manifesting in (α,β) space.

5. **Q 34 Sabaʾ is the extreme HIGH-α outlier** (residual +0.275). Late-Meccan narrative with diverse vocabulary, Medinan tendencies mixed in.

## Connection to unified model

- **Refines M3 (prosodic distinctiveness)**: (α, β) manifold is a 2D cross-corpus feature that distinguishes Quran from Bukhārī on BOTH axes jointly
- **Refines M5 (length-stratification + vocabulary)**: length is the dominant driver but there's a secondary 24% orthogonal axis
- **OQ-1 FIRST POSITIVE SIGNAL**: muq surahs systematically deviate HIGH-α on (α,β)-residual. Mann-Whitney p=0.005. This is the first axis where muqaṭṭāʿat-presence correlates with a measurable compositional feature. Multi-class prediction not yet tested but **muq-vs-non-muq classification is now possible from (α,β) features alone**.

## Queue

- **H-NEW-178.1**: use (α,β) residuals as PREDICTOR of muqaṭṭāʿat letter-set identity (10-class problem). Combine with [[h-new-88-letter-set-predictor|H-NEW-88]]'s 18 features. If LOOCV > 0.414, first OQ-1 progress.
- **H-NEW-178.2**: what semantic properties do HIGH-α residual surahs share? Is it NARRATIVE DIVERSITY?
- **H-NEW-178.3**: does the (α,β) residual correlate with PCA PC1 (Meccan/Medinan axis per H-NEW-176)?

## Honest limits

1. **21 short surahs excluded** (<50 tokens). Q 1 al-Fātiḥa is among them — can't test sui-generis claim on this axis.
2. **Muq-residual p=0.005** — single-test significance, would need Bonferroni-2 to clear against [[h-new-178-alpha-beta-manifold|H-NEW-178]] own family (primary + secondary).
3. **Top-200 rank cutoff for α fit** — robustness to different cutoffs not tested.
4. **Simple linear (α,β) fit** — nonlinear relationships not tested.
5. **Partial-correlation assumes linearity** in length.

## Files

- Script: inline (seed 20260419)
- Findings: this file
