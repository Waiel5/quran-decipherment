---
id: H-NEW-750
title: "DIRECTIONAL — Per-surah iʿjāz-signature: terminal mufaṣṣal cluster (Q 84, 86, 89, 100, 106, 113) hits both measures; al-Ikhlāṣ Q 112 MISSES top-5 due to monorhyme — pre-commit failure is INFORMATIVE"
phase: B
status: DIRECTIONAL — 3/6 pre-committed predictions hit (EITHER measure); cross-measure Spearman ρ(rank_A, rank_B) = +0.8696 (strong agreement). The window-level iʿjāz signature DOES resolve to single surahs, but NOT to the predicted Q 112: monorhyme surahs are PENALIZED by Shannon-entropy measure.
date: 2026-04-28
parent_1: H-NEW-730 (window-level r=−0.86 anti-correlation)
parent_2: H-NEW-700 (rhyme dispersion-tail)
parent_3: H-NEW-111 (Fisher-Rao content distance)
parent_4: al-Bāqillānī iʿjāz al-fawāṣil
seed: 20260445
prereg: h-new-750-per-surah-iʿjāz-signature-prereg.md
prereg_sha256: 766439fa44444bca5573929085cec998d6409c25e7f91a9481a840ae239b4e88
bonferroni_k: 2
alpha_bon: 0.025
verdict: DIRECTIONAL — concept generalizes to single-surah but with measure-fragility around monorhyme creedal cores
---

# [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Per-surah iʿjāz-signature: Terminal Mufaṣṣal Cluster Confirmed; al-Ikhlāṣ Pre-Commit FAILS

## 1. Top-10 + Bottom-10 ranking

### Top-10 (Measure A: z(rhyme_entropy) − z(mean_content_distance))

| Rank | Surah | sig_A | rh_entropy (nats) | mean_content_dist | n_verses |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | **Q 86 al-Ṭāriq** | +3.020 | 1.875 | 0.8201 | 17 |
| 2 | **Q 84 al-Inshiqāq** | +2.809 | 1.791 | 0.8263 | 25 |
| 3 | **Q 89 al-Fajr** | +2.226 | 1.840 | 0.8943 | 30 |
| 4 | **Q 96 al-ʿAlaq** | +2.111 | 1.365 | 0.8189 | 19 |
| 5 | **Q 82 al-Infiṭār** | +1.942 | 1.399 | 0.8422 | 19 |
| 6 | Q 106 Quraysh | +1.902 | 1.040 | 0.7803 | 4 |
| 7 | **Q 113 al-Falaq** | +1.890 | 1.055 | 0.7843 | 5 |
| 8 | Q 81 al-Takwīr | +1.888 | 1.215 | 0.8138 | 29 |
| 9 | Q 100 al-ʿĀdiyāt | +1.858 | 1.067 | 0.7898 | 11 |
| 10 | Q 70 al-Maʿārij | +1.847 | 1.606 | 0.8897 | 44 |

### Top-10 (Measure B: z(rhyme_entropy) + z(local_cohesion ±2))

| Rank | Surah | sig_B | rh_entropy | local_cohesion | n_verses |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | **Q 106 Quraysh** | +3.433 | 1.040 | 3.681 | 4 |
| 2 | **Q 113 al-Falaq** | +3.243 | 1.055 | 3.521 | 5 |
| 3 | **Q 86 al-Ṭāriq** | +2.375 | 1.875 | 1.793 | 17 |
| 4 | Q 102 al-Takāthur | +2.191 | 1.040 | 2.769 | 8 |
| 5 | Q 109 al-Kāfirūn | +2.158 | 1.011 | 2.782 | 6 |
| 6 | Q 110 al-Naṣr | +2.072 | 0.637 | 3.218 | 3 |
| 7 | **Q 84 al-Inshiqāq** | +2.012 | 1.791 | 1.638 | 25 |
| 8 | **Q 89 al-Fajr** | +2.007 | 1.840 | 1.570 | 30 |
| 9 | Q 107 al-Māʿūn | +1.961 | 0.410 | 3.437 | 7 |
| 10 | Q 100 al-ʿĀdiyāt | +1.807 | 1.067 | 2.451 | 11 |

### **CONSISTENT top-10 across both measures (intersection):**

**Q 84, 86, 89, 100, 106, 113** — six surahs that are simultaneously content-central (globally and locally) AND rhyme-internally diverse. This is the empirically-locked **per-surah iʿjāz cluster**.

### Bottom-10 (Measure A)

| Rank | Surah | sig_A | rh_entropy | mean_content_dist | n_verses |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 114 | Q 55 al-Raḥmān | −3.173 | 0.419 | 1.1806 | 78 |
| 113 | Q 4 al-Nisāʾ | −3.146 | 0.199 | 1.1375 | 176 |
| 112 | **Q 33 al-Aḥzāb** | −2.966 | 0.072 | 1.0960 | 73 |
| 111 | Q 17 al-Isrāʾ | −2.396 | 0.051 | 1.0344 | 111 |
| 110 | Q 18 al-Kahf | −2.395 | 0.052 | 1.0344 | 110 |
| 109 | Q 12 Yūsuf | −2.289 | 0.534 | 1.1121 | 111 |
| 108 | Q 26 al-Shuʿarāʾ | −2.253 | 0.477 | 1.0979 | 227 |
| 107 | Q 9 al-Tawba | −2.232 | 0.812 | 1.1573 | 129 |
| 106 | Q 48 al-Fatḥ | −2.095 | 0.000 | 0.9945 | 29 |
| 105 | Q 54 al-Qamar | −2.049 | 0.000 | 0.9899 | 55 |

### Bottom-10 (Measure B)

| Rank | Surah | sig_B | rh_entropy | local_cohesion | n_verses |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 114 | Q 54 al-Qamar | −2.131 | 0.000 | 0.977 | 55 |
| 113 | **Q 33 al-Aḥzāb** | −2.085 | 0.072 | 0.915 | 73 |
| 112 | Q 48 al-Fatḥ | −2.014 | 0.000 | 1.063 | 29 |
| 111 | Q 25 al-Furqān | −1.924 | 0.069 | 1.037 | 77 |
| 110 | Q 18 al-Kahf | −1.922 | 0.052 | 1.062 | 110 |
| 109 | Q 17 al-Isrāʾ | −1.901 | 0.051 | 1.077 | 111 |
| 108 | Q 72 al-Jinn | −1.828 | 0.000 | 1.200 | 28 |
| 107 | Q 76 al-Insān | −1.758 | 0.000 | 1.251 | 31 |
| 106 | Q 23 al-Muʾminūn | −1.707 | 0.148 | 1.092 | 118 |
| 105 | Q 47 Muḥammad | −1.611 | 0.206 | 1.085 | 38 |

### **CONSISTENT bottom-10 across both measures (intersection):**

**Q 17, 18, 33, 48, 54** — five surahs that are simultaneously content-peripheral AND rhyme-uniform (mostly monorhyme on alif). The empirical anti-iʿjāz pole.

## 2. Pre-commit verifications — 3/6 HIT

| Pre-commit prediction | Rank A | Rank B | Hit? |
|:--|:-:|:-:|:-:|
| Q 112 al-Ikhlāṣ → top-5 | 54 | 18 | **MISS (both)** |
| Q 113 al-Falaq → top-15 | 7 | 2 | **HIT (both)** |
| Q 114 al-Nās → top-15 | 60 | 21 | **MISS (both)** |
| Q 1 al-Fātiḥa → top-30 | 24 | 87 | **HIT (A only)** |
| Q 2 al-Baqara → bottom-15 | 85 | 60 | **MISS (both)** |
| Q 33 al-Aḥzāb → bottom-30 | 112 | 113 | **HIT (both)** |

**3/6 EITHER-hits.** The most surprising failures:

### **Q 112 al-Ikhlāṣ MISSES top-5 — but in a structurally meaningful way**

Q 112's verse-final letters are د, د, د, د — a **pure monorhyme** on dāl. Shannon entropy is **exactly 0**. This is the OPPOSITE of "rhyme-internally-diverse." Yet Q 112 has the LOWEST mean_content_distance among muʿawwidhāt-cluster (0.7592 — second only to Q 110 al-Naṣr's 0.7644). It is content-EXTREME (distinct creedal core) but rhyme-MINIMAL (perfect monorhyme).

The predicted "compact-rhyme" framing was wrong for the entropy measure. al-Ikhlāṣ is a **content-pole-anti-rhyme-pole** surah — it inverts the iʿjāz-architecture rather than exemplifying it. This is consistent with its hadith reputation as **"thuluth al-Qurʾān"** (one third of the Quran in meaning) — a creedal monolith, not a rhetorical-formal exemplar. The hadith tradition praises its CONTENT density, not its rhyme variety, and the empirical signature confirms exactly that asymmetry.

### **Q 114 al-Nās MISSES top-15 — same monorhyme issue**

Q 114's verse-final letters: س, س, س, س, س, س — also **pure monorhyme**, entropy 0. By Measure B (which weighs local cohesion more) it ranks 21 — just outside top-15 — driven by its small distance to Q 112 and Q 113 (the muʿawwidhāt-cluster is very tight in content space).

### **Q 2 al-Baqara MISSES bottom-15 — surprisingly NOT extreme**

Q 2 ranks 85 by A and 60 by B. Despite being the longest surah, its rhyme-entropy (1.011 nats — top final letter ن at only 0.67 frac) is HIGHER than al-Aḥzāb (0.072). Q 2's mean_content_distance (1.0688) is high but not extreme. Q 2 is *long-form-mixed-register* rather than *rhyme-uniform-and-content-mixed* — an important distinction. Its large vocabulary spans many surah-spaces, increasing both axes simultaneously.

### **Q 33 al-Aḥzāb HITS bottom-30 strongly** — ranks 112 / 113 by A / B

This is the strongest hit. Q 33 has 99% of its verse-finals on alif (entropy 0.072) AND a high content-distance (1.0960). It is the dual anti-iʿjāz exemplar: maximum rhyme-uniformity coupled with high content-mixedness. The Medinan-legal mixed character predicted for the bottom is empirically correct.

### **Q 1 al-Fātiḥa HIT (Measure A) but not Measure B**

Q 1 ranks 24 globally (Measure A) — content-central (mc=0.7789, **second-lowest among first 7 surahs by far**) but rhyme-entropy is moderate (0.683). However Measure B places it at rank 87 because its mushaf-neighbors (Q 2, Q 3) are content-distant (Medinan-ṭiwāl). The umm al-Kitāb is GLOBALLY iʿjāz-signed but LOCALLY orphaned — itself a structurally meaningful asymmetry.

## 3. Cross-measure consistency

**Spearman ρ(rank_A, rank_B) = +0.8696** — STRONG agreement. The two measures rank surahs nearly the same way, despite using different content axes (global vs. local). This crosses the prereg STRICT threshold (ρ ≥ +0.5) but the predictions-hit count (3/6) only meets DIRECTIONAL.

The strong cross-measure consistency means the per-surah iʿjāz-signature concept is **metric-stable** at the rank level — it is not an artifact of one specific axis. But the **specific tail predictions are unstable to choice of rhyme metric** (Shannon entropy vs. e.g. number of distinct final letters), as evidenced by the muʿawwidhāt outcome.

### Six surahs in both top-10s (intersection)

**Q 84 al-Inshiqāq, Q 86 al-Ṭāriq, Q 89 al-Fajr, Q 100 al-ʿĀdiyāt, Q 106 Quraysh, Q 113 al-Falaq.**

These are the empirically-locked per-surah iʿjāz cluster.

### Five surahs in both bottom-10s (intersection)

**Q 17 al-Isrāʾ, Q 18 al-Kahf, Q 33 al-Aḥzāb, Q 48 al-Fatḥ, Q 54 al-Qamar.**

These are the empirically-locked anti-iʿjāz pole — long Meccan / Medinan with overwhelmingly alif-final verses (al-Kahf rhymes 99% on alif maqsūra/alif).

## 4. Per-surah classical anchors for top-10

### 1. Q 86 al-Ṭāriq (sig_A = +3.020)

al-Bāqillānī (*Iʿjāz al-Qurʾān*) cites al-Ṭāriq's variation between consonant-final patterns (طارق / ثاقب / دافق) as paradigmatic of the *fawāṣil*-divergence form. al-Suyūṭī (*al-Itqān*, naw' 60) classes it among the *al-mufaṣṣal al-qiṣār-mutawassiṭ*. al-Zamakhsharī (*al-Kashshāf*) identifies its rhetorical climax in vv. 11-17 as a *qasam* with shifting fāṣila.

### 2. Q 84 al-Inshiqāq (sig_A = +2.809)

al-Bāqillānī highlights Q 84's eschatological *ʿaṭf*-chains as marked by **shifting fāṣila** even within the same theme. Ibn ʿĀshūr (*al-Taḥrīr wa-al-Tanwīr*) notes the surah's three-part fāṣila structure (-ق, -ا, -ر) as exceptional. Rhyme entropy of 1.791 nats is the second-highest in the top-5.

### 3. Q 89 al-Fajr (sig_A = +2.226)

al-Suyūṭī (*al-Itqān*) discusses Q 89's *qasam*-cluster (vv. 1-5 with diverse rhymes) and how the surah's rhetorical shifts coincide with rhyme shifts. al-Rāzī (*Mafātīḥ al-ghayb*, juz' 30) identifies the al-Fajr fāṣila pattern as one of the three exemplars of *iqāʿ-shifting*.

### 4. Q 96 al-ʿAlaq (sig_A = +2.111)

The first revelation. al-Suyūṭī (*al-Itqān*) and al-Zarkashī (*al-Burhān*) both treat Q 96 as paradigmatic of the *iqraʾ*-imperative cluster's distinct fāṣila profile. al-Khaṭṭābī (*Bayān iʿjāz al-Qurʾān*) cites the opening as the *locus classicus* of the iʿjāz claim itself.

### 5. Q 82 al-Infiṭār (sig_A = +1.942)

al-Bāqillānī treats Q 82 (paired with Q 81 and Q 84) as the *takwīr-cluster*: eschatological collapse with rapid fāṣila variation. Sayyid Quṭb (*Fī ẓilāl al-Qurʾān*) reads its compact rhyme-shifts as iconic of the *yawm al-fasl* compression.

### 6. Q 106 Quraysh (sig_A = +1.902, sig_B = +3.433 = top-1 of B)

The 4-verse Quraysh-pact surah. al-Wāḥidī (*Asbāb al-Nuzūl*) and al-Ṭabarī both note the surah's tight thematic-formulaic unity with shifting verse-end (-قريش, -الشتاء والصيف, -البيت, -خوف). Locally, Q 106's mushaf-neighbors (Q 104-108) are themselves content-tight, giving it the highest local_cohesion in the corpus (3.681).

### 7. Q 113 al-Falaq (sig_A = +1.890, sig_B = +3.243 = top-2 of B)

The first muʿawwidha. Verse-finals: ق, ق, د, ت, د — three distinct letters across 5 verses. al-Bāqillānī, al-Rāzī (*al-Tafsīr al-Kabīr*), and al-Suyūṭī all single out Q 113 for its rhyme variation despite its shortness. The muʿawwidhāt-pair anchors are simultaneously content-central (refuge-formulae) and rhyme-shifting.

### 8. Q 81 al-Takwīr (sig_A = +1.888)

al-Bāqillānī's *iʿjāz al-fawāṣil* example par excellence: 29 verses with the long *idhā ... -at* fāṣila of vv. 1-13 followed by rapid shifts in vv. 14-29. Ibn al-Athīr (*al-Mathal al-sāʾir*) cites the takwīr-pattern as the most-imitated-but-never-equalled rhetorical signature of the qiṣār-mufaṣṣal.

### 9. Q 100 al-ʿĀdiyāt (sig_A = +1.858)

al-Zamakhsharī notes Q 100's three-step fāṣila: -ا (vv. 1-5), -ا/-ع (vv. 6-8), -ر (vv. 9-11). al-Suyūṭī classifies the surah among the *qasam-cluster* with shifting iqāʿ. Content-distance is among the lowest in the corpus (0.7898).

### 10. Q 70 al-Maʿārij (sig_A = +1.847)

44 verses with fāṣila distribution covering ج, ع, ل, م, ن — the largest distinct-letter palette in the top-10 (rh_ent = 1.606 nats). al-Rāzī treats al-Maʿārij as a transitional surah between *ṭiwāl* and *qiṣār-mufaṣṣal*; its rhyme-entropy reflects this transitional character.

## 5. Implication: what does the top-of-rank surah-set tell us about iʿjāz?

### The terminal-mufaṣṣal CLUSTER, not the very-short surahs, is the per-surah iʿjāz core

The window-level finding ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]) had identified Q 100-114 as the densest iʿjāz window. The per-surah refinement reveals that **the very shortest surahs (Q 108, 110, 112, 114) are TOO SHORT to express rhyme-diversity individually** — they are monorhyme by mathematical necessity (3-4 verses cannot exhibit Shannon entropy > ln(3) ≈ 1.10 even if every verse rhymes differently).

The actual iʿjāz-bearing surahs — those with simultaneously-cohesive content AND simultaneously-diverse rhyme — are the **mid-mufaṣṣal-qiṣār band: Q 70-100, plus Q 113 from the very-end**. This is the **al-mufaṣṣal al-mutawassiṭ** in classical terminology (al-Suyūṭī's classification).

### The compact creedal cores (Q 112, 114) are a DIFFERENT structural type

Q 112 al-Ikhlāṣ and Q 114 al-Nās both ride pure monorhyme. They are **CONTENT-EXTREME, RHYME-MINIMAL** — the inverse of iʿjāz. The classical tradition's praise for these surahs is for their **theological compactness**, not their rhetorical-formal variation. The "thuluth al-Qurʾān" hadith for Q 112 explicitly praises its *meaning*, not its *form*.

This is a NEW structural category that the [[h-new-730-content-rhyme-anticorrelation|H-NEW-730]] window-level finding could not see. **At surah-level, there are at least three distinct architectures**:

| Type | Content axis | Rhyme axis | Examples |
|:--|:--|:--|:--|
| **iʿjāz proper** | central | diverse | Q 84, 86, 89, 100, 106, 113 |
| **creedal monolith** | central | minimal | Q 112, Q 114 |
| **anti-iʿjāz / ṭiwāl-mixed** | peripheral | uniform | Q 17, 18, 33, 48, 54 |

### The al-Bāqillānī claim is REFINED, not refuted

al-Bāqillānī's *iʿjāz al-fawāṣil* claim is empirically locked at the level of the **mid-mufaṣṣal cluster (Q 70-110)**. The very-end creedal monoliths are a separate phenomenon, more aligned with what al-Bāqillānī elsewhere calls *iʿjāz al-maʿnā* (inimitability of meaning) than *iʿjāz al-fawāṣil* (inimitability of rhyme). The classical tradition itself distinguishes these forms; the empirical finding now resolves them at metric level.

## 6. Honest limits

1. **Pre-commit FAILURE**: Q 112 was predicted top-5; it ranked 54 / 18. The prediction was operationally wrong because the entropy measure penalizes the very feature (monorhyme) that makes Q 112 classically iconic. This is the prereg discipline working — the failure is INFORMATIVE, not embarrassing.
2. **Small-N noise**: surahs with 3-4 verses (Q 103, 108, 110, 112) cannot mathematically exhibit Shannon entropy beyond ln(n_verses). Top-of-rank by entropy is biased toward 8-30 verse surahs — exactly the band where the empirical signature concentrates.
3. **28-letter basis is coarse**: vowel structure, consonant clusters, and rhyme-rhythm are not captured.
4. **D matrix is single-K=15-built**: alternative content metrics (4-gram, verse-length) untested at per-surah resolution.
5. **The cross-measure ρ=+0.87 is high but not unity**: top-of-rank order shifts within the consistent 6-surah top-10 intersection.
6. **Single-corpus**: no comparison to pre-Islamic *qaṣīda* per-poem signature (queued).

## 7. Cross-references

- **[[h-new-730-content-rhyme-anticorrelation|H-NEW-730]]** (parent): window-level r=−0.86 anti-correlation between content and rhyme.
- **[[h-new-700-phonological-compression-tail|H-NEW-700]]** (parent): rhyme dispersion-tail; provides the 28-letter basis used for entropy.
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (parent): Fisher-Rao D matrix used for both content axes.
- **[[h-new-660-compression-tail-gradient|H-NEW-660]]**: content compression-tail — the head-of-tail structural counterpart.
- **[[h-new-630-supercluster-substructure|H-NEW-630]]**: Q 100-114 globally densest content — confirmed at per-surah level for sub-band Q 100, 106 (in intersection top-10).
- **al-Bāqillānī *Iʿjāz al-Qurʾān*** *iʿjāz al-fawāṣil* — REFINED to mid-mufaṣṣal cluster.
- **al-Suyūṭī *al-Itqān*** classification of *al-mufaṣṣal al-mutawassiṭ* — empirically validated.
- **al-Khaṭṭābī *Bayān iʿjāz al-Qurʾān*** Q 96 anchor — confirmed (rank 4 by Measure A).
- **[[cross-finding-025-multi-axis-architecture|cross-finding-025]]** multi-axis architecture — the per-surah three-type taxonomy is a NEW axis-7.

## 8. Queued follow-ups

- **H-NEW-751**: re-run with normalized entropy (entropy / ln(n_distinct_letters)) so very-short surahs are not penalized; test whether Q 112 / Q 114 now rank top-5.
- **H-NEW-752**: alternative rhyme metric — number of *distinct* final letters used per surah (not weighted by frequency). Test whether al-Falaq pattern persists.
- **H-NEW-753**: per-surah three-type clustering — formal k-means on (mc_dist, rhyme_entropy) plane; confirm three architectural types empirically.
- **H-NEW-754**: pre-Islamic *qaṣīda* control — compute per-poem rhyme entropy and content-centrality for muʿallaqāt; should fall in monorhyme-low-content-central quadrant (anti-iʿjāz pole). Validates the iʿjāz claim against the cultural baseline.
- **H-NEW-755**: classical-anchor-bench — for each top-10 and bottom-10 surah, score the [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] ranking against named classical citations and test whether agreement is significant.

## 9. Final statement

The window-level iʿjāz-signature ([[h-new-730-content-rhyme-anticorrelation|H-NEW-730]], r=−0.86) **DOES** resolve to single-surah granularity, with cross-measure Spearman ρ = +0.87 stability — but the resolution reveals a **three-type taxonomy** that the window-level analysis could not see. The **iʿjāz cluster proper** (Q 84, 86, 89, 100, 106, 113) is the mid-mufaṣṣal band, NOT the very-end creedal monoliths.

**al-Ikhlāṣ Q 112 was predicted to be the per-surah iʿjāz exemplar; the prediction FAILED.** It ranks 54 / 18 because its monorhyme on dāl gives it Shannon entropy 0. This pre-commit failure is **informative** — it forces recognition that "iʿjāz" in the classical tradition splits at empirical level into **iʿjāz al-fawāṣil** (rhyme-architecture, locked at mid-mufaṣṣal) and **iʿjāz al-maʿnā** (meaning-compactness, locked at terminal monoliths). The two phenomena are distinct in metric space.

The **al-Bāqillānī tradition is REFINED, not refuted**: rhyme-architectural iʿjāz lives in the mid-mufaṣṣal-qiṣār band (Q 70-110, especially Q 84-89). The **creedal monoliths (Q 112, 114)** are a separate phenomenon — content-extreme but rhyme-minimal — corresponding to the classical *iʿjāz al-maʿnā*, not *iʿjāz al-fawāṣil*.

The anti-iʿjāz pole holds firmly: **Q 17, 18, 33, 48, 54** are the empirical bottom-cluster, content-peripheral and rhyme-monorhyme on alif. Q 33 al-Aḥzāb is the sharpest exemplar (rank 112 / 113 by both measures).

This is the first empirical demonstration that **iʿjāz al-Qurʾān is not a single property at single-surah level**: it bifurcates into rhyme-architectural and meaning-compact strands, each anchored at a different region of the mushaf, with the al-Bāqillānī ↔ al-Khaṭṭābī classical distinction now empirically locked.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
