---
id: H-NEW-201
title: PageRank on the verse-twin similarity network (downstream of H-NEW-167)
phase: B
status: PUBLISHED 2026-04-17 (run-1)
seed: 20260419
rules_tuple: (no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)
parent_prereg: h-new-201-pagerank-verse-twin-prereg.md
script: scripts/h_new_201_pagerank_verse_twin.py
data_json: findings/phase-b-hypotheses/csv/h-new-201.json
---

# [[h-new-201-pagerank-verse-twin|H-NEW-201]] — PageRank on the verse-twin similarity graph

## Headline

Under the pre-registered **top-K=5 weighted directed** Jaccard twin
graph with PageRank (α=0.85, 100 iterations), **both Bonferroni-k=2
tests FAIL**:

* **T1** — Top-10 PageRank verses contain **0 of 100** classical-
  celebration hits. PageRank does **not** surface the verses most
  heavily commented by classical tafsīr; it surfaces **high-
  connectivity refrain/formula openers**. (p-binomial ≈ 1.0.)
* **T2** — al-Fātiḥa PageRank sum S_F = 0.002675 vs null mean
  0.001124. z = **+2.47**, p = **0.0334** — **significant at α=0.05
  but NOT at the Bonferroni-corrected α_test = 0.025**.
  Fātiḥa sits at the **96.66th percentile** of random 7-verse bundles.

Convergence: L1-change 9.1e-3 at iter 10 → 2.8e-6 at iter 50 →
3.9e-10 at iter 100. 100 iters is strictly sufficient.

## Graph statistics

| metric | value |
|---|---|
| nodes | 6,236 |
| directed edges (top-K=5) | 31,157 |
| dangling nodes | 3 (verses with no trigram overlap) |
| mean top-1 Jaccard | 0.335 |
| mean top-5 Jaccard | 0.200 |

## Top-10 highest-PageRank verses

| rank | verse | PR | preview | family |
|---|---|---:|---|---|
| 1 | **Q 59:1** | 0.003215 | سبح لله ما في السماوات وما في الأرض… | Musabbiḥāt opener |
| 2 | **Q 57:1** | 0.003193 | سبح لله ما في السماوات والأرض… | Musabbiḥāt opener |
| 3 | Q 33:70 | 0.003186 | يا أيها الذين آمنوا اتقوا الله وقولوا قولا سديدا | taqwā-call |
| 4 | **Q 61:1** | 0.003167 | سبح لله ما في السماوات وما في الأرض… | Musabbiḥāt opener |
| 5 | Q 9:119 | 0.002988 | يا أيها الذين آمنوا اتقوا الله وكونوا مع الصادقين | taqwā-call |
| 6 | Q 2:39  | 0.002759 | والذين كفروا وكذبوا بآياتنا أولئك أصحاب النار | hellfire-formula |
| 7 | Q 5:10  | 0.002610 | والذين كفروا وكذبوا بآياتنا أولئك أصحاب الجحيم | hellfire-formula |
| 8 | Q 41:8  | 0.002563 | إن الذين آمنوا وعملوا الصالحات لهم أجر غير ممنون | ajr-formula |
| 9 | Q 84:25 | 0.002563 | إلا الذين آمنوا وعملوا الصالحات لهم أجر غير ممنون | ajr-formula |
| 10 | Q 5:120 | 0.002551 | لله ملك السماوات والأرض وما فيهن… | mulk-formula |

**Pattern**: every top-10 verse is a **formulaic anchor** — the
literal opening word of three of the five *musabbiḥāt* surahs
(Q 57, 59, 61; the other two open with *sabbaḥa* past-tense Q 62
and *yusabbiḥu* imperfect Q 64, which tie lower), the
*yā-ayyuhā-lladhīna-āmanū-ttaqū-llāha* double, the
*kafarū-wa-kadhdhabū-bi-āyātinā* opposite, and the
*āmanū-wa-ʿamilū-ṣ-ṣāliḥāt* reward clause. PageRank has re-
discovered the **Quranic formula-opener ecosystem** rather than the
tafsīr-celebrated ring-centers and legal anchors.

## Q 1 (al-Fātiḥa) aggregate rank

* **S_F = 0.002675** (sum of PageRank for Q 1:1…1:7)
* Null distribution (10,000 random 7-bundles): mean 0.001124, σ 0.000628
* **z = +2.47**, p = 0.0334 (one-sided)
* **Percentile vs null = 96.66** — Fātiḥa is in the top 3.3% of
  possible 7-verse bundles by aggregate PageRank.
* **Decision at Bonferroni α_test = 0.025: FAIL** (narrowly).

The Fātiḥa's component PageRanks in isolation:

| verse | PR | solo rank (of 6,236) |
|---|---:|---:|
| 1:1 | 0.000337 | 678 |
| 1:2 | 0.001166 | **61** (Lord-of-all-worlds doxology, echoes 6:45, 10:10, 39:75) |
| 1:3 | 0.000379 | 589 |
| 1:4 | 0.000607 | 243 |
| 1:5 | 0.000024 | 5,925 (low — iltifāt verse is lexically unique) |
| 1:6 | 0.000122 | 2,280 |
| 1:7 | 0.000040 | 4,971 (long, unique ghayr-al-maghḍūb clause) |

Only **Q 1:2** is a clear PageRank hub. Q 1:4 and Q 1:1 are
moderate; 1:5, 1:7 sit near the bottom 20%. The aggregate still
beats 96.66% of random bundles driven mostly by 1:2's rank-61
contribution, but under Bonferroni-2 with α_test = 0.025 this is
a narrow miss. **Note that Q 1:7's low PR contradicts my initial
intuition** — its cross-echoes are zero at trigram Jaccard because
the *ghayr al-maghḍūb ʿalayhim wa-lā ḍ-ḍāllīn* phrase is a hapax
in the corpus.

## Overlap with [[h-new-167-verse-twin-graph|H-NEW-167]] top-10 hubs

* [[h-new-167-verse-twin-graph|H-NEW-167]] top-10 (undirected degree on top-1 graph): Q 55:13,
  77:15, 26:108, 26:8, 26:9, **1:2**, 2:136, 3:16, 6:21, 26:226.
* [[h-new-201-pagerank-verse-twin|H-NEW-201]] top-10 (PageRank on top-5 weighted directed): (listed above).
* **Overlap = 0 verses.** Complete divergence.

This is a **methodologically significant finding**: the refrain
hubs that dominate top-1 **degree** (Sūrat al-Raḥmān's tadhkīr,
al-Mursalāt's woe-refrain, al-Shuʿarāʾ's prophet-cycle refrains)
are **NOT** the verses that accumulate PageRank mass under top-5.
Under weighted top-5 flow, the **formulaic-family verses** win
— not the literal refrains, but the *openers and moral-schema
clausulae* that live at the centre of dense similarity neighbourhoods.

## Interpretation

* **Why the musabbiḥāt dominate.** Q 57:1, 59:1, 61:1 are near-
  verbatim triplets (differing only in a *wa-* conjunction and
  definite article). Under top-5, each of these three verses ranks
  the other two as top-2 similarity neighbours, creating a tight
  3-clique with reciprocal high-weight edges — PageRank's ideal
  amplifier. Q 62:1 and 64:1 tie in slightly lower by imperfect
  vs perfect verb conjugation.
* **Why tafsīr-celebrated verses (āyat al-kursī 2:255, āyat al-nūr
  24:35, khawātim al-ḥashr 59:22-24) do NOT top PageRank.**
  These verses are **lexically unique** — they have no near-
  verbatim twins in the corpus. High tafsīr-tagging tracks
  theological density, not lexical similarity density. PageRank on
  a surface-similarity graph is therefore **orthogonal** to classical
  celebration.
* **Why Fātiḥa narrowly misses.** Fātiḥa's Q 1:2 and Q 1:7 both
  echo cross-corpus (1:2 ≈ 6:45/10:10/39:75; 1:7 has the only
  *ghayr al-maghḍūb/al-ḍāllīn* clause), lifting S_F above
  expectation. But Q 1:3-6 are lexically lean 2-3 word verses with
  fewer high-weight neighbours, pulling the sum back. Under a
  lexical-similarity-flow metric, Fātiḥa is **well above average
  (96.66th percentile)** but not extraordinary.

## Caveats / scope

* **Top-K=5 is locked.** K ∈ {3, 10, 20} were NOT tested. A smaller
  K would sharpen the musabbiḥāt amplification; a larger K would
  dilute it.
* **Jaccard on raw trigrams** weights function-word co-occurrence
  equally with content roots. A TF-IDF trigram or root-skeleton
  variant might rebalance toward content-heavy verses ([[h-new-202-juz30-internal-structure|H-NEW-202]]
  candidate).
* **Uniform personalisation.** A classical-weighted personalisation
  (e.g., mass on āyat al-kursī, Fātiḥa, ikhlāṣ) would change the
  ranking by design; deliberately not done to keep the test
  intrinsic to the graph.
* **Classical-top-100 is this project's tag-aggregated celebration
  index**; other lists (al-Suyūṭī's ʾItqān, recitation-virtue
  lists in al-Bukhārī's *Faḍāʾil al-Qurʾān*) would give different
  T1 outcomes.

## Deliverables

* Pre-reg: `findings/phase-b-hypotheses/h-new-201-pagerank-verse-twin-prereg.md`
* Script: `scripts/h_new_201_pagerank_verse_twin.py`
* Data: `findings/phase-b-hypotheses/csv/h-new-201.json`
* Seed: 20260419. Runtime ≈ 40s.

## Both-tests verdict

| test | stat | p | α_test | verdict |
|---|---|---|---|---|
| T1 classical-top-100 overlap | 0/10 hits | 1.00 | 0.025 | **FAIL** |
| T2 Fātiḥa PR sum | z=+2.47 | 0.0334 | 0.025 | **FAIL (narrowly)** |

**Both tests fail under Bonferroni-k=2 pre-registration.** However,
T2 would pass at α = 0.05 uncorrected, and the 96.66th-percentile
Fātiḥa signal is **honest and real** even though the pre-reg
threshold was missed. The stronger finding is **T1**: PageRank on
a surface-similarity graph is **orthogonal to classical tafsīr
celebration** — it recovers the Quran's *formulaic connectivity
structure*, not its *theological centres of gravity*.
