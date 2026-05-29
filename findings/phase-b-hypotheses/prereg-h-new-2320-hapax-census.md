# Pre-registration — H-NEW-2320: Corpus-wide hapax-legomenon (singleton-root) census and Meccan-concentration test

**Pre-registered by:** Waiel Al-Shujaa
**Date:** 2026-05-29 (locked BEFORE any computation)
**Seed:** 20260509 · **Permutations:** 10000
**Rules-tuple:** (QAC root v0.4, Buckwalter ROOT field, Hafs-Kūfan, root-bearing tokens only — particles/pronouns without ROOT excluded; basmala counted as it appears in the QAC data)

## Background

H-NEW-1930 found Q 1 al-Fātiḥa carries 3 corpus-SINGLETON roots in only 7 verses (a microcosm signal). This generalizes that observation: enumerate EVERY corpus-singleton root (hapax legomenon at the root level — a root attested exactly once in the entire 114-surah corpus) and map its distribution. This is a close-reading GENERATOR: it scans the whole root inventory rather than testing a named prior.

## Definitions

- **Root token:** a QAC morphology segment carrying a `ROOT:` feature. Tokens without a root (most particles, some pronouns) are excluded from the denominator.
- **Hapax root:** a root whose total corpus token-frequency = 1.
- **Per-surah hapax rate:** (number of hapax-root tokens located in surah *s*) / (number of root-bearing tokens in surah *s*).
- **Surah region:** `type` field of quran-text/quran-no-tashkeel.json — `meccan` or `medinan`.

## Primary hypothesis (direction LOCKED before observation)

> **H1:** The per-token hapax rate is **HIGHER in Meccan surahs than in Medinan surahs.**
> Rationale: early-Meccan oath/eschatological surahs are classically noted for rare/exotic cosmic vocabulary (al-qāriʿa, al-ʿādiyāt, etc.), which should manifest as elevated corpus-singleton density.

**Direction is locked: Meccan > Medinan.** If the observed direction REVERSES (Medinan ≥ Meccan), the result is published as a NULL/反direction finding with full prominence — no post-hoc re-rationalization.

**Test statistic:** Δ = mean(per-token hapax rate | Meccan surahs) − mean(per-token hapax rate | Medinan surahs), unweighted across surahs.
**Null model:** permute the meccan/medinan labels across the 114 surahs (preserving the count of each), recompute Δ, 10000 times, seed 20260509. One-sided p = fraction of null Δ ≥ observed Δ.

## Secondary (descriptive, no pass/fail)

- S1: Total count of hapax roots in the corpus.
- S2: Per-surah hapax-root count residual vs size-proportional expectation E_s = H · n_s / N (where H = total hapax tokens, n_s = surah root-tokens, N = corpus root-tokens). Report the top-10 positive-residual surahs.
- S3: Reproduce the Q 1 al-Fātiḥa hapax count and list its hapax roots (cross-check H-NEW-1930).
- S4: Spearman correlation between per-token hapax rate and canonical surah number (descriptive).

## Quality gates

- Direction matches pre-commit (else NULL with prominence).
- Bonferroni: only one primary test (H1); secondaries are descriptive, no correction needed.
- All counts computed from data/morphology/quranic-corpus-morphology-0.4.txt; no values from memory.
- Verdict ∈ {CONFIRMED, DIRECTIONAL, NULL, CONFIRMED-BUT-MEANINGLESS}.

## Files

- This pre-reg (SHA-256 self-locked; hash embedded in scripts/h-new-2320.py and verified at runtime)
- scripts/h-new-2320.py
- csv/h-new-2320.json
- h-new-2320-hapax-census.md
