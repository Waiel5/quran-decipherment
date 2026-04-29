---
id: Q019-F-04
title: Maryam-as-best-of-women hadith network density — Q 19 surah-naming as anchored in Bukhārī #3290 cluster
phase: B+
date: 2026-04-28
agent: Q019-maryam-specialist (Wave-D)
test: hadith-network density of Q 19-relevant transmissions vs short-Meccan / short-Medinan / Quranic-other-female-named (none) comparators
rules_tuple: (9-canonical-Sunni-books; AhmedBaset JSON corpus; substring keyword search; basmala-not-applicable; Hafs-Kufan)
seed: 20260428
bonferroni_k: 4
bonferroni_family: Q019-novel-findings
alpha_bon: 0.0125
---

# Q019-F-04 — Pre-registration

## Hypothesis (DIRECTION-LOCKED)

**H1**: The Q 19 hadith network (sub-corpus of all Q 19-relevant transmissions across the 9 canonical books) is ANCHORED in a **moderate-density cluster**, where the dominant sub-cluster is the **Maryam-as-best-of-women** tradition (Bukhārī #3290 + #3271 + parallels in Muslim, Tirmidhī, Aḥmad).

The Q 19 hadith density is predicted to be **moderate** — substantially less than Q 1 al-Fātiḥa, Q 36 Yāsīn, or Q 112 al-Ikhlāṣ — because Q 19's authentic *faḍāʾil* (recitation virtues) are sparse (the Ubayy *faḍl* is mawḍūʿ).

**Direction**: Q 19 hadith count (after de-duplication of false-positive matches) is in the **40th–60th percentile** of per-surah hadith counts.

## Null distribution

Permutation: shuffle the surah-keyword assignments across all 114 surahs while preserving total hadith counts; compute Q 19's rank.

10,000 perms, seed 20260428.

Test statistic: Q 19's percentile rank of cleaned hadith count.

## Direction of effect

Observed (preliminary, before cleaning false-positives):
- Q 19 raw hits ≈ 236 across 9 books
- Estimated cleaned (Q19-relevant) ≈ 25–30 distinct
- Comparator: Q 1 ≈ 150+; Q 36 ≈ 30+; Q 112 ≈ 80+; Q 24 = 64-citations (in `Q024-citations.md`)

Predicted Q 19 cleaned percentile rank ≈ 50%–60% (median range), consistent with moderate hadith density.

## Bonferroni correction

α = 0.05 / 4 = **0.0125**.

## Success / failure criteria

- **PASS** = Q 19 cleaned hadith count is in the 40th-60th percentile range; cluster-anchor sub-test confirms Maryam-best-of-women is the densest sub-cluster (≥30% of cleaned hits).
- **FAIL** = Q 19 cleaned count is in top-10% (would imply a richer hadith corpus than expected for Q 19) OR bottom-10% (would imply Q 19 is hadith-poor like Q 96 al-ʿAlaq); OR Maryam-best-of-women cluster is NOT the densest sub-cluster.

## Secondary tests

- (a) **Najāshī sub-cluster size**: count Najāshī-related hadith that explicitly mention Q 19 recitation. Pre-flight: NOT canonical-6-attested by exact wording; this is a sīra-level subset (Aḥmad + Ibn Isḥāq).
- (b) **ʿĪsā-ibn-Maryam eschatological-return cluster**: 30+ hadith. This is **larger** than the Maryam-best-of-women cluster; question is whether it's *content-anchored* in Q 19 vs Q 43 vs Q 5.
- (c) **Faḍāʾil recitation tradition for Q 19**: count canonical-6 hadiths recommending Q 19 recitation. Pre-flight: 0 in canonical-6 (Ubayy *faḍl* is mawḍūʿ).

## MW-1..MW-7 protections

- MW-1: keyword search rule pre-specified.
- MW-2: 10K perms.
- MW-3: 3 secondary tests.
- MW-4: not applicable.
- MW-5: replicate using broader keyword set (variant spellings).
- MW-6: control = Q 96 al-ʿAlaq (canonical-poor first-revealed comparator); Q 18 al-Kahf (mushaf-neighbour, different content).
- MW-7: post-hoc cap respected.

## Garden-of-forking-paths log

- The Q019-citations-raw.json output has 236 raw hits; the cleaned subset is approximate. Cleaning (de-duplication + relevance-filtering) is itself a methodology choice — locked here as: "include hits where keyword AND content-or-asbāb refers to Q 19 directly".
- Q 1's "150+" comparator is approximate from `data/literature/hadith/Q001-citations.md` (not exhaustively counted at this layer).
- Q 24's "64" comparator is `data/literature/hadith/Q033-citations.json`-style, manually curated.

## SHA256

To be computed at runtime by `scripts/Q019_F_04_maryam_best_of_women_hadith_network.py`.
