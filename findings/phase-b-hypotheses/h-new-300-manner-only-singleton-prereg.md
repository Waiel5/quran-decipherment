---
id: H-NEW-300
title: "Does mean_manner alone (1-D) preserve H-NEW-232's singleton nearest-centroid 8/10? — maximal parsimony test at singleton layer"
phase: B
status: PRE-REGISTERED 2026-04-19
date: 2026-04-19
agent: team-lead (inline; ID 300 chosen to skip codex-sequential-claim range)
parent_1: H-NEW-271 (single-phon-feature mean_manner ALONE reaches 0.6552 cluster ceiling)
parent_2: H-NEW-232 (15-dim nearest-centroid 8/10 singleton match)
open_question: OQ-1 at singleton layer under maximal parsimony
seed: 20260423
bonferroni_k: 2
bonferroni_family: h-new-300-manner-only-singleton
alpha_bon: 0.025
n_perm: 1000
rules_tuple: "(29 canonical muq surahs; single 1-D feature = mean_manner (Ibn Jinnī manner-of-articulation ordinal stop=1/fric=2/glide=3/lateral=4/nasal=5/trill=6 averaged across letter-set); z-scored against 19 multi-member muq surahs; Euclidean nearest-centroid; inherits H-NEW-232 apriori-accepted-clusters verbatim; MW-5 shuffle-label null n_perm=1000 seed 20260423)"
direction: "Cell A match count ≥ 7/10 AND permutation p_arm < α_bon; Cell B specificity match count ≥ H-NEW-232 baseline 8/10"
verdict: PENDING
---

# [[h-new-300-manner-only-singleton|H-NEW-300]] — Maximal parsimony test: `mean_manner` alone at singleton layer

## 1. Question

[[h-new-271-muq-minimal-phon-family|H-NEW-271]] established that a SINGLE classical-tajwīd phonological feature (`mean_manner`) alone reaches the [[h-new-165-phonological-predictor|H-NEW-165]] muq cluster ceiling (RF LOOCV 0.6552, all 4 multi-member classes at 1.0 recall). This is a cluster-level sufficiency claim.

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (and later [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] + [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]) established that the full 15-dim codebook produces 8/10 singletons matching their classical a-priori accepted cluster under nearest-centroid propagation.

**Question**: does the 1-D `mean_manner` feature ALONE also preserve the 8/10 singleton nearest-centroid match, or does singleton-layer coherence specifically require the multi-dim codebook?

If YES (8/10 preserved at 1-D): Ibn Jinnī's manner-of-articulation is **SINGULARLY SUFFICIENT at BOTH cluster AND singleton layers** — the deepest parsimony reduction possible for OQ-1.

If NO (<8/10 at 1-D): singleton coherence is a genuinely MULTI-DIMENSIONAL phenomenon even though cluster-layer is 1-D sufficient.

## 2. Hypothesis

**H1 (parsimony persists to singletons)**: 1-D `mean_manner` produces ≥ 7/10 singleton-match (within 1 singleton of the 15-dim 8/10 baseline). Cell A PASS.

**H0 (multi-dim needed at singletons)**: 1-D `mean_manner` produces < 7/10 match — singleton coherence degrades when dimensionality collapses.

Direction-committed: 1-D match count ≥ 7/10 AND permutation p < α_bon = 0.025.

## 3. Protocol

1. Compute [[h-new-165-phonological-predictor|H-NEW-165]] classical-tajwīd feature vector for all 29 muq surahs (reuse logic from [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]]/290 script).
2. Extract ONLY `mean_manner` (feature index 2 in the 15-dim vector) → 1-D per-surah score.
3. Z-score across 19 multi-member surahs only (same normalization reference as [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]).
4. Compute 4 multi-member-cluster centroids in 1-D mean_manner z-space (scalar means).
5. For each of 10 singletons, compute |singleton_z − centroid_z| distance to each of 4 cluster centroids; report nearest cluster.
6. Count matches against [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] apriori_accepted_clusters (verbatim).
7. MW-5: shuffle cluster labels on 19 multi-members 1000 times (seed 20260423); re-compute centroids; re-compute match count.

## 4. Bonferroni + MW-5

k = 2 cells:
- Cell A: match count ≥ 7/10 AND perm p < 0.025
- Cell B: specificity match count ≥ 8 (equals [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] baseline)

MW-5 positive control: shuffled-label null should produce ≈ 3-4/10 matches (given 4-cluster assignment with average 1.6 accepted clusters per singleton).

## 5. Decision rules

| Cell A (≥7 matches AND p<0.025) | Cell B (≥8 matches) | Verdict |
|---|---|---|
| PASS | PASS | **MAXIMAL-PARSIMONY-SINGULARLY-SUFFICIENT** |
| PASS | FAIL (7/10) | **PASS-ROBUST-WITH-1-SINGLETON-LOSS** |
| FAIL | — | **MULTI-DIM-REQUIRED-AT-SINGLETONS** |

## 6. Predictions per singleton (pre-committed descriptive expectations)

Based on the [[h-new-271-muq-minimal-phon-family|H-NEW-271]] cluster centroids in 1-D manner-ordinal space (ALM=4.0, ALR=4.33, HM=3.5, TSM=2.67), each singleton's manner value determines nearest cluster directly. I pre-commit my expectation HERE before running:

| Singleton | Letters | Predicted manner mean | Predicted cluster | Apriori accepted | Expected match? |
|:-:|:--|:-:|:-:|:--|:-:|
| ALMS (Q 7) | ا,ل,م,ص | (3+4+5+2)/4 = 3.5 | HM | {ALM} | ✗ |
| ALMR (Q 13) | ا,ل,م,ر | (3+4+5+6)/4 = 4.5 | ALR | {ALM, ALR} | ✓ |
| KHYAS (Q 19) | ك,ه,ي,ع,ص | (1+2+3+2+2)/5 = 2.0 | TSM | {HM, TSM} | ✓ |
| TH (Q 20) | ط,ه | (1+2)/2 = 1.5 | TSM | {TSM} | ✓ |
| TS (Q 27) | ط,س | (1+2)/2 = 1.5 | TSM | {TSM} | ✓ |
| YS (Q 36) | ي,س | (3+2)/2 = 2.5 | TSM | {ALM, ALR} | ✗ |
| S (Q 38) | ص | 2 | TSM | {TSM} | ✓ |
| HMASQ (Q 42) | ح,م,ع,س,ق | (2+5+2+2+1)/5 = 2.4 | TSM | {HM} | ✗ |
| Q (Q 50) | ق | 1 | TSM | {HM, TSM} | ✓ |
| N (Q 68) | ن | 5 | ALM | {ALM, ALR} | ✓ |

**Pre-committed expected match count: 7/10** (Cell A boundary — 3 predicted misses: Q 7 ALMS, Q 36 YS, Q 42 HMASQ).

If the prediction holds, verdict is **PASS-ROBUST-WITH-1-SINGLETON-LOSS** ([[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] had 8 matches; [[h-new-271-muq-minimal-phon-family|H-NEW-271]] 1-D predicts 7). This would be a small degradation but still strong — manner-of-articulation ALONE maintains 70% singleton coherence.

## 7. Honest limits

1. **Pre-committed prediction table is based on simple manner-ordinal mean** — RF might not exactly match this nearest-centroid judgment if data z-scores differ from predicted means.
2. **Z-scoring compresses/expands the 1-D axis** — actual nearest-cluster depends on z-scored distance, not raw mean.
3. **Singleton-layer 10 N**: single-singleton shift = 10% of sample. 7 vs 8 is a borderline distinction.
4. **Shared loss with [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]**: Q 36 YS and Q 42 HMASQ (already "misses" at 15-dim) likely remain misses at 1-D. Q 7 ALMS is a NEW predicted loss specific to 1-D reduction.
5. **Single seed** — no cross-seed sensitivity at singleton layer.
6. **Classical apriori sets inherited** — same interpretive-bound limits as [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]].

## 8. Classical anchor

Ibn Jinnī *Sirr al-Ṣināʿa ʿIlm al-Iʿrāb* vol 1 section on manner-of-articulation: stop/fricative/glide/lateral/nasal/trill as a primary ṣifa. This is the classical tradition's single most-informative phonological coordinate per [[h-new-271-muq-minimal-phon-family|H-NEW-271]].

## 9. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_300_manner_only_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-300.json`
- Findings: `findings/phase-b-hypotheses/h-new-300-manner-only-singleton.md`
- Journal: not written (inline)

Pre-reg locked 2026-04-19. Execution follows immediately.
