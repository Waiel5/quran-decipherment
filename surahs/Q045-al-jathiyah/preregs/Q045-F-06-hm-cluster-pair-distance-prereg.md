---
prereg_id: Q045-F-06
title: HM 7-cluster within-pair FR-distance ranking of Q 45
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-06 — HM ↔ Q 45 within-cluster pair-distance ranking

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Within the ḥawāmīm 7-cluster {Q 40, Q 41, Q 42, Q 43, Q 44, Q 45, Q 46}, Q 45's *median* Fisher-Rao distance to other HM members is **strictly less than** the median FR-distance of Q 45 to a random size-6 sample of non-HM surahs (10000-permutation null).

This is the within-cluster-cohesion test for Q 45, parallel to Q043-F-07.

## 2. Null / negation

**H0**: Q 45's median within-HM FR-distance is greater than or equal to the median FR-distance to random size-6 non-HM samples.

## 3. Operationalization

- Source: `findings/phase-b-hypotheses/csv/h-new-111.json`.
- HM cluster = {40, 41, 42, 43, 44, 45, 46}; HM_others (for Q 45) = {40, 41, 42, 43, 44, 46}.
- Observed metric: median `D[Q45, hm]` for hm in HM_others.
- Null: 10000 perms; size-6 sampled from non-HM-non-Q45 surahs.
- One-sided lower-tail p.

## 4. Direction lock

Pre-committed: **observed < null median**.

## 5. Bonferroni

k=3. α_corrected = 0.0167.

## 6. Success / failure criteria

- **PASS-DIRECTED**: p < 0.0167 AND observed < null median.
- **DIRECTIONAL**: observed < null median, p ≥ 0.0167.
- **NULL**: observed ≥ null median.
- **PRE-COMMIT-VIOLATION**: reverse-direction → published as NULL with full prominence.

## 7. Seed

`20260509`. `n_perm = 10000`.

## 8. Output

JSON to `csv/Q045-F-06.json`: observed_median, null_distribution stats, p_one_sided, per-pair distances, verdict.

## 9. Rationale

Q 45 is the smallest HM surah by verse-count (37 verses) and shares the *tanzīl al-kitāb* opener-formula (Q 39:1, 40:1, 41:1, 45:1, 46:1 per Q 39's H-NEW-1270 cluster). The hypothesis is that Q 45 should tilt toward HM tightly given the shared formula. Counter-prediction from cross-finding-025: thin markers may NULL on FR. The pre-reg locks the test honestly either way.

## 10. Honest limits

- The non-HM-non-Q45 sampling pool is 107 surahs; null is well-resolved.
- The QAC root-attestation is source-of-truth.
- The *tanzīl al-kitāb* shared formula is a marker but spans both HM and non-HM (Q 39 is not HM); this test isolates the HM-axis specifically.
