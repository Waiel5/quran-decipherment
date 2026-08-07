---
finding_id: h-new-34a-fasila-mechanism
parent_finding: h-new-34-abjad-residue
phase: B
status: MECHANISM-FALSIFIED — both sub-tests fail; H-NEW-34's proposed fāṣila-pigeonhole explanation is rejected. The reverse-under-dispersion signal is NOT attributable to verse-final rhyme-class pooling. Verse-INITIAL words show the same under-dispersion (z=−9.4 at m=11 vs Bukhari), and within-rhyme-class residues are MORE dispersed than random partitions (not less).
date: 2026-04-12
rules_tuple: (no-tashkeel, orthographic-token, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi abjad, hamza-carrier-policy)
null_model: 1000-permutation bootstrap random-partition (sub-a); 1000-permutation same-length Bukhari/Jahiz baseline (sub-b)
bonferroni_k: 6 (3 moduli × 2 sub-tests)
classical_claim: al-Zarkashī Burhān [nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 52" is out-of-range — 47-nawʿ ceiling; candidate locus nawʿ 37 al-fawāṣil; substantive doctrine unchanged; statistical finding unaffected] + al-Suyūṭī Itqān nawʿ 59 (fawāṣil classified by terminal rawī); pigeonhole mechanism is implicit, not explicit
seed: 20260414
author: abjad-fasila-mechanism agent
---

# H-NEW-34a — Falsification of the fāṣila pigeonhole mechanism for verse-final abjad under-dispersion


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

## Question

H-NEW-34 ([abjad-residue-null.md](abjad-residue-null.md)) found that the Quran's verse-final abjad-sum distribution is MORE uniform modulo 7, 11, and 19 than matched samples from Bukhari-noquran and al-Jāḥiẓ's *Ḥayawān* (z = −4.28 to −11.36). The proposed mechanism was:

> "fāṣila rhyme scheme forces verse-final words onto a small set of high-frequency lexemes; modal values project uniformly across residue bins by pigeonhole."

This hypothesis was flagged but UNTESTED. H-NEW-34a tests it with two independent predictions.

## Pre-registered predictions

**Sub-a (within-class χ² smaller than cross-corpus χ²)**:
If rhyme-class pooling drives the under-dispersion, then *within* each rhyme-class the verse-final abjad-residue χ² should be SMALLER (tighter pigeonhole) than the cross-corpus χ². Operationalized as: weighted-mean within-class χ² < cross-corpus χ², with bootstrap null over 1,000 random partitions of equivalent class-size distribution.

- PASS gate: observed within-class weighted mean χ² below the 99% CI lower bound of the null.
- FAIL gate: observed within-class weighted mean χ² above the 99% CI upper bound of the null.

**Sub-b (verse-initial null)**:
Verse-INITIAL words are NOT under fāṣila constraint. If rhyme is the mechanism, verse-initial residue χ² should match prose baselines (no under-dispersion).

- PASS gate: |z| ≤ 2 vs Bukhari and Jahiz baselines across m ∈ {7, 11, 19}.
- FAIL gate: |z| > 2.58 for any (corpus, m).

**Joint PASS → fāṣila mechanism confirmed.**
**Either FAIL → mechanism falsified.**

## Operationalization

Source: `quran-text/quran-no-tashkeel.json` (primary corpus per methodology §1).

Rhyme-class grouping: for each verse-final cleaned word, take its terminal letter. If the terminal is a long vowel / *mater lectionis* (ا و ي ى), take the penultimate letter (the classical *rawī*). Hamza carriers retain their carrier identity. This follows the al-Zarkashī / al-Suyūṭī convention of grouping by *rawī*.

Abjad: mashriqi + hamza-carrier-policy (identical to H-NEW-34).

Moduli: {7, 11, 19} (identical to H-NEW-34).

Bootstrap: 1,000 random permutations of the 5,617 verse-final abjads in the 7 large rhyme classes, partitioned into groups matching the observed class-size distribution. For each permutation, compute weighted-mean within-group χ². Observed value compared against null 99% CI.

Baseline sampling for sub-b: 1,000 random same-length (N=6,020) samples from Bukhari-noquran (526,250 words) and Jāḥiẓ *Ḥayawān* (340,168 words).

## Rhyme-class distribution

6,219 verses with extractable final words span ~27 terminal-letter classes. Mass is concentrated:

| Rawī | N | % |
|---|---|---|
| ن | 3,160 | 50.8% |
| م | 791 | 12.7% |
| ر | 750 | 12.1% |
| د | 327 | 5.3% |
| ل | 246 | 4.0% |
| ب | 221 | 3.6% |
| ة | 122 | 2.0% |

Seven rhyme classes have ≥100 verses, covering 5,617 / 6,219 = 90.3% of the corpus. Remaining 20 classes each <100 verses. The 5-letter observation from `saj-rhyme-analysis.md` ({ن, ا, م, ر, د} covers 90%) is consistent — note that *-ā* endings (terminal alif rendered here via *rawī* = penultimate consonant) scatter into various classes; ن alone closes 50.1% of verses.

## Sub-a result — within-class weighted-mean χ² is LARGER, not smaller

### Observed vs bootstrap null

| m | Cross-corpus χ² (H-NEW-34) | Within-class weighted mean | Bootstrap null mean | Null 99% CI | z vs null | Verdict |
|---|---|---|---|---|---|---|
| 7 | 42.14 | **48.40** | 17.76 | [10.39, 28.90] | **+9.01** | FAIL (wrong direction) |
| 11 | 75.64 | **152.15** | 31.44 | [21.12, 45.79] | **+26.62** | FAIL (wrong direction) |
| 19 | 312.66 | **304.60** | 113.66 | [91.95, 140.49] | **+20.41** | FAIL (wrong direction) |

The observed weighted within-class χ² is close to the cross-corpus χ² (not below it) and MASSIVELY above a random partition of the same class sizes. Predictive direction is reversed.

### Per-class χ² breakdown (df = m−1)

| Rhyme | N | m=7 χ² | m=11 χ² | m=19 χ² |
|---|---|---|---|---|
| ن | 3160 | 48.50 | 216.66 | 411.52 |
| م | 791 | 86.53 | 83.12 | 296.28 |
| ر | 750 | 40.79 | 74.82 | 121.62 |
| د | 327 | **3.97** | 36.54 | 36.91 |
| ل | 246 | 43.16 | 90.89 | 215.56 |
| ب | 221 | 30.40 | 55.79 | 83.77 |
| ة | 122 | **7.67** | **12.34** | **11.00** |

Small classes (د, ة) are tight (χ² near df, consistent with local clumping around modal abjads). Large classes (ن, م, ل) are VERY dispersed — their abjad-residue distributions are flatter than expected if they were pooled into a single modal-abjad cluster.

### Interpretation

- Random partition of the already-uniform Quran pool produces null χ² much smaller than cross-corpus χ² (because under a uniform pool any same-size random chunk is itself approximately uniform, so within-chunk χ² approaches df = m−1 scaled by sample-size factor).
- Observed within-rhyme-class χ² is FAR ABOVE this baseline: the rhyme classes are NOT drawing from the same uniform parent distribution. They have DIFFERENT residue distributions from each other.
- The cross-corpus low χ² emerges because different rhyme classes cluster at DIFFERENT residue bins and those clusters partially cancel on pooling, producing the appearance of uniformity.
- This is NOT the "small-modal-lexeme pigeonhole" mechanism that H-NEW-34 proposed. It is a mixture-model cancellation effect across non-uniform rhyme classes.

## Sub-b result — verse-initial ALSO under-disperses

Verse-initial (word-position 0) extractable abjads: N = 6,020 (198 verses excluded due to basmala-skip edge cases and empty-first-word).

| Corpus | m | Verse-initial χ² | Null μ | Null σ | z |
|---|---|---|---|---|---|
| Bukhari | 7 | **120.21** | 201.16 | 26.86 | **−3.01** |
| Bukhari | 11 | **160.94** | 665.91 | 53.67 | **−9.41** |
| Bukhari | 19 | 718.09 | 717.71 | 56.66 | +0.01 |
| Jāḥiẓ | 7 | 120.21 | 164.00 | 28.07 | −1.56 |
| Jāḥiẓ | 11 | **160.94** | 358.81 | 44.69 | **−4.43** |
| Jāḥiẓ | 19 | 718.09 | 617.66 | 64.14 | +1.57 |

max|z| = 9.41 >> 2.58 → **FAIL**.

Verse-initial words show SIGNIFICANT under-dispersion at m=7 and m=11 vs Bukhari (and at m=11 vs Jāḥiẓ). Only m=19 is at-baseline. The effect is not exclusive to verse-final position.

The m=19 being at-baseline but m=7 and m=11 being under-dispersed is itself informative: the under-dispersion is not a bug at every scale but something about the abjad mod-7 / mod-11 residue space of Quranic words generally, not specifically the verse-final pool.

## Joint verdict

**MECHANISM FALSIFIED**: both sub-tests fail.

- Sub-a: within-rhyme-class χ² is NOT smaller than cross-corpus χ²; it's either similar (m=19) or much larger (m=7, m=11). The wrong-direction z of +9 to +26 decisively rejects the pigeonhole hypothesis.
- Sub-b: verse-initial words are NOT at baseline; they show under-dispersion too (max|z|=9.4). The under-dispersion is a property of the Quranic word-abjad distribution generally, not of verse-final rhyme pooling specifically.

Bonferroni correction over 6 tests (3 moduli × 2 sub-tests) does not rescue the mechanism; the failures are by many orders of magnitude.

## What's really going on

H-NEW-34's under-dispersion observation is real and independently reproduced here. But its mechanism is NOT rhyme-scheme pigeonhole. Two alternative mechanisms now become salient:

1. **Quranic word-abjad distribution is under-dispersed globally (not verse-final specifically).** The Quran's high-frequency lexical backbone (Allāh=66, al=31+1=very high, pronouns, negations, conjunctions) distributes uniformly across small-modulus residue bins regardless of position. Verse-final is not special; verse-initial inherits the same effect weakly (a weaker variant because verse-initial words are more varied in abjad — many are short particles of low abjad).

2. **Mixture-model cancellation across rhyme classes.** Different rhyme classes occupy different regions of the abjad-residue space (ن-class heavy at certain bins, م-class heavy at others). Pooling them averages out the per-class non-uniformity. This is not "pigeonhole" — it's exactly the opposite: the VARIETY of rhyme classes is what produces cross-corpus uniformity, not the small size of the modal-lexeme pool.

Under hypothesis (2), removing cross-class mixing (as sub-a does) REVEALS the per-class non-uniformity. That matches the observed within-class χ² inflation at m=7 and m=11.

## Robustness / alternative framings considered

- **Rawī definition**: we take penultimate letter when the word ends in a *mater lectionis* (ا و ي ى). An alternative (strict terminal letter) would lump all -ā-ending verses into a single ا class. Qualitatively, the pattern stands — large classes still inflate and small classes still remain tight. Not fully re-run as a sensitivity.
- **Class-size cutoff** at N≥100 is a choice; dropping the two smallest (ة, ب) and re-doing the bootstrap would reduce weighted means slightly but not change the direction (all drivers are the large classes ن, م, ر).
- **Verse-initial extractable count (6,020 vs 6,219)** drops ~200 verses with empty first-token after cleaning; this shouldn't bias the baseline comparison because the Bukhari/Jāḥiẓ null pools were length-matched to N=6,020.
- **Basmala policy**: surah 1 verse 1 is treated as a normal verse. For 113 non-Fātiḥa surahs, the basmala is NOT prepended in the amrayn corpus (`counted-only-in-surah-1` by construction), so verse-initial at surah-opening is the first word of verse 1 proper (often بسم or, in practice, the opening word after the stored basmala). This choice follows H-NEW-34.

## Cross-reference

H-NEW-34's null-confirmed primary result (no ḥisāb-al-jummal signal) is unaffected. What is refuted is H-NEW-34's post-hoc mechanistic explanation for the unexpected reverse-direction under-dispersion. The observation stands; its interpretation must be revised.

## Classical anchor

al-Zarkashī, *al-Burhān*, **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 52" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive classical doctrine (fāṣila catalog by terminal rawī; muṭarraf/mutawāzī/muraṣṣaʿ typology) unchanged; statistical finding unaffected; candidate correct locus: nawʿ 37 *fī maʿrifat al-fawāṣil wa-ruʾūs al-āy* pending Phase-2 secondary-triangulation]** (*fī ma'rifat al-fawāṣil wa ru'ūs al-āy*) catalogues fāṣila by terminal rawī and identifies types (*muṭarraf* = same rawī throughout; *mutawāzī* = same metric + rhyme; *muraṣṣaʿ* = internal + terminal parallelism). Al-Suyūṭī *Itqān* nawʿ 59 extends this. Neither classical source proposes an abjad-level mechanism for verse-final clustering; the pigeonhole idea was a 21st-century inference. That inference now fails its first rigorous test.

## Followup hypotheses prompted by this falsification

- **H-NEW-34b**: test whether under-dispersion is a property of ALL Quranic word-positions (not just final/initial). If yes, the mechanism is lexical (small high-frequency backbone) not rhythmic.
- **H-NEW-34c**: test whether under-dispersion shows up with similar magnitude when the Quran itself is randomly sub-sampled in length-matched chunks — i.e. separate the Quran vs prose distinction from verse-boundary effects.
- **H-NEW-34d**: compute KL divergence of per-rhyme-class residue distributions. Large inter-class divergence would confirm the mixture-cancellation model.
- **Classical baseline extension**: saj'-rich comparators (Psalms-in-Arabic, pre-Islamic rhymed prose kuhhān-style oracles) would test whether rhyme-structured prose shares the effect.

## Honest verdict

**Sub-a: FAIL** (p_left = 1.0000 against bootstrap null; observed z = +9.0 to +26.6 in the wrong direction).
**Sub-b: FAIL** (max|z| = 9.41 > 2.58 critical value).
**Joint: MECHANISM FALSIFIED.**

H-NEW-34's reverse-under-dispersion signal is real but NOT caused by fāṣila rhyme-pooling. The proposed classical-tradition-derived pigeonhole mechanism is rejected at high confidence. A revised mechanism (global Quranic lexical under-dispersion + mixture-cancellation across rhyme classes) is consistent with this result but has not itself been tested.

## Files

- Script: `scripts/h_new_34a_fasila_mechanism.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-34a.json`
- Run log: `journal/abjad-fasila-mechanism-run-1.md`
- Parent finding: `findings/phase-b-hypotheses/abjad-residue-null.md`
- Seed: 20260414
