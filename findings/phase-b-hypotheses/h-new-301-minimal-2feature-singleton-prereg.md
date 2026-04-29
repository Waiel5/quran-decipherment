---
id: H-NEW-301
title: "Minimal 2-feature subset that restores 8/10 singleton nearest-centroid (completing the OQ-1 parsimony picture)"
phase: B
status: PRE-REGISTERED 2026-04-19
date: 2026-04-19
agent: team-lead (inline; ID 301 chosen to skip codex-sequential range)
parent_1: H-NEW-271 (cluster-layer 1-D sufficient: mean_manner alone)
parent_2: H-NEW-300 (singleton-layer 1-D FAILS: 7/10 at p=0.20)
parent_3: H-NEW-232 (15-dim baseline: 8/10 at p≈0.025)
open_question: OQ-1 at singleton parsimony
seed: 20260424
bonferroni_k: 2
bonferroni_family: h-new-301-minimal-2feature-singleton
alpha_bon: 0.025
n_perm: 1000
rules_tuple: "(29 canonical muq surahs; 10 distinct phonological-axis pool from H-NEW-271 plus letter_count = 11 features total; all C(11,2)=55 pairs; z-scored per-feature against 19 multi-members; Euclidean nearest-centroid; inherits H-NEW-232 apriori-accepted-clusters verbatim; maxT permutation null within 55-pair search family; seed 20260424)"
direction: "Cell A: at least ONE 2-feature pair achieves match count ≥ 8; Cell B: maxT p < α_bon"
verdict: PENDING
---

# [[h-new-301-minimal-2feature-singleton|H-NEW-301]] — Minimal 2-feature subset for singleton 8/10 match

## 1. Question

[[h-new-271-muq-minimal-phon-family|H-NEW-271]] established 1-D sufficiency at CLUSTER layer.
[[h-new-300-manner-only-singleton|H-NEW-300]] established 1-D INSUFFICIENCY at SINGLETON layer (7/10, p=0.20).
[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] established 15-dim baseline 8/10 at singleton layer.

**What is the MINIMAL feature set for 8/10 singleton match?** Is it 2-D? 3-D? Or does only the full 15-dim codebook achieve 8/10?

This is the natural completion of the OQ-1 parsimony picture. Two-feature search is the smallest non-trivial next step.

## 2. Hypothesis

**H1 (2-D suffices)**: at least one pair of features achieves 8/10 singleton match under nearest-centroid. Cell A PASS.

**H0 (2-D insufficient)**: no 2-feature pair reaches 8/10 — singleton resolution requires 3+ dimensions.

## 3. Protocol

1. Feature pool = 10 deduplicated phonological axes from [[h-new-271-muq-minimal-phon-family|H-NEW-271]] + letter_count scaffold = **11 total**:
   - mean_makhraj, mean_voice, mean_manner, mean_emphatic, mean_pharyngeal, mean_sonorant, mean_continuant, mean_idhlaq, mean_vowel_carrier, has_qalqala, letter_count
2. Enumerate all C(11, 2) = **55 pairs**.
3. For each pair: z-score each dimension against 19 multi-members; Euclidean nearest-centroid distance in 2-D; count singleton matches against [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] apriori-accepted-clusters.
4. **maxT permutation null**: shuffle cluster labels on 19 multi-members 1000 times (seed 20260424); for each shuffle, compute max-match-over-55-pairs; observed max vs null max distribution.
5. Arm-wise p = (1 + #perms with max_null ≥ max_obs) / (n_perm + 1).

## 4. Bonferroni + MW-5

k = 2 cells:
- Cell A: at least one pair achieves 8+ matches
- Cell B: maxT permutation p < α_bon = 0.025

MW-5 positive control: the synthetic 15-dim baseline must reproduce [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 8/10 (already verified in [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]/165.2 replications; inherited).

## 5. Decision rules

| Cell A | Cell B | Verdict |
|---|---|---|
| PASS (≥1 pair 8+) | PASS (p<0.025) | **MINIMAL-2D-SUFFICIENT** |
| PASS | FAIL | **MARGINAL** (pair exists but permutation-suggestive) |
| FAIL | — | **MULTI-DIM-GT-2-REQUIRED** |

## 6. Pre-committed predictions

Given [[h-new-300-manner-only-singleton|H-NEW-300]]'s finding that 1-D manner saturates at 7/10 with Q 7 ALMS, Q 36 YS, Q 42 HMASQ as misses, the 2-D expansion should help by adding an ORTHOGONAL axis that differentiates these 3 misses.

Predicted strong candidates:
- `mean_manner + mean_makhraj` — adds place-of-articulation orthogonal to manner
- `mean_manner + letter_count` — adds cardinality scaffold
- `mean_makhraj + letter_count` — from [[h-new-271-muq-minimal-phon-family|H-NEW-271]] Arm B cluster-level winner

Predicted match count: 8-9/10 from at least one of these pairs. If NONE reaches 8/10, then singleton layer requires ≥3 dimensions.

## 7. Honest limits

1. Only 55 pairs tested — 3+-feature subsets NOT searched in this finding.
2. Pool of 11 features inherited from [[h-new-271-muq-minimal-phon-family|H-NEW-271]]/165 — alternative feature families not tested.
3. 10-singleton N is small — 7 vs 8 is a single-singleton distinction.
4. maxT permutation null is search-corrected within the 55-pair family but NOT across alternative classifier choices (RF, logistic, etc.).
5. Classical apriori sets inherited from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — same interpretive-bound.

## 8. Classical anchor

Ibn Jinnī's multi-dimensional ṣifāt framework: this test identifies which TWO ṣifāt are collectively sufficient for singleton resolution. If 2-D suffices, the classical practice of using multiple ṣifāt jointly is empirically justified at minimum rank 2.

## 9. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_301_minimal_2feature_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-301.json`
- Findings: `findings/phase-b-hypotheses/h-new-301-minimal-2feature-singleton.md`

Pre-reg locked 2026-04-19. Execution follows.
