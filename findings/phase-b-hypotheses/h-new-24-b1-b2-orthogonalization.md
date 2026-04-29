---
finding_id: h-new-24-b1-b2
phase: B
status: CONFIRMED — novel per-surah-multiset claim strongly supported; length-confound decisively ruled out; letter-ordering contribution is NEGATIVE (real ordering suppresses boundary signal)
date: 2026-04-13
rules_tuple: (no-tashkeel, whitespace-stripped, letter-level, rasm, 31-letter)
null_models:
  - sub-e: within-surah letter shuffle (preserves surah lengths + per-surah multisets, destroys ordering)
  - sub-f: length-matched i.i.d. from global Quran unigram (preserves lengths, destroys multisets)
  - uniform-shuffle (re-run): destroys everything
  - random K-placement chance null (re-run at each K)
parent_finding: h-new-24 (letter-multiset surah-boundary detectability)
bonferroni_k: 3 (sub-e vs sub-f vs K-sweep localization)
seed: 20260413
author: computational-tester
---

# [[h-new-24-b1-b2-orthogonalization|H-NEW-24]]-B1+B2 — Length-confound orthogonalization and K-sensitivity sweep

## Why these tests exist

Parent finding [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] established that letter-multiset JS-divergence scanning
detects 41/113 interior surah boundaries at (w=2000, ε=500), vs chance mean 24.6
(null SD 3.75, z=+4.39). Sub-(c) uniform-shuffle passed (shuffled Quran → 28
hits, within the 95% chance band).

Skeptical-auditor audit-019 flagged that the uniform shuffle **destroys three
things at once**:
1. Per-surah letter multisets (the novel claim)
2. Letter ordering within a surah
3. (redundantly) any length-induced sampling structure

Without separating these, "letter-multiset discontinuity is detectable" cannot
be distinguished from "long-to-short surah length transitions cause sampling-
rate discontinuities" (trivial length confound) or "letter-ordering effects
mediate the signal" (compositional claim).

This document reports two follow-ups:
- **B1** — sub-(e) and sub-(f) decompose the signal
- **B2** — K-sensitivity sweep at K ∈ {30, 60, 113, 200, 300}

## B1 — Orthogonalization nulls

### Sub-(e) — Within-surah shuffle (50 perms)

For each of 114 surahs, shuffle its letters uniformly at random. Preserves:
- Surah order (mushaf)
- Exact surah lengths
- Exact per-surah letter unigram multisets

Destroys: letter-order structure (bigrams, trigrams, word shape, phrase).

**Result**: mean 53.24 hits, sd 2.45, range [48, 59].

### Sub-(f) — Length-matched i.i.d. null (50 perms)

Generate 114 synthetic blocks with exact Quranic surah lengths, each block
drawn i.i.d. from the global Quranic letter unigram distribution. Preserves
only the length pattern; per-surah heterogeneity **fully destroyed**.

**Result**: mean 25.10 hits, sd 4.59, range [15, 38].

### Reference: chance null = 24.57; real Quran observation = 41

### Signal decomposition (excess over chance)

Real excess = 41 − 24.57 = **+16.43**

| Source | Hits | Excess | Fraction of real signal |
|---|---|---|---|
| Sub-(e) within-surah shuffle (multiset preserved) | 53.24 | **+28.67** | **174.5%** |
| Sub-(f) length-matched i.i.d. (length only) | 25.10 | +0.53 | **3.2%** |
| Remaining (letter-ordering contribution) | 41 − 53.24 = −12.24 | −12.24 | **−74.5%** |

### Interpretation

**1. The novel per-surah letter-multiset claim is strongly confirmed.** Sub-(e),
which preserves only the per-surah unigram multisets while destroying all
letter ordering, produces MORE boundary hits than the real Quran (53 vs 41).
The per-surah letter inventories alone are sufficient to explain more than
100% of the observed boundary signal.

**2. Length confound is decisively ruled out.** Sub-(f), which preserves
surah lengths but removes all per-surah multiset heterogeneity, produces
25.1 hits — essentially identical to the chance mean (24.57). Length-induced
sampling-rate discontinuities contribute only 3.2% of the observed signal.

**3. The real letter-ordering contribution is NEGATIVE (−74.5%).** This is
the most surprising piece: the real Quran's letter sequence is LESS detectable
by the JS-scanner than its per-surah-shuffled versions. Ordering SMOOTHS or
masks what would otherwise be an even sharper per-surah multiset discontinuity.

### Why does letter-ordering suppress the boundary signal?

Several candidate mechanisms (not separately tested):

a. **Word-boundary redundancy**: In the real Quran, within-word letter runs
   have correlations (Arabic templatic morphology — typical CV patterns and
   root-consonant interleaving). These correlations produce local bigram
   clumpiness that the JS window averages over. Shuffling destroys these
   clumps and produces a cleaner unigram sample per window, which makes
   multiset discontinuities more visible.

b. **Partial smoothing via repeated phrases**: The Quran has many
   cross-surah shared phrases (e.g., *wa-huwa al-ʿalīmu l-ḥakīm*,
   *bismillāh al-raḥmān al-raḥīm*) that appear near surah boundaries and
   contribute identical letter-runs on both sides of a boundary, reducing
   JS divergence. Shuffling scrambles these matching runs.

c. **Stylometric matching across adjacent surahs**: rhyme-scheme
   continuity and common divine-name chains mean adjacent surahs share more
   letter-level structure than their unigram distributions suggest.

This is an unexpected positive finding: **the Quran's letter-order structure
systematically obscures multiset-based boundary detection**. The finding may
be relevant to future compositional analysis.

### Sub-(e)/(f) PASS thresholds (Bonferroni k=3)

- Sub-(e) novel claim threshold: excess over chance / real excess ≥ 50%
  → 174.5% ≫ 50%, **STRONG PASS**
- Sub-(f) trivial confound threshold: excess over chance / real excess < 50%
  → 3.2% ≪ 50%, **STRONG PASS (trivial confound ruled out)**

Both pass with enormous margin.

## B2 — K-sensitivity sweep

### Setup

For K ∈ {30, 60, 113, 200, 300}, re-run top-K local-maxima extraction from
the same JS scan (w=2000, stride=100, min-sep=500), measure one-to-one
detection against the 113 true boundaries at ε=500.

### Real Quran

| K | hits | precision | recall | F1 |
|---|---|---|---|---|
| 30 | 13 | **0.433** | 0.115 | 0.182 |
| 60 | 21 | 0.350 | 0.186 | 0.243 |
| 113 | 41 | 0.363 | 0.363 | 0.363 |
| 200 | 60 | 0.300 | 0.531 | **0.383** |
| 300 | 68 | 0.227 | 0.602 | 0.329 |

**Peak F1 is at K=200** (0.383), not at K=113. Precision is highest at
K=30 (0.433) but the absolute number of hits (13) is too small to pass
Bonferroni vs chance.

### Chance random-placement null (2000 perms per K)

| K | chance mean | z | pass α=0.0025? |
|---|---|---|---|
| 30 | 7.21 ± 2.25 | **+2.57** | FAIL (needs +2.81) |
| 60 | 13.98 ± 2.94 | **+2.38** | FAIL |
| 113 | 24.61 ± 3.82 | **+4.29** | **PASS** |
| 200 | 38.93 ± 4.14 | **+5.09** | **PASS** (strongest) |
| 300 | 51.97 ± 4.53 | **+3.54** | **PASS** |

### Uniform-shuffle null (30 perms per K, re-run for each K)

| K | shuffle mean | real z vs shuffle |
|---|---|---|
| 30 | 7.93 ± 2.72 | +1.87 |
| 60 | 14.53 ± 3.82 | +1.69 |
| 113 | 26.00 ± 4.23 | **+3.54** |
| 200 | 43.23 ± 5.27 | **+3.18** |
| 300 | 59.13 ± 3.94 | **+2.25** |

Shuffle null is slightly above chance null (+1.4 at K=113) because
permutation preserves global unigram — consistent with parent finding.

### Localization analysis

Precision-lift = real_precision / chance_precision:

| K | lift_P | F1_lift |
|---|---|---|
| 30 | **1.80** | 1.80 |
| 60 | 1.50 | 1.50 |
| 113 | 1.67 | 1.67 |
| 200 | 1.54 | 1.54 |
| 300 | **1.31** | 1.31 |

lift@K=30 / lift@K=300 = **1.378** → **MILDLY LOCALIZED**.

The head of the prediction ranking is nominally more precise, but not
dramatically so. The signal is NOT sharply localized to a few high-confidence
peaks — it's spread across a broad band of 100-300 moderate peaks. The
finding is "diffuse-to-mild-head" rather than "few-decisive-boundaries".

### K-sweep verdict

- **K=200 is the optimal operating point**: highest F1 (0.383) and highest
  chance-null z (+5.09).
- **K=113 was not the uniquely best choice**: it was the test-imposed "match
  the number of true boundaries" choice, but from a pure detection-power
  standpoint K=200 is better.
- **K=30 is not reliable**: z=+2.57 vs chance fails α=0.0025, despite the
  high precision (0.433).
- **The signal is NOT localized to a tight head**, contradicting the
  optimistic reading of "a few decisive boundaries". 
- **The signal is NOT purely diffuse either**: lift ratio 1.38 (head / tail)
  means the top 30 predictions are ~38% better than the tail, which is a
  mild concentration.

## Joint B1+B2 verdict

| Test | Question | Result |
|---|---|---|
| **B1 sub-(e)** | Does per-surah multiset heterogeneity explain signal? | **YES — 174.5% of excess preserved** |
| **B1 sub-(f)** | Does length-sampling explain signal? | **NO — 3.2% of excess preserved** |
| **B2 K-sweep** | Is the signal localized to a few peaks? | **Mildly — lift 1.38×, optimal K=200** |
| **Joint verdict** | Is [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] a real novel finding? | **YES, upgraded** |

**Upgrade recommendation for [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] parent**:
- Status: PARTIAL → **CONFIRMED** at the essential claim level
- The novel claim "per-surah letter multisets are discriminably heterogeneous
  in a way that JS-scan picks up" is validated beyond the original test's
  power.
- The trivial-length-confound explanation is ruled out.
- New piece: letter-ordering in the real Quran SUPPRESSES rather than
  contributes to the signal.

## Amendments to parent finding language

Add to [[h-new-24-b1-b2-orthogonalization|H-NEW-24]].md interpretation section:

> **Mechanism isolation (B1/B2)**: The signal is driven by per-surah letter-
> unigram multiset heterogeneity (174.5% preserved under within-surah shuffle),
> NOT by length-induced sampling (3.2%). The real Quran's letter-order
> structure suppresses the signal slightly relative to a per-surah-multiset-
> preserving shuffle. K-sensitivity sweep shows optimal detection at K=200
> (F1=0.383), confirming the signal is broadly distributed across ~200
> moderate peaks rather than concentrated in a decisive head.

## Garden of forking paths (disclosed)

- **50 perms per null-type** in B1 (not 200 or 500). Given the tight spread
  (sd 2.45 for sub-e, 4.59 for sub-f), 50 is sufficient for the z-test;
  point estimates stable.
- **30 uniform-shuffle perms** in B2 K-sweep is small compared to 2000 chance
  perms. Shuffle stats are descriptive, not primary tests.
- **Localization 1.38× threshold** is a heuristic. A formal test would
  require jackknife resampling of the top-K lists.
- **No K>300** tested — the signal might plateau further out, but the
  "localized vs diffuse" question is already answered.
- **Sub-(e) used random.Random(20260413) reseeded per perm series** (not
  per perm) — permutations are sequential not independent from the master
  stream. This is standard practice and does not affect validity.
- **Sub-(f) unigram sampling** uses binary search on cumulative distribution;
  small floating-point imprecision but negligible at N~330k.

## Limits

1. **No surah-level heterogeneity analysis within B1** — which surahs drive
   the signal? A per-surah breakdown would identify the most
   multiset-distinctive surahs. Not run.
2. **Letter-order suppression mechanism not directly tested** — the −74.5%
   number is robust but the CAUSE (bigram clumpiness, repeated phrases,
   cross-surah phrase-matching) is speculated. Bigram-level analysis could
   pin this down but is beyond the scope of B1/B2.
3. **Single scale (w=2000) tested** — the orthogonalization could differ
   at w=500 or w=5000. B2 parent finding already established w=2000 is
   near-optimal.
4. **n=50 perms for B1** is adequate for point estimation but thin for
   confidence intervals; the qualitative decomposition is unambiguous
   at these margins.

## Files

- Script B1: `scripts/h_new_24_b1_orthogonalize.py`
- Script B2: `scripts/h_new_24_b2_k_sweep.py`
- Output B1: `findings/phase-b-hypotheses/csv/h-new-24-b1.json`
- Output B2: `findings/phase-b-hypotheses/csv/h-new-24-b2.json`
- Parent: `findings/phase-b-hypotheses/letter-multiset-boundary-detection.md`
- Seed: 20260413
