---
id: H-NEW-271-2
title: Minimal singleton-rescue search over H-NEW-271's mean_manner axis
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-271
parent_2: H-NEW-271-1
parent_3: H-NEW-232
open_question: OQ-1 at the singleton layer under minimal 2-D rescue
seed: 20260419
n_perm: 1000
bonferroni_family: h-new-271-2-singleton-rescue
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(canonical 29 muq surahs; locked H-NEW-271 deduplicated phonological feature pool; anchor mean_manner retained in every candidate; exactly 9 one-feature augmentations by the remaining phonological axes only; H-NEW-232 accepted-cluster sets reused verbatim; z-scored against the 19 multi-member surahs only; 2-D Euclidean nearest-centroid primary; nearest multi-member surah reported descriptively; best augmentation selected by maximum singleton-match count with preregistered tie-break on total nearest-centroid distance then lexicographic augmentation name; familywise maxT label-shuffle null across all 9 candidates; seed 20260419)"
direction_primary: "determine whether any minimal 2-D augmentation of mean_manner restores the H-NEW-232 singleton propagation level or otherwise yields a familywise-significant rescue"
---

# [[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]] - Minimal singleton rescue over the `mean_manner` axis

## Question

`[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` established that the muq multi-member cluster ceiling can be
recovered by the single phonological axis `mean_manner`.

`[[h-new-271-1-manner-singleton|H-NEW-271.1]]` then showed that the singleton layer does **not** survive that
1-D collapse:

- `5 / 10` singleton matches against the locked `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` accepted sets
- `p_perm = 0.41`
- verdict: `MULTI-DIM-REQUIRED-AT-SINGLETONS`

This finding asks the next bounded question:

> If `mean_manner` is kept fixed as the anchor axis, can **one additional
> phonological feature** from the locked `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` codebook rescue the
> singleton geometry?

The task is deliberately narrow. It does **not** reopen the full subset-search
problem. It asks only whether a minimal 2-D augmentation can recover what the
1-D collapse lost.

## Locked feature universe

The source feature inventory is the deduplicated phonological pool already
locked in `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]`:

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

The following are excluded by lock:

- `letter_count` (non-phonological scaffold; not allowed here)
- duplicate fraction columns (`frac_emphatic`, `frac_pharyngeal`,
  `frac_sonorant`, `frac_idhlaq`)
- any 3-D or larger subset
- any metric other than the inherited Euclidean nearest-centroid geometry

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

For each candidate pair:

1. Build the 2-D feature matrix from the locked `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]` codebook.
2. Split the 29 canonical muq surahs into:
   - 19 multi-member reference surahs
   - 10 singleton query surahs
3. Z-score using the 19 multi-member surahs only.
4. Compute the four multi-member centroids: `ALM`, `ALR`, `HM`, `TSM`.
5. Assign each singleton to its nearest centroid in the 2-D z-space.
6. Count a singleton as a hit iff the assigned centroid belongs to its locked
   `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` accepted set.
7. Also report nearest multi-member surah descriptively for comparability with
   `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` / `[[h-new-271-1-manner-singleton|H-NEW-271.1]]`.

Primary per-candidate statistic:

- singleton hit count out of 10

Secondary descriptive quantity:

- total nearest-centroid distance across the 10 singletons

## Candidate-selection rule

The inferential unit is the **best-performing augmentation** chosen from the 9
locked candidates.

Ranking is pre-registered:

1. higher singleton hit count
2. if tied, smaller total nearest-centroid distance
3. if still tied, lexicographically earlier augmentation name

This tie-break affects only the reported canonical winner. The p-value is based
on the primary hit-count statistic only.

## Null model

Familywise maxT null:

1. Shuffle the 19 multi-member cluster labels while preserving the observed
   label multiset.
2. For each shuffled labeling, recompute the 4 centroids for **all 9 locked
   candidate pairs**.
3. For each candidate pair, recompute the singleton hit count.
4. Record the **maximum** singleton hit count attained by any candidate pair
   under that shuffle.
5. Repeat `n_perm = 1000`.

Corrected p-value:

`p_maxT = (1 + # perms with max_hits >= observed_best_hits) / (n_perm + 1)`

This is the inferential correction for searching over the 9 possible
augmentations.

## Decision rules

### Full restoration

`[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]-LEVEL-RESTORED` iff:

1. the best candidate attains `>= 8 / 10` singleton hits, and
2. `p_maxT < 0.05`

### Significant but sub-baseline rescue

`SIGNIFICANT-PARTIAL-RESCUE` iff:

1. the best candidate attains `>= 6 / 10` singleton hits, and
2. `p_maxT < 0.05`,
3. but the full restoration rule above is not met

### No rescue

`NO-MAXT-RESCUE` otherwise.

The `>= 6 / 10` bar is locked as the minimal rescue threshold because it is the
smallest strict improvement over the `[[h-new-271-1-manner-singleton|H-NEW-271.1]]` collapse (`5 / 10`) while
still clearing a majority of singleton cases.

## Expected outcome

The bounded expectation is modest:

- some 2-D augmentations may improve on the 1-D `mean_manner` collapse
- but a full return to the `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` level (`8 / 10`) is not assumed

This finding is intended to answer the minimal-rescue question honestly, not to
force a parsimony claim beyond what the singleton layer will support.

## Deliverables

- Script: `scripts/h_new_271_2_minimal_singleton_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-2.json`
- Findings: `findings/phase-b-hypotheses/h-new-271-2-minimal-singleton-rescue.md`
- Journal: `journal/h-new-271-2-run-1.md`
