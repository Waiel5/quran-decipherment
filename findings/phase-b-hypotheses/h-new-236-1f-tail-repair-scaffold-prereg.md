# [[h-new-236-1f-tail-repair-scaffold|H-NEW-236.1f]] — Late-tail scaffold repair sweep pre-registration

```yaml
finding_id: h-new-236-1f
title: "Late-tail scaffold repair sweep from H-NEW-236.1c Cell A — test whether adding only the H-NEW-236.1b M_H late-tail edges can jointly repair L_path and L_tail_91_114 without reopening the local mufaṣṣal-short block"
parents:
  - h-new-236-1c (Cell A = top-50 + Juz' 30 top-5; local block CLOSED, L_path and L_tail_91_114 over-corrected HIGH in simulator)
  - h-new-236-1b (M_H top-100 = first strict terminal mechanism pass; contains a late-tail scaffold inside Q 91-114)
grandparent: h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020
date: 2026-04-18
specialist: autonomous (H-NEW-236.1f)
seed: 20260423
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq constraints + H-NEW-236.1c Cell-A base + cumulative late-tail M_H edge preservation for k in {0..10})"
bonferroni_k: 11
alpha_family: 0.05
alpha_bon: 0.004545454545454545
cells:
  - k=0: exact H-NEW-236.1c Cell A base (top-50 + Juz' 30 top-5); positive-control anchor
  - k=1..10: add the first k late-tail edges from the locked scaffold [(91,92), (92,93), (95,96), (96,97), (97,98), (98,99), (99,100), (100,101), (101,102), (109,110)]
n_simulations: 1000
n_random_null: 1000
```

## 1. Hypothesis

**H0 (late-tail scaffold insufficient):** starting from the over-correcting
[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A base, no cumulative late-tail prefix `k ∈ {1..10}`
returns both empirical `L_path` and empirical `L_tail_91_114` to the
simulator 95% CI while keeping empirical `L_mufaṣṣal-short` and
`Block-χ²` inside. If so, the split-terminal picture remains suggestive
but this late-tail-only scaffold is not sufficient by itself.

**H1 (distributed late-tail scaffold repairs the over-correction):**
there exists a first `k* ∈ {1..10}` such that:

1. empirical `L_path` is inside the simulator 95% CI,
2. empirical `L_tail_91_114` is inside the simulator 95% CI,
3. empirical `L_mufaṣṣal-short` stays inside the simulator 95% CI,
4. empirical `Block-χ²` stays inside the simulator 95% CI.

If such a `k*` exists, the strongest reading is:

> the terminal block has a **split architecture**:
> front-loaded Juz' 30 hinges create the local block closure, while a
> distributed late-tail scaffold inside Q 91-114 counter-balances that
> pressure and keeps the closing tail short.

## 2. Motivation and parent context

[[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] showed that adding only the strongest internal Juz' 30
hinges to the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 scaffold collapses the local
mufaṣṣal-short residual but overshoots globally:

- `L_mufaṣṣal-short` moves inside the simulator CI
- `Block-χ²` moves inside the simulator CI
- `L_path` becomes too high in the simulator
- `L_tail_91_114` becomes too high in the simulator

[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] then showed that the first strict full closure is the much
broader M_H top-100 hinge scaffold, and the explorer synthesis isolated
the most plausible repair subset inside that success case:

`(91,92), (92,93), (95,96), (96,97), (97,98), (98,99), (99,100),
 (100,101), (101,102), (109,110)`

This run asks the narrowest next question:

- hold the proven-overcorrecting [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A base fixed
- add only the late-tail scaffold edges from M_H
- find the first cumulative `k` at which the global path and tail recover
  without reopening the local block

## 3. Locked edge sets

### 3.1 Base scaffold

The base cell is copied directly from [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A:

- [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 global hinge scaffold
- plus the five internal Juz' 30 hinges:
  `(78,79), (79,80), (88,89), (83,84), (80,81)`

No other Juz' 30 edges from [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell B are allowed.

### 3.2 Late-tail scaffold (cumulative order locked pre-run)

The only extra edges allowed are the following ten M_H top-100 edges,
added cumulatively in exactly this order:

1. `(91,92)`
2. `(92,93)`
3. `(95,96)`
4. `(96,97)`
5. `(97,98)`
6. `(98,99)`
7. `(99,100)`
8. `(100,101)`
9. `(101,102)`
10. `(109,110)`

`k=0` adds none of them. `k=10` adds all ten. No other M_H edges may be
added in this run.

## 4. Generative procedure

Start from the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] simulator family. Locked procedure:

1. Load the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A hinge list from disk and use it as the
   exact base scaffold.
2. Load the [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] M_H top-100 hinge list from disk and verify
   that all ten late-tail edges in §3.2 belong to it.
3. For each `k ∈ {0..10}`, preserve the base scaffold plus the first `k`
   late-tail edges.
4. Keep the same simulator conventions as [[h-new-236-generative-simulator|H-NEW-236]] / 236.1 / 236.1b /
   236.1c:
   - classical-block structure
   - Q1 lock
   - length stratification
   - M2-muq constraints
   - hinge-respecting within-block 2-opt
   - `T_HOT=0.05`, `T_COLD=0.001`, `SA_ITERS=200`
   - `N_sim=1000`, `N_random=1000`
5. No soft penalties, no extra rhyme/liturgical constraints, no added
   Juz' 30 edges beyond the five already present in Cell A, and no top-K
   sweep outside the ten locked late-tail edges.

## 5. Positive-control discipline

`k=0` is the pre-registered positive-control anchor because it is
exactly the [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] Cell A mechanism under a new seed.

Positive-control PASS requires all of the following:

1. empirical `L_mufaṣṣal-short` is inside the simulator 95% CI,
2. empirical `Block-χ²` is inside the simulator 95% CI,
3. empirical `L_path` is outside the simulator 95% CI on the LOW side,
4. empirical `L_tail_91_114` is outside the simulator 95% CI on the LOW
   side,
5. the absolute drift in simulator means versus the landed [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]]
   Cell A means is small:
   - `|Δ L_path sim_mean| ≤ 0.50`
   - `|Δ L_tail_91_114 sim_mean| ≤ 0.75`
   - `|Δ L_mufaṣṣal-short sim_mean| ≤ 0.50`

If the positive control fails, the run is reported but interpreted as an
instrument failure rather than as evidence on the hypothesis.

## 6. Observables

Primary repair observables:

- `L_path`
- `L_tail_91_114`
- `L_mufaṣṣal-short`
- `Block-χ²`

Continuity observable:

- `W_wrap`

The decisive question is the first `k` where the two global observables
(`L_path`, `L_tail_91_114`) re-enter while the two local observables
(`L_mufaṣṣal-short`, `Block-χ²`) stay inside.

## 7. Locked interpretation rules

For each cell `k`:

| Outcome | Verdict |
|---|---|
| `L_path`, `L_tail_91_114`, `L_mufaṣṣal-short`, and `Block-χ²` all inside sim 95% CI | **TAIL-SCAFFOLD-REPAIR** |
| local block stays closed, but one or both global observables remain outside | **LOCAL-CLOSED-GLOBAL-NOT-YET-REPAIRED** |
| global observables repair but local block re-opens | **GLOBAL-REPAIR-BUT-LOCAL-REOPENED** |
| neither pattern occurs | **NO-REPAIR** |

Overall verdict:

- first `k*` with `TAIL-SCAFFOLD-REPAIR` → supports a
  **distributed late-tail scaffold / split-terminal architecture**
- no such `k*` → this specific late-tail-only scaffold is **not
  sufficient**, even if some monotone improvement appears

The earliest `k*` is the main result, not the best-looking later cell.

## 8. Bonferroni discipline

`k = 11` cumulative cells (`0..10`), so `α_bon = 0.05 / 11 =
0.004545454545454545` per cell.

This run is primarily mechanistic and ordered, so the headline remains
the first-repair cell under the locked cumulative sweep, but the family
size is disclosed explicitly.

## 9. Honest limits

1. This is not a full M_H replay. Even `k=10` adds only the late-tail
   subset of M_H, not the other 40 edges that separate top-100 from the
   [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 baseline.
2. The edge order is theory-driven, not rank-driven. It is locked from
   the explorer synthesis of the late-tail scaffold and is not chosen
   post hoc after seeing the results.
3. A pass would establish sufficiency of this scaffold on top of Cell A,
   not uniqueness. Other edge subsets or soft penalties could also work.
4. A fail would not refute the split-terminal picture completely. It
   would show only that this hard-adjacency late-tail-only repair is not
   sufficient under the existing simulator.
5. `W_wrap` is tracked for continuity with the [[h-new-236-generative-simulator|H-NEW-236]] family but is
   not part of the primary repair criterion.

## 10. Deliverables

- `scripts/h_new_236_1f_tail_repair_scaffold.py`
- `findings/phase-b-hypotheses/csv/h-new-236-1f.json`
- `findings/phase-b-hypotheses/h-new-236-1f-tail-repair-scaffold.md`
- `journal/h-new-236-1f-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
