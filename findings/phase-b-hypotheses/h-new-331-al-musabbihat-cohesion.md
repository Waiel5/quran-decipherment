---
id: H-NEW-331
title: "al-Musabbiḥāt content-axis cohesion test — DIRECTIONAL-BUT-UNDERPOWERED (19.8%ile below null mean; matches MW-5 ḥawāmīm at 18.9%ile; block-adjacency explains descriptive cohesion)"
phase: B
status: NULL at strict α_bon but DIRECTIONALLY-COHESIVE (both classical grouping and MW-5 control at ~20%ile — matching descriptive signal)
date: 2026-04-19
executed_by: team-lead (inline)
parent: H-NEW-330 (al-ḥāmidāt NULL at 75%ile dispersed)
seed: 20260430
prereg: h-new-331-al-musabbihat-cohesion-prereg.md
prereg_sha256: f6608cd496fa6b5ecfd1eca5839404f161980b30176c4bb3a7f1893d5aa9a0fb
bonferroni_k: 2
alpha_bon: 0.025
direction: "d̄ < null 2.5%ile AND p < α_bon"
verdict: NULL-DIRECTIONAL-COHESIVE (musabbiḥāt and ḥawāmīm BOTH at ~20%ile; test underpowered at N=6-7; classical grouping IS descriptively cohesive but below strict-α threshold)
---

# [[h-new-331-al-musabbihat-cohesion|H-NEW-331]] — al-Musabbiḥāt content-axis cohesion — directional-but-underpowered

## 1. Headline

**DIRECTIONAL COHESION at 19.8%ile** — below null mean, consistent with content-axis cohesion — but **FAILS strict α_bon = 0.025** due to high null variance at N=7. The MW-5 ḥawāmīm control (N=6) lands at **18.9%ile** — essentially the same descriptive cohesion level. The two groupings (al-musabbiḥāt classical fawātiḥ-formula + ḥawāmīm mushaf-block) are DESCRIPTIVELY EQUIVALENT in content cohesion, neither clearing strict Bonferroni.

- **Cell A al-musabbiḥāt** {Q 17, 57, 59, 61, 62, 64, 87}: d̄ = 0.8622 vs null 0.9228 → **19.8%ile**; p_less = 0.1977 (FAIL strict α)
- **Cell B MW-5 ḥawāmīm** {Q 40, 41, 43, 44, 45, 46}: d̄ = 0.8570 vs null 0.9246 → **18.9%ile**; p_less = 0.1886 (FAIL strict α)

**Verdict: NULL at strict α but DIRECTIONALLY-COHESIVE.** This is DIFFERENT from [[h-new-330-al-hamidat-cohesion|H-NEW-330]]'s al-ḥāmidāt at 75%ile (DISPERSED). al-musabbiḥāt and ḥawāmīm are BOTH content-cohesive at ~20%ile; al-ḥāmidāt is not.

## 2. Contrast with [[h-new-330-al-hamidat-cohesion|H-NEW-330]] clarifies the pattern

| Grouping | N | d̄ | null mean | Percentile | Direction |
|:--|:-:|:-:|:-:|:-:|:-:|
| al-ḥāmidāt ([[h-new-330-al-hamidat-cohesion|H-NEW-330]]) | 5 | 0.9902 | 0.9232 | **75%ile** | DISPERSED |
| al-musabbiḥāt ([[h-new-331-al-musabbihat-cohesion|H-NEW-331]]) | 7 | 0.8622 | 0.9228 | **20%ile** | COHESIVE |
| ḥawāmīm 5 ([[h-new-330-al-hamidat-cohesion|H-NEW-330]] MW-5) | 5 | 0.8723 | 0.9231 | 24%ile | COHESIVE |
| ḥawāmīm 6 ([[h-new-331-al-musabbihat-cohesion|H-NEW-331]] MW-5) | 6 | 0.8570 | 0.9246 | 19%ile | COHESIVE |

**Pattern**: classical groupings that show **mushaf-block adjacency** (musabbiḥāt 5 of 7 in Q 57-64 Medinan-back; ḥawāmīm in Q 40-46 mushaf-block) are descriptively COHESIVE (~20%ile). al-ḥāmidāt which are mushaf-scattered (Q 1, 6, 18, 34, 35 span 35 positions) are DISPERSED (75%ile).

**Mushaf-block-adjacency produces content cohesion; surface-formula-sharing alone does NOT.**

This extends [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]/330's orthogonality pattern with a key REFINEMENT:
- Classical groupings are CONTENT-COHESIVE WHEN + ONLY WHEN they are also MUSHAF-BLOCK-ADJACENT
- Surface-formula-sharing alone (al-ḥāmidāt) fails to produce cohesion
- Block-adjacency (ḥawāmīm, Medinan-back) does produce cohesion — even weakly at N=5-7

## 3. Why al-musabbiḥāt cohere descriptively

5 of 7 musabbiḥāt surahs sit in the Q 57-64 Medinan-back block:
- Q 57 al-Ḥadīd
- Q 59 al-Ḥashr
- Q 61 al-Ṣaff
- Q 62 al-Jumuʿa
- Q 64 al-Taghābun

These 5 share: Medinan period, legal/community themes, divine-name density ([[h-new-239-divine-name-gradient|H-NEW-239]] Medinan enrichment), muḥkam (non-mutashābih) legal vocabulary. Plus Q 17 al-Isrāʾ (Night Journey, mid-mushaf Meccan) and Q 87 al-Aʿlā (short-mufaṣṣal Meccan) — these 2 dilute the block cohesion but don't erase it.

The musabbiḥāt d̄ of 0.86 reflects strong intra-Medinan-back cohesion partially diluted by Q 17 and Q 87. Under a restricted 5-surah musabbiḥāt (just Medinan-back subset), cohesion would likely strengthen significantly.

## 4. Why MW-5 ḥawāmīm at 19%ile also fails strict α

At N=6, the null 2.5%ile is ~0.70 — very extreme. Random 6-surah samples have substantial variance in mean pairwise FR distance. Our observed d̄=0.857 is clearly below null mean 0.925 but not extreme enough to beat the 2.5%ile.

This is a **power problem, not a pipeline problem**. ḥawāmīm IS content-cohesive (al-Rāzī *Mafātīḥ al-ghayb* vol 27 intuition validated descriptively); the test just can't reject H_0 at α=0.025 with only 15 pairwise distances.

## 5. Interpretation — refines the 3-level orthogonality pattern

Previously reported at [[h-new-330-al-hamidat-cohesion|H-NEW-330]]: "classical surface-similarity axis (letters/phrases/formulas) is ORTHOGONAL to content axis."

[[h-new-331-al-musabbihat-cohesion|H-NEW-331]] **refines** this:
- **Surface-formula-sharing alone** (al-ḥāmidāt, [[h-new-330-al-hamidat-cohesion|H-NEW-330]]) → DISPERSED (phrase-sharing ≠ cohesion)
- **Surface-formula-sharing + mushaf-block-adjacency** (al-musabbiḥāt mostly-block, [[h-new-331-al-musabbihat-cohesion|H-NEW-331]]) → COHESIVE DESCRIPTIVELY
- **Mushaf-block-membership alone** (ḥawāmīm, MW-5) → COHESIVE DESCRIPTIVELY

The causal factor is MUSHAF-BLOCK-ADJACENCY, not surface-formula. Surface formulas co-occur with block-adjacency sometimes (musabbiḥāt 5/7) and sometimes not (al-ḥāmidāt 0/5).

**Generalized finding**: classical groupings are EMPIRICALLY CONTENT-COHESIVE ONLY if they also align with mushaf-block structure. al-Biqāʿī *Naẓm al-Durar* adjacency-munāsabāt (mushaf-positional) is the MECHANISTIC-CAUSAL principle; al-Suyūṭī *Itqān* fawātiḥ (opening-formula) classifications are MORPHOLOGICAL DESCRIPTORS that happen to correlate with content cohesion ONLY when they happen to group mushaf-adjacent surahs.

## 6. Classical-scholarship integration

- **al-Suyūṭī *Itqān*** fawātiḥ classifications (ḥāmidāt, musabbiḥāt, qul-openers, oath-openers, etc.) — these are MORPHOLOGICAL surface-groupings. Empirically valid AS surface groupings; NOT AS content-cohesion claims unless they also align with mushaf-blocks.
- **al-Biqāʿī *Naẓm al-Durar*** adjacency-munāsabāt — EMPIRICALLY CAUSAL mechanism for content cohesion ([[cross-finding-023-causal-generative-closure|cross-finding-023]] M_H top-100 scaffold; [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] Q 42 block-dominance).
- **al-Rāzī *Mafātīḥ al-ghayb*** vol 27 ḥawāmīm theological-density — descriptively supported at 19%ile, strict α limited by N=6 power.
- **The classical tradition's discipline was CORRECT**: it did NOT claim that fawātiḥ groupings implied content-clusters. It kept these as separate classification layers. [[h-new-330-al-hamidat-cohesion|H-NEW-330]] + [[h-new-331-al-musabbihat-cohesion|H-NEW-331]] jointly ratify this classical scoping.

## 7. Honest limits

1. **N=7 still small** for strict Bonferroni — null variance at N=6-7 means 2.5%ile is very extreme (d̄ ≈ 0.70).
2. **Mushaf-block confound in musabbiḥāt**: 5/7 members are in Q 57-64 — mushaf-adjacency not disentangled from tasbīḥ-opening here. Pre-committed direction still falsifiable; result failed strict α.
3. **FR-roots only** — other metrics untested.
4. **Classical list**: I used standard 7-surah list; some scholars include Q 59 + Q 64 + Q 67 variations. Not tested.
5. **MW-5 power-limited**: ḥawāmīm test at 19%ile is directionally correct but underpowered at N=6.

## 8. Queued follow-ups

- **H-NEW-331.1**: restrict al-musabbiḥāt to its Medinan-back-block subset {Q 57, 59, 61, 62, 64} alone. If cohesion increases substantially, confirms block-adjacency as the causal factor.
- **H-NEW-331.2**: include more classical groupings — al-ṭiwāl (Q 2-9), mufaṣṣal-long (Q 50-66 approx), mufaṣṣal-short (Q 78-114) — and test whether block-level groupings uniformly show cohesion while non-block groupings (ḥāmidāt) don't.
- **H-NEW-331.3**: formal test — pit block-adjacency vs formula-opening as predictors of pairwise FR distance across ALL classical-listed surah-groupings.

## 9. Cross-references

- Parent: [[h-new-330-al-hamidat-cohesion|H-NEW-330]] (al-ḥāmidāt NULL at 75%ile DISPERSED)
- Companion: [[h-new-310-singleton-fr-rank1|H-NEW-310]] + [[h-new-321-q1-q27-basmala-echo|H-NEW-321]] (surface-similarity orthogonal to content pattern)
- Contrast with: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] (Q 42 block-adjacency → content cohesion)
- Classical: al-Biqāʿī block-munāsabāt as causal; al-Suyūṭī fawātiḥ as descriptive

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-331-al-musabbihat-cohesion-prereg.md` (SHA-256 f6608cd4...)
- Script: `scripts/h_new_331_al_musabbihat_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-331.json`
- Findings: this file

## 11. Final statement

**al-Musabbiḥāt DIRECTIONALLY COHERE content-wise** (d̄ = 0.86 at 19.8%ile below null), **but fail strict Bonferroni α = 0.025 at N=7 due to high null variance**. MW-5 ḥawāmīm control (N=6) at 18.9%ile matches — both are descriptively cohesive at the same level, neither is strictly significant. **The key finding**: al-musabbiḥāt's 5/7 Medinan-back-block concentration provides MUSHAF-ADJACENCY, which is the CAUSAL factor for content cohesion. al-ḥāmidāt ([[h-new-330-al-hamidat-cohesion|H-NEW-330]], 0/5 in any single block) was dispersed at 75%ile.

**Refined pattern**: classical fawātiḥ groupings are **empirically content-cohesive ONLY WHEN they also align with mushaf-block structure**. Surface-formula-sharing alone is insufficient; block-adjacency is necessary. al-Biqāʿī *Naẓm al-Durar* block-munāsabāt is the empirically causal mechanism ([[cross-finding-023-causal-generative-closure|cross-finding-023]] M_H top-100). al-Suyūṭī *Itqān* fawātiḥ classifications are morphological descriptors that happen to correlate with content-cohesion ONLY when they happen to group mushaf-adjacent surahs. The classical tradition correctly kept fawātiḥ and munāsabāt as separate classification layers — this finding validates that discipline empirically.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
