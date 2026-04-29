---
id: H-NEW-195
title: Per-surah letter-bigram entropy — per-surah unpredictability and comparison to Bukhārī matched chunks
phase: B
status: PRE-REGISTERED
date: 2026-04-17
specialist: team-lead (inline execution)
seed: 20260419
bonferroni_k: 2
alpha: 0.05
alpha_bonferroni: 0.025
n_null: 10000
rules_tuple: "(Hafs-Kūfan; text = quran-text/quran-no-tashkeel.json; letters stripped of tashkeel and Quranic pause marks; NO rasm-normalization — raw unicode Arabic letters U+0621..U+064A; whitespace/punctuation dropped; per-surah bigram counts; Bukhārī = data/baseline-corpora/raw/bukhari-noquran.txt split at \\bباب\\b, top-114 longest segments by letter count, same normalization)"
parent_findings:
  - h-new-25 (trigram phonotactic entropy Quran<baselines)
  - h-new-159 (Heap β per-surah variance 2.5× Bukhārī)
  - h-new-163 (dispersion ranking all surahs)
  - h-new-172 (α per-surah)
  - h-new-178 (α,β manifold; muq +0.034 residual)
pre_reg: findings/phase-b-hypotheses/h-new-195-entropy-per-surah-prereg.md
script: scripts/h_new_195_per_surah_bigram_entropy.py
output_json: findings/phase-b-hypotheses/csv/h-new-195.json
output_csv: findings/phase-b-hypotheses/csv/h-new-195-per-surah.csv
---

# [[h-new-195-entropy-per-surah|H-NEW-195]] — Per-surah letter-bigram entropy

## Motivation

H-NEW-25 established that Quran has lower trigram conditional entropy than
4 matched classical Arabic baselines at corpus-level. That test was
corpus-aggregate. Here we push to per-surah resolution: does each surah
carry a distinct bigram entropy signature, and does per-surah entropy
(length-controlled residual) correlate with existing non-content axes
([[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] dispersion, [[h-new-178-alpha-beta-manifold|H-NEW-178]] (α,β), muqaṭṭaʿāt status, Nöldeke)?

This also re-tests the H-NEW-25 corpus-level finding at bigram resolution
with proper matched-chunk baselines (Bukhārī top-114 bab-segments).

## Method

### Step 1 — Per-surah bigram distribution

For each surah s (1..114):
1. Concatenate verse strings (no-tashkeel, Quranic pause marks removed:
   `[\u06D6-\u06DF\u0610-\u061A\u064B-\u065F\u0670]`).
2. Strip whitespace/punctuation; keep only Arabic letters U+0621..U+064A.
3. Extract all adjacent letter-pairs (L1, L2) WITHIN the concatenated
   string (cross-verse pairs included — entropy measures structural
   letter-order statistics of the surah as a whole).
4. Empirical bigram distribution p(L1, L2) = count(L1,L2)/N_bigrams.
5. Shannon joint entropy H(L1,L2) = -Σ p log₂ p (bits).
6. Unigram entropy H(L1) from marginal p(L1) = Σ_{L2} p(L1,L2).
7. Conditional entropy H(L2|L1) = H(L1,L2) - H(L1).

### Step 2 — Length-controlled residual

OLS fit H(L2|L1) vs log₁₀(N_bigrams) across 114 surahs.
Residual_s = observed H(L2|L1) - predicted H(L2|L1).

### Step 3 — Top/bottom-5

Report top-5 lowest H(L2|L1) (most predictable) and top-5 highest
H(L2|L1) (most surprising) BOTH raw AND length-residualized.

### Step 4 — Bukhārī matched baseline

Load `data/baseline-corpora/raw/bukhari-noquran.txt`. Split on `\bبابb\b`.
Apply SAME normalization. Sort segments by letter count; take top-114 by
length. For each, compute H(L2|L1). Compare mean entropy Quran vs
Bukhārī, Welch two-sample t-test (two-sided), and Mann-Whitney U.

### Step 5 — Correlations

Spearman correlation of residual (length-controlled H(L2|L1)) with:
- [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] dispersion (from [[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv column dispersion_h163)
- [[h-new-178-alpha-beta-manifold|H-NEW-178]] α (alpha), β (beta_h159) — two separate correlations
- muqaṭṭaʿāt binary (is_muq from [[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv)
  (Mann-Whitney U; muq vs non-muq residual)
- Nöldeke order (data/revelation-order.csv, noldeke_order)

Direction NOT pre-committed (exploratory-descriptive). Report ALL raw
correlations + nominal p-values. Finding "strongest correlate" = highest
|ρ| among these five.

## Primary pre-registered tests (Bonferroni k=2)

1. **PRIMARY**: mean H(L2|L1) differs Quran vs Bukhārī (Welch t, two-sided)
   — direction NOT pre-committed, as both directions are theoretically
   motivated (Quran could be more-structured → lower H, or more-varied
   → higher H).
2. **SECONDARY**: Residual H(L2|L1) differs muqaṭṭaʿāt vs non-muq
   surahs (Mann-Whitney U, two-sided), direction NOT pre-committed.

α_bon = 0.025 each.

## Secondary / descriptive outputs (not gating)

- Per-surah CSV: sid, n_letters, n_bigrams, H_unigram, H_bigram_joint,
  H_cond, residual_H_cond
- Top-5 lowest/highest H_cond (both raw and residual-ranked)
- Five correlations (Spearman) + p-values
- Distribution summary (mean, sd, min, max) Quran and Bukhārī

## MW-5 control

Positive control: shuffled Quran text (letter-shuffle within each surah)
MUST produce H_cond ≈ H_unigram (no conditional structure). If shuffled
H_cond < unshuffled Quran H_cond by less than 0.1 bits on average, the
instrument is broken (shuffling destroys structure → should RAISE H_cond
toward unigram).

MW-1 length-control: Bukhārī segments sorted by letter count are matched
to Quran surahs sorted by letter count (paired); report paired Wilcoxon
in addition to Welch.

## Garden-of-forking-paths log

- **Fixed**: no rasm-normalization (raw Arabic letters). Rationale: the
  H-NEW-25 trigram test used rasm-normalization and found Quran<baseline;
  here we use raw letters to SEPARATE from that result — a new test
  axis, not a re-run of H-NEW-25.
- **Fixed**: cross-verse bigrams included (no verse-boundary resets).
  Rationale: verse-boundaries are liturgical, not phonological; stripping
  them would undercount within-utterance bigram structure. Sensitivity:
  also report Quran-wide comparison with verse-reset bigrams as a
  disclosure.
- **Fixed**: top-114 longest Bukhārī segments (matches [[h-new-145-muq-code-decoding|H-NEW-145]] /
  [[h-new-159-heap-beta-per-chapter|H-NEW-159]] / [[h-new-147-bukhari-cross-corpus|H-NEW-147]] convention).
- **Fixed**: seed 20260419, consistent with [[h-new-178-alpha-beta-manifold|H-NEW-178]], [[h-new-193-q1-attractors|H-NEW-193]].
- **Fixed**: bonferroni k=2 (primary Quran-vs-Bukhārī; secondary
  muq-vs-non-muq). The five correlations are descriptive-exploratory
  (not Bonferroni-corrected) — disclosure.
- **Fixed**: Welch t (unequal variances) for primary, Mann-Whitney for
  secondary, consistent with [[h-new-178-alpha-beta-manifold|H-NEW-178]].
- **Fixed**: base-2 logarithms (bits).
- **Fixed**: H(L2|L1) (NOT H(L2|L1,L0)) as primary — bigram only.

## Pass/fail

- **PRIMARY PASS**: Quran-vs-Bukhārī Welch p < 0.025.
- **SECONDARY PASS**: muq-vs-non-muq Mann-Whitney p < 0.025.
- **MW-5 PASS**: shuffled Quran H_cond - unshuffled Quran H_cond ≥ 0.1 bits.
- Full test PASS iff primary & secondary & MW-5.
- PARTIAL if only one of primary/secondary passes AND MW-5 passes.
- NULL if neither primary nor secondary passes AND MW-5 passes.
- INSTRUMENT-BROKEN if MW-5 fails.

## Expected behavior under null

Under null (letter sequences behave as iid draws from unigram),
H_cond ≈ H_unigram. Arabic has strong phonotactic constraints, so real
texts show H_cond 1.0-2.0 bits below H_unigram. No prior on Quran vs
Bukhārī sign.
