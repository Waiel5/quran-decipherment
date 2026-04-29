# H-NEW-273 Run 1 — Q1<->Q108 twin liturgical-anchor

**Date**: 2026-04-18  
**Agent**: codex  
**Seed**: 20260418  
**Verdict**: `PASS-NARROW`  
**Pre-reg SHA-256**: `a7d159419d9e33825345abd5a6b02647169c9c4d6f9347079c0621e0eabd9827`

## Task

Take ownership of `H-NEW-273` only and formalize a single bounded
`Q1 <-> Q108` twin liturgical-anchor test.

Constraints I followed:

- no HANDOFF edits
- no ledger edits
- no touching other H-NEW files
- ship one crisp operationalization, not a theory dump

## Scoping decision

I explicitly did **not** re-run the already-landed wrap-around distance
claim from `H-NEW-137/138`.

Instead I chose one narrow speech-act axis:

- divine-reference density
- imperative density

Surah score:

```text
S(s) = sqrt(D(s) * I(s))
D(s) = share of QAC STEM-root tokens in {Alh, rbb, rHm}
I(s) = IMPV tokens / verse
```

Pair score:

```text
T(a,b) = S(a) + S(b)
```

Primary target:

- `Q1 + Q108`

Primary null:

- exact enumeration of all unordered `Early Meccan` pairs with one surah
  in the `5-7`-verse bin and one in the `3-4`-verse bin

This gave a small but clean exact null, which was the main reason for
choosing the operationalization.

## Important honesty note

Metric-family choice was made after bounded local scoping of a handful of
candidate liturgical operationalizations. So this is the **first landed
formal run**, but not a discovery-blind gold-standard prereg.

That is why I kept the interpretation tight and treated the result as
`PASS-NARROW`, not as a large upgrade.

## Files created

1. `scripts/h_new_273_q1_q108_twin_liturgical_anchor.py`
2. `findings/phase-b-hypotheses/h-new-273-q1-q108-twin-liturgical-anchor-prereg.md`
3. `findings/phase-b-hypotheses/csv/h-new-273.json`
4. `findings/phase-b-hypotheses/h-new-273-q1-q108-twin-liturgical-anchor.md`
5. `journal/h-new-273-run-1.md`

## Formal run result

### Primary target: Q1 + Q108

Target components:

| Surah | Divine share | IMPV / verse | Surah score |
|---|---:|---:|---:|
| Q1 | 0.3043 | 0.1429 | 0.2085 |
| Q108 | 0.1429 | 0.6667 | 0.3086 |

Pair score:

- `T(Q1,Q108) = 0.517160`

Exact matched null:

- `N = 31` alternative pairs
- null mean `0.181099`
- null SD `0.151325`
- descriptive `z = +2.2208`
- exact upper-tail `p = 0.03125`
- descending rank `1 / 32`

Top competing null pairs:

1. `Q108 + Q114` = `0.452966`
2. `Q1 + Q112` = `0.432152`
3. `Q108 + Q113` = `0.424084`

### Descriptive contrast: Q113 + Q114

I also ran the obvious refuge-pair contrast under its own matched
Early-Meccan `5-7` + `5-7` null:

- score `0.259822`
- exact upper-tail `p = 0.107143`
- descending rank `3 / 28`

This did **not** pass.

## Interpretation note

The non-pass on `Q113 + Q114` is the reason the landed verdict is
`PASS-NARROW` rather than anything stronger.

The exact statement I am comfortable with is:

> on the locked `sqrt(divine-share x imperative-density)` axis,
> `Q1 + Q108` is the top matched short Early-Meccan pair.

The statement I am **not** comfortable with is:

> this metric is a general liturgical-pair detector.

It is not.

## Final disposition

`H-NEW-273` is landed as a bounded positive with explicit limits:

- primary exact null passes
- contrast genericity check does not
- result should stay pair-specific
