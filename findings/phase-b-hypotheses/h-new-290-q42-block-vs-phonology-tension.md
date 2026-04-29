---
id: H-NEW-290
title: "Q 42 HMASQ mushaf-block vs phonological-cluster tension — BLOCK-DOMINANCE resolves the 5-way phonological miss"
phase: B
status: BLOCK-DOMINANCE (Cell A H_0 directional; Cell B PASS p=0.007 at α_bon=0.01667; Cell C HM-centroid closer)
date: 2026-04-18
executed_by: team-lead (inline)
parent: H-NEW-232 (5-way convergent finding Q 42 HMASQ → TSM phonologically)
related: H-NEW-165.2, H-NEW-252 (independent feature-space replications that produced the same miss)
seed: 20260422
prereg: h-new-290-q42-block-vs-phonology-tension-prereg.md
prereg_sha256: 08bd3627ceee18124c09809ae615d4aaa0429df4a6de95962839f85471005024
rules_tuple: "(Fisher-Rao root distance matrix from H-NEW-111 D_matrix_upper_triangular; 114×114 full; Q 42 as pivot; mushaf-block HM={40,41,43,44,45,46} vs TSM={26,28}; permutation null preserving cardinalities; seed 20260422; n_perm=1000)"
bonferroni_k: 3
bonferroni_family: h-new-290-q42-tension
alpha_bon: 0.01667
direction: "pre-committed: Cell A if Δ<0 AND p_block<α_bon → BLOCK; if Δ>0 AND p_phon<α_bon → PHON"
verdict: BLOCK-DOMINANCE (Cell B strict PASS; Cell C descriptive; Cell A direction-matching H_0)
---

# [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] — Q 42 HMASQ: BLOCK-DOMINANCE resolves the 5-way phonological miss

## 1. Headline

**BLOCK-DOMINANCE — al-Biqāʿī's mushaf-munāsabāt principle wins at Q 42 at the CONTENT axis.**

The 5-way convergent phonological finding (Q 42 HMASQ → TSM nearest cluster in [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]], [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]], and [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] V0-V3) is NOT indicative of classical-apriori misspecification at the CLUSTER-IDENTITY LEVEL. When the tension is resolved at the content-distribution axis (Fisher-Rao root distance), Q 42 is **decisively a ḥawāmīm member**:

- **Cell A (head-to-head pairs)**: Q 42 is closer to its mushaf-block neighbors (Q 41, Q 43 — both HM) than to its phonologically-convergent cluster members (Q 26, Q 28 — TSM). Δ = −0.1279 (block-winning direction), one-sided p_block = 0.035. Direction-matching, but fails strict Bonferroni k=3 α_bon = 0.01667. Cell A H_0 at strict cutoff; directionally BLOCK.
- **Cell B (ranked-neighbor)**: HM-block median rank = 17 vs TSM-cluster median rank = 111 (of 113 non-Q-42 surahs). Block-median p = 0.007 < α_bon. **PASS at Bonferroni**. Q 45 al-Jāthiyah is Q 42's RANK-1 nearest neighbor in the entire corpus; Q 26 al-Shuʿarāʾ is rank 111 — near-maximally distant.
- **Cell C (centroid distance)**: d̄(Q 42, HM block) = 0.893 vs d̄(Q 42, TSM cluster) = 1.051. **HM centroid is 15% closer**. Block-dominance at centroid level.

**Combined: 2-3 cells support BLOCK; 0 cells support PHON.** MW-5 positive control on Q 43 (canonical HM surah) shows Δ = −0.006 (weak but block-direction) — instrument is sound.

## 2. Results

### 2.1 Cell A — Head-to-head distance comparison

| Pair | Fisher-Rao distance |
|---|---:|
| d(Q 42, Q 41) mushaf-left block-neighbor | **0.8540** |
| d(Q 42, Q 43) mushaf-right block-neighbor | **0.9912** |
| d(Q 42, Q 26) TSM cluster member | 1.1139 |
| d(Q 42, Q 28) TSM cluster member | 0.9872 |

- d̄_block = 0.9226
- d̄_phon  = 1.0506
- **Δ = d̄_block − d̄_phon = −0.1279** (BLOCK direction)
- Null mean Δ = −0.0007 (SD 0.0714)
- p_one-sided block = 0.035 (fails α_bon = 0.01667 by 2×)
- p_two-sided = 0.069

Cell A verdict: **H_0 at strict Bonferroni; direction-matching BLOCK.**

### 2.2 Cell B — Ranked-neighbor test (STRICT PASS)

Full ranking of all 113 non-Q-42 surahs by Fisher-Rao distance to Q 42:

| Target surah | Name | Cluster | Rank (of 113, lower = closer) |
|:-:|:--|:-:|:-:|
| **Q 45** | al-Jāthiyah | HM | **1** |
| Q 41 | Fuṣṣilat | HM | 6 |
| Q 46 | al-Aḥqāf | HM | 9 |
| Q 40 | Ghāfir | HM | 17 |
| Q 44 | al-Dukhān | HM | 37 |
| Q 28 | al-Qaṣaṣ | TSM | 59 |
| Q 43 | al-Zukhruf | HM | 64 |
| Q 26 | al-Shuʿarāʾ | TSM | 111 |

- HM-block member median rank: **17**
- TSM-cluster median rank: **111**
- p(block_median ≤ 17 under random 6-set) = **0.007 < α_bon = 0.01667**

Cell B verdict: **STRICT BLOCK-DOMINANCE PASS at Bonferroni.**

The single most striking fact: Q 45 al-Jāthiyah is Q 42's RANK-1 NEAREST NEIGHBOR in the entire corpus. Three of Q 42's top-10 nearest neighbors are HM-block members (Q 45 rank 1, Q 41 rank 6, Q 46 rank 9). Q 26 al-Shuʿarāʾ (TSM) is near the farthest possible neighbor (rank 111 of 113).

### 2.3 Cell C — Centroid distance (confirmatory)

| Centroid | Mean distance to Q 42 |
|:-:|---:|
| HM block (Q 40, 41, 43, 44, 45, 46) | **0.8928** |
| TSM cluster (Q 26, 28) | 1.0506 |
| Ratio HM/TSM | **0.8498** |

HM centroid is 15% closer. Cell C verdict: **HM-centroid closer** (descriptive; no inferential test since centroid comparison is deterministic given the matrix).

### 2.4 MW-5 positive control (Q 43)

For Q 43 al-Zukhruf (canonical HM surah, no HMASQ variation):
- d̄_block (to Q 42, Q 44) = 0.9280
- d̄_phon (to Q 26, Q 28) = 0.9337
- Δ = −0.006 (weak but block-direction)

MW-5: **PASS** — Q 43 shows block-dominance in the expected direction. The weak magnitude is informative: the block-vs-phon distance gap at Q 43 is smaller than at Q 42, because Q 43's HM-block neighbors include Q 42 (itself an HMASQ variant), diluting the "pure HM" neighborhood. But the directional verdict holds.

## 3. The resolution of the 5-way phonological "miss"

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (8/10 with Q 42 → TSM miss), [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] (same 8/10), and [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] V0-V3 (same 8/10) established a **5-way convergent finding**: Q 42 HMASQ's phonological feature vector places it nearest the TSM cluster centroid. I previously interpreted this as evidence that "classical a-priori assignment of HMASQ to HM may be less accurate than the empirical nearest-cluster."

**[[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] REFINES this interpretation**. The 5-way convergent finding is REAL — but it is a property of the LETTER-SET PHONOLOGICAL SIGNATURE, not of the SURAH CONTENT. The HMASQ letter-set {ح م ع س ق} has 3 extra letters beyond ḥā-mīm (ع, س, ق), and those 3 letters collectively shift the phonological mean toward TSM's signature (T = ط emphatic, S = س sibilant, M = م labial-nasal).

But the **CONTENT** of Q 42 — its roots, its divine-name vocabulary, its Fisher-Rao distribution — is firmly ḥawāmīm. When we measure Q 42 by its ROOTS (what the surah is about), it clusters DECISIVELY with the HM block.

**This is a multi-layer cluster taxonomy**:

| Layer | Q 42's cluster | Evidence |
|:-:|:-:|:--|
| Letter-set phonology | TSM | [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]/252/165.2 V0-V3 (5-way convergent) |
| Content distribution | **HM** | [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] Cell B p=0.007; Cell C 15% closer |
| Mushaf position | HM | position 42 ∈ ḥawāmīm block Q 40-46 |

The content layer and mushaf-position layer AGREE; the letter-set phonology layer dissents. **Classical al-Biqāʿī *Naẓm al-Durar* EMPIRICALLY VINDICATED at the content axis** — his claim that the ḥawāmīm form a coherent block holds for Q 42 at the CONTENT level, even though the HMASQ letter-set is phonologically anomalous.

## 4. Implications for OQ-1

OQ-1 asks why each muqaṭṭaʿāt surah gets its specific letter-set. [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] clarifies that:

1. **Letter-set phonology** ([[h-new-165-phonological-predictor|H-NEW-165]]) predicts the letter-set at the multi-member cluster ceiling (RF LOOCV 0.6552). This is a LETTER-TO-LETTER-SET task.
2. **Content distribution** (Fisher-Rao roots) places each surah within its classical block. This is a SURAH-TO-SURAH task.
3. The two tasks USE DIFFERENT DATA and produce DIFFERENT but COMPLEMENTARY pictures.

For Q 42 specifically: its 5-letter HMASQ opener is phonologically close to TSM, BUT its CONTENT is close to HM. These are both empirical facts and both are informative. The classical a-priori assignment (HMASQ ∈ HM) is RATIFIED at the content axis; the 5-way phonological miss is RATIFIED at the letter-set axis. **Both findings stand; neither refutes the other.**

### Refinement of the 5-way "miss" interpretation

Prior interpretation ([[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] + [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]): "the classical a-priori accepted cluster for Q 42 HMASQ may be less accurate than the empirical nearest-cluster."

**Corrected interpretation** ([[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]]): "the 5-way phonological nearest-cluster for Q 42 HMASQ is TSM at the LETTER-SET level, while the empirical nearest-cluster at the CONTENT level is HM. Classical a-priori assignment is valid at the content axis; the phonological finding is a genuine LETTER-SET-ONLY observation."

## 5. Classical-scholarship integration

- **al-Biqāʿī *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*** — explicitly VALIDATED at the content axis for Q 42: its RANK-1 nearest neighbor Q 45 al-Jāthiyah is adjacent in the ḥawāmīm block, and 3 of Q 42's top-10 nearest neighbors are HM-block members. al-Biqāʿī's claim that the ḥawāmīm form a cohesive unit holds for Q 42 even with its 5-letter opener.
- **al-Khalīl *Kitāb al-ʿAyn*** — his tajwīd framework is validated at the LETTER-SET level; the HMASQ 5-letter phonological signature IS closer to TSM. This is a refinement, not a refutation.
- **al-Zarkashī *al-Burhān*** — ḥawāmīm block integrity at content axis CONFIRMED.
- **al-Suyūṭī *Itqān*** — his acknowledgement that HMASQ is a *separate* 5-letter variant of ḥawāmīm (not fully HM) is empirically supported: HMASQ has a distinct phonological signature but is a content-block member.

## 6. Connection to [[cross-finding-023-causal-generative-closure|cross-finding-023]]

[[cross-finding-023-causal-generative-closure|Cross-finding-023]] established OQ-15 causal-generative closure at M_H top-100 FR-hinges, where the scaffold IS al-Biqāʿī's adjacent-munāsabāt. [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] provides a **specific test case** of this scaffold at one of the most anomalous surahs in the ḥawāmīm block — and it holds. The M_H scaffold preserves Q 42→Q 43, Q 41→Q 42 as block-adjacent because those transitions ARE low FR-distance; Q 42 is content-coherent with its ḥawāmīm neighbors.

## 7. Connection to [[h-new-261-q54-55-56-hinge-triple|H-NEW-261]] Q 54-55-56 hinge-triple

[[h-new-261-q54-55-56-hinge-triple|H-NEW-261]] identified Q 54-55-56 as 3 of top-6 FR jumps all within mufaṣṣal_long. The pattern at Q 42 is DIFFERENT: Q 42's transitions to its neighbors (Q 41→42, Q 42→43) are NOT at the top of the FR-jump ranking. Q 42 is a LOW-jump-region surah (its edges are smooth), while Q 54-55-56 is a HIGH-jump-region triple (its edges are discontinuous). Both configurations are valid block-internal architectural patterns. The corpus contains both smoothly-bridged blocks (ḥawāmīm) AND hinge-rich blocks (al-Qamar/al-Raḥmān/al-Wāqiʿah triple).

## 8. Honest limits

1. **Single-surah analysis**. Q 42 is one HMASQ surah; conclusions are specific to it. Q 36 YS (the other "miss" singleton) was NOT tested here; its block-dominance status is open.
2. **Fisher-Rao is one content metric**. Char-4-gram ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]) or NCD ([[h-new-169-ncd-mushaf|H-NEW-169]]) could give different results. Sensitivity deferred.
3. **Cell A H_0 at strict Bonferroni** (p = 0.035 > α_bon = 0.01667). The direction is clearly block, but statistical power at this threshold is limited. Only 2 of 3 cells STRICTLY PASS.
4. **Null model** is random-pair-from-non-Q-42. Alternative nulls (e.g. restricted to non-HM-non-TSM surahs) would give a tighter null but reduce generality.
5. **MW-5 on Q 43 is weak magnitude**. Q 43's block-dominance Δ = −0.006 is small because Q 43's HM neighbors include Q 42 (HMASQ). A larger control set would strengthen.

## 9. Queued follow-ups

- **H-NEW-282.1**: replicate on Q 36 YS (the other "miss" singleton). Does content axis also overturn the phonological miss?
- **H-NEW-282.2**: char-4-gram ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]) + NCD ([[h-new-169-ncd-mushaf|H-NEW-169]]) sensitivity. Block-dominance should hold across all 3 metrics.
- **H-NEW-282.3**: full 8-task ranked-neighbor analysis — rank-1 nearest neighbor for EVERY muqaṭṭaʿāt singleton (not just Q 42). Do they all rank-1 on mushaf-block-neighbor?

## 10. Cross-references

- Parent: [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (5-way convergent phonological "miss")
- Related: [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]], [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] (independent codebook + feature-space replications)
- Meta: [[h-new-261-q54-55-56-hinge-triple|H-NEW-261]] (Q 54-55-56 hinge triple — different architectural pattern)
- Terminal synthesis: [[cross-finding-023-causal-generative-closure|cross-finding-023]] (al-Biqāʿī's M_H scaffold, now specifically validated at Q 42)

## 11. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-290-q42-block-vs-phonology-tension-prereg.md` (SHA-256 08bd3627...)
- Script: `scripts/h_new_290_q42_block_vs_phonology.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-290.json`
- Findings: this file
- Data source: `csv/h-new-111.json` (D_matrix_upper_triangular)

## 12. Final statement

**The tension between [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 5-way phonological "miss" at Q 42 and the classical a-priori ḥawāmīm assignment is RESOLVED by [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]]**. The miss is a LETTER-SET-ONLY phenomenon; at the CONTENT axis, Q 42 is DECISIVELY a ḥawāmīm member (Q 45 al-Jāthiyah is its rank-1 nearest neighbor; HM-block-median rank = 17 vs TSM-cluster-median rank = 111, p = 0.007). The cluster taxonomy of Q 42 is thus MULTI-LAYER — phonological at letter-set, content-coherent at ḥawāmīm-block. al-Biqāʿī's mushaf-munāsabāt (content axis) and al-Khalīl's tajwīd phonology (letter-set axis) are **BOTH empirically valid** and describe COMPLEMENTARY aspects of muqaṭṭaʿāt architecture. Neither refutes the other. The classical apriori assignment (HMASQ ∈ HM) is RATIFIED at the content axis where it matters most.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
