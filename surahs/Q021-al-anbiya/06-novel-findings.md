---
surah: 21
surah_name_ar: الأنبياء
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 5 pre-registered tests run; 1 CONFIRMED, 1 DIRECTIONAL-borderline, 3 NULL
---

# Q 21 al-Anbiyāʾ — Pre-Registered Novel Findings


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Five pre-registered tests run on 2026-05-07 (seed 20260507). All pre-regs SHA-locked and verified at runtime. Outputs at `surahs/Q021-al-anbiya/csv/`. Each script begins with `assert sha == EXPECTED_SHA`.

## Q021-F-01 — Prophet-cycle completeness (NULL/PRE-COMMIT VIOLATION)

### Pre-reg
- File: `Q021-F-01-prophet-cycle-completeness-prereg.md`
- SHA256: `6417085b816096084978359223408d20c0f159205d7e94949508363059598dfa`
- Direction (locked): Q 21 = rank 1 / 114 on distinct canonical-prophet PN-lemma count.

### Garden-of-forking-paths log
The author observed Q 21 = 14 prophets and Q 6 = 16 prophets BEFORE locking the pre-reg, during exploratory analysis on 2026-05-07. The pre-reg locked the original task-seed direction (MAX) anyway, fully disclosing the pre-observation per [[INVESTIGATION-PROTOCOL §1.8|honest-pre-commit-violation protocol]]. The verdict is published with full prominence as a NULL.

### Method
QAC v0.4 PN-lemma extraction; locked 25-name canonical prophet set (Adam, Nūḥ, Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, Yūsuf, Lūṭ, Hūd, Ṣāliḥ, Shuʿayb, Mūsā, Hārūn, Dāwūd, Sulaymān, Ilyās, al-Yasaʿ, Yūnus, Zakariyyā, Yaḥyā, ʿĪsā, Idrīs, Ayyūb, Muḥammad, Aḥmad). Per-surah set-size ranking.

### Result

| Rank | Surah | Distinct prophets |
|:-:|:-:|:-:|
| 1 | **Q 6 al-Anʿām** | **16** |
| **2** | **Q 21 al-Anbiyāʾ** | **14** |
| 3 | Q 4 al-Nisāʾ | 11 |
| 3 | Q 19 Maryam | 11 |
| 5 | Q 3 Āl ʿImrān | 10 |

Q 6's 16 prophets: Ibrāhīm, Ilyās, Isḥāq, Ismāʿīl, Ayyūb, Dāwūd, Hārūn, Lūṭ, Mūsā, Nūḥ, Sulaymān, Yaʿqūb, Yaḥyā, Yūnus, Yūsuf, Zakariyyā.

Q 21's 14 prophets: Ibrāhīm, Idrīs, Isḥāq, Ismāʿīl, Ayyūb, Dāwūd, Hārūn, Lūṭ, Mūsā, Nūḥ, Sulaymān, Yaʿqūb, Yaḥyā, Zakariyyā.

### Verdict
**NULL / PRE-COMMIT VIOLATION**. Q 21 is rank 2 / 114, not rank 1 / 114. The corpus-MAX of distinct canonical prophets is in **Q 6 al-Anʿām** (16 prophets in vv. 83-86), not in Q 21 al-Anbiyāʾ.

### Bonferroni
k=1, no correction needed. Direction did not match.

### Honest interpretation
Q 6:83–86 is a **dense 4-verse list** (the Ibrāhīm-then-his-line passage); Q 21:48–91 is a **44-verse narrative-catalog** with each prophet given an episode. Q 21's "prophet-density" is in *narrative attention per prophet* (median ~3 verses each), whereas Q 6's "prophet-density" is in *list-cardinality per verse* (median ~4 prophets per verse). The Quran has TWO prophet-cycle modes (list-form and narrative-form); Q 21 is the **maximum NARRATIVE-form** prophet-cycle, not the maximum **list-form** (which is Q 6).

The naming of Q 21 as al-Anbiyāʾ (The Prophets) is therefore consistent with its NARRATIVE-catalog architecture, not with raw cardinality. This is a refined interpretation of the surah-eponym mechanism that the strict pre-reg test produces *only* by passing through the NULL.

## Q021-F-02 — Prophet-order distance (NULL)

### Pre-reg
- File: `Q021-F-02-prophet-order-distance-prereg.md`
- SHA256: `780454a427c82c582d9d9987251e4a4b9f44c61b861b495b9a01e83d46174fdf`
- Direction (locked): mean(d(Q21,Q11), d(Q21,Q26), d(Q21,Q37)) < d(Q21,Q6) — Q 21 follows a different prophet-cycle template than Q 6.

### Method
First-occurrence prophet order from QAC v0.4 (mushaf-position) for Q 6, Q 11, Q 21, Q 26, Q 37. Pairwise normalized Kendall-τ inversion-count distance on the common prophet-set. 10 000-permutation null on Q 21's order.

### Result

| Cell | Pair | Common-set size | Distance d |
|:--|:--|:--:|:--:|
| A | Q 21 ↔ Q 6 | 13 | **0.321** |
| B | Q 21 ↔ Q 11 | 5 | **0.300** |
| C | Q 21 ↔ Q 26 | 4 | 0.500 |
| D | Q 21 ↔ Q 37 | 5 | 0.200 |

- mean(B,C,D) = 0.333; observed diff = +0.024 (mean_alt − Q6 = +0.024 — sign WRONG).
- Permutation p (one-sided, locked direction) = **0.5597**.
- Cells passing direction (d(alt) < d(Q6)): 2 / 3 (Q 11 closer at 0.300 < 0.321; Q 37 closer at 0.200 < 0.321; Q 26 farther at 0.500).

### Verdict
**NULL**. The pre-committed direction (Q 21 closer to {Q 11, Q 26, Q 37} than to Q 6) FAILS in aggregate — Q 26's distance (0.500) more than offsets the closeness of Q 11 and Q 37, producing a mean *farther* than Q 6. The permutation null gives p = 0.56 (no signal on this side). Sign is wrong.

### Honest interpretation
Q 21's prophet-order is not closer to other narrative-cycle surahs in aggregate. Q 21 (Mūsā/Hārūn → Ibrāhīm → Lūṭ → Isḥāq/Yaʿqūb → Nūḥ → Dāwūd/Sulaymān → Ayyūb → Ismāʿīl/Idrīs → Zakariyyā/Yaḥyā) is actually mid-distance between Q 6 (chronological-genealogical: Ibrāhīm-line first, then Mūsā) and the other narrative cycles. Q 21 has its own ordering template — closest to Q 37 (d=0.200, both sub-narrative-block) and Q 11 (d=0.300, also narrative) — but Q 26 is far (d=0.500), and these cancel out the locked aggregate direction.

The substantive content claim (Q 21 has its own template) is not falsified, but the strict pre-committed test is NULL.

## Q021-F-03 — True-isolate lexical dispersion (CONFIRMED)

### Pre-reg
- File: `Q021-F-03-isolation-prereg.md`
- SHA256: `16d48c7847fcb704f6588ce04df6239df227c529b1608616d1ca283bdee27587`
- Direction (locked): Q 21's mean-d-to-5-nearest > corpus median (HIGHER = more isolated).

### Method
H-NEW-111 pipeline (QAC v0.4 STEM roots, top-K=500, Dirichlet α=0.5, L1-normalize, Fisher-Rao). Per-surah mean distance to 5 nearest neighbors. Rank Q 21.

### Result
- **Q 21 mean-d-to-5-nearest = 0.8338** (corpus median = 0.7519).
- **Q 21 isolation rank: 18 / 114** (85th percentile — top 16% most isolated).
- Q 21's 5 nearest neighbors: **Q 7 al-Aʿrāf (d=0.806), Q 23 al-Muʾminūn (d=0.821), Q 29 al-ʿAnkabūt (d=0.832), Q 43 al-Zukhruf (d=0.846), Q 36 Yā-Sīn (d=0.864)**.
- Corpus mean = 0.7642, corpus median = 0.7519. Q 21 sits 1.13 standard-deviations above mean.

### True-isolate cluster ranks (the 5 H-NEW-126 surahs)

| Surah | Mean-d-to-5-nearest | Isolation rank |
|:--|:--:|:--:|
| Q 16 al-Naḥl | 0.7424 | 60 / 114 |
| **Q 21 al-Anbiyāʾ** | **0.8338** | **18 / 114** |
| Q 22 al-Ḥajj | 0.7702 | 38 / 114 |
| Q 23 al-Muʾminūn | 0.7937 | 32 / 114 |
| Q 25 al-Furqān | 0.8113 | 25 / 114 |

Within the 5 true-isolates, **Q 21 is the MOST isolated** by FR-roots-mean-d-to-5-nearest. The H-NEW-126 cluster-invariance label is independently corroborated by the FR-distance metric.

### Verdict
**CONFIRMED**. Q 21 is rank 18 / 114 (top-16% most isolated) on the locked metric. Direction matched. Bonferroni k=1 passed at α=0.05 (top-30 → CONFIRMED bracket).

### Bonferroni
k=1; this is the strict-success bracket (top-30).

### Honest limits
- The CONFIRMED bracket of "top-30" is operationally defined; rank 18 is comfortably inside but the cutoff is a methodological choice.
- Other isolation metrics (max-similarity, sum-of-TSP-costs, char-4-gram-NCD) might shift Q 21 by several ranks. The pre-reg locked the FR-roots-mean-d-to-5-nearest specifically.
- 4 of Q 21's 5 nearest neighbors (Q 7, Q 23, Q 29, Q 43) are themselves prophet-narrative or narrative-rich surahs. The "isolation" measure picks up Q 21's signature because its prophet-narrative-density is unusually high relative to most non-narrative surahs in the corpus.

## Q021-F-04 — Cosmological-cluster cohesion (NULL/DIRECTIONAL-borderline)

### Pre-reg
- File: `Q021-F-04-cosmological-cluster-prereg.md`
- SHA256: `849143dd5a63399a9deb1f1782ae90fa7ba340267d8b0276f5389e4d9ce1c4cc`
- Direction (locked): mean pairwise cosine of vv. 30-33 > permutation null.

### Method
QAC v0.4 STEM-root vectors per verse. Mean pairwise cosine (6 pairs) over Q 21:30-33. Permutation null A: 10 000 random contiguous 4-verse blocks. Permutation null B: 10 000 random non-contiguous 4-verse samples.

### Result
- Observed sim = **0.1410**.
- Contiguous-null mean = ~0.124 (median ≈ same); **p (one-sided) = 0.1274**.
- Non-contiguous-null mean = ~0.094; **p (one-sided) = 0.0564**.

### Verdict
**NULL** (per strict pre-reg). The contiguous-null p = 0.127 fails the α = 0.05 (and 0.10) thresholds. The non-contiguous null p = 0.056 is just-above α = 0.05, meeting the DIRECTIONAL-borderline criterion specified in the pre-reg.

### Honest interpretation
Q 21:30-33 is **not significantly more cohesive than typical 4-verse blocks elsewhere in Q 21**. The al-Biqāʿī claim that vv. 30-33 form a *naẓm*-coherent cosmological unit is not falsified at the QAC-roots level — but it is also not strongly empirically distinct. Two readings:
1. The cosmological cluster is real but subtle (the al-Biqāʿī reading captures *thematic* coherence not purely *root-vocabulary* coherence). The non-contig p = 0.056 hints at this.
2. Q 21 has multiple internally-cohesive 4-verse blocks (e.g., the prophet-cycle individual-prophet sub-blocks vv. 78-82 Dāwūd-Sulaymān, vv. 89-90 Zakariyyā-Yaḥyā), making the cosmological cluster not uniquely tight.

The CONFIRMED reading is unsupported. The DIRECTIONAL-borderline reading (non-contig only) is honest.

### Bonferroni
k=1; α=0.05; both p-values fail.

## Q021-F-05 — Q21+Q22 true-isolate adjacency (NULL — NEAR-NEIGHBOR-BUT-NOT-CLUSTER)

### Pre-reg
- File: `Q021-F-05-true-isolate-adjacency-prereg.md`
- SHA256: `303446650a70ae0dbad6e03200139e8a421a29dd7ee13cd6e5753a124511ad66`
- Cell A (locked): rank of d(Q21,Q22) within 10 within-cluster pairs is LOW (top-half).
- Cell B (locked): TSP-cost rank is HIGH (already-observed at rank 16/113).

### Method
- Cell A: Pairwise FR-distance among {Q 16, 21, 22, 23, 25}; rank Q 21–Q 22 within 10 pairs.
- Cell B: Q 21–Q 22 fraction_residual rank from H-NEW-720.

### Result

#### Within-cluster pairwise FR-distances (sorted ascending = low rank → most similar):

| Rank | Pair | FR-distance |
|:-:|:-:|:-:|
| 1 | (Q 16, Q 22) | 0.7544 |
| 2 | (Q 16, Q 23) | 0.7659 |
| 3 | (Q 22, Q 23) | 0.7791 |
| 4 | (Q 16, Q 25) | 0.7964 |
| 5 | (Q 23, Q 25) | 0.8076 |
| 6 | (Q 22, Q 25) | 0.8129 |
| 7 | (Q 16, Q 21) | 0.8458 |
| 8 | (Q 21, Q 25) | 0.8745 |
| 9 | (Q 21, Q 23) | 0.8208 |
| **10** | **(Q 21, Q 22)** | **0.9592** |

⭐ Q 21–Q 22 is **the MOST-DISTANT pair** within the 5-surah true-isolate cluster (rank 10/10).

- Cell A: rank 10 (BOTTOM, not top) → **FAIL** (locked direction was LOW).
- Cell B: TSP rank 16/113, fraction_residual 2.14% → **PASS** (HIGH-COST direction confirmed).

#### Joint interpretation
- Cell A FAILS, Cell B PASSES → **NEAR-NEIGHBOR-BUT-NOT-CLUSTER**.

### Verdict
**NULL — NEAR-NEIGHBOR-BUT-NOT-CLUSTER**. The Q 21–Q 22 mushaf-adjacency is **structurally INCOHERENT internally to the true-isolate cluster**: Q 21 and Q 22 are mushaf-adjacent (mushaf positions 21, 22) but FR-roots-far-apart (d=0.959, the cluster's farthest pair). The other 9 within-cluster pairs are FR-closer; in particular, Q 16 ↔ Q 22 (mushaf gap 6) is the cluster's FR-closest pair (d=0.754).

⭐ This is a **structurally surprising finding**: the true-isolate cluster {Q 16, 21, 22, 23, 25} is unified at the H-NEW-126 cluster-invariance level (no clustering system catches them) but UNGLUED at the FR-roots-pairwise-distance level — and specifically, the only mushaf-adjacent pair within the cluster (Q 21–Q 22) is the cluster's MOST-distant pair. This means the true-isolate label is genuinely about *unique-each*, not about *internally-coherent-cluster*.

### Bonferroni
k=2, α=0.025. Cell A fails the locked direction with the maximum-possible adverse rank (10/10). Cell B was pre-observed (disclosed in pre-reg §2) and is treated under MW-7 single-test α=0.05 with no Bonferroni penalty.

### Honest interpretation
- The true-isolate {Q 16, 21, 22, 23, 25} cluster is a **set of 5 sui-generis surahs**, not a *coherent sub-cluster*. The H-NEW-126 cluster-invariance label is a NULL-on-clustering, not a positive-cohesion claim.
- The Q 21–Q 22 expensive boundary (rank 16/113) makes architectural sense: the mushaf pays the cost of placing two FR-distant prophet-cycle vs hajj-pilgrimage surahs adjacently. This is a *deliberate structural choice* in the canonical ordering, not a *coincidence of two near-isolates being near each other*.
- Within-cluster, the FR-CLOSEST true-isolate pair is Q 16 ↔ Q 22 (al-Naḥl ↔ al-Ḥajj), which are 6 surahs apart in the mushaf. This suggests the true-isolate cluster is a *thematic* cluster (broadly: comprehensive-civilizational-overview surahs) that the mushaf does NOT physically place together.

## Cross-finding-strength assessment

| Test | Verdict | Strength |
|:--|:--:|:--|
| Q021-F-01 prophet-completeness | NULL/PRE-COMMIT-VIOLATION | Q 21 = rank 2/114 (Q 6 = 16, Q 21 = 14) |
| Q021-F-02 prophet-order-template | NULL | sign wrong, p = 0.56 |
| Q021-F-03 lexical-isolation | **CONFIRMED** | rank 18/114, 85th percentile |
| Q021-F-04 cosmological-cluster | NULL (borderline non-contig) | p_contig=0.127, p_non_contig=0.056 |
| Q021-F-05 Q21+Q22 adjacency | NULL — NEAR-NEIGHBOR-BUT-NOT-CLUSTER | Q21-Q22 is rank 10/10 (FARTHEST) within true-isolate cluster |

**1 of 5 tests CONFIRMED; 4 NULL.** The 4 NULLs are all *informative* — they refine our understanding of Q 21 in a structurally meaningful way:
- F-01 NULL refines: Q 21 is the *narrative-form* prophet-cycle MAX (Q 6 is the *list-form* MAX).
- F-02 NULL refines: Q 21's prophet-order is NOT a unified "narrative-cycle" template; it has its own ordering.
- F-04 NULL refines: the cosmological cluster vv. 30-33 has thematic but not lexical-root distinctness.
- F-05 NULL refines: the true-isolate cluster is *cluster-invariant* but NOT *FR-coherent*; Q 21-Q 22 is its *most-distant* pair.

The single CONFIRMED test (F-03) directly corroborates H-NEW-126: Q 21's true-isolate label has an empirical FR-distance signature.

## Cross-references

- `01-empirical-profile.md` (architectural metrics: UAS rank 16, Δ%ile −5.71, sig_A −1.865).
- `02-content-analysis.md` (the 6-block content structure; the 14-prophet catalog at vv. 48-91).
- `03-tafsir-survey.md` §6, §10 (the prophet-catalog and Q 21:30 cosmological-iʿjāz classical claims).
- `05-classical-claims-audit.md` (audit of the al-Bāqillānī Q 21:30 cosmological-iʿjāz claim and the al-Biqāʿī 4-verse cluster claim).
- All 5 pre-reg files in `surahs/Q021-al-anbiya/Q021-F-NN-*-prereg.md`.
- All 5 scripts in `surahs/scripts/Q021_F_NN_*.py`.
- All 5 outputs in `surahs/Q021-al-anbiya/csv/Q021-F-NN.json`.
- [[h-new-126|H-NEW-126]] true-isolate finding (corroborated by F-03; refined by F-05).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] Q 21-Q 22 rank 16/113.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — Q 21 fits the *Structural-twin-pair-of-one* sui-generis tail.

## NULL-headline

⭐ The single most-important Q 21 finding is the F-05 NULL: **the true-isolate cluster {Q 16, 21, 22, 23, 25} is invariant-to-clustering but NOT FR-coherent; the only mushaf-adjacent pair within it (Q 21-Q 22) is the cluster's MOST-distant FR pair.** This refines the H-NEW-126 finding from "true-isolate = unified-novel-class" to "true-isolate = each-sui-generis". Q 21's structural position in the Quran is therefore: a NARRATIVE-form prophet-cycle peak (F-01 NULL → narrative MAX), lexically isolated (F-03 CONFIRMED), placed mushaf-adjacent to its FR-most-distant cluster-mate (F-05). The mushaf pays a top-15 TSP-cost to do this.
