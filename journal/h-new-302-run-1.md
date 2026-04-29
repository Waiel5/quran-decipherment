---
finding_id: h-new-302
run: 1
date: 2026-04-20
specialist: codex
verdict: NULL
---

# H-NEW-302 run 1 journal

## Task

Formalize the already-noticed OQ-17 `B6/B7` staircase inside the inherited
`cross-finding-012` octile family.

The question was narrower than the parent result:

- not whether the Pattern-B axes cohere
- but whether the muqattaat marker axis peaks earlier than the broader
  scripture-announcement content axes

## Timeline

1. Locked the prereg on the inherited `H-NEW-125` / `cross-finding-012`
   assets.
2. Reused the exact octile binning logic from `cross-finding-012`.
3. Forced an imported-family positive control:
   reproduced the parent Pattern-B observed peak bins exactly.
4. Computed the observed peak-lag statistic
   `L_peak = mean_content_peak - marker_peak`.
5. Ran `10000` Noldke-rank permutations with octile reassignment.
6. Wrote JSON and findings artifacts.

## Locked result

- observed marker peak:
  `B6`
- observed content peaks:
  `B7, B7, B6, B7`
- observed `L_peak`:
  `0.75`
- exact positive-control reproduction:
  `PASS`
- permutation `p_lag`:
  `0.42845715428457154`
- verdict:
  `NULL`

## Structural reading

The descriptive staircase is real and reproduced exactly, but the formal
peak-lag statistic is weak under the inherited null.

This means the project can still say:

- marker layer at `B6`
- most content axes at `B7`

But it cannot honestly say that this one-bin lead-lag is a protected formal
timing result.

## Interpretation

The run narrows the OQ-17 frontier instead of expanding it.

- `cross-finding-012` remains the correct formal anchor
- `cross-finding-017` remains descriptive refinement only
- the next honest OQ-17 move, if any, should be a richer margin-sensitive
  timing statistic rather than another coarse peak-bin test
