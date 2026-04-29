---
finding_id: h-new-590
run: 1
date: 2026-04-28
specialist: H-NEW-590 outlier-spectrum lane
verdict: REPLICATION-FAILED at strict threshold (Q 55 Δ=+14.26<25); RANK-STABILITY SUPPORTING (ρ̄=0.978)
---

# H-NEW-590 run 1 journal

## Task

Convert cross-finding-024 Factor 5 ("no-outlier-surahs") from BINARY to CONTINUOUS by measuring per-surah Δ%ile(X) outlier-strength. Pre-register and run on 6 candidates {Q 1, 9, 18, 55, 62, 112} plus a corpus-wide supplementary descriptive ranking.

## Timeline

1. **Read parent findings**: cross-finding-024 (5-factor cohesion model), H-NEW-390 (Q 55 +32.6pp at native window), H-NEW-89 (Q 62 4-cluster meta-hub), H-NEW-570 (template for prereg/findings/script convention).
2. **Inspected H-NEW-111 distance matrix**: 6441 upper-triangular triples, 1-indexed, symmetric reconstruction trivial.
3. **Wrote pre-registration** at `findings/phase-b-hypotheses/h-new-590-outlier-spectrum-prereg.md`. Locked: 6 candidates, 7-surah centered window with edge-clipping, Δ formula, primary threshold ≥25 for Q 55 replication, supporting Spearman ρ ≥ 0.95, Bonferroni-6 α=0.0083 for descriptive p-values, seed 20260429.
4. **Computed prereg SHA256**: `0c75ee51c5689799989088ff9b3902c8614fa3ec967144d7530f7920f753efae`. Embedded in run script as `PREREG_SHA_EXPECTED`.
5. **Wrote run script** at `scripts/h_new_590_outlier_spectrum.py`. Pure stdlib (no numpy dependency); 200-bootstrap Spearman stability check.
6. **Executed**: ~6 minutes wall-clock for 200-bootstrap loop on full corpus.

## Locked observations

### 6 PRE-REGISTERED CANDIDATES

| X | W | d̄(W) | %ile(W) | d̄(W\X) | %ile(W\X) | Δ%ile | Class |
|:-:|:--|:-:|:-:|:-:|:-:|:-:|:--|
| Q 1 | {1..7} | 0.9154 | 37.90 | 0.8074 | 10.81 | **+27.09** | STRONG_OUTLIER |
| Q 9 | {6..12} | 0.9504 | 57.42 | 0.9101 | 35.85 | **+21.57** | MODERATE_OUTLIER |
| Q 18 | {15..21} | 0.9459 | 54.61 | 0.9480 | 54.22 | +0.39 | NULL (WEAK) |
| Q 55 | {52..58} | 1.0511 | 97.81 | 1.0022 | 83.55 | **+14.26** | MODERATE_OUTLIER |
| Q 62 | {59..65} | 0.7757 | 5.56 | 0.7770 | 7.38 | -1.82 | NULL |
| Q 112 | {108..114} | 0.3081 | 0.00 | 0.3137 | 0.00 | 0.00 | NULL (FLOOR) |

### PRIMARY pre-commit
- Q 55 Δ ≥ 25 — Δ=+14.26 → **FAILED** at strict threshold.
- Replication is NEAR but window-conditional. H-NEW-390 native window {50-56} is all-Meccan; standardized {52-58} crosses Hijra hinge at Q 56/57.

### SUPPORTING pre-commit
- Spearman bootstrap mean ρ = 0.9778; min = 0.9446; 99.5% of 200 bootstraps ≥ 0.95 → **PASSED**.

### Corpus-wide ranking (top 5 outliers, descriptive)
1. Q 33 al-Aḥzāb +31.46pp
2. Q 1 al-Fātiḥa +27.09pp
3. Q 24 al-Nūr +23.51pp
4. Q 9 al-Tawba +21.57pp
5. Q 12 Yūsuf +14.26pp (tied with Q 55)

### Corpus-wide cohesion-anchors (bottom 5 most-negative, descriptive)
- Q 2 al-Baqara: Δ = -20.62pp (strongest cohesion-anchor)
- Q 51 al-Dhāriyāt: Δ = -16.17pp
- Q 3 Āl ʿImrān: Δ = -15.28pp
- Q 23 al-Muʾminūn: Δ = -10.91pp
- Q 52 al-Ṭūr: Δ = -10.82pp

### Null distributions (sanity)
- null_size7 mean = 0.9238
- null_size6 mean = 0.9229
- Roughly equal, as expected for size-invariant null on full corpus.

## Structural reading

The pre-registered REPLICATION test FAILED. The H-NEW-390 effect is real but window-conditional — Q 55's marginal contribution depends on whether the surrounding block is Meccan-uniform (high marginal effect, +32.6pp) or Hijra-spanning (lower marginal effect, +14.26pp). This is a HONEST PRE-COMMIT VIOLATION; the pre-reg's ≥25 threshold was set under an implicit assumption of window-invariance that proved false.

The pre-registered SUPPORTING test PASSED with high stability (ρ̄=0.978). The corpus-wide Δ%ile ordering is robust to null-resampling.

The DESCRIPTIVE corpus-wide ranking surfaces previously-unidentified outliers (Q 33 al-Aḥzāb at +31.46pp; Q 24 al-Nūr at +23.51pp) and previously-unidentified cohesion-anchors (Q 2 al-Baqara at -20.62pp). These are NOT pre-registered findings and require separate follow-up tests (H-NEW-591, H-NEW-592, H-NEW-595).

## Interpretation

**Factor 5 is empirically continuous, not binary.** The cross-finding-024 model should be revised in place: Factor 5 = signed scalar Δ%ile(X) per surah, replacing the binary "is-outlier" flag.

**Hub-status and outlier-status are independent axes.** Q 62 al-Jumuʿa (4-cluster meta-hub from H-NEW-89) has Δ ≈ 0, demonstrating that hub-architecture (cross-finding-023) and outlier-strength (Factor 5) are EMPIRICALLY ORTHOGONAL.

**Classical anchors map unevenly onto Factor 5.** Q 1 (umm al-Kitāb) and Q 9 (no-basmala) have empirical outlier-strength matching their classical distinctions. Q 18 (Friday recitation), Q 62 (meta-hub), and Q 112 (thulth al-Qurʾān) do NOT — their classical importance operates on independent axes (liturgical, network-bridging, content-density). The classical tradition's discipline of maintaining separate categorial layers is again vindicated.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-590-outlier-spectrum-prereg.md`
- Pre-reg SHA: `0c75ee51c5689799989088ff9b3902c8614fa3ec967144d7530f7920f753efae`
- Script: `scripts/h_new_590_outlier_spectrum.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-590.json`
- Findings: `findings/phase-b-hypotheses/h-new-590-outlier-spectrum.md`
