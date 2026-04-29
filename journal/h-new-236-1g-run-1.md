# H-NEW-236.1g Run 1 Journal

**Date**: 2026-04-18  
**Finding ID**: h-new-236-1g  
**Status**: complete

## Commands

```bash
python3 -m py_compile scripts/h_new_236_1g_direct_tranche_test.py
python3 scripts/h_new_236_1g_direct_tranche_test.py
```

## Result

The run completed cleanly and the positive control passed.

Main outcome:

- `overall_verdict = NO-DIRECT-ISOLATED-TRANCHE-REPAIR`
- `primary_repair_cells = []`
- `strict_4of4_cells = []`

All four main cells were `LOCAL-CLOSED-GLOBAL-FAIL`.

## Key numbers

Positive control drift versus H-NEW-236.1c Cell A:

- `L_path sim_mean abs delta = 0.000190`
- `L_tail_91_114 sim_mean abs delta = 0.005235`
- `L_mufassal_short sim_mean abs delta = 0.000074`

Main cells:

- `cell_a_base_plus_exact_tranche`
  - `L_path sim_mean = 86.8654`, pct `0.0`
  - `L_tail_91_114 sim_mean = 10.7110`, pct `0.0`
  - `L_mufassal_short sim_mean = 16.7727`, pct `5.6`
  - `Block-chi2 pct = 94.3`

- `cell_b_base_plus_core_only`
  - `L_path sim_mean = 86.6765`, pct `0.2`
  - `L_tail_91_114 sim_mean = 10.6108`, pct `0.4`
  - `L_mufassal_short sim_mean = 16.6038`, pct `28.0`
  - `Block-chi2 pct = 64.7`

- `cell_c_base_plus_overlap_pair_only`
  - `L_path sim_mean = 86.7414`, pct `0.1`
  - `L_tail_91_114 sim_mean = 10.6546`, pct `0.1`
  - `L_mufassal_short sim_mean = 16.6375`, pct `23.6`
  - `Block-chi2 pct = 75.4`

- `cell_d_top50_plus_exact_tranche`
  - `L_path sim_mean = 86.4333`, pct `2.2`
  - `L_tail_91_114 sim_mean = 10.4597`, pct `0.4`
  - `L_mufassal_short sim_mean = 16.3359`, pct `86.4`
  - `Block-chi2 pct = 82.8`
  - `best_local_closed_cell = true`

## Notes

The strongest new partial signal is `cell_d_top50_plus_exact_tranche`:
the exact decisive five-edge tranche closes the local terminal block on
the plain top-50 scaffold without any H-NEW-236.1c Juz30 top-5
additions, but it still fails both globals. That makes the five-edge
tranche a real local mechanism candidate, not a full repair law.
