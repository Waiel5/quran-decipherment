---
test_id: Q022-F-08
title: "Q 22's two sajda verses (22:18, 22:77) are at major within-surah block-boundaries"
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q022-F-08-sajda-block-boundary
alpha_bon: 0.025
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-08 Pre-registration — Q 22 sajda verses at block-boundaries

## Hypothesis

The two Q 22 sajda verses lie at structurally salient positions within the surah:
- **22:18** is the cosmic-roll-call prostration ("Do you not see that to Allāh prostrates whoever is in the heavens and earth — the sun, the moon, the stars...") — at the end of the opening cosmological-eschatological block (vv. 1-18) and immediately before the disputants-of-God block (vv. 19-24).
- **22:77** is the imperative-prostration ("O you who believe, bow and prostrate and worship your Lord") — at the start of the closing exhortation block (vv. 77-78), immediately after the ḥajj-and-jihād thematic core (vv. 25-76).

Classical *munāsaba* writers (al-Biqāʿī, *Naẓm al-Durar*, vol. 5 on Q 22; al-Rāzī, *Mafātīḥ al-ghayb* on Q 22:77) treat both verses as structural pivots.

If this is structurally encoded, the verse-to-verse content-similarity DELTAS around vv. 18 and 77 should rank in the upper 30% of the surah's 77 inter-verse deltas (high delta = block boundary).

## Pre-committed prediction

**Direction-locked**: For verse v in {18, 77}, at least one of the adjacent deltas (v-1 → v, v → v+1) ranks in the **TOP 30% of all 77 inter-verse deltas** in Q 22 (i.e., ≤ rank 23 by descending-delta = top-30% boundary).

## Tests (Bonferroni-2 family, α_bon = 0.025)

For each target verse v ∈ {18, 77}:

1. **T(v)**: Compute deltas d(v-1, v) = 1 − cos(TF(v-1), TF(v)) and d(v, v+1) = 1 − cos(TF(v), TF(v+1)).
   - PASS(v) if min(rank(d(v-1,v)), rank(d(v,v+1))) ≤ 23 (top-30%).

2. **Permutation null context**: 10,000 random verse-position assignments — what fraction of random pairs are top-30%? Baseline: ~30% by definition. The Bonferroni-2 protection is for the two-verse family, not the within-surah permutation.

## Tokenization

- Source: `quran-text/quran-no-tashkeel.json`, surah index 21 (Q 22).
- Strip Arabic-script annotation marks (sajda glyph ۩, pause marks ۚ ۖ ۗ ۘ ۛ ۜ ۠ ۡ ۤ ۦ ۧ ۨ ۭ).
- Tokens: whitespace-separated word-forms (orthographic-token level).
- TF vectors with cosine similarity.

## Direction-of-effect lock

Predicted: PASS for BOTH v = 18 AND v = 77.
If FAIL for either or both, publish as NULL or DIRECTIONAL per scoring below.

## Success criteria

- VINDICATED: BOTH v18 AND v77 pass at α_bon = 0.025 (both have at least one adjacent delta in top-30%).
- DIRECTIONAL: ONE of v18, v77 passes.
- NULL: NEITHER passes.

## Garden-of-forking-paths log

- BEFORE running: chose "at least one adjacent delta in top-30%" because a sajda-verse can be a boundary if it OPENS a new block (delta on v-1→v) OR CLOSES one (delta on v→v+1); requiring both would over-constrain.
- BEFORE running: top-30% threshold chosen because Q 22 has 77 inter-verse deltas and 30% (≈ 23 boundaries) yields a non-trivial discrimination — 70% of deltas are "not-boundary."
- BEFORE running: word-level TF cosine chosen over root-level because block-boundary in classical *munāsaba* is at SURFACE thematic shift (vocabulary change), not abstract root pattern.
- BEFORE running: locked v = 18, 77 from al-Suyūṭī's enumeration (nawʿ 30) and al-Tirmidhī #578; the prediction does NOT depend on adopting the Mālikī single-sajda position.
- Pilot-information acknowledgment: a pilot run of this test was performed during scaffolding; pilot results were not used to adjust the pre-reg threshold. The 30% threshold was locked from the analytical reasoning above. Pilot revealed that v77 PASSES on both adjacent deltas (both rank ≤ 22/77) while v18's adjacent deltas rank ~66-69/77 (LOW deltas — v18 is in a thematically continuous cosmic block). This makes the predicted "VINDICATED on both" likely to fail; it will be reported as a SPLIT result (DIRECTIONAL with v77 passing, v18 failing). The pre-commit direction stands.

## Honest limits

- 77 inter-verse deltas in a single surah is a small-N within-surah test. The top-30% threshold is not a strict statistical significance; it's a descriptive structural-boundary criterion.
- Inter-verse cosine on short verses (Q 22 has many 5-15 word verses) yields high deltas mechanically due to vocabulary sparsity. Long-verse Q 22 may have inflated boundary deltas.
- The hypothesis is binary per verse (boundary / not-boundary). A more granular test would examine multi-verse window similarity.
