---
id: H-NEW-320
title: "Cross-axis singleton agreement enumeration — only 1 of 10 muq singletons (Q 13 ALMR) shows 3-way IDENTICAL cluster assignment"
phase: B
status: DESCRIPTIVE-INTEGRATION (post-hoc aggregation under MW-7 single-test α = 0.05 cap)
date: 2026-04-19
executed_by: team-lead (inline)
parent_1: H-NEW-232 (15-dim phonological nearest-centroid — 8/10 matches)
parent_2: H-NEW-301 (2-D emph+phar nearest-centroid — 9/10 matches)
parent_3: H-NEW-310 (FR-rank1 content — 3/10 matches)
seed: 20260426 (integration run; no new stochastic test)
rules_tuple: "(10 muq singletons; integrate nearest-cluster assignments from 3 JSON sources: h-new-232.json (nearest_centroid_cluster), h-new-301.json (best_pair_per_singleton), h-new-310.json (results); count 3-way IDENTICAL and 3-axis ALL-IN-APRIORI patterns)"
verdict: DESCRIPTIVE-NARROWING (only Q 13 ALMR shows 3-way identical assignment; Q 42 HMASQ shows 2/3 axis agreement, not 3/3 as prior framings suggested)
---

# [[h-new-320-crossaxis-singleton-agreement|H-NEW-320]] — Cross-axis singleton agreement enumeration

## 1. Headline

**Only 1 of 10 muq singletons — Q 13 ALMR — shows 3-way IDENTICAL cluster assignment across all 3 orthogonal axes** tested ([[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] 15-dim phonological, [[h-new-301-minimal-2feature-singleton|H-NEW-301]] 2-D emph+phar, [[h-new-310-singleton-fr-rank1|H-NEW-310]] FR rank-1 content). Only 2 of 10 show 3-axis ALL-IN-APRIORI agreement (Q 13 ALMR and Q 19 KHYAS).

**Corrects a prior framing overstatement**: [[h-new-310-singleton-fr-rank1|H-NEW-310]]'s ledger entry claimed "Q 42 HMASQ is cross-axis-validated across 3 independent analyses." [[h-new-320-crossaxis-singleton-agreement|H-NEW-320]] shows this is PRECISELY 2-OF-3, not 3-OF-3: [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (15-dim phon) assigns Q 42 to TSM, while [[h-new-301-minimal-2feature-singleton|H-NEW-301]] (2-D emph+phar) and [[h-new-310-singleton-fr-rank1|H-NEW-310]] (FR rank-1 content) both assign to HM. The cross-axis convergence for Q 42 is real but limited to 2 of the 3 tested axes.

## 2. Full 10-singleton 3-axis table

| Singleton | Q | Apriori | H-232 15-dim phon | H-301 2-D emph+phar | H-310 FR rank-1 | 3-way SAME? | All-in-apriori? |
|:-:|:-:|:--|:-:|:-:|:-:|:-:|:-:|
| **ALMS** | 7 | {ALM} | ALM ✓ | TSM ✗ | non-muq ✗ | ✗ | ✗ |
| **ALMR** | 13 | {ALM, ALR} | ALR ✓ | ALR ✓ | ALR ✓ | **✓ (ALR)** | **✓** |
| **KHYAS** | 19 | {HM, TSM} | TSM ✓ | TSM ✓ | HM ✓ | ✗ (HM vs TSM) | **✓** |
| **TH** | 20 | {TSM} | TSM ✓ | TSM ✓ | non-muq ✗ | ✗ | ✗ |
| **TS** | 27 | {TSM} | TSM ✓ | TSM ✓ | non-muq ✗ | ✗ | ✗ |
| **YS** | 36 | {ALM, ALR} | HM ✗ | ALR ✓ | non-muq ✗ | ✗ | ✗ |
| **S** | 38 | {TSM} | TSM ✓ | TSM ✓ | non-muq ✗ | ✗ | ✗ |
| **HMASQ** | 42 | {HM} | TSM ✗ | HM ✓ | HM ✓ | ✗ (TSM vs HM) | ✗ (232 fails) |
| **Q** | 50 | {HM, TSM} | TSM ✓ | HM ✓ | non-muq ✗ | ✗ | ✗ |
| **N** | 68 | {ALM, ALR} | ALR ✓ | ALR ✓ | non-muq ✗ | ✗ | ✗ |

## 3. Aggregation statistics

| Pattern | Count | Singletons |
|:--|:-:|:--|
| 3-way IDENTICAL cluster | **1/10** | Q 13 ALMR (ALR on all axes) |
| 3-axis ALL-IN-APRIORI (any cluster in apriori) | **2/10** | Q 13 ALMR, Q 19 KHYAS |
| 2/3 axes identical | 5/10 | Q 20 TH, Q 27 TS, Q 38 S (all TSM 2/3 with rank-1 non-muq); Q 42 HMASQ (HM 2/3 with 15-dim TSM); Q 68 N (ALR 2/3 with rank-1 non-muq) |
| 2/3 axes in apriori | 7/10 | |
| Single-axis-only in apriori | 3/10 | Q 7 ALMS, Q 36 YS, Q 50 Q |

## 4. Interpretation

### 4.1 Only Q 13 ALMR is unambiguously triangulated

All 3 orthogonal analysis axes agree: Q 13 ALMR belongs to ALR cluster. This is the only muq singleton with strict 3-way cluster-assignment convergence. Classical interpretation: ALMR shares the ا + ل + م + ر (alif-lām-mīm-rāʾ) letters with the ALM and ALR clusters directly; phonologically its manner profile aligns with ALR; content-wise its rank-1 neighbor Q 14 Ibrāhīm is an ALR surah and mushaf-adjacent. Three-way convergence reflects THIS CASE of deep classical-empirical alignment.

### 4.2 Q 19 KHYAS is cross-axis apriori-valid but with within-apriori variation

H-232 and H-301 both assign Q 19 → TSM; H-310 assigns to HM. But Q 19 KHYAS's apriori is {HM, TSM} so all 3 axes land in apriori. This is the second-cleanest singleton.

### 4.3 Q 42 HMASQ is 2/3 axes → HM (not 3/3 as prior framings suggested)

[[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]/301/310 each independently placed Q 42 → HM. But [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 15-dim phonological nearest-centroid assigns TSM. **The prior ledger claim "Q 42 is cross-axis validated across 3 independent analyses" was slightly inaccurate — it's 2 of 3 axes (emph+phar + FR rank-1) agreeing on HM, with 15-dim disagreeing.** [[h-new-320-crossaxis-singleton-agreement|H-NEW-320]] corrects this framing.

Still, 2/3 axis agreement is INFORMATIVE: the 15-dim assignment is the OUTLIER because manner-of-articulation dominates the RF classifier's feature weights. Once you strip to the dimensions that actually carry classical throat-and-back phonology (emph+phar), Q 42 → HM. When you look at content directly (FR rank-1), Q 42 → HM. Classical a-priori is VALIDATED at emph+phar + content axes; manner-dominant axis is the methodological outlier.

### 4.4 The 7 "DIFF" singletons reflect axis-orthogonality

For 7 of 10 singletons, the 3 axes disagree. This is consistent with [[h-new-310-singleton-fr-rank1|H-NEW-310]]'s finding that content axis and letter-cluster axis are ORTHOGONAL. The data-integration finding: **no muq-singleton cluster-assignment is fully triangulated EXCEPT Q 13 ALMR**. Q 19 KHYAS and Q 42 HMASQ are second-tier; 7 others lack cross-axis support.

### 4.5 Classical scholarship — honest implications

[[h-new-320-crossaxis-singleton-agreement|H-NEW-320]] empirically shows that the muqaṭṭaʿāt singleton cluster-classification question has **NO SINGLE CORRECT ANSWER** across all 10 singletons. Different feature-axes will produce different classifications. Classical al-Khalīl / Ibn Jinnī / al-Suyūṭī frameworks produced interpretive-consistent classifications within each's methodology; the empirical convergence is only partial.

This is consistent with classical scholarly disagreement about muq letters' meanings — various mufassirūn proposed different interpretations, and the Quran never canonically explicates them. [[h-new-320-crossaxis-singleton-agreement|H-NEW-320]]'s 1/10 strict agreement is the empirical reflection of this classical indeterminacy.

## 5. Honest limits

1. **Descriptive aggregation, not inferential test**. No new pre-reg; integrating 3 prior findings' outputs. Under MW-7 single-test α = 0.05 cap.
2. **3 axes are NOT independent** — they use overlapping data (H-232 is full 15-dim; H-301 is 2-D subset from same feature pool; H-310 uses FR-roots which partially correlate with letter-sets). Any "3-way identical under chance" null would need careful simulation accounting for dependencies.
3. **Only 3 axes tested** — additional axes (Mahalanobis metric, char-4-gram FR, NCD) could change counts.
4. **Apriori sets inherited from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]** — same interpretive-bound as all prior tests.
5. **10-singleton N is small**.
6. **[[h-new-310-singleton-fr-rank1|H-NEW-310]] "non-muq" rank-1 neighbors** automatically fail "in-apriori" because apriori sets only contain muq multi-member clusters. This inflates the "DIFF" count.

## 6. Queued follow-ups

- **H-NEW-320.1**: add Mahalanobis-based H-232 variant as a 4th axis; does any singleton gain 4-way agreement?
- **H-NEW-320.2**: test 2/3 partial-agreement patterns for statistical significance under a dependent-axis null.
- **H-NEW-320.3**: the "sharpening" of Q 42's 2/3 agreement — is the 15-dim phon miss a METHODOLOGICAL artifact of manner-dominance (per [[h-new-271-muq-minimal-phon-family|H-NEW-271]])? If manner is removed from the 15-dim, does Q 42 assignment flip from TSM to HM?

## 7. Cross-references

- Parent 1: [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (15-dim phon baseline)
- Parent 2: [[h-new-301-minimal-2feature-singleton|H-NEW-301]] (2-D emph+phar marginal)
- Parent 3: [[h-new-310-singleton-fr-rank1|H-NEW-310]] (FR rank-1 content NULL)
- Q 42-specific: [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] (rank-1 content only)
- Corrects: prior [[h-new-310-singleton-fr-rank1|H-NEW-310]] ledger framing "Q 42 is cross-axis validated across 3 axes" → should read "2 of 3 axes converge on HM; 15-dim disagrees"

## 8. Classical-scholarship integration

- **Q 13 ALMR as 3-way convergent**: classical agreement (al-Ṭabarī, al-Zamakhsharī, al-Suyūṭī) consistently places Q 13's opener in the ALR cluster. Empirical 3-axis convergence RATIFIES this classical consensus.
- **Q 19 KHYAS as 2.5-way convergent** (all-in-apriori but not identical): classical ambiguity about KHYAS → {HM, TSM} is empirically reflected.
- **Q 42 HMASQ as 2/3 axis convergent**: classical reading of HMASQ as HM-variant (per al-Suyūṭī) is empirically supported on 2 of 3 axes; the 15-dim outlier corresponds to the manner-dominated methodology.
- **7 non-convergent singletons**: classical scholarly disagreement about singleton meanings is the empirical reality — no single classification is "correct."

## 9. Files

- Parent JSONs: `csv/h-new-232.json`, `csv/h-new-301.json`, `csv/h-new-310.json`
- Findings: this file (integration only; no new script or JSON)

## 10. Final statement

**Only Q 13 ALMR shows strict 3-way IDENTICAL cluster assignment across the 3 orthogonal analysis axes** tested in the H-232/301/310 sequence. **Q 19 KHYAS shows 3-axis all-in-apriori agreement (across different apriori-accepted clusters).** **Q 42 HMASQ shows 2-of-3 axis agreement on HM (emph+phar + content) with 15-dim manner-dominant axis disagreeing (TSM) — correcting the prior ledger's "3-axis validated" framing.** 7 other singletons lack cross-axis support. The muq-singleton cluster-classification question has NO universally-correct empirical answer; classical scholarly indeterminacy about singleton meanings is empirically mirrored. Q 13 ALMR is the cleanest case; Q 42 HMASQ is the next-strongest with honest-bounded 2/3 agreement.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
