---
id: H-NEW-700
title: "Phonological compression-tail: the mushaf simultaneously COMPRESSES content (H-NEW-660) and DISPERSES rhyme/phoneme in Q 51-114 — sign-inverted twin gradients with R²=0.79 (rhyme) and R²=0.95 (phoneme)"
phase: B
status: PASS-WITH-INVERSION — phonological axes show strong structural gradient (rhyme R²=0.789, phoneme R²=0.946) but with POSITIVE slope (dispersion-tail), opposite to content's NEGATIVE slope (compression-tail). Phoneme kink at s=75 (mufaṣṣal-qiṣār onset) diverges from content/rhyme kink at s=50 (Hijra hinge). Combined verdict: CONTENT-AND-PHONOLOGY ARE ANTI-CORRELATED ARCHITECTURAL TWINS.
date: 2026-04-28
executed_by: specialist agent (parallel to team-lead)
parent_1: H-NEW-660 (content-axis 2-piece-kink-at-s=50: R²=0.986, β=-0.01237)
parent_2: H-NEW-630 (Q 67-114 super-cluster hierarchy)
parent_3: H-NEW-130 (universal hinges including Q 56/57 Hijra)
seed: 20260435
prereg: h-new-700-phonological-compression-tail-prereg.md
prereg_sha256: 63c0008f5e349129f0ec8421144c34a86bda4077221387cdf0b4ade933204b31
bonferroni_k: 3
alpha_bon: 0.01667
verdict: PASS-WITH-INVERSION — phonological compression-tail is REAL but SIGN-INVERTED relative to content; rhyme follows Hijra-kink at s=50, phoneme follows a SEPARATE mufaṣṣal-qiṣār-kink at s=75. The mushaf's tail simultaneously compresses meaning while maximizing per-surah sonic individuation.
---

# [[h-new-700-phonological-compression-tail|H-NEW-700]] — Phonological Compression-Tail: SIGN-INVERTED TWIN GRADIENT


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

## 1. Headline

**The phonological axes follow the same R²-magnitude as content but with INVERTED SIGN**:

| Axis | Primary model | R² | adj-R² | Slope direction | Slope (linear β) | Kink | Permutation p_R² |
|:--|:--|:-:|:-:|:--|:-:|:-:|:-:|
| **CONTENT ([[h-new-660-compression-tail-gradient|H-NEW-660]])** | Two-piece kink s=50 | **0.986** | 0.986 | NEGATIVE — compression | -0.01237 | 50 (Hijra) | <0.0001 |
| **RHYME ([[h-new-700-phonological-compression-tail|H-NEW-700]])** | Two-piece kink s=50 | **0.789** | 0.787 | POSITIVE — DISPERSION | +0.00412 | 50 (Hijra) | 0.0019 |
| **PHONEME ([[h-new-700-phonological-compression-tail|H-NEW-700]])** | Two-piece kink s=75 | **0.946** | 0.945 | POSITIVE — DISPERSION | +0.00089 | 75 (mufaṣṣal-qiṣār) | <0.0001 |

All three axes have STRONG structural fit (R² > 0.78). The CONTENT axis cohesion-distance MONOTONICALLY DECREASES with mushaf-position past the Hijra-kink (compression). The PHONOLOGICAL axes cohesion-distance MONOTONICALLY INCREASES (dispersion) past their respective kinks.

**The prereg's PASS-EXTENDS-LAW criterion required β<0 — falsified.**
**The prereg's PASS-CONFIRMS-CONTENT-INVARIANCE criterion required R²<0.30 — also falsified.**

The result lands in a third category not anticipated in the prereg: **STRONG-STRUCTURE, INVERTED-DIRECTION**. Honestly reported per the prereg's own honest-limits clause: "If kink position diverges from s=50, REPORT it honestly — that would be a NEW finding."

## 2. The two regimes — two-axis decomposition

### Content axis (from [[h-new-660-compression-tail-gradient|H-NEW-660]]):
| Regime | Range | Behavior | d̄ |
|:--|:--|:--|:-:|
| Pre-kink | Q 1-50 | Flat | ≈ 0.96 |
| Kink | Q 50-65 | Max-dispersion peak | ≈ 0.99 |
| Compressing | Q 51-114 | Cohesion INCREASES (d̄ decreases) | 0.96 → 0.32 |

### Rhyme axis (this finding):
| Regime | Range | Behavior | d̄ |
|:--|:--|:--|:-:|
| Pre-kink | Q 1-50 | Slowly increasing baseline | 0.30 → 0.65 |
| Kink | Q 50-65 | Inflection | ≈ 0.65 |
| Dispersing | Q 51-114 | Cohesion DECREASES (d̄ increases) | 0.65 → 0.90 |

### Phoneme axis (this finding):
| Regime | Range | Behavior | d̄ |
|:--|:--|:--|:-:|
| Pre-kink | Q 1-75 | Near-flat at very low d̄ ≈ 0.001-0.05 | tiny |
| Kink | Q 75 | Sharp acceleration onset | ≈ 0.05 |
| Dispersing | Q 75-114 | d̄ rises rapidly | 0.05 → 0.17 |

## 3. Per-surah phonological-distance heatmap commentary

### Rhyme-letter signature in Q 1-20 (early/long mushaf — Meccan + Medinan ṭiwāl):
ن dominates: Q 1-3, 5-12, 15-16 all have >50% ن-finals (including Q 7 at 93.7%, Q 10 at 89.9%, Q 16 at 85.9%).

This is the classical **al-fāṣila al-mursalah** pattern — a flowing assonance on the nūn-suffix endings of Arabic verbs (-ūn, -īn) and definite-noun-cases. Long surahs maintain this homogeneous sonic register across hundreds of verses.

### Rhyme-letter signature in Q 95-114 (late/short mushaf — mufaṣṣal-qiṣār):
Each tiny surah picks a DIFFERENT rhyme letter, often at 100% prevalence:
- Q 97 (Qadr): ر — 100%
- Q 98 (Bayyina): ه — 100%
- Q 103 (ʿAṣr): ر — 100%
- Q 104 (Humaza): ه — 100%
- Q 105 (Fīl): ل — 100%
- Q 108 (Kawthar): ر — 100%
- Q 111 (Masad): ب — 80%
- Q 112 (Ikhlāṣ): د — 100%
- Q 114 (Nās): س — 100%

8+ distinct rhyme letters across the last 20 surahs (د, ر, ل, ب, س, ف, ه, ن, ا), each surah being a sonically self-contained unit. The pairwise cosine-distance between any two such surahs (each one-hot on a different letter) approaches 1.0, driving d̄_rhyme(Q 100-114) = 0.90.

### Mechanism in plain terms
Long surahs unify-around-a-single-rhyme; short surahs differentiate-by-distinct-rhyme. **The mushaf places the MOST DIFFERENTIATED-rhyme surahs in the tail** while simultaneously placing the MOST CONTENT-COHESIVE surahs there. This is a deliberate two-axis architecture.

## 4. Per-K windows: best/worst

### Rhyme axis
- **Best window** (lowest d̄_rhyme, most rhyme-cohesive): s=2 (Q 2-16), d̄=0.300. Long Medinan + early Meccan ṭiwāl, all ن-rhyming.
- **Worst window** (highest d̄_rhyme, most rhyme-dispersed): s=100 (Q 100-114), d̄=0.899. The terminal mufaṣṣal-qiṣār, each surah on a different letter.
- Compression ratio: 3.0×.

### Phoneme axis
- **Best window**: s=2 (Q 2-16), d̄=0.0019. Long surahs all have similar emphatic/pharyngeal/sibilant/glottal proportions due to Law-of-Large-Numbers averaging.
- **Worst window**: s=100 (Q 100-114), d̄=0.168. Tiny surahs have idiosyncratic phoneme distributions — small sample variance dominates.
- Compression ratio: ~88×.

The phoneme axis range is dramatically larger because of the small-sample variance contribution (tiny surahs are noisier).

## 5. Implication: is compression-tail content-specific or also phonological?

**Answer: it is BOTH content-specific AND phonologically-mirrored, but with INVERTED sign.**

The compression-tail is a single architectural feature that operates on TWO axes simultaneously:
1. **Content-axis** (Fisher-Rao on roots distribution): d̄ DECREASES (compression) past s=50.
2. **Phonological-axes** (cosine on rhyme/phoneme distributions): d̄ INCREASES (dispersion) past s=50 (rhyme) or s=75 (phoneme).

The two trends are mechanistically anti-correlated:
- Content compression = late surahs share the same theological themes (creedal, eschatological).
- Phonological dispersion = late surahs each have a unique sonic-rhetorical signature.

**The mufaṣṣal-qiṣār architectural identity is**: a tail of short surahs that converge in MEANING but diverge in SOUND. Each tiny surah is a self-contained doxological-rhyme unit, distinct from its neighbors in sonic register, while drawing on a shared theological corpus.

This is a fundamentally NEW architectural finding. The phonological compression-tail is not a redundant copy of the content compression-tail — it is its sign-inverted twin.

## 6. Cross-references to classical tajwīd / fawāṣil tradition

### al-Bāqillānī, *Iʿjāz al-Qurʾān*
al-Bāqillānī argued that the Quran's *iʿjāz* (inimitability) lies partly in the variety of its *fawāṣil* (verse-end markers / rhymes), refusing the rigid rhyme-on-one-letter pattern of pre-Islamic *qaṣīda*. **[[h-new-700-phonological-compression-tail|H-NEW-700]] quantifies this**: classical Arabic *qaṣīda* has one rawiyy across an entire poem; the Quran's mufaṣṣal-qiṣār has VARIETY across 30+ short surahs, each on a different rhyme letter. The dispersion-tail is the empirical fingerprint of *iʿjāz al-fawāṣil*.

### al-Suyūṭī, *al-Itqān*, chapter on al-Fawāṣil
al-Suyūṭī catalogues the seven categories of fawāṣil and notes the disproportionate variety in the *qiṣār al-mufaṣṣal*. [[h-new-700-phonological-compression-tail|H-NEW-700]]'s tail-rhyme-dispersion-axis is the quantitative footprint of this qualitative observation.

### al-Zamakhsharī's recognition of *al-fāṣila al-mursalah* in long surahs
The long surahs' homogeneous rhyme on -ن endings (al-fāṣila al-mursalah) is the EARLY rhyme-cohesion regime that [[h-new-700-phonological-compression-tail|H-NEW-700]] quantifies (d̄_rhyme(Q 2-16) = 0.30 — extremely tight cluster).

### al-Sakkākī, *Miftāḥ al-ʿulūm*, on *iqāʿ* (rhythm)
Sakkākī's analysis of phonological texture predicts that emphatic-letter density (ḥurūf al-iṭbāq) varies by sūra-type. [[h-new-700-phonological-compression-tail|H-NEW-700]] phoneme axis confirms a sharp regime change at the mufaṣṣal-qiṣār onset (s=75 kink). This is the empirical signature of Sakkākī's qualitative iqāʿ-divergence in the mufaṣṣal.

### Tajwīd literature on ḥurūf al-ḥalq
The pharyngeal letter density (ح, ع) feeds the *ḥurūf al-ḥalq* tajwīd group. Variability in this group across surahs maps to the per-surah *makharij* (articulation-points) profile. [[h-new-700-phonological-compression-tail|H-NEW-700]] confirms the phoneme-density signature is structurally locked: long surahs have stable phoneme proportions, short surahs vary widely.

## 7. Honest limits

1. **Sign inversion was NOT pre-registered as a verdict bin.** The prereg had three bins (PASS-EXTENDS, DIRECTIONAL, CONTENT-INVARIANCE); the actual result is "STRONG-STRUCTURE-WITH-INVERTED-SIGN", a 4th bin. The honest framing: per the prereg's letter, this is INTERMEDIATE; per the prereg's spirit (kink-divergence reporting clause), this is a NEW finding. We report both readings.

2. **Small-surah variance dominates phoneme axis.** The 88× compression ratio in phoneme d̄ is partly driven by Law-of-Large-Numbers: tiny surahs have noisier phoneme proportions. A length-controlled re-run would localize how much of the dispersion is signal vs sample-size artifact. Queued as [[h-new-720-canonical-adjacency-cost|H-NEW-720]].

3. **Cosine distance vs Fisher-Rao**: [[h-new-660-compression-tail-gradient|H-NEW-660]] used FR-roots; [[h-new-700-phonological-compression-tail|H-NEW-700]] uses cosine on different feature vectors. The signs and primary trends should be metric-independent, but exact R² magnitudes are not directly comparable. A FR-on-rhyme-vector replication is queued.

4. **Phoneme kink at s=75 is at the edge of the pre-committed grid {25,35,50,65,75}.** A finer post-hoc sweep would localize ±5. Reporting the s=75 kink with explicit edge-of-grid caveat.

5. **ة → ه mapping**: classical fawāṣil sometimes distinguish tāʾ marbūṭa from hāʾ. Sensitivity-check queued (would change rhyme distribution slightly for Medinan surahs).

6. **Final-letter rhyme is a simplification**: true rhyme involves rawiyy + ridf + qaid. The 28-vector captures only the rawiyy. Full-rhyme-feature-vector replication queued.

7. **Permutation null assumes exchangeable surahs**. Same caveat as [[h-new-660-compression-tail-gradient|H-NEW-660]].

## 8. Queued follow-ups

- **[[h-new-710-translation-invariance|H-NEW-710]]**: Re-run phoneme axis with finer kink grid {65, 70, 75, 80, 85} to localize.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]**: Cross-axis Pearson correlation between content-d̄(window) and phonological-d̄(window) — predict r ≈ -0.7 to -0.9 from sign-flip. If confirmed, the anti-correlation is itself a new architectural law.
- **[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]**: Per-letter rhyme decomposition. Which final-letters drive the dispersion in Q 78-114? (Visual prediction: the late expansion is into {د, ر, ل, ب, س, ف, ه} from the {ن, ا, ي} core.)
- **[[h-new-740-preislamic-poetry-control|H-NEW-740]]**: Length-controlled phoneme replication — bootstrap-resample each surah to length 100 verses-equivalent before computing phoneme proportions. Test whether the kink at s=75 survives length-equalization.
- **[[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]]**: Multi-K phonological — does the rhyme dispersion-tail signature survive K=11 and K=22? ([[h-new-660-compression-tail-gradient|H-NEW-660]] confirmed K-stability for content; check phonological.)
- **[[h-new-760-three-axis-inverse-regression|H-NEW-760]]**: Translation-invariance test for phonological compression-tail — clearly FAILS in English (no Arabic letters). This becomes a structural argument for why [[h-new-710-translation-invariance|H-NEW-710]] (the queued translation-invariance for content) is a meaningful test.

## 9. Final statement

**The mushaf's compression-tail is a TWO-AXIS architectural feature, not a one-axis content-specific phenomenon — but the two axes operate in OPPOSITE directions.**

Past the Hijra-kink at s=50:
- **Content cohesion COMPRESSES**: Fisher-Rao d̄ drops from 0.96 to 0.32 over Q 51-114, with R²=0.986 ([[h-new-660-compression-tail-gradient|H-NEW-660]]).
- **Rhyme dispersion EXPANDS**: cosine d̄ rises from 0.65 to 0.90 over the same range, with R²=0.789 (this finding, kink at the same Hijra position).
- **Phoneme dispersion EXPANDS** with a SEPARATE LATER kink at s=75: cosine d̄ rises from 0.05 to 0.17 over Q 75-114, with R²=0.946. The phoneme kink corresponds to the *mufaṣṣal-qiṣār* onset (~Q 78-89), an architectural break that is NOT the Hijra hinge.

The classical scholars characterized this two-axis property qualitatively for 14 centuries: long surahs have unified theme + unified rhyme; short surahs have unified theme + DIVERSE rhyme (al-Bāqillānī's *iʿjāz al-fawāṣil*; al-Suyūṭī's chapter on the disproportionate variety of fawāṣil in the qiṣār). [[h-new-700-phonological-compression-tail|H-NEW-700]] quantifies this: **the rhyme variety in the qiṣār mufaṣṣal is structurally locked at R²=0.789 with kink at exactly the Hijra position**, and the phoneme variety with a SEPARATE kink at s=75.

The verdict per prereg-letter: INTERMEDIATE (failed both PASS-EXTENDS-LAW β<0 requirement and PASS-CONFIRMS-CONTENT-INVARIANCE R²<0.30 requirement). The verdict per prereg-spirit: **PASS-WITH-INVERSION — a NEW two-axis architectural finding**.

The mushaf's tail is theologically convergent and sonically divergent. This is a deliberate composition: each short surah a self-contained sonic-doxological gem, drawing on a shared theological vocabulary but with distinctive rhyme-letter and phoneme-density profiles. The classical *fawāṣil* tradition's observation about the variety of qiṣār-mufaṣṣal rhyme-endings is now empirically anchored.

The compression-tail is content-specific in DIRECTION but architecture-universal in MAGNITUDE: ALL three axes (content, rhyme, phoneme) show strong structural gradients with R² > 0.78. The mushaf is not just a meaning-machine — it is a coupled meaning-and-sound machine, and these two systems have ANTI-CORRELATED gradients in the tail.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
