---
id: H-NEW-590
title: "Outlier-strength spectrum — convert cross-finding-024 Factor 5 from binary to continuous via per-surah Δ%ile"
phase: B
status: PRE-REGISTERED 2026-04-28
date: 2026-04-28
agent: specialist (H-NEW-590 outlier-spectrum lane)
parent_1: cross-finding-024 (5-factor cohesion model — Factor 5 NO-OUTLIER-SURAHS, currently BINARY)
parent_2: H-NEW-390 (Q 55 al-Raḥmān = +32.6pp disruption in Meccan-musabbiḥāt block Q 50-56)
parent_3: H-NEW-89 (Q 62 al-Jumuʿa as 4-cluster meta-hub)
parent_4: H-NEW-111 (mushaf Fisher-Rao distance matrix)
seed: 20260429
bonferroni_k: 6
bonferroni_family: h-new-590-outlier-spectrum
alpha_bon: 0.0083
rules_tuple: "(FR from H-NEW-111 D_matrix_upper_triangular keyed by 1-indexed surah pairs; for each X ∈ {1, 9, 18, 55, 62, 112}, define 7-surah window W = [max(1,X-3) … min(114,X+3)] clipped at corpus edges with Q1 → {1..7} and Q112 → {108..114}; d̄(W) = mean of C(|W|,2) pairwise FR distances; d̄(W\\X) = same after removing X; null-7 = 10000 random size-|W| subsets of {1..114}; null-6 = 10000 random size-|W|-1 subsets; %ile = fraction of nulls with d̄ ≤ observed; Δ%ile(X) = %ile(W) − %ile(W\\X); seed 20260429 fixed; supplementary corpus-wide rank computes Δ for all 114 surahs descriptively. k=6 Bonferroni α_bon=0.05/6=0.0083)"
direction: |
  POSITIVE Δ%ile = X is an outlier-disruptor (block more dispersed WITH X than WITHOUT X).
  NEGATIVE Δ%ile = X is a cohesion-anchor (block less dispersed WITH X than WITHOUT X).
  
  Pre-registered direction is POSITIVE for outlier-strength (larger Δ = stronger outlier).
  
  PRIMARY pass-criterion (replication of H-NEW-390):
    Q 55 Δ%ile ≥ 25 ⇒ REPLICATION CONFIRMED.
  
  SUPPORTING pass-criterion (corpus-wide stability):
    Spearman rank correlation of full Δ-vector under bootstrap (10000 random null-redraws with new sub-seeds derived from base seed) ≥ 0.95 ⇒ rank-stability SUPPORTING.
  
  Per-candidate descriptive verdicts (NOT gated):
    STRONG OUTLIER: Δ ≥ 25
    MODERATE OUTLIER: 10 ≤ Δ < 25
    WEAK OUTLIER: 0 < Δ < 10
    NULL / non-outlier: Δ ≈ 0 (|Δ| < 5)
    COHESION ANCHOR: Δ ≤ -10 (X stabilizes its block)
  
  Bonferroni-6 α_bon=0.0083 applies to per-candidate p-value tests if any inferential claim is made. The PRIMARY test (Q 55 Δ ≥ 25) is a magnitude test, not a p-value test, so Bonferroni applies as a sanity α for descriptive p-values reported alongside.
verdict: PENDING
---

# [[h-new-590-outlier-spectrum|H-NEW-590]] — Outlier-strength spectrum

## 1. Question

**[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]** locks 5 factors of content-cohesion. Factor 5 ("no-outlier-surahs") is currently treated as BINARY: a surah is either an outlier (e.g. Q 55) or not. **[[h-new-390-q55-outlier-exclusion|H-NEW-390]]** quantified Q 55's effect at +32.6pp in the Meccan-musabbiḥāt block Q 50-56.

**The natural next move**: convert Factor 5 from binary to a CONTINUOUS spectrum by measuring per-surah outlier-strength via a unified Δ%ile statistic. This generalizes the Q 55 measurement to every surah and produces a corpus-wide outlier-strength ranking.

## 2. Locked candidate set (N=6)

| X | Name | Classical anchor |
|:-:|:--|:--|
| Q 1 | al-Fātiḥa | umm al-Kitāb (al-Bukhārī ḥadīth #756 *fātiḥat al-kitāb*) |
| Q 9 | al-Tawba / Barāʾa | unique no-basmala surah (al-Suyūṭī *al-Itqān* nawʿ 23) |
| Q 18 | al-Kahf | Friday-recitation merit (Muslim ḥadīth; al-Nawawī) |
| Q 55 | al-Raḥmān | ʿarūs al-Qurʾān (al-Tirmidhī #3291) — [[h-new-390-q55-outlier-exclusion|H-NEW-390]] +32.6pp |
| Q 62 | al-Jumuʿa | [[h-new-89-meta-cluster-network|H-NEW-89]] 4-cluster meta-hub |
| Q 112 | al-Ikhlāṣ | thulth al-Qurʾān (al-Bukhārī ḥadīth #5013) |

Set is LOCKED. No additions or substitutions post-hoc.

## 3. Window construction (locked)

For each X, the centered 7-surah window W is:

- W(X) = {X-3, X-2, X-1, X, X+1, X+2, X+3} clipped to [1..114]
- Q 1: W = {1, 2, 3, 4, 5, 6, 7} (left-edge)
- Q 9: W = {6, 7, 8, 9, 10, 11, 12}
- Q 18: W = {15, 16, 17, 18, 19, 20, 21}
- Q 55: W = {52, 53, 54, 55, 56, 57, 58}
- Q 62: W = {59, 60, 61, 62, 63, 64, 65}
- Q 112: W = {108, 109, 110, 111, 112, 113, 114} (right-edge)

NB: the Q 55 window here {52..58} is NEAR but not identical to the [[h-new-390-q55-outlier-exclusion|H-NEW-390]] Meccan-musabbiḥāt block {50..56}. The [[h-new-590-outlier-spectrum|H-NEW-590]] windowing is STANDARDIZED (centered on X) for cross-candidate comparability. The Q 55 result is therefore a NEAR-replication, not an exact replication, of [[h-new-390-q55-outlier-exclusion|H-NEW-390]] — magnitudes are expected to be similar but not identical.

## 4. Statistic (locked)

For each candidate X:

```
d̄(W)        = mean of C(|W|,2) pairwise FR distances on W
d̄(W\X)      = mean of C(|W|-1,2) pairwise FR distances on W minus X
%ile(W)     = fraction of 10000 random size-|W| subsets s ⊂ {1..114} with d̄(s) ≤ d̄(W)
%ile(W\X)   = fraction of 10000 random size-|W|-1 subsets s ⊂ {1..114} with d̄(s) ≤ d̄(W\X)
Δ%ile(X)    = %ile(W) − %ile(W\X)
```

Both null distributions are drawn independently. Seed = 20260429. The same null draws are reused across candidates (i.e. the 10000 random size-7 subsets computed once, the 10000 random size-6 subsets computed once) so that all candidate %iles are computed against a single shared null per cardinality.

Δ%ile is reported in PERCENTAGE POINTS (0-100 scale).

## 5. Pre-committed thresholds

| Test | Predicted | Gate |
|:--|:-:|:--|
| Q 55 Δ%ile | ≥ 25 | REPLICATION of [[h-new-390-q55-outlier-exclusion|H-NEW-390]] |
| Other 5 candidates | UNCOMMITTED magnitude | descriptive only |
| Corpus-wide Spearman bootstrap | ≥ 0.95 | SUPPORTING rank-stability |
| Bonferroni-6 α | 0.0083 | applied to per-candidate descriptive p-values |

**Aggregate H1**: Q 55 Δ ≥ 25 (REPLICATION) AND Spearman bootstrap rank-correlation ≥ 0.95 (SUPPORTING).

**Aggregate NULL**: Q 55 Δ < 25 (replication failure — would falsify [[h-new-390-q55-outlier-exclusion|H-NEW-390]]-style outlier-effect at standardized window).

## 6. Corpus-wide supplementary

After the 6-candidate test, compute Δ%ile(X) for ALL 114 surahs using the same windowing rule (with edge-clipping). Report:

- top-10 strongest outliers (largest positive Δ)
- bottom-10 strongest cohesion-anchors (most negative Δ, if any)
- Spearman bootstrap stability of the full 114-vector

This is DESCRIPTIVE only. No new inferential claims.

## 7. Direction-locking

- POSITIVE Δ = outlier-disruptor.
- NEGATIVE Δ = cohesion-anchor.
- Pre-registered direction is POSITIVE for outlier-strength.
- Direction is locked BEFORE viewing results.

## 8. Honest limits

1. **FR-roots only** — outlier-status at char-4-gram or verse-len untested here.
2. **Window size 7 is a choice** — alternative widths (5, 9, 11) untested.
3. **Edge-clipping for Q 1 and Q 112** — left/right windows are not centered, biases unknown.
4. **The Q 55 measurement is NEAR-replication of [[h-new-390-q55-outlier-exclusion|H-NEW-390]]**, not exact (window {52..58} vs [[h-new-390-q55-outlier-exclusion|H-NEW-390]] {50..56}).
5. **Bonferroni-6** treats the 6 candidates as equally-pre-committed; corpus-wide ranking does NOT use Bonferroni since it is descriptive-supplementary.
6. **N=10000 nulls** gives ~1pp resolution on percentile.
7. **The classical anchor for Q 62 ([[h-new-89-meta-cluster-network|H-NEW-89]] 4-cluster meta-hub) does not predict outlier-disruption**; Q 62 is included to test whether meta-hub status correlates with outlier-strength.
8. **Q 9's no-basmala uniqueness is morphological**, not necessarily content-disruptive — empirical question.

## 9. Classical-scholarship anchor (per candidate)

- **Q 1 al-Fātiḥa**: al-Bukhārī #756 *fātiḥat al-kitāb*; umm al-Kitāb. Recited in every ṣalāh. If structurally distinct, classical centrality predicts EITHER strong outlier (unique liturgical role) OR cohesion-anchor (synthesizing the corpus).
- **Q 9 al-Tawba / Barāʾa**: al-Suyūṭī *al-Itqān* nawʿ 23 — unique surah without basmala opener. Ibn ʿAbbās tradition: continuous with Q 8 al-Anfāl. Outlier-status predicted by no-basmala uniqueness; could go either way empirically.
- **Q 18 al-Kahf**: Muslim ḥadīth #809 (Friday-recitation merit); al-Nawawī *al-Adhkār*. Four-narrative structure (Sleepers, Garden, Mūsā/al-Khiḍr, Dhū al-Qarnayn) — narrative-register surah. Outlier prediction unclear.
- **Q 55 al-Raḥmān**: al-Tirmidhī #3291 *ʿarūs al-Qurʾān* "Bride of the Quran" — classical uniqueness designation. [[h-new-390-q55-outlier-exclusion|H-NEW-390]] +32.6pp. Pre-registered Δ ≥ 25 prediction.
- **Q 62 al-Jumuʿa**: [[h-new-89-meta-cluster-network|H-NEW-89]] 4-cluster meta-hub status; classically grouped with musabbiḥāt openers (sabbaḥa). Hub ≠ outlier; meta-hub status could predict either positive or negative Δ.
- **Q 112 al-Ikhlāṣ**: al-Bukhārī #5013 *thulth al-Qurʾān* "one-third of the Quran" — classical uniqueness designation. Compact creedal surah. Outlier candidate.

## 10. Deliverables

- Pre-reg this file (locked 2026-04-28).
- SHA256 hash embedded in run script.
- Run script: `scripts/h_new_590_outlier_spectrum.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-590.json`
- Findings markdown: `findings/phase-b-hypotheses/h-new-590-outlier-spectrum.md`
- Journal entry: `journal/h-new-590-run-1.md`

Pre-reg locked 2026-04-28.
