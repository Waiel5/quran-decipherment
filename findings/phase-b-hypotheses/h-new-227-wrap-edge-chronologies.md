---
id: H-NEW-227
title: Wrap-edge d(last,first) across chronologies — mushaf ṭawāf-like closure test
phase: B
date: 2026-04-17
seed: 20260419
permutations: 10000
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; D from H-NEW-111)
h_new_111_sha256: 4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc
h_new_212_sha256: b9725730c032d2bacea13a8b099c01ef5f009bfb2bb7ca5f1cf688f0ac341fba
---

# [[h-new-227-wrap-edge-chronologies|H-NEW-227]] — Mushaf wrap-edge vs chronology wrap-edges

## Question

Does the mushaf "ṭawāf-like" wrap-around d(Q 114 → Q 1) beat the analogous wrap-edge d(final, initial) under Nöldeke (1860), Egyptian Standard (1924), Bell (1937), and Blachère (1947)?

## Method

- Reuse 114×114 Fisher-Rao angular distance matrix **D** from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (QAC-STEM top-500 roots, Dirichlet α=0.5, L1-normalized).
- For each ordering π, compute wrap-edge = D[π[-1], π[0]].
- Null: 10,000 uniform-random permutations; for each, record D[perm[-1], perm[0]].  Compute one-sided lower-tail permutation p-value for mushaf wrap.
- Bonferroni k=1 per task spec; α=0.05.

## Results

| Ordering | first | last | wrap-edge d(last,first) | z | p₁ₛ |
|---|---:|---:|---:|---:|---:|
| mushaf | Q1 | Q114 | 0.3884 | -2.537 | 0.0277 |
| noldeke_1860 | Q96 | Q5 | 1.2173 | +1.406 | 0.9514 |
| egyptian_1924 | Q96 | Q110 | 0.4688 | -2.154 | 0.0461 |
| bell_1937 | Q96 | Q5 | 1.2173 | +1.406 | 0.9514 |
| blachere_1947 | Q96 | Q110 | 0.4688 | -2.154 | 0.0461 |

Null wrap mean=0.9217, sd=0.2102, median=0.9534, q05=0.4799

## Leaderboard (tightest wrap first)

1. **mushaf** d=0.3884 (Q114 → Q1)  ← mushaf
2. **egyptian_1924** d=0.4688 (Q110 → Q96)
3. **blachere_1947** d=0.4688 (Q110 → Q96)
4. **noldeke_1860** d=1.2173 (Q5 → Q96)
5. **bell_1937** d=1.2173 (Q5 → Q96)

## Head-to-head Δ (negative ⇒ mushaf is tighter)

| Chronology | d(last,first) | Δ = d_mushaf − d_chrono | Δ/SD | Interpretation |
|---|---:|---:|---:|---|
| noldeke_1860 | 1.2173 | -0.8290 | -3.943 | mushaf TIGHTER |
| egyptian_1924 | 0.4688 | -0.0804 | -0.382 | mushaf TIGHTER |
| bell_1937 | 1.2173 | -0.8290 | -3.943 | mushaf TIGHTER |
| blachere_1947 | 0.4688 | -0.0804 | -0.382 | mushaf TIGHTER |

## Verdict

- PRIMARY (mushaf wrap-edge vs permutation null): p₁ₛ = 0.027697, α = 0.05 → **PASS**
- Mushaf wrap tighter than ALL 4 chronologies? **True**
- Mushaf rank among 5 orderings: **1/5**

## Interpretation

The ṭawāf-like wrap-around is the claim that the mushaf closes a geodesic loop: its last→first jump is short relative to a random endpoint pairing *and* relative to what each classical chronology would produce at its last→first transition.

If the mushaf wrap is **tighter than all four chronologies** AND significantly tight vs the random null, the closure is a feature of the canonical order specifically, not an artifact of any reconstructed chronology.

## Related findings
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] / [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]: provide the D matrix and whole-path analyses.
- [[h-new-137-wrap-around-closure|H-NEW-137]]: Q1 content-closeness to TERMINAL_TRIAD (Primary PASS).
- [[h-new-144-cyclic-tsp|H-NEW-144]]: cyclic TSP including the mushaf as a loop.
- [[h-new-185-ring-laplacian|H-NEW-185]]: ring-Laplacian spectral test.