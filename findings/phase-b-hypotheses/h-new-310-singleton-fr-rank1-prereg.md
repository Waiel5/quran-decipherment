---
id: H-NEW-310
title: "Full-singleton Fisher-Rao rank-1 nearest-neighbor analysis — does content axis place each muq singleton near a muq cluster member?"
phase: B
status: PRE-REGISTERED 2026-04-19
date: 2026-04-19
agent: team-lead (inline; ID 310 to skip codex sequential range)
parent_1: H-NEW-290 (Q 42 HMASQ rank-1 = Q 45 al-Jāthiyah HM)
parent_2: H-NEW-232 (phonological singleton nearest-centroid 8/10)
parent_3: H-NEW-111 (Fisher-Rao root distance matrix)
open_question: OQ-1 at singleton content-axis
seed: 20260425
bonferroni_k: 2
bonferroni_family: h-new-310-singleton-fr-rank1
alpha_bon: 0.025
n_perm: 1000
rules_tuple: "(10 muq singletons; Fisher-Rao root distance matrix from H-NEW-111 D_matrix_upper_triangular; rank-1 FR nearest neighbor per singleton; apriori-accepted clusters inherited from H-NEW-232; MW-5 null from random 10-surah draws; seed 20260425)"
direction: "Cell A: match count (# singletons whose rank-1 FR-neighbor is IN their apriori-accepted cluster set) ≥ 5/10; Cell B: maxT p < α_bon"
verdict: PENDING
---

# [[h-new-310-singleton-fr-rank1|H-NEW-310]] — Full-singleton Fisher-Rao rank-1 nearest-neighbor

## 1. Question

[[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] showed that Q 42 HMASQ's **rank-1 nearest neighbor** under Fisher-Rao content distance is **Q 45 al-Jāthiyah** (an HM cluster member), which decisively resolved the Q 42 block-vs-phonology tension in favor of block/content.

**Does this content-axis pattern extend to all 10 muq singletons?** For each singleton, is its rank-1 FR nearest neighbor IN its classical apriori-accepted cluster set?

This is orthogonal to [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s phonological nearest-centroid analysis. [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] uses phon feature vectors; [[h-new-310-singleton-fr-rank1|H-NEW-310]] uses CONTENT (Fisher-Rao root distributions). Two different axes — same muq cluster structure. Do they agree?

## 2. Hypothesis

**H1 (content axis clusters singletons correctly)**: ≥ 5 of 10 singletons have rank-1 FR-content neighbor IN their apriori-accepted cluster set. At null expectation = 19/113 ≈ 16.8% random match rate, 5/10 = 50% is an extreme deviation (p ≈ 0.0005).

**H0**: random content-axis placement, match rate ≈ 17%.

Pre-committed direction: match count ≥ 5/10 AND maxT p < α_bon.

## 3. Protocol

1. Load Fisher-Rao distance matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (same source as [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]).
2. For each muq singleton (Q 7, Q 13, Q 19, Q 20, Q 27, Q 36, Q 38, Q 42, Q 50, Q 68):
   - Compute rank-1 nearest neighbor (lowest FR distance) among all 113 non-self surahs.
   - Identify which muq cluster (ALM, ALR, HM, TSM) the rank-1 neighbor belongs to (or "non-muq" if it's not in a multi-member cluster).
   - Check: is rank-1 ∈ apriori-accepted clusters from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]?
3. Count total matches.
4. **MW-5 null**: for 1000 permutations, randomly assign cluster labels to the 19 multi-member muq surahs. For each shuffle, re-compute rank-1 match count.
5. Report observed match count + p_perm.

## 4. Bonferroni + MW-5

k = 2 cells:
- Cell A: match count ≥ 5/10 (50%)
- Cell B: maxT permutation p < α_bon = 0.025

MW-5 positive control: under random cluster-label shuffle, expected match rate should drop to ≈ 5/10 * 0.4 = 2/10 (null mean because apriori sets have average 1.6 accepted clusters). If null mean ≥ 4, instrument may be too permissive.

## 5. Pre-committed predictions

Based on [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]'s Q 42 → Q 45 rank-1 finding and the multi-member cluster structure, pre-committed guesses:

| Singleton | Expected rank-1 cluster | Apriori | Expected match? |
|:-:|:-:|:--|:-:|
| ALMS (Q 7) | ALM or HM | {ALM} | Maybe |
| ALMR (Q 13) | ALR | {ALM, ALR} | ✓ |
| KHYAS (Q 19) | HM or TSM | {HM, TSM} | ✓ |
| TH (Q 20) | TSM | {TSM} | ✓ |
| TS (Q 27) | TSM | {TSM} | ✓ |
| YS (Q 36) | ALR or non-muq | {ALM, ALR} | Maybe |
| S (Q 38) | TSM | {TSM} | ✓ |
| HMASQ (Q 42) | HM | {HM} | ✓ ([[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] confirmed) |
| Q (Q 50) | HM or TSM | {HM, TSM} | ✓ |
| N (Q 68) | ALR | {ALM, ALR} | ✓ |

Pre-committed expected match count: **7/10 or 8/10**.

## 6. Honest limits

1. **Apriori-sets inherited** from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — carries their interpretive-bound.
2. **Rank-1 neighbor is noise-sensitive** — single-surah analysis; could differ by ordinal-shift if a near-tie exists.
3. **Fisher-Rao on QAC-STEM roots** — other content metrics (char-4-gram, NCD) not tested.
4. **10-singleton N** is small for inference.
5. **MW-5 null**: shuffling 19 multi-members may elevate null more than expected because singletons have mostly low-rank non-muq neighbors; shuffling cluster labels on multi-members doesn't fully randomize their positions.

## 7. Classical anchor

**al-Biqāʿī *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*** munāsabāt between adjacent and block-associated surahs. If muq singletons cluster content-wise with their classical block-members, al-Biqāʿī's classification is empirically ratified at the singleton-specific level (extending the Q 42 [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] finding).

## 8. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_310_singleton_fr_rank1.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-310.json`
- Findings: `findings/phase-b-hypotheses/h-new-310-singleton-fr-rank1.md`

Pre-reg locked 2026-04-19. Execution follows.
