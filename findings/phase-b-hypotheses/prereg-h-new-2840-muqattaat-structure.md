---
prereg_id: H-NEW-2840
title: What IS the muqaṭṭaʿāt clustering? — sub-cluster structure, per-family distance, distinguishing vocabulary, singleton placement
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
status: PRE-REGISTRATION — locked before any outcome statistic was computed
parent: H-NEW-2820
method_parent: [H-NEW-2820, H-NEW-2760, H-NEW-2720, H-NEW-2680, H-NEW-2790]
seed_primary: 20260509
seed_replication: 20260519
n_perm_quran: 10000
n_perm_baseline: 2000
n_offsets: 200
tests_in_family: 12
alpha_bonferroni: 0.00416667
novelty_gate: 0.000416667
---

# Pre-registration — H-NEW-2840

## 0. Why this test exists

`H-NEW-2820` established that the muqaṭṭaʿāt sets are **clustered** in root-content space
under a null that holds unit size fixed: the muqaṭṭaʿāt-29 at the **0.45th** percentile
(size-only quintiles) and **5.44th** (size × period), the ḥawāmīm-7 at the **0.05th**
(size-only) and **0.21st** (size × period). That result sat as a published NULL from
2026-05-20 to 2026-08-07 because `h-new-570`'s size-blind null **never once drew a
comparison set of the muqaṭṭaʿāt's size — 0 of 10,000 draws**.

**No description of that clustering's internal structure exists**, because until 2026-08-07
the instrument said there was nothing to describe. This pre-registration locks that
description and the tests that bound it.

**The descriptive characterisation is the deliverable regardless of what any test returns.**
Section 8 states this as a binding commitment: even if every inference in §5 fails, §7's
descriptive outputs are published in full, with the failures stated at equal prominence.

---

## 1. Frozen inputs

Every file below is SHA-256-recorded in the run manifest, in repository-relative form, and
verified at runtime with `SystemExit` on mismatch.

| path | role |
|:--|:--|
| `quran-text/quran-no-tashkeel.json` | corpus |
| `data/morphology/quranic-corpus-morphology-0.4.txt` | QAC STEM root tokens |
| `data/morphology/surah-root-graph.json` | H-NEW-126's per-surah root counts |
| `data/revelation-order.csv` | Nöldeke rank and Meccan/Medinan period |
| `findings/phase-b-hypotheses/csv/h-new-111.json` | the published Fisher-Rao matrix |
| `findings/phase-b-hypotheses/csv/h-new-570.json` | the published percentiles |
| `scripts/h_new_570_muqattaat_content_cluster.py` | the published routine, for the bit-identity assertion |
| `scripts/h_new_126_isolate_core.py` | the published profile routine (channel definitions) |
| `findings/phase-b-hypotheses/scripts/h-new-2680.py` | the partition code, lifted verbatim |
| `data/baseline-corpora/raw/bukhari-noquran.txt` | genre control |
| `data/baseline-corpora/raw/jahiz-hayawan.txt` | genre control |

---

## 2. Instruments — locked

**`D_frozen`** — the 114 × 114 Fisher-Rao angular distance matrix over per-surah root
distributions, read from `csv/h-new-111.json` (top-500 QAC STEM roots, Dirichlet α = 0.5,
L1-normalised, `d = 2·arccos Σ√(p_i q_i)`). This is the matrix `h-new-570` used. **The
harness asserts `mean_pairwise(D_frozen, SET_MUQ) == 0.9388131231527093` to 1 × 10⁻¹² against
the published routine `h_new_570_muqattaat_content_cluster.mean_pairwise`, and exits on
mismatch.** All primary arms use `D_frozen`.

**`D_rebuilt`** — the same matrix recomputed from the QAC file by the h-new-111 recipe.
Used **only** for the ablation arms of §5 R10/R11, and **only** in rebuilt-vs-rebuilt
contrasts. It is never compared against `D_frozen` as though the two were interchangeable.

**`D_surface`** — top-500 **surface word types**, Dirichlet α = 0.5, Fisher-Rao. Used for the
genre control only, because no morphological analyser exists for the baselines. The Qurʾān's
own surface values are computed in the same instrument as the like-for-like reference
(H-NEW-2820 §8.1).

---

## 3. The nuisance channels, and the primary null

### 3.1 Channel, inherited not re-derived

`H-NEW-2820` §2.1 ranked the channels for this exact statistic on the data:
**`log word count` ρ = +0.8998** (dominant), root-set size +0.8554, verse count +0.8395,
mean verse length +0.6509. **That ranking is inherited and `log word count` is locked as the
size channel.** `word count` is `len(real_words(...))` summed over a surah's verses — the
definition `h_new_126_isolate_core.compute_profiles` uses as `total_tokens`, and the one
H-NEW-2820 measured.

The compositional imbalance is already measured (H-NEW-2820 §2): the muqaṭṭaʿāt-29 have
**4.27×** the median word count of the other 85 (Cohen's *d* = 1.26) and are **10.3 %**
Medinan against **29.4 %**.

### 3.2 The primary null — mandatory, and stated as the thing that could kill the finding

> **`N_PERIOD` (PRIMARY).** Permute set membership within strata formed by
> **log-word-count quintiles × Meccan/Medinan period** — 10 strata — taking exactly the
> observed set's occupancy in each stratum. Donor pool = **all 114 surahs**, which is
> `h-new-570`'s own convention and H-NEW-2820's.

**If the structure dies under `N_PERIOD`, the finding is that "the mystery-letter surahs
cluster" reduces to "long Meccan surahs cluster", and it will be reported in exactly those
words.** This is written before the run precisely so it cannot be softened after it.

Estimability was checked before locking (§10): at k = 5 the strata require
{4: 5, 6: 13, 7: 1, 8: 8, 9: 2} donors from pools of {14, 19, 4, 13, 9}. **Estimable.**

Secondary nulls, all pre-registered, all reported whatever they return:

- **`N_SIZE5`** — log-word-count quintiles only (H-NEW-2820's A2-k5 primary).
- **`N_SIZE10`** — log-word-count deciles (UNIT-DRIFT-DEFECT §6.1: *"a stratified permutation
  null must declare its bin width and report at least two"*).
- **`N_PUB`** — the size-blind null, regenerated draw-for-draw with `random.Random(20260520)`,
  for continuity with the published percentile.

**§6.3 rule: where two bin widths disagree, the finer is the honest one and the disagreement
is itself the result.**

---

## 4. The letter-string partitions — locked before any distance was computed

### 4.1 P1 — exact opening string (PRIMARY)

Mechanical, judgment-free: two surahs are in the same class iff their muqaṭṭaʿāt strings are
identical. **14 classes.** This is the literal reading of the question *"do surahs sharing an
opening string sit closer?"*, and it involves no choice of mine.

| class | string | surahs | n |
|:--|:--|:--|--:|
| ALM | الم | 2, 3, 29, 30, 31, 32 | 6 |
| ALMS | المص | 7 | 1 |
| ALR | الر | 10, 11, 12, 14, 15 | 5 |
| ALMR | المر | 13 | 1 |
| KHYAS | كهيعص | 19 | 1 |
| TH | طه | 20 | 1 |
| TSM | طسم | 26, 28 | 2 |
| TS | طس | 27 | 1 |
| YS | يس | 36 | 1 |
| SAD | ص | 38 | 1 |
| HM | حم | 40, 41, 43, 44, 45, 46 | 6 |
| HM-ASQ | حم عسق | 42 | 1 |
| QAF | ق | 50 | 1 |
| NUN | ن | 68 | 1 |

Classes with n ≥ 2: **ALM (6), ALR (5), ṬSM (2), ḤM (6)** — **41 within-class pairs of 406**.

### 4.2 P2 — classical block naming (SECONDARY, registered)

The tradition's own categories, which are externally attested and therefore not my choice,
but which do require two judgments I am declaring here: that Q 27 (طس) joins the
**ṭawāsīn** with Q 26 and Q 28, and that Q 42 (حم عسق) joins the **ḥawāmīm** with Q 40–46.
Both are standard; both are judgments; **P2 is therefore secondary and P1 primary.**

- ALM {2, 3, 29, 30, 31, 32} · ALR {10, 11, 12, 14, 15} · ṬAWĀSĪN {26, 27, 28} ·
  ḤAWĀMĪM {40, 41, 42, 43, 44, 45, 46} · singletons {7, 13, 19, 20, 36, 38, 50, 68}

**49 within-class pairs of 406.** Both partitions are reported in full regardless of outcome.

---

## 5. Registered inferences — 12, with directions locked

Bonferroni α = 0.05 / 12 = **0.00416667**. The project's novelty rule gives the stricter gate
**0.000416667**; with 10,000 permutations the minimum attainable p is
1/(1 + 10000) = 9.999 × 10⁻⁵, which clears it. **Any inference claimed as novel must clear
0.000416667; the Bonferroni bar alone is reported but is not sufficient for a novelty claim.**

`R0` is a reproduction check, not an inference, and is not counted in the family.

| # | question | statistic | **locked direction** | null |
|:--|:--|:--|:--|:--|
| **R0** | reproduction | `d̄(SET_MUQ)` on `D_frozen`; the four H-NEW-2820 matched percentiles | exact / ±1 pp | — |
| **R1** | Q1 one cluster or several | `S1` = max average-silhouette over k ∈ {2,3,4,5} | **observed > null** (more sub-structured) | `N_PERIOD` |
| **R2** | Q2 **PRIMARY** | `Δ = W̄_within − B̄_between`, partition P1 | **Δ < 0** (same string ⇒ closer) | `F1` |
| **R3** | Q2 size-controlled | same `Δ`, partition P1 | **Δ < 0** | `F2` |
| **R4** | Q2 per-family | `d̄` within ALM (n = 6) | **observed < null** (tighter) | `N_PERIOD` at n = 6 |
| **R5** | Q2 per-family | `d̄` within ALR (n = 5) | **observed < null** | `N_PERIOD` at n = 5 |
| **R6** | Q2 per-family | `d̄` within ṬSM (n = 2) | **observed < null** | `N_PERIOD` at n = 2 |
| **R7** | Q2 per-family | `d̄` within ḤM (n = 6) | **observed < null** | `N_PERIOD` at n = 6 |
| **R8** | Q3 vocabulary | `max|z|` over tested roots, weighted log-odds | **observed > null** | `N_PERIOD` |
| **R9** | Q4 singletons | mean matched-centrality percentile, 6 one-off strings vs 23 class members | **TWO-SIDED — not locked** | `N_PERIOD` |
| **R10** | independence | matched percentile of `d̄(SET_MUQ)`, `D_rebuilt` minus {`ktb`, `qrA`} | **stays ≤ 10.0** | `N_PERIOD` |
| **R11** | independence | same, minus {`ktb`, `qrA`, `tlw`, `nzl`, `Ayy`, `*kr`, `wHy`, `frq`} | **stays ≤ 10.0** | `N_PERIOD` |
| **R12** | Q2 secondary partition | `Δ`, partition P2 | **Δ < 0** | `F1` |

### 5.1 Definitions, so the runner cannot drift from the text

**`S1` — average silhouette.** Agglomerative **average-linkage** (UPGMA) on the 29 × 29
submatrix; ties broken by the lowest `(i, j)` index pair. Cut at k ∈ {2, 3, 4, 5}. For point
*i* in cluster *A*: `a(i)` = mean distance to the other members of *A*; `b(i)` = min over
clusters *B* ≠ *A* of the mean distance from *i* to *B*; `s(i) = (b−a)/max(a,b)`, and
**`s(i) = 0` when |A| = 1**. `S1 = max_k mean_i s(i)`. A matched null draw is clustered by the
identical procedure.

**`S2`** (registered distinguishing output, not an inference) `= 1 − W₂/W₁`, where
`W_k = Σ_c Σ_{i<j ∈ c} D_ij / Σ_c C(n_c, 2)` is the pooled mean within-cluster distance at the
k-cut, so `W₁ = d̄`.

**`Δ`, `F1`, `F2`.** `W̄_within` = mean of `D` over the within-class pairs; `B̄_between` = mean
over the remaining pairs of the 29; `Δ = W̄_within − B̄_between`.
**`F1`** permutes the class labels among the 29, preserving the class-size multiset — so
muqaṭṭaʿāt membership and the whole set's size composition are **fixed by construction**.
**`F2`** permutes class labels **within tertiles of log word count computed on the 29** — the
strict arm, and the one that decides R3.

**Per-family nulls R4–R7.** `N_PERIOD` at the family's own n: strata are log-word-count
quintiles × period over the 114, occupancy taken from the family. **If a family's stratum
demand exceeds its donor pool the arm returns `NOT-ESTIMABLE` and no verdict is drawn from
it** — the H-NEW-2820 §2.2b outcome, which is a result and not a failure.

**Adjacency control `FAM-c`** (registered distinguishing output attached to R4–R7, not an
inference). The ḥawāmīm are the consecutive mushaf run 40–46 and the ALM/ALR classes are
partly consecutive; mushaf-adjacent surahs may be close for reasons that have nothing to do
with the letters (H-NEW-111). `FAM-c` compares each family's `d̄` to the `d̄` of **random
contiguous runs of the same length** drawn from the whole mushaf. **A family that does not
beat its own adjacency control is reported as adjacency-explained**, whatever R4–R7 return.

**`R8` — the max-statistic, chosen so multiplicity is handled by construction.** Roots tested:
every QAC STEM root with a corpus-wide count **≥ 20** (threshold locked here; `n_tested`
reported). Per root the Monroe-style weighted log-odds with an informative Dirichlet prior
taken from the whole-corpus root distribution:

```
delta_w = log((y_w^G + a_w) / (n^G + a_0 - y_w^G - a_w))
        - log((y_w^R + a_w) / (n^R + a_0 - y_w^R - a_w))
var_w   = 1/(y_w^G + a_w) + 1/(y_w^R + a_w)
z_w     = delta_w / sqrt(var_w)
```

with `a_0 = 1000` and `a_w = a_0 · p_w^corpus`. The **confirmatory** statistic is
`max_w |z_w|` against its null distribution over matched draws — a single test, exactly
corrected for the number of roots. **The word list itself is a descriptive screen at
Benjamini–Hochberg q = 0.05 and is labelled as such**, never as 700 independent findings.

**`R9` — singleton placement.** `centrality(s)` = mean `D(s, t)` over the other 28.
`pctile_matched(s)` = the percentile of `centrality(s)` among 10,000 substitutes drawn from
*s*'s own log-word-count × period stratum and scored against the same other 28.
**Locked classification:** `INSIDE` if `pctile_matched ≤ 25`; `OUTSIDE` if `≥ 75`;
`INTERMEDIATE` otherwise. `BRIDGE` is a separate, additive label: the surah's three nearest
neighbours within the 29 fall in **two or more different multi-member P1 classes**.
R9's inference is the two-sided comparison of mean `pctile_matched` between the six one-off
strings {19, 20, 36, 38, 50, 68} and the 23 members of multi-member classes.

*(Note declared in advance: Q 7, 13, 27, 42 have one-off exact strings under P1 but belong to
multi-member classes under P2. R9's split follows **P1**, and the P2 split is reported beside
it. The two answers may differ and both will be published.)*

**`R10`/`R11` — ablation.** `D_rebuilt` is recomputed from QAC with the named roots deleted
**before** the top-500 selection, so the vocabulary refills to 500 and the comparison is not
a 498-dimension-versus-500-dimension artefact. The contrast is
`pct(D_rebuilt_full)` versus `pct(D_rebuilt_ablated)` — **both rebuilt**. The Buckwalter root
strings are the QAC ones, verified present before locking: `ktb` 319, `qrA` 88, `tlw` 63,
`nzl` 293, `Ayy` 382, `*kr` 292, `wHy` 78, `frq` 72.

---

## 6. The genre control

The H-NEW-2680 partition code is lifted **verbatim** from the frozen source by the H-NEW-2720
mechanism, with per-fragment SHA-256 checks before `exec` (`AR_DIAC`/`NON_AR` regex block,
`normalise_words`, `build_pseudo_corpus`). Each baseline stream is cut to **the Qurʾān's exact
verse word-length profile** and grouped on **the Qurʾān's exact surah verse counts**, so the
pseudo-group taken at the same 29 slots has identical verse counts, verse lengths and word
counts to the real muqaṭṭaʿāt set, to the token. **Same imbalance, no content mechanism.**
200 offsets per baseline, 2,000 permutations per offset. The Qurʾān's own verses are **never
re-partitioned**; its real verses are the units (H-NEW-2720, and H-NEW-2820 §8.8, whose first
run failed on exactly this).

Computed per offset: `d̄` of the 29 slots and its matched percentile; `Δ` under P1 with `F1`;
`S1` and its matched percentile.

**Registered modifier.** `-GENRE-SHARED` is appended to a verdict if the **median** offset of
**either** baseline reaches a value at least as extreme as the Qurʾān's own value **in the
surface instrument** for that statistic. The fraction of offsets reaching the claim's bar is
reported regardless, because H-NEW-2820 §4.2 found one baseline partition in six clears the
10 % bar — **the bar is loose and the margin is what carries a verdict.**

---

## 7. Descriptive outputs — published unconditionally

Locked here so that no negative test can suppress them.

1. The **average-linkage dendrogram** of the 29, with every merge height.
2. The **k = 2…5 partitions** with membership listed surah by surah.
3. The **29 × 29 distance table** summarised as: each surah's nearest and farthest neighbour
   within the 29, and its nearest neighbour among all 114.
4. **Per-class mean within-class distance** for both P1 and P2, beside the between-class mean
   and beside each class's adjacency control.
5. The **distinguishing-root list** at BH q = 0.05, with actual roots, their glosses, their
   rate in the 29 and in the 85, and their matched-null percentile.
6. The same list for **ḥawāmīm versus the other 22 muqaṭṭaʿāt** (descriptive screen only).
7. **`centrality` and `pctile_matched` for all 29**, with the locked INSIDE/OUTSIDE/BRIDGE
   labels, singletons flagged.

---

## 8. Verdict rules — to be diffed clause-by-clause against the runner before declaring

```
SUB-STRUCTURED        R2 clears alpha_bonferroni under F1
                      AND R3 clears alpha_bonferroni under F2
                      AND at least one of R4-R7 clears alpha_bonferroni
SUB-STRUCTURE-WEAK    R2 clears under F1 but R3 does not clear under F2
NO-SUB-STRUCTURE      R2 does not clear under F1
```

Modifiers, appended in this order:

```
-SIZE-EXPLAINED       R1 clears under N_SIZE5 but NOT under N_PERIOD (the primary)
-GENRE-SHARED         the median offset of either baseline reaches the Quran's own
                      surface-instrument value on Delta (section 6)
-ADJACENCY-EXPLAINED  every family passing R4-R7 fails its own FAM-c adjacency control
```

Independence label, reported separately and never combined with the above:

```
PILLAR1-DISTINCT      R10 AND R11 both keep the matched percentile <= 10.0
PILLAR1-ENTANGLED     either ablation lifts the matched percentile above 10.0
```

> **Binding statement on independence, written before the result.** H-NEW-2760's Pillar 1 and
> this finding are computed on **the same 29 surahs in the same corpus**. Whatever R10/R11
> return, **this finding is not an independent confirmation of Pillar 1 and will not be
> reported as one.** H-NEW-2670 showed that stacking constraints on the same object
> manufactures apparent uniqueness. `PILLAR1-DISTINCT` would mean only that the two results
> do not reduce to the same measurement — not that they multiply.

**The descriptive characterisation of §7 is published in full under every verdict above,
including `NO-SUB-STRUCTURE`.**

---

## 9. Predictions, registered so they can be wrong

1. **The ḥawāmīm will be the tightest class**, and will clear R7. H-NEW-2820 already has them
   at the 0.05th percentile as a set; this predicts the tightening survives per-class
   size-matching.
2. **`Δ` will be negative under F1 and will attenuate under F2**, because ALM contains Q 2 and
   Q 3 — the two longest surahs in the corpus — so part of any within-class closeness is size.
3. **R1 will be the weakest arm.** A set of 29 that is *tight* need not be *sub-structured*,
   and the silhouette of a tight blob is low. I expect R1 to fail and I am registering that
   expectation rather than quietly dropping the arm afterwards.
4. **The ablations will not kill the cluster.** The Book roots are 8 of 500 dimensions; if
   removing them moved the percentile past 10, that would be a strong and surprising result
   about Pillar 1, not about this finding.

---

## 10. Garden of forking paths — everything known before the lock

- **A pre-lock feasibility probe was run and it computed no outcome statistic.** It
  established exactly three things, all recorded here: (a) `D_rebuilt` agrees with the
  published `D` to **4.999 × 10⁻⁷**, which is the published matrix's own 6-decimal rounding,
  and the frozen matrix reproduces `d̄ = 0.938813123152709` against the published
  0.9388131231527093; (b) the `N_PERIOD` strata are **estimable at k = 3, 4 and 5**, with the
  k = 5 occupancy given in §3.2; (c) the class sizes and their size/period composition, given
  in §4. **No pairwise distance among the 29, no within-class mean, no cluster structure and
  no root statistic was computed before this document was locked.**
- **The channel ranking was inherited from H-NEW-2820 §2.1, not re-derived**, so it cannot
  have been chosen to suit this result.
- **Both bin widths (k = 5, k = 10) are registered**, k = 5 primary, per UNIT-DRIFT-DEFECT §6.1.
- **Both partitions (P1, P2) are registered**, P1 primary, and both are reported.
- **Directions are locked for eleven of twelve inferences.** R9 is registered explicitly as
  two-sided because I have no defensible prior on where the one-off strings sit; declaring a
  direction there would be a guess dressed as a hypothesis.
- **The adjacency confound is named before the run** and given its own control, because the
  ḥawāmīm being consecutive is the obvious alternative explanation for the prediction in §9.1.
- **Nothing is stacked with Pillar 1** (§8).
- **Run discipline.** The run directory is created with `exist_ok=False`; every file inside it
  is opened with mode `'x'`; `results.json` is written exactly once at completion; progress
  checkpoints are written **outside** the run directory to
  `runs/h-new-2840-progress/` in files that are never rewritten. **No run directory is ever
  deleted, including a defective one.** Manifest paths are repository-relative.
- **Seeds** 20260509 primary, 20260519 replication; every classification is reported at both,
  and any classification that differs between them is labelled `SEED-FRAGILE`.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any distance among the twenty-nine was measured.
A result that was hidden by a broken null deserves a description before it deserves a claim.
Bismillāhi al-Raḥmāni al-Raḥīm.*
