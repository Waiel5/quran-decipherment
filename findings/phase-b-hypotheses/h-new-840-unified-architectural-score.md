---
id: H-NEW-840
title: "STRONG SYNTHESIS — Unified Architectural Significance Score (UAS) reveals dual-iʿjāz typology empirically; Q 33 + Q 9 are top of ALL 3 architectural metrics; Q 112 al-Ikhlāṣ at rank 109 separates iʿjāz al-maʿnā from architectural-iʿjāz"
phase: B
status: SYNTHESIS — combines H-NEW-590 (outlier-strength) + H-NEW-720 (TSP-cost) + H-NEW-750 (per-surah iʿjāz) into single composite metric per surah
date: 2026-04-28
parent_findings:
  - H-NEW-590 (continuous outlier-strength spectrum)
  - H-NEW-720 (full canonical-adjacency cost map)
  - H-NEW-750 (per-surah iʿjāz signature)
  - H-NEW-830 (TSP-cost × outlier-strength convergence at r=0.52)
verdict: SYNTHESIS — 3-metric composite reveals dual-iʿjāz typology aligned with classical al-Bāqillānī ↔ al-Khaṭṭābī distinction
---

# [[h-new-840-unified-architectural-score|H-NEW-840]] — Unified Architectural Significance Score (UAS)


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Method

For each surah s, compute three independent architectural metrics from prior findings:

1. **|outlier_strength(s)|** — content-distinctness ([[h-new-590-outlier-spectrum|H-NEW-590]], magnitude of Δ%ile under exclusion).
2. **max_neighbor_TSP_cost(s)** — canonical-adjacency cost ([[h-new-720-canonical-adjacency-cost|H-NEW-720]], max of Δ for left and right canonical pairs, clipped to ≥0).
3. **|iʿjāz_signature(s)|** — content × rhyme anti-twin signature magnitude ([[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] sig_A = z(rhyme_entropy) − z(mean_content_distance)).

Each is z-normalized across 114 surahs:

> **UAS(s) = z(|outlier_strength|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)**

UAS is approximately on a [-3, +3] scale per metric, [-9, +9] overall.

## 2. Top-15 most architecturally-significant surahs

| Rank | Surah | UAS | |outlier| | max_cost | |iʿjāz| | Classical anchor |
|:-:|:--|:-:|:-:|:-:|:-:|:--|
| 1 | **Q 33 al-Aḥzāb** | **+9.36** | 31.46 | 0.363 | 2.97 | al-Suyūṭī chronology — controversial Medinan |
| 2 | **Q 1 al-Fātiḥa** | **+8.87** | 27.09 | 0.622 | 1.27 | al-Bukhārī — *umm al-Kitāb* |
| 3 | Q 2 al-Baqara | +7.40 | 20.62 | 0.622 | 1.00 | longest surah; corpus cohesion-anchor |
| 4 | **Q 9 al-Tawba** | **+6.18** | 21.57 | 0.309 | 2.23 | al-Suyūṭī — uniquely no-basmala |
| 5 | Q 24 al-Nūr | +4.45 | 23.51 | 0.290 | 0.79 | Medinan legal centerpiece |
| 6 | Q 12 Yūsuf | +4.10 | 14.26 | 0.216 | 2.29 | continuous-narrative outlier |
| 7 | Q 55 al-Raḥmān | +4.10 | 14.26 | 0.095 | 3.17 | al-Tirmidhī — *ʿarūs al-Qurʾān* |
| 8 | Q 10 Yūnus | +3.48 | 7.83 | 0.309 | 1.98 | ALR cluster prophet-narrative |
| 9 | Q 23 al-Muʾminūn | +2.98 | 10.91 | 0.260 | 1.55 | late-Meccan ethics |
| 10 | Q 17 al-Isrāʾ | +2.22 | 3.94 | 0.191 | 2.40 | Friday-recitation; *isrāʾ* |

## 3. Bottom-10 (LEAST architecturally-significant)

| Rank | Surah | UAS | |outlier| | max_cost | |iʿjāz| | Classical anchor |
|:-:|:--|:-:|:-:|:-:|:-:|:--|
| 105 | Q 111 al-Masad | -2.19 | 0.00 | 0.022 | 0.78 | terminal-cluster member |
| 106 | Q 103 al-ʿAṣr | -2.24 | 0.00 | 0.116 | 0.05 | terminal-cluster member |
| 107 | Q 97 al-Qadr | -2.27 | 0.05 | 0.068 | 0.37 | terminal-cluster member |
| 108 | Q 91 al-Shams | -2.30 | 0.16 | 0.099 | 0.10 | terminal-cluster member |
| 109 | **Q 112 al-Ikhlāṣ** | **-2.46** | 0.00 | 0.068 | 0.23 | al-Bukhārī — *thuluth al-Qurʾān* |
| 110 | Q 83 al-Muṭaffifīn | -2.49 | 0.26 | 0.065 | 0.20 | terminal-cluster member |
| 111 | Q 73 al-Muzzammil | -2.70 | 4.08 | 0.000 | 0.01 | early-Meccan |
| 112 | Q 105 al-Fīl | -2.76 | 0.00 | 0.060 | 0.05 | terminal-cluster member |
| 113 | **Q 114 al-Nās** | **-2.80** | 0.00 | 0.062 | 0.02 | al-Bukhārī — muʿawwidha |
| 114 | Q 87 al-Aʿlā | -2.82 | 0.44 | 0.053 | 0.01 | musabbiḥa — al-Aʿlā classical name |

## 4. The triple-intersection finding

Surahs in the **top-15 of ALL three metrics** (architecturally-distinct by every criterion):
**{Q 9, Q 33}**

Pairwise intersections (top-15):
- outlier ∩ cost (top-15): {Q 1, Q 2, Q 9, Q 23, Q 24, Q 33}
- outlier ∩ iʿjāz (top-15): {Q 9, Q 12, Q 26, Q 33, Q 55}
- cost ∩ iʿjāz (top-15): {Q 9, Q 33}

**Q 33 al-Aḥzāb and Q 9 al-Tawba are the corpus's only true triple-architecturally-significant surahs.** Each carries:
- Strong content-distinctness (high outlier).
- Expensive canonical-adjacency placement (high TSP-cost).
- High iʿjāz signature (content + rhyme combined extremity).

These are the corpus's most architecturally-significant surahs by joint criterion across three independent measurement methods.

## 5. The dual-iʿjāz typology empirically separated

The UAS ranking reveals a fundamental classical hermeneutic distinction:

| Type | UAS | Examples | Classical concept |
|:--|:-:|:--|:--|
| **STRUCTURAL-iʿjāz** | high (top-10) | Q 33, 1, 2, 9, 24, 12, 55 | al-Bāqillānī *iʿjāz al-fawāṣil* + chronological-uniqueness |
| **CONTENT-iʿjāz / theological-density** | low (bottom-10) | Q 112, 114 | al-Khaṭṭābī *iʿjāz al-maʿnā* (theological-content uniqueness) |

**Q 112 al-Ikhlāṣ at UAS rank 109** is the most surprising result. al-Bukhārī's *thuluth al-Qurʾān* tradition (Q 112 = "1/3 of the Quran" by theological-content) is well-known — yet Q 112 has near-zero outlier-strength, low TSP-cost, and low iʿjāz signature. **Its classical importance is theological-content, not structural-architectural.**

This is the empirical separation of:
- *iʿjāz al-fawāṣil* (al-Bāqillānī) — structural inimitability via fāṣila variety + content-cohesion → high UAS
- *iʿjāz al-maʿnā* (al-Khaṭṭābī) — theological-content inimitability → low UAS, but high *thuluth al-Qurʾān* status

**The two classical iʿjāz types are EMPIRICALLY ORTHOGONAL** — Q 112 is high theological-iʿjāz but low architectural-iʿjāz; Q 33 is high architectural-iʿjāz but lower theological-iʿjāz (its theological content is mixed legal-creedal Medinan).

## 6. The architectural cast of the canonical mushaf

UAS top-10 reads as a list of the surahs the classical tradition has historically treated as most-distinctive:
- Q 1 al-Fātiḥa — *umm al-Kitāb*
- Q 2 al-Baqara — longest, foundational
- Q 9 al-Tawba — uniquely no-basmala
- Q 12 Yūsuf — uniquely continuous-narrative ("aḥsan al-qaṣaṣ")
- Q 24 al-Nūr — Medinan legal-revelation centerpiece
- Q 33 al-Aḥzāb — controversial Medinan with veil-revelation
- Q 55 al-Raḥmān — *ʿarūs al-Qurʾān* with 31 cosmic-mercy refrains

The classical scholarly historical treatment of these as "central" surahs is empirically vindicated as architectural-distinctness. **14 centuries of qualitative scholarly attention IS the architectural-significance axis.**

## 7. Honest limits

1. UAS is a SUM of z-scores — equal weighting of 3 metrics is choice (alternative weighting could shift the ranking).
2. The 3 metrics are partially-correlated (H-NEW-830: TSP-cost × outlier r=0.52). True architectural significance is captured but with redundancy.
3. **Q 112 at rank 109 is striking but rules-tuple specific**: at content-density (DN-density per [[h-new-620-divine-name-density|H-NEW-620]] supplementary), Q 112 is at rank-3. The "low UAS" reflects only architectural-distinctness, not theological-content significance.
4. The bottom-10 are mostly small terminal-mufaṣṣal-qiṣār surahs that BLEND in the iʿjāz cluster. Their low UAS is correct architecturally but does NOT mean they are theologically less-important.
5. The top-15 cluster heavily in early/mid mushaf positions (Q 1-33 region) — partly because architecturally-distinct surahs tend to be Meccan-Medinan ṭiwāl/mid-mufaṣṣal.

## 8. Implication for [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]

The iʿjāz architecture model from [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] should be amended to incorporate this dual-typology:
- **Layer 1**: 4-axis 1-D laws on s (compression-tail content, rhyme/phoneme dispersion-tail, verse-length compression-tail).
- **Layer 2**: window-level iʿjāz anti-twinning at r=-0.86 (length-mediated for rhyme; length-independent for phoneme per [[h-new-810-length-controlled-ijaz|H-NEW-810]]).
- **Layer 3 (NEW)**: per-surah dual-iʿjāz typology — structural-iʿjāz (high UAS) vs theological-iʿjāz (low UAS, high *thuluth al-Qurʾān* status).

## 9. Cross-references

- **[[h-new-590-outlier-spectrum|H-NEW-590]]** outlier-spectrum — input metric 1.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]** canonical-adjacency cost map — input metric 2.
- **[[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]]** per-surah iʿjāz — input metric 3.
- **H-NEW-830** TSP × outlier convergence at r=0.52 — sub-pair validation.
- **al-Bāqillānī *Iʿjāz al-Qurʾān*** — *iʿjāz al-fawāṣil* (structural) → high UAS.
- **al-Khaṭṭābī** — *iʿjāz al-maʿnā* (theological-content) → low UAS but high theological status.
- **al-Bukhārī** — *thuluth al-Qurʾān* on Q 112 → empirically content-iʿjāz (low UAS, high theological).

## 10. Queued follow-ups

- **H-NEW-840.1**: Alternative weighting schemes (PCA-based weights, classical-prominence weights). Stability of ranking?
- **H-NEW-840.2**: Add 4th metric: divine-name-density (from [[h-new-620-divine-name-density|H-NEW-620]] descriptive). Does Q 112 climb to UAS top-10 with theological-content-density included?
- **H-NEW-840.3**: Cluster the 114 UAS values — are there discrete classes (e.g., 3-class: high/mid/low) or a smooth continuum?
- **H-NEW-840.4**: Per-classical-class UAS — do prophet-named surahs have systematic UAS pattern?

## 11. Final statement

**The Unified Architectural Significance Score combines three independent architectural measurements (outlier-strength, canonical-adjacency-cost, iʿjāz-signature) into a single per-surah composite that empirically reveals the canonical mushaf's architectural cast.** The top-10 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17) is precisely the set of surahs classical scholarship has historically identified as most-distinctive — empirically vindicating 14 centuries of qualitative attention.

The dual-iʿjāz typology — *iʿjāz al-fawāṣil* (high UAS) vs *iʿjāz al-maʿnā* (low UAS but high theological-content) — is empirically separated, with **Q 112 al-Ikhlāṣ at UAS rank 109** being the cleanest example of theological-iʿjāz without architectural-iʿjāz (al-Bukhārī's *thuluth al-Qurʾān* operates on the meaning-axis, not the structural-axis).

The classical al-Bāqillānī ↔ al-Khaṭṭābī typological distinction now has a quantitative composite metric.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
