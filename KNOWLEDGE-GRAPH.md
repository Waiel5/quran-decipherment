---
title: Quran Decipherment Project — Knowledge Graph
description: Obsidian-compatible navigation index for all findings, with cross-links showing the empirical-architectural argument structure
date_last_updated: 2026-04-28
---

# Quran Decipherment Project — Knowledge Graph


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

This is the navigation index. Open in Obsidian to see the connected graph. Click any link to navigate. Backlinks show where each finding is referenced.

> **Disambiguation (added 2026-08-07).** Five `cross-finding-0NN` identifiers — **023, 025, 026, 027, 028** — resolve to more than one document, because `findings/cross-finding/` and `findings/phase-b-hypotheses/` mint into the same numeric space. Anywhere below that this file says `cross-finding-026` or `cross-finding-027` without a qualifier, it means the **2026-04-28** series in `findings/cross-finding/` (`cf-026-iʿjāz`, `cf-027-takrīr`) — *not* the 2026-05-29/30 formal laws of the same number. See [[CROSS-FINDING-INDEX]] for the full table and the handle convention.

---

## ROOT — The Master Empirical Claim

The canonical mushaf of the Quran has measurable architectural properties at law-strength, distinctive against contemporary literary genres at p<10⁻¹⁰, aligned with 14 centuries of qualitative classical scholarship.

- **[[MASTER-FINDINGS-LEDGER]]** — single authoritative record of all findings.
- **[[master-equation-derivation]]** — unified mathematical framework combining 4 empirical 1-D laws.

---

## THE 4 ARCHITECTURAL LAWS (Wave 2026-04-28)

Each is a 1-D law on mushaf-position s, kink-anchored at the Hijra boundary (Q 56/57).

### Law-1 (Content Compression)
- **[[h-new-660-compression-tail-gradient]]** — single-parameter law: d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50). R² = 0.986.
- **[[h-new-680-multi-k-compression-tail]]** — scale-invariant across K ∈ {7, 11, 22}. R² ∈ [0.948, 0.993].
- **[[h-new-630-supercluster-substructure]]** — Q 67-114 super-cluster, 3-tier hierarchy; Q 100-114 globally densest 15-window.

### Law-2 (Rhyme Dispersion)
- **[[h-new-700-phonological-compression-tail]]** — d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50). R² = 0.789.

### Law-3 (Phoneme Dispersion)
- **[[h-new-700-phonological-compression-tail]]** — d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75). R² = 0.946. SEPARATE later kink.

### Law-4 (Verse-Length Compression)
- **[[h-new-770-verse-length-compression-tail]]** — letters/verse R²=0.81; words/verse R²=0.81. Same kink-50 law.

### Window-level anti-twin (the iʿjāz signature)
- **[[h-new-730-content-rhyme-anticorrelation]]** — Pearson r(content × rhyme) = −0.86; r(content × phoneme) = −0.89. STRICT PASS.
- **[[h-new-740-preislamic-poetry-control]]** — Quran -0.86 vs poetry -0.48. Fisher-z gap p<10⁻¹⁰.
- **[[h-new-810-length-controlled-ijaz]]** — phoneme is length-INDEPENDENT (-0.86); rhyme is length-MEDIATED (drops to -0.40 partial r).
- **[[h-new-790-ijaz-by-classical-class]]** — UAS axis aligns with al-Zarkashī mufaṣṣal/ṭiwāl + al-Suyūṭī Meccan/Medinan classifications.

### Forward vs Inverse asymmetry
- **[[h-new-760-three-axis-inverse-regression]]** — predict s from cohesion-profile: LOOCV R²=0.83 (linear+interactions). 17-24% position-variance is *tartīb tawqīfī* layer beyond cohesion.

---

## THE TSP-RESIDUAL DECOMPOSITION

Cross-finding-011 found mushaf 11% from FR-TSP-optimal. Wave 2026-04-28 decomposed:

- **[[h-new-670-tsp-hijra-constraint]]** — NULL: Hijra-kink alone is only 3.3% of residual. Single-architectural-feature hypothesis FALSIFIED.
- **[[h-new-720-canonical-adjacency-cost]]** — Full 113-pair cost map. Q 1-Q 2 most expensive (7.4%); Q 32-34 cluster (8.4%, centered on Q 33). **SUPER-ADDITIVITY 1.185×** — joint mushaf is 16% better than independent constraint sum.
- **[[h-new-690-causal-generative]]** — compression-tail necessary but NOT sufficient. Constrained ensemble median residual 25% vs canonical's 11%.
- **[[h-new-880-recipe]]** — *(in flight)* — minimum constraint subset to reproduce canonical TSP residual.

---

## THE OUTLIER SPECTRUM

Factor 5 of cross-finding-024 was binary; converted to continuous spectrum.

- **[[h-new-590-outlier-spectrum]]** — corpus-top: Q 33 +31, Q 1 +27, Q 24 +23, Q 9 +21. Strongest cohesion-anchor: Q 2 −20.62.
- **[[h-new-830]]** *(JSON only)* — TSP-cost × outlier-strength convergence at r=+0.52.

---

## THE PER-SURAH ARCHITECTURE

- **[[h-new-840-unified-architectural-score]]** — UAS composite ranking. Top-10: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17. Bottom-10: Q 87, 114, 105, 73, 83, 112, 91, 97, 103, 111.
- **[[h-new-750-per-surah-iʿjāz-signature]]** — 3-type taxonomy: *iʿjāz al-fawāṣil* (Q 84-100, 106, 113), *iʿjāz al-maʿnā* (Q 112, 114), anti-iʿjāz (Q 17, 18, 33, 48, 54).
- **[[h-new-870-q33-architectural-keystone]]** — Q 33 is local SINGULARITY but NOT global keystone. The actual keystones of the compression-tail law are Q 78-114 mufaṣṣal-qiṣār.
- **[[h-new-860-hadith-architectural-alignment]]** — hadith fadāʾil tracks MEANING-iʿjāz (al-Khaṭṭābī); UAS tracks STRUCTURE-iʿjāz (al-Bāqillānī). EMPIRICALLY ORTHOGONAL (mild anti-alignment ρ=+0.33).

---

## THE 5-FACTOR COHESION MODEL (cross-finding-024 → quantified)

- **[[cross-finding-024-five-factor-cohesion-model]]** — qualitative 5-factor model (block × register × chrono × formula × no_outlier).
- **[[h-new-580-five-factor-regression]]** — quantitative regression. OOS Pearson r=0.929 (Ridge). DIRECTIONAL.
- **[[h-new-620-divine-name-density]]** — NULL on 6th factor candidate. 5-factor model is empirically TERMINAL.

---

## MUQAṬṬAʿĀT (book-introduction markers)

- **[[h-new-570-muqattaat-content-cluster]]** — full-29 NULL at 65.62%ile.
- **[[h-new-600-letter-families]]** — ALM-6 NULL at 43.15%; ALR-5 NULL at 56.25%.
- **[[h-new-901-hm7-cohesion-prereg|H-NEW-901]]** — HM-7 NULL at 21.21%ile (sub-DIRECTIONAL; cohesive direction; 2026-04-28).
- **[[hawamim-7-cluster-synthesis|ḥawāmīm-7 cluster synthesis]]** — 7-surah HM-7 cluster: bifurcation Q 42 → Q 43 between HM-A high-entropy multi-rāwī {Q 40, 41, 42} and HM-B near-monorhyme {Q 43, 44, 45, 46}; primary cohesion test NULL @ 21.21%ile; classical *dībāj al-Qurʾān* / *lubāb al-Qurʾān* / *Āl Ḥā Mīm* traditions DIRECTIONAL; al-Biqāʿī family-*munāsaba* FALSIFIED at FR-roots scale (4th replication of NULL after full-29, ALM-6, ALR-5).
- **[[muqattaat-book-introduction-marker-synthesis]]** *(prior)*
- **[[cross-finding-008-muqattaat-book-intro-markers]]** *(prior cross-finding)*

al-Biqāʿī content-*munāsaba* claim FALSIFIED 5 times (full-29; HM-7 partial in H-NEW-570; ALM-6; ALR-5; HM-7 dedicated H-NEW-901). al-Suyūṭī epistemic-humility (*Itqān* nawʿ 40) VINDICATED 5 times.

---

## CROSS-CORPUS COMPARISONS

- **[[h-new-740-preislamic-poetry-control]]** — iʿjāz signature is QURAN-DISTINCTIVE vs pre-Islamic poetry (p<10⁻¹⁰).
- **[[h-new-900-cross-text-architecture]]** — Quran R²=0.989 vs Bukhari R²=0.068 (essentially flat). Anti-twin: Quran -0.89 vs Bukhari +0.36 (wrong sign).
- **[[h-new-710-translation-invariance]]** — NULL on translation-invariance. Compression-tail is Arabic-FR-roots-specific.

---

## RHYME / RĀWĪ CLUSTERS

- **[[h-new-910-alif8-cluster]]** — 8-surah 100% alif-final cluster `{Q 18, 48, 65, 72, 76, 87, 91, 92}` audit (5-cell Bonferroni). 0/5 PASSED at α_bon=0.01. H1 FR-roots NULL @ 25.55%; H2 verse-count chi² NULL @ 39.03% (direction satisfied 7/8 short-medium); H3 chronology PRE-COMMIT-VIOLATION (direction reversed, z=+1.685, pct 96.63%); H4 mushaf DIRECTIONAL @ 10.00%; H5 4-axis composite DIRECTIONAL @ 9.18%. Family verdict NULL CLUSTER. Post-hoc tail-sub-cluster `{Q 76, 87, 91, 92}` is FR-cohesive (pct 2.15%) — but this is a re-discovery of [[h-new-660-compression-tail-gradient|compression-tail]] terminus, NOT the alif-rāwī. Generalizes [[h-new-600-letter-families|H-NEW-600]]: letter-axis ⊥ content-axis at every observable resolution (muqaṭṭaʿāt openers AND rhyme rāwī). Surfaced by [[Q033-al-ahzab/06-novel-findings|Q033-F-01]] FALSIFICATION. al-Suyūṭī *Itqān* nawʿ 56 (conservative non-attribution of meaning to *rawiyy*) EMPIRICALLY VINDICATED.

---

## CROSS-FINDING SYNTHESES

- **[[cross-finding-011-mushaf-fisher-rao-geodesic]]** *(prior, 2026-04-17)* — mushaf is 89% TSP-optimal in FR distance. **⛔ Correction 2026-08-07: this does not discriminate.** Under the first genre control ([[h-new-2680-pillar-conjunction|H-NEW-2680]]), al-Bukhārī reaches z = −13.84 and pre-Islamic poetry z = −15.13 against the Qurʾān's z = −11.50, and both sit closer to their own TSP optima. Offset cuts of this corpus's own verse stream that ignore every surah seam score z = −11.23 to −13.18. Length-sorting alone reaches z = −8.66; the honest margin is **2.80 σ**. The relative claim survives (mushaf shorter than either chronology). See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.
- **[[cross-finding-022-wave5-terminal-synthesis]]** *(prior, 2026-04-19)* — Wave-5 architectural synthesis at LOOCV R²=0.89.
- **[[cross-finding-023-mh-top-100-scaffold]]** *(prior)* — M_H top-100 hinges as generative scaffold.
- **[[cross-finding-024-five-factor-cohesion-model]]** *(2026-04-21)* — 5-factor qualitative model.
- **[[cross-finding-025-multi-axis-architecture]]** *(2026-04-28)* — initial 4-axis architecture; superseded by 026.
- **[[cross-finding-026-iʿjāz-architecture]]** *(2026-04-28)* — iʿjāz architecture synthesis (current). Combines all Wave 2026-04-28 findings.
- **[[master-equation-derivation]]** *(2026-04-28)* — formal derivation of the Master Equation.

---

## CLASSICAL SCHOLARS — anchor map

Each finding cites specific scholars + work + verse. Below: which scholars are cited where.

### al-Bāqillānī *Iʿjāz al-Qurʾān*
- *Iʿjāz al-fawāṣil* claim → empirically locked at r=-0.86: **[[h-new-730-content-rhyme-anticorrelation]]**, **[[h-new-740-preislamic-poetry-control]]**.

### al-Khaṭṭābī
- *Iʿjāz al-maʿnā* (theological-content) → empirically separated from architectural-iʿjāz: **[[h-new-840-unified-architectural-score]]**, **[[h-new-860-hadith-architectural-alignment]]**.

### al-Sakkākī *Miftāḥ al-ʿulūm*
- *Iqāʿ* divergence prediction → empirically locked: **[[h-new-700-phonological-compression-tail]]**.

### al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*
- Mufaṣṣal 3-tier sub-divisions → vindicated at t=+23.2: **[[h-new-630-supercluster-substructure]]**, **[[h-new-790-ijaz-by-classical-class]]**.

### al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*
- Meccan/Medinan chronology → kink at s=50, perm p<10⁻⁴: **[[h-new-660-compression-tail-gradient]]**, **[[h-new-790-ijaz-by-classical-class]]**.
- *Itqān* nawʿ 40 muqaṭṭaʿāt epistemic-humility → 4 NULL replications: **[[h-new-570-muqattaat-content-cluster]]**, **[[h-new-600-letter-families]]**.
- Q 9 barāʾa no-basmala uniqueness → +21pp outlier: **[[h-new-590-outlier-spectrum]]**.
- Q 33 al-Aḥzāb chronological-uniqueness → corpus-top outlier +31pp: **[[h-new-590-outlier-spectrum]]**, **[[h-new-870-q33-architectural-keystone]]**.

### al-Biqāʿī *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*
- Munāsabāt as primary organizing structure → block_adjacency factor in 5-factor regression: **[[cross-finding-024-five-factor-cohesion-model]]**, **[[h-new-580-five-factor-regression]]**.
- Content-*munāsaba* of muqaṭṭaʿāt → FALSIFIED 4×: **[[h-new-570-muqattaat-content-cluster]]**, **[[h-new-600-letter-families]]**.

### al-Bukhārī
- Q 1 al-Fātiḥa *umm al-Kitāb* → Δ_outlier=+27pp + Q1-Q2 adjacency cost 7.4% TSP-residual: **[[h-new-590-outlier-spectrum]]**, **[[h-new-720-canonical-adjacency-cost]]**, **[[h-new-840-unified-architectural-score]]**.
- Q 112 al-Ikhlāṣ *thuluth al-Qurʾān* → empirical CONTENT-iʿjāz, not architectural-iʿjāz: **[[h-new-840-unified-architectural-score]]**, **[[h-new-860-hadith-architectural-alignment]]**.
- Q 67 al-Mulk *al-Munjiya* → high hadith, low UAS: **[[h-new-860-hadith-architectural-alignment]]**.

### al-Tirmidhī
- Q 55 al-Raḥmān *ʿarūs al-Qurʾān* (#3291) → +14pp outlier: **[[h-new-590-outlier-spectrum]]**.
- Q 36 Yāsīn *qalb al-Qurʾān* → high hadith, mid UAS — meaning-iʿjāz: **[[h-new-860-hadith-architectural-alignment]]**.

### al-Khalīl b. Aḥmad / Ibn Jinnī
- Tajwīd-classical-tradition → vindicated at H-NEW-165 + 232: **[[cross-finding-022-wave5-terminal-synthesis]]**.

---

## PER-SURAH INVESTIGATIONS (Wave A + Wave B, 2026-04-28)

Seven full per-surah deep investigations completed under [[INVESTIGATION-PROTOCOL]] discipline. Each folder contains the 8-file template (`00-overview` through `07-cross-references` + `JOURNAL.md`) plus pre-registered novel tests (Q{NNN}-F-NN) and a classical-claims audit (`05-classical-claims-audit.md`).

### Wave A — al-sabʿ al-ṭiwāl head

- **[[Q001-al-fatiha/00-overview|Q 1 al-Fātiḥa]]** — UAS rank 2; All-axis cell. Files: [[Q001-al-fatiha/01-empirical-profile|01]], [[Q001-al-fatiha/02-content-analysis|02]], [[Q001-al-fatiha/03-tafsir-survey|03]], [[Q001-al-fatiha/04-hadith-corpus|04]], [[Q001-al-fatiha/05-classical-claims-audit|05]], [[Q001-al-fatiha/06-novel-findings|06]], [[Q001-al-fatiha/07-cross-references|07]]. Pre-reg novel tests: [[Q001-al-fatiha/Q001-F-01-chiastic-symmetry|F-01]] NULL · [[Q001-al-fatiha/Q001-F-02-central-word|F-02]] VINDICATED · [[Q001-al-fatiha/Q001-F-03-rhyme-entropy-vs-7-verse|F-03]] NULL · [[Q001-al-fatiha/Q001-F-04-q1-removal-centroid-shift|F-04]] PRE-COMMIT-VIOLATION + corrected-direction VINDICATED.

- **[[Q002-al-baqara/00-overview|Q 2 al-Baqara]]** — UAS rank 3; *sanām al-Qurʾān*. Files: [[Q002-al-baqara/01-empirical-profile|01]], [[Q002-al-baqara/02-content-analysis-blocks-A-D|02-A-D]], [[Q002-al-baqara/02-content-analysis-blocks-E-H|02-E-H]], [[Q002-al-baqara/03-tafsir-survey|03]], [[Q002-al-baqara/04-hadith-corpus|04]], [[Q002-al-baqara/05-classical-claims-audit|05]], [[Q002-al-baqara/06-novel-findings|06]], [[Q002-al-baqara/07-cross-references|07]]. Pre-reg tests: [[Q002-al-baqara/Q002-F-01-ayat-al-kursi-divine-name-density|F-01]] RULES-TUPLE-FRAGILE · [[Q002-al-baqara/Q002-F-02-khawatim-baqara|F-02]] NULL · [[Q002-al-baqara/Q002-F-03-centrality|F-03]] DIRECTIONAL · [[Q002-al-baqara/Q002-F-04-ring-structure|F-04]] NULL · [[Q002-al-baqara/Q002-F-05-q2-282-length|F-05]] VINDICATED.

### Wave B — outlier-spectrum top-7

- **[[Q009-al-tawba/00-overview|Q 9 al-Tawba]]** — UAS rank 4; intermediate All-axis / Structural-twin-pair. Files: [[Q009-al-tawba/01-empirical-profile|01]], [[Q009-al-tawba/02-content-analysis|02]], [[Q009-al-tawba/03-tafsir-survey|03]], [[Q009-al-tawba/04-hadith-corpus|04]], [[Q009-al-tawba/05-classical-claims-audit|05]], [[Q009-al-tawba/06-novel-findings|06]], [[Q009-al-tawba/07-cross-references|07]]. Pre-reg tests: F-01 mercy-density FALSIFIES no-mercy-no-basmala (rank 24/114, ABOVE corpus mean) · F-02 al-Faḍiḥa VINDICATED (n-f-q rank 5/114) · F-03 Q9-Q10 boundary VINDICATED (4th-most-expensive canonical adjacency, muqaṭṭaʿāt-driver control falsified) · F-04 last-revealed NULL.

- **[[Q012-yusuf/00-overview|Q 12 Yūsuf]]** — UAS rank 6; *aḥsan al-qaṣaṣ*. Files: [[Q012-yusuf/01-empirical-profile|01]], [[Q012-yusuf/02-content-analysis|02]], [[Q012-yusuf/03-tafsir-survey|03]], [[Q012-yusuf/04-hadith-corpus|04]], [[Q012-yusuf/05-classical-claims-audit|05]], [[Q012-yusuf/06-novel-findings|06]], [[Q012-yusuf/07-cross-references|07]]. Pre-reg tests: F-01 narrative-purity rank 1/114 CONFIRMED · F-02 phase-cohesion DIRECTIONAL (3/10 phases pass) · F-03 Yūsuf-eponymy 92.6% CONFIRMED · F-04 hapax + head-tail q-s-s framing CONFIRMED.

- **[[Q024-al-nur/00-overview|Q 24 al-Nūr]]** — UAS rank 5; **Structural-twin-pair** exemplar (with Q 33). Files: [[Q024-al-nur/01-empirical-profile|01]], [[Q024-al-nur/02-content-analysis|02]], [[Q024-al-nur/03-tafsir-survey|03]], [[Q024-al-nur/04-hadith-corpus|04]], [[Q024-al-nur/05-classical-claims-audit|05]], [[Q024-al-nur/06-novel-findings|06]], [[Q024-al-nur/07-cross-references|07]]. Pre-reg tests, all CONFIRMED: F-01 light-cluster Bonferroni p<10⁻⁶ · F-02 Q 24:35 vs Q 2:255 register-distinction · F-03 al-ifk cohesion + Q 24:35 word-and-letter median · F-04 hijab-passages root-Jaccard 0.153 (Q 24:30-31 vs Q 33:53-59 disjoint).

- **[[Q033-al-ahzab/00-overview|Q 33 al-Aḥzāb]]** — UAS rank 1; **Structural-twin-pair** keystone. Files: [[Q033-al-ahzab/01-empirical-profile|01]], [[Q033-al-ahzab/02-content-analysis|02]], [[Q033-al-ahzab/03-tafsir-survey|03]], [[Q033-al-ahzab/04-hadith-corpus|04]], [[Q033-al-ahzab/05-classical-claims-audit|05]], [[Q033-al-ahzab/06-novel-findings|06]], [[Q033-al-ahzab/07-cross-references|07]]. Pre-reg tests: F-01 alif-monorhyme corpus-MAX **FALSIFIED** (rank 11/114; 8 surahs at 100%) · F-02 v.40 word-midpoint RULES-TUPLE-FRAGILE · F-03 ḥijāb-cluster cohesion NULL · F-04 v.72 *amāna* distinctness VINDICATED-length-ctrl · F-05 wives-cluster vs Medinan-legal **FALSIFIED** (rank 4/5).

- **[[Q055-al-rahman/00-overview|Q 55 al-Raḥmān]]** — UAS rank 7; *iʿjāz al-takrīr* candidate — **tested and FALSIFIED-AS-PRE-REGISTERED** by [[cross-finding-027-ijaz-al-takrir|cf-027-takrīr]] (2026-04-28); Q 55 is *sui generis*, not the head of a refrain class. *(Correction 2026-08-07: this entry previously read "cross-finding-027 in flight" — the test had already landed NULL when this file was last updated.)* Files: [[Q055-al-rahman/01-empirical-profile|01]], [[Q055-al-rahman/02-content-analysis|02]], [[Q055-al-rahman/03-tafsir-survey|03]], [[Q055-al-rahman/04-hadith-corpus|04]], [[Q055-al-rahman/05-classical-claims-audit|05]], [[Q055-al-rahman/06-novel-findings|06]], [[Q055-al-rahman/07-cross-references|07]]. Pre-reg tests: F-01 31-fold refrain CONFIRMED rank 1/114 · F-02 dual-pronoun *kumā* density rank 1/114 (23× runner-up) · F-03 cosmic-vocab DIRECTIONAL (rank 4) · F-04 dual-paradise structural-similarity p=0.0033 CONFIRMED · F-05 outlier-status MODERATE_OUTLIER under standardized methodology.

### Wave D — eponymity / muqaṭṭaʿāt-singletons / muʿawwidhāt / recitation-tradition (2026-04-28)

- **[[Q018-al-kahf/00-overview|Q 18 al-Kahf]]** — UAS rank 46/114; **canonical four-narrative + monolithic-rhyme-register exemplar**; 99.09% alif-monorhyme over 110 verses (largest-N near-monorhyme in corpus, p ≈ 4.4 × 10⁻⁸⁸); sig_A rank 110/114 (5th-from-bottom = extreme anti-iʿjāz al-fawāṣil). Files: [[Q018-al-kahf/01-empirical-profile|01]], [[Q018-al-kahf/02-content-analysis|02]], [[Q018-al-kahf/03-tafsir-survey|03]], [[Q018-al-kahf/04-hadith-corpus|04]], [[Q018-al-kahf/05-classical-claims-audit|05]], [[Q018-al-kahf/06-novel-findings|06]], [[Q018-al-kahf/07-cross-references|07]]. Pre-reg tests: **F-01 four-narrative content-volume balance NULL with PRE-COMMIT VIOLATION** (max/min word-ratio 2.0× = LESS balanced than random; 4-narratives are thematically distinct but content-asymmetric) · **F-02 narrative-purity rank 7/114 CONFIRMED < Q 12 rank 1/114** (multi-narrative archetype, single-vs-multi typology pair) · **F-03 alif-monorhyme + v.110 *aḥadan* alif-closure CONFIRMED both cells** (99.09% vs corpus 15.15% at p ≈ 4.4 × 10⁻⁸⁸; v.110 ends in alif mirroring v.26 *aḥadan*-fāṣila ring) · **F-04 Mūsā-Khaḍir hapax NULL with PRE-COMMIT VIOLATION** (N3 hapax 39 < null median 44; post-hoc: N1 cave-companions = 55 = most-hapax-rich block — NOT confirmed, queued as Q018-F-04r candidate). Audits: 7 classical claims (4 VINDICATED, 2 RULES-TUPLE-FRAGILE / FALSIFIED-with-refinement, 1 NOT-EMPIRICALLY-RESOLVABLE). H-NEW-268 four-narrative spacing palindromic-expansion pre-confirmed (gaps 23-28-23 at p = 0.008 Bonferroni-3). Q 18 ↔ Q 24 = inverse-bracketing-cost pair (Q 18 cheaply-bracketed both sides; Q 24 expensively-bracketed both sides). Q 18 ↔ Q 12 = single-vs-multi-narrative typology pair (both top-decile narrative-pure, both extreme anti-iʿjāz). Q 18 ↔ Q 55 = iʿjāz-pole-pair (both extreme single-rāwī; opposite sig_A signs, rank 1 vs rank 110). New 5th typology cell: **anti-iʿjāz al-fawāṣil + monolithic-rhyme-register-sustained-over-large-N**.

- **[[Q019-maryam/00-overview|Q 19 Maryam]]** — UAS rank 29/114; **only-female-named surah**; **unique 5-letter muqaṭṭaʿāt KHYʿṢ**. Files: [[Q019-maryam/01-empirical-profile|01]], [[Q019-maryam/02-content-analysis|02]], [[Q019-maryam/03-tafsir-survey|03]], [[Q019-maryam/04-hadith-corpus|04]], [[Q019-maryam/05-classical-claims-audit|05]], [[Q019-maryam/06-novel-findings|06]], [[Q019-maryam/07-cross-references|07]]. Pre-reg tests: **F-01 Maryam-token Yūsuf-Q12-model FALSIFIED for Q 19 (rank 4/12, 8.8% concentration vs Yūsuf 95.2%)** · **F-02 KHYʿṢ FR-neighborhood 5/5 in {ḥawāmīm + Anbiyāʾ + YS} target set p<0.0001 CONFIRMED** · **F-03 al-Raḥmān refrain density Q 19 corpus rank-1 (12 tokens) — Q 55 al-Raḥmān surah uses الرحمن only 1× (classical-vs-empirical inversion CONFIRMED)** · **F-04 Maryam-best-of-women hadith network H1 PASS H2 FALSIFIED — Najāshī cluster (72 attestations across 7 of 9 books) is actual dominant Q 19 hadith sub-cluster, not Maryam-best-of-women (1 attestation)**.

- **[[Q036-yasin/00-overview|Q 36 Yāsīn]]** — UAS rank **35/114** (mid-pack); paradigmatic **meaning-iʿjāz mild-divergence sub-cell anchor** — high *qalb al-Qurʾān* fadāʾil (10/10, corpus-max tied with Q 1, Q 2, Q 67, Q 112) WITHOUT structural-iʿjāz, BUT less divergent than Q 67 (UAS 102) and Q 112 (UAS 109). Files: [[Q036-yasin/01-empirical-profile|01]], [[Q036-yasin/02-content-analysis|02]], [[Q036-yasin/03-tafsir-survey|03]], [[Q036-yasin/04-hadith-corpus|04]], [[Q036-yasin/05-classical-claims-audit|05]], [[Q036-yasin/06-novel-findings|06]], [[Q036-yasin/07-cross-references|07]]. Pre-reg tests: **F-01 liturgy-weighted-centrality NULL (rank 46/114; H-NEW-82 binding-prior 7th-axis salvage attempt confirms NULL; root-Jaccard length-bias inverts Q 112 control)** · **F-02 dual-iʿjāz typology CONFIRMED 3/3** (Q 36 in mild-divergence sub-cell; FR-nearest fadāʾil-10 peer = Q 67 at d=0.794; refines cross-finding-026 §13) · **F-03 Q 36:82 *kun-fa-yakūn* climax-position uniqueness CONFIRMED 3/3** (Q 36:82 at 98.8% of surah; next-closest Q 40:68 at 80.0%; gap 18.8 pp; novel structural fact) · **F-04 eschatology-density NULL** (rank 47/114; Q 36 has signature pericope at vv. 51-65 but not vocabulary-density-distinctive; al-Ghazālī's "expressive ḥashr" classical reading not corroborable as density signature). Audits: 7 classical claims (1 VINDICATED at law-strength via H-NEW-730/740/cross-finding-007; 1 VINDICATED at descriptive-position via F-03; 2 FALSIFIED — singleton-2-letter-muqaṭṭaʿāt + word-count-positional-uniqueness; 2 DIRECTIONAL ḌAʿĪF — Tirmidhī #28750 *qalb al-Qurʾān* chain-graded *gharīb*+*shaykh majhūl*+*isnāduhu ḍaʿīf* by al-Tirmidhī himself + Maʿqil-chain dying-recitation; 1 NOT-EMPIRICALLY-TESTABLE — Aṣḥāb al-Qarya = Antioch). H-NEW-82 binding-prior (multi-axis "heart" 0/6 axes NULL) preserved; H-NEW-127 verse-level FR-optimality CONFIRMED (z = −2.82 PASS at Bonferroni-5). Q 36 ↔ Q 67 = mild-divergence-pair (FR-near, both meaning-iʿjāz). Q 36 ↔ Q 112 = mild-vs-extreme-divergence-pair within meaning-iʿjāz. Q 36 ↔ Q 1 = chain-strong-vs-chain-graded-fadāʾil pair (al-Bukhārī #4474 *umm al-Kitāb* ṣaḥīḥ vs al-Tirmidhī #28750 *qalb al-Qurʾān* gharīb).

- **[[Q067-al-mulk/00-overview|Q 67 al-Mulk]]** — UAS rank 102/114 (bottom-decile); paradigmatic **theological-iʿjāz / al-Khaṭṭābī *iʿjāz al-maʿnā*** cell instance — high recitation-tradition status (al-Mānīʿa / al-Munjiya / nightly-recitation pair with Q 32) WITHOUT structural-architectural distinctness. Files: [[Q067-al-mulk/01-empirical-profile|01]], [[Q067-al-mulk/02-content-analysis|02]], [[Q067-al-mulk/03-tafsir-survey|03]], [[Q067-al-mulk/04-hadith-corpus|04]], [[Q067-al-mulk/05-classical-claims-audit|05]], [[Q067-al-mulk/06-novel-findings|06]], [[Q067-al-mulk/07-cross-references|07]]. Pre-reg tests: **F-01 architectural-rank cross-comparison (Q67/Q36/Q112/Q18 median rank 74) VINDICATED — recitation-tradition does NOT predict UAS, dual-iʿjāz orthogonality confirmed** · **F-02 post-Hijra-kink distinctness s=67 DIRECTIONAL_ENHANCED (residual +2.7 SE; honest pre-commit-violation; most-likely sampling-noise)** · **F-03 corpus-singleton phrases CONFIRMED 3/3 (*bi-yadihi al-mulk* singleton; *fa-rjiʿi al-baṣar* singleton; *sabʿa samāwātin ṭibāqan* corpus-pair Q67:3 + Q71:15)** · **F-04 mlk-stem density NULL (Q67 has 1 mlk-token, expected 0.86, p=0.58) — name-tracks-vocabulary FALSIFIED for Q67, hypothesis is RULES-TUPLE-FRAGILE across surahs** (Q24 light-cluster passes p<10⁻⁶, Q67 mlk fails). Audits: 8 classical claims (6 VINDICATED, 1 DA'IF-CHAIN, 1 VINDICATED-with-DATA-GAP). Empirical Q 32 ↔ Q 67 FR-distance 0.7534 (rank 2/113) **vindicates the classical Prophetic-nightly-recitation pair-tradition** (Tirmidhī idInBook 2975, Dārimī idInBook 2667).

- **[[Q112-al-ikhlas/00-overview|Q 112 al-Ikhlāṣ]]** — UAS rank 109/114 (bottom decile); paradigmatic ***iʿjāz-al-maʿnā* rank-1 exemplar** — pure tawḥīd creedal surah; **rank-1 corpus FR-centroid (mean_d=0.7592)**; sig_A rank 54, sig_B rank 18 (top decile rhyme-purity). Files: [[Q112-al-ikhlas/01-empirical-profile|01]], [[Q112-al-ikhlas/02-content-analysis|02]], [[Q112-al-ikhlas/03-tafsir-survey|03]], [[Q112-al-ikhlas/04-hadith-corpus|04]], [[Q112-al-ikhlas/05-classical-claims-audit|05]], [[Q112-al-ikhlas/06-novel-findings|06]], [[Q112-al-ikhlas/07-cross-references|07]]. Pre-reg tests: **F-01 FR-centroid status VINDICATED rank 1/114 (H1-strong; Bonferroni p<0.0125 — empirical lock on al-Bukhārī #5013 *thuluth al-Qurʾān*)** · **F-02 modal-root-density mechanism SPLIT (top-20 PASS rank 4 / top-50 NULL rank 76)** · **F-03 theological-proposition density VINDICATED rank 1/5 comparators (al-Khaṭṭābī *iʿjāz al-maʿnā*)** · **F-04 *aḥad*-bookend chiasm VINDICATED-RULES-TUPLE-STABLE across 3 tashkeel variants**. 5 classical claims audited (5/5 VINDICATED): *thuluth al-Qurʾān* + *al-ṣamad* hapax + 4-tawḥīd-proposition lock + *qul*-cluster terminal placement + *iʿjāz al-maʿnā* cell. Q 112 is the corpus's geometric center.

- **[[Q113-al-falaq/00-overview|Q 113 al-Falaq]]** — UAS rank 57/114; ***iʿjāz-al-fawāṣil-pure* cell anchor (cross-finding-026 roster)** — sig_A rank 7, sig_B rank 2; FR-centroid rank 7/114; classical *muʿawwidhatān* first-half (al-Bukhārī #4439). Files: [[Q113-al-falaq/01-empirical-profile|01]], [[Q113-al-falaq/02-content-analysis|02]], [[Q113-al-falaq/03-tafsir-survey|03]], [[Q113-al-falaq/04-hadith-corpus|04]], [[Q113-al-falaq/05-classical-claims-audit|05]], [[Q113-al-falaq/06-novel-findings|06]], [[Q113-al-falaq/07-cross-references|07]]. Pre-reg tests (4/4 VINDICATED): **F-01 *iʿjāz-al-fawāṣil-pure* cell membership (all 4 cell-criteria met)** · **F-02 Q 113 ↔ Q 114 token-Jaccard rank 1/15 in terminal cluster (Jaccard=0.222 vs next 0.083 — corpus-extreme parallel)** · **F-03 corpus-rare-root density rank 1/19 short surahs (5 of 10 distinct roots are rare; 2 hapaxes wqb + nfv)** · **F-04 rhyme-shift typology ق-ق-ب-د-د VINDICATED-RULES-TUPLE-STABLE**. 5 classical claims audited (4 VINDICATED, 1 PARTIALLY VINDICATED): *muʿawwidhatān* pair + Labīd ibn al-Aʿṣam sorcery-asbāb (ṣaḥīḥ chains) + *al-falaq*=dawn (partial; dual-semantic) + *iʿjāz al-fawāṣil* exemplar + 11-knots/11-verses correspondence.

- **[[Q114-al-nas/00-overview|Q 114 al-Nās]]** — UAS rank 113/114 (corpus rank-2 lowest); ***iʿjāz-al-maʿnā* cell co-member with Q 112** — pure س monorhyme via *al-nās*-repetition; FR-centroid rank 6/114; corpus terminus. Files: [[Q114-al-nas/01-empirical-profile|01]], [[Q114-al-nas/02-content-analysis|02]], [[Q114-al-nas/03-tafsir-survey|03]], [[Q114-al-nas/04-hadith-corpus|04]], [[Q114-al-nas/05-classical-claims-audit|05]], [[Q114-al-nas/06-novel-findings|06]], [[Q114-al-nas/07-cross-references|07]]. Pre-reg tests (4/4 VINDICATED): **F-01 *iʿjāz-al-maʿnā* cell co-membership (all 4 cell-criteria met)** · **F-02 *al-nās* token-density rank 1/19 short surahs (0.20)** · **F-03 asymmetric FR-tightness Q 113 ↔ Q 114 VINDICATED — Q 114→Q 113 is #1 nearest, Q 113→Q 108 is #1 (NOT Q 114)** · **F-04 3-tier divine-aspect (rabb / mālik / ilāh) rules-tuple stable**. 5 classical claims audited (5/5 VINDICATED + 1 chain-graded ḍaʿīf): *muʿawwidhatān* pair + INTERNAL-evil refuge (vs Q 113 EXTERNAL) + Ibn Masʿūd omission tradition (canonicity vindicated, omission chain *ḍaʿīf*) + *iʿjāz al-maʿnā* cell co-member + 100% س monorhyme via repetition.

- **[[muawwidhat-cluster-synthesis|muʿawwidhāt cluster synthesis]]** (2026-04-28) — cluster-level synthesis for Q 112 + Q 113 + Q 114 (folk-extended muʿawwidhāt-3) and Q 113 + Q 114 (strict classical *muʿawwidhatān*). **Pre-registered cluster cohesion test VINDICATED at p=0.0006** (10000-perm null) — muʿawwidhāt-3 mean pairwise FR=0.290 vs null 0.920 (3.18× tighter). Strict pair Q 113-Q 114 cohesion VINDICATED at p=0.0033 (3.39× tighter than random pairs). Cluster spans **2 of 4 *iʿjāz*-cells**: Q 112 + Q 114 in *iʿjāz-al-maʿnā*, Q 113 in *iʿjāz-al-fawāṣil-pure*. Architectural unique cell-spanning property. Cluster cohesion json: `surahs/muawwidhat-cluster-cohesion.json`.

### Wave C — ḥawāmīm-7 cluster synthesis

- **[[hawamim-7-cluster-synthesis|ḥawāmīm-7 cluster synthesis]]** (2026-04-28) — cluster-level synthesis for Q 40-46 (the ḥawāmīm-7 letter-family).
  - PRIMARY pre-registered test [[h-new-901-hm7-cohesion-prereg|H-NEW-901]] NULL @ 21.21%ile (cohesive direction; sub-DIRECTIONAL).
  - HM-A {Q 40, 41, 42} high-rhyme-entropy (mean 2.375 bits) multi-rāwī vs HM-B {Q 43, 44, 45, 46} near-monorhyme (mean 0.766 bits ن-dominant).
  - Q 42 = corpus-unique two-verse muqaṭṭaʿāt (حم + عسق), HM-A apex, max sig_A in cluster (+1.27).
  - Q 41:53 = corpus-hapax *afaq*+*anfus* lexical pair (single attestation in 6,236 verses).
  - Q 42 → Q 43 canonical-adjacency cost = 0.2357 = 2× any other HM-7 transition; bifurcation seam.
  - Member overviews: [[Q040-ghafir/00-overview|Q 40]], [[Q041-fussilat/00-overview|Q 41]], [[Q042-al-shura/00-overview|Q 42]], [[Q043-al-zukhruf/00-overview|Q 43]], [[Q044-al-dukhan/00-overview|Q 44]], [[Q045-al-jathiyah/00-overview|Q 45]], [[Q046-al-ahqaf/00-overview|Q 46]].

### 4-cell typology (cross-finding-026 §13 amendment, 2026-04-28)

- **All-axis** cell: [[Q001-al-fatiha/00-overview|Q 1]] (high outlier + high TSP + high sig_A; *umm al-Kitāb*).
- **Structural-twin-pair** cell: [[Q024-al-nur/00-overview|Q 24]], [[Q033-al-ahzab/00-overview|Q 33]] (high outlier + bracketed top-15 adjacency BOTH SIDES + LOW sig_A; "outlier-without-fawāṣil-virtuosity").
- **iʿjāz-al-fawāṣil-pure** cell: Q 86, 89, 100, 106, **[[Q113-al-falaq/00-overview|Q 113]] (Wave-D 2026-04-28 confirmation, all 4 criteria met, [[Q113-al-falaq/Q113-F-01-fawasil-pure-cell|Q113-F-01]])** (high sig_A, moderate outlier; al-Bāqillānī *fawāṣil* exemplars).
- **iʿjāz-al-maʿnā** cell: **[[Q112-al-ikhlas/00-overview|Q 112]] (rank-1 FR-centroid exemplar, [[Q112-al-ikhlas/Q112-F-01-fr-centroid|Q112-F-01]])**, **[[Q114-al-nas/00-overview|Q 114]] (FR-centroid rank 6, co-member, [[Q114-al-nas/Q114-F-01-cell-co-member|Q114-F-01]])**, Q 67 (Wave-D 2026-04-28 confirmation) (low UAS, recitation-tradition / *faḍāʾil*-rich; *thuluth al-Qurʾān* / muʿawwidhāt / *al-Mānīʿa*).
- **iʿjāz-al-takrīr** *(5th-cell candidate — TESTED AND FALSIFIED as pre-registered by [[cross-finding-027-ijaz-al-takrir|cf-027-takrīr]], 2026-04-28; the typology stays at 4 cells + the Q 18 6th cell below)*: [[Q055-al-rahman/00-overview|Q 55]] (rank-1 refrain density + corpus-min sig_A) is *sui generis*, not a class head. *(Correction 2026-08-07: previously read "queued as cross-finding-027".)*
- **anti-iʿjāz-with-monolithic-rhyme-register** *(6th-cell, established by Wave-D Q 18)*: [[Q018-al-kahf/00-overview|Q 18]] (sig_A rank 110/114; 99.09% alif-monorhyme over 110 verses; cheaply-bracketed both sides; mid UAS via |sig_A| magnitude alone). Q 18 is the project's clearest case of "monolithic-register-sustained-over-large-N" as an architectural mechanism distinct from outlier-disruption (Q 24/Q 33), fāṣila-virtuosity (Q 33/Q 55), and recitation-tradition theological-iʿjāz (Q 67/Q 112).

### Falsifications and vindications (Wave A/B)

See [[MASTER-FINDINGS-LEDGER]] §9.8-9.10 for the 8 falsifications, 9 vindications, and 8 NEW corpus-wide structural facts. Headline:

- **Falsified**: Q 33 alif-monorhyme corpus-MAX; Q 9 no-mercy-no-basmala classical reasoning; Q 8+Q 9 unity (FR rank 81/113, MORE dissimilar than typical adjacent pairs); Q 5:3 as last-revealed-verse (lowest classical citation density of 4 candidates); Q 24:30-31 ↔ Q 33:53-59 ḥijāb parallelism (Jaccard 0.153, mutually exclusive technical terms); ʿarūs al-Qurʾān ḥadīth canonical-strength (graded ḍaʿīf); Khalifa Code-19 basmala-19-letters rules-tuple-fragile; Q 33:40 *khātam al-nabiyyīn* structural-focal-point rules-tuple-fragile.
- **Vindicated**: Q 1 *umm al-Kitāb* (multi-axis); Q 12 *aḥsan al-qaṣaṣ* (rank 1/114 narrative-purity); Q 9 *al-Faḍiḥa* (al-Bukhārī #4674; nfq rank 5/114); Q 24:35 Light-verse centrality (literal word-and-letter median); Q 9:128-129 as classical "last-revealed verse" by tafsir density (64/384); Q 33:21 *uswa ḥasana* as foundation of *sunna* doctrine; Q 55 31-fold refrain + dual-pronoun *thaqalān*; Q 1 FR-nearest = muʿawwidhāt cluster (al-Biqāʿī *Fātiḥa-bracket*); Q 12 + Q 55 = FR-MAXIMALLY-DISTANT (dual-iʿjāz orthogonality concretized).

---

## CLASSICAL SCHOLARS — anchor map (Wave A/B updates)

Augmenting the corpus-level anchor map above with per-surah Wave A/B vindications:

### al-Bukhārī (per-surah extensions)
- Q 1 *umm al-Kitāb* (#4474) — multi-axis VINDICATED at law-strength: [[Q001-al-fatiha/05-classical-claims-audit|Q 1 audit Claim 1]].
- Q 9 *al-Faḍiḥa* (#4674, Saʿīd b. Jubayr → Ibn ʿAbbās) — VINDICATED at p<10⁻⁶: [[Q009-al-tawba/05-classical-claims-audit|Q 9 audit Audit 3]] / [[Q009-al-tawba/06-novel-findings|Q009-F-02]].
- Q 2:255 *āyat al-kursī* greatest-verse (#4008) — RULES-TUPLE-FRAGILE: [[Q002-al-baqara/05-classical-claims-audit|Q 2 audit Claim 2]].
- Q 2 khawātim "kafatāhu" (#5009) — NULL on divine-name density: [[Q002-al-baqara/05-classical-claims-audit|Q 2 audit Claim 5]].

### al-Tirmidhī (per-surah extensions)
- Q 2 = *sanām al-Qurʾān* (#2878) — VINDICATED multi-metric: [[Q002-al-baqara/05-classical-claims-audit|Q 2 audit Claim 1]].
- Q 55 *ʿarūs al-Qurʾān* — actual source CORRECTED to Mishkāt #2083 / Bayhaqī's *Shuʿab*; canonical-strength FALSIFIED (graded ḍaʿīf): [[Q055-al-rahman/05-classical-claims-audit|Q 55 audit Claim 1]].
- Q 33 *fadāʾil*-silence — VINDICATED (10 citations vs dedicated *bāb*s for Q 36/55/67/112): [[Q033-al-ahzab/05-classical-claims-audit|Q 33 audit Claim 5]].

### al-Suyūṭī *al-Itqān* (per-surah extensions)
- Q 9 = 7th of al-sabʿ al-ṭiwāl — VINDICATED-WITH-NUANCE (outlier-rank 4/114 within the group): [[Q009-al-tawba/05-classical-claims-audit|Q 9 audit Audit 4]].
- Q 1 25+ alternate names catalog — descriptive observation flagged for cross-corpus correlation with UAS: [[Q001-al-fatiha/06-novel-findings|Q001-F-07]].

### al-Qurṭubī *al-Jāmiʿ li-aḥkām al-Qurʾān*
- Q 24 *maqṣūd* = chastity-and-covering — VINDICATED (60% of verses): [[Q024-al-nur/05-classical-claims-audit|Q 24 audit Audit 1]].
- Q 9 no-basmala 5-position debate — Position 5 (no-mercy-no-basmala) FALSIFIED at empirical density: [[Q009-al-tawba/05-classical-claims-audit|Q 9 audit Audit 2]].

### al-Ṭabarsī *Majmaʿ al-bayān*
- Q 24 named for light-density — VINDICATED at Bonferroni p < 10⁻⁶: [[Q024-al-nur/05-classical-claims-audit|Q 24 audit Audit 3]] / [[Q024-al-nur/06-novel-findings|Q024-F-01]].

### al-Thaʿlabī *al-Kashf wa-l-bayān*
- Q 24 letter/word counts (5,680 / 1,316 / 64) — VINDICATED at 1.3% / 0.2% precision against Hafs-Kufan no-tashkeel: [[Q024-al-nur/05-classical-claims-audit|Q 24 audit Audit 8]].

### al-Biqāʿī *Naẓm al-Durar*
- Q 2 scaffold-claim — REFINED to scaffold-as-outlier-anchor (Q 112 is actual centroid): [[Q002-al-baqara/05-classical-claims-audit|Q 2 audit Claim 4]].
- Q 24:35 structural midpoint (ring-tradition) — VINDICATED at literal word-and-letter median: [[Q024-al-nur/05-classical-claims-audit|Q 24 audit Audit 6]].
- Q 55 *ʿarūs al-Qurʾān* chapter-title codification — VINDICATED at honorific-uniqueness; isnād-canonical-strength FALSIFIED.

### al-Bayhaqī *Shuʿab al-Īmān*
- Q 55 *ʿarūs al-Qurʾān* (Mishkāt #2083) — primary classical attestation, graded ḍaʿīf: [[Q055-al-rahman/05-classical-claims-audit|Q 55 audit Claim 1]].

### al-Bāqillānī *Iʿjāz al-Qurʾān* (per-surah refinement)
- Q 24 sig_A = −0.79, rank 82/114 — *iʿjāz al-fawāṣil* claim FALSIFIED-locally for Q 24, VINDICATED-globally at corpus r=−0.86. The Q 24 case **motivated the Q-24-specialist's 4-cell typology amendment** (cross-finding-026 §13): [[Q024-al-nur/05-classical-claims-audit|Q 24 audit Audit 2]].

### al-Khaṭṭābī *iʿjāz al-maʿnā* (per-surah refinement)
- Q 33:56 *ṣalawāt verse* — empirically NOT-STRUCTURAL-DISTINCTIVE = liturgical-theological iʿjāz, not architectural: [[Q033-al-ahzab/05-classical-claims-audit|Q 33 audit Claim 3]] (concrete instance of theological-iʿjāz / structural-iʿjāz orthogonality).

### Landed NULL: [[cross-finding-027-ijaz-al-takrir|cf-027-takrīr]] (2026-04-28)

> **Correction 2026-08-07.** This section previously read "Queued: cross-finding-027 (in flight)" and gave the status as "5th-cell candidate, awaiting cross-surah evaluation." The test had in fact already landed on 2026-04-28. The result is recorded below, and the ID is disambiguated: `cf-027-takrīr` is the 2026-04-28 refrain axis, **not** `cf-027-formal`, the 2026-05-30 eponymy-independence law. See [[CROSS-FINDING-INDEX]].

The Q 55 specialist's proposed **iʿjāz al-takrīr** (refrain-iʿjāz) axis — empirically anchored by Q 55's 31-fold refrain + 23× dual-pronoun density + corpus-min sig_A — was tested at corpus level under SHA-locked pre-registration (`findings/cross-finding/cross-finding-027-prereg.md`, SHA 14b4ae88…) across candidate refrain-surahs (Q 26 *inna fī dhālika la-āyātan...*; Q 77 *wayl-un yawmaʾidh-in li-l-mukadhdhibīn*). Classical antecedents: al-Zamakhsharī *iqtisās*, al-Sakkākī *takrīr* in *Miftāḥ al-ʿulūm*.

**Verdict: FALSIFIED as pre-registered.** Of three Bonferroni-3 sub-tests at α=0.0167, only the Q 55 cross-corpus genre-distinctness cell passed (p=0.0038); the candidate-refrain set (Q 26, Q 77) failed to cluster with Q 55 on FR-roots, sig_A, or refrain-density combined-z. Under a post-hoc recurrence-restricted re-formulation (MW-7 capped) the axis is DIRECTIONAL on Q 55 alone — **Q 55 is *sui generis*, not the head of a multi-surah class.** The 5-cell promotion of cross-finding-026 §13 therefore did **not** happen; the typology stands at 4 cells plus the Q 18 6th cell. Full record: [[cross-finding-027-ijaz-al-takrir|cf-027-takrīr]] and `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` §13.5.

---

## METHODOLOGY GUARDS (MW-1..MW-7)

- **[[04-DISCIPLINE]]** — full methodology and pre-reg standards.
- **[[HONEST-LIMITS-LEDGER]]** — complete limit-acknowledgments.
- **[[TEAM-AMENDMENTS-LOG]]** — all in-flight pre-reg amendments.

---

## DEFINITIONS

- **Compression-tail**: the empirical phenomenon that content-cohesion-distance decreases monotonically toward the mushaf terminus, post Hijra-kink.
- **iʿjāz al-fawāṣil**: classical claim (al-Bāqillānī) — Quran's structural inimitability via fāṣila-variety + content-cohesion. Empirical signature: window-level anti-correlation r=-0.86 between content-cohesion-distance and rhyme-dispersion-distance.
- **iʿjāz al-maʿnā**: classical claim (al-Khaṭṭābī) — Quran's theological-content inimitability. Empirical signature: high content-density (Q 112, 114) without architectural distinctness.
- **Hijra-kink**: empirical 2-piece-linear breakpoint at s=50 (window-midpoint at Q 56/57). Coincides with classical Meccan/Medinan boundary.
- **Mufaṣṣal**: al-Zarkashī's terminology for Q 50-114 (or sometimes Q 48-114). Empirical compression-tail region.
- **Mufaṣṣal-qiṣār**: Q 78-114 (al-Suyūṭī) — empirical iʿjāz peak zone.
- **Tartīb tawqīfī**: doctrine that the mushaf-order is divinely ordained, not editorially chosen. Empirical signature: structural commitments beyond TSP-optimality (Q 1 first, terminal pair, Hijra hinge, etc.).
- **UAS** (Unified Architectural Significance): per-surah composite metric = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|).

---

## HOW TO USE THIS GRAPH

In Obsidian:
1. Open this file in Obsidian.
2. Click any `[[wikilink]]` to navigate.
3. Open the Graph View to see the connections visually.
4. Backlinks (right sidebar) show where each finding is referenced.
5. Tag-search: e.g., search for "iʿjāz" to find all related findings.

The argument structure is:
> Empirical laws (1-4 axes) → window-level anti-twinning (iʿjāz lock) → cross-corpus distinctness (Quran-specific) → per-surah architectural significance (dual typology) → classical-scholarship vindication (multiple anchors).

Each step is empirically grounded, pre-registered, and open to falsification.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
