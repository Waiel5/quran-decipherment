---
id: H-NEW-1550
title: Oath-opener (qasamīyāt; *wa-l-* cosmic-or-natural-noun) whole-surah Fisher-Rao cohesion test
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1550-oath-opener-cluster (Cell A uniform + Cell B length-matched)
alpha_bon: 0.025
direction_of_effect: TIGHTER — mean intra-cluster Fisher-Rao distance over the 15 strict-*wa-l-*-oath-opener surahs is LOWER than the mean of 10,000 random equally-sized surah-cluster draws under uniform and length-matched nulls (one-tailed permutation null)
origin: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 67 (*al-aqsām fī l-Qurʾān*) catalogs the *qasamīyāt* — surahs opening with a cosmic/natural-object oath formula. The strict-formula subset is the surah whose first verse begins with **wāw + definite article + cosmic/natural noun** (e.g. *wa-l-shams*, *wa-l-fajr*, *wa-l-tīn*, *wa-l-ʿaṣr*). This is a THICK surface-orthographic marker — the entire opening block is the oath-formula apparatus — and predominantly Early-Meccan short-mufaṣṣal in chronological placement. The cluster should therefore exhibit Fisher-Rao cohesion at WHOLE-SURAH scale, in contrast to the discourse-marker NULLs (H-NEW-1360 prophet-vocative whole-surah NULL, H-NEW-1330 sajda NULL, H-NEW-1340 al-ḥamdu NULL) where the marker is a thinner deictic/devotional cue rather than a sustained opening-formula apparatus.
verdict_ceiling: PASS-DIRECTED (k=2 Bonferroni; MW-5 PC arm via H-NEW-1190 sub-sample)
rules_tuple:
  orthography: no-tashkeel (for FR root-distribution; min-tashkeel reserved for v1 grep verification)
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1 (Q 1 not in cluster; immaterial)
  verse_numbering: hafs-kufan
  detection_rule: v1 begins with strict-oath formula `r"^\s*وال"` over no-tashkeel text (wāw + definite article + noun); excludes *lā-uqsimu* (Q 75, Q 90) and muqaṭṭaʿ-then-oath (Q 68 `ن ۚ والقلم`); muqaṭṭaʿ-only openings (Q 36 يس) excluded
  null_model: 10,000 random draws of 15 surahs from {1..114} (uniform); 10,000 length-matched draws constrained to total verse-count within ±20% of the cluster total (587 verses)
  fr_source: findings/phase-b-hypotheses/csv/h-new-111.json (114×114 Fisher-Rao distance matrix on QAC stem-roots)
---

# H-NEW-1550 pre-registration — Oath-opener (qasamīyāt) cluster Fisher-Rao cohesion


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

## Origin and classical anchor

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, **nawʿ 67** (*al-aqsām fī l-Qurʾān* — "the oaths in the Qurʾān") catalogs and classifies the divine oaths. The strict-formula sub-class is the set of surahs whose **first verse** begins with the oath-particle wāw + definite article + cosmic or natural object: *wa-l-shams*, *wa-l-layl*, *wa-l-ḍuḥā*, *wa-l-tīn*, *wa-l-ʿaṣr*, *wa-l-fajr*, *wa-l-najm*, *wa-l-ṭūr*, *wa-l-dhāriyāt*, *wa-l-ṣāffāt*, *wa-l-mursalāt*, *wa-l-nāziʿāt*, *wa-l-burūj* (`wa-l-samāʾi dhāti l-burūj`), *wa-l-ṭāriq* (`wa-l-samāʾi wa-l-ṭāriq`), *wa-l-ʿādiyāt*.

This is a **thick surface-orthographic marker** — the entire opening block is the *qasam* apparatus, not a 1-2 word deictic or imperatival cue. Chronologically, these are predominantly Early-Meccan short-mufaṣṣal (al-Suyūṭī assigns them to the early Meccan strata in *al-Itqān* nawʿ 1). The thick-marker + chronological-clustering combination predicts whole-surah FR cohesion, in contrast to the recent discourse-marker NULL family:

- H-NEW-1360 (prophet-vocative *yā-ayyuhā al-nabī*, 6-surah set): whole-surah FR NULL at p = 0.5734
- H-NEW-1330 (sajda surahs): whole-surah FR NULL
- H-NEW-1340 (al-ḥamdu li-llāhi opener-only surahs): whole-surah FR NULL

The differentiating prediction is: thick + chronologically-clustered → FR-cohesive at whole-surah scale; thin/scattered → NULL at whole-surah scale (potentially cohesive at narrower pericope scale per cross-finding-025).

## Cluster — strict reverification at runtime

The cluster is locked to the set of 15 surahs whose v1 begins with `r"^\s*وال"` over `quran-text/quran-no-tashkeel.json`:

| Surah | Opening (no-tashkeel) | Verses |
|:--|:--|:--|
| Q 37 al-Ṣāffāt | والصافات صفا | 182 |
| Q 51 al-Dhāriyāt | والذاريات ذروا | 60 |
| Q 52 al-Ṭūr | والطور | 49 |
| Q 53 al-Najm | والنجم إذا هوى | 62 |
| Q 77 al-Mursalāt | والمرسلات عرفا | 50 |
| Q 79 al-Nāziʿāt | والنازعات غرقا | 46 |
| Q 85 al-Burūj | والسماء ذات البروج | 22 |
| Q 86 al-Ṭāriq | والسماء والطارق | 17 |
| Q 89 al-Fajr | والفجر | 30 |
| Q 91 al-Shams | والشمس وضحاها | 15 |
| Q 92 al-Layl | والليل إذا يغشى | 21 |
| Q 93 al-Ḍuḥā | والضحى | 11 |
| Q 95 al-Tīn | والتين والزيتون | 8 |
| Q 100 al-ʿĀdiyāt | والعاديات ضبحا | 11 |
| Q 103 al-ʿAṣr | والعصر | 3 |

**Cluster size: 15. Total verses: 587.**

Explicitly excluded (per pre-registered inclusion criteria — strict-oath formula only):

- Q 68 al-Qalam (نٓ ۚ والقلم وما يسطرون) — muqaṭṭaʿ-letter precedes the oath particle; not strict-opener.
- Q 75 al-Qiyāma (لا أقسم بيوم القيامة) — *lā-uqsimu* negation-oath formula; different oath-syntax.
- Q 90 al-Balad (لا أقسم بهذا البلد) — same as Q 75.
- Q 36 Yā-Sīn — opens with muqaṭṭaʿ يس, not an oath.
- Q 56 al-Wāqiʿa, Q 81 al-Takwīr — open with *idhā* temporal-conditional, not oath.

The script will re-grep at runtime with `r"^\s*وال"` on each surah's v1 and abort if the returned set ≠ the locked 15.

## Hypothesis (primary test)

**H1**: The 15-surah strict-oath-opener cluster exhibits LOWER mean pairwise Fisher-Rao distance (computed over QAC stem-root distributions per H-NEW-111) than equally-sized random clusters.

**Test statistic**: mean of C(15,2) = 105 pairwise FR distances over the 15-surah cluster, computed from the H-NEW-111 FR matrix.

## Null distributions (two cells, Bonferroni k=2 at α_bon = 0.025)

- **Cell A (uniform null)**: 10,000 random draws of 15 surahs from {1..114}; one-tailed p = P(null intra-mean FR ≤ observed).
- **Cell B (length-matched null)**: 10,000 draws constrained to total cluster verses ∈ [587 × 0.8, 587 × 1.2] = [469.6, 704.4]; same statistic.

Cell B controls for the cluster's total-verse-count signature — short Meccan surahs share other architectural features (high d̄_content per Wave 2026-04-28's compression-tail law), and Cell B isolates the oath-opener-specific signal above the generic short-Meccan-grouping signal.

## MW-5 PC arm — H-NEW-1190 sub-sample {Q 69, Q 97, Q 101}

The instrument-validity positive-control is the H-NEW-1190 sub-sample {Q 69, Q 97, Q 101} — same PC used by H-NEW-1360, H-NEW-1330, H-NEW-1340, H-NEW-1380. Required: p_PC ≤ 0.05 for the primary verdict to count; if p_PC > 0.05 the verdict is reported as NULL-BROKEN (instrument failure on this run, not substantive).

## Direction lock

Direction is LOCKED before computation: **observed intra-cluster FR < null mean (TIGHTER)**. Pre-commit violation = observed intra-cluster FR > null mean (LOOSER); this would be published as NULL-PRECOMMIT-VIOLATION with full prominence per Protocol §1.8.

## Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| Cell A pass (p ≤ 0.025) AND Cell B pass AND PC pass | PASS-DIRECTED |
| Cell A pass AND Cell B fail AND PC pass | DESCRIPTIVE-ONLY (length confound) |
| Cell A fail AND Cell B pass AND PC pass | PARTIAL |
| Both fail AND PC pass | NULL |
| PC fail | NULL-BROKEN (instrument failure) |
| Reversed direction (FR > null) | PRE-COMMIT-VIOLATION → NULL with full prominence |

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel (FR computation inherits H-NEW-111's tuple) |
| Token level | QAC v0.4 stem-root |
| Counting unit | per-surah root-distribution, Fisher-Rao distance from H-NEW-111 |
| Basmala | counted-only-in-Q1 (Q1 not in cluster) |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |
| Aggregation scale | WHOLE-SURAH (this is the deliberate test — thick marker should cohere at this scale) |
| Detection regex | `r"^\s*وال"` on v1 of `quran-text/quran-no-tashkeel.json`; verification: must return exactly the locked 15 |

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: FR matrix H-NEW-111 + 105-pair mean + length-matched perm null specified above. Same instrument as H-NEW-1360, H-NEW-1330, H-NEW-1340.
- **MW-2 (corpus-prior)**: 10,000 perms each cell; minimum standard met.
- **MW-3 (alternative-models)**: Two cells (uniform + length-matched) provide the alternative-null arm.
- **MW-4 (over-fitting)**: No fitted parameter. Cluster size 15 emerges directly from the regex; not tuned.
- **MW-5 (replication)**: PC arm H-NEW-1190 sub-sample {Q 69, Q 97, Q 101}; expects p_PC ≤ 0.05 for instrument validity.
- **MW-6 (instrument-control)**: The discourse-marker NULL family (H-NEW-1330, 1340, 1360) provides the negative control showing the same instrument returns NULL on thinner markers. The contrast is the substantive prediction: thick + chronologically-clustered → PASS; thin/scattered → NULL.
- **MW-7 (post-hoc cap)**: This is a SINGLE-DIRECTION pre-registered test on a CLASSICAL-CATALOGED cluster (al-Suyūṭī *Itqān* nawʿ 67). Not post-hoc.

## Garden-of-forking-paths disclosure

- Cluster locked to **strict-oath formula only** (v1 begins with wāw + definite article). This excludes *lā-uqsimu* surahs (Q 75, Q 90) and muqaṭṭaʿ-then-oath (Q 68). The exclusion is deliberate: the test isolates the THICK surface-orthographic marker, not the general semantic-category of "surahs with oaths in the opening." Alternative wider cluster (17 surahs adding Q 75, Q 90) is queued as H-NEW-1550-sens-wider if the strict cluster PASSES; alternative narrower cluster (cosmic-only, excluding human-action *wa-l-ʿādiyāt* and human-time *wa-l-ʿaṣr*) is queued as H-NEW-1550-sens-cosmic if PASSES.
- Cell B length-window ±20% chosen to match H-NEW-1360 / H-NEW-1330 / H-NEW-1340 family for cross-test comparability. Not tuned.
- Seed 20260509 matches the broader scale-of-aggregation session (H-NEW-1360, H-NEW-1380, H-NEW-1520, H-NEW-1330, H-NEW-1340) for within-session consistency.
- PC sub-sample {Q 69, Q 97, Q 101} is the H-NEW-1190 anchor; not tuned to this test.

## Connection to existing findings

- **al-Suyūṭī, *al-Itqān*, nawʿ 67**: classical-catalog source for the *qasamīyāt* category. This pre-reg promotes the classical category-claim to a falsifiable structural test at whole-surah FR scale.
- **H-NEW-1360 prophet-vocative whole-surah NULL** (FR root-distribution, 6-surah set): differentiating negative control — discourse-marker thinness predicts NULL at whole-surah scale.
- **H-NEW-1330 sajda NULL**, **H-NEW-1340 al-ḥamdu NULL**: parallel discourse-marker NULLs for the same prediction class.
- **H-NEW-1380 Iblīs pericope-cohesion PASS** (z = +4.76): demonstrates scale-of-aggregation principle; this test is at the SURAH scale because the marker (oath-opener formula) IS the whole-opening apparatus.
- **cross-finding-025 marker-thickness threshold** (PRELIMINARY-SYNTHESIS): this pre-reg tests the THICK-marker side of the threshold; PASS would supply the second-strongest supporting finding for the cross-finding-025 thickness axis (alongside H-NEW-1260 *yā-ayyuhā alladhīna āmanū* CONFIRMED at root-cohesion).
- **Wave 2026-04-28 compression-tail laws**: short-Meccan surahs cluster on d̄_content (R²=0.986); Cell B controls explicitly for total-verse-count to isolate the *qasam*-specific signal above the generic short-Meccan signal.

## Anti-flip

The reverse direction (observed intra-cluster FR > null mean) = pre-commit violation → published as NULL with prominence. A clean NULL (observed ≈ null mean) is itself informative — it would mean the *qasamīyāt* cluster's cohesion is fully accounted for by total-verse-count (Cell B) and the *qasam* opener formula adds no FR-detectable surface-root signature beyond chronological short-Meccan stratification.

## Pre-commit attestation

Locked by SHA256. Run script verifies before computation. SHA computed after this file is finalized; embedded in `scripts/h-new-1550.py` as EXPECTED_SHA. Any mismatch = fail-fast.
