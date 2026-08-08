---
id: OPEN-H-NEW-2940
title: "OPEN QUESTION — the inverse re-cut arm, unrun after three agent failures"
status: NOT RUN — no result exists; do not cite any number for this test
date: 2026-08-08
author: Waiel Al-Shujaa
blocks: the cross-corpus magnitude claim of H-NEW-2880/2890/2910
---

# OPEN — the inverse re-cut arm has NOT been run

**No result exists for this test. Nothing may be cited from it.** This file exists so the
question is not silently lost, and so a future session does not have to rediscover why it matters.

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
