# [[h-new-236-2a-other-observables|H-NEW-236.2a]] - Broader observable coverage under the landed M_H top-100 scaffold: pre-registration

```yaml
finding_id: h-new-236-2a
title: "Broader observable coverage under the landed M_H top-100 scaffold"
parent: h-new-236-1b
related:
  - h-new-239
  - h-new-231
  - h-new-178
grandparent: h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020
date: 2026-04-18
specialist: autonomous (H-NEW-236.2a)
seed: 20260422
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens for the inherited Fisher-Rao distance matrix per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + M_H TOP-100-HINGE-PRESERVATION imported directly from H-NEW-236.1b, plus post-simulation evaluation on external per-surah observables from H-NEW-239 / H-NEW-231 / H-NEW-178, seed 20260422)"
bonferroni_k: 3
alpha_family: 0.05
alpha_bon: 0.016666666666666666
compatibility_interval: 95% simulated central interval
control:
  - MW-6 imported-family positive control: the fresh-seed M_H top-100 rerun must keep the original 4-observable family closed and reproduce the parent mufaṣṣal-short z within |delta| <= 2.0
cells:
  - cell_A_density_gradient_rho
  - cell_B_kl_gradient_rho
  - cell_C_alpha_beta_residual_gradient_rho
n_simulations: 1000
n_random_null: 1000
```

## 1. Motivation

[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] established that the landed `M_H` top-100 hinge scaffold is
the first strict 4/4 closure on the original adjudication family:

- `L_path`
- `W_wrap`
- `Block-chi2`
- `L_tail_91_114`

That result answers the narrow causal-generative question for the original
instrument family. It does **not** yet answer the broader question:

> Does the landed scaffold also preserve independent semantic and
> compositional order signatures that the project already treats as
> meaningful, or is the closure narrowly instrument-bound to the original
> four observables?

This run opens that new branch directly.

## 2. Hypothesis

**H0:** the landed `M_H` top-100 scaffold closes only the original
[[h-new-236-generative-simulator|H-NEW-236]] observables. When evaluated on independent order-sensitive
observables derived from [[h-new-239-divine-name-gradient|H-NEW-239]], [[h-new-231-kl-divergence-per-surah|H-NEW-231]], and [[h-new-178-alpha-beta-manifold|H-NEW-178]], the
empirical canonical mushaf will mostly fall outside the simulator's
compatibility envelope.

**H1:** the landed `M_H` top-100 scaffold generalizes beyond the original
4-observable family. The empirical canonical mushaf will remain inside
the simulator's compatibility envelope on most or all of the
pre-registered external observables.

Primary question:

> Is `M_H` broad enough to preserve additional meaningful order
> signatures, or is its success narrow and instrument-specific?

## 3. Locked simulator reuse

This run does **not** invent a new generator.

It reuses the landed [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] `M_H` family as directly as possible:

1. Import the existing `h_new_236_1b_mufassal_terminal.py` module.
2. Reuse its:
   - Fisher-Rao matrix loader
   - canonical edge ranking
   - `M_H` top-100 hinge builder
   - hinge-respecting initial tour construction
   - stochastic 2-opt annealer
   - original 4-observable computation for the positive control
3. Change only what is necessary for this branch:
   - fresh seed `20260422`
   - capture the simulated tours themselves
   - evaluate extra observables on those tours after generation

Shared run counts are locked:

- `N_sim = 1000` M_H top-100 constrained samples
- `N_random = 1000` fully random permutations as a descriptive baseline

## 4. Locked observable family

Each primary observable is an **order statistic** computed from a
previously-landed per-surah metric series.

The common form is:

- let `pos(s)` be the position of surah `s` in a given ordering
- compute Spearman `rho(pos(s), x_s)` across the locked surah set for that
  observable

This yields a directly order-sensitive scalar that can be evaluated on the
canonical mushaf, on each `M_H` simulated ordering, and on the random
baseline.

### Cell A - [[h-new-239-divine-name-gradient|H-NEW-239]] divine-name density gradient

Metric source:

- `findings/phase-b-hypotheses/csv/h-new-239-per-surah.tsv`

Per-surah scalar:

- `density = name_tokens / word_count`

Locked observable:

- `rho_pos_density_114 = Spearman(position, divine_name_density)` over all
  114 surahs

Rationale:

- [[h-new-239-divine-name-gradient|H-NEW-239]]'s primary result is an order gradient: divine-name density
  decreases with mushaf position.

### Cell B - [[h-new-231-kl-divergence-per-surah|H-NEW-231]] KL-from-corpus gradient

Metric source:

- recomputed inline from `quran-text/quran-no-tashkeel.json`

Per-surah scalar:

- `KL(p_surah || p_corpus)` with the same [[h-new-231-kl-divergence-per-surah|H-NEW-231]] definition:
  Dirichlet smoothing `alpha = 0.5` on the full corpus vocabulary

Locked observable:

- `rho_pos_kl_114 = Spearman(position, KL_from_corpus)` over all
  114 surahs

Rationale:

- [[h-new-231-kl-divergence-per-surah|H-NEW-231]] established that corpus-divergence is tightly structured by
  surah-scale compositional mode. This run asks whether that ordering
  gradient is preserved under the landed scaffold.

### Cell C - [[h-new-178-alpha-beta-manifold|H-NEW-178]] alpha-beta residual gradient

Metric sources:

- `findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv`
- [[h-new-178-alpha-beta-manifold|H-NEW-178]] fitted line `alpha = -3.526 * beta + 3.689`

Per-surah scalar:

- `alpha_beta_residual = alpha - (-3.526 * beta + 3.689)`

Locked eligibility set:

- only the surahs in `[[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv` whose `alpha` and
  `beta_h159` are both finite
- this inherits [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s `N >= 50` token domain restriction and the
  parent file's finite-beta availability
- expected evaluable subset size at lock time: `n = 79`

Locked observable:

- `rho_pos_alpha_beta_residual_finite = Spearman(position, alpha_beta_residual)`
  over the fixed finite-residual subset, using each surah's global
  position in the tested ordering

Rationale:

- [[h-new-178-alpha-beta-manifold|H-NEW-178]] identified `alpha_beta_residual` as a meaningful secondary
  compositional axis beyond raw length. This run asks whether that axis
  is also arranged compatibly with the landed `M_H` ordering family.

## 5. Positive control

Before adjudicating the extra observables, the imported-family rerun must
show that the simulator has not drifted.

`MW-6` positive control PASS requires all of the following on the fresh
`M_H` rerun:

1. empirical `L_path` inside the simulated 95% CI
2. empirical `W_wrap` inside the simulated 95% CI
3. empirical `Block-chi2` inside the simulated 95% CI
4. empirical `L_tail_91_114` inside the simulated 95% CI
5. reproduced `L_mufaṣṣal-short` z within `|delta| <= 2.0` relative to
   the landed [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] parent value

If MW-6 fails, the run is instrument-invalid and no broader-coverage
claim is allowed.

## 6. Locked interpretation rules

For each primary cell:

- `PASS` = empirical observable lies inside the `M_H` simulator 95% CI
- `LOW-OUTSIDE` = empirical observable is below the sim 95% interval
- `HIGH-OUTSIDE` = empirical observable is above the sim 95% interval

The random baseline is descriptive only. It is reported to show whether
`M_H` is merely reproducing what any ordering would preserve.

Overall verdict mapping:

- `3/3 PASS` + MW-6 PASS -> `BROAD-GENERALIZATION`
- `2/3 PASS` + MW-6 PASS -> `PARTIAL-GENERALIZATION`
- `1/3 PASS` + MW-6 PASS -> `WEAK-GENERALIZATION / MOSTLY-NARROW`
- `0/3 PASS` + MW-6 PASS -> `NARROW / INSTRUMENT-BOUND`
- MW-6 FAIL -> `INVALID-RUN`

Primary count rule is used instead of a new p-value family because this
branch is a **compatibility sweep against a landed simulator family**,
not a search for one isolated directional surprise. `bonferroni_k = 3`
is disclosed for family discipline, but the pre-registered adjudication
criterion remains the simulator 95% compatibility envelope so the result
is directly comparable to [[h-new-236-generative-simulator|H-NEW-236]] / 236.1b.

## 7. Honest limits

1. These are **order-sensitive summaries of prior per-surah metrics**,
   not re-runs of the original [[h-new-239-divine-name-gradient|H-NEW-239]] / 231 / 178 inferential cells.
2. The inherited generator keeps the classical block partition fixed. Any
   observable whose signal is mostly block-membership rather than
   within-block ordering is therefore partly frozen by design.
3. [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s residual is only defined on the fixed 93-surah
   `N >= 50` file domain, and only a finite-residual subset of that file
   is numerically evaluable because some `beta_h159` entries are `NaN`.
   The short-surah tail excluded by the parent finding stays excluded
   here, and the `NaN` rows are excluded as well.
4. [[h-new-231-kl-divergence-per-surah|H-NEW-231]] had no standalone per-surah CSV in the repo. The metric is
   recomputed inline from the text using the published definition.
5. A PASS here means **compatibility with the landed scaffold**, not that
   the scaffold alone causally generates the parent finding in the
   stronger standalone sense.

## 8. Garden-of-forking-paths log (locked before execution)

- Seed `20260422`
- Imported [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] `M_H` top-100 generator family
- `N_sim = 1000`
- `N_random = 1000`
- Three primary observable cells only:
  - `rho_pos_density_114`
  - `rho_pos_kl_114`
  - `rho_pos_alpha_beta_residual_finite`
- MW-6 positive control as defined above
- No post-hoc extra observables promoted into the primary family

## 9. Deliverables

- `scripts/h_new_236_2a_other_observables.py`
- `findings/phase-b-hypotheses/h-new-236-2a-other-observables.md`
- `findings/phase-b-hypotheses/csv/h-new-236-2a.json`
- `journal/h-new-236-2a-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
