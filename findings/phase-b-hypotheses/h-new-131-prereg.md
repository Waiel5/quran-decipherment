---
finding_id: h-new-131
title: "Q 108 al-Kawthar MST-super-hub robustness investigation"
specialist: specialist-B (quran-equation-solvers)
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 2
bonferroni_family: h-new-131-q108-supernode
alpha_bon: 0.025
alpha_raw: 0.05
parent_finding: h-new-134
parent_data: findings/phase-b-hypotheses/csv/h-new-111.json
rules_tuple: "(114 surahs Hafs-Kūfan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
pre_reg_standard: PRE-REG-STANDARD-04
amendment_2026-04-17: "audit-036 recommended amendment (TIGHTENING, self-verifying per feedback_bonferroni_tightening_vs_loosening): Cell A relabeled as DESCRIPTIVE-ROBUSTNESS bright-line check (no p-value test, no Bonferroni slot). Cell B Bonferroni family reduced to k=2 over {JS, TV}. Hellinger remains as rank-monotone consistency-check with FR (not an independent inferential slot). Cell A bright-line thresholds unchanged (≤5 REFUTE / 6-14 WEAK / ≥15 SURVIVE). α_bon: 0.0167 → 0.025. Applied pre-execution."
---

# [[h-new-131-q108-supernode|H-NEW-131]] — Q 108 al-Kawthar MST super-hub: robustness investigation

## Motivation

[[h-new-134-formal-prophet-named-signature|H-NEW-134]] descriptively observed that Q 108 al-Kawthar has MST-degree 24
under Fisher-Rao arccos-Bhattacharyya on top-500 QAC-STEM roots with
Dirichlet α=0.5 smoothing — a 2.4× outlier over the next-highest node
(Q 7, degree 10). [[h-new-134-formal-prophet-named-signature|H-NEW-134]] itself flagged the likely mechanism:
Q 108 is the shortest surah (3 verses, 10 words), and a distribution
over 500 roots built from 10 tokens is dominated by the α=0.5 Dirichlet
prior, producing a quasi-uniform shape that is nearest-neighbor to many
other small surahs.

**Question**: is Q 108's super-hub status (a) a MECHANICAL artifact of
Dirichlet-smoothing a very-short surah, (b) a METRIC-SPECIFIC artifact of
Fisher-Rao, or (c) a genuine STRUCTURAL property of its information-
geometric position that survives both robustness tests? [[h-new-134-formal-prophet-named-signature|H-NEW-134]] itself
queued this as H-NEW-134.1 / H-NEW-134.2. This pre-reg implements both.

## Hypotheses

### Direction A — Dirichlet-smoothing robustness (PRIMARY)

**H_0 (structural claim)**: Q 108's MST-degree remains ≥ 15 under
Dirichlet α=0.01 (near-unsmoothed) on the top-500 roots.

**H_1 (smoothing artifact)**: Q 108's MST-degree drops below 15.

**Decision**: if Q 108's degree is ≤ 5 under α=0.01, the super-hub
status is REFUTED as smoothing artifact and [[h-new-134-formal-prophet-named-signature|H-NEW-134]]'s claim is
demoted to "mechanical". If Q 108's degree remains ≥ 15, the super-hub
status SURVIVES the most severe robustness test. Intermediate values
(6-14) indicate partial mechanical contribution; super-hub status
survives but WEAKLY.

### Direction B — Cross-metric robustness (PRIMARY)

For each of three alternative metrics:

- **Hellinger**: D_H(p,q) = √(½ Σ (√p_i − √q_i)²)   [bounded [0,1], monotone with Fisher-Rao]
- **Jensen-Shannon**: D_JS(p,q) = √( ½·KL(p‖m) + ½·KL(q‖m) ) where m = (p+q)/2
- **Total variation (L1)**: D_TV(p,q) = ½ Σ |p_i − q_i|

compute the MST on the same 114 surah-distributions (α=0.5 smoothed,
i.e. same input as [[h-new-134-formal-prophet-named-signature|H-NEW-134]]) and record Q 108's degree.

**H_0 (metric-specific artifact)**: Q 108's degree < 15 under ≥ 2 of 3
alternative metrics.

**H_1 (cross-metric robustness)**: Q 108's degree ≥ 15 under ≥ 2 of 3
alternative metrics.

**Decision**: if Q 108 retains degree ≥ 15 under ≥ 2/3 alternative
metrics, the super-hub status is ROBUST across metric choice. If < 2/3,
the [[h-new-134-formal-prophet-named-signature|H-NEW-134]] claim is Fisher-Rao-specific.

Note: Hellinger and Fisher-Rao are monotone transforms (Hellinger = sin(D_FR/2)·√2 ≈ D_FR/√2 for small D_FR). The MST under Hellinger is therefore
EXPECTED to equal the MST under Fisher-Rao (Kruskal is rank-only). This
is a consistency check, not an independent test. The independent tests
are JS and TV.

### Direction C — Thematic-structural sanity (DESCRIPTIVE ONLY)

Compute Q 108's actual root-count profile (unsmoothed). For each of the
top-5 roots present (by raw count in Q 108), report:

- Its rank in the global top-500 list (1 = highest-frequency root in the
  whole corpus).
- Its raw global count.

Also compute: what fraction of Q 108's smoothed probability mass sits
on the top-50 globally-frequent roots? If > 90%, Q 108's distribution
is CLOSE TO THE GLOBAL MEAN on the high-freq axes — i.e. it's central
because it's "average". If < 50%, Q 108 concentrates on unusual roots
— structurally meaningful.

This is a purely descriptive read; no test.

## Method (locked)

### Cell A — No-smoothing MST

1. Rebuild the 114×500 count matrix using the SAME QAC-STEM root
   tokenization and SAME top-500 root selection as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (read from
   parent data if available; otherwise re-derive from QAC v0.4 with
   identical rules).
2. Apply Dirichlet α=0.01 (essentially no smoothing: 500·0.01 = 5.0
   prior mass, << even the shortest surah's 10 real tokens).
3. L1-normalize to probability simplex.
4. Compute Fisher-Rao arccos-Bhattacharyya D-matrix (same formula as
   [[h-new-111-fisher-rao-mushaf|H-NEW-111]]).
5. Kruskal's MST on the 114×114 complete graph weighted by D.
6. Report Q 108's degree and top-10 node degrees.

**Caveat about α=0**: with α=0 and Q 108 having only 10 raw tokens,
490 of the 500 roots have p=0, Bhattacharyya coefficient with most
surahs becomes 0, and D_FR=π (maximum). This would make Q 108
INFINITELY FAR from every surah that doesn't share at least one of
its 10 roots. Using α=0.01 is the minimum-smoothing
compromise that keeps distances finite. A strict "no-smoothing"
variant with Laplace ε=1e-9 added only where p=0 is queued as a
follow-up sanity check but is NOT the primary test in Cell A.

### Cell B — Cross-metric MST

Using the SAME input probabilities as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (α=0.5), compute the
three D-matrices (Hellinger, JS, TV) and their MSTs. Record Q 108's
degree in each.

Hellinger is reported for consistency-check only (expected ≡ FR-MST by
monotonicity). JS and TV are the two independent robustness tests.

Effective k for Cell B: 2 independent tests (JS, TV). But we keep
Bonferroni k=3 (Cell A + JS + TV) to match the pre-reg family size
committed to the auditor.

### Cell C — Root-rank descriptive

1. Extract Q 108's raw root-count vector (unsmoothed).
2. Sort roots by raw count in Q 108, take top-5.
3. For each, look up its global-corpus rank in the top-500 ordering.
4. Compute fraction of Q 108's (α=0.5)-smoothed probability on
   top-50 globally-frequent roots.

No test; purely descriptive.

## Bonferroni accounting (amended per audit-036 2026-04-17)

- Family = [[h-new-131-q108-supernode|h-new-131]]-q108-supernode
- Cell A = DESCRIPTIVE-ROBUSTNESS bright-line check, NOT an inferential
  Bonferroni slot. No p-value; no α_bon allocation. It is a
  READ on whether Q 108's descriptive degree survives a direct
  mechanism-probe (reducing smoothing).
- Inferential family = Cell B alternative-metric tests only
  = {Jensen-Shannon, total variation} = k = 2
- α_bon = 0.05 / 2 = 0.025
- Cell A bright-line decision rule (unchanged): degree ≤ 5 → REFUTE
  [[h-new-134-formal-prophet-named-signature|H-NEW-134]] claim; 6 ≤ degree ≤ 14 → WEAKLY-SURVIVES; degree ≥ 15 →
  SURVIVES. These thresholds are descriptive and pre-committed.
- Cell B PASS: ≥ 2 of {FR, JS, TV} have Q 108 degree ≥ 15 (FR is the
  parent observation; Hellinger is rank-monotone redundancy with FR
  and excluded from the inferential family; JS and TV are the two
  independent inferential slots).
- Note: the "≥ 2/3" composite rule on FR/JS/TV is non-standard
  α-accounting under positive metric-dependency. Bonferroni k=2 is
  conservative under positive dependence; acknowledge in findings.

## Pre-committed acceptance matrix

| Cell A result | Cell B result | Final verdict |
|---|---|---|
| degree ≥ 15 (α=0.01) | ≥ 2/3 metrics agree | **STRUCTURAL** ([[h-new-134-formal-prophet-named-signature|H-NEW-134]] super-hub confirmed robust) |
| degree ≥ 15 | < 2/3 agree | **Fisher-Rao-specific** (metric artifact, not generic centrality) |
| 6 ≤ degree ≤ 14 | ≥ 2/3 agree | **WEAKLY STRUCTURAL** (mixed mechanical + structural) |
| 6 ≤ degree ≤ 14 | < 2/3 agree | **WEAKLY ARTIFACT** (mostly mechanical, some metric-specific residual) |
| degree ≤ 5 | any | **REFUTED as smoothing artifact** — demote [[h-new-134-formal-prophet-named-signature|H-NEW-134]] super-hub claim |

## Garden of forking paths

- α=0.01 threshold chosen as "near-zero, finite distances": 500·0.01 = 5
  total prior mass vs Q 108's 10 real tokens → prior is one-third of
  smoothed mass. This is the MINIMAL smoothing that keeps KL/JS finite.
  Alternatives considered and REJECTED pre-result: α=0 exactly (would
  diverge), α=0.001 (prior mass 0.5 ≈ still finite but D_FR saturates
  to π for most Q 108 pairs — destroys rank information), α=0.1 (too
  close to the α=0.5 baseline to be a meaningful robustness test).
- **Cell A PRIMARY threshold degree ≥ 15**: chosen because it's
  ~1.5× the SECOND-HIGHEST observed degree (Q 7 at 10). A claim that
  "Q 108 is a super-hub" should mean it's CLEARLY above the runner-up.
  Threshold 15 is the mid-point between "distinctly dominant" (≥ 15)
  and "not clearly dominant" (≤ 10). Alternative thresholds rejected
  pre-result: 10 (would accept mere tie with Q 7), 20 (would demand
  near-replication of the original 24).
- Three alternative metrics (Hellinger, JS, TV) chosen from standard
  probability-distance zoo. Alternatives considered and REJECTED
  pre-result: KL-divergence (asymmetric, not a metric), chi-square
  (unbounded, dominated by low-prob cells — bad for sparse data),
  earth-mover (requires ground-distance on the 500 roots, undefined
  here), cosine (not a true distribution metric, though common — we
  deliberately exclude it to keep the comparison within
  proper-simplex-metric territory).
- MST algorithm: Kruskal on complete graph. Prim would give an
  identical MST (unique-edge-weights property holds with probability 1
  under floating-point; ties broken by smaller-index-node convention).
- Direction A is 1-sided (degree drop) because the only theoretically-
  plausible effect of reducing smoothing is to make Q 108 LESS central
  (smoothing makes its distribution approach uniform, which is
  max-central). It cannot plausibly increase degree.

## Self-verification

- All three tests use the SAME input corpus and token set as [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
- Cell A differs ONLY in Dirichlet α. Cell B differs ONLY in the
  distance function applied to the SAME α=0.5 probabilities.
- Cell C is a read on the Q 108 distribution; independent of MST.
- Seed 20260417; no random components (MST is deterministic given D).

## Deliverables

1. This pre-reg: `findings/phase-b-hypotheses/h-new-131-prereg.md`.
2. Script: `scripts/h_new_131_q108_supernode.py`.
3. JSON: `findings/phase-b-hypotheses/csv/h-new-131.json` with all
   MST degree vectors, top-10 hubs per condition, Q 108 descriptive
   root profile.
4. Findings: `findings/phase-b-hypotheses/h-new-131-q108-supernode.md`.
5. Journal: `journal/h-new-131-run-1.md`.

Null and pass will be published with equal prominence.
