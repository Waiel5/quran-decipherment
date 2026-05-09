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
