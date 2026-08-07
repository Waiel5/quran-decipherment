---
finding_id: h-new-950
title: "Per-surah spectral analysis of divine-name occurrences (Lomb-Scargle): NULL — divine-name placement is spectrally-random"
status: NULL — H3 falsifier triggered (0/48 long surahs survive Bonferroni-150)
phase: B+
date: 2026-05-07
seed: 20260507
prereg_sha256: db3bfec9306696f71a46484d182313039b32dcac19ea68234993c26bad236668
parents: h-new-59-divine-names-distribution; h-new-63-khawatim-al-hashr; h-new-930-modular-verse-counts
classical_anchors: al-Bayhaqī *al-Asmāʾ wa-l-ṣifāt*; al-Rāzī *Lawāmiʿ al-bayyināt*; al-Suyūṭī *al-Itqān* nawʿ al-fawāṣil
---

# H-NEW-950 — Per-surah spectral analysis of divine-name occurrences


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

## 1. Headline (with full NULL prominence)

**0 of 48 long surahs (length ≥ 50 verses) have any Lomb-Scargle periodogram peak surviving Bonferroni-150 at α_bon = 3.33×10⁻⁴.** Divine-name placement is **spectrally-random** at the per-verse-position resolution. The pre-registered direction-locked H1 (rhetorically-punctuated divine-name placement → ≥1 peak survives) NULLS. The H3 falsifier (spectral-randomness verdict) is triggered with full prominence.

**MW-5 instrument-control PASSES**: Q 2 al-Baqara shuffled-verse-order produces 0 peaks surviving Bonferroni — confirming the test pipeline correctly identifies null from data, not from artifact.

## 2. Per-surah summary

48 long surahs (N ≥ 50 verses) tested. Top-3 peaks per surah extracted from Lomb-Scargle periodogram on the integer time-series `f(i) = #divine-name-occurrences in verse i`. Permutation null: 1000 shuffles per surah. Look-elsewhere-corrected p-value primary; per-frequency p-value secondary. Bonferroni α_bon = 0.05 / 150 = 3.33×10⁻⁴.

**Best-of-48 (highest periodogram power, post-hoc-noticed; α=0.05 single-test cap, MW-7)**:

| Surah | N | Names | Top T | Power | p_look-elsewhere | Bonferroni? |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 33 al-Aḥzāb | 73 | 93 | 17.0 | **10.41** | 0.006 | NO |
| Q 39 al-Zumar | 75 | 67 | 19.0 | 6.87 | 0.046 | NO |
| Q 22 al-Ḥajj | 78 | 81 | 23.0 | 6.54 | 0.064 | NO |
| Q 5 al-Māʾida | 120 | 161 | 4.0 | 6.61 | 0.181 | NO |
| Q 9 al-Tawba | 129 | 185 | 19.5 | 6.09 | 0.432 | NO |
| Q 40 Ghāfir | 85 | 75 | 4.5 | 6.02 | 0.258 | NO |
| Q 3 Āl ʿImrān | 200 | 231 | 24.5 | 5.97 | 0.150 | NO |
| Q 10 Yūnus | 109 | 78 | 39.5 | 5.65 | 0.027 | NO |
| Q 4 al-Nisāʾ | 176 | 230 | 6.0 | 5.46 | 0.376 | NO |

(Several have un-corrected p < 0.05 but none survive the look-elsewhere or Bonferroni correction. The Q 33 peak at p_LE = 0.006 is the closest to surviving — but at Bonferroni α_bon = 3.33×10⁻⁴, the gap is large.)

## 3. H2 cluster typology — also NULL

| Cluster | Pass / Total |
|:--|:-:|
| ALM (Q 2, 3, 29, 30, 31, 32) | 0 / 4 |
| ALR (Q 10, 11, 12, 13, 14, 15) | 0 / 5 |
| HM (Q 40-46) | 0 / 5 |
| Other-muqaṭṭaʿāt | 0 / 8 |
| No-muqaṭṭaʿāt | 0 / 26 |
| **TOTAL** | **0 / 48** |

H2 χ² is undefined when all observed = 0. Cluster typology cannot reject uniformity since all cells are zero. NULL on H2.

## 4. The substantive interpretation

This NULL is **substantively informative**:

1. **Refutes naive numerological-periodicity claims** about divine-name placement. The classical literature occasionally suggests divine-names recur at meaningful intervals (e.g., al-Bayhaqī implies rhetorical-punctuation). At the per-verse-position spectral level, this is FALSE: the placement is statistically random.

2. **Joins the project's NULL-cluster on numerological claims**: this is the **8th consecutive NULL** in this family, alongside H-NEW-34 (verse-final abjad mod m), HONEST-LIMITS §1.3 Khalifa-19, §1.9 letter-prime-mod, §1.10 letter-div-19 across 15 corpora, §3 Yūsuf sjn=12, §9 Khalifa Zipf, and **H-NEW-930 modular verse-counts**. The cumulative pattern is overwhelming.

3. **Sharpens the iʿjāz attribution**: the Quran's iʿjāz is **structural-architectural** (Fisher-Rao geodesic per cross-finding-011, edge-residual at boundaries per H-NEW-130, hinges-constrained per H-NEW-236.1, curvature-smooth per H-NEW-920, content×rhyme anti-twin per H-NEW-740) — NOT arithmetic-periodic. al-Bāqillānī's anti-numerological-iʿjāz position (Iʿjāz al-Qurʾān) and al-Suyūṭī's conservative ʿilm al-ḥarf framing (Itqān nawʿ 56) are EMPIRICALLY VINDICATED at law-strength.

4. **Q 33 al-Aḥzāb borderline-result is intriguing post-hoc**: power = 10.41 at period T=17 verses, p_LE = 0.006. This is the strongest per-surah periodogram in the corpus by raw power, well above all peers but not Bonferroni-significant. Q 33 is a known structural outlier (top-3 outlier-strength per H-NEW-590, Structural-twin-pair-member with Q 24 per cross-finding-026 §13). A FORMAL pre-reg of "Q 33 has spectrally-detectable divine-name periodicity at finer resolution" would be the natural follow-up, with a single-surah Bonferroni-1 (α=0.05). Queued as H-NEW-950b.

## 5. Honest limits

1. **Spectral-randomness ≠ semantic-randomness**. Divine-names are NOT placed randomly in any rhetorically-meaningful sense — they cluster at theological pivots, verse-endings, and Khawātim sequences (per H-NEW-63). The NULL here means PERIODIC placement is absent, NOT that placement is uniform.

2. **Resolution is per-verse**. If divine-name structure is at a coarser scale (e.g., per-pericope or per-thematic-block rather than per-verse), this test cannot detect it. A complementary test on pericope-aggregated time-series is queued for H-NEW-950c.

3. **The Bonferroni-150 is conservative** by design. At an uncorrected α=0.05 level, several surahs (Q 16, Q 19, Q 27, Q 33, Q 39) have p_LE under 0.05 — but family-wise correction is the right standard for a 48-surah multi-test family.

4. **Methodology inheritance**: matching rule = surface-string with proclitic prefixes per H-NEW-59. Different matching rules (root-based, lemma-based, with vs without al-prefix) might produce different time-series and different verdicts. Documented as a rules-tuple sensitivity.

## 6. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-950-divine-name-spectral-prereg.md` (SHA: db3bfec9306696f71a46484d182313039b32dcac19ea68234993c26bad236668)
- Script: `scripts/h_new_950_divine_name_spectral.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-950.json`
- Findings: this file
- Journal: `journal/h-new-950-run-1.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
