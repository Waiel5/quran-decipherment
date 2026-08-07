---
finding_id: H-NEW-2840
title: The muqaṭṭaʿāt cluster is one cluster, not several — the letter string does not carve it, its distinguishing vocabulary is Meccan register, and the one class that does cohere is a mushaf-adjacency effect a partitioned ḥadīth collection reproduces half the time
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
target_claims: [H-NEW-2820 REVERSES-CLUSTERED, H-NEW-600, H-NEW-610, H-NEW-570 MW-5]
prereg: findings/phase-b-hypotheses/prereg-h-new-2840-muqattaat-structure.md
prereg_sha256: 321f7fe90f9f4f956b4ab91cf0e39179553175b895068ad69ac6d3e9c1e11c2a
run: findings/phase-b-hypotheses/runs/h-new-2840/20260807T101255Z/
run_posthoc: findings/phase-b-hypotheses/runs/h-new-2840-posthoc/20260807T103932Z/
run_posthoc_genre: findings/phase-b-hypotheses/runs/h-new-2840-posthoc-genre/20260807T104225Z/
rule_applied: findings/UNIT-DRIFT-DEFECT.md §3 Screen B (grouping form), §5, §6.1, §7
method_parent: [H-NEW-2820, H-NEW-2830, H-NEW-2760, H-NEW-2720, H-NEW-2680]
seeds: 20260509 primary / 20260519 replication
n_perm: 10000 Qurʾān arms / 2000 per baseline offset / 200 offsets per baseline
tests_in_family: 12
alpha_bonferroni: 0.00416667
verdict_registered: NO-SUB-STRUCTURE-ADJACENCY-EXPLAINED (both seeds; not SEED-FRAGILE)
verdict_independence: PILLAR1-DISTINCT — and explicitly NOT an independent confirmation of Pillar 1
status: >-
  The clustering H-NEW-2820 uncovered is a SINGLE cluster. The 29 are LESS internally
  sub-structured than size-and-period-matched sets (silhouette 0.0829 against a null mean of
  0.1103, 9.31st percentile), and the hierarchical structure that does exist is a size
  gradient that cuts across the letter classes. The opening string predicts content position
  in direction but not at the corrected bar (Δ = −0.0338, p = 0.0325 free / 0.0348
  size-restricted against α_bon = 0.00417), and the whole of that effect is one class:
  dropping the ḥawāmīm lifts p to 0.156. Of the 19 surahs in a multi-member letter class,
  only 4 have their nearest neighbour inside their own class. No root distinguishes the 29
  from the other 85 once size and period are held fixed — 0 survive BH against 19 under the
  size-blind null, and the size-blind list is a Meccan-versus-Medinan register list. The
  ḥawāmīm are corpus-extreme under every within-corpus matched null (0.08th percentile,
  p = 0.0009) and are the ONE arm that clears α_bon — but they are the contiguous mushaf run
  40–46, and taking the same contiguous slots from a matched partition of al-Bukhārī or
  al-Jāḥiẓ reproduces their tightness at the median, with 47.5–52.0 % of arbitrary offsets at
  or below the Qurʾān's own value. The non-contiguous 29-set is NOT reproduced that way
  (6.5–8.0 %). Within one instrument and the same 200 offsets, that difference is contiguity.
verdict: >-
  The set clusters; its internal organisation is not the letters. Three of the four
  multi-member classes do nothing (ALR is 79th-percentile DISPERSED, ṬSM 62nd, ṭawāsīn 36th),
  ALM moves from a published 43.15th percentile to 2.81 without clearing the bar, and the
  ḥawāmīm's strength is at the strength of "six consecutive chunks of one continuous book".
  H-NEW-600's DOUBLE NULL does not survive as stated — ALM's null was size-blind and reverses
  toward cohesion, ALR's is confirmed and hardens in the opposite direction — and its two
  four-month-old queued follow-ups both return NULL under matching.
---

# H-NEW-2840 — What the muqaṭṭaʿāt cluster is

**Pre-reg SHA-256 `321f7fe9…e11c2a`, runtime-verified, committed at `bee950a31` before any
distance among the twenty-nine was measured. Twelve frozen inputs SHA-verified. The
H-NEW-2680 partition code is lifted verbatim, three fragments SHA-checked before `exec`. The
Fisher–Rao matrix path is asserted bit-identical to the published `h-new-570` routine at
startup — `0.938813123152709`, exact equality, not a tolerance. Registered run 1,584 s.
Written under the write-once rule: the run directory is created with `exist_ok=False`, every
file in it is opened with mode `'x'`, `results.json` is written exactly once at completion,
and checkpoints go outside it. No run directory was deleted.**

---

## 0. The opening, and what it turned out to be

H-NEW-2820 established that the muqaṭṭaʿāt sets are strongly clustered in root-content space
under a size-matched null — a result that sat as a published NULL for three and a half months
because `h-new-570`'s null **never once drew a comparison set of the right size in 10,000
draws**. Nobody had looked at the internal structure of that clustering, because until
2026-08-07 the instrument said there was nothing there.

**Twelve inferences were registered with directions locked. Ten of twelve fail their
corrected bar. The two that matter most fail in ways that are informative rather than empty,
and one arm passes and then loses most of its meaning to a control the pre-registration did
not register and this finding ran anyway.** The descriptive map — which was committed to
unconditionally in pre-reg §7 — is below in full, and it is the deliverable.

---

## 1. Reproduction — the instrument, and four published numbers from two other findings

| what | published | recomputed |
|:--|--:|--:|
| `d̄`(muqaṭṭaʿāt-29), frozen matrix | 0.9388131231527093 | **0.938813123152709** |
| `d̄`(ALM-6), H-NEW-600 PRIMARY | 0.9257 | **0.92568** |
| `d̄`(ALR-5), H-NEW-610 PRIMARY | 0.9552 | **0.95518** |
| `d̄`(ḥawāmīm-7), H-NEW-570 MW-5 | 0.8672 | **0.86724** |
| `d̄`(MW-6 non-muq-6), H-NEW-600 | 1.0129 | **1.01291** |
| size-blind percentiles, regenerated | 43.15 / 56.25 / 20.90 / 88.10 | 41.89 / 55.92 / 19.62 / 87.54 |

The percentiles are fresh Monte-Carlo draws and agree to ≈ 1.3 pp. **Nothing in H-NEW-600 or
H-NEW-570 is wrong as arithmetic.** What is challenged is the null.

**The matrix rebuild also settles a small discrepancy in the record.** H-NEW-2830 reports its
QAC rebuild as *"bit-identical to the stored matrix at every one of its 6,441 pairs (max entry
difference exactly 0.0)"*. My unrounded rebuild differs from the stored matrix by up to
**4.999 × 10⁻⁷** and moves `d̄` by **2.2 × 10⁻⁸**. These agree: `h-new-2830-independence.py:141`
returns `np.round(D, 6)`, and its own docstring states the full-precision shift as
`2.2e-8` — exactly the figure measured here. **The stored matrix is published rounded to six
decimals; "bit-identical" is true after rounding and only after rounding.** Every ablation
contrast below is rebuilt-against-rebuilt, never rebuilt-against-frozen.

---

## 2. Q1 — is it one cluster or several? **One. And less sub-structured than matched sets.**

| statistic | observed | null mean | z | **p** | percentile |
|:--|--:|--:|--:|--:|--:|
| **S1** max silhouette, k ∈ {2,3,4,5} — `N_PERIOD` **(primary)** | **0.08286** | 0.11030 | −1.28 | 0.90691 | **9.31** |
| S1 — `N_SIZE5` | 0.08286 | 0.12949 | −0.77 | 0.82202 | 17.80 |
| S1 — `N_SIZE10` | 0.08286 | 0.12716 | −0.76 | 0.83132 | 16.87 |
| S2 = 1 − W₂/W₁ | 0.01294 | 0.01730 | — | 0.6273 | — |

**R1 fails, and it fails in the direction opposite to the locked one.** The 29 are not more
sub-structured than size-and-period-matched sets of 29; they are **less** so, sitting at the
9.31st percentile. Best k = 2, and the k = 2 cut is not a structure — it splits **two
outliers, Q 12 Yūsuf and Q 26 al-Shuʿarāʾ, off from the other 27.**

**Pre-reg §9.3 predicted this arm would be the weakest and registered the expectation rather
than dropping the arm afterwards.** It was right, and the reason is worth stating: *a tight
set need not be a lumpy one*, and a silhouette measures lumpiness.

**The structure that does exist is size, and it cuts across the letters.** At k = 4 the
partition is:

| cluster | n | within `d̄` | median word count | members |
|:--|--:|--:|--:|:--|
| c0 | 15 | 0.8810 | 1159 | 2, 3, 7, 10, 11, 13, 14, 27, 28, 29, 30, 31, **40, 42, 45** |
| c2 | 12 | 0.8897 | 694 | 15, 19, 20, 32, 36, 38, **41, 43, 44, 46**, 50, 68 |
| c1 / c3 | 1 / 1 | — | 1795 / 1320 | 12 · 26 |

**The ḥawāmīm are split across both halves.** So is ALM (2, 3, 29, 30, 31 in c0; 32 in c2) and
so is ALR (10, 11, 13, 14 in c0; 15 in c2). The two large clusters differ by a factor of 1.7
in median word count and by 0.009 in internal cohesion. **The dendrogram is a size gradient
wearing no letters.**

---

## 3. Q2 — does the opening string predict content position? **In direction, yes. At the corrected bar, no. And it is one class.**

`Δ = W̄_within − B̄_between` over the 29. `F1` permutes class labels freely, so muqaṭṭaʿāt
membership and the whole set's size composition are fixed by construction; `F2` permutes them
only within size tertiles of the 29. α_bon = **0.00416667**.

| partition | `W̄` within | `B̄` between | **Δ** | pairs | **p (F1)** | **p (F2)** | replication |
|:--|--:|--:|--:|--:|--:|--:|--:|
| **P1 exact string (primary)** | 0.90845 | 0.94222 | **−0.03378** | 41 / 365 | **0.03250** | **0.03480** | 0.02960 / 0.04120 |
| P2 classical blocks (secondary) | 0.90543 | 0.94339 | **−0.03796** | 49 / 357 | **0.01260** | — | 0.01110 |

**All four registered directions held. None cleared.** R2, R3 and R12 miss α_bon by factors of
3 to 8. Under a single-test reading Δ would be "significant"; under the registered family of
twelve it is not, and the family correction is the honest instrument.

### 3.1 The whole of Δ is the ḥawāmīm (post-hoc, D5)

| dropped class | n remaining | Δ | p (F1) |
|:--|--:|--:|--:|
| — (full P1) | 29 | −0.03378 | 0.03250 |
| drop ALR | 24 | −0.04934 | **0.01120** |
| drop ALM | 23 | −0.03759 | 0.05099 |
| drop ṬSM | 27 | −0.03153 | 0.04480 |
| **drop ḤM** | 23 | **−0.02302** | **0.15588** |

Dropping any class but the ḥawāmīm leaves the effect where it was or **improves** it — removing
ALR nearly halves the p-value, because ALR actively works against the hypothesis (§4).
Removing the ḥawāmīm takes p from 0.033 to **0.156**. The same holds under P2 (0.0126 → 0.102).
**"The letter string predicts content position" is not a property of the muqaṭṭaʿāt system. It
is a property of one block.**

### 3.2 The sharpest form of the same fact, and it needs no p-value

For each of the 29, its nearest neighbour among the other 28:

> **Of the 19 surahs that belong to a multi-member letter class, only 4 have their nearest
> neighbour inside their own class** — and those four are two pairs: **Q 2 ↔ Q 3** (the two
> Medinan ALM surahs, and the tightest pair in the entire set at `d` = **0.6309**) and
> **Q 41 ↔ Q 46** (two ḥawāmīm, `d` = **0.7254**).

Fifteen of nineteen sit closest to a surah that opens with a **different** string. That is the
answer to Q2 stated without any null at all.

---

## 4. The per-class table — every class, every null

Observed `d̄` within the class, against four nulls. `N_PERIOD` (log-word-count quintiles ×
Meccan/Medinan) is the registered primary. Percentiles are % of null draws at or **below** the
observation, so **low = tighter**.

| class | n | contiguous? | `d̄` | **`N_PERIOD` pct / p** | `N_SIZE5` pct | within-the-29 pct | registered `FAM-c` pct | **size-conditional adjacency p** |
|:--|--:|:-:|--:|--:|--:|--:|--:|--:|
| **ḤM** {40,41,43,44,45,46} | 6 | ✓ (40–46) | **0.85704** | **0.08 / 0.00090** ✔ | **0.03** | 0.81 | 47.27 | **0.00010** |
| ALM {2,3,29,30,31,32} | 6 | ✗ (2–32) | 0.92568 | **2.81** / 0.02820 | 8.60 | 35.55 | 66.12 | **0.00010** |
| ṬSM {26,28} | 2 | ✗ | 0.95371 | 62.02 / 0.62024 | 49.17 | 58.53 | 79.06 | 0.39396 |
| **ALR** {10,11,12,14,15} | 5 | ✗ | 0.95518 | **79.31** / 0.79312 | 40.61 | 66.01 | 82.21 | 0.55944 |
| *ḥawāmīm-7* {40–46} | 7 | ✓ | 0.86724 | **0.30** / 0.0031 | 0.07 | — | — | 0.07909 |
| *ṭawāsīn-3* {26,27,28} | 3 | ✓ | 0.90567 | 35.73 | — | — | 63.96 | 0.22568 |

**Only ḤM clears α_bon**, at p = 0.00090 (replication 0.00110), and its size-only arm at
p = 0.00040 clears even the novelty gate of 0.000416667 — by 1.7 × 10⁻⁵, which is inside
Monte-Carlo resolution and should not be leaned on.

**ALR is the result worth stopping at.** It is the family with the strongest classical prior —
al-Biqāʿī reads الر as opening the *qiṣaṣ* block, al-Rāzī notes the same cohesion, and
H-NEW-97 independently found ALR to be 4/5 PROPHET_PERSON at p_mc = 0.0059 — and under a
size-and-period-matched null it is **at the 79th percentile: more dispersed than matched sets,
and more dispersed than its own size-blind 56th**. Matching moved it the *wrong* way.

There is a reading that fits, offered as interpretation and not as a result: **the ALR surahs
share a narrative genre by telling different stories.** Yūnus, Hūd, Yūsuf, Ibrāhīm each carry a
different prophet's proper nouns and narrative furniture, so a shared *kind* of content
produces *divergent* root distributions. The ḥawāmīm, by contrast, return to one subject.
H-NEW-97's own data says as much from the other side: ḤM is the one class that is
PROPHET_PERSON-**free**.

### 4.1 The one class that survives both controls is not the one that clears the bar

ALM is non-contiguous (span Q 2 to Q 32), sits at the 2.81st matched percentile, beats a
size-conditional adjacency control at p = 1 × 10⁻⁴, and is reproduced by only **10.5 % /
13.0 %** of arbitrary baseline offsets (§7.3). It does not clear α_bon. **The ḥawāmīm clear the
bar and lose the genre control; ALM survives the controls and misses the bar.** Both facts are
the finding; neither is a claim.

---

## 5. Q3 — what is the cluster about? **Meccan register — and that is exactly what the primary null removes.**

Registered arm R8: the maximum |z| over all 411 QAC roots with a corpus count ≥ 20, using
Monroe-style weighted log-odds with an informative Dirichlet prior. A max-statistic, so
multiplicity is handled by construction.

| null | max\|z\| observed | null mean | **p** | roots surviving BH q = 0.05 |
|:--|--:|--:|--:|--:|
| size-blind (post-hoc) | 8.672 | 5.62 | 0.0464 | **19** |
| `N_SIZE5` (post-hoc) | 8.672 | 5.46 | 0.0426 | **0** |
| **`N_PERIOD` — registered** | **8.672** | **8.275** | **0.4027** | **0** |

**R8 returns NULL. Under a size-and-period-matched null, no root distinguishes the 29 from the
other 85 at any corrected threshold.** The word list the question asked for exists only under
the size-blind null — and here it is, because naming it is what shows why it dies:

| root | | rate /10⁴ in the 29 | in the 85 | z | |
|:--|:--|--:|--:|--:|:--|
| `qwl` | قول *say* | 471.4 | 311.0 | **+8.67** | ENRICHED |
| `Ayy` | ايي *sign, verse* | 117.5 | 57.2 | **+6.62** | ENRICHED |
| `tbE` | تبع *follow* | 50.5 | 28.0 | +3.69 | ENRICHED |
| `Alh` | اله *god* | 553.1 | 722.2 | **−7.33** | DEPLETED |
| `ymn` | يمن *right hand, oath* | 6.1 | 24.9 | −4.52 | DEPLETED |
| `Alw` | الو *ālāʾ, bounties* | 1.9 | 14.2 | −3.82 | DEPLETED |
| `rDw` | رضو *be pleased, riḍwān* | 8.5 | 23.7 | −3.71 | DEPLETED |
| `mwl` | مول *māl, wealth* | 10.9 | 27.1 | −3.69 | DEPLETED |
| `EZm` | عظم *great* | 18.9 | 37.9 | −3.59 | DEPLETED |
| `jhd` | جهد *strive, jihād* | 3.3 | 14.6 | −3.55 | DEPLETED |
| `TEm` | طعم *food* | 4.7 | 16.3 | −3.45 | DEPLETED |

**Read the two columns as a single fact.** What is enriched is the vocabulary of Meccan
proclamation and dispute — *he said*, *sign*, *follow*, *people*, *sorcery*, *corruption*, *the
chiefs*. What is depleted is the vocabulary of the Medinan community — *oath*, *riḍwān*,
*mawlā*, *jihād*, *food*, *spending*. **The size-blind list is a Meccan-versus-Medinan register
list.** The muqaṭṭaʿāt are 10.3 % Medinan against 29.4 % for the rest, and when the null is
stratified on period the list evaporates. That is not a failure of the test; it is the test
working, and it is precisely the outcome pre-reg §3.2 committed to reporting in those words.

**And the list is worse than "register", which is the point of printing it.** `Alw` الو is the
fourth-strongest depletion in the table, and **31 of its 37 corpus tokens are in Q 55 al-Raḥmān
alone** — the refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān*. A "root that distinguishes the
muqaṭṭaʿāt from the rest of the corpus" is here **one surah's refrain, appearing in a surah
that is not one of the 29**. Any size-blind vocabulary contrast on a group this compositionally
skewed will pick up single-surah artefacts, and this one does.

### 5.1 The ḥawāmīm profile — coherent, classical, and not established

The ḥawāmīm against the other 107 surahs, `N_PERIOD`-matched. Registered as descriptive only.
**max|z| = 5.06, p = 0.6916, 0 roots survive BH.** The individual roots, several of which clear
0.05 uncorrected, are worth naming because the profile is internally consistent:

| enriched | | /10⁴ ḥawāmīm | rest | z | p | | depleted | | | | |
|:--|:--|--:|--:|--:|--:|:-:|:--|:--|--:|--:|--:|
| `dEw` | دعو *call, invoke* | 119.8 | 42.5 | +5.06 | 0.027 | | `Ahl` | اهل *people, family* | 3.3 | 30.4 | −2.23 |
| `swE` | سوع *the Hour* | 43.3 | 8.7 | +4.46 | 0.008 | | `qtl` | قتل *kill* | 10.0 | 40.3 | −2.21 |
| `byn` | بين *make clear, mubīn* | 199.7 | 111.7 | +3.77 | 0.009 | | `Alh` | اله *god* | 499.2 | 651.9 | −2.96 |
| `ywm` | يوم *Day* | 156.4 | 86.4 | +3.40 | 0.043 | | | | | | |
| `kbr` | كبر *arrogance* | 76.5 | 33.3 | +3.28 | 0.072 | | | | | | |
| `jdl` | جدل *disputation* | 23.3 | 5.3 | +3.05 | **0.016** | | | | | | |
| `Afk` | افك *falsehood* | 23.3 | 5.6 | +2.97 | 0.089 | | | | | | |
| `ryb` | ريب *doubt* | 23.3 | 7.0 | +2.54 | **0.005** | | | | | | |
| `Erb` | عرب *Arabic* | 16.6 | 4.1 | +2.46 | **0.009** | | | | | | |

Against the other **22 muqaṭṭaʿāt** the same shape sharpens: `qwl` (*say*) is **depleted** at
z = −3.70, and so are `Ahl`, `Axw` (*brother*), `nfs`, `nws` — **the machinery of prophet
narrative** — while `jHm` (*jaḥīm*), `E*b` (*punishment*), `ErD`, `Znn` are enriched. The
ḥawāmīm are the block that argues rather than narrates. That is the classical reading of Q 40–46
and the profile matches it. **It is not established here**: nothing survives correction for 411
roots, and the two arms that fire hardest are the two whose null overlaps the observation most
(§7.1).

> **One trap, named so it is not walked into.** Two "enriched" roots in the ḥawāmīm list are
> homographs of muqaṭṭaʿāt strings — `Hmm` حمم (*ḥamīm*, boiling water) at 5 tokens against 3,
> and `Alm` الم (*alīm*, painful) at 9 against 23 elsewhere in the 29. **Both are at counts
> where nothing can be concluded, and neither is evidence that the letters abbreviate a word.**
> This is exactly the coincidence ʿilm al-ḥarf feeds on, and H-NEW-2670 measured what such
> coincidences are worth: roughly one random 14-letter subset in four can be made to look
> unique given free choice of axes.

---

## 6. Q4 — where do the singletons fall? The map

`centrality(s)` = mean distance to the other 28. `pctile_matched` = its percentile among
10,000 substitutes drawn from *s*'s own log-word-count × period stratum, scored against the
same other 28. Locked: `INSIDE` ≤ 25, `OUTSIDE` ≥ 75. **BRIDGE** = the three nearest neighbours
inside the 29 span two or more multi-member classes.

| surah | class | centrality | **pct** | label | 3 nearest in the 29 | |
|:--|:--|--:|--:|:--|:--|:--|
| **Q 13** al-Raʿd | ALMR | 0.9248 | **0.00** | INSIDE | 14, 40, 41 | BRIDGE · one-off string |
| Q 41 Fuṣṣilat | ḤM | 0.8727 | 5.15 | INSIDE | 46, 32, 45 | BRIDGE |
| Q 45 al-Jāthiya | ḤM | 0.8848 | 14.65 | INSIDE | 31, 32, 41 | BRIDGE |
| Q 32 al-Sajda | ALM | 0.9031 | 14.74 | INSIDE | 41, 45, 46 | |
| **Q 7** al-Aʿrāf | ALMS | 0.8888 | 23.77 | INSIDE | 10, 28, 11 | BRIDGE · one-off string |
| Q 46 al-Aḥqāf | ḤM | 0.8879 | 31.37 | INTERMEDIATE | 41, 32, 45 | BRIDGE |
| Q 2 al-Baqara | ALM | 0.9618 | 32.79 | INTERMEDIATE | 3, 7, 29 | |
| Q 3 Āl ʿImrān | ALM | 0.9737 | 32.81 | INTERMEDIATE | 2, 40, 29 | BRIDGE |
| Q 44 al-Dukhān | ḤM | 0.9481 | 35.49 | INTERMEDIATE | 32, 15, 45 | BRIDGE |
| Q 10 Yūnus | ALR | 0.9018 | 38.13 | INTERMEDIATE | 7, 27, 29 | |
| Q 40 Ghāfir | ḤM | 0.9023 | 38.19 | INTERMEDIATE | 7, 13, 10 | |
| Q 27 al-Naml | ṬS | 0.9060 | 42.31 | INTERMEDIATE | 7, 10, 28 | BRIDGE · one-off string |
| Q 29 al-ʿAnkabūt | ALM | 0.9105 | 46.21 | INTERMEDIATE | 10, 45, 11 | BRIDGE |
| Q 43 al-Zukhruf | ḤM | 0.9131 | 52.56 | INTERMEDIATE | 36, 15, 41 | BRIDGE |
| **Q 50** Qāf | QAF | 0.9817 | 57.26 | INTERMEDIATE | 32, 68, 38 | **one-off** |
| **Q 36** Yā-Sīn | YS | 0.9151 | 58.27 | INTERMEDIATE | 43, 15, 41 | BRIDGE · **one-off** |
| Q 28 al-Qaṣaṣ | ṬSM | 0.9249 | 61.21 | INTERMEDIATE | 7, 27, 10 | |
| Q 11 Hūd | ALR | 0.9208 | 62.51 | INTERMEDIATE | 7, 10, 29 | BRIDGE |
| Q 14 Ibrāhīm | ALR | 0.9231 | 68.67 | INTERMEDIATE | 13, 40, 42 | |
| **Q 68** al-Qalam | NUN | 1.0159 | 71.17 | INTERMEDIATE | 32, 50, 44 | BRIDGE · **one-off** |
| Q 15 al-Ḥijr | ALR | 0.9341 | 78.92 | OUTSIDE | 36, 43, 32 | BRIDGE |
| **Q 20** Ṭā-Hā | TH | 0.9739 | 84.34 | **OUTSIDE** | 7, 41, 43 | **one-off** |
| **Q 42** al-Shūrā | ḤM-ʿSQ | 0.9469 | 89.41 | **OUTSIDE** | 45, 14, 13 | BRIDGE · one-off string |
| Q 26 al-Shuʿarāʾ | ṬSM | 0.9978 | 92.27 | OUTSIDE | 7, 15, 36 | |
| **Q 38** Ṣād | SAD | 0.9681 | 94.71 | **OUTSIDE** | 50, 32, 43 | BRIDGE · **one-off** |
| **Q 19** Maryam | KHYʿṢ | 0.9714 | 94.92 | **OUTSIDE** | 43, 46, 41 | **one-off** |
| Q 30 al-Rūm | ALM | 0.9674 | 95.13 | OUTSIDE | 45, 10, 40 | BRIDGE |
| Q 31 Luqmān | ALM | 0.9688 | 100.00 | OUTSIDE | 45, 13, 14 | BRIDGE |
| Q 12 Yūsuf | ALR | 1.0362 | 100.00 | OUTSIDE | 7, 27, 28 | |

**R9's inference: the six one-off strings sit at a mean matched percentile of 76.8 against
50.3 for the 23 class members — a gap of +26.5 — at two-sided p = 0.0546.** Registered
two-sided because I had no defensible prior. It does not clear α_bon. **Three of the six are
OUTSIDE** (Q 20, Q 38, Q 19) and none is INSIDE.

Four things in the table are worth more than the p-value:

1. **The most central surah in the entire set has a one-off string.** Q 13 al-Raʿd (المر) sits
   at the **0th** matched percentile and bridges ALR and ḤM. The letters that occur once are
   not the surahs that sit outside.
2. **Q 7 al-Aʿrāf (المص) is the hub.** It is the nearest neighbour, within the 29, of **eight**
   of the other twenty-eight — Q 10, 11, 12, 20, 26, 27, 28, 40. No other surah is nearest to
   more than three. The single surah with the unique four-letter opening is the centre of the
   network.
3. **Q 42 al-Shūrā is outside the block it belongs to.** The one ḥawāmīm surah with the extra
   عسق sits at the **89th** percentile while the other six are at 5–53, and adding it to the
   block loosens it: ḤM-6 is at the 0.08th percentile, ḥawāmīm-7 at the 0.30th, and under the
   size-conditional adjacency control ḤM-6 is at p = 1 × 10⁻⁴ and ḥawāmīm-7 at p = 0.079.
   **The anomalous string marks an anomalous member.** This is descriptive; no test was
   registered for it.
4. **19 of the 29 have their nearest neighbour in the whole corpus inside the 29** (65.5 %).
   That is the cluster, seen without a null. The ten exceptions reach outward to Q 6, 23, 25,
   51, 78 and — for Q 68 al-Qalam — to Q 100 al-ʿĀdiyāt.

---

## 7. The controls — including two that damage this finding

### 7.1 The matched null for this group is **more than half this group**

The single most important number here, and it belongs beside every percentile in this file and
in H-NEW-2820.

| null | mean overlap with the observed 29 | as a fraction |
|:--|--:|--:|
| **`N_PERIOD` — primary** | **16.32 of 29** | **56.3 %** |
| `N_SIZE10` | 14.99 | 51.7 % |
| `N_SIZE5` | 14.16 | 48.8 % |
| size-blind (the published null) | 7.37 | 25.4 % |

**A "matched random 29-set" is, on average, sixteen of the muqaṭṭaʿāt.** This is
H-NEW-2820 §2.2b — *a size-matched comparison group cannot be built from the 85
non-muqaṭṭaʿāt at all* — stated as a power bound rather than an impossibility. It caps what
any matched arm can detect, and it is the direct explanation for why R8 returns NULL: the null
sets have most of the observed set's vocabulary in them because they have most of its surahs
in them. **Every matched result in this finding and in H-NEW-2820 is conservative for this
reason, and every matched NULL here is correspondingly weak evidence of absence.**

### 7.2 My registered adjacency control was size-confounded. Here is the measurement, and the repair.

`FAM-c` compares a class to random contiguous mushaf runs of the same length. It fired the
`-ADJACENCY-EXPLAINED` modifier. **It should not be trusted, and the reason is measurable:**

| run length | run null mean `d̄` | ρ(run `d̄`, run mean log word count) | size-matched null mean |
|:--|--:|--:|--:|
| 6 | **0.7781** | **+0.838** | 0.95041 |
| 7 | 0.7814 | +0.832 | — |

A random contiguous run sits **0.17 below** the size-matched null, and its `d̄` correlates with
its own mean log word count at ρ = +0.84. Contiguous mushaf runs are size-homogeneous, and
size-homogeneous sets are close — so `FAM-c` reintroduces the exact channel this finding
exists to control. **This is `UNIT-DRIFT-DEFECT` §5's "a control that does not use the
strongest channel is not a control", committed inside a finding whose whole subject is that
rule.** I registered it, I ran it, and it is wrong.

**The repair (post-hoc): contiguous runs restricted to those whose mean log word count is
within ±0.25 of the class's.**

| class | observed | conditional-run null | z | **p** | qualifying runs |
|:--|--:|--:|--:|--:|--:|
| ḤM-6 | 0.85704 | 0.93219 | −2.00 | **0.00010** | 22,175 |
| ALM-6 | 0.92568 | 0.95953 | −2.19 | **0.00010** | 32,923 |
| ḥawāmīm-7 | 0.86724 | 0.93175 | −1.83 | 0.07909 | 24,319 |
| ṭawāsīn-3 | 0.90567 | 0.94432 | −0.66 | 0.22568 | 31,900 |
| ALR-5 | 0.95518 | 0.95368 | +0.06 | 0.55944 | 32,487 |
| ṬSM-2 | 0.95371 | 0.96225 | −0.10 | 0.39396 | 31,635 |

**Under the repaired control the `-ADJACENCY-EXPLAINED` modifier reverses for ALM and ḤM.**
The registered verdict keeps the modifier because that is what the registered rule computed;
the repair is post-hoc and carries no verdict. **A reader should carry both, and should note
that the repair helps this finding, which is why it is quarantined.**

### 7.3 The genre control — and it is the reason the ḥawāmīm result cannot be called a discrimination

200 matched partitions per baseline, cut to the Qurʾān's exact verse word-length profile and
grouped on its exact surah verse counts, so the pseudo-class taken at the same surah slots has
**identical verse counts, verse lengths and word counts to the real class, to the token**. The
Qurʾān's own verses are never re-partitioned. Surface word types throughout, since no
morphological analyser exists for the baselines.

**(a) The whole 29-set is NOT reproduced.**

| | Qurʾān (surface) | al-Bukhārī (200 offsets) | al-Jāḥiẓ (200 offsets) |
|:--|--:|--:|--:|
| `d̄` matched percentile | **4.80** | 0.00 / **43.15** / 96.35 | 0.00 / **36.85** / 99.90 |
| offsets at or below the Qurʾān's surface value | — | **8.0 %** | **6.5 %** |
| offsets at or below the Qurʾān's **root** value (5.48) | — | **10.0 %** | **8.0 %** |
| offsets clearing the claim's own 10 % bar | — | 15.5 % | 17.5 % |

*(min / median / max.)* This reproduces H-NEW-2820 §4.2 — which measured 16.5 % / 16.0 % on the
10 % bar — in an independently written harness.

**(b) The ḥawāmīm ARE reproduced, and at the median.**

| class | contiguous? | Qurʾān | al-Bukhārī median | al-Jāḥiẓ median | offsets ≤ Qurʾān (B / J) |
|:--|:-:|--:|--:|--:|--:|
| **ḥawāmīm-7** | ✓ | **3.20** | **3.67** | **2.75** | **47.5 % / 52.0 %** |
| **ḤM-6** | ✓ | **0.30** | 4.03 | 4.85 | **21.5 % / 19.5 %** |
| ṭawāsīn-3 | ✓ | 35.65 | 7.85 | 8.85 | 85.0 % / 86.0 % |
| **ALM-6** | ✗ | **1.00** | 18.55 | 16.38 | **10.5 % / 13.0 %** |
| ALR-5 | ✗ | 37.00 | 10.75 | 12.02 | 75.5 % / 77.0 % |
| ṬSM-2 | ✗ | 67.95 | 32.38 | 33.77 | 83.5 % / 85.0 % |
| **muqaṭṭaʿāt-29** | ✗ | **4.80** | 43.15 | 36.85 | **8.0 % / 6.5 %** |

**Read the `contiguous?` column against the last one.** Every contiguous class is reproduced by
arbitrary partitions of a ḥadīth collection or a book of adab zoology at rates of 19–86 %;
every non-contiguous class is reproduced at 6.5–13 % or else fails outright. **Within one
instrument, one set of 200 offsets, and one null, the difference between the reproduced and
the unreproduced is contiguity.** In a matched partition, contiguous slots are contiguous
chunks of one continuous book and share local vocabulary by construction.

**The honest consequence, stated at full weight: the ḥawāmīm result — the one arm in this
finding that clears its bar — is at the strength of "six consecutive chunks of a single
continuous text", and roughly half of arbitrary offsets match it.** H-NEW-600 §4 guessed this
("HM-7 partial cohesion is a chronology + consecutive-mushaf-position effect"), reached it from
a premise that was wrong (that 20.90 % was weak), and lands on the right answer under a proper
control.

**One qualification that cuts the other way and must not be dropped.** Per
`STATE-OF-THE-PROJECT-2026-08-07.md` §4.7, this statistic is **contiguity-sensitive**, so
arbitrary cuts *preserve* local continuity and make the law **easier** for a baseline. A
baseline pass is therefore **weak** evidence against a contiguity-sensitive claim. §7.3(b) is
not a refutation of the ḥawāmīm; it is a demonstration that the claim cannot be called a
discrimination, and that the within-corpus arms (§4, §7.2) are where its weight sits.

**(c) The class-structure statistic Δ is genre-shared, and my modifier missed it by 0.0005.**

| | Qurʾān (surface) | al-Bukhārī | al-Jāḥiẓ |
|:--|--:|--:|--:|
| Δ | **−0.04587** | −0.12597 / **−0.04859** / +0.00782 | −0.10618 / **−0.03637** / +0.00544 |
| Δ `F1` p | **0.00600** | 0.00050 / **0.00650** / 0.66267 | 0.00050 / **0.00975** / 0.66617 |
| offsets clearing α_bon | — | **46.5 %** | **41.0 %** |
| offsets with Δ p ≤ the Qurʾān's | — | **50.0 %** | **45.0 %** |

**Half of arbitrary partitions of al-Bukhārī produce a within-class-versus-between-class
contrast at least as extreme as the Qurʾān's, and al-Bukhārī's median Δ (−0.04859) is *more*
negative than the Qurʾān's (−0.04587).** The registered `-GENRE-SHARED` modifier did not fire —
see §9.1, where the reason is a pre-registration ambiguity I am obliged to disclose rather
than resolve in my own favour. **Substantively, Δ is genre-shared, and the modifier's silence
is a technicality.**

**(d) S1.** Qurʾān p = 0.80060; al-Bukhārī median 0.52599; al-Jāḥiẓ median 0.48626. The Qurʾān
is less sub-structured than its own matched null **and** than the median arbitrary partition.

---

## 8. Independence from Pillar 1 — assessed, and it does not combine in either direction

Pillar 1 (H-NEW-2760) and this finding are computed on **the same 29 surahs in the same
corpus**. Pre-reg §8 bound this in advance and the binding holds whatever the arms returned.

**R10 / R11 — Book-root ablation, rebuilt-against-rebuilt.** Roots are removed *before* the
top-500 selection, so the vocabulary refills to 500 and the contrast is not a
498-versus-500-dimension artefact.

| matrix | `N_PERIOD` pct | `N_SIZE5` pct |
|:--|--:|--:|
| rebuilt, full 500 | **5.48** | **0.43** |
| **R10** minus {`ktb` كتب, `qrA` قرأ} | 6.01 | 0.44 |
| **R11** minus {`ktb`, `qrA`, `tlw` تلو, `nzl` نزل, `Ayy` ايي, `*kr` ذكر, `wHy` وحي, `frq` فرق} | **6.94** | **0.66** |

Both stay far inside the 10 % bar → **`PILLAR1-DISTINCT`**. The rebuilt-full values reproduce
H-NEW-2820's frozen-matrix A2c = 5.44 and A2-k5 = 0.45 in a separately built harness.

**This extends H-NEW-2830 rather than repeating it.** That finding removed Pillar 1's two
marker roots and benchmarked the shift against 200 frequency-matched arbitrary pairs. R11 goes
further: removing **the whole revelation-and-recitation vocabulary** — Book, recite, send down,
sign, remind, inspire, criterion, 1,587 tokens and eight of five hundred dimensions — moves the
matched percentile by 1.46 points and leaves the cluster at the 6.94th percentile.

**What this licenses, and what it does not.**

- It refutes double-counting: the clustering is not the Book signal in a second instrument.
- It equally refutes the mirror worry — that Pillar 1's residual is topical composition —
  since whatever the 29 share is demonstrably *not* revelation vocabulary.
- **It does not make this an independent confirmation of Pillar 1, and this finding is not
  reported as one.** Same group, same non-random selection, same conditioned space, same
  10.3 %-versus-29.4 % Medinan skew. H-NEW-2670 established that given free choice of
  properties, roughly one random 14-letter subset in four can be made to look as unique as the
  muqaṭṭaʿāt. **Two properties of one group are not two confirmations.** Pillar 1 stands
  exactly where H-NEW-2760 left it: rate ratio 2.580 against the registered channel, **1.694**
  against the stronger one, its published `p = 3.17 × 10⁻¹²` withdrawn.

---

## 9. Verdicts

**Diffed clause-by-clause against pre-registration §8 before declaring, and again after.**

| | primary seed | replication seed |
|:--|:--|:--|
| **registered verdict** | **`NO-SUB-STRUCTURE-ADJACENCY-EXPLAINED`** | **`NO-SUB-STRUCTURE-ADJACENCY-EXPLAINED`** |
| R2 (Δ, F1) | p = 0.03250 | p = 0.02960 |
| R3 (Δ, F2) | p = 0.03480 | p = 0.04120 |
| classes passing R4–R7 | ḤM | ḤM |
| **independence** | **`PILLAR1-DISTINCT`** (narrow 6.01, wide 6.94) | — |

**Not `SEED-FRAGILE`.** Ten of twelve registered inferences fail their corrected bar: R1, R2,
R3, R4 (ALM), R5 (ALR), R6 (ṬSM), R8, R9, R12 all fail; R7 (ḤM) passes; R10 and R11 pass in the
"stays inside the bar" sense their direction was locked to.

### 9.1 Three gaps between the runner and the pre-registration, found by doing the diff

Disclosed because the diff is what found them, which is the argument for doing it.

1. **`-GENRE-SHARED` is ambiguous in the pre-registration and the two readings disagree.**
   §6 says the modifier fires if *"the median offset of either baseline reaches the Qurʾān's
   own value in the surface instrument for that statistic."* The runner read "that statistic"
   as Δ's **p-value**: al-Bukhārī's median 0.00650 against the Qurʾān's 0.00600 — it does not
   fire, **by 0.0005**. Read as Δ **itself**, al-Bukhārī's median −0.04859 is more extreme than
   the Qurʾān's −0.04587 and **it does fire**. **Under the stricter reading the verdict is
   `NO-SUB-STRUCTURE-GENRE-SHARED-ADJACENCY-EXPLAINED`, and that is the reading a reader
   should carry** — per `UNIT-DRIFT-DEFECT` §6 clause 6, where two nulls disagree, report both
   and take the stricter. The registered verdict line is left as the runner computed it; this
   is the correction, not a substitution.
2. **`FAM-c` is a broken control (§7.2)** and the `-ADJACENCY-EXPLAINED` modifier it fired is
   mechanically correct and substantively wrong. The repair is post-hoc and reverses it for
   ALM and ḤM.
3. **One reported diagnostic used the wrong reference value.** In `results.json`,
   `genre_offset_fractions[*].frac_dbar_pct_below_quran_root` was computed against
   `R1.N_PERIOD.pct_le` — which is **S1's** percentile (9.31), not `d̄`'s (5.48). The stored
   values are 0.140 / 0.155; **the correct figures are 0.100 (al-Bukhārī) and 0.080
   (al-Jāḥiẓ)**, recomputed from the retained per-offset values and used in §7.3(a). The
   correction **improves** the Qurʾān's margin, which is why it is stated here rather than
   quietly applied.

### 9.2 The registered predictions were three-quarters right, and the wrong quarter is named

Pre-reg §9 registered four. **§9.1 (the ḥawāmīm are the tightest class and clear R7)** —
confirmed, and then largely undone by §7.3(b). **§9.2 (Δ negative under F1, attenuating under
F2)** — direction confirmed; attenuation **did not happen** (p 0.0325 → 0.0348, essentially
unchanged), so the ALM size story I expected is not what carries Δ. **§9.3 (R1 will fail)** —
confirmed. **§9.4 (the ablations will not kill the cluster)** — confirmed.

---

## 10. What should change in the project record

Flagged, not applied — a correction to another finding's file is not mine to make.

- **`h-new-600-letter-families.md` needs its own correction notice, and it is now a
  discharge rather than a warning.** Its existing notice says its ALM-6 and ALR-5 results are
  *"UNTESTED, not cleared"* and that running them through the H-NEW-2820 stratified null *"is
  the cheap next step and has not been done."* **It has now been done.** The two halves of its
  DOUBLE NULL move in opposite directions:

  | | published (size-blind) | regenerated | **`N_PERIOD` matched** | direction |
  |:--|--:|--:|--:|:--|
  | ALM-6 | 43.15 | 41.89 | **2.81** | toward cohesion; still short of α_bon (p = 0.0282) |
  | ALR-5 | 56.25 | 55.92 | **79.31** | **away** — more dispersed than matched sets |

  Its §3 calls ALR *"the decisive falsifier… the family with the strongest prior is the one
  most thoroughly NULL."* **That sentence survives matching and gets stronger**, and it is the
  only load-bearing claim in H-NEW-600 that does. Its §4 table row for ALM does not survive.
  Its honest-limit 7 — *"FR uses L1-normalized probability vectors (length-controlled per
  H-NEW-111 MW-1), so this is not a confound"* — is **asserted, not computed, and false**:
  `d̄` correlates with mean log word count at ρ = +0.8998 (H-NEW-2820 §2.1). That is
  `STATE-OF-THE-PROJECT` §4.5 and `UNIT-DRIFT-DEFECT` §5's *"normalisation is not
  invariance"*, in a file that predates both.
- **Two of H-NEW-600 §9's queued follow-ups are discharged**, both NULL under `N_PERIOD`:
  **H-NEW-620** (ALMR-extended-6 = ALR-5 ∪ {Q 13}) at the **49.17th** percentile, and
  **H-NEW-630** (Q 29–32, al-Biqāʿī's "tight Meccan block" inside ALM) at the **33.67th**.
  Its **H-NEW-640** (ALR against a chronology-and-adjacency-controlled null) is partly
  discharged by §7.2 and §7.3. Its MW-6 instrument check reproduces and stays over-dispersed
  (87.54 size-blind, **93.49** matched), so that instrument caveat holds.
- **`h-new-570-muqattaat-content-cluster.md` / `H-NEW-570-REVERSAL-2026-08-07.md`** — the
  reversal stands and is confirmed in a separately written harness (5.48 against 5.44, 0.43
  against 0.45). **Two additions belong in the notice**: the ḥawāmīm half of it is
  contiguity-reproducible by baselines (§7.3b), and the matched null overlaps the observed set
  by 56 % (§7.1).
- **`findings/UNIT-DRIFT-DEFECT.md` §6** — the cheap-diagnostics list should gain **null
  overlap**: *when a stratified null must draw from strata the group itself dominates, report
  the mean overlap between a null draw and the observed group.* At 56.3 % it bounds power
  directly, costs one line of code, and is more informative than any p-value computed against
  such a null. It sits naturally beside the "0 of 10,000" diagnostic already recorded there.
- **`findings/UNIT-DRIFT-DEFECT.md` §5** — §7.2 of this file is a fresh instance of *"a
  control that does not use the strongest channel is not a control"*, committed by a
  pre-registered control inside a finding about that rule, and caught only by measuring the
  control itself. Worth one line as the third case.
- **`STATE-OF-THE-PROJECT-2026-08-07.md` §1** — if the muqaṭṭaʿāt content cohesion is listed,
  it should be listed as **a single cluster with no letter-class structure**, at 5.48 (period-
  matched) and with the note that its strongest sub-part is contiguity-reproducible.
- **`h-new-1395-hawamim-cluster.md` and `h-new-1760-hawamim-opener-pericope.md`** — both
  already carry reversal notices. Both should gain §7.3(b): the whole-surah ḥawāmīm cohesion
  is reproduced by contiguous slots of a partitioned baseline about half the time.

---

## 11. Honest limits

1. **The matched null contains the group.** 56.3 % mean overlap (§7.1). Every matched NULL
   here — R8 above all — is weak evidence of absence, and every matched pass is conservative.
   This is the dominant limitation of the whole design and no arm escapes it.
2. **The genre arm cannot use roots.** No morphological analyser exists for the baselines, so
   §7.3 is surface-word-type only. The Qurʾān's surface values are reported for like-for-like
   comparison and the two instruments agree on the 29-set (4.80 surface, 5.48 root), but a
   surface result does not automatically transfer to the root layer.
3. **A partition is not a composed book, and here that cuts against the control.** The class
   statistics are contiguity-sensitive; arbitrary cuts preserve local continuity and make the
   baselines' job easier. §7.3(b) shows the ḥawāmīm claim cannot be called a discrimination;
   it does not show the claim is false, and the asymmetry is stated in §7.3 rather than used
   as a blanket excuse.
4. **`FAM-c`, a registered control, is invalid** (§7.2). Its repair is post-hoc and helps this
   finding, so it is quarantined and carries no verdict.
5. **Monte-Carlo resolution on the vocabulary screen.** With 10,000 draws the smallest
   attainable two-sided per-root p is 2.0 × 10⁻⁴, so BH at q = 0.05 over 411 roots requires at
   least two roots at the floor. The size-blind arm reached it (19 survivors); the matched arms
   were nowhere near it, so the resolution limit is not what produced their zeros.
6. **The `d̄` statistic is size-dependent by construction** (ρ = +0.90, H-NEW-2820 §2.1). Every
   result here is a size-conditional statement, and conditioning on size may remove mechanism
   as well as confound — `h-new-46` is a STRONG-PASS that the muqaṭṭaʿāt concentrate in long
   surahs, so holding length fixed removes part of what they *are*.
7. **The classes are small.** ṬSM has two members and one pair; ALM, ALR and ḤM have 5–6.
   No power correction rescues a class at the 79th percentile, but ṬSM's 62nd is
   uninterpretable and is reported only for completeness.
8. **P2 requires two judgments of mine** — that Q 27 joins the ṭawāsīn and Q 42 the ḥawāmīm.
   Both are classically attested; both are choices. P1 is mechanical and is primary.
9. **Three matched genres.** The reference class is small, as it is for every percentile in
   H-NEW-2720 and H-NEW-2820.
10. **The interpretation in §4 — that ALR diverges because its surahs tell different stories —
    is interpretation.** It is consistent with H-NEW-97's independent name-class result and
    with the depleted narrative vocabulary in §5.1, and it was not registered and is not
    tested.

---

## 12. Garden of forking paths

- **Everything in §§2–9 was computed after the lock at SHA `321f7fe9…e11c2a`, which was
  committed at `bee950a31` before the runner existed.**
- **The pre-lock probe computed no outcome statistic.** It established the matrix rebuild
  fidelity, the strata estimability at k = 3/4/5, and the class sizes — all recorded in
  pre-reg §10 before the lock. No pairwise distance among the 29, no within-class mean, no
  cluster structure and no root statistic was computed before the document was locked.
- **The channel ranking was inherited from H-NEW-2820 §2.1, not re-derived**, so it cannot
  have been chosen to suit this result.
- **Both bin widths and both partitions were registered**, k = 5 and P1 primary; all four are
  reported.
- **Directions were locked for eleven of twelve inferences**; R9 was registered two-sided in
  advance because I had no prior.
- **The four registered predictions are scored in §9.2 and one is wrong.**
- **Three runner/pre-registration gaps are disclosed in §9.1**, one of which changes the
  verdict string under the stricter reading and is reported as such.
- **The per-class genre control of §7.3(b) was NOT registered**, was run because the registered
  arms showed the whole effect was one contiguous class, and it is **the arm that most damages
  this finding**. It is labelled post-hoc throughout and lives in its own run directory.
- **Post-hoc material is confined to §§3.1, 5, 7.2, 7.3(b) and 10**, each labelled, none
  carrying a verdict.
- **Write-once observed**: run directories created with `exist_ok=False`, every file opened
  `'x'`, `results.json` written once at completion, checkpoints outside the run directory in
  files never rewritten. **No run directory was deleted.**
- **The pre-registration was committed before the run; no other commit was made by this lane
  before the finding was complete.**

---

## 13. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2840-muqattaat-structure.md`
  (SHA-256 `321f7fe90f9f4f956b4ab91cf0e39179553175b895068ad69ac6d3e9c1e11c2a`, committed
  `bee950a31`)
- Registered runner: `findings/phase-b-hypotheses/scripts/h-new-2840.py` — pre-reg SHA-gated;
  lifts the H-NEW-2680 partition code verbatim with three fragment SHA checks; asserts the
  Fisher–Rao path bit-identical to the published `h-new-570` routine
- Post-hoc: `findings/phase-b-hypotheses/scripts/h-new-2840-posthoc.py` and
  `findings/phase-b-hypotheses/scripts/h-new-2840-posthoc-genre.py`
- Runs (immutable, never deleted), each with a `manifest.json` recording every frozen input
  SHA in repository-relative form:
  - `findings/phase-b-hypotheses/runs/h-new-2840/20260807T101255Z/` — **registered primary**
  - `findings/phase-b-hypotheses/runs/h-new-2840/20260807T100806Z-SMOKE/` — smoke, retained
  - `findings/phase-b-hypotheses/runs/h-new-2840-posthoc/20260807T103932Z/`
  - `findings/phase-b-hypotheses/runs/h-new-2840-posthoc-genre/20260807T104225Z/`
- Machine output: `findings/phase-b-hypotheses/csv/h-new-2840.json`

---

*Run 2026-08-07 by Waiel Al-Shujaa. The twenty-nine are one cluster and the letters do not
carve it: fifteen of nineteen class members sit closest to a surah that opens differently, the
one class that coheres is six consecutive surahs, and a partitioned book of adab zoology cut at
the same six slots does the same thing half the time. The vocabulary that looked like the
cluster's subject was the Meccan register, and it left when period entered the null. What is
left is real and small and single: a set of twenty-nine that are nearer to one another than to
anything their size and period would predict, with no internal order that the opening letters
explain. Bismillāhi al-Raḥmāni al-Raḥīm.*
