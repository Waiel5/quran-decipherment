---
id: H-NEW-271-3
title: Anchored 3-D singleton rescue after H-NEW-271.2
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-271
parent_2: H-NEW-271-2
parent_3: H-NEW-232
open_question: OQ-1 at the singleton layer under anchored 3-D rescue
seed: 20260419
n_perm: 1000
bonferroni_family: h-new-271-3-anchored-3d-singleton-rescue
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(canonical 29 muq surahs; locked H-NEW-271 deduplicated phonological feature pool; fixed anchor pair mean_manner + mean_vowel_carrier inherited from H-NEW-271.2 best raw pair; exactly 8 one-feature phonological augmentations from the remaining pool only; H-NEW-232 accepted-cluster sets reused verbatim; z-scored against the 19 multi-member surahs only; 3-D Euclidean nearest-centroid primary; nearest multi-member surah reported descriptively; best augmentation selected by singleton hit count with preregistered tie-break on total nearest-centroid distance then lexicographic augmentation name; familywise maxT label-shuffle null across all 8 anchored triples; seed 20260419)"
direction_primary: "determine whether adding exactly one further phonological axis to the fixed H-NEW-271.2 best raw pair yields a familywise-significant 3-D rescue of the singleton layer"
---

# [[h-new-271-3-anchored-3d-singleton-rescue|H-NEW-271.3]] - Anchored 3-D singleton rescue after `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`

## Question

`[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` showed that the muq multi-member cluster ceiling can collapse to the
single phonological axis `mean_manner`.

`[[h-new-271-1-manner-singleton|H-NEW-271.1]]` then showed that this 1-D collapse does not preserve the
singleton layer:

- `5 / 10` singleton matches
- `p_perm = 0.41`
- verdict: `MULTI-DIM-REQUIRED-AT-SINGLETONS`

`[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` supplied the first bounded repair:

- best raw pair = `mean_manner + mean_vowel_carrier`
- best hits = `8 / 10`
- corrected `p_maxT = 0.0899100899100899`
- verdict: `NO-MAXT-RESCUE`

So the next bounded question is:

> If the `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` best raw pair is locked as the anchor, does adding
> exactly one further phonological axis from the remaining pool produce a 3-D
> singleton rescue that survives proper familywise correction?

This finding does not reopen the 2-D search and does not allow arbitrary
subset growth. It asks only whether the anchored 2-D geometry can be completed
by one more phonological axis.

## Locked feature universe

The source inventory is the deduplicated phonological pool already locked in
`[[h-new-271-muq-minimal-phon-family|H-NEW-271]]`:

1. `mean_makhraj`
2. `mean_voice`
3. `mean_manner`
4. `mean_emphatic`
5. `mean_pharyngeal`
6. `mean_sonorant`
7. `mean_continuant`
8. `mean_idhlaq`
9. `mean_vowel_carrier`
10. `has_qalqala`

### Fixed anchor pair

Every candidate triple must contain the exact `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` best raw pair:

1. `mean_manner`
2. `mean_vowel_carrier`

### Locked augmentation pool

The only legal third-axis augmentations are the remaining 8 phonological axes:

1. `mean_makhraj`
2. `mean_voice`
3. `mean_emphatic`
4. `mean_pharyngeal`
5. `mean_sonorant`
6. `mean_continuant`
7. `mean_idhlaq`
8. `has_qalqala`

The 8 tested triples are therefore exactly:

1. `mean_manner + mean_vowel_carrier + mean_makhraj`
2. `mean_manner + mean_vowel_carrier + mean_voice`
3. `mean_manner + mean_vowel_carrier + mean_emphatic`
4. `mean_manner + mean_vowel_carrier + mean_pharyngeal`
5. `mean_manner + mean_vowel_carrier + mean_sonorant`
6. `mean_manner + mean_vowel_carrier + mean_continuant`
7. `mean_manner + mean_vowel_carrier + mean_idhlaq`
8. `mean_manner + mean_vowel_carrier + has_qalqala`

### Exclusions

The following are excluded by lock:

- `letter_count`
- duplicate fraction columns (`frac_emphatic`, `frac_pharyngeal`,
  `frac_sonorant`, `frac_idhlaq`)
- any attempt to replace either anchor axis
- any 4-D or larger subset
- any metric other than inherited Euclidean nearest-centroid geometry

## Locked target and scoring

The target is the exact `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` singleton propagation task, using the
accepted-cluster sets verbatim:

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

For each candidate triple:

1. Build the 3-D feature matrix from the locked `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` codebook.
2. Split the 29 canonical muq surahs into:
   - 19 multi-member reference surahs
   - 10 singleton query surahs
3. Z-score using the 19 multi-member surahs only.
4. Compute the four multi-member centroids: `ALM`, `ALR`, `HM`, `TSM`.
5. Assign each singleton to its nearest centroid in 3-D z-space.
6. Count a singleton as a hit iff the assigned centroid belongs to its locked
   `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` accepted set.
7. Also report nearest multi-member surah descriptively for comparability with
   `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]`, `[[h-new-271-1-manner-singleton|H-NEW-271.1]]`, and `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`.

Primary per-candidate statistic:

- singleton hit count out of 10

Secondary descriptive quantity:

- total nearest-centroid distance across the 10 singletons

## Candidate-selection rule

The inferential unit is the best-performing anchored triple chosen from the 8
locked candidates.

Ranking is pre-registered:

1. higher singleton hit count
2. if tied, smaller total nearest-centroid distance
3. if still tied, lexicographically earlier augmentation name

This tie-break affects only the reported canonical winner. The corrected
p-value is based on the primary hit-count statistic only.

## Null model

Familywise maxT null:

1. Shuffle the 19 multi-member cluster labels while preserving the observed
   label multiset.
2. For each shuffled labeling, recompute the 4 centroids for all 8 locked
   candidate triples.
3. For each candidate triple, recompute the singleton hit count.
4. Record the maximum singleton hit count attained by any candidate triple
   under that shuffle.
5. Repeat `n_perm = 1000`.

Corrected p-value:

`p_maxT = (1 + # perms with max_hits >= observed_best_hits) / (n_perm + 1)`

This is the inferential correction for searching over the 8 legal third-axis
augmentations.

## Decision rules

### Significant 3-D improvement

`SIGNIFICANT-3D-IMPROVEMENT` iff:

1. the best triple attains `> 8 / 10` singleton hits, and
2. `p_maxT < 0.05`

### Significant 3-D rescue

`SIGNIFICANT-3D-RESCUE` iff:

1. the best triple attains `>= 8 / 10` singleton hits, and
2. `p_maxT < 0.05`,
3. but the improvement rule above is not met

### No rescue

`NO-MAXT-3D-RESCUE` otherwise.

This is deliberately stricter than a raw comparison to `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`. The
claim only passes if the anchored 3-D family survives its own familywise null.

## Expected outcome

The bounded expectation is narrow:

- some anchored triples may tie or slightly improve on the `8 / 10` raw result
  from `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`
- but a formal 3-D rescue is not assumed

This follow-up is meant to answer whether compact closure exists at 3-D, not to
force one.

## Deliverables

- Script: `scripts/h_new_271_3_anchored_3d_singleton_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-3.json`
- Findings: `findings/phase-b-hypotheses/h-new-271-3-anchored-3d-singleton-rescue.md`
- Journal: `journal/h-new-271-3-run-1.md`
