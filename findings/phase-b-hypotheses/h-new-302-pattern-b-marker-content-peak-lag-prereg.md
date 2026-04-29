---
id: H-NEW-302
title: Pattern-B marker-versus-content peak-lag test
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-20
agent: codex
parent_1: cross-finding-012
parent_2: cross-finding-017
parent_3: H-NEW-129
open_question: OQ-17 marker-versus-content timing inside the scripture-announcement apparatus
bonferroni_family: h-new-302-pattern-b-peak-lag
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(reuse H-NEW-125 per-surah axis values exactly; reuse cross-finding-012 equal-count Noldke octile bins B1..B8 exactly; marker axis = muq_cardinality; content axes = qul_density, book_reference_density, eschatological_density, loanword_density; for each axis define peak_bin(a) as the smallest octile attaining the maximum observed bin mean; primary statistic L_peak = mean_content peak_bin(a) - peak_bin(marker); null by 10000 permutations of the 114 Noldke ranks across surahs with octile reassignment recomputed each time; one-sided upper-tail for content peaking later than marker; imported-family positive control = exact reproduction of cross-finding-012 observed Pattern-B peak bins under the inherited observed octile mapping)"
direction_primary: "test whether the broader scripture-announcement content apparatus peaks one octile later than the muqattaat marker axis under the already-landed cross-finding-012 sub-bin family"
---

# [[h-new-302-pattern-b-marker-content-peak-lag|H-NEW-302]] - Pattern-B marker-versus-content peak-lag test

## Question

`[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]` already established that the five Pattern-B axes cohere
inside the Noldke octile family, and `[[cross-finding-017-b6-b7-staircase|cross-finding-017]]` sharpened the
descriptive picture to a `B6/B7` staircase:

- `muq_cardinality` peaks at `B6`
- `qul_density`, `book_reference_density`, and `loanword_density` peak at `B7`
- `eschatological_density` remains at `B6`

So the live OQ-17 question is no longer whether the apparatus exists at all.
It is whether the already-noticed asymmetry itself can be formalized:

> does the muqattaat marker layer peak earlier than the broader
> scripture-announcement content layer?

This is a **post-hoc-noticed formalization** of an already disclosed descriptive
pattern, so the strongest honest positive verdict available is
`PASS-DIRECTED`.

## Fixed upstream assets

Reuse exactly:

- `findings/phase-b-hypotheses/csv/h-new-125.json`
- the equal-count octile binning procedure from `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`
- the same 114 surahs and inherited Noldke ranks

No new extractor, no new chronology table, and no new axis family are permitted.

## Locked axes

Marker axis:

- `muq_cardinality`

Content axes:

- `qul_density`
- `book_reference_density`
- `eschatological_density`
- `loanword_density`

## Peak-bin rule

For each axis `a`, compute its mean value in each octile `B1..B8`.

Define:

`peak_bin(a) = smallest bin index attaining max_b mean_a(Bb)`

The smallest-bin tie rule is locked up front.

## Primary statistic

Let:

`content_peaks = {peak_bin(qul), peak_bin(book), peak_bin(eschat), peak_bin(loan)}`

Define:

`L_peak = mean(content_peaks) - peak_bin(muq_cardinality)`

Interpretation:

- `L_peak > 0` means the content layer peaks later than the marker layer
- `L_peak = 0` means no average lag
- `L_peak < 0` means the content layer peaks earlier

## Null

Hold the observed per-surah axis values fixed.

Permute the 114 Noldke ranks across surahs, recompute octile membership under
the inherited equal-count rule, then recompute all peak bins and `L_peak`.

Use:

- `N_perm = 10000`
- seed `20260420`

Primary one-sided upper-tail:

`p_lag = (1 + #{pi : L_peak(pi) >= L_peak(obs)}) / (1 + 10000)`

## Imported-family positive control

Before any permutation inference, verify that the inherited observed octile
mapping reproduces the exact `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]` Pattern-B peak bins:

- `qul_density -> B7`
- `book_reference_density -> B7`
- `eschatological_density -> B6`
- `muq_cardinality -> B6`
- `loanword_density -> B7`

If this reproduction fails, the run is invalid.

## Decision rule

- `PASS-DIRECTED` iff `p_lag < 0.05`
- `NULL` otherwise

## Why this test

This is the highest-EV next OQ-17 move because:

1. it directly formalizes the already-noticed `B6/B7` asymmetry
2. it stays inside the strongest surviving chronology family after
   `[[h-new-129-joint-late-meccan-peak|H-NEW-129]]` failed
3. it asks a principle-level timing question without inventing any new feature
   families or chronology tables

## Honest limits

1. This is a post-hoc formalization of a descriptive asymmetry, not a
   discovery-clean new branch.
2. A pass would certify only a peak-lag inside the inherited octile family, not
   a full causal explanation of why the lag exists.
3. The null tests timing asymmetry under rank reassignment, not the broader
   truth of the scripture-announcement apparatus, which was already handled by
   `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`.

## Deliverables

- Script: `scripts/h_new_302_pattern_b_peak_lag.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-302.json`
- Findings: `findings/phase-b-hypotheses/h-new-302-pattern-b-marker-content-peak-lag.md`
- Journal: `journal/h-new-302-run-1.md`
