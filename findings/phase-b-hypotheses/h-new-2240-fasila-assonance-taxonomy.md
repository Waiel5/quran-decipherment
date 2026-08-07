---
id: H-NEW-2240
title: "Verse-final assonance / fāṣila rhyme-class taxonomy — corpus census + within-surah homogeneity"
phase: B
date: 2026-05-29
author: Waiel Al-Shujaa
verdict: PASS (direction-locked) — surahs are strongly rhyme-homogeneous
prereg_sha256: b2b9a8aca1336dde53bad83c323a06d2cc5fedb66894d36467c1c57484790ab2
seed: 20260509
n_perms: 10000
---

# H-NEW-2240 — Verse-final assonance / fāṣila rhyme-class taxonomy


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

**Verdict: PASS (direction-locked).** Each surah is rhyme-**homogeneous**: the mean
within-surah assonance-class Shannon entropy is **1.071 nats**, versus a corpus-shuffle
null mean of **1.830 nats** (null min over 10,000 perms = 1.771; observed sits far
below the entire null support). **p_entropy < 0.0001** (one-sided lower, locked
direction). The secondary statistic — mean within-surah dominant-class share — is
**0.574** observed with **p_share < 0.0001** (locked upper direction). Both pass the
Bonferroni k=2 threshold α = 0.025, and **both replicate at seeds 20260510 and 99**
(p < 0.0001 in every cell). No pre-commit violation. Pre-reg SHA-256
`b2b9a8aca1336dde53bad83c323a06d2cc5fedb66894d36467c1c57484790ab2`, verified at runtime.

All numbers are computed from disk by `scripts/h-new-2240.py` and stored in
`csv/h-new-2240.json`.

---

## 1. The assonance-class generator (algorithmic, pre-registered)

The single-rāwī-letter view (H-NEW-700 `rhyme_letter_diagnostics`) collapses -ūn and
-īn into one "nūn" bucket and splits the alif-maqṣūra -ā from the dagger-alif -ā.
Classical fāṣila study (al-Bāqillānī *Iʿjāz al-Qurʾān*; Ibn Abī al-Iṣbaʿ *Badīʿ
al-Qurʾān*; al-Zarkashī *al-Burhān*, nawʿ al-fawāṣil; al-Suyūṭī *al-Itqān*, nawʿ 59)
hears the ending as the **pausal rime** = madd/ridf long vowel + closing rāwī.

The generator (deterministic, no per-verse judgment), on the verse-final word of
`quran-min-tashkeel.json` (long vowels preserved as graphemes), in **waqf/pausal**
convention:

1. Strip harakāt, tanwīn, shadda, sukūn, and all recitation/pause marks (including the
   sajda sign ۩); convert dagger-alif ◌ٰ → full alif ا.
2. **Open endings** (final grapheme is itself a long vowel): ا/ى → **`-ā`**, و → `-ū`,
   ي → `-ī`, final hamza → `-āʾ`/`-ʾ`.
3. **Tā-marbūṭa** ة → **`-ah`** (its own class — heard -ah in pause).
4. **Closed endings**: keyed by the ridf (the vowel before the rāwī) + rāwī letter:
   long-ā ridf → `-āC` (e.g. -āb, -ār, -ān); long-ū → `-ūC` (-ūn, -ūr); long-ī → `-īC`
   (-īn, -īm, -īr); no long ridf → short `-C` (e.g. -ad, -ab, -ar).

This realises **69 distinct assonance classes** across the 6236 verses. A coarse
seven-way grouping by ridf-vowel ({ī-rime, ū-rime, ā-rime, open-ā, open-other, -ah,
short}) is reported descriptively; the **locked test uses the full 69-class alphabet**.

**Hand-validation** (script reproduces these): Q 18 al-Kahf = 110/110 `-ā`; Q 1 ends
on `-īm`/`-īn` (al-raḥīm, al-ʿālamīn, al-dīn, nastaʿīn, al-mustaqīm, al-ḍāllīn);
Q 55 al-Raḥmān dominated by `-ān` with the *fa-bi-ayyi … tukadhdhibān* refrain;
Q 112 al-Ikhlāṣ = `-ad` (aḥad, al-ṣamad, yūlad); Q 108 al-Kawthar = `-ar`;
Q 114 al-Nās = `-ās`.

---

## 2. Corpus census — assonance-class frequencies

| Rank | Class | Count | Share | Gloss |
|:-:|:--|:-:|:-:|:--|
| 1 | **-ūn** (`-ūن`) | 1755 | 28.1% | madd ū + nūn — the dominant mufaṣṣal masc.-plural / verbal seal |
| 2 | **-īn** (`-īن`) | 1297 | 20.8% | madd ī + nūn — oblique plural / nisba seal |
| 3 | **-ā** (open) | 1216 | 19.5% | open long-ā (alif / alif maqṣūra) — the al-Kahf-type accusative-tanwīn-in-pause |
| 4 | **-īm** (`-īم`) | 551 | 8.8% | madd ī + mīm (raḥīm/ʿalīm/ḥakīm class) |
| 5 | **-īr** (`-īر`) | 178 | 2.9% | madd ī + rāʾ (qadīr/baṣīr class) |
| 6 | **-ah** (ة) | 122 | 2.0% | tā-marbūṭa |
| 7 | **-r** (short -ar) | 120 | 1.9% | short closed -ar (al-kawthar / al-abtar type) |
| 8 | **-īd** | 103 | 1.7% | madd ī + dāl |
| 9 | **-āb** | 102 | 1.6% | madd ā + bāʾ (kitāb/ʿadhāb class) |
| 10 | **-ūr** | 81 | 1.3% | madd ū + rāʾ (ghafūr/nūr class) |
| 11 | **-ār** | 71 | 1.1% | madd ā + rāʾ (al-nār / al-abrār class) |
| 12 | **-ān** | 68 | 1.1% | madd ā + nūn (al-Raḥmān class) |

**The top 3 classes account for 68.4% of all verse-endings; -ūn + -īn alone = 48.9%.**
This is the empirical face of the *mufaṣṣal* cadence the tradition names: the
nūn-sealed madd ending dominates the corpus.

### Coarse ridf-vowel grouping (whole corpus)

| Group | Share |
|:--|:-:|
| **ī-rime** (-īC) | 36.4% |
| **ū-rime** (-ūC) | 31.1% |
| **open-ā** | 19.5% |
| ā-rime (-āC) | 5.7% |
| short (no long ridf) | 5.3% |
| -ah (tā marbūṭa) | 2.0% |

So **~87%** of all endings carry a long high vowel (ī or ū) or an open long-ā — the
corpus is overwhelmingly *madd*-rhymed.

---

## 3. Per-surah dominant class & mono-class surahs

**30 of 114 surahs are mono-class** (one assonance class ≥ 80% of verses). **14 are
perfectly mono-class (100%)**:

| Surah | Class | n | Surah | Class | n |
|:--|:-:|:-:|:--|:-:|:-:|
| Q 18 al-Kahf | -ā | 110/110 | Q 91 al-Shams | -ā | 15/15 |
| Q 48 al-Fatḥ | -ā | 29/29 | Q 92 al-Layl | -ā | 21/21 |
| Q 54 al-Qamar | -r | 55/55 | Q 97 al-Qadr | -r | 5/5 |
| Q 65 al-Ṭalāq | -ā | 12/12 | Q 103 al-ʿAṣr | -r | 3/3 |
| Q 72 al-Jinn | -ā | 28/28 | Q 108 al-Kawthar | -r | 3/3 |
| Q 76 al-Insān | -ā | 31/31 | Q 112 al-Ikhlāṣ | -d | 4/4 |
| Q 87 al-Aʿlā | -ā | 19/19 | Q 114 al-Nās | -ās | 6/6 |

Full mono-class set (≥80%): **Q 4, 17, 18, 19, 20, 25, 33, 47, 48, 53, 54, 55, 63, 65,
71, 72, 73, 76, 78, 87, 91, 92, 97, 98, 103, 105, 108, 111, 112, 114.**

**Coarse-group dominance is near-universal**: every one of the 114 surahs has a
dominant *coarse* ridf-class; the per-surah coarse-dominant distribution is ī-rime 39,
open-ā 25, ū-rime 22, short 16, ā-rime 6, -ah 6. There is no surah whose endings are
ridf-vowel-balanced — homogeneity is even stronger at the coarse level than at the
69-class level.

**Most rhyme-heterogeneous surahs** (lowest dominant share — all long Meccan): Q 14
Ibrāhīm (dom -īd 19.2%, 15 classes, entropy 2.386), Q 34 Sabaʾ (20.4%), Q 22 al-Ḥajj
(21.8%, 14 classes), Q 11 Hūd (22.8%, 18 classes), Q 42 al-Shūrā (24.5%). Even these
are coarsely ī-rime-dominated; their surface heterogeneity is the within-ī-rime
alternation -īm/-īn/-īr/-īd that the single-letter view already showed.

---

## 4. Pre-registered homogeneity test (direction-locked, PASS)

| Statistic | Observed | Null mean | Null support (10k perms) | p (locked) |
|:--|:-:|:-:|:-:|:-:|
| Mean within-surah class **entropy** (nats) | **1.0710** | 1.8299 | [min 1.771, 2.5% 1.802, 97.5% 1.857] | **<0.0001** |
| Mean within-surah **dominant share** | **0.5741** | — | — | **<0.0001** |

- **Direction (locked before computing): observed entropy < null** (lower = more
  homogeneous). Confirmed: the observed mean entropy lies **below the minimum of all
  10,000 permutations** — the surah↔rhyme association is far outside chance.
- Effect size: observed entropy is **0.76 nats below null mean** (≈ the corpus carries
  ~2.1× fewer effective classes per surah than a size-matched shuffle).
- **Bonferroni k=2 → α = 0.025**; both statistics pass.
- **Replication (MW-5)**: re-running the null at seeds 20260510 and 99 gives
  p_entropy = p_share < 0.0001 in every cell. Stable.
- **Control (MW-6)**: the corpus-shuffle null *preserves* the exact marginal class
  frequencies and each surah's verse-count, destroying only the surah↔class binding —
  so the result is not an artifact of the global dominance of -ūn/-īn.

This empirically confirms, at law-strength, that the fāṣila is organised *per surah*:
a surah picks an assonance class (or a tight family) and sustains it. This is the
quantitative form of al-Zarkashī's and al-Suyūṭī's *murāʿāt al-fāṣila* (maintenance of
the ending) — every surah is a near-rhyme-unit.

---

## 5. Exploratory: blockiness / pericope-shift (MW-7-capped, does NOT gate verdict)

Within-surah label-shuffle (2,000 perms, seed 20260509) tests whether the *sequence*
of endings is "blocky" (same-class verses cluster) beyond what the surah's own class
mix forces:

| Statistic | Observed | Null (within-surah shuffle) | p (one-sided) |
|:--|:-:|:-:|:-:|
| Total class-switches (lower = blockier) | **2727** | ≈ 3422.8 | **0.0005** |
| Σ longest mono-class run per surah (higher = blockier) | **1592** | ≈ 1184.0 | **0.0005** |

The real verse-ending sequence has **~20% fewer class-switches and ~34% longer maximal
mono-class runs** than a within-surah shuffle. So assonance is not only chosen
per-surah but **laid down in contiguous blocks** — consistent with the classical
intuition that a *change of fāṣila marks a section (pericope) boundary*. **Caveat
(MW-7):** we have no pre-registered independent pericope segmentation on disk for all
114 surahs, so this is a *necessary* signature (rhyme is blocky) not a *validated*
alignment to externally-defined sections; single-test α = 0.05, exploratory only.

---

## 6. Relation to prior findings

- **H-NEW-700** (`rhyme_letter_diagnostics`, single rāwī letter): this finding is the
  *rime-level* refinement. Concordant on dominance (nūn-class surahs here split into
  the -ūn vs -īn assonance classes; both remain dominant), and it resolves H-NEW-700's
  two known distortions (merging -ūn/-īn; splitting -ā). The d̄_rhyme dispersion-tail
  law (H-NEW-700: d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0,s−50)) operates on the letter
  distribution; the present per-surah entropies (1.071 mean) are its assonance-class
  analogue and are fully consistent (long Meccan surahs = higher entropy).
- **H-NEW-2070** (verse-final divine-name pairing, al-fawāṣil head/seal grammar): the
  ghafūr+raḥīm / ʿazīz+ḥakīm / samīʿ+ʿalīm seals all fall in the -īm/-īr assonance
  classes — the head/seal *naming* grammar and the assonance-*class* grammar are two
  faces of the same fāṣila constraint. H-NEW-2240 supplies the rhyme-class chassis on
  which the name-pairing rides.
- **Classical anchor**: al-Bāqillānī's governed *naẓm* cadence and al-Zarkashī's
  *murāʿāt al-fāṣila* are vindicated as a real, surah-local, statistically extreme
  structure (entropy below the entire 10,000-perm null).

---

## 7. Honest limits

- **Pausal convention is a choice.** Defining the rime in waqf (dropping final short
  vowels) is the standard recitational basis for rhyme, and is pre-registered, but a
  *waṣl* (continuous) definition would reclassify some endings (e.g. -un vs -ūn
  distinctions). The locked test uses pausal; the full-tashkeel final-vowel diagnostic
  is reported in the JSON for transparency.
- **The homogeneity result is near-tautological for a rhymed text** — that is exactly
  why the *direction was locked*: a reversal (surahs *less* homogeneous than chance)
  would have been a major negative. The value of the test is the **effect magnitude**
  (below the entire null support) and the *quantification* per surah, not the mere
  sign.
- **Pericope alignment is exploratory** (no on-disk gold-standard segmentation for all
  114 surahs); only the weaker "rhyme is blocky" claim is supported.
- **Orthographic edge-cases**: the imāla/madd small-high-mark endings (e.g.
  *al-ẓunūnā*, Q 33:10/66/67) are treated as open -ā after mark-stripping, matching the
  Ḥafṣ pausal reading; final standalone hamza is its own minor class. These affect <1%
  of verses and do not move the verdict.

---

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2240-fasila-assonance-taxonomy.md`
  (SHA-256 `b2b9a8aca1336dde53bad83c323a06d2cc5fedb66894d36467c1c57484790ab2`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2240.py` (embeds + verifies SHA)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2240.json`
- Finding: this file.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
