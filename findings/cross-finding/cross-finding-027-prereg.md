---
id: cross-finding-027-prereg
title: "Pre-registration — iʿjāz al-takrīr (refrain-iʿjāz) as a third architectural axis"
phase: B+
status: PRE-REGISTERED — locked before computation
date: 2026-04-28
parent_synthesis: cross-finding-026-iʿjāz-architecture
proposing_specialist: Q 55 al-Raḥmān specialist (cross-finding-027 proposal in surahs/Q055-al-rahman/06-novel-findings.md §"Synthesis")
seed: 20260428
permutations: 10000
---

# Pre-registration — cross-finding-027: iʿjāz al-takrīr (refrain-iʿjāz)


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
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Background

Cross-finding-026 established a **dual-iʿjāz typology** with two axes locked at law-strength:

1. **al-Bāqillānī *iʿjāz al-fawāṣil*** — quantified by H-NEW-750's `sig_A` (rhyme-entropy + content-distance composite); empirically locked at r=−0.86 anti-twin.
2. **al-Khaṭṭābī *iʿjāz al-maʿnā*** — quantified by hadith-architectural alignment (e.g., Q 112 corpus FR-centroid + *thuluth al-Qurʾān* status); empirically orthogonal to UAS.

The Q 55 al-Raḥmān specialist observed an **anomaly**: Q 55 has CORPUS-MIN `sig_A` (rank 114/114, lowest *iʿjāz al-fawāṣil*) yet wins UAS rank 7/114, AND wins corpus-rank-1 in three separate refrain/dual-pronoun/dual-block metrics:

- 31-fold *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain (rank 1/114; runner-up Q 26 at 8 verse-repetitions)
- *kumā* density 9.09/100w (rank 1/114; 23× runner-up Q 66)
- Cosine-paired dual-paradise blocks (vv. 46-61 vs 62-77, cos=0.918, perm p=0.0033)

Neither al-Bāqillānī nor al-Khaṭṭābī fits Q 55's signature. **The specialist proposes a third axis**: *iʿjāz al-takrīr* (refrain-saturation iʿjāz). Classical antecedents:

- al-Sakkākī, *Miftāḥ al-ʿulūm* — discussion of *takrīr* as a balagha-feature (chapter on *aḥwāl al-musnad ilayhi*).
- al-Zamakhsharī, *al-Kashshāf* on Q 55 — explicitly addresses the function of *takrīr* in al-Raḥmān (commentary on the 31-fold refrain).
- al-Bāqillānī, *Iʿjāz al-Qurʾān* (al-Saqqā ed.) — discusses repetition (*tikrār*) within his iʿjāz framework (separate from *fawāṣil* analysis).

## Hypothesis (DIRECTION-LOCKED)

**H1 (third-axis hypothesis)**: Per-surah refrain-saturation defines an architectural axis that is:
- **(H1a) Orthogonal to `sig_A`** (al-Bāqillānī iʿjāz al-fawāṣil): |Pearson r(refrain-saturation, sig_A)| < 0.30.
- **(H1b) Moderate-positively correlated with UAS**: 0.10 < Pearson r(refrain-saturation, UAS) < 0.60. (A high-saturation surah should be architecturally non-generic.)
- **(H1c) The Q 55 specialist's nominated cluster** {Q 26, 55, 70, 77, 109} contains ≥3 surahs in the corpus top-10 by refrain-saturation.
- **(H1d) Cross-corpus distinct**: Q 55 refrain-saturation > maximum refrain-saturation of any pre-Islamic dīwān/muʿallaqa block of comparable length.

## Null hypotheses (FALSIFIERS)

**H0a (orthogonality fails)**: |Pearson r(refrain-saturation, sig_A)| ≥ 0.50 → refrain-saturation reduces to a re-coding of axis 1; third-axis hypothesis FALSIFIED.

**H0b (UAS correlation absent or strongly anti-correlated)**: Pearson r(refrain-saturation, UAS) ∉ [0.10, 0.60] → refrain-saturation is either trivially aligned with content-density (UAS) or it is anti-architectural; either way, it is NOT a separate axis with the predicted direction.

**H0c (cluster fails)**: Of the nominated {Q 26, 55, 70, 77, 109}, fewer than 3 appear in the top-10 → the proposed cluster is not the actual high-saturation cluster.

**H0d (genre-norm)**: Q 55's refrain-saturation falls within the pre-Islamic poetry baseline distribution → refrain-saturation is a generic Arabic-genre signature, not a Quran-specific authorial feature.

## Refrain-saturation methodology

For each surah S with word-list W_S (length L_S, no-tashkeel, ʾalif-normalized):

1. **N-gram counting**: For N ∈ {3, 4, 5, 6} word-window:
   - Count all consecutive N-grams in W_S.
   - Find max-frequency N-gram and its count c_N.
   - `coverage_N(S) = c_N × N / L_S` (fraction of surah-words covered by this N-gram's occurrences).

2. **Saturation score**: `sat(S) = max over N ∈ {3,4,5,6} of coverage_N(S)`.

3. **Rank corpus-wide** by `sat(S)`.

4. **Top-decile threshold**: surahs at rank ≤ 12 (top decile of 114) are "high refrain-saturation".

5. **Rules-tuple**: `(no-tashkeel, orthographic-token, ʾalif-normalized [ءا→ا, [إأآٱ]→ا, ى→ي], words-as-units, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Cross-validate sat(Q55) against min-tashkeel for sensitivity.

## Statistical tests (Bonferroni-3)

Family of tests: {H1a orthogonality, H1b UAS-correlation, H1d cross-corpus}.
α_corrected = 0.05 / 3 = **0.0167**.

- **Test 1 (orthogonality)**: Pearson r(sat, sig_A) on N=114. Two-sided p. Permutation null with 10000 random label-shuffles of sig_A.
- **Test 2 (UAS correlation)**: Pearson r(sat, UAS) on N=114. One-sided p (direction = positive, locked here). Permutation null with 10000 random label-shuffles of UAS.
- **Test 3 (cross-corpus)**: For each baseline corpus (8 dīwān/muʿallaqa files), split into surah-comparable blocks of 350 words (Q55 word-count proxy), compute saturation, take maximum. Compare to Q55 saturation. Empirical p = (# baseline blocks ≥ Q55 sat) / total blocks.

H1c (cluster) is descriptive — count of nominated cluster in top-10. No formal hypothesis test (it's exploratory ranking).

## Success criteria (decision tree)

- All of {H1a passes, H1b passes, H1d passes} at Bonferroni-corrected α=0.0167 → **CONFIRMED 3rd-axis** verdict.
- 2 of 3 pass → **DIRECTIONAL** verdict.
- ≤1 of 3 passes → **FALSIFIED** verdict; iʿjāz al-takrīr collapses into one of the existing axes or is genre-normal.

H1c (cluster fit) is reported descriptively in all cases.

## Pre-commit violation handling

If sign of r(sat, sig_A) is large-magnitude (>|0.50|), publish as NULL with explicit "third-axis hypothesis falsified" header. Do NOT massage methodology post-hoc.

If r(sat, UAS) is negative or extreme positive (>0.60), publish as DIRECTIONAL with discussion of which existing axis refrain-saturation collapses into.

## Cross-validation

- Compute on no-tashkeel; replicate on min-tashkeel (post-ʾalif-normalization).
- Report sat(Q55) under both. If |Δ| > 20% relative, flag rules-tuple-fragile.

## Anti-hallucination commitments

- Every classical citation includes scholar + work + chapter/section. al-Sakkākī *Miftāḥ al-ʿulūm* (chapter on *al-musnad*); al-Zamakhsharī *al-Kashshāf* (commentary on Q 55:13); al-Bāqillānī *Iʿjāz al-Qurʾān* (al-Saqqā 1954 ed.).
- All numerical claims computed from disk artifacts; no values from memory.
- Equal NULL prominence: any failed sub-hypothesis published with full prominence.

## Files (locked schema)

- Pre-reg: `findings/cross-finding/cross-finding-027-prereg.md` (this file)
- Script: `scripts/cross_finding_027_refrain_saturation.py`
- JSON: `findings/cross-finding/csv/cross-finding-027.json`
- Findings: `findings/cross-finding/cross-finding-027-ijaz-al-takrir.md`

## Seed and reproducibility

`seed = 20260428` for all permutation tests. `n_permutations = 10000`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
