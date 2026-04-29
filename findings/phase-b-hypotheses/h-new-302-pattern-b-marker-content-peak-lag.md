# [[h-new-302-pattern-b-marker-content-peak-lag|H-NEW-302]] - Pattern-B marker-versus-content peak-lag test

**Finding ID**: `[[h-new-302-pattern-b-marker-content-peak-lag|h-new-302]]`  
**Date**: `2026-04-20`  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-302-pattern-b-marker-content-peak-lag-prereg.md`  
**Pre-reg SHA-256**: `4c590bf8e33133ad89ddcc5f6203f32936c4df21677ec7dfce5a0e785fa12e84`  
**Seed**: `20260420`  
**Rules tuple**: `(reuse [[h-new-125-chronology-content|H-NEW-125]] per-surah axis values exactly; reuse [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] equal-count Noldke octile bins B1..B8 exactly; marker axis = muq_cardinality; content axes = qul_density, book_reference_density, eschatological_density, loanword_density; for each axis define peak_bin(a) as the smallest octile attaining the maximum observed bin mean; primary statistic L_peak = mean_content peak_bin(a) - peak_bin(marker); null by 10000 permutations of the 114 Noldke ranks across surahs with octile reassignment recomputed each time; one-sided upper-tail for content peaking later than marker; imported-family positive control = exact reproduction of [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] observed Pattern-B peak bins under the inherited observed octile mapping)`  
**Verdict**: **NULL**. The descriptive `B6/B7` staircase is real, but the formal peak-lag statistic is not unusual under the inherited rank-shuffle null: `L_peak = 0.75`, `p_lag = 0.428457`.

## Headline

This run asked a narrower OQ-17 question than `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`:

> once the scripture-announcement apparatus is already known to cohere across
> Noldke octiles, do the broader content axes actually peak later than the
> muqattaat marker axis in a way that survives the inherited permutation null?

Answer:

- **descriptively yes**
- **inferentially no**

So the `B6/B7` split remains a useful descriptive refinement, but not a formal
timing result.

## 1. Imported-family positive control

Before any new inference, the run had to reproduce the parent
`[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]` Pattern-B peak bins under the inherited observed octile
mapping.

It did exactly:

| Axis | Reproduced peak |
|---|---:|
| `qul_density` | `B7` |
| `book_reference_density` | `B7` |
| `eschatological_density` | `B6` |
| `muq_cardinality` | `B6` |
| `loanword_density` | `B7` |

That imported-family positive control passed cleanly, so the new null result is
about the statistic, not a broken pipeline.

## 2. Observed peak-lag statistic

Locked axes:

- marker: `muq_cardinality`
- content: `qul_density`, `book_reference_density`,
  `eschatological_density`, `loanword_density`

Observed peak bins:

- marker `muq_cardinality -> B6`
- content peaks -> `B7`, `B7`, `B6`, `B7`

Primary statistic:

`L_peak = mean(7, 7, 6, 7) - 6 = 0.75`

So the descriptive picture is exactly the staircase already discussed in
continuity:

- marker layer peaks at `B6`
- most content axes peak one bin later at `B7`

## 3. Permutation result

Null:

- `10000` Noldke-rank shuffles
- octile reassignment recomputed each time
- one-sided upper-tail for larger positive lag

Primary result:

| Metric | Value |
|---|---:|
| `L_peak` | **0.75** |
| `p_lag` | **0.428457** |
| Null mean | 0.171675 |
| Null q95 | 4.25 |
| Null q99 | 5.5 |
| Null max | 7.0 |
| Descending rank | 3922 / 10001 |

`4284 / 10000` permutations met or exceeded the observed lag, so the observed
`0.75` lead-lag is nowhere near unusual enough to support a pass.

## 4. Why the result is null

The key point is not that the observed direction disappears. It does not.

The key point is that the statistic is too coarse to isolate a strong timing
signal under this null family:

- each axis contributes only its single peak octile
- peak locations can jump substantially under shuffled rank assignments
- one-bin marker/content separations are common enough that the observed
  `B6/B7` split does not stand out

So this is not a contradiction of `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]`. It is a limit on how far
the inherited octile peak-bin statistic can be pushed.

## 5. Interpretation

The honest read is:

- `[[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]` still provides the formal OQ-17 anchor
- `[[cross-finding-017-b6-b7-staircase|cross-finding-017]]` still provides the right descriptive refinement
- but the stronger sentence
  "the marker layer formally peaks earlier than the content layer"
  is **not certified**

In practical terms:

> the scripture-announcement apparatus remains real, but the `B6 -> B7`
> marker-first/content-lag reading stays descriptive only.

## 6. Implication for OQ-17

This run narrows the chronology frontier again.

If OQ-17 work continues, the next honest move should **not** be another coarse
peak-bin statistic. It should be a richer margin-sensitive timing instrument, or
else the project should stay with the broader concordance result and stop trying
to over-formalize the `B6/B7` wrinkle.

That is exactly consistent with the lesson already learned from `[[h-new-129-joint-late-meccan-peak|H-NEW-129]]`:
coarse timing summaries are fragile in this branch.

## 7. Honest limits

1. This was a post-hoc formalization of an already disclosed descriptive
   asymmetry, not a discovery-clean new branch.
2. The null is specific to Noldke-rank shuffles plus octile reassignment.
3. A null here does not weaken the broader scripture-announcement apparatus; it
   only limits the marker-versus-content lead-lag overclaim.
