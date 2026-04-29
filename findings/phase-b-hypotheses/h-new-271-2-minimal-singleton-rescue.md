---
id: H-NEW-271-2
title: Minimal singleton rescue over H-NEW-271's mean_manner axis
phase: B
status: NO-MAXT-RESCUE
date: 2026-04-19
executed_by: codex
parent_1: H-NEW-271
parent_2: H-NEW-271-1
parent_3: H-NEW-232
open_question: OQ-1 at the singleton layer under minimal 2-D rescue
seed: 20260419
prereg: h-new-271-2-minimal-singleton-rescue-prereg.md
prereg_sha256: 012b53b50215afa01f1c0fe49b81898bbc894e19a5c8ccfa47e20babf89d7833
alpha: 0.05
rules_tuple: "(29 canonical muq surahs; locked H-NEW-271 deduplicated phonological pool; anchor mean_manner retained in every candidate; exactly 9 one-feature phonological augmentations; H-NEW-232 accepted-cluster sets reused verbatim; z-scored against the 19 multi-member surahs only; 2-D Euclidean nearest-centroid primary; best augmentation selected by hit count with preregistered tie-break on total nearest-centroid distance then lexicographic name; familywise maxT label-shuffle null across all 9 candidates; seed 20260419)"
verdict: NO-MAXT-RESCUE
---

# [[h-new-271-2-minimal-singleton-rescue|H-NEW-271.2]] - Minimal singleton rescue over the `mean_manner` axis

## Headline

**NO-MAXT-RESCUE.**

- The best 2-D augmentation is **`mean_manner + mean_vowel_carrier`**.
- It reaches **`8 / 10` singleton hits**, exactly the raw `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` level.
- But the familywise maxT correction over the 9 locked augmentations gives
  **`p_maxT = 0.0899100899100899`** (`(1 + 89) / 1001`).
- So the raw restoration is **descriptive only**, not an inferential pass.

This is the core result: a minimal 2-D rescue exists in raw geometry, but it is
not rare enough under the locked search-corrected null to support a formal
claim.

## Best augmentation pair

| Quantity | Result |
|---|---|
| Best pair | `mean_manner + mean_vowel_carrier` |
| Hit count | `8 / 10` |
| Hit rate | `0.800` |
| Any pair reaches `>= 8 / 10`? | `YES` |
| Corrected p-value | `0.0899100899100899` |
| Verdict | `NO-MAXT-RESCUE` |

The canonical winner is unique. No other pair ties it at `8 / 10`.

## Candidate ladder

| Pair | Hits | Rate |
|---|---:|---:|
| `mean_manner + mean_vowel_carrier` | 8 | 0.800 |
| `mean_manner + mean_sonorant` | 7 | 0.700 |
| `mean_manner + mean_idhlaq` | 7 | 0.700 |
| `mean_manner + mean_voice` | 6 | 0.600 |
| `mean_manner + mean_pharyngeal` | 6 | 0.600 |
| `mean_manner + mean_continuant` | 6 | 0.600 |
| `mean_manner + mean_emphatic` | 6 | 0.600 |
| `mean_manner + has_qalqala` | 5 | 0.500 |
| `mean_manner + mean_makhraj` | 3 | 0.300 |

So the rescue is highly specific: only one augmentation reaches the raw
`[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]` level, and only two others get to `7 / 10`.

## Best-pair singleton table

Best pair: `mean_manner + mean_vowel_carrier`

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

Nearest multi-member surah and nearest centroid agree for all 10 singleton
cases under the winning pair, so the remaining uncertainty is not due to
centroid-vs-neighbor mismatch. The unresolved cases are the same geometric
problem cases themselves: `HMASQ` and `N`.

## What changed relative to [[h-new-271-1-manner-singleton|H-NEW-271.1]]

`[[h-new-271-1-manner-singleton|H-NEW-271.1]]` on `mean_manner` alone gave only `5 / 10`.

Adding `mean_vowel_carrier` rescues three additional singleton cases:

- `ALMS`
- `ALMR`
- `YS`

That is the substantive raw discovery in this finding. The smallest 2-D
augmentation that restores the full raw `8 / 10` is not sonorancy,
pharyngeality, or emphaticity. It is **vowel-carrier structure**, which is
driven by the presence of `ا` and `ي` in the muq letter-sets.

## Why the verdict is still negative

The familywise null is the correct reference, not the raw hit count.

Under the 9-way maxT null:

- familywise-null mean max hits = **4.765**
- familywise-null `q95 = 8.0`
- familywise-null `q99 ≈ 8.01`
- observed best hits = **8**

So an `8 / 10` best-of-9 result is right at the 95th-percentile boundary of the
search-corrected null. It is interesting, but not enough to claim an
inferential rescue at `alpha = 0.05`.

## Interpretation

The right reading is narrow and honest:

1. `mean_manner` alone was too coarse for the singleton layer.
2. Adding exactly one more phonological axis can restore the **raw** `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]`
   topology.
3. But after correcting for the 9 augmentation attempts, the evidence is still
   not strong enough to declare that rescue non-random.

That means the singleton layer is more delicate than the cluster layer. The
multi-member ceiling truly collapsed to one dimension in `[[h-new-271-muq-minimal-phon-family|H-NEW-271]]`; the
singleton layer does not collapse that far, and even the best bounded 2-D
repair remains inferentially short.

## Verdict

**NO-MAXT-RESCUE**

- A raw `[[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]`-level restoration exists:
  `mean_manner + mean_vowel_carrier -> 8 / 10`.
- But the corrected p-value is `0.0899100899100899`, which fails the locked
  familywise `alpha = 0.05` bar.
- Therefore no minimal 2-D augmentation can yet be claimed as a significant
  rescue of the singleton layer.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-271-2-minimal-singleton-rescue-prereg.md`
- Script: `scripts/h_new_271_2_minimal_singleton_rescue.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-271-2.json`
- Journal: `journal/h-new-271-2-run-1.md`
