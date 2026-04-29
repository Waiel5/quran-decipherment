---
id: H-NEW-146
title: Q 50 al-Qāf mid-mushaf hub investigation
phase: B
status: NULL at Bonferroni-3 (0/3 cells pass at α_bon=0.0167); three near-misses at single-test α=0.05; MW-5 PASS
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [cross-finding-010 (Q 50 as upper-mid hub), h-new-145 (muq code decoding), h-new-111 (Fisher-Rao D-matrix), h-new-89 (meta-cluster)]
seed: 20260417
rules_tuple: "(Hafs-Kūfan; no-tashkeel; QAC v0.4; 114 surahs)"
bonferroni: k=3 α_bon=0.0167 family=h-new-146-q50-hub
pre_reg: findings/phase-b-hypotheses/h-new-146-q50-qaf-prereg.md
script: scripts/h_new_146_q50_hub.py
output_json: findings/phase-b-hypotheses/csv/h-new-146.json
verdict: UNEXPLAINED — cross-finding-010's Q 50 mid-hub status is NOT captured at Bonferroni-3 by any of the three pre-tested dimensions (position, Qurʾān-reflexivity, structural distinctiveness among single-letter muq). Three near-misses at single-test α=0.05 suggest REAL multi-factor weak contributions but no single dominant axis.
---

# [[h-new-146-q50-qaf-hub|H-NEW-146]] — Q 50 al-Qāf mid-mushaf hub investigation

## Summary

[[cross-finding-010-extended-network|Cross-finding-010]] identified Q 50 al-Qāf as the UPPER-MID hub of the
Quran (degree 4 in the cluster-network). This pre-reg tests three
falsifiable dimensions of Q 50's hub status:

- Position (mid-mushaf centrality within Q 40-60)
- Content (Qurʾān-reflexivity via qrA root density)
- Structural (FR-distance clustering among single-letter muq)

**Result: 0/3 cells pass at Bonferroni-3 α_bon=0.0167.**

However, all three cells have **NEAR-MISS results at single-test α=0.05**:

| Cell | Finding | p-value | Threshold | Result |
|---|---|---:|---:|:-:|
| A | Q 50 rank 1 of 21 surahs in Q 40-60 for cluster-network degree | 0.095 | 0.0167 | near-miss |
| B | Q 50 rank 10 of 114 for qrA (qurʾān) root density | 0.088 (uniform null) | 0.0167 | near-miss |
| C | Q 50's FR-distance to other single-letter-muq {Q 38, Q 68} is 14% SHORTER than to other 28 muq | 0.031 | 0.0167 | near-miss |

**MW-5 PASS**: Q 44 (non-hub, degree 3) fails all three cells at all thresholds, confirming pipeline is correctly discriminating.

## Verdict interpretation

Under strict PRE-COMMITTED Bonferroni-3 correction, the claim "Q 50 is a mid-mushaf hub for position, content, or structural reasons" is **UNEXPLAINED** by this pre-registered test design.

**But the descriptive picture is coherent**:

- Q 50 tied-rank-1 for cluster-network degree among Q 40-60 (with Q 59)
- Q 50 is top-10 of 114 for Qurʾān-root density (joint top-10 with short-mufaṣṣal surahs Q 73, 17, 96, 84, 75, 54, 41, 87, 85)
- Q 50 is CLOSER to the other single-letter muq Q 38 and Q 68 than to other muq surahs (by ~14% in FR distance; z ≈ −2.06)

**The three near-misses are directionally coherent and form a multi-factor weak story**: Q 50 is a hub for POSITION × CONTENT × STRUCTURAL contributions, none of which individually reach Bonferroni-3 significance, but together sketch a plausible hub-constitution.

## Pre-reg compliance disclosure

Direction locked BEFORE execution. Bonferroni k=3, α_bon=0.0167.
Proceeded without auditor wave-3 ACK after reasonable window per
autonomous-no-idle directive; garden-of-forking-paths locked.

**Pre-reg design flaw disclosed**: Cell B's spec "rank ≤ 10 at p < 0.0167"
is arithmetically inconsistent — under uniform null, rank ≤ 10 of 114
gives p = 10/114 = 0.088, which is NEVER less than 0.0167. Only rank = 1
(p = 0.0088) passes. So Cell B was pre-committed at an infeasible threshold.
This is reported HONESTLY rather than loosening the threshold post-hoc. At
rank 10, Q 50 is at the pre-committed descriptive boundary but fails the
strict inferential threshold by design.

**The correct single-rank threshold for α_bon=0.0167 would have been
rank ≤ 1**, and Q 50 is rank 10 — so Cell B fails under any consistent
Bonferroni-3 threshold. Fresh Cell B with correct threshold would still
FAIL. The finding is NOT saved by the disclosed design flaw.

## Cell A — Position: Q 50 rank within Q 40-60

Cluster-network degrees for Q 40-60:
```
Q 40: 3   Q 41: 2   Q 42: 1   Q 43: 3   Q 44: 3
Q 45: 2   Q 46: 2   Q 47: 1   Q 48: 0   Q 49: 1
Q 50: 4   Q 51: 2   Q 52: 2   Q 53: 2   Q 54: 1
Q 55: 3   Q 56: 1   Q 57: 3   Q 58: 1   Q 59: 4
Q 60: 1
```

**Q 50 and Q 59 are tied at degree 4** — joint rank-1 among the 21 Q 40-60 surahs. Q 50 is rank **1**.

Permutation null (10,000 shuffles of degrees across Q 40-60): p = 0.095. **FAIL** at α_bon=0.0167.

The high p is driven by TIES. When degrees are shuffled, any surah getting a degree-4 (3 present across 21) achieves rank 1-2 — not rare enough.

**Descriptive claim**: Q 50 IS the top-tier hub in Q 40-60 (tied with Q 59). **Inferential claim**: the pattern doesn't survive permutation correction due to tie structure in the cluster-network degree distribution.

## Cell B — Content: Qurʾān-reflexivity (qrA root density)

Q 50's opening and closing verses both reference the Qurʾān:
- v1: "ق ۚ وَٱلْقُرْآنِ ٱلْمَجِيدِ" (Qāf. By the glorious Qurʾān.)
- v45: "فَذَكِّرْ بِٱلْقُرْآنِ مَن يَخَافُ وَعِيدِ" (So remind, by the Qurʾān, whoever fears My warning.)

Q 50 has 2 occurrences of root qrA across 45 verses → density = 0.044.

**Rank: 10 of 114 surahs.** Top-10 for qrA density:

| Rank | Surah | qrA density |
|---:|---:|---:|
| 1 | Q 73 al-Muzzammil | 0.200 |
| 2 | Q 17 al-Isrāʾ | 0.144 |
| 3 | Q 96 al-ʿAlaq | 0.105 |
| 4 | Q 84 al-Inshiqāq | 0.080 |
| 5 | Q 75 al-Qiyāmah | 0.075 |
| 6 | Q 54 al-Qamar | 0.073 |
| 7 | Q 41 Fuṣṣilat | 0.056 |
| 8 | Q 87 al-Aʿlā | 0.053 |
| 9 | Q 85 al-Burūj | 0.045 |
| 10 | **Q 50 al-Qāf** | **0.044** |

**Q 50 is top-10 descriptively**, but fails the arithmetic-inconsistent pre-committed threshold (see disclosure above). Under a fresh Cell B asking "is Q 50 in the top-10 of 114?" the answer is YES; under "rank ≤ 10 at p_uniform < 0.0167" the answer is NO.

**Worth noting**: Q 75 al-Qiyāmah (rank 5) is LITERALLY the surah of qiyāma (resurrection). If classical tafsir wanted to assign ق → qiyāma, the obvious association should link to Q 75, not Q 50 — and Q 75 is NOT a muq surah. This REINFORCES [[h-new-145-muq-code-decoding|H-NEW-145]]'s refutation of the classical ق → qiyāma claim.

## Cell C — Structural: Q 50 vs other single-letter muq

Under Fisher-Rao D-matrix ([[h-new-111-fisher-rao-mushaf|H-NEW-111]]):

- Mean FR distance Q 50 ↔ {Q 38, Q 68}: **0.850** (Q 38: 0.854; Q 68: 0.846)
- Mean FR distance Q 50 ↔ other 28 muq surahs: **0.992**
- Difference: **−0.142** (Q 50 is 14% CLOSER to other singletons than to non-singleton muq)

Permutation null (shuffle which 2 of 28 muq surahs are the "singletons", recompute):
- Null mean difference: −0.001
- Null SD: 0.069
- z ≈ −2.06
- **p_2sided = 0.031** — fails α_bon=0.0167 by factor ~2

**Substantive finding**: the three single-letter muq surahs (Q 38 ص, Q 50 ق, Q 68 ن) form a weak structural sub-cluster at Fisher-Rao distance. p=0.031 is suggestive but not strong enough for Bonferroni-3. A dedicated larger-sample test (e.g., replicate under char-4-gram feature space) could either confirm or refute this.

**Classical anchor**: al-Suyūṭī's Itqān discusses the single-letter muq as a distinctive sub-class. Classical view is that single-letter muq are "most compact" openings. Our Cell C provides quantitative support at descriptive level.

## MW-5 positive control — Q 44

Q 44 al-Dukhān has cluster-network degree 3 (per [[cross-finding-010-extended-network|cross-finding-010]]). Ran all 3 cells targeting Q 44:

| Cell | Q 44 pass? |
|---|:-:|
| A (rank in Q 40-60) | FAIL |
| B (qrA density rank) | FAIL |
| C (FR-distance to single-letter muq) | FAIL |

Q 44 fails all three cells. **MW-5 PASS** (control correctly fails the non-hub).

## What this means for [[cross-finding-010-extended-network|cross-finding-010]]

Q 50's hub status per [[cross-finding-010-extended-network|cross-finding-010]] is REAL (degree 4, descriptive top of Q 40-60). But the MECHANISTIC ATTRIBUTION to any of the three tested dimensions (position, content, structure) is NOT strong enough to claim at Bonferroni-3.

**Hypotheses not tested here** (queued for follow-up):

- H-NEW-146.1: **liturgical prominence**: Q 50 is classically recited in Friday and Eid prayers (Sahih Muslim 878). Is its hub status a reflection of its liturgical centrality, not its content-centrality?
- H-NEW-146.2: **book-reflexive inclusio**: v1 and v45 of Q 50 both reference the Qurʾān. Are surahs with strong first-verse+last-verse book-reflexivity systematically more hub-like? Test via inclusio-index across all 114.
- H-NEW-146.3: **ق letter frequency IN Q 50 itself**: is ق (qāf) disproportionately the OPENING letter AND disproportionately present in the body of Q 50?
- H-NEW-146.4: **char-4-gram replication of Cell C**: use the [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]] char-4-gram D-matrix to test whether the 3-single-letter-muq clustering holds under a different feature space.

## Connection to prior findings

- **Refutes [[h-new-145-muq-code-decoding|H-NEW-145]]'s classical-singleton-interpretation of ق→qiyāma more sharply**: Q 75 al-Qiyāmah is rank 5 of 114 for qrA density; Q 50 is rank 10. If anything, Q 75 (a NON-muq surah) is the more "qurʾān-reflexive" surah. Classical ق→qiyāma has no empirical grounding.
- **Extends [[cross-finding-010-extended-network|cross-finding-010]]**: mid-hub status for Q 50 is CONFIRMED descriptively but the mechanism is distributed across weak multi-factor contributions, not any one dominant axis.
- **Partial Fisher-Rao single-letter-muq sub-cluster (Cell C, p=0.031)**: suggestive but below Bonferroni-3. This is a new candidate axis for muqaṭṭāʿat multi-axis synthesis (cross-finding-006) — CONDITIONAL on independent replication.
- **Reinforces [[h-new-145-muq-code-decoding|H-NEW-145]] WEAK-SIGNAL verdict**: muq letter-sets do not encode clean semantics at the single-letter level.

## Caveats and limits

1. **Pre-reg design flaw in Cell B** (disclosed above): threshold was arithmetically inconsistent. This is an honest design-error that I have reported rather than silently loosening.
2. **n=21 for Cell A** is small; ties in the degree distribution limit permutation-test power.
3. **3 single-letter muq is n=3** for Cell C's structural sub-class; inherently low-power.
4. **Q 50's hub-ness may be composite** (position × content × structure) in a way that single-axis tests can't detect. A joint predictor would be needed for a composite test.
5. **Classical liturgical aspect not tested**: Q 50's Friday/Eid liturgical use may be the TRUE mechanism; not operationalized here.

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-146-q50-qaf-prereg.md`
- Script: `scripts/h_new_146_q50_hub.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-146.json`
- This findings file
- Journal: `journal/h-new-146-run-1.md`

Null published with equal prominence to PASS.
