---
id: H-NEW-301-5
title: Empirical-table residual-row rescue over the 55-pair singleton family
phase: B
status: TARGETED-RESIDUAL-RESCUE
date: 2026-04-19
executed_by: codex
parent_1: H-NEW-301
parent_2: H-NEW-271-5
parent_3: H-NEW-274
open_question: OQ-1 empirical-table residual compact burden on YS and N
seed: 20260425
prereg: h-new-301-5-empirical-table-residual-row-rescue-prereg.md
prereg_sha256: 63e596462615d794f74f76e91bfba049d47317705a95a73a4535066ea6977207
n_perm: 20000
alpha: 0.05
rules_tuple: "(29 canonical muq surahs; same 11-feature pool and same C(11,2)=55 pair family as H-NEW-301; accepted singleton table switched only to the locked H-NEW-274 empirical version; primary endpoint restricted to the two live residual rows YS and N only; candidate pairs ranked by rescued-row count over {YS,N}, then by summed positive accepted-vs-rejected centroid margin over {YS,N}, then lexicographic pair label; 2-D Euclidean nearest-centroid geometry with z-scoring against the 19 multi-member surahs only; familywise maxT label-shuffle null across the same 55-pair family; seed 20260425)"
verdict: TARGETED-RESIDUAL-RESCUE
---

# [[h-new-301-5-empirical-table-residual-row-rescue|H-NEW-301.5]] - Empirical-table residual-row rescue over the `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` pair family

## Headline

**TARGETED-RESIDUAL-RESCUE.**

The live compact burden left by `[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` was not diffuse. When the
inferential target is narrowed exactly to the two surviving empirical-table
residual rows,

- `YS -> HM`
- `N -> {ALM, ALR}`

the full 55-pair `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` family contains a clear winner:

- **best pair**: `mean_voice + mean_sonorant`
- **targeted rescue**: `2 / 2`
- **targeted positive-margin sum**: `4.567826058189053`
- **familywise maxT p-value**: `0.00004999750012499375`

So the `YS` / `N` residual subproblem now has an honest compact 2-D closure.

## What the result is and is not

This is **not** a full compact 10-singleton closure.

- the best targeted pair scores only `8 / 10` on the full empirical-table
  singleton task
- the two global misses under the targeted winner are `ALMS` and `S`

But it **is** a real new closure of the live residual branch:

- `[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` showed that the empirical-table compact failure had narrowed to
  `YS` and `N`
- `[[h-new-301-5-empirical-table-residual-row-rescue|H-NEW-301.5]]` now shows that those two rows together collapse strongly to a
  specific 2-D phonological coordinate

That is a genuine refinement of OQ-1.

## Best pair

| Quantity | Result |
|---|---|
| Best targeted pair | `mean_voice + mean_sonorant` |
| Targeted rescue count | `2 / 2` |
| Positive-margin sum | `4.567826058189053` |
| Total singleton hits | `8 / 10` |
| Familywise maxT p-value | `0.00004999750012499375` |
| Count-only diagnostic p-value | `0.8431578421078946` |
| Verdict | `TARGETED-RESIDUAL-RESCUE` |

The count-only diagnostic matters. Merely finding a pair that rescues both
rows is not unusual once the 55-pair search is honored. What is unusual is the
**strength** of the rescue.

## Why the margin tie-break matters

Across the 55 tested pairs:

- `14 / 55` pairs rescue both target rows at the count level
- the highest full-task score among those `2 / 2` rescue pairs is `9 / 10`

So the row-count alone is weak. The null confirms that:

- `p_count_only = 0.8431578421078946`

Under the maxT null, some pair almost always rescues both rows somewhere in the
55-pair family.

What separates the observed winner is the **margin geometry**:

- null mean of the best positive-margin sum = `0.8081389520148301`
- null SD = `0.43793622686917316`
- null `q95 = 1.5935361327274289`
- null `q99 = 2.0387486618975244`
- observed best margin sum = `4.567826058189053`

So the inferential signal does **not** live in `2 / 2` by itself. It lives in
how decisively `mean_voice + mean_sonorant` separates the accepted centroids
from the rejected ones on the two live rows.

## Target-row details

### `YS`

Under `mean_voice + mean_sonorant`:

- nearest cluster = `HM`
- accepted set = `{HM}`
- accepted-best distance = effectively `0`
- nearest rejected distance = `2.538672162464229`
- margin = `2.5386721624642288`

So `YS` lands essentially **exactly on the `HM` centroid** in this 2-D space.

### `N`

Under the same pair:

- nearest cluster = `ALM`
- accepted set = `{ALM, ALR}`
- accepted-best distance = `5.07734432492846`
- nearest rejected distance = `7.106498220653284`
- margin = `2.029153895724824`

So `N` also clears its accepted set by a wide margin.

## Best-pair singleton table

Best pair: `mean_voice + mean_sonorant`

| Singleton | Surah | Nearest cluster | Accepted clusters | Match? |
|---|---:|---|---|---|
| ALMS | 7 | HM | {ALM} | NO |
| ALMR | 13 | ALM | {ALM, ALR} | YES |
| KHYAS | 19 | HM | {HM, TSM} | YES |
| TH | 20 | TSM | {TSM} | YES |
| TS | 27 | TSM | {TSM} | YES |
| YS | 36 | HM | {HM} | YES |
| S | 38 | HM | {TSM} | NO |
| HMASQ | 42 | TSM | {TSM} | YES |
| Q | 50 | TSM | {HM, TSM} | YES |
| N | 68 | ALM | {ALM, ALR} | YES |

This pair solves the targeted `YS` / `N` problem, not the full singleton
problem.

## Candidate ladder

Top targeted pairs by the pre-registered objective:

| Pair | Targeted rescue | Margin sum | Total hits |
|---|---:|---:|---:|
| `mean_voice + mean_sonorant` | 2 | 4.567826 | 8 |
| `mean_voice + has_qalqala` | 2 | 3.159364 | 8 |
| `mean_voice + mean_continuant` | 2 | 3.159364 | 8 |
| `mean_voice + mean_emphatic` | 2 | 3.159364 | 7 |
| `mean_makhraj + mean_sonorant` | 2 | 2.895527 | 8 |
| `mean_emphatic + mean_sonorant` | 2 | 2.870708 | 8 |
| `mean_sonorant + has_qalqala` | 2 | 2.870708 | 9 |
| `mean_sonorant + mean_continuant` | 2 | 2.870708 | 9 |

Two points matter:

1. `mean_sonorant` is persistent across many of the strongest targeted pairs.
2. The canonical winner is not the best full-task pair. It is the pair that
   most strongly resolves the specific live residue.

## Interpretation

`[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` showed that the classical-table singleton family had a descriptive
2-D winner (`mean_emphatic + mean_pharyngeal`) but no search-corrected compact
closure.

`[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` then showed that under the stronger empirical table, the compact
failure had narrowed specifically to `YS` and `N`.

`[[h-new-301-5-empirical-table-residual-row-rescue|H-NEW-301.5]]` now closes that narrowed branch:

- the residual burden is genuinely **2-D**
- the relevant 2-D coordinate is **`mean_voice + mean_sonorant`**
- the inferential force comes from the targeted margin, not from row-count
  alone

So OQ-1 now has a cleaner split than before:

- **global singleton compact closure** below the full `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` geometry is
  still not certified
- **the live empirical-table residual branch** `YS` / `N` is now isolated and
  solved by a specific compact 2-D phonological axis

## Classical anchor

The surviving residue does not collapse onto the same pair that mattered for
the classical-table `[[h-new-301-minimal-2feature-singleton|H-NEW-301]]` search. Under the stronger empirical table,
the decisive coordinate is `mean_voice + mean_sonorant`.

That keeps the solution inside the classical tajwīd / ṣifāt family:

- `mean_voice` corresponds to the voicedness axis
- `mean_sonorant` tracks the resonant-liquid-nasal envelope

So the residual compact solution remains classically phonological rather than
requiring a non-phonological escape route.

## Honest limits

1. This is a targeted follow-up to the landed `YS` / `N` residue. It does not
   certify a single compact pair for all 10 singleton rows.
2. The count-only version of the claim is weak under the 55-pair search. The
   margin statistic is essential.
3. `ALM` and `ALR` are identical centroids in the winning 2-D space, so the
   pair resolves `N` only at the accepted-set level, not as an internal
   `ALM` vs `ALR` discriminator.
4. The winning pair misses `ALMS` and `S`, so the full singleton geometry
   remains nontrivial.

## Verdict

**TARGETED-RESIDUAL-RESCUE**

The full OQ-1 singleton problem is still not compactly closed. But the live
empirical-table residual branch is no longer vague. The pair
`mean_voice + mean_sonorant` rescues `YS` and `N` together with an extreme
maxT-protected margin, converting the post-`[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` residue into a
specific low-dimensional classical phonological subproblem that is now solved.
