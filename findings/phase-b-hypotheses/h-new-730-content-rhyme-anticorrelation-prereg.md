---
id: H-NEW-730
title: "Pre-reg — Content × Rhyme architectural anti-correlation: window-by-window Pearson r"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 (content compresses) + H-NEW-700 (rhyme disperses) — both at R²≥0.79 on same Hijra-kink; test if they are anti-correlated at window-level
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260442
---

# [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] — Content/Rhyme Anti-Correlation: Pre-Registration

## 1. Hypothesis

[[h-new-660-compression-tail-gradient|H-NEW-660]] found content-cohesion COMPRESSES toward the mushaf terminus (β = −0.01237, R²=0.986). [[h-new-700-phonological-compression-tail|H-NEW-700]] found phonological-rhyme DISPERSES on the same Hijra-kink (β = +0.00412, R²=0.789). 

**Hypothesis**: at window-level, the two metrics are NEGATIVELY correlated. Specifically:

> Pearson r(d̄_content_window, d̄_rhyme_window) ≤ −0.60.

If confirmed, this empirically locks the **iʿjāz architecture**: theological convergence simultaneous with sonic divergence is a window-by-window structural anti-twin signature.

## 2. Test design

For each K=15 window starting at s ∈ {1, ..., 100}:
- d̄_content[s] = mean pairwise FR-roots distance (load from [[h-new-660-compression-tail-gradient|h-new-660]] or recompute).
- d̄_rhyme[s] = mean pairwise rhyme-cosine distance (load from [[h-new-700-phonological-compression-tail|h-new-700]].json key `rhyme.d_observed`).
- Compute Pearson r and Spearman ρ.

### Permutation null
Shuffle d̄_rhyme positions (10000 perms, seed 20260442). Recompute Pearson r each time. Empirical p-value of |r_observed| ≥ |r_null|.

### Cross-window check
Identify the windows where:
- Both d̄_content LOW and d̄_rhyme HIGH (max iʿjāz signature: cohesive content + diverse rhyme) — terminal-tail expected.
- Both d̄_content HIGH and d̄_rhyme LOW (anti-iʿjāz: dispersed content + uniform rhyme) — head ṭiwāl expected.

## 3. Pre-committed direction

- Pearson r < 0 (negative correlation).
- |r| ≥ 0.60.
- Permutation p ≤ 0.025 (Bonferroni-2 — Pearson + Spearman).

## 4. Pre-committed thresholds

- **STRICT PASS**: r ≤ −0.60, p ≤ 0.025, |Spearman ρ| ≤ −0.55.
- **DIRECTIONAL**: r ≤ −0.40, p ≤ 0.05.
- **NULL**: r > −0.40 OR p > 0.05.

## 5. Bonferroni structure

Pearson + Spearman → Bonferroni-2 → α_corrected = 0.025.

## 6. What would FALSIFY

- r > 0: content and rhyme co-compress (would falsify the iʿjāz anti-twin).
- |r| < 0.40: weak relationship.

## 7. Methodology rules

- MW-1: instrument-prior — both metrics use existing project methodology.
- MW-3: alternative-models — Spearman in addition to Pearson.
- MW-7: not applicable (this is a primary pre-registered test).
- PRE-REG-STANDARD-04: hypothesis, null, direction, success criteria locked.

## 8. Files

- Script: `scripts/h_new_730_content_rhyme_anticorrelation.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-730.json`
- Findings: `findings/phase-b-hypotheses/h-new-730-content-rhyme-anticorrelation.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
