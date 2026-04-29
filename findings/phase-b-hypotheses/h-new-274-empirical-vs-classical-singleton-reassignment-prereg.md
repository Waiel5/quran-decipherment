---
id: H-NEW-274
title: Empirical-vs-classical a-priori reassignment test for Q36 YS and Q42 HMASQ
phase: B
status: PRE-REGISTERED
date: 2026-04-18
agent: codex
parent_1: H-NEW-232
parent_2: H-NEW-252
parent_3: H-NEW-165.2
open_question: OQ-1 singleton interpretation
rules_tuple: "(discovery source locked to h-new-232.json only; empirical replacements locked to discovery nearest-centroid assignments for YS and HMASQ only; holdout spaces locked to h-new-252 joint 17-dim and h-new-165.2 V1/V2/V3; paired 40-cell classical-vs-empirical table comparison; exact one-sided discordant-cell binomial test; alpha_primary=0.025)"
alpha_primary: 0.025
direction: "empirical reassignment table should outperform the inherited classical table on holdout singleton-account cells without any holdout-space regression"
verdict: PENDING
---

# [[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]] — empirical-vs-classical a-priori reassignment test

## Question

[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] established an 8/10 singleton nearest-centroid account under the
classical accepted-cluster table inherited from classical tajwīd reasoning. The
two misses were:

- Q 36 `YS`: observed nearest centroid `HM`, classical accepted set `{ALM, ALR}`
- Q 42 `HMASQ`: observed nearest centroid `TSM`, classical accepted set `{HM}`

[[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]] and [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] then reproduced those same two disagreements across
independent feature formulations. That raises a tighter question:

**Is the singleton-layer account materially stronger if those two disputed
accepted-cluster entries are replaced by their empirical nearest-cluster
assignments?**

This finding does not retest the phonological geometry itself. It tests the
competing **interpretation tables** laid on top of that geometry.

## Competing tables (locked before execution)

### Table C — classical inherited table

Copied verbatim from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] / [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]:

- `ALMS -> {ALM}`
- `ALMR -> {ALM, ALR}`
- `KHYAS -> {HM, TSM}`
- `TH -> {TSM}`
- `TS -> {TSM}`
- `YS -> {ALM, ALR}`
- `S -> {TSM}`
- `HMASQ -> {HM}`
- `Q -> {HM, TSM}`
- `N -> {ALM, ALR}`

### Table E — empirical replacement table

Start from Table C and replace only the two disputed singleton entries:

- `YS -> {HM}`
- `HMASQ -> {TSM}`

All other singleton entries remain unchanged.

## Discovery / holdout split (locked)

### Discovery source

Only one artifact is allowed to define the empirical replacements:

- `findings/phase-b-hypotheses/csv/h-new-232.json`

Specifically, the replacements are taken from the discovery artifact's
`nearest_centroid_cluster` field for:

- `YS`
- `HMASQ`

No other prior artifact may alter Table E.

### Holdout evaluation spaces

The primary test scores Tables C and E only on these four locked holdout spaces:

1. `[[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]` joint 17-dim space:
   `findings/phase-b-hypotheses/csv/h-new-252.json -> joint_results`
2. `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` V1 Watson modern voice:
   `variants[id=watson_modern_voice]`
3. `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` V2 strict pharyngeal split:
   `variants[id=strict_pharyngeal_split]`
4. `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` V3 Holes glottal ha/ayn:
   `variants[id=holes_glottal_ha_ayn]`

Excluded by design:

- `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` baseline discovery space from primary scoring
- `[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]` baseline V0 because it is the same geometry family as the
  discovery baseline
- `[[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]` phon-only replication because it duplicates the discovery-space
  family without adding a new feature formulation

## Primary outcome

Unit of analysis: **singleton-space cell**.

- 10 singleton rows per holdout space
- 4 holdout spaces
- total primary cell count = `40`

For each cell, score:

- `match_C = 1` if the space's nearest centroid lies in Table C's accepted set
- `match_E = 1` if the same nearest centroid lies in Table E's accepted set

Primary statistic:

- exact one-sided binomial test on the **discordant** cells only
- success = `E improves where C fails`
- failure = `C matches where E fails`
- null = symmetric directional advantage (`p = 0.5`) over discordant cells

## Materiality rule (locked)

Table E is considered **materially stronger** only if all three conditions hold:

1. `delta_matches_holdout = total_E - total_C >= 6`
2. `worsened_cells = 0`
3. exact one-sided discordant-cell `p < 0.025`

Rationale:

- maximum possible gain is 8 cells (`2 disputed singletons x 4 holdout spaces`)
- requiring `>= 6` forbids calling a tiny or unstable edge "material"
- requiring zero regressions prevents a trade-one-win-one-loss verdict

## Secondary descriptive output

This is reported descriptively and does not affect the verdict.

### Distance-margin check

For each holdout space compute:

- `YS empirical margin = min(d(ALM), d(ALR)) - d(HM)`
- `HMASQ empirical margin = d(HM) - d(TSM)`

Positive values mean the empirical replacement is geometrically closer than the
classical alternative set.

## Decision rule

- `PASS-HOLDOUT-STRONGER`:
  all three primary materiality conditions pass
- `PARTIAL`:
  `delta_matches_holdout > 0` but at least one primary condition fails
- `NULL`:
  `delta_matches_holdout <= 0`

## Garden-of-forking-paths locks

1. Discovery is locked to `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` only.
2. Only `YS` and `HMASQ` may be replaced.
3. Replacement sets are single-cluster sets, not widened unions.
4. No alternate replacement-table families are evaluated.
5. Holdout spaces are locked to the four artifacts above.
6. No new feature spaces, distances, or nulls are introduced.
7. Primary inference uses the discordant-cell exact binomial only.
8. Distance margins are descriptive only.

## Honest limits

1. This is a **meta-evaluation of interpretation tables**, not a new raw-feature
   discovery. It inherits the earlier geometries.
2. The four holdout spaces are not independent corpora; they are alternate
   feature formulations on the same 29 muq surahs.
3. Table E is discovery-derived from `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]`; it can only claim holdout
   replication across related spaces, not independent scripture-level
   confirmation.

## Files

- Pre-reg: this file
- Script: `scripts/h_new_274_empirical_vs_classical_singleton_reassignment.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-274.json`
- Findings: `findings/phase-b-hypotheses/h-new-274-empirical-vs-classical-singleton-reassignment.md`
- Journal: `journal/h-new-274-run-1.md`
