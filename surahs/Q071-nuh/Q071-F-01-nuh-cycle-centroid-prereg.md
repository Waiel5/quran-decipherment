---
finding_id: Q071-F-01
title: Q 71 Nūḥ as the lexical CENTROID / anchor of the Nūḥ-pericope cycle (H-NEW-2260 extension)
parent_finding: H-NEW-2260 (prophet-cycle pericope parallelism — Nūḥ PASS z=+2.51)
date_pre_registered: 2026-05-30
seed: 20260509
n_perm: 10000
agent: Q 71 Nūḥ specialist (Waiel Al-Shujaa)
test_type: within-cycle centrality rank (Arm A) + length-matched anchor-swap permutation null (Arm B)
bonferroni_family: Q071-novel-tests-2026-05-30
bonferroni_k: 2
alpha_bon: 0.025
direction_locked: "Q 71 (the dedicated Nūḥ surah) is the MOST-CENTRAL pericope of the Nūḥ cycle (Arm A rank == 1) AND its mean intra-cycle root-Jaccard EXCEEDS a length-matched random-anchor null (Arm B z > 0, one-sided greater)"
acceptance_window: "Arm A: Q 71 centrality-rank == 1 of 6. Arm B: p_perm <= alpha_bon = 0.025 with z > 0 (Q 71 actual centrality above random-anchor null)."
mw5_positive_control: "Mūsā cycle centroid recomputed on the same pipeline (H-NEW-2260 stored Jaccards) — sanity that the centrality machinery ranks pericopes monotonically."
mw6_instrument_control: "random-28-verse window drawn from the corpus replaces Q 71 as the cycle's 6th member (anchor-swap null), 10000 draws."
mw7_internal_check: "reproduce the 15 stored H-NEW-2260 Nūḥ pairwise Jaccards from QAC v0.4 ROOT before computing centrality (run-time assertion, tol 1e-9)."
---

# Q071-F-01 — Is Q 71 the lexical CENTROID / anchor of the Nūḥ-pericope cycle?

## 1. Motivation

H-NEW-2260 established that the **Nūḥ pericope cycle** {Q 7:59-64, Q 11:25-49,
Q 23:23-30, Q 26:105-122, Q 54:9-17, **Q 71:1-28**} coheres at pericope scale:
mean pairwise QAC-ROOT Jaccard J=0.1805, z=+2.51, p_perm=0.0087 (PASS-DIRECTED,
Bonferroni-3). The conserved core was the concrete flood lexicon `flk` (ark),
`grq` (drowning), `njw` (deliverance), plus the rejection roots `qwm`/`mlA`/`k*b`.

Q 71 is the corpus's **only whole-surah dedicated to the Nūḥ narrative** — the
single surah that bears the prophet's name and tells his story end-to-end. The
*natural, intuitive* hypothesis a reader forms is that this dedicated surah is the
**hub / centroid / anchor** of the cycle: the lexical reservoir from which (or
toward which) the scattered cross-surah retellings draw. This test makes that
intuition falsifiable.

## 2. Hypothesis (direction LOCKED before observation)

**H1 (the intuitive, locked direction):** Q 71 is the MOST-CENTRAL pericope of the
Nūḥ cycle — it has the highest mean pairwise root-Jaccard to the other five
pericopes (Arm A: centrality-rank == 1 of 6) — and its observed mean intra-cycle
Jaccard exceeds what a length-matched random window contributes when swapped in as
the cycle's sixth member (Arm B: z > 0, one-sided greater, p_perm ≤ α_bon).

**H0 (null):** Q 71 is not the centroid (rank > 1), and/or a length-matched random
anchor reproduces Q 71's intra-cycle centrality (Arm B p_perm > α_bon).

Direction is LOCKED toward H1 (Q-71-as-centroid). If Q 71 is NOT rank-1, Arm A is
**NULL by pre-commit**. If the random-anchor null mean ≥ Q 71's observed centrality
(z ≤ 0), Arm B is a **PRE-COMMIT VIOLATION**, published with full prominence.

## 3. Method

- **Corpus / instrument:** QAC v0.4 ROOT, verse-union pericope root-sets, exactly
  the H-NEW-2260 / H-NEW-1380 / H-NEW-1500 extraction (`first ROOT feature per
  segment`). Rules-tuple `(no-tashkeel, QAC v0.4 ROOT, verse-union pericope,
  basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
- **Pericope inventory (LOCKED, copied verbatim from H-NEW-2260):**
  Q 7:59-64, Q 11:25-49, Q 23:23-30, Q 26:105-122, Q 54:9-17, Q 71:1-28.
- **Arm A — centrality rank.** For each pericope p, `centrality(p) = mean_{q≠p}
  Jaccard(p,q)`. Rank the 6 pericopes by centrality (1 = most central). Record
  Q 71's rank.
- **Arm B — anchor-swap permutation null.** Replace Q 71 with a random contiguous
  28-verse window drawn uniformly from the whole corpus (length-matched to Q 71's
  L=28); recompute the swapped pericope's mean Jaccard to the fixed other five.
  10000 draws, seed 20260509. Statistic = Q 71's observed mean-Jaccard-to-other-5
  (= its Arm-A centrality value). `z = (obs − null_mean)/null_std`; one-sided
  `p_perm = #(null ≥ obs)/10000`.
- **Run-time guards:** SHA-256 of THIS pre-reg embedded in the script and verified
  fail-fast; the 15 stored H-NEW-2260 Nūḥ pairwise Jaccards reproduced (MW-7).

## 4. Acceptance window (LOCKED)

| Arm | PASS-DIRECTED | DIRECTIONAL | NULL / VIOLATION |
|:--|:--|:--|:--|
| A (rank) | rank == 1 | rank == 2 | rank ≥ 3 → NULL |
| B (anchor-swap) | z>0 AND p_perm ≤ 0.025 | z>0 AND p_perm ≤ 0.05 | z ≤ 0 → PRE-COMMIT VIOLATION; or p_perm > 0.05 → NULL |

Bonferroni across this surah's k=2 primary-test arms: α_bon = 0.05/2 = 0.025.

Overall verdict logic:
- Both arms PASS-DIRECTED → **Q071-F-01 CONFIRMED** (Q 71 is the cycle centroid).
- A NULL but B PASS → **PARTIAL** (Q 71 lexically cohesive with the cycle but not
  its most-central member).
- A NULL and B NULL/VIOLATION → **Q071-F-01 NULL** (Q 71 is NOT the cycle anchor;
  the dedicated-surah-as-hub intuition is falsified).

## 5. Garden-of-forking-paths

- The 6-pericope inventory and the ROOT-Jaccard instrument are inherited LOCKED
  from H-NEW-2260; we do not re-segment or re-instrument. (Re-segmentation would
  be MW-7-capped exploratory.)
- "Centroid" is operationalized as **max mean-pairwise-Jaccard** (graph-centrality
  / medoid sense), locked before observation. We do NOT switch to an alternative
  centrality (e.g. min-max, eigenvector) post-hoc.
- Arm B uses a CONTIGUOUS verse window (matching H-NEW-2260's length-matched null),
  not a random root-set of matched size — locked for comparability with the parent.
- The direction is LOCKED toward the *intuitive* hypothesis precisely so that an
  honest NULL (if Q 71 is peripheral) is a first-class, non-cherry-picked result.

## 6. Honest disclosure (pre-observation)

The intuition "the dedicated surah is the lexical hub" is plausible but NOT
guaranteed: Q 71 is the longest pericope (L=28, 87 unique roots) and carries large
blocks of vocabulary the short cross-surah retellings lack (the cosmological-signs
block vv 15-20: sun/moon/heavens/earth; the five named idols v 23; the "by night
and day" complaint). High *private* vocabulary mass lowers Jaccard centrality even
when the surah is thematically central. So a long dedicated surah can be the
NARRATIVE anchor while being a lexical OUTLIER of its own cycle. We pre-commit to
the lexical operationalization and will report whichever way it falls.

## 7. Cross-references

- [[h-new-2260-prophet-cycle-pericope|H-NEW-2260]] — parent (Nūḥ PASS z=+2.51).
- [[cross-finding-025-formal|cross-finding-025]] — scale-of-aggregation pericope-flip.
- [[h-new-111|H-NEW-111]] — at whole-surah FR scale the five cross-surah Nūḥ hosts
  (Q 7/11/23/26/54) are among Q 71's MOST DISTANT surahs (ranks 79-102/113) — a
  prior reason to doubt the centroid intuition.
- 06-novel-findings.md Q071-F-01 — result.
