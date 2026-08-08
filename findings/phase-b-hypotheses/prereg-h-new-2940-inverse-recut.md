---
id: prereg-H-NEW-2940
title: "Pre-registration — the inverse re-cut: merge this corpus's own verses to prose unit lengths and measure Δ"
date: 2026-08-08
author: Waiel Al-Shujaa
status: LOCKED BEFORE RUN
replaces: the extrapolation in findings/phase-b-hypotheses/h-new-2930-unit-length-screen.md §3
opens: findings/phase-b-hypotheses/OPEN-H-NEW-2940-inverse-recut.md
---

# Pre-registration — H-NEW-2940, the inverse re-cut

Short by design. This locks a direction, one primary measurement, and a decision rule.

## 1. The question

`h-new-2930` corrected the pausal cross-corpus headline from 5.3× to 3.63× by **extrapolating a
nine-point linear fit 0.86 prose-ranges below the shortest book in the baseline**. That
extrapolation is the finding's weakest link and its own §4 says so.

Replace it with a measurement requiring **no baseline text**: merge this corpus's own adjacent
verses into longer units matching prose unit lengths, and measure Δ at the merged length. At a
merged length of ~65 words the comparison sits **inside** the 49–91 word prose range, so no
extrapolation is needed at all.

## 2. Instrument — reused, not reimplemented

Sections 0–6 of `findings/phase-b-hypotheses/scripts/h-new-2870.py` are executed **verbatim** by
`exec`, exactly as `findings/phase-b-hypotheses/scripts/h-new-2880.py` does: the phonemiser, the
pausal conventions, both rime extractors, the corpus load, GATE A (orthography) and GATE B
(instrument validation). Nothing is reimplemented. Both parent gates must pass or the run aborts.

Rime variant **R2** (the tanwin-transparent repair, primary in H-NEW-2880). Tuple **P1** only.

## 3. Reproduction gate — runs first, aborts everything downstream

Δ at native verse units under R2/P1 must reproduce the published value

    0.18686703691604045

to within 1e-12. **If it does not, the run stops and reports that; every number below is void.**

Note for the record: H-NEW-2930 and the task brief both write this as **0.18690**, which is this
same number at four decimals. There is no discrepancy — 0.186867 rounds to 0.1869.

## 4. Unit-length axis — a correction declared BEFORE the run

The nine prose books' unit lengths (49.16–91.12 words) were measured in
`findings/phase-b-hypotheses/scripts/h-new-2890.py` by `arabic_words(t)`, which is

    [w for w in t.split() if any("ء" <= c <= "ي" for c in w)]

On that same tokeniser this corpus has **77,429 words over 6,236 verses = 12.4165 words per
verse** — the figure `h-new-2890.py` itself prints for this corpus, as `12.4`.

**H-NEW-2930's "82,375 words / 13.21" is off this axis**: it counts the Tanzil `.txt`
(82,260 words, 13.19 per verse), a different file with different word splitting, and then plugs
that length into a fit calibrated on `arabic_words` lengths. The effect on 2930's headline is
small and is reported, not hidden: the predicted Δ moves from 0.05154 to 0.05187 and the residual
from 3.63× to 3.60×. **Every unit length in this run uses `arabic_words`.**

## 5. Merge rules — both fixed before any Δ is computed

Units never span a surah, matching how adjacent pairs have always been formed in this family.
A unit's label is `rime_of(" ".join(constituent verse texts), conv)`.

- **M1, primary — greedy threshold.** Walk a surah's verses in order accumulating into a unit;
  close the unit when its cumulative `arabic_words` count reaches T; a surah's trailing remainder
  forms a final, possibly short, unit.
- **M2, robustness — fixed group size.** Merge consecutive blocks of exactly g verses; a surah's
  final block may be shorter.

T and g are chosen by a **Δ-free rule**: the integer minimising
`|77429 / n_units − target|`. This depends only on corpus geometry and is computable, as it was,
before any Δ exists. For the primary target of 65 words this selects **T = 59**, achieving
**65.121** words per unit.

**Merge gate:** for every unit and both conventions, the label of the joined text must equal the
label of its **last constituent verse** — the instrument reads a unit's final word, so merging
must be exactly a thinning of the ending sequence. Any mismatch aborts the run.

## 6. Targets

**65 words is the primary and only required arm.** 50, 75 and 91 are run only if the primary
lands cleanly, and gate nothing.

## 7. The statistic and the one number

Δ = A(P1) − A(C) over adjacent unit pairs within surah, pooled across surahs — the same estimator
shape as the native Δ.

The deliverable is the **fraction of the gap closed**:

    f = (Δ_native − Δ_merged) / (Δ_native − Δ_prose)

with Δ_prose primary = **0.0304878**, the mean of H-NEW-2930's nine-book table, which is the
"~0.030" the decision rule was written against.

**Declared before the run, because it changes this denominator.** Each of 2930's nine per-book Δ
values is the **maximum over the six cells** that H-NEW-2910 reports for that book
({S5, S3, S0} stripping × {all pairs, readable pairs}); H-NEW-2910 designates no primary
segmentation. That selection inflates the prose baseline and therefore makes the residual
**conservative**. So f is also reported against the three internally consistent alternatives —
S5, S3 and S0 readable-pair means across all nine books — and against the fit prediction at the
achieved merged length.

Also reported: the **in-range residual ratio** Δ_merged / Δ̂(L_achieved), where Δ̂ is the
nine-book linear fit. This is the like-for-like successor to 2930's 3.63×, with no extrapolation.
**Fit gate:** refitting 2930's own table must reproduce its published slope −0.000398 and
intercept 0.05679 to the precision printed there.

## 8. Decision rule — the OPEN file's rule, made operational

| f | verdict |
|:--|:--|
| **f ≥ 0.75** | re-cutting closes most of the gap. Δ is a unit-length effect; the cross-corpus magnitude claim is **FINISHED AND WITHDRAWN**. |
| **f ≤ 0.25** | re-cutting closes little. The residual is **real and larger** than 2930's extrapolation suggested. |
| 0.25 < f < 0.75 | **PARTIAL** — reported as such, with no headline either way. |

## 9. Diagnostics — declared, non-gating

Phase offsets 0…g−1 under M2; agreement at verse lag g without merging; native Δ restricted to
the surahs that survive merging; and a randomised-segmentation arm at seeds 20260509 / 20260519.
None of these can change the verdict of §8.

## 10. Output discipline

Immutable run directory `runs/h-new-2940/<UTC stamp>`, `os.makedirs(..., exist_ok=False)`, all
writes in mode `'x'`. Checkpoints written **per arm** to `scratch/h-new-2940-checkpoints/`,
**outside** the run directory, write-once. Manifest paths repo-relative. No run directory is ever
deleted. **No finding is written to its final path before the run directory exists.** This
pre-registration is not edited after the run; `scripts/verify-prereg-locks.sh` enforces that.
