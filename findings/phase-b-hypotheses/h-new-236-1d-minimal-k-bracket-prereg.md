# [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] — Minimal-K bracket search for strict 4/4 closure: pre-registration

```yaml
finding_id: h-new-236-1d
title: "Minimal-K bracket search for strict 4/4 closure under top-K hinge extension"
parent: h-new-236-1b (top-100 hinge extension is sufficient for strict 4/4 closure; K=50 is not)
grandparent: h-new-236-1a (top-30 and top-50 close L_path but not mufaṣṣal-short)
great-grandparent: h-new-236-1 (top-15 hinges close 73% of the residual)
ancestor: h-new-236 (primary 4-principle simulator) -> cross-finding-020 (the complete equation)
siblings:
  - h-new-236-1c (targeted Juzʾ-30 internal hinges close locally but overcorrect globally)
date: 2026-04-18
specialist: autonomous (H-NEW-236.1d)
seed: 20260421
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-K-HINGE-PRESERVATION, seed 20260421)"
bonferroni_k: 6
alpha_family: 0.05
alpha_bon: 0.008333333333333333
control:
  - MW-5 positive control: top-50 baseline must remain non-closing on strict 4/4 and keep L_mufaṣṣal-short outside high
cells:
  - K73
  - K80
  - K85
  - K90
  - K95
  - K100
n_simulations: 1000
n_random_null: 1000
```

## 1. Hypothesis

**H0**: None of the pre-registered intermediate top-K hinge cuts
`K ∈ {73, 80, 85, 90, 95, 100}` achieves strict 4/4 closure under the
[[h-new-236-generative-simulator|H-NEW-236]] simulator family. The smallest tested strict-passing K is
undefined on this grid, and the inherited sufficiency claim from
[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] remains the only closure fact.

**H1**: At least one pre-registered top-K cut achieves strict 4/4
closure. The principal output is the **smallest tested K** whose
simulator puts all four primary observables inside the simulated 95% CI.

This run is a **parsimony-bracket refinement**, not a re-test of whether
closure is possible at all. The inherited state before execution is:

- `K=50` does **not** close strictly ([[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] MW-5)
- `K=100` **does** close strictly ([[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] M_H)

The open question is therefore:

> What is the smallest tested top-K hinge saturation, centered on the
> point where mufaṣṣal-short first enters the hinge ranking, that still
> produces strict 4/4 closure?

## 2. Motivation and locked K grid

Three prior runs fix the search geometry:

1. **[[h-new-236-1a-extended-hinges|H-NEW-236.1a]]**: `K=30` and `K=50` bring empirical `L_path` inside
   the simulator 95% CI and fully close ḥawāmīm, but
   `L_mufaṣṣal-short` remains a large positive miss.
2. **[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]**: `K=100` is sufficient for strict 4/4 closure.
3. **[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]**: targeted Juzʾ-30 internal hinge injection proves
   that omitted terminal hinges are genuinely causal, but the targeted
   add-on version overcorrects the global path and tail.

The first internal mufaṣṣal-short consecutive edge appears at **rank 73**
in the canonical Fisher-Rao consecutive-edge ranking. That fact makes
the region around the low 70s the natural place to search for the first
strictly sufficient `K`.

The K grid is therefore locked **before execution** as:

- `K=73`: first internal mufaṣṣal-short edge enters
- `K=80`: immediate post-entry coarse checkpoint
- `K=85`: lower-mid bracket
- `K=90`: upper-mid bracket
- `K=95`: near-sufficiency checkpoint below the inherited `K=100` pass
- `K=100`: reproduce the inherited strict-pass anchor inside this run

No adaptive insertion of extra K values is allowed after results are
seen.

## 3. Generative procedure

This run uses the existing [[h-new-236-generative-simulator|H-NEW-236]] simulator family with **no new
mechanism** beyond varying the hinge cutoff:

1. Load the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao surah distance matrix.
2. Rank all 113 canonical consecutive mushaf edges by descending
   Fisher-Rao distance.
3. For each cell `K`, preserve the top-`K` ranked canonical consecutive
   edges as hard constraints.
4. Build hinge-respecting initial tours using the same classical block
   scaffold as [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]].
5. Run within-block stochastic 2-opt annealing with the same schedule:
   `T_HOT=0.05`, `T_COLD=0.001`, `SA_ITERS=200`.
6. Generate `N_sim=1000` constrained samples per cell and a shared
   `N_random=1000` random-null baseline.
7. Run one MW-5 positive control at `K=50` under the fresh seed. It
   must fail strict 4/4 and keep `L_mufaṣṣal-short` outside high.

Nothing else is changed:

- no targeted Juzʾ-30 injection
- no rhyme-class constraint
- no liturgical-pair constraint
- no sub-block partition

This is a pure **top-K saturation** search.

## 4. Observables

Primary observables are unchanged from [[h-new-236-generative-simulator|H-NEW-236]]:

1. `L_path`
2. `W_wrap`
3. `Block-χ²` over `{L_tiwal, L_hawamim, L_mufassal_short}`
4. `L_tail_91_114`

Secondary diagnostics reported per cell:

- `L_mufaṣṣal-short` percentile and z-score
- included mufaṣṣal-short internal hinge count
- simulator CI width for `L_path`

## 5. Locked interpretation rules

For each tested `K`, define:

- **STRICT-4/4-PASS**:
  `L_path`, `W_wrap`, `Block-χ²`, and `L_tail_91_114` are all inside the
  simulator 95% CI.
- **LOCAL-BLOCK-PASS / GLOBAL-FAIL**:
  `L_mufaṣṣal-short` enters the simulator distribution, but strict 4/4
  fails.
- **NULL**:
  strict 4/4 fails and `L_mufaṣṣal-short` remains outside high.

Primary output:

- `K*_tested = min{K : STRICT-4/4-PASS}`

Bracket rule:

- If at least one cell passes, the reported tested bracket is
  `(largest failing tested K below K*_tested, K*_tested]`.
- If `K=73` passes, combine with inherited knowledge from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] /
  [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] and report `(50, 73]`.
- If no intermediate cell passes but `K=100` passes, report the
  narrowed bracket honestly from the highest failing tested K below 100.
- No monotonicity assumption is imposed. If a smaller K passes and a
  larger K later fails, the non-monotonicity is reported explicitly.

## 6. Bonferroni discipline

Primary family size is `k=6` (`K73`, `K80`, `K85`, `K90`, `K95`,
`K100`). The MW-5 top-50 positive control is a calibration check, not a
member of the primary adjudication family.

`alpha_bon = 0.05 / 6 = 0.008333333333333333`

## 7. Honest limits

1. This is a **sparse bracket search**, not an exhaustive sweep. The
   true minimal sufficient `K` can still lie between tested points.
2. The result is conditional on the same hard-hinge 2-opt generator used
   by [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / 1b. It does not adjudicate soft-weighted variants.
3. Fresh-seed sensitivity is not swept. One new seed is used per
   project convention.
4. A strict 4/4 pass is more conservative than the looser
   `L_mufaṣṣal-short + L_path` rule used as the primary cell decision in
   [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]. This is intentional because the user’s request is a
   **strict closure bracket**.
5. `K=100` is included as an internal reproduction anchor even though it
   is already known to pass from [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]. Its role here is to keep
   the bracket search inside one freshly generated result table.

## 8. Garden-of-forking-paths log (locked before execution)

- Seed `20260421`
- `K` grid `{73, 80, 85, 90, 95, 100}`
- MW-5 top-50 control
- Same simulator family and annealing schedule as [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] / 1b
- Strict pass rule = all four primary observables inside sim 95% CI

## 9. Deliverables

- `scripts/h_new_236_1d_minimal_k_bracket.py`
- `findings/phase-b-hypotheses/h-new-236-1d-minimal-k-bracket.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1d.json`
- `journal/h-new-236-1d-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
