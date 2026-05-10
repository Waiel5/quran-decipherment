---
prereg_id: Q043-F-07
title: HM 7-cluster within-pair FR-distance ranking of Q 43
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-07 — HM ↔ Q 43 within-cluster pair-distance ranking

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Within the ḥawāmīm 7-cluster {Q 40, Q 41, Q 42, Q 43, Q 44, Q 45, Q 46}, Q 43's *median* Fisher-Rao distance to other HM members is **strictly less than** the median FR-distance of Q 43 to a random size-6 sample of non-HM surahs (10000-permutation null).

This is the within-cluster-cohesion test for Q 43 specifically, replicating the Q041-F-03 design that found Q 41/Q 42 the tightest HM pair.

## 2. Null / negation

**H0**: Q 43's median within-HM FR-distance is greater than or equal to the median FR-distance to random size-6 non-HM samples (no cluster effect).

## 3. Operationalization

- Source: `findings/phase-b-hypotheses/csv/h-new-111.json` (114×114 FR distance matrix on QAC stem-roots).
- HM cluster = {40, 41, 42, 43, 44, 45, 46}; HM_others (for Q 43) = {40, 41, 42, 44, 45, 46} (6 members).
- Observed metric: median over `D[Q43, hm]` for hm in HM_others.
- Null: 10000 permutations of size-6 sampled from non-HM-non-Q43 surahs; compute median.
- One-sided lower-tail p = (# null medians ≤ observed) / 10000.

## 4. Direction lock

Pre-committed direction: **observed < null median** (Q 43 is tighter to HM than to random).

## 5. Bonferroni

Member of Q 43 novel-findings family (k=3 in this batch). α_corrected = 0.0167.

## 6. Success / failure criteria

- **PASS-DIRECTED**: p < 0.0167 AND observed < null median.
- **DIRECTIONAL**: observed < null median but p ≥ 0.0167.
- **NULL**: observed ≥ null median.
- **PRE-COMMIT-VIOLATION**: any reverse-direction result published with full prominence.

## 7. Seed

`20260509`. `n_perm = 10000`.

## 8. Output

JSON to `csv/Q043-F-07.json`: observed_median, null_distribution stats, p_one_sided, verdict, per-pair distances Q43↔HM_others.

## 9. Rationale

The ḥawāmīm 7-cluster shares the muqaṭṭaʿāt opener حم. Prior work (H-NEW-1190, Q041-F-03) found the cluster is NOT root-FR-cohesive as a whole, but specific pairs (Q 41/Q 42) are tight. This test extracts Q 43's pairwise profile within the cluster — does it tilt toward HM or toward the corpus?

## 10. Honest limits

- Cross-finding-025 marker-thickness rule warns that thin shared markers (muqaṭṭaʿāt = 1 verse out of 89) may not drive FR-cohesion. This test is therefore designed to NULL under that rule; the directional pre-commit is the more interesting (cluster-cohesion) direction.
- The QAC root-attestation is the source-of-truth; alternative root-segmentations not tested.
- The non-HM-non-Q43 sampling pool is 107 surahs; size-6 draws are dense enough for stable null.
