---
id: H-NEW-370
title: "Mufaṣṣal-ṭiwāl (Q 50-66) cohesion — completes al-Suyūṭī 3-part empirical hierarchy at N=17 high power"
phase: B
status: PRE-REGISTERED 2026-04-20
date: 2026-04-20
agent: team-lead (inline; ID 370 to skip codex range)
parent_1: H-NEW-360 (mufaṣṣal-awsāṭ Q 67-77 at 7.1%ile)
parent_2: H-NEW-350 (mufaṣṣal-qiṣār Q 107-114 at 0%ile EXTREME)
seed: 20260504
bonferroni_k: 2
bonferroni_family: h-new-370-mufassal-tiwal-cohesion
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(17 classical mufaṣṣal-ṭiwāl surahs = {Q 50..66}; FR root distance matrix from H-NEW-111; primary = mean pairwise FR within 17-surah set; null = 10000 random 17-surah draws; seed 20260504)"
direction: "Cell A d̄ < null 2.5%ile AND p_less < α_bon=0.025; predicted 3-10%ile range"
verdict: PENDING
---

# [[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] — Mufaṣṣal-ṭiwāl cohesion (completes 3-part hierarchy)

## 1. Question

With [[h-new-360-mufassal-awsat-cohesion|H-NEW-360]] (mufaṣṣal-awsāṭ 7.1%ile) + [[h-new-350-al-tiwal-cohesion|H-NEW-350]] Cell B (mufaṣṣal-qiṣār Q 107-114 subset 0%ile), two of al-Suyūṭī *Itqān*'s three mufaṣṣal sub-divisions have been empirically tested. The third is mufaṣṣal-ṭiwāl {Q 50-66}. **Does it complete a monotonic cohesion hierarchy?**

Predicted under content-homogeneity hypothesis ([[h-new-350-al-tiwal-cohesion|H-NEW-350]]/360):
- qiṣār Q 107-114: 0%ile (shortest, most formulaic) ✓ known
- awsāṭ Q 67-77: 7.1%ile (medium-short, eschatological) ✓ known
- ṭiwāl Q 50-66: ~3-10%ile (medium-long, mixed Meccan eschatology + Medinan legal)

If ṭiwāl lands at 3-10%ile, the al-Suyūṭī 3-part classification is empirically validated as a monotonic gradient in content-cohesion. If ṭiwāl lands at 15-20% (ṭiwāl-proper-like), the hierarchy is non-monotonic or needs refinement.

## 2. Hypothesis

**H1**: d̄(mufaṣṣal-ṭiwāl) at 3-10%ile AND strict α_bon=0.025 PASS.

**H0**: ṭiwāl at 15%+ OR fails strict α.

Pre-committed direction: strict PASS expected at N=17 (highest power in the series).

## 3. Classical boundaries

Classical *mufaṣṣal-ṭiwāl* varies between:
- Q 49-66 (some scholars)
- Q 50-66 (most common)
- Q 50-77 (aggregates ṭiwāl + awsāṭ)

I use **Q 50-66 (17 surahs)** per most-common classical definition (al-Suyūṭī *Itqān*, al-Zarkashī *Burhān*).

## 4. Protocol

1. Load [[h-new-111-fisher-rao-mushaf|H-NEW-111]] FR distance matrix.
2. Ṭiwāl S = {Q 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66}; d̄.
3. Null: 10000 random 17-surah draws; compute d̄_null.
4. MW-5 positive control: 17 random surahs from terminal region (Q 98-114) — expected high cohesion.

## 5. Bonferroni

k=2, α_bon=0.025.

## 6. Honest limits

1. N=17 is the highest-N test in this series — power should be sufficient for strict α if cohesion is ≥ moderate.
2. Classical boundaries are slightly variable.
3. FR-roots only.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_370_mufassal_tiwal_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-370.json`
- Findings: `findings/phase-b-hypotheses/h-new-370-mufassal-tiwal-cohesion.md`

Pre-reg locked 2026-04-20.
