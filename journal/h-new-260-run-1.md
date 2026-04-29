# H-NEW-260 — Run 1 journal

**Date**: 2026-04-18  
**Specialist**: autonomous  
**Parent**: H-NEW-253  
**Seed**: 20260419  
**Runtime**: <1 second

## Procedure

1. Read the locked pre-reg `h-new-260-q54-q55-dyad-prereg.md`.
2. Inspected the existing script scaffold `scripts/h_new_260_q54_q55_dyad.py`.
3. Verified it matches the prereg closely enough to execute directly:
   - Cell A = joint verse-length ACF against adjacent-pair baseline
   - Cell B = root Jaccard against adjacent-pair baseline
   - Cell C = FR asymmetry against adjacent-triple baseline
4. Ran the script without modifying the inferential design.

## Results

- **Cell A**: NULL
  - `max|ACF| = 0.2558`
  - percentile = `54.85`
- **Cell B**: NULL
  - Jaccard = `0.1449`
  - percentile = `37.61`
- **Cell C**: NULL
  - `|d(54,55) - d(55,56)| = 0.0022`
  - percentile = `2.23`
  - upper-tail empirical `p = 0.9823`

Overall verdict:

- **0/3 PASS**
- **LENGTH_ADJACENCY_ARTIFACT / dyad claim collapses**

## Important interpretive note

Cell C fails in an especially informative way:

- the prereg expected **large asymmetry**
- the data show **near-symmetry**

So the Q 54-55-56 triple is not "Q 54 mirror vs Q 56 closure" under this
instrument. It is more evenly spaced than the adjacent-triple baseline.

## MW-5 sanity

Five random adjacent pairs were drawn.

- 0/5 replicated the Cell A + Cell B signature jointly.

So the null verdict is not an MW-5 failure or broken instrument issue.

## Conclusion

This run should **not** be read as weakening H-NEW-253's narrower
descriptive claim that Q 54 is the closest restricted Mode-B sibling to
Q 55. It only blocks the stronger upgrade to a preregistered
three-cell dyad.

The right downstream wording is:

- **Q 54 is a descriptive near-neighbour**
- **Q 54+Q 55 is not a formally supported architectural dyad**

## Files produced

- `findings/phase-b-hypotheses/h-new-260-q54-q55-dyad.md`
- `findings/phase-b-hypotheses/csv/h-new-260.json`
- `findings/phase-b-hypotheses/csv/h-new-260-adjacent-pair-baselines.csv`
- `journal/h-new-260-run-1.md`
