---
finding_id: h-new-137
title: "Wrap-around liturgical ring: Q 1 ↔ terminal-triad content-closure test"
specialist: (unassigned; queued for specialist-b / synthesizer / next-session)
date_prereg: 2026-04-17
seed: 20260418
bonferroni_k: 3
bonferroni_family: h-new-137-wrap-around-closure
alpha_bon: 0.0167
alpha_raw: 0.05
direction_primary: "mean_d(Q 1, {Q 108..114}) < corpus_mean_d(Q 1, ·); one-sided lower-tail"
direction_secondary_A: "d(Q 1, Q 114) < 10th-percentile of d(Q 1, ·) distribution (one-sided lower-tail)"
direction_secondary_B: "all 4 metrics (FR, Hellinger, JS, TV) agree on lower-tail direction"
K_top_features: 500
dirichlet_alpha: 0.5
length_control: "MW-1 via L1-normalization of per-surah distributions"
rules_tuple: "(114 surahs Hafs-Kūfan, no-tashkeel, basmala-counted-only-in-surah-1, QAC-STEM root tokens, mushaf order, 4 distance metrics)"
perms: 10000
verdict_ceiling: "PASS-DIRECTED (not CONFIRMED until independent replication on char-4-gram feature space per H-NEW-138)"
parent_model: "theorist-2026-04-17-unified-equation.md §2 P8"
source_observation: "scratch/inline-2026-04-17-q1-nearest-neighbors.md (team-lead inline 2026-04-17, 4-metric cross-replication null p ≈ 3.9×10⁻⁶)"
---

# [[h-new-137-wrap-around-closure|H-NEW-137]] — Wrap-around liturgical ring: Q 1 ↔ terminal-triad closure test

## Motivation

The theorist's 7-principle unified-equation proposal
(`scratch/theorist-2026-04-17-unified-equation.md`) includes P8
"Wrap-around liturgical ring" as a SUPPORTED candidate principle,
upgraded 2026-04-17 after team-lead's 4-metric cross-replication
observation: Q 1 al-Fātiḥa's 10 nearest content-neighbors are 10/10
short-mufaṣṣal surahs (Q ≥ 78), under Fisher-Rao, Hellinger,
Jensen-Shannon, and (with rank-11 for Q 108) Total Variation metrics.
Null p ≈ 3.9×10⁻⁶ under random-neighbor null, observed under all 4
metrics.

That observation is POST-HOC (detected in a nearest-neighbor scan, not
pre-registered). The architectural claim — the mushaf's opening Q 1
and closing Q 108-114 occupy the same content-zone, forming a
topological RING closure — requires a pre-registered permutation-null
test to survive the project's MW-6 disciplinary frame.

[[h-new-137-wrap-around-closure|H-NEW-137]] is that pre-reg. It operationalizes the ring-closure claim
as a one-sided test that Q 1 is anomalously close to the terminal-triad
surahs relative to the rest of the corpus, under multiple metrics,
with permutation-null significance.

## Hypothesis

**Primary (H1)**. Let d(x, y) = Fisher-Rao arccos-Bhattacharyya
distance on top-500 QAC-STEM root distributions (Dirichlet-0.5
smoothed, L1-normalized). Define:

- TERMINAL_TRIAD = {Q 108, Q 109, Q 110, Q 111, Q 112, Q 113, Q 114}
  (7 surahs — the final 7 of the mushaf, spanning the short-mufaṣṣal /
  refuge / invocation cluster. Chosen as 7 rather than 3 because P8
  references "Q 108-114" as the closing content-zone, not just the
  muʿawwidhatān.)
- mean_d_TRIAD = (1/7) Σ_{s ∈ TERMINAL_TRIAD} d(Q 1, s)
- mean_d_REST = (1/106) Σ_{s ∉ TERMINAL_TRIAD, s ≠ Q 1} d(Q 1, s)

**H1 claim**: mean_d_TRIAD < mean_d_REST at permutation-null
p < α_bon (one-sided lower-tail). The permutation null re-samples 7
surahs uniformly at random from the 113 non-Q-1 surahs and computes
the mean d(Q 1, ·) over each sample; the observed mean_d_TRIAD is
compared to this null distribution.

**Secondary A (descriptive, stronger)**. d(Q 1, Q 114) is below the
10th percentile of the distribution {d(Q 1, s) : s ∈ {all 113 non-Q-1
surahs}}. This tests whether Q 114, specifically the mushaf's
FINAL surah, is unusually close to Q 1.

**Secondary B (cross-metric robustness)**. Primary H1 test is repeated
under 3 additional metrics:
- Hellinger: d_H(p, q) = sqrt((1/2) Σ_k (sqrt(p_k) − sqrt(q_k))²)
- Jensen-Shannon: d_JS(p, q) = sqrt((1/2) KL(p||m) + (1/2) KL(q||m)),
  m = (p+q)/2
- Total Variation: d_TV(p, q) = (1/2) Σ_k |p_k − q_k|

Secondary B PASSES iff ALL 4 metrics (including primary FR) produce
mean_d_TRIAD < null permutation-median with consistent direction.

## Pre-registered Bonferroni family

**k = 3** (primary FR test + Secondary A Q 1↔Q 114 test +
Secondary B cross-metric agreement test). **α_bon = 0.05/3 = 0.0167**.

- Primary PASS criterion: perm p < 0.0167 one-sided
- Secondary A PASS criterion: d(Q 1, Q 114) < P10 of d(Q 1, ·)
  distribution (this is a descriptive threshold; single-test α=0.05
  ceiling applies since it's a position-test, not a p-value)
- Secondary B PASS criterion: all 4 metrics show mean_d_TRIAD below
  their respective permutation-null medians (descriptive; not a
  probability test)

Overall verdict mapping:
- ALL 3 pass → **PASS-DIRECTED** (wrap-around closure established
  under multi-metric disciplinary frame)
- Primary + Sec A pass, Sec B partial → **PARTIAL-PASS**
- Primary only → **WEAK-PASS** (tighten before CONFIRMED)
- Primary fails → **NULL** (P8 loses its only pre-registered
  empirical anchor; theorist must demote P8 from SUPPORTED back to
  CANDIDATE)

## MW-5 positive-control

**Before** running the primary test, the executor must verify that the
distance pipeline reproduces a known result: Q 1's nearest neighbor
under the primary FR metric must be Q 108 al-Kawthar at d ≈ 0.338
(matches team-lead inline 2026-04-17 observation). Tolerance ±0.01
on the distance; rank-1 for Q 108 required.

If MW-5 fails, the run is invalid and the script must be debugged
before re-executing the primary test.

## Specification

### Data

- Corpus: `/Users/grey/Downloads/quran/data/quran-uthmani-no-tashkeel.*`
  (locked 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1)
- Root extraction: QAC-STEM v0.4 (same pipeline as [[h-new-111-fisher-rao-mushaf|H-NEW-111]])
- Feature space: top-500 roots by corpus frequency (same K as [[h-new-111-fisher-rao-mushaf|H-NEW-111]])
- Per-surah distribution: count[root] / Σ count[·] on the top-500
  roots, Dirichlet(α=0.5) smoothed

### Distance metrics (4 total)

All 4 operate on the same top-500-root distribution per surah:

1. **FR (primary)**: d_FR(p, q) = 2·arccos(Σ_k sqrt(p_k · q_k))
2. **Hellinger**: d_H(p, q) = sqrt((1/2) Σ_k (sqrt(p_k) − sqrt(q_k))²)
3. **Jensen-Shannon**: d_JS(p, q) = sqrt(JS_divergence(p, q))
4. **Total Variation**: d_TV(p, q) = (1/2) Σ_k |p_k − q_k|

### Permutation null

For the primary H1 test:
- Compute observed mean_d_TRIAD under FR
- 10,000 permutations: each permutation samples 7 distinct non-Q-1
  surahs uniformly, computes (1/7) Σ d_FR(Q 1, s_sampled)
- Null distribution = empirical distribution of 10,000 permutation means
- One-sided lower-tail p = (#{perm_mean ≤ observed} + 1) / (10,001)

Secondary B repeats the above for each of the 4 metrics.

### Seed

Seed = 20260418 (matches theorist's pre-reg seed for the wrap-around
principle series).

### Garden-of-forking-paths disclosure (pre-reg commitments)

- **TERMINAL_TRIAD is fixed at 7 surahs Q 108-114** (not variable).
  The 7-surah choice matches P8's content-closure-zone definition
  (short-mufaṣṣal + muʿawwidhatān combined). No post-hoc re-definition.
- **Distance metrics are fixed at 4** (FR, Hellinger, JS, TV). No
  addition of exotic metrics mid-run.
- **K = 500 top roots** (matches [[h-new-111-fisher-rao-mushaf|H-NEW-111]] parent).
- **Dirichlet α = 0.5** (matches [[h-new-111-fisher-rao-mushaf|H-NEW-111]] parent).
- **No length residualization**: MW-1 via L1-normalization is the
  sole length control. (Team-lead's observation noted Q 1 is the
  shortest in the mushaf at 7 verses; Q 108 is shortest at 3 verses.
  Short-surah length bias is a known confound; pre-reg discloses
  this and relies on L1-normalization as the control.)

### Post-hoc protection

This pre-reg LOCKS:
1. Family-size k=3
2. α_bon = 0.0167
3. Direction one-sided lower-tail for primary
4. Seed 20260418
5. TERMINAL_TRIAD = {Q 108..114}
6. 4 metrics, K=500, α=0.5
7. Permutation count = 10,000
8. MW-5 re-verification before primary execution

Any deviation from the above MUST be journaled and clearly flagged
in the findings file. Post-hoc re-definition of TERMINAL_TRIAD or
metric-selection is a HARD VIOLATION and invalidates the pre-reg.

## Falsifiability

The test is genuinely falsifiable:
- If Q 1's mean distance to the terminal triad is NOT lower than to
  a random 7-surah sample, P8 loses its pre-registered empirical
  support.
- If only 1 or 2 of the 4 metrics pass, the cross-metric claim
  (team-lead's 4-metric replication) would be locally-significant
  but non-robust — demoting P8.
- If Secondary A (Q 1 ↔ Q 114 specifically in bottom 10%) fails,
  the "closing-the-line" topological reading weakens: Q 1 may be
  close to short-mufaṣṣal as a class but not specifically to the
  terminal surah.

## Expected outcome (theorist prediction)

Strong PASS-DIRECTED on all 3 tests:
- Primary: perm p_one-sided < 0.001 (expectation based on team-lead's
  10/10 short-mufaṣṣal observation translating to mean-distance being
  FAR below null-median)
- Secondary A: d(Q 1, Q 114) in bottom 5% (NOT just bottom 10%);
  team-lead observation noted Q 112 at d=0.356 (rank 4), Q 113 at
  0.382 (rank 8); Q 114 is expected around rank 10-15 — still
  within bottom 15% easily
- Secondary B: all 4 metrics agree (per 4-metric cross-replication
  already observed)

## Verdict ceiling

**PASS-DIRECTED** is the maximum verdict achievable at this pre-reg
alone. To reach CONFIRMED, the project requires independent
replication at a DIFFERENT feature space (e.g. char-4-gram or
verse-length histogram per [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] companion pre-reg).

## Queue for follow-up

- **[[h-new-138-wrap-around-feature-robustness|H-NEW-138]]** (companion pre-reg): feature-space robustness of the
  wrap-around closure (char-4-gram + verse-length repeat)
- If [[h-new-137-wrap-around-closure|H-NEW-137]] PASS + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] PASS: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] candidate
  synthesis "Mushaf architecture as topological ring"
- If [[h-new-137-wrap-around-closure|H-NEW-137]] PASS + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] NULL: P8 demoted to feature-specific
  claim, not architectural

## Integration with other findings

- Parent: theorist unified-equation P8
- Refinement of: [[h-new-89-meta-cluster-network|H-NEW-89]] "Q 1 structurally isolated" (this pre-reg
  reframes isolation as cluster-taxonomy isolation, not content-
  neighborhood isolation)
- Relates to: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (mushaf Fisher-Rao geodesic) — P8 is
  a CLOSURE amendment to P2's linear-geodesic claim
- Relates to: [[cross-finding-010-extended-network|cross-finding-010]] (4-region hub architecture) — this
  pre-reg tests whether the front and back-terminal regions are
  content-mirrors

## Files

- Pre-reg (this file): `findings/phase-b-hypotheses/h-new-137-wrap-around-closure-prereg.md`
- Source observation: `scratch/inline-2026-04-17-q1-nearest-neighbors.md`
- Parent model: `scratch/theorist-2026-04-17-unified-equation.md` §2 P8
- D-matrix reuse: `findings/phase-b-hypotheses/csv/h-new-111.json`
  (FR matrix already computed; permutation null can be computed
  directly from it without re-extracting features)
- Script (to be written): `scripts/h_new_137_wrap_around_closure.py`
- Expected runtime: < 60 seconds (distance matrix is pre-computed;
  only permutation loop and Hellinger/JS/TV re-computation required)
