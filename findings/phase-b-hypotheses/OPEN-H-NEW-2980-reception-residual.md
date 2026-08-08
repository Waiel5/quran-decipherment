---
id: OPEN-H-NEW-2980
title: "OPEN QUESTION — the reception-weight residual rosters, unrun after a connection failure"
status: NOT RUN — no result exists; do not cite any number for this test
date: 2026-08-08
author: Waiel Al-Shujaa
instrument_ready: findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv
---

# OPEN — the reception-residual rosters have NOT been produced

**No result exists. Nothing may be cited from this test.** This file exists so the question is not
silently lost — the same mechanism that got `OPEN-H-NEW-2940` eventually run after three lanes
died on it, and which turned a soft extrapolated 3.63× into a measured 6.08×.

## The question

H-NEW-860.1 built `csv/h-new-860-1-reception-weights.csv` — a **formal per-verse reception weight
for all 6,236 verses**, derived from the full 50,884-record ḥadīth corpus. It replaced a hand-built
rubric that carried no discriminative information. **It has been used for exactly one correlation
and nothing else.**

Cross it against the structural instruments (`csv/h-new-590.json` outlier strength,
`csv/h-new-840.json` UAS) and produce two rosters, top 30 each with verse text and both ranks:

1. **Structurally extreme, rarely cited** — verses the instruments flag as extraordinary that the
   ḥadīth tradition passes over.
2. **Heavily cited, structurally ordinary** — verses the tradition dwells on that the instruments
   find unremarkable.

**The rosters are the deliverable and stand independent of any inference.**

## Constraints, already established and not to be rediscovered

- **A handful of verses dominate** — al-Fātiḥa, āyat al-kursī, the muʿawwidhāt. **Rank statistics
  only, no means.** Report the top-20 raw counts so the concentration is visible.
- **Unit drift applies** if reception is expressed as a rate: mushaf position correlates with log
  word count at ρ = −0.934. Prefer exact counts and ranks; residualise on verse length before
  calling anything a residual.
- **Expected verdict on the inferential arm: NULL.** H-NEW-2620 asked the same question of the
  tafsīr corpus and returned NULL on all six registered inferences once length was residualised.
  **A clean NULL alongside a good roster is a complete result.**

## Why it is unrun

One lane, failed on `API Error: Unable to connect to API (ENOTFOUND)` before producing any
artifact. **Four lanes were lost to connection errors on 2026-08-08** across this and the
H-NEW-2940 family. **The failures are infrastructure, not scope** — narrowing briefs between
attempts, as was done for 2940, was treating the wrong cause. The task as briefed is small and
should complete on a stable connection.

## To run it

Pre-register, SHA-lock, immutable run directory (mode `'x'`, `exist_ok=False`, checkpoints
outside), never delete a run directory, never edit the pre-registration after the run —
`scripts/verify-prereg-locks.sh` enforces the last.
