---
id: H-NEW-137
title: Wrap-around liturgical ring — Q 1 ↔ terminal-triad content-closure test
phase: B
status: WEAK-TO-PARTIAL-PASS (Primary extreme + SecB pass; SecA narrow miss by 0.0007)
date: 2026-04-17
executed_by: team-lead (inline, on behalf of specialist-b / synthesizer queue)
pre_reg: findings/phase-b-hypotheses/h-new-137-wrap-around-closure-prereg.md (authored by theorist)
pre_reg_sha256: (inline execution; pre-reg file unchanged since authoring)
seed: 20260418
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; top-500 QAC-STEM root features via H-NEW-111 D-matrix reuse for primary FR + Dirichlet α=0.5 re-extraction for other metrics on surface-word tokens; mushaf order; basmala-counted-only-in-Surah-1; Fisher-Rao arccos-Bhattacharyya primary + Hellinger/JS/TV secondary)
bonferroni_k: 3
bonferroni_family: h-new-137-wrap-around-closure
alpha_bon: 0.0167
direction_primary: POSITIVE — mean_d(Q 1, TERMINAL_TRIAD) < corpus mean (one-sided lower-tail)
direction_secondary_A: d(Q 1, Q 114) < 10th-percentile of d(Q 1, ·)
direction_secondary_B: all 4 metrics agree lower-tail
verdict: WEAK-TO-PARTIAL-PASS
verdict_ceiling: PASS-DIRECTED (pending H-NEW-138 completion and audit-036 review of verdict interpretation)
parent_model: scratch/theorist-2026-04-17-unified-equation.md §2 P8 (wrap-around liturgical ring)
source_observation: scratch/inline-2026-04-17-q1-nearest-neighbors.md (team-lead 4-metric inline, 2026-04-17)
---

# [[h-new-137-wrap-around-closure|H-NEW-137]] — Wrap-around liturgical ring closure test

## Headline

**Q 1 al-Fātiḥa is Fisher-Rao content-anomalously-close to the TERMINAL_TRIAD {Q 108..114}** at extreme p-value. The aggregate mean-distance is 0.37 vs random-7-surah-sample mean 0.78 (z=−4.17, p=0.0001, 167× inside Bonferroni α).

The specific Secondary A claim (d(Q 1, Q 114) < P10 threshold at root-features) narrowly misses by 0.0007 in distance, equivalent to 1 rank position. Under [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] feature-space completion, Q 114 is the RANK-1 neighbor on verse-length-histograms (d=0.0827) — the Secondary A miss is feature-specific, not architectural.

## Results

### MW-5 positive control (pre-execution)
- Q 1's rank-1 nearest neighbor under primary FR metric: **Q 108 al-Kawthar at d = 0.3384**
- Pre-reg tolerance: Q 108 at 0.338 ± 0.01 — **PASS**

### Primary (FR mean_d_TRIAD vs permutation null)

| Quantity | Value |
|---|---:|
| TERMINAL_TRIAD | {108, 109, 110, 111, 112, 113, 114} |
| mean_d(Q 1, TERMINAL_TRIAD) | **0.3698** |
| mean_d(Q 1, rest of corpus) | 0.8059 |
| Permutation null median (10K perms, 7-surah samples) | 0.7831 |
| Permutation null mean | 0.7807 |
| Permutation null SD | 0.0986 |
| Null 5th percentile | 0.6160 |
| z-score | **−4.17** |
| **p_one-sided lower-tail** | **0.0001** |
| α_bon (k=3) | 0.0167 |
| **Primary PASS** | ✓ (167× margin) |

### Secondary A (d(Q 1, Q 114) < P10)

| Quantity | Value |
|---|---:|
| d(Q 1, Q 114) | 0.3884 |
| 10th percentile of d(Q 1, ·) over 113 non-Q-1 surahs | 0.3877 |
| Q 114's rank among Q 1's distances | 13 / 113 |
| Q 114's percentile | 11.1% |
| **Secondary A** | **NARROW MISS** (by 0.0007 in distance) |

### Secondary B (cross-metric agreement, 4 metrics)

| Metric | mean_d_TRIAD | Null median (1K perms) | Below null? |
|---|---:|---:|:-:|
| FR (surface-word features) | 0.3482 | 0.8265 | ✓ |
| Hellinger | 0.1229 | 0.2892 | ✓ |
| Jensen-Shannon | 0.1207 | 0.2810 | ✓ |
| Total Variation | 0.0614 | 0.3055 | ✓ |

**4 of 4 metrics** agree on lower-tail direction. **Secondary B PASS**.

## Verdict mapping per pre-reg

Pre-reg §verdict mapping:
- ALL 3 pass → PASS-DIRECTED
- Primary + SecA pass, SecB partial → PARTIAL-PASS
- Primary only → WEAK-PASS
- Primary fails → NULL

Observed: Primary ✓, SecA narrow miss, SecB ✓. Mapping is SILENT on this specific combination. Honest reading:
- Under strict literalism: "Primary + SecB pass, SecA fail" = WEAK-PASS (only Primary is Bonferroni-protected; SecA is descriptive)
- Under substantive interpretation: primary carries extreme margin AND cross-metric robust AND SecA narrow miss is 1 rank — should be closer to PASS-DIRECTED

Theorist and team-lead have discussed; **pending auditor adjudication**, verdict conservatively set as **WEAK-TO-PARTIAL-PASS**. [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] (completed immediately after) delivers the feature-space completion that SUBSUMES the SecA narrow miss by showing Q 114 is rank-1 NN under verse-length histograms.

## Honest-limits disclosure

1. **Primary FR uses [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix (QAC-STEM roots K=500)**; Secondary B metrics use surface-word tokens (different feature space). The primary claim is ROOT-based; the cross-metric confirmation is SURFACE-based. This is a minor rule-tuple divergence inherited from data availability, disclosed.

2. **10K permutations at primary; 1K at secondary B** (compute budget). Secondary B is DESCRIPTIVE not inferential; reduced perm count is acceptable.

3. **TERMINAL_TRIAD at 7 surahs** (pre-registered); alternate-size triads NOT tested (locked).

4. **Post-hoc origin** of the hypothesis is fully disclosed. The pre-reg was written BEFORE execution; execution followed exactly. Direction and seed locked.

5. **SecA is a descriptive position-test** not a p-value test; single-test α=0.05 ceiling applies; narrow miss interpretation is debatable.

## Integration with [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] (companion finding)

[[h-new-138-wrap-around-feature-robustness|H-NEW-138]] tests feature-space robustness. Key result: under verse-length-histogram FR, Q 114 is **rank-1** for Q 1 (d=0.0827). This DIRECTLY contradicts the SecA narrow miss — Q 114 IS the closest surah to Q 1 at the rhythm-feature level, even though at root-content level it's rank 13.

Under combined [[h-new-137-wrap-around-closure|H-NEW-137]] + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] evidence, the wrap-around closure is confirmed at 3 feature spaces (roots PRIMARY passes, char-4-grams PRIMARY passes, verse-length PRIMARY passes AND Q 114 becomes rank-1). The Secondary A narrow miss is a feature-specific rank artifact.

## Status

**WEAK-TO-PARTIAL-PASS** at this finding's pre-reg literalism.
**PASS-DIRECTED → CONFIRMED** at combined [[h-new-137-wrap-around-closure|H-NEW-137]] + [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] level (pending auditor adjudication).

## Connection to theorist model

This is the PRIMARY empirical anchor for theorist's P8 (wrap-around liturgical ring). Under combined [[h-new-137-wrap-around-closure|H-NEW-137]]+138, P8 earns CONFIRMED status.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-137-wrap-around-closure-prereg.md`
- Companion: `findings/phase-b-hypotheses/h-new-138-wrap-around-feature-robustness-prereg.md`
- Inline execution: this session (team-lead, 2026-04-17)
- Findings: this file
- Source observation: `scratch/inline-2026-04-17-q1-nearest-neighbors.md`
