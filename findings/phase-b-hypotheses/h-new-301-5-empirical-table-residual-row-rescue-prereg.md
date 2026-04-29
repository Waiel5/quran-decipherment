---
id: H-NEW-301-5
title: Empirical-table residual-row rescue over the 55-pair singleton family
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-301
parent_2: H-NEW-271-5
parent_3: H-NEW-274
open_question: OQ-1 empirical-table residual compact burden on YS and N
seed: 20260425
n_perm: 20000
bonferroni_family: h-new-301-5-empirical-residual-row-rescue
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(29 canonical muq surahs; same 11-feature pool and same C(11,2)=55 pair family as H-NEW-301; accepted singleton table switched only to the locked H-NEW-274 empirical version; primary endpoint restricted to the two live residual rows YS and N only; candidate pairs ranked by rescued-row count over {YS,N}, then by summed positive accepted-vs-rejected centroid margin over {YS,N}, then lexicographic pair label; 2-D Euclidean nearest-centroid geometry with z-scoring against the 19 multi-member surahs only; familywise maxT label-shuffle null across the same 55-pair family; seed 20260425)"
direction_primary: "determine whether any 2-feature pair rescues both empirical-table residual rows YS and N and whether the best targeted rescue is rare under the 55-pair maxT null"
---

# [[h-new-301-5-empirical-table-residual-row-rescue|H-NEW-301.5]] - Empirical-table residual-row rescue over the `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` pair family

## Question

`[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` tightened the OQ-1 singleton residue under the stronger
`[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` accepted-cluster table:

- `YS -> HM`
- `HMASQ -> TSM`

Under that stronger table, the best compact `mean_manner`-anchored 2-D rescue
still failed familywise correction and the live blockers became exactly:

- `YS`
- `N`

This finding asks the next honest bounded question:

> If the inferential target is narrowed to the two surviving empirical-table
> residual rows only, does the same 55-pair compact search family from
> `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` contain a pair that rescues both `YS` and `N` in a way that
> survives a full 55-pair maxT null?

This is not a new generic singleton search. It is a targeted residual-row
adjudication.

## Locked feature family

The feature family is inherited exactly from `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]`:

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
11. `letter_count`

All `C(11, 2) = 55` unordered pairs are tested.

No new features, no anchor restriction, and no metric changes are permitted.

## Locked accepted table

The accepted-cluster table is the locked empirical table from `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]`:

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

## Locked target rows

Only two rows are inferentially targeted:

- `YS`
- `N`

All other singleton rows remain descriptive context only.

## Geometry

For each of the 55 candidate pairs:

1. Build the 2-D feature matrix for the 29 canonical muq surahs.
2. Split into:
   - 19 multi-member reference surahs
   - 10 singleton query surahs
3. Z-score each feature using the 19 multi-member surahs only.
4. Compute the four multi-member centroids:
   - `ALM`
   - `ALR`
   - `HM`
   - `TSM`
5. For each singleton, compute Euclidean distance to each centroid.

The nearest accepted cluster is descriptive only.

## Primary targeted statistic

For each target row `s` in `{YS, N}` and each candidate pair `p`, define:

- accepted set `A_s`
- centroid distance `d_s(c)` to cluster `c`
- accepted-vs-rejected margin

`m_s(p) = min_{c not in A_s} d_s(c) - min_{a in A_s} d_s(a)`

Interpretation:

- `m_s(p) > 0` means the best accepted centroid is strictly closer than every
  rejected centroid
- `m_s(p) = 0` means an exact boundary tie
- `m_s(p) < 0` means some rejected centroid beats the accepted set

Define for each pair `p`:

- targeted rescue count

`R(p) = sum_{s in {YS, N}} 1[m_s(p) > 0]`

- summed positive targeted margin

`M+(p) = sum_{s in {YS, N}} max(m_s(p), 0)`

Candidate ranking is pre-registered:

1. larger `R(p)`
2. if tied, larger `M+(p)`
3. if still tied, lexicographically earlier pair label

The observed best pair is the top-ranked pair under this rule.

## Secondary descriptive outputs

These are reported but not used in the inferential decision:

- total singleton hit count out of 10 under the empirical table
- per-singleton nearest centroid table for the observed best pair
- number of 55 pairs achieving `R(p) = 2`
- highest total-hit score among pairs with `R(p) = 2`

## Null model

Familywise maxT null over the same 55-pair search family:

1. Shuffle the 19 multi-member cluster labels while preserving the observed
   cluster-size multiset.
2. For each shuffle, recompute the four centroids for every one of the 55
   candidate pairs.
3. For each pair, recompute the targeted tuple `(R(p), M+(p))`.
4. Record the permutation maximum under the same lexicographic ranking rule.
5. Repeat `n_perm = 20000`.

Corrected p-value:

`p_maxT = (1 + # perms with T_null >= T_obs) / (n_perm + 1)`

where the comparison is lexicographic on:

- first `R`
- then `M+`

Diagnostic only:

- `p_count_only = (1 + # perms with max_R_null >= R_obs) / (n_perm + 1)`

This diagnostic reports how uninformative the row-count alone is once the
55-pair search is honored.

## Decision rules

Define:

- Cell A PASS iff the observed best pair has `R_obs = 2`
- Cell B PASS iff `p_maxT < 0.05`

Verdict table:

| Cell A | Cell B | Verdict |
|---|---|---|
| PASS | PASS | `TARGETED-RESIDUAL-RESCUE` |
| PASS | FAIL | `DESCRIPTIVE-ONLY` |
| FAIL | any | `NULL` |

## Expected reading

Two very different outcomes are possible:

1. If both rows are rescued but the maxT null is loose, then the result is
   only descriptive and OQ-1 remains stuck on a small-N targeted residue.
2. If both rows are rescued and the lexicographic maxT null is strong, then
   the residual compact burden is no longer diffuse. It is carried by a
   specific 2-D low-dimensional subproblem that can now be isolated honestly.

## Honest limits

1. This finding does **not** ask for a full compact 10-singleton closure.
2. The margin-based tie-break is load-bearing; count-only rescue may be very
   common under the 55-pair search.
3. Only the `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` 11-feature family is searched.
4. The accepted table is inherited from `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]`; this finding does not
   reopen that table.
5. The target set `{YS, N}` is justified by the landed `[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` residue;
   this is a follow-up, not a discovery search over arbitrary singleton rows.

## Classical anchor

If the residual pair is low-dimensional at all, it should live on a classical
ṣifāt axis rather than on ad hoc modern features. This finding therefore asks
whether the surviving `YS` / `N` burden collapses to a compact 2-D classical
phonological coordinate inside the already-validated `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` family.

## Deliverables

- Script: `scripts/h_new_301_5_empirical_table_residual_row_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-301-5.json`
- Findings: `findings/phase-b-hypotheses/h-new-301-5-empirical-table-residual-row-rescue.md`
- Journal: `journal/h-new-301-5-run-1.md`
