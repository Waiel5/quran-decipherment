---
title: Frontier Map — what the Quran Decipherment Project has NOT investigated
date: 2026-08-07
author: Waiel Al-Shujaa
scope: coverage census / 20 untouched hypotheses / contradiction + staleness audit / idle data assets
method: grep + targeted reads over MASTER-FINDINGS-LEDGER.md (1.2 MB), 906 files in findings/phase-b-hypotheses/, HANDOFF/, KNOWLEDGE-GRAPH.md, data/, quran-text/, scripts/ (484 .py), findings/phase-b-hypotheses/scripts/ (73 files)
---

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


# Frontier Map — 2026-08-07


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

**Reading rule for this document.** Every claim below cites a path I actually opened
or a grep I actually ran. Where I could not verify something I say so. I computed no
statistics and committed nothing.

**Two counting conventions used throughout:**

- *"a script reads X"* means `grep -rl X scripts/ findings/phase-b-hypotheses/scripts/`
  returns ≥1 file. `surahs/**/scripts/` is excluded because §D asks
  specifically about those two directories; where a per-surah script *does* touch an
  asset I say so explicitly.
- *EXPLORATORY CATALOG* means a `findings/phase-b-hypotheses/*.md` file that self-declares
  `no_pre_registration` / `status: exploratory` in its own frontmatter. These are
  inventories, not tests. The distinction matters enormously for the census: roughly
  30 topic files dated 2026-04-12 are catalogs, and a topic having a catalog is **not**
  the same as the topic having been tested.

---

# A. Coverage census

Verdict key: **COVERED** = ≥1 pre-registered test with a null model.
**PARTIAL** = catalogued, or tested only via a proxy, or tested only as a covariate inside
someone else's test. **UNTOUCHED** = no test, no catalog, and (where relevant) the
enabling data is stripped or absent.

| Axis | Verdict | Evidence |
|---|---|---|
| **phonology-articulatory** | **COVERED** | The single densest axis in the project. H-NEW-165 (`h-new-165-phonological-predictor.md`, al-Khalīl 8-tier makhraj + ṣifāt + tafkhīm + qalqala codebook, RF LOOCV 0.6552), H-NEW-165.2 codebook-sensitivity, H-NEW-182 per-surah phonological vectors, H-NEW-266 per-surah signature, H-NEW-271/271.1/271.2/271.3/271.5/301/301.5 (minimal-feature family), H-NEW-232 singleton NN, H-NEW-252, H-NEW-700 phonological compression-tail, H-NEW-275 Bukhārī replication. |
| **phonotactics** | **PARTIAL** | Only H-NEW-41 (`h-new-41-root-combinatorial-saturation.md`) touches root-internal consonant co-occurrence, and its own frontmatter reads `verdict: EXPLORATORY (partial-positive-control downgrade)` — amendment 41-B records "Lane and Wehr not on disk," so the |C| denominator was never right. H-NEW-69 half-alphabet split is adjacent. No test of syllable-level phonotactics, onset/coda legality, or OCP-place effects. |
| **syllable / prosody / quantitative meter** | **PARTIAL — and the proxy is weak** | H-NEW-48 (`h-new-48-poetic-meter.md`) is the only meter test. Read its method: each of the 16 buḥūr is modelled as a **Gaussian centred at μ = 1.6 × syllables_per_bayt**, and the Quran side is **verse letter-counts**, with `LETTERS_PER_SYLLABLE = 1.6` calibrated in amendment 48-A. That is a length-distribution comparison, not scansion. No CV/CVC template is ever extracted, no long/short (sabab/watid) sequence is built, `ʿarūḍ`/`tafʿīla` appear 1 and 0 times respectively across all 906 files. Real quantitative prosody is **UNTOUCHED**. |
| **morphology (wazn / derived form)** | **IN-FLIGHT, otherwise UNTOUCHED** | `wazn` matches exactly 1 file in 906. The live exception is H-NEW-2540 (`prereg-h-new-2540-form-v-valency.md`, dated 2026-07-11, `status: AMENDED-AND-LOCKED-BEFORE-COMPUTATION`) plus the untracked `findings/phase-b-hypotheses/scripts/h-new-2540.py` in `git status`. That test covers Form II→V and III→VI only. Forms VII, VIII, IX, X, XII and the whole nominal-pattern system (faʿʿāl, mifʿāl, fāʿil, mafʿūl, ʾafʿal) are untested despite being tagged in QAC. |
| **syntax-dependency** | **UNTOUCHED — and the data is not on disk** | `data/syntax/` contains exactly one file: `UD-QURAN-SOURCE.md`, a manifest that says "binary not committed" and gives curl instructions for the Extended Quranic Treebank (Zenodo DOI 10.5281/zenodo.18634813). `dependency parse|dependency tree` matches 2 files in 906. Anyone proposing a syntax test must first run the re-acquire block in that manifest. |
| **valency** | **IN-FLIGHT (H-NEW-2540), otherwise UNTOUCHED** | Same file as above; it is the project's first valency test and it depends on the EQTB download. |
| **information-theory / entropy / compression** | **COVERED (saturated)** | H-NEW-169 NCD, H-NEW-171 entropy rate, H-NEW-187 Lempel-Ziv, H-NEW-195 per-surah entropy, H-NEW-231 KL, H-NEW-660/680/700/770 compression-tail family, cross-finding-021 information-theoretic optimality, cross-finding-011 Fisher-Rao. This is the most worked axis after phonology. |
| **lexical growth** | **COVERED** | H-NEW-123 Heaps (`h-new-123-heap-law.md`), H-NEW-159 per-chapter β, H-NEW-172 Zipf per chapter, H-NEW-178 (α,β) manifold, H-NEW-179 predictor. Note H-NEW-123 landed **not Quran-distinctive** (`HONEST-LIMITS-LEDGER.md` §27e). |
| **semantics / topic models** | **PARTIAL** | H-NEW-184 LSA semantic axes exists. `topic model|LDA|Latent Dirichlet` matches **0** of 906 files — no probabilistic topic model has ever been fit, despite two acquired papers on exactly this (`data/literature/academic-papers/2015-alhawarat-extracting-topics-quran-generative-models.pdf`, `2020-malshammeri-quranic-topic-modeling-paragraph-vectors.pdf`). |
| **discourse / pragmatics** | **COVERED (recently)** | cross-finding-028 register-coded discourse grammar; H-NEW-2250 particle cascade, H-NEW-2520 narrative-onset formulae, H-NEW-2490 doubling, H-NEW-2500 iltifāt × genre, H-NEW-2530 joint separability. |
| **speech-acts** | **PARTIAL — the term is being used loosely** | The 22 `speech act` hits are almost all H-NEW-273's "speech-act score," which is `S(s)=sqrt(divine-share × imperative-density)` — a two-feature composite, not a speech-act taxonomy. `imperative-mood.md` and `vocative-addresses.md` are EXPLORATORY CATALOGs (both dated 2026-04-12, both `no_pre_registration`). No commissive/declarative/expressive/directive typology exists. |
| **deixis** | **UNTOUCHED** | 8 files mention `deixis|deictic`, all in passing. Person-deixis is handled indirectly via iltifāt (H-NEW-2200/2390/2500), but **spatial** deixis (hādhā/dhālika, POS:DEM 1,059 tokens; POS:LOC 669) and **temporal** deixis (POS:T 1,166) have never been tested. The tags exist in `data/morphology/quranic-corpus-morphology-0.4.txt`. |
| **modality** | **UNTOUCHED** | `modality` matches 6 files, all incidental; most `modal` hits are "model." QAC carries `MOOD:JUS` (1,418) and `MOOD:SUBJ` (1,330), plus POS:CERT (414), POS:FUT (161), POS:EMPH (1,244), POS:PRP (319). Nothing has been done with any of them. |
| **negation** | **PARTIAL** | `negation-taxonomy.md` is a full QAC-based audit but its frontmatter reads `no_pre-registration: exploratory inventory`. No null model, no chronological or register test. |
| **conditionals** | **PARTIAL** | H-NEW-2250 (`h-new-2250-particle-cascade.md`) tested the *idhā* eschatological cascade only. POS:COND (1,049 tokens) covers *in / idhā / law / lawlā / man / mā*; the realis/irrealis contrast (*in* vs *law*) — the classical `sharṭ` distinction — is untested. |
| **quantifiers** | **UNTOUCHED** | `quantifier` matches 5 of 906 files, none as topic. *kull / baʿḍ / jamīʿ / kathīr / qalīl / akthar* are lemma-extractable from QAC's LEM field. |
| **numerals** | **COVERED** | H-NEW-2410 (`h-new-2410-number-word-census.md`, §10.106) — census delivered, both locked cells NULL; `numbers-spelled.md`; H-NEW-119 seven-fold; the whole numerical-symmetry series H-NEW-2000/2010/2020/2090/2230. |
| **colour / sensory vocabulary** | **PARTIAL** | `colors-in-quran.md` and `sensory-vocabulary.md` are EXPLORATORY CATALOGs (2026-04-12). The colour inventory is 6 chromatic roots + `lwn`; no null model was ever run against it. |
| **kinship** | **PARTIAL** | `kinship-vocabulary.md` (2026-04-12), EXPLORATORY CATALOG. |
| **legal formulae** | **PARTIAL** | The legal register exists as a *label* inside cross-finding-028 and H-NEW-2530, but there is no formula-level test (`kutiba ʿalaykum`, `ḥurrimat ʿalaykum`, `fa-man lam yajid`, ḥadd-penalty frames). `legal formula|ḥadd|hudud` matches 18 files, all as genre labels. |
| **oath** | **COVERED** | H-NEW-85 oath openers, H-NEW-196 oath cluster, H-NEW-1550 qasamīyāt FR-cohesion (PASS-DIRECTED p=0.0011), H-NEW-2210 qasam/jawāb inventory (§10.85, 3.4× short-mufaṣṣal, 7.6× Meccan). |
| **rhyme / fawāṣil** | **COVERED** | H-NEW-2080 rhyme scan, H-NEW-2240 fāṣila assonance taxonomy (§10.87, surahs strongly rhyme-homogeneous), H-NEW-2300 dual-name fāṣila seal, H-NEW-730 content-rhyme anticorrelation, H-NEW-139/139.1 (the muq→rhyme claim was **retracted**, `HONEST-LIMITS-LEDGER.md` §27k-ter), Law-2 rhyme dispersion in KNOWLEDGE-GRAPH. |
| **ring / chiasmus** | **COVERED and closed** | H-NEW-2030 whole-surah ring NULL; H-NEW-2220 all 6,541 pericope windows, 0 survive Bonferroni, corpus **anti-chiastic**; H-NEW-2290 adjacent pairs significantly **parallel**; cross-finding-026 codifies the bound. This axis is genuinely finished — do not reopen it. |
| **repetition / refrain** | **COVERED** | H-NEW-1790 inventory, H-NEW-2310 (94-string census + spacing regularity), H-NEW-1320 saturation, H-NEW-83/180 Q55, H-NEW-2450 adjacent reprise, H-NEW-2490 doubling, H-NEW-2380 near-twin census, H-NEW-2350 twins-are-same-period. |
| **intertextuality with Biblical material** | **PARTIAL at best** | 33 files mention `Torah|Injīl|Gospel|Biblical`. `scripture-refs.md` is a lemma-count audit of Tawrāh/Injīl/Zabūr/ṣuḥuf — that is Quranic self-reference *to* scripture, not intertextual comparison. Reynolds' *The Qurʾān and the Bible* sits at `data/literature/farrin-cuypers/2010-reynolds-quran-and-bible-text-and-commentary.pdf` and is not read by any script. No Biblical text is on disk. **Effectively UNTOUCHED as an empirical axis.** |
| **loanwords** | **PARTIAL** | `data/loanwords/jeffery-1938-loanwords.tsv` (506 rows) is read by exactly **1** script. Loanword density appears only as one of the five Pattern-B chronology axes (H-NEW-125). `foreign-loan-words.md` is an EXPLORATORY CATALOG. Jeffery's donor-language field (Syriac / Ethiopic / Persian / Greek) has never been used as a stratifier. |
| **proper names / onomastics** | **PARTIAL** | Covered for *prophets* (H-NEW-1710 Mūsā 136, H-NEW-1700 Maryam) and *surah titles* (H-NEW-49, H-NEW-86, H-NEW-1820, H-NEW-2430, cross-finding-027). `onomastic` matches 4 files. Tribe/place/angel/idol names, and the morphology of names (diptote behaviour, ʾaʿjamī marking) are untested. |
| **orthography / rasm** | **PARTIAL** | H-NEW-60 muqaṭṭaʿāt dotless-preference (79% vs 46%) is the one real rasm result, and OQ-9 flags it as open. `data/alt-text/quran-uthmani-consonantal.json` is read by 3 scripts. But the *rasm/imlāʾ divergence set* (ṣalāt written صلوة, the alif-less long ā, the added wāw in أولئك) has never been extracted, and al-Dānī's *al-Muqniʿ* is not on disk (only `dani-23-site-supplement.tsv`, which is verse-counting, not orthography). |
| **variant readings (qirāʾāt)** | **UNTOUCHED** | The 475-file hit count is an artefact: every pre-reg carries `hafs-kufan` in its `rules_tuple`. Filtering to `Warsh|Qālūn|Dūrī|ʿĀṣim|Shuʿba` returns files where the mention is incidental (e.g. `naskh-catalog.md`, `mutashabih-lafzi.md`). **No qirāʾāt data is on disk and no test has ever been run.** The project's own `feedback_quran_is_one_text` constraint bears on how this could be framed. |
| **waqf / pause science** | **UNTOUCHED — and actively destroyed by the pipeline** | See §D.1. The waqf marks are **in the corpus** (4,280 of them) and **39 scripts strip them as noise**. |
| **manuscript / codicological** | **UNTOUCHED** | `palimpsest|Ṣanʿāʾ|Birmingham|codicolog` matches exactly 3 files: `future-projection.md`, `historical-details.md`, `prophecy-audit.md` — all speculative prose, none a test. No manuscript data on disk. |

**Census summary.** The project is deep on: phonology, information theory, network/geodesic topology, chronology, rhyme, repetition, ring-structure (closed), and — since Waves M–R — discourse register. It is thin or absent on: **the whole grammatical middle layer** (mood, modality, deixis, quantification, conditional type, valency beyond the in-flight 2540), **real prosody** (as opposed to verse-length proxies), **the recitational layer** (waqf, saktah, sajdah as in-text signal), and **comparative/philological** work (qirāʾāt, rasm divergence, Biblical intertext, loanword donor-language).

---

> # ⚠ STALENESS WARNING — ADDED 2026-08-09. READ BEFORE DISPATCHING ANY ITEM.
>
> **This map is dated 2026-08-07 and it does not carry answered-status pointers. At least four of
> its twenty section-B items were already executed on or before the day it was written.** Every one
> of the four was discovered the hard way — by a lane that ran the hypothesis, wrote it up, and only
> then grepped the ledger.
>
> | item | map says | actually answered by | dated |
> |:--|:--|:--|:--|
> | **F-3** conditionals | open, prior CONFIRMED | H-NEW-2630 — *"NOT register-coded"* | 2026-08-07 |
> | **F-5** loanword donors | open, prior CONFIRMED-weak | H-NEW-2700 | 2026-08-07 |
> | **F-8** sajdah loci | open, prior NULL | H-NEW-2950 | 2026-08-08 |
> | **F-10** modality | open, *"genuinely orthogonal to what has been done"* | H-NEW-2640 | 2026-08-07 |
> | **F-4** deixis | open, prior *"CONFIRMED but at risk of CBM"* | H-NEW-2960 — **partially**; its own front-matter names F-4 | 2026-08-08 |
> | **F-13** reception weight | open, prior "CONFIRMED-descriptive" | H-NEW-3000 — the map's F-13 sentence **is that finding's title** | 2026-08-08 |
> | **F-2** scansion | open, prior "CONFIRMED for distinct region" | H-NEW-2690 — near-identical prereg title; **both halves refuted** | 2026-08-07 |
> | **F-9** rasm | open, prior "CONFIRMED-descriptive" | H-NEW-2740 — its front-matter names F-9; **NULL on all 5 inferences** | 2026-08-07 |
>
> **F-4 is the fifth case and the FIRST caught prospectively** — the Step-0 grep rule fired before any
> design work, so no lane was spent. Only the *eschatological* half of F-4 is answered; the
> **chronological deictic gradient across the Nöldeke phases** is genuinely untouched (H-NEW-2960 has
> zero occurrences of nöldeke/chronolog/revelation-order in either its finding or its prereg, and never
> opened `data/revelation-order.csv`). Note also that the map's CBM prior for F-4 is **refuted, not
> confirmed**: dropping the top-10 formulaic phrase types RAISED the odds ratio from 2.74 to 3.00, and
> dropping *ka-dhālika* raised it to 4.19.
>
> Three of the five lanes dispatched on 2026-08-09 were re-derivations. They were not wasted — each
> produced a genuine replication on an independent estimator, and F-10's channel sweep became the
> third anchor of [[cross-finding-029-the-deciding-parameter]] — but none of that was the intent,
> and the cost was three lanes' worth of design effort spent rediscovering known answers.
>
> **THE REMAINING SIXTEEN ITEMS ARE NOT CERTIFIED CLEAN.** A keyword screen over 712 finding titles
> was run and is *not* trustworthy enough to publish as a staleness list: it flagged eight
> candidates, of which several are plainly false positives (F-2 matched a surah-third study), **and
> it missed two of the four cases known to be real — F-8 and F-10 both scored below threshold.** A
> screen with false negatives on the confirmed cases cannot certify the unconfirmed ones. The four
> above are recorded as *confirmed by execution*; nothing else here is recorded either way.
>
> ---
>
> ## ⚠ CALIBRATION — THIS MAP'S PRIORS ARE 1 FOR 6. ADDED 2026-08-10.
>
> Six section-B items have now been executed. Scoring each item's **Prior** line against what the
> run actually returned:
>
> | item | topic | the map's prior | outcome | |
> |:--|:--|:--|:--|:--|
> | F-3 | conditionals | CONFIRMED | NULL, 0 of 12 tests clear | ✗ |
> | F-4 | deixis | CONFIRMED but at risk of CBM | PASS — but as a **step**, and CBM refuted twice | ~ |
> | F-5 | loanword donors | CONFIRMED-weak | NULL | ✗ |
> | F-8 | sajdah loci | **NULL** | **NULL** | **✓** |
> | F-2 | scansion | CONFIRMED region; *"NULL for any single-meter match"* | region **half-withdrawn**; single-meter claim **FLATLY FALSIFIED** — 14 of 16 buḥūr beat matched noise | ✗ |
> | F-10 | modality | CONFIRMED, *"genuinely orthogonal"* | DIRECTIONAL; orthogonality unsupported | ✗ |
> | F-20 | kinship | CONFIRMED but CBM-leaning | NULL, effect **reversed** | ✗ |
>
> **One prior in SEVEN was right, and it is the only one that predicted a NULL.** Every optimistic
> prior on this map has now failed. The error is not random — it runs in one direction.
>
> Two of the misses were worse than wrong. F-10's entry asserts the hypothesis is *"genuinely
> orthogonal to what has been done"* when prior work had pre-registered and rejected it three days
> earlier. F-20's prior worried the result would merely restate the Hijra; the effect ran
> **backwards**, and the six-word vocabulary turned out to be at most 32% clean.
>
> **Treat every remaining `Prior.` line as an unscored guess, not evidence.** Six is a small sample
> and this is a calibration note, not a law — but a lane pre-registering a direction should derive
> it from published anchors, as the protocol already requires, and must not cite this map's prior as
> one of them.
>
> Where a *confound* is named the map has done better — but **not uniformly, and the exception is
> instructive.** F-4's and F-14's confound warnings were both real and both changed the design.
> **F-7's did not: it named the divine-name overlap (which turned out innocent, +51.0% → +51.7% on
> deletion) and missed the rhyme-shape confound that was fatal.** Confound predictions are therefore
> **2-for-3, not 2-for-2** — and the F-7 lane reports that it weighted the map's confound line as
> evidence *because this calibration block told it to*. Treat the confound line as a hypothesis to
> test, not a finding to inherit.
>
> ## 📊 SECTION-B SCORECARD — updated 2026-08-10. 13 of 20 resolved.
>
> | item | topic | resolved by | outcome |
> |:--|:--|:--|:--|
> | F-2 | scansion | H-NEW-2690 / 2730 | **already answered** — both halves refuted |
> | F-3 | conditionals | H-NEW-2630 | **already answered** — NULL |
> | F-4 | deixis | H-NEW-2960 + 3070 | **half already answered**; PASS, but as a *step* not a gradient |
> | F-5 | loanword donors | H-NEW-2700 / 3020 | **already answered** — NULL |
> | F-6 | derived-form profile | H-NEW-3130 | NULL, 0 of 9 cells |
> | F-7 | ṣīghat al-mubālagha | H-NEW-3150 | PASS as locked, **not believed** — control artefact |
> | F-8 | sajdah loci | H-NEW-2950 / 3030 | **already answered** — NULL, underpowered-severe |
> | F-10 | modality | H-NEW-2640 / 3040 | **already answered** — DIRECTIONAL |
> | F-11 | tafsīr disagreement | H-NEW-3160 | NULL, 0 of 3 |
> | F-12 | asbāb chronology | H-NEW-3120 | NULL — instrument truncated at surah 77 |
> | F-13 | reception weight | H-NEW-3000 | **already answered** — NULL |
> | F-14 | quantifier scope | H-NEW-3080 | **CONFIRMED** — on three *baʿḍ* tokens in two verses |
> | F-20 | kinship | H-NEW-3090 | NULL, effect reversed |
>
> **TEN of the sixteen were already answered before dispatch** — F-15 (H-NEW-2800, COMPLETE) and F-16
> (H-NEW-2870 / 2880 / 2890) were found by an automated check *after* this scorecard was first
> written, having been listed as unresolved.
>
> **RUN `scripts/check-frontier-staleness.sh` BEFORE DISPATCHING ANYTHING.** It greps `frontier_item:`
> tags across `findings/` and returns in about a second. It would have caught F-9 before three lanes
> and four of my own attempts were spent on it. Absence from its output is **not** proof an item is
> open — a finding can answer an item without carrying the tag — but presence is proof it is closed. Of all thirteen: **eight NULL-ish,
> three pass-ish, and the single substantive CONFIRMED (F-14) rests on a denominator of three
> tokens.**
>
> **Still unresolved (7):** F-1 waqf *(carries a data warning — the file it names is a 13-way
> outlier)* · F-9 rasm *(three lanes dispatched, none produced output)* · F-15 legal formulae
> *(check H-NEW-2800 first)* · F-16 pausal rhyme *(check H-NEW-2870 first)* · F-17 dependency depth
> *(needs EQTB; note the parser contamination)* · F-18 translation invariance *(check H-NEW-710
> first)* · F-19 Buckwalter phoneme.
>
> **What this scorecard is for.** Not to disparage the map — its *data* lines have been accurate
> almost everywhere, and its *confound* lines changed four designs for the better. It is to record
> that **"UNTOUCHED" was the least reliable field in the document**, wrong on seven of thirteen, and
> that the cost of trusting it was three lanes' full design effort before Step 0 was made mandatory.

> **BINDING RULE FOR ANY LANE DISPATCHED FROM THIS MAP:** grep `findings/` and
> `MASTER-FINDINGS-LEDGER.md` for your hypothesis **before designing the test**, and put the result
> in the pre-registration's forking-paths log as an explicit entry. H-NEW-3010's log had sixteen
> entries about instrument choices and not one asking whether the work already existed. The check
> that determines *whether to run at all* belongs before the checks about *how to run*.

# B. The 20 highest-value UNTOUCHED hypotheses

Ranked. Each carries: (1) the hypothesis, (2) **verified** on-disk data, (3) the obvious
confound, (4) classical anchor with on-disk verification status, (5) my honest prior.

Prior key: **CONFIRMED** / **NULL** / **CBM** (confirmed-but-meaningless — will pass but
reduce to length, frequency, or genre).

---

### F-1. Waqf marks encode a prosodic boundary system that predicts fāṣila strength
**Hypothesis.** The four Sajāwandī pause grades in the Uthmānī text (mīm = lāzim, jīm = jāʾiz, ṣlà = waṣl awlā, qlà = waqf awlā) are not editorial commentary but track a real syntactic-prosodic boundary hierarchy; grade should predict verse-final rhyme-class stability and clause-length distribution.
**Data (verified).** `quran-text/quran-full-tashkeel.json` contains: U+06DA jīm ×2,083; U+06D6 ṣlà ×1,651; U+06D7 qlà ×511; U+06D8 mīm ×21; U+06DC saktah ×8; U+06DB muʿānaqa ×6. I counted these directly. Rhyme classes already computed in H-NEW-2240.
**Confound.** The marks are a later editorial layer (Sajāwandī d. 560/1165), so any signal may just re-encode the *grammarian's* clause analysis rather than a property of the text. Mitigation: the interesting test is whether waqf grade adds anything **beyond** a syntactic parse — which is exactly why this pairs with the EQTB acquisition.
**Classical anchor.** al-Sajāwandī *ʿIlal al-wuqūf*; al-Suyūṭī *Itqān* nawʿ 27 (*fī al-waqf wa-l-ibtidāʾ*). `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf` **is on disk** — nawʿ-level verification is possible per the project's own MW-6 discipline.
**Prior.** CONFIRMED. Highest-EV item on this list because the instrument is free, in-corpus, and the project has been deleting it for months.

> **⚠ DATA WARNING ADDED 2026-08-09 — READ BEFORE RUNNING F-1.** The six counts above reproduce
> **exactly** against `quran-full-tashkeel.json`. But that file is the **only one of thirteen** in the
> repo giving those numbers. Twelve others — including `quran-min-tashkeel.json`,
> `quran-no-tashkeel.json` and all ten Tanzil alt-text files — agree with each other and disagree with
> it: ṣlà 1682, qlà 603, mīm 22, jīm 1972, muʿānaqa 12, **and lā (U+06D9) ×68 where full-tashkeel has
> ZERO**. jīm moves *up* by 111 while qlà moves *down* by 92, so this is a **re-grading, not a
> truncation**. Critically, **lā is the mark meaning *do not stop*** — the inventory's only
> prohibition grade — so running F-1 on the file named here would test a boundary hierarchy with its
> entire negative grade silently absent. Note too that `quran-no-tashkeel.json` carries MORE waqf
> marks than `quran-full-tashkeel.json`; "no tashkeel" strips vowels, not pause marks.
> Which inventory is correct is **not** settled. See [[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]] —
> the source file is now a rules-tuple element and F-1 must run under **both** inventories.

### F-2. Real quantitative scansion — the Quran's sabab/watid profile vs the 16 buḥūr
**Hypothesis.** Extracting actual syllable weight from the vocalised text and building the long/short sequence per verse will show the Quran occupies a *distinct region* of prosodic space rather than merely a distinct length distribution — and that saj‛-dense short surahs sit closer to *rajaz*/*sarīʿ* than long Medinan prose does.
**Data (verified).** `quran-text/quran-full-tashkeel.json` — 122,777 fatḥa, 46,069 kasra, 37,454 ḍamma, 22,678 shadda, 9,726 superscript alef, 3,988 sukūn, 37,147 U+06E1 (Uthmānī sukūn variant), plus tanwīn. That is everything needed for CV templating. Controls: 7 muʿallaqāt with known meters at `data/baseline-corpora/raw/muallaqa-*.txt` and 8 dīwāns.
**Confound.** Pausal forms. Classical scansion applies *waqf* rules at line-end (dropping final short vowels/tanwīn), so naive scansion of the fully-vocalised text will systematically mis-weight every verse-final syllable. Must implement pausal reduction — which is F-1's instrument, so the two are natural partners.
**Classical anchor.** al-Khalīl b. Aḥmad's ʿarūḍ; al-Bāqillānī *Iʿjāz al-Qurʾān* on "neither nathr nor shiʿr." Both already anchor H-NEW-48; al-Bāqillānī is mapped in `KNOWLEDGE-GRAPH.md` line 131. Al-Khalīl's *Kitāb al-ʿAyn* is cited but I did **not** find the primary text on disk.
**Prior.** CONFIRMED for "distinct region," NULL for any single-meter match. Would supersede H-NEW-48 rather than replicate it.

### F-3. Realis vs irrealis conditionals (*in* vs *law*) are register-coded
**Hypothesis.** *in* (open condition) concentrates in legal-Medinan; *law*/*lawlā* (counterfactual) concentrates in polemic and eschatological warning. This is the missing fourth column of cross-finding-028.
**Data (verified).** QAC POS:COND = 1,049 tokens in `data/morphology/quranic-corpus-morphology-0.4.txt`; lemma field distinguishes the particles. Register labels already locked in `findings/classical-sources/neuwirth-sinai-genre-labels.tsv` (read by 9 scripts).
**Confound.** Verse length and surah length — the legal register lives in long surahs. cross-finding-028's own `H-NEW-2530` confusion matrix shows legal is the hardest register (8/20). Must residualise on length, per MW-1.
**Classical anchor.** The *sharṭ* / *jazāʾ* apparatus in al-Zarkashī *al-Burhān*; `data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf` **is on disk**.
**Prior.** ~~CONFIRMED~~ — **RETIRED 2026-08-09. F-3 WAS ALREADY ANSWERED BY H-NEW-2630 ON THE VERY DAY THIS MAP WAS WRITTEN**
(`findings/phase-b-hypotheses/h-new-2630-conditional-register.md`, 2026-08-07, ledger §10.147), whose title
states the conclusion outright: *"Realis vs irrealis conditionals are NOT register-coded — the mood hypothesis
is rejected; conditional PRESENCE is the real signal."* This entry carried no pointer to it, and H-NEW-3010
duly re-derived it two days later. The two statistics are **the same statistic**: 2630's mood balance
`C = (n_R − n_I)/(n_R + n_I)` and 3010's irrealis share `n_I/(n_R + n_I)` satisfy `C = 1 − 2·share` exactly,
so both found legal-lowest and both returned NULL — on two independent register labellings and two null models.

**The real successor is NOT the mood question.** It is 2630's own open item: the **mood-blind PRESENCE**
question — does the mere presence of a conditional mark register, independent of which particle — tested under
a *stratified* length control. 2630 hit 20/20 legal recall on it post-hoc and asked for exactly this design;
H-NEW-3010 built the design and then re-tested mood with it instead.

**And the confound named in this entry is misidentified.** This entry says *"verse length and surah length — the
legal register lives in long surahs."* Measured: the surah-length half is nearly absent (Spearman ρ = +0.0719 on
verse count); the **verse-length** half is the entire confound (ρ = **+0.5467** on mean verse length). Median
words per verse: legal 19.36 against irrealis-register 4.58, a 4.2× gap, on identical median verse counts (38 vs 38).

### F-4. Spatial-deictic distance (hādhā vs dhālika) tracks eschatological reference
**Hypothesis.** Proximal demonstratives cluster on present/this-world referents, distal on the Hereafter and on scripture-as-object (`dhālika l-kitāb`), giving a measurable deictic gradient across the Nöldeke phases.
**Data (verified).** QAC POS:DEM = 1,059 tokens, POS:LOC = 669, POS:T = 1,166. Chronology from `data/revelation-order.csv` (read by 65 scripts).
**Confound.** `dhālika l-kitāb` at Q2:2 and the muqaṭṭaʿāt-opening formula will dominate the distal count. Must exclude or separately model the 29 opening formulae — the project already has that set locked (H-NEW-53/57).
**Classical anchor.** The classical debate over `dhālika` in Q2:2 (Ibn ʿAbbās, al-Ṭabarī). Verifiable — `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/2/2.json` exists on disk (I verified the directory has 286 verse files for surah 2).
**Prior.** CONFIRMED but at risk of CBM: the effect may be entirely carried by ~20 formulaic phrases.

### F-5. Loanword donor-language stratifies the Late-Meccan Pattern-B peak
**Hypothesis.** H-NEW-125 treats "loanwords" as one undifferentiated axis. Split by Jeffery's donor language: Syriac/Aramaic religious vocabulary should peak Late-Meccan with the scripture-announcement apparatus (OQ-17), while Persian administrative/material vocabulary should peak Medinan.
**Data (verified).** `data/loanwords/jeffery-1938-loanwords.tsv`, 506 rows, currently read by **1** script. `data/revelation-order.csv`.
**Confound.** Jeffery's etymologies are contested and the donor-language field is his judgement, not consensus. A negative result could be an artefact of his classification. Pre-register the etymology set from the TSV as-is and declare it a rules-tuple dependency (the project has explicit machinery for this — see `feedback_rules_tuple_bidirectional`).
**Classical anchor.** al-Suyūṭī *al-Muhadhdhab fīmā waqaʿa fī l-Qurʾān min al-muʿarrab* and *Itqān* nawʿ 38. Itqān **is on disk**; *al-Muhadhdhab* is **not**.
**Prior.** CONFIRMED-weak. Directly sharpens OQ-17, which the HANDOFF marks as live.

### F-6. Derived-form profile is a surah-level stylistic fingerprint
**Hypothesis.** The distribution over verb forms I–X is a per-surah signature that predicts genre independently of root vocabulary — Form IV (causative/declarative, 4,585 tokens) should mark divine-agency narrative, Form V/VI (reflexive/reciprocal) should mark community/legal discourse.
**Data (verified).** I counted directly from QAC: (IV) 4,585, (II) 1,615, (VIII) 1,161, (III) 497, (V) 466, (X) 459, (VI) 106, (VII) 63, (XII) 13, (IX) 11, (XI) 1.

> **⚠ DATA WARNING ADDED 2026-08-10 — THESE ARE NOT VERB COUNTS.** All eleven reproduce exactly, but
> only when counting **every POS carrying a form tag**: V 7,009 + N 1,778 + ADJ 170 + PN 20 = 8,977.
> The nominals are *maṣdars* and participles. The hypothesis says *"distribution over **verb** forms
> I–X"*, and verb-only (`POS:V`) the counts are **IV 3,487 · II 1,300 · VIII 963 · V 414 · X 369 ·
> III 334 · VI 77 · VII 51 · XII 9 · IX 5 · XI 0** — Form IV moves by **1,098 tokens (31%)**. Whether
> deverbal nominals are included is a **rules-tuple element**, not a detail.
>
> **And Form I does not exist in QAC.** Zero verbs carry an explicit `(I)` tag; **12,347 verbs are
> untagged — 64% of all 19,356 verbs.** "Forms I–X" therefore requires Form I to be *derived* as
> "verb with no form tag," which is an inference rather than a reading and must be declared.
>
> On verbs, **XI = 0** and IX (5), XII (9), VII (51) cannot carry a test. Say so rather than
> including them silently. Same shape as [[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]]: the counts are
> verified against one reading of the question and ambiguous across readings.
**Confound.** Root identity. Many roots are lexically restricted to one form, so a "form profile" may just be a coarse root profile. Must test with root held fixed — which is precisely the design H-NEW-2540 uses for II→V, so the method is already validated in-house.
**Classical anchor.** Sībawayhi/al-Zamakhsharī on `maʿānī al-abniya`. Neither primary text is on disk; `findings/classical-sources/99-names-wazn-classification.tsv` gives a wazn classification for the divine names only and is read by **0** scripts.
**Prior.** CONFIRMED but high CBM risk. Worth running because the confound test is the interesting half.

### F-7. Nominal-pattern (ṣīghat al-mubālagha) density marks the fāṣila slot
**Hypothesis.** The intensive patterns faʿʿāl / faʿūl / fāʿil that dominate the divine names are over-represented at verse-final position beyond what the hapax-slot mechanism (H-NEW-23) already explains.
**Data (verified).** QAC lemma + POS:ADJ (1,961) + PN (3,911); `findings/classical-sources/99-names-wazn-classification.tsv` supplies the classical wazn labels and is **currently unused by any script**.
**Confound.** Massive overlap with H-NEW-2070 / H-NEW-2300 (dual-name fāṣila seal) and with the hapax-final result. Must residualise on divine-name presence, or the test just rediscovers that verses end with divine names.
**Classical anchor.** al-Ghazālī *al-Maqṣad al-asnā* (attribute morphology) — `findings/classical-sources/ghazali-attribute-pairs.tsv` on disk, **unused**.
**Prior.** CBM. Listed because the instrument is free and the residualised version is genuinely open.

### F-8. Sajdah loci are prosodically marked
**Hypothesis.** The 15 in-text sajdah glyphs (U+06E9) sit at verses that are independently extreme on imperative density and second-person address — i.e. the prostration points are *textually* signalled, not only ritually assigned.
**Data (verified).** I counted 15 × U+06E9 in `quran-text/quran-full-tashkeel.json`. Prior sajdah work (H-NEW-1330 whole-surah NULL, H-NEW-1510 pericope PASS) used a **manually supplied verse list**, not the in-corpus glyph.
**Confound.** n=15. Any test is underpowered; the honest framing is an exact permutation over candidate verses, not an asymptotic test.
**Classical anchor.** al-Suyūṭī, *al-Itqān*, **nawʿ 35** (*fī ādāb tilāwatihi wa-tālīhi*), V01 p. 380 — verified in the Arabic at `raw/suyuti-itqan.openiti.raw.txt` line 6783. **CORRECTED 2026-08-09:** this entry previously read "the 14 vs 15 dispute (Ḥanafī vs Shāfiʿī; Q 38:24 and Q 22:77)", which is the textbook summary and is wrong on three points. al-Suyūṭī — himself a Shāfiʿī — gives **fourteen**; Q 22:77 is not contested (he writes *wa-fī l-Ḥajji sajdatān*); and Q 38:24 is a distinction of **degree**, excluded from the *ʿazāʾim* while prostration there remains *mustaḥabba*. The muṣḥaf's 15 glyphs are the **union** of the competing counts, not either one. The English *Itqān* PDF is abridged at this passage — a study searching only it would conclude he is silent. See [[h-new-3030-sajdah-glyph]] §2.3.
**Prior.** NULL, most likely — but a clean NULL here retires a live ambiguity and the count discrepancy itself (glyph says 15) is worth documenting.

### F-9. The rasm/imlāʾ divergence set is non-randomly distributed
**Hypothesis.** Words whose Uthmānī spelling differs from standard orthography (صلوة, ٱلرحمن without alif, أولئك with otiose wāw) cluster in specific registers or positions rather than being scattered.
**Data (verified).** Both spellings are on disk and alignable: `data/alt-text/quran-uthmani-txt.txt` (**read by 0 scripts**) vs `data/alt-text/quran-simple-txt.txt`; also `data/alt-text/quran-uthmani-consonantal.json` (3 scripts).
**Confound.** Tanzil's "simple" text is itself a normalisation with its own conventions; the diff will contain a large tail of purely systematic transformations. Needs a hand-curated divergence typology before any counting.
**Classical anchor.** al-Dānī *al-Muqniʿ fī rasm maṣāḥif al-amṣār*; Abū Dāwūd *Mukhtaṣar al-tabyīn*. **Neither on disk** — `findings/classical-sources/dani-23-site-supplement.tsv` is al-Dānī's *al-Bayān fī ʿadd āy*, a verse-counting work, not the rasm treatise. Do not cite it as an orthography anchor.
**Prior.** CONFIRMED-descriptive. Feeds OQ-9 (pre-iʿjām), which is entirely open.

### F-10. Modality (jussive/subjunctive + certainty particles) separates command from prediction
**Hypothesis.** The mood system distinguishes *deontic* (legal command, prohibition) from *epistemic/alethic* (eschatological certainty) contexts, and this separation is orthogonal to the function-word axis that cross-finding-028 already uses.
**Data (verified).** QAC `MOOD:JUS` 1,418, `MOOD:SUBJ` 1,330, POS:PRO 332, POS:CERT 414, POS:FUT 161, POS:EMPH 1,244.
**Confound.** Jussive is heavily driven by *lam* + past-negation, a purely syntactic trigger with no modal content. Must split *lam*-jussive from imperative-jussive from conditional-jussive.
**Classical anchor.** The *ṭalab* / *khabar* division in balāgha; al-Sakkākī *Miftāḥ al-ʿulūm* is in the KNOWLEDGE-GRAPH anchor map (line 137) but I did **not** find the text on disk.
**Prior.** CONFIRMED. Genuinely orthogonal to what has been done, and it is a natural fifth pillar for cross-finding-028.

### F-11. Twelve tafsīr traditions disagree systematically — and the disagreement is measurable
**Hypothesis.** Per-verse commentary *length* across the 12 on-disk tafsīr editions defines a "contested verse" score; contested verses should be enriched for the project's already-identified structural outliers (H-NEW-590 outlier spectrum, the celebrated-verse set).
**Data (verified).** `data/literature/classical-tafsir/spa5k-tafsir-api/` holds **12 editions** (8 Arabic, 4 English) each with a per-verse JSON file — 286 files for surah 2, 227 for surah 26, 206 for surah 7, etc. This is on the order of 75,000 files. **Exactly one script reads it**: `scripts/Q058_F_03_najwa_abrogation.py`.
**Confound.** Commentary length tracks verse length and verse *difficulty* in the mundane sense (rare words, legal detail), not structural interest. Must residualise on verse length and hapax count.
**Classical anchor.** This *is* the classical corpus — al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Baghawī, al-Jalālayn, Ibn ʿAbbās, al-Wāsiṭ, al-Saddī, Tanwīr al-Miqbās, al-Muyassar, al-Wāḥidī's *Asbāb*, Maʿārif.
**Prior.** CONFIRMED, and the highest-leverage *unused asset* in the repository. Also converts `feedback_intelligence_layer` from an aspiration into a measurement.

### F-12. Asbāb al-nuzūl coverage is a chronology instrument
**Hypothesis.** al-Wāḥidī's occasions-of-revelation coverage (which verses have a sabab at all) is an independent chronology signal that can be cross-validated against Nöldeke and against the project's own H-NEW-267 Hijra lexical frontier.
**Data (verified).** `data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/` — per-verse coverage, read by **0** scripts (the one spa5k reader hits al-Ṭabarī). `asbab-nuzul.md` exists in phase-b but is a prose survey.
**Confound.** Sabab coverage is strongly biased toward Medinan legal material because that is what the genre records. That bias *is* the signal, but it means the test cannot claim independence from the Meccan/Medinan label — it must be run *within* phase.
**Classical anchor.** al-Wāḥidī *Asbāb al-nuzūl*; al-Suyūṭī *Lubāb al-nuqūl*. Wāḥidī is on disk in translation.
**Prior.** CONFIRMED but partly CBM. Its real value is as a covariate for other tests.

### F-13. The 9-book hadith corpus gives a *reception-weight* per verse
**Hypothesis.** Number of distinct hadith citations per verse across the nine canonical books is a measure of liturgical/legal salience that is independent of every structural axis the project has built — and the residual (structurally extreme but rarely cited, or heavily cited but structurally ordinary) is where the interesting verses live.
**Data (verified).** `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` plus per-collection dirs (`bukhari`, `muslim`, `tirmidhi`, `abu-dawud`, `nasai`, `ibn-majah`). Read by 4 per-surah scripts only, all single-surah lookups.
**Confound.** Citation counts are dominated by al-Fātiḥa, āyat al-kursī, and the muʿawwidhāt — a handful of ritual texts. Rank-based statistics only; no means.
**Classical anchor.** The *faḍāʾil al-Qurʾān* genre; already partially engaged (H-NEW-1780 sahihayn-vs-sunan, H-NEW-860 hadith architectural alignment).
**Prior.** CONFIRMED-descriptive, high interest either way.

### F-14. Quantifier scope marks the universalism/particularism divide
**Hypothesis.** *kull* (universal) vs *baʿḍ* / *min* (partitive) distribution separates the ethical-universalist register from the community-legal register, giving an independent handle on `ethical-universalism.md`.
**Data (verified).** QAC LEM field; no new data needed.
**Confound.** *kull* is heavily formulaic (`kull shayʾ qadīr`, `kull nafs dhāʾiqat al-mawt`). Formula-exclusion list must be pre-registered.
**Classical anchor.** The uṣūl debate on `ʿumūm` and `khuṣūṣ` (al-Shāfiʿī *Risāla*, al-Ghazālī *Mustaṣfā*). **Neither on disk.** Report as an unverified anchor.
**Prior.** CBM — likely dominated by the formulae.

### F-15. Legal-formula frames are a closed inventory with positional structure
**Hypothesis.** A small set of legal frames (`kutiba ʿalaykum`, `ḥurrimat ʿalaykum`, `uḥilla lakum`, `fa-man lam yajid`, `wa-lakum fī … ḥayāt`) accounts for most legal-register verse onsets, and they occupy characteristic positions within their surahs.
**Data (verified).** `quran-text/quran-no-tashkeel.json` (the project's standard primary, 269 script references) + QAC.
**Confound.** Frame list selection is post-hoc unless drawn from an independent source. Draw it from al-Qurṭubī's *aḥkām* headings, which are on disk (`spa5k-tafsir-api/ar-tafseer-al-qurtubi/`), and lock it before counting.
**Classical anchor.** al-Qurṭubī *al-Jāmiʿ li-aḥkām al-Qurʾān*; al-Jaṣṣāṣ *Aḥkām al-Qurʾān*. Qurṭubī on disk; Jaṣṣāṣ not.
**Prior.** CONFIRMED-descriptive. Fills the one genuinely empty cell in cross-finding-028's three-register table.

### F-16. Pausal-form rhyme: the fāṣila is defined at the *pausal* phonology, not the citation form
**Hypothesis.** Rhyme classes computed on pausal forms (final short vowel and tanwīn dropped, tāʾ marbūṭa → hāʾ) will be markedly more homogeneous than the H-NEW-2240 taxonomy computed on written forms — and the residual mismatches will localise to specific surahs.
**Data (verified).** `quran-text/quran-full-tashkeel.json` + the existing H-NEW-2240 result to diff against.
**Confound.** This is close to a definitional restatement — "rhyme looks better under the rules reciters actually use." The finding is only interesting as a *magnitude* and as a localisation of residuals.
**Classical anchor.** Classical `waqf` phonology; Ibn al-Jazarī *al-Nashr*. **Not on disk.**
**Prior.** CONFIRMED but partly CBM. Worth doing because it is a correctness fix to a landed result, not only a new claim.

### F-17. Dependency depth predicts register (requires EQTB acquisition)
**Hypothesis.** Mean dependency depth and mean arc length per verse separate the three registers of cross-finding-028 and correlate with the compression scores of the OQ-20 family.
**Data.** **NOT on disk.** `data/syntax/UD-QURAN-SOURCE.md` gives the acquisition recipe, SHA-256 checksums, and notes `Quranic.csv` is UTF-16 TSV despite the extension. H-NEW-2540 needs the same file, so acquisition cost is shared.
**Confound.** EQTB annotation accuracy is flagged in the H-NEW-2540 pre-reg itself as "the material annotation limit." Any result inherits parser error.
**Classical anchor.** al-Jurjānī *Dalāʾil al-iʿjāz* on `naẓm` — and the project already has a `jurjani_predicted_asyndeton_tier` bridge (used in H-NEW-127.6/127.7). Note that bridge **failed** the phase-aware control (p=0.0945), so this would be a second, syntactically grounded attempt at the same anchor.
**Prior.** CONFIRMED. This is the single biggest structural axis the project cannot currently see.

### F-18. Ten translations give a translation-invariance test that is actually powered
**Hypothesis.** OQ-14 (translation-invariance) has never been run. Verse-twin structure computed independently in 10 languages will show which twin pairs are surface-Arabic artefacts and which are meaning-level.
**Data (verified).** `data/alt-text/risan-quran-json/dist/` contains `quran_en.json`, `quran_ur.json`, `quran_tr.json`, `quran_fr.json`, `quran_es.json`, `quran_id.json`, `quran_ru.json`, `quran_bn.json`, `quran_zh.json`, `quran_sv.json`, plus `quran_transliteration.json`. **Zero scripts read any of them.** Also `data/alt-text/risan-quran-json/dist/verses/` holds 6,236 per-verse files. `data/translations/en.sahih.txt` is read by 3 scripts.
**Confound.** Translations are not independent — most modern renderings are influenced by a small number of predecessors, and several of these are relay translations. Treat the 10 as a correlated family, not 10 independent draws; report a single pooled statistic.
**Classical anchor.** None applicable; this is a modern methodological question. NM-41 in `HANDOFF/03-NEXT-MOVES.md` gives a pre-reg seed (≥30% top-50 overlap = PASS) that can be adopted almost verbatim.
**Prior.** PARTIAL is the honest guess — I expect 15–30%, landing in NM-41's own "PARTIAL" band, which would be an informative result.

### F-19. Buckwalter transliteration enables a phoneme-level analysis that grapheme work cannot reach
**Hypothesis.** The project's phonology work (H-NEW-165 etc.) is built on *graphemes* with a hand-built feature codebook. A transliteration-based phonemic representation would distinguish long/short vowels and gemination that the grapheme layer collapses, and should improve or break the muqaṭṭaʿāt singleton ceiling that OQ-1 leaves open at 8/10.
**Data (verified).** `quran-text/quran-transliteration.json` — 114 surahs, verse-level Buckwalter-style romanisation (I read the Q1 sample). **Read by 0 scripts.** Note it is a *loose* romanisation (`alrrahmani`, `naAAbudu`), so it must be validated against `quran-full-tashkeel.json` before use.
**Confound.** If the romanisation is derived from the same vocalised text, this adds no information — it is a re-encoding. Must verify independence, and if it is derived, use the tashkeel directly instead.
**Classical anchor.** Ibn Jinnī *Sirr ṣināʿat al-iʿrāb* — already the anchor for H-NEW-165's ṣifāt layer.
**Prior.** NULL for "improves OQ-1" (H-NEW-252 showed the phonological axis saturates), CONFIRMED for "reveals collapsed distinctions." Ranked here rather than higher because of the derivation risk.

### F-20. Kinship terms encode a lineage-vs-covenant contrast
**Hypothesis.** Biological kinship terms (*walad*, *raḥim*, *nasab*) and affiliative terms (*ikhwa*, *awliyāʾ*, *mawlā*) are in complementary distribution across Meccan/Medinan, tracking the replacement of tribal by confessional affiliation.
**Data (verified).** `kinship-vocabulary.md` already has the inventory (its own frontmatter lists its dependencies as QAC + `quran-min-tashkeel.json`); `data/revelation-order.csv` for phase.
**Confound.** The Medinan surahs are longer and legally dense, so any affiliative-term rise may be a legal-register effect. Must run within-register, using the cross-finding-028 labels.
**Classical anchor.** The *muʾākhāt* (brothering) tradition; `sira-ibn-hisham.txt` is at `data/baseline-corpora/raw/` (read by 2 scripts as a *corpus baseline*, never as a historical source).
**Prior.** CONFIRMED but CBM-leaning — it may simply restate the Hijra, which H-NEW-267 already established at AUC 1.000.

**Ranking rationale.** F-1, F-2, F-11, F-17 are the four I would fund first: each opens a *layer* rather than a single claim, and three of the four need no new data. F-17 is the only one gated on a download.

---

# C. Contradiction and staleness audit

This is the adversarial section. Each item names a file and, where possible, a line.

### C-1. **Four duplicate `cross-finding` IDs — and all four collide on the project's four standing laws**

> **RESOLVED + PARTIALLY CORRECTED 2026-08-07.** C-1 is now actioned in
> `findings/CROSS-FINDING-INDEX.md` (authoritative disambiguation table + handle convention),
> and the wrong pointers are fixed in place. **Two claims in the original C-1 below were wrong
> and are withdrawn — see the "Corrections" note at the end of this item.** The count is
> **five** colliding IDs (023, 025, 026, 027, 028) across **eleven** files, not four; and the
> recommended fix has changed from renumbering to additive disambiguation.

Two directories independently mint `cross-finding-0NN` IDs, and their ranges overlap:

| ID | `findings/phase-b-hypotheses/` | `findings/cross-finding/` |
|---|---|---|
| 025 | `cross-finding-025-formal-scale-of-aggregation-law.md` (2026-05-09, pericope-flip law) | `cross-finding-025-multi-axis-architecture.md` (2026-04-28, 5-factor regression synthesis) |
| 026 | `cross-finding-026-formal-cohesion-vs-chiasmus-bifurcation.md` (2026-05-29) | `cross-finding-026-iʿjāz-architecture.md` (2026-04-28) |
| 027 | `cross-finding-027-formal-eponymy-independence-law.md` (2026-05-30) | `cross-finding-027-ijaz-al-takrir.md` (2026-04-28, **NULL on pre-reg**) |
| 028 | `cross-finding-028-formal-register-coded-discourse-grammar.md` (2026-05-30) | `cross-finding-028-liturgical-pair-fr.md` (2026-05-07) |

These are not filename near-misses. I read the frontmatter of all eight: each carries a bare
`id: cross-finding-0NN`. **Every unqualified prose reference to "cross-finding-025/026/027/028"
in the repository is ambiguous.** Also affected: `cross-finding-010` and `cross-finding-012`
each have two files inside phase-b-hypotheses alone (`-prereg` variants aside — I excluded those),
and `cross-finding-023` exists as both `cross-finding-023-causal-generative-closure.md` and
`cross-finding-023-oq15-causal-generative-closure.md`.

**Live damage.** `KNOWLEDGE-GRAPH.md:217` reads "4-cell typology (cross-finding-026 §13 amendment,
2026-04-28)" and `KNOWLEDGE-GRAPH.md:222` reads "*(5th-cell candidate, queued as cross-finding-027)*".
Both point at the *2026-04-28* series. A reader following those pointers today lands on the
cohesion/chiasmus law and the eponymy law — completely different findings. The KNOWLEDGE-GRAPH
has not been updated since the second series was minted.

**Recommended fix:** re-mint the 2026-05-29/30 series under a distinct prefix (e.g. `LAW-01..04`)
and add a redirect table, or renumber the older series. Do not leave both.

#### Corrections to C-1 (2026-08-07)

Three amendments, all from re-verification during the fix pass:

1. **`cross-finding-010` and `cross-finding-012` are NOT collisions — claim withdrawn.** The
   counting command did not exclude pre-registration files, so it read each prereg/result pair
   as a duplicate. A prereg is *supposed* to share its result's `id:`. Verified:
   `cross-finding-010-extended-network-prereg.md` (`status: PRE-REGISTERED 2026-04-17`) pairs
   with `cross-finding-010-extended-network.md` (`status: MIXED`); same for 012. The genuine
   collisions are **023, 025, 026, 027, 028**.
2. **`cross-finding-025` has three claimants, not two** — `cf-025-multiaxis` (2026-04-28),
   `cf-025-marker` (2026-05-09 PRELIMINARY), and `cf-025-formal` (2026-05-09 FORMAL).
   A fourth, never-minted claimant exists for **027**: a Medinan-ṭiwāl cluster proposed at
   `findings/phase-b-hypotheses/h-new-560-meccan-tiwal.md:70` and `MASTER-FINDINGS-LEDGER.md:1428`.
3. **The "Live damage" paragraph named the wrong lines.** `KNOWLEDGE-GRAPH.md:217` carries the
   date "2026-04-28" inline and is therefore unambiguous in context — calling it actively wrong
   was too strong. The genuinely wrong pointers were lines **187, 223, 278 and 280**, which
   described `cf-027-takrīr` as "in flight" / "queued" for a test that had already landed
   FALSIFIED on 2026-04-28. Those four are now corrected, along with
   `MASTER-FINDINGS-LEDGER.md:1667` and a dead path at
   `cross-finding-025-formal-scale-of-aggregation-law.md:75`.

**Superseded recommendation.** Renumbering was rejected: hundreds of cross-references and the
whole ledger point at current paths, and renumbering would rewrite the record of what was
minted when. The adopted fix is additive — an index, a handle convention built on the
`finding_id: cross-finding-0NN-formal` qualifier the four law files *already* carry, and
in-place correction of only the pointers that assert something false.

### C-2. **cross-finding-025 (the formal law) has not absorbed cross-finding-026, which bounds it**

`cross-finding-025-formal-scale-of-aggregation-law.md` ends (last section, "Update 2026-05-10")
with: *"the pericope-flip law stands at corpus-wide law strength across narrative / liturgical /
discourse / liturgical-opener / orthographic-opener marker classes (5/5)"* and *"The next
falsification-target is the first NULL/NULL pair."*

Since then: `MASTER-FINDINGS-LEDGER.md:6136` (§10.81, 2026-05-29) added ring-composition as a
**6th flip**, and `cross-finding-026-formal-cohesion-vs-chiasmus-bifurcation.md` (2026-05-29) then
**split the law**, showing the ring arm does **not** hold (H-NEW-2220: 0/6541 windows survive
Bonferroni; corpus anti-chiastic). Neither the 6th-flip addition nor the 026 bound appears anywhere
in the 025 file. Anyone reading 025 standalone — which its "FORMAL CODIFICATION" status invites —
will believe the law covers positional ring structure. It does not.

### C-3. **cross-finding-027's headline number is stale by one cell**

`cross-finding-027-formal-eponymy-independence-law.md:14` and `:23` both state
**"47/89 eponymous surahs NOT rank-1 (52.8%)"**.

`MASTER-FINDINGS-LEDGER.md:6385` (§10.112, 2026-05-30) states: *"CORRECTS the H-NEW-1820 summary
list which wrongly placed Q98 in the rank-1 set; Q98 moves to the 47/89→48/89 non-rank-1 majority."*
`surahs/Q098-al-bayyina/00-overview.md:51` says the same and `:114` repeats it.

The correct figure is **48/89 (53.9%)**. It is wrong in at least six places:
- `cross-finding-027-formal-eponymy-independence-law.md:14, :23, :26`
- `h-new-1820-title-density-independence-formal.md:3, :10, :29, :76, :86` — **and line 54 of that
  file still lists Q 98 al-Bayyina among the 42 rank-1 surahs**, the exact cell Q098-F-01 falsified.
  The file carries no correction note.
- `MASTER-FINDINGS-LEDGER.md:4424, :4450, :5502, :5521`

The direction of the error is favourable (it strengthens the law), which is precisely why it has
gone uncorrected. It is still an uncorrected error in a FORMAL law's stated evidence.

### C-4. **cross-finding-027 rests on n=5 for its "stronger pillar"**

`cross-finding-027-formal-eponymy-independence-law.md:26`: *"The five testable cycles (Nūḥ Q71 rank
5/6, Ibrāhīm Q14 5/6, Hūd Q11 3/5, Maryam Q19 4/5, Yūnus Q10 2/4) span the full eligible population
— this is a law over the eligible set, not a sample."*

Two problems. (a) "0/5" carries a lot of the law's rhetorical weight (`:26` calls it *the stronger
pillar* over 52.8%), but the confirmatory Arm C is a uniform-rank null over five observations; the
finding file itself notes *"0/5 rank-1 vs ~1/5 expected"* (`h-new-2430-eponymous-cycle-centrality.md:83`).
(b) The "law over the eligible set" framing means the claim cannot generalise beyond these five
cycles — but the law's stated form ("**A** surah's name predicts neither…") reads as universal.
This is the clearest instance of "a law worded more broadly than its anchors support."

Additionally, `h-new-2430-eponymous-cycle-centrality.md:88+` documents that this law **falsified** an
earlier project claim (the "core-episode-carrier = hub" mechanism from §10.119/§10.120). I did not
check whether those two ledger sections were updated in place — a follow-up should.

### C-5. **cross-finding-028's law statement outruns its own confusion matrix**

The law states each of the three registers *"carry a distinct, mutually-distinguishing signature."*
`h-new-2530-register-grammar.md:100` reports: *"Legal-Medinan is the hardest (8/20): 12 of its 20
surahs are misclassified."* Line 78 reports the *idhā*-cascade feature has only **5 host surahs
corpus-wide** and is *"NOT significant alone (sparse)"* at p=0.374. The 76.9% headline is against a
44% majority baseline on N=91.

To the finding file's credit, `:106-108` calls this *"an honest qualification of the joint law, not
a defeat of it."* But that qualification did **not** propagate into the formal law file — which
presents the three-column register table with no accuracy caveat.

### C-6. **OQ-2 cites a file that does not exist, and merges two different test cells**

`HANDOFF/05-OPEN-QUESTIONS.md:59` marks OQ-2 **ANSWERED** and cites
`findings/phase-b-hypotheses/h-new-168-q16-25-concentrator-mode.md`.
That file **does not exist**. `ls findings/phase-b-hypotheses/ | grep 168` returns only
`h-new-168-q16-q25-dispersion.md` and its prereg.

The substance survives — I opened the real file and its Cell C is *"mean pairwise Jaccard = 0.319 vs
null 0.135 ± 0.039; p ≈ 0.0001 — 2.4× more stems"* (`h-new-168-q16-q25-dispersion.md:28`). But OQ-2
reports it as *"pairwise Jaccard = 2.4× random (p ~ 0.0001); permutation p_perm = 0.0006"*, gluing
Cell C's Jaccard to **Cell B's dispersion p-value** (`:27`) as if they were one statistic. They are
different cells with different observables.

Relatedly: `HONEST-LIMITS-LEDGER.md:1015` (§27f) still carries *"Q 16-25 shadow-cluster thesis —
NULL-BROKEN (H-NEW-94, 2026-04-17)"*. OQ-2 says H-NEW-168 *"supersedes the NULL-BROKEN verdict."*
I did not find a supersession note in §27f itself.

### C-7. **Fifteen duplicated section numbers in MASTER-FINDINGS-LEDGER.md**

`grep -oE '^## §10\.[0-9]+' | sort | uniq -c | awk '$1>1'` returns:

```
2 §10.55   2 §10.56   4 §10.57   2 §10.58   2 §10.63   2 §10.66
2 §10.68   3 §10.70   2 §10.71   2 §10.72   2 §10.73   2 §10.76
2 §10.78   2 §10.79   3 §10.80
```

§10.57 is used **four times** (H-NEW-1570, H-NEW-1550, H-NEW-1520, H-NEW-1710). §10.70 and §10.80
three times each. Every cross-reference of the form "see §10.57" in this project is ambiguous, and
§10.80 is cited by `HONEST-LIMITS`-adjacent prose (e.g. §10.80.3 is referenced as "closed by
H-NEW-2230" at `MASTER-FINDINGS-LEDGER.md:6198`) without disambiguation.

### C-8. **H-NEW-290's title carries the wrong wikilink**

`h-new-290-q42-block-vs-phonology-tension.md` — its `# ` heading renders as
`[[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] — Q 42 HMASQ: BLOCK-DOMINANCE resolves
the 5-way phonological miss`. The YAML frontmatter correctly says `id: H-NEW-290`. This is a
`scripts/linkify_findings.py` artefact (that script is named as the generator in
`findings/ORPHAN-REFERENCES.md:3`). Anyone using Obsidian graph navigation will see H-NEW-290's
content filed under H-NEW-282. Worth a sweep for other instances — I found this one incidentally,
so there are likely more.

### C-9. **The orphan-reference backlog is large and includes load-bearing IDs**

`findings/ORPHAN-REFERENCES.md` (generated 2026-04-28) lists references with **no matching file**.
The top of the table: `cross-finding-008` (123 mentions), `H-NEW-35` (75), `H-NEW-59` (66),
`H-NEW-1` (61), `H-NEW-23` (58), `H-NEW-34` (57), `cross-finding-006` (50).

`cross-finding-008` is the muqaṭṭaʿāt book-reference anchor cited throughout OQ-3 and OQ-6.
`H-NEW-23` is the hapax-slot mechanism cited in `MASTER-FINDINGS-LEDGER.md:104` as *"strongest
statistical signal in the project."* Neither has a file of its own. The report itself offers three
benign explanations (`:16-24`), and some are certainly right — but a project whose single strongest
claim has no dedicated findings file is carrying real citation risk. This report is also four
months stale (2026-04-28) and predates everything from Wave M onward.

### C-10. **H-NEW-48's meter result is a length test wearing a prosody label**

`h-new-48-poetic-meter.md` verdict: *"the first published quantitative confirmation of al-Bāqillānī's
classical claim that the Quran is 'neither prose (nathr) nor poetry (shiʿr)'."* The method (same
file, §"Quran vs each of 16 meters") is: model each baḥr as a Gaussian on **letters per bayt**, then
two-sample KS against Quran **verse letter-counts**. The letters↔syllables bridge is a single
constant, `LETTERS_PER_SYLLABLE = 1.6`, introduced in amendment 48-A.

This tests whether Quranic verses are the same *length* as lines of classical verse. It cannot
distinguish a text that is metrical-but-different-length from one that is non-metrical. The verdict
line should be narrowed, or F-2 should be run. The finding is not wrong; the label is wider than the
instrument.

### C-11. **H-NEW-41's null was never repaired**

`h-new-41-root-combinatorial-saturation.md` frontmatter: `verdict: EXPLORATORY (partial-positive-control
downgrade)`, amendment `41-B. SHA-256 lock of classical reference. Lane and Wehr not on disk.`
`HANDOFF/03-NEXT-MOVES.md:100` (NM-7) queues the repair and specifies the acquisition (Lane's Lexicon
root index + Hans Wehr 4th ed.). Neither is on disk today — I checked `data/literature/` subdirectories
and found no lexicon. NM-7 has been open since the Wave-2 queue and remains blocked on the same
acquisition. Its one surviving signal (guttural-coronal C2-C3 under-representation, z=−6.94) is
therefore still uninterpretable.

### C-12. **H-NEW-2540's dependency data is not on disk at the time of writing**

`findings/phase-b-hypotheses/scripts/h-new-2540.py` is untracked in `git status`, and
`prereg-h-new-2540-form-v-valency.md` states the test *"uses … the Extended Quranic Treebank (EQTB)
only for dependency relations."* `data/syntax/` contains only the manifest; the manifest itself says
`binary not committed`. Whoever runs 2540 must execute the curl/unzip block in
`data/syntax/UD-QURAN-SOURCE.md` first and verify the three SHA-256 values recorded there. Flagging
this because a run that silently falls back to QAC-only would violate the locked pre-reg.

---

# D. Data assets that exist but are UNUSED

Method: for each candidate path, `grep -rl <name> scripts/ findings/phase-b-hypotheses/scripts/`.
Count 0 = no script in either directory reads it. Where a `surahs/**/scripts/` file does read
something, I say so.

### D.1 The single biggest one: the waqf apparatus is present and systematically deleted

`quran-text/quran-full-tashkeel.json` carries the complete Sajāwandī pause system. Counts I made
directly from the file:

| Codepoint | Mark | Count |
|---|---|---:|
| U+06DA | ۚ jīm — *waqf jāʾiz* | 2,083 |
| U+06D6 | ۖ ṣlà — *al-waṣl awlā* | 1,651 |
| U+06D7 | ۗ qlà — *al-waqf awlā* | 511 |
| U+06D8 | ۘ mīm — *waqf lāzim* | 21 |
| U+06DC | ۜ sīn — *saktah* | 8 |
| U+06DB | ۛ three dots — *muʿānaqa* | 6 |
| U+06E9 | ۩ *sajdah* locus | 15 |
| U+06DE | ۞ *rub‛ al-ḥizb* | 199 |

**≈4,280 pause markers plus 214 division markers.** `grep -rlE '06[Dd][6-9ABCabc]' scripts/
findings/phase-b-hypotheses/scripts/` returns **39 scripts** — and in every case I inspected the
range appears inside a *stripping* regex. Representative:
`scripts/h_new_41_root_combinatorial.py:137` — `AR_DIACRITIC_RE = re.compile(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]')`; the trailing range swallows every waqf mark.
`findings/phase-b-hypotheses/scripts/h-new-2490.py:51-58` is even more explicit: it defines
`PAUSE = set(chr(c) for c in range(0x06D6, 0x06EE))` purely in order to remove it, with the comment
*"waqf/codex glyphs U+06D6-U+06ED -> STRIPPED."*

This is not an unused file. It is an unused *signal inside a heavily used file*, which is why it has
been invisible. It powers F-1, F-8, and (via pausal forms) F-2 and F-16.

### D.2 Files read by zero scripts in either script directory

**Text / corpus**
- `quran-text/quran-transliteration.json` — full Buckwalter-style romanisation, 114 surahs. (F-19)
- `quran-text/quran-flat-full-tashkeel.txt`
- `quran-text/quran-flat-min-tashkeel.txt`
- `data/alt-text/quran-uthmani-txt.txt`, `quran-uthmani-txt-2.txt`
- `data/alt-text/quran-uthmani-min-txt.txt`, `quran-uthmani-min-txt-2.txt` (F-9)
- `data/alt-text/risan-quran-json/dist/` — **10 language editions** (`quran_en/ur/tr/fr/es/id/ru/bn/zh/sv.json`)
  plus `quran_transliteration.json` plus `dist/verses/` (**6,236 per-verse files**). Zero reads. (F-18)

**Classical instrument tables** (all in `findings/classical-sources/`, all read by 0 scripts):
- `99-names-wazn-classification.tsv` — wazn + ṣīghat mubālagha + Ghazālī ṣifa classification (F-7)
- `99-names-ground-truth.tsv`
- `ghazali-attribute-pairs.tsv` (F-7)
- `kirmani-30-pair-tuples.tsv` — al-Kirmānī *mutashābih* pairs; NM-22 in `03-NEXT-MOVES.md:156`
  explicitly asks for cross-referencing against al-Kirmānī and this table has never been opened
- `mutlaq-muqayyad-pairs.tsv` — the uṣūl *muṭlaq/muqayyad* pairs
- `ibn-abi-l-isba-tasdir-catalog.tsv` — *tasdīr* (verse-final echo of verse-initial) catalog
- `dani-23-site-supplement.tsv` — al-Dānī *al-Bayān fī ʿadd āy*, 23-site conditional supplement to
  the AMEND-13 40-site list; header says `fires_when: AMEND-13 40-site primary passes` — I did not
  trace whether that gate ever fired
- `fresh-wave-3-classical-anchors.md`, `h-new-18-ext-kirmani-11-20.md`,
  `h-new-19-ext-classical-anchors.md`, `h-new-40-convergence-analysis.md`,
  `hashr-citation-chain-analysis.md`, `hashr-verification-memo.md`, `sub-c-rhetorical-rubric.md`

*(For contrast: `neuwirth-sinai-genre-labels.tsv` is read by 9 scripts and is the workhorse of the
whole OQ-20 line. The tables above are the same kind of instrument, unused.)*

**Derived baseline results** (`data/baseline-corpora/`, all 0 reads):
`test1-matching-pairs.csv`, `test2-concentration.csv`, `test3-div19.csv`, `test4-ring-scores.csv`,
`letter-z-tests.csv`, `letter-z-quran-vs-matched-bukhari.csv`, `baseline-stats.csv`,
`analysis-summary.json`, `rahma-114-test.json`. These are outputs of `data/baseline-corpora/analyze.py`
/ `analyze2.py` that no downstream test consumes.

**Morphology**
- `data/morphology/root-cooccurrence-graph.json` — 0 reads. (`surah-root-graph.json` gets 13,
  `root-stats.csv` gets 5, so the root graph is the odd one out.)

**Other**
- `data/INTEGRATION.md`, `data/h_new_40/` (directory is empty — `ls` returns nothing)
- `data/baseline-corpora/raw/diwan-amr-ibn-kulthum.txt` — 0 reads while the other seven dīwāns get 2 each

### D.3 Assets read once, i.e. effectively idle

- **`data/literature/classical-tafsir/spa5k-tafsir-api/`** — 12 tafsīr editions
  (`ar-tafsir-al-tabari`, `ar-tafseer-al-qurtubi`, `ar-tafsir-ibn-kathir`, `ar-tafsir-al-baghawi`,
  `ar-tafsir-al-wasit`, `ar-tafsir-muyassar`, `ar-tafseer-al-saddi`, `ar-tafseer-tanwir-al-miqbas`,
  `en-al-jalalayn`, `en-tafisr-ibn-kathir`, `en-tafsir-ibn-abbas`, `en-tafsir-maarif-ul-quran`,
  plus `en-asbab-al-nuzul-by-al-wahidi`), each with per-verse JSON across all 114 surahs — on the
  order of **75,000 files**. Read by exactly **one** script in the two script directories:
  `scripts/Q058_F_03_najwa_abrogation.py`. The al-Wāḥidī *Asbāb* edition is read by **zero**.
  This is the largest idle instrument in the repository. (F-11, F-12, F-15)
- **`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`** — read by 4 scripts, all
  single-surah lookups (`Q068_F_05`, `Q073_F_03`, `Q032_F_05`, `Q044_F_06`). No corpus-wide use. (F-13)
- **`data/loanwords/jeffery-1938-loanwords.tsv`** — 506 rows, 1 read. (F-5)
- **`data/translations/en.sahih.txt`** — 3 reads, all as an illustration layer; several catalog files
  note "English is illustrative, Arabic is load-bearing." Never used as a measurement. (F-18)

### D.4 Data the project *thinks* it has but does not

- **Extended Quranic Treebank / UD-Quran.** `data/syntax/` contains only `UD-QURAN-SOURCE.md`
  (`status: external reproducibility input; binary not committed`). No dependency data on disk.
  Blocks F-17 and gates the in-flight H-NEW-2540.
- **Lane's Lexicon / Hans Wehr root index.** Named as required by NM-7 (`03-NEXT-MOVES.md:100-103`)
  and by amendment 41-B. Not on disk. Blocks the H-NEW-41 repair (C-11).
- **al-Dānī *al-Muqniʿ*** (rasm). Not on disk; do not mistake `dani-23-site-supplement.tsv` for it.
- **No Biblical/Syriac text of any kind**, so the intertextuality axis has no comparison corpus —
  only Reynolds' commentary PDF.
- **No qirāʾāt data of any kind.**

---

# Appendix — orientation notes for whoever picks this up

- **Latest ledger entry** is `MASTER-FINDINGS-LEDGER.md` §10.138 (session consolidation, Waves M–R,
  2026-05-29/30). Highest H-NEW id with a landed finding is **2530**; **2540** is pre-registered and
  in flight; per the session's agent roster, **2550 / 2560 / 2570** are also live
  (nisf-al-ḥurūf, fāṣila clause-seal, lexical curriculum). Do not propose those.
- **Do not reopen**: within-pericope chiasmus / ring composition (cross-finding-026 closed it at
  three scales); emphatic sound-symbolism (H-NEW-2340 NULL, H-NEW-2370 NULL-REVERSED — retired at
  all scales); the OQ-16 scaffold-level answer (`05-OPEN-QUESTIONS.md:352` says so explicitly).
- **OQ-13 (sound-level) and OQ-14 (translation-invariance)** are the two open questions in the
  HANDOFF with the least follow-through. OQ-13 has been partly absorbed by the H-NEW-165 phonology
  line but its *recitation* half (waqf, tajwīd-rhythm, stress) is untouched — that is F-1/F-2/F-16.
  OQ-14 has never been run at all — that is F-18, and NM-41 already supplies a pre-reg seed.
- **File-count check**: `findings/phase-b-hypotheses/*.md` = 906 files (I counted). `scripts/*.py` = 484.
  `findings/phase-b-hypotheses/scripts/` = 73 entries. `surahs/` = 119 entries.
