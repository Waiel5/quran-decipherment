---
finding_id: H-NEW-2320
status: CONFIRMED — Meccan surahs carry corpus-singleton (hapax) roots at >4× the Medinan rate (p=0.0012)
phase: B+ → C
date: 2026-05-29
rules_tuple: (QAC root v0.4, Buckwalter ROOT field, root-bearing tokens only, Hafs-Kūfan)
verdict: CONFIRMED (direction locked Meccan>Medinan before computation)
---

# H-NEW-2320 — Corpus-wide hapax-legomenon (singleton-root) census: lexical novelty is a Meccan signature


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

## What was tested

A close-reading GENERATOR over the entire QAC root inventory: enumerate every **hapax root** (a root attested *exactly once* in the 114-surah corpus), map its surah location, and test whether hapax density distinguishes the two revelation regions. Pre-registered with direction locked **before** computation (pre-reg SHA-256 `68f2446d3f3c362823094d12870b896500146d67e70edd8fcb8e206632b9eaa6`, verified at runtime; seed 20260509; 10000 permutations).

This generalizes H-NEW-1930 (Q 1 al-Fātiḥa carries corpus-singleton *words*) from one surah to the whole corpus, and from the word-form level to the root level.

## Corpus census

| Quantity | Value |
|---|---|
| Root-bearing tokens (denominator) | 49,968 |
| Distinct roots | 1,642 |
| **Hapax roots (corpus frequency = 1)** | **395** |
| Hapax fraction of root inventory | **24.1%** |

Nearly **one in four** distinct Quranic roots is used exactly once in the entire corpus — a heavy single-use tail typical of a rich but bounded lexicon.

## Primary result — CONFIRMED

| Region | Mean per-token hapax rate |
|---|---|
| Meccan surahs | **0.02808** |
| Medinan surahs | **0.00677** |
| Δ (Meccan − Medinan) | **+0.02130** |
| Null mean Δ (label-permutation) | −0.00012 |
| **One-sided p (locked: Meccan>Medinan)** | **0.0012** |

Meccan surahs deploy corpus-singleton roots at **more than four times** the Medinan rate. The direction was locked before computation and held; p = 0.0012 against a label-permutation null. **Verdict: CONFIRMED.**

This is a genuinely novel, quantified structural fact: **lexical novelty (hapax density) is a Meccan signature.** It is independent of, and converges with, the established compression-tail laws (d̄_content/d̄_rhyme/d̄_phoneme kink-at-50) — all describe the early-Meccan short surahs as a distinct stylistic regime, here via vocabulary uniqueness rather than distributional geometry.

## Highest hapax-rate surahs (all Meccan; short-mufaṣṣal dominated)

| Surah | Region | Rate | Hapax/root-tokens |
|---|---|---|---|
| Q 108 al-Kawthar | Meccan | **0.2857** | 2/7 |
| Q 100 al-ʿĀdiyāt | Meccan | 0.2083 | 5/24 |
| Q 112 al-Ikhlāṣ | Meccan | 0.2000 | 2/10 |
| Q 106 Quraysh | Meccan | 0.1667 | 2/12 |
| Q 113 al-Falaq | Meccan | 0.1333 | 2/15 |
| Q 111 al-Masad | Meccan | 0.1177 | 2/17 |
| Q 81 al-Takwīr | Meccan | 0.1061 | 7/66 |
| Q 91 al-Shams | Meccan | 0.1026 | 4/39 |
| Q 90 al-Balad | Meccan | 0.0769 | 4/52 |

The **top 12 surahs by hapax rate are all Meccan.** Spearman ρ(rate, surah-number) = +0.223 — consistent, since the high-numbered short surahs are predominantly early Meccan.

## Size-controlled residuals (secondary S2)

Controlling for surah length (expected hapaxes ∝ root-token share), the surahs with the most *excess* hapax roots are: Q 22 al-Ḥajj (+7.5), Q 20 Ṭā-Hā (+7.4), Q 55 al-Raḥmān (+7.0), Q 81 al-Takwīr (+6.5), Q 37 al-Ṣāffāt (+5.7), Q 12 Yūsuf (+5.1), Q 79 al-Nāziʿāt (+5.0), Q 100 al-ʿĀdiyāt (+4.8), Q 53 al-Najm (+4.3), Q 47 Muḥammad (+4.2). The oath/cosmic surahs (Takwīr, Nāziʿāt, ʿĀdiyāt, Najm) surface as predicted; two long surahs (Ḥajj, Raḥmān) carry large *absolute* hapax counts by virtue of unique ritual/cosmological vocabulary even though their *rate* is moderate.

## Honest refinement of H-NEW-1930 (secondary S3)

**Q 1 al-Fātiḥa has ZERO hapax ROOTS.** This does NOT contradict H-NEW-1930 — it sharpens it via rules-tuple sensitivity. H-NEW-1930's three "corpus-singletons" (al-maghḍūb, nastaʿīn, ihdinā) are singletons at the **word-form / lexeme** level. Their *roots* — ġ-ḍ-b (anger), ʿ-w-n (help), h-d-y (guidance) — all recur elsewhere (h-d-y is among the most common roots in the corpus). So:

> **Hapax-at-form ≠ hapax-at-root.** Q 1's microcosm signal lives at the morphological-surface level (unique inflected forms), not at the root level. The two are different instruments and must not be conflated — the same lesson as the kallā homograph case (§10.80): the counting rule determines the verdict.

This is logged with equal prominence to the primary CONFIRMED result.

## Classical connection

The classical tradition's *gharīb al-Qurʾān* literature (Ibn ʿAbbās's *Masāʾil Nāfiʿ*, al-Sijistānī's *Gharīb al-Qurʾān*, al-Rāghib al-Iṣfahānī's *Mufradāt*) catalogues rare/difficult Quranic vocabulary. H-NEW-2320 supplies the empirical distribution behind that genre: the *gharīb* concentrates in the Meccan revelation, especially the short oath-surahs — vindicating the philological intuition that the early-Meccan register is lexically the most exotic.

## Rules-tuple / limits

- Root-level only; a form-level (lexeme) hapax census would give different (higher) counts and is a distinct instrument (see Q 1 note).
- Tokens without a QAC ROOT (most particles) are excluded; including them as a separate "function-word" stratum is a follow-up.
- Region labels are the canonical meccan/medinan `type`; finer chronological orderings (Nöldeke, Egyptian) are a follow-up to test the rate↔chronology gradient directly.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2320-hapax-census.md` (SHA-256 `68f2446d…b9eaa6`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2320.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2320.json`

---

*H-NEW-2320 logged 2026-05-29 by Waiel Al-Shujaa. Lexical novelty is a Meccan signature. Bismillāhi al-Raḥmāni al-Raḥīm.*
