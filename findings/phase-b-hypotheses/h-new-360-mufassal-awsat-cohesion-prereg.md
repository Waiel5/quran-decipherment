---
id: H-NEW-360
title: "Mufaṣṣal-awsāṭ (Q 67-77) cohesion — N=11 higher-power block test; predicted intermediate cohesion"
phase: B
status: PRE-REGISTERED 2026-04-20
date: 2026-04-20
agent: team-lead (inline; ID 360 to skip codex)
parent_1: H-NEW-350 (ṭiwāl 17.3%ile; terminal-tail 0%ile)
parent_2: H-NEW-340 (block+formula stacking)
seed: 20260503
bonferroni_k: 2
bonferroni_family: h-new-360-mufassal-awsat-cohesion
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(11 classical mufaṣṣal-awsāṭ surahs = {Q 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77}; FR root distance matrix from H-NEW-111; primary statistic = mean pairwise FR within 11-surah set; null = 10000 random 11-surah draws; seed 20260503)"
direction: "Cell A mufaṣṣal-awsāṭ d̄ < null 2.5%ile AND p_less < α_bon; Cell B MW-5 predicted-DISPERSED control: random 11-surah draw at median position (no classical grouping)"
verdict: PENDING
---

# [[h-new-360-mufassal-awsat-cohesion|H-NEW-360]] — Mufaṣṣal-awsāṭ cohesion test

## 1. Question

[[h-new-350-al-tiwal-cohesion|H-NEW-350]] revealed a cohesion HIERARCHY across block types:
- Q 107-114 terminal tail: 0.0%ile STRICT PASS (extreme cohesion via content-homogeneity)
- al-ṭiwāl: 17.3%ile DIRECTIONAL (block-adjacent but content-diverse)

**Middle prediction**: mufaṣṣal-awsāṭ (Q 67-77) is the intermediate register — 11 short/medium surahs, mostly Meccan eschatological. Should fall between the two extremes.

Classical *mufaṣṣal-awsāṭ* = Q 67 al-Mulk through Q 77 al-Mursalāt:
- Q 67 al-Mulk (30v), Q 68 al-Qalam (52v), Q 69 al-Ḥāqqah (52v), Q 70 al-Maʿārij (44v)
- Q 71 Nūḥ (28v), Q 72 al-Jinn (28v), Q 73 al-Muzzammil (20v), Q 74 al-Muddaththir (56v)
- Q 75 al-Qiyāma (40v), Q 76 al-Insān (31v), Q 77 al-Mursalāt (50v)

Common themes: Day of Resurrection imagery, prophet Nūḥ, jinn, prayer, judgment.

## 2. Hypothesis

**H1 (content-homogeneity + block → cohesion)**: d̄(awsāṭ) < null 2.5%ile AND p_less < α_bon=0.025. Predicted percentile: between 0%ile (terminal tail extreme) and 8%ile (musabbiḥāt block).

**H0 (awsāṭ not cohesive)**: d̄ at median or above.

Pre-committed direction: mufaṣṣal-awsāṭ PASS at strict α_bon=0.025 at N=11.

## 3. Protocol

1. Load [[h-new-111-fisher-rao-mushaf|H-NEW-111]] FR distance matrix.
2. Classical set S_awsāṭ = {Q 67-77}; compute d̄.
3. Null: 10000 random 11-surah draws.
4. MW-5 negative control: random 11-surah draw from {Q 30-60} (middle mushaf, no classical block) — expected at ~50%ile (null-typical).

## 4. Bonferroni + MW-5

k=2 cells. α_bon=0.025.

## 5. Pre-committed predictions

Based on content-homogeneity hypothesis ([[h-new-350-al-tiwal-cohesion|H-NEW-350]]):
- **Predicted percentile: 2-7%ile** (between terminal-tail 0% and musabbiḥāt-block 8%)
- **Strict PASS expected** at N=11 (higher power than N=5-8)

If awsāṭ falls at 17%+ (ṭiwāl-like), the content-homogeneity hypothesis is weakened. If awsāṭ falls at 0-5%, hypothesis strongly supported.

## 6. Classical-scholarship anchor

- al-Suyūṭī *Itqān* on mufaṣṣal 3-part subdivision (ṭiwāl / awsāṭ / qiṣār)
- al-Zarkashī *al-Burhān* on mufaṣṣal boundaries
- Classical unanimity that Q 67-77 form the "middle" mufaṣṣal

## 7. Honest limits

1. Classical awsāṭ boundaries vary — some list Q 49-77 or Q 67-84. I use the canonical Q 67-77 (11 surahs).
2. N=11 should give strict α power if cohesion is real.
3. FR-roots only.

## 8. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_360_mufassal_awsat_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-360.json`
- Findings: `findings/phase-b-hypotheses/h-new-360-mufassal-awsat-cohesion.md`

Pre-reg locked 2026-04-20.
