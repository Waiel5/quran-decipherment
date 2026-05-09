---
test_id: Q072-F-01
title: 5-qul-opener cluster {Q 72, 109, 112, 113, 114} FR-cohesion REPLICATION with H-NEW-1190 sub-sample PC
hypothesis_class: cluster-cohesion
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
rules_tuple: "(no-tashkeel, QAC stem-roots top-K=500 per H-NEW-111, dirichlet-alpha=0.5, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi script, mushaf order)"
bonferroni_k_local: 1
alpha_local: 0.05
---

# Q072-F-01 — 5-qul opener cluster FR-cohesion (REPLICATION of H-NEW-74 / §10.18)

## Hypothesis

The 5 surahs whose entire first verse (v.1, w.1) is the imperative `qul` — {Q 72 al-Jinn, Q 109 al-Kāfirūn, Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās} — form a Fisher-Rao content-cohesive sub-cluster of the corpus relative to a random-5-subset-of-114 null.

This test REPLICATES the prior inline finding (MASTER-LEDGER §10.18, dated 2026-05-08) which reported within-cluster mean FR = 0.4983 vs null mean 0.9237, z = −4.206, p = 0.00233 over 100,000 permutations. Today's test re-runs the computation under different random seed (`20260509`) and re-uses the project-default 10,000 permutations to confirm reproducibility on the same H-NEW-111 instrument and to add an MW-5 positive-control with the H-NEW-1190 sub-sample.

## Prior

The 4-qul classical sub-cluster {Q 109, 112, 113, 114} = al-muʿawwidhāt-extended is a well-established short-Meccan creedal-protective grouping; its tight content-cohesion is unsurprising. The empirical question is whether **Q 72 al-Jinn (a 28-verse middle-Meccan narrative-and-creedal surah)** participates in this cluster at the FR-content axis beyond the trivial shared opener.

## Pre-committed prediction

**Direction: PASS** — within-cluster mean FR < random-5-subset null mean at p < 0.01 (the prior found p = 0.00233; today's prediction is that the p-value remains < 0.01 under independent seed).

## Null distribution

10,000 random subsets of size 5 drawn uniformly without replacement from {1, ..., 114}; for each, compute the mean pairwise FR distance from the H-NEW-111 matrix; the null distribution is over these means.

## MW-5 positive control

H-NEW-1190 sub-sample {Q 69, Q 97, Q 101} (the *wa-mā adrāka mā* anchor triple — H-NEW-1190 is CONFIRMED FR-cohesive at p = 0.00068). This is the MW-5 control RECOMMENDED by SESSION-HANDOFF-2026-05-09-PM §1.b after H-NEW-1301 demonstrated that the HM-cluster does NOT carry FR root-distribution tightness.

PC PASS criterion: random-3-subset null gives PC observed mean < 5%ile.

## Success criteria

- **PASS (PRIMARY)**: cluster within-mean ≤ 5%ile of 10,000-perm null **AND** MW-5 PC passes at 5%ile. Specifically: replicated p < 0.01.
- **DIRECTIONAL**: within-mean below null mean but p > 0.05.
- **NULL**: within-mean ≥ null mean (direction-reversed; flag as pre-commit violation).

## Failure conditions (NULL with prominence)

- If within-mean ≥ null mean → pre-commit violation flagged.
- If MW-5 PC fails → primary test downgraded to DIRECTIONAL.

## Computation

Input: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (`D_matrix_upper_triangular`).
Output: `surahs/Q072-al-jinn/csv/Q072-F-01.json`.
Script: `scripts/Q072_F_01_five_qul_replication.py`.

## Honest limit

This is a REPLICATION not a discovery; the 5-qul cluster has already been published at MASTER-LEDGER §10.18. Today's test contributes a second independent seed + a different MW-5 PC and so functions as an independent-replication strengthening cross-finding-008 / 028. A NULL result here would be informative (suggesting the prior result was seed-sensitive) but is not the predicted outcome.
