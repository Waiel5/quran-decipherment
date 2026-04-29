# Journal — H-NEW-236.2a run 1

- Date: 2026-04-18
- Pre-reg: `findings/phase-b-hypotheses/h-new-236-2a-other-observables-prereg.md`
- Pre-reg SHA-256: `b9b3272e42856f09e9d847491db2466f7e45bfd9228926aed7d955252bcf7ada`
- Script: `scripts/h_new_236_2a_other_observables.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-236-2a.json`
- Seed: `20260422`

## Command

```bash
python3 scripts/h_new_236_2a_other_observables.py
```

## MW-6 positive control

- PASS
- parent `L_mufassal_short z = +1.3141`
- reproduced `z = +1.3166`
- `delta z = +0.0025`
- original `L_path / W_wrap / Block-chi2 / L_tail_91_114` all remained inside the sim 95% CI

## External observable results

- `cell_A_density_gradient_rho`
  - verdict `PASS`
  - empirical `rho = -0.4755`
  - sim mean `-0.4794`
  - sim 95% CI `[-0.4924, -0.4669]`
  - percentile `68.6`
  - random mean `-0.0033`

- `cell_B_kl_gradient_rho`
  - verdict `PASS`
  - empirical `rho = +0.9201`
  - sim mean `+0.9172`
  - sim 95% CI `[+0.9121, +0.9224]`
  - percentile `79.5`
  - random mean `-0.0001`

- `cell_C_alpha_beta_residual_gradient_rho`
  - verdict `PASS`
  - empirical `rho = -0.2557448880`
  - sim mean `-0.2557448880`
  - sim 95% CI exactly `[-0.2557448880, -0.2557448880]`
  - percentile `100.0`
  - random mean `+0.0006`

## Immediate interpretation

The top-level locked verdict is `BROAD-GENERALIZATION` (`3/3` passes).

But the evidence is not symmetric:

- Cells A and B are genuinely informative and show that the landed
  `M_H` scaffold preserves both the H-NEW-239 density gradient and the
  H-NEW-231 KL gradient.
- Cell C is a compatibility pass with zero simulator variance because
  the finite H-NEW-178 residual subset is effectively frozen by the
  top-100 hard-hinge chain.

Straight summary:

- broad generalization is supported
- strongest new evidence is semantic/compositional gradient preservation
- the H-NEW-178 cell should not be over-claimed
