---
id: H-NEW-271-3
title: Anchored 3-D singleton rescue after H-NEW-271.2
phase: B
status: NO-MAXT-3D-RESCUE
date: 2026-04-19
executed_by: codex
parent_1: H-NEW-271
parent_2: H-NEW-271-2
parent_3: H-NEW-232
open_question: OQ-1 at the singleton layer under anchored 3-D rescue
seed: 20260419
prereg: h-new-271-3-anchored-3d-singleton-rescue-prereg.md
prereg_sha256: 8313eda918f49a95cc488f0f71c11fe88391e105b487edeb21d86e2aad563c90
alpha: 0.05
rules_tuple: "(29 canonical muq surahs; locked H-NEW-271 deduplicated phonological pool; fixed anchor pair mean_manner + mean_vowel_carrier inherited from H-NEW-271.2 best raw pair; exactly 8 one-feature phonological augmentations from the remaining pool only; H-NEW-232 accepted-cluster sets reused verbatim; z-scored against the 19 multi-member surahs only; 3-D Euclidean nearest-centroid primary; best augmentation selected by singleton hit count with preregistered tie-break on total nearest-centroid distance then lexicographic name; familywise maxT label-shuffle null across all 8 anchored triples; seed 20260419)"
verdict: NO-MAXT-3D-RESCUE
---

# [[h-new-271-3-anchored-3d-singleton-rescue|H-NEW-271.3]] - Anchored 3-D singleton rescue after `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`

## Headline

**NO-MAXT-3D-RESCUE.**

- The best anchored triple is
  **`mean_manner + mean_vowel_carrier + mean_sonorant`**.
- It reaches **`8 / 10` singleton hits**, which ties the raw `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` and
  `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` level.
- No anchored triple exceeds `8 / 10`.
- The familywise maxT correction over the 8 legal third-axis augmentations
  gives **`p_maxT = 0.08691308691308691`** (`(1 + 86) / 1001`).
- So the anchored 3-D search still fails inferentially.

The bounded conclusion is direct: compact singleton closure still does not
survive at 3-D.

## Best triple

| Quantity | Result |
|---|---|
| Best triple | `mean_manner + mean_vowel_carrier + mean_sonorant` |
| Hit count | `8 / 10` |
| Hit rate | `0.800` |
| Any triple reaches `>= 8 / 10`? | `YES` |
| Any triple improves on `8 / 10`? | `NO` |
| Corrected p-value | `0.08691308691308691` |
| Verdict | `NO-MAXT-3D-RESCUE` |

The canonical winner is unique only after the preregistered tie-break on total
nearest-centroid distance. Four triples tie at `8 / 10`, but
`mean_sonorant` wins the distance tie-break.

## Candidate ladder

| Triple | Hits | Rate |
|---|---:|---:|
| `mean_manner + mean_vowel_carrier + mean_sonorant` | 8 | 0.800 |
| `mean_manner + mean_vowel_carrier + mean_pharyngeal` | 8 | 0.800 |
| `mean_manner + mean_vowel_carrier + mean_voice` | 8 | 0.800 |
| `mean_manner + mean_vowel_carrier + mean_continuant` | 8 | 0.800 |
| `mean_manner + mean_vowel_carrier + has_qalqala` | 7 | 0.700 |
| `mean_manner + mean_vowel_carrier + mean_emphatic` | 7 | 0.700 |
| `mean_manner + mean_vowel_carrier + mean_idhlaq` | 7 | 0.700 |
| `mean_manner + mean_vowel_carrier + mean_makhraj` | 4 | 0.400 |

This is the important structural result: widening the pair to 3-D creates more
ways to tie the raw `8 / 10` level, but it does not create any route past it.

## Best-triple singleton table

Best triple: `mean_manner + mean_vowel_carrier + mean_sonorant`

| Singleton | Surah | Nearest multi-surah | Nearest cluster | Accepted clusters | Match? |
|---|---:|---:|---|---|---|
| ALMS | 7 | 2 | ALM | {ALM} | YES |
| ALMR | 13 | 10 | ALR | {ALM, ALR} | YES |
| KHYAS | 19 | 26 | TSM | {HM, TSM} | YES |
| TH | 20 | 26 | TSM | {TSM} | YES |
| TS | 27 | 26 | TSM | {TSM} | YES |
| YS | 36 | 2 | ALM | {ALM, ALR} | YES |
| S | 38 | 26 | TSM | {TSM} | YES |
| HMASQ | 42 | 26 | TSM | {HM} | NO |
| Q | 50 | 26 | TSM | {HM, TSM} | YES |
| N | 68 | 40 | HM | {ALM, ALR} | NO |

Nearest multi-member surah and nearest centroid again agree for all 10
singletons. The remaining misses are still `HMASQ` and `N`, exactly as in the
best raw 2-D solution from `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]`.

## What changed relative to [[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]

Almost nothing inferentially:

- `[[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]]` best pair: `8 / 10`, `p_maxT = 0.0899100899100899`
- `[[h-new-271-3-anchored-3d-singleton-rescue|H-NEW-271.3]]` best triple: `8 / 10`, `p_maxT = 0.08691308691308691`

So narrowing the family from 9 candidate pairs to 8 anchored triples improves
the corrected p-value only marginally. The singleton layer still sits on the
same boundary.

The new descriptive information is that four different third-axis additions can
tie the raw `8 / 10` level:

- `mean_sonorant`
- `mean_pharyngeal`
- `mean_voice`
- `mean_continuant`

But none of them fixes the two persistent failures, and none reaches `9 / 10`.

## Why the verdict stays negative

Under the 8-way maxT null:

- familywise-null mean max hits = **`4.556`**
- familywise-null sd = **`2.0680580262652204`**
- familywise-null `q95 = 8.0`
- familywise-null `q99 = 9.0`
- observed best hits = **`8`**

So the best anchored 3-D result again lands right on the 95th-percentile
boundary of the search-corrected null. That is not enough for an inferential
pass at `alpha = 0.05`.

## Interpretation

The honest read is:

1. The singleton layer still refuses compact closure.
2. Anchoring on `mean_manner + mean_vowel_carrier` does not produce a decisive
   3-D rescue.
3. Third-axis freedom broadens the set of raw `8 / 10` ties, but it does not
   increase the ceiling or eliminate the same two failure cases.

So the OQ-1 story remains split:

- the multi-member cluster layer is radically parsimonious under `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]`
- the singleton layer is not compactly resolved at 1-D, 2-D, or this bounded
  3-D follow-up

## Verdict

**NO-MAXT-3D-RESCUE**

- best triple:
  `mean_manner + mean_vowel_carrier + mean_sonorant`
- corrected `p_maxT = 0.08691308691308691`
- best hits = `8 / 10`
- no triple exceeds `8 / 10`

Therefore the singleton layer still does not admit a familywise-significant
compact rescue under this anchored 3-D search.

## Files

- Pre-reg:
  `findings/phase-b-hypotheses/h-new-271-3-anchored-3d-singleton-rescue-prereg.md`
- Script: `scripts/h_new_271_3_anchored_3d_singleton_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-3.json`
- Journal: `journal/h-new-271-3-run-1.md`
