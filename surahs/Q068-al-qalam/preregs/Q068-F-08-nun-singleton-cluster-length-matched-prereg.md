---
finding_id: Q068-F-08
title: "Q 68 al-Qalam — Nūn-letter muqaṭṭaʿ singleton uniqueness + {Q 38, Q 50, Q 68} FR cluster vs length-matched null (MW-5 replication of Q050-F-04 with different null)"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: "Q068-F-08 (a) Nūn-opener uniqueness audit; (b) singleton-triplet FR cluster vs length-matched null"
alpha_raw: 0.05
alpha_bon: 0.025
direction: "Sub-test (a): EXACT enumeration; Sub-test (b): POSITIVE-LOW (triplet expected MORE FR-cohesive than length-matched triplets) — MW-5 replication of Q050-F-04 (which used random-3-surah null)"
---

# Q068-F-08 — NŪN-OPENER UNIQUENESS + LENGTH-MATCHED SINGLETON CLUSTER (MW-5 REPLICATION)

## Hypothesis

Two sub-tests, axis-disjoint from Q050-F-04 (which used a random-3-surah null on the same triplet):

### Sub-test (a) — Nūn-letter muqaṭṭaʿ uniqueness

Among the 29 muqaṭṭaʿāt-opener surahs (per al-Suyūṭī, *al-Itqān*, nawʿ on muqaṭṭaʿāt-opening), Q 68 is hypothesized to be the **ONLY** surah opening with the single letter Nūn. This is the corpus-EXACT verification step.

### Sub-test (b) — Singleton-triplet FR cluster vs length-matched null (MW-5 replication)

The triplet (Q 38 Ṣād, Q 50 Qāf, Q 68 Nūn) was tested by Q050-F-04 for FR-cohesion against a random-3-surah null (p=0.267, NULL). This sub-test re-tests under a **length-matched null** — random triplets drawn from surahs whose verse-counts are within ±50% of the targets (45, 52, 88). MW-5 requires replication at multiple K/seeds/sub-samples; this is the **length-matched-null** replication.

## Locked operationalization

### Sub-test (a) — uniqueness audit

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` for each of the 29 muqaṭṭaʿāt-opener surahs (Q 2, 3, 7, 10-15, 19, 20, 26-32, 36, 38, 40-46, 50, 68 — 29 surahs per classical canon).
- Extract the muqaṭṭaʿ-letter token(s) of v.1 (whitespace-tokenized first token).
- Enumerate surahs whose first token is the single Arabic letter ن.

### Sub-test (b) — length-matched FR cluster null

- Triplet: {Q 38, Q 50, Q 68}.
- Verse counts: Q 38=88, Q 50=45, Q 68=52.
- Length-matched pool: all surahs with verse-count in [22.5, 132] (0.5× to 1.5× of {45, 52, 88}'s union range) AND NOT in the triplet.
- For each of 10,000 permutations: sample a random triple from the pool (without replacement), compute its mean pairwise FR-distance from `h-new-111.json`.
- Observed: mean pairwise FR for {Q 38, Q 50, Q 68}.
- Empirical p_low = (# perm triples with mean ≤ observed) / 10000.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi; FR matrix from h-new-111 SHA ea3f0ee41d41...)`

## Null distribution

- Sub-test (a): exact enumeration — no null.
- Sub-test (b): 10,000 length-matched random triples; one-sided low-p test.

## Direction (LOCKED)

- Sub-test (a): expectation = 1 (Q 68 alone).
- Sub-test (b): POSITIVE-LOW (triplet mean < length-matched null mean at p < 0.025 Bonferroni-2).

## Success / failure criteria

| Sub-test | Verdict | Criterion |
|:--|:--|:--|
| (a) | **VINDICATED** | Exactly 1 Nūn-opener = Q 68 |
| (a) | **DIRECTIONAL** | 2 Nūn-openers (no other expected) |
| (a) | **NULL** | 0 or ≥ 3 Nūn-openers |
| (b) | **VINDICATED-LM** | p_low < 0.025 (Bonferroni-2) under length-matched null |
| (b) | **DIRECTIONAL-LM** | 0.025 ≤ p_low < 0.05 |
| (b) | **NULL-LM** | p_low ≥ 0.05 (replicates Q050-F-04 NULL with different null distribution) |
| (b) | **DIRECTION_REVERSED** | Triplet mean > length-matched null mean (pre-commit violation) |

## Coordination with Q050-F-04

Q050-F-04 used a **random-3-surah null** drawn from the full 114-surah space (returning p_low = 0.267, NULL). Q068-F-08 sub-test (b) uses a **length-matched null** (subsetting to verse-count-similar surahs only). The two nulls are AXIS-DISJOINT by methodology (different reference populations); no Bonferroni overlap. If both return NULL, the singleton-cluster FR-cohesion claim is **double-replication NULL** (much stronger evidence against the cluster hypothesis). If sub-test (b) returns PASS while Q050-F-04 returned NULL, the rules-tuple is fragile — length-matching is the critical methodological choice.

## Honest limits

- The triplet is only 3 surahs (Q 38, Q 50, Q 68), so statistical power is intrinsically limited. Both nulls' p-values are sensitive to small-N triplet sampling.
- The length-matched null excludes the corpus extremes (Q 2 al-Baqara at 286 verses; Q 108 al-Kawthar at 3 verses), so the null distribution is tighter than the random-3-surah null. Under tighter null, an observed mean of 0.870 may be MORE significant — or LESS, depending on whether length-matched surahs happen to be FR-clustered themselves.
- Sub-test (a) "Nūn-opener uniqueness" is trivial in the sense that the classical scholarly consensus is unanimous — but it is empirical-corpus-confirmation, not classical-claim derivation.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_08_nun_singleton_cluster_length_matched.py`.
- JSON: `csv/Q068-F-08.json`.
- Findings: in `06-novel-findings.md`.
