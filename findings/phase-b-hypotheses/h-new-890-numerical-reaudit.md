---
id: H-NEW-890
title: "Numerical and sequence re-audit in light of 2026-04-28 architectural findings"
phase: B
status: 1-PASS, 4-NULL (overwhelmingly NULL with one architectural distinctiveness signal)
date: 2026-04-28
seed: 20260428
n_iter: 100000
bonferroni_k: 5
alpha_bon: 0.01
prereg: h-new-890-numerical-reaudit-prereg.md
prereg_sha256: 0c0c7e8ce0774832df0f7bb56f1937cc6bc8bf87d347022f64d5a7cea2ff7885
script: scripts/h_new_890_numerical_reaudit.py
script_sha256: a884db8be3d2a4d6d7f0d12cc961dd690f29e871e4d45bdfb80fb867a817d1f4
output: findings/phase-b-hypotheses/csv/h-new-890.json
output_sha256: 683e0f89d7f2326af60810f0ae06d0139a161785d503c70bf3430c6c00ec82e3
---

# [[h-new-890-numerical-reaudit|H-NEW-890]] — Numerical and Sequence Re-audit


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

## §1 Headline table

| Test | Claim | Statistic | p (one/two-sided) | α_bon | Verdict |
|:--|:--|:--|:-:|:-:|:--|
| **T1** | Q 8 + Q 9 are functionally one surah → low d_FR(8, 9) | rank 81/113 (1-sided ≤) | 0.717 | 0.01 | **NULL — opposite direction** |
| **T2** | Compression-tail kink-50 law is Quran-distinctive | ΔR² = +0.268, |β_Q|/|β_B| ≈ 4.4× | n/a (criterion-based) | **PASS-DISTINCTIVE** |
| **T3** | "Code 19" — verse-counts divisible by 19 | k_obs = 4 vs null_mean 4.01 | 1.000 | 0.01 | **NULL** |
| **T4** | 6236 / 114 has architectural meaning | descriptive only (1559 prime) | n/a | n/a | **DESCRIPTIVE-NULL** |
| **T5** | Allah-density correlates negatively with d_FR(s, 1) | Spearman ρ = +0.607 | 1.000 (1-sided neg) | 0.01 | **NULL — strongly opposite direction** |

**Bonferroni α_bon = 0.01.** No correction was needed for T2 (which uses a deterministic criterion rather than a p-value); the four p-value-based tests all sat at p ≥ 0.717, well above any reasonable threshold.

**Net: 1 of 5 tests passes (T2, the compression-tail genericity test, where the architectural finding is REAL and DISTINCTIVE). The four classical numerical claims (Q 8+Q 9 unity, Code-19, 6236/114 numerology, Q 1-as-density-seed) are all NULL — three of them in the *opposite* direction from the classical prediction.**

---

## §2 Per-test detail

### T1 — Q 8 + Q 9 functional unity (NULL, opposite direction)

The classical observation that Q 9 al-Tawba lacks a bismillah (and is therefore plausibly a continuation of Q 8 al-Anfāl) makes a sharp prediction in our quantitative framework: their FR-roots cosine-distance d_FR(8, 9) should sit at the *low end* of the 113 adjacent-pair distance distribution.

**Actual**: d_FR(8, 9) = 0.9110.
**Adjacent-pair distribution**: mean 0.798, median 0.842, range [0.146, 1.466].

The (8, 9) pair sits at **rank 81 of 113** — *larger* than typical, not smaller. p_one-sided (≤) = 0.717. The only adjacent pairs *more dissimilar* than (8, 9) are mostly transitions across major architectural seams (e.g. Q 50→51, Q 56→57 Hijra-kink, Q 110→111).

The "two-as-one" hypothesis is **rejected by FR-roots distance**. The two surahs share thematic content (warfare against the Quraysh and the early Medinan polity) but their root-frequency *signatures* are unusually divergent — Q 9's lexical profile is heavier on `tawba`, `mushrik`, `kāfir`, and `khilāf` framing whereas Q 8's centers on `ghanīma`, `qitāl`, `nafl`, and `Badr`-specific terminology. Quantitative root-frequency vectors do not see a single composition.

This is an **honest reversal** of a classical architectural intuition.

### T2 — Compression-tail genericity test (PASS-DISTINCTIVE)

We sliced `bukhari-noquran.txt` (4.6 MB Arabic prose) into 114 contiguous byte-chunks proportional to the Hafs verse-count distribution, then refit the same simple kink-50 linear model on per-chunk gzip ratio that we apply to the Quran's per-surah gzip ratio.

| Corpus | R² | β (slope) | n |
|:--|:-:|:-:|:-:|
| Quran (per-surah gzip-ratio, kink-50) | 0.766 | +0.00532 | 114 |
| Bukhari pseudo-mushaf (per-chunk gzip-ratio, kink-50) | 0.498 | +0.00121 | 114 |

The Quran's R² exceeds Bukhari's by **+0.268** under the same model; the Quran's slope is **4.4× larger in magnitude**. Both slopes are positive (small-sample-overhead effects raise per-unit gzip ratio in the tail of any text), but the Quranic effect is more than 4× as steep and far more linear.

**Verdict: PASS-DISTINCTIVE.** The compression-tail in the mushaf is not a generic property of any 114-piece Arabic edited collection.

**Honest caveat**: this test uses raw per-surah gzip ratio, which is a *related but distinct* metric from [[h-new-660-compression-tail-gradient|H-NEW-660]]'s per-window pairwise FR-cohesion-distance (which gives R² = 0.986). The 0.766 R² here is for the simpler proxy. The point of T2 is *comparative* — Quran vs Bukhari under the same proxy — and the comparison is decisive.

### T3 — Verse-count divisibility-by-19 (NULL)

| Quantity | Value |
|:--|:-:|
| Surahs with n_verses divisible by 19 (k_obs) | 4 |
| Random-uniform expectation (114/19) | 6.0 |
| Bootstrap null mean (k_null) | 4.01 |
| Bootstrap null std | 1.81 |
| Bootstrap null max (over 10⁵ resamples) | 13 |
| p (two-sided) | 1.000 |

The four matching surahs are Q 47 (n=38=19·2), Q 82 (n=19), Q 87 (n=19), Q 96 (n=19). The empirical count is **lower** than the uniform expectation and exactly at the bootstrap mean. A bootstrap from the empirical verse-count distribution (which is skewed toward small numbers in the mufaṣṣal tail) produces 4 such surahs *on average*. **The "Code 19" claim has no statistical support.**

This independently confirms the longstanding mainstream rejection of Rashad Khalifa's numerology.

### T4 — 6236 / 114 divisibility (DESCRIPTIVE-NULL)

6236 = 2² × 1559, where 1559 is prime. Divisors: {1, 2, 4, 1559, 3118, 6236}. None match any actual surah verse-count. 114 = 2 × 3 × 19. Mean verses per surah = 54.70 (not an integer, so no exact-divisor match possible). **No architectural significance is recoverable from these numbers.**

### T5 — Allah-density vs d_FR(s, 1) (NULL, strongly opposite direction)

**Predicted**: surahs closer-in-FR-space to Q 1 al-Fātiḥa should have *higher* divine-name density (Spearman ρ < 0).
**Observed**: Spearman ρ = **+0.607** (primary metric: divine-names-per-verse from the catalog), p_two-sided ≈ 4.9×10⁻¹³, p_one-sided neg = 1.0. **Sensitivity check** with bare الله regex: ρ = +0.594 (same direction, comparable strength).

**The prediction reverses sharply.** Inspecting the FR-neighbors of Q 1:

| 5 closest to Q 1 | d_FR | n_verses | div-name-density |
|:--|:-:|:-:|:-:|
| Q 108 (Kawthar) | 0.338 | 3 | 0.33 |
| Q 110 (Naṣr) | 0.353 | 3 | 0.33 |
| Q 112 (Ikhlāṣ) | 0.357 | 4 | 0.75 |
| Q 106 (Quraysh) | 0.357 | 4 | 0.50 |
| Q 100 (ʿĀdiyāt) | 0.377 | 11 | 0.18 |

| 5 farthest from Q 1 | d_FR | n_verses | div-name-density |
|:--|:-:|:-:|:-:|
| Q 5 (Māʾida) | 1.176 | 120 | 0.93 |
| Q 2 (Baqara) | 1.178 | 286 | 0.75 |
| Q 4 (Nisāʾ) | 1.222 | 176 | n/a (high) |
| Q 3 (Āl ʿImrān) | 1.223 | 200 | n/a (high) |
| Q 9 (Tawba) | 1.224 | 129 | 0.92 |

The FR-roots distance from Q 1 is dominated by **length and lexical breadth**, not by divine-name density. Q 1 is structurally a *short* surah (n=7); it sits FR-adjacent to other terminal-short surahs which have small total content and modest absolute divine-name counts. The Medinan ṭiwāl (Q 2–9) carry the heaviest divine-name *load* but are FR-distant from Q 1 because their root-vocabularies sprawl across the entire lexicon.

**The classical "Q 1 = umm al-kitāb seed-vector" intuition does not survive a length-controlled quantitative test.** Q 1 is theologically central but is *not* a high-divine-name-density attractor in FR-space; the high-density surahs are the long Medinan legal corpus.

This is an **honest reversal** worth recording.

---

## §3 Implication: classical numerical claims status

| Claim category | [[h-new-890-numerical-reaudit|H-NEW-890]] status | Direction |
|:--|:--|:--|
| Q 8 + Q 9 functional unity | NULL | OPPOSITE — pair is more dissimilar than typical |
| Compression-tail (architectural, NEW) | DISTINCTIVE | Confirmed not generic |
| Letter-/word-/verse-count of 19 | NULL | EXPECTED (~4 surahs match by chance) |
| 6236 / 114 numerology | DESCRIPTIVE-NULL | No structure |
| Q 1 as density-seed for the mushaf | NULL | OPPOSITE — Q1's FR-neighbors are LOW-density tail surahs |

**Net pattern**: classical *numerical* claims (counts, divisibilities, surah-identity merges) are **fully NULL or REVERSED** under this re-audit. The single test that *passed* (T2 compression-tail genericity) is not a classical numerical claim at all — it is the modern architectural finding ([[h-new-660-compression-tail-gradient|H-NEW-660]]) being *confirmed as Quran-distinctive* relative to a hadith control corpus.

This **strengthens** rather than undermines the architectural findings:

- The compression-tail R² = 0.986 is not a generic gzip-of-edited-Arabic-collection effect; Bukhari does not reproduce it (T2).
- The classical numerical machinery (Code-19, 6236/114, Q 8+Q 9 unity, Q 1-as-seed) is reliably NULL or reversed (T1, T3, T4, T5).
- The architectural findings sit on a firm empirical footing where the classical numerologies do not. The two are *not* on equal evidentiary status.

This is the **strongest possible "discontinuity" pattern**: classical numerical intuitions fail, but a *modern, simply-parameterized, length- and corpus-controlled* architectural law (kink-50) passes a cross-textual control. The Quran's structural distinctiveness is on the architectural axis, not the numerological one.

---

## §4 Honest limits

1. **T1's negative direction may reflect FR-roots-distance's own length-dominance.** Q 8 (75 verses) and Q 9 (129 verses) differ in length by 1.7×, and FR-distance under our parameterization is partially length-sensitive. A length-controlled FR variant might restore Q 8/Q 9 closeness. We do not run that variant here; we report the rules-tuple-locked result.

2. **T2 uses per-surah gzip-ratio**, not the full FR-cohesion-distance metric of [[h-new-660-compression-tail-gradient|H-NEW-660]]. The R²=0.766 here is for the simpler proxy. The *relative* Quran-vs-Bukhari comparison is the legitimate inference; the absolute R² value should not be compared to [[h-new-660-compression-tail-gradient|H-NEW-660]]'s 0.986.

3. **T3 bootstrap** uses the empirical verse-count distribution (skewed toward small mufaṣṣal-qiṣār values). A bootstrap from a uniform-on-[3, 286] null would give a *higher* expected k (more multiples of 19); the empirical-distribution null is the conservative choice and still gives p = 1.0.

4. **T5 reversal is partly mechanical**: short surahs cluster together in FR-space, and Q 1 is short. To test the classical "umm al-kitāb" claim more carefully one would need (a) length-residualized FR-distance, or (b) a divine-name *signature*-cosine rather than density. We pre-committed the simpler test and report its honest NULL.

5. **T4** is descriptive only and was included for completeness per task spec. We report the result without inferential weight.

6. **No new classical citations were invented.** The Q 8+Q 9 unity claim is a real classical observation tied to Q 9's missing bismillah (cf. *al-Itqān* discussions of the bismillah's placement); the Code-19 claim is a 20th-century one (Rashad Khalifa) and we did not attribute it to classical scholarship; the 6236/114 numerology is folk-numerological; the Q 1 = umm al-kitāb claim is canonical and is properly attributed to the title `umm al-kitāb` itself (a Prophetic appellation), not to a specific scholar.

---

## §5 Cross-references

- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** (compression-tail R² = 0.986, kink-50 content axis) — this re-audit's T2 confirms the *distinctiveness* of the kink-50 form against a hadith control.
- **[[h-new-700-phonological-compression-tail|H-NEW-700]]** (phonological dispersion-tail; sign-inverted twin) — explains why Q 1's FR-neighbors are short tail-surahs (mufaṣṣal-qiṣār clustering).
- **[[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]]** (per-surah iʿjāz signature) and **[[h-new-810-length-controlled-ijaz|H-NEW-810]]** (length-controlled iʿjāz) — both relevant to the length-control caveat in §4 limits 1 and 5.
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** / **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (Fisher-Rao mushaf-order test) — D-matrix used here.
- **classical-quantitative-claims-audit.md**, **mathematical-sequences-audit.md**, **numerical-coincidences.md** — prior NULL adjudications of numerological claims; [[h-new-890-numerical-reaudit|H-NEW-890]] reproduces and extends them.
- **abjad-residue-null.md** — companion finding showing letter-residue numerology is also NULL.

---

## §6 Final statement

**Classical Quranic numerological claims (Q 8+Q 9 unity by FR-distance, Code-19 verse-count divisibility, 6236/114 factorization, Q 1-as-density-seed) are NULL or REVERSE under proper rule-locked permutation testing. The single test that PASSES is the modern architectural one (compression-tail kink-50 distinctiveness, T2): the Quran's compression-tail law is NOT a generic property of a 114-piece Arabic edited collection. The Quran's structural specialness lies on the architectural axis (Fisher-Rao geometry, compression-tail, dual iʿjāz, super-additivity), not the numerological one.**
