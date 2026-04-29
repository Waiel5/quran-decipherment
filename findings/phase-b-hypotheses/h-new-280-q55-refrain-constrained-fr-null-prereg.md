---
id: H-NEW-280
title: "Q55 Fisher-Rao constrained-null salvage: fixed refrain slots, shuffled non-refrain verses"
phase: B
status: PRE-REGISTERED-FOR-BOUNDED-RUN
date: 2026-04-18
specialist: codex
seed: 20260418
parent_backdrop:
  - h-new-127
  - h-new-83
audit_trigger: "OQ-20 follow-up after H-NEW-127's Q55 reversal: smallest honest salvage test is to preserve the 31 refrain slots and shuffle only the 47 non-refrain verses."
scope_note: "Q55 only. This run does not reopen the 5-surah family from H-NEW-127 and cannot by itself promote the broader verse-fractal claim."
rules_tuple: "(Q55 only; no-tashkeel; QAC-STEM root tokens; QAC v0.4; Hafs-Kufan; K=300 top global roots; Dirichlet alpha=0.5; Fisher-Rao angular distance; full 78-verse path length)"
primary_direction: "canonical Q55 path length L_canon < constrained-null random mean when the 31 refrain positions are fixed and only the 47 non-refrain verses are permuted across the 47 non-refrain slots"
alpha_raw: 0.05
perms: 10000
refrain_positions_locked:
  - 13
  - 16
  - 18
  - 21
  - 23
  - 25
  - 28
  - 30
  - 32
  - 34
  - 36
  - 38
  - 40
  - 42
  - 45
  - 47
  - 49
  - 51
  - 53
  - 55
  - 57
  - 59
  - 61
  - 63
  - 65
  - 67
  - 69
  - 71
  - 73
  - 75
  - 77
---

# [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]] - Q55 constrained-null Fisher-Rao salvage

## Question

[[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]'s Q55 result was dominated by a null-model defect specific to
refrain-heavy surahs: under unconstrained full-verse permutation, the 31
near-identical refrain verses can cluster together, making the canonical
alternating structure look artificially long. OQ-20 therefore named the
smallest honest salvage test explicitly:

> keep the 31 refrain positions fixed, shuffle only the 47 non-refrain
> verses across the 47 non-refrain slots, and recompute the same full
> 78-verse Fisher-Rao path length.

This run implements exactly that and nothing broader.

## Relationship to prior work

- `[[h-new-127-verse-fisher-rao-fractal|h-new-127]]` established the original verse-level Fisher-Rao family and
  found Q55 reversed under the unconstrained null (`z = +5.39`,
  `p = 1.0`) while 4 of 5 other surahs passed.
- `[[h-new-83-rahman-refrain-extension|h-new-83]]` locked the refrain operationalization for Q55: exact
  refrain count `31`, first at `v13`, with the full position list used
  here.
- `findings/per-verse-annotations.csv` also tags the same refrain verses
  as `rahman-refrain`; it is corroborative context only, not the primary
  operational definition.

This is an audit-triggered bounded follow-up, not an independent family
replication.

## Hypothesis

**Primary bounded test**:
When the 31 exact refrain slots in Q55 are held fixed, the canonical
ordering of the 47 non-refrain verses is shorter in full 78-verse
Fisher-Rao path length than random constrained permutations of those 47
non-refrain verses.

Operationally:

- `L_canon` is the canonical 78-verse Q55 path length under the same
  Fisher-Rao machinery as [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]].
- `L_perm` is computed on a constrained permutation where:
  - every refrain verse remains in its canonical slot, and
  - the 47 non-refrain verses are uniformly shuffled across the 47
    non-refrain slots.
- Primary p-value:
  `p = (#{L_perm <= L_canon} + 1) / (PERMS + 1)` using the one-sided
  lower-tail convention from [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]].

## Locked method

### Feature space and distance

The feature space is inherited unchanged from [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]:

- QAC v0.4 STEM-root parser
- top `K = 300` global roots
- Dirichlet `alpha = 0.5`
- L1 normalization per verse
- Fisher-Rao angular distance

No alternate `K`, no alternate smoothing, no alternate metric, no block
permutation, and no expansion to other surahs.

### Refrain operationalization

The refrain is defined by exact normalized text match to Q55:13, using
the same normalization logic as [[h-new-83-rahman-refrain-extension|H-NEW-83]]. The extracted positions must
match the locked [[h-new-83-rahman-refrain-extension|H-NEW-83]] list in the YAML frontmatter above. If they do
not, the run is instrument-broken.

### Null construction

For each of `10,000` permutations:

1. Keep the 31 refrain verses in their canonical slots.
2. Shuffle the 47 non-refrain verse identities uniformly.
3. Place those 47 verse identities into the 47 canonical non-refrain
   slots.
4. Compute the full 78-verse path length over adjacent verses.

This null removes the specific refrain-clustering loophole while
preserving the global refrain schedule that defines Q55's architecture.

## Decision rule

- `PASS-BOUNDED` if `p < 0.05` in the pre-registered lower-tail
  direction (`L_canon` significantly shorter than constrained null).
- `NULL` otherwise.

Regardless of p-value, report:

- `z = (L_canon - null_mean) / null_sd`
- whether Q55 remains anti-geodesic under this constrained null
  (`z > 0`) or not (`z <= 0`)

## Scope boundary

This run does **not**:

- reopen the 5-surah [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] family,
- alter [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]'s published verdict,
- test block-preserving nulls,
- test other refrain surahs,
- claim independent replication of the broader OQ-20 fractal hypothesis.

It answers only the narrow Q55 question: does the anti-geodesic reversal
survive once refrain clustering is disallowed?
