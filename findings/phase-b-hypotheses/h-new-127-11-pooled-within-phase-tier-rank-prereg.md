---
finding_id: h-new-127-11
title: "H-NEW-127.11 pooled within-phase rank test for residual Jurjani-tier OQ-20 structure"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-7
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "jurjani_predicted_asyndeton_tier from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
phase_axis: "neuwirth_phase from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; conditioning axis = neuwirth_phase; statistic = sum of within-phase Kruskal-Wallis H values over informative phase blocks only; informative block rule = at least two tier classes present and at least one class count > 1; outer null shuffles tier labels only within each informative phase block, preserving observed counts; 114 surahs)"
verdict_ceiling: "POSITIVE if the within-phase label-shuffle permutation p for the pooled statistic T = sum(H_phase) is < 0.05; NULL otherwise"
scope_note: "This is the tier-axis analogue of H-NEW-127.10. It does not recompute compression scores, does not merge or relabel phases, and does not use global ranks. It asks only whether any Jurjani-tier separation survives once scoring itself is restricted to within-phase rank structure."
deliverables:
  - scripts/h_new_127_11_oq20_pooled_within_phase_tier_rank_test.py
  - findings/phase-b-hypotheses/csv/h-new-127-11.json
  - findings/phase-b-hypotheses/h-new-127-11-pooled-within-phase-tier-rank.md
  - journal/h-new-127-11-run-1.md
---

# [[h-new-127-11-pooled-within-phase-tier-rank|H-NEW-127.11]] preregistration

Primary question:

- After the direct phase backbone in [[h-new-127-9-phase-structure|H-NEW-127.9]], the phase-aware null in
  [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]], and the pooled within-phase collapse of the coarse-prefix
  branch in [[h-new-127-10-pooled-within-phase-rank|H-NEW-127.10]], does any residual Jurjani-tier OQ-20 structure
  survive when the test statistic itself is computed only from within-phase
  rank separation?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score
  already computed in
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`

Primary label axis:

- `jurjani_predicted_asyndeton_tier` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Conditioning axis:

- `neuwirth_phase` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Chosen residual design:

- Partition the 114 surahs by the exact locked `neuwirth_phase` labels.
- Inside each phase block, compute Kruskal-Wallis `H` across the Jurjani-tier
  classes present in that block, using only the observations from that block.
- Define an informative phase block in advance as a phase containing at least
  two distinct tier classes and at least one class with count `> 1`.
- Define the pooled test statistic as
  `T = sum(H_phase)` across informative phase blocks only.
- Generate the null by shuffling tier labels only within each informative
  phase block while preserving the exact observed tier counts inside that
  block; excluded blocks remain fixed and do not contribute to `T`.

Why this design is preferred here:

- [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]] already imposed a phase-aware null, but its omnibus statistic
  still used global ranks on raw `z_s`.
- The current question is narrower: whether there is residual tier separation
  inside phase, not whether a global cross-phase omnibus happens to survive a
  constrained null.
- Summing within-phase `H` values removes the between-phase location ladder
  from the statistic itself and pools only the blocks where tier reassignment
  can meaningfully change a within-phase class comparison.
- A phase-centered global residualization would introduce an avoidable modeling
  layer and still pool blocks with very different within-phase support
  structures.

Excluded-block rule:

- Single-class phase blocks are excluded because they have no within-phase
  class comparison at all.
- Multi-class blocks in which every class is a singleton are also excluded
  because they contribute no meaningful repeated-label structure to the pooled
  within-phase statistic under this design.
- These excluded blocks will still be listed descriptively.

Primary test:

- Statistic: `T = sum(H_phase)` across informative phase blocks
- Outer null: shuffle tier labels only within each informative phase block,
  preserving the observed tier counts inside that block
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `T` is
  `< 0.05`

Descriptive reporting:

- Informative and excluded phase-block diagnostics
- Observed `H_phase` contributions by informative phase
- Pooled null mean and sd for `T`
- Tier counts inside the informative phases

Why this is bounded:

- The compression score is not recomputed here; it is read from a locked
  repository artifact.
- The tier labels are read exactly from a locked TSV field.
- The exact locked phase labels are used as-is.
- The procedure is a constrained label-shuffle only; no chronology model is
  fit and no post hoc phase pooling is introduced.

Interpretive target:

- If the pooled within-phase statistic is positive, then some Jurjani-tier
  structure survives after the direct phase ladder is removed from both the
  null and the scoring rule.
- If it is null, the honest read is that the OQ-20 tier branch has no clean
  residual support on this stricter within-phase rank test either.
