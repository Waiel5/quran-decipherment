---
id: H-NEW-560
title: "Meccan-only mufaṣṣal-ṭiwāl {Q 50-56, 67-77} N=17 cohesion — does chronology-homogenization rescue ṭiwāl from H-550 NULL?"
phase: B
status: PRE-REGISTERED 2026-04-22
date: 2026-04-22
agent: team-lead (inline)
parent_1: H-NEW-550 (full ṭiwāl NULL at 23.32%ile)
parent_2: H-NEW-540 (awsāṭ CONFIRMED 0.00%)
parent_3: H-NEW-500 (qiṣār CONFIRMED 0.00%)
seed: 20260519
bonferroni_k: 3
bonferroni_family: h-new-560-meccan-tiwal
alpha_bon: 0.01667
rules_tuple: "(FR from H-NEW-111; PRIMARY 17-set M = {Q 50, 51, 52, 53, 54, 55, 56, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77} Meccan-only ṭiwāl — Q 57-66 Medinan block EXCLUDED; wait N=17 not 18: Q 50-56 = 7, Q 67-77 = 11, sum=18. Corrected to N=18. Let me recount: Q 50,51,52,53,54,55,56 = 7 surahs; Q 67,68,69,70,71,72,73,74,75,76,77 = 11 surahs; total 18. MW-5 full ṭiwāl N=28 from H-550 (reconfirm NULL ~23%ile); MW-6 Medinan-ṭiwāl-only N=10 {Q 57-66}. k=3 Bonferroni.)"
direction: |
  PRIMARY H1: d̄(Meccan-ṭiwāl-18) ≤ 10%ile of random-18 null — chronology-homogenization rescues cohesion.
  MW-5 REPLICATE: d̄(full ṭiwāl-28) = NULL (~23%ile); replicates H-550.
  MW-6: d̄(Medinan-ṭiwāl-10 Q 57-66) ≤ 15%ile of random-10 null — known partial-cluster (musabbiḥāt-5 + 5 others) should be moderately-cohesive.
  Aggregate: PRIMARY + MW-5 + MW-6 all passed = chronology is the primary driver of ṭiwāl's dispersion.
verdict: PENDING
---

# [[h-new-560-meccan-tiwal|H-NEW-560]] — Meccan-ṭiwāl chronology-homogenization test

## 1. Question

[[h-new-550-mufassal-tiwal-completion|H-NEW-550]] found ṭiwāl Q 50-77 at 23.32%ile — moderate, not extreme. Hypothesis from H-550 discussion: dispersion comes from Meccan+Medinan chronology-mixing.

**Test**: Restrict to Meccan-only ṭiwāl {Q 50-56 + Q 67-77} N=18. If this is ≤10%ile, chronology was the dilution-mechanism. If still NULL, ṭiwāl is inherently heterogeneous beyond chronology.

## 2. Protocol

PRIMARY set M = {Q 50, 51, 52, 53, 54, 55, 56, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77}, N=18.

Classical chronology (al-Suyūṭī *Itqān* nawʿ 1): all these 18 are Meccan.

d̄(M); 10000 random 18-subsets; percentile.

MW-5: full ṭiwāl N=28, replicate H-550 (~23%ile NULL).
MW-6: Medinan-ṭiwāl N=10 {Q 57-66} — mixed Medinan community-legal + musabbiḥāt-5 sub-cluster.

## 3. Pre-commits

| Test | Predicted | Gate |
|:--|:-:|:--|
| PRIMARY Meccan-ṭiwāl-18 | ≤ 10%ile | chronology rescue |
| MW-5 full ṭiwāl-28 | ~23%ile NULL | replicate H-550 |
| MW-6 Medinan-ṭiwāl-10 | ≤ 15%ile | musabbiḥāt-partial cluster |

## 4. Honest limits

1. Set M contains Q 55 (outlier, H-430) and Q 56 (rank-3 H-410) — may dilute.
2. Q 74 al-Muddaththir / Q 73 al-Muzzammil are among earliest Meccan revelations; possibly distinct-register.
3. MW-6 is small (N=10); heavy-tailed null.
4. FR-roots only.

## 5. Classical anchor

al-Suyūṭī *Itqān* chronology-classification: all 18 surahs in set M are Meccan. Meccan register consensus: prophetic-narrative, eschatological-warnings, cosmic-imagery, early-Meccan-brevity-threshold.

## 6. Deliverables

Pre-reg this file; script `h_new_560_meccan_tiwal.py`; JSON `csv/h-new-560.json`; findings `[[h-new-560-meccan-tiwal|h-new-560]]-meccan-tiwal.md`.

Pre-reg locked 2026-04-22.
