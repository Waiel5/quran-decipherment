---
id: H-NEW-910
title: "Alif-8 cluster cohesion test — 0 of 5 PASSED Bonferroni-5; H3 chronology REVERSED (PRE-COMMIT VIOLATION → published as NULL); H4+H5 DIRECTIONAL; H5 rhyme-axis is the cluster definition itself; alif-monorhyme is a SURFACE rāwī feature, not a deep architectural cluster"
phase: B+
status: 5 pre-registered cells, all reported with full prominence — 0 PASSED at α_bon=0.01; H3 direction REVERSED; H4 + H5 DIRECTIONAL only; sub-cluster {Q 76, 87, 91, 92} (mushaf tail) IS architecturally cohesive (post-hoc, capped α=0.05); comparator-16 BREAKS cohesion
date: 2026-04-28
prereg: h-new-910-alif8-cluster-prereg.md
prereg_sha256: d3f08bada8705b2654810c0ffb89fc51de6970f7f22916e56dc1de6266f84fb9
script: scripts/h_new_910_alif8_cluster.py
json: findings/phase-b-hypotheses/csv/h-new-910-alif8-cluster.json
seed: 20260428
n_perms: 10000
bonferroni_k: 5
alpha_bon: 0.01
parent_finding: Q033-F-01 (the FALSIFICATION of "Q 33 corpus-MAX alif-monorhyme")
methodological_parent: H-NEW-600 (letter-family cohesion permutation null template)
verdict: NULL CLUSTER (with rules-tuple-fragile and tail-sub-cluster nuances) — alif-monorhyme is a SURFACE phonological feature, not a deep architectural cluster; the architecture lives in the mufaṣṣal-qiṣār TAIL sub-cluster, not in the full 8
---

# H-NEW-910 — The 100% alif-final-letter 8-surah cluster: cohesion audit


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline (NULL prominence equal to PASS prominence)

> **Alif-monorhyme is a SURFACE rāwī feature, not a deep architectural cluster.**

The 8 surahs at literal 100% alif-final-letter under the locked rules-tuple — `S = {Q 18 al-Kahf, Q 48 al-Fatḥ, Q 65 al-Ṭalāq, Q 72 al-Jinn, Q 76 al-Insān, Q 87 al-Aʿlā, Q 91 al-Shams, Q 92 al-Layl}` — fail to cohere on FR-roots, on verse-count distribution (perm p=39.03%), and on al-Suyūṭī revelation order. They show only DIRECTIONAL signal on mushaf-position cohesion (pct=10.00%) and on a 4-axis composite (pct=9.18%). At Bonferroni-5 α=0.01: **0 of 5 cells PASSED**.

A pre-commit violation must be flagged: H3 chronology direction REVERSED — the cluster is *more* chronologically dispersed than random (effect z = +1.685, pct = 96.63% in the LESS-than direction). Per Protocol §1.8, this is published as NULL with explicit pre-commit-violation flag.

The architecture that DOES emerge — entirely post-hoc and α=0.05-ceiling capped per [[INVESTIGATION-PROTOCOL|MW-7]] — is in a SUB-CLUSTER: `{Q 76, Q 87, Q 91, Q 92}` (the four mufaṣṣal-qiṣār-tail members of the alif-8). They cohere on FR-roots at pct=2.15% and on mushaf-position at pct=0.80%. This is the [[h-new-700-phonological-compression-tail|H-NEW-700]] terminal-qiṣār region asserting itself again — independently re-discovered via the alif-rāwī cut.

The full alif-8 is therefore **two clusters glued together by rāwī alone**: (a) a mid-mushaf medinan/late-Meccan group {Q 18, 48, 65, 72} that does NOT cohere, and (b) a mufaṣṣal-qiṣār tail {Q 76, 87, 91, 92} that DOES cohere — but for reasons orthogonal to the alif-rāwī (i.e., the [[h-new-660-compression-tail-gradient|compression-tail]] / [[h-new-700-phonological-compression-tail|dispersion-tail]] mufaṣṣal-qiṣār architecture, already documented).

## 2. Pre-registered claims (locked, SHA256-verified at runtime)

Pre-reg SHA: `d3f08bada8705b2654810c0ffb89fc51de6970f7f22916e56dc1de6266f84fb9`. Verified at runtime by `scripts/h_new_910_alif8_cluster.py` line 33.

| ID | Hypothesis | Direction LOCKED | α_bon | Test |
|:-:|:--|:--|:-:|:--|
| **H1** | Within-cluster mean FR-roots distance LESS than random-8 baseline | LESS | 0.01 | 10000-perm null on h-new-111 D-matrix |
| **H2** | Verse-count distribution concentrates short-medium ([1-50] ≥ 6/8) and chi² rejects baseline | concentrated short-medium | 0.01 | chi² + 10000-perm null |
| **H3** | Within-cluster mean rev-order distance LESS than random | LESS | 0.01 | 10000-perm null on al-Suyūṭī chronology |
| **H4** | Within-cluster mean mushaf-pos distance LESS than random | LESS | 0.01 | 10000-perm null on positions 1..114 |
| **H5** | 4-axis (content / rhyme / phoneme / verse-len) z-summed within-cluster mean LESS than random | LESS | 0.01 | 10000-perm null, single composite cell |

Family-α: Bonferroni-5 → **α_bon = 0.01**. Single-cell DIRECTIONAL gate: ≤ 16.67%.

## 3. Methodology

### 3.1 Cluster definition (rules-tuple)

`(min-tashkeel, orthographic-token, last-letter-of-verse-after-stripping-final-pause-mark, alif-set = {ا, آ, أ, إ, ى, ٰ}, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

Inherited from [[Q033-al-ahzab/preregs/Q033-F-01-alif-monorhyme-prereg|Q033-F-01]]. The dagger-alif `ٰ` (U+0670) is included in the alif-set because the verse-final ـٰ in surahs like Q 87 (الأَعْلَى) and Q 92 (تَجَلَّى) realizes phonologically as alif. Re-derivation script line 134 (`verify_cluster()`) confirms cluster membership at runtime; abort if mismatched.

**Re-derived cluster (this run)**: `[18, 48, 65, 72, 76, 87, 91, 92]` ✓ matches canonical.

### 3.2 Statistic per H_n

- **H1**: d̄_FR(S) = (1/28) Σ FR(s_i, s_j) over C(8,2) pairs from `h-new-111.json::D_matrix_upper_triangular`.
- **H2**: chi² goodness-of-fit on verse-count buckets `{[1-20], [21-50], [51-100], [101-200], [201+]}`; null = 10000 random-8 chi² draws.
- **H3**: d̄_rev(S) = (1/28) Σ |rev(s_i) − rev(s_j)| over pairs.
- **H4**: d̄_mushaf(S) = (1/28) Σ |s_i − s_j|.
- **H5**: composite = Σ_{axis ∈ {content, rhyme, phoneme, verse-len}} (within-cluster mean pairwise |Δ| / corpus_std_axis).

Per-surah axis values:
- **content**: mean FR-distance from surah s to all other 113 surahs (centroid-distance proxy from h-new-111).
- **rhyme**: Shannon entropy of last-letter distribution under min-tashkeel (=0 for all 8 cluster surahs by construction).
- **phoneme**: (emphatic + pharyngeal + sibilant + glottal) / total non-tashkeel chars under full-tashkeel.
- **verse-len**: mean words-per-verse under no-tashkeel.

### 3.3 Permutations

Seed = `20260428`. n_perms = 10000 per cell. Sub-seeds: H1=SEED, H2=SEED+2, H3=SEED+3, H4=SEED+4, H5=SEED+5/+6, sub-cluster=SEED+7/+8, comparator-16=SEED+16/17/18.

## 4. Results table (all 5, full prominence regardless of outcome)

| H_n | Test | Observed | Null mean | Null std | Effect z | Percentile | α_bon=0.01 | Verdict |
|:-:|:--|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| **H1** | FR-roots cohesion | 0.8850 | 0.9089 | 0.0476 | **−0.502** | 25.55% | FAIL | **NULL** |
| **H2** | Verse-count chi² (buckets [3,4,0,1,0]) | χ²=4.016 | (perm) | — | — | perm-p=39.03% | FAIL | **NULL** *(direction satisfied: 7/8 short-medium)* |
| **H3** | Chronology cohesion | 50.57 | 38.16 | 7.36 | **+1.685** | **96.63%** | FAIL | **NULL — PRE-COMMIT VIOLATION (direction REVERSED)** |
| **H4** | Mushaf-position cohesion | 28.68 | 38.05 | 6.99 | −1.340 | **10.00%** | FAIL | **DIRECTIONAL** (sub-α 16.67%) |
| **H5** | 4-axis composite | 3.738 | 4.524 | 0.589 | −1.335 | **9.18%** | FAIL | **DIRECTIONAL** (sub-α 16.67%) |

**Family verdict** (Bonferroni-5 at α_bon = 0.01): **0 PASSED**. **NULL CLUSTER**.

### 4.1 H5 per-axis decomposition (transparency, not a separate Bonferroni cell)

| Axis | Within-cluster mean |Δ| | Percentile in random-8 null | Note |
|:--|:-:|:-:|:--|
| content (FR-centroid distance) | 0.1036 | 30.83% | NULL — cluster surahs have heterogeneous content profiles |
| **rhyme** (Shannon entropy of last-letter) | 0.3216 | **0.07%** | **TRIVIALLY EXTREME** — the cluster is DEFINED by rhyme uniformity (entropy=0 for all 8 by construction); this percentile is not informative |
| phoneme (emph+phar+sib+glot density) | 0.0194 | 31.18% | NULL — cluster has heterogeneous phoneme profiles |
| verse-len (words/verse) | 10.0153 | 91.19% | **REVERSED** — cluster has MORE verse-length variance than random |

The rhyme percentile of 0.07% is a **methodological artifact**: the cluster is defined as the set of surahs whose rhyme entropy is 0, so naturally any random-8 sample has a higher within-cluster |Δ_rhyme|. This is exactly the [[h-new-600-letter-families|H-NEW-600]] §6 warning: when the cluster is selected on a feature, that feature's cohesion is mechanically inflated.

The interesting axes are the OTHER three (content, phoneme, verse-len), all of which are NULL or REVERSED. **Strip away the rhyme axis (which built the cluster) and the alif-8 has no architectural signature.**

## 5. Interpretation

### 5.1 What we asked vs. what we found

We pre-registered five tests asking whether the alif-monorhyme rāwī tracks deeper architectural features. The five-cell answer:

- The rāwī does NOT track FR-roots content distribution.
- The rāwī does NOT track verse-count concentration at chi²-significant levels (though direction is satisfied — 7/8 are in short-medium buckets, vs. 4.71/8 expected; this is a real but sub-significant lean).
- The rāwī ANTI-tracks chronology — the alif-rāwī surahs span the full revelation period (rev-orders 8, 9, 26, 40, 69, 98, 99, 111) and are MORE dispersed than random (effect z = +1.685, pct 96.63%). The pre-committed direction is reversed; per Protocol §1.8, this is honestly NULL.
- The rāwī tracks mushaf-position weakly (pct 10.00%, sub-α directional but not Bonferroni-passing).
- The rāwī tracks the 4-axis composite weakly (pct 9.18%) but ONLY because the rhyme axis was built into the cluster.

### 5.2 What does the alif-cluster ENCODE?

**Nothing the rāwī itself doesn't already say.** Under our 5-cell pre-registered audit, the alif-monorhyme is a phonological surface form. It is the same phenomenon as the pre-Islamic alif-monorhyme *qaṣīda* (Labid, ʿAmr b. Kulthūm — 0.9888 and 0.9810 alif-rate, per [[Q033-al-ahzab/06-novel-findings|Q033-F-01]] poetry control). The Quran has 8 surahs that adopt this form, distributed across all chronological periods (early Meccan Q 87/91/92, mid-Meccan Q 72/18, Medinan Q 76/65/48), all length classes (12 verses to 110 verses), and all content registers (eschatology Q 92, oath-section Q 91, eulogy Q 18, divorce-law Q 65).

**The classical-tradition framing is correct**: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 56 (on *al-fawāṣil*) treats the alif as one of multiple *rawiyy* options across the corpus, NOT as a structural-cluster signature. This pre-reg empirically vindicates al-Suyūṭī's conservative non-attribution of meaning to rāwī choice at the cohesion level.

### 5.3 What the post-hoc tail-sub-cluster IS encoding

When we restrict to `{Q 76, Q 87, Q 91, Q 92}` — the four alif-cluster members in the mufaṣṣal-qiṣār region (mushaf ≥ 75) — we find:

- **FR-roots cohesion**: pct = 2.15% (would PASS Bonferroni-5 if pre-registered)
- **Mushaf-position cohesion**: pct = 0.80% (very tight — they sit at 76, 87, 91, 92)

This sub-cluster is **NOT a finding about the alif-rāwī**. It is a re-discovery of the [[h-new-660-compression-tail-gradient|compression-tail]] / [[h-new-700-phonological-compression-tail|dispersion-tail]] / [[cross-finding-026-iʿjāz-architecture|iʿjāz architecture]] terminus, found via the alif-rāwī cut. Per [[INVESTIGATION-PROTOCOL|Protocol §1.7 (MW-7)]], post-hoc finds carry single-test α=0.05 ceiling — at that ceiling, the tail-sub-cluster is DIRECTIONAL but not law-strength.

### 5.4 Comparator-16 (post-hoc, capped α=0.05)

Adding the next 4 highest-alif surahs `{Q 33 (0.9863), Q 20 (0.9852), Q 17 (0.9820), Q 25 (0.9740)}` to make a 12-surah set (we sought 8 but only 4 surahs sit in [0.97, 0.99999), so the comparator is 12 not 16):

| Test | 12-surah observed | Percentile |
|:--|:-:|:-:|
| FR-roots | 0.9749 | 86.84% (worse than null mean) |
| Chronology | 42.17 | 79.72% |
| Mushaf | 35.45 | 24.83% |

Adding Q 17, Q 20, Q 25, Q 33 — long Meccan narrative surahs heavy with prophet-stories — DEGRADES every cohesion measure. This confirms: the alif-rāwī is not even WEAKLY a content-marker; the long-narrative alif-rāwī surahs (Q 17, 18, 20, 25, 33) are content-heterogeneous as a class.

### 5.5 Rules-tuple sensitivity (post-hoc)

| Variant | Cluster at 100% | Match canonical 8? |
|:--|:--|:-:|
| `(min-tashkeel, alif-set incl. dagger-alif ٰ)` (canonical) | {18, 48, 65, 72, 76, 87, 91, 92} | ✓ |
| `(min-tashkeel, alif-set EXCL. dagger-alif)` | {18, 48, 72, 76, 91} | ✗ — drops Q 65, 87, 92 |
| `(no-tashkeel text, alif-set incl. dagger-alif)` | {18, 48, 65, 72, 76, 87, 91, 92} | ✓ |

The 100%-claim is **rules-tuple-FRAGILE under one orthographic variant**: if dagger-alif `ٰ` is excluded (treated as a tashkeel mark rather than alif-realization), the cluster shrinks to 5: `{Q 18, Q 48, Q 72, Q 76, Q 91}`. The dropped surahs all end on dagger-alif rather than full alif: Q 65 (e.g., *إِلَّا اللَّهَ*; verse-finals on dagger-alif sequences), Q 87 (titled *al-Aʿlā* with verse-finals تَجَلَّى-pattern), Q 92 (similar dagger-alif endings).

The rules-tuple-fragility is **phonologically defensible**: the verse-final ـٰ realizes as a long alif sound in recitation, even when written with the dagger mark. Both inclusion and exclusion of ٰ can be argued. We honestly report both.

### 5.6 Comparison to [[h-new-600-letter-families|H-NEW-600]] template

| Cluster | Selection feature | FR-roots %ile | Verdict |
|:--|:--|:-:|:--|
| ALM-6 (h-new-600) | shared muqaṭṭaʿāt opener | 43.15% | NULL — letter-axis ⊥ content |
| ALR-5 (h-new-600) | shared muqaṭṭaʿāt opener | 56.25% | NULL — letter-axis ⊥ content |
| **alif-8 (h-new-910)** | **shared verse-final letter (rāwī)** | **25.55%** | **NULL — rāwī-axis ⊥ content** |

H-NEW-910 generalizes the H-NEW-600 finding: **letter-level structural features (whether muqaṭṭaʿāt openers or rhyme rāwī) are EMPIRICALLY ORTHOGONAL to whole-surah FR-roots content distribution.** This is consistent with the [[cross-finding-026-iʿjāz-architecture|iʿjāz anti-twin]] result r(content × rhyme) = −0.86 at the window-d̄ level — letter-level and content-level operate on independent axes.

## 6. NULL prominence statement

Per [[INVESTIGATION-PROTOCOL|Protocol §1.3]], NULL findings carry equal prominence to confirmations. The headline of H-NEW-910 is **NULL**:

> The 8-surah 100% alif-final cluster does NOT cohere on any of the 5 pre-registered architectural dimensions at Bonferroni-5 α=0.01. Alif-monorhyme is a SURFACE rāwī feature — a phonological choice — not a marker of deep content/length/chronology/mushaf/4-axis architecture. The classical scholars who treated rāwī choice as poetic-formal rather than structural-thematic (al-Suyūṭī *Itqān* nawʿ 56; al-Bāqillānī *Iʿjāz* §6 on *fawāṣil*-variety) are empirically vindicated.

Direction-violation transparency: H3 chronology was pre-committed with direction LESS-than-null. The observed direction is GREATER-than-null at z = +1.685 (pct 96.63% in the LESS-than direction; equivalently, pct 3.37% in the GREATER-than direction). Per Protocol §1.8, this is published as NULL with explicit pre-commit-violation flag. We do NOT re-frame as "the cluster is chronologically dispersed" — that would be post-hoc direction-flipping. We honestly report: pre-committed direction failed.

## 7. Cross-references and Obsidian wikilinks

- [[Q033-al-ahzab/06-novel-findings|Q033-F-01]] — the FALSIFICATION that surfaced this 8-surah cluster.
- [[Q017-al-isra/06-novel-findings|Q017-F-01]] — Q 17 alif-rate=0.9910 (rules-tuple-discrepancy with this run's 0.9820 logged below).
- [[h-new-600-letter-families|H-NEW-600]] — the methodological parent (letter-cluster cohesion permutation null template).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — the compression-tail law that explains the post-hoc tail-sub-cluster.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — rhyme/phoneme dispersion-tail; complementary axis on which alif-8 is trivially extreme by construction.
- [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] — the iʿjāz anti-twin r=−0.86 that this NULL is fully consistent with.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — the synthesis frame the NULL slots into.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rankings: cluster members have UAS ranks 7 (Q 18), 50ish (Q 48), low (Q 65, 72, 76, 87, 91, 92). Heterogeneous UAS → consistent with H1 NULL.

### 7.1 Classical-source citations

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 56 (*fī al-fawāṣil wa-aqsāmihā*) — treats *rawiyy* alif as one option among many; does NOT claim alif-rāwī surahs share content. **Empirically vindicated.**
- al-Bāqillānī, *Iʿjāz al-Qurʾān*, §6 on *fawāṣil* variety — the Quran's iʿjāz is in REFUSING single-rāwī uniformity globally, not in the local rāwī choice. **Empirically vindicated** by H1 NULL on alif-cluster coherence.
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, *nawʿ* 38 — mufaṣṣal sub-tier classification (ṭiwāl / awsāṭ / qiṣār) places Q 76, 87, 91, 92 in the qiṣār tier, Q 65, 72 in awsāṭ, Q 48 in ṭiwāl-edge, Q 18 outside mufaṣṣal entirely. The cluster spans 4 of al-Zarkashī's structural tiers. **Empirically vindicated** by H4 not-quite-passing.
- Pre-Islamic: Labid b. Rabīʿa, *Muʿallaqa* (alif-monorhyme, 0.9888); ʿAmr b. Kulthūm *Muʿallaqa* (alif-monorhyme, 0.9810). Per Q033-F-01 cross-corpus control, alif-monorhyme is a Jāhilī *qaṣīda* form. The Quran's adoption of the form in 8 surahs is consistent with the form being a recognized Arabic poetic convention, not a corpus-internal architectural marker.

### 7.2 H-NEW-910 contributes to:

- The MW-1..MW-7 protections sequence: H-NEW-910 is a MW-6 instrument-control on the alif-rāwī axis (analogous to how H-NEW-600 was MW-6 on the muqaṭṭaʿāt axis).
- The "letter-axis ⊥ content-axis" generalization: now confirmed across muqaṭṭaʿāt openers (H-NEW-600), full-29 (H-NEW-570), HM-7 (H-NEW-570), AND rhyme rāwī (H-NEW-910).

## 8. Honest limits and DATA-GAPS

- **Q 17 rules-tuple discrepancy**: our re-derivation gives Q 17 alif-rate = 0.9820 (109/111). [[Q017-al-isra/06-novel-findings|Q017-F-01]] reports 0.9910 (110/111). The difference is one verse — likely Q 17:108 ending in a hamza-on-yāʾ (ـئاً) treated as alif by one rule and not the other. We do NOT use Q 17 in the canonical 8-cluster (both runs agree it falls below 1.0); the cluster is rock-solid. The Q 17 discrepancy is flagged as a follow-up rules-tuple alignment task.
- **H5 axis selection is partly post-hoc within the pre-reg**: we declared "4 axes" pre-registration but could not fully specify the per-surah axis values from existing artifacts. The Shannon-entropy-of-last-letter rhyme axis is mechanically extreme by cluster construction; we report this and exclude it interpretively. A cleaner pre-reg would have used d̄_rhyme(window) from h-new-700 rather than per-surah entropy.
- **Verse-count buckets [1-20], [21-50], [51-100], [101-200], [201+] were pre-locked** before observation, but they are arbitrary. A continuous-distribution test (e.g., KS) might give a different answer. Pre-reg held as written; chi² gave perm-p = 39.03%.
- **Comparator-16 was 12 not 16**: only 4 surahs sit in [0.97, 0.99999) (Q 33 = 0.9863, Q 20 = 0.9852, Q 17 = 0.9820, Q 25 = 0.9740). A larger comparator threshold (≥0.95) would dilute further; the 12-surah comparator unambiguously breaks cohesion.
- **Sub-cluster {Q 76, 87, 91, 92} is post-hoc**: the FR-roots pct=2.15% would PASS Bonferroni-5 if pre-registered, but it is not — it was found by inspection of mushaf-positions. We honestly cap at α=0.05 single-test ceiling per MW-7. Pre-registration of this sub-cluster as a follow-up is recommended.
- **Rules-tuple fragility**: cluster shrinks to 5 if dagger-alif is excluded from alif-set. The 100%-claim is therefore tied to a specific orthographic interpretation. The 5-surah core `{Q 18, 48, 72, 76, 91}` is stable across both rules-tuple variants tested.
- **No tafsir-deep-dive**: this is a CORPUS-cluster pre-reg, not per-surah deep dive. The 8 surahs each warrant independent tafsir survey (al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī) which is out of scope here. **DATA-GAP: surah-level tafsir surveys for Q 48, Q 65, Q 72, Q 76, Q 87, Q 91, Q 92 (Q 18 is in the Wave-D backlog).**
- **No hadith-deep-dive**: especially Q 18 *Sūrat al-Kahf* has heavy Friday-recitation hadith corpus (Muslim #1888, al-Ḥākim, al-Bayhaqī) which is not engaged here. **DATA-GAP**.
- **Phoneme axis used grapheme proxy**: the H5 phoneme density used emphatic/pharyngeal/sibilant/glottal grapheme counts as a phoneme proxy. A proper phoneme analysis would use the IPA-aligned full-tashkeel transliteration. The grapheme proxy is the project default but is admittedly coarse.

## 9. Summary table for ledger

| Item | Value |
|:--|:--|
| ID | H-NEW-910 |
| Cluster (LOCKED) | {Q 18, 48, 65, 72, 76, 87, 91, 92} |
| Pre-reg SHA | `d3f08bada8705b2654810c0ffb89fc51de6970f7f22916e56dc1de6266f84fb9` |
| Bonferroni cells | 5 |
| α_bon | 0.01 |
| Cells PASSED Bon-5 | **0 of 5** |
| Cells DIRECTIONAL | 2 (H4 mushaf, H5 4-axis) |
| Cells NULL | 3 (H1 FR-roots, H2 verse-count, H3 chronology) |
| Pre-commit violations | 1 (H3 chronology direction reversed) |
| Family verdict | **NULL CLUSTER — alif-monorhyme is a SURFACE rāwī feature** |
| Post-hoc sub-cluster {76,87,91,92} | FR pct=2.15%, mushaf pct=0.80% (architecture re-discovered via alif-cut) |
| Comparator-12 | breaks cohesion (FR pct=86.84%) |
| Rules-tuple fragility | cluster shrinks to 5 under no-dagger-alif variant |

## 10. Wikilinks (Obsidian)

[[h-new-910-alif8-cluster-prereg|prereg]] · [[Q033-F-01-alif-monorhyme-prereg|Q033-F-01 prereg]] · [[Q017-F-01-alif-monorhyme-prereg|Q017-F-01 prereg]] · [[h-new-600-letter-families|H-NEW-600]] · [[h-new-660-compression-tail-gradient|H-NEW-660]] · [[h-new-700-phonological-compression-tail|H-NEW-700]] · [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] · [[h-new-840-unified-architectural-score|H-NEW-840]] · [[cross-finding-026-iʿjāz-architecture|CF-026]]

*Bismillāhi al-Raḥmāni al-Raḥīm.*
