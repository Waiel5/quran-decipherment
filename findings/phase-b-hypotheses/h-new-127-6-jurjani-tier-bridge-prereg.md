---
finding_id: h-new-127-6
title: "H-NEW-127.6 Jurjani-tier bridge for locked per-surah compression z-scores"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-4
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "jurjani_predicted_asyndeton_tier from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; Kruskal-Wallis H; outer null permutes tier labels across surahs preserving tier counts; 114 surahs)"
verdict_ceiling: "POSITIVE if the label-shuffle permutation p for Kruskal-Wallis H is < 0.05; NULL otherwise"
scope_note: "This is a full 114-surah tier-bridge test on an already-locked compression observable. It does not rerun the expensive within-surah OQ-20 search and it does not relabel or merge any tier classes."
deliverables:
  - scripts/h_new_127_6_oq20_jurjani_tier_bridge.py
  - findings/phase-b-hypotheses/csv/h-new-127-6.json
  - findings/phase-b-hypotheses/h-new-127-6-jurjani-tier-bridge.md
  - journal/h-new-127-6-run-1.md
---

# [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] preregistration

Primary question:

- Does the locked `jurjani_predicted_asyndeton_tier` field stratify the locked
  per-surah OQ-20 compression score `z_s`?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score
  already computed in
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`

Primary label axis:

- `jurjani_predicted_asyndeton_tier` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Primary test:

- Kruskal-Wallis `H` across the locked tier groups
- Outer null: shuffle tier labels across the 114 surahs while preserving the
  observed tier counts
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `H` is
  `< 0.05`

Descriptive reporting:

- Tier counts
- Mean `z_s` by tier
- Median `z_s` by tier

Why this is bounded:

- The compression score is not recomputed here; it is read from a locked
  repository artifact.
- The tier axis is fixed before the run.
- The null is label-shuffle only, not a re-estimation of the compression model.

Interpretive target:

- The question is whether the OQ-20 class structure lines up with the classical
  asyndeton bridge encoded in the locked TSV.
