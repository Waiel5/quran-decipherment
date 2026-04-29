# H-NEW-276 run journal

Date: 2026-04-18
Operator: codex

## Scope

Local completion of the H-NEW-276 deep-null rerun after the prereg and
script were already on disk but no harvested finding file had landed
yet.

## Run notes

- Command executed: `python3 scripts/h_new_276_q27_hub_resolution.py`
- The script used the locked fixed-margin bipartite double-edge-swap
  null with:
  - `n_perm = 10000`
  - `accepted_swaps_per_perm = 500`
  - `hub_threshold = 2`
- Progress completed cleanly through `10000 / 10000`.
- Output JSON written successfully to
  `findings/phase-b-hypotheses/csv/h-new-276.json`.

## Key outputs

- `z_max_obs = 2.043820`
- `p_exist = 0.135986`
- `Q27 rank = 1`
- `Q27 p_adj_fwer = 0.135986`
- overall verdict = `NO-HUB-SURVIVES-DEEP-NULL`

## Continuity note

This run materially strengthens the negative side of H-NEW-263 Cell B:
the deeper null moves the hub-existence claim farther away from the
Bonferroni threshold rather than closer to it.
