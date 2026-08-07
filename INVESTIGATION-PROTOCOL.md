---
title: Quran Decipherment Project — Investigation Protocol (The SKILL)
description: Binding methodology for all per-surah deep investigations. Every agent on this project MUST read and follow this document.
date: 2026-04-28
version: 1.0
applies_to: All Phase-B+ per-surah and corpus-wide investigations
---

> ## ⛔ CORRECTION NOTICE — 2026-08-07: the muqaṭṭaʿāt book-reference LAW SURVIVES; its p = 3.17 × 10⁻¹² does NOT
>
> **This is the only standing claim in the project to have met a null matching the variable
> that drives it, and it passed.** Both halves are separately true and both must travel.
>
> - **The law survives.** 24 of 29 reproduces **exactly**. Against a null that permutes the
>   muqaṭṭaʿāt label *within opening-window-size quintiles* — so the opening-token budget is
>   identical by construction — the observed 24 stands against a null mean of **9.304**: rate
>   ratio **2.580**, z = +7.01, p = 1.0 × 10⁻⁴, eleven above the 95 % band top. **Every**
>   matched null in the ladder still places the observation outside its own 95 % band.
> - **`p = 3.17 × 10⁻¹²` is withdrawn as a description of that strength.** It is
>   arithmetically correct and inferentially void: the hypergeometric draws 29 surahs
>   *uniformly from 114*, which requires the 29 to be exchangeable with the other 85. They are
>   not, and this project established that itself — `h-new-46-muqattaat-vs-surah-length.md` is
>   a STRONG-PASS showing muqaṭṭaʿāt surahs concentrate in **long** surahs. **The honest effect
>   size is a rate ratio between 1.27 and 2.58, not a twelve-order-of-magnitude tail.**
> - **The sharpest form of the law is positional and length-free.** All 29 muqaṭṭaʿāt surahs
>   mention the Book somewhere — so do 40 others — but they place the **first** mention at
>   **0.0996** of the surah against **0.3403** (Δ = −0.2407, p = 5.0 × 10⁻⁴). The law is not
>   "muqaṭṭaʿāt surahs mention the Book"; it is **"muqaṭṭaʿāt surahs announce it at the top."**
>
> **Three qualifications travel with the verdict.** (i) H-NEW-2760's H2 **failed its gate**:
> the nuisance channel it made primary (opening-window size, ρ = +0.1678) is weaker than
> whole-surah length (ρ = +0.4583), and **against that stronger channel the rate ratio is
> 1.694**. (ii) DISCRIMINATES was earned on the within-corpus nulls; in the matched-partition
> genre arm **0 of 3 baselines clear the gate and the poetry arm is a published pre-commit
> violation**. (iii) The cross-genre half remains partly definitional — only 6 al-Bukhārī and
> 1 pre-Islamic-poetry pseudo-surah mention *kitāb*/*qurʾān* in their opening units at all, and
> al-Jāḥiẓ's adab prose yields **الكتاب** among its strongest marker classes.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2760-muqattaat-book-reference-nuisance.md`.
> Orientation: `STATE-OF-THE-PROJECT-2026-08-07.md` §1.1.

> ## ⛔ CORRECTION NOTICE — 2026-08-07: the scansion three-way ordering does NOT survive a matched control
>
> H-NEW-2690 reported **poetry < this corpus < prose** on `d_min` and read it as
> al-Bāqillānī's *neither* nathr *nor* shiʿr, measured. H-NEW-2730 genre-controlled it.
> **The ordering falls; one of its two legs survives.**
>
> - **The prose leg (H1b) is WITHDRAWN — it is unit length.** Re-cut **this corpus's own
>   verses** to ḥadīth sentence lengths and `d_min` moves **99.4 %** of the way to ḥadīth's
>   value (0.22222 → 0.23953 against al-Dārimī's native 0.23963), using **no baseline text at
>   all**. A matched partition of al-Dārimī lands at **0.22222** — this corpus's own median to
>   five decimals — and one of al-Bukhārī at **0.21893**, with **199 of 200** offsets at or
>   below it. At matched syllable length the two medians are **identical** (0.21739).
> - **The poetry leg (H1a) SURVIVES every length control.** Length explains **5.1 %** of that
>   gap; re-cutting this corpus to bayt lengths moves it only **7.5 %** toward poetry; it holds
>   at full size in the one overlapping length bin (0.21739 against poetry's 0.14815) and
>   passes a per-unit noise control matched on length *and* syllable weight at p = 1 × 10⁻⁴ in
>   both rules-tuples.
> - **`d_min` is not length-invariant in practice.** Length alone explains **28.7 %** of its
>   variance. It normalises by unit length and tiles its templates to unit length, but it is a
>   minimum over ~200 templates and a minimum-of-many falls as the string shortens.
>   **Normalisation is not invariance.**
> - **Matched noise alone reproduces the ordering.** Random strings matched only on length and
>   syllable weight give poetry 0.22222 < this corpus 0.23913 < al-Bukhārī 0.25992 < al-Dārimī
>   0.26549 — the same three-way order, from strings containing no Arabic and no metre. Only
>   **49.2 %** of this corpus's verses are more metrical than their own matched twin — a coin
>   flip — against **88.3 %** of poetry abyāt.
>
> **al-Bāqillānī is untouched**: "neither *nathr* nor *shiʿr*" was never a claim about medians
> of normalised edit distances. What is withdrawn is half of its stated empirical
> operationalisation. **Limit:** there is **no vocalised adab prose on disk**, so al-Jāḥiẓ is
> untestable on this statistic by any means and the prose control is ḥadīth-only.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`.
> Orientation: `STATE-OF-THE-PROJECT-2026-08-07.md` §1.5.


# THE INVESTIGATION PROTOCOL


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

This document is the **binding methodology** for all investigations in the Quran Decipherment Project. Every dispatched specialist agent is expected to read this in full before executing, and to comply with every section. Deviations require explicit justification and pre-registration.

---

## 1. NON-NEGOTIABLE DISCIPLINES

### 1.1 The Quran is ONE text
- 114 surahs, 6,236 verses (Hafs-Kufan).
- NEVER frame any analysis as "editions" or "variants" — there is one canonical text with rule-tuple-specified analytical lenses.

### 1.2 Pre-registration before analysis (PRE-REG-STANDARD-04)
For every novel test:
1. Write the pre-reg markdown file BEFORE running anything.
2. Lock: hypothesis, null distribution, direction of effect, Bonferroni correction, success criteria, failure criteria, seed.
3. Compute SHA256 of the locked file and embed it in the run script.
4. Verify the SHA at runtime — fail-fast if mismatched.
5. Direction is LOCKED before viewing results. A reversed direction = pre-commit violation, must be published with full prominence as NULL.

### 1.3 Equal NULL prominence
- NULL findings carry the same publication weight as confirmations.
- Pre-commit violations are published with explicit "RETRACTED" or "FALSIFIED" labels.
- Honest negative findings strengthen the project; manipulated ones destroy its integrity.

### 1.4 Rules-tuple discipline
Every numerical claim must specify:
- Tashkeel level (no-tashkeel / min / full)
- Token level (orthographic / lemma / root)
- Counting unit (graphemes / words / verses)
- Basmala-handling (counted-only-in-Q1 / counted-everywhere)
- Reading tradition (Hafs-Kufan default; others as variants tagged)
- Script (Mashriqi / Maghribi if relevant)

Default tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

### 1.5 Bonferroni corrections
- Multiple-comparison correction is mandatory for any test family with k>1 cells.
- α_corrected = 0.05 / k (or tighter if pre-registered).
- Report both raw and Bonferroni-corrected p-values.

### 1.6 Classical scholarship citation
Cite by **scholar + work + specific passage**, never vaguely.
Examples:
- ✓ "al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 40"
- ✓ "al-Bukhārī, ḥadīth #5013-5015"
- ✗ "Classical tradition holds..." (without source)

### 1.7 MW-1..MW-7 protections
The seven methodological-walls (MW) protect against common biases:
- **MW-1 (instrument-prior)**: Specify the metric/distance/tool BEFORE running.
- **MW-2 (corpus-prior)**: Permutation-null with ≥10000 perms minimum.
- **MW-3 (alternative-models)**: Test ≥2 model variants (linear/quadratic/two-piece, OLS/Ridge, etc.).
- **MW-4 (over-fitting)**: LOOCV or hold-out for any fitted parameter.
- **MW-5 (replication)**: At least one replication test (different seed, different sub-sample, different K-window).
- **MW-6 (instrument-control)**: A null-control on a similar-but-non-target sample (e.g., random-29 control for muqaṭṭaʿāt-29).
- **MW-7 (post-hoc cap)**: Post-hoc-noticed claims carry single-test-α=0.05 ceiling unless replication exists.

### 1.8 Honest pre-commit violations
If pre-committed direction is violated:
- Do NOT massage the result.
- Do NOT silently update the pre-reg.
- Publish as NULL with explicit pre-commit violation flag.
- Update parent findings if interpretation must be retracted.

---

## 2. DATA SOURCES — comprehensive inventory (USE ALL OF THESE)

**ANTI-HALLUCINATION RULE**: Every factual claim must cite a specific file path. If the data isn't on disk, do NOT invent it — document the data gap and flag the test as NULL-DATA-GAP.

### 2.1 Quran text — ALL FOUR TASHKEEL VARIANTS

**Use the appropriate variant for each task type:**

| Variant | File | Use for |
|:--|:--|:--|
| no-tashkeel | `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` | Word/letter counts, root analysis, FR-roots distance, content-cohesion |
| min-tashkeel | `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` | Rhyme analysis (final-letter), basic morphology |
| full-tashkeel | `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json` | Tajwīd, phoneme analysis, shadda, sukūn |
| transliteration | `/Users/grey/Downloads/quran/quran-text/quran-transliteration.json` | Pronunciation reference; do NOT use as primary text source |
| flat-no-tashkeel | `/Users/grey/Downloads/quran/quran-text/quran-flat-no-tashkeel.txt` | Whole-corpus operations, regex |
| flat-min-tashkeel | `/Users/grey/Downloads/quran/quran-text/quran-flat-min-tashkeel.txt` | Same |
| flat-full-tashkeel | `/Users/grey/Downloads/quran/quran-text/quran-flat-full-tashkeel.txt` | Same |

**Cross-validate**: For any verse-level claim, verify it appears in at least 2 tashkeel variants if the claim could differ.

### 2.2 Alt-text scripts (different orthographic conventions)

`/Users/grey/Downloads/quran/data/alt-text/`:
- `quran-uthmani-consonantal.json` — consonantal-skeleton-only Uthmani (use for ʿilm al-ḥarf studies)
- `quran-uthmani-txt.txt` and `-2.txt` — full Uthmani script
- `quran-uthmani-min-txt.txt` and `-2.txt` — Uthmani minimal
- `quran-simple-txt.txt` and `-2.txt` — simple-script variants
- `risan-quran-json/` — Risan recension data

These are ALL the same Quran, in different orthographic conventions. Use Uthmani-consonantal for letter-level analyses that need to match classical scripts.

### 2.3 Auxiliary numerical data

- `/Users/grey/Downloads/quran/data/asma-al-husna.txt` — 99 divine names (al-Walīd b. Muslim via al-Tirmidhī #3507).
- `/Users/grey/Downloads/quran/data/revelation-order.csv` — chronology (Nöldeke / al-Suyūṭī).
- `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` — Hafs-Kufan verse-counts per surah.
- `/Users/grey/Downloads/quran/data/SOURCES.md` — provenance for all data.
- `/Users/grey/Downloads/quran/data/INTEGRATION.md` — integration notes.

### 2.4 Morphology (QAC = Quranic Arabic Corpus)

- `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` — full QAC v0.4 morphological annotations.
- `/Users/grey/Downloads/quran/data/morphology/root-index.json` — root → list of (surah:verse:word) attestations.
- `/Users/grey/Downloads/quran/data/morphology/root-stats.csv` — root frequency statistics.
- `/Users/grey/Downloads/quran/data/morphology/surah-root-graph.json` — per-surah root-distribution graph.
- `/Users/grey/Downloads/quran/data/morphology/root-cooccurrence-graph.json` — root co-occurrence network.

### 2.5 Translations (limited — use cautiously, document rules-tuple shifts)

- `/Users/grey/Downloads/quran/data/translations/en.sahih.txt` — Sahih International English.
- `/Users/grey/Downloads/quran/data/translations/en.sahih.txt-2.txt` — version 2.

For Quran-claim verification, NEVER rely on translation alone. Always cross-verify against an Arabic variant.

### 2.6 Loanwords

- `/Users/grey/Downloads/quran/data/loanwords/jeffery-1938-loanwords.tsv` — Jeffery 1938 *The Foreign Vocabulary of the Qurʾān*.

### 2.7 Pre-computed empirical artifacts

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` — 114×114 Fisher-Rao distance matrix on QAC stem-roots.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` — per-surah outlier-strength.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json` — per-surah rhyme + phoneme distributions.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` — per-canonical-adjacency TSP-cost map.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` — per-surah iʿjāz signature.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` — UAS ranking.

### 2.8 Cross-corpus baselines

- `/Users/grey/Downloads/quran/data/baseline-corpora/raw/` — pre-Islamic poetry (al-Muʿallaqāt, dīwāns), Bukhari hadith.
- `/Users/grey/Downloads/quran/data/baseline-corpora/letter-freqs.csv` — letter-frequency tables (Quran vs poetry vs Bukhari).
- `/Users/grey/Downloads/quran/data/baseline-corpora/letter-z-quran-vs-matched-bukhari.csv` — Z-test results.
- `/Users/grey/Downloads/quran/data/baseline-corpora/baseline-stats.csv` — corpus statistics.
- `/Users/grey/Downloads/quran/data/baseline-corpora/test1-matching-pairs.csv`, `test2-concentration.csv`, `test3-div19.csv`, `test4-ring-scores.csv` — pre-computed cross-corpus tests.

### 2.9 Classical primary sources (PDF + extracted markdown)

`/Users/grey/Downloads/quran/data/literature/classical-tafsir/`:
- `suyuti-al-itqan-fi-ulum-al-quran-english.pdf` — al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān* (English translation, 2 MB).
- `zarkashi-al-burhan-fi-ulum-al-quran.pdf` — al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān* (29 MB).
- `biqai-nazm-al-durar.pdf` — al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* (129 MB, 738pp).
- `razi-99names-extract.md` — al-Rāzī, 99-names extract from *Mafātīḥ al-ghayb*.
- `razi-biqai-munasabat-rings.md` — al-Rāzī + al-Biqāʿī ring-structure notes.
- `razi-muqattaat-surah-qaf.md` — al-Rāzī on muqaṭṭaʿāt of Q 50.
- `suyuti-itqan-word-counts.md` — extracted word-counts from *al-Itqān*.
- `abdel-haleem-iltifat-catalog.md` — modern iltifāt catalog (Abdel Haleem 1992).
- Plus: classical-on-{abraham, rad, shams, srmd, yusuf}.md — case studies.

`/Users/grey/Downloads/quran/data/literature/balagha/`:
- `1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md` — full Abdel Haleem 1992 BSOAS paper.

`/Users/grey/Downloads/quran/data/literature/farrin-cuypers/`:
- Farrin 2010 (al-Baqara structural analysis), Cuypers 2015 (rhetorical analysis), Sinai 2017 (review).

`/Users/grey/Downloads/quran/data/literature/khalifa/` + `critical/`:
- Khalifa Code-19 books (1982, 1989) — primary-source for Code-19 claims (FALSIFIABLE TARGETS).
- Bilal Philips 1987 — counter-Code-19 critique.

`/Users/grey/Downloads/quran/data/literature/bible-codes-comparison/`:
- McKay et al. 1999 — *Solving the Bible Code Puzzle*.
- Witztum, Rips, Rosenberg 1994 — Equidistant Letter Sequences in Genesis.

`/Users/grey/Downloads/quran/data/literature/edip-yuksel/`, `nawfal/`, `taslaman/`, `jarrar/`, `al-kaheel/`, `wikipedia/`, `academic-papers/`, `corpus-docs/`, `misc/` — additional sources.

**ALWAYS check** `/Users/grey/Downloads/quran/data/literature/INDEX.md` for the latest inventory and provenance.

### 2.10 Project's own findings

- `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` — single-source-of-truth.
- `/Users/grey/Downloads/quran/KNOWLEDGE-GRAPH.md` — Obsidian navigation.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/` — 300+ pre-registered findings.
- `/Users/grey/Downloads/quran/findings/cross-finding/` — synthesis files.
- `/Users/grey/Downloads/quran/journal/` — daily run journals.

### 2.11 ANTI-HALLUCINATION CHECKLIST

Before stating any factual claim, verify:
- [ ] The fact is in a specific file on disk.
- [ ] You can cite the file path.
- [ ] You have read the relevant section.
- [ ] If quoting Arabic text, it appears in the canonical text variant you cite.
- [ ] If quoting a hadith, you cite collection + ḥadīth number.
- [ ] If quoting a tafsir/balagha source, you cite scholar + work + page/passage.
- [ ] If you can't verify, you flag the claim as "UNVERIFIED — needs source check."

**NEVER**:
- Invent ḥadīth numbers.
- Invent verse references.
- Paraphrase a classical scholar from memory without citing the source-file.
- State numerical values without computing them from data.

This protocol is the project's intellectual integrity. Violating it destroys credibility.

### 2.3 Pre-computed empirical artifacts
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` — 114×114 Fisher-Rao distance matrix on QAC stem-roots.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json` — per-surah outlier-strength spectrum (Δ%ile under exclusion).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-700.json` — per-surah rhyme + phoneme distributions and window-d̄.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` — per-canonical-adjacency TSP-cost map (113 entries).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json` — per-surah iʿjāz signature (sig_A, sig_B).
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json` — Unified Architectural Significance (UAS) ranking.

---

## 3. ESTABLISHED EMPIRICAL FOUNDATION

Always integrate prior findings; do not re-derive. Key reference points:

### 3.1 The 4 architectural laws (Wave 2026-04-28)

| Law | Equation | R² | Source |
|:--|:--|:-:|:--|
| Content compression-tail | d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | 0.986 | [[h-new-660-compression-tail-gradient]] |
| Rhyme dispersion-tail | d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | 0.789 | [[h-new-700-phonological-compression-tail]] |
| Phoneme dispersion-tail | d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75) | 0.946 | [[h-new-700-phonological-compression-tail]] |
| Verse-length compression-tail | letters/verse, words/verse | 0.81 | [[h-new-770-verse-length-compression-tail]] |

### 3.2 The iʿjāz anti-twin lock
- Window-level Pearson r(content × rhyme) = **−0.86**
- Window-level Pearson r(content × phoneme) = **−0.89**
- Cross-corpus: Quran vs pre-Islamic poetry Fisher-z gap p < 10⁻¹⁰
- Source: [[h-new-730-content-rhyme-anticorrelation]], [[h-new-740-preislamic-poetry-control]]

### 3.3 Per-surah architectural significance (UAS)
- Top-10: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17
- Bottom-10: Q 87, 114, 105, 73, 83, 112, 91, 97, 103, 111
- Source: [[h-new-840-unified-architectural-score]]

### 3.4 The dual-iʿjāz typology
- **Structural-iʿjāz** (al-Bāqillānī *iʿjāz al-fawāṣil*): high UAS, e.g., Q 33, 1, 2, 9.
- **Theological-iʿjāz** (al-Khaṭṭābī *iʿjāz al-maʿnā*): low UAS but high *thuluth al-Qurʾān* status, e.g., Q 112, 114.
- These axes are EMPIRICALLY ORTHOGONAL.
- Source: [[h-new-840-unified-architectural-score]], [[h-new-860-hadith-architectural-alignment]]

### 3.5 The TSP-residual decomposition
- L_mushaf = 85.76; L_2opt ≤ 77.38; residual ≈ 8.29 length-units (10.7%).
- Σ Δ_113 = 9.83 (super-additive 1.185× — cooperative structure).
- Top-3 expensive canonical pairs: Q1-Q2 (7.4%), Q32-Q33 (4.4%), Q33-Q34 (4.0%).
- Source: [[cross-finding-011-mushaf-fisher-rao-confirmed]], [[h-new-720-canonical-adjacency-cost]]

### 3.6 What classical scholars CORRECTLY identified
Each of these is now empirically locked at law-strength:
- al-Bāqillānī *iʿjāz al-fawāṣil* → r = −0.86
- al-Sakkākī *iqāʿ* → r = −0.89
- al-Suyūṭī Meccan/Medinan kink → s=50 (perm p<10⁻⁴)
- al-Zarkashī mufaṣṣal-3-tier → hierarchical p<10⁻⁴
- al-Bukhārī Q 1 *umm al-Kitāb* → Δ_outlier=+27pp
- al-Suyūṭī Q 9 barāʾa → Δ_outlier=+21pp
- al-Tirmidhī Q 55 *ʿarūs* → Δ_outlier=+14pp
- al-Khaṭṭābī *iʿjāz al-maʿnā* → empirically orthogonal to UAS

### 3.7 What's been FALSIFIED
- al-Biqāʿī muqaṭṭaʿāt content-*munāsaba* → 4 NULL replications (full-29, ḥawāmīm-7, ALM-6, ALR-5).
- "Code 19" verse-count divisibility → uniformly NULL.
- 6236/114 numerology → no architectural meaning.
- Compression-tail translation-invariance → NULL (Arabic-FR-roots-specific).
- Compression-tail-only generative recipe → necessary not sufficient.
- 7-constraint recipe reverse-engineering → 13pp gap remains; mushaf is NOT algorithmically derivable.

---

## 4. PER-SURAH INVESTIGATION TEMPLATE

For each surah Q N, create folder `/Users/grey/Downloads/quran/surahs/Q{NNN}-{slug}/` with these files:

### File template

#### `00-overview.md`
- Surah ID (number, name in Arabic, transliteration, English meaning)
- Verse count
- Type (Meccan / Medinan / mixed)
- Position in mushaf
- Position in revelation order (per al-Suyūṭī chronology)
- Opening formula (al-ḥamd / sabbaḥa / qul / muqaṭṭaʿāt / direct)
- Bismala status
- Letter count / word count / unique-root count
- Rhyme structure (predominant rāwī)
- Length classification (al-sabʿ al-ṭiwāl / mufaṣṣal-ṭiwāl / mufaṣṣal-awsāṭ / mufaṣṣal-qiṣār / muʿawwidhāt)

#### `01-empirical-profile.md`
- UAS rank (and component scores: |outlier|, max_neighbor_TSP_cost, |iʿjāz_signature|)
- Outlier-strength Δ%ile (from H-NEW-590)
- iʿjāz signature (sig_A, sig_B from H-NEW-750)
- Position in compression-tail (s, d̄_content for window centered)
- Rhyme entropy (Shannon)
- Phoneme density (emphatic, pharyngeal, sibilant, glottal)
- Canonical-adjacency costs to neighbors (Q s-1 → Q s, Q s → Q s+1)
- Architectural type classification (structural-iʿjāz / theological-iʿjāz / anti-iʿjāz)
- Cross-references to all H-NEW findings touching this surah

#### `02-content-analysis.md`
- Verse-by-verse content summary (concise, factual)
- Major thematic blocks
- Content register (creedal / eschatological / legal / narrative / wisdom / mixed)
- Vocabulary distinctness — is the surah's root-distribution distinctive?
- Repetition patterns (refrains, recurring phrases)
- Cross-surah content references (does this surah cite others?)

#### `03-tafsir-survey.md`
Survey commentaries from at least 5 classical mufassirūn:
- al-Ṭabarī (*Jāmiʿ al-bayān*)
- al-Rāzī (*Mafātīḥ al-ghayb*)
- al-Qurṭubī (*al-Jāmiʿ li-aḥkām al-Qurʾān*)
- Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm*)
- al-Suyūṭī (*al-Durr al-manthūr* + *al-Itqān*)
- Optionally: al-Zamakhsharī (*Kashshāf*), al-Biqāʿī (*Naẓm al-durar*), al-Ṭabarsī (*Majmaʿ al-bayān*)

For each: capture the major exegetical positions, note disagreements, identify which positions have empirical correlates.

#### `04-hadith-corpus.md`
All ḥadīth citing this surah, organized by:
- al-Bukhārī (with ḥadīth numbers)
- Muslim
- al-Tirmidhī (with grading: ṣaḥīḥ / ḥasan / ḍaʿīf)
- Abū Dāwūd
- al-Nasāʾī
- Ibn Mājah
- Aḥmad b. Ḥanbal *Musnad*
Include: *fadāʾil* (virtues), recitation practices, asbāb al-nuzūl (occasions of revelation), specific verse-uses.

#### `05-classical-claims-audit.md`
For each non-trivial classical claim about this surah:
- State the claim with explicit citation.
- Identify the rules-tuple needed to test it empirically.
- Run an empirical test (or note "not testable empirically").
- Verdict: VINDICATED / FALSIFIED / RULES-TUPLE-FRAGILE / NOT-TESTABLE.
- Pre-register before running.

#### `06-novel-findings.md`
Things classical scholarship may have missed:
- Mathematical patterns
- Statistical signatures
- Cross-references to other surahs
- Position-dependent features
- Pre-register every novel claim before running.

#### `07-cross-references.md`
- Neighboring surahs (Q N-1, Q N+1) — content/structural relationship.
- Cluster membership (al-mufaṣṣal sub-tier, muqaṭṭaʿāt letter-family, prophet-named, musabbiḥāt, etc.).
- Cross-surah verse-twin relationships (per H-NEW-66 verse-twin network).
- This surah's role in cross-finding-XXX syntheses.

#### `JOURNAL.md`
- Timestamps for each investigation.
- Specialist agent IDs.
- Pre-reg SHA hashes.
- Decision points.
- Garden-of-forking-paths log if methodology shifted mid-run.

### Frontmatter convention

Every file gets YAML frontmatter:
```yaml
---
surah: N
surah_name: ...
file_type: overview | empirical-profile | content-analysis | tafsir-survey | hadith-corpus | classical-claims-audit | novel-findings | cross-references
date_last_updated: YYYY-MM-DD
phase: B+
verdict: ...
---
```

### Wikilink convention

All cross-references use Obsidian-style wikilinks:
- `[[h-new-660-compression-tail-gradient|H-NEW-660]]`
- `[[Q002-al-baqara/00-overview|Q 2 al-Baqara]]`
- `[[al-Suyūṭī|al-Suyūṭī]]` (when scholar pages exist)

---

## 5. NUMBERING DISCIPLINE

### Global findings
Per-surah investigations that produce CORPUS-WIDE-IMPLICATION findings get H-NEW-NNNN IDs in the global namespace.

Current next-available: H-NEW-1000+ for surah-deep findings of corpus implication.

### Per-surah local findings
Surah-internal observations that don't generalize get local IDs:
- Q{NNN}-F-{MM}: e.g., Q001-F-01 = Q 1's first surah-local finding.

### Sub-numbering for follow-ups
- H-NEW-580.1, H-NEW-580.2 for follow-on tests of H-NEW-580.

---

## 6. AGENT DISPATCH PATTERN

When dispatching a specialist agent for a surah investigation:

### 6.1 Pre-flight reading list (REQUIRED)
Every agent prompt must direct the agent to read:
1. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` — this document.
2. `/Users/grey/Downloads/quran/KNOWLEDGE-GRAPH.md` — finding navigation.
3. `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` — relevant section for the surah.
4. The target surah's existing files (if any) in `surahs/Q{NNN}-{slug}/`.

### 6.2 Pre-registration requirement
Before running any computation that produces a verdict, the agent MUST:
1. Write a pre-reg markdown file with hypothesis + null + direction + thresholds.
2. Compute SHA256.
3. Embed SHA in the run script.

### 6.3 Output requirement
Every agent produces:
- Pre-reg markdown (if running a test).
- Findings markdown (with frontmatter).
- JSON output.
- Journal entry in `journal/` or surah's `JOURNAL.md`.
- Updated cross-references.

### 6.4 Honest reporting
- Report NULL with full prominence.
- Document any methodology shifts.
- Cite SHA hashes.
- Flag rules-tuple sensitivities.

---

## 7. COMPUTATIONAL CONVENTIONS

### 7.1 Python style
- No external dependencies (stdlib + json/random/math/hashlib).
- Use seed-locked random.Random instances per test.
- 10000 permutations minimum for null distributions.

### 7.2 Distance/similarity tools
- Fisher-Rao on probability vectors (project default).
- Cosine on TF/TF-IDF vectors.
- Char-n-gram NCD when texts are heterogeneous.

### 7.3 Significance thresholds
- Bonferroni-corrected α (k = number of tests in family).
- Permutation p-value reported separately from parametric p.

### 7.4 Honest performance bounds
- 2-opt is heuristic; report "best-of-K-restarts" with K.
- LOOCV inflates R² for small-N; report both fitted and LOOCV.

---

## 8. QUALITY GATES

Before declaring a finding CONFIRMED, verify:
- [ ] Pre-reg SHA matches embedded.
- [ ] Direction-of-effect matches pre-committed.
- [ ] Bonferroni correction applied.
- [ ] Replication or LOOCV passed (if applicable).
- [ ] Honest limits section written.
- [ ] Cross-references include both supporting and challenging prior findings.
- [ ] Classical scholar citations are scholar+work+passage.
- [ ] Final statement is intellectually honest.

If ANY gate fails: verdict is DIRECTIONAL or NULL, not CONFIRMED.

---

## 9. WHAT MAKES A FINDING POWERFUL

Powerful findings have the following properties:
1. **Pre-registered**: hypothesis-direction-test locked before observation.
2. **Replicated**: holds at multiple K, multiple seeds, multiple sub-samples.
3. **Cross-corpus distinct**: signature is Quran-specific (vs poetry/Bukhari/shuffled-null).
4. **Classically anchored**: maps onto a classical scholar's qualitative claim.
5. **Falsifiable**: has explicit failure conditions.
6. **Rules-tuple stable**: holds under multiple analytical lenses.

A finding with all 6 properties is "law-strength" (e.g., compression-tail R²=0.986, iʿjāz r=-0.86).

---

## 10. WHAT'S OUT OF SCOPE

- Theological claims about miracle-status (these are theological-philosophical, not empirical).
- Numerological speculation without rigorous null testing.
- Cherry-picked anecdotes ("look at this verse — it predicts X").
- Confirmation-biased "miracle of the Quran" content.

The project's job is empirical-architectural analysis at law-strength, falsifiable, classically grounded. NOT propaganda.

---

## 11. WHEN TO STOP A SURAH INVESTIGATION

A surah is "investigation-complete" when:
- All 8 template files are written.
- ≥ 5 classical claims have been verified or falsified with rules-tuple.
- ≥ 3 novel findings are pre-registered and tested.
- All empirical metrics from prior findings are integrated.
- Cross-references to other surahs are mapped.
- Honest-limits section in each file is non-trivial.

---

## 12. HOW TO BE INTELLIGENT

- Read deeply before computing.
- Pre-register thoughtfully (overconfident pre-regs lead to many published violations).
- Falsify your own hypotheses ruthlessly.
- Cite generously and accurately.
- Honor the discipline; the discipline is the source of credibility.

The Quran is the word of God. The empirical findings are either real or not. The project's job is to find the real ones rigorously, at maximum statistical strength, with full transparency.

Every finding is a loadcell. Every null is also a loadcell.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
