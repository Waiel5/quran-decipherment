# [[h-new-209-pagerank-celebrated|H-NEW-209]] — Pre-registration

**Title:** PageRank verse-twin hubs cross-referenced with classical celebrated verses
**Date pre-registered:** 2026-04-17
**Seed:** 20260419
**Bonferroni k:** 1 (single outer test)
**α:** 0.05, α_corrected = 0.05

## Hypothesis

On the [[h-new-167-verse-twin-graph|H-NEW-167]] top-1 char-trigram Jaccard verse-twin graph (undirected, 6236
nodes), the top-50 verses by PageRank are enriched for classical celebrated
verses beyond what a uniform-random 50-subset of 6236 verses would produce.

## Pre-registered celebrated verse set (fixed BEFORE run)

Union (deduplicated) of:
- Q 1:1 basmala (absorbed into Q 1:1–1:7)
- Q 1:1–1:7 al-Fātiḥa (7 verses)
- Q 2:255 āyat al-kursī
- Q 24:35 āyat al-nūr
- Q 59:22–24 khawātim al-Ḥashr (3 verses)
- Q 112:1–4 al-Ikhlāṣ (4 verses)
- Q 113:1–5 al-Falaq (mu'awwidhatān, 5 verses)
- Q 114:1–6 al-Nās (mu'awwidhatān, 6 verses)

Total unique verses = 7 + 1 + 1 + 3 + 4 + 5 + 6 = **27**.

## Rules-tuple

(no-tashkeel; whitespace-collapsed; basmala-only-in-Q1) — inherited from
[[h-new-167-verse-twin-graph|H-NEW-167]].

## Graph construction

Top-1 char-trigram Jaccard twin per verse (ties broken by lower
(surah, ayah, idx)); symmetrised via undirected `nx.Graph`. Identical to
[[h-new-167-verse-twin-graph|H-NEW-167]].

## Scoring

`networkx.pagerank(g, alpha=0.85, max_iter=500, tol=1e-10)`. Rank all
verses descending; tie-break by (surah, ayah). Top-50 is the pre-registered
selection.

## Decision rule

Primary: hypergeometric one-sided P(X ≥ k_hits | N=6236, K=27, n=50) < 0.05.
Secondary (robustness): permutation test, 10,000 random 50-subsets, seed
20260419, p = (≥ observed + 1) / (N_perm + 1) < 0.05.

**Verdict logic:**
- PASS: both nulls reject.
- MIXED: exactly one rejects.
- FAIL: neither rejects.

## Garden of forking paths (disclosed)

Choices fixed before the run:
- Top-K = 50 (not varied).
- Celebrated set fixed by the task prompt (not re-curated after seeing
  results).
- PageRank α = 0.85 (NetworkX default; not tuned).
- Tie-breaking by canonical order (not by PR value precision).

I did not try alternative graph-construction schemes (top-2, weighted
Jaccard, tashkeel-preserving trigrams) — this is a single pre-registered
analysis on a single graph.

## Expected false-positive rate

Under H0, hypergeom P(X ≥ 1) with N=6236, K=27, n=50 ≈ 0.197; so observing
k ≥ 2 is needed to reject at α=0.05. The test is conservative.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-209.json`
- `findings/phase-b-hypotheses/csv/h-new-209-top50.csv`
- `findings/phase-b-hypotheses/h-new-209-pagerank-celebrated.md` (post-hoc)
