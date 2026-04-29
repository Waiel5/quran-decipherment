---
id: H-NEW-232
title: OQ-1 singleton nearest-neighbor placement — phonological interpretation of 10 singleton letter-sets
phase: B
status: prereg
date: 2026-04-17
agent: h-new-232-autonomous
parent: H-NEW-165
open_question: OQ-1 (why does each muq surah get its specific letter-set?) — singleton branch
seed: 20260419
rules_tuple: "(no-tashkeel; canonical 14 distinct letter-sets; hafs-kufan; H-NEW-165 locked 15-dim classical tajwīd feature codebook; Euclidean distance in z-scored feature space; seed 20260419)"
bonferroni_k: 2
bonferroni_family: h-new-232-oq1-singleton
alpha_bon: 0.025
direction: "coherence (pre-committed) — for each of the 10 singleton letter-sets, the RF-predicted nearest multi-member cluster under H-NEW-165 phonological geometry SHOULD match the a-priori classical-tajwīd profile listed in §Interpretation-rules below; ≥ 7 of 10 singletons matching → PASS-COHERENT"
verdict: PENDING
---

# [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — OQ-1 singleton nearest-neighbor placement (phonological interpretation of 10 singleton letter-sets)

## Classical / project anchor

[[h-new-165-phonological-predictor|H-NEW-165]] established that the 4 multi-member muq letter-set clusters (ALM, ALR, HM, TSM) are perfectly phonologically separable under a 15-dim classical-tajwīd feature vector (RF LOOCV top-1 = 0.6552 = multi-member structural ceiling). The 10 singleton classes (ALMS, ALMR, KHYAS, TH, TS, YS, S, HMASQ, Q, N) are STRUCTURALLY LOOCV-UNREACHABLE: only 1 sample per class, absent from training fold. This finding parks OQ-1 at "cluster-level solved, singleton-level open."

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] RE-FRAMES the singleton problem. Instead of LOOCV classification (impossible by construction), we ask: **in the same phonological feature space that perfectly recovers the 4 multi-member clusters, where does each singleton sit?** For each singleton, compute:
1. its distance to each of 19 multi-member-cluster surahs,
2. its distance to each of the 4 cluster centroids,
3. the resulting nearest-cluster assignment.

If the classical-tajwīd phonological space captures real compositional structure of muq-letter selection, then singletons — whose letter-sets share ṣifāt with multi-member-cluster letter-sets — should sit NEAREST the cluster whose phonological profile they share. The claim is **interpretive**, not inferential: there is no external ground-truth label for "which cluster should Q 50 ق belong to?" beyond the classical-tajwīd a-priori analysis.

Classical anchors:
- al-Khalīl al-Farāhīdī *Kitāb al-ʿAyn* (8-tier makhraj from pharyngeal to labial).
- Ibn Jinnī *Sirr Ṣināʿat al-Iʿrāb* I.46ff. (ṣifāt catalogue).
- al-Suyūṭī *al-Itqān fī ʿUlūm al-Qurʾān* III §36: the 14 muq letters contain ALL 7 ḥurūf mustaʿliya.

## Hypothesis (pre-registered)

**H1 (primary)**: In the [[h-new-165-phonological-predictor|H-NEW-165]] 15-dim z-scored phonological feature space, for each of the 10 singleton letter-sets, the nearest of the 4 multi-member cluster centroids matches the pre-committed classical-tajwīd profile match in §Interpretation rules at a rate ≥ 7 / 10 (70%). This is operationalized as PASS-COHERENT.

**H2 (secondary)**: MW-5 cheat control — shuffling the surah→letter-set label mapping and recomputing nearest-cluster-centroid assignments produces a random/incoherent pattern (matching-rate ≤ 3 / 10 under shuffled labels, empirically verified via 1000-permutation null).

## Feature set (LOCKED — inherited verbatim from [[h-new-165-phonological-predictor|H-NEW-165]])

- 15-dim feature vector per surah:
  - 9 per-letter means over its letter-set: makhraj (al-Khalīl 8-tier ordinal), voice (jahr/hams), manner (stop/fricative/glide/lateral/nasal/trill), emphatic (tafkhīm), pharyngeal (mustaʿliya ∪ pharyngeals), sonorant, continuant, idhlāq, vowel_carrier.
  - 1 letter_count.
  - 4 fractions: frac_emphatic, frac_pharyngeal, frac_sonorant, frac_idhlāq.
  - 1 has_qalqala indicator.
- Feature codebook LOCKED per `scripts/h_new_165_phonological_predictor.py` — NO new features, NO re-codings.
- Per-surah feature vector is letter-set-intrinsic (no surah-text-derived information; no leakage).

## Distance metric (LOCKED — chosen before execution)

- **Euclidean distance on z-scored features** (z-scoring uses the 19 multi-member-cluster surahs as the reference sample; singletons are projected into the SAME z-space without contributing to its scaling).
- Rationale for choosing Euclidean over Mahalanobis or cosine:
  - Mahalanobis requires invertible feature-covariance; with 19 training samples and 15 features, Σ is singular or near-singular → unreliable.
  - Cosine discards magnitude differences that are meaningful for ordinal makhraj and fractional measures.
  - Euclidean on z-scored features is the standard classical nearest-neighbor metric, matches the L2 implicit in the RF proximity used by [[h-new-165-phonological-predictor|H-NEW-165]].
- Declared BEFORE execution. No post-hoc metric switching.

## Dependent variables

For each of the 10 singletons (Q 7 ALMS, Q 13 ALMR, Q 19 KHYAS, Q 20 TH, Q 27 TS, Q 36 YS, Q 38 S, Q 42 HMASQ, Q 50 Q, Q 68 N), report:
1. `nearest_multi_member_surah` — the single closest of the 19 multi-member surahs.
2. `nearest_cluster_by_surah` — cluster label of above.
3. `nearest_cluster_by_centroid` — closest of 4 cluster centroids computed over the 19 multi-member surahs.
4. `distances_to_4_centroids` — full distance vector to {ALM, ALR, HM, TSM} centroids.
5. `coherence_match` — 1 if nearest_cluster_by_centroid == pre-committed classical-tajwīd cluster (see §Interpretation rules); 0 otherwise.

## Interpretation rules (pre-committed classical-tajwīd profile match)

**Written BEFORE executing the script. Based ONLY on al-Khalīl / Ibn Jinnī / al-Suyūṭī classical phonological analysis of each singleton letter-set.**

| Singleton | Letters | Classical-tajwīd profile | A-priori expected nearest cluster | Reasoning |
|---|---|---|---|---|
| Q 7 ALMS | ا, ل, م, ص | sonorant-heavy + 1 emphatic alveolar | **ALM** | ALMS = ALM ∪ {ص}; shares ا, ل, م verbatim; dominant profile matches ALM |
| Q 13 ALMR | ا, ل, م, ر | fully sonorant | **ALM** or **ALR** | ALMR = ALM ∪ {ر} = ALR ∪ {م}; both are valid a-priori — tie-break accepted |
| Q 19 KHYAS | ك, ه, ي, ع, ص | mixed: pharyngeal ع + emphatic ص + sonorant ي + glottal ه + velar ك | **HM** (pharyngeal) OR **TSM** (emphatic/alveolar) | pharyngeal + emphatic profile matches HM (ح pharyngeal) + TSM (ط emphatic); either accepted |
| Q 20 TH | ط, ه | emphatic alveolar stop + glottal fricative | **TSM** | ط anchors TH exactly as ط anchors TSM; strong a-priori match |
| Q 27 TS | ط, س | emphatic alveolar stop + alveolar fricative | **TSM** | TS = TSM ∖ {م}; near-verbatim subset, strongest a-priori match |
| Q 36 YS | ي, س | sonorant palatal glide + alveolar fricative | **ALR** or **ALM** | sonorant+alveolar profile matches sonorant-heavy clusters; either ALR or ALM accepted |
| Q 38 S | ص | single emphatic alveolar fricative | **TSM** | ص clusters with ط (TSM-anchor) — both emphatic alveolar fricatives/stops |
| Q 42 HMASQ | ح, م, ع, س, ق | pharyngeal-heavy (ح, ع) + emphatic-uvular (ق) + labial-nasal (م) + alveolar (س) | **HM** | HMASQ = HM ∪ {ع, س, ق}; shares ح, م verbatim; dominant profile matches HM |
| Q 50 Q | ق | single emphatic uvular stop | **HM** (pharyngeal) OR **TSM** (emphatic) | ق shares emphatic ṣifa with ط (TSM) and pharyngeal ṣifa with ح (HM); either accepted |
| Q 68 N | ن | single alveolar nasal sonorant | **ALM** or **ALR** | ن is pure sonorant-idhlāq; profile matches ALM (م sonorant-idhlāq) or ALR (ر sonorant-idhlāq); either accepted |

**Pass bar**: ≥ 7 of 10 singletons match one of the a-priori accepted clusters.

## Procedure (locked)

1. Build 29 × 15 phonological feature matrix per [[h-new-165-phonological-predictor|H-NEW-165]] codebook.
2. Split into 19 multi-member rows (training/reference for z-scoring + centroids) and 10 singleton rows (query).
3. Z-score features using multi-member-only mean + SD.
4. Compute 4 cluster centroids in z-space.
5. For each singleton: compute Euclidean distance to all 19 multi-member surahs + to all 4 centroids; record nearest.
6. Evaluate coherence_match per singleton against §Interpretation rules.
7. **MW-5 cheat control**: shuffle letter-set labels across the 19 multi-member surahs 1000× (seed 20260419). For each shuffle, recompute centroids and singleton-nearest assignments; count matching-rate. Pre-committed: matching-rate distribution should concentrate well below 0.70.
8. Report all metrics BEFORE committing verdict.

## Verdict decision rule (locked, pre-committed)

- **PASS-COHERENT**: ≥ 7 of 10 singleton nearest-cluster assignments match a-priori classical-tajwīd profile AND MW-5 shuffled-label matching-rate p < 0.025.
- **PASS-WEAK**: 5–6 of 10 singletons match AND shuffled p < 0.05.
- **NULL**: ≤ 4 of 10 match OR shuffled-p ≥ 0.05 — phonological nearest-neighbor is random; singleton selection is NOT phonologically coherent at the classical-tajwīd-profile level.

## Bonferroni

- `bonferroni_k = 2` (primary: coherence matching-rate; secondary: MW-5 shuffled-label null)
- `alpha_bon = 0.025`
- `bonferroni_family = [[h-new-232-oq1-singleton-nearest-neighbor|h-new-232]]-oq1-singleton`

## Garden-of-forking-paths log

1. **Distance metric locked** to Euclidean on z-scored features BEFORE running. No switching to Mahalanobis/cosine if Euclidean gives null.
2. **z-scoring reference sample** locked to the 19 multi-member surahs only (prevents singletons from influencing the scale against which they are compared). Not swapped post-hoc to the full 29.
3. **Coherence-matching criterion** pre-committed in the table above BEFORE any computation. The "accepted clusters" column was written from classical al-Khalīl/Ibn Jinnī reasoning only.
4. **Tie-allowances** (Q 13, Q 19, Q 36, Q 50, Q 68 — 5 of 10 singletons have ≥ 2 a-priori accepted clusters): these widen the pass bar, reported transparently. The pre-committed pass bar (≥ 7 of 10) requires genuinely good matches beyond the tie-allowances.
5. **MW-5 null uses 1000 shuffles** at seed 20260419 locked.
6. **No post-hoc re-specification** of which singleton maps to which cluster.
7. **Interpretive-not-decisive disclosure**: even on PASS-COHERENT this remains interpretive — there is no external ground-truth singleton-cluster assignment to validate against beyond classical phonological reasoning.
8. **Singleton-singleton distances are NOT used** in the verdict (only singleton → multi-member-cluster distances). Reporting them descriptively is allowed, but they do not influence the verdict.

## Expected outcome (pre-committed)

Based on the [[h-new-165-phonological-predictor|H-NEW-165]] findings document (which noted the RF-misassignment pattern for singletons is internally coherent: Q 19 KHYAS ↔ Q 42 HMASQ, Q 20 TH ↔ Q 27 TS, Q 38 S ↔ Q 50 Q), I expect moderate-to-strong coherence: 6–9 of 10 singletons matching. A NULL (≤ 4 matching) would be genuinely surprising and would downgrade the [[h-new-165-phonological-predictor|H-NEW-165]] interpretation.

## Honest limits (MANDATORY)

- **No external ground truth**. This is an INTERPRETIVE test: we cannot say "Q 50 Q SHOULD classically be assigned to HM" — only that IF it is, it is phonologically coherent. A pass signals that classical-tajwīd phonology is a consistent framework for singleton-letter-set selection, not that it is THE unique selection rule.
- **Small sample (10 singletons)**: the ≥ 7/10 bar is a reasonably strong signal but not a population test.
- **Tie-allowances soften the pass bar**: 5 of 10 singletons are a-priori-compatible with 2 clusters; tie-breaks are logged as partial matches.
- **Euclidean in z-scored 15-D is one of many possible distances**; sensitivity analysis (Mahalanobis, cosine) is deferred to a future H-NEW-232.1 if primary passes.
- **Phonological-codebook sensitivity** (already flagged in [[h-new-165-phonological-predictor|H-NEW-165]] honest-limits) propagates here.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_232_oq1_singleton.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-232.json`
- Findings: `findings/phase-b-hypotheses/h-new-232-oq1-singleton-nearest-neighbor.md`
- Journal: `journal/h-new-232-run-1.md`

## Cross-references

- Parent: [[h-new-165-phonological-predictor|H-NEW-165]] (multi-member cluster phonological predictor, PASS-PRIMARY top-1 0.6552)
- OQ-1 singleton branch; queues H-NEW-232.1 (distance-metric sensitivity) if primary passes
- Classical anchors: al-Khalīl *Kitāb al-ʿAyn*, Ibn Jinnī *Sirr al-Ṣināʿa*, al-Suyūṭī *Itqān* III §36
