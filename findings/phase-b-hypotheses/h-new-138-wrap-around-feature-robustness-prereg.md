---
finding_id: h-new-138
title: "Wrap-around liturgical ring: feature-space robustness (char-4-gram + verse-length histogram replication)"
specialist: (unassigned; queued for specialist-b / next-session; LOWER PRIORITY than H-NEW-137)
date_prereg: 2026-04-17
seed: 20260418
bonferroni_k: 2
bonferroni_family: h-new-138-wrap-around-features
alpha_bon: 0.025
alpha_raw: 0.05
direction_primary_chargram: "mean_d(Q 1, TERMINAL_TRIAD) < null under char-4-gram features"
direction_primary_vlen: "mean_d(Q 1, TERMINAL_TRIAD) < null under verse-length histograms"
K_char_features: 2000
K_vlen_bins: 8
length_control: "MW-1 via L1-normalization"
rules_tuple: "(114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-surah-1, char-4-gram tokens OR verse-length-bins, mushaf order, Fisher-Rao metric)"
perms: 10000
verdict_ceiling: "CONFIRMED (together with H-NEW-137, establishes feature-independent wrap-around architectural claim)"
parent_model: "theorist-2026-04-17-unified-equation.md §2 P8"
parent_preceg: "h-new-137-wrap-around-closure-prereg.md"
depends_on: "H-NEW-137 (primary FR test) must execute and pass before H-NEW-138 is dispatched"
---

# [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] — Wrap-around liturgical ring: feature-space robustness

## Motivation

[[h-new-137-wrap-around-closure|H-NEW-137]] tests the wrap-around closure claim (P8) under 4 distance
metrics on a single feature space (top-500 QAC-STEM roots). The
[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] pattern established that mushaf-geodesic claims
require **feature-space** replication to reach CONFIRMED status
(root + char-4-gram both replicated at z ≈ −11; verse-length
partially replicated but failed near-optimality band).

[[h-new-138-wrap-around-feature-robustness|H-NEW-138]] applies the same feature-space robustness standard to the
wrap-around closure claim. It tests whether mean_d(Q 1, TERMINAL_TRIAD)
remains significantly below null under TWO feature spaces orthogonal
to roots: character 4-grams and verse-length histograms.

## Hypothesis

**Primary Feature A — character 4-grams (H1a)**. Using the same
feature extraction as [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] (top-2000 character-4-grams per
surah, L1-normalized, Dirichlet-0.5 smoothed), the Fisher-Rao
mean_d(Q 1, TERMINAL_TRIAD) is below the 7-surah-sample permutation-
null distribution median, one-sided lower-tail p < α_bon = 0.025.

**Primary Feature B — verse-length histograms (H1b)**. Using the
same 8-bin verse-length histogram feature extraction as [[h-new-111c-fisher-rao-verselen|H-NEW-111c]]
(log-spaced bins: [1-3, 4-6, 7-10, 11-15, 16-25, 26-40, 41-70, 71+]
tokens per verse), the Fisher-Rao mean_d(Q 1, TERMINAL_TRIAD) is
below the 7-surah-sample permutation-null distribution median,
one-sided lower-tail p < α_bon = 0.025.

Under [[h-new-137-wrap-around-closure|H-NEW-137]]'s 4-metric cross-replication, both feature spaces
should also PASS under Hellinger / JS / TV as descriptive
robustness checks (not counted in Bonferroni family here — those
metric-replications were pre-registered in [[h-new-137-wrap-around-closure|H-NEW-137]]).

## Pre-registered Bonferroni family

**k = 2** (2 feature-space tests under primary FR metric).
**α_bon = 0.05/2 = 0.025**.

Overall verdict mapping:
- BOTH feature spaces pass primary FR test → **STRONG-PASS**
  (combined with [[h-new-137-wrap-around-closure|H-NEW-137]], escalates P8 toward CONFIRMED)
- Char-4-gram passes, verse-length fails → **PARTIAL-PASS** (P8
  holds on content-feature axis; rhythm-feature axis is feature-
  specific)
- Char-4-gram fails, verse-length passes → **ANOMALY** (inverted
  from [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s pattern; flag for re-examination)
- BOTH fail → **NULL** (P8's wrap-around claim is feature-space-
  specific to roots; demote architectural status)

## MW-5 positive control

Before executing either primary test, the executor must:

1. Re-verify that [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]'s char-4-gram Fisher-Rao matrix
   reproduces the mushaf-geodesic z = −11.41 result (published in
   `findings/phase-b-hypotheses/csv/h-new-111b.json`). Tolerance ±0.5
   on z-score.

2. Re-verify that [[h-new-111c-fisher-rao-verselen|H-NEW-111c]]'s verse-length-histogram Fisher-Rao
   matrix reproduces its mushaf-geodesic z = −9.84 result (published
   in `findings/phase-b-hypotheses/csv/h-new-111c.json`). Tolerance
   ±0.5 on z-score.

If EITHER MW-5 fails, the run is invalid for that feature.

## Specification

### Data reuse

- Char-4-gram features: reuse `scripts/h_new_111b_*.py` pipeline,
  top-K_char=2000, Dirichlet-0.5, L1-normalized, mushaf order
- Verse-length-histogram features: reuse `scripts/h_new_111c_*.py`
  pipeline, 8-bin log-spaced, Dirichlet-0.5, L1-normalized

### Distance metric

Fisher-Rao arccos-Bhattacharyya (primary metric per [[h-new-137-wrap-around-closure|H-NEW-137]]).

### Permutation null

For each feature space:
- Compute observed mean_d_TRIAD under FR on that feature space
- 10,000 permutations: each samples 7 distinct non-Q-1 surahs
  uniformly, computes (1/7) Σ d_FR(Q 1, s_sampled)
- One-sided lower-tail p per permutation empirical distribution

### Seed

Seed = 20260418 (shared with [[h-new-137-wrap-around-closure|H-NEW-137]] for reproducibility).

### Garden-of-forking-paths

Pre-reg LOCKS:
1. 2 feature spaces (char-4-gram, verse-length) — NO exotic
   additions (e.g. semantic embeddings, phonological features) in
   this pre-reg; those would require a separate future pre-reg
2. K_char = 2000, K_vlen_bins = 8 (match [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] and [[h-new-111c-fisher-rao-verselen|H-NEW-111c]])
3. Dirichlet α = 0.5 (matches parent pre-regs)
4. FR as the ONLY distance metric (not 4; the 4-metric
   cross-replication was the axis of [[h-new-137-wrap-around-closure|H-NEW-137]] not [[h-new-138-wrap-around-feature-robustness|H-NEW-138]])
5. TERMINAL_TRIAD = {Q 108..114} (matches [[h-new-137-wrap-around-closure|H-NEW-137]]; 7 surahs)
6. Bonferroni k = 2, α_bon = 0.025

## Falsifiability

- If char-4-gram + verse-length BOTH FAIL, the wrap-around closure
  is root-feature-specific → P8 demotes from SUPPORTED to
  FEATURE-SPECIFIC (less architectural)
- If only verse-length fails, P8 is a CONTENT architectural claim
  but not a RHYTHM one — consistent with [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s own
  pattern (where root + char-4-gram replicated but verse-length
  diverged on near-optimality)

## Expected outcome (theorist prediction)

- **Char-4-gram PASS**: high probability. [[cross-finding-011-mushaf-fisher-rao-confirmed|Cross-finding-011]]
  confirmed root and char-4-gram replicate each other at z ≈ −11.
  If the geodesic-like structure replicates across content feature
  spaces, the wrap-around closure should too.
- **Verse-length PASS**: uncertain. Q 1 (7 verses, short) and
  Q 108-114 (3, 6, 3, 5, 4, 5, 6 verses respectively) are all short.
  Their verse-length histograms should be similar by construction
  (length-coupled feature). This could produce a trivial PASS — not
  informative about content-level wrap-around. Flag this as a
  "length-confound artifact" if verse-length passes strongly while
  char-4-gram fails.

## Verdict ceiling

**CONFIRMED** (P8 wrap-around closure as architectural principle)
achievable if:
- [[h-new-137-wrap-around-closure|H-NEW-137]] primary + Secondary B (4-metric) PASS
- [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] char-4-gram PASS

Verse-length result is a supporting triangulation, not a required
axis, per [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s pattern.

## Depends on

**[[h-new-137-wrap-around-closure|H-NEW-137]] must execute and pass** before [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] is dispatched.
If [[h-new-137-wrap-around-closure|H-NEW-137]] NULLs, [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] is moot (P8 is already falsified at
the parent feature space).

## Integration with other findings

- Parent: [[h-new-137-wrap-around-closure|H-NEW-137]] (feature-specific wrap-around test)
- Parent model: theorist unified-equation P8
- Reuse: [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] pipeline (char-4-gram), [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] pipeline
  (verse-length)
- Relates to: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s feature-space pattern (root +
  char-4-gram replicate; verse-length partially diverges)

## Files

- Pre-reg (this file):
  `findings/phase-b-hypotheses/h-new-138-wrap-around-feature-robustness-prereg.md`
- Depends on ([[h-new-137-wrap-around-closure|H-NEW-137]] result):
  `findings/phase-b-hypotheses/h-new-137-wrap-around-closure-prereg.md`
- Parent feature pipelines:
  - `scripts/h_new_111b_*.py` (char-4-gram)
  - `scripts/h_new_111c_*.py` (verse-length histograms)
- D-matrices to reuse:
  - `findings/phase-b-hypotheses/csv/h-new-111b.json`
  - `findings/phase-b-hypotheses/csv/h-new-111c.json`
- Script (to be written): `scripts/h_new_138_wrap_around_features.py`
- Expected runtime: < 60 seconds (D-matrices pre-computed from
  [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] parent scripts)
