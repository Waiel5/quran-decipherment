---
finding_id: h-new-258
title: "Cross-corpus replication of H-NEW-236 M_H scaffold logic on the H-147 Bukhari instrument"
specialist: autonomous
date_prereg: 2026-04-18
seed: 20260424
parent_findings:
  - "H-NEW-147 file lineage (`h-new-147-bukhari-cross-corpus.md` / on-disk JSON id `h-new-145`)"
  - "H-NEW-236.1b (Quran M_H top-100 strict closure)"
bonferroni_k: 4
bonferroni_family: h-new-258-bukhari-mh-replication
alpha_raw: 0.05
alpha_bon: 0.0125
rules_tuple: "(Bukhari segmentation/order instrument inherited exactly from H-NEW-147: split `bukhari-noquran.txt` on `باب`, whitespace tokenization, light-stemming, top-500 roots, Fisher-Rao arccos-Bhattacharyya, retain the 114 longest segments in the post-sort order used by H-NEW-147; top-K canonical consecutive-edge preservation over that retained sequence; chain-order local search with fixed chain orientation; seed 20260424)"
verdict_ceiling: "PASS-DIRECTED (nearest honest cross-corpus analogue only; observables are not one-to-one with Quran 236 family)"
---

# [[h-new-258-bukhari-mh-replication|H-NEW-258]] — Bukhari M_H replication pre-registration

## Motivation

`[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]` established a strong Quran-side result: under the
project's mushaf simulator, extending preserved canonical consecutive
Fisher-Rao edges to `K=100` (`M_H`) is sufficient for strict 4/4
closure. The open cross-corpus question is whether that kind of hinge
scaffold logic has any analogue in the Bukhari baseline setting, or
whether the Quranic result is unusually dense and corpus-specific.

The comparison cannot be exact. Bukhari does **not** have the Quran
simulator's classical-block grammar, Q1 lock, tail observable, or
block-level residual inventory. The nearest honest approximation is
therefore narrower:

> take the exact `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` Bukhari segmentation / distance
> instrument, rank its canonical consecutive Fisher-Rao edges, preserve
> the top-K of those edges as hard directed hinges, and ask whether the
> inherited Bukhari canonical order becomes generatively typical under
> the resulting constrained local-search family.

This tests the **form** of the Quranic `M_H` logic without pretending
that the Bukhari observable stack is identical.

## Critical inheritance disclosure

Two awkward inherited facts are locked and disclosed before execution:

1. The parent file is named
   `findings/phase-b-hypotheses/h-new-147-bukhari-cross-corpus.md`, but
   its on-disk finding id / JSON id is `[[h-new-145-muq-code-decoding|h-new-145]]`. This run treats that
   file lineage as the operative parent and cites the mismatch
   explicitly.
2. The `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` loader sorts Bukhari bab-segments by length and then
   keeps the top 114 in that post-sort order. It does **not** reconstruct
   raw textual bab order after selection. This run inherits that exact
   instrument rather than inventing a cleaner one, per instruction.

## Hypothesis

Primary question:

> Does an analogous top-K preserved-canonical-adjacency scaffold make
> the inherited Bukhari canonical order generatively typical, and if so
> at what hinge density?

Pre-registered directional expectations:

- `K=0` should remain open: the inherited Bukhari canonical order should
  stay above the simulated unconstrained local-minimum distribution, in
  line with `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` where `L_canonical = 108.16` and
  `L_2opt = 90.41`.
- `K=100` is the primary analogue cell. If even `K=100` fails to bring
  empirical `L_path` inside the simulator 95% CI, the Quranic `M_H`
  result is unusually specific.
- If closure occurs only at very high K (e.g. first passing cell is
  `K=100`), that supports a **high-density analogue**.
- If closure occurs at much lower K (`K=15`, `K=30`, or `K=50`), that
  supports a **looser analogue** and weakens any claim that dense
  top-100 hinge preservation is uniquely diagnostic.

## Data and instrument

- Source corpus: `data/baseline-corpora/raw/bukhari-noquran.txt`
- Segmentation: split on literal `باب`
- Segment filtering/selection: exactly the `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` method, i.e.
  tokenize by whitespace, sort segments by token count descending, take
  the top 114 in that retained order
- Root proxy: exact inherited light-stemmer from `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]`
- Distribution matrix: top-500 global roots, Dirichlet `alpha = 0.5`,
  L1-normalized
- Distance metric: Fisher-Rao arccos-Bhattacharyya

## Canonical sequence and hinge ranking

Let the inherited retained Bukhari sequence be `B_1 ... B_114`.

1. Compute the 113 canonical consecutive-edge distances
   `d(B_i, B_{i+1})`.
2. Rank those 113 directed edges by descending distance.
3. For each tested `K`, preserve the top-K ranked directed canonical
   edges as hard hinges.
4. Build directed chains from those hinges; chain orientation is fixed
   by the inherited canonical sequence.

## Generative approximation

Because Bukhari lacks the Quran simulator's extra structure, the
generative family here is:

1. Build hinge chains from the top-K preserved edges.
2. Treat each chain as an indivisible oriented unit.
3. Randomly permute chain order.
4. Run chain-order local search by subsequence-reversal proposals while
   preserving chain orientation.
5. Record final `L_path` after optimization.

This is not claimed to be the exact Quran `236` simulator. It is the
nearest honest Bukhari analogue of "canonical high-cost adjacencies are
preserved, free structure re-optimizes around them."

## Cells

Primary family:

- `K=15`
- `K=30`
- `K=50`
- `K=100`

Calibration / inherited baseline:

- `K=0` control

These values are locked before execution because they mirror the main
Quran hinge cutoffs that matter in the `236` sequence while keeping the
experiment modest.

## Positive control

Before cell interpretation, the script must reproduce the inherited
`[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` Bukhari instrument numerically:

- recomputed `L_canonical` should match the parent within `0.5`
  Fisher-Rao units
- recomputed best-of-10 unconstrained 2-opt `L_2opt` should match the
  parent within `0.5` Fisher-Rao units

If this fails, the run is inadmissible because it is not using the same
Bukhari instrument.

## Primary observable

Only one primary closure observable is available cross-corpus:

- `L_path` of the inherited Bukhari canonical sequence

Per cell, report:

- simulator mean / SD / 95% interval for `L_path`
- percentile of empirical canonical `L_path`
- chain count and free-chain count
- closure percentage of the baseline mean-gap relative to `K=0`

## Locked interpretation rules

Per cell:

- **CLOSED**: empirical `L_path` lies inside the simulator 95% CI
- **OPEN-HIGH**: empirical `L_path` lies above the simulator 95% CI
- **OPEN-LOW**: empirical `L_path` lies below the simulator 95% CI

Overall verdict mapping:

- **NO-ANALOGUE**: `K=100` remains open
- **HIGH-DENSITY-ANALOGUE**: `K=100` closes but `K=50` does not
- **LOOSE-ANALOGUE**: first closing cell is `K=15`, `K=30`, or `K=50`

Secondary descriptive output:

- `first_closing_k` among the tested grid
- `K100_closes` boolean

## Honest limits

1. This is a **path-only** analogue. It cannot replicate the Quran-side
   4/4 verdict because Bukhari lacks matched block/tail observables.
2. The inherited Bukhari sequence is only as faithful as `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]`'s
   top-114-by-length retained-order instrument.
3. The local-search family here is a fresh approximation for this
   experiment, not a previously landed Bukhari simulator lineage.
4. Any direct Quran-vs-Bukhari comparison must respect the observable
   mismatch: Quran top-100 strict closure was 4-observable; Bukhari here
   is path-only.
5. A positive result would show an analogue of scaffold logic, not a
   full causal-generative equivalence between corpora.

## Deliverables

1. `scripts/h_new_258_bukhari_mh_replication.py`
2. `findings/phase-b-hypotheses/csv/h-new-258.json`
3. `findings/phase-b-hypotheses/h-new-258-bukhari-mh-replication.md`
4. `journal/h-new-258-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
