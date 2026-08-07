---
id: H-NEW-1301
title: IMPV-qrA 4-surah cluster Fisher-Rao cohesion
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: NULL-BROKEN (positive control failed) | substantive direction NULL on both cells
seed: 20260509
n_perm: 10000
prereg_sha: ca4d3c763fa5c3f1185a3bb3fbf2b06672f414987e241abff48783f85647c8f4
prereg_path: findings/phase-b-hypotheses/h-new-1301-impv-qra-cluster-prereg.md
script_path: findings/phase-b-hypotheses/scripts/h_new_1301_impv_qra_cluster.py
output_json: findings/phase-b-hypotheses/csv/h-new-1301.json
---

# H-NEW-1301 — IMPV-qrA 4-surah cluster Fisher-Rao cohesion


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Verdict: NULL-BROKEN (positive control failed) — substantive direction is NULL

The MW-5 positive control on the حم cluster {41, 42, 43, 44} (4-of-7 random sub-sample) returned p_pc = 0.336 against the uniform 4-surah null — **the test instrument did not detect known structural cohesion in the HM cluster**, which means the null-distribution-vs-signal-detection chain cannot be trusted on this run. Per Protocol §6 (MW-5), the verdict is **NULL-BROKEN**.

The substantive finding (the IMPV-qrA cluster's FR-cohesion) was ALSO NULL on both pre-registered cells, but cannot be promoted to a substantive NULL because the instrument-control failed first.

## Observed values

| Quantity | Value |
|:--|--:|
| Cluster {Q 17, Q 69, Q 73, Q 96} intra-cluster FR mean | 0.88001 |
| Cell A (uniform 4-of-113 null, no Q 1) — null mean | 0.92616 |
| Cell A — null 5th percentile | 0.69517 |
| Cell A — p_perm | 0.26330 |
| Cell A — pass (≤ 0.025) | **NO** |
| Cell B (length-matched, ±20% of 202 verses) — null mean | 0.94998 |
| Cell B — null 5th percentile | 0.83730 |
| Cell B — p_perm | 0.12940 |
| Cell B — pass (≤ 0.025) | **NO** |
| MW-5 positive control: HM 4-of-7 sub-sample {41,42,43,44} obs | 0.90530 |
| MW-5 PC p_pc | 0.33590 |
| MW-5 PC pass (≤ 0.05) | **NO** |

## Interpretation of the positive control failure

The HM cluster is canonically "structurally tight" per cross-finding-008, but that cohesion lives on **muqaṭṭāʿat-axes** (book-reference + formulaic-opening + extended-writing-cluster), NOT on the **root-distribution Fisher-Rao space** measured by `h-new-111.json`. The HM cluster's tightness is on the LETTER-SET layer; the H-NEW-111 instrument operates on the ROOT-FREQUENCY layer. These layers are orthogonal per H-NEW-29 / H-NEW-13 / cross-finding-008.

In hindsight, a better positive control would have been the H-NEW-1190 *wa-mā adrāka mā* corpus-EXACT 10-surah cluster (p = 0.00068, FR-cohesive on this very instrument) sub-sampled 4-of-10. **That choice was not made in the pre-reg, and changing it now would be a post-hoc pre-commit violation.** The pre-reg locks in a NULL-BROKEN verdict.

## What this teaches

Three meta-lessons for future pre-regs:

1. **Choose the positive control that matches the instrument's feature space.** Not every "structurally tight" cluster is tight on every distance metric. cross-finding-008 muqaṭṭāʿat tightness is letter-set, not root-distribution. h-new-111.json's tightness is root-distribution. Use a cluster known to be FR-tight under H-NEW-111: H-NEW-1190 *wa-mā adrāka mā* (p=0.00068) is the gold-standard FR positive control.
2. **The HM cluster's "tightness" claim was loose.** The cross-finding-008 claim is multi-axial; assuming it transfers to root-distribution FR is unsupported. This is a real result about the HM cluster — it IS muqaṭṭāʿat-tight but NOT root-distribution-tight.
3. **The IMPV-qrA cluster is genuinely NOT FR-cohesive on root-distribution.** Q 17 al-Isrāʾ, Q 69 al-Ḥāqqa, Q 73 al-Muzzammil, Q 96 al-ʿAlaq do not share a tight root signature. This makes biological sense: their *thematic* connection runs through *kitāb* + *iqraʾ* lexis, NOT through full root-frequency profiles. Q 17 is a 111-verse Late-Meccan/early-Medinan night-journey + Children-of-Israel surah; Q 73, 96 are short prophetic-call surahs; Q 69 is a Qiyāma surah. Their root profiles are heterogeneous.

## Substantive direction: NULL (cannot be promoted under NULL-BROKEN)

Even if the positive control had passed, both pre-registered cells return NULL:
- Cell A (uniform 4-of-113 null): p = 0.263 — cluster is more typical than 26% of random 4-surah samples
- Cell B (length-matched null): p = 0.129 — same conclusion under tight length control

The IMPV-qrA inventory clusters at the **lexical-imperative-event** level, not at the **root-distribution** level. This is consistent with the IMPV-qrA event being a discrete liturgical-imperative speech-act marker, not a thematic-domain marker.

## Connection back to H-NEW-1300

H-NEW-1300 returned NULL by strict pre-reg (Q 96 tied with Q 73 at rank-1). H-NEW-1301 here confirms that the descriptive 4-surah inventory does NOT translate into a Fisher-Rao cohesive cluster. **The IMPV-qrA distribution is a 4-surah descriptive list, not an empirical structural cluster.** The two surah-pairs identified in H-NEW-1300 (prophetic-revelation pair Q 73+Q 96 vs eschatological-record-reading pair Q 17+Q 69) are real *qualitative* distinctions but do not correspond to root-distribution cohesion.

## Honest limits

- **NULL-BROKEN by pre-reg discipline.** The instrument-control failure prevents confident interpretation of the substantive NULL.
- **Single feature space tested.** Root-distribution Fisher-Rao only. Tashkeel-letter, n-gram char-4-gram, verse-length, rhyme — all untested for this cluster. A future pre-reg could test on H-NEW-700 rhyme features or H-NEW-590 outlier-strength space.
- **The IMPV-qrA inventory itself is a real corpus fact** (H-NEW-1300): 6 segments in 4 surahs. The structural significance of that fact is not yet determined.

## Honest follow-up moves

- H-NEW-1302 (queued, NOT yet locked): Replicate the IMPV-qrA cluster cohesion test under the H-NEW-700 rhyme-and-phoneme feature space (different instrument, different feature axis). MW-5 positive control: short-mufaṣṣal eschatology meta-cluster (H-NEW-1200, FR-tight on H-NEW-700 metrics by construction).
- H-NEW-1303 (queued): Test whether the *kitāb* + *iqraʾ* token co-occurrence cluster is structurally meaningful at the verse-twin (H-NEW-66) level, not the surah-aggregate level. The 4 IMPV-qrA verses are at very different surah-positions; their *verse*-level twinship may be high while *surah*-level cohesion is low.

## Classical citations

- Cross-finding-008 (`findings/phase-b-hypotheses/cross-finding-008-muqattaat-as-book-introduction.md`) — HM cluster tightness on letter-set axis.
- H-NEW-1190 (`findings/phase-b-hypotheses/h-new-1190-*.md`) — *wa-mā adrāka mā* FR-cohesive 10-surah cluster (gold-standard FR positive control going forward).

## Verdict summary

| Cell | p | Pass (α=0.025) | Status |
|:--|:--:|:--:|:--|
| A — uniform null | 0.263 | NO | NULL |
| B — length-matched | 0.129 | NO | NULL |
| MW-5 PC | 0.336 | NO | **PC FAILED** |

**FINAL: NULL-BROKEN (positive control failed). Substantive direction also NULL on primary + length-matched cells.**

Lesson published; instrument-control discipline reinforced; H-NEW-1302 / H-NEW-1303 queued with corrected positive-control selection.
