# [[h-new-258-bukhari-mh-replication|H-NEW-258]] — Bukhari M_H replication on the inherited H-147 instrument

**Finding ID**: [[h-new-258-bukhari-mh-replication|h-new-258]]  
**Date**: 2026-04-18  
**Specialist**: autonomous  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-258-bukhari-mh-replication-prereg.md`  
**Pre-reg SHA-256**: `5bf851ff1406f95c6e331b829013b45e02f0300ea1abcec5ecd1d7864df56cca`  
**Seed**: 20260424  
**Parents**: `[[h-new-147-bukhari-cross-corpus|h-new-147]]-bukhari-cross-corpus.md` file lineage / on-disk JSON id `[[h-new-145-muq-code-decoding|h-new-145]]`; `[[h-new-236-1b-mufassal-terminal-mechanism|h-new-236-1b]]-mufassal-terminal-mechanism.md`  
**Rules tuple**: `(Bukhari segmentation/order instrument inherited exactly from [[h-new-147-bukhari-cross-corpus|H-NEW-147]]: split `bukhari-noquran.txt` on `باب`, whitespace tokenization, light-stemming, top-500 roots, Fisher-Rao arccos-Bhattacharyya, retain the 114 longest segments in the post-sort order used by [[h-new-147-bukhari-cross-corpus|H-NEW-147]]; top-K canonical consecutive-edge preservation over that retained sequence; chain-order local search with fixed chain orientation; seed 20260424)`  
**Verdict**: **LOOSE-ANALOGUE.** On the inherited Bukhari instrument, the canonical retained-segment path is open at `K=0` but already closes at `K=15`. `K=100` also closes, but only as a low-tail near-boundary cell. The Quran's `M_H top-100` closure therefore does **not** replicate at comparable density on Bukhari; the Bukhari path-only analogue is much looser and less specific.

---

## Headline

Using the exact Bukhari segmentation / Fisher-Rao instrument from
`[[h-new-147-bukhari-cross-corpus|H-NEW-147]]`, I asked the nearest honest cross-corpus question:

> if we preserve the top-K highest-distance canonical consecutive edges
> of the inherited Bukhari segment sequence, does the canonical Bukhari
> order become generatively typical in the same way the Quran does under
> `[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]`?

The answer is **yes in a weak path-only sense, but no in the dense Quranic
sense**.

- `K=0` remains clearly open:
  empirical `L_path = 108.1640` vs sim mean `103.7244`, 95% CI
  `[102.3024, 104.9985]`, percentile `100.0`.
- `K=15` already closes:
  sim mean `107.5352`, 95% CI `[106.0366, 108.9043]`, empirical
  percentile `78.0`, with `85.84%` closure of the `K=0` mean-gap.
- `K=30`, `K=50`, and `K=100` all also close, but they **over-shift the
  simulator above the empirical canonical path**:
  empirical percentiles `16.0`, `9.7`, and `8.3` respectively.
- `K=100` is therefore **not** the informative Bukhari analogue. The
  first closing cell is already `K=15`.

So the cross-corpus read is straightforward:

> Bukhari admits a preserved-adjacency scaffold analogue, but it is much
> looser than the Quran's landed `M_H top-100` story. On this inherited
> Bukhari instrument, dense top-100 saturation is unnecessary and
> actually mis-centers the simulator.

## 1. Control reproduction

Before interpreting any hinge cells, the script reproduced the inherited
`[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` Bukhari instrument:

| Quantity | Parent (`[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` JSON id `[[h-new-145-muq-code-decoding|h-new-145]]`) | Recomputed here | Delta |
|---|---:|---:|---:|
| `L_canonical` | `108.1640` | `108.1640` | `0.0000` |
| `L_2opt` best-of-10 | `90.4096` | `90.2285` | `-0.1811` |

Both values are within the pre-registered `0.5`-unit tolerance.
**Control PASS.** The run is using the same retained Bukhari sequence
and the same Fisher-Rao geometry family as the parent.

## 2. Cell table

| Cell | Chains left | Sim mean `L_path` | Sim 95% CI | Empirical pct | Mean-gap `emp - sim` | Verdict |
|---|---:|---:|---:|---:|---:|---|
| `K=0` | 114 | `103.7244` | `[102.3024, 104.9985]` | `100.0` | `+4.4396` | `OPEN-HIGH` |
| `K=15` | 99 | `107.5352` | `[106.0366, 108.9043]` | `78.0` | `+0.6288` | `CLOSED` |
| `K=30` | 84 | `108.6933` | `[107.3555, 109.7300]` | `16.0` | `-0.5293` | `CLOSED` |
| `K=50` | 64 | `109.0152` | `[107.7391, 109.9965]` | `9.7` | `-0.8512` | `CLOSED` |
| `K=100` | 14 | `108.5340` | `[108.1168, 109.3151]` | `8.3` | `-0.3700` | `CLOSED` |

### Immediate read

1. The inherited Bukhari canonical order is genuinely above the
   unconstrained local-minimum family at `K=0`.
2. A **small** preserved-edge scaffold is already sufficient to bring it
   inside.
3. Heavier hinge saturation does **not** improve centering. It pushes
   the simulated mean above empirical and leaves the canonical sequence
   sitting in the lower tail.

That is not the Quranic `236.1b` pattern. The Quranic top-100 cell was a
strict 4/4 closure result with the empirical mushaf near the upper part
of the simulator but still tightly aligned across multiple observables.
The Bukhari result here is path-only and becomes weakly over-constrained
as K rises.

## 3. What the first closing cell says

The best new number in this run is simply:

> **`first_closing_k = 15`**

That matters more than the fact that `K=100` also closes.

At `K=15`, the canonical retained Bukhari path has already moved from a
clear positive miss (`+4.44` Fisher-Rao units above the `K=0` sim mean)
to a modest residual (`+0.63` above the `K=15` sim mean), while
remaining comfortably inside the simulator interval at percentile `78.0`.

This means the Bukhari instrument does **not** require anything like the
Quran's dense `M_H top-100` scaffold to recover its canonical path. The
high-cost-adjacency logic is present, but it is much more compressible.

## 4. Why `K=100` is not the main story

If one looked only at the `K=100` cell, one could say:

> "Bukhari also closes under top-100 preserved canonical edges."

That sentence is technically true but substantively misleading.

The actual `K=100` pattern is:

- only `14` chains remain free
- sim mean `108.5340` is already **above** empirical `108.1640`
- empirical percentile is only `8.3`
- the lower CI bound `108.1168` sits just beneath empirical

So `K=100` closes, but not in a strong "the empirical sequence is where
the constrained simulator naturally wants to live" sense. It is a
near-boundary low-tail closure under high saturation.

The stronger and cleaner Bukhari result is the opposite: sparse
preservation at `K=15` already does most of the work.

## 5. Cross-corpus interpretation

### What generalizes

- Preserving a small set of high-cost canonical consecutive edges does
  carry real generative information outside the Quran.
- Bukhari's inherited retained-segment sequence is not just a generic
  random order under the same Fisher-Rao geometry family.

### What does not generalize

- The **density** of the Quranic `M_H top-100` closure does not carry
  over.
- On Bukhari, the analogue is already present at `K=15`; by `K=30+` the
  simulator is no longer centering the empirical canonical path better,
  it is overshooting it.

### Straight read

The Quranic `[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]]` result looks **unusually dense/specific**
relative to this Bukhari baseline. Bukhari supports the existence of
hinge-scaffold logic in a broad sense, but not the need for a dense
top-100 preserved-adjacency law on the one observable available here.

## 6. Top-15 scaffold content

The first closing Bukhari scaffold (`K=15`) preserves these canonical
edges in the inherited retained-order numbering:

- `14-15`
- `109-110`
- `62-63`
- `110-111`
- `10-11`
- `56-57`
- `13-14`
- `78-79`
- `54-55`
- `70-71`
- `68-69`
- `77-78`
- `95-96`
- `96-97`
- `19-20`

This is a scattered path scaffold, not a single concentrated terminal
patch. That is another reason the Bukhari result should not be read as a
clean analogue of the Quran's late-terminal closure story.

## 7. Honest limits

1. This is a **path-only** cross-corpus analogue. It cannot reproduce
   the Quran-side 4/4 closure criterion because Bukhari lacks matched
   block / tail observables.
2. The inherited Bukhari "canonical" sequence is the exact
   `[[h-new-147-bukhari-cross-corpus|H-NEW-147]]` retained-order instrument, which sorts segments by length
   before retaining the top 114. It is not a raw recovered bab order.
3. The parent file / JSON naming mismatch is real: the file lineage says
   `147`, while the on-disk JSON id is `[[h-new-145-muq-code-decoding|h-new-145]]`.
4. The constrained local-search family here is fresh for `[[h-new-258-bukhari-mh-replication|H-NEW-258]]`.
   The control reproduction shows it is on the right geometry, but it is
   still a new implementation.
5. Because the Bukhari instrument has only one primary observable, any
   Quran-vs-Bukhari density comparison must be treated as suggestive,
   not exact.

## 8. Honest conclusion

`[[h-new-258-bukhari-mh-replication|H-NEW-258]]` lands a qualified cross-corpus replication.

There **is** a Bukhari preserved-adjacency analogue: the inherited
canonical Bukhari path is open at `K=0` and closes once the top `15`
canonical Fisher-Rao edges are preserved. But that is precisely why the
result does **not** look like the Quran's `M_H top-100` closure in any
strong sense. On this inherited Bukhari instrument, the scaffold signal
is much looser, and dense `K=100` saturation is unnecessary.

The cleanest interpretation is:

> scaffold logic is not uniquely Quranic, but the Quranic top-100
> closure remains unusually dense and specific relative to this Bukhari
> baseline.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-258-bukhari-mh-replication-prereg.md`
- Script: `scripts/h_new_258_bukhari_mh_replication.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-258.json`
- Journal: `journal/h-new-258-run-1.md`
