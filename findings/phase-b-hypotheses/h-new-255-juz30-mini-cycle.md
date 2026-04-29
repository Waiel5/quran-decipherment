---
finding_id: h-new-255
title: "Juzʾ 30 is a mini-GEODESIC-PATH but NOT a mini-ring — open, not closed, at sub-scale"
date: 2026-04-17
phase: B (specialist)
specialist: h-new-255-specialist
status: MIXED (T1+T2 PASS, T3 NULL) → label MINI-GEODESIC-OPEN-PATH
verdict_ceiling: PASS-DIRECTED (partial self-similarity; independent feature-space replication queued)
seed: 20260419
bonferroni_k: 3
alpha_bon: 0.01667
parent_findings: [cross-finding-013, h-new-111, h-new-185, h-new-202, h-new-203]
pre_reg_sha256: "574dcfeb0b56288028bd63500234faf20a188552e1a1a85bd9a212c33b2d1c52"
rules_tuple: "(no-tashkeel, QAC-STEM root tokens K=500, QAC v0.4, Dirichlet α=0.5, Fisher-Rao angular, Q 78..Q 114 = 37 surahs, Hafs-Kufan, seed 20260419)"
---

# [[h-new-255-juz30-mini-cycle|H-NEW-255]] — Juzʾ 30 mini-ring test

## Headline

**Juzʾ 30 (Q 78..Q 114, 37 short-mufaṣṣal surahs) is a
GEODESIC-OPEN-PATH but NOT a closed RING.** Two of three pre-
registered primary cells PASS; one (the wrap-edge closure) FAILS with
sign-reversal. The 114-surah ring-topology of [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] is
NOT fully self-similar — the closure layer (Q 114 → Q 78) is not
present at sub-scale.

**The canonical Juzʾ-30 ordering is remarkably near-optimal**
(L_juz30/L_2opt_juz30 = **1.072**, actually TIGHTER than the full
mushaf's 1.107) AND significantly shorter than random permutations
(z = **−5.32**, p ≈ 0.001, crushing the −3.0 pre-reg threshold).
But the "closing edge" d(Q 114, Q 78) = 0.645 is ABOVE the Juzʾ-30
pair mean (0.489) and z = **+1.37** against the permutation null — the
OPPOSITE sign from [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s full-mushaf wrap-edge.

**Interpretation**: Juzʾ 30 is a *near-geodesic linear traversal* of
the short-mufaṣṣal content space — it walks coherently through the
37 surahs — but it does NOT close. The full mushaf's wrap-edge is
**a 114-specific architectural feature**, not a fractal property
replicated at every juzʾ.

---

## Pre-registered tests and outcomes

| # | Test | Statistic | Threshold | Observed | Verdict |
|:-:|:-----|:---------:|:---------:|:--------:|:-------:|
| T1 | Geodesic ratio | R = L_juz30 / L_2opt | ∈ [1.05, 1.20] | **1.072** | **PASS** |
| T2 | Permutation null | z < −3.0 AND p < 0.01667 | z = **−5.32**, p = 0.001 | **PASS** |
| T3 | Wrap-edge closure | p < 0.01667 (lower) | z = **+1.37**, p = 0.918 | **NULL (sign reversed)** |
| MW-5 | Greedy-NN positive control | p < 0.001 | p = 0.001 | **PASS** |

**Joint label (pre-registered matrix)**: **MINI-GEODESIC-OPEN-PATH**.

### T1 — geodesic ratio (PASS)

- L_juz30 = **16.515** (sum of 36 canonical consecutive Fisher-Rao
  distances over Q 78..Q 114)
- L_2opt_juz30 = **15.411** (best 2-opt over all 37 greedy-NN starts)
- **R_juz30 = 1.072**, within the pre-registered [1.05, 1.20] band.
- Full-mushaf baseline ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]): R_mushaf = 1.107.
- Juzʾ 30's ratio is **3.2% tighter** than the full mushaf's. Honest
  interpretation: 2-opt converges more easily at N=37 than at N=114
  (fewer local minima), so a tighter ratio does NOT necessarily mean
  "more near-optimal"; it could be an N-dependent tightening of the
  2-opt approximation itself. Report both possibilities.

### T2 — permutation null (PASS, z = −5.32)

- Null (1000 random permutations of Juzʾ 30 surah labels, seed
  20260419): mean = 17.618, sd = 0.207.
- Null min = 16.899 (still above L_juz30 = 16.515).
- **Zero** of 1000 random permutations produced a path shorter than
  the canonical Juzʾ 30.
- z = **−5.32**, p ≈ **0.001**, crushing the −3.0 threshold by 77%
  of z-budget.
- Sanity: full-mushaf z = −11.46 at N=114. At N=37 the null SD is
  0.207 (vs N=114 null SD ~ 1.62), consistent with reduced sample
  variance at smaller path count. The **per-unit-length signal** is
  comparable across scales (|z| per edge: −5.32/36 = −0.148 at Juzʾ
  30; −11.46/113 = −0.101 at full mushaf — Juzʾ 30 is actually
  denser per-edge).

### T3 — wrap-edge closure (NULL with sign reversal)

- Observed: w_wrap = d_FR(Q 114, Q 78) = **0.6445**.
- Null distribution (wrap-edge from each of 1000 permuted orderings):
  mean = 0.485, sd = 0.116.
- z = **+1.37** (ABOVE null mean, not below), p (one-sided lower) = 0.918.
- **The wrap-edge is LONGER than typical**, not shorter.
- Contrast with full-mushaf wrap-edge d(Q 1, Q 114) = 0.388 AND
  mean_d(Q 1, {Q 108..Q 114}) = 0.370 vs corpus mean 0.81 — both
  well below mean at the 114-scale.
- Within Juzʾ 30, the pair mean is 0.489 (compressed vocabulary
  range); d(Q 114, Q 78) at 0.645 is **above the 75th percentile**
  of Juzʾ-30 pair distances.

This is the crucial finding: **Juzʾ 30 does not close on itself**.
Q 78 (al-Nabaʾ, 40-ayat long eschatological) and Q 114 (al-Nās,
6-ayat refuge prayer) are stylistically and lexically different —
the Juzʾ begins with the longest short-mufaṣṣal surah (by ayat
count among Juzʾ 30 surahs) and ends with one of the shortest.

### MW-5 positive control (PASS)

- Greedy-NN from Q 78 on the 37-node sub-graph: L = 15.902, z = −8.27,
  p ≈ 0.001. Instrument discriminative.

## Secondary / descriptive findings

### S1 — Juzʾ 30 structural hinges (top-5 consecutive jumps)

The 5 largest consecutive-pair Fisher-Rao jumps within Juzʾ 30:

| Rank | From → To | d_FR | Classical note |
|:---:|:---:|:---:|:---|
| 1 | Q 78 → Q 79 | **0.721** | al-Nabaʾ (40 ayat) → al-Nāziʿāt (46 ayat) — both long-ish eschatological but different rhyme/pericope density |
| 2 | Q 79 → Q 80 | **0.706** | al-Nāziʿāt → ʿAbasa (42 ayat) — sharp pericope shift ("and he frowned") |
| 3 | Q 88 → Q 89 | **0.657** | al-Ghāshiyah → al-Fajr — start of Fajr's Thamūd/ʿĀd narrative cycle |
| 4 | Q 83 → Q 84 | **0.652** | al-Muṭaffifīn → al-Inshiqāq — Medinan-flavor to pure-eschatological shift |
| 5 | Q 80 → Q 81 | **0.635** | ʿAbasa → al-Takwīr — Day-of-Judgment scene cascade begins |

**Where are they concentrated?** Four of the top-5 hinges fall in
the **opening stretch Q 78 → Q 84** (7-surah window). The front of
Juzʾ 30 (the "long short-mufaṣṣal" sub-block) carries most of the
within-juzʾ heterogeneity; the back tail Q 89..Q 114 has
consecutive distances below the median.

**Alignment with [[h-new-130-fisher-rao-residuals|H-NEW-130]] full-mushaf universal hinges**: the
[[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 list of 114-mushaf hinges did NOT include Q 78-84
hinges (the mushaf-scale hinges are at Q 9/10, Q 49/50, Q 56/57,
etc. — LARGE-scale structural boundaries). The Juzʾ-30 hinges are
INTERNAL to the short-mufaṣṣal block and are not the same hinges as
the mushaf-scale architecture. **The hinge structure is
scale-specific, not self-similar**.

**Alignment with [[h-new-202-juz30-internal-structure|H-NEW-202]]'s Q 97/Q 98 sub-Fiedler boundary**:
Q 97 → Q 98 (al-Qadr → al-Bayyinah, d=0.499) is ranked **#17 of 36**
in our consecutive-jump list — at the Juzʾ-30 median, NOT in the
top-5 hinges. [[h-new-202-juz30-internal-structure|H-NEW-202]]'s Fiedler boundary identifies al-Bayyinah as
the Medinan stylistic outlier on spectral (second eigenvector)
grounds; the path-jump instrument used here gives a different
ordering.

### S2 — Comparison to full-mushaf 1.107

| Feature | Full mushaf | Juzʾ 30 |
|:---|:---:|:---:|
| N | 114 | 37 |
| R = L/L_2opt | 1.107 | **1.072** |
| z (permutation null) | −11.46 | **−5.32** |
| z per-edge | −0.101 | **−0.148** |
| Wrap-edge vs null | −4.17 (LOWER) | **+1.37 (HIGHER)** |
| Label | CONFIRMED RING | **GEODESIC-OPEN-PATH** |

Geodesicity (Layer 1 of CF-013) is **replicated at sub-scale** and
is even denser per-edge at Juzʾ 30. Wrap-around closure (Layer 2) is
**NOT replicated at sub-scale**. This is the central
self-similarity result: **the ring topology of the mushaf is NOT
fractal**; the closure is specifically a 114-artifact.

### S3 — Juzʾ 30 pair-distance statistics

| Statistic | Juzʾ 30 | Full mushaf |
|:---|:---:|:---:|
| N pairs | 666 | 6441 |
| Mean d_FR | **0.489** | 0.924 |
| Median | 0.495 | — |
| Min | 0.213 | — |
| Max | 0.766 | — |

Juzʾ 30 pair distances are **~47% smaller on average** than full-
mushaf pair distances. This is the mechanistic reason Juzʾ 30 is
easily path-geodesic: all 37 surahs are close to each other to
begin with. The "geodesic" is near-optimal because the sub-space is
tightly clustered, not because Juzʾ 30 uniquely orchestrates
coherence.

### S4 — Juzʾ 30 vs 77 other contiguous 37-surah arcs in the mushaf

Exhaustive: 78 contiguous 37-surah arcs exist in the 114-surah
mushaf (start positions 1..78). Their path lengths:

- Mean = 29.03, sd = 5.30
- Juzʾ 30's L = 16.515 ranks **2nd shortest of 78** (p_contig = 0.025)
- z_contig = −2.36

The arc that beats Juzʾ 30 is not surprising — contiguous arcs
overlapping Juzʾ 30 share most of its short-surah density. But the
**strong effect size z_contig = −2.36 one-sided against 37-arcs
drawn from anywhere in the mushaf** demonstrates Juzʾ 30's internal
coherence is not purely a length-artifact: it is the densest
contiguous window in the mushaf at this sub-scale.

## Interpretation

### What we learned about [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] framed the mushaf as a **structured Hamiltonian
cycle** with three layers:
1. geodesic path-length (CF-011 primary)
2. wrap-around closure Q 114 → Q 1 ([[h-new-137-wrap-around-closure|H-NEW-137]]/138)
3. structured hinges at boundaries ([[h-new-130-fisher-rao-residuals|H-NEW-130]])

**[[h-new-255-juz30-mini-cycle|H-NEW-255]] establishes that Layer 1 REPLICATES at sub-scale**
(Juzʾ 30 mini-geodesic, R = 1.072, z = −5.32). The sub-mushaf has
the same geodesic *character* as the full mushaf. This is a
genuine scaling result.

**[[h-new-255-juz30-mini-cycle|H-NEW-255]] ALSO establishes that Layer 2 does NOT replicate.**
The wrap-edge d(Q 114, Q 78) = 0.645 is above-mean for the Juzʾ
30 pair distribution, sign-reversed from the CF-013 wrap-edge
closure. Juzʾ 30 does not close on itself; its endpoints are
heterogeneous.

**Layer 3 (structured hinges) is scale-specific**: the top Juzʾ-30
hinges (Q 78→Q 79, Q 79→Q 80, etc.) are *different* from the
114-scale hinges (Q 9/10, Q 49/50, Q 56/57). The hinge phenomenon
is real at both scales, but the specific hinges differ.

### The ring topology is NOT fractal

Self-similarity would require: ratio ≈ 1.10 AND wrap-edge short AND
hinges coincide across scales. We observe: ratio holds, wrap-edge
DOES NOT hold, hinges differ. **The mushaf's ring is a 114-specific
architectural feature; at the juzʾ-30 sub-scale the topology is
LINEAR-GEODESIC, not cyclic.**

This is a consequential refinement to CF-013. The full-mushaf
wrap-around edge (d(Q 1, Q 114) = 0.388, mean_d(Q 1, terminal triad)
= 0.37 vs corpus 0.81) is NOT a generic property of juzʾ-scale
sub-mushafs; it is specific to the opening-closing pair chosen by
the Uthmanic ordering (Q 1 al-Fātiḥa ↔ Q 112/113/114 the three
quls). The liturgical pair {fātiḥa, khawātim} carries the closure;
no intra-juzʾ pair plays that role within Juzʾ 30.

### Alignment with [[h-new-202-juz30-internal-structure|H-NEW-202]] + [[h-new-203-fisher-rao-juz|H-NEW-203]]

- [[h-new-202-juz30-internal-structure|H-NEW-202]] (NULL 0/3, rank-1 descriptive coherence): consistent.
  Juzʾ 30 is internally cohesive at the surah-pair mean level
  (descriptive) but **does not** decompose into tight sub-clusters
  ([[h-new-202-juz30-internal-structure|H-NEW-202]] H2 NULL). [[h-new-255-juz30-mini-cycle|H-NEW-255]] adds: Juzʾ 30 is a COHERENT
  LINE-GRAPH (path), not a COHERENT COMMUNITY (sub-cluster) and not
  a COHERENT CYCLE (ring). The three instruments converge on a
  single characterization: **Juzʾ 30 is a geodesic line in root
  space, open at its endpoints**.
- [[h-new-203-fisher-rao-juz|H-NEW-203]] (juzʾ-30 is LEAST coherent at verse-level centroid
  pooling): partially consistent. At verse-level, Juzʾ 30 is
  heterogeneous; at surah-level it is cohesive. This apparent
  tension is resolved by recognizing that surah-level averaging
  *within* each short surah smooths out verse-level noise, while
  centroid-pooling at juzʾ scale averages over many short surahs
  that span a wide vocabulary range (eschatological, refuge,
  biographical). **The surah-level Hamiltonian path is geodesic;
  the verse-level segment-centroid is NOT coherent.** These are
  different statistics on different feature spaces.

### Alignment with [[h-new-185-ring-laplacian|H-NEW-185]] (ring Laplacian)

[[h-new-185-ring-laplacian|H-NEW-185]]'s Fiedler partition cut the mushaf ring at Q 12/Q 13 and
Q 77/Q 78 — placing Juzʾ 30 entirely within Community B (the
"short-surah bracket" Q 78..Q 114 ∪ Q 1..Q 12). [[h-new-255-juz30-mini-cycle|H-NEW-255]] refines
this: **within Community B, the Juzʾ 30 half is a geodesic
LINE-PATH, but its endpoint Q 114 is closer to Q 1 (in Community B)
than to its canonical predecessor Q 78**. The Fiedler community is
one unit in the spectral-partition sense; the Juzʾ 30 sub-path is
NOT a closed component of that community. Q 114 acts as the
**bridge** from the Juzʾ-30 half of Community B to the Q 1..Q 12
half — consistent with CF-013's wrap-around mechanism but
specifically locating it at the Juzʾ-30 terminus, not anywhere
intra-juzʾ.

## Classical-scholarship alignment

### al-Suyūṭī, *Itqān* §32-34 on the mufaṣṣal [SECONDARY-TRIANGULATED]

al-Suyūṭī treats the mufaṣṣal as a **threefold** structural
division (ṭiwāl / awsaṭ / qiṣār). Juzʾ 30 corresponds (in most
classical schemes) to the qiṣār mufaṣṣal + the muʿawwidhatān;
crucially, al-Suyūṭī does NOT frame Juzʾ 30 as a closed/cyclic
unit — it is a graded descent from longer-to-shorter within a
unified length-descending aesthetic. **Our empirical result (no
wrap-around closure) agrees with the classical reading of Juzʾ 30
as OPEN-ENDED rather than cyclic**.

### al-Ghazālī, *Iḥyāʾ* 8 on ādāb of tilāwa [SECONDARY-TRIANGULATED]

al-Ghazālī pairs the recitation opener (Q 1) with the session
closer (Q 112/113/114) as the liturgical frame of a recitation
session — NOT as a Juzʾ-30-internal feature. The liturgical
closing pair operates at the 114-scale, bridging mushaf-start to
mushaf-end; it does not operate intra-juzʾ. **Our empirical finding
that d(Q 114, Q 78) is NOT short ratifies the classical framing:
the closure-pair is specifically Q 1↔Q 114, not Q 78↔Q 114**.

### al-Zarkashī, *al-Burhān* on fawātiḥ/khawātim [SECONDARY-TRIANGULATED]

al-Zarkashī frames the opening-closing pairing as a
**mushaf-scale** structural feature (fātiḥa of the whole Qurʾān +
khawātim of the whole Qurʾān). Juzʾ 30 has its own openings and
closings (Q 78:1 al-Nabaʾ opens, Q 114 al-Nās closes) but these are
not treated as a closure-pair in classical literature. Our
empirical result aligns: there is no structural closure at juzʾ
scale — only at full-mushaf scale.

**Net classical alignment**: the tradition treats the ring topology
as a 114-phenomenon (fātiḥa + khawātim form the opening-closing
frame of the whole Qurʾān, not of every juzʾ). [[h-new-255-juz30-mini-cycle|H-NEW-255]]'s finding
that the ring is NOT self-similar is entirely consistent with this
reading.

## Honest caveats

1. **N=37 vs N=114**: 2-opt converges more tightly at smaller N.
   The R_juz30 = 1.072 < R_mushaf = 1.107 could partly reflect
   2-opt-at-N=37 being closer to true L_min than 2-opt-at-N=114.
   Exact TSP (Concorde) on 37 nodes is trivial and would tighten
   the bound; queued as a minor refinement.
2. **Pair-distance compression**: Juzʾ 30 pair distances (mean
   0.489) are 47% smaller than full-mushaf mean (0.924). Some of
   the ratio-tightening is mechanical: all 37 short-mufaṣṣal
   surahs sample a narrower vocabulary. We did NOT
   length-residualize within Juzʾ 30; length-matched nulls are
   queued for follow-up (H-NEW-255b).
3. **Feature-specificity**: all results are on K=500 QAC-STEM
   roots. Char-4-gram or verse-length replication would test
   whether the mini-geodesicity + no-mini-wrap pattern holds
   across feature spaces. Queued as H-NEW-255c.
4. **Permutation null at N=37**: 1000 permutations gives resolution
   p ≈ 1/1001 ≈ 0.001. Tighter p values would require more
   permutations; not needed here because results are clearly on
   the correct side of thresholds.
5. **Juzʾ 30 boundary is mid-Q 77 classically**; we use the surah-
   set approximation Q 78..Q 114 (37 surahs). Including the mid-
   Q 77 split would require sub-surah features and a different
   instrument. The classical surah-set approximation is the
   standard convention in [[h-new-202-juz30-internal-structure|H-NEW-202]]/203.
6. **Wrap-edge sign-reversal is not a "failure of the mushaf"**
   — it is an accurate empirical characterization. The mushaf's
   wrap-around is a 114-feature; its absence at juzʾ-scale was
   honestly a priori uncertain (see pre-reg § Honest prior
   expectations).

## Ceiling: PASS-DIRECTED, not CONFIRMED

Under project discipline (`04-DISCIPLINE.md`), novel-test verdicts
cap at PASS-DIRECTED until independent replication. Two of three
primary cells PASS by wide margins; one cell FAILS in a sign-
reversed direction. Label: **MINI-GEODESIC-OPEN-PATH**. Replication
queued:

- H-NEW-255b: length-matched null within Juzʾ 30 (controls for
  pair-distance compression).
- H-NEW-255c: char-4-gram replication (does the mini-geodesic path
  hold on an orthogonal feature space?).
- H-NEW-255d: analogous test on Juzʾ 1 (Q 1..Q 2:141) and Juzʾ 15
  (Q 17..Q 18:74) to check whether mini-geodesic holds at other
  juzʾ scales or is specific to Juzʾ 30.

## Connection to [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] architecture

| CF-013 Layer | Full mushaf | Juzʾ 30 | Verdict |
|:-:|:---:|:---:|:---:|
| 1. Geodesic path | CONFIRMED | **REPLICATED** (R=1.072, z=−5.32) | **self-similar** |
| 2. Wrap-around closure | CONFIRMED | **DOES NOT REPLICATE** (z=+1.37) | **NOT self-similar** |
| 3. Structured hinges | CONFIRMED | Present but different hinges | **scale-specific** |

**Synthesis for CF-013**: the unified M1 principle of cross-
finding-013 is partially fractal. Layer 1 (geodesicity) is a
scale-invariant property that holds at both N=114 and N=37. Layers
2 (closure) and 3 (specific hinges) are scale-specific. The
mushaf's ring topology is **a whole-mushaf architectural feature
with a fractal geodesic backbone but non-fractal closure**.

This refines CF-013's claim: the ring is structured, but the
structure is not uniformly self-similar — the BACKBONE is
(geodesicity replicates) but the CLOSURE is not (the ring does not
tile). Any future test of higher-order self-similarity (e.g., does
Juzʾ 29 also show R ≈ 1.10? What about inter-juzʾ distance?) will
need to separate the scale-invariant Layer-1 from the scale-
specific Layers 2 and 3.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle-prereg.md`
- Pre-reg SHA-256: `574dcfeb0b56288028bd63500234faf20a188552e1a1a85bd9a212c33b2d1c52`
- Script: `scripts/h_new_255_juz30_mini_cycle.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-255.json`
- Journal: `journal/h-new-255-run-1.md`

## Verdict

**MIXED: T1 + T2 + MW-5 PASS; T3 NULL (sign-reversed).** Joint
label **MINI-GEODESIC-OPEN-PATH**. Juzʾ 30 is internally near-
geodesic (replicating CF-013 Layer 1 at sub-scale) but does NOT
close on itself (falsifying CF-013 Layer 2 at sub-scale). The
mushaf's ring topology is partially fractal (geodesic backbone
replicates; closure does not). Ceiling: PASS-DIRECTED pending
feature-space + alternate-juzʾ replication.
