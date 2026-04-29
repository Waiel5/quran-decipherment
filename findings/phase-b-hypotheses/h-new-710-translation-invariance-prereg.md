---
id: H-NEW-710
title: "Pre-reg — Translation-invariance of compression-tail: does H-NEW-660's R²=0.986 signature survive in English Sahih International?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 §10 — queued follow-up; structural-vs-Arabic-syntax test
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
seed: 20260436
parent: H-NEW-660
---

# [[h-new-710-translation-invariance|H-NEW-710]] — Translation-Invariance of Compression-Tail: Pre-Registration

## 1. Hypothesis

[[h-new-660-compression-tail-gradient|H-NEW-660]] established that the Arabic mushaf's content-cohesion has a two-piece-linear-kink structure with R²=0.986 over K=15 windows of FR-roots distance. Critical interpretive question: **is this signature deep-structural (semantic-architectural) or surface-Arabic-specific (root-system / morphology)?**

If the compression-tail is STRUCTURAL, it should survive in translation (since translation preserves content while losing Arabic-specific morphology).
If the compression-tail is ARABIC-SURFACE-SPECIFIC, it should disappear or weaken substantially in translation.

> H₁: applying the [[h-new-660-compression-tail-gradient|H-NEW-660]] protocol (K=15, kink-grid two-piece, linear, quadratic) to English-stem-cosine distance yields R² ≥ 0.30 with β < 0 (compression-tail present in translation).
>
> H₀: English R² < 0.30, OR β ≥ 0 (signature is Arabic-syntax-specific).

## 2. Translation source — LOCKED

**Source on disk** (verified via `ls /Users/grey/Downloads/quran/data/translations/`):
- `en.sahih.txt` — text-only (6249 lines)
- `en.sahih.txt-2.txt` — surah|verse|text format (6249 lines, 6236 with structured rows)

**LOCKED translation: `en.sahih.txt-2.txt`** — Sahih International English. Reasoning:
- It's the available English translation file with surah/verse delimiters.
- Sahih International is contemporary, semantically faithful, less paraphrase-heavy than Yusuf Ali; reasonable for content-cohesion measurement.
- Pickthall is NOT on disk; cannot be used.

**Rules-tuple shift documented**: [[h-new-660-compression-tail-gradient|H-NEW-660]] used Arabic FR-roots; [[h-new-710-translation-invariance|H-NEW-710]] substitutes a *content-vocabulary* measure (top-K stems cosine). This is a different operationalization of "content cohesion" — one designed for English where the Arabic root-system does not exist. The substitution is necessary; we accept the rules-tuple shift.

## 3. Stemming choice — LOCKED

**LOCKED**: simple lowercase + strip non-alphabetic + strip stopwords + Porter-style suffix stripping (built-in, no external library). The exact stemmer:

1. Lowercase the text.
2. Strip all non-alpha characters (replace with space).
3. Tokenize on whitespace.
4. Remove stopwords from a fixed list (the, a, an, of, in, to, and, or, but, is, are, was, were, be, been, being, have, has, had, do, does, did, will, would, can, could, should, may, might, shall, must, that, this, these, those, who, whom, whose, which, what, when, where, why, how, with, from, by, at, on, for, as, it, its, he, him, his, she, her, hers, they, them, their, theirs, we, us, our, ours, you, your, yours, i, me, my, mine, all, any, some, no, not, so, then, than, also, too, only, just, very, more, most, much, many, indeed, but, yet, now, into, upon, unto).
5. Strip suffixes (Porter-light): -ing, -ed, -es, -s, -ly, -er, -est, -ment, -tion, -sion, -ness, -ity. Apply LONGEST-MATCH first; only if remaining stem ≥ 3 chars.
6. Drop tokens shorter than 3 chars after stemming.

**Bracket-content removal**: Sahih International uses `[...]` for translator interpolations. We strip `[...]` entirely BEFORE tokenization.

**Top-K vocabulary**: K=200 most frequent stems across the entire 114-surah corpus. Each surah is represented by a 200-d count vector over this fixed vocabulary; cosine distance d_en(i,j) = 1 − cos(v_i, v_j).

## 4. Test design

For each consecutive K=15 window starting at position s ∈ {1, 2, ..., 100}:
- Compute d̄_en(window) = mean of pairwise cosine distances.
- Regress d̄_en on s (centered: s̃ = s − 50.5).
- Report slope β, intercept α, R², residual SE.

### Permutation null
Shuffle the 114 surahs to a random order (10000 perms, seed 20260436). Recompute all 100 windows' d̄_en on the shuffled mushaf. Refit linear regression. Get null distribution. Empirical p-value of observed.

### Alternative model fits (3 — Bonferroni)
1. Linear: d̄ = α + β·s
2. Quadratic: d̄ = α + β·s + γ·s²
3. Two-piece linear: d̄ = α + β·max(0, s − kink), kink ∈ {25, 35, 50, 65, 75} grid.

Pick PRIMARY = highest adjusted-R² among the three families (two-piece is grid-searched internally; only the family counts toward Bonferroni).

## 5. Pre-committed direction

- β < 0 (slope is negative; cohesion-distance decreases with mushaf-position) — same direction as Arabic.
- Permutation p ≤ α_bon = 0.01667.

## 6. Bonferroni structure

3 alternative model fits → Bonferroni-3 → α_corrected = 0.05/3 = 0.01667.

## 7. INTERPRETIVE thresholds (locked)

- **STRONG translation-invariant**: English R² ≥ 0.70 with two-piece kink at s ∈ [40, 60]. Compression-tail is STRUCTURAL — deep semantic-architectural law beyond Arabic morphology.
- **PARTIAL invariance**: English R² ∈ [0.30, 0.70]. Some content-axis bleed; the law is partly structural, partly Arabic-specific.
- **NULL on translation-invariance**: English R² < 0.30. Compression-tail is Arabic-syntax-specific (FR-roots-system tied).

Pass/fail under PRE-REG-STANDARD-04 (formal):
- **STRICT PASS**: primary R² ≥ 0.50, β < 0, perm p ≤ 0.01667.
- **DIRECTIONAL**: primary R² ≥ 0.30, β < 0, perm p ≤ 0.05.
- **NULL**: otherwise.

## 8. What would FALSIFY translation-invariance

- β ≥ 0: gradient direction wrong → compression is Arabic-specific, doesn't survive English content-vocab.
- R² < 0.30: gradient is not a primary signal in English content-vocab → Arabic-syntax-specific.

## 9. Predicted ranges (honest)

- I do NOT have a strong directional prior. The Arabic R²=0.986 was extraordinary; partial degradation in English is expected (a) because cosine-stem-distance is a noisier proxy than FR-roots, and (b) because the Sahih translator inserts content (`[...]`) that varies by surah-style.
- A rough expected range: R² ∈ [0.20, 0.70] depending on whether the underlying compression is content-driven or Arabic-rhetoric-driven.
- The prediction at the high end (R² ≥ 0.70) would be a striking result (structural-not-surface).

## 10. Files

- Script: `/Users/grey/Downloads/quran/scripts/h_new_710_translation_invariance.py`
- Output JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-710.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-710-translation-invariance.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-710-run-1.md`

## 11. Methodology rules

- MW-1: instrument-prior — English-stem-cosine (rules-tuple shift documented).
- MW-3: alternative-models — linear, quadratic, two-piece (kink-grid {25,35,50,65,75}).
- MW-7 (post-hoc): N/A — pre-registered.
- PRE-REG-STANDARD-04: hypothesis, null, direction, Bonferroni, success criteria, INTERPRETIVE thresholds all locked BEFORE execution.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
