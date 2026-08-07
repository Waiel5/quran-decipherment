---
id: H-NEW-950
title: Per-surah spectral analysis of divine-name occurrences (Lomb-Scargle periodogram of verse-position time series)
phase: B
status: PRE-REGISTERED
agent: divine-name-spectral-specialist
parent_finding: H-NEW-59 (corpus-wide divine-name distribution); H-NEW-63 (Khawātim al-Ḥashr maximum density)
date: 2026-05-07
seed: 20260507
rules_tuple: (no-tashkeel; surface-string match against asma-al-husna.txt with proclitic prefixes {و,ف,ب,ل,ك,س,فب,وب,فل,ول,وس,فس}; allows ال-prefix variants by definition (names already begin with ال); hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
n_long_surahs_threshold: 50  # length > 50 verses; expected ~48-50 surahs qualify
n_perm: 1000  # permutation null per surah
top_k_peaks: 3
bonferroni_family: "long_surahs × top-3 spectral peaks"
bonferroni_k: 150  # PRE-SPECIFIED 50 long surahs × top-3 peaks. If actual N_long = 48, k=150 is TIGHTER than 144 — self-verifying retention
alpha_bon: 0.000333  # 0.05 / 150
alpha_raw: 0.05
direction: "RHETORICALLY-PUNCTUATED divine-name placement → at least one Lomb-Scargle peak per surah survives Bonferroni-corrected α"
falsifier: "0 of N_long surahs have any peak with permutation-p ≤ α_bon → spectral-randomness verdict (NULL with full prominence)"
matching_rule_locked: |
  surface-string match against the 99-name list at /Users/grey/Downloads/quran/data/asma-al-husna.txt
  using exact-word + proclitic-prefix matching (same logic as H-NEW-59).
  ALLAH (الله) IS INCLUDED as a divine name (consistent with classical taxonomy of asmāʾ Allāh al-ḥusnā;
  also maximally-frequent and hence the dominant signal-source).
  Multi-word names (Mālik al-Mulk, Dhū al-Jalāl wa-l-Ikrām) matched as whitespace-bounded substrings.
  Basmala in Q 1:1 IS counted (it is a verse of Q 1; basmalas before other surahs are NOT counted because they are not numbered verses in Hafs).
classical_claims_audited:
  - claim: "Divine-names recur at meaningful narrative junctures (verse-endings, transition points, theological pivots)"
    source_a: al-Bayhaqī, *al-Asmāʾ wa-l-ṣifāt* (Beirut: Dār al-Kutub al-ʿIlmiyya), bāb on raʾfa, ʿilm
    source_b: al-Rāzī, *Lawāmiʿ al-bayyināt fī sharḥ asmāʾ Allāh wa-l-ṣifāt* (passage on the rhetorical function of divine-name placement)
    audit_status: PENDING-VERIFICATION (cited per H-NEW-950 task spec; verification by physical-edition consultation deferred — flagged SECONDARY-TRIANGULATED since the claim that divine names structurally punctuate verse-endings appears across multiple classical sources including al-Suyūṭī *al-Itqān* nawʿ on fawāṣil)
---

# H-NEW-950 — Pre-registration: per-surah spectral analysis of divine-name occurrences


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

## Hypothesis (DIRECTION-LOCKED, before observation)

**H1.** For each long surah (length > 50 verses), construct the integer time-series `f(i) = (number of divine-name occurrences in verse i)` for `i = 1, ..., N_s`. Run a Lomb-Scargle periodogram over candidate periods `T ∈ [2, N_s/2]`. Identify the top-3 peaks by power. Test the significance of each peak under a permutation null (1000 random shuffles of `f`; recompute periodogram; threshold). Apply Bonferroni correction with `k = 150` (50 long surahs × top-3 cells; α_bon = 3.33×10⁻⁴).

> **DIRECTION**: at least one peak in at least one long surah survives Bonferroni → divine-name placement carries spectrally-detectable periodicity (rhetorical-punctuation hypothesis).

**H2.** The set of long surahs that DO show significant periodicity, if non-empty, is non-uniform across muqaṭṭaʿāt-cluster types (HM-cluster Q40-46, ALR-cluster Q10-15, ALM-cluster Q2-3-29-30-31-32, singletons {Q19, Q20, Q27, Q36, Q38, Q50, Q68}, no-muqaṭṭaʿāt). Test by χ² of "passes" against "expected proportional to long-surah count per cluster".

**H3 (FALSIFIER).** If 0 of the long surahs has any peak surviving Bonferroni (α_bon = 3.33×10⁻⁴), then divine-name placement is spectrally-RANDOM, refuting any naive numerological-periodicity claim and joining the catalog of clean directed-NULLS at full prominence.

## Pre-committed analytic choices (locked before computation)

1. **Long-surah threshold.** `N_s ≥ 50`. (Strict ≥, NOT > — fixed here as inclusive of 50 verses.)
2. **Time series.** `f(i)` = integer count of divine-name occurrences in verse `i` of surah `s` (`i = 1..N_s`).
3. **Matching rule.** Locked above (`matching_rule_locked`).
4. **Periodogram.** `scipy.signal.lombscargle` (normalize=False) on samples at `t_i = i` (integer 1..N_s) with angular-frequency grid `ω = 2π/T` for `T ∈ {2, 2.5, 3, ..., floor(N_s/2)}` (step 0.5; cap candidate-period grid at floor(N_s/2)). Document: because samples are evenly-spaced, Lomb-Scargle is mathematically equivalent to FFT for the comparable frequency-grid; we use Lomb-Scargle for code-explicit safety.
5. **Top-3 peak identification.** After computing the periodogram, locate the three highest-power peaks separated by at least one grid-step (no peak-coalescence).
6. **Permutation null.** For each surah, run 1000 random shuffles of `f` (preserving surah length and total name-count); compute the periodogram each time; record the maximum power across all permutations at each peak's frequency. The empirical p-value for peak `j` is the fraction of permutations whose power at peak-`j`'s frequency `ω_j` is ≥ the observed power.
7. **Bonferroni.** k = 150 (pre-specified at task-spec issuance, retained even if actual N_long = 48 since k=150 is TIGHTER than k=N_long×3 = 144). α_bon = 0.05 / 150 = 3.33×10⁻⁴.
8. **Peak survival test.** A peak passes if its empirical permutation-p ≤ α_bon AND the observed power exceeds the 99.967-percentile of the per-permutation maximum-power distribution (peak-detection-corrected; this guards against the "look-elsewhere" inflation since the peak was identified by maximum power on the observed series). Report BOTH the per-frequency p AND the look-elsewhere-corrected p; primary verdict uses the look-elsewhere-corrected one.
9. **Cluster typology (H2).** χ² test with cluster bins:
    - HM-cluster: Q40, Q41, Q42, Q43, Q44, Q45, Q46 (4 of 7 are long-surahs likely)
    - ALR-cluster: Q10, Q11, Q12, Q13?, Q14, Q15
    - ALM-cluster: Q2, Q3, Q29, Q30, Q31, Q32
    - Other-muqaṭṭaʿāt: Q7, Q19, Q20, Q26, Q27, Q28, Q36, Q38, Q50, Q68
    - No-muqaṭṭaʿāt: all remaining long surahs
   χ² with df = (n_clusters - 1) = 4. α = 0.05 (single-test, follow-up to H1).
10. **MW-5 instrument-control.** Shuffle the verse-order of Q 2 (al-Baqara) once with the seed; recompute the periodogram; confirm no peak survives Bonferroni. This is a positive-control on the NULL side: if a shuffled series produces a "significant" peak, the null is broken.

## Files

- pre-reg: `findings/phase-b-hypotheses/h-new-950-divine-name-spectral-prereg.md` (this file)
- script: `scripts/h_new_950_divine_name_spectral.py`
- raw output: `findings/phase-b-hypotheses/csv/h-new-950.json`
- findings: `findings/phase-b-hypotheses/h-new-950-divine-name-spectral.md`
- journal: `journal/h-new-950-run-1.md`

## Data

- Quran no-tashkeel: `quran-text/quran-no-tashkeel.json` (Hafs-Kufan, basmala counted as verse Q 1:1 only)
- 99 divine names: `data/asma-al-husna.txt` (al-Tirmidhī #3507 list)

## Methodological wall (MW) checks

- **MW-1 (instrument-prior)**: scipy.signal.lombscargle pre-specified; period-grid pre-specified.
- **MW-2 (permutation-null)**: 1000 perms per surah (the spec-mandated minimum for this lane; reduced from project-default 10000 for compute economy on 48 surahs × 1000 = 48000 periodogram evaluations).
- **MW-5 (positive-control / negative-control)**: Q 2 shuffle as MW-5 instrument-control on the NULL side.
- **MW-7 (post-hoc cap)**: This is a fully pre-registered novel test, no post-hoc cap needed.

## Pre-commit attestation

- Direction LOCKED before observing any periodogram output.
- Matching rule LOCKED at pre-reg time.
- Bonferroni k LOCKED at 150 (per task spec; tighter than k=144 for actual N=48; retention is SELF-VERIFYING per Bonferroni asymmetry rule).
- Seed LOCKED at 20260507.
- Equal NULL prominence: H3 falsifier carries full publication weight equal to H1.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
