# Journal — H-NEW-236.1h run 1

Date: 2026-04-18  
Specialist: autonomous  
Finding: `h-new-236-1h`

## Scope

Run a fine soft interpolation test inside the H-NEW-236.1e near-miss band using
the exact same soft terminal penalty family and simulator conventions, with a
locked lambda grid `{0.06, 0.07, 0.08, 0.09}`.

## Commands

```bash
python3 -m py_compile scripts/h_new_236_1h_fine_soft_band.py
python3 scripts/h_new_236_1h_fine_soft_band.py
```

## Outcome

- Compile check passed.
- Run completed cleanly and wrote
  `findings/phase-b-hypotheses/csv/h-new-236-1h.json`.
- MW-5 positive control passed:
  - fresh `lambda = 0` `L_mufassal_short z = +10.408`
  - parent H-NEW-236.1a top-50 `z = +10.664`

## Main result

- `lambda = 0.06`: `SOFT-NULL`
- `lambda = 0.07`: `SOFT-CLOSES-PRIMARY`
- `lambda = 0.08`: `SOFT-PARSIMONY-CONFLICT`
- `lambda = 0.09`: `SOFT-PARSIMONY-CONFLICT`

Top-level verdict:

- `strict_4of4_cells = []`
- `primary_only_cells = ['cell_b_lambda_0p07']`
- `overall_verdict = FINE SOFT BAND FINDS PRIMARY-ONLY CLOSURE`

## Key interpretation

The H-NEW-236.1e near-miss band was real. A narrow primary-only sweet spot
exists at `lambda = 0.07`, but strict closure still fails because
`L_tail_91_114` remains just outside low. The soft route is therefore partially
causal but still incomplete.
