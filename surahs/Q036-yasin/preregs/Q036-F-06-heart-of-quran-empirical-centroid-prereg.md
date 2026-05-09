---
finding_id: Q036-F-06
title: Q 36 Yāsīn — "Heart of the Qurʾān" empirical FR-centroid audit
date: 2026-05-09
phase: B+
seed: 20260509
type: pre-registration
status: locked-before-run
---

# Q036-F-06 — Is Q 36 the corpus FR-centroid (empirical "heart" by mean Fisher–Rao distance)?

## 1. Background

The classical *qalb al-Qurʾān* tradition (al-Tirmidhī idInBook=2970, isnād-weak per al-Tirmidhī himself) names Q 36 as the "heart of the Qurʾān". [[h-new-82-yasin-heart|H-NEW-82]] already tested this on 6 different operationalisations of "centrality" and found Q 36 ranks #1 on 0/6 axes. Q036-F-01 (the local Q 36 specialist's 2026-04-28 7th-axis salvage attempt with liturgy-weighted Jaccard) was also NULL.

This pre-reg adds **one more axis**: the corpus Fisher–Rao distance centroid. The pre-committed prediction is binding: Q 36 is **NOT** the corpus FR-centroid; rather, that distinction belongs to Q 112 al-Ikhlāṣ (per [[h-new-1220-fr-centroid-q112]] and the project's standing reading of `h-new-111.json`).

## 2. Hypothesis

H₀ (null): Q 36 has the minimum mean Fisher–Rao distance to all other surahs (i.e., Q 36 is the corpus FR-centroid).

H₁ (pre-committed direction): Q 36 is **NOT** the FR-centroid. The corpus FR-centroid is **Q 112 al-Ikhlāṣ** (or another surah with very few but high-frequency theological roots, e.g., Q 109 / Q 113 / Q 114). Q 36's rank on the FR-centroid ordering is mid-pack (rank ≥ 30 of 114).

## 3. Direction (locked BEFORE observation)

- **PRE-COMMITTED PREDICTION**: Q 112 ranks 1 (or in the top 3) on min(mean FR distance to corpus); Q 36 ranks ≥ 30.
- **PASS-DIRECTED (the prediction holds)**: Q 112 in top-3 AND Q 36 outside top-30. Verdict: H-NEW-82 reaffirmed on a 7th axis = FR-distance centrality.
- **REVERSED (the prediction fails)**: Q 36 in top-3 OR Q 112 outside top-10. Publish as NULL with full prominence and flag as pre-commit reversal.

## 4. Rules-tuple

`(no-tashkeel, QAC v0.4 stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Fisher–Rao distance computed on the root-frequency probability simplex (unit-L1-normalised root vectors per surah), Hellinger-equivalent on the simplex:
`d_FR(p, q) = 2 · arccos(Σᵢ √(pᵢ · qᵢ))`

## 5. Data sources

- `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC stem-root annotations, ROOT: field)
- `findings/phase-b-hypotheses/csv/h-new-111.json` (corpus-stats sanity check)

## 6. Procedure

1. Parse QAC v0.4 to extract (surah, root) tokens. Build per-surah root frequency vectors over the global root vocabulary (~1642 distinct roots per `h-new-111.json` corpus_stats).
2. L1-normalise each surah's vector to a probability simplex.
3. Compute 114×114 Fisher–Rao matrix.
4. For each surah s, compute `mean_FR(s) = (1/113) · Σ_{t≠s} d_FR(s, t)`.
5. Rank surahs by ascending mean_FR. Surah with min mean_FR is the empirical FR-centroid.
6. Record Q 36's rank and Q 112's rank.

## 7. Success criteria (PASS-DIRECTED)

- Q 112 mean_FR rank ∈ {1, 2, 3} — top-3.
- Q 36 mean_FR rank ≥ 30.

Both must hold for PASS-DIRECTED-REAFFIRMED.

## 8. NULL / REVERSED criteria

- Q 36 in top-3 → REVERSED (pre-commit violation).
- Q 112 outside top-10 → partial NULL (the literature's standing identification of Q 112 as FR-centroid is shaken).

## 9. MW protections

- MW-1: FR distance pre-locked.
- MW-2: deterministic computation (no permutations); corpus-prior is the natural mean.
- MW-3: alternative model = also compute median FR distance per surah; both should put Q 112 high and Q 36 mid.
- MW-5: cross-check ranks against h-new-111c (verse-length FR variant) — should be qualitatively consistent (Q 36 mid, Q 112 high in centroid-rank).
- MW-7: post-hoc cap not triggered (single pre-locked metric).

## 10. Honest limits

- Q 112 wins on FR-centroid largely because of its short length and theological-core vocabulary (high-frequency roots `Alh`/`Hd`/`SmD`/`wld` overlap with most surahs). FR-centroid is therefore a **short-and-thematically-broad** signature, not a "heart" in any rhetorical sense.
- The metric is unweighted for liturgy; the liturgy-weighted version was already tested and NULL'd by Q036-F-01.
- A length-normalised cosine variant (queued but POST-HOC) might yield a different centroid; the binding result here is unweighted FR.

## 11. Seed and SHA

Seed: 20260509 (n/a for deterministic test).
Pre-reg SHA-256 to be embedded into the run script at lock-time.
