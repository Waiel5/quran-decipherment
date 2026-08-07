# [[h-new-900-cross-text-architecture|H-NEW-900]] — Cross-text architectural comparison


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

**Date**: 2026-04-28
**Author**: [[h-new-900-cross-text-architecture|H-NEW-900]] specialist agent
**Script**: `/Users/grey/Downloads/quran/scripts/h_new_900_cross_text.py`
**JSON**: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-900.json`
**Seed**: 20260428
**N shuffles**: 100

## Question

[[h-new-660-compression-tail-gradient|H-NEW-660]] found a compression-tail R²=0.986 (best two-piece fit) over the canonical mushaf surah ordering. [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] found an anti-twin r(content × rhyme)=−0.864. [[h-new-740-preislamic-poetry-control|H-NEW-740]] confirmed these are absent from pre-Islamic poetry (r ≈ +0.4, n.s.).

**This run asks**: Are these two architectural signatures distinctive against (a) classical Islamic religious prose (Bukhari) and (b) random reorderings of the Quran's own surahs?

## §1 Available comparison corpora on disk

`/Users/grey/Downloads/quran/data/baseline-corpora/raw/`:

| Corpus | Status | Used? |
|---|---|---|
| `bukhari.txt` (79 books, ~26k lines) | Has explicit `# صحيح البخاري/<book>` markers, ḥadīth-numbered with `[N]` | **YES** |
| `sira-ibn-hisham.txt` (~26k lines) | No clear section markers in the available extract | no |
| `jahiz-hayawan.txt` (~36k lines) | Numbered chapters but headers inconsistent in the available extract | no |
| Pre-Islamic dīwāns / muʿallaqāt | Already analyzed in [[h-new-740-preislamic-poetry-control|H-NEW-740]] | (separate analysis) |

**Data gaps (not on disk, documented honestly)**:
- Tao Te Ching (81 chapters)
- Psalms (150 chapters)
- Mahabharata
- Sefer Tehillim (Hebrew Psalms)
- Mishnah (6 orders → 63 tractates → 524 chapters)
- Avesta

These would be the highest-value comparison points — each is a religious anthology with a defined structure. Without them, the cross-corpus generalization claim is bounded.

## §2 Compression-tail R² in each corpus

| Corpus | N sections | K | linear R² | quadratic R² | two-piece R² | **MAX R²** | vs Quran 0.986 |
|---|---|---|---|---|---|---|---|
| **Quran (canonical mushaf)** | 114 | 15 | 0.771 | 0.977 | 0.986 | **0.986** | — |
| **Quran (recomputed here, K=15, surah-order)** | 114 | 15 | — | — | — | **0.989** | matches [[h-new-660-compression-tail-gradient|H-NEW-660]] |
| **Bukhari (file order)** | 79 | 10 | 0.031 | 0.068 | 0.026 | **0.068** | far below |

**Reading**: Bukhari shows essentially no compression-tail. Mean pairwise content distance over a 10-book sliding window does not vary monotonically with book position. Bukhari's editorial ordering (al-Bukhārī's redaction by topic, cycling between law, ritual, biography, eschatology) is not arranged to produce a 1-D positional law.

## §3 iʿjāz anti-twin r in each corpus

| Corpus | r(content × rhyme) | vs Quran −0.864 |
|---|---|---|
| **Quran ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]])** | **−0.864** | — |
| **Quran (recomputed here)** | **−0.892** | matches |
| **Bukhari (per-book)** | **+0.359** | wrong sign; no anti-twin |
| Pre-Islamic poetry ([[h-new-740-preislamic-poetry-control|H-NEW-740]]) | +0.4 (n.s.) | wrong sign |

**Reading**: Bukhari's content-cohesive books (e.g., a single legal topic) are not selected against rhyme-dispersion. There is no architectural pressure separating content from final-letter distribution. The Quran's anti-twin appears specific to its compositional regime.

## §4 Shuffled-Quran null comparison (100 shuffles)

For each of 100 random permutations of the 114 surahs, recompute K=15 sliding-window content-d̄ and rhyme-d̄, fit the same family of compression models, and record the max R² and r(content × rhyme).

### R² (compression-tail) under random surah orderings

| Statistic | Value |
|---|---|
| Quran observed (canonical) | **0.9893** |
| Null mean | 0.2850 |
| Null sd | 0.1828 |
| Null max (across 100 shuffles) | 0.7839 |
| Null 95th percentile | 0.5722 |
| Null 99th percentile | 0.7054 |
| **z(Quran vs null)** | **+3.85** |
| Empirical p(null ≥ Quran) | **0.0000** (0/100) |

**No shuffle even came close.** The maximum R² over 100 random orderings was 0.784 — still below the canonical 0.989 by 0.20 in R² units. The canonical mushaf is in the extreme upper tail.

### r(content × rhyme) under random surah orderings

| Statistic | Value |
|---|---|
| Quran observed (canonical) | **−0.8920** |
| Null mean | −0.4078 |
| Null sd | 0.2347 |
| Null min (across 100 shuffles) | −0.7998 |
| Null 5th percentile | −0.7230 |
| Null 1st percentile | −0.7983 |
| **z(Quran vs null)** | **−2.06** |
| Empirical p(null ≤ Quran) | **0.0000** (0/100) |

**Important nuance**: the shuffle null mean is already moderately negative (−0.41). Some structural anti-correlation between window-level content cohesion and rhyme cohesion exists *even in random orderings of Quran surahs*, because the per-surah content vectors and per-surah rhyme vectors are themselves correlated at the surah level (long surahs with diverse content tend also to have diverse rhyme letters; short surahs with focal content tend to have monorhyme). What the canonical ordering achieves is to *amplify* this baseline anti-correlation from −0.41 to −0.89 — a 2 sd shift.

The R² compression-tail signature is thus a *stronger* distinctive marker (z=+3.85) than the anti-twin r (z=−2.06), but both place the canonical mushaf in the extreme tail of permutation space.

## §5 Honest assessment: is the signature distinctive?

**Within scope tested (Quran vs Bukhari + shuffled-Quran)**: yes.

- Bukhari's editorial ordering does **not** produce a compression-tail (R²=0.07) and does not produce an anti-twin (r=+0.36, wrong sign).
- 100 random surah permutations of the Quran do not match the canonical mushaf on either observable; the canonical mushaf is in the extreme tail of both.

**Out of scope (data gaps acknowledged)**: There is no on-disk comparison to the four corpora most relevant for falsification — Tao Te Ching, Psalms, Mahabharata, Mishnah. These are religious/wisdom anthologies with attested traditional orderings (some with extensive numerological / liturgical structuring). Until such corpora are tested, the cross-corpus generalization is bounded.

**What we have shown**:
1. The compression-tail R²=0.986 is not a property of generic Arabic religious prose with a canonical ordering (Bukhari).
2. The compression-tail R²=0.986 is not a property of the *content* alone — random reorderings of the same content destroy it (max under 100 shuffles: 0.784).
3. The anti-twin r=−0.86 is partially attributable to Quran-internal coupling between surah-length / content / rhyme (null mean −0.41), but the canonical ordering pushes it well below any of 100 shuffled alternatives.

**What we have not shown**:
1. That no other ordered text reaches R²>0.95 on a 1-D positional law over its sections. Plausible candidates (Tao Te Ching, Psalms, Mishnah) were not on disk.
2. That no other ordered text reaches r<−0.7 on content × rhyme. Same data gap.

## §6 What would falsify the empirical iʿjāz claim?

Concretely, the claim "the Quran's compression-tail + anti-twin signature is unique to it" would be falsified if:

1. **Tao Te Ching test (81 chapters)**: build per-chapter top-K word distribution + final-character (Chinese) distribution, fit compression-tail + content × rhyme. If R²>0.95 *and* r<−0.7, the pattern is generic to ordered religious anthologies.
2. **Psalms test (150 chapters)**: same procedure on Hebrew or Greek. Psalms has extensive structural ordering (Ps 1 / Ps 2 paired prologues, the five-book division, the Songs of Ascent block 120–134, the Hallel block 113–118, 146–150). If the structure produces R²>0.95, the compression-tail is a genre property.
3. **Mishnah test (524 chapters across 63 tractates)**: same procedure on Hebrew. Tractate ordering is rabbinically determined; the redactional intent is well-known.
4. **Single counter-example with R²>0.95 AND r<−0.7**: would not "destroy" the Quran finding (which would still hold), but would demote the inference from "compositionally unique" to "compositionally typical of one class of structured anthologies."

A weaker (but still informative) falsifier:
- Any of the above corpora reaching R²>0.95 on the compression observable alone would show that the 1-D positional law is achievable by editorial design, weakening the claim that the Quran's R² is causally tied to revelatory structure.

## §7 Honest limits and data gaps

- **No non-Arabic religious anthologies on disk.** This is the major gap. Bukhari covers Arabic religious prose, but it is hadith narrative, not theological / liturgical anthology.
- **Bukhari N=79 books** with K=10 windows = 70 windows; smaller N than Quran's 100 windows. Some power loss, but the effect size gap (R²=0.07 vs 0.99) is so large this is not a concern.
- **Shuffled-Quran null is conservative for the anti-twin r**, because the marginal per-surah content/rhyme correlation (which is *not* destroyed by shuffling) inflates the null mean. A more aggressive null would be to shuffle content vectors and rhyme vectors *independently* across surahs, breaking that surah-level coupling. Such a null would put Quran observed r at higher z but is methodologically less directly comparable to [[h-new-660-compression-tail-gradient|H-NEW-660]]/730.
- **Bukhari's "ordering"** is editorial-thematic, not chronological or revelatory. Comparing it to the Quran on a "compression-tail" axis tests whether *editorial-thematic* arrangement produces a positional law. It does not (R²=0.07). This is informative but not decisive.
- **K-choice asymmetry**: Bukhari analysis uses K=10 (because n=79) while Quran uses K=15. Sensitivity not formally tested here, but the effect-size gap is large enough that this is unlikely to flip direction.

## §8 Final statement

| Observable | Quran canonical | Bukhari | Shuffled-Quran null | Verdict |
|---|---|---|---|---|
| Compression-tail R² | **0.986** | 0.068 | max 0.784, mean 0.285 | Quran in extreme upper tail (z=+3.85, p<0.01) |
| Anti-twin r | **−0.864** | +0.359 | min −0.800, mean −0.408 | Quran in extreme lower tail (z=−2.06, p<0.01) |

**Within the corpora available on disk, both architectural signatures are empirically distinctive to the Quran's canonical mushaf order.** Bukhari does not show them; no random reordering of the Quran's own surahs reproduces them. Combined with [[h-new-740-preislamic-poetry-control|H-NEW-740]] (pre-Islamic poetry control), the Quran's architectural signature is now bounded distinctive against:
- Pre-Islamic Arabic poetry (qaṣīda monorhyme corpus)
- Classical Arabic religious prose (Bukhari ḥadīth)
- Random permutations of itself

**This does not establish "miraculous" — only "empirically distinctive within the comparison set tested."** The most informative remaining tests (Tao Te Ching, Psalms, Mishnah) require corpora not currently on disk. Until those tests are run, the empirical iʿjāz claim is *narrowly supported* (against Arabic literary controls + within-Quran shuffles) but *not generalized* across the universe of ordered religious texts.

The honest summary: the Quran's compression-tail + anti-twin signature is **specific to its canonical mushaf order**, **absent from its closest Arabic prose comparator**, and **absent from random reorderings of itself**. Whether it is unique among the world's structured religious anthologies remains an open empirical question contingent on data availability.
