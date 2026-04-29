# Journal — H-NEW-236.1c run 1

- Date: 2026-04-18
- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1c-targeted-mufassal-hinges-prereg.md`
- Pre-reg SHA-256: `001eff4e16af49c9f8b40e1e00ec827e0612cfe3b3b375ee12a82bc89453f67e`
- Script: `scripts/h_new_236_1c_targeted_mufassal_hinges.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-236-1c.json`
- Seed: `20260419`

## Command

```bash
python3 scripts/h_new_236_1c_targeted_mufassal_hinges.py
```

## Top-line results

- `cell_a_top50_plus_j30_top5`
  - `mufassal_gap = 0.073522`
  - `gap_closed = 91.79%`
  - `sim_passes = 2/4`
  - verdict `PARTIAL-TERMINAL-CLOSURE`
- `cell_b_top50_plus_j30_top10`
  - `mufassal_gap = -0.085664`
  - `gap_closed = 109.57%`
  - `sim_passes = 2/4`
  - verdict `PARTIAL-TERMINAL-CLOSURE`

## Interpretation logged immediately after run

The targeted Juzʾ-30 internal hinges are clearly causal for the
mufaṣṣal-short block residual:

- both cells move `L_mufassal_short` inside the simulator 95% CI
- both cells move `Block-χ²` inside as well

But both cells overcorrect globally:

- `L_path` falls BELOW the simulator 95% CI
- `L_tail_91_114` falls BELOW the simulator 95% CI even more strongly

So the remaining frontier is not "find the missing Juzʾ-30 hinges." It
is "what preserves those front-loaded hinges while also keeping the late
tail unusually short?"
