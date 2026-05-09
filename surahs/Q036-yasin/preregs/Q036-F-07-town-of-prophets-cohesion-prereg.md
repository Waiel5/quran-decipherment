---
finding_id: Q036-F-07
title: Q 36 Yāsīn vv. 13-32 — "town destroyed for rejecting prophets" lexical cohesion with parallel pericopes
date: 2026-05-09
phase: B+
seed: 20260509
type: pre-registration
status: locked-before-run
---

# Q036-F-07 — Q 36:13-32 lexical cohesion with Q 11:42-95 / Q 7:73-93 / Q 27:45-58 (parallel town-destruction pericopes) vs ambient Q 36

## 1. Background

Q 36:13-32 narrates the *aṣḥāb al-qarya* (Companions of the City) pericope: three messengers sent to a town, rejected, then divinely destroyed (with the believing man's salvation as the redemptive countersign). This is the longest sustained narrative in Q 36 (20 verses, ~24% of the surah by verse-count).

Parallel "town destroyed for rejecting prophets" pericopes elsewhere in the corpus include:
- **Q 7:73-93**: Thamūd / Madyan / Lūṭ destruction-after-rejection cycle.
- **Q 11:42-95**: extended Hūd/Ṣāliḥ/Lūṭ/Shuʿayb destruction-after-rejection cycle.
- **Q 27:45-58**: Thamūd + Lūṭ destruction-after-rejection cycle (shorter, in al-Naml).

**Pre-registered prediction**: the root-vocabulary of Q 36:13-32 shows higher Jaccard similarity to the union-root-set of {Q 7:73-93, Q 11:42-95, Q 27:45-58} than to the rest of Q 36 (vv. 1-12 + vv. 33-83), and that difference is significant under a permutation null.

## 2. Hypothesis

H₀ (null): root-Jaccard(Q 36:13-32, parallel-pericopes-union) ≤ root-Jaccard(Q 36:13-32, Q 36-ambient), i.e., the town-pericope vocabulary is NOT more aligned with parallel pericopes than with its own surah's ambient material.

H₁ (directional, pre-committed): root-Jaccard(Q 36:13-32, parallel-pericopes-union) **> root-Jaccard(Q 36:13-32, Q 36-ambient)**, AND this gap is significant at p ≤ 0.05 under a permutation null in which the 20 verses of Q 36:13-32 are replaced by 10,000 random 20-verse contiguous spans drawn from Q 36's 83 verses.

## 3. Direction (locked BEFORE observation)

- **PASS-DIRECTED**: J(pericope, parallel-union) > J(pericope, Q-36-ambient) AND p_perm ≤ 0.05.
- **NULL**: J(pericope, parallel-union) ≤ J(pericope, Q-36-ambient) OR p_perm > 0.05.
- **REVERSED**: J(pericope, parallel-union) < J(pericope, Q-36-ambient) by ≥ 0.05 in absolute difference → publish with full prominence.

## 4. Rules-tuple

`(no-tashkeel, QAC v0.4 stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi, verse-range-inclusive)`

Verse ranges:
- Q 36:13-32 (20 verses) — primary pericope.
- Q 7:73-93 (21 verses) — Thamūd-cycle.
- Q 11:42-95 (54 verses) — extended Hūd-Shuʿayb cycle.
- Q 27:45-58 (14 verses) — Thamūd/Lūṭ in al-Naml.
- Q 36-ambient = Q 36:1-12 + Q 36:33-83 (63 verses, all of Q 36 outside the test pericope).

Jaccard similarity:
`J(A, B) = |roots(A) ∩ roots(B)| / |roots(A) ∪ roots(B)|`

## 5. Procedure

1. Parse QAC v0.4 to extract (surah, verse, root) tokens.
2. Build root-sets for the 5 spans above.
3. Compute:
   - J₁ = J(Q 36:13-32, Q 7:73-93 ∪ Q 11:42-95 ∪ Q 27:45-58)
   - J₂ = J(Q 36:13-32, Q 36:1-12 ∪ Q 36:33-83)
   - Δ = J₁ − J₂ (pre-committed direction: positive)
4. Permutation null: for each of 10,000 trials, draw a random 20-verse contiguous span from Q 36 (valid start positions = 1..64), compute J(random-span, parallel-union) − J(random-span, Q 36-rest), and tally how many trials produce Δ_random ≥ Δ_observed.
5. Permutation p = (count of Δ_random ≥ Δ_observed + 1) / (10000 + 1).
6. Seed: 20260509.

## 6. Success criteria (PASS-DIRECTED)

- Δ > 0 (J₁ > J₂).
- p_perm ≤ 0.05.

## 7. NULL / REVERSED criteria

- Δ ≤ 0 → NULL (parallel-pericope alignment is no stronger than within-surah ambient alignment) → published with full prominence.
- Δ > 0 but p_perm > 0.05 → DIRECTIONAL-NULL (effect-direction correct but null-distribution-indistinguishable).

## 8. MW protections

- MW-1: Jaccard distance + root vocabulary pre-locked.
- MW-2: 10,000 permutations.
- MW-3: alternative-model = also compute the test using Q 11:42-95 alone (the longest parallel) AND the test using lemma vocabulary instead of stem-roots; report both as robustness.
- MW-5: replication = different verse-set definition of "parallel pericopes" (broader: {Q 7:73-93, Q 11:42-95, Q 26:105-191, Q 27:45-58, Q 54:9-42}) → should preserve direction.
- MW-6: instrument-control = also compute J(random-Meccan-pericope, parallel-union) − J(random-Meccan-pericope, source-surah-rest) for a few other 20-verse spans from Q 7, 11, 26 to confirm the test is calibrated.
- MW-7: post-hoc cap not triggered (pre-locked single test family).

## 9. Honest limits

- Q 11:42-95 dominates the parallel-union by sheer size (54 verses); the test should also report J₁ with Q 11:42-95 removed to check for size-dominance.
- The "town" pericopes have overlapping but not identical vocabulary; e.g., Q 36:13-32 uniquely contains the *muʾadhdhin* / believing-man motif (Q 36:20-27) that has no exact parallel in the named-prophet destructions of Q 7/11/27.
- Mass-shared theological roots (الله, ربب, رسل, ايي, قول) inflate Jaccard regardless of pericope content. A *novelty-only* control (J restricted to roots appearing < 20 times across the corpus) is a queued follow-up but POST-HOC.
- The 20-verse contiguous-span null is the natural choice for Q 36's 83-verse length; alternative shuffled-bag null is also queued as MW-3 robustness.

## 10. Seed and SHA

Seed: 20260509.
Pre-reg SHA-256 to be embedded into the run script at lock-time.
