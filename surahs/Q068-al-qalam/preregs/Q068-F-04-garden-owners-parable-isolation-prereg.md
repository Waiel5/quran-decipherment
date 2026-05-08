---
finding_id: Q068-F-04
title: "Q 68:17-33 garden-owners parable — lexical isolation (Jaccard) and within-surah distinctness"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 2
bonferroni_family: "Q068-F-04 (a) Jaccard-distance to nearest parable + (b) within-surah max-vocabulary-distinctness"
alpha_raw: 0.05
alpha_bon: 0.025
direction: "TWO-SIDED for (a); POSITIVE for (b) — within-surah distinctness expected MAXIMAL at parable region"
---

# Q068-F-04 — STORY-OF-THE-GARDEN-OWNERS

## Hypothesis

Q 68:17-33 contains a unique parable: the *aṣḥāb al-janna* (garden-owners) who plot to harvest before the poor arrive at dawn, are then struck by a calamity at night, and discover their garden destroyed. The parable has **no exact narrative parallel** elsewhere in the Quran. Both classical (al-Ṭabarī, Ibn Kathīr ad loc.) and modern scholars treat it as an isolated unit.

This test operationalizes the parable's empirical "isolation":

- **Sub-test (a) — cross-surah lexical Jaccard distance**: Compute Jaccard distance (root-level, QAC) from the Q 68:17-33 root-set to the root-sets of:
  - **Q 18:32-44** (the Two Garden-Owners parable, the closest narrative cognate)
  - **Q 36:13-32** (the Aṣḥāb al-Qarya parable, the city-three-messengers parable)
  - and to all other 51-verse-or-shorter contiguous parable-candidate windows in the corpus (control distribution)
- **Sub-test (b) — within-surah max-distinctness**: Within Q 68's own 52 verses, identify which K=17-verse contiguous window has MAXIMAL Jaccard distance to its complement-in-surah. Pre-commit prediction: the parable window v.17-33 (or any contiguous 17-verse window overlapping the parable) is the maximum.

## Locked operationalization

### Sub-test (a): cross-surah Jaccard

- Source: QAC root-tokens, no-tashkeel, Hafs-Kufan.
- Q 68:17-33 root-set R_qalam (deduplicated roots).
- Q 18:32-44 root-set R_kahf.
- Q 36:13-32 root-set R_yasin.
- Jaccard distance d(A,B) = 1 - |A∩B|/|A∪B|.
- Compute d(R_qalam, R_kahf), d(R_qalam, R_yasin).
- **Control distribution**: take 10,000 random contiguous K=17-verse windows from anywhere in the corpus (excluding the 3 parables themselves), compute their root-sets and Jaccard distance to R_qalam.
- Empirical p = (# control windows with Jaccard distance ≥ observed) / 10000 — for *both* d(qalam, kahf) and d(qalam, yasin).
- The pre-registered prediction is: d(qalam, kahf) and d(qalam, yasin) are HIGH (i.e., parables are lexically dissimilar) but **not necessarily the corpus-extreme** — because parables share genre vocabulary (planted/garden/dawn/calamity).

### Sub-test (b): within-surah max-distinctness

- Slide K=17-verse contiguous windows across Q 68's 52 verses (i.e., windows starting at v.1, v.2, ..., v.36 → 36 windows).
- For each window W: Jaccard distance from W's root-set to its in-surah complement (Q 68 \ W).
- Pre-commit prediction: the window starting at v.17 (== v.17-33, the parable) has the corpus-MAXIMAL Jaccard distance over all 36 windows.
- Permutation null: shuffle root-tokens within Q 68 (keeping the v.17 window's TOKEN-COUNT fixed, but reassigning roots from Q 68's pool); recompute the position of the maximum window. p = (# perms where v.17 window is the max) / 10000.
- **Direction-locked POSITIVE**: v.17 window IS the maximum (or top-3) at p < 0.025.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan)`

## Direction (LOCKED)

- Sub-test (a): two-sided (parable could be lexically close OR distant from cognate parables; both informative).
- Sub-test (b): POSITIVE (parable expected to be the within-surah max).

## Success / failure criteria

| Verdict | Sub-test (a) | Sub-test (b) |
|:--|:--|:--|
| **VINDICATED** (joint) | p_(a) < 0.025 | AND p_(b) < 0.025 AND v.17 is corpus-max |
| **DIRECTIONAL** | One sub-test passes | |
| **NULL** | Neither passes | |

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_04_garden_owners_parable_isolation.py`.
- JSON: `csv/Q068-F-04.json`.
- Findings: in `06-novel-findings.md`.
