# Pre-registration — H-NEW-2330: Lexical burstiness / topical clumping of Quranic roots

**Pre-registered by:** Waiel Al-Shujaa
**Date:** 2026-05-29 (locked BEFORE computation)
**Seed:** 20260509 · **Permutations/simulations:** 10000
**Rules-tuple:** (QAC root v0.4, Buckwalter ROOT field, root-bearing tokens only, Hafs-Kūfan)

## Background

H-NEW-2320 established that corpus-singleton (hapax) roots concentrate in Meccan surahs. This pre-reg asks the complementary question about the *content* vocabulary (roots used more than once): is the Quran's vocabulary **topically clumped** — i.e. do content roots cluster within single surahs more than a random allocation would predict? This is the linguistic property of *burstiness* (a content word, once used, tends to recur locally), here measured at the surah scale for the first time on this corpus.

## Definition

- **Surah-local burst root:** a root with corpus frequency **≥ 3** whose tokens all fall in **exactly one** surah.
- **Observed statistic L_obs:** the count of surah-local burst roots in the actual corpus.

## Null model

For each root with corpus frequency *f*, allocate its *f* tokens independently across the 114 surahs by a multinomial draw with surah probabilities p_s = (root-tokens in surah *s*) / (total root-tokens). This destroys topical clumping while preserving (a) each root's frequency and (b) each surah's size. For each of 10000 simulated corpora, recompute L (count of freq≥3 roots confined to one surah). 

**L_null = mean over simulations.** One-sided p = fraction of simulations with L_sim ≥ L_obs.

## Primary hypothesis (direction LOCKED)

> **H1:** L_obs > L_null — the Quran's content vocabulary is **more topically clumped** (more single-surah bursts) than random allocation predicts.

If the observed direction reverses (L_obs ≤ L_null, i.e. vocabulary is more evenly spread than chance), publish as NULL/reversed with full prominence.

## Secondary (descriptive)

- S1: Distribution of root **dispersion** = number of distinct surahs each root appears in; report the "lexical spine" (roots appearing in ≥ 90 of 114 surahs).
- S2: The most extreme surah-local bursts (highest-frequency roots confined to one surah) and their surahs.
- S3: Region split of burst roots (Meccan vs Medinan) — connect to H-NEW-2320.

## Quality gates

- Direction matches pre-commit (else NULL with prominence).
- One primary test; secondaries descriptive (no Bonferroni needed).
- All counts from data/morphology/quranic-corpus-morphology-0.4.txt.
- Verdict ∈ {CONFIRMED, NULL, CONFIRMED-BUT-MEANINGLESS}.

## Files

- This pre-reg (SHA-256 self-locked; embedded in scripts/h-new-2330.py, runtime-verified)
- scripts/h-new-2330.py · csv/h-new-2330.json · h-new-2330-lexical-burstiness.md
