---
id: H-NEW-271-5
title: Empirical-table minimal singleton rescue over H-NEW-271's mean_manner axis
phase: B
status: NO-MAXT-EMPIRICAL-RESCUE
date: 2026-04-19
executed_by: codex
parent_1: H-NEW-271
parent_2: H-NEW-271-2
parent_3: H-NEW-274
open_question: OQ-1 at the singleton layer under empirical-table minimal 2-D rescue
seed: 20260419
prereg: h-new-271-5-empirical-table-singleton-rescue-prereg.md
prereg_sha256: 75176bfd4db305916601ebacefa3bca2013efe4c23fde1c5ab33132f2a4589f2
alpha: 0.05
rules_tuple: "(29 canonical muq surahs; locked H-NEW-271 deduplicated phonological feature pool; anchor mean_manner retained in every candidate; exactly 9 one-feature phonological augmentations from the remaining pool only; accepted-cluster table updated only by the locked H-NEW-274 empirical replacements YS->HM and HMASQ->TSM; z-scored against the 19 multi-member surahs only; 2-D Euclidean nearest-centroid primary; best augmentation selected by singleton hit count with preregistered tie-break on total nearest-centroid distance then lexicographic augmentation name; familywise maxT label-shuffle null across all 9 candidates; seed 20260419)"
verdict: NO-MAXT-EMPIRICAL-RESCUE
---

# [[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]] - Empirical-table minimal singleton rescue over `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]`

## Headline

**NO-MAXT-EMPIRICAL-RESCUE.**

- The best pair under the stronger `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` empirical singleton table is
  **`mean_manner + mean_sonorant`**.
- It reaches **`8 / 10` singleton hits**, tying the raw `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` /
  `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` level but not improving on it.
- The familywise maxT correction over the 9 legal augmentations worsens to
  **`p_maxT = 0.2077922077922078`**.
- The persistent misses shift to **`YS`** and **`N`**.

So the stronger empirical singleton table does **not** rescue compact
parsimony. It changes *which* cases remain difficult, but it does not produce
an inferential compact rescue.

## Best pair

| Quantity | Result |
|---|---|
| Best pair | `mean_manner + mean_sonorant` |
| Hit count | `8 / 10` |
| Hit rate | `0.800` |
| Any pair reaches `>= 8 / 10`? | `YES` |
| Corrected p-value | `0.2077922077922078` |
| Verdict | `NO-MAXT-EMPIRICAL-RESCUE` |

The canonical winner is unique only after the preregistered tie-break on total
nearest-centroid distance. `mean_manner + mean_vowel_carrier` also reaches
`8 / 10`, but `mean_sonorant` wins the distance tie-break under the empirical
table.

## Candidate ladder

| Pair | Hits | Rate |
|---|---:|---:|
| `mean_manner + mean_sonorant` | 8 | 0.800 |
| `mean_manner + mean_vowel_carrier` | 8 | 0.800 |
| `mean_manner + mean_idhlaq` | 8 | 0.800 |
| `mean_manner + mean_voice` | 7 | 0.700 |
| `mean_manner + mean_pharyngeal` | 7 | 0.700 |

The key structural point is not the exact winner. It is that even after moving
to the stronger `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` accepted table, the best compact 2-D family still
tops out at `8 / 10`, and the corrected null is less favorable than before.

## Best-pair singleton table

Best pair: `mean_manner + mean_sonorant`

| Singleton | Surah | Nearest cluster | Accepted clusters | Match? |
|---|---:|---|---|---|
| ALMS | 7 | ALM | {ALM} | YES |
| ALMR | 13 | ALR | {ALM, ALR} | YES |
| KHYAS | 19 | TSM | {HM, TSM} | YES |
| TH | 20 | TSM | {TSM} | YES |
| TS | 27 | TSM | {TSM} | YES |
| YS | 36 | TSM | {HM} | NO |
| S | 38 | TSM | {TSM} | YES |
| HMASQ | 42 | TSM | {TSM} | YES |
| Q | 50 | TSM | {HM, TSM} | YES |
| N | 68 | HM | {ALM, ALR} | NO |

The interpretive shift is clean:

- under the older table, `HMASQ` was one of the compact-rescue blockers
- under the stronger empirical table, `HMASQ` is repaired automatically
- but `YS` becomes a blocker instead, alongside `N`

So the compact-rescue failure is not just "the classical table was too rigid."
The failure survives the move to the stronger table; it simply relocates.

## Why the verdict stays negative

Under the 9-way empirical-table maxT null:

- familywise-null mean max hits = **`4.637`**
- familywise-null sd = **`2.686862668615573`**
- familywise-null `q95 = 9.0`
- familywise-null `q99 = 9.0`
- observed best hits = **`8`**

This is materially harsher than `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`, where the 95th percentile of
the familywise max-hit null was only `8.0`. Under the empirical table, an
observed best score of `8 / 10` is not close to enough.

## What changed relative to [[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]

- `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` best pair under the inherited table:
  `mean_manner + mean_vowel_carrier`, `8 / 10`, `p_maxT = 0.0899100899100899`
- `[[h-new-271-5-empirical-table-singleton-rescue|H-NEW-271.5]]` best pair under the empirical table:
  `mean_manner + mean_sonorant`, `8 / 10`, `p_maxT = 0.2077922077922078`

So the stronger table does **not** make compact rescue easier. It actually
makes the inferential position worse, because the best observed hit count does
not rise while the familywise null gets harsher.

## Interpretation

The honest read is:

1. `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` really did improve the singleton interpretation table.
2. But compact 2-D rescue still does not survive familywise correction under
   that stronger table.
3. The residual burden now sits on `YS` and `N`, not on `HMASQ`.

This sharpens OQ-1 again. The open question is no longer whether compact
parsimony fails only because the old accepted table was imperfect. It fails
even after the accepted table is upgraded to the stronger empirical version.

## Verdict

**NO-MAXT-EMPIRICAL-RESCUE**

- best pair:
  `mean_manner + mean_sonorant`
- corrected `p_maxT = 0.2077922077922078`
- best hits = `8 / 10`
- persistent misses under the empirical table:
  `YS`, `N`

Therefore the singleton layer still does not admit a familywise-significant
compact 2-D rescue even after adopting the stronger `[[h-new-274-empirical-vs-classical-singleton-reassignment|H-NEW-274]]` empirical
accepted-cluster table.

## Files

- Pre-reg:
  `findings/phase-b-hypotheses/h-new-271-5-empirical-table-singleton-rescue-prereg.md`
- Script: `scripts/h_new_271_5_empirical_table_singleton_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-5.json`
- Journal: `journal/h-new-271-5-run-1.md`
