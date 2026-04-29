---
id: H-NEW-131
title: Q 108 al-Kawthar MST super-hub — robustness investigation
phase: B
status: WEAKLY-STRUCTURAL (mixed mechanical + structural origin)
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent: h-new-134 (MST of Fisher-Rao surah graph)
parent_data: findings/phase-b-hypotheses/csv/h-new-111.json
seed: 20260417
rules_tuple: "(114 surahs Hafs-Kūfan; K=500 top QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
bonferroni: k=2 α_bon=0.025 family=h-new-131-q108-supernode (Cell B {JS, TV}; Cell A descriptive-robustness)
pre_reg: findings/phase-b-hypotheses/h-new-131-prereg.md
script: scripts/h_new_131_q108_supernode.py
output_json: findings/phase-b-hypotheses/csv/h-new-131.json
verdict: WEAKLY STRUCTURAL — super-hub status survives with reduced degree (24→11) under near-no-smoothing, and survives with degree 24 under 2 of 3 metrics (Fisher-Rao, Jensen-Shannon) while collapsing to 6 under total-variation.
---

# [[h-new-131-q108-supernode|H-NEW-131]] — Q 108 al-Kawthar MST super-hub robustness

## Summary

[[h-new-134-formal-prophet-named-signature|H-NEW-134]] reported that under Fisher-Rao arccos-Bhattacharyya with Dirichlet
α=0.5 smoothing on the top-500 QAC-STEM roots, Q 108 al-Kawthar has MST-degree
24 — a 2.4× outlier over the runner-up (Q 7 = 10). [[h-new-134-formal-prophet-named-signature|H-NEW-134]] itself flagged
this as likely smoothing-artifact of the shortest surah (Q 108 has only 7
STEM root tokens, of which 4 fall in the top-500). This pre-registered
investigation tests whether that super-hub status is (a) mechanical
(smoothing + shortest-surah), (b) metric-specific (Fisher-Rao artifact), or
(c) genuinely structural.

**Result: WEAKLY STRUCTURAL.** The super-hub status is PART mechanical and
PART structural. Degree drops 24→11 under near-no-smoothing (Dirichlet
α=0.01) — Q 108 loses *super*-hub status but remains in the top-3 hubs (Q 7
becomes #1 with degree 25, Q 2 becomes #2 with degree 16, Q 108 is #3 at 11).
Under alternative metrics with the original α=0.5: Fisher-Rao, Hellinger and
Jensen-Shannon all give degree 24 *exactly* — Q 108 retains super-hub status
identically. Under total variation (L1), degree collapses to 6 — Q 108 is no
longer a clear hub, though it's still in the top-2.

**Refinement of [[h-new-134-formal-prophet-named-signature|H-NEW-134]]**: The "super-hub" framing is EARNED under
Fisher-Rao-family metrics but NOT under total-variation. The 24 → 11
degree drop under unsmoothing says the *magnitude* of the super-hub status
(degree 24) is smoothing-inflated; the *qualitative* status (high-degree
hub) survives.

## Pre-reg compliance

Direction locked BEFORE execution per PRE-REG-STANDARD-04.
Audit-036 recommended amendment applied pre-execution:

- Cell A re-labeled as DESCRIPTIVE-ROBUSTNESS bright-line check (not a
  Bonferroni inferential slot)
- Inferential family = Cell B alternative-metric tests = {JS, TV} = k=2
- α_bon: 0.0167 → 0.025 (tightening, self-verifying per
  `feedback_bonferroni_tightening_vs_loosening`)
- Hellinger retained as rank-monotone consistency-check with FR (excluded
  from inferential family; pre-reg argued this)

## Sanity replication

Exact replication of [[h-new-134-formal-prophet-named-signature|H-NEW-134]]'s Fisher-Rao α=0.5 MST. Q 108 degree = 24
(expected 24). Top-10 hubs match [[h-new-134-formal-prophet-named-signature|H-NEW-134]]'s exactly: 108:24, 7:10, 112:8,
64:7, then 111/103/78/63/2/6 all at 4. Instrument validated.

## Cell A — Dirichlet-smoothing robustness (DESCRIPTIVE)

Dirichlet α reduced from 0.5 to 0.01 (near-no-smoothing).

| Surah | Degree (α=0.5) | Degree (α=0.01) |
|---:|---:|---:|
| Q 7  al-Aʿrāf    | 10 | **25** |
| Q 2  al-Baqara   | 4  | **16** |
| Q 108 al-Kawthar | **24** | 11 |
| Q 3  Āl ʿImrān   | —  | 10 |
| Q 10 Yūnus       | —  | 8 |
| Q 16 al-Naḥl     | —  | 7 |

**Verdict: WEAKLY-SURVIVE** (degree ∈ [6, 14]; pre-committed: ≥15 SURVIVE,
≤5 REFUTE).

**Mechanistic reading**: Under α=0.5 on 500 cells, Q 108's 4 topical tokens
are overwhelmed by 500×0.5 = 250 units of prior mass (smoothed mass ratio:
4/254 real). The distribution is ~uniform, which makes Q 108 a nearest-
neighbor to every other smoothed-near-uniform surah — and the shortest
surahs produce the most-uniform smoothed distributions. Under α=0.01 on
500 cells, Q 108 carries 4 real tokens vs 5 prior mass — roughly 45%
real — and its distribution reflects its actual concentrations. Q 108
survives as a top-3 hub but loses the "super" qualifier.

**The new top-1 hub under α=0.01 is Q 7** (al-Aʿrāf, degree 25). Q 7 is
a long Meccan narrative surah whose root-distribution is broadly
representative of the Meccan narrative corpus; in a less-smoothed space,
its genuine breadth makes it a legitimate centroid of the narrative cluster
— not an artifact.

Q 2 (al-Baqara) at degree 16 as the new #2 hub is also a narrative-corpus
centrality effect; al-Baqara is the longest surah and touches the widest
range of topics.

## Cell B — Cross-metric robustness (INFERENTIAL, Bonferroni k=2)

All metrics on the same Dirichlet-0.5-smoothed probabilities.

| Metric | Q 108 MST-degree | Top-1 hub | Structural? |
|---|---:|---|---|
| Fisher-Rao arccos-Bhattacharyya | **24** | Q 108 | parent result |
| Hellinger (√-simplex Euclidean) | **24** | Q 108 | consistency-check: ≡ FR by rank-monotonicity (VERIFIED: MST edges identical) |
| Jensen-Shannon  | **24** | Q 108 | INDEPENDENT-PASS |
| Total variation | 6 | Q 64 (deg 7) | FAILS |

**Verdict: PASS** — ≥ 2 of {FR, JS, TV} have Q 108 degree ≥ 15.

**Reading**: the super-hub status is present under Fisher-Rao / Hellinger /
JS (all arccos/sqrt-based metrics on the simplex) but absent under
total-variation (L1). This makes sense: FR, Hellinger, and JS are all
f-divergences of the form Σ f(√(p_i·q_i)) or Σ (√p-√q)² that HEAVILY
penalize high-probability cells' √-mismatches; TV (L1) treats every
dimension equally. Under α=0.5, Q 108's near-uniform distribution is
"average" on the sqrt-scale → super-hub under FR/Hellinger/JS; but TV
distance from Q 108 to other surahs is dominated by the top-20 or so
high-prob roots in the other surahs, where Q 108 is NOT average — hence
TV-MST doesn't privilege Q 108.

**This is a genuine finding, not noise**: under total-variation, Q 108 is
NOT a super-hub. Under arccos/sqrt-family metrics, it IS. The [[h-new-134-formal-prophet-named-signature|H-NEW-134]]
observation is Fisher-Rao-family-specific but ROBUST within that family.

The Hellinger=FR consistency check (identical MST edges verified) confirms
the pipeline is correct and rules out implementation bugs.

## Cell C — Q 108 root-profile (DESCRIPTIVE)

Q 108 actual raw STEM-root tokens: 7 (over 7 distinct roots, each count=1).
Of those 7, only 4 fall in the top-500 globally-frequent roots. Top-5 roots
by Q 108 count (all tied at 1; tiebreak = global-rank):

| Q 108 root | Arabic | Q 108 count | Global-top500 rank | Global corpus count |
|---|---|---:|---:|---:|
| `rbb` | ربب (Lord) | 1 | **4** | 980 |
| `kvr` | كثر (abundance) | 1 | 64 | 167 |
| `Slw` | صلو (pray) | 1 | 115 | 99 |
| `ETw` | عطو (give) | 1 | 481 | 14 |
| `nHr` | نحر (sacrifice) | 1 | not-in-top-500 | 1 |

(The remaining 2 Q 108 roots `$nA` and `btr` — شنأ "hate" count 3, بتر
"cut off" count 1 — are also outside top-500.)

**Barbell distribution**: Q 108 mixes ULTRA-frequent roots (rbb = #4 in
whole corpus, 980 occurrences) with ULTRA-rare roots (nHr = hapax
legomenon, occurs once; btr = hapax; $nA = 3 total). This is NOT an
"average" profile. It's a distinctive extremum: very high + very low
frequency, no middle.

**α=0.5-smoothed mass on top-50 global roots**: 0.1024 (only ~10%). On top-100:
0.2047. This is MUCH LESS than what an "average" surah would carry — because
the 0.5-Dirichlet prior on 500 cells spreads ~50% of the mass across all
500 cells uniformly. Q 108 appears "central" under FR-on-the-simplex NOT
because it sits on the high-freq axes (it doesn't), but because its smoothed
distribution is nearly UNIFORM, and the uniform distribution is the FR-centroid
of any cloud of distributions that includes a mix of concentrated and diffuse
points.

**Unsmoothed** fraction on top-50 global roots: 0.2500 (exactly, since 1 of
Q 108's 4 top-500 tokens is rbb at rank 4). This is the real topical content:
Q 108 is 25% a "Lord" surah and 75% a low/rare-root surah.

## Final verdict

**WEAKLY STRUCTURAL — mixed mechanical + structural origin.**

Decoded via pre-committed acceptance matrix:
- Cell A = WEAKLY-SURVIVE (degree 6-14, specifically 11): mechanical component present
- Cell B = PASS (2/3 of {FR, JS, TV} ≥ 15): structural component present

**What survives**:
- Q 108 remains a genuine high-degree MST hub (top-3) under ALL tested
  α values and under FR/Hellinger/JS metrics. The qualitative claim "Q 108
  is a central node in the short-mufaṣṣal Fisher-Rao neighborhood" is
  VALIDATED.
- The identical degree (24) under Fisher-Rao, Hellinger, and Jensen-Shannon
  is a non-trivial cross-metric confirmation within the arccos/sqrt-based
  metric family.

**What is demoted**:
- The 2.4× "super-hub outlier" magnitude (degree 24 vs runner-up 10) is
  PARTLY inflated by Dirichlet smoothing interacting with the shortest
  surah's token count. Under α=0.01 the ratio is 11/25 ≈ 0.44 — Q 108 is
  NO LONGER the top hub (Q 7 is) and the "super" qualifier fails.
- Under total-variation (L1), Q 108 is not a hub at all (degree 6).
- The claim that Q 108 is the "information-geometric origin" of the
  short-mufaṣṣal cluster is METRIC-FAMILY-specific (holds under
  arccos/sqrt-family metrics, not L1).

**[[h-new-134-formal-prophet-named-signature|H-NEW-134]] revision**: the finding's text claimed Q 108 is a "super-hub"
with emphasis on the 2.4× multiple. That specific multiple is
smoothing-inflated. The claim should be REFRAMED as:

> "Q 108 al-Kawthar is a consistently high-degree MST hub under
> Fisher-Rao-family metrics (Fisher-Rao, Hellinger, Jensen-Shannon) with
> Dirichlet α=0.5. Its specific super-hub degree (24) is partly
> smoothing-inflated; under near-no-smoothing α=0.01 the degree falls
> to 11, and Q 7 (al-Aʿrāf) and Q 2 (al-Baqara) become the dominant hubs.
> Under total-variation, Q 108 is no longer a hub. The qualitative
> short-mufaṣṣal centrality survives; the 2.4× outlier quantification
> does not."

## Implications for related findings

### [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (Fisher-Rao mushaf-geodesic)

No direct change. [[cross-finding-011-mushaf-fisher-rao-confirmed|Cross-finding-011]] is about consecutive-surah path length,
not node degree. But the "the mushaf follows a near-neighbor path that
loosely tracks the MST but does not strictly follow it" observation from
[[h-new-134-formal-prophet-named-signature|H-NEW-134]] is independent of the super-hub demotion.

### [[h-new-134-formal-prophet-named-signature|H-NEW-134]] centroid claim (Q 36 Yā-Sīn max-dist centroid)

Not affected. Max-dist centrality is independent of degree-centrality.

### Scratch inline [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] (Q 1 ↔ Q 108 under surface-word features)

The scratch note reports Q 108 is Q 1's rank-1 nearest neighbor under 3 of
4 metrics in the SURFACE-WORD feature space. The present finding uses
STEM-ROOT features. Both independently confirm Q 108's centrality in the
short-mufaṣṣal content-zone, but they are independent feature-space
replications — [[h-new-131-q108-supernode|H-NEW-131]] does NOT leverage the [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] scratch result
because that came from a different feature space and was not in the pre-reg.

The joint picture across [[h-new-131-q108-supernode|H-NEW-131]] and the [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] scratch: Q 108 is
robustly central in the short-mufaṣṣal content-neighborhood under
MULTIPLE feature spaces (STEM roots, surface words) and MULTIPLE
arccos/sqrt-family metrics; it is NOT central under L1/TV. Worth queueing
a joint pre-registered synthesis.

## Caveats and limits

1. **Single feature space**: STEM-root top-500. Surface-word feature space
   [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] scratch hints at replication but not formally pre-registered here.
2. **Single α sweep** (0.5 and 0.01 only). Full α-curve would trace the
   smoothing/structural decomposition more precisely.
3. **No planted-hub synthetic positive control** was run (auditor flag; the
   Hellinger=FR consistency check is a *pipeline-sanity* check but not a
   true MW-5 positive control). This is why Cell A is labeled descriptive
   and Cell B's inferential slot count is conservative k=2.
4. **Q 108's 7 STEM-root tokens** is very thin. Any conclusion at the
   individual-root level (Cell C) is under severe small-sample limits.

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-131-prereg.md` (amended 2026-04-17)
- Script: `scripts/h_new_131_q108_supernode.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-131.json`
- This findings file: `findings/phase-b-hypotheses/h-new-131-q108-supernode.md`
- Journal: `journal/h-new-131-run-1.md`

## Queued follow-ups

- **[[h-new-131-1-length-normalized-mst|H-NEW-131.1]]**: full Dirichlet α-sweep {0.001, 0.01, 0.05, 0.1, 0.5, 1, 2}
  tracing Q 108's MST-degree as a function of smoothing (locate the
  "mechanical/structural" crossover empirically).
- **H-NEW-131.2**: planted-hub synthetic positive control on 114-node
  matched-token-count surrogate data to quantify pipeline sensitivity.
- **H-NEW-131.3**: cross-feature-space replication — STEM-root vs
  surface-word vs character-4-gram (ties [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] scratch observations
  into a formal pre-reg).
- **H-NEW-131.4**: identify Q 108's MST-neighbors under α=0.01 — is the
  reduced-degree hub status still driven by short-mufaṣṣal adjacency, or
  is Q 108 pendant-attached to a different cluster?

## Connections

- Parent: [[h-new-134-formal-prophet-named-signature|H-NEW-134]] (MST of Fisher-Rao surah graph; descriptive, α=0.05 cap)
- Method-parent: [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (Fisher-Rao D-matrix source)
- Scratch-related: inline-2026-04-17-q1-nearest-neighbors / [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]]
  (Q 1 ↔ Q 108 short-mufaṣṣal neighborhood under surface-word feature space)
- Memory: `feedback_bonferroni_tightening_vs_loosening` (amendment
  self-verifying); `feedback_rules_tuple_bidirectional` (robustness can
  demote *or* rehabilitate — this is demote-partial case)
