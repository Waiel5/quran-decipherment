---
id: H-NEW-252
title: Combined classical-tajwīd phonological + (Zipf α, Heap β) residual predictor for muqaṭṭaʿāt singletons — extension of H-NEW-232
phase: B
status: PRE-REGISTERED 2026-04-18
date: 2026-04-18
agent: team-lead (inline)
parent: H-NEW-232 (8/10 singletons; p=0.025 just inside Bonferroni-2)
grandparent: H-NEW-165 (RF LOOCV ceiling 0.6552); H-NEW-178 (α,β manifold; muq-residual p=0.005)
seed: 20260421
bonferroni_k: 2
bonferroni_family: h-new-252-combined-phon-alphabeta-singleton
alpha_bon: 0.025
n_perm: 1000
rules_tuple: "(H-NEW-165 15-dim classical-tajwīd phonological features from csv/h-new-232.json + (α,β) features from csv/h-new-172-per-surah.csv; 17-dim concatenated joint feature space z-scored across 19 multi-member muq surahs; Euclidean nearest-centroid classifier; MW-5 shuffle-label null n_perm=1000 seed 20260421)"
direction: "Cell A match count observed > null mean with p_perm < α_bon; Cell B specificity — joint predictor should match ≥ H-NEW-232's 8/10 baseline, not worse"
verdict: PENDING
---

# [[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] — Combined classical-tajwīd + (α, β) predictor for muq singletons

## 1. Question

Does augmenting [[h-new-165-phonological-predictor|H-NEW-165]]'s 15-dim classical-tajwīd phonological feature vector with [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s (Zipf α, Heap β) per-surah residual coordinates improve the cross-class nearest-neighbor coherence of [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 10 muqaṭṭaʿāt singleton assignments?

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] achieved 8/10 singletons matching their classical a-priori accepted cluster on the 15-dim phonological feature space alone (p=0.025 just inside Bonferroni-2 α_bon=0.025). The two misses were Q 36 YS → HM (a-priori {ALM, ALR}) and Q 42 HMASQ → TSM (a-priori {HM}).

[[h-new-178-alpha-beta-manifold|H-NEW-178]] found that muqaṭṭaʿāt surahs have systematically HIGHER (α, β) residual at p = 0.005 — a positive non-phonological signal for muq identity. The question is whether ADDING this 2-dim complement to the 15-dim phonological space changes the singleton assignments.

## 2. Hypothesis

**H0 (no improvement):** joint 17-dim nearest-centroid assignment matches ≤ 8/10 singletons to their classical a-priori accepted cluster. The phonological and (α, β) features are orthogonal in a way that does not improve coherence.

**H1 (improvement):** joint 17-dim nearest-centroid assignment matches **≥ 9/10 singletons** to their classical a-priori accepted cluster. The additional (α, β) coordinates disambiguate Q 36 or Q 42 (or both), moving their nearest-cluster onto the classical-accepted set.

**Direction pre-committed**: joint match_count > [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 8/10 baseline AND permutation p < α_bon = 0.025.

## 3. Data sources

- **Phonological features (15-dim)**: `findings/phase-b-hypotheses/csv/h-new-232.json` field `centroids_z` + per-surah raw features reconstructed from the [[h-new-165-phonological-predictor|H-NEW-165]] `feature_names` list:
  `[mean_makhraj, mean_voice, mean_manner, mean_emphatic, mean_pharyngeal, mean_sonorant, mean_continuant, mean_idhlaq, mean_vowel_carrier, letter_count, frac_emphatic, frac_pharyngeal, frac_sonorant, frac_idhlaq, has_qalqala]`
- **(α, β) features (2-dim)**: `findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv` columns `alpha` and `beta_h159`. For the 19 multi-member + 10 singleton muq surahs.

## 4. Protocol

1. Load the raw 15-dim phonological feature vectors for all 29 muq surahs from the [[h-new-165-phonological-predictor|H-NEW-165]] script output (recompute if [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] JSON lacks raw per-surah features).
2. Load (α, β) per-surah from `[[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv` for the same 29 surahs. If any muq surah has `status=insufficient-data` for α (Q 1 al-Fātiḥa is not muq so this should not occur among the 29; verify), drop that surah and report.
3. Concatenate 15 + 2 = **17-dim joint feature vector**.
4. Z-score each dimension using the 19 multi-member surah means and standard deviations (same normalization reference as [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]).
5. Compute multi-member-cluster centroids in the 17-dim z-space.
6. For each of 10 singletons, compute Euclidean distance to each of 4 cluster centroids; report nearest cluster.
7. Count singletons where nearest cluster ∈ classical a-priori accepted set (same apriori_accepted_clusters dict from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]).
8. MW-5 shuffle null: permute cluster labels on the 19 multi-member surahs 1000 times (seed 20260421); re-compute centroids; re-compute match count. Report null mean + permutation p.

## 5. Bonferroni

k = 2 cells (Cell A match count, Cell B specificity vs [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] baseline). α_bon = 0.025.

## 6. MW-5 positive control

The permutation null (shuffling cluster labels) should destroy the nearest-centroid signal. Expected null match rate ≈ 0.30-0.40 given that two classical a-priori sets include multiple clusters (e.g. ALMR, KHYAS, YS, Q, N all have 2 accepted clusters). If null mean ≥ 5/10, the instrument is too permissive and the verdict should be treated as PIPELINE-WEAK.

## 7. Decision rules

| Cell A (match count) | Cell B (vs baseline) | Final verdict |
|---|---|---|
| ≥ 9/10 AND perm p < 0.025 | ≥ 8/10 | **PASS-IMPROVEMENT** |
| = 8/10 AND perm p < 0.025 | = 8/10 | **PASS-RATIFIED** (no improvement but significance preserved) |
| < 8/10 | < 8/10 | **NULL-DEGRADED** (α,β harms phonological signal) |
| otherwise | — | MIXED |

## 8. Interpretation rules (pre-committed)

- **If Q 36 YS now matches {ALM, ALR}**: the α,β axis resolves Y/S as a sonorant-lateral + linear-narrative concentration, re-aligning it with the letter-cluster expectation.
- **If Q 42 HMASQ now matches {HM}**: the α,β axis resolves pharyngeal-emphatic combined with narrative-density to prefer HM.
- **If both match**: 10/10 coherence — the classical tajwīd axis + compositional manifold jointly explain singleton identity, closing OQ-1 singleton layer at full strength.

## 9. Honest limits

1. **Joint feature space is post-hoc motivated**: [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s α,β + [[h-new-165-phonological-predictor|H-NEW-165]]'s phonological were each independently pre-registered, but the COMBINATION is a new feature engineering choice. Report under MW-7 single-test α cap if verdict is marginal.
2. **Small N (10 singletons)**: the decision rule boundary (8/10 vs 9/10) is 10% of the sample. High variance in the 1-2 singleton shifts is expected.
3. **α,β for short surahs**: Q 68 Nūn (52 verses) has small N_lemma; its α estimate may be noisy. Report boot_alpha_hi - boot_alpha_lo interval per singleton.
4. **Euclidean metric**: Mahalanobis would weight by feature covariance; not tested here. Cell A verdict would hold under Euclidean; robustness to metric choice is a sensitivity variant (H-NEW-252.1).
5. **Classical a-priori sets are themselves interpretive**: the assignments {ALMS→ALM, ALMR→{ALM,ALR}, KHYAS→{HM,TSM}, TH→TSM, TS→TSM, YS→{ALM,ALR}, S→TSM, HMASQ→HM, Q→{HM,TSM}, N→{ALM,ALR}} use [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s tajwīd-similarity judgment which has itself a garden-of-forking-paths exposure.

## 10. Classical-scholarship anchors

- **al-Khalīl al-Farāhīdī *Kitāb al-ʿAyn*** — 8-tier makhraj ordinal for all 28 Arabic letters.
- **Ibn Jinnī *Sirr al-Ṣināʿa ʿIlm al-Iʿrāb*** — ṣifāt catalog (emphatic, pharyngeal, sonorant, continuant, idhlāq).
- **al-Suyūṭī *al-Itqān*** — remarks on muqaṭṭaʿāt letters containing the 7 mustaʿliya.
- **Zipf's law** (post-classical but Arabic-applicable) — per-surah Zipf α as structural vocabulary feature.
- **Heaps' law** — per-surah β as vocabulary-growth stratification feature.

## 11. Deliverables

- Pre-reg: this file (SHA-256 will be computed post-lock)
- Script: `scripts/h_new_252_combined_phon_alphabeta.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-252.json`
- Findings: `findings/phase-b-hypotheses/h-new-252-combined-phon-alphabeta-singleton.md`
- Journal: `journal/h-new-252-run-1.md`

Pre-reg locked 2026-04-18. Execution follows immediately.
