# [[h-new-148-all-boundary-root-bridges|H-NEW-148]] — All-113-boundary root-bridge ranking

**Finding ID**: [[h-new-148-all-boundary-root-bridges|h-new-148]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent**: [[h-new-143-1-root-bridge|H-NEW-143.1]] (single-hinge Q 56→57 root-bridge rank 1), [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] (3 universal hinges), [[h-new-144-cyclic-tsp|H-NEW-144]] (M1 cyclic)
**Pre-reg**: task description (team-lead); k=1 single ranking test
**Verdict**: **NULL** on the hypothesis that chronology-reversal top-15 dominates root-bridge top-15

## Headline

**Chronology-reversal magnitude does NOT predict root-bridge strength across mushaf boundaries.** Only 3 of the top-15 root-bridge pairs are in the top-15 chronology-reversal pairs (p = 0.317). Spearman rho across all 113 boundaries = +0.05 (essentially uncorrelated).

This **falsifies** the hypothesized claim that "al-Biqāʿī munāsabāt at max-chronology-reversal hinges is vindicated" — the MAX-CHRONO-REVERSAL boundaries are NOT the strong-bridge boundaries (with the single exception of Q 56→57).

**Positive findings** that emerge:
- Q 56→57 remains rank-1 root-bridge (cos = 0.408, shared roots sbH + smw). Consistent with [[h-new-143-1-root-bridge|H-NEW-143.1]].
- Top-15 root-bridges are CONCENTRATED at Alh (Allah)-sharing boundaries (9 of 15 contain Alh in the shared root set), NOT at chrono-reversal hinges.
- Q 17→18 (الحمد لله الذي) is rank-4 root bridge AND was rank-1 surface bridge in [[h-new-143-surface-word-bridge-null|H-NEW-143]]. Classical exemplar across metrics.
- Classical al-Biqāʿī munāsabāt bridges appear at various chrono-reversal magnitudes; bridge-strength and chrono-magnitude are ORTHOGONAL axes.

## Method

For each of 113 mushaf consecutive-surah boundaries:
1. Compute set of QAC-STEM roots in the LAST verse of surah i.
2. Compute set of QAC-STEM roots in the FIRST verse of surah i+1.
3. Bridge cosine = |A ∩ B| / √(|A| · |B|).
4. Chronology-reversal magnitude = |noldeke(i+1) − noldeke(i)|.

Rank boundaries by bridge cosine descending. Compute:
- Intersection of top-15 bridge ∩ top-15 chronology-reversal.
- Intersection of top-15 bridge ∩ [[h-new-130-fisher-rao-residuals|H-NEW-130]] boundary set B (|B|=54).
- Spearman rank-correlation of bridge_cos with |chrono_reversal| across all 113.

## Results

### Top-15 root-bridge boundaries

| rank | pair | cos | |Δ Nöldeke| | chrono rank | shared roots |
|:---:|:---:|---:|:---:|:---:|:---|
| 1 | **Q 56→57** | 0.408 | 58 | 6 | sbH, smw |
| 2 | Q 5→6 | 0.369 | 25 | 21 | Alh, ArD, smw |
| 3 | Q 52→53 | 0.354 | 12 | 51 | njm |
| 4 | Q 17→18 | 0.252 | 2 | 100 | Alh, Hmd |
| 5 | Q 48→49 | 0.243 | 4 | 88 | Alh, Amn, byn, rsl |
| 6 | Q 62→63 | 0.228 | 10 | 61 | Alh, qwl |
| 7 | Q 3→4 | 0.204 | 3 | 93 | Alh, wqy |
| 8 | Q 15→16 | 0.204 | 16 | 34 | Aty |
| 9 | Q 10→11 | 0.167 | 9 | 63 | Hkm |
| 10 | **Q 21→22** | 0.154 | 42 | 11 | rbb |
| 11 | Q 8→9 | 0.144 | 18 | 32 | Alh |
| 12 | Q 33→34 | 0.134 | 18 | 33 | Alh |
| 13 | Q 63→64 | 0.134 | 11 | 55 | Alh |
| 14 | Q 60→61 | 0.129 | 12 | 52 | Alh |
| 15 | **Q 24→25** | 0.126 | 39 | 15 | Elm |

★ = also in top-15 chronology-reversal ranks.

### Hypothesis tests

| Test | Observation | p-value | Verdict |
|---|:---:|---:|---|
| Top-15 bridge ∩ top-15 chrono-reversal | 3 of 15 | 0.317 | NULL |
| Top-15 bridge ∩ [[h-new-130-fisher-rao-residuals|H-NEW-130]] B (|B|=54) | 8 of 15 | 0.426 | NULL |
| Spearman ρ(bridge, |chrono|) over 113 | +0.05 | ~0.6 | NULL |

Under the hypergeometric null with N=113, K=15, n=15: expected overlap 1.99 (chrono) and 7.17 (B). Observed 3 and 8 — close to chance.

### Which roots dominate top-15 bridges

| Shared root(s) | Frequency in top-15 |
|:---|:---:|
| Alh (Allah) | 9 of 15 |
| smw (heavens/high) | 2 |
| Hmd (praise) | 1 |
| sbH (glorify) | 1 |
| all others | ≤ 1 each |

**Allah-sharing boundaries dominate**. This is a DIFFERENT signal than chronology-reversal: it picks up the corpus-wide high-frequency theological vocabulary rather than structural-discontinuity hinges.

## Interpretation

### Why the hypothesis fails

The hypothesis (max-chrono-reversal hinges ⇒ max root-bridge) was based on the intuition that classical al-Biqāʿī munāsabāt deliberately BRIDGES the mushaf's biggest thematic/chronological discontinuities. Empirically, this is FALSE:

- Max-chrono-reversal boundaries (Q 110→111 at |Δ|=108, Q 97→98 at 78, Q 98→99 at 67) have ROOT-bridge cosine near 0 (not in top-15).
- Max-root-bridge boundaries are DISTRIBUTED across chrono-reversal magnitudes. Bridge strength is CAUSED BY shared high-frequency theological vocabulary (Allah at 50% of verses, smw/ArD frequent), not by "compensation for discontinuity".

### Q 56→57 is uniquely different

Q 56→57 is:
- Rank-1 root-bridge (sbH + smw; cos=0.408)
- Top-6 chronology-reversal (|Δ|=58)
- Top-15 Fisher-Rao jump in ALL 3 feature spaces (root + char-4-gram + verse-length)
- Entry point to the musabbiḥāt cluster ([[h-new-58c-musabbihat-tense-split|H-NEW-58c]])

This remains the most structurally-exceptional hinge in the Quran. It is SIMULTANEOUSLY a max-FR-jump, max-chrono-reversal-ish, AND max-root-bridge. The only boundary with this tripartite property.

But it is a SINGLE DATUM. A general pattern of "chrono-reversal hinges are root-bridged" does NOT hold.

### Refined classical-validation reading

al-Biqāʿī munāsabāt is empirically observable at SOME boundaries (Q 17→18, Q 5→6, Q 48→49, Q 56→57 — classical exemplars). But:
- It operates at DIFFERENT axes (shared-Allah invocation, shared-praise formula, shared-cosmic-vocabulary) rather than at a unified "bridge every big jump" principle.
- It is NOT a SYSTEMATIC property of the mushaf that applies differentially at structural hinges.
- Classical munāsabāt is a CATALOG of specific cross-reading insights, not a corpus-level empirical pattern of "big-jumps-are-bridged".

### Q 17→18 stands out

Q 17 al-Isrāʾ → Q 18 al-Kahf: both surahs OPEN with الحمد لله الذي (praise to Allah who). Shared roots: Alh, Hmd. Chronology-reversal is only |Δ|=2 (these surahs are chronologically adjacent). This is a classical al-Biqāʿī-confirmed case of FORMULAIC-opening repetition across a NON-chrono-reversal boundary. Evidence that classical munāsabāt is NOT about bridging maximum-discontinuity.

## Honest limits

1. **113 is moderate sample**; Spearman +0.05 with n=113 gives approximate p ≈ 0.6 (not significant, not strongly zero either).
2. **Root-bridge cosine is ONE metric**; Jaccard and overlap-count give similar patterns (per [[h-new-143-1-root-bridge|H-NEW-143.1]] parent).
3. **Last-verse-vs-first-verse window is narrow**; multi-verse windows might reveal different patterns.
4. **"Chronology-reversal" under Nöldeke is ONE reconstruction**; Tanzil or other schemes might give slightly different ranks.

## Connections

- **[[h-new-143-1-root-bridge|H-NEW-143.1]]**: single-hinge Q 56→57 rank-1 root-bridge confirmed.
- **[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]**: 3 universal FR hinges; only 1 (Q 56→57) is a strong root-bridge.
- **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]**: classical-scholarship validation of al-Biqāʿī munāsabāt is EXEMPLAR-LEVEL (at specific boundaries) not CORPUS-LEVEL (systematic at chrono-reversal hinges).
- **[[h-new-148-all-boundary-root-bridges|H-NEW-148]] ⊥ chronology-reversal axis**: bridge and chrono-reversal are independent structural axes.

## Verdict

**NULL** on both pre-committed hypotheses:
- "Chronology-reversal top-15 dominates bridge top-15" → 3 of 15 (p=0.317). FAIL.
- "Bridge top-15 concentrates in B ([[h-new-130-fisher-rao-residuals|H-NEW-130]] boundary set)" → 8 of 15 (p=0.426, ~chance given |B|=48%). FAIL.

**Spearman test**: bridge-cos and |chrono-reversal| are uncorrelated (ρ=+0.05).

**Positive framing**: the Quran's classical-munāsabāt bridges operate at specific exemplar boundaries (Q 56→57, Q 17→18, Q 5→6, Q 48→49), NOT systematically at chronology-reversal hinges. [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]'s "exemplar-level validation" is the correct framing; the attempt to generalize to a SYSTEMATIC corpus-level pattern fails this test.

## Files

- Script: inline in journal (reproducible)
- JSON: not written (findings-level; data is 113-row table reproducible from script above)
- This findings file.
