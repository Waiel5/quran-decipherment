---
finding_id: h-new-255
title: "Juzʾ 30 mini-ring test: does Q 78-114 exhibit self-similar Fisher-Rao near-geodesic + wrap-around ring topology?"
specialist: h-new-255-specialist
date_prereg: 2026-04-17
seed: 20260419
bonferroni_k: 3
bonferroni_family: h-new-255-juz30-mini-cycle
alpha_bon: 0.01667
alpha_raw: 0.05
parent_findings: [cross-finding-013, h-new-111, h-new-185, h-new-202, h-new-203]
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, Dirichlet α=0.5, Fisher-Rao angular distance, Hafs-Kufan, mushaf sub-range Q 78..Q 114 = 37 surahs)"
---

# [[h-new-255-juz30-mini-cycle|H-NEW-255]] — Juzʾ 30 mini-ring test

## Motivation

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] established that the canonical 114-surah mushaf is a
**structured Hamiltonian cycle** in Fisher-Rao content space (Layer 1
geodesicity L_mushaf/L_2opt = 1.107, z=−11.46; Layer 2 wrap-around
Q 114 → Q 1 mean_d_TRIAD = 0.37 vs corpus 0.81; Layer 3 structured
hinges at boundaries). [[h-new-185-ring-laplacian|H-NEW-185]] spectral-partitioned the mushaf ring
into two Fiedler communities with one cut at **Q 77/Q 78** — exactly
the classical Juzʾ 30 boundary. [[h-new-202-juz30-internal-structure|H-NEW-202]] showed Juzʾ 30 is the MOST
internally cohesive juzʾ (rank-1 of 30 by mean edge weight) but is not
Bonferroni-significant against random 37-arc nulls. [[h-new-203-fisher-rao-juz|H-NEW-203]] found
Juzʾ 30 is the LEAST-coherent juzʾ at verse-level pooled centroid
distance.

The 37-surah sub-mushaf Q 78..Q 114 — the short-mufaṣṣal or *juzʾ
ʿamma* — is the most-memorized, ritually most-used portion of the
Qurʾān. Classical scholarship (al-Suyūṭī *Itqān* on the mufaṣṣal
divisions; al-Ghazālī on ādāb of recitation; al-Nawawī's *adhkār* on
the three "quls" + muʿawwidhatān as closing liturgy) treats it as a
self-contained structural unit.

**Question**: does Juzʾ 30 have its OWN ring-topology signature at a
sub-scale — a mini-cycle that MIRRORS the 114-surah cycle? If so, the
ring-topology is SELF-SIMILAR across scales, which would be a
significant architectural refinement to [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s unified
M1 principle.

## Data and locked parameters

- Corpus: 114 surahs, Hafs-Kufan, no-tashkeel, basmala-counted-only-in-surah-1
  (matches [[h-new-111-fisher-rao-mushaf|H-NEW-111]] conventions).
- Feature: QAC v0.4 STEM root tokens per surah
  (`data/morphology/quranic-corpus-morphology-0.4.txt`).
- Top-K roots: K = 500 globally (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] / [[h-new-203-fisher-rao-juz|H-NEW-203]]).
- Dirichlet smoothing α = 0.5 (Jeffreys; same as parent).
- Fisher-Rao angular distance: d(p,q) = 2·arccos(Σ √(p_i q_i)).
- Sub-mushaf: 37 surahs Q 78..Q 114 (canonical Juzʾ 30 definition by
  whole-surah approximation; classical Juzʾ 30 starts mid-Q 77 but the
  **surah-set** of Juzʾ 30 is Q 78..Q 114 inclusive).
- Seed: 20260419.
- n_perm = 1000 (sub-problem N=37; 1000 sufficient for p to resolve
  below α_bon = 0.01667).

## Hypotheses and locked thresholds

### Test 1 (Primary — mini-geodesicity). α_bon = 0.01667.

Let σ_juz30 = (78, 79, …, 114) be the canonical Juzʾ 30 sub-order.
Define:
- L_juz30 = Σ_{k=78..113} d_FR(S_k, S_{k+1}) (36 consecutive edges)
- L_2opt_juz30 = 2-opt TSP-heuristic optimum on the 37×37 sub-matrix
  D_juz30[i,j] = d_FR(S_i, S_j) for i, j ∈ {78..114}, open path, best
  over all 37 greedy-NN starts + 2-opt refinement.

Test statistic:  **R_juz30 = L_juz30 / L_2opt_juz30**.

**PASS-1** iff R_juz30 ∈ [1.05, 1.20].
**NULL-1** iff R_juz30 < 1.05 or R_juz30 > 1.20.

Rationale: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s full-mushaf ratio is 1.107. The band
[1.05, 1.20] spans "strictly tighter than full-mushaf" down to
"clearly outside the near-optimal band". A ratio < 1.05 would mean
Juzʾ 30 is MORE near-optimal than the full mushaf (possible but would
require careful attribution given 2-opt's easier convergence at
N=37); a ratio > 1.20 would mean Juzʾ 30 is NOT near-geodesic, i.e.
ring-topology is a 114-scale phenomenon not a self-similar one.

### Test 2 (Primary — mini-permutation null). α_bon = 0.01667.

Null: 1000 uniform random permutations of the 37 Juzʾ 30 surahs
(Fisher-Yates shuffle with Python `random.Random(SEED)`). For each
permutation π, compute L_π = Σ d_FR(S_{π_k}, S_{π_{k+1}}).

Test statistic:  **z_juz30** = (L_juz30 − mean(L_π)) / sd(L_π).
p_2 = (1 + #{L_π ≤ L_juz30}) / (n_perm + 1), one-sided lower.

**PASS-2** iff z_juz30 < −3.0 AND p_2 < 0.01667.
**NULL-2** iff z_juz30 ≥ −3.0 OR p_2 ≥ 0.01667.

Rationale: full-mushaf z = −11.46 ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]). N=37 has much
higher null SD than N=114 so |z| will be smaller; −3.0 is the
conservative signal-detection threshold for "genuinely non-random at
small N".

### Test 3 (Primary — mini-wrap-around). α_bon = 0.01667.

Wrap-edge observed: **w_wrap = d_FR(S_114, S_78)**.

Null distribution: for each of the 1000 Juzʾ-30 permutations (same
1000 as Test 2), extract the wrap-edge d_FR(S_{π_37}, S_{π_1}) as a
null sample.

p_3 = (1 + #{w_null ≤ w_wrap}) / (n_perm + 1), one-sided lower.

**PASS-3** iff p_3 < 0.01667.
**NULL-3** iff p_3 ≥ 0.01667.

Rationale: parallels [[h-new-137-wrap-around-closure|H-NEW-137]]'s wrap-around test at sub-scale. If
Juzʾ 30 has its own ring-closure signature, d(Q 114, Q 78) should be
shorter than typical d(S_a, S_b) for Juzʾ-30 surahs.

### Joint verdict matrix

| T1 ratio | T2 z/p | T3 wrap | Label |
|---|---|---|---|
| PASS [1.05,1.20] | PASS z<−3.0 | PASS p<.0167 | **SELF-SIMILAR-RING** (all 3: mini-ring confirmed; CF-013 topology is fractal) |
| PASS | PASS | NULL | **MINI-GEODESIC-OPEN-PATH** (Juzʾ 30 is geodesic but not a closed mini-ring) |
| PASS | NULL | * | **COMPOSITIONALLY-COHERENT-NON-SIGNIFICANT** (shape right, small-N power limit) |
| NULL ratio | * | * | **NOT-MINI-RING** (Juzʾ 30 is NOT a sub-scale ring; topology is 114-specific) |

## Secondary / descriptive (not bonferroni-counted)

- S1. **Internal structural hinges**: compute the 36 consecutive-pair
  FR distances d(S_k, S_{k+1}) for k=78..113. Rank and report the
  top-5 jumps (analogous to [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s 15-largest-jump hinge
  decomposition at full-mushaf scale). Flag alignment with [[h-new-130-fisher-rao-residuals|H-NEW-130]]
  universal hinges or [[h-new-202-juz30-internal-structure|H-NEW-202]]'s Q 97/Q 98 sub-Fiedler boundary.
- S2. **Comparison to full-mushaf 1.107**: descriptive diff
  (R_juz30 − 1.107). If R_juz30 = 1.107 ± 0.02, that is quantitative
  self-similarity. Report but not inferential.
- S3. **Distance statistics**: mean, median, min, max of all 666
  upper-triangular pair distances within Juzʾ 30; compare to
  full-mushaf (corpus mean ~0.81 from [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]).
- S4. **Juzʾ 30 vs random 37-surah contiguous arc from full mushaf**:
  does Juzʾ 30's path length beat random 37-contiguous arcs (not just
  random 37-permutations of ITSELF)? This is an auxiliary control to
  [[h-new-202-juz30-internal-structure|H-NEW-202]] H1's near-miss framing. Descriptive.

## MW-5 positive control

Greedy-NN from Q 78 on the 37-node sub-graph. If p_5 ≥ 0.001 for
z_greedy vs same 1000-permutation null, the instrument is broken
and primary verdicts are inadmissible.

## Pre-committed failure modes

| Scenario | Report |
|---|---|
| T1 + T2 + T3 all PASS | SELF-SIMILAR-RING (strongest positive) |
| T1 + T2 PASS, T3 NULL | MINI-GEODESIC-OPEN-PATH |
| T1 PASS, T2 NULL | COMPOSITIONALLY-COHERENT but N=37 small; not a ring |
| T1 NULL | NOT-MINI-RING; CF-013 topology is 114-specific |
| MW-5 pos-ctrl p ≥ 0.001 | INSTRUMENT-BROKEN; primaries inadmissible |

## Garden of forking paths (pre-declared)

- **Ring-closure 2-opt variant**: I am using OPEN-PATH 2-opt for
  L_2opt_juz30 (consistency with [[h-new-111-fisher-rao-mushaf|H-NEW-111]] convention). A CYCLE-2opt
  variant (closed tour) is tractable but would create a new
  comparison baseline (not matched to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s 1.107).
  Locking: open-path 2-opt.
- **Juzʾ 30 boundary = Q 77 or Q 78**: classical Juzʾ 30 starts at
  Q 78:1 (not mid-Q 77). Sub-mushaf = Q 78..Q 114 = 37 surahs. If
  sensitivity check shows different R with Q 77..Q 114 = 38 surahs,
  report as S5 descriptive only (NOT primary). Locking the 37-surah
  definition.
- **Permutation vs sub-matrix null**: primary null is 1000 permutations
  of Juzʾ 30 surah labels on the Juzʾ-30 sub-matrix (preserves
  sub-matrix structure). An alternative (random 37-subset of 114
  surahs) would test a different claim (whether Juzʾ 30 as a SET is
  special, not whether its ORDER is). Locking: order-null on same
  surah set.
- **Wrap-edge definition**: locked as d(S_114, S_78). An
  alternative "mean_d(S_114, {S_78..S_80})" (triad wrap, per [[h-new-137-wrap-around-closure|H-NEW-137]]
  form) would be a composite. Locking the single-edge form as
  strictly analogous to the "close Hamiltonian cycle" definition.
- **Hinge threshold**: S1 descriptive only; no Bonferroni budget.
- K=500, α=0.5, Fisher-Rao distance inherited unchanged from parent.
- n_perm=1000 locked; if p resolves below 1/1001 will report as "p <
  0.001" consistent with project conventions.

## Deliverables

1. Pre-reg (this file); SHA-256 emitted to stderr.
2. Script: `scripts/h_new_255_juz30_mini_cycle.py` (seed 20260419,
   deterministic).
3. JSON: `findings/phase-b-hypotheses/csv/h-new-255.json`.
4. Findings: `findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle.md`.
5. Journal: `journal/h-new-255-run-1.md`.
6. Ledger entry: Wave-5 block in MASTER-FINDINGS-LEDGER.md.

## Honest prior expectations

Based on the [[h-new-202-juz30-internal-structure|H-NEW-202]] near-miss on H1 (p=0.019 at raw α=0.05, z=−1.82
vs random 37-arc null), I EXPECT:
- T1 (ratio): likely PASS. Juzʾ 30 is the most-cohesive juzʾ
  descriptively ([[h-new-202-juz30-internal-structure|H-NEW-202]] S1).
- T2 (z): marginal. N=37 null SD ~ 4-5× larger than N=114; z
  target −3.0 is tight. My prior is ~50/50 between PASS and NULL.
- T3 (wrap): uncertain. d(Q 114, Q 78) might be short (both Meccan
  short-mufaṣṣal) OR unremarkable (Q 78 al-Nabaʾ is long-eschatological
  while Q 114 al-Nās is 6-ayat refuge — possibly large gap).
- [[h-new-203-fisher-rao-juz|H-NEW-203]] S3 already noted Juzʾ 30 is verse-level LEAST coherent at
  centroid pooling; this is at different scale than surah-level
  sub-Hamiltonian-path and may signal that mini-cycle fails even if
  rank-1 juzʾ cohesion holds.

All three cells could land anywhere NULL↔PASS; I have not
peeked at the Juzʾ-30 sub-matrix prior to filing this pre-reg.
