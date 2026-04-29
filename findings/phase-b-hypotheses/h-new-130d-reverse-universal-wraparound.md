# [[h-new-130d-reverse-universal-wraparound|H-NEW-130d]] — Reverse-order trivial + universal-hinges + wrap-around integration

**Finding ID**: [[h-new-130d-reverse-universal-wraparound|h-new-130d]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent**: [[h-new-130-fisher-rao-residuals|H-NEW-130]] / [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]] / [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]] (all CONFIRMED / REPLICATED)
**Also integrates**: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] (mushaf as topological ring), [[h-new-137-wrap-around-closure|H-NEW-137]] (wrap-around closure)
**Type**: post-hoc descriptive INTEGRATION finding (not a new pre-registered claim); no new Bonferroni slot
**Verdict**: three-part result, each with its own type

## What this finding is and isn't

Team-lead queued three sub-tasks:
- **T-L.1**: apply boundary-test to REVERSE mushaf order (same 15 hinges?)
- **T-L.2**: identify UNIVERSAL hinges across all 3 feature spaces
- **T-L.3**: how does [[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b/130c interact with [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] wrap-around?

None of these are new pre-registered hypothesis-tests. T-L.1 is a mathematical exercise (the answer is trivial by metric-symmetry). T-L.2 is a cataloging/descriptive task already answered by [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]'s Secondary B output. T-L.3 is a cross-finding-integration analysis on already-computed D-matrices.

So this document is a **post-hoc descriptive integration finding** with no new p-values pre-registered. The three sub-results are each reported with their appropriate type: T-L.1 is a mathematical note, T-L.2 is a catalog-reference to existing cell, T-L.3 is an EXPLORATORY-POST-HOC observation.

---

## T-L.1 — Reverse-mushaf boundary test

### Result: TRIVIALLY IDENTICAL (by metric symmetry)

Fisher-Rao distance is symmetric: `D[i, j] = D[j, i]`. The consecutive pairs of the reversed mushaf (114→113, 113→112, ..., 2→1) are the same UNORDERED pairs as the forward mushaf (1→2, 2→3, ..., 113→114). Since top-15 is a set-of-unordered-pairs operation, the top-15 is identical. Boundary-coincidence (|M ∩ B|) is identical.

**Verification** (programmatic, script `scripts/h_new_130_fisher_rao_residuals.py` + ad-hoc check): forward-top-15 unordered-pair set == reverse-top-15 unordered-pair set at 15/15 intersection on all three feature spaces.

### Why the test is not meaningfully informative

Symmetry of the metric is a mathematical property, not an empirical finding. The test as team-lead phrased it cannot distinguish a "hinge-marking" mushaf from any other ordering — it is invariant under reversal.

### Non-trivial variant (suggested for T-L.1-alt)

A meaningfully-different ordering-permutation is one that is NOT simply a reversal, e.g., **length-sorted**, **chronological (Nöldeke)**, **odd-even interleaved**, or **random**. Those would break the "same top-15" property and would probe whether the top-15 hinges are mushaf-specific.

The closest-in-spirit test already in the corpus: **MW-5 in [[h-new-130-fisher-rao-residuals|H-NEW-130]] and [[h-new-130b-fisher-rao-residuals-char4gram|H-NEW-130b]]/130c** — synthetic sort-by-verse-count ordering produces ZERO overlap with the mushaf's top-15 on any feature space. Length-sort is NOT a mushaf-preserving transformation; the top-15 is mushaf-specific at 0/15 shared under length-sort.

**Verdict on T-L.1**: reverse-mushaf is trivially identical by metric symmetry; the non-trivial length-sort version was already answered in [[h-new-130-fisher-rao-residuals|H-NEW-130]]'s MW-5 (mushaf-specificity confirmed).

---

## T-L.2 — Universal hinges across 3 feature spaces

Already reported as **Secondary B of [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]**. Cross-referenced here for the integrated-findings view.

### The 3 universal hinges

| pair | boundary types |
|:---:|:---|
| **Q 14 → Q 15** | phase_Late-Meccan→Middle-Meccan (Ibrāhīm → al-Ḥijr; both ALR muq) |
| **Q 49 → Q 50** | mufaṣṣal-alt_start, muq_presence, period_Medinan→Meccan, phase_Medinan→Middle-Meccan (al-Ḥujurāt → Qāf) |
| **Q 56 → Q 57** | period_Meccan→Medinan, phase_Early-Meccan→Medinan (al-Wāqiʿah → al-Ḥadīd; **musabbiḥāt entry**) |

### Null-expectation for 3-way intersection

For three independent 15-of-113 selections, naive expected intersection is `15³ / 113² ≈ 0.26`. Observed 3; ~11× null. Under the stricter assumption that each top-15 set is CORRELATED (because all three reflect underlying mushaf structure), the effective null is higher and the observed 3 is less surprising — but still structural.

### What these three pairs share

All three are **period- or phase-axis boundaries** AND have **liturgical/structural significance**:
- Q 14→15: reading-cluster edge (long-الم block → prophet-narrative block)
- Q 49→50: mufaṣṣal canonical start (one of several; alt-variant)
- Q 56→57: entry to musabbiḥāt cluster

None of the 3 universal hinges are in the long-mufaṣṣal or short-mufaṣṣal zones. Mushaf's most feature-invariant boundaries are all in **the middle of the mushaf**, at classically-recognized structural transitions.

**Verdict on T-L.2**: CATALOGED. Three universal hinges identified. All three are classical structural transitions. File into [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] addendum for synthesis.

---

## T-L.3 — Wrap-around edge interaction

### Setup

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]] established that mushaf order behaves like a **topological ring**: Q 114 al-Nās is Fisher-Rao-close to Q 1 al-Fātiḥa, such that an "invisible closure edge" would make the mushaf into a closed loop rather than an open path.

[[h-new-130-fisher-rao-residuals|H-NEW-130]] established that the mushaf's 15 largest forward-consecutive pair distances are ALL structural-boundary hinges. If the wrap-around edge Q 114 → Q 1 were to be included in the set of candidate edges, does it behave like a HINGE (high distance, structural boundary) or like a CONTINUITY edge (low distance, non-boundary)?

### Empirical result (all three feature spaces)

| Feature | d(Q 114 → Q 1) | Mean of 113 forward pairs | Forward-top-15 cutoff | Rank among 113 forward pairs | In forward top-15? |
|---|---:|---:|---:|:-:|:-:|
| Root (QAC-STEM) | 0.388 | 0.759 | 1.002 | **97 of 113** | NO |
| Char-4-gram | 0.423 | 0.790 | 1.035 | **98 of 113** | NO |
| Verse-length | **0.083** | 0.687 | 1.263 | **113 of 113** (SMALLEST) | NO |

**The wrap-around edge is NOT a hinge on any feature space.** It is a strong-continuity edge, especially on verse-length (literally rank-1 smallest of all 113+1 candidate edges — Q 114 and Q 1 have nearly identical verse-length distributions).

### What this means

The mushaf's **open-path architecture** has two topologically distinct edge-types:

1. **Structural-hinge edges**: the 15 top-distance consecutive pairs, all in the pre-committed boundary set B. Mark transitions between named sections (Meccan/Medinan, muqaṭṭāʿat-clusters, sabʿ al-ṭiwāl, mufaṣṣal).
2. **Continuity edges**: the 98 non-top-15 consecutive pairs (and the invisible wrap-around edge). Low distance, connect adjacent surahs in a coherent local sequence.

**The wrap-around edge is a CONTINUITY edge, not a hinge.** It supports [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s topological-ring claim. If Q 114 → Q 1 were added as the 114th edge of a closed ring, it would be among the SHORTEST edges — meaning a ring-structure mushaf (the hypothesized reading cycle) is geodesically-efficient CLOSED, not just open.

### Implication for [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] topological-ring claim

[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s evidence gets stronger under [[h-new-130d-reverse-universal-wraparound|H-NEW-130d]]: not only is d(Q 114, Q 1) low (which [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] established), but d(Q 114, Q 1) is ALSO not at a hinge. The ring-closure is smooth, not structurally-marked — exactly what a topological-ring metaphor predicts. Cyclical reading patterns (e.g., a "recite from al-Fātiḥa to al-Nās and start again" liturgical practice) fit this architecture.

### Under theorist's 6-principle (or 5-principle, post-P2+P8 merger) model

If P8 (wrap-around liturgical ring) and P2 (local-continuity Fisher-Rao geodesic) merge, the merged principle becomes: **"mushaf is a structured-cycle geodesic"** — local-continuity (P2) with structural-boundary hinges ([[h-new-130-fisher-rao-residuals|H-NEW-130]] decomposition) and smooth wrap-around closure (P8). [[h-new-130d-reverse-universal-wraparound|H-NEW-130d]] provides the three-part empirical anchor for this merger.

**Verdict on T-L.3**: EXPLORATORY-POST-HOC. Wrap-around edge behaves as continuity on all 3 feature spaces, consistent with [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s ring-closure claim. This is descriptive integration, not a new hypothesis-test; a future pre-reg could formalize "structured-cycle geodesic" as a unified claim.

---

## Integrated observation

The mushaf has three distinct edge-types in Fisher-Rao space:

1. **15 structural-hinge edges** (forward-top-15 in at least one feature space): all in B.
2. **3 UNIVERSAL structural-hinge edges** (in forward-top-15 of ALL three features): Q 14→15, Q 49→50, Q 56→57.
3. **~98 continuity edges** (non-top-15 forward pairs): low distance, coherent local sequence.
4. **1 wrap-around edge** (Q 114 → Q 1, not observed in mushaf but hypothesized): CONTINUITY-type, supports topological-ring.

This is consistent with a **"punctuated continuity" architecture**: the mushaf is a smooth path through root-distribution space, punctuated by 15 deliberately-large structural jumps at classical boundaries. The 3 universal hinges are the maximum-robustness structural markers (appear in every feature-space view). The wrap-around closes the ring smoothly, not at a hinge.

---

## Limits

1. **T-L.1 result is mathematically trivial**, not informative. Reporting for completeness.
2. **T-L.2 null expectation is naive** (assumes independence of 3 feature-space top-15 sets, which is not strictly true). The cardinality-3 pre-committed threshold was conservative; hitting exactly 3 is not a ceiling-bound result.
3. **T-L.3 is exploratory-post-hoc**. The wrap-around analysis was done AFTER seeing the top-15 hinges on all three feature spaces. Formal inferential claim requires independent pre-reg. Reporting as descriptive observation integrating existing findings.
4. **Nothing here substitutes for cross-corpus replication** (T-L.4, pending). Everything is within-Quran; nothing probes whether a similarly-structured non-Quranic corpus would exhibit the same pattern.

## Files

- Parent findings: [[h-new-130-fisher-rao-residuals|H-NEW-130]], 130b, 130c (all written).
- Parent D-matrices: [[h-new-111-fisher-rao-mushaf|H-NEW-111]], 111b, 111c.
- [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] (topological-ring) written separately.
- This file is integration-only; no new script (logic in inline bash of journal for reproducibility).

## Action for other teammates

- **Integrator**: consider whether [[h-new-130d-reverse-universal-wraparound|H-NEW-130d]] is a standalone finding worthy of a MASTER-LEDGER row, or whether it should be folded into [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s addendum + [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] cross-reference. My recommendation: the latter.
- **Theorist**: the three-part integration (hinges + universal + wrap-around-continuity) may simplify the 5-principle model further. If P2 (local continuity) and P8 (wrap-around ring) can merge under "punctuated structured-cycle geodesic", that's potentially a 4-principle model.
- **Auditor**: no new inferential claim in [[h-new-130d-reverse-universal-wraparound|H-NEW-130d]]; I've explicitly tagged T-L.3 as EXPLORATORY-POST-HOC.
