---
finding_id: h-new-127-4
title: "H-NEW-127.4 coarse-prefix localization of locked per-surah compression class structure"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-3
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "coarse_prefix(sinai_genre), defined mechanically as the literal first hyphen-delimited token of the locked sinai_genre field in findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; Kruskal-Wallis H; outer null permutes coarse labels across surahs preserving coarse class counts; 114 surahs)"
verdict_ceiling: "POSITIVE if the label-shuffle permutation p for Kruskal-Wallis H is < 0.05; NULL otherwise"
scope_note: "This is a bounded localization rerun of H-NEW-127.3 on the same locked observable. The only change is a mechanical coarsening of the genre axis; no relabeling beyond first-token extraction is permitted."
deliverables:
  - scripts/h_new_127_4_oq20_coarse_prefix_localization.py
  - findings/phase-b-hypotheses/csv/h-new-127-4.json
  - findings/phase-b-hypotheses/h-new-127-4-coarse-prefix-localization.md
  - journal/h-new-127-4-run-1.md
---

# [[h-new-127-4-coarse-prefix-localization|H-NEW-127.4]] preregistration

Primary question:

- Does the positive [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] OQ-20 class-mapping result survive a purely mechanical compression of the locked `sinai_genre` taxonomy down to first-token coarse classes?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score already computed in `csv/compression_self_ref_results.json`

Primary label axis:

- `coarse_prefix(sinai_genre)`
- Definition: split the locked `sinai_genre` string on hyphens and take the literal first token
- Examples under the file's spelling: `narrative-qaṣaṣ -> narrative`, `oath-sworn-eschatological -> oath`, `scripture-reflective -> scripture`
- If a label has no hyphen, the whole label is its coarse class

Primary test:

- Kruskal-Wallis `H` across coarse-prefix classes
- Outer null: shuffle coarse-prefix labels across the 114 surahs while preserving the observed coarse class counts
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `H` is `< 0.05`

Descriptive reporting:

- Coarse class counts
- Mean and median `z_s` by coarse class

Why this is bounded:

- The compression score is not recomputed here; it is read from the same locked repository artifact used in [[h-new-127-3-compression-class-mapping|H-NEW-127.3]].
- The coarsening rule is fully mechanical and fixed before the run.
- The null is label-shuffle only, not a re-estimation of the compression model.

Interpretive target:

- If the coarse-prefix omnibus still passes, the [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] class structure compresses to a coarser axis.
- If it collapses, then the [[h-new-127-3-compression-class-mapping|H-NEW-127.3]] result depends materially on finer-grained label structure and does not compress cleanly to first-token classes.
