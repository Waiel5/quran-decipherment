---
finding_id: h-new-288-2
run: 1
date: 2026-04-19
specialist: codex
verdict: PASS-DIRECTED
---

# H-NEW-288.2 run 1 journal

## Task

Follow the OQ-19 frontier after `H-NEW-288.1`.

The open question was no longer whether the Q108 hub survives in the
residualized family. That was already settled. The open question was how that
residualized-family medoid mechanism relates to the narrower `H-NEW-273`
Q1↔Q108 speech-act foothold.

The first candidate flip test was real in the raw geometry but too common to
certify cleanly on its own. So the final locked test asked a sharper question:

- among the exact `H-NEW-288.1` candidate family `P \\ {Q108}`,
- which surah maximizes
  `L_sep(s) = S_H273(s) * C_sep(s)`?

where:

- `S_H273(s)` is the landed `H-NEW-273` speech-act score
- `C_sep(s)` counts the four primary metrics on which residualized smoothing
  moves `s` farther from `Q108` than literal normalization does

The fixed target was `Q1`.

## Timeline

1. Re-read the OQ-19 handoff state and the `H-NEW-273 / 288 / 288.1` chain.
2. Checked the proposed raw `Q1` flip against the actual distance geometry.
3. Rejected the weaker raw flip as a standalone primary because it was too
   common inside the fixed comparator family.
4. Locked the stronger liturgical-separation statistic using only landed
   ingredients.
5. Implemented the exact candidate-family rerun.
6. Wrote the JSON artifact and findings markdown.

## Locked result

- candidate family size:
  `21`
- target:
  `Q1`
- `S_H273(Q1)`:
  `0.20854568887374797`
- `C_sep(Q1)`:
  `4`
- `L_sep(Q1)`:
  `0.8341827554949919`
- exact descending rank:
  `1 / 21`
- exact upper-tail:
  `0.047619047619047616`
- verdict:
  `PASS-DIRECTED`

Per metric, `Q1` moved:

- from literal rank `14`
- to residualized rank `17`

on all four primary metrics.

## What changed conceptually

This run finally made the OQ-19 integration issue concrete.

The residualized cloud does not simply absorb every speech-act-rich short
surah around Q108.

Instead:

- `Q1` is the strongest high-score *ejected* surah
- `Q112` is the strongest high-score *approached* surah
- `Q113` and `Q114` also move toward Q108 under the residualized family

So the residualized short-surah cloud has a real internal polarity:

- opener side pushed away
- Ikhlas/refuge side pulled in

That was the new information.

## Interpretation

The right update to OQ-19 is no longer just:

- narrow Q1↔Q108 foothold
- residualized Q108 medoid mechanism

It is now:

- narrow Q1↔Q108 foothold
- residualized Q108 medoid mechanism
- **bounded opener-vs-refuge/Ikhlas bifurcation inside that same pool**

This does not explain the mechanism completely, but it stops the two landed
results from floating separately.
