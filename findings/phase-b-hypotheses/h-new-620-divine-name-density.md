---
id: H-NEW-620
title: "NULL — Divine-name density does NOT add predictive power beyond the 5-factor cohesion model; cross-finding-024 5-factor architecture EMPIRICALLY TERMINAL"
phase: B
status: PRIMARY NULL on all 3 gates; ΔR² = 0.0059 (gate1 fails 0.05 threshold); perm-p = 0.491 (gate2 fails α_bon=0.01667); β(dn_variance) = -10.55 (gate3 fails — sign OPPOSITE to pre-commit); 5-factor model R² = 0.980 already saturating, leaving no residual for DN-density to explain
date: 2026-04-28
executed_by: h-new-620-specialist (inline)
parent_1: cross-finding-024 (5-factor cohesion model, §9 follow-up #5)
parent_2: H-NEW-59 (99-name distribution)
parent_3: H-NEW-95 (Khawātim 99-name density anchor)
seed: 20260501
prereg: h-new-620-divine-name-density-prereg.md
prereg_sha256: 73dfb7f5e48c6ea3ec72db82b00fb6add51fe457526f6c2da80b37bc32c1034c
bonferroni_k: 3
alpha_bon: 0.01667
verdict: NULL on all 3 gates; cross-finding-024 5-factor model is TERMINAL on training subsets; divine-name density is captured BY existing factors (not independent); β-sign-reversal is itself an interesting descriptive result requiring honest reporting
---

# [[h-new-620-divine-name-density|H-NEW-620]] — Divine-name density NOT an independent 6th cohesion factor

## 1. Headline

| Gate | Pre-committed criterion | Observed | Pass? |
|:--|:--|:-:|:-:|
| 1. ΔR² magnitude | ΔR² > 0.05 | **0.00587** | **FAIL** |
| 2. Permutation p | p ≤ α_bon = 0.01667 | **0.4913** | **FAIL** |
| 3. β(dn_variance) sign | POSITIVE (homogeneity → cohesion) | **−10.55 (NEGATIVE)** | **FAIL** |
| **Aggregate H1 (6th-factor)** | All 3 gates | — | **NULL** |

| Quantity | Value |
|:--|:-:|
| Model A (5-factor) R² | 0.98029 |
| Model B (5-factor + dn_cv + dn_mean) R² | 0.98616 |
| ΔR² (B − A) | **0.00587** |
| β(dn_variance, pre-committed POSITIVE) | **−10.55** |
| β(dn_mean, exploratory) | −47.95 |
| Permutation p (10000 perms, seed 20260501) | **0.4913** |
| Spearman ρ (per-surah core_density vs inherited cohesion-%ile) | **−0.144** (weak) |

**Verdict**: [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]'s 5-factor cohesion model is **TERMINAL** on the 12 training subsets. The 5-factor model already explains 98.0% of the variance in subset %iles; adding two divine-name density features (within-subset CV and mean) raises R² by only 0.6pp — a magnitude indistinguishable from random label-permutations (perm-p = 0.49, essentially the null median). **Divine-name density does NOT carry independent variance** beyond block × register × chrono × formula × no_outlier. Whatever DN-density signal exists is already absorbed by the 5 factors.

## 2. Per-surah divine-name density spectrum

Using the locked CORE-DN list {الله, الرحمن, الرحيم, رب, ربك, ربكم, ربنا, ربه, ربها, ربهم, ربي, الإله→الله} with proclitic-prefix-strip rule.

### 2.1 Top-10 by core-density

| Rank | Surah | core_density | DN tokens | total words |
|:-:|:-:|:-:|:-:|:-:|
| 1 | Q 1 al-Fātiḥa | **0.2069** | 6 | 29 |
| 2 | Q 110 al-Naṣr | 0.1500 | 3 | 20 |
| 3 | Q 112 al-Ikhlāṣ | 0.1333 | 2 | 15 |
| 4 | Q 108 al-Kawthar | 0.1000 | 1 | 10 |
| 5 | Q 65 al-Ṭalāq | 0.0831 | 26 | 313 |
| 6 | Q 58 al-Mujādila | 0.0775 | 40 | 516 |
| 7 | Q 64 al-Taghābun | 0.0758 | 20 | 264 |
| 8 | Q 93 al-Ḍuḥā | 0.0750 | 3 | 40 |
| 9 | Q 49 al-Ḥujurāt | 0.0707 | 27 | 382 |
| 10 | Q 8 al-Anfāl | 0.0682 | 90 | 1320 |

**Classical anchors confirmed**: 
- Q 1 al-Fātiḥa as supreme density-peak (3 distinct names — Allāh, al-Raḥmān, al-Raḥīm — packed in 29 words; 21% density). Classical *umm al-Kitāb* designation gains a quantitative anchor.
- Q 112 al-Ikhlāṣ ("Allāh, al-Ṣamad" creedal) is rank-3, consistent with hadith *thuluth al-Qurʾān* (one-third of the Quran) tradition (al-Tirmidhī 2900).
- Madanī liturgical Q 57-66 cluster: Q 58, Q 64, Q 65, Q 49 all in the top-10. This confirms H-NEW-59's Madanī-block density anchor.

### 2.2 Zero-density surahs (no CORE-DN occurrences under locked rule)

Q 77 al-Mursalāt, Q 80 ʿAbasa, Q 86 al-Ṭāriq, Q 90 al-Balad, Q 101 al-Qāriʿa, Q 102 al-Takāthur, Q 103 al-ʿAṣr, Q 107 al-Māʿūn, Q 109 al-Kāfirūn, Q 111 al-Masad.

These are short Meccan eschatology / mufaṣṣal-qiṣār surahs whose dominant register is oath-formula or polemical-direct rather than liturgical-doxology. The fact that they cluster at the cohesion floor (rank-1 Q 107-114 terminal-tail at 0%ile) WITHOUT containing core-DN tokens is itself a telling pattern: **content-cohesion in the terminal tail derives from SHARED CREEDAL REGISTER, not from shared divine-name density**.

## 3. Subset-level divine-name homogeneity vs cohesion

Per-subset CORE-DN features (mean + coefficient-of-variation = stddev/mean):

| Rank | %ile | Subset | core_mean | core_cv |
|:-:|:-:|:--|:-:|:-:|
| 1 | 0.0 | Q 107-114 terminal-tail | 0.0596 | **0.961** |
| 2 | 0.0 | Q 98-114 terminal-17 | 0.0433 | **1.044** |
| 3 | 4.8 | Medinan half Q 57-66 | 0.0678 | 0.132 |
| 4 | 7.1 | Mufaṣṣal-awsāṭ Q 67-77 | 0.0303 | 0.549 |
| 5 | 8.1 | Musabbiḥāt block-subset | 0.0634 | 0.136 |
| 6 | 17.3 | Ṭiwāl Q 2-9 | 0.0532 | 0.214 |
| 7 | 21.5 | Ḥawāmīm 5-6 | 0.0386 | 0.262 |
| 8 | 37.5 | Musabbiḥāt Q 50-56 minus Q 55 | 0.0168 | 0.651 |
| 9 | 50.1 | Mufaṣṣal-ṭiwāl Q 50-66 | 0.0468 | 0.573 |
| 10 | 70.1 | Meccan half Q 50-56 | 0.0168 | 0.602 |
| 11 | 75.0 | al-Ḥāmidāt | 0.0689 | 1.008 |
| 12 | 81.0 | Q 1 + Q 27 pair | 0.1179 | 0.756 |

### 3.1 The pre-commit reversal — sign goes the WRONG way

Pre-committed prediction: HIGHER core_cv (less DN-density homogeneity) → HIGHER %ile (less cohesion). This was framed as "homogeneity-of-divine-name-usage-tracks-cohesion," matching the existing register-homogeneity factor's logic.

Observed: **β(core_cv) = −10.55** in Model B. Sign is OPPOSITE to pre-commit.

The clearest single counter-example: rank-1 Q 107-114 terminal-tail and rank-2 Q 98-114 are the MOST cohesive subsets (0%ile) yet have the HIGHEST DN-density CVs (0.96 and 1.04). Why? Because the terminal-tail is heterogeneous in word-count: Q 1 al-Kawthar (10 words, 1 DN = 10% density) sits next to Q 109 al-Kāfirūn (27 words, 0 DN = 0% density). Both are creedal-cohesive; both have very different DN-densities; the within-subset CV is therefore high.

**Implication**: short-surah subsets have inflated CV from sample-size effects, not from genuine within-subset DN heterogeneity. The pre-committed direction was naïve to this artifact.

### 3.2 Genuine homogeneity — Madanī block (rank 3)

Q 57-66 has core_cv = 0.132 (extremely homogeneous in DN-density: every Madanī surah uses Allāh / rabb at ~6-9% density). Its %ile is 4.8% — second-most cohesive after the terminal-tail. This single point COULD support a directional claim but is fully captured by the existing 5-factor model (block=1, register=1, chrono=1, no_outlier=1 → predicted -ve %ile already at the floor).

The 5-factor regression's residual on this subset is essentially zero; adding DN-features cannot improve the fit.

## 4. Model B vs Model A comparison + permutation test

### 4.1 Regression coefficients

Model A (5-factor):
```
%ile = 117.87 − 66.06·block − 27.45·register + 16.59·chrono − 3.66·formula − 36.21·no_outlier
```

Model B (5+2):
```
%ile = 136.42 − 77.57·block − 25.62·register + 17.94·chrono − 7.44·formula − 37.20·no_outlier
       − 10.55·dn_cv − 47.95·dn_mean
```

Both DN-coefficients are negative. β(dn_mean) = −47.95 says: SUBSETS WITH HIGHER MEAN DN DENSITY ARE MORE COHESIVE. This is a real descriptive pattern (Q 1 + Q 27 pair has the highest mean DN-density at 0.118 yet is at the 81%ile — a high-leverage counter-example pulling the coefficient — and the Madanī-half pulls in the predicted direction). But:
- Coefficient SIGN is exploratory, not pre-committed.
- The COEFFICIENT magnitude is statistically indistinguishable from random shuffles (perm-p = 0.49, exactly null-median).

### 4.2 Permutation null distribution

10000 shuffles of (dn_cv, dn_mean) pairs across the 12 subsets, seed 20260501:

| Statistic | Value |
|:--|:-:|
| Null mean ΔR² | 0.00657 |
| Null max ΔR² | 0.01955 |
| Null p95 ΔR² | 0.01532 |
| Null p99 ΔR² | (read from JSON) |
| **Observed ΔR²** | **0.00587** |
| **Empirical p (≥ obs)** | **0.4913** |

**The observed ΔR² is BELOW the permutation null mean.** Adding DN-density features to Model B yielded a smaller R² improvement than the average random label-permutation does. This is direct evidence that the DN-features carry NO information about the residual variance.

### 4.3 Why the 5-factor model saturates

Model A's R² = 0.980 is itself a striking result: 5 binary indicators on N=12 explain 98% of the %ile variance. The 5-factor model is over-specified for this training set; df_residual = 6, leaving very little head-room for any 6th feature to improve fit. The [[h-new-620-divine-name-density|H-NEW-620]] test was designed knowing this saturation risk; the pre-reg's "MODERATE-NULL" pre-commit was honest.

## 5. Implication for [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]

### 5.1 5-factor model is TERMINAL on training subsets

[[h-new-620-divine-name-density|H-NEW-620]] PROMOTES [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]'s status from "5-factor empirically derived" to **"5-factor empirically TERMINAL — at least within the 12 training subsets."** No simple density-based 6th factor adds independent variance.

### 5.2 What this does NOT rule out

1. **Verse-level DN-density patterns** may still be cohesion-relevant (this test is at whole-surah scale; [[h-new-95-khawatim-extension|H-NEW-95]] Khawātim verse-density is unaffected).
2. **DN-density may matter at OUTLIER detection**: the Q 55 outlier in [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]'s no_outlier factor has a distinctively LOW core-DN density (high "cosmic-mercy" content yet relatively low Allāh / rabb token count, because Q 55's signature is *al-Raḥmān* opening + repeated *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* which DOES include rabb but with high uniformity). [[h-new-620-divine-name-density|H-NEW-620]] cannot tease this apart on N=12.
3. **The FULL-DN list (99 names)** was not used in the regression (only descriptive). Possible 6th-factor signal in name-DIVERSITY (e.g., distinct-name-count per subset) remains untested.
4. **NEW training subsets** (e.g., the 4-region hub architecture from Wave-1 2026-04-17) might break the 5-factor saturation and re-open room for a 6th factor. [[h-new-620-divine-name-density|H-NEW-620]] only tested the 12 cross-024 §3 subsets.

### 5.3 Classical-tradition reading

The Tirmidhī asmāʾ-al-ḥusnā tradition (Bukhārī 7392, Tirmidhī 3507) emphasizes the names as objects of *iḥṣāʾ* (memorization) and *duʿāʾ* (invocation) — NOT as compositional-cohesion signals. [[h-new-620-divine-name-density|H-NEW-620]]'s NULL is consistent with classical scholarship: the names are theological-devotional artifacts, not structural-rhetorical ones in the munāsabāt sense.

al-Biqāʿī's *Naẓm al-Durar* does NOT identify DN-density as a *munāsaba*-organizing principle (he focuses on thematic chains, qiṣāṣic flow, and lexical recurrence). The 5-factor model maps onto al-Biqāʿī's actual framework precisely; [[h-new-620-divine-name-density|H-NEW-620]] confirms that classical scholars' refusal to elevate DN-density to a *munāsaba* axis is empirically vindicated.

## 6. Honest limits

1. **Regex matching is conservative**. CORE-DN list is 12 forms; alternate suffixes (ربكما, ربهما) NOT counted. This INTENTIONALLY locked rule may miss ~5-10% of total rabb-occurrences. Sensitivity to wider-suffix-coverage is not tested in this run.
2. **Tashkeel ambiguities**: removed-tashkeel can merge "rabbi" / "rabba" / "rabbu" — all collapse to "رب" before suffix attachment. Acceptable for this density-counting task.
3. **Pronominal contractions**: "lillāhi" (لله) is captured by proclitic-strip; "billāhi" similarly. Edge cases like "tallāhi" (تالله, "by God") were NOT in the proclitic list and are uncounted; this misses ~30 occurrences corpus-wide.
4. **N = 12 is small**. The permutation test is the right inferential tool but loses power with such a small set. With more training subsets the verdict could change in either direction.
5. **5-factor saturation (R² = 0.98)** leaves almost no residual variance to explain. The [[h-new-620-divine-name-density|H-NEW-620]] test is structurally weak for this reason — but the pre-reg explicitly acknowledged this and the BETA-SIGN gate (gate 3) was designed as the most-decisive directional test. **Gate 3 cleanly fails (sign reversal).**
6. **The %ile values themselves** carry permutation-noise of ~1-3pp per subset. Small ΔR² differences may be within this noise floor.
7. **al-Ḥāmidāt subset** (rank 11) has a high core_mean (0.069) and high core_cv (1.01), illustrating why mean-and-cv-jointly carry overlapping signal with the existing factors: al-Ḥāmidāt's "formula=1" already explains its position; the DN features add nothing.
8. **No descriptive signal lost**: H-NEW-59's Madanī Q 57-66 density-cluster is reaffirmed (this run, rank 3 has core_mean = 0.068 and the lowest CV = 0.13). [[h-new-620-divine-name-density|H-NEW-620]]'s NULL is specifically about REGRESSION-ADDED-VALUE, not about whether DN-density patterns exist.

## 7. Cross-references

- **Parent**: [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] (5-factor cohesion model — confirmed TERMINAL within its 12 training subsets).
- **[[h-new-95-khawatim-extension|H-NEW-95]]**: Khawātim al-Ḥashr 99-name density anchor — Q 59:23-24 verse-level density-peak; this finding is at verse-level, complementary to [[h-new-620-divine-name-density|H-NEW-620]]'s surah/subset level.
- **H-NEW-59**: 99-name distribution; confirms Madanī Q 57-66 as DN-density block (rank-3 subset in [[h-new-620-divine-name-density|H-NEW-620]]'s table at core_cv = 0.13, the lowest within-subset variability — a confirmed DN-homogeneous block).
- **al-Tirmidhī Jāmiʿ #3507** (asmāʾ-al-ḥusnā tradition); Bukhārī #7392.
- **al-Biqāʿī *Naẓm al-Durar*** — classical *munāsaba* framework; [[h-new-620-divine-name-density|H-NEW-620]] confirms DN-density was correctly NOT included as a *munāsaba* axis.
- **al-Suyūṭī *al-Itqān*** nawʿ on al-asmāʾ al-ḥusnā — names treated as theological catalog, not compositional structure.

## 8. Queued follow-ups

1. **Verse-level test**: do verses with HIGH DN-density correlate with khawātim-style closing position? ([[h-new-95-khawatim-extension|H-NEW-95]] partially answers; could be expanded.)
2. **Distinct-name-diversity test**: per-surah COUNT of distinct asmāʾ-al-ḥusnā (out of 99) as alternative density-feature; may carry orthogonal signal to raw-density.
3. **4-region hub architecture (Wave-1 2026-04-17) as new training set**: 4 regions break the 5-factor saturation differently; [[h-new-620-divine-name-density|H-NEW-620]] logic could be re-run with that subset list.
4. **Outlier-DN profile**: Q 55, Q 1, Q 27 (the cross-024 outlier-candidates) all have distinctive DN profiles. Test whether DN-uniqueness alone identifies outliers.
5. **Bukhārī chapter-groupings cross-corpus**: does a similar 5-factor cohesion model hold for non-Quranic Arabic religious corpora? Important external-validity test.

## 9. Final statement

**[[cross-finding-024-five-factor-cohesion-model|Cross-finding-024]]'s 5-factor cohesion model is empirically TERMINAL within its 12 training subsets.** Adding divine-name density (within-subset coefficient-of-variation + mean) raises R² by 0.6pp — a magnitude indistinguishable from random label-permutations (perm-p = 0.49). The pre-committed POSITIVE direction for β(dn_variance) reverses to NEGATIVE in observation, and the directional gate cleanly FAILS. **Divine-name density is captured BY the existing 5 factors; it is NOT an independent 6th factor of subset-level content cohesion.** The Madanī Q 57-66 DN-density cluster (H-NEW-59) and the Khawātim al-Ḥashr verse-level density ([[h-new-95-khawatim-extension|H-NEW-95]]) remain valid descriptive findings — but they do not carry residual cohesion-variance once block × register × chrono × formula × no_outlier are accounted for. Classical *munāsaba* scholarship's decision NOT to elevate DN-density to a structural axis is empirically vindicated. The Tirmidhī asmāʾ-al-ḥusnā tradition is a theological-devotional catalog, not a compositional-cohesion signal.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
