---
finding_id: Q044-F-02
title: Q 44 has corpus-extreme *mubīn* (مبين) density per 1000 words
date_locked: 2026-04-28
seed: 20260428
phase: B+
test_family: per-surah
---

# Q044-F-02 pre-registration: mubīn-density extreme

## Hypothesis (direction-locked)

Q 44 al-Dukhān has a **higher density of the lexeme *mubīn* (مبين) per 1000 orthographic-words** than the corpus mean (excluding Q 44 itself).

**Pre-committed direction**: Q 44 *mubīn*-density > corpus-mean-excluding-Q-44.

The qualitative observation that motivates this pre-reg: Q 44 contains *mubīn* at vv. 2 (al-Kitāb), 10 (dukhān), 13 (rasūl), 19 (sulṭān), 33 (balāʾ) — five attestations in 59 verses / 364 words.

## Null hypothesis

H₀: Q 44's *mubīn*-density is at or below corpus-mean-excluding-Q-44.

## Operationalization

- **Tashkeel level**: no-tashkeel (default).
- **Source file**: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- **Match form**: orthographic-token regex `\bمبين\b` — exact word *mubīn* (5 letters م-ب-ي-ن including word-boundary; will not match longer compounds).
- **Counting unit**: token count of `\bمبين\b` per surah / total orthographic-words in surah × 1000.

## Verdict criteria

- **VINDICATED at corpus-extreme strength** if Q 44's z-score (Gaussian via mean+SD of corpus-excluding-Q-44 densities) ≥ +1.0 AND Q 44 ranks in top-3 of 114 surahs.
- **DIRECTIONAL** if z ≥ +0.5 but rank > 3.
- **NULL** if z < +0.5.
- **PRE-COMMIT VIOLATION + NULL** if z < 0 (Q 44 below corpus mean).

## Garden-of-forking-paths log (BEFORE running)

- Tashkeel level locked: no-tashkeel.
- Match-pattern locked: exact word boundary regex `\bمبين\b`; will not match e.g., *al-mubīn* with definite article (which would be *المبين*) — need to also include *المبين* as a separate count layered in.

  **Decision (pre-locked)**: count BOTH `مبين` and `المبين` as Q 44 *mubīn*-attestations, BUT use the same rule for ALL surahs in the baseline. (This is the single locked operationalization; deviation = pre-commit violation.)
- Density unit locked: per 1000 orthographic-words within the surah.
- Direction-of-effect locked: Q 44 > corpus-mean-excl-Q-44.

## Replication plan

Re-run on `quran-text/quran-min-tashkeel.json` (should be substring-stable).

## Bonferroni

Single direction-test, k=1, α=0.05.

## Run script

`/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/scripts/Q044_F_02_mubin_density.py`.

## Output

`/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-02.json`.
