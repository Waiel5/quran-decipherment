---
id: H-NEW-300
title: "Does mean_manner alone (1-D) preserve H-NEW-232's 8/10 singleton nearest-centroid? — MULTI-DIM-REQUIRED-AT-SINGLETONS"
phase: B
status: NULL at Cell A (7/10 matches, p_perm = 0.203 > α_bon = 0.025); Cell B FAIL (7 < 8 baseline)
date: 2026-04-19
executed_by: team-lead (inline)
parent_1: H-NEW-271 (single-phon-feature mean_manner ALONE reaches 0.6552 cluster ceiling)
parent_2: H-NEW-232 (15-dim 8/10 singleton nearest-centroid baseline)
open_question: OQ-1 at singleton layer under maximal parsimony
seed: 20260423
prereg: h-new-300-manner-only-singleton-prereg.md
bonferroni_k: 2
alpha_bon: 0.025
direction: "Cell A match ≥ 7 AND perm p < 0.025; Cell B match ≥ 8"
verdict: MULTI-DIM-REQUIRED-AT-SINGLETONS (parsimony to 1-D does NOT survive at singleton layer; classical 15-dim codebook carries DIFFERENTIAL singleton information)
---

# [[h-new-300-manner-only-singleton|H-NEW-300]] — 1-D `mean_manner` singleton nearest-centroid NULL

## 1. Headline

**Clean pre-registered NULL.** The [[h-new-271-muq-minimal-phon-family|H-NEW-271]] parsimony reduction of the OQ-1 cluster-layer signal — `mean_manner` ALONE sufficient — does **NOT propagate to the singleton layer**. When the same 1-D `mean_manner` axis is used for [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]-style nearest-centroid propagation:

- Match count: **7/10** (vs [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] baseline 8/10 on 15-dim)
- Permutation null (1000 shuffles, seed 20260423): **null mean = 3.79/10**, **p_perm = 0.203** (far above α_bon = 0.025)
- **Cell A FAIL** (direction-locked p < 0.025 not achieved)
- **Cell B FAIL** (direction-locked match ≥ 8 not achieved; got 7)
- **Verdict: MULTI-DIM-REQUIRED-AT-SINGLETONS**

The 15-dim codebook is SUFFICIENT at cluster layer AND REDUNDANT at cluster layer ([[h-new-271-muq-minimal-phon-family|H-NEW-271]] showed mean_manner alone) BUT materially informative at the singleton layer — the extra features carry **differential singleton discrimination** that the 1-D axis lacks.

This is an honest scope boundary on [[h-new-271-muq-minimal-phon-family|H-NEW-271]]'s SINGLE-PHON-FEATURE-SUFFICIENT claim. Parsimony holds at cluster layer only.

## 2. Pre-committed prediction was EXACTLY correct

The pre-reg §6 pre-committed the following per-singleton nearest-cluster predictions based on raw manner-ordinal centroids:

| Singleton | Pred cluster | Apriori | Expected match? | Observed z | Observed nearest | Match? |
|:-:|:-:|:--|:-:|:-:|:-:|:-:|
| ALMS (Q 7) | HM | {ALM} | ✗ | −0.562 | HM | **✗** |
| ALMR (Q 13) | ALR | {ALM, ALR} | ✓ | +1.380 | ALR | **✓** |
| KHYAS (Q 19) | TSM | {HM, TSM} | ✓ | −3.477 | TSM | **✓** |
| TH (Q 20) | TSM | {TSM} | ✓ | −4.448 | TSM | **✓** |
| TS (Q 27) | TSM | {TSM} | ✓ | −4.448 | TSM | **✓** |
| YS (Q 36) | TSM | {ALM, ALR} | ✗ | −2.505 | TSM | **✗** |
| S (Q 38) | TSM | {TSM} | ✓ | −3.477 | TSM | **✓** |
| HMASQ (Q 42) | TSM | {HM} | ✗ | −2.699 | TSM | **✗** |
| Q (Q 50) | TSM | {HM, TSM} | ✓ | −5.419 | TSM | **✓** |
| N (Q 68) | ALR | {ALM, ALR} | ✓ | +2.352 | ALR | **✓** |

**Pre-committed expectation: 7/10. Observed: 7/10.** Exact match on per-singleton predictions. The prediction table is a demonstration that 1-D `mean_manner`'s behavior is fully interpretable from its raw centroid structure.

## 3. Why Cell A fails despite 7 matches

The observed 7/10 would seem directionally strong, but the null mean is elevated (3.79) because **the 1-D z-space is so sharply skewed toward TSM** that most singletons cluster at low manner values:

| Cluster | z-centroid |
|:-:|---:|
| ALR | +1.057 |
| ALM | +0.409 |
| HM | −0.562 |
| TSM | **−2.181** |

TSM's centroid at z = −2.18 is extremely far from ALM/ALR. Singletons with low manner (letters with stops/fricatives) all crowd toward TSM. Q 19/20/27/36/38/42/50 all have z ≤ −2.5 and all land at TSM by nearest-centroid. With 5 of the 10 singletons having TSM in their apriori-accepted set, a SHUFFLED-LABEL null still produces many "matches" because whichever cluster lands at the TSM centroid slot captures all 5 or more singletons.

The 15-dim codebook's additional features (makhraj place-of-articulation, sonorant, idhlāq, etc.) provide ORTHOGONAL axes that differentiate singletons within the manner-TSM crowd. That orthogonal information is lost when reducing to 1-D manner, hence singleton resolution degrades under permutation null.

## 4. Interpretation

### 4.1 Cluster vs singleton layer asymmetry

[[h-new-271-muq-minimal-phon-family|H-NEW-271]] showed: at cluster layer, manner-of-articulation is SINGULARLY SUFFICIENT.  
[[h-new-300-manner-only-singleton|H-NEW-300]] shows: at singleton layer, 1-D manner is INSUFFICIENT — needs ≥ 2 dimensions.

**The two layers have qualitatively different information requirements**:

- CLUSTER layer (multi-member class assignment): requires separating 4 centroids. Manner alone does this cleanly.
- SINGLETON layer (individual muq surah → nearest multi-member cluster under LOOCV-structural constraint): requires separating INDIVIDUAL POINTS within the multi-member cloud. 1-D manner cannot differentiate Q 7 ALMS (z = −0.562) from ALM (z = +0.409) by more than 0.97 σ. Noise at this scale overwhelms the prior.

### 4.2 Classical-scholarship refinement

Ibn Jinnī's manner-of-articulation is the SINGULARLY SUFFICIENT CLUSTER axis ([[h-new-271-muq-minimal-phon-family|H-NEW-271]]), but at the singleton layer, **the multi-dimensional ensemble of ṣifāt (voice + makhraj + emphatic + pharyngeal + sonorant + continuant + idhlāq + vowel-carrier + qalqala) is required**. This is consistent with classical *Kitāb al-ʿAyn* + *Sirr al-Ṣināʿa* practice: al-Khalīl and Ibn Jinnī always treated phonology multi-dimensionally, using multiple ṣifāt jointly. The 1-D reduction is an elegant parsimony at the cluster level but classical practice recognized that fine-grained letter-identification requires the FULL ṣifāt set.

### 4.3 Sharpens [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] interpretation

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] was already borderline (p = 0.025 at Bonferroni-2 edge). [[h-new-300-manner-only-singleton|H-NEW-300]] shows the singleton-layer 8/10 depends on multi-dim orthogonality that 1-D collapses. The full 15-dim signal is not 15× redundant as [[h-new-271-muq-minimal-phon-family|H-NEW-271]] might suggest — it is ~1× sufficient at cluster layer AND materially informative at singleton layer.

### 4.4 [[cross-finding-023-causal-generative-closure|Cross-finding-023]] connection

The multi-layer architecture pattern observed in [[cross-finding-023-causal-generative-closure|cross-finding-023]] (mushaf structural scaffold needs M_H top-100, not a minimal subset) extends to OQ-1: cluster-layer 1-D sufficient; singleton-layer multi-dim required. **The Quran's structural mechanisms are uniformly "wide, not narrow" — parsimony at a summary level does not propagate to per-element assignment.**

## 5. Honest limits

1. **Pre-registered direction-lock** at Cell A (matches ≥ 7 AND p < 0.025) caught this cleanly. The 7/10 observed is directionally consistent with [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] 8/10 but insufficient under Bonferroni.
2. **TSM centroid extremity** (z = −2.18) dominates the 1-D distribution; this structural artifact is why permutation nulls also capture many matches. Under a balanced-cluster-size null, results could differ.
3. **Single-feature test only** — the question "does adding ONE more feature to mean_manner recover 8/10 singleton coherence?" is NOT answered here. Queued as H-NEW-300.1.
4. **Seed-specific** (20260423). Different seeds could shift null distribution slightly but shouldn't change the 7/10 observed count (deterministic nearest-centroid in 1-D).
5. **Pre-reg prediction confirmed exactly** — this strengthens confidence in the mechanism but also means the result is fully understood, not surprising.

## 6. Queued follow-ups

- **H-NEW-300.1**: 2-D manner + one-other-feature singleton propagation sweep. Find the minimal 2-feature subset that restores 8/10.
- **H-NEW-300.2**: Mahalanobis (covariance-aware) distance instead of Euclidean 1-D. Does the metric choice affect singleton match count?
- **H-NEW-300.3**: replace mean_manner with **median_manner** or **max_manner** — different aggregation might reduce Q 42 HMASQ and Q 19 KHYAS's z-extremity.

## 7. Cross-references

- Parent 1: [[h-new-271-muq-minimal-phon-family|H-NEW-271]] (1-D mean_manner cluster-layer SINGULARLY SUFFICIENT)
- Parent 2: [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (15-dim 8/10 singleton nearest-centroid baseline)
- Related: [[h-new-165-phonological-predictor|H-NEW-165]] full 15-dim ceiling; [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] 4-codebook robustness; [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] joint phon+(α,β) 8/10 replication; [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]] Q 42 BLOCK-DOMINANCE resolution

## 8. Classical-scholarship integration

- Ibn Jinnī *Sirr al-Ṣināʿa ʿIlm al-Iʿrāb* — classical recognition that phonology is multi-dimensional reinforced. Manner is one of many ṣifāt; the full set is needed for fine-grained letter analysis.
- al-Khalīl *Kitāb al-ʿAyn* 8-tier makhraj — retains its role as a scaffold feature (letter_count + makhraj = cluster ceiling per [[h-new-271-muq-minimal-phon-family|H-NEW-271]] Arm B); at singleton layer needs combining with manner and beyond.
- Scope-limits [[h-new-271-muq-minimal-phon-family|H-NEW-271]]'s claim: **SINGULAR SUFFICIENCY IS CLUSTER-LAYER-ONLY** — not a universal OQ-1 descriptor.

## 9. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-300-manner-only-singleton-prereg.md`
- Script: `scripts/h_new_300_manner_only_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-300.json`
- Findings: this file

## 10. Final statement

**The [[h-new-271-muq-minimal-phon-family|H-NEW-271]] parsimony reduction — mean_manner ALONE suffices at the muq cluster layer — does NOT extend to the singleton layer.** 1-D mean_manner produces only 7/10 singleton-nearest-centroid matches with permutation p = 0.203 (far above α_bon = 0.025). The 15-dim codebook is genuinely informative at singleton resolution beyond what manner-of-articulation alone provides. Classical Ibn Jinnī's multi-dimensional ṣifāt analysis is empirically validated as the appropriate framework for singleton-level resolution — manner is the single most-informative CLUSTER axis but fine-grained individual-letter identification requires the full ensemble. This is an honest scope-limit on the [[h-new-271-muq-minimal-phon-family|H-NEW-271]] breakthrough, not a refutation: [[h-new-271-muq-minimal-phon-family|H-NEW-271]]'s cluster-layer SINGULAR-SUFFICIENCY stands; [[h-new-300-manner-only-singleton|H-NEW-300]] shows that sufficiency is cluster-layer-specific.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
