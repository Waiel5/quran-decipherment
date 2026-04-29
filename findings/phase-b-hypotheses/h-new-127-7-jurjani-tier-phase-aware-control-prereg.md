---
finding_id: h-new-127-7
title: "H-NEW-127.7 phase-aware control for the Jurjani-tier bridge"
specialist: codex
parent_finding: h-new-127
audit_backdrop: h-new-127-6
date_prereg: 2026-04-19
seed: 20260419
alpha: 0.05
n_perm: 20000
observable: "z_s = -gzip_z from findings/phase-b-hypotheses/csv/compression_self_ref_results.json; larger z_s means more compressible relative to the locked length-matched null"
label_axis: "jurjani_predicted_asyndeton_tier from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
phase_axis: "neuwirth_phase from findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
rules_tuple: "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = jurjani_predicted_asyndeton_tier; control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles tier labels only within phase blocks, preserving observed tier counts inside each phase; 114 surahs)"
verdict_ceiling: "POSITIVE if the within-phase label-shuffle permutation p for Kruskal-Wallis H is < 0.05; NULL otherwise"
scope_note: "This is a bounded phase-aware control on the already-locked H-NEW-127.6 tier bridge. It does not recompute the expensive compression observable and it does not relabel, pool, or merge either tiers or phases."
deliverables:
  - scripts/h_new_127_7_oq20_jurjani_tier_phase_control.py
  - findings/phase-b-hypotheses/csv/h-new-127-7.json
  - findings/phase-b-hypotheses/h-new-127-7-jurjani-tier-phase-aware-control.md
  - journal/h-new-127-7-run-1.md
---

# [[h-new-127-7-jurjani-tier-phase-aware-control|H-NEW-127.7]] preregistration

Primary question:

- Does the positive [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]] alignment between the locked compression score
  `z_s` and the locked `jurjani_predicted_asyndeton_tier` axis survive a
  phase-aware control, rather than being explained by chronology or phase
  composition alone?

Primary observable:

- `z_s = -gzip_z`, where `gzip_z` is the surah-level compression z-score
  already computed in
  `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`

Primary label axis:

- `jurjani_predicted_asyndeton_tier` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Control axis:

- `neuwirth_phase` from
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`

Chosen control design:

- Use the raw locked `z_s` values.
- Compute the same global Kruskal-Wallis `H` across the three tier groups as in
  [[h-new-127-6-jurjani-tier-bridge|H-NEW-127.6]].
- Replace the unrestricted label-shuffle null with a stricter null that shuffles
  tier labels only within each observed phase block.
- This preserves the observed tier counts inside every phase while breaking any
  within-phase tier-to-`z_s` association.

Why this control is preferred here:

- It directly conditions on the locked phase structure without introducing an
  extra modeling layer.
- It preserves the exact observed phase composition of the corpus.
- It answers the narrow question of whether the tier bridge has signal beyond
  phase assignment itself.

Primary test:

- Kruskal-Wallis `H` across the locked tier groups
- Outer null: shuffle tier labels only within each `neuwirth_phase` block while
  preserving the observed tier counts inside that block
- Decision rule: **POSITIVE** iff the one-sided permutation p-value for `H` is
  `< 0.05`

Descriptive reporting:

- Tier counts
- Mean and median `z_s` by tier
- Phase-by-tier contingency table
- Count of informative phase blocks, defined as phases containing at least two
  distinct tiers

Why this is bounded:

- The compression score is not recomputed here; it is read from a locked
  repository artifact.
- The tier and phase fields are both fixed before the run.
- The null is a constrained label-shuffle only, not a refit of the compression
  model or a chronology model.

Interpretive target:

- If the result remains positive under this control, the Jurjani-tier bridge
  survives chronology conditioning.
- If it collapses, the honest read is that the bridge is at least substantially
  phase-mediated under the locked taxonomy.
