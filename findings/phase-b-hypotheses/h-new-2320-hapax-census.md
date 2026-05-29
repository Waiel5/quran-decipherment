---
finding_id: H-NEW-2320
status: CONFIRMED — Meccan surahs carry corpus-singleton (hapax) roots at >4× the Medinan rate (p=0.0012)
phase: B+ → C
date: 2026-05-29
rules_tuple: (QAC root v0.4, Buckwalter ROOT field, root-bearing tokens only, Hafs-Kūfan)
verdict: CONFIRMED (direction locked Meccan>Medinan before computation)
---

# H-NEW-2320 — Corpus-wide hapax-legomenon (singleton-root) census: lexical novelty is a Meccan signature

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
