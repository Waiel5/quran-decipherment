---
id: H-NEW-280
title: "Q55 Fisher-Rao constrained-null salvage"
phase: B
status: "NULL - fixed-refrain constrained null removes the anti-geodesic reversal, but canonical Q55 is not significantly shorter than the constrained null"
date: 2026-04-18
specialist: codex
parent: h-new-127
context:
  - h-new-83
seed: 20260418
pre_reg: findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null-prereg.md
script: scripts/h_new_280_q55_refrain_constrained_fr_null.py
output_json: findings/phase-b-hypotheses/csv/h-new-280.json
verdict: "NULL - p = 0.312168783122, z = -0.458439; Q55 is no longer anti-geodesic under the constrained null"
---

# [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]] - Q55 Fisher-Rao constrained-null salvage

## Summary

This run implements the narrow OQ-20 salvage test and nothing broader:

- keep the 31 exact Q55 refrain positions fixed,
- permute only the 47 non-refrain verses across the 47 non-refrain
  slots,
- recompute the same full 78-verse Fisher-Rao path length used in
  [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]].

**Result**: canonical Q55 is **slightly shorter** than the constrained
null mean, but not by enough to pass.

- `L_canon = 13.639165`
- constrained-null mean `= 13.693339`
- constrained-null SD `= 0.118168`
- `z = -0.458439`
- one-sided lower-tail `p = 0.312168783122`

So the bounded verdict is **NULL**.

## Headline update to the Q55 story

[[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]'s unconstrained full-permutation null made Q55 look strongly
anti-geodesic:

- [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] full null: mean `11.252899`, `z = +5.393938`, `p = 1.0`

Under the fixed-refrain constrained null in this run:

- [[h-new-280-q55-refrain-constrained-fr-null|H-NEW-280]] constrained null: mean `13.693339`, `z = -0.458439`,
  `p = 0.312169`

That is the key refinement. Once refrain clustering is disallowed, the
Q55 reversal does **not** survive. The constrained-null mean moves upward
by about `+2.44` path-length units relative to [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]], and canonical
Q55 is no longer on the wrong side of the distribution.

But the result does **not** flip into a positive pass either. Canonical
Q55 is only `0.054173` path-length units below the constrained-null mean,
which is about `0.46` SD. That is directionally shorter, not
statistically persuasive.

## Interpretation

The smallest honest salvage test lands in the middle:

- **The anti-geodesic claim is not robust.**
  Q55 does **not** remain anti-geodesic once the null preserves the
  surah's 31-slot refrain schedule.
- **The geodesic-optimality claim is also not rescued.**
  Canonical Q55 is not significantly shorter than the constrained null at
  the pre-registered one-sided `alpha = 0.05`.

So the bounded answer is:

> [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]]'s Q55 reversal was largely a null-construction artifact
> caused by allowing illegal refrain clustering, but Q55 still does not
> show a positive within-surah Fisher-Rao path-shortening effect under
> this corrected constrained null.

## Scope boundary

This finding does **not** reopen the broader [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] 5-surah family.
It only refines the Q55 exception mechanism. The broader OQ-20 status
therefore remains:

- 4 of 5 surahs were suggestive in [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]],
- Q55 no longer supports an anti-geodesic exception under the constrained
  null,
- but Q55 also does not become a positive pass here,
- so the verse-fractal family is still not promoted by this bounded
  salvage alone.

## Core numbers

| Quantity | Value |
|----------|------:|
| Refrain positions fixed | 31 |
| Non-refrain verses shuffled | 47 |
| `L_canon` | 13.639165 |
| Constrained-null mean | 13.693339 |
| Constrained-null SD | 0.118168 |
| `z` | -0.458439 |
| `#{L_perm <= L_canon}` | 3121 / 10000 |
| One-sided lower-tail `p` | 0.312168783122 |
| Anti-geodesic under constrained null? | No |

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null-prereg.md`
- Script: `scripts/h_new_280_q55_refrain_constrained_fr_null.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-280.json`
- Journal: `journal/h-new-280-run-1.md`
