---
finding_id: h-new-127-3
title: "H-NEW-127.3 class-mapping of locked per-surah compression z-scores"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-2
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "sinai_genre from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = sinai_genre; Kruskal-Wallis H; outer null permutes genre labels across surahs preserving class counts; 114 surahs)"
verdict_ceiling: "POSITIVE if the label-shuffle permutation p for Kruskal-Wallis H is < 0.05; NULL otherwise"
scope_note: "This is a full 114-surah class-mapping test on an already-locked compression observable. It does not rerun the expensive within-surah OQ-20 path search, and it does not pool or relabel sparse genre categories."
deliverables:
  - scripts/h_new_127_3_oq20_class_mapping.py
  - findings/phase-b-hypotheses/csv/h-new-127-3.json
  - findings/phase-b-hypotheses/h-new-127-3-compression-class-mapping.md
  - journal/h-new-127-3-run-1.md
---

# [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] preregistration

Primary question:

- Do the locked Neuwirth/Sinai genre labels stratify the repository-locked per-surah compression scores?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score already computed in `csv/compression_self_ref_results.json`

Primary test:

- Kruskal-Wallis `H` across `sinai_genre` groups
- Outer null: shuffle genre labels across the 114 surahs while preserving the observed class counts
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `H` is `< 0.05`

Why this is bounded:

- The score is not recomputed here; it is read from a locked repository artifact.
- The label axis is fixed before the run.
- The null is label-shuffle only, not a re-estimation of the compression model.

Why `sinai_genre`:

- It is the direct genre column in the locked Neuwirth-Sinai TSV.
- I am not pooling sparse labels, because that would change the class structure after seeing the data.
- The exact locked taxonomy is therefore used as-is, even though some labels are singletons and the test is low-power in that respect.

