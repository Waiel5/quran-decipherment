---
id: H-NEW-271-5
title: Empirical-table minimal singleton-rescue search over H-NEW-271's mean_manner axis
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-271
parent_2: H-NEW-271-2
parent_3: H-NEW-274
open_question: OQ-1 at the singleton layer under empirical-table minimal 2-D rescue
seed: 20260419
n_perm: 1000
bonferroni_family: h-new-271-5-empirical-singleton-rescue
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(canonical 29 muq surahs; locked H-NEW-271 deduplicated phonological feature pool; anchor mean_manner retained in every candidate; exactly 9 one-feature augmentations by the remaining phonological axes only; accepted-cluster table updated only by the locked H-NEW-274 empirical replacements YS->HM and HMASQ->TSM; z-scored against the 19 multi-member surahs only; 2-D Euclidean nearest-centroid primary; nearest multi-member surah reported descriptively; best augmentation selected by maximum singleton-match count with preregistered tie-break on total nearest-centroid distance then lexicographic augmentation name; familywise maxT label-shuffle null across all 9 candidates; seed 20260419)"
direction_primary: "determine whether any minimal 2-D augmentation of mean_manner survives correction once the singleton accepted table is updated to the stronger H-NEW-274 empirical version"
---

# [[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]] - Empirical-table minimal singleton rescue over the `mean_manner` axis

## Question

`[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` asked whether any one-feature augmentation of `mean_manner`
could rescue the singleton layer under the inherited `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` accepted
cluster table. The best pair reached `8 / 10`, but the familywise
correction stayed non-significant (`p_maxT = 0.0899`).

`[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` then materially sharpened the interpretation table itself. Using
`[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` as discovery and four locked holdout spaces for evaluation, it
showed that the stronger accepted table is:

- `YS -> HM`
- `HMASQ -> TSM`

This finding asks the next bounded question:

> Was the `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` compact-rescue failure mainly an artifact of the
> weaker inherited singleton table, or does the compact-rescue line still fail
> even under the stronger `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` empirical table?

The geometry and candidate family stay fixed. Only the accepted-cluster table
changes, and only by the two locked `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` replacements.

## Locked feature universe

The source feature inventory is the same deduplicated phonological pool locked
in `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]`:

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

### Locked anchor

Every candidate model must contain:

- `mean_manner`

### Locked augmentation pool

The only allowed augmentations are the remaining 9 phonological axes:

1. `mean_makhraj`
2. `mean_voice`
3. `mean_emphatic`
4. `mean_pharyngeal`
5. `mean_sonorant`
6. `mean_continuant`
7. `mean_idhlaq`
8. `mean_vowel_carrier`
9. `has_qalqala`

The 9 tested pairs are therefore exactly:

1. `mean_manner + mean_makhraj`
2. `mean_manner + mean_voice`
3. `mean_manner + mean_emphatic`
4. `mean_manner + mean_pharyngeal`
5. `mean_manner + mean_sonorant`
6. `mean_manner + mean_continuant`
7. `mean_manner + mean_idhlaq`
8. `mean_manner + mean_vowel_carrier`
9. `mean_manner + has_qalqala`

### Exclusions

The following remain excluded by lock:

- `letter_count`
- duplicate fraction columns
- any 3-D or larger subset
- any metric other than the inherited Euclidean nearest-centroid geometry

## Locked target and scoring

The target is the exact `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` singleton propagation task, except that
the accepted-cluster table is replaced by the locked `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` empirical
version:

- `ALMS -> {ALM}`
- `ALMR -> {ALM, ALR}`
- `KHYAS -> {HM, TSM}`
- `TH -> {TSM}`
- `TS -> {TSM}`
- `YS -> {HM}`
- `S -> {TSM}`
- `HMASQ -> {TSM}`
- `Q -> {HM, TSM}`
- `N -> {ALM, ALR}`

For each candidate pair:

1. Build the 2-D feature matrix from the locked `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` codebook.
2. Split the 29 canonical muq surahs into:
   - 19 multi-member reference surahs
   - 10 singleton query surahs
3. Z-score using the 19 multi-member surahs only.
4. Compute the four multi-member centroids: `ALM`, `ALR`, `HM`, `TSM`.
5. Assign each singleton to its nearest centroid in the 2-D z-space.
6. Count a singleton as a hit iff the assigned centroid belongs to its locked
   accepted set above.
7. Also report nearest multi-member surah descriptively.

Primary per-candidate statistic:

- singleton hit count out of 10

Secondary descriptive quantity:

- total nearest-centroid distance across the 10 singletons

## Candidate-selection rule

The inferential unit is the best-performing augmentation chosen from the 9
locked candidates.

Ranking is pre-registered:

1. higher singleton hit count
2. if tied, smaller total nearest-centroid distance
3. if still tied, lexicographically earlier augmentation name

## Null model

Familywise maxT null:

1. Shuffle the 19 multi-member cluster labels while preserving the observed
   label multiset.
2. For each shuffled labeling, recompute the 4 centroids for all 9 locked
   candidate pairs.
3. For each candidate pair, recompute the singleton hit count.
4. Record the maximum singleton hit count attained by any candidate pair under
   that shuffle.
5. Repeat `n_perm = 1000`.

Corrected p-value:

`p_maxT = (1 + # perms with max_hits >= observed_best_hits) / (n_perm + 1)`

## Decision rules

### Full restoration

`EMPIRICAL-H232-LEVEL-RESTORED` iff:

1. the best candidate attains `>= 8 / 10` singleton hits, and
2. `p_maxT < 0.05`

### Significant but sub-baseline rescue

`EMPIRICAL-SIGNIFICANT-PARTIAL-RESCUE` iff:

1. the best candidate attains `>= 6 / 10` singleton hits, and
2. `p_maxT < 0.05`,
3. but the full restoration rule above is not met

### No rescue

`NO-MAXT-EMPIRICAL-RESCUE` otherwise.

## Expected outcome

The bounded expectation is open:

- if the weaker inherited table was the main blocker, the best pair may
  strengthen materially here
- if compact rescue still fails, that failure is more decisive than before,
  because it will have survived the move to the stronger `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]`
  accepted-cluster table

## Deliverables

- Script: `scripts/h_new_271_5_empirical_table_singleton_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-5.json`
- Findings: `findings/phase-b-hypotheses/h-new-271-5-empirical-table-singleton-rescue.md`
- Journal: `journal/h-new-271-5-run-1.md`
