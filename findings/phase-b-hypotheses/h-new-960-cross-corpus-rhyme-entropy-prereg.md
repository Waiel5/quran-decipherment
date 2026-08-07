---
id: H-NEW-960
title: "PRE-REG — Cross-corpus rhyme-letter Shannon-entropy distinctness: per-surah Quran rhyme-letter entropy vs matched-length pre-Islamic poetry blocks"
phase: B
status: PRE-REGISTERED (locked before observation)
date: 2026-05-07
specialist: cross-corpus-rhyme-specialist
parent_1: H-NEW-740 (cross-corpus iʿjāz al-fawāṣil composite distinct at p<10⁻¹⁰)
parent_2: H-NEW-700 (per-surah top-letter rhyme-dominance methodology)
parent_3: al-Bāqillānī *Iʿjāz al-Qurʾān*, *iʿjāz al-fawāṣil* axis
parent_4: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on al-fawāṣil (variety of qiṣār-mufaṣṣal rhyme endings)
seed: 20260507
n_perms: 10000
n_bootstrap: 10000
bonferroni_k: 4
bonferroni_family: H2-quartile-by-verse-length
alpha_bon: 0.0125
alpha_h1: 0.00001
verdict: PRE-REGISTERED
---

# H-NEW-960 — Cross-Corpus Rhyme Letter Shannon-Entropy Distinctness


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

## 1. Background and motivation

**H-NEW-740** (parent) confirmed cross-corpus distinctness of the Quran vs pre-Islamic monorhyme qaṣīda corpora on the *composite* (content × rhyme) axis: r_Quran = −0.86 vs r_pre-Islamic = −0.48 (full) / −0.35 (no-antara), with Fisher-z gap p < 10⁻¹⁰. The architectural anti-twin signature was vindicated.

**H-NEW-700** (parent) established per-surah rhyme-letter dominance — most surahs have a strongly dominant rāwī (top-letter fraction often > 0.7), with two regimes: long surahs unify on a single nūn-rhyme (al-fāṣila al-mursalah), short qiṣār-mufaṣṣal each pick a distinct letter at often 100% prevalence.

**What has NOT been tested**: whether the per-surah rhyme-letter Shannon entropy ALONE — stripped of any content-axis pairing — is statistically distinct between the Quran and pre-Islamic poetry. The composite distinctness in H-NEW-740 could in principle be carried by either the content axis OR the rhyme axis OR their joint interaction. **H-NEW-960 narrows to letter-only**: is the Quranic rhyme-letter distribution PER SURAH measurably more uniform (lower entropy) than matched-length blocks of pre-Islamic poetry, or not?

This is informative both ways:
- **If LOWER**: extends H-NEW-740 to the letter-axis alone — "Quran rhyme is more rāwī-uniform per unit than pre-Islamic poetry of equivalent length"
- **If EQUAL or HIGHER (NULL/REVERSED)**: residual finding — the cross-corpus distinctness in H-NEW-740 lives in the *composite* signal, not in the letter-axis alone. Pre-Islamic monorhyme qaṣīda is, after all, the canonical monorhyme genre; this might reasonably show poetry to be ≥ Quran in pure rhyme-uniformity.

## 2. Hypotheses (DIRECTION-LOCKED)

### H1 — Primary direction-locked test (one-sided, paired)
**Mean per-surah rhyme-letter Shannon entropy across all 114 surahs is LOWER (more rhyme-uniform) than the mean rhyme-letter entropy of matched-length pre-Islamic poetry blocks.**

- Per-surah-V Quranic surah is paired with closest-matched-length poetry block (V consecutive bayts).
- Test: Wilcoxon signed-rank, ONE-SIDED LOWER (Q < poetry).
- Pre-commit threshold: **p < 10⁻⁵** for high-strength claim.
- Direction: Q < poetry (LOWER ENTROPY = MORE UNIFORM in Q).

### H2 — Quartile robustness (Bonferroni-4, α_bon = 0.0125)
Verse-length quartiles:
- **VS** (very-short): V < 5 verses
- **S** (short): 5 ≤ V ≤ 10
- **M** (medium): 11 ≤ V ≤ 20
- **L** (long): V > 20

Direction-locked one-sided Wilcoxon at α_bon = 0.05/4 = 0.0125 in EACH non-empty quartile.
- 4/4 quartiles passing: H2 CONFIRMED (robust to length-stratification)
- 3/4: PARTIAL
- ≤ 2/4: H2 NULL (cross-corpus distinctness is length-confounded)

### H3 — Falsifier (NULL-of-equal-prominence)
If poetry has rhyme-entropy ≤ Quran (rhyme-uniformity-equal or rhyme-MORE-uniform), the Quran's rhyme is NOT distinct as a per-surah letter-axis genre signature.
- Verdict: **NULL — RHYME-LETTER-AXIS EQUAL OR FAVOR POETRY** (residual finding: composite-distinctness from H-NEW-740 lives in the joint, not the rhyme-letter axis alone)
- Documented with the same prominence as the positive verdict.

## 3. Verdict bands

| Band | Criterion |
|:--|:--|
| **HIGH-STRENGTH-CONFIRMS** | H1 p < 10⁻⁵ AND H2 4/4 quartiles pass at α_bon |
| **CONFIRMS** | H1 p < 10⁻⁵ AND H2 ≥ 3/4 quartiles pass at α_bon |
| **DIRECTIONAL-CONFIRMS** | H1 0.001 < p < 10⁻⁵ |
| **DIRECTION-LOCKED-NULL** | H1 p ≥ 0.05 in pre-committed direction |
| **NULL-RESIDUAL-LIVES-IN-COMPOSITE** | H1 reversed direction (poetry ≤ Quran) — residual finding |
| **NULL-DATA-GAP** | Poetry corpus insufficient (<30 blocks of matched length) |

## 4. Methodology

### 4.1 Rules-tuple (locked)

| Item | Quran | Pre-Islamic Poetry |
|:--|:--|:--|
| Tashkeel level | min-tashkeel (per H-NEW-700) | strip diacritics + variant-normalize (per H-NEW-740 parser) |
| Rhyme letter | last orthographic letter of verse, normalized to 28-letter alphabet | last orthographic letter of bayt-line, same normalization |
| Variant map | ى→ي, ة→ه, أ/إ/آ/ٱ→ا, ؤ→و, ئ→ي | same |
| Counting unit | verse = entry in `quran-min-tashkeel.json` verses[] | bayt-line filtered by `looks_like_bayt()` (H-NEW-740 heuristic) |
| Reading tradition | Hafs-Kufan | n/a (qaṣīda print conventions) |
| Basmala handling | counted-only-in-Q1 (Q1 has 7 verses including basmala by Hafs-Kufan; Q2-Q114 basmalas not enumerated as verses) | n/a |

### 4.2 Quran data

- Source: `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json`
- 114 surahs; for each surah s:
  - V_s = surah's total_verses
  - For each verse v in surah, extract last letter via `get_final_letter()` from H-NEW-740
  - Compute Shannon entropy H(Q_s) = − Σᵢ p_i log₂ p_i over the 28-letter distribution
  - p_i = (count of verses ending in letter i) / V_s (no Dirichlet smoothing — empirical)

### 4.3 Pre-Islamic poetry data

- Source: `/Users/grey/Downloads/quran/data/baseline-corpora/raw/`
- Files: 7 muʿallaqāt + 6 dīwāns (per H-NEW-740 manifest)
- Bayt-line extraction: `looks_like_bayt()` heuristic (≥6 Arabic words, ≥0.7 Arabic-char ratio, no prose markers; full code at `scripts/h_new_740_preislamic_poetry_control.py:126`)
- Concatenated sequential bayt-lines per qāfiya-section (preserves contiguity)

### 4.4 Matched-length sampling

For each Quranic surah of length V_s:
1. From the union of all available poetry sources, enumerate all candidate windows of EXACTLY V_s contiguous bayts WITHIN A SINGLE QĀFIYA-SECTION (preserves monorhyme integrity, mimics natural-poetic-unit).
2. If V_s > max-section-size in poetry corpus (e.g., V_s = 286 for Q2): use FALLBACK — closest-available-length window across the entire concatenated poetry-bayt-line stream (cross-section permitted, documented).
3. If multiple candidates available: sample 1 with seed-locked rng (seed 20260507) to provide ONE matched-length pair.
4. Compute Shannon entropy H(P_s) of the 28-letter distribution of the V_s bayts in that window.

**Note on V_s > poetry-section-cap**: The pre-Islamic corpus has limited section sizes (most ≤ 100 bayts; max-bayt-block ≈ 200-300 in long dīwāns). For long Quranic surahs (V_s > 200), the matched-length poetry block may have to span qāfiya-section boundaries OR multiple poets. **Pre-commit decision**: When V_s exceeds max-single-section size, sample V_s contiguous bayts across the entire concatenated bayt-line stream (effectively concatenating sources). This BIASES toward HIGHER entropy in poetry (multiple rāwīs spanned), which is the SAME direction as H1's prediction — so the inference is conservative.

### 4.5 Test statistics

**Primary (H1)**: Wilcoxon signed-rank, paired (H(Q_s), H(P_s)) over s=1..114. ONE-SIDED, alternative: H(Q_s) < H(P_s).

**Quartile (H2)**: Same Wilcoxon paired, restricted to surahs in each quartile (VS, S, M, L). Bonferroni α_bon = 0.0125 per cell.

**Bootstrap CI (10000 reps, seed 20260507)**: 
- Mean Q-entropy
- Mean P-entropy
- Mean paired Δ = H(Q) − H(P)
- 95% percentile CI on Δ

### 4.6 Data-gap protocol

**If poetry corpus yields < 30 valid blocks across the whole pipeline** (e.g., parser fails or matched-length unavailable for >40% of surahs), declare **NULL-DATA-GAP**, do not fabricate. Run the entropy on Q alone and report the absolute-value as a Q-only finding, flagging cross-corpus comparison as deferred.

### 4.7 Garden-of-forking-paths log

Pre-commit choices made BEFORE viewing data:
- Quartile cuts: V<5, 5-10, 11-20, V>20 (chosen from project's standard mufaṣṣal-tier boundaries; no entropy values examined)
- Pairing: closest-length poetry block; randomization within tied lengths via seed-locked rng
- Cross-section sampling permitted only when V_s > max-section size (otherwise within-section)
- Smoothing: NO Dirichlet smoothing on entropy (empirical Shannon)
- Logarithm base: log₂ (bits)
- Pre-commit p threshold for HIGH-STRENGTH: 10⁻⁵ (declared in body BEFORE observation)

## 5. Critical disclosures

1. **Cross-corpus tests are HIGH RISK**: poetry-corpus orthographic conventions, pre-tashkeel-removal artifacts, and shorter natural-line-blocks could confound. Direction-of-bias for V > poetry-section-max is documented (§4.4) and is conservatively in the SAME direction as H1.

2. **The composite-axis already passed in H-NEW-740**: this test narrows to letter-only. A NULL here does NOT retract H-NEW-740 — it RESIDUALIZES it (the composite-distinctness lives in joint structure, not letter-axis alone).

3. **Entropy ≠ top-letter dominance**: H-NEW-700 reports top-letter fraction. Shannon entropy is a richer measure that captures the SHAPE of the distribution, not just its mode. A surah at 70% top-letter has Shannon entropy ≈ 1.5 bits (with the rest spread); at 100% it has entropy 0; uniform-28 has log₂(28) ≈ 4.81 bits.

4. **Pre-Islamic qaṣīda is monorhyme by definition** — sections are nominally 100%-monorhyme. So poetry blocks that fall WITHIN a qāfiya-section will have very low entropy. The cross-corpus question becomes: does Q's natural per-surah rhyme-letter distribution match poetry's monorhyme convention, or is it lower (Q more uniform), or higher (Q more rhyme-diverse than monorhyme convention)?

5. **Direction prediction reasoning**: H-NEW-700's per-surah top-letter fraction across 114 surahs is highly variable — many short qiṣār-mufaṣṣal at 100% but many long surahs at 50-80%. Pre-Islamic qaṣīda is canonically 100%-monorhyme per qāfiya-section. The PRE-COMMITTED direction (Q < poetry, Q LOWER entropy) is therefore the LESS-OBVIOUS direction (suggesting Q is even MORE rhyme-uniform than poetry per matched length). Reverse direction (Q > poetry) is the more naive expectation given monorhyme convention. **Direction is locked at LOWER per the task brief; if the data reverses, this is a pre-commit violation, published as NULL with prominence.**

## 6. Outputs

- Pre-reg: this file
- Script: `/Users/grey/Downloads/quran/scripts/h_new_960_cross_corpus_rhyme_entropy.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-960.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-960-cross-corpus-rhyme-entropy.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-960-run-1.md`
- MASTER-FINDINGS-LEDGER update: insert after H-NEW-950

## 7. Replication / quality gates

- Pre-reg SHA computed and embedded in script
- Runtime SHA verification (fail-fast)
- Seed locked: 20260507
- N_PERMS = 10000 (bootstrap)
- Direction PRE-LOCKED at LOWER
- Bonferroni declared: k=4, α_bon=0.0125 (H2 family)
- Equal NULL prominence rule honored

*Bismillāhi al-Raḥmāni al-Raḥīm.*
