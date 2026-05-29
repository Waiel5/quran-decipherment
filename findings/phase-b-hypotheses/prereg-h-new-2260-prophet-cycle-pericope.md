---
finding_id: H-NEW-2260
title: "Prophet-cycle pericope parallelism/cohesion — Nūḥ / Mūsā / Ibrāhīm"
phase: B+
status: PRE-REGISTRATION (locked before computation)
date: 2026-05-29
author: Waiel Al-Shujaa
extends: cross-finding-025-formal (scale-of-aggregation pericope-flip law)
---

# PRE-REGISTRATION — H-NEW-2260 Prophet-cycle pericope parallelism/cohesion

## 0. Motivation and framing

The same prophet-narrative recurs across many surahs of the Quran. Classical
ʿulūm al-Qurʾān treats this as *takrār al-qaṣaṣ* (repetition of narrative);
al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on *takrār al-qiṣaṣ*, and
al-Suyūṭī, *al-Itqān*, nawʿ 63 (*fī qaṣaṣ al-Qurʾān*) both discuss why the
same story is retold with different wording in different sūras. The empirical
question this finding poses is narrow and falsifiable: **do same-prophet
pericopes share root-vocabulary above what equally-sized random pericopes drawn
from the corpus would share?**

This is a pericope-scale test in the sense of
`cross-finding-025-formal` (the scale-of-aggregation pericope-flip law). The
recurring-prophet narrative is a *content marker* that is diffuse at
whole-surah scale (e.g. the Nūḥ story occupies 6 verses of the 206-verse Q 7,
but is the whole of the 28-verse Q 71). At the *pericope scale* — the bounded
verse-block that actually narrates the prophet's story — the marker IS the
content, so cohesion is expected to be detectable above the random-pericope
baseline if the cycles re-use a stable narrative lexicon.

Note (cross-finding-025): the Christ-narrative (H-NEW-1310) was NULL at
whole-surah scale; the pericope-flip pattern is the project's expectation.
But cross-finding-025 §4 also pre-commits us to a sharper outcome: **a
prophet-cycle that does NOT cohere even at pericope scale is itself a
first-class finding about narrative variation** (the Quran retelling the same
story with genuinely disjoint vocabulary). NULL is published with equal
prominence.

## 1. Hypothesis (DIRECTION-LOCKED, before computation)

For each of the three prophet cycles, the mean pairwise root-Jaccard among the
cycle's pericopes is **GREATER** than the mean of a permutation null built from
equally-sized random pericopes drawn from the corpus.

- **Direction lock (all three cycles): TIGHTER — J_mean(cycle) > null_mean, i.e. z > 0.**
- Locked BEFORE any computation. A result with J_mean < null_mean (z < 0) is a
  **pre-commit violation**, published as NULL with full prominence.
- A z > 0 but p ≥ α_corrected is **DIRECTIONAL** (trend, not significant).

## 2. Locked pericope inventory (boundaries verified against `quran-text/quran-no-tashkeel.json` on disk)

All verse ranges below were read directly from the canonical no-tashkeel text
and confirmed to (a) exist and (b) narrate the named prophet. Lengths (L) are
inclusive verse counts.

### 2.1 NŪḤ cycle — 6 pericopes (15 pairs)

| Pericope | Surah | Verses | L | Content |
|:--|:--|:--|:-:|:--|
| Q 7:59-64    | Al-Aʿrāf      | 59-64   | 6  | Nūḥ sent to his people; the ملأ reject; flood-deliverance |
| Q 11:25-49   | Hūd           | 25-49   | 25 | Full Nūḥ pericope: warning, ark, flood, the son, landing |
| Q 23:23-30   | Al-Muʾminūn   | 23-30   | 8  | Nūḥ sent; ملأ reject; ark + deliverance prayer |
| Q 26:105-122 | Al-Shuʿarāʾ   | 105-122 | 18 | qawm Nūḥ deny; messenger-formula; deliverance + drowning |
| Q 54:9-17    | Al-Qamar      | 9-17    | 9  | qawm Nūḥ deny; flood (abwāb al-samāʾ); deliverance |
| Q 71:1-28    | Nūḥ           | 1-28    | 28 | Whole surah: Nūḥ's preaching + duʿāʾ against his people |

### 2.2 MŪSĀ cycle — 4 pericopes (6 pairs)

Bounded burning-bush / Pharaoh-commissioning pericopes (the recurrent
"nār → nidāʾ → ʿaṣā/yad → idhhab ilā firʿawn" episode).

| Pericope | Surah | Verses | L | Content |
|:--|:--|:--|:-:|:--|
| Q 20:9-36  | Ṭāhā      | 9-36  | 28 | Fire; holy valley Ṭuwā; staff + hand; mission to Pharaoh; Hārūn |
| Q 27:7-14  | Al-Naml   | 7-14  | 8  | Fire; "būrika man fī al-nār"; staff + hand; nine signs to Pharaoh |
| Q 28:29-35 | Al-Qaṣaṣ  | 29-35 | 7  | Fire at al-Ṭūr; staff + hand; Hārūn as helper; mission |
| Q 79:15-26 | Al-Nāziʿāt | 15-26 | 12 | Holy valley Ṭuwā; idhhab ilā firʿawn; Pharaoh's denial + punishment |

### 2.3 IBRĀHĪM cycle — 5 pericopes (10 pairs)

| Pericope | Surah | Verses | L | Content |
|:--|:--|:--|:-:|:--|
| Q 6:74-83    | Al-Anʿām    | 74-83   | 10 | Āzar + idols; star/moon/sun argument; ḥanīf monotheism |
| Q 19:41-50   | Maryam      | 41-50   | 10 | Ibrāhīm pleads with his father; departure; gift of Isḥāq/Yaʿqūb |
| Q 21:51-70   | Al-Anbiyāʾ  | 51-70   | 20 | Smashing the idols; "qāla bal faʿalahu kabīruhum"; the fire→cool |
| Q 26:69-104  | Al-Shuʿarāʾ | 69-104  | 36 | Idol-debate; Ibrāhīm's duʿāʾ; Day-of-Judgement extension |
| Q 37:83-113  | Al-Ṣāffāt   | 83-113  | 31 | Idols; the fire; the sacrifice (dhabīḥ) + Isḥāq tidings |

## 3. Instrument (MW-1, locked before run)

- Text: `quran-text/quran-no-tashkeel.json` (verse existence + boundary check).
- Roots: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4). For
  each verse, the set of ROOT-tagged stems (first ROOT feature per segment) —
  **identical extraction to H-NEW-1380 / H-NEW-1500 / H-NEW-1510 / H-NEW-1520 /
  H-NEW-1760** for cross-finding-025 comparability.
- Pericope root-set = union of ROOT sets across the pericope's verses.
- Metric: **mean pairwise root-Jaccard** over all pericope-pairs in the cycle.
  J(A,B) = |A ∩ B| / |A ∪ B|.

## 4. Null distribution (MW-2)

- **Permutation null, seed = 20260509, n_perm = 10000.**
- For each cycle, each permutation draws as many random pericopes as the cycle
  has, each one a **contiguous window of the same verse-length** as the
  corresponding observed pericope, with the window's start drawn uniformly over
  the flat-indexed 6,236-verse corpus. The same per-pericope length-vector is
  preserved (length-matched null), so the null controls for pericope size.
- Statistic recomputed per permutation: mean pairwise root-Jaccard.
- z = (J_obs − null_mean) / null_std. One-tailed p = #(null ≥ obs) / n_perm.

## 5. Multiple comparisons (Bonferroni across 3 cycles)

- Family size k = 3 (Nūḥ, Mūsā, Ibrāhīm).
- **α_corrected = 0.05 / 3 = 0.016667.**
- Report raw permutation p and the Bonferroni-corrected threshold for each.

## 6. Decision rules (per cycle)

| Condition | Verdict |
|:--|:--|
| J_obs < null_mean (z < 0) | **PRE-COMMIT-VIOLATION** (NULL, full prominence) |
| z > 0 and p < 0.016667 (Bonferroni) | **PASS-DIRECTED** |
| z > 0 and 0.016667 ≤ p < 0.05 | **DIRECTIONAL** (sub-Bonferroni) |
| z > 0 and p ≥ 0.05 | **NULL-AT-PERICOPE-SCALE** (cohesion not detected) |

Cross-cycle synthesis verdict:
- **≥ 2 of 3 cycles PASS-DIRECTED** → further cross-finding-025 evidence
  (prophet-cycle pericopes cohere; pericope-scale cohesion generalizes to the
  recurring-narrative marker class).
- **A cycle that NULLs** is published as a substantive finding about that
  prophet-cycle's narrative variation (the Quran retells it with disjoint
  vocabulary), NOT massaged.

## 7. Rules-tuple

`(no-tashkeel, QAC v0.4 ROOT-token, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

Rules-tuple sensitivity note (bidirectional, per project memory): the QAC ROOT
extraction is the load-bearing choice. A complementary lemma-level or
orthographic-token lens could shift a marginal cycle. This pre-reg locks the
ROOT lens (for cross-finding-025 comparability); any post-hoc lens-variant is
flagged MW-7 (single-test α cap) and reported as exploratory.

## 8. MW protections summary

- MW-1 instrument-prior: metric + extraction locked above.
- MW-2 corpus-prior: 10000-perm length-matched null.
- MW-3 alternative-models: length-matched contiguous-window null is the model;
  per-pair Jaccard table reported so the reader can inspect drivers.
- MW-6 instrument-control: the null IS the random-pericope control (equal size).
- MW-7 post-hoc cap: any lens not in §7 is exploratory-only.

## 9. Files

- This pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2260-prophet-cycle-pericope.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2260.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2260.json`
- Finding: `findings/phase-b-hypotheses/h-new-2260-prophet-cycle-pericope.md`

Direction is LOCKED. Equal NULL prominence. SHA-256 of this file is embedded in
the run script and verified at runtime.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
