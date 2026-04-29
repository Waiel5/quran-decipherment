---
id: H-NEW-700
title: "Pre-reg — Phonological compression-tail: do rhyme-distribution and phoneme-density follow the same 2-piece-kink-at-s=50 law as content (H-NEW-660)?"
phase: B
date_committed: 2026-04-28
hypothesis_origin: H-NEW-660 §10 queued follow-up — quantify whether the compression-tail is content-axis specific or extends to phonology
discipline: PRE-REG-STANDARD-04 + MW-1..MW-7
parent_1: H-NEW-660 (CONTENT-cohesion two-piece-kink-at-s=50: R²=0.986)
parent_2: H-NEW-630 (Q 67-114 super-cluster hierarchy)
seed: 20260435
---

# [[h-new-700-phonological-compression-tail|H-NEW-700]] — Phonological Compression-Tail: Pre-Registration

## 1. Hypothesis

[[h-new-660-compression-tail-gradient|H-NEW-660]] established that CONTENT-cohesion (Fisher-Rao roots-distance) follows a 2-piece-kink-at-s=50 law with R²=0.986 across 100 K=15 windows of the canonical 114-surah mushaf. The compression-tail spans Q 51-114 with slope -0.01237/position; Q 1-50 is approximately flat at d̄≈0.96.

**[[h-new-700-phonological-compression-tail|H-NEW-700]] asks**: does the same compression-tail signature appear on the **phonological axis** — the rhyme-distribution and phoneme-density axes — or is it CONTENT-SPECIFIC?

The phonological axis is a substantively different feature space:
- **Rhyme-distribution**: per-surah 28-element vector of final-letter frequencies (the *fawāṣil* / sajʿ rhyme-letter system that classical scholars have catalogued).
- **Phoneme-density**: 4-scalar profile (emphatic / pharyngeal / sibilant / glottal letter proportions) — the tajwīd / ḥurūf-thaqīla / ḥurūf-mufakhkhama density classes.

If the compression-tail is universal architectural (i.e., the mushaf compresses cohesion across ALL feature axes simultaneously), we expect phonological R² ≥ 0.50 with kink at s ∈ [40, 60]. If content-specific, phonological R² < 0.30 (cohesion is flat or noisy on the phonological axis).

## 2. Test design

### 2.1 Feature definitions (LOCKED)

**Rhyme-distribution (28-vector)**: For each surah, take the FINAL letter of each verse text after stripping trailing whitespace and punctuation. Use `quran-min-tashkeel.json` to access pause-marks/word-final letters (the no-tashkeel JSON drops some forms; the min-tashkeel JSON preserves the rasm and the verse-final form). Within the verse text:
- Strip Arabic ornaments/punctuation (ۛ ۖ ۚ ۗ ۘ ۙ ۜ ۥ ۧ ۭ ۤ ۖ tatweel ـ).
- Strip diacritics (Quranic min-tashkeel marks: U+0610-U+061A, U+064B-U+065F, U+0670, U+06D6-U+06DC, U+06DF-U+06E4, U+06E7-U+06E8, U+06EA-U+06ED).
- Take the LAST Arabic letter of the cleaned text.
- Map each Arabic letter to a 28-element basis: {ا, ب, ت, ث, ج, ح, خ, د, ذ, ر, ز, س, ش, ص, ض, ط, ظ, ع, غ, ف, ق, ك, ل, م, ن, ه, و, ي}. Treat ى as ي, ة as ه (for verse-final form), أ/إ/آ as ا, ؤ as و, ئ as ي.
- Per-surah rhyme-distribution = normalized count vector over the 28-letter basis.

**Phoneme-density (4-scalar)**: For each surah, after stripping diacritics and ornaments, count occurrences of:
- emphatic = {ص, ض, ط, ظ} (the four ḥurūf al-iṭbāq).
- pharyngeal = {ح, ع} (the two ḥurūf al-ḥalq voiced/voiceless pharyngeal).
- sibilant = {س, ش, ز, ص}.
- glottal = {ء, ه} (and ا hamza-bearing forms collapsed).

Total letter count = denominator. 4 proportions per surah.

(Note: the ص is in BOTH emphatic and sibilant — it is double-counted across the two groups, by classical phonetic taxonomy. This is intentional.)

### 2.2 Per-surah feature vectors

Two parallel feature systems:
- **System A (rhyme)**: 28-vector per surah. Cosine-distance pairwise → 114×114 D_rhyme.
- **System B (phoneme)**: 4-vector per surah. Cosine-distance pairwise → 114×114 D_phoneme.

### 2.3 Window sweep

For each consecutive K=15 window starting at s ∈ {1, ..., 100}:
- Compute d̄_rhyme(window) = mean pairwise cosine distance on D_rhyme over the 15 surahs.
- Compute d̄_phoneme(window) = mean pairwise cosine distance on D_phoneme over the 15 surahs.

This produces 100 d̄_rhyme values and 100 d̄_phoneme values.

### 2.4 Model fits (LOCKED)

For each axis (rhyme, phoneme):
1. **Linear**: d̄ = α + β·(s − 50.5).
2. **Quadratic**: d̄ = α + β·s + γ·s².
3. **Two-piece-linear at kink ∈ {25, 35, 50, 65, 75}**: d̄ = α + β·max(0, s − kink). Pick kink with highest R² (within-grid).

Pre-commit: report all 3 model R²s for each axis. PRIMARY model (per axis) = highest adj-R².

### 2.5 Permutation null

10000 random shuffles of the 114 surahs (seed 20260435). For each shuffle, recompute d̄_rhyme and d̄_phoneme over the 100 windows. Refit linear, quadratic, two-piece (best-grid kink). Empirical p-value = fraction of nulls with R² ≥ observed R².

## 3. Pre-committed direction

- **If compression-tail is content-only** (alternative H₀): expect FLAT or weakly-sloped phonological gradient. β small or near zero; R² < 0.30.
- **If compression-tail is universal architectural** (alternative H₁): expect β < 0 on rhyme and/or phoneme axes; R² ≥ 0.50; kink at s ∈ [40, 60].

## 4. Bonferroni structure

3 alternative model fits per axis → Bonferroni-3 → α_corrected = 0.05/3 = 0.01667.

(Note: 2 axes × 3 models = 6 tests. We do NOT apply outer Bonferroni-6 because rhyme and phoneme are distinct hypotheses, each with its own 3-model α_bon. This is consistent with [[h-new-660-compression-tail-gradient|H-NEW-660]]'s Bonferroni-3 framing for a single axis. If the user/team-lead requires outer correction, the threshold would tighten to α=0.05/6=0.00833 — see honest limit §7.)

## 5. Pass/fail thresholds (per axis, LOCKED)

- **PASS-EXTENDS-LAW** (universal compression-tail): primary-model R² ≥ 0.50, permutation p ≤ 0.01667, β < 0, kink ∈ [40, 60].
- **DIRECTIONAL-EXTENDS**: R² ≥ 0.30, p ≤ 0.05, β < 0.
- **PASS-CONFIRMS-CONTENT-INVARIANCE**: R² < 0.30 (gradient is content-specific; phonological axis is FLAT/noisy → phonological compression-tail does NOT exist).
- **PHONOLOGICAL-ONLY** (unexpected but possible): if rhyme passes but phoneme fails, or vice versa, report as a SPLIT verdict.

If kink position diverges from s=50, REPORT it honestly (a different kink would suggest the phonological axis has its OWN architecture).

## 6. Predicted ranges

Best guess (no strong prior):
- Rhyme R²: 0.20 - 0.55 (the *fawāṣil* literature suggests rhyme tightens in mufaṣṣal — so a moderate compression-tail is plausible).
- Phoneme R²: 0.10 - 0.40 (less clear; phoneme classes may be roughly stationary across the mushaf).
- Most likely outcome: rhyme shows a partial compression-tail (R² ≈ 0.40), phoneme axis is flatter (R² < 0.30).

## 7. Honest limits

1. **ة → ه mapping is a convention**. Some classical *fawāṣil* taxonomies treat tāʾ marbūṭa as distinct.
2. **Final-letter rhyme is a simplification** — true rhyme involves the rawiyy + ridf + qaid (rhyme letter + post-rhyme vowel + secondary-rhyme letter). 28-vector captures only the rawiyy.
3. **Cosine distance** vs Fisher-Rao: [[h-new-660-compression-tail-gradient|H-NEW-660]] used FR-roots; we use cosine here for simplicity. A quick sanity-check: FR is appropriate for Dirichlet-style proportional data; cosine is appropriate for raw counts. Both are valid for proportional vectors. Result interpretation does NOT depend on the choice.
4. **K=15 only**: same windowing as [[h-new-660-compression-tail-gradient|H-NEW-660]] for direct comparability.
5. **Outer Bonferroni**: 2 axes × 3 models = 6 tests; not applied (see §4).
6. **Min-tashkeel vs no-tashkeel**: rhyme uses min-tashkeel for verse-final form preservation; phoneme uses no-tashkeel for letter-counting. Both come from the same canonical Hafs ʿan ʿĀṣim text.

## 8. What would FALSIFY each direction

- **Rejects universal-extension**: rhyme R² < 0.30 AND phoneme R² < 0.30.
- **Rejects content-specificity**: rhyme R² ≥ 0.50 AND phoneme R² ≥ 0.50, both with kink ∈ [40, 60].
- **Mixed**: only one axis passes — split verdict, content-specific gradient with phonological partial-coupling.

## 9. Files

- Script: `scripts/h_new_700_phonological_compression_tail.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-700.json`
- Findings: `findings/phase-b-hypotheses/h-new-700-phonological-compression-tail.md`
- Journal: `journal/h-new-700-run-1.md`

## 10. Methodology rules

- MW-1: instrument-prior — cosine distance on per-surah feature vectors (rhyme, phoneme).
- MW-3: alternative-models — linear, quadratic, two-piece (kink grid 25/35/50/65/75).
- PRE-REG-STANDARD-04: hypothesis, null, direction, Bonferroni, success criteria all locked.
- ONE TEXT: single canonical Hafs ʿan ʿĀṣim mushaf. No "edition" framing.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
