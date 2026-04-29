# [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] — OQ-18 Q17 conditional bridge test

## Summary

[[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] left a narrow residual problem inside `Q16..Q25`: the
locked concept/object nucleus `{Q16, Q21, Q22, Q23, Q25}` passed the
exact pairwise-localization test, but it was only rank `8 / 252`, and
every one of the seven strictly better relabelings included `Q17`.

[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] turns that observation into the tightest bounded follow-up
available on the same instrument:

- keep the same `Delta_pair` statistic from [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]]
- keep the same fixed `Q16..Q25` zone
- condition the exact null on `Q17` being excluded from the positive
  side

Under that `126`-state conditioned space, the locked nucleus is the
**unique exact maximum**.

## Result

Primary statistic reused from [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]]:

`Delta_pair(S) = mean_jaccard(++) - mean_jaccard(other pairs)`

Observed at the locked nucleus
`S* = {Q16, Q21, Q22, Q23, Q25}`:

- mean Jaccard across `++` pairs = `0.34138556942690185`
- mean Jaccard across `other` pairs = `0.31251771040264437`
- observed `Delta_pair(S*) = 0.02886785902425748`

Primary conditioned null:

- admissible space = all `C(9,5) = 126` five-surah subsets of `Q16..Q25`
  with `Q17` excluded from the positive side

Exact conditioned result:

- exact descending rank = `1 / 126`
- subsets `>=` observed = `1`
- exact upper-tail `p = 1 / 126 = 0.007936507936507936`
- conditioned null mean = `-0.004939076660072468`
- conditioned null median = `-0.006061755410743996`
- conditioned null min = `-0.03169181948860378`
- conditioned null max = `0.02886785902425748`

Verdict: **PASS-DIRECTED**

## Why this is stronger than [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]]

[[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] gave the full-space result:

- observed `Delta_pair(S*) = 0.02886785902425748`
- exact rank = `8 / 252`
- exact upper-tail `p = 8 / 252 = 0.031746031746031744`

[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] asks what happens once the specific leak candidate from that
result, `Q17`, is barred.

The answer is sharp:

- among the `126` assignments that exclude `Q17`, **none** beats the
  locked nucleus
- among the `126` assignments that include `Q17`, **seven** beat the
  locked nucleus

That is exactly the pattern expected if `Q17` is the single residual
bridge around an otherwise stable nucleus.

## Descriptive bridge diagnostics

These numbers are descriptive only, but they point in the same
direction.

Best one-swap outsider replacement of the locked nucleus:

- `Q17` replacing `Q21` gives
  `{Q16, Q17, Q22, Q23, Q25}` with `Delta_pair = 0.0346190439274357`
  and gain `+0.005751184903178219`
- `Q20` replacing `Q22` gives `Delta_pair = 0.023534808510252636`
  and gain `-0.0053330505140048445`
- `Q18` replacing `Q21` gives `Delta_pair = 0.02283488740258932`
  and gain `-0.0060329716216681595`
- `Q24` replacing `Q25` gives `Delta_pair = 0.018458974618540347`
  and gain `-0.010408884405717134`
- `Q19` replacing `Q21` gives `Delta_pair = 0.007298358714302788`
  and gain `-0.021569500309954692`

Mean Jaccard from each outsider to the locked nucleus:

- `Q17` = `0.3420193401695428`
- `Q20` = `0.32168166956743544`
- `Q18` = `0.3163796176488051`
- `Q24` = `0.30826448956935626`
- `Q19` = `0.2889420860360043`

So even on the bounded descriptive side, `Q17` is not just one outsider
among several. It is the only outsider whose best single swap actually
improves the target statistic.

## Interpretation

This is the strongest honest bounded statement now available for the
`Q17` branch:

- the [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] nucleus is real at the pair level
- the residual mismatch in [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] is not diffuse across the whole
  complement
- it is concentrated at `Q17`

That does **not** mean `Q17` belongs inside the locked [[h-new-126-isolate-core|H-NEW-126]]
concept/object class. The categorical label claim from [[h-new-286-oq18-within-zone-name-class-contrast|H-NEW-286]] stays
unchanged.

What [[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] shows is narrower and more exact:

> for the pairwise root-overlap table inside `Q16..Q25`, the name-class
> nucleus is fully stable once `Q17` is removed from contention.

So the remaining leak is a **single-bridge phenomenon**, not a broad
failure of the name-class mechanism.

## Bottom line

[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]] upgrades the vague [[h-new-286-1-oq18-pairwise-name-class-localization|H-NEW-286.1]] leak note into a precise
bounded result.

Conditioned on `Q17` being excluded from the positive side, the locked
OQ-18 nucleus `{Q16, Q21, Q22, Q23, Q25}` is the **unique optimum** of
the exact pairwise-localization statistic, with
`p = 1 / 126 = 0.0079365`.

That is strong evidence that `Q17` is the real residual bridge around
the OQ-18 nucleus inside `Q16..Q25`.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-286-2-q17-conditional-bridge-test-prereg.md`
- Script: `scripts/h_new_286_2_oq18_q17_conditional_bridge_test.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-286-2.json`
- Journal: `journal/h-new-286-2-run-1.md`
