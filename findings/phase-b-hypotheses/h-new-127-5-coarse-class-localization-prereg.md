---
finding_id: h-new-127-5
title: "H-NEW-127.5 coarse-class one-vs-rest localization of locked compression structure"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "coarse_prefix(sinai_genre), defined mechanically as the literal first hyphen-delimited token of the locked sinai_genre field in findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; 18 fixed one-vs-rest coarse-class cells; two-sided localization statistic T_c = |mean(z_s in c) - mean(z_s outside c)|; outer label-shuffle null preserves coarse class counts; familywise maxT correction across all 18 cells; 114 surahs)"
verdict_ceiling: "POSITIVE if at least one coarse class has familywise maxT-adjusted p < 0.05; NULL otherwise"
scope_note: "This is a bounded post-omnibus localization of H-NEW-127.4. The observable and coarse classes are locked from the repository; no manual pooling or relabeling is permitted."
deliverables:
  - scripts/h_new_127_5_oq20_coarse_class_localization.py
  - findings/phase-b-hypotheses/csv/h-new-127-5.json
  - findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization.md
  - journal/h-new-127-5-run-1.md
---

# [[h-new-127-5-coarse-class-localization|H-NEW-127.5]] preregistration

Primary question:

- Which coarse-prefix classes, if any, actually drive the positive [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]]
  omnibus when each coarse class is tested against its complement under a
  familywise-corrected design?

Locked inputs:

- Observable: `z_s = -gzip_z` from
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- Label axis: `coarse_prefix(sinai_genre)` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`, defined as the
  literal first hyphen-delimited token
- Universe: all 114 surahs

Fixed coarse classes:

- The 18 classes are whatever coarse-prefix labels arise mechanically from the
  locked TSV under the above rule. No classes may be merged, dropped, or
  hand-edited after inspection.

Per-class statistic:

- For each coarse class `c`, compute the signed one-vs-rest effect
  `delta_c = mean(z_s | c) - mean(z_s | not c)`
- Primary inferential statistic is two-sided:
  `T_c = |delta_c|`

Direction handling:

- The localization inference is explicitly two-sided.
- Sign is reported descriptively from `delta_c` after inference.
- No one-sided direction is chosen from the observed data.

Null and correction:

- Outer null: shuffle the locked coarse-prefix labels across the 114 surahs
  while preserving the exact observed class counts
- For each permutation, recompute all 18 `T_c` values and the family maximum
  `M = max_c T_c`
- Single-step familywise maxT adjusted p-value for class `c`:
  `p_maxT(c) = (1 + #{perms with M_perm >= T_c_obs}) / (n_perm + 1)`
- Also report classwise permutation p-values descriptively:
  `p_raw(c) = (1 + #{perms with T_c_perm >= T_c_obs}) / (n_perm + 1)`

Decision rule:

- **POSITIVE** iff at least one coarse class has `p_maxT < 0.05`
- **NULL** otherwise

Descriptive reporting:

- Signed class means and complement means
- Signed `delta_c`
- Raw two-sided permutation p-values
- maxT-adjusted familywise p-values
- Ranking of coarse classes by mean `z_s`
- Top positive and top negative coarse classes descriptively

Interpretive target:

- If only a small number of classes survive correction, the [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] omnibus
  is localized to specific coarse classes rather than being uniformly diffuse.
- If none survive, then the coarse-prefix omnibus is real but not cleanly
  attributable to any single coarse class under familywise control.
