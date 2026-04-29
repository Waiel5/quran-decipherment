---
finding_id: h-new-288-4
run: 1
date: 2026-04-19
specialist: codex
verdict: PASS-DIRECTED
---

# H-NEW-288.4 run 1 journal

## Task

Follow the OQ-19 frontier after `H-NEW-288.3`.

The whole-axis speech-act projection had just failed cleanly. The next honest
move was therefore to test a narrower local factor inside the same fixed
5-7-verse side, without reopening generic length-control families.

The smallest candidate was token count from the same QAC STEM parse already in
use.

## Timeline

1. Reused the fixed side `B` and fixed short-core `K`.
2. Reused the residualized family and four primary metrics from `H-NEW-288.1`.
3. Computed residualized core-closeness on `B`.
4. Tested token-count projection under the exact `8!` assignment null.
5. Ran verse count only as a descriptive contrast.
6. Wrote the JSON artifact and findings markdown.

## Locked result

- observed `T_tok`:
  `-0.6615868684750684`
- per-metric token-count correlations:
  `-0.6803367264`, `-0.6809346817`, `-0.6425597402`, `-0.6425163256`
- exact `p_short`:
  `0.04352570620768334`
- verdict:
  `PASS-DIRECTED`

Descriptive contrast:

- `T_verse = -0.2627342668146082`
- descriptive `p = 0.2660332541567696`

## Structural reading

The important surprise was not just that the token-count effect was negative.
It was that it survived while verse count did not.

So the local factor is finer than the coarse verse-length bins already in play.

Inside the exact `H-NEW-273` 5-7 verse side:

- more token-dense surahs sit farther from the residualized short-core
- more token-light surahs sit closer to it

That gives the project a real local ordering factor after the whole-axis
speech-act projection failed.

## Interpretation

This run does not overturn the family adjudication line.

Instead it tells you how to read the split more honestly:

- not purely semantic
- not reducible to verse count
- but containing a real local residual token-count gradient

That is the new information.
