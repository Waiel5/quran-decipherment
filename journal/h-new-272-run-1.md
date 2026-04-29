# Journal — H-NEW-272 run 1

Date: 2026-04-18  
Specialist: autonomous  
Finding: `h-new-272`

## Scope

Run the pre-registered mixed hard-soft completion test at fixed `lambda = 0.07`
using only two inferential cells:

- `cell_a_lambda0p07_plus_exact_tranche`
- `cell_b_lambda0p07_plus_overlap_pair`

The positive control is the parent H-NEW-236.1h `lambda = 0.07` soft-only cell
reproduced through the new mixed-code path.

## Commands

```bash
python3 -m py_compile scripts/h_new_272_mixed_hard_soft_completion.py
python3 scripts/h_new_272_mixed_hard_soft_completion.py
```

## Execution note

An initial execution finished the simulations but crashed during JSON assembly
because the output summary mistakenly requested random-null preference fields
that the random sampler does not store. I fixed that output-only bug, changed no
simulation logic and no preregistered cells, then reran the exact same locked
experiment. The final JSON written on the successful rerun is authoritative.

## Outcome

- Compile check passed.
- Final run completed cleanly and wrote
  `findings/phase-b-hypotheses/csv/h-new-272.json`.
- Positive control passed exactly:
  - parent verdict = `SOFT-CLOSES-PRIMARY`
  - control verdict = `SOFT-CLOSES-PRIMARY`
  - max abs sim-mean drift across
    `L_path / W_wrap / L_mufassal_short / L_tail_91_114` = `0.0`

## Main result

- `cell_a_lambda0p07_plus_exact_tranche`: `MIXED-PARSIMONY-CONFLICT`
- `cell_b_lambda0p07_plus_overlap_pair`: `MIXED-PARSIMONY-CONFLICT`
- `strict_4of4_cells = []`
- `primary_only_cells = []`
- `overall_verdict = MIXED-HARD-SOFT-COMPLETION-FAILS`

## Key numbers

### Exact five-edge tranche

- `L_path` empirical percentile `0.6`, outside low
- `L_mufassal_short` empirical percentile `53.6`, inside
- `L_tail_91_114` empirical percentile `0.1`, outside low
- `Block-chi2` empirical percentile `52.2`, inside
- drift vs parent `lambda = 0.07`:
  - `L_path sim_mean +0.238852`
  - `L_tail_91_114 sim_mean +0.499058`
  - `weighted preference mean -5.548`

### Overlap pair

- `L_path` empirical percentile `1.2`, outside low
- `L_mufassal_short` empirical percentile `85.1`, inside
- `L_tail_91_114` empirical percentile `0.4`, outside low
- `Block-chi2` empirical percentile `85.1`, inside
- drift vs parent `lambda = 0.07`:
  - `L_path sim_mean +0.097414`
  - `L_tail_91_114 sim_mean +0.390723`
  - `weighted preference mean -4.442`

## Interpretation

The mixed hard complements do not finish the H-NEW-236.1h soft sweet spot.
Both tested cells preserve the local/block side but reopen the path residual and
still leave the tail outside low. The two-edge overlap subset is less damaging
than the full five-edge tranche, but it still fails cleanly.
