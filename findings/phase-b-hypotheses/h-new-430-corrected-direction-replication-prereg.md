---
id: H-NEW-430
title: "Outlier-factor generalization — CORRECTED-DIRECTION replication of H-NEW-420 with Q 62 NULL-control"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline)
parent_1: H-NEW-420 (pre-reg NULL on mis-signed direction; strong inverse post-hoc)
parent_2: H-NEW-400 (Q 62 exclusion +1.6pp NULL — the only prior correctly-signed exclusion test on this framework)
parent_3: H-NEW-390 (Q 55 inclusion disruption +32.6pp — sign-convention source)
seed: 20260510
bonferroni_k: 6
bonferroni_family: h-new-430-corrected-direction
alpha_bon: 0.008333
rules_tuple: "(FR from H-NEW-111; for each target k ∈ {9, 12, 24, 33, 55, 62}: define block_k = {k-2, k-1, k, k+1, k+2} ∩ [1,114]; compute d̄_full, d̄_exc, percentiles p_full, p_exc via 10000 random-subset permutations; delta_pp = p_exc − p_full. CORRECTED DIRECTION: delta_pp ≤ −15.0 ⟺ CONFIRM-outlier. Q 55 PC expected CONFIRM (-10pp ≤ delta ≤ -5pp loose-PC; strict-PC if ≤ -15pp). Q 62 NC expected NULL (|delta| < 5pp). Bonferroni k=6; α_bon = 0.008333)"
direction: |
  Per-target pre-committed direction:
  - Q 9 al-Tawbah: CONFIRM if delta ≤ -15pp (H-420 post-hoc: -20.72)
  - Q 12 Yūsuf: CONFIRM if delta ≤ -15pp (H-420 post-hoc: -20.88)
  - Q 24 al-Nūr: CONFIRM if delta ≤ -15pp (H-420 post-hoc: -26.16)
  - Q 33 al-Aḥzāb: CONFIRM if delta ≤ -15pp (H-420 post-hoc: -35.69) — predicted STRONGEST
  - Q 55 al-Raḥmān (PC): PASS-PC if delta ≤ -5pp (H-420: -10.52); STRICT-PC-CONFIRM if delta ≤ -15pp
  - Q 62 al-Jumuʿa (NC): NULL-CONTROL-PASS if |delta| < 5pp (H-420 analogue: H-NEW-400 exclusion was +1.6pp on the non-±2 block, but NOT directly comparable — this test is the first ±2-block exclusion for Q 62)
  Aggregate H1: ≥4/4 novels CONFIRM + PC PASS + NC NULL-CONTROL-PASS = outlier-factor empirically established as generalizing.
verdict: PENDING
---

# [[h-new-430-corrected-direction-replication|H-NEW-430]] — Corrected-direction replication + Q 62 NULL-control

## 1. Question

[[h-new-420-novel-outlier-exclusion|H-NEW-420]] observed a large, consistent inverse-direction effect (all 4 novel outliers + Q 55 PC show delta ≤ -10pp exclusion-restoration) but failed pre-registration because the direction-lock was wrong-signed.

**[[h-new-430-corrected-direction-replication|H-NEW-430]] re-pre-registers with the correctly-signed direction and adds Q 62 al-Jumuʿa as a NULL-control** to convert the post-hoc finding into a pre-registered, Bonferroni-protected confirmation.

**Key difference from [[h-new-420-novel-outlier-exclusion|H-NEW-420]]**:
- Direction: `delta ≤ -15pp` (correctly signed).
- NC: Q 62 tested on its own ±2 block (first time on this framework).
- k increased to 6 (4 novels + Q 55 PC + Q 62 NC), α_bon = 0.008333.

## 2. Protocol

Identical to [[h-new-420-novel-outlier-exclusion|H-NEW-420]] **except**:
1. Seed 20260510 (fresh independent permutation draws).
2. Direction: `delta_pp ≤ -15.0` confirms.
3. Targets: {Q 9, 12, 24, 33} (novels) + {Q 55} (positive control; predicted CONFIRM) + {Q 62} (NULL control; predicted |delta|<5pp).
4. Bonferroni k=6.

For each target k:
- block_k = {k-2, k-1, k, k+1, k+2} ∩ [1, 114]
- d̄_full = mean pairwise FR on block_k
- d̄_exc = mean pairwise FR on block_k \ {k}
- p_full, p_exc = percentiles vs 10000 random size-matched subsets
- delta_pp = p_exc − p_full

Q 62's block: {60, 61, 62, 63, 64}. Contains fellow musabbiḥāt members Q 61 and Q 64 (high-cohesion classical-block members per [[h-new-340-musabbihat-block-subset|H-NEW-340]]). Q 62 predicted NULL because its own ±2 neighborhood is tightly coherent.

## 3. Pre-committed predictions

| Target | Role | Predicted delta_pp | Pass condition |
|:-:|:--|:-:|:--|
| Q 9 | novel outlier | ≤ -15 | CONFIRM |
| Q 12 | novel outlier | ≤ -15 | CONFIRM |
| Q 24 | novel outlier | ≤ -15 | CONFIRM |
| Q 33 | novel outlier | ≤ -15 (predicted strongest) | CONFIRM |
| Q 55 | positive control | ≤ -5 loose; ≤ -15 strict | PC-PASS |
| Q 62 | NULL control | `|delta|` < 5 | NC-PASS |

**Aggregate H1**: ≥4/4 CONFIRM + PC-PASS + NC-PASS = outlier-factor generalization CONFIRMED.

**H0**: any PC-FAIL (Q 55 delta > -5pp) OR NC-FAIL (|Q 62 delta| ≥ 5pp) breaks the instrument → provisional INSTRUMENT-BROKEN until rebuild.

## 4. Honest limits

1. **This is NOT statistical independence from [[h-new-420-novel-outlier-exclusion|H-NEW-420]].** Same source matrix [[h-new-111-fisher-rao-mushaf|H-NEW-111]], same protocol, same targets. What IS independent: (a) fresh permutation seed, (b) correct direction-lock (no data-peeking possible at this point since sign was fixed pre-execution), (c) addition of Q 62 NC — NEW test never run on this framework.
2. **Replication with known expected outcome is a weaker form of confirmation** than novel pre-registered prediction. The scientific novelty in [[h-new-430-corrected-direction-replication|H-NEW-430]] is the **Q 62 NC behavior** — if it behaves as predicted (NULL), the instrument is validated; if it shows large effect, the instrument over-counts and all prior outlier claims are suspect.
3. **The Q 62 NC prediction is the SCIENTIFICALLY DECISIVE test**. All 4 novels are known to pass; Q 55 PC is known to pass. Q 62 NC outcome is genuinely unknown at pre-reg time.
4. **±2 window is FR-roots-only.**
5. **Bonferroni k=6 at α_bon=0.008333**: for strict-inferential claim, the 1-1.667th percentile gate is narrow given N=4/5 subsets. But the directional effect sizes from H-420 are -20 to -36pp, well beyond any single-test α gate.
6. **PC loose/strict split**: loose ≤-5pp allows Q 55 to PASS-PC even with the neighborhood-contrast damping discovered post-hoc in H-420. Strict ≤-15pp is harder but the honest target.

## 5. Classical anchor for Q 62 NC prediction

Q 62 al-Jumuʿa ±2 neighborhood:
- **Q 60 al-Mumtaḥanah**: Medinan, 13 verses, muhājirāt-women-testing verses — community-legal register.
- **Q 61 al-Ṣaff**: Medinan, 14 verses, *yusabbiḥu li-Llāhi* opening (musabbiḥāt member), jihād-formation-ranks theme.
- **Q 62 al-Jumuʿa**: Medinan, 11 verses, *yusabbiḥu li-Llāhi* opening, Friday-prayer institution.
- **Q 63 al-Munāfiqūn**: Medinan, 11 verses, hypocrite-diagnostics.
- **Q 64 al-Taghābun**: Medinan, 18 verses, *yusabbiḥu li-Llāhi* opening (musabbiḥāt member), eschatological-balance.

**Classical tradition** (al-Suyūṭī *Itqān* ch. 17; al-Zamakhsharī *Kashshāf* on Q 59:1) groups Q 57, 59, 61, 62, 64 as the *musabbiḥāt al-khams* — the five *yusabbiḥu*-openers. **Three of Q 62's four ±2 neighbors are musabbiḥāt members** (Q 61, 64 directly; Q 60 adjacent). This is maximally-coherent neighborhood — strongest test that the metric is not over-counting.

## 6. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_430_corrected_direction_replication.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-430.json`
- Findings: `findings/phase-b-hypotheses/h-new-430-corrected-direction-replication.md`

Pre-reg locked 2026-04-21.
