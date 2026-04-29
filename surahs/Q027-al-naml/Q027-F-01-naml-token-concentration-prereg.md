---
finding_id: Q027-F-01
title: Naml-token (ant) concentration in Q 27 vs corpus
date_preregistered: 2026-04-28
phase: B+
---

# Q027-F-01 — Naml-token concentration

## Hypothesis
The Arabic surface forms of *naml* (ant) — namely the orthographic strings `النمل`, `نمل`, `نملة` (under no-tashkeel) — are concentrated overwhelmingly in Q 27, the surah whose name is *al-Naml*. Prediction: ≥ 80% of all corpus attestations occur in Q 27 (parallel to Q012-F-03, where *yūsuf* hit 92.6%).

## Null distribution
Permutation null: under H0, *naml*-tokens distribute proportional to surah token-length. With N_corpus *naml* attestations and surah-i length p_i = words_i / total_words, permuted concentration = max_i (k_i / N), where k_i ~ Multinomial(N, {p_i}).

## Direction (LOCKED before observation)
Concentration of *naml*-tokens in Q 27 will be > 80% (one-sided test, upper tail).

## Test statistic
`q27_concentration` = (# *naml*-tokens in Q 27) / (# *naml*-tokens corpus-wide).

## Permutation procedure
- Seed 42, 10000 permutations.
- Each permutation: redistribute observed total *naml*-tokens via Multinomial with p_i = words_i / total_words.
- Compute concentration on max-receiving surah.
- p-value = (1 + #(perm_concentration >= observed)) / (1 + n_perm).

## Bonferroni
k = 4 novel pre-registered tests in this surah investigation (Q027-F-01..04). α_corrected = 0.0125.

## Success criteria
- observed q27_concentration ≥ 0.80 AND p_perm < 0.0125.

## Failure criteria / pre-commit violation flags
- If q27_concentration < 0.80, declare DIRECTIONAL or NULL with full prominence.
- If reversed direction (Q 27 has near-zero), publish as NULL pre-commit-violation.

## Rules tuple
`(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Match strings: {`النمل`, `نمل`, `نملة`}. The token `نملي` (Q 3:178, root م ل ي *imlāʾ* "extension of respite") is EXCLUDED — different lexical root, ascertained by context.

## Anti-hallucination
- Corpus file: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Naml tokens computed from disk; values cited only after computation.
