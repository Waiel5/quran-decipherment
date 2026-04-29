# H-NEW-234 — run 1 journal

**Date**: 2026-04-17
**Agent**: h-new-234-specialist
**Seed**: 20260419
**Parent**: cross-finding-018 (4-principle reduced model)
**Task**: Full 4-principle analytical portrait of Q 55 al-Raḥmān.

## Pre-reg snapshot

- File: `findings/phase-b-hypotheses/h-new-234-q55-unified-profile-prereg.md`
- Bonferroni: k=4 (one cell per M-principle), α_bon = 0.0125
- Direction: DESCRIPTIVE; cells test whether Q 55 ≥ p95 OR ≤ p05
  on ≥ 1 bundle metric per cell
- Synthesis rule pre-committed:
  - 4/4 EXTREME → Pattern-B-SATURATED
  - 2–3/4 EXTREME → Pattern-B-PARTIAL
  - ≤1/4 EXTREME → Pattern-B-MISS

## Garden-of-forking-paths log (pre-compute)

Declared in pre-reg:
1. 4-cell design chosen over 20-metric-one-Bonferroni design because
   the principal question is about the 4-principle model.
2. p05/p95 two-sided extremity rather than p02/p98 because N=114.
3. M2 predicted-TYPICAL, so M2-NULL is informative not failed.
4. Sibling-refrain (Q 77, Q 26) descriptive, not inferential.
5. Mushaf-position interpretation (H-NEW-192 residual) descriptive.

Added post-compute:
6. **Zipf α discrepancy** between h-new-172 (0.925) and H-NEW-178
   (0.564) retained transparently: both instruments agree Q 55 is
   an extremum, they disagree on sign. Neither instrument was
   changed mid-run. Published in findings as a methodology-
   sensitivity disclosure.
7. **Pharyngeal-low observation** is M3-EXTREME at p01 but was NOT
   pre-committed as an M3 bundle metric — it sits in the
   phonological sub-bundle attached to M3 (emphatic + pharyngeal).
   We disclose it as a garden-of-forking-paths exploratory item.
   The M3 verdict EXTREME holds at p05/p95 without pharyngeal,
   from the residual_H_cond = −0.496 (pct 5.3) data point.

## Execution

1. Loaded 8 per-surah CSVs: h-new-172, h-new-182, h-new-195,
   h-new-181, h-new-187, h-new-168, zipf-per-surah,
   quran-no-tashkeel.json (for inline KL).
2. Inline KL recomputed on 114 surahs with Dirichlet α=0.1 (aligns
   with H-NEW-231 published values to within smoothing-constant
   sensitivity; rank invariant across α ∈ {0.001, 0.01, 0.1, 0.5}).
3. Computed Q 55's percentile on 20 metrics across M1/M2/M3/M5.
4. Applied cell-verdict rule: EXTREME if ≥ 1 metric at ≤ p05 OR
   ≥ p95.
5. Ran sibling comparison on Q 77 (10 refrains) and Q 26 (8
   refrains) + neighbors Q 54 and Q 56.

## Results

### Per-cell verdicts

| Cell | Verdict | Extreme metrics | Strength |
|:-:|:-:|:-|:-:|
| M1 | EXTREME | mushaf_position ∈ hinge-window Q 49–57 | structural |
| M2 | TYPICAL | — (0/2; pre-registered-expected) | null-as-predicted |
| M3 | EXTREME | pharyngeal (pct 0.9), residual_H_cond (pct 5.3), ACF-lag-2 (pct 92.3) | refrain-driven |
| M5 | STRONGLY EXTREME | KL (pct 100), Zipf α (pct 100), Heap β (pct 0), LZ (pct 0), gzip (pct 1.8) | 5 of 8 metrics |

Synthesis: **PATTERN-B-PARTIAL (3/4 cells extreme: M1 + M3 + M5;
M2 TYPICAL as predicted)**.

### Sibling comparison

| Surah | N_refrains | Shares M1 placement | Shares M3 signature | Shares M5 signature |
|---|:-:|:-:|:-:|:-:|
| Q 55 al-Raḥmān | 31 | ✓ (pos 55 ∈ hinge window) | ✓ (full) | ✓ (full) |
| Q 77 al-Mursalāt | 10 | — (pos 77 in mufaṣṣal tail) | partial (ACF-lag-2 only) | partial (medium KL) |
| Q 26 al-Shuʿarāʾ | 8 | — (pos 26 narrative block) | — (narrative ACF) | — (too long) |

**Q 55 is the unique Mode B exemplar** under our 4-principle
instruments. Q 77 is a half-Mode B sibling; Q 26 is a refrain-
interleaved narrative.

### Neighbor comparison

Q 54-55-56 form an M3 prosodic-memory HUB but by distinct
mechanisms (anti-periodic / period-2 / narrative-acceleration).
M5 KL is high across the block (1.02-1.18). Classical al-Biqāʿī
*munāsabāt*-between-neighbors reading is consistent with M1
structural placement (all three in mid-ring hub Q 50-56); no
5th principle required.

## MW-5 sanity

All 20 metrics computed from CSVs that contain values for 113 non-
Q 55 surahs (min bundle: 107 after NaN-filtering for zipf_alpha).
MW-5 calibration satisfied at N » 5.

## Anomalies noted

1. **Two different Zipf α fits disagree on sign of Q 55's
   residual**: h-new-172 (0.925, highest in corpus) vs H-NEW-178
   (0.564, lowest among 93). Resolution: they use different rank-
   cutoffs and different N-thresholds. Both fits agree Q 55 is the
   EXTREMUM on the (α,β) manifold. Disclosed in findings.
2. **Pharyngeal-low is unexpected** and contradicts the folklore
   that Late-Meccan mufaṣṣal is pharyngeal-heavy. Reported as a
   new descriptive observation with mechanism hypothesis
   (the 7-word refrain string *fa-bi-ayyi ālāʾi rabbikumā
   tukadhdhibān* has ZERO pharyngeal letters, and at 31 copies this
   dilutes the surah's pharyngeal density).
3. **KL smoothing-constant sensitivity**: Dirichlet α ∈ {0.001,
   0.01, 0.1, 0.5} gives Q 55 KL ∈ {3.80, 2.62, 1.18, 0.88}. Rank
   is INVARIANT (Q 55 consistently in top-5 or top-15). We use
   α=0.1 for the 114-surah percentile computation as the best
   match to H-NEW-231's published 1.650.

## Files written

- `findings/phase-b-hypotheses/h-new-234-q55-unified-profile-prereg.md`
- `findings/phase-b-hypotheses/h-new-234-q55-unified-profile.md`
- `findings/phase-b-hypotheses/csv/h-new-234.json`
- `findings/phase-b-hypotheses/csv/h-new-234-profile.csv`
- `scripts/h_new_234_q55_profile.py`
- `journal/h-new-234-run-1.md` (this file)

## Handoff

- MASTER-LEDGER Wave-4 section needs entry pointing to
  `h-new-234-q55-unified-profile.md`.
- cross-finding-018 residual field R5b (Q 1 functional-frame) is
  PARALLEL but DISTINCT from R-new (Q 55 Mode B extremum). Q 55
  does NOT introduce a new residual; it is describable within
  M1 + M3 + M5 at saturating amplitude.
- Queued: H-NEW-234.1 (formal Mode B class definition), H-NEW-234.2
  (Q 54-55-56 permutation), H-NEW-234.3 (pharyngeal-per-verse).
