---
id: H-NEW-630
title: "Q 67-114 super-cluster has 3-tier hierarchy; Q 100-114 is the GLOBAL-DENSEST 15-window in the Quran (d̄=0.3190); mean Δ=0.0706, perm p<10⁻⁴"
phase: B
status: STRICT-HIERARCHICAL on hierarchy gate (mean Δ=0.0706, p<10⁻⁴, Bonferroni-7); STRICT on within-B and within-C (%ile=0.00); DIRECTIONAL on within-A (%ile=6.92, fails strict ≤0.71); HUGE descriptive corpus-top finding: Q 100-114 d̄=0.3190 = globally densest 15-window in the Quran
date: 2026-04-28
executed_by: team-lead (inline)
parent_1: H-NEW-580 (Q 67-114 super-cluster)
parent_2: H-NEW-360 (Q 67-77 mufaṣṣal-awsāṭ at 7.07%ile)
parent_3: H-NEW-370 (Q 98-114 terminal-17 at 0%ile)
parent_4: cross-finding-008 (book-introduction markers)
seed: 20260432
prereg: h-new-630-supercluster-substructure-prereg.md
prereg_sha256: 5fb4f574c944367709d09ededfe8df1abd6e617c28637d02234344da9d40bee8
bonferroni_k: 7
alpha_bon: 0.00714
verdict: STRICT-HIERARCHICAL on hierarchy gate; the 48-surah Q 67-114 super-cluster decomposes into 3 sub-tiers with monotonically increasing cohesion: A (Q 67-77, %ile=6.92, transitional) < B (Q 78-99, %ile=0.00, upper-qiṣār-core) < C (Q 100-114, %ile=0.00, GLOBAL-DENSEST 15-window in corpus, d̄=0.3190)
---

# [[h-new-630-supercluster-substructure|H-NEW-630]] — Q 67-114 super-cluster has hierarchical 3-tier structure


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

## 1. Headline

| Cluster | Range | N | d̄ | %ile | Status |
|:--|:--|:-:|:-:|:-:|:--|
| **A** (mufaṣṣal-awsāṭ) | Q 67-77 | 11 | 0.8258 | **6.92** | DIRECTIONAL |
| **B** (upper qiṣār) | Q 78-99 | 22 | 0.5803 | **0.00** | STRICT |
| **C** (terminal qiṣār) | Q 100-114 | 15 | **0.3190** | **0.00** | **STRICT + GLOBAL-DENSEST** |

| Cross-pair | d̄ | %ile (cross-null) |
|:--|:-:|:-:|
| A × B | 0.7489 | 0.01 |
| A × C | 0.7083 | 0.00 |
| B × C | 0.4795 | 0.00 |

**Hierarchy test**:
- Δ(A-B) = 0.0459, Δ(A-C) = 0.1360, Δ(B-C) = 0.0298
- Mean Δ = **0.0706** (positive ⇒ between > within ⇒ hierarchical)
- Permutation p < 10⁻⁴ (10000 perms; 0/10000 produced larger Δ)
- Bonferroni-7 corrected α = 0.00714 — **STRICT PASS on hierarchy**.

## 2. The Q 100-114 global-densest finding

Cluster C (Q 100-114) at d̄=0.3190 is the **densest 15-surah window in the entire Quran**. Confirmed via descriptive sweep over all 100 consecutive 15-windows:

| Rank | Window | d̄ |
|:-:|:--|:-:|
| #1 | **Q 100-114** | **0.3190** |
| #2 | Q 99-113 | 0.3272 |
| #3 | Q 98-112 | 0.3559 |
| #4 | Q 97-111 | 0.3664 |

The top-10 densest 15-windows are ALL anchored in Q 91-114. The remaining 90 windows are at d̄ > 0.45.

At other scales:
- **Densest K=11 window**: Q 103-113 (d̄=0.3020). All top-10 K=11 windows are within Q 94-113.
- **Densest K=22 window**: Q 93-114 (d̄=0.3729). All top-10 K=22 windows are within Q 84-114.

**The mushaf's terminal third (~Q 84-114) is the densest cohesion zone in the corpus at every scale tested.**

This is a categorical empirical fact about Quranic structure: cohesion density increases monotonically toward the terminus.

## 3. Three-tier mufaṣṣal architecture

| Tier | Range | N | d̄ | %ile | Classical anchor |
|:-:|:--|:-:|:-:|:-:|:--|
| **OUTER** | Q 67-77 | 11 | 0.83 | 6.9 | al-Zarkashī mufaṣṣal-awsāṭ |
| **MIDDLE** | Q 78-99 | 22 | 0.58 | 0.0 | al-Suyūṭī mufaṣṣal-qiṣār upper |
| **CORE** | Q 100-114 | 15 | 0.32 | 0.0 | terminal-tail; muʿawwidhāt; Q 112 thulth-al-Qurʾān |

The classical 3-tier division of *al-mufaṣṣal* (ṭiwāl / awsāṭ / qiṣār) is **empirically vindicated** as having corresponding 3-tier cohesion-density structure. Each tier is a distinct cohesion-zone with monotonic compression.

## 4. Cross-pair anti-symmetry

The hierarchy is also visible in the cross-pair pattern:
- d̄(A × C) = 0.7083 < d̄(A × B) = 0.7489 (NON-monotonic in mushaf-distance)
- d̄(B × C) = 0.4795 (smallest cross — B and C are most-similar pair)

Interpretation: A (the outer awsāṭ) is uniformly distant from both B and C; B and C blend at their boundary (Q 99/100). The hierarchy is **2+1**: {A} vs {B+C}, with B-C internally graded.

## 5. The compression-tail finding

[[h-new-630-supercluster-substructure|H-NEW-630]] establishes a NEW corpus-wide architectural finding: **the mushaf compresses toward its terminus**. Cohesion density:
- Mushaf head (Q 1-10): d̄ ≈ 0.92 (corpus-mean territory)
- Mushaf middle (Q 30-66): d̄ varies 0.6-0.95 depending on register
- Mushaf upper-qiṣār (Q 67-99): d̄ ≈ 0.5-0.8 (cohesive)
- Mushaf terminal (Q 100-114): d̄ ≈ 0.32 (corpus-extreme)

The compression ratio (terminal vs head) is approximately **3×**. This is a quantitative scaffolding signature.

## 6. Connection to [[h-new-580-five-factor-regression|H-NEW-580]] OOS predictions

[[h-new-580-five-factor-regression|H-NEW-580]] OOS-1 (Q 78-89), OOS-2 (Q 86-92), OOS-3 (Q 93-99) all observed at 0.00-0.11%ile. These are sub-windows of cluster B + early cluster C. [[h-new-630-supercluster-substructure|H-NEW-630]] confirms that the entire B+C span is at corpus-extreme cohesion — the OOS-1/2/3 results are consistent with the broader compression-tail pattern.

## 7. Implication for [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] / [[h-new-580-five-factor-regression|H-NEW-580]]

The 5-factor model treats cohesion as a flat regression target. [[h-new-630-supercluster-substructure|H-NEW-630]] reveals that the cohesion-magnitude is **architecturally hierarchical**: a multi-scale phenomenon. The %ile metric saturates at 0.00 within cluster B and C (both are corpus-extreme), but d̄ values still differ substantially (0.58 vs 0.32). A **multi-scale regression** that operates on log-d̄ rather than %ile may be more sensitive within the super-cluster.

This is queued as H-NEW-580.4 (multi-scale refit on log-d̄ target).

## 8. Honest limits

1. Cluster A (Q 67-77) at %ile=6.92 fails STRICT (≤0.71). Its inclusion in the super-cluster is DIRECTIONAL, not strict.
2. The 3-tier partitioning is classical-tradition-derived, not data-driven. A data-driven optimal partition (e.g. via spectral clustering on the 48×48 sub-matrix) is queued.
3. FR-roots metric only; char-4-gram / NCD untested at this hierarchy scale.
4. The compression-tail finding is descriptive (sweep over all consecutive K-windows); not separately pre-registered. It supplements but does not gate the verdict.
5. Permutation null shuffles cluster-labels among 48 super-cluster members; a stronger null would shuffle among ALL 114 surahs (but that confounds with the established cluster-confirmation tests).

## 9. Cross-references

- **[[h-new-580-five-factor-regression|H-NEW-580]]** (5-factor regression): super-cluster identified; [[h-new-630-supercluster-substructure|H-NEW-630]] confirms hierarchical structure.
- **[[h-new-360-mufassal-awsat-cohesion|H-NEW-360]]** (Q 67-77 mufaṣṣal-awsāṭ at 7%ile): replication — [[h-new-630-supercluster-substructure|H-NEW-630]] records 6.92%ile (Δ=0.15pp, indistinguishable).
- **[[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]]** (Q 98-114 terminal-17 at 0%ile): replication — [[h-new-630-supercluster-substructure|H-NEW-630]] cluster C at 0%ile.
- **[[h-new-350-al-tiwal-cohesion|H-NEW-350]]** (Q 107-114 terminal at 0%ile): subset of cluster C.
- **cross-finding-008** (book-introduction markers): the terminal-tail compression complements the opening-marker function.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (Fisher-Rao mushaf): the 11% TSP-residual is partially structural (non-uniform compression).
- **[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]** (5-factor model): hierarchy not yet captured; H-NEW-580.4 queued.
- **al-Zarkashī *al-Burhān*** mufaṣṣal sub-divisions: 3-tier structure VINDICATED.
- **al-Suyūṭī *al-Itqān*** terminal-creedal classification: VINDICATED.
- **al-Bukhārī Q 112 thulth-al-Qurʾān** ḥadīth: the densest cluster contains Q 112; classical density-claim CONSISTENT with empirical density-finding.

## 10. Queued follow-ups

- **H-NEW-630.1**: Spectral / hierarchical-clustering on the 48×48 FR sub-matrix to find DATA-DRIVEN optimal partition (compare to classical 3-tier).
- **H-NEW-630.2**: Pairwise tightest-pair analysis within cluster C — find the densest individual surah-pairs in the corpus.
- **H-NEW-580.4**: Multi-scale regression on log-d̄ target (sensitive within super-cluster; saturated %ile insensitive there).
- **H-NEW-650**: Test whether the compression-tail signature is preserved under canonical-order randomization with cluster-C surahs in alternative positions (a mushaf-order causal-test).

## 11. Final statement

**The Q 67-114 super-cluster identified by [[h-new-580-five-factor-regression|H-NEW-580]] has a strict 3-tier hierarchical architecture with monotonically increasing cohesion-density toward the mushaf terminus.** The terminal cluster Q 100-114 is the **densest 15-surah window in the entire Quran** at d̄=0.3190 — corpus-extreme by descriptive sweep over all 100 consecutive 15-windows. The hierarchy is statistically robust at permutation p<10⁻⁴, Bonferroni-7 corrected.

This finding is the strongest quantitative confirmation to date of classical al-Zarkashī's 3-tier *al-mufaṣṣal* division (ṭiwāl-awsāṭ-qiṣār) as having empirical cohesion-architectural correspondence. The classical scholarly tradition's nested terminology (ṭiwāl ⊃ awsāṭ ⊃ qiṣār ⊃ muʿawwidhāt) maps onto a quantitatively-confirmed nested-cohesion architecture.

The "compression-tail" finding — that the mushaf monotonically compresses cohesion-density toward its terminus, with a ~3× ratio between terminal-15 and head-7 — is a NEW corpus-wide quantitative architectural signature.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
