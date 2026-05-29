---
id: H-NEW-2080
title: "PRE-REG — Exhaustive verse-final rhyme-scheme (fāṣila) corpus scan + monorhyme inventory"
phase: B
status: PRE-REGISTERED (locked before observation)
date: 2026-05-29
specialist: rhyme-scan-specialist (candidate-pattern generator for verse-final rhyme)
parent_1: H-NEW-700 (per-surah top-letter rhyme-dominance methodology; rhyme dispersion-tail R²=0.789)
parent_2: phase-b-saj-rhyme-run-1 (2026-04-12 saj fāṣila analysis; fasila_1/2/3 skeleton extraction; 18 perfect monorhymes claimed)
parent_3: H-NEW-960 (cross-corpus rhyme-letter Shannon-entropy; per-surah rāwī uniformity)
parent_4: al-Bāqillānī *Iʿjāz al-Qurʾān*, *iʿjāz al-fawāṣil* axis
parent_5: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on al-fawāṣil
seed: 20260509
n_perms: not-applicable-descriptive-inventory (baseline is closed-form expectation)
bonferroni_k: 2
bonferroni_family: {H1-nūn/mīm-dominance, H2-perfect-monorhyme-count}
alpha_bon: 0.025
verdict: PRE-REGISTERED
---

# H-NEW-2080 — Exhaustive Rhyme-Scheme (Fāṣila) Corpus Scan + Monorhyme Inventory

## 0. Purpose

This is a CANDIDATE-PATTERN GENERATOR for verse-final rhyme (fāṣila). The prior project rhyme work
(H-NEW-700, phase-b-saj-rhyme-run-1, H-NEW-960) computed per-surah top-letter dominance and the
dispersion-tail gradient, but never tabulated the **corpus-wide rhyme-final-letter histogram** in one
place, never verified the widely-repeated **"the Quran is ~85% -ūn/-īn (nūn/mīm) rhyme"** claim against
a baseline, and never produced a single canonical **scheme-classification + perfect-monorhyme inventory**.
H-NEW-2080 fills those three gaps as a single descriptive instrument.

## 1. Background and motivation

It is a popular claim (folk-rhetorical, often attributed loosely to the *fawāṣil* tradition) that the
overwhelming majority of Quranic verses rhyme on the nasal endings -ūn / -īn / -īm — i.e. on the letters
nūn (ن) and mīm (م). H-NEW-700 §3 documented that long surahs (Q 2-16) are heavily ن-final
(*al-fāṣila al-mursalah*), and phase-b-saj-rhyme-run-1 §1 found the top two 2-letter fasilas are ون
(1755) and ين (1297). But the corpus-wide SINGLE-LETTER (rāwī-level) histogram, and the explicit test of
whether ن+م alone clear 50%, has not been locked and reported.

## 2. Rules-tuple (LOCKED)

- **Text variant**: `quran-text/quran-min-tashkeel.json` (min-tashkeel, per task spec and SKILL §2.1 rhyme-analysis default).
- **Reading tradition**: Hafs-Kufan (6,236 verses).
- **Counting unit**: verse-final letter (rāwī-level), i.e. the LAST Arabic letter of the LAST whitespace-delimited word of each verse.
- **Trailing-glyph handling (LOCKED)**: 17 verses in the min-tashkeel JSON carry a STANDALONE recitation glyph as their final whitespace token — 15 sajda marks (۩ U+06E9, *sajdat al-tilāwa*) and 2 small-high-seen pause marks (ۜ U+06DC). These are NOT words and carry no rāwī. When a trailing token strips to an empty consonant-skeleton, it is SKIPPED and the preceding genuine word supplies the rāwī. (Verified empirically before lock; affects Q 7:206, 13:15, 16:50, 17:109, 18:1, 19:58, 22:18, 22:77, 25:60, 27:26, 32:15, 38:24, 41:38, 53:62, 69:28, 84:21, 96:19.)
- **Letter definition**: graphemes, diacritics stripped, normalized per the phase-b-saj-rhyme-run-1 NORM map for cross-consistency:
  - hamza-carriers collapsed: أ إ آ ٱ → ا ; ؤ → و ; ئ → ي
  - alif maksura ى → ا (pausal long-ā)
  - teh marbuta ة → ه (pausal /h/)
  - dotless beh ٮ → ب
- **Basmala**: counted only as verse 1:1 (the sole basmala that is itself a numbered verse, Hafs-Kufan). No basmala is prepended to other surahs as a counted verse.
- **Pausal form**: rhyme is anchored on the consonant skeleton (case endings drop in pause). This matches the saj_rhyme.py instrument exactly so results are directly comparable.

## 3. Hypotheses (DIRECTION-LOCKED)

### H1 — Nūn/Mīm dominance (PRIMARY, direction-locked)
**The combined corpus-wide share of verses whose final letter is nūn (ن) OR mīm (م) is > 50%.**

- Statistic: `share_nun_mim = (count_final_nun + count_final_mim) / 6236`.
- Direction: nūn+mīm > 50% (LOCKED before observation).
- Pass: `share_nun_mim > 0.50`.
- NULL: `share_nun_mim ≤ 0.50` — published with full prominence as the popular "85% nasal-rhyme" claim being a folk-overstatement; report the actual figure.
- Note on the "85%" framing: the popular claim conflates the 2-letter fasilas (ون+ين+يم) with single-letter rāwī. We test BOTH:
  - **H1a (rāwī-level)**: final-letter ∈ {ن, م} > 50%.
  - **H1b (fasila-2 nasal-class)**: final-2-skeleton ∈ {ون, ين, يم, ان, ام, ون, ين} nasal-ending share — reported descriptively (NOT a pass/fail gate, exploratory) to adjudicate where the "85%" figure comes from.

### H2 — Perfect-monorhyme count (direction-locked)
**At least 10 surahs are PERFECT monorhymes** (100% of their verses share the same final letter / rāwī).

- Statistic: `n_perfect = #{surahs with U1 == 1.000}` where U1 = fraction of verses ending in the surah's dominant final-letter.
- Direction: n_perfect ≥ 10 (LOCKED).
- Pass: `n_perfect ≥ 10`.
- NULL: `n_perfect < 10`.
- Cross-check: with the trailing-glyph handling above, this should reproduce the phase-b-saj-rhyme-run-1 figure of 18 perfect monorhymes; any residual divergence flags an instrument inconsistency that must be reported.

### Bonferroni
Family of k=2 pass/fail gates (H1a, H2). α_bon = 0.05/2 = 0.025. Since H1/H2 are descriptive-threshold tests against a fixed corpus (no sampling), the formal p-value role is played by the **baseline comparison** in §4; α_bon governs the baseline z-tests.

## 4. Null / baseline (LOCKED)

**Baseline = random Arabic word-final letter distribution.** Two baselines, both pre-committed:

- **B1 (corpus-letter-frequency baseline)**: under the null that verse-final letters are drawn i.i.d. from the
  Quran's overall letter-frequency distribution (`data/baseline-corpora/letter-freqs.csv`, row `quran-no-tashkeel`),
  the expected nūn+mīm share = `freq(ن) + freq(م)` ≈ 0.082 + 0.081 ≈ 0.163. The OBSERVED verse-final
  nūn+mīm share is tested against this expectation via a one-proportion z-test (n=6236).
  - Pre-committed direction: observed >> expected (verse-final position is rhyme-engineered, NOT random-letter-draw).
  - α_bon = 0.025.
- **B2 (positional-shuffle sanity)**: report the share of nūn+mīm among ALL word-final letters of NON-verse-final
  words in the corpus, as an internal control. If verse-final nūn+mīm share substantially exceeds the
  generic word-final share, the rhyme-slot is confirmed as actively letter-selected. (Descriptive, reported, not a hard gate.)

## 5. Deliverables

- Corpus rhyme-final-letter HISTOGRAM (all distinct rāwī letters, counts, %).
- Per-surah rhyme-scheme classification: each surah tagged MONORHYME-PERFECT / MONORHYME-DOMINANT (U1 ≥ 0.80) / ALTERNATING (two letters each ≥ 0.30) / FREE (no letter ≥ 0.50), with U1 and dominant rāwī.
- Perfect-monorhyme surah list (U1 == 1.000), ranked by verse-count (longest perfect monorhyme first).
- Nūn/mīm dominance verdict (H1a) + the fasila-2 nasal adjudication of the "85%" claim (H1b).
- Baseline z-test results (B1, B2).
- Connection to H-NEW-700 (this histogram is the corpus-level marginal of the per-surah dispersion-tail).

## 6. Success / failure bins

- **PASS-BOTH**: H1a (>50%) AND H2 (≥10 perfect) both hold, AND B1 z >> 0 at α_bon. → nūn/mīm dominance + monorhyme-richness CONFIRMED.
- **PARTIAL**: exactly one of {H1a, H2} holds.
- **NULL**: neither holds.
- Pre-commit violation (any direction reversed) published with full prominence.

## 7. Seed and reproducibility

- seed: 20260509 (used only for any tie-breaking ordering; the inventory itself is deterministic).
- Instrument: `findings/phase-b-hypotheses/scripts/h-new-2080.py`.
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-2080.json`.
- This pre-reg is SHA256-locked; the SHA is embedded in the run script and verified at runtime (fail-fast on mismatch).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
