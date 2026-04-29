---
id: H-NEW-134-FORMAL
title: Prophet-named surahs show a conservative surface-form narrative signature beyond name-root enrichment
phase: B
status: INSTRUMENT-BROKEN
date: 2026-04-18
prereg: findings/phase-b-hypotheses/h-new-134-formal-prophet-named-signature-prereg.md
script: scripts/h_new_134_formal_prophet_named_signature.py
json: findings/phase-b-hypotheses/csv/h-new-134-formal.json
seed: 20260418
n_perm: 100000
bonferroni_family: h-new-134-formal-prophet-named-signature
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: (hafs-kufan; no-tashkeel; canonical 114; verse-level surface-token markers; exact slot-matched null by type × verse-count band × muq-status)
---

# [[h-new-134-formal-prophet-named-signature|H-NEW-134]]-FORMAL — Prophet-named surah signature

## Headline

The strict prophet-named set looks positive on both preregistered
surface-form axes, but the planted MW-5 control fails on both axes
under the same slot-matched permutation instrument.

So the correct landing is:

> **INSTRUMENT-BROKEN**, not PASS.

This is not a fake positive. The observed strict-6 prophet set is
indeed above its matched null on both primary axes. But the exact same
instrument fails to recognize a deterministic planted high-marker set
with the same slot profile. That means the matcher / null is not
discriminative enough for inferential promotion.

## Strict primary set

Strict prophet-named set:

- Q 10 Yūnus
- Q 11 Hūd
- Q 12 Yūsuf
- Q 14 Ibrāhīm
- Q 47 Muḥammad
- Q 71 Nūḥ

Primary axes were intentionally surface-form only:

1. `vocative_share` = fraction of verses containing `يا`
2. `sequencer_share` = fraction of verses containing one of
   `{اذ, واذ, ثم, فلما, لما}`

Bonferroni family:

- `k = 2`
- `alpha_bon = 0.025`

## Primary numbers

### Axis A — Vocative share

- observed strict-6 mean = `0.07938`
- null mean = `0.05592`
- null sd = `0.01121`
- `z = +2.09`
- one-sided `p = 0.01945`
- **passes** `alpha_bon = 0.025`

### Axis B — Sequencer share

- observed strict-6 mean = `0.11218`
- null mean = `0.06455`
- null sd = `0.01123`
- `z = +4.24`
- one-sided `p = 9.9999e-06`
- **passes** `alpha_bon = 0.025`

If we ignored MW-5, this would read as a clean `2/2`
`PASS-DIRECTED`.

## Why the verdict is INSTRUMENT-BROKEN

The preregistered MW-5 planted control was:

- for each strict slot, choose the non-target surah with the highest
  `vocative_share + sequencer_share`
- then rerun the exact same slot-matched null

Planted surahs:

- Q 7
- Q 20
- Q 26
- Q 27
- Q 35
- Q 58

### MW-5 Axis A — Vocative share

- observed planted mean = `0.08681`
- null mean = `0.07780`
- one-sided `p = 0.16114`
- **fails**

### MW-5 Axis B — Sequencer share

- observed planted mean = `0.09405`
- null mean = `0.10988`
- one-sided `p = 0.94625`
- **fails**

That is decisive. A planted high-marker set with the same slot profile
should have passed easily if the slot-matched null were behaving as a
useful discriminative instrument. Because it did not, the strict-6
positive-looking result cannot be promoted.

## Sensitivity and auxiliary outputs

### Expanded named-human-figure sensitivity

Expanded set:

- strict-6 above, plus Q 19 Maryam and Q 31 Luqmān

This expanded set also looks positive:

- `vocative_share`: `p = 9.9999e-06`
- `sequencer_share`: `p = 0.01462`

But these are descriptive only under the same broken instrument. They
do not rescue the verdict.

### Auxiliary speech-share audit

- observed strict-6 mean = `0.21667`
- null mean = `0.18703`
- one-sided `p = 0.08663`
- **does not pass**

That auxiliary result is directionally consistent with the narrative
reading, but again it cannot be promoted under an instrument-broken
run.

## Interpretation

What the data probably indicate:

- prophet-named surahs do have elevated vocative and narrative-sequencer
  surface-form shares under this strict title-based set
- the expanded named-human-figure set shows the same direction

What we are **not** allowed to say:

- that [[h-new-134-formal-prophet-named-signature|H-NEW-134]]-formal validates a prophet-named surface-form
  signature

The reason is not that the target effect vanished. The reason is that
the null-instrument failed its own precommitted positive control. Under
project discipline, that stops promotion.

## Honest limits

1. The slot profile is sparse at `meccan|100+|muq`: after removing the
   targets, only three control surahs remain. That makes the matching
   space much tighter and likely contributes to the MW-5 failure.
2. The planted control is deterministic and aggressive; it is exactly
   the right stress test for this null, and the null failed it.
3. The main family deliberately excluded prophet-name lexica and
   root-space structure. This is a surface-form test only.
4. Because the feasibility screen preceded the prereg, the best
   possible ceiling would have been `PASS-DIRECTED`, not CONFIRMED, even
   if MW-5 had succeeded.

## Bottom line

**[[h-new-134-formal-prophet-named-signature|H-NEW-134]]-FORMAL lands as INSTRUMENT-BROKEN.**

The strict prophet-named surahs are elevated on both locked surface-form
axes, and the expanded person-named sensitivity set is elevated too.
But the planted MW-5 control fails under the same slot-matched
permutation instrument, so the run cannot support inferential promotion.

The honest legacy of this run is narrower:

> the prophet-named surface-form idea remains plausible, but this
> particular slot-matched null is not trustworthy enough to certify it.
