---
finding_id: Q018-F-01
title: "Q 18 four-narrative architectural balance — word-count parity test"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 18001
n_perm: 10000
bonferroni_k: 3
alpha_raw: 0.05
alpha_bonferroni: 0.0167
direction: balanced (no-direction-locked); two-tailed
---

# Q018-F-01 — Four-narrative architectural balance

## Hypothesis

Q 18 is the corpus's canonical four-narrative surah. The H-NEW-268 locked four-narrative blocks are:
- **N1** Aṣḥāb al-Kahf, vv. 9-26 (length 18 verses)
- **N2** Two gardens, vv. 32-44 (length 13 verses)
- **N3** Mūsā-Khaḍir, vv. 60-82 (length 23 verses)
- **N4** Dhū al-Qarnayn, vv. 83-101 (length 19 verses by classical reading; 16 by H-NEW-268 conservative endpoint)

The published H-NEW-268 finding establishes that the START-INDEX geometry has a real palindromic-expansion signature (gaps 23-28-23) at p = 0.008 Bonferroni-3. The complementary question is the **WORD-COUNT BALANCE**: are the four narratives equal in word-count, or asymmetric? This is not a verse-index test (already done) but a content-volume test.

## Operational definition

For each narrative N1..N4, compute:
- `n_verses_N`
- `n_words_N` (no-tashkeel orthographic, mushaf-marks-stripped)
- `n_root_tokens_N` (QAC v0.4)

Three balance statistics:
1. **Cell A — verse-count balance**: `max_verse_count / min_verse_count` ratio across the four narratives. Lower ratio = more balanced.
2. **Cell B — word-count balance**: `max_word_count / min_word_count` ratio.
3. **Cell C — root-token-count balance**: `max_root_token_count / min_root_token_count` ratio.

Locked block-end for N4: v. 101 (al-Ṭabarī classical reading), giving N4 = vv. 83-101 = 19 verses. (The H-NEW-268 conservative endpoint v. 98 gives 16; we use the classical endpoint here for content-volume purposes.)

## Null distribution

For each balance statistic, generate 10,000 permutation nulls by:
- Drawing 4 random non-overlapping blocks from Q 18 with the same verse-count tuple (18, 13, 23, 19) — using the same exact-ordered-placement null as H-NEW-268.
- Computing the same balance statistic.

p-value = P(observed_ratio ≤ random_ratio) (one-tailed, since we test "more balanced than random").

## Direction (LOCKED)

**Direction**: `observed_ratio < median(null)`. We test whether the four narratives are *more balanced* (lower max/min ratio) than randomly-placed blocks of the same lengths.

Pre-commit violation: if `observed_ratio > median(null)`, the narratives are *less balanced* than random, and we report this as a NULL with prominence.

## Success criteria

For each cell A, B, C independently:
- p_one_tailed < α_Bonferroni = 0.05 / 3 = 0.0167: **CONFIRMED** for that cell.
- 0.0167 < p < 0.05: **DIRECTIONAL** for that cell.
- p ≥ 0.05: **NULL** for that cell.

Combined verdict: "CONFIRMED on N/3 cells".

## Failure criteria

- Observed ratio > median(null): pre-commit violation, NULL with prominence.
- All three cells fail: full NULL.

## Rules-tuple

`(no-tashkeel, orthographic-word for word-count; QAC v0.4 stem-roots for root-token; basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-marks-stripped)`.

## Expected behavior under H1

If the four narratives are deliberately balanced, the empirical max/min ratio should be at the *low* end of the null distribution. Note: the verse-count tuple (18, 13, 23, 19) gives max/min = 23/13 = 1.77 — not particularly balanced *as verses*. The interesting question is whether word-count or root-token-count balance is *better* than the verse-count balance suggests, indicating compensating word-density per verse.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q018_F_01_narrative_balance.py`.
- JSON: `csv/Q018-F-01.json`.
- Findings: `06-novel-findings.md` Q018-F-01 section.
