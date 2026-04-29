# Journal — H-NEW-183 run 1

**Date**: 2026-04-17
**Seed**: 20260419
**Executor**: autonomous test agent
**Pre-reg**: `findings/phase-b-hypotheses/h-new-183-chronology-predictor-prereg.md`

## Command

```
python3 scripts/h_new_183_chronology_predictor.py
```

## Stdout (run 1, final)

```
Wrote /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-183.json
Verdict: CHRONOLOGY-QUANTITATIVE
Ridge full: R2=0.8356  MAE=8.74  rho=0.920
Ridge length-only: R2=0.4462  MAE=19.30  rho=0.668
RF full: R2=0.8438  MAE=8.35  rho=0.915
Perm null: mean=-0.1242 97.5%=-0.0053 p_obs=0.001996
H1=True  H2=True
MW-5 holdout: R2_test=0.9262 MAE_test=5.98
```

## Data inputs

- `data/revelation-order.csv` (114 rows, column `noldeke_order`)
- `findings/phase-b-hypotheses/csv/h-new-123.json` (per-surah N, β, K from Heap fit)
- `findings/phase-b-hypotheses/csv/h-new-125.json` (per-surah 15-axis values)
- `findings/phase-b-hypotheses/csv/h-new-168-per-surah-dispersion.csv`
  (per-surah dispersion score)

## Missing values

35 / 114 surahs have NaN β and K (short surahs, N_tokens < 100). Imputed to
column median. Dispersion / H-NEW-125 axes are complete (no NaN).

## Pre-reg compliance

- 12 named features: kept exactly.
- Ridge(α=1.0) + RF(n=500, max_depth=None, seed=20260419): kept exactly.
- LOOCV per model: kept.
- 500-perm null with seed 20260419: kept.
- 80/20 MW-5 holdout with seed 20260419: kept.
- Bonferroni-2, α_test = 0.025: kept.
- Verdict grid: kept from pre-reg.

## Discovered issues

None. Analysis ran cleanly in ~2 min (500 LOOCV × ridge ~ 57k ridge fits,
+ 114-fold LOOCV RF).

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-183.json` (full JSON with per-surah
  predictions and residuals)
- `findings/phase-b-hypotheses/h-new-183-chronology-predictor.md` (finding)
