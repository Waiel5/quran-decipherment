---
surah: 38
test_id: Q038-F-04
title: David-Solomon-Job triad — trial-by-power/wealth/health thematic signature in Q 38:17-44
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 2
bonferroni_family: Q038-F-04-davidic-triad
alpha_bon: 0.025
---

# Q038-F-04 — Pre-registration: David-Solomon-Job inner-triad coherence

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** The Q 38:17-44 inner sub-sequence (David vv. 17-26 → Solomon vv. 30-40 → Job vv. 41-44) forms a coherent **trial-by-X** thematic block, where X cycles power/justice (Dāwūd) → wealth/dominion (Sulaymān) → health/patience (Ayyūb). Distinguishing signature: the triad is **internally lexically coherent** (above-baseline TF-IDF cosine on Q 38-internal vocabulary) AND distinct from the Q 38:1-16 (Quraysh-polemic) and Q 38:45-88 (Abrahamic-cycle + eschatology) blocks.

**H0:** The triad is no more internally cohesive than random size-matched verse-blocks within Q 38.

**Direction:** triad_internal_cohesion > permutation null mean (LOCKED). Triad's internal cohesion exceeds Q 38's other blocks at p < α_bon.

## 2. Operational definition

**Triad-block**: Q 38:17-44 (28 verses).
**Block-A (Quraysh-polemic)**: Q 38:1-16 (16 verses).
**Block-C (Abrahamic + eschatology)**: Q 38:45-88 (44 verses).

**Test 1 — Internal cohesion:** TF-IDF on Q 38-internal vocabulary (no-tashkeel orthographic-tokens, IDF computed across the 88 verses); compute mean pairwise cosine similarity within the triad. Permutation null: 10000 shuffled re-assignments of which 28 verses constitute the "triad" sample, drawn without replacement from Q 38's 88 verses.

**Test 2 — Triad-vs-other-blocks distinctness:** Compute mean pairwise cosine similarity for triad and for each of blocks A and C. Pre-committed direction: triad cohesion > 0.5 × (block-A + block-C cohesion).

**Bonferroni**: 2 tests (test 1 cohesion + test 2 distinctness), α_bon = 0.025.

## 3. Test statistic

- Test 1 primary: triad mean pairwise TF-IDF cosine; null: 10000 random 28-verse samples from Q 38; one-tailed p_greater.
- Test 2 primary: triad cohesion / mean(blockA cohesion, blockC cohesion); pre-committed > 1.0.

## 4. Success / Failure

- **Strict success (CONFIRMED)**: both tests pass at α_bon = 0.025.
- **Directional**: 1 of 2 passes.
- **NULL**: 0 of 2 pass.
- **Pre-commit violation**: triad cohesion BELOW null mean (would indicate the triad is internally dispersed, falsifying the trial-by-X hypothesis).

## 5. Honest limits known a priori

- The triad spans 28 verses — modest power; this is the largest ad hoc thematic block we can isolate, but TF-IDF on this scale is power-limited.
- The verse-boundaries (David vv. 17-26 ends, then 27-29 are short generalizations, Solomon starts at 30) — the test treats vv. 17-44 as a single block, accepting that vv. 27-29 are "transition material." Pre-committed alternative: include vv. 27-29 (treated as Davidic coda) in the triad.
- The Quran does not formally identify these three as a "trial trilogy"; this is a synthetic-literary reading. The classical tafsir (al-Ṭabarī, al-Rāzī, Ibn Kathīr) treats them as separate prophet-vignettes. The test is whether the synthetic reading has empirical support — DOWNGRADED to a hypothesis-generating rather than a hypothesis-confirming test.
- The Q 38 narrative is a synthetic compilation; the test asks whether the COMPILER (whoever assembled Q 38) placed these three vignettes adjacently because of trial-by-X coherence, OR whether the adjacency is incidental.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, TF-IDF on Q 38-internal vocabulary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q038_F_04_davidic_triad.py`.
