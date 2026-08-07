---
id: H-NEW-750
title: "Pre-reg — Per-surah iʿjāz-signature ranking: from window-level to single-surah"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-730 (window-level r=−0.86 anti-correlation between content-cohesion and rhyme-dispersion). Now decompose to per-surah iʿjāz-signature.
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260445
---

# [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Per-surah iʿjāz-signature: Pre-Registration


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
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

## 1. Hypothesis

[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] locked the iʿjāz architecture at *window-level* (K=15 sliding window, r=−0.8643 anti-correlation between content-cohesion and rhyme-dispersion). Question: does the same anti-twin signature *resolve cleanly to individual surahs*? Can we identify the single surahs that are simultaneously content-central AND rhyme-internally-diverse?

**Hypothesis**: there exist surahs whose iʿjāz-signature (z-score of rhyme-internal-entropy minus z-score of content-distance to other surahs) is high enough to identify them as individual exemplars of the iʿjāz architecture. The *muʿawwidhāt* (Q 113-114), *al-Ikhlāṣ* (Q 112), and other terminal-mufaṣṣal surahs should rank top-of-distribution.

## 2. Two locked measures

### Measure A — global content-distance × rhyme-internal-entropy

For each surah s ∈ {1, ..., 114}:

1. **Content-centrality**: mean_content_distance(s) = mean_{i≠s} D[s][i], where D is the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao distance matrix. LOWER = more content-central / more cohesive.
2. **Rhyme-internal-diversity**: rhyme_entropy(s) = Shannon entropy (in nats) of the surah's verse-final-letter distribution, mapped to the canonical 28-letter Arabic basis using the [[h-new-700-phonological-compression-tail|H-NEW-700]] normalization. HIGHER = more rhyme-diverse (less monorhyme).
3. **iʿjāz_signature_A(s) = z(rhyme_entropy) − z(mean_content_distance)**.
4. Rank all 114 surahs by iʿjāz_signature_A.

### Measure B — local mushaf-neighborhood content-cohesion × rhyme-internal-entropy

For each surah s ∈ {1, ..., 114}:

1. **Local-content-cohesion**: 1 / mean_{i ∈ {s−2, s−1, s+1, s+2} ∩ [1,114]} D[s][i]. HIGHER = more locally-cohesive in mushaf-neighborhood (smaller distance to ±2 neighbors).
2. **Rhyme-internal-diversity**: same Shannon entropy as Measure A.
3. **iʿjāz_signature_B(s) = z(rhyme_entropy) + z(local_cohesion)**.
4. Rank all 114 surahs by iʿjāz_signature_B.

## 3. Pre-committed predictions

The classical tradition (al-Bāqillānī, al-Suyūṭī) singles out specific terminal-mufaṣṣal surahs as iʿjāz exemplars. Predictions BEFORE running:

| Surah | Prediction A | Prediction B | Classical anchor |
|:--|:--|:--|:--|
| **Q 112 al-Ikhlāṣ** | top-5 (either measure) | top-5 (either measure) | al-Bāqillānī: 4-verse creedal core; "thuluth al-Qurʾān" hadith |
| **Q 113 al-Falaq** | top-15 | top-15 | muʿawwidhāt-pair; al-Suyūṭī |
| **Q 114 al-Nās** | top-15 | top-15 | muʿawwidhāt-pair; al-Suyūṭī |
| **Q 1 al-Fātiḥa** | high (top-30) | high (top-30) | umm al-Kitāb; al-Rāzī mafātīḥ al-ghayb |
| **Q 2 al-Baqara** | bottom-15 | bottom-15 | longest, mixed registers, rhyme-uniform |
| **Q 33 al-Aḥzāb** | bottom-30 | bottom-30 | Medinan-legal mixed |

A prediction "hits" if the surah falls in the predicted bin under EITHER measure (logical OR), which we will report transparently along with the per-measure result.

## 4. Pre-committed thresholds

The two measures are not independent (they share the rhyme_entropy term and an inverse-related content axis). For the OVERALL claim that the iʿjāz-signature concept generalizes from window-level to per-surah:

- **STRICT PASS**: ≥ 4 of 6 pre-committed predictions hit AND Spearman ρ between Measure A and Measure B ranks ≥ +0.5.
- **DIRECTIONAL**: ≥ 3 of 6 hit AND Spearman ρ ≥ +0.3.
- **WEAK / NULL**: ≤ 2 of 6 predictions hit OR Spearman ρ < +0.3.

## 5. Bonferroni structure

Two measures (A, B) → Bonferroni-2 → α_corrected = 0.025 for any per-measure significance test invoked downstream (e.g., resampling-based confidence intervals on rank stability).

## 6. What would FALSIFY

- al-Ikhlāṣ Q 112 NOT in top-5 by EITHER measure: undermines the prediction that the 4-verse creedal core is the per-surah iʿjāz exemplar.
- al-Baqara Q 2 NOT in bottom-15 by EITHER measure: undermines the head-ṭiwāl ↔ anti-iʿjāz pole correspondence.
- Spearman ρ(rank_A, rank_B) < +0.3: measures disagree → per-surah signature is metric-fragile and the window-level finding does not cleanly resolve.

## 7. Methodology rules

- MW-1: instrument-prior — both axes use existing project methodology ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] D matrix; [[h-new-700-phonological-compression-tail|H-NEW-700]] final-letter normalization).
- MW-3: alternative-models — Measure B (local mushaf-neighborhood cohesion) is the alternative to Measure A (global content-distance).
- MW-7: not applicable.
- PRE-REG-STANDARD-04: hypothesis, null, direction, success criteria locked BEFORE run.
- ONE-text discipline: NULL must be reported with equal prominence as PASS. Pre-commit FAILURES are INFORMATIVE.

## 8. Honest expected limits

- Per-surah Shannon entropy is noisy at small N=verse-count. Q 108 al-Kawthar has only 3 verses → entropy bounded by ln(3) ≈ 1.099 nats. We will report n_verses alongside entropy.
- Single-surah content-distance to others is sensitive to root-token-count; small surahs may have inflated distance simply due to limited vocabulary.
- The 28-letter basis underestimates true rhyme structure (it ignores consonant clusters, vowels, and stress).

## 9. Files

- Script: `scripts/h_new_750_per_surah_iʿjāz.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-750.json`
- Findings: `findings/phase-b-hypotheses/h-new-750-per-surah-iʿjāz-signature.md`
- Journal: `journal/h-new-750-run-1.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
