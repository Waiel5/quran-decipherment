# H-NEW-283 run journal

Date: 2026-04-18
Operator: codex

## Scope

Finalized local run for the H-NEW-283 max-edge follow-up after the prereg and
script were locked into the repo.

## Run notes

- Command executed: `python3 scripts/h_new_283_divine_name_max_edge.py`
- The script used the locked fixed-margin bipartite double-edge-swap null with:
  - `n_perm = 10000`
  - `accepted_swaps_per_perm = 500`
  - `alpha = 0.025`
- The run completed cleanly under worker processes.
- Output JSON written successfully to
  `findings/phase-b-hypotheses/csv/h-new-283.json`.

## Key outputs

- `M_obs = 10`
- `M_null_mean = 9.7615`
- `M_null_sd = 0.8430`
- `p_adj = 0.600040`
- `Q2-Q3 unique max edge = true`
- `MW-5 pass = true`
- overall verdict = `MAX-EDGE-NO-PASS`

## Continuity note

The parent-line synthetic control had to be retargeted from a hub-style
construction to a planted-pair max-edge control so that the positive control
actually validated the new inferential object.

