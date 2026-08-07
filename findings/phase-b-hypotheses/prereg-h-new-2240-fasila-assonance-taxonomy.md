---
id: H-NEW-2240
title: "Verse-final assonance / fāṣila rhyme-class taxonomy — corpus census + within-surah homogeneity test"
phase: B
date_preregistered: 2026-05-29
seed: 20260509
n_perms: 10000
status: PRE-REGISTERED (direction-locked before computation)
author: Waiel Al-Shujaa
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

## 0. Motivation and classical anchor

Classical fāṣila study treats the verse-ending (al-fāṣila) as more than the single
rāwī (rhyme) letter. al-Bāqillānī (*Iʿjāz al-Qurʾān*) discusses the *naẓm* of the
endings; Ibn Abī al-Iṣbaʿ al-Miṣrī (*Badīʿ al-Qurʾān*, *Taḥrīr al-taḥbīr*) and
al-Zarkashī (*al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on al-fawāṣil) classify endings by
the *muqaṭṭaʿ* / pausal rime: the long vowel (madd / ridf) plus the closing consonant
(rāwī), e.g. the dominant *mufaṣṣal* class -ūn/-īn (madd + nūn), the alif-maqṣūra class
-ā, the -īm / -īn class, the open -ār / -ūr class, the tā-marbūṭa -ah class, etc.
al-Suyūṭī (*al-Itqān*, nawʿ 59, *al-fawāṣil wa-l-ru'ūs*) catalogues the *tawāzun* of
endings. The single-rāwī-letter view (already computed in H-NEW-700
`rhyme_letter_diagnostics`) collapses -ūn and -īn (both nūn) into one class even though
they are heard as a unified assonance class precisely because both share the
madd-+-nūn rime; conversely it splits -ā (alif) from -ā (alif maqṣūra / dagger alif)
which are heard identically. The assonance-class view corrects both.

This finding builds a **generator** that classifies all 6236 verse-endings into
assonance classes defined by the **pausal rime** (the final syllable as recited in
waqf: long vowel if present + final consonant), then produces the corpus census and a
pre-registered within-surah homogeneity test.

## 1. Rules-tuple (locked)

- **Primary text**: `quran-text/quran-min-tashkeel.json` (long vowels ا/و/ي/ى and
  dagger-alif ٰ are preserved as graphemes — this is the correct file for rime
  extraction). SHA-recorded at runtime.
- **Secondary text**: `quran-text/quran-full-tashkeel.json` — used ONLY to read the
  final short-vowel / sukūn / tanwīn diagnostic per verse (reported, not used to
  define classes, since fāṣila are heard in pause where final short vowels drop).
- Token level: orthographic (verse-final whitespace-delimited word).
- Counting unit: verse (all 6236; basmala of Q1:1 IS a verse here, consistent with
  the file; basmalas elsewhere are not separate verses in these files).
- Reading tradition: Ḥafṣ ʿan ʿĀṣim, Kūfan verse-count (6236).
- Script: Mashriqī (as stored).
- Pause convention: **waqf / pausal** — the rhyme is computed on the rime as heard at
  a stop, i.e. final short vowels and final tanwīn are dropped to their bare form;
  final tā-marbūṭa is treated as -ah (its own class), final alif/alif-maqṣūra/dagger-
  alif all map to the long-ā rime.

## 2. Class-scheme definition (ALGORITHMIC — pre-registered)

For each verse, take its text, isolate the final orthographic word, and clean it:

**Step A — strip non-rime marks.** Remove every character that is NOT an Arabic base
letter and NOT a long-vowel grapheme: i.e. remove the short-vowel harakāt
(fatḥa ◌َ U+064E, ḍamma ◌ُ U+064F, kasra ◌ِ U+0650), tanwīn
(◌ً U+064B, ◌ٌ U+064C, ◌ٍ U+064D), shadda (◌ّ U+0651), sukūn (◌ْ U+0652), and any
recitation/pause marks (sajda ۩ U+06E9, small high marks U+06E0, U+06DC, U+06DB, etc.),
tatweel (U+0640). **Dagger alif (◌ٰ U+0670) is CONVERTED to a full alif ا** (it marks a
long-ā). Strip the standalone sajda token if it is the final word.

**Step B — extract the pausal rime.** Let `c` = final base consonant grapheme of the
cleaned word; let `p` = the grapheme immediately before `c`.

1. If `c` is a **long-vowel / madd terminator** itself — i.e. `c ∈ {ا, ى, و, ي, ء}`
   with no following consonant — the rime is an OPEN ending:
   - `ا` or `ى` (alif / alif maqṣūra) → class **`-ā`** (open long-ā).
   - `و` → class **`-ū`**; `ي` → class **`-ī`** (open long high vowel).
   - `ء` (final hamza, e.g. شَيء، السَّماء) → if preceded by long vowel ا → class
     **`-āʾ`**; else class **`-ʾ`**.
2. Else `c` is a true consonant (the rāwī). Look at `p`:
   - If `p ∈ {ا, ٰ→ا}` (long ā before the rāwī, the *ridf*): class **`-āC`** where
     `C` is the rāwī letter → e.g. -āb, -ār, -āl, -ān, -āt, -ād, -āq, ...
   - If `p = و` (long ū / ridf): class **`-ūC`** → -ūn, -ūr, -ūd, -ūm, ...
   - If `p = ي` (long ī / ridf): class **`-īC`** → -īn, -īm, -īr, -īl, -īd, ...
   - Else (no long-vowel ridf, i.e. closed short syllable): class **`-aC`** keyed by
     the rāwī letter `C` only → e.g. -C(b), -C(d), -C(r) (the "muqaṭṭaʿ short" rimes,
     e.g. كِتاب-type are -āb so go above; طَه، يس endings, لَهَب، تَبَّ → -ab/-CC).

**Step C — class label.** The class label is the tuple `(ridf-vowel ∈ {ā,ū,ī,∅}, rāwī
letter)` plus the open-ending classes `{-ā,-ū,-ī,-āʾ,-ʾ}` and the tā-marbūṭa class
`-ah` (final ة U+0629, treated as its own class regardless of preceding vowel, since in
pause it is heard as -ah). This is a **fully deterministic function of the cleaned
final word** — no human judgment per verse.

This yields a class alphabet of the form: `-ūn, -īn, -ā, -ah, -īm, -ūr, -ār, -ūd, -ab,
-ūn` … The number of realized classes is an OUTPUT, not pre-set. To keep the
homogeneity test well-powered, the entropy is computed over the FULL realized class
alphabet (no merging); a secondary "coarse" grouping (by ridf-vowel only: {ā-rime,
ū-rime, ī-rime, open-ā, open-other, -ah, short}) is reported for description but the
LOCKED test uses the full alphabet.

## 3. Census deliverables (descriptive, no verdict)

- Corpus class-frequency table (class → count, share), full alphabet.
- Per-surah dominant class and its share.
- Number of surahs that are **mono-class** (dominant class ≥ 80% of verses).
- The coarse ridf-vowel grouping shares.

## 4. PRE-REGISTERED HYPOTHESIS (direction-LOCKED)

**H1 (homogeneity).** Each surah is rhyme-**homogeneous**: the assonance is sustained
within a surah far more than chance. Operationally, the **mean within-surah
assonance-class Shannon entropy** (averaged over the 114 surahs, weighting each surah
equally) is **significantly LOWER** than under a corpus-shuffle baseline that randomly
reassigns the 6236 verse-endings to surahs while **preserving each surah's verse
count**.

- **Direction LOCKED**: observed mean within-surah entropy `< ` null distribution
  (lower = more homogeneous = supports H1).
- **Statistic**: `H_obs = (1/114) Σ_s Entropy_s`, where `Entropy_s` is the Shannon
  entropy (natural log, nats) of the assonance-class distribution of surah `s`'s
  verse-endings.
- **Null**: permutation. Pool all 6236 class labels; shuffle; deal into 114 bins of
  the true sizes; recompute `H_perm`. **seed = 20260509**, **10000 permutations**.
- **p-value** (one-sided, locked direction): `p = (#{H_perm ≤ H_obs} + 1)/(10001)`.
- **Secondary statistic (replication)**: mean within-surah **dominant-class share**
  `D_obs = (1/114) Σ_s max_c (count_{s,c}/n_s)`; locked direction `D_obs > ` null.
  Bonferroni family k=2 → α = 0.025.

**SUCCESS** (PASS / CONFIRMED-DIRECTIONAL): `H_obs` significantly below null at
p < 0.025 AND effect direction as locked (lower entropy), AND secondary share
statistic concordant.

**FAILURE / NULL**: p ≥ 0.025, OR direction reversed. **If the observed mean entropy
is HIGHER than null (surahs LESS homogeneous than chance) → pre-commit VIOLATION,
published as NULL with full prominence.** (This is not expected — fāṣila homogeneity
is near-tautological for a rhymed text — so a non-result would itself be a strong
negative.)

## 5. Secondary descriptive question (NOT a locked hypothesis — exploratory, MW-7 capped)

**Pericope-boundary alignment.** Do assonance-class *changes* (a verse whose class
differs from the previous verse's class, within a surah) cluster at known internal
section boundaries? This is the classical "fawāṣila shift = section break" intuition
(al-Zarkashī). We lack a pre-registered independent pericope segmentation on disk for
all 114 surahs, so this is reported **descriptively only**: per-surah count and rate of
class-switches, the longest mono-class run, and the run-length distribution vs a
within-surah shuffle (does the real sequence have LONGER same-class runs than a shuffle
of the same surah's labels — i.e. is the rhyme "blocky"?). This blockiness test is
MW-7-capped (single-test α = 0.05, exploratory) and does NOT gate the H1 verdict.

## 6. Methodological protections

- **MW-1**: class scheme + entropy statistic fixed here, before computation.
- **MW-2**: permutation null, 10000 perms, seed 20260509.
- **MW-3**: two statistics (entropy + dominant share), Bonferroni k=2.
- **MW-5 (replication)**: re-run at seed 20260510 and seed 99 (report concordance).
- **MW-6 (control)**: the corpus-shuffle IS the matched control (preserves marginal
  class frequencies and surah sizes; destroys only the surah↔class association).
- **MW-7**: pericope/blockiness exploratory, single-α capped.

## 7. Output files

- This pre-reg.
- `findings/phase-b-hypotheses/scripts/h-new-2240.py` (embeds this file's SHA-256;
  verifies at runtime).
- `findings/phase-b-hypotheses/csv/h-new-2240.json` (all numbers).
- `findings/phase-b-hypotheses/h-new-2240-fasila-assonance-taxonomy.md` (findings).

All numbers in the findings come from the JSON, which comes from disk. Equal NULL
prominence guaranteed.
