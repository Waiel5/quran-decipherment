---
finding_id: h-new-111c
title: "Fisher-Rao information-geodesic test of mushaf order — SECOND INDEPENDENT REPLICATION on verse-length histograms"
specialist: h-new-111c-specialist
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 3
bonferroni_family: h-new-111c-verse-length-hist
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "L_mushaf < L_random at permutation p < 0.0167 (one-sided lower-tail)"
direction_secondary_ratio: "L_mushaf / L_2opt < 1.2 (pre-registered 'near-optimal' band)"
direction_secondary_nold: "L_mushaf ≤ L_nold (mushaf at-or-below chronology; descriptive sign + two-sided p vs null)"
bin_edges_locked: "[1, 5, 10, 15, 25, 40, 60, 100, inf] — 8 bins, pre-committed BEFORE any computation"
dirichlet_alpha: 0.5
length_control: "MW-1 NOT applied as residualization — verse-length IS the feature here, not a nuisance. This differs in sense from H-NEW-111's MW-1: we are measuring RHYTHMIC shape distributions, and normalizing THEM to sum to 1 is the right per-surah step (removes total-surah-size; preserves rhythmic shape) but we deliberately do not residualize against surah-length because that IS the per-surah length shape."
rules_tuple: "(no-tashkeel, whitespace-tokenized verse text, basmala-counted-only-in-surah-1 via text, mushaf order, Hafs-Kufan)"
perms: 10000
parent_finding: h-new-111
parent_replication_lane: "SECOND orthogonal replication of H-NEW-111; first is h-new-111b on char-4-grams"
verdict_ceiling: "PASS-DIRECTED (part of a replication family; promotion of parent H-NEW-111 to CONFIRMED requires THIS + h-new-111b both passing)"
---

# [[h-new-111c-fisher-rao-verselen|H-NEW-111c]] — Fisher-Rao on verse-length histograms (second independent replication)

## Motivation

[[h-new-111-fisher-rao-mushaf|H-NEW-111]] established that the Quran's mushaf ordering of 114 surahs is
information-geodesic-optimal on the ROOT-DISTRIBUTION simplex (z=−11.46,
L/L_opt=1.107, p<10⁻⁴). This was flagged PASS-DIRECTED pending independent
replication on a distinct feature space.

This pre-reg files the **SECOND** such replication. It operationalizes each
surah as a distribution over **verse-length bins** (token counts per verse)
rather than roots or character n-grams. This axis measures RHYTHMIC shape
(short staccato eschatology vs long legal discourse vs medium narrative) and
is lexicon-independent.

A parallel first replication (`[[h-new-111b-fisher-rao-char-4gram|h-new-111b]]`) operates on character-4-gram
histograms; this one operates on verse-length histograms. If BOTH pass, the
original [[h-new-111-fisher-rao-mushaf|H-NEW-111]] claim of mushaf information-geometric optimality promotes
to CONFIRMED.

## Hypothesis

**Primary (H1)**: The total Fisher-Rao path length
`L_mushaf = Σ_{i=1..113} D_FR(p_i, p_{i+1})` on the verse-length histogram
simplex is SHORTER than under a uniform random permutation of the 114 surahs.
One-sided lower-tail, α_bon = 0.0167.

**Secondary A (ratio)**: `L_mushaf / L_2opt < 1.2` where `L_2opt` is a 2-opt
+ greedy-NN TSP upper bound on `L_min`. Matches the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] threshold band.

**Secondary B (Nöldeke / Tanzil comparison)**: Is mushaf path length ≤ Nöldeke
chronology path length? Descriptive sign + two-sided p vs the same 10,000-
permutation null. Report Tanzil revelation order too.

## Method (LOCKED BEFORE RESULTS VIEWED)

### Data
- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
  (114 surahs, 6,236 verses).
- Tokenization: whitespace-split per verse; verse token count = number of
  whitespace-separated substrings. This matches the verse text as stored
  (including basmala in surah 1 verse 1, but basmala is NOT counted as an
  independent verse in surahs 2..114 per the project's basmala rule).
- Chronology: `data/revelation-order.csv` (same as [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).

### Bin edges — LOCKED BEFORE COMPUTATION

```
BIN_EDGES = [1, 5, 10, 15, 25, 40, 60, 100, inf]
```

This produces **8 bins**:

| Bin | Range (tokens) |
|-----|-----|
| 1 | [1, 5)  |
| 2 | [5, 10) |
| 3 | [10, 15) |
| 4 | [15, 25) |
| 5 | [25, 40) |
| 6 | [40, 60) |
| 7 | [60, 100) |
| 8 | [100, ∞) |

These are pre-committed in this pre-reg BEFORE the script is run. No post-hoc
re-binning. The bins are informed only by general knowledge that Quranic
verses range from ~1 token (e.g. fawātiḥ alone) to several hundred tokens
(longest verses in al-Baqarah, al-Mā'idah). No per-surah distribution has
been inspected.

### Feature space
- For each surah i: count how many of its verses fall into each of the 8 bins
  → raw 8-vector c_i.
- Dirichlet smoothing α=0.5 on every cell; L1-normalize → probability vector
  p_i on the 8-simplex.

### Distance
Fisher-Rao angular distance:

    D[i,j] = 2 · arccos( Σ_k sqrt(p_i[k] · p_j[k]) )

Clipped to [0, π]. Same metric as [[h-new-111-fisher-rao-mushaf|H-NEW-111]].

### Primary test
- `L_mushaf = Σ_{i=1..113} D[i, i+1]`
- Null: 10,000 uniform random permutations of the 114 surah IDs; same RNG
  seed (20260417); recompute L for each.
- `p_primary = (#{L_perm ≤ L_mushaf} + 1) / (PERMS + 1)`.

### Secondary A: TSP upper bound
- Greedy-NN from each of the 114 starts → best path → 2-opt → report
  `L_2opt_best` and `L_mushaf / L_2opt_best`.

### Secondary B: Nöldeke/Tanzil
- Build σ_nold and σ_tanzil orderings; compute `L_nold`, `L_tanzil`.
- Compare to same null. Two-sided p on Nöldeke.

### MW-5 positive control
- Greedy-NN from surah 1 on the same distance matrix. Must fire p < 0.001.
  If not, null BROKEN and primary inadmissible.

### MW-1 handling (distinct in sense from [[h-new-111-fisher-rao-mushaf|H-NEW-111]])

IMPORTANT: In [[h-new-111-fisher-rao-mushaf|H-NEW-111]], MW-1 length residualization meant "L1-normalize
root-distributions so total-token-count drops out." In this test, the
feature space IS built FROM verse-lengths. We still L1-normalize the per-
surah bin histograms (so per-surah TOTAL verse count drops out — a 3-verse
surah and a 286-verse surah with the same rhythmic shape will have D=0),
but we deliberately do NOT residualize against total verse count or mean
verse length as a regression step. Doing so would remove the very signal
we are measuring.

This is disclosed in garden-of-forking-paths below as a KNOWN mechanical
confound risk.

## Pre-committed acceptance window

- **PRIMARY PASS**: `p_primary < 0.0167` (Bonferroni 3).
- **SECONDARY A**: ratio < 1.2 = "near-optimal"; 1.2..2.0 = "geodesic-like";
  ≥ 2.0 = "not geodesic-like".
- **SECONDARY B**: p_nold_two_sided < 0.0167 fires as "chronology also
  non-random"; additionally report sign.

## Garden of forking paths

### Replication intent (DISCLOSED)
- This is a REPLICATION of [[h-new-111-fisher-rao-mushaf|H-NEW-111]]. Parent result is KNOWN to me; parent
  result showed mushaf path length far below null on root distributions.
- I am NOT eyeballing the verse-length histograms before running. Bin edges
  were chosen from a priori reasoning about Quranic verse-length dynamic
  range, not from inspection.

### Mechanical-confound caveat (DISCLOSED BEFORE RUNNING)

**This feature is LESS orthogonal to known Uthmanic ordering than char-4-grams**.
The canonical mushaf order places long surahs first (al-Baqarah through the
"sevens" and "meʾūn") and short surahs last (the mufaṣṣal from al-Ḥujurāt
or Qāf onward). Long surahs tend to have MANY long verses; short surahs
tend to have MANY short verses. So adjacent mushaf surahs are often similar
in verse-length distribution MECHANICALLY, not because some deeper design
chose them.

Therefore:
- A **PASS** (primary < 0.0167) is mostly **CONFIRMATORY of the known length
  ordering**, only mildly informative of an information-geometric optimality
  that goes beyond length.
- A **NULL** (primary ≥ 0.0167) would be SURPRISING given the known length
  structure, and would partially contradict [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s generality.
- The COMPARISON OF INTEREST is therefore not the primary test itself but:
    (a) L_mushaf / L_2opt ratio — does mushaf come CLOSE to optimal on this
        axis too? [[h-new-111-fisher-rao-mushaf|H-NEW-111]] got 1.107 on roots. On rhythm, a similar ratio
        would say the mushaf ordering is not only length-sorted but
        near-optimally so.
    (b) Sign vs Nöldeke: Nöldeke chronology is NOT length-sorted (the
        al-ʿAlaq–al-Qalam opening of Nöldeke chronology is short surahs).
        If L_mushaf << L_nold, that reflects the length-sorted mushaf
        structure more than information-geometric optimality.
    (c) Sign vs length-sorted (descending): if L_mushaf is close to
        L_length_sorted_descending, the mushaf ordering is essentially a
        length-sort and this replication is mechanically confounded.
        If L_mushaf is meaningfully SHORTER than L_length_sorted_descending,
        the mushaf has rhythmic coherence BEYOND pure length-sorting.
        This is the honest discriminator.

### Alternatives considered and rejected pre-result
- Bin edges alternatives: [1,3,6,10,20,40,80,inf] (7 bins); [1,10,20,40,80,inf]
  (5 bins); quantile-based binning (post-hoc-looking, rejected). Chose
  [1,5,10,15,25,40,60,100,inf] for 8 bins matching a log-ish progression with
  enough resolution in the short-verse regime (which is where mufaṣṣal
  rhythm lives).
- Dirichlet α: 0.5 (Jeffreys) matching [[h-new-111-fisher-rao-mushaf|H-NEW-111]] family. Alternatives rejected.
- Metric: Fisher-Rao (same as parent). Fixing this across the family makes
  replication comparable.
- Null: uniform random permutation of 114 surah IDs (not length-stratified
  — which would be bizarre here since length IS the signal).

### Specialist-judgment note on MW-1

Team-lead spec defaults to MW-1-by-residualization at primary level. Here
MW-1-by-residualization would DESTROY the primary signal (removing verse-
length dependence before measuring verse-length-histogram similarity is
incoherent). I interpret MW-1 in its root-spirit: "length is never a free
variable." It is NOT free here — it IS the signal, acknowledged upfront
with the confound caveat above. The L1-normalization of per-surah histograms
does address the "per-surah total-verse-count" confound.

If team-lead disagrees with this specialist override, remedy = demote result
to EXPLORATORY pending a redesigned MW-1 framing, or file a new [[h-new-111c-fisher-rao-verselen|H-NEW-111c]]'
with a different feature. This is disclosed per "Specialist-judgment-overrides-
team-lead" protocol.

## Failure modes

- Positive control fails → INSTRUMENT BROKEN; hold result.
- Primary p ≥ 0.0167 → NULL; surprising given length structure; report with
  equal prominence; the parent [[h-new-111-fisher-rao-mushaf|H-NEW-111]] then remains PASS-DIRECTED on one
  replication ([[h-new-111b-fisher-rao-char-4gram|h-new-111b]]) and fails on this axis.
- Primary passes, ratio ≥ 2.0 → mushaf is shorter-than-random but far from
  optimal even in rhythm space.
- Primary passes with ratio ≈ L_length_sorted_desc / L_2opt ratio → the
  replication is mechanically confounded and provides NO INDEPENDENT EVIDENCE
  for the parent claim. Explicit call-out required in findings file.
- Primary passes AND L_mushaf substantially shorter than L_length_sorted_desc →
  rhythmic coherence exists BEYOND length-sorting; genuine independent
  replication.

## Deliverables
1. Pre-reg (this file).
2. Script `scripts/h_new_111c_fisher_rao_verselen.py` (seed 20260417).
3. JSON `findings/phase-b-hypotheses/csv/h-new-111c.json`.
4. Findings `findings/phase-b-hypotheses/h-new-111c-fisher-rao-verselen.md`.
5. Journal `journal/h-new-111c-run-1.md`.
