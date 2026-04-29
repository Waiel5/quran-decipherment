# H-NEW-126 Run 1 — Journal

**Date**: 2026-04-17
**Agent**: h-new-126-specialist
**Seed**: 20260417
**N_PERM**: 10,000
**Bonferroni**: k=4, α_bon=0.0125
**Family**: h-new-126-isolate-core

## Task

Characterize the 5-surah true-isolate-core {Q 16, 21, 22, 23, 25}
identified by cross-finding-010 as surviving as isolates under ALL 20
cluster systems. What unites them? What separates them from every
other surah?

## Workflow

1. Read HANDOFF/01-WHAT-WE-KNOW.md, HANDOFF/04-DISCIPLINE.md,
   cross-finding-010 in full.
2. Read the H-NEW-94 script (similar Q 16-25 zone deep-dive) for
   conventions: path handling, morphology root-graph, random-window null.
3. Read H-NEW-125 pre-reg for 15-axis chronology-content map — borrowed
   operational definitions for Allah-density, prophet-narrative density.
4. Inspected `data/morphology/surah-root-graph.json` — confirmed
   `{surah_id: {root: count}}` structure, 1642 distinct roots total.
5. Confirmed `data/revelation-order.csv` has `noldeke_order` column (1..114).
6. Wrote pre-reg with YAML frontmatter declaring `bonferroni_k=4`,
   `alpha_bon=0.0125`, per-cell direction locks, and explicit post-hoc
   disclosure (single-test α=0.05 cap).
7. Wrote script implementing Cell A (root-Jaccard), Cell B (descriptive),
   Cell C (imp/int/dec 3-vector), Cell D (9-axis profile).
8. Used independent RNGs (SEED+1, SEED+3) per cell to avoid
   cross-contamination.
9. Ran script; elapsed ~2.2s.
10. Wrote findings file with per-cell tables, synthesis, honest NULL
    disclosure for Cell C.

## Key choices pre-registered

- Bonferroni k=4 (conservative; Cells B and D descriptive, but kept
  k=4 in the family for Bonferroni-tightening not loosening per asymmetry rule)
- Cell A null: random 5-sets from 109 non-core surahs (direct
  exchangeability for 5-tuples)
- Cell C null: random 5-sets in imp/int/dec space; one-sided lower
  (core expected tight)
- MW-5 pre-selected: ḥawāmīm for Cell A, musabbiḥāt for Cell C

## Cell A result

**PASS-DIRECTED** at p=0.0009. Observed mean pairwise root-Jaccard
0.3414 vs null mean 0.1291 (2.64× enrichment). MW-5 ḥawāmīm fires at
p=0.0046 (confirms the null is a valid detector).

Verdict ceiling is PASS-DIRECTED (not CONFIRMED) due to post-hoc
subset provenance.

## Cell B result

**DESCRIPTIVE — 5/5 concept-or-object-named.** Pre-committed
classification all verified:
- Q 16 al-Naḥl = object (Bee)
- Q 21 al-Anbiyāʾ = concept (Prophets)
- Q 22 al-Ḥajj = concept (Pilgrimage)
- Q 23 al-Muʾminūn = concept (Believers)
- Q 25 al-Furqān = concept (Criterion)

Genre-coherent.

## Cell C result

**NULL-BROKEN.** MW-5 positive control failed: the classically-verified
tight cluster musabbiḥāt inner-5 {Q 57, 59, 61, 62, 64} does NOT
cluster tight in imp/int/dec space (p=0.67, obs=16.08 vs null=14.53).

This failed despite the target 5-core showing dramatic directional
tightness (p=0.0157, obs=5.32 vs null=14.83 — 2.8× tighter than null).

Per pre-reg, MW-5 failure → Cell C NULL-BROKEN regardless of target
result. The 3-vector is too coarse for rhetorical-mode fingerprinting.

Honest NULL publication with same prominence as Cell A PASS.

## Cell D result

**DESCRIPTIVE.** Each core surah's most-distinctive axis (vs 114-surah corpus):

| Surah | Axis | Direction | Percentile |
|---|---|---|---|
| 16 al-Naḥl | unique_root_count | HIGH | 92.5 |
| 21 al-Anbiyāʾ | surah_length | HIGH | 88.2 |
| 22 al-Ḥajj | noldeke_rank | HIGH | 93.4 (late-Medinan) |
| 23 al-Muʾminūn | surah_length | HIGH | 89.0 |
| 25 al-Furqān | unique_root_count | HIGH | 78.5 |

All 5 at HIGH percentile extremes — the core is MAXIMALIST not MINIMALIST.

## Synthesis

The 5-core is CONCEPT-NAMED, LONG, CHRONOLOGICALLY-SCATTERED,
ROOT-VOCAB-SHARING — a kernel of abstract-argumentative Meccan (+1
Medinan) discourse invisible to opener/name/cluster taxonomies.

## Followups queued

- H-NEW-126.1: Cell A with length-matched null (length-bucketed 5-sets)
- H-NEW-126.2: Cell A with char 5-gram Dice and H-NEW-66 verse-twin
  similarity (independent replication for CONFIRMED status)
- H-NEW-126.3: finer rhetorical-mode axis (Cell C redesign)

## Honest caveats published

- Post-hoc subset (5-core from cross-finding-010)
- Length confound (3/5 core are long Meccan)
- Cell C NULL-BROKEN (MW-5 failed)
- PASS-DIRECTED ceiling until independent replication

## Integrity

- Seed 20260417 locked in YAML
- Directions locked BEFORE viewing null
- MW-5 failure disclosed (not suppressed)
- Garden-of-forking-paths logged in pre-reg
- Bonferroni-4 is tightening (self-verifying)

## Elapsed

~2.2s script runtime; ~30min total including pre-reg authoring and
findings write-up.
