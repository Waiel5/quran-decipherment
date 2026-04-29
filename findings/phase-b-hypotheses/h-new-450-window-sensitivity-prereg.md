---
id: H-NEW-450
title: "Outlier-factor window-sensitivity — does Q 33/24/12/9 block-disruption replicate at ±3 and ±5?"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline)
parent_1: H-NEW-430 (4/4 novel outliers confirmed at ±2)
parent_2: H-NEW-440 (H-410 ranks are window-specific; Q 56 ±2-vs-±3 inconsistent)
parent_3: H-NEW-410 (full-corpus ±2 spectrum)
seed: 20260512
bonferroni_k: 18
bonferroni_family: h-new-450-window-sensitivity
alpha_bon: 0.002778
rules_tuple: "(FR from H-NEW-111; for each target k ∈ {9, 12, 24, 33, 55, 62} and window w ∈ {2, 3, 5}: block_k_w = {k-w,...,k-1,k,k+1,...,k+w} ∩ [1,114]; compute d̄_full, d̄_exc (k removed), percentiles p_full p_exc via 10000 random size-matched subsets; delta_pp(k, w) = p_exc − p_full. Per-cell Bonferroni k=18, α_bon=0.002778. Primary H1: novels show delta_pp(k, w) ≤ -15pp for ALL w ∈ {2,3,5}. Aggregate H1: ≥3/4 novels pass the window-consistency criterion AND Q 55 PC delta ≤ -5pp at ALL windows AND Q 62 NC |delta|<5pp at ALL windows.)"
direction: |
  Per-outlier window-consistency criterion (all 3 windows): delta_pp ≤ -15.0pp for ALL w.
  Per-PC (Q 55): delta ≤ -5.0pp at ALL windows (loose); strict ≤-15pp at any window is a bonus.
  Per-NC (Q 62): |delta| < 5.0pp at ALL windows.
  Aggregate: ≥3/4 novels pass + PC loose-pass at all windows + NC pass at all windows.
verdict: PENDING
---

# [[h-new-450-window-sensitivity|H-NEW-450]] — Window-sensitivity of outlier-factor

## 1. Question

[[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]] revealed that [[h-new-410-outlier-spectrum|H-NEW-410]]'s outlier ranking is **window-specific**: Q 56 al-Wāqiʿah ranked 3rd on ±2-window mean-distance but contributed only −0.15pp to ±2-block exclusion. The apparent rank was driven by a *specific* ±2 window that included Medinan Q 58.

**Does this window-sensitivity also undermine the [[h-new-430-corrected-direction-replication|H-NEW-430]] confirmed outliers?** If Q 33's |−34.89pp| exclusion effect at ±2 shrinks to <10pp at ±3 or ±5, then "corpus-strongest content-outlier" is a window-artifact claim, not a robust empirical invariant.

Conversely, if Q 33 / Q 24 / Q 12 / Q 9 all show |delta|≥15pp consistently across ±2, ±3, ±5, then the outlier-factor is a robust genuine-invariant — much stronger than window-specific.

Q 55 PC expected to show lower magnitude (because Q 55's ±k neighborhood at larger k absorbs Medinan members, diluting the single-outlier effect, per [[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]]'s lesson). Q 62 NC expected near-zero across all windows (NC robustness test).

## 2. Protocol

For each target k ∈ {9, 12, 24, 33, 55, 62} and window w ∈ {2, 3, 5}:
1. block_k_w = {k−w, …, k−1, k, k+1, …, k+w} ∩ [1, 114]
2. d̄_full = mean pairwise FR on block_k_w
3. d̄_exc = mean pairwise FR on block_k_w \ {k}
4. p_full, p_exc via 10000 random size-matched subsets (SAME FRESH seed per test)
5. delta(k, w) = p_exc − p_full

18 tests total (6 surahs × 3 windows). Bonferroni α_bon = 0.05/18 = 0.002778.

## 3. Pre-committed predictions

| Surah | Role | Pass criterion |
|:-:|:--|:--|
| Q 9 | novel | delta ≤ −15pp at ALL w∈{2,3,5} |
| Q 12 | novel | delta ≤ −15pp at ALL w |
| Q 24 | novel | delta ≤ −15pp at ALL w |
| Q 33 | novel | delta ≤ −15pp at ALL w (predicted strongest) |
| Q 55 | PC | delta ≤ −5pp at ALL w (loose) |
| Q 62 | NC | \|delta\| < 5pp at ALL w |

**Aggregate H1 CONFIRMED**: ≥3/4 novels maintain |−15pp|≥ across ALL windows AND Q 55 PC loose-pass at all windows AND Q 62 NC pass at all windows.

**Aggregate H0 / instrument-doubt**: any NC failure (Q 62 shows |delta|≥5pp at any window) = metric is window-sensitive for non-outliers too → outlier-factor claims weakened.

## 4. Predictions conditional on [[h-new-440-joint-outlier-pair-exclusion|H-NEW-440]] lessons

Given H-440's finding that Q 56 is NOT a cohesion-disruptor in ±2-block, we expect:
- Q 33 al-Aḥzāb at ±3 / ±5 will include Q 29 al-ʿAnkabūt, Q 30 al-Rūm (Meccan) and Q 36 Yā Sīn, Q 37 al-Ṣāffāt (Meccan). **More Meccan dilution — predict Q 33 effect possibly LARGER at ±3/±5** because Medinan register-contrast increases against bigger Meccan neighborhood.
- Q 24 al-Nūr at ±3 / ±5: adds Q 21 al-Anbiyāʾ (Meccan), Q 27 al-Naml (Meccan), Q 28 al-Qaṣaṣ (Meccan) — all Meccan prophetic-narrative. Q 24's Medinan-legal contrast should PERSIST or strengthen.
- Q 12 Yūsuf at ±3 / ±5: mixed Meccan-narrative neighborhood. Effect should hold or soften modestly.
- Q 9 al-Tawbah at ±3 / ±5: expands to Q 6 al-Anʿām, Q 13 al-Raʿd (both Meccan); effect should PERSIST as Medinan-warfare-edict vs Meccan-narrative contrast.
- Q 55 PC at ±3 / ±5: adds Q 51, 52 (Meccan) and Q 58, 59, 60 (Medinan) — increased chronology-seam dilution. Expect effect to DROP below −5pp magnitude, possibly to strict-fail on loose criterion.
- Q 62 NC at ±3 / ±5: adds Q 58, 59, 60 (Medinan), Q 65, 66, 67 (mix); still Medinan-dense — predict near-zero effect maintained.

## 5. Classical anchor (window-width scholarly precedent)

Classical *munāsabāt* (inter-surah-coherence) scholarship:
- **al-Biqāʿī** *Naẓm al-Durar* works at ±1 to ±2 window (immediate adjacency) — his per-surah analysis explicitly discusses *munāsaba* between *al-sūra al-sābiqa wa-al-lāḥiqa* (preceding and following surah).
- **al-Suyūṭī** *Tanāsuq al-Durar fī tanāsub al-Suwar* organizes by ±1 window.
- **al-Rāzī** *Mafātīḥ al-ghayb* often extends to ±5+ window for thematic-arc analysis (e.g., his discussion of the Meccan-period narrative-arc grouping).

**Empirical implication**: ±2 matches al-Biqāʿī's classical window; ±5 matches al-Rāzī's broader-thematic-arc. If outlier-factor is consistent across both windows, it's scholarly-anchored empirically across two distinct classical-methodology traditions.

## 6. Honest limits

1. **N=3 (at ±2 boundary surahs) to N=11 (at ±5 mid-corpus)** — subset sizes vary, null distributions differ.
2. **Target block for ±5 is very large** — 11-surah block for mid-corpus targets. Random null becomes wider.
3. **Bonferroni at k=18, α_bon=0.002778** — for 11000 perms resolution is 0.01% → significant. But percentile-delta approach is descriptive; primary test is effect-size-threshold, not p-value.
4. **No control for chronology / content-register homogeneity** — window-width effects will be confounded with chronology-mixing. Disentanglement requires [[h-new-460-q24-q33-hijab-pair|H-NEW-460]] chronology-homogenized test.
5. **FR-roots only.**
6. **Seed 20260512 is fresh** — no data-peeking concern, but not independent of underlying [[h-new-111-fisher-rao-mushaf|H-NEW-111]] matrix.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_450_window_sensitivity.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-450.json`
- Findings: `findings/phase-b-hypotheses/h-new-450-window-sensitivity.md`

Pre-reg locked 2026-04-21.
