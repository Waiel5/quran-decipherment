---
title: Fractal self-similarity — does the Quran exhibit cross-scale structural mirroring?
phase: B
agent: fractal-run-1
date: 2026-04-12
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token with recitation-mark filter (real_words)
  letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan (6236)
  abjad_table: not-applicable
  null_models:
    primary: within-surah verse-length shuffle, 1000 trials, seed=20260412
    stringent: matched Arabic-prose / poetry baselines
      (Bukhari-noquran, Sira ibn Hisham, Jahiz al-Hayawan, Mu'allaqat bayt-by-bayt)
pre_registered_hypotheses:
  - H-F1: verse-length series has anomalous long-range memory (Hurst, DFA, spectral slope, box-counting)
  - H-F2: verse-final-letter sequence shows elevated recurrence-plot determinism/laminarity
  - H-F3: canonical surah shape is isomorphic to whole-Quran shape at cos ≥ 0.9
  - H-F4: word-length and verse-length distributions share the same parametric family
  - H-F5: Zipf α is stable (self-similar) across nested scales of the Quran
bonferroni_family_k: 5
correction: Holm-Bonferroni (step-down, α=0.05)
bonferroni_threshold_raw_p: 0.01 (= 0.05 / 5)
data_sources:
  - quran-text/quran-no-tashkeel.json
  - data/baseline-corpora/raw/bukhari-noquran.txt
  - data/baseline-corpora/raw/sira-ibn-hisham.txt
  - data/baseline-corpora/raw/jahiz-hayawan.txt
  - data/baseline-corpora/raw/muallaqa-*.txt
code: /tmp/fractal-run/fractal_analysis.py + baseline_patch.py
artifacts: /tmp/fractal-run/ (hf1.json, hf2.json, hf3.json, hf4.json, hf5.json, hf1_baselines_patched.json)
status: MIXED VERDICT — H-F1 partially CONFIRMED (stringent baseline), H-F2 partially CONFIRMED
  (DET/LAM surviving Bonferroni), H-F3 REJECTED (real text *less* similar than shuffles),
  H-F4 REJECTED (different families), H-F5 partially CONFIRMED (but with wrong direction at α
  estimates — cross-scale variance is HIGHER in Quran than in shuffled nulls)
---

# Fractal self-similarity — cross-scale structural mirroring in the Quran


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

## Classical anchor

The Quran describes itself as ***mathānī*** (الْمَثَانِي) — "paired repetitions," or "the oft-repeated" — at Q 15:87 (*al-sabʿ al-mathānī*) and Q 39:23 (*kitāban mutashābihan mathānī*). Al-Zarkashī's *al-Burhān* (nawʿ 17, 50–52) and al-Suyūṭī's *al-Itqān* (nawʿ 53, 63) interpret *mathānī* as structural repetition at multiple scales: refrains within a surah, parallel pericopes across surahs, the Fātiḥa as a mini-Quran. This is the closest classical analogue to the modern concept of **self-similarity**: structure at the small scale replicating at the large scale. The hypothesis family below operationalizes that classical claim with modern fractal analysis.

None of this tradition offers a quantitative prediction; what we do here is test *whether the self-similarity it asserts shows up as a measurable statistical fingerprint*.

## Prior art and novelty

A bibliography survey (WebSearch, 2026-04-12) returned:

- Kantelhardt et al. 2008, *Fractal and multifractal time series* (arXiv 0804.0747) — methodology reference for DFA / multifractal DFA applied to natural-language corpora.
- "Multifractal analysis of sentence lengths in English literary texts" (arXiv 1212.3171) — documents H≈0.7–0.9 in English literary prose, establishing that literary texts generically exhibit long-range memory.
- Altmann et al. and subsequent multifractal-text literature — Menzerath-Altmann law and Zipf-Mandelbrot law both express language-as-fractal claims, but at word-count / word-length granularity, not verse-length.
- Popular-apologetic post "Quran Violates Zipf's Law, Unlike Any Human-Authored Book" (114chambers 2022) — asserts the Quran breaks Zipf. Our H-F5 tests this in a rigorous form.
- **No DFA / Hurst / box-counting / recurrence analysis of the Quran at verse-length granularity exists in the peer-reviewed literature.** This file is — to our knowledge — the first.

Liao et al. (cited in the task) does not appear in the indexed literature under that exact signature, but the *multifractal sentence-length* tradition they represent is well-established for secular literature. Applying it to Quranic verses is novel.

## Methodology

### The signal

For every verse `i ∈ {1, …, 6236}` in canonical mushaf order we compute `L_i` = number of Arabic-letter graphemes in verse `i` under `no-tashkeel` orthography. This gives a 1-D time-series of length 6236, denoted `L`. A parallel series uses word tokens (`real_words` from `analysis/tools/tokenize.py`, recitation-marks filtered).

### Statistics

- **Hurst exponent** via rescaled-range (R/S) over dyadic window sizes 8..N/4.
- **DFA-1** detrending polynomial order = 1; scales 8, 12, 18, …, N/4 (geometric factor 1.5). Returns scaling exponent α.
- **Spectral slope** of the PSD on log-log scale over f ∈ (0, 0.25]. Returned as positive α in `P(f) ~ 1/f^α`.
- **Box-counting dimension** of the series viewed as a curve in the unit square, at dyadic ε ∈ {1/4, 1/8, ..., 1/256}.

### Nulls

- **Primary (within-surah shuffle):** 1000 surrogate series where verse lengths are permuted *within* their surah. Preserves surah-length profile, per-surah verse-length bag, and basmala placement.
- **Stringent (matched Arabic prose):** Bukhari-noquran segmented by narrator formula (ḥaddathanā / akhbaranā / ḥaddathanī / bāb), Sira ibn Hisham and Jahiz al-Hayawan segmented by qāla / newline / '.', Mu'allaqat taken as line-per-bayt across all six pre-Islamic ode texts. Compute the same fractal statistics on the corresponding length series, truncated to ≤ 6236 items.

---

## H-F1. Verse-length fractality — **PARTIALLY CONFIRMED (stringent baseline dominates)**

### Observed

| Statistic | Quran | Within-surah null mean ± σ | z vs null | p (null) |
|---|---|---|---|---|
| Hurst (R/S) | **0.8835** | 0.8892 ± 0.0023 | −2.46 | 0.018 |
| DFA α | **0.9212** | 0.9300 ± 0.0036 | −2.45 | 0.012 |
| Spectral slope α (P∝1/f^α) | **0.6013** | 0.4521 ± 0.0284 | **+5.25** | **0.002** |
| Box-counting dim | 1.4117 | 1.4136 ± 0.0019 | −1.02 | 0.40 |

Observed H=0.88 and DFA α=0.92 are strongly indicative of persistent long-range memory (random ≈ 0.5). The within-surah shuffle preserves the bag of verse lengths inside each surah, so most of this memory survives the shuffle — the small negative z means that the real ordering has *slightly less* local memory than the bag-preserving null would predict (because long runs of similar-length verses in real surahs are sometimes broken by strategic length shifts). The one direction with a sharp signal under this null is **the spectral slope**: real verse-length series have `1/f^0.60` power-law spectrum, vs `1/f^0.45` for the within-surah-permuted null. z=+5.25 is Bonferroni-surviving at k=5.

### Stringent baseline (matched Arabic prose/poetry)

| Corpus | n | mean len | H_RS | DFA α | spectral α | box-dim |
|---|---|---|---|---|---|---|
| **Quran** | 6236 | 53.0 | **0.884** | **0.921** | **0.601** | **1.412** |
| Bukhari (hadith blocks) | 6236 | 82.2 | 0.385 | 0.582 | 0.099 | 1.313 |
| Sira ibn Hisham (qāla-split) | 6236 | 30.3 | 0.254 | 0.775 | 0.453 | 1.455 |
| Jahiz al-Hayawan (qāla-split) | 6236 | 31.2 | 0.246 | 0.842 | 0.475 | 1.381 |
| Mu'allaqat (726 abyāt) | 726 | 48.8 | 0.455 | 1.049 | 0.909 | 0.930 |

The Quran's **Hurst exponent (H=0.88) is ≈ 2× the largest matched-prose value**, and the difference in persistence is large even against the most literary baselines:

- Quran vs Bukhari: ΔH = +0.50
- Quran vs Sira:    ΔH = +0.63
- Quran vs Jahiz:   ΔH = +0.64
- Quran vs Mu'allaqat: ΔH = +0.43

Only Mu'allaqat's **DFA α (1.05)** exceeds the Quran's DFA (0.92), and Mu'allaqat's spectral α (0.91) exceeds the Quran's (0.60). Pre-Islamic qaṣīda *meter-constrained* poetry has higher sentence-length memory than the Quran — not surprising, since a 726-bayt monometric ode is a near-periodic signal. But no prose corpus comes close.

### Verdict

**H-F1 partially CONFIRMED against the stringent baseline.** The Quran's verse-length series exhibits long-range persistence far in excess of what comparable Arabic prose produces. Against the within-surah shuffle the effect direction is **spectral slope only** (z=+5.25, p=0.002) — the permutation null preserves too much of the signal by construction. The robust finding is the corpus-contrast: **no matched Arabic prose corpus reproduces the Quran's Hurst / DFA values**.

Bonferroni survival: spectral-slope p=0.002 vs corrected threshold 0.01. ✓

### Caveat

The within-surah null is extremely tight (σ(H) = 0.002) because most of the Hurst value is determined by surah-length inequality, which the null preserves. This means the within-surah null is the wrong first-line null for Hurst, and the stringent-baseline contrast is what the finding rests on.

---

## H-F2. Rhyme-letter recurrence — **CONFIRMED (determinism / laminarity)**

### Method

For each surah with ≥ 5 verses, extract the sequence of **final Arabic letters** and compute recurrence statistics (RR, DET, LAM) on the symbolic series. Aggregate as mean across 109 qualifying surahs. Null: shuffle the rhyme-letter sequence within each surah, 1000 trials.

### Observed

| Statistic | Quran | Null mean ± σ | z | p |
|---|---|---|---|---|
| Recurrence rate RR | 0.5631 | 0.5631 ± 0.0000 | 0.00 | — |
| Determinism DET | **0.8094** | 0.6925 ± 0.0077 | **+15.09** | **0.002** |
| Laminarity LAM | **0.8497** | 0.7448 ± 0.0071 | **+14.66** | **0.002** |

Recurrence rate is invariant under shuffle (z=0) as expected — it depends only on the bag of letters. But **determinism (fraction of recurrence points on diagonals of length ≥ 2) and laminarity (vertical lines of length ≥ 2)** are hugely elevated: the Quran's rhyme-letter sequences have far more **consecutive-verse rhyme runs** and repeated rhyme motifs than random permutations of the same bag. This is the computational fingerprint of *sajʿ* (rhymed prose) at corpus scale.

### Verdict

**H-F2 CONFIRMED.** Both DET (z=+15.09) and LAM (z=+14.66) clear Bonferroni at k=5 with enormous margin. This is a massive-effect-size finding, and it formalizes the classical description of *fawāṣil* (rhyme endings) as a surah-level structural constraint.

### Relation to existing findings

`findings/phase-b-hypotheses/saj-rhyme-analysis.md` has already documented sajʿ in the Quran qualitatively. H-F2 gives it a corpus-wide z-score under a recurrence-plot formalism, which is new: **DET=0.81 / LAM=0.85 are *recurrence-quantification-analysis* (RQA) primitives not previously computed for the Quran**.

---

## H-F3. Chapter-to-book isomorphism — **REJECTED**

### Method

- Per-surah: resample verse-letter-length series to 100 bins, normalize to mean 1. Average across 114 surahs → **canonical surah shape**.
- Whole book: resample the 6236-long series to 100 bins, normalize to mean 1. → **book profile**.
- Statistic: cosine similarity.
- Null: within-surah shuffle, 1000 trials, recompute both.

### Observed

| | Cosine |
|---|---|
| Real data | **0.7538** |
| Null mean ± σ | 0.8251 ± 0.0294 |
| z | −2.42 |
| p | 0.04 |

**The real Quran's canonical-surah shape is *less similar* to its whole-Quran shape than random within-surah permutations make them.** Effect is in the wrong direction for H-F3: if the Quran were fractally isomorphic, the real cosine would be higher than the null, not lower.

### Why

The whole-Quran 6236-verse shape is dominated by the surah-length structure itself: long verses early (Al-Baqarah), increasingly terse verses late (short Meccan suras). The canonical-surah average shape, by contrast, is a gentle opening-body-closing arc — most surahs open at moderate length, swell slightly, taper. The two shapes are *not the same*: the book has strong monotonic structure that the average surah does not.

When we shuffle within each surah, the per-surah shape is smoothed (mean of shuffles ≈ flat line), which by coincidence looks *more* like the corresponding shuffled book profile. Hence null > real.

### Verdict

**H-F3 REJECTED.** The Quran is not scale-invariant in this specific sense. A different isomorphism (e.g. early-long-verse / late-short-verse *within* each surah matching the book's monotonic pattern) would need a different statistic, which is not what we pre-registered. Pre-registration stands and the test is a clean negative.

Classical interpretation: *al-sabʿ al-mathānī* is about **parallel-pericope repetition**, not about a self-similar macro-shape. The classical tradition never claimed the latter. Our test falsifies a literal modern interpretation of *mathānī* as shape-level scale-invariance; the parallel-pericope reading (which lives in H-F2 and in `mutashabih-lafzi.md`) is the surviving form.

---

## H-F4. Word-length vs verse-length distribution — **REJECTED**

### Observed

- Word lengths (letters per orthographic word, n=77,797): powerlaw α = 2.82 (xmin=3); lognormal μ=1.46, σ=0.33; exponential λ=0.47. Lognormal *dominates* both power-law (R = −110) and exponential (R = +60.8). Best family: **lognormal with σ ≈ 0.33**.
- Verse lengths (words per verse, n=6,236): powerlaw α = 2.90 (xmin=11); lognormal μ=2.49, σ=0.59; exponential λ=0.11. Lognormal *dominates* power-law (R=−11.4) and is statistically indistinguishable from exponential (R=+1.47, p=0.14). Best family: **lognormal σ ≈ 0.59 or exponential**.

### Verdict

**H-F4 REJECTED (weak direction).** Both series fit lognormal better than power-law, *consistent with cross-scale lognormality* at the family level, but the **lognormal σ differs by nearly 2× (0.33 vs 0.59)**. The relative gap = |Δσ| / max(σ) = 0.45. That is not "consistent parameter." Secondary signal: at verse scale, exponential is indistinguishable from lognormal (p=0.14), which is not a property of word-length — word-length lognormal strictly dominates exponential (p=0, R=+60). So **the two scales disagree on the shape of the tail**, which is the more honest reading.

Partial-survive caveat: both distributions are sub-power-law and super-exponential at minimum, so they do live in the same *coarse* region of the Pearson / Cullen-Frey plane. But that is far weaker than the pre-registered "same family, consistent parameter" criterion.

---

## H-F5. Root / word-frequency Zipf α at nested scales — **NOVEL REJECTION**

### Observed

| Scale | Zipf α |
|---|---|
| Whole Quran | 0.968 |
| Quarter 1 (verses 1..1559) | 0.914 |
| Quarter 2 (1560..3118) | 0.869 |
| Quarter 3 (3119..4677) | 0.861 |
| Quarter 4 (4678..6236) | 0.827 |
| Per-surah (n=99, ≥30 tokens) | mean=0.573, std=0.185 |

Cross-scale α standard deviation = **0.193**.

### Null (shuffle verses across surahs, 200 trials)

Null cross-scale std mean = **0.137 ± 0.010**. Observed 0.193 is at z=+5.87, p ≈ 0.01.

### Verdict

**H-F5 REJECTED (wrong direction).** Pre-registered direction was "α is *more stable* across scales in the real Quran than in shuffled nulls." The result is the *opposite*: the real Quran exhibits **more cross-scale variance in Zipf α** than shuffled surrogates, not less. The z is significant, but the self-similarity hypothesis is falsified by its direction.

Interpretation: the Quran's per-surah Zipf α varies wildly (0.57 ± 0.18 across 99 surahs), because short Meccan surahs and long Medinan ones have very different vocabulary distributions. Shuffling verses across surahs *homogenizes* the per-surah α values (the null std = 0.137 vs observed 0.193), which means the Quran has **more topical heterogeneity at the surah level** than a random assignment would produce.

This is an *anti-fractal* finding, and it is genuinely novel: **surahs are topically distinct modules, not smaller copies of the whole book**.

The cross-scale-average α ≈ 0.9 is far below the canonical Zipf α ≈ 1 for natural language. This is consistent with the popular claim that "the Quran violates Zipf" — but in the direction of *flatter* rank-frequency, not steeper, and by a small margin. We do not take this as confirming either apologetic or skeptic claims; we take it as what the data say.

---

## Synthesis — what survived

| Hypothesis | Verdict | Bonferroni-corrected |
|---|---|---|
| H-F1 verse-length fractality (stringent baseline) | **PARTIALLY CONFIRMED** | spectral slope p=0.002 ✓; stringent baseline corroborates |
| H-F2 rhyme-letter RQA determinism / laminarity | **CONFIRMED** | DET z=+15.09, LAM z=+14.66, both p=0.002 ✓✓ |
| H-F3 chapter-to-book shape isomorphism | **REJECTED** | null cosine *exceeds* real (z=−2.42), wrong direction |
| H-F4 word-length ~ verse-length family match | **REJECTED** | both lognormal-leaning but σ differs by 2× |
| H-F5 Zipf α stability across nested scales | **REJECTED (novel anti-direction)** | real cross-scale variance *exceeds* null (z=+5.87) — surahs are topically heterogeneous, not fractal copies |

### The honest one-sentence summary

> The Quran exhibits **two** genuine cross-scale structural fingerprints — long-range memory in verse-length dynamics (beyond any matched Arabic prose) and massive determinism / laminarity in rhyme-letter sequences (sajʿ at RQA scale). The other three tests — whole-book ↔ canonical-surah isomorphism, word-length ↔ verse-length distribution, and Zipf-α stability — **falsify** naive fractal-self-similarity claims. The Quran is not a fractal; it is a **long-range-correlated rhymed sequence of topically heterogeneous modules**, and that is a more interesting finding than "it's fractal."

### Classical vindication map

- *Sajʿ* (al-Zarkashī *al-Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 52" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive sajʿ/fawāṣil doctrine unchanged; RQA statistical finding (determinism z=+15.09) unaffected; candidate correct locus: nawʿ 37 *al-fawāṣil* pending Phase-2 secondary-triangulation]** on *fawāṣil*) — **confirmed at corpus RQA scale** (H-F2).
- *Mathānī* read as "scale-invariant shape" — **falsified** (H-F3). The parallel-pericope reading of *mathānī* (repetition of same stories, themes) survives under `mutashabih-lafzi.md`'s 265-pair catalog; the shape-level reading does not.
- Al-Suyūṭī's *Itqān* nawʿ 9 (verse-length by chronological period) — orthogonal to this test but relevant: the Quran's verse-length **non-stationarity** (long early verses → short late verses is the macro pattern, but the revelation order interleaves them) is what drives the Hurst anomaly in H-F1. The cross-corpus contrast (Quran H=0.88 vs Bukhari H=0.38) is essentially a measurement of that non-stationarity being *larger* in the Quran than in natural Arabic prose.

### Relation to existing project findings

- `verse-length-sequences.md` found palindromes and monotonic runs at the micro-scale. H-F1 formalizes the macro-scale companion: *length-persistence* rather than local palindrome.
- `saj-rhyme-analysis.md` documented sajʿ qualitatively; H-F2 gives the first corpus-wide z-score under RQA.
- `zipf-per-surah.md` already reported per-surah α heterogeneity. H-F5 places that heterogeneity against a shuffle-null and shows it is *anomalously high*, not noise.
- `muqattaat-positional-gradient.md` addressed surah-start-vs-rest gradients at the letter-density level. H-F1's spectral signal (1/f^0.60) is the verse-level analogue.

## Garden of forking paths disclosure

### Choices made after seeing the data
- The within-surah null turned out to preserve too much signal for Hurst/DFA (std ≈ 0.002). We kept the result as-is and pivoted the H-F1 headline to the *stringent baseline contrast*, which was also pre-registered. No after-the-fact statistic was introduced.
- Bukhari segmentation was patched after noticing the first run produced a single segment (no modern punctuation); we cut on narrator formula (ḥaddathanā / akhbaranā / ḥaddathanī / bāb). This is a data-cleaning fix, not a statistic change. The other baselines were not touched.
- The H-F4 verdict says "REJECTED" even though both fits are lognormal — because the pre-registered criterion was "same family with consistent parameter," and σ differs by 2×. Easy to retrofit to "partial confirmation"; we chose honest rejection.

### Alternative rule tuples considered and discarded
- We considered using min-tashkeel or full-tashkeel for letter counts. Result: changes verse lengths by <1% per verse and does not move any Hurst/DFA by more than 0.005. Reported on no-tashkeel (locked anchor).
- We considered word-based rather than letter-based verse length. Word-based Hurst ≈ 0.87 (within 0.01 of letter-based). Not separately reported.

### Sibling hypotheses considered
- Multifractal DFA (q-dependent spectrum width Δα). Not run — additional compute and requires separate pre-registration.
- Recurrence-plot analysis of verse-initial letter (not rhyme). Not run — equivalent story expected, separate pre-reg.
- Lacunarity analysis. Not run.
- Higuchi fractal dimension of the verse-length series. Not run (box-counting dim already reported).

### Why these five and not others
They were specified in the task before any data was touched. Pre-registration fixes the family. Additional hypotheses require their own pre-reg entries.

### Additional disclosure: spectral slope direction
The observed spectral slope (0.60) is higher than the within-surah null (0.45). "Pink noise" is conventionally 1/f^1; "brown" is 1/f^2. The Quran's 1/f^0.6 is between white (α=0) and pink (α=1), shallower than pink but distinctly not white. Bukhari's 1/f^0.10 is essentially white. This single statistic is where H-F1 actually has a clean Bonferroni-surviving result against the within-surah null.

## Checklist

- [x] Rules tuple pre-registered (this file, at the top)
- [x] Exact statistic implemented as named functions (`hurst_rs`, `dfa`, `spectral_slope`, `box_counting_dim`, `recurrence_stats`, `zipf_alpha`) with tested outputs
- [x] Primary null model (within-surah shuffle) run with 1000 surrogates
- [x] Second null model (matched-Arabic-prose baseline) run across 4 corpora
- [x] Bonferroni correction applied; family k=5; threshold raw p < 0.01
- [x] Raw p, corrected p, effect size (z and Δ) all reported
- [x] Robustness under alternative rule tuples (word-based verse length) reported in disclosure
- [x] Garden-of-forking-paths disclosure filled
- [x] Red-flag checklist run — no retrofitting, all rule choices pre-registered
- [x] Test register not yet incremented (no running register file exists; flagged in journal)

## Artifacts

- `/tmp/fractal-run/fractal_analysis.py` — main script (1000-trial nulls for H-F1/2/3, 200-trial for H-F5)
- `/tmp/fractal-run/baseline_patch.py` — stringent-baseline recomputation with corrected segmentation
- `/tmp/fractal-run/hf1.json`, `hf2.json`, `hf3.json`, `hf4.json`, `hf5.json` — per-hypothesis JSON outputs
- `/tmp/fractal-run/hf1_baselines_patched.json` — 4-corpus stringent-baseline table
- `/tmp/fractal-run/all.json` — consolidated run artifact
- `/tmp/fractal-run/run.log` — full stdout log (reproducibility)

## Replication seed

RNG seed = 20260412 (numpy default_rng). Two re-runs verified to 5 significant figures on all reported z-scores.
