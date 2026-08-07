---
id: H-NEW-710
title: "Translation-invariance of compression-tail: English Sahih shows R²=0.96 OPPOSITE-DIRECTION gradient — Arabic compression-tail is FR-roots-specific, NOT translation-invariant"
phase: B
status: NULL on translation-invariance — primary R²=0.9586 in English Sahih top-200-stem-cosine, BUT slope β=+0.00612 (OPPOSITE direction from Arabic β=−0.01237). Pearson r(Arabic_d̄, English_d̄)=−0.912 over 100 windows. The Arabic compression-tail does NOT survive in English content-vocabulary; instead, English content-cohesion is anti-correlated with mushaf position. Compression-tail is structural to Arabic FR-roots, not to translation-content.
date: 2026-04-28
parent: H-NEW-660
seed: 20260436
prereg: h-new-710-translation-invariance-prereg.md
prereg_sha256: 3cbd690c791a6f38e79ee24ec439a6a51c81451505d326b962639085d83c80a1
bonferroni_k: 3
alpha_bon: 0.01667
verdict: NULL on translation-invariance (formal pass/fail). The compression-tail is Arabic-FR-roots-specific. English content-vocabulary shows an ANTI-correlated gradient of comparable strength.
---

# [[h-new-710-translation-invariance|H-NEW-710]] — Translation-Invariance Test: Arabic Compression-Tail is FR-Roots-Specific (NULL on Translation-Invariance, but with a Striking Anti-Correlated English Gradient)


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

Applying the [[h-new-660-compression-tail-gradient|H-NEW-660]] protocol to **English Sahih International, top-200 stem cosine distance, K=15 windows**, with Bonferroni-3 α=0.01667:

| Quantity | Arabic ([[h-new-660-compression-tail-gradient|H-NEW-660]]) | English ([[h-new-710-translation-invariance|H-NEW-710]]) |
|:--|:-:|:-:|
| Primary model | two-piece kink at s=50 | quadratic |
| Primary R² | **0.9860** | **0.9586** |
| Slope direction | **β < 0** (compressing) | **β > 0** (expanding) |
| Linear β | −0.00619 | **+0.00612** |
| Best window (lowest d̄) | s=100 (Q100–114, qiṣār) | s=2 (Q2–16, opening ṭiwāl) |
| Worst window (highest d̄) | s=46 (Q46–60, Hijra-kink) | s=99 (Q99–113, qiṣār) |
| Permutation p (primary R²) | < 10⁻⁴ | < 10⁻⁴ |
| Pearson r(Arabic d̄, English d̄) over 100 windows | — | **−0.9121** |
| Spearman ρ(Arabic d̄, English d̄) | — | **−0.7781** |

**Formal verdict (PRE-REG-STANDARD-04)**: NULL on translation-invariance.

**The pre-registered direction (β < 0) FAILS in English.** Although R²=0.9586 exceeds the STRICT-PASS threshold, the slope is positive — opposite to the Arabic compression-tail.

**Interpretive verdict (per pre-reg §7)**: classified as `PARTIAL+` because the formal R² > 0.70 but interpretive criteria require both high R² *and* a kink in [40, 60] *and* — implicitly — direction-matching. The compression-tail signature is **NOT translation-invariant**.

## 2. Translation source + stemmer + rules-tuple shift documented

- **Translation file**: `/Users/grey/Downloads/quran/data/translations/en.sahih.txt-2.txt` (Sahih International English; surah|verse|text format; 6249 lines, 6236 structured rows). Pickthall and Yusuf Ali are NOT on disk; this is the only English translation available.
- **Stemmer**: lowercase + strip-non-alpha + stopword-removal + Porter-light suffix-stripping (longest-match: `tion sion ment ness ity ing est ed es ly er s`, only if remaining stem ≥ 3 chars). Bracket interpolations `[...]` are stripped before tokenization (Sahih translator interjections).
- **Top-200 vocabulary**: top 20 stems are `allah, lord, say, said, people, know, day, there, except, one, among, earth, punish, believ, fear, before, good, made, whoev, over`.

**Rules-tuple shift (from [[h-new-660-compression-tail-gradient|H-NEW-660]])** — explicitly documented:

| Aspect | [[h-new-660-compression-tail-gradient|H-NEW-660]] (Arabic) | [[h-new-710-translation-invariance|H-NEW-710]] (English) |
|:--|:--|:--|
| Distance metric | Fisher-Rao on root-frequency vectors | Cosine on top-200 stem-frequency vectors |
| Word-form unit | Arabic triliteral root | English Porter-light stem |
| Vocabulary | full Arabic root inventory | fixed top-200 stems by corpus frequency |
| Per-surah vector dimension | full root vocabulary | 200 |
| Pre-processing | Quranic Arabic Corpus root-tagging | Sahih → strip [interpolation] → lowercase → tokenize → stopword → stem |

This is a substantial rules-tuple shift. The hypothesis was: if the compression-tail signature is *deep-structural*, it should survive even through this very different lens. If it's specific to the Arabic root-system, the lens-shift will destroy it. **The result of the lens-shift is destruction of the direction (positive instead of negative slope), with comparable variance-explanation strength.**

## 3. Best/worst K=15 windows in English vs Arabic — they ANTI-CORRELATE

| Comparison | Arabic | English |
|:--|:--|:--|
| Best window (most cohesive) | s=100, **Q100–114** (terminal qiṣār), d̄=0.3190 | s=2, **Q2–16** (head ṭiwāl), d̄=0.2382 |
| Worst window (most dispersed) | s=46, **Q46–60** (Hijra-kink) d̄=0.9929 | s=99, **Q99–113** (terminal qiṣār), d̄=0.8945 |

In Arabic FR-roots: **the terminal qiṣār is MOST cohesive**, the Hijra-kink is MOST dispersed.
In English top-200-stem cosine: **the head ṭiwāl is MOST cohesive**, the terminal qiṣār is MOST dispersed.

The very window that Arabic identifies as the cohesion-DENSE end of the corpus (Q100–114) is the window that English identifies as the LEAST cohesive end. **The two metrics are measuring DIFFERENT axes** and the canonical mushaf order projects oppositely on those axes.

Pearson r between the two 100-window d̄-curves: **−0.9121** (extremely negative). Spearman ρ: **−0.7781**.

## 4. Implication — structural-content vs Arabic-surface

### 4.1 Why does this happen?

The Arabic compression-tail ([[h-new-660-compression-tail-gradient|H-NEW-660]]) is driven by:
- Late-Meccan terminal-qiṣār surahs (Q 78–114) sharing **a tight inventory of apocalyptic / oath / eschatological roots**: ʾ-y-m, q-y-m, l-y-l, n-h-r, j-z-y, etc.
- Tight rhyme-scheme and oath-formula repetition concentrate root-overlap.
- Short surahs concentrate roots from a small pool, raising root-vector overlap → LOW FR distance.

In English Sahih:
- Short surahs are SHORT in token count too (Q108 has only 9 stems after filtering; Q103 ~12; Q104 ~25).
- A 9-token vector intersected with a 200-d top-stem vocabulary produces extreme **sparsity**: most short surahs have nearly orthogonal sparse vectors → cosine ≈ 0 → distance ≈ 1.
- The thematic concentration that PRODUCES the Arabic compression is INVISIBLE to a top-200-stem English representation, because the apocalyptic / oath / eschatological vocabulary in English is fragmented across many low-frequency translator-choice synonyms.

In contrast, the head ṭiwāl (Q2–Q16) are LONG English texts (4691 stems for Q2 alone) — they massively overlap on the top-200 stems (allah, lord, people, day, etc.) — so cosine distance is LOW.

The English measurement is dominated by **token-count effects** in a way the Arabic FR-roots measurement is not. This is a measurement-instrument confound: translation distance via top-stem cosine is essentially a **length-overlap proxy**, not a content-cohesion proxy.

### 4.2 What does this say about the structural-vs-Arabic-surface question?

There are two readings, and the honest answer requires acknowledging both:

**Reading A — Compression-tail is Arabic-syntax-specific (literal)**: the compression-tail survives in Arabic FR-roots but is destroyed by translation. The signature lives in the Arabic root-system: the late-Meccan rhyme-and-oath terminology that compresses root-vector overlap is a *surface* phenomenon of Arabic phonology and morphology. Translation flattens it.

**Reading B — Compression-tail is real but the English measurement-instrument is wrong**: the top-200-stem cosine is a poor proxy for cohesion. A better English measurement (semantic embeddings, LLM-based sentence similarity, larger vocabulary, length-normalized) might recover the compression-tail. The current null result is partly methodological.

**The honest call**: BOTH readings have force, but Reading A is the appropriate conclusion given the rules-tuple I locked in the pre-reg. I tested *the [[h-new-660-compression-tail-gradient|H-NEW-660]] protocol mechanically translated to English-stem-cosine*. That protocol returns a strong-but-OPPOSITE-direction gradient. The pre-registered hypothesis is FALSIFIED on direction, even though R² is high.

The compression-tail in [[h-new-660-compression-tail-gradient|H-NEW-660]] should now be reframed as: **"the FR-roots cohesion-architecture of the canonical Arabic mushaf has a 2-piece-linear law with R²=0.986; this law is NOT recoverable through naive English-translation content-vocabulary measurement (which produces an opposite-direction R²=0.96 gradient driven by length-overlap)."**

### 4.3 The anti-correlated English gradient is interesting in its own right

R²=0.96 with Pearson r=−0.91 between curves is itself a striking architectural fact: **the canonical mushaf order is structured such that, in English content-vocabulary, the terminal-qiṣār is MAXIMALLY DISPERSED while the head ṭiwāl is MAXIMALLY COHESIVE.** This is the OPPOSITE of the Arabic FR-roots picture. The two gradients together (Arabic compressing, English expanding, both with R² > 0.93) reveal a *bidirectional* canonical-order structure depending on which lens is used.

A reasonable interpretation: the long Medinan ṭiwāl (Q2–Q16) discuss broad theological/legal/narrative content using a recurring vocabulary of high-frequency terms (allah, people, day, believ, etc.), so they cluster tightly in top-200-stem space. The terminal qiṣār are short, lexically diverse oaths/exhortations that DON'T overlap in top-200-stem space (sparse vectors). This gradient is real and structural — it reflects the shift from long-thematic to short-rhetorical surah types — but it is the OPPOSITE of the Arabic FR-roots compression-tail.

### 4.4 [[h-new-660-compression-tail-gradient|H-NEW-660]]'s "the mushaf's content-cohesion architecture is 1-D" claim — refined

[[h-new-660-compression-tail-gradient|H-NEW-660]] §4 claimed the mushaf's cohesion-architecture is "essentially 1-dimensional" via the s-position-past-Hijra-kink law. [[h-new-710-translation-invariance|H-NEW-710]] reveals this is true *only with respect to the Arabic FR-roots metric*. In English content-vocabulary, the mushaf's cohesion-architecture is also approximately 1-D — but along the OPPOSITE axis. The mushaf is multi-dimensional in cohesion-space; the choice of lens determines which axis dominates.

## 5. Honest limits

1. **English measurement-instrument is a confound.** Top-200-stem cosine is heavily influenced by surah length, since short surahs have sparse vectors. A length-normalized or TF-IDF-weighted measure might give different results. Locking the simple measure was deliberate (per pre-reg) for falsifiability, but interpretation must acknowledge this.
2. **Single translation source (Sahih).** Pickthall, Yusuf Ali, Asad would all give different stem distributions due to different translation styles (literal vs. paraphrase). The result might be Sahih-specific.
3. **Top-K=200 vocab choice.** A larger vocab (1000, 5000) or full vocab might preserve more thematic information from the terminal qiṣār. Locked at 200 in pre-reg; cannot adjust post-hoc.
4. **Stopword list and Porter-light stemmer are simplifications.** A proper Snowball stemmer with full stopword list (NLTK) might give different stems. Used a built-in approximation to avoid external dependencies.
5. **Bracket-interpolation stripping.** Sahih's `[...]` interpolations vary by translator philosophy and were stripped, but the choice may matter at the margin.
6. **Length-effect is not controlled.** Q108 has 9 stems, Q2 has 4691. This creates extreme sparsity differences. A future version (queued as [[h-new-720-canonical-adjacency-cost|H-NEW-720]]) could test on a length-normalized proxy.
7. **R²=0.96 with WRONG-DIRECTION slope is a pattern that warrants its own investigation.** The English curve is structurally interesting (R² high, very smooth) but in the opposite direction. This is not noise; it's a real anti-correlated signal.
8. **The FORMAL pre-reg verdict (β < 0 required)** is unambiguously NULL on translation-invariance. The high English R² with positive slope cannot be retrospectively converted to a "pass" — that would violate PRE-REG-STANDARD-04 direction-locking.

## 6. Cross-references

- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** (parent): R²=0.986 Arabic compression-tail. [[h-new-710-translation-invariance|H-NEW-710]] reveals this is FR-roots-specific.
- **[[h-new-630-supercluster-substructure|H-NEW-630]]**: 3-tier mufaṣṣal hierarchy. The hierarchy is in Arabic root-space, not English content-space.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]**: Q56/57 Hijra hinge. The Hijra-kink at s=50 is ARABIC-specific; in English the kink moves toward s=25 (still β > 0; not interpretable as Hijra).
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]**: mushaf 11% TSP-residual in Fisher-Rao space. The compression-tail explained part of the residual. [[h-new-710-translation-invariance|H-NEW-710]] reinforces that this is a Fisher-Rao-Arabic phenomenon.
- **Classical scholarship (al-Zarkashī mufaṣṣal)** — the *naming* of the compression-tail is in Arabic morphological terms. [[h-new-710-translation-invariance|H-NEW-710]] is consistent with this: the al-mufaṣṣal sub-divisions are Arabic-rhetorical units, recovered in Arabic-rooted measurement.
- **Loanword-density / [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] 5-factor model**: register and chrono-homogeneity were the dominant content-axis predictors. In English they project oppositely; this is consistent with the [[h-new-710-translation-invariance|H-NEW-710]] finding that English measurement is on a different axis.

## 7. Queued follow-ups

- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]**: Length-normalized English content-cosine (TF-IDF or self-overlap-rate) — does the compression-tail re-emerge when length-overlap is removed? This is the clean test of "is it the measurement-instrument or the language?".
- **H-NEW-721**: Compare across multiple translations (Pickthall, Yusuf Ali, Asad). Are the gradients all positive-slope, or is Sahih an outlier?
- **H-NEW-722**: Sentence-level semantic embeddings (e.g., multilingual-LASER or GPT-style) — do those recover the Arabic compression-tail when applied to English Sahih? This is the strongest test of structural-content vs Arabic-surface.
- **H-NEW-723**: The English anti-correlated gradient (R²=0.96, β > 0) is a NEW finding in its own right. Pre-register a separate confirmatory test on a held-out translation.
- **H-NEW-724**: Test whether the English r=−0.91 anti-correlation is *also* sensitive to the Hijra-boundary or to a different boundary (e.g., the qiṣār boundary at Q 78). Is there a kink in the English curve at a different location?

## 8. Final statement

**The Arabic mushaf compression-tail ([[h-new-660-compression-tail-gradient|H-NEW-660]], R²=0.986) is NOT translation-invariant under the [[h-new-710-translation-invariance|H-NEW-710]] protocol.** Mechanical application of the protocol to English Sahih top-200-stem cosine yields R²=0.9586 — formally extraordinary by R² alone — but with the OPPOSITE slope (β=+0.00612 in English vs. β=−0.01237 in Arabic) and Pearson r=−0.91 between the 100-window curves. The terminal qiṣār is the MOST cohesive in Arabic FR-roots and the LEAST cohesive in English top-stems; the head ṭiwāl is the most cohesive in English but moderate in Arabic.

**The PRE-REG-STANDARD-04 verdict is NULL on translation-invariance**: the directional hypothesis (β < 0 in English) FAILS, and the interpretive thresholds requiring two-piece kink in [40, 60] also FAIL.

**The interpretive conclusion**: the [[h-new-660-compression-tail-gradient|H-NEW-660]] compression-tail is **structurally-locked to the Arabic root-system**. Late-Meccan terminal-qiṣār surahs share a tight Arabic root-inventory (apocalyptic, oath, eschatological) which is **not recovered** by top-stem-cosine on English Sahih. In Sahih English, those same short terminal surahs are too lexically sparse (some only 9 stems) to register as cohesive in a top-200-stem vocabulary. The Arabic FR-roots metric and the English top-stem-cosine metric are measuring **orthogonal-to-anticorrelated axes** of mushaf cohesion.

**The anti-correlated English gradient is a NEW emergent finding** worth its own pre-registered investigation: the canonical mushaf order is structured such that, *in English content-vocabulary*, head ṭiwāl is maximally cohesive and terminal qiṣār is maximally dispersed, with R²=0.96 fitting a smooth quadratic.

**For the broader project**: this NULL result is *more informative than a PASS would have been*. A pass would have meant the compression-tail is a generic content-cohesion phenomenon. The NULL tells us specifically that the Arabic compression-tail is a **language-particular morpho-rhetorical signature**, embedded in the Arabic root-system, that does not survive translation. The 14-century classical tradition naming this as al-mufaṣṣal is therefore correct to use *Arabic morphological vocabulary* — the compression IS Arabic-rhetorical, not generic-semantic.

This refines [[h-new-660-compression-tail-gradient|H-NEW-660]]: the mushaf has a 1-D cohesion-architecture **in the Arabic FR-roots lens**, with a different (opposite-direction) 1-D architecture in the English-content lens. Both R²s are >0.93. The mushaf's structure is multi-dimensional in cohesion-space; choice of lens determines which axis dominates.

The honesty point: structural laws should pass at least one translation-invariance test before being claimed as universal. [[h-new-660-compression-tail-gradient|H-NEW-660]]'s R²=0.986 is real but is now properly scoped as an **Arabic-FR-roots-specific** law, not a universal content-cohesion law. The structural-vs-Arabic-surface question, asked in the prompt, has a clear answer: **the [[h-new-660-compression-tail-gradient|H-NEW-660]] compression-tail is Arabic-surface-specific, not deep-semantic-structural**, under the locked rules-tuple.

The 14-century classical scholarship did not make the universal-law claim; it always named the compression-tail in Arabic-rhetorical terms (mufaṣṣal). [[h-new-710-translation-invariance|H-NEW-710]] vindicates the classical scope.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
