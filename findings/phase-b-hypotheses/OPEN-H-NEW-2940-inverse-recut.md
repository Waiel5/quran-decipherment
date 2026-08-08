---
id: OPEN-H-NEW-2940
title: "CLOSED — the inverse re-cut arm, run 2026-08-08"
status: "CLOSED — measured. f = −0.0067; see findings/phase-b-hypotheses/h-new-2940-inverse-recut.md"
date: 2026-08-08
author: Waiel Al-Shujaa
blocks: nothing further — the cross-corpus magnitude claim is now measured, not extrapolated
resolved_by: findings/phase-b-hypotheses/h-new-2940-inverse-recut.md
---

# CLOSED — the inverse re-cut arm has now been run

**Resolved 2026-08-08.** Run `runs/h-new-2940/20260808T115534Z`, finding at
`findings/phase-b-hypotheses/h-new-2940-inverse-recut.md`.

The native Δ reproduced **bit-identically** (0.18686703691604045, difference 0.0). Merging this
corpus's own verses to **65.121 words** — mid-prose, inside the baseline range — gives Δ =
**0.18791**, closing **f = −0.0067** of the gap: none of it. Every one of eight arms across four
target lengths and two merge rules closes at most 12.3%.

Per the decision rule locked below and in the pre-registration: **the residual is real and
LARGER than H-NEW-2930's extrapolation suggested — 6.08× measured in range, against 3.63×
extrapolated.** The magnitude claim is not withdrawn.

The text below is the question as it stood before the run, left unaltered.

---

## The question as it stood on 2026-08-08, before the run

This file existed so the question was not silently lost, and so a future session did not have to
rediscover why it mattered.

## The question

`h-new-2930-unit-length-screen.md` corrected the pausal cross-corpus headline from **5.3× to
3.63×** — but by **extrapolating a nine-point linear fit 0.86 full prose-ranges beyond the data**,
to a unit length (13.21 words) that is 3.7× shorter than the shortest prose book in the baseline.
**That extrapolation is the weakest link in the finding**, and 2930 says so in its own §4.

It can be replaced by a direct measurement requiring **no baseline text at all**, using the method
that killed the scansion result in `h-new-2730-scansion-genre-control.md`, run backwards:

> **Merge this corpus's own adjacent verses into longer units matching prose unit lengths
> (~50, 65, 75, 91 words), and measure how far Δ moves toward the prose value (~0.030).**

**The decision rule, locked here before any run:**
- If re-cutting alone closes **most** of the gap between 0.18690 and ~0.030, the cross-corpus
  magnitude claim is **finished** — Δ is a unit-length effect and must be withdrawn.
- If it closes **little**, the residual is real and **larger** than 2930's extrapolation suggested.

## What is NOT at stake

**H-NEW-2880's within-corpus null is untouched by this and by everything in H-NEW-2930.** It
permutes this corpus's own citation endings against itself with class count, class sizes and
concentration held exactly fixed — floor variance **0.00 across 160,000 draws**, z = **+15.03**,
0/10,000. No cross-corpus unit length enters it. That result stands regardless of how this
question resolves.

## Why it is unrun

Three dispatched lanes failed on it: two returned **nothing at all** — no finding, no run
directory, no scratch files — and the third failed on a mid-response connection error. The task
was narrowed from five deliverables to a single number between the second and third attempt, and
still did not complete.

**It was not attempted by hand**, deliberately: reusing `scripts/h-new-2880.py`'s rime extractors
and pausal tuples verbatim is a stated requirement, and a hand-rolled extractor that did not match
them would produce a number that could not be compared to the published Δ. Reporting such a number
would be precisely the class of error this week's rule documents exist to prevent.

## To run it

Reuse `findings/phase-b-hypotheses/scripts/h-new-2880.py` — its rime extractors and both pausal
tuples, verbatim, not reimplemented. Pre-register, SHA-lock, immutable run directory, mode `'x'`,
checkpoints outside it. Seeds 20260509 / 20260519.

**Until it runs, the honest statement of the cross-corpus magnitude is: ~3.6× by extrapolation,
with the extrapolation acknowledged as unreliable in both directions.** Not 5.3×, and not a
measured 3.63×.

---

## Superseded by the run

The paragraph above is now superseded. The extrapolation was unreliable **in the direction that
favours the null**: measured at matched unit length the residual is **6.08×**, not ~3.6×. See
`findings/phase-b-hypotheses/h-new-2940-inverse-recut.md` §4.
