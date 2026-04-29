---
finding_id: h-new-127-9
title: "H-NEW-127.9 direct phase-structure test for locked per-surah compression z-scores"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-8
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "neuwirth_phase from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = neuwirth_phase; Kruskal-Wallis H; outer null permutes phase labels across surahs preserving class counts; 114 surahs)"
verdict_ceiling: "POSITIVE if the label-shuffle permutation p for Kruskal-Wallis H is < 0.05; NULL otherwise"
scope_note: "This is a direct full-corpus phase test on the already-locked OQ-20 compression observable. It does not rerun the expensive within-surah OQ-20 path search, and it does not pool or collapse disputed phase labels."
deliverables:
  - scripts/h_new_127_9_oq20_phase_structure.py
  - findings/phase-b-hypotheses/csv/h-new-127-9.json
  - findings/phase-b-hypotheses/h-new-127-9-phase-structure.md
  - journal/h-new-127-9-run-1.md
---

# [[h-new-127-9-phase-structure|H-NEW-127.9]] preregistration

Primary question:

- Does the exact locked `neuwirth_phase` field directly stratify the repository-locked per-surah OQ-20 compression scores?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score already computed in `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`

Primary test:

- Kruskal-Wallis `H` across `neuwirth_phase` groups
- Outer null: shuffle phase labels across the 114 surahs while preserving the observed phase counts
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `H` is `< 0.05`

Why this is bounded:

- The compression score is not recomputed here; it is read from a locked repository artifact.
- The label axis is fixed before the run.
- The null is label-shuffle only, not a re-estimation of the compression model.

Why `neuwirth_phase`:

- [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]] and [[h-new-127-8-coarse-prefix-phase-aware-control|H-NEW-127.8]] already indicate that phase composition mediates later genre-tier projections.
- This follow-up therefore asks the direct question rather than another mediated one: whether the raw OQ-20 observable is itself phase-structured.
- The exact locked phase labels are used as-is, including sparse disputed singleton labels, because post hoc pooling would change the class system after seeing the data.
