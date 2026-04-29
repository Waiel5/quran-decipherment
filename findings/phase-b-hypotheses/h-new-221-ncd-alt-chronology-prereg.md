---
finding_id: h-new-221
title: Cross-feature replication of H-NEW-212 under NCD (Normalized Compression Distance)
status: pre-registered
bonferroni_family: h-new-221
bonferroni_k: 3
alpha_bon: 0.0167
seed: 20260419
permutations: 10000
date_prereg: 2026-04-17
parent_lineage: H-NEW-169 (NCD-lzma mushaf test), H-NEW-212 (Fisher-Rao alt-chronology test)
---

# [[h-new-221-ncd-alt-chronology|H-NEW-221]] — Alternative chronologies under NCD (Normalized Compression Distance)

## Motivation

[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] established under Fisher-Rao (QAC STEM root probability vectors,
K=500 top roots, Dirichlet-smoothed, angular distance) that the mushaf order
has path length SHORTER than Egyptian 1924, Bell 1937 and Blachère 1947 —
with all three p < 0.0167 under the null, and mushaf rank-1 over all five
orderings (incl. Nöldeke-Schwally 1860 reference). This used a PARAMETRIC
feature space: token counts → Dirichlet-smoothed probabilities → angular
distance in a statistical simplex.

[[h-new-221-ncd-alt-chronology|H-NEW-221]] replicates the same 3-chronology family under a NON-PARAMETRIC
information-theoretic feature space: **Normalized Compression Distance**
using lzma (preset=9|EXTREME), zero-byte separator, arithmetic-mean
symmetrization. The D-matrix is loaded directly from [[h-new-169-ncd-mushaf|H-NEW-169]]'s
`csv/h-new-169-ncd-matrix.npy` (114×114, 0-indexed).

If mushaf beats Egyptian / Bell / Blachère at NCD as well, that is
non-parametric evidence that the mushaf-organizing-principle is
**CODE-INDEPENDENT** (not QAC-stem-specific, not Dirichlet-specific, not
K=500-specific). This extends [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] and [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] to THREE
INDEPENDENT feature spaces vs chronology:
  (i)   QAC STEM root Fisher-Rao ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] / 212 basis)
  (ii)  char-4gram K=2000 Fisher-Rao ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] basis)
  (iii) NCD-lzma (non-parametric, this hypothesis)

## Pre-registered tests (Bonferroni k=3, α_bon=0.05/3=0.0167)

  PRIMARY-1 — L_egyptian < L_random (1-sided lower, perm p < 0.0167)
  PRIMARY-2 — L_bell     < L_random (1-sided lower, perm p < 0.0167)
  PRIMARY-3 — L_blachere < L_random (1-sided lower, perm p < 0.0167)

Nöldeke-Schwally 1860 and mushaf are reported as descriptive references
(not members of the Bonferroni family — same convention as [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]).

## Secondary (descriptive, not hypothesis-level)

- Leaderboard over all 5 orderings (shortest wins)
- Mushaf rank among 5
- Pairwise path-length diffs L_c − L_mushaf in null-SD units
- Cross-feature concordance vs [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] (does the leaderboard preserve
  order under NCD?)

## Data sources / integrity

- `findings/phase-b-hypotheses/csv/h-new-169-ncd-matrix.npy` (NCD D-matrix,
  SHA-256 logged)
- `data/revelation-order.csv` (mushaf_order, revelation_order=Egyptian-1924,
  noldeke_order)
- Bell / Blachère rank tables: hard-coded inside the [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] script, reused
  verbatim here (same ties and imputations) — SHA-256 of script logged so
  any drift is detectable.

## Data-quality caveats (inherited from [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]])

- Bell s15 imputed rank 52 (coded "M" not numeric in French Wikipedia source)
- Bell s81/s82 both rank 15 → mushaf-order secondary
- Blachère s80/s84 both rank 24 → mushaf-order secondary

## Null

10,000 uniform permutations of surah IDs 1..114, seed 20260419 (matches
[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] seed; null is still independent because D-matrix differs). One-sided
lower p-value: `(#{L_perm ≤ L_ordering} + 1) / (PERMS + 1)`.

## Verdict rule

- Any PRIMARY-i passes iff its p < α_bon = 0.0167.
- Report family_any_pass and mushaf_still_wins_over_all_3_chronologies.
- NO directional inference beyond mushaf-vs-chronology here — this is a
  replication, not a forking discovery path.

## Output

`csv/h-new-221.json` and `[[h-new-221-ncd-alt-chronology|h-new-221]]-ncd-alt-chronology.md` report.
