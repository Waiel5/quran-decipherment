---
finding_id: H-NEW-2430
title: "Eponymous-surah cycle-centrality law — is a dedicated prophet-surah the lexical centroid of its narrative cycle?"
phase: B+
status: PRE-REGISTRATION (locked before computation)
date: 2026-05-30
author: Waiel Al-Shujaa
extends: "H-NEW-1820 (title-density-independence) + H-NEW-2260 (prophet-cycle pericope cohesion) + Q071-F-01 (Nūḥ peripheral) + Q020-F-06 (Ṭā-Hā = Mūsā hub)"
seed: 20260509
n_perm: 10000
---

# PRE-REGISTRATION — H-NEW-2430 Eponymous-surah cycle-centrality law

## 0. Motivation and framing

Two project findings define a candidate cross-finding principle:

- **§10.119 Q071-F-01** — the surah named *Nūḥ* (Q 71) is **PERIPHERAL** to its
  own Nūḥ-narrative cycle: it ranks **5 of 6** in mean-pairwise root-Jaccard
  centrality (the centroid is the briefer Q 7:59-64), and its anchor-swap null
  was NULL (z=+0.424, p=0.278). Q 71 develops distinct daʿwa/idol material
  rather than recapitulating the shared ark/flood core.
- **§10.120 Q020-F-06** — the surah *Ṭā-Hā* (Q 20) **IS** the lexical HUB of the
  Mūsā burning-bush cycle (signature 5/6; hub-strength z=+5.807, p=0.0001) —
  because it carries the cycle's **core full episode**. (Note: Q 20 is NOT an
  eponymous prophet-surah; "Ṭā-Hā" is a muqaṭṭaʿāt title, not the name "Mūsā".)

Together they suggest a discriminating principle: **a dedicated/eponymous
surah is its narrative-cycle's lexical HUB iff it carries the cycle's CORE
episode, not a thematic variant.** This pre-registration tests whether that
principle generalizes to a **corpus-wide law** across every figure that has
BOTH a dedicated eponymous surah AND a recurring multi-surah narrative cycle.

It is the direct cross-cycle generalization of **H-NEW-1820** (title-density
independence: 47/89 = 52.8% of eponymous surahs are NOT rank-1 in their own
title-root). H-NEW-1820 is about a surah's *title-root density* within the
whole corpus; H-NEW-2430 lifts the same independence claim to a surah's
*narrative-lexical centrality* within its own retelling-cycle.

## 1. Candidate inventory — who has BOTH an eponymous surah AND a recurring cycle?

Task candidates assessed against the two membership conditions (verified on disk
in `quran-text/quran-no-tashkeel.json`):

| Figure | Eponymous surah | Recurring multi-surah cycle? | Eponymous-surah narrative pericope | Testable? |
|:--|:--|:--|:--|:--|
| **Nūḥ** | Q 71 (نوح) | YES (H-NEW-2260, 6 pericopes) | Q 71:1-28 (whole surah, a member) | **YES** |
| **Ibrāhīm** | Q 14 (ابراهيم) | YES (H-NEW-2260, 5 pericopes) | Q 14:35-41 (his Mecca-duʿāʾ — a *distinct* episode NOT in the H-NEW-2260 set) | **YES** (add eponymous member) |
| **Hūd** | Q 11 (هود) | YES (Hūd→ʿĀd, ≥5 retellings) | Q 11:50-60 (a member) | **YES** |
| **Maryam** | Q 19 (مريم) | YES (nativity/ʿĪsā, ≥5 loci) | Q 19:16-34 (a member) | **YES** |
| **Yūnus** | Q 10 (يونس) | YES (fish/dhū-l-nūn, ≥4 loci) | Q 10:98 (the eponym is a 1-verse *allusion*, not the episode) | **YES** (thin eponymous member by design) |
| Yūsuf | Q 12 (يوسف) | **NO** — the Yūsuf story is confined to Q 12 (only naming-mentions at Q 6:84, Q 40:34); no recurring narrative cycle exists | n/a | **NO — degenerate** |
| Muḥammad | Q 47 (محمد) | **NO** — Muḥammad is not a narrated multi-surah prophet-*story* figure | n/a | **NO — degenerate** |

**Five testable eponymous cycles: Nūḥ, Ibrāhīm, Hūd, Maryam, Yūnus.**

The **Mūsā** cycle (H-NEW-2260 / Q020-F-06) is included as a **documented
control / counter-case only**: there is NO "Sūrat Mūsā", so Mūsā contributes
**no eponymous data point**. It is the reference showing the hub can be a
non-eponymous core-episode carrier (Q 20). Yūsuf and Muḥammad are documented as
degenerate exclusions (no cycle), NOT silently dropped.

## 2. Locked pericope inventories (boundaries verified on disk)

All verse ranges read directly from `quran-text/quran-no-tashkeel.json`,
confirmed to exist and to narrate the named figure. The **eponymous-surah
pericope is marked ◆** in each cycle. Lengths (L) are inclusive verse counts.

### 2.1 NŪḤ cycle — 6 pericopes (reused verbatim from H-NEW-2260)
| Pericope | Surah | Verses | L |
|:--|:--|:--|:-:|
| Q 7:59-64    | al-Aʿrāf    | 59-64   | 6 |
| Q 11:25-49   | Hūd         | 25-49   | 25 |
| Q 23:23-30   | al-Muʾminūn | 23-30   | 8 |
| Q 26:105-122 | al-Shuʿarāʾ  | 105-122 | 18 |
| Q 54:9-17    | al-Qamar    | 9-17    | 9 |
| **◆ Q 71:1-28** | **Nūḥ**  | **1-28** | **28** |

### 2.2 IBRĀHĪM cycle — 6 pericopes (H-NEW-2260's 5 + eponymous Q 14)
| Pericope | Surah | Verses | L |
|:--|:--|:--|:-:|
| Q 6:74-83    | al-Anʿām    | 74-83   | 10 |
| **◆ Q 14:35-41** | **Ibrāhīm** | **35-41** | **7** |
| Q 19:41-50   | Maryam      | 41-50   | 10 |
| Q 21:51-70   | al-Anbiyāʾ  | 51-70   | 20 |
| Q 26:69-104  | al-Shuʿarāʾ  | 69-104  | 36 |
| Q 37:83-113  | al-Ṣāffāt   | 83-113  | 31 |

### 2.3 HŪD cycle — 5 pericopes (Hūd sent to ʿĀd)
| Pericope | Surah | Verses | L |
|:--|:--|:--|:-:|
| Q 7:65-72    | al-Aʿrāf    | 65-72   | 8 |
| **◆ Q 11:50-60** | **Hūd** | **50-60** | **11** |
| Q 26:123-140 | al-Shuʿarāʾ  | 123-140 | 18 |
| Q 46:21-26   | al-Aḥqāf    | 21-26   | 6 |
| Q 54:18-21   | al-Qamar    | 18-21   | 4 |

### 2.4 MARYAM cycle — 5 pericopes (nativity / ʿĪsā-sign)
| Pericope | Surah | Verses | L |
|:--|:--|:--|:-:|
| Q 3:35-47    | Āl ʿImrān   | 35-47   | 13 |
| **◆ Q 19:16-34** | **Maryam** | **16-34** | **19** |
| Q 21:91      | al-Anbiyāʾ  | 91      | 1 |
| Q 23:50      | al-Muʾminūn | 50      | 1 |
| Q 66:12      | al-Taḥrīm   | 12      | 1 |

### 2.5 YŪNUS cycle — 4 pericopes (fish / dhū-l-nūn / ṣāḥib al-ḥūt)
| Pericope | Surah | Verses | L |
|:--|:--|:--|:-:|
| **◆ Q 10:98** | **Yūnus** | **98** | **1** |
| Q 21:87-88   | al-Anbiyāʾ  | 87-88   | 2 |
| Q 37:139-148 | al-Ṣāffāt   | 139-148 | 10 |
| Q 68:48-50   | al-Qalam    | 48-50   | 3 |

## 3. Instrument (MW-1, locked before run)

- Roots: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4); for
  each verse the set of first-ROOT-feature-per-segment stems — **identical
  extraction to H-NEW-2260 / Q071-F-01 / H-NEW-1380 / H-NEW-1500**.
- Pericope root-set = union of ROOT-sets across the pericope's verses.
- **Centrality** of pericope p = mean_{q≠p} Jaccard(root(p), root(q)) over the
  cycle (the medoid / graph-centrality sense, locked identically to Q071-F-01).
- **Rank** = position when the cycle's pericopes are sorted by centrality
  descending (1 = most central). Record the eponymous pericope's rank.

## 4. Null distributions (MW-2, seed 20260509, 10000 perms)

Two complementary nulls, both length-matched contiguous-window draws over the
flat-indexed 6,236-verse corpus (matching the H-NEW-2260 / Q071-F-01 null):

- **Per-cycle anchor-swap null (Arm B, one per cycle).** Replace the eponymous
  pericope with a random contiguous window of the SAME verse-length; recompute
  its mean Jaccard to the cycle's fixed other members. Statistic = the eponymous
  pericope's observed mean-Jaccard-to-others (its Arm-A centrality value).
  z = (obs − null_mean)/null_std; one-sided p = #(null ≥ obs)/10000.
- **Cross-cycle rank null (Arm C, the corpus-wide law cell).** Under the null
  that eponymy is unrelated to centrality, the eponymous pericope's rank within
  a cycle of size n is uniform on {1..n}. For each cycle draw a uniform rank;
  the cross-cycle statistic is the **median eponymous rank** (and, secondarily,
  the count of cycles with rank==1). 10000 simulated rank-vectors give the null
  distribution of the median. We report where the observed median sits.

## 5. Hypothesis (DIRECTION-LOCKED, before computation)

**H1 (LOCKED, the project-generalizing prediction):** eponymous surahs are
**NOT systematically the cycle centroid** — the **median eponymous
centrality-rank across the five cycles is WORSE than rank-1** (median > 1),
generalizing H-NEW-1820. Equivalently, **fewer than half (< 2.5, i.e. ≤ 2 of
5) of the eponymous surahs are rank-1.**

- Direction LOCKED toward eponymy ≠ centrality (median rank > 1).
- **Per-cycle refinement (pre-committed, descriptive, MW-7-capped):** where the
  eponymous surah carries the cycle's CORE full episode it should rank high
  (toward 1); where it develops variant/allusive material it should rank low.
  This is the discriminating mechanism, reported per cycle but NOT a separate
  confirmatory cell.
- **REVERSAL CONDITION (pre-commit violation, FULL PROMINENCE):** if eponymous
  surahs ARE systematically rank-1 (median == 1, i.e. ≥ 3 of 5 are rank-1, AND
  the cross-cycle rank-null one-sided p < 0.05 in the rank-1-favoring
  direction) → the locked direction is REVERSED; published prominently as the
  surprising positive law "eponymy ⇒ centrality".

## 6. Decision rules

### Arm A (per cycle, descriptive rank)
| eponymous rank | label |
|:--|:--|
| 1 of n | CENTROID |
| 2 | NEAR-CENTROID |
| ≥ 3 | PERIPHERAL |

### Arm B (per cycle, anchor-swap null; Bonferroni across k=5 cycles, α = 0.05/5 = 0.01)
| condition | verdict |
|:--|:--|
| z ≤ 0 | NULL (eponymous below random-anchor centrality) |
| z > 0 and p ≤ 0.01 | PASS (eponymous lexically cohesive above random anchor) |
| z > 0 and 0.01 < p ≤ 0.05 | DIRECTIONAL |
| z > 0 and p > 0.05 | NULL |

(Arm B PASS means only that the eponymous pericope shares more than a random
window — it does NOT mean centroid. A surah can be cohesive yet non-central.)

### Arm C (cross-cycle law — the confirmatory cell)
| condition | verdict |
|:--|:--|
| median eponymous rank > 1 (≤ 2 of 5 rank-1) | **H1 CONFIRMED: eponymy ≠ centrality** |
| median == 1 AND rank-null one-sided p < 0.05 | **REVERSAL — eponymy ⇒ centrality (pre-commit violation, full prominence)** |
| median == 1 but rank-null p ≥ 0.05 | inconclusive-at-N (report as DIRECTIONAL-reversal, MW-7 cap) |

## 7. Rules-tuple

`(no-tashkeel, QAC v0.4 ROOT-token, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

Bidirectional rules-tuple note (project memory): the QAC ROOT lens is the
load-bearing choice, locked for comparability with H-NEW-2260 / Q071-F-01 /
Q020-F-06. A lemma-level or orthographic-token lens could rehabilitate or demote
a marginal cycle; any such variant is MW-7-capped exploratory, not run here.

## 8. MW protections

- MW-1 instrument-prior: metric + extraction + centrality definition locked above.
- MW-2 corpus-prior: 10000-perm length-matched nulls (Arms B and C).
- MW-3 alternative-models: two nulls (anchor-swap window + uniform-rank); per-pair
  Jaccard tables emitted for inspection.
- MW-4 over-fitting: no fitted parameters; ranks are non-parametric.
- MW-5 replication: Nūḥ rank reproduces Q071-F-01 (rank 5/6) exactly; the Mūsā
  control reproduces Q020-F-06's hub-strengths — both runtime assertions.
- MW-6 instrument-control: the random-window null IS the size-matched control;
  Mūsā (no eponym) is the cross-cycle counter-case.
- MW-7 post-hoc cap: the per-cycle core-vs-variant refinement and any lens not in
  §7 are exploratory-only.

## 9. Files

- This pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2430-eponymous-cycle-centrality.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2430.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2430.json`
- Finding: `findings/phase-b-hypotheses/h-new-2430-eponymous-cycle-centrality.md`

Direction is LOCKED. Equal NULL prominence. SHA-256 of this file is embedded in
the run script and verified at runtime.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
