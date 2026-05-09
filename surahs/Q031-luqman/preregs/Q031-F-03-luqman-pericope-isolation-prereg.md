---
test: Q031-F-03
title: Q 31:12-19 Luqmān-pericope lexical-isolation from rest of Q 31
test_type: TF-IDF block-isolation + permutation null
direction_locked: positive (Luqmān-pericope is more lexically distinct from rest-of-surah than random-spans of comparable length)
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q031-luqman-specialist (single test in family)
alpha_bon: 0.05 (single test, no Bonferroni)
acceptance_window:
  primary: TF-IDF block-isolation > 95th percentile of permutation null
date_locked: 2026-05-09
---

# Q031-F-03 — Pre-registration

## 1. Rationale

The Luqmān-pericope (vv.12-19) is the structural-content core of Q 31. It is hypothesized to be lexically distinct from the rest-of-Q31 (vv.1-11 + vv.20-34), because:
- It uses didactic-pedagogical vocabulary (yā bunayya, ḥikma, waṣṣaynā, mukhtāl, fakhūr, tuṣaʿʿir, etc.)
- It contains 3 yā-bunayya tokens (concentrated in 8 verses)
- It deploys the iltifāt voice-shift at vv.14-15 (interpolation-discontinuity)
- It includes 5+ Q 31-exclusive token-types (vocabulary unique to this surah).

The pre-registered direction: the Luqmān-pericope's TF-IDF lexical-isolation score should be HIGHER than random 8-verse spans drawn from elsewhere in Q 31.

## 2. Hypothesis

**H1**: cosine-distance(Luqmān-pericope-tokens, rest-of-Q31-tokens) > 95th percentile of cosine-distance(random-8-verse-span, rest-of-Q31).

This is operationalized as: TF-IDF cosine distance of the pericope's token-bag from the surah-rest token-bag is greater than that of 95% of random 8-verse contiguous spans of Q 31.

## 3. Method

- Tokenization: orthographic-token, no-tashkeel, basmala-counted-only-Q1.
- Token-bag: count-vector over types in the surah's token set.
- TF-IDF: term-frequency × inverse-document-frequency, with documents = the 8-verse span and rest-of-Q31. (Variation: rest-of-Q31 = vv.1-11 + vv.20-34 = 26 verses.)
- Cosine distance: 1 - cos(span_vec, rest_vec).
- Permutation null: 10,000 random contiguous 8-verse windows of Q 31 (range vv.1-27 valid starting indices, since 8 verses must fit in 34). Compute cosine distance between each random-span's token-bag and the corresponding rest-of-Q31 (Q 31 minus the span). Compute null distribution.
- One-tailed p = P(perm_isolation ≥ observed_pericope_isolation).

## 4. Pre-committed acceptance window

- PASS: perm-p < 0.05 (single-test α; no Bonferroni).
- DIRECTIONAL: perm-p ≥ 0.05 BUT observed > null mean.
- NULL: observed isolation ≤ null mean.

## 5. Garden-of-forking-paths log

- The pericope-bound (vv.12-19, 8 verses) is determined by classical scholarship (al-Biqāʿī, Ibn Kathīr) — independent of the permutation null. NOT post-hoc-tuned.
- The 8-verse-span comparator length is matched to the pericope length.
- The TF-IDF measure is one of several reasonable lexical-isolation measures; this is the pre-committed operationalization (consistent with Q037-F-02 specialist on Q 37 sacrifice-block).

## 6. Honest limits

- An 8-verse pericope in a 34-verse surah leaves only 26 verses for the rest-of-surah. The rest-of-surah is not tokenization-saturated — small samples produce noisier TF-IDF estimates.
- The pericope's distinctiveness is partly genre-driven (didactic vs cosmic-eschatological); this is an intrinsic structural-thematic property of Q 31, not an independent statistical signal.
- INDEPENDENT REPLICATION would require comparing Q 31:12-19 to a comparator-pericope (e.g. Q 18:71-82 al-Khaḍir-Mūsā wisdom discourse, Q 12:9-18 Yūsuf father-counsel) to test if the lexical-isolation generalizes across didactic-pericopes.

## 7. Direction lock

LOCKED positive (Luqmān-pericope > random 8-verse spans of Q 31).

## 8. SHA-locking

This pre-reg file's SHA256 will be computed at write-time and verified at run-time.

## 9. Cross-references

- [[surahs/Q037-al-saffat/06-novel-findings]] §Q037-F-02 — sacrifice-block isolation pre-reg template (this pre-reg follows the same structure).
- [[surahs/Q031-luqman/02-content-analysis]] §3 — Luqmān-pericope detailed verse-by-verse.
