---
id: H-NEW-390
title: "Q 55 al-Raḥmān outlier-exclusion test — isolate outlier-disruptor vs register-heterogeneity"
phase: B
status: PRE-REGISTERED 2026-04-20
date: 2026-04-20
agent: team-lead (inline; ID 390 skip codex)
parent: H-NEW-380 (Meccan half {Q 50-56} at 70.1%ile DISPERSED)
seed: 20260506
bonferroni_k: 2
bonferroni_family: h-new-390-q55-exclusion
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(Meccan-Q50-56 minus Q 55 = {Q 50, 51, 52, 53, 54, 56} N=6; vs Full Meccan-Q50-56 {Q 50-56} N=7 baseline from H-NEW-380; FR from H-NEW-111; 10000-perm null; seed 20260506)"
direction: "Cell A exclusion-subset d̄ < null 2.5%ile AND p < α_bon; Cell B comparison-delta: removing Q 55 reduces percentile by ≥50pp"
verdict: PENDING
---

# [[h-new-390-q55-outlier-exclusion|H-NEW-390]] — Q 55 al-Raḥmān outlier-exclusion test

## 1. Question

[[h-new-380-hijra-split|H-NEW-380]] showed Meccan half {Q 50-56} at 70.1%ile DISPERSED. Q 55 al-Raḥmān is an established OUTLIER ([[h-new-231-kl-divergence-per-surah|H-NEW-231]] highest KL-divergence among long surahs; [[h-new-234-q55-unified-profile|H-NEW-234]] unique cosmic-refrain profile). **Is Q 55 the specific disruptor, or is Meccan sub-register heterogeneity independent?**

Direct test: remove Q 55 and retest {Q 50, 51, 52, 53, 54, 56} at N=6.

## 2. Hypothesis

**H1 (Q 55 is the specific outlier-disruptor)**: exclusion-subset passes strict α_bon=0.025 OR percentile drops to ≤20%ile (large improvement from 70%).

**H0 (Meccan sub-register is heterogeneous independent of Q 55)**: exclusion-subset stays at 40%+ — little change.

Pre-committed direction: exclusion improves to ≤20%ile (delta ≥ 50 percentile points).

## 3. Protocol

1. FR matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
2. Exclusion subset {Q 50, 51, 52, 53, 54, 56} N=6; compute d̄.
3. Full Meccan half {Q 50-56} N=7 from [[h-new-380-hijra-split|H-NEW-380]] (d̄=0.9711, 70.1%ile).
4. Null: 10000 random 6-surah draws.

## 4. Pre-committed expectations

If Q 55 is strong outlier: removing it should:
- Decrease d̄ substantially
- Push percentile DOWN by ≥50pp (from 70% to ≤20%)

If Q 55 is not the key disruptor: percentile stays ~40-70%.

## 5. Honest limits

1. N=6 power limit per [[h-new-340-musabbihat-block-subset|H-NEW-340]] discussion (α_bon=0.025 hard at N=6).
2. Descriptive comparison to [[h-new-380-hijra-split|H-NEW-380]]'s N=7 result is the primary insight.
3. FR-roots only.

## 6. Classical anchor

- [[h-new-231-kl-divergence-per-surah|H-NEW-231]] Q 55 KL-divergence: highest among long surahs
- [[h-new-234-q55-unified-profile|H-NEW-234]] Q 55 as refrain-stylistic outlier
- al-Tirmidhī #3291 *ʿarūs al-Qurʾān*
- al-Zamakhsharī Q 55 as cosmic-mercy singular

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_390_q55_outlier_exclusion.py`
- JSON: `csv/h-new-390.json`
- Findings: `[[h-new-390-q55-outlier-exclusion|h-new-390]]-q55-outlier-exclusion.md`

Pre-reg locked 2026-04-20.
