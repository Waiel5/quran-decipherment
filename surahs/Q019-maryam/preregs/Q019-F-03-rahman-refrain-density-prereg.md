---
id: Q019-F-03
title: al-Raḥmān refrain density — Q 19 corpus rank-1 by absolute count vs Q 55 al-Raḥmān comparator
phase: B+
date: 2026-04-28
agent: Q019-maryam-specialist (Wave-D)
test: per-surah token frequency + density permutation null
rules_tuple: (no-tashkeel, orthographic-token, exact-substring "الرحمن", basmala-NOT-counted-in-content (counted only in Q1), Hafs-Kufan, Mashriqi)
seed: 20260428
bonferroni_k: 4
bonferroni_family: Q019-novel-findings
alpha_bon: 0.0125
---

# Q019-F-03 — Pre-registration

## Hypothesis (DIRECTION-LOCKED)

**H1**: Q 19 Maryam has the **highest absolute count** of *al-Raḥmān* (الرحمن) tokens in the corpus body (excluding basmala). Pre-flight observation: Q 19 = 12 occurrences, vs Q 43 = 5, Q 21 = 4, Q 36 = 4, Q 67 = 4.

**H2 (counter-direction lock)**: Q 55 al-Raḥmān ("the Most Merciful" surah) — despite being NAMED al-Raḥmān — has FEWER al-Raḥmān tokens than Q 19. The classical reading associates Q 55 with the divine-name *al-Raḥmān*, but the *literal token* الرحمن appears only at v.1 of Q 55 (and 0 elsewhere in its body). Q 55's refrain is *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* (31×), NOT the noun *al-Raḥmān*.

**Direction**: Q 19 absolute al-Raḥmān count > Q 55's; Q 19 ranks 1.

## Null distribution

Permutation: redistribute the corpus's 169 (estimated) al-Raḥmān tokens across all 114 surahs uniformly weighted by surah length. 10,000 perms, seed 20260428.

Test statistic: rank of Q 19 in absolute count.

## Direction of effect

Observed: Q 19 = 12 (verified `02-content-analysis.md`); Q 55 ≈ 1 (verse 1 only). Q 19 ranks 1.

Under permutation null (uniform-by-length), Q 19's expected count ≈ 12 × (Q19_words / total_words) ≈ 169 × (1012 / 78000) ≈ 2.2. Observed 12 is ≈ 5× expected.

## Bonferroni correction

α = 0.05 / 4 = **0.0125**.

## Success / failure criteria

- **PASS** = Q 19 rank = 1 absolute count, permutation p < 0.0125.
- **FAIL** = Q 19 rank > 1, OR permutation p ≥ 0.0125.

## Secondary tests

- (a) **Density-per-verse**: Q 19 = 12/98 = 0.122/v. Q 1 = 2/7 = 0.286/v (highest density given short length). What is Q 19's density-rank when controlling for surah length ≥ 30 verses?
- (b) **Position within Q 19**: are the 12 al-Raḥmān tokens *concentrated* in the eschatological closing (vv. 59-98)? Pre-flight: 8 of 12 are in vv. 58–96. Test: position-permutation null (verse-position re-randomized within surah) — is the cluster-position significant?
- (c) **Comparator extension**: Q 67 al-Mulk has 4 occurrences in 30 verses = 0.133/v. Per-verse density rank: Q 1 > Q 67 > Q 19 > Q 55 (0/v) > Q 43.

## MW-1..MW-7 protections

- MW-1: substring count rule pre-specified.
- MW-2: 10K perms.
- MW-3: 3 secondary tests.
- MW-4: not applicable.
- MW-5: replicate using min-tashkeel and full-tashkeel variants.
- MW-6: control = Q 55 al-Raḥmān as the surah-named-comparator (expected to score 0 in body).
- MW-7: post-hoc cap respected.

## Garden-of-forking-paths log

- The Q 19 al-Raḥmān-count finding emerged from `02-content-analysis.md` content-scan. Pre-reg locked HERE before formal run.
- Counter-prediction (H2) is the **classical-vs-empirical inversion**: Q 55 is *named* al-Raḥmān but *uses* it 1×; Q 19 is *named* Maryam but *uses* al-Raḥmān 12×. This is a highly-publishable inversion if confirmed.

## SHA256

To be computed at runtime by `scripts/Q019_F_03_rahman_refrain_density.py`.
