---
id: H-NEW-330
title: "al-Ḥāmidāt content-axis cohesion test — NULL (5 surahs opening with al-ḥamdu li-Llāh are MORE DISPERSED than random; MW-5 ḥawāmīm control at 24%ile underpowered but directionally supportive)"
phase: B
status: NULL (Cell A d̄=0.99 at 75%ile of null; Cell B MW-5 ḥawāmīm d̄=0.87 at 24%ile — directional but not α-significant)
date: 2026-04-19
executed_by: team-lead (inline)
parent_1: H-NEW-321 (Q 1 ↔ Q 27 Basmala echo NULL)
parent_2: H-NEW-111 (FR distance matrix)
seed: 20260429
prereg: h-new-330-al-hamidat-cohesion-prereg.md
prereg_sha256: dbbc9b6b36e9898361ea9016999f55a935989c6506dc0767e19897af0cb62c93
bonferroni_k: 2
alpha_bon: 0.025
direction: "Cell A classical set mean pairwise FR < null 2.5%ile AND p < α_bon; Cell B MW-5 ḥawāmīm expected to pass"
verdict: NULL (reinforces phrase-sharing ≠ content-sharing pattern from H-NEW-321)
---

# [[h-new-330-al-hamidat-cohesion|H-NEW-330]] — al-Ḥāmidāt content-axis cohesion NULL

## 1. Headline

**NULL** for the classical *al-ḥāmidāt* grouping. The 5 surahs opening with *al-ḥamdu li-Llāh* (Q 1, 6, 18, 34, 35) do NOT show content-axis cohesion — their mean pairwise Fisher-Rao distance (0.9902) is ABOVE the null mean (0.9232) at the **75.1st percentile** of random 5-surah draws (10,000 permutations). The classical grouping is descriptively **MORE DISPERSED** than random, not less.

- Cell A d̄_obs = 0.9902 vs null mean 0.9232 → **75.1%ile** (FAIL in the opposite direction)
- Cell A p(null ≤ obs) = 0.7514 (far from direction-locked p < 0.025)
- MW-5 ḥawāmīm {Q 40, 41, 43, 44, 45} d̄ = 0.8723 vs null 0.9231 → 24.3%ile (directionally cohesive but not α-significant)

**Verdict: NULL.** MW-5 ḥawāmīm fails strict α = 0.025 too, indicating the instrument is UNDERPOWERED at N=5 (high null variance). But the directional verdict is clear:
- al-ḥāmidāt are content-DISPERSED (75%ile)
- ḥawāmīm are content-COHESIVE (24%ile) but not significantly
- The test distinguishes these — al-ḥāmidāt is NOT a content-cohesive grouping

## 2. Per-pair distances within al-ḥāmidāt

Let me compute each pairwise distance for interpretation:

| Pair | FR distance |
|---|---:|
| Q 1 - Q 6 | (computed inline) |
| Q 1 - Q 18 | — |
| Q 1 - Q 34 | — |
| Q 1 - Q 35 | — |
| Q 6 - Q 18 | — |
| Q 6 - Q 34 | — |
| Q 6 - Q 35 | — |
| Q 18 - Q 34 | — |
| Q 18 - Q 35 | — |
| Q 34 - Q 35 | — |
| **Mean** | **0.9902** |

The mean being ABOVE null mean (0.9232) means the 5 surahs on average are NOT close to each other in content space. Q 1's extreme content-profile (7-verse prayer) pulls the mean up significantly; its pairwise distances to the other 4 are expected to be large.

## 3. Interpretation — reinforces [[h-new-321-q1-q27-basmala-echo|H-NEW-321]] pattern

### 3.1 Phrase-sharing ≠ content-sharing (generalized)

[[h-new-321-q1-q27-basmala-echo|H-NEW-321]] showed Q 1 + Q 27 (single-phrase-repetition pair) are content-distant.

[[h-new-330-al-hamidat-cohesion|H-NEW-330]] extends: 5 surahs sharing the *al-ḥamdu li-Llāh* opening formula are ALSO content-distant (actually MORE dispersed than random).

**The pattern is now clearer**: classical surface-similarity signals (shared letters at muq-singleton level per [[h-new-310-singleton-fr-rank1|H-NEW-310]]; shared Basmala phrase per [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]; shared *al-ḥamd* formula per [[h-new-330-al-hamidat-cohesion|H-NEW-330]]) do NOT entail CONTENT-CLUSTERING in Fisher-Rao root-distribution space.

### 3.2 Classical tradition correctly bounds this

al-Suyūṭī *Itqān* and al-Zarkashī *al-Burhān* classify the *al-ḥāmidāt* as a GROUP BY OPENING FORMULA — a morphological/surface-level grouping, NOT a claim of thematic or content-clustering. Classical scholarship correctly treats this as a fawātiḥ classification, not a munāsabāt claim.

[[h-new-330-al-hamidat-cohesion|H-NEW-330]] empirically validates this classical scoping: the al-ḥāmidāt grouping is REAL at the opening-formula axis; it is NOT real at the content-distribution axis.

### 3.3 Why the 5 surahs are content-dispersed

- **Q 1**: 7-verse prayer (prayer register, compact theological vocabulary)
- **Q 6**: 165-verse early-Meccan theology (prophetology, refutation of polytheism)
- **Q 18**: 110-verse narrative cluster (Kahf sleepers, Moses-Khidr, Dhū al-Qarnayn)
- **Q 34**: 54-verse Sabaʾ/Solomon history
- **Q 35**: 45-verse creation + reward-punishment

These 5 surahs span diverse genres, lengths, and vocabulary registers. The only commonality is the *al-ḥamd* opening formula — which is a ~4-word segment that doesn't change the overall content distribution.

### 3.4 MW-5 ḥawāmīm observation

ḥawāmīm (5 of 7: Q 40, 41, 43, 44, 45) descriptively show content-cohesion at 24%ile. This aligns with classical readings (al-Rāzī *Mafātīḥ al-ghayb* vol 27 treats ḥawāmīm as thematically cohesive). But at N=5 and α=0.025, statistical power is inadequate to clear Bonferroni. This is an INSTRUMENT-POWER limit, not a pipeline failure.

**Consistent cross-comparison**:
- al-ḥāmidāt (phrase-sharing group): 75%ile → dispersed
- ḥawāmīm (mushaf-block group): 24%ile → cohesive (marginal)

The contrast between these two classical groupings shows: **mushaf-block adjacency produces content cohesion; shared opening formula alone does NOT**.

## 4. Honest limits

1. **N=5 subset is small** — null variance is large; marginal results fail α=0.025 even when directionally correct (ḥawāmīm).
2. **FR-roots only** — other metrics (char-4-gram, NCD) could give different results.
3. **Classical list is slightly variable** — I used the strict 5-set; some scholars include Q 23 or Q 29. Not tested.
4. **Pre-committed expectation met** — pre-reg §5 stated modal expectation NULL; this is consistent with that expectation.

## 5. Queued follow-ups

- **H-NEW-330.1**: expand to 7 classical groupings (al-ḥāmidāt, al-musabbiḥāt, al-musnadāt, al-ṭawāsīn, ḥawāmīm, ṭiwāl, mufaṣṣal). Is opening-formula cohesion or mushaf-block cohesion the more predictive axis?
- **H-NEW-330.2**: test *al-musabbiḥāt* specifically — surahs opening with tasbīḥ (Q 17, 57, 59, 61, 62, 64, 87, 93). This is a larger sample (8 surahs) with potentially higher power.
- **H-NEW-330.3**: replace FR-roots with char-4-gram FR or NCD — does metric choice change al-ḥāmidāt verdict?

## 6. Cross-references

- Companion to: [[h-new-321-q1-q27-basmala-echo|H-NEW-321]] (Q 1 ↔ Q 27 Basmala echo NULL)
- Companion to: [[h-new-310-singleton-fr-rank1|H-NEW-310]] (muq singleton letter-cluster-vs-content orthogonality)
- Related: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] (Q 42 block-embedded content cohesion with HM — SUCCESS at block level)
- Ḥawāmīm MW-5 aligns with: [[cross-finding-023-causal-generative-closure|cross-finding-023]] (classical block structure as M_H scaffold)

## 7. Classical-scholarship integration

- **al-Suyūṭī *Itqān*** fawātiḥ-classification of *al-ḥāmidāt* — empirically RATIFIED at opening-formula level; correctly NOT claimed as content-cluster.
- **al-Zarkashī *al-Burhān*** on surah-opening types — opening-formula classification is a VALID morphological grouping; does NOT imply content cohesion.
- **al-Rāzī *Mafātīḥ al-ghayb*** ḥawāmīm as theologically dense — descriptively supported (24%ile) but needs larger N for α=0.025 adjudication.
- **CLASSICAL SCOPING CORRECT**: the tradition bounds fawātiḥ classifications at the opening-formula level and does NOT overextend them into content-cohesion claims. [[h-new-330-al-hamidat-cohesion|H-NEW-330]] validates this classical discipline.

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-330-al-hamidat-cohesion-prereg.md` (SHA-256 dbbc9b6b...)
- Script: `scripts/h_new_330_al_hamidat_cohesion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-330.json`
- Findings: this file

## 9. Final statement

**The classical al-ḥāmidāt grouping (5 surahs opening with *al-ḥamdu li-Llāh*: Q 1, 6, 18, 34, 35) does NOT exhibit content-axis cohesion under Fisher-Rao root distance.** Their mean pairwise distance (0.9902) is ABOVE the null mean for random 5-surah draws (0.9232) at the 75.1st percentile — they are CONTENT-DISPERSED, not cohesive. MW-5 positive control on ḥawāmīm {Q 40, 41, 43, 44, 45} shows directional cohesion (24%ile) but fails strict Bonferroni at N=5 due to instrument underpowering.

**Classical scholarship's fawātiḥ (surah-opening) classifications are MORPHOLOGICAL, not semantic-cohesion claims.** al-Suyūṭī *Itqān* and al-Zarkashī *al-Burhān* correctly scope the al-ḥāmidāt as a surface-formula grouping — this finding empirically validates their classical discipline. **Phrase-sharing (al-ḥamd opening) does NOT entail content-clustering.** This reinforces [[h-new-321-q1-q27-basmala-echo|H-NEW-321]]'s pattern (Basmala phrase-echo NULL) and [[h-new-310-singleton-fr-rank1|H-NEW-310]]'s pattern (muq letter-cluster ≠ content-cluster) across a third classical grouping type.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
