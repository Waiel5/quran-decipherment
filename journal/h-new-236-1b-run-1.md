# Journal — H-NEW-236.1b run 1

- Date: 2026-04-18
- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism-prereg.md`
- Pre-reg SHA-256: `8c006dfc7e79c74083cfef054787b637d110c9f400285403703ff0a868db7df6`
- Script: `scripts/h_new_236_1b_mufassal_terminal.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-236-1b.json`
- Seed: `20260420`

## Command

```bash
python3 scripts/h_new_236_1b_mufassal_terminal.py
```

## Positive control

- top-50 baseline reproduced under new seed
- parent `L_mufassal_short z = +10.6640`
- reproduced `z = +10.9170`
- tolerance check `|Δ| <= 2.0` passed

## Mechanism results

- `cell_M_H_top100`
  - verdict `MECHANISM-CLOSES-STRICT`
  - `L_mufassal_short pct = 91.70`
  - `z = +1.314`
  - `L_path` inside sim 95% CI
  - `sim_passes = 4/4`

- `cell_M_R_rhyme`
  - verdict `PARSIMONY-CONFLICT`
  - `L_mufassal_short pct = 12.90`
  - `z = -1.128`
  - closes local block but breaks `L_path`

- `cell_M_L_liturgical`
  - verdict `PARSIMONY-CONFLICT`
  - `L_mufassal_short pct = 67.10`
  - `z = +0.515`
  - closes local block but breaks `L_path`

- `cell_M_B_subblock`
  - verdict `MECHANISM-NULL`
  - `L_mufassal_short pct = 100.00`
  - `z = +11.976`

## Immediate interpretation

This is the first strict end-to-end causal-generative closure in the
H-NEW-236 family.

The closure comes from the broad hinge-extension cell, not from the
smaller classical-mechanism cells. That means:

- OQ-15 causal-generative layer is now confirmed
- but the parsimony question is still open
- next target is the smallest `top-K` depth that still yields strict
  closure
