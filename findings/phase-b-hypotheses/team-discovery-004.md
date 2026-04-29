---
finding_id: H-NEW-4
title: Muqaṭṭaʿāt-opening surahs do NOT show accelerated lexical-introduction vs length-matched non-muqaṭṭaʿāt
date: 2026-04-12
rules_tuple:
  orthography: no-tashkeel (verse text) + QAC v0.4 morphology for lemmas
  word_definition: QAC STEM lemma (LEM field)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
null_model: length-stratified (deciles) label permutation, 2000 draws
acceptance_criterion: Bonferroni-corrected p < 0.005 at ANY checkpoint (k=6) for positive confirmation
verdict: REFUTED
---

## Claim

The 29 muqaṭṭaʿāt-opening surahs (2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68) exhibit a DISTINCT lexical-introduction curve vs non-muqaṭṭaʿāt surahs matched for length. Specifically: faster type-token-ratio (TTR) in the early portion of the surah — a "lexical header" effect beyond the known letter-density finding.

## Method

- QAC v0.4 gives per-token STEM lemmas (LEM field). Per-surah lemma sequence in textual order.
- At checkpoints t ∈ {50, 100, 200, 500, 1000, 2000} tokens, compute TTR = unique_lemmas(first t) / t.
- Compare mean TTR for muqaṭṭaʿāt vs non-muqaṭṭaʿāt surahs at each checkpoint.
- **Length-stratified label permutation** (10 deciles by length), 2000 draws, to control for length effects.
- Apply Bonferroni with k=6 checkpoints: threshold α/6 = 0.00833.

## Results

| Checkpoint t | n_muq | n_non_muq | TTR(muq) | TTR(non_muq) | obs diff | z (strat. perm) | p_ge |
|---|---|---|---|---|---|---|---|
| 50 | 29 | 85 | 0.787 | 0.785 | +0.002 | +1.96 | 0.033 |
| 100 | 29 | 55 | 0.696 | 0.703 | −0.008 | +1.34 | 0.091 |
| 200 | 29 | 42 | 0.604 | 0.598 | +0.006 | +1.08 | 0.144 |
| 500 | 24 | 21 | 0.469 | 0.478 | −0.009 | **−1.03** | 0.849 |
| 1000 | 11 | 13 | 0.376 | 0.385 | −0.009 | **−1.29** | 0.897 |
| 2000 | 3 | 4 | 0.285 | 0.283 | +0.003 | NaN | — |

## Verdict: REFUTED

- No checkpoint produces a corrected p < 0.00833 (Bonferroni).
- The strongest raw p is cp=50 at p=0.033 — not surviving correction.
- At cp=500 and cp=1000, the **direction reverses**: muqaṭṭaʿāt surahs have slightly LOWER TTR (more lemma repetition) than length-matched non-muqaṭṭaʿāt. This is contrary to the "front-loaded" claim.
- The muqaṭṭaʿāt phenomenon does NOT manifest as accelerated lexical novelty. Its distinctiveness is at the **letter/phonological level** (already documented in prior findings), not at the lexical level.

## Interpretation

Muqaṭṭaʿāt surahs, after stripping their letter-opener, are lexically indistinguishable from length-matched non-muqaṭṭaʿāt prose. The semantic content after the letters follows ordinary Quranic vocabulary-growth kinetics. This:
- Supports the view that muqaṭṭaʿāt are a **formal opener**, phonetically and graphemically distinctive, without a downstream lexical signature.
- Refutes the "lexical-header" conjecture (that muqaṭṭaʿāt mark content-dense openings).
- Is consistent with al-Suyūṭī's treatment of muqaṭṭaʿāt as a separate *nawʿ* — they are a formal device, not a rhetorical-semantic one.

## Garden of forking paths disclosure

### Choices made after seeing the data
- None. Stats and null model pre-registered.

### Alternative rule tuples
- Could have used word tokens (orthographic) instead of QAC lemmas. Lemma-level is the more semantically meaningful unit for a vocabulary-introduction claim.
- Could have compared against Markov-surrogate corpus rather than length-matched surahs. Length-matched is the stricter relevant comparison.

### Sibling hypotheses
- Letter-density signature (already tested in prior findings) — that IS significant for muqaṭṭaʿāt.
- Root-introduction rate (distinct from lemma): NOT tested; adjacent hypothesis.

### Why this one and not those
- The claim is specifically about lexical (lemma) introduction rate. Switching to roots would be a different hypothesis.

## Seed
`random.seed(20260413)`. Raw: `scratch/team-discovery/result-004.json`.
