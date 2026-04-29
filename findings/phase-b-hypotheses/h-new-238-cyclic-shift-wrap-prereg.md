---
id: H-NEW-238
title: Cyclic-shift wrap-edge analysis — is Q 1 the minimum-wrap-edge start-point among all 114 rotations?
phase: B (pre-registration)
date: 2026-04-17
seed: 20260419
parent_findings: [H-NEW-227, H-NEW-228, cross-finding-013, H-NEW-111, H-NEW-212, H-NEW-192]
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; QAC-STEM top-500 roots; Dirichlet α=0.5; L1-normalized; Fisher-Rao arccos Bhattacharyya; D inherited from H-NEW-111)
direction: Q 1 at position 1 minimizes wrap-edge across all 114 cyclic shifts of the mushaf ordering (one-sided; ranked-by-ascending-wrap-edge rank of Q 1 expected to be 1)
verdict: PENDING
---

# [[h-new-238-cyclic-shift-wrap|H-NEW-238]] — Cyclic-shift wrap-edge analysis (pre-registration)

## Parent context

- **[[h-new-227-wrap-edge-chronologies|H-NEW-227]]**: established the canonical mushaf wrap-edge d(Q 114, Q 1) =
  0.3884 is the TIGHTEST among 5 orderings (mushaf + 4 chronologies) and
  passes the permutation null (p = 0.0277 < α = 0.05). Mushaf wraps BELOW
  the null 5th percentile (0.4799).
- **[[h-new-228-sa-min-entropy-ordering|H-NEW-228]]**: established the mushaf total-path length is 10.8% above
  the adversarial 2-opt SA-min Fisher-Rao TSP solution (structured but not
  globally optimal).
- **[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]**: unified the path-geodesic ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]) and the
  wrap-around ([[h-new-137-wrap-around-closure|H-NEW-137]]/227) into a single topological object: the
  mushaf is a **Hamiltonian CYCLE (ring)** in Fisher-Rao content space,
  closed by the Q 114 → Q 1 wrap-edge.

If the mushaf is topologically a ring, there is no intrinsic "start"
from the cycle's perspective — any cyclic shift produces the same cycle
(same total length; same 114 edges including the wrap). The CANONICAL
choice of Q 1 at position 1 must therefore be *extrinsic*: driven by a
principle outside pure content-geodesicity. Two candidate principles:

1. **P3 (liturgical frame)**: Q 1 al-Fātiḥa is designated *fātiḥat
   al-kitāb* ("Opener of the Book"), obligatorily recited at every ṣalāh
   raka; al-Suyūṭī (*Itqān*), Ibn Taymiyya (*Majmūʿ al-Fatāwā*, tawqīfī
   doctrine), and al-Zarkashī (*Burhān*) treat Q 1 placement as
   divinely-fixed liturgical signature. [[h-new-192-mushaf-position-decomposition|H-NEW-192]] found Q 1 is the
   largest position-prediction residual in the corpus (feature-predicted
   position = 105, actual = 1, Δ = −104) — sui-generis liturgical
   exception.
2. **M1 (structured-cycle geodesic)**: if Q 1 at position 1 is ALSO
   the minimum-wrap-edge start, then the liturgical and geodesic
   designations ALIGN and Q 1 is extrinsically overdetermined.

This test quantifies the compositional-vs-liturgical trade-off at Q 1
by asking: **among all 114 cyclic shifts of the mushaf ordering, does
Q 1 at position 1 give the minimum wrap-edge?**

## Question

For each cyclic shift k ∈ {1, 2, ..., 114}, let π_k be the mushaf
ordering rotated so that Q k is at position 1 (i.e., the cycle
(Q k, Q k+1, ..., Q 114, Q 1, ..., Q k−1) read left-to-right). The
wrap-edge of π_k is

  W(k) = d_FR(π_k[-1], π_k[0]) = d_FR(Q k−1, Q k)  (mod 114)

where Q 0 ≡ Q 114. The 114 wrap-edges are exactly the 114 *consecutive
adjacencies* of the mushaf cycle (including the canonical wrap Q 114 →
Q 1 at k=1).

**Primary descriptive question**: what is the rank of k=1 (canonical Q 1
start) in the ascending-sorted list of W(1), W(2), ..., W(114)? If rank
= 1, Q 1 is the M1-minimum-wrap-edge start. If rank > 10, Q 1 is a
PURELY liturgical designation (M1 would prefer a different start).

## Design

### Cell Primary (one descriptive test, Bonferroni k = 1):

**H0**: Q 1's wrap-edge rank among the 114 cyclic shifts is NOT rank 1
      (null: no special status; Q 1 is an arbitrary rotation point of
      the ring).

**H1**: Q 1's wrap-edge rank IS rank 1 (one-sided lower-tail: Q 1 is
      the minimum-wrap-edge start-point).

**Verdict mapping**:

| Rank of Q 1 | Interpretation | Verdict label |
|:-:|:---|:-:|
| 1 | P3 ∧ M1 ALIGN at Q 1 — liturgical ∩ geodesic | PASS |
| 2–10 | P3 dominant, M1-compatible (Q 1 near-minimum) | PASS-DIRECTED |
| 11–57 | P3 dominant, M1-neutral (Q 1 arbitrary mid-pack) | NULL (expected under pure liturgical) |
| 58–114 | P3 ANTI-aligned with M1 (Q 1 in worst half) | NULL-ANTI |

Under the pre-registered Bonferroni k=1, α_bon = 0.05, a *strict*
lower-tail significance test would require Q 1 to be at rank 1 *or*
rank 1 among random shifts (p_one_sided = 1/114 ≈ 0.00877 for rank 1;
p ≈ 10/114 ≈ 0.0877 for rank ≤ 10). Only rank = 1 passes α_bon = 0.05
under the strict test. Rank 2–10 is the PASS-DIRECTED band.

### Cell Sanity (MW-5):

**S1**: The 114 wrap-edges W(1..114) are the 114 consecutive edges
of the mushaf Hamiltonian cycle. Their SUM equals the cycle-TSP
length L_cycle(mushaf) = L_path(mushaf) + W(1). This is a SANITY
check: total cycle length is invariant under cyclic shift, as it
must be.

**S2**: For comparison, draw 1,000 random cyclic shifts of
uniform-random Hamiltonian cycles (not the mushaf). The expected
rank of the first position in a random cycle's wrap-edge ranking
is 57.5 (uniform expectation). If Q 1's rank in the MUSHAF cycle
is near 57.5, this is consistent with liturgical-only placement
(no preference). If near 1, this is consistent with M1-alignment.

## Numbers to report

1. Full 114-row table of (k, Q k−1, Q k, W(k)) sorted by ascending
   W(k).
2. Rank of k=1 (canonical Q 1 start) and rank of k=2 (Q 2 start), etc.
3. Top-10 tightest-wrap starting-points: the 10 rotations with
   smallest W(k).
4. Bottom-10 loosest-wrap starting-points.
5. Min, max, mean, median, std of W(1..114).
6. Cycle total length (invariance check): sum of W(1..114) ≡
   L_cycle(mushaf).
7. The starting-point k* that minimizes W(k) (i.e., which surah at
   position 1 would M1 prefer?).
8. Rank-percentile of Q 1: rank(Q1) / 114.

## Method

1. Load the 114×114 Fisher-Rao distance matrix D from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]
   (QAC-STEM K=500 roots, Dirichlet α=0.5, L1-normalized, arccos
   Bhattacharyya). Verify h111 SHA-256 matches [[h-new-227-wrap-edge-chronologies|H-NEW-227]]'s source.
2. For k ∈ {1..114}, compute W(k) = D[Q(k−1)][Q k] where Q 0 ≡ Q 114
   (the mushaf ring interpretation).
3. Rank-sort W(1..114) ascending; report rank of k=1.
4. Output:
   - JSON summary to `findings/phase-b-hypotheses/csv/h-new-238.json`
   - Findings markdown to
     `findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap.md`

## What this test does NOT claim

- It does NOT test whether Q 1 is special for any reason other than
  wrap-edge Fisher-Rao. Other metrics (char-4-gram, NCD-lzma,
  verse-length, Hellinger, JS, TV) may give different rankings. Only
  Fisher-Rao root distribution is tested here. Cross-feature extension
  is queued as a follow-on.
- It does NOT claim Q 1 placement is PURELY liturgical or PURELY
  compositional; it QUANTIFIES the position of Q 1 on the M1-optimality
  spectrum. Extreme ranks (1 or 114) would be informative in either
  direction.
- It does NOT supersede [[h-new-227-wrap-edge-chronologies|H-NEW-227]]'s finding that the mushaf wrap is
  tighter than all 4 chronologies — that remains the headline. This
  test asks a DIFFERENT question: within the mushaf cycle itself, is
  the canonical rotation the wrap-minimum?

## Garden-of-forking-paths log (pre-run)

- **Chosen direction**: one-sided lower-tail (Q 1 rank = 1 is the PASS
  direction). Justification: parent [[h-new-227-wrap-edge-chronologies|H-NEW-227]] established mushaf wrap
  is unusually tight vs null; if this tightness is concentrated at
  the canonical rotation, Q 1 rank = 1 is the pre-registered
  prediction.
- **Chosen metric**: Fisher-Rao (not char-4-gram or verse-length).
  Justification: parent [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] is defined on Fisher-Rao
  roots; this test is internal to that feature space. Cross-feature
  sensitivity is a QUEUED follow-up, not the primary test.
- **Chosen α_bon**: 0.05 (Bonferroni k=1). Single descriptive test;
  no multi-cell correction needed.
- **Chosen smoothing**: Dirichlet α=0.5 (inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]]);
  no fresh re-computation.
- **Chosen verdict mapping**: rank = 1 is PASS; rank 2–10 is
  PASS-DIRECTED; rank > 10 is NULL. Justification: the ring
  topology doesn't privilege any rotation, so "near-minimum" (top 10
  of 114 ≈ 9th percentile) is the natural PASS-DIRECTED threshold.

No post-hoc changes anticipated. If the verdict falls in the
NULL-ANTI band (Q 1 rank > 57), the expected interpretation is still
consistent with P3-PURE (liturgical override of M1) and will be
reported transparently.

## Classical anchor

- **al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān**: §on *fātiḥat al-kitāb*
  treats Q 1 as the obligatory opener of every ṣalāh raka and
  canonical *umm al-kitāb*. Liturgical (P3) designation is explicit.
  [SECONDARY-TRIANGULATED; per [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]]
- **Ibn Taymiyya, Majmūʿ al-Fatāwā**: majority doctrine that the
  mushaf sūra-order is *tawqīfī* (divinely-fixed by the Prophet,
  not by committee). This is the strong-P3 framing: Q 1 at position
  1 is revelatory, not compositional. [SECONDARY-TRIANGULATED]
- **al-Zarkashī, al-Burhān fī ʿulūm al-Qurʾān**: §on fawātiḥ and
  khawātim — Q 1 is the archetypal fātiḥa. [SECONDARY-TRIANGULATED]

If this test yields rank = 1 for Q 1, we have quantitative alignment
between P3 (liturgical) and M1 (geodesic). If rank > 10, P3 is the
sole driver of Q 1 placement and al-Suyūṭī's liturgical-only framing
is quantitatively vindicated. Either outcome is informative for the
classical-vs-empirical convergence meta-theme.

## Files (to be produced)

- Pre-reg: this file.
- Script: `scripts/h_new_238_cyclic_shift_wrap.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-238.json`
- Findings: `findings/phase-b-hypotheses/h-new-238-cyclic-shift-wrap.md`
- Journal: `journal/h-new-238-run-1.md`
- Ledger entry: `MASTER-FINDINGS-LEDGER.md` Wave-4 section.
