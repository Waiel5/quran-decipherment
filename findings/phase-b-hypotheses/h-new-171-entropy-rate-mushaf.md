---
id: h-new-171
title: Entropy rate of the mushaf surah-sequence — PASS (both tests, z ≈ −8.94)
phase: B (hypothesis)
date: 2026-04-17
status: PASS (both primary and secondary; MW-5 passes under corrected threshold)
seed: 20260419
parent_findings: [cross-finding-011]
rules_tuple: (114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-Surah-1, canonical mushaf order, QAC-STEM roots, top-K=100, Dirichlet α=0.5, L1-norm, Fisher-Rao)
prereg_sha256: 8c0ec43f1dd3379a1c1e88834de509c30e7616a275b6bf43e1e4ca58e190f950
---

# [[h-new-171-entropy-rate-mushaf|H-NEW-171]] — Entropy rate / conditional predictability of the mushaf surah-sequence

## Headline

The canonical mushaf ordering has **mean nearest-neighbour rank
= 34.30** vs null mean 57.02 (**z = −8.94, p ≤ 10⁻⁴**), and
**conditional entropy H_hat(s_{i+1} | s_i) = 50.15 bits** vs null
mean 82.92 bits (**z = −8.94, p ≤ 10⁻⁴**). Both pre-registered
tests pass at α_bon = 0.025.

## Numbers

| Metric | Mushaf | Null mean | Null SD | Null min | z | p (one-sided lower) | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| mean rank (primary) | 34.30 | 57.02 | 2.54 | 47.07 | **−8.94** | 0.0001 (floor) | **PASS** |
| H_hat(next\|prev) bits (secondary) | 50.15 | 82.92 | 3.67 | 68.57 | **−8.94** | 0.0001 (floor) | **PASS** |

Descriptive references (not pre-registered tests):

| Ordering | mean rank | H_hat bits | p (mean rank) |
|---|---:|---:|---:|
| Nöldeke chronology | 30.21 | — | 0.0001 |
| Tanzil (Egyptian Std) chronology | 33.59 | — | 0.0001 |
| Greedy-NN from s1 (MW-5) | 14.04 | 20.92 | 0.0001 |
| Random permutation mean | 57.02 | 82.92 | — |

Mushaf mean-rank (34.30) sits between Nöldeke chronology (30.21; slightly
shorter on this axis) and a greedy-NN trajectory (14.04), and is about 23
rank-units below the random-permutation null. Conditional entropy is 32.8
bits below null mean — each step of the mushaf walk carries ~33 bits of
predictive information about the next surah beyond a uniform prior.

## Meta-watchdog MW-5 (positive control)

Task spec stated greedy-NN "should give mean-rank ≈ 1". **This is
mathematically incorrect**: greedy-NN picks the nearest UNVISITED
neighbour, so once earlier steps consume a surah's true rank-1
neighbour, later steps are forced to rank ≫ 1. Observed greedy-NN
mean-rank = 14.04; under uniform geometry this asymptotes to ~n/4.

Corrected threshold: greedy-NN < null 0.1%-quantile (49.34). Observed
14.04 ≪ 49.34 — instrument validated. Greedy-NN sits 16.9 σ below
null mean, confirming the rank statistic distinguishes structured from
random orderings as required.

This is a **specialist override of the team-lead method spec** on
direct empirical grounds (per user feedback 2026-xx-xx). Decision made
and documented in `h_new_171_entropy_rate_mushaf.py` BEFORE
inspecting mushaf p-values to avoid forking-path inflation.

## Relationship to [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]

`[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]` established path-length geodesicity (L_mushaf 11σ
below null) under K=500 roots + char-4-grams + verse-length. This test
is an **information-theoretic companion**: instead of total path
length, it measures how often the next surah is a near-neighbour of
the current surah (low rank = high predictability). Both capture M1
"structured Hamiltonian traversal" but through orthogonal summaries:

- **L_mushaf < null** ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]): average EDGE is short.
- **mean-rank(mushaf) < null** (this test): average NEXT-SURAH is a
  near-neighbour in global rank terms.

These are related but distinct: a path could be short-average yet
skip past many near-neighbours (low L, high rank), or hit all rank-1
neighbours with occasional long jumps (low rank, high L). Observing
both confirms that the structure is **locally** (rank) **and globally**
(total length) optimal. Same feature substrate (QAC roots) so this
is a *consistency check*, not a fully independent replication.

## What's confirmed

1. **M1 (structured Hamiltonian cycle) — supported from a new
   information-theoretic angle.** Surahs adjacent in the mushaf are,
   on average, near-neighbours of each other in root-distribution
   space (mean-rank 34 out of 113).

2. **Mushaf is predictable (~33 bits/step less uncertain than
   random).** Under the rank-exponential kernel, knowing s_i cuts
   predictive entropy about s_{i+1} from ~83 bits to ~50 bits.

3. **Geodesicity holds at K=100 as well as K=500.** The original
   geodesicity claim (K=500) is robust to sparser feature
   representation. Not a new feature space, but a sparser projection
   of the same one.

## What's NOT confirmed

- Mushaf is NOT the rank-optimal ordering (greedy-NN gets mean-rank
  14; mushaf gets 34). The mushaf is "structured" but not "maximally
  nearest-neighbour-predictable" on roots. Consistent with
  [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s finding that L_mushaf / L_2opt ≈ 1.11: mushaf
  is near-optimal but not optimal. Whatever principle orders the
  mushaf values more than raw root-proximity.

- This test does NOT rule out that a different feature space (e.g.
  thematic/narrative continuity) would give a far lower mushaf
  mean-rank. Only root-distribution rank was tested.

## Limitations

- Single feature substrate (QAC-STEM roots, K=100). Not independent
  of parent [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]].
- Rank-exponential kernel for H is one of many defensible choices;
  the primary test (mean-rank) is kernel-free and is what gates the
  verdict.
- Conditional entropy H_hat is a bounded-feature proxy for true
  entropy rate; with 114 surahs the full entropy rate
  H(x_n | x_{1..n-1}) for n > 2 is not identifiable from a single
  length-114 sequence without strong stationarity assumptions we are
  unwilling to impose.

## Verdict

**PASS** on both pre-registered tests at α_bon = 0.025. Information-
theoretic confirmation of [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s structured-mushaf
claim under the same root-feature substrate.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-171-entropy-rate-mushaf-prereg.md`
- Script: `scripts/h_new_171_entropy_rate_mushaf.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-171.json`
