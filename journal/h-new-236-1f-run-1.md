# Journal — H-NEW-236.1f run 1

- Date: 2026-04-18
- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1f-tail-repair-scaffold-prereg.md`
- Pre-reg SHA-256: `9498db4f7de8b4404fc32bc6bafbd0435fd88b45ea26f8f98ddaacbbeead6ba3`
- Script: `scripts/h_new_236_1f_tail_repair_scaffold.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-236-1f.json`
- Seed: `20260423`

## Command

```bash
python3 scripts/h_new_236_1f_tail_repair_scaffold.py
```

## Positive control

- `k=0` reproduces H-NEW-236.1c Cell A exactly in pattern
- `L_path` / `L_tail_91_114` remain outside low
- `L_mufassal_short` / `Block-chi2` remain inside
- simulator-mean drifts vs parent are tiny:
  - `|Δ L_path sim_mean| = 0.000276`
  - `|Δ L_tail_91_114 sim_mean| = 0.003405`
  - `|Δ L_mufassal_short sim_mean| = 0.000088`
- positive control verdict: `PASS`

## Sweep result

- no `k` achieves the primary repair criterion
- no `k` achieves family 4/4 closure
- `k=0..5` keep the local block closed but never repair `L_path` or
  `L_tail_91_114`
- `k=6`, `k=9`, `k=10` reopen the local block
- `k=7` and `k=8` re-close the local block, but both global observables
  still remain outside low

Key boundary cells:

- `cell_k_00`
  - verdict `LOCAL-CLOSED-GLOBAL-NOT-YET-REPAIRED`
  - `L_path sim_mean = 86.5084`
  - `L_tail sim_mean = 10.5066`
  - `L_mufassal_short sim_mean = 16.4415`
  - `Block-chi2 = 1.86`

- `cell_k_08`
  - first cell containing `99-100` and `100-101`
  - verdict `LOCAL-CLOSED-GLOBAL-NOT-YET-REPAIRED`
  - `L_path sim_mean = 86.9480`
  - `L_tail sim_mean = 10.7907`

- `cell_k_10`
  - first cell containing the full exploratory `95->100` tranche
  - verdict `NO-REPAIR`
  - `L_path sim_mean = 87.0607`
  - `L_tail sim_mean = 10.8329`
  - `L_mufassal_short` outside low
  - `Block-chi2` outside

## Immediate interpretation

This is a real negative result, not a broken run.

The late-tail scaffold remains structurally interesting, especially
because the exploratory `95->100` tranche is mostly outside the rhyme
and liturgical covariates, but the present hard-prefix design does not
repair the H-NEW-236.1c over-correction.

Best current read:

- late-tail-only hard adjacency is insufficient
- the decisive terminal information is either more selective than this
  cumulative prefix or needs to enter as a softer / interacting
  constraint rather than a pure hard scaffold
