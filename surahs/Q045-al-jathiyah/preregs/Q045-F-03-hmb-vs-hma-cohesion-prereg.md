---
prereg_id: Q045-F-03
title: HM-B sub-block FR-roots cohesion vs HM-A — Q 45's content-cohesion role
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:10:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-03 — HM-B vs HM-A FR-roots cohesion + Q 45 leave-one-out role

## 1. Hypothesis (direction-locked)

**H1 (cohesion ordering)**: Within the ḥawāmīm-7 cluster, HM-B (Q 43, 44, 45, 46) and HM-A (Q 40, 41, 42) have distinguishable mean pairwise FR-roots distances. Pre-committed direction: **HM-A is *tighter* than HM-B** (i.e., d̄_FR(HM-A) < d̄_FR(HM-B)), because HM-A's three surahs are revelation-cluster-consecutive (al-Suyūṭī chronology #60, #61, #62) while HM-B's four surahs span more chronological territory.

**H1b (Q 45's leave-one-out cohesion role)**: When Q 45 is removed from HM-B, the remaining {Q 43, Q 44, Q 46} mean d̄_FR is *higher* than HM-B-with-Q45. I.e., Q 45 is a **cohesion-tightener** within HM-B (its presence pulls the mean DOWN).

## 2. Null

**H0a**: d̄_FR(HM-A) ≥ d̄_FR(HM-B), i.e., HM-A is not tighter.
**H0b**: Q 45 leave-one-out has no effect or pushes d̄ UP-by-removal (i.e., Q 45's presence loosens the cluster).

## 3. Operationalization

- FR-roots distance source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular` field).
- Mean pairwise distance: arithmetic mean of all C(k,2) within-cluster pairs.
- HM-A cluster: {40, 41, 42}; 3 pairs.
- HM-B cluster: {43, 44, 45, 46}; 6 pairs.
- HM-B-minus-Q45: {43, 44, 46}; 3 pairs.
- Permutation null: 10,000 random size-3 (and size-4) subsets drawn from the 114-surah index space; report percentile of observed d̄ in null distribution.
- Seed: 20260428.

## 4. Direction lock

Pre-committed direction:
- **H1**: d̄(HM-A) < d̄(HM-B). Reversal = **PRECOMMIT_VIOLATION**.
- **H1b**: d̄(HM-B-minus-Q45) > d̄(HM-B). Reversal = **PRECOMMIT_VIOLATION**.

## 5. Bonferroni

k = 2 (H1 + H1b); α_corrected = 0.05/2 = 0.025.

## 6. Success / failure criteria

- **VINDICATED**: H1 direction matches AND p_perm(H1) < 0.025; H1b direction matches.
- **DIRECTIONAL**: H1 direction matches but p_perm(H1) > 0.025.
- **NULL**: H1 direction matches with no significance; H1b also null/inconclusive.
- **Precommit violation**: H1 direction reversed (HM-A *looser* than HM-B).

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q045-F-03.json` with: d̄(HM-A), d̄(HM-B), d̄(HM-B-minus-Q45), null mean, percentile, p_perm, verdict, plus the 6 individual HM-B pairwise distances and 3 HM-A pairwise distances.

## 9. Motivation

The HM-7 cluster is the only consecutive 7-surah block sharing a muqaṭṭaʿāt opening. Earlier work in the project ([[hawamim-7-cluster-bifurcation]]) established that HM-A is high-rhyme-entropy multi-rāwī and HM-B is near-monorhyme. The bifurcation was at the *prosodic* axis. The present test asks whether the bifurcation also exists at the **FR-roots content axis** — and what Q 45's specific role is. Pre-committed prediction: HM-A's tighter chronological clustering predicts tighter content cohesion. The Q 45 leave-one-out is motivated by the empirical observation in `h-new-590` Q 45's classification as `COHESION_ANCHOR` (Δ%ile = -10.68 — Q 45 *anchors* its 7-window neighborhood); the test asks whether the anchoring extends to the HM-B sub-block specifically.

## 10. Honest pre-commit caveats

- The pre-committed HM-A < HM-B direction could turn out reversed; the test is not a layup. Q 45's COHESION_ANCHOR signal in h-new-590 is at the 7-window level, NOT the 4-surah HM-B level — extending it to HM-B is a real prediction.
- Pre-Islamic-poetry control / whole-Meccan-baseline control NOT pre-registered here; deferred to follow-up if the primary test passes.
