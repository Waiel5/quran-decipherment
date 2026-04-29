---
finding_id: h-new-127-8
title: "H-NEW-127.8 phase-aware control for the coarse-prefix OQ-20 omnibus"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "coarse_prefix(sinai_genre), defined as the literal first hyphen-delimited token of sinai_genre from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
phase_axis: "neuwirth_phase from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles coarse-prefix labels only within phase blocks, preserving observed coarse-prefix counts inside each phase; 114 surahs)"
verdict_ceiling: "POSITIVE if the within-phase label-shuffle permutation p for Kruskal-Wallis H is < 0.05; NULL otherwise"
scope_note: "This is a bounded phase-aware control on the already-locked H-NEW-127.4 coarse-prefix omnibus. It does not recompute the compression observable and it does not relabel, pool, or merge phases. The only class construction is the already-locked first-token extraction rule from H-NEW-127.4."
deliverables:
  - scripts/h_new_127_8_oq20_coarse_prefix_phase_control.py
  - findings/phase-b-hypotheses/csv/h-new-127-8.json
  - findings/phase-b-hypotheses/h-new-127-8-coarse-prefix-phase-aware-control.md
  - journal/h-new-127-8-run-1.md
---

# [[h-new-127-8-coarse-prefix-phase-aware-control|H-NEW-127.8]] preregistration

Primary question:

- Does the positive [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] coarse-prefix OQ-20 omnibus survive a
  chronology-aware control once coarse-prefix labels are shuffled only within
  locked `neuwirth_phase` blocks?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score
  already computed in
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`

Primary label axis:

- `coarse_prefix(sinai_genre)`, defined mechanically as the literal first
  hyphen-delimited token of `sinai_genre` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Control axis:

- `neuwirth_phase` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Chosen control design:

- Use the raw locked `z_s` values.
- Compute the same global Kruskal-Wallis `H` across the coarse-prefix classes
  as in [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]].
- Replace the unrestricted label-shuffle null with a stricter null that shuffles
  coarse-prefix labels only within each observed phase block.
- This preserves the observed coarse-prefix counts inside every phase while
  breaking any within-phase coarse-prefix-to-`z_s` association.

Why this control is preferred here:

- It directly conditions on the locked phase structure without introducing an
  extra modeling layer.
- It asks the narrow follow-up implied by [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]]: whether the distributed
  [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] signal still exceeds what phase composition alone can generate.
- It keeps the class axis identical to [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] except for the null
  restriction.

Primary test:

- Kruskal-Wallis `H` across the locked coarse-prefix groups
- Outer null: shuffle coarse-prefix labels only within each `neuwirth_phase`
  block while preserving the observed coarse-prefix counts inside that block
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `H` is
  `< 0.05`

Descriptive reporting:

- Coarse-prefix counts
- Mean and median `z_s` by coarse-prefix class
- Phase-by-coarse-prefix contingency diagnostics
- Count of informative phase blocks, defined as phases containing at least two
  distinct coarse-prefix classes
- Count of surahs inside informative vs frozen phase blocks

Why this is bounded:

- The compression score is not recomputed here; it is read from a locked
  repository artifact.
- The coarse-prefix labels are generated mechanically from a locked TSV field.
- The null is a constrained label-shuffle only, not a refit of the compression
  model or a chronology model.

Interpretive target:

- If the result remains positive under this control, the coarse-prefix OQ-20
  structure survives chronology conditioning.
- If it collapses, the honest read is that the [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] omnibus is at least
  substantially phase-mediated under the locked taxonomy.
