# H-NEW-265 Run 1 — v1-w1 qul-openers micro-cluster

**Date**: 2026-04-18  
**Agent**: h-new-265-specialist  
**Seed**: 20260418  
**N_PERM**: 10,000  
**Bonferroni**: `k = 3`, `alpha_bon = 0.0167`  
**Verdict**: `NULL`  
**Pre-reg SHA-256**: `591bfca98c86eeaaab179d734e33df33b8ea1d1d08c70275b9cecff9fd9d3d4b`

## Task

Land H-NEW-265 as a **tight** formal test of whether the five v1-w1
`qul`-openers `{Q72, Q109, Q112, Q113, Q114}` form a coherent
micro-cluster **after stripping the trivial opener itself**.

## Design actually locked

Three inferential cells, all one-sided upper:

1. **Cell A** — v1 residual root-set Jaccard after dropping word 1
2. **Cell B** — v1-v3 residual root-set Jaccard after dropping v1-w1
3. **Cell C** — whole-surah root-set Jaccard after removing opener-root
   `qwl`

All three cells use the same matched-null discipline:

- QAC STEM-token mass computed at the exact cell window
- nearest-12 by `|log(token_mass+1)|`
- random matched 5-sets sampled without replacement
- 10,000 draws

MW-5 control locked before execution:

- `MUSABBIHAT_INNER_5 = {57,59,61,62,64}`
- same three cells
- same opener-stripping logic
- Cell C removes control opener-root `sbH`
- MW-5 must pass at nominal `p < 0.05` on all 3 cells

## Implementation

Created:

- `scripts/h_new_265_qul_openers_microcluster.py`
- `findings/phase-b-hypotheses/csv/h-new-265.json`
- findings markdown
- this journal

No non-owned files touched.

## Execution result

### Target quintet

| Cell | Observed | Null mean | p_perm | Verdict |
|---|---:|---:|---:|---|
| A | 0.0500 | 0.0133 | 0.0579 | NULL |
| B | 0.0512 | 0.0227 | 0.0702 | NULL |
| C | 0.0379 | 0.0259 | 0.0975 | NULL |

`0/3` cells pass Bonferroni.

### MW-5 positive control

| Cell | Observed | Null mean | p_perm | Verdict |
|---|---:|---:|---:|---|
| A | 0.6406 | 0.0392 | 0.0001 | PASS |
| B | 0.1866 | 0.0699 | 0.0001 | PASS |
| C | 0.2497 | 0.1625 | 0.0001 | PASS |

MW-5 is cleanly valid on all 3 cells. Pipeline is not broken.

## Main structural readout

The 5-set does not behave like a unified quintet after opener stripping.
The overlap collapses mostly to the already-known short-tail pair
**Q113 + Q114**:

- Cell A: only Q113↔Q114 is non-zero (`0.50`)
- Cell B: Q113↔Q114 = `0.20`, Q112↔Q114 = `0.125`, everything else weak or zero
- Cell C: Q113↔Q114 = `0.176`, Q112↔Q114 = `0.067`, Q72 does not stay close

This is the key reason the result lands `NULL` rather than
`DIMENSION-SPECIFIC`.

## Interpretation

H-NEW-74's literal opener result stands:

- `{72,109,112,113,114}` is the exact v1-w1 `qul` opener inventory

H-NEW-265 narrows the claim:

- beyond the literal shared opener, the quintet does **not** form a
  Bonferroni-surviving lexical micro-cluster under the locked matched
  null

The strongest genuine sub-family inside the five remains the
muʿawwidhatān pair, with limited spillover to Q112.

## Honest limits

- All three cells are lexical-root Jaccard variants, so they are
  correlated.
- The nearest-12 matched null is a heuristic, chosen to keep MW-1
  explicit without expanding scope.
- This run does not test liturgical or hadith familyhood, only lexical
  opener-stripped coherence.

## Files written

1. `scripts/h_new_265_qul_openers_microcluster.py`
2. `findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster-prereg.md`
3. `findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster.md`
4. `findings/phase-b-hypotheses/csv/h-new-265.json`
5. `journal/h-new-265-run-1.md`
