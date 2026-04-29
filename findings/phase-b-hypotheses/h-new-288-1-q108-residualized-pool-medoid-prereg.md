---
finding_id: h-new-288-1
title: "H-NEW-288.1 Q108 residualized-pool medoid test"
specialist: codex
parent_finding: h-new-288
audit_backdrop: h-new-273 / h-new-284 / h-new-288
date_prereg: 2026-04-19
seed: 20260419
alpha: descriptive-bounded
k_top: 500
metrics_primary:
  - fisher_rao
  - jensen_shannon
  - euclidean_l2
  - cosine_angle
metric_diagnostic:
  - total_variation
pool_rule: "P = {surahs with noldeke_phase = Early Meccan and verse_count <= 17}"
rules_tuple: "(114 surahs; QAC v0.4 STEM roots; K=500 top roots; literal family = count/N_i plus flat alpha=0.5; residualized family = raw counts plus alpha_i = 0.5 * mean_tokens / N_i; fixed pool P defined from revelation-order.csv and hafs-verse-counts.tsv only; mean pairwise distance medoid ranks computed inside P; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; total variation diagnostic only)"
verdict_ceiling: "POOL-MEDOID-SEPARATION if C_res >= 3 and Delta_med >= 10; otherwise NO-CLEAN-POOL-MEDOID-SEPARATION"
scope_note: "This is the mechanistic follow-up after H-NEW-288. It does not ask another generic normalization-family question. It asks whether residualized smoothing makes Q108 the geometric medoid of a fixed short Early-Meccan pool."
deliverables:
  - scripts/h_new_288_1_q108_residualized_pool_medoid.py
  - findings/phase-b-hypotheses/csv/h-new-288-1.json
  - findings/phase-b-hypotheses/h-new-288-1-q108-residualized-pool-medoid.md
  - journal/h-new-288-1-run-1.md
---

# [[h-new-288-1-q108-residualized-pool-medoid|H-NEW-288.1]] preregistration

Primary question:

- After [[h-new-288-normalization-family-adjudication|H-NEW-288]] established that the surviving Q108 hub belongs
  specifically to the residualized smoothing family, what is the simplest
  local-geometry mechanism that explains that survival?

Sharp hypothesis:

- Under the residualized family, Q108 is not merely "less penalized by
  length." It becomes the **geometric medoid** of a fixed short
  Early-Meccan pool.
- Under the literal family, the same pool should not center on Q108.

Locked pool:

- `P = {surahs with noldeke_phase = Early Meccan and verse_count <= 17}`
- `noldeke_phase` comes from `data/revelation-order.csv`
- verse count comes from `data/hafs-verse-counts.tsv`
- the pool is fixed before looking at any MST edges or [[h-new-288-normalization-family-adjudication|H-NEW-288]] neighbor
  lists

Why this pool:

- It captures the short Early-Meccan cloud into which Q108 plausibly falls
  under residualized smoothing without defining the pool from the result we are
  trying to explain.
- It is narrower and more mechanistic than another whole-corpus MST rerun.

Families compared:

- **Literal family**: `count / N_i`, then flat `alpha = 0.5`
- **Residualized family**: raw counts plus
  `alpha_i = 0.5 * mean_tokens / N_i`

Primary metrics:

- Fisher-Rao
- Jensen-Shannon
- Euclidean L2
- Cosine-angle

Diagnostic-only metric:

- Total variation

Primary statistic:

- For each family `F`, primary metric `m`, and surah `s in P`, define
  `dbar_F,m(s) = mean_{t in P, t != s} d_F,m(s,t)`
- Rank surahs in `P` by ascending `dbar_F,m(s)`; rank `1` is the medoid
- Let `R_F,m(Q108)` be the medoid-rank of Q108
- Let `C_res = #{m : R_res,m(Q108) = 1}`
- Let `Delta_med = median_m [R_lit,m(Q108) - R_res,m(Q108)]`

Decision rule:

- **POOL-MEDOID-SEPARATION** iff
  `C_res >= 3` and `Delta_med >= 10`
- otherwise **NO-CLEAN-POOL-MEDOID-SEPARATION**

Descriptive reporting:

- exact pool membership
- Q108 medoid rank by metric under both families
- top-5 medoids in each family / metric
- diagnostic total-variation ranks

Why this is bounded:

- pool is fixed from chronology and verse-count metadata only
- family definitions are inherited verbatim from [[h-new-288-normalization-family-adjudication|H-NEW-288]]
- no new null model is invented
- total variation is explicitly demoted to diagnostic because [[h-new-284-length-residualized-metric-robustness-mst|H-NEW-284]]
  and [[h-new-288-normalization-family-adjudication|H-NEW-288]] already established it as the one dissenter

Interpretive target:

- If Q108 is rank-1 across most primary metrics only under the
  residualized family, then the mechanism is local geometric centering
  inside a fixed short Early-Meccan cloud, not merely a family-label
  artifact.
- If not, [[h-new-288-normalization-family-adjudication|H-NEW-288]] remains a family split without a clean local medoid
  explanation.
