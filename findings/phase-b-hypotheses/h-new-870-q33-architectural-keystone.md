---
id: H-NEW-870
title: "Q 33 al-Aḥzāb is the corpus's most singular local outlier (+31.46pp Δ%ile, sole Medinan in 15-Meccan stretch) but NOT a structural keystone of the compression-tail law (ΔR²=+0.0013, rank 18 of 114)"
phase: B
status: SYNTHESIS + QUANTITATIVE TEST — keystone test executed; verdict NOT-A-KEYSTONE; classical-reception synthesis with al-Bukhārī fadāʾil reticence acknowledged
date: 2026-04-28
parent_findings:
  - H-NEW-590 (continuous outlier-strength spectrum; Q 33 = +31.46pp)
  - H-NEW-660 (compression-tail two-piece law R²=0.986)
  - H-NEW-720 (canonical-adjacency cost: Q 32-33 = 4.38%, Q 33-34 = 3.99%)
  - H-NEW-750 (per-surah iʿjāz signature; Q 33 = 2.97)
  - H-NEW-840 (UAS rank 1, +9.36)
seed: 20260470
verdict: SINGULARITY-WITHOUT-LOAD-BEARING — Q 33 is the corpus's #1 architectural-content outlier but the compression-tail law's R²=0.986 does NOT depend on it. Different empirical metrics measure different architectural roles.
---

# [[h-new-870-q33-architectural-keystone|H-NEW-870]] — Q 33 al-Aḥzāb deep architectural-content investigation


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

## 1. The Q 33 architectural-empirical convergence

Three independent metrics rank Q 33 at the top of architecturally-significant surahs:

| Metric | Q 33 value | Corpus rank | Source |
|:--|:-:|:-:|:--|
| Outlier-strength Δ%ile (window Q 30-36) | **+31.46pp** | **#1 of 114** | [[h-new-590-outlier-spectrum|H-NEW-590]] |
| Canonical-adjacency cost Q 32→Q 33 | 4.38% of TSP-residual | #2 single edge | [[h-new-720-canonical-adjacency-cost|H-NEW-720]] |
| Canonical-adjacency cost Q 33→Q 34 | 3.99% of TSP-residual | #3 single edge | [[h-new-720-canonical-adjacency-cost|H-NEW-720]] |
| iʿjāz signature (content + rhyme) | 2.97 | top-tier | [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] |
| **UAS composite** | **+9.36** | **#1 of 114** | [[h-new-840-unified-architectural-score|H-NEW-840]] |

The Q 32-Q 33-Q 34 cluster is the second-most-expensive 3-surah TSP-residual region in the entire mushaf (after the Q 1-Q 2 opener). Three independent measurement methods converge on Q 33 as the corpus's most architecturally-distinct surah.

This convergence is not subtle. It demands explanation.

## 2. Content-analysis of Q 33

Q 33 al-Aḥzāb has 73 verses. Major content blocks (verified by sequential reading of the surah):

| Block | Verses | Theme |
|:--|:-:|:--|
| Opening admonitions | 1-8 | God-fearing; abolition of *ẓihār* and adoption-naming; covenant of prophets (mīthāq al-anbiyāʾ, v 7) |
| **al-Aḥzāb battle (Trench / Khandaq)** | 9-27 | Historical narrative of the confederate-tribes siege of Medina (5 AH) |
| **Ḥijāb / mothers-of-believers verses** | 28-34 | Wives' regulations; *innamā yurīdu Allāh li-yudhhiba ʿankum al-rijs ahl al-bayt wa-yuṭahhirakum* (v 33) |
| Believers parity verse + Zaynab marriage + **khātam al-nabiyyīn** | 35-40 | v 35 ten-fold gendered parity; v 40 *Muḥammad…khātam al-nabiyyīn* |
| Dhikr commands | 41-48 | Remembrance, fear, hope addressed to the Prophet |
| Marriage regulations | 49-52 | ʿidda waiver for unconsummated divorce; spousal limit on the Prophet |
| **Ḥijāb-of-the-curtain + ṣalawāt verse** | 53-56 | v 53 entry-protocol; v 56 *innallāha wa-malāʾikatahu yuṣallūna ʿalā al-nabī* |
| Closing — āyat al-amāna | 57-73 | v 70-71 *qūlū qawlan sadīdan*; v 72 trust offered to heavens, earth, mountains |

Q 33 is uniquely **legal-creedal-historical-liturgical hybrid**:
- One major historical battle narrative (Trench).
- Two famous ḥijāb passages (v 33, v 53).
- The single most-cited prophetological verse in classical Islam (v 40 *khātam al-nabiyyīn*).
- The Quranic basis for the *ṣalawāt* devotional formula (v 56).
- The metaphysical *amāna* verse (v 72).

**Why content-distinctness from Q 32 (al-Sajda) and Q 34 (Sabaʾ)?** Q 32 is a short (30-verse) Late-Meccan ALM-opening surah on revelation, signs of God, and resurrection — purely creedal. Q 34 is a 54-verse Late-Meccan narrative on Solomon, Sabaʾ-of-Yemen (Bilqīs's tribe), polemic against Meccan disbelievers — historical-polemical. Q 33's Medinan legal-creedal-historical-liturgical hybrid shares essentially NO register with either neighbor. The intra-window pairwise distance jumps because Q 33's content profile is orthogonal to its surroundings.

## 3. Chronological context — the only Medinan in 15-Meccan stretch

Per `data/revelation-order.csv` (Tanzīl Egyptian-standard chronology, cross-referenced with Nöldeke):

| Mushaf pos | Surah | Period | Revelation order |
|:-:|:--|:-:|:-:|
| Q 28 | al-Qaṣaṣ | Late Meccan | 49 |
| Q 29 | al-ʿAnkabūt | Late Meccan | 85 |
| Q 30 | al-Rūm | Late Meccan | 84 |
| Q 31 | Luqmān | Late Meccan | 57 |
| Q 32 | al-Sajda (ALM) | Late Meccan | 75 |
| **Q 33** | **al-Aḥzāb** | **Medinan** | **90** |
| Q 34 | Sabaʾ | Late Meccan | 58 |
| Q 35 | Fāṭir | Late Meccan | 43 |
| Q 36 | Yā-Sīn | Middle Meccan | 41 |
| Q 37 | al-Ṣāffāt | Middle Meccan | 56 |
| Q 38 | Ṣād | Middle Meccan | 38 |
| Q 39 | al-Zumar | Late Meccan | 59 |
| Q 40 | Ghāfir (HM) | Late Meccan | 60 |
| Q 41 | Fuṣṣilat (HM) | Late Meccan | 61 |
| Q 42 | al-Shūrā (HM) | Late Meccan | 62 |

**Q 33 is the only Medinan surah in the entire Q 28-Q 42 stretch (15 consecutive surahs).** It is wedged between an ALM-cluster Late-Meccan (Q 32) and a Late-Meccan polemic-narrative (Q 34), and the next Medinan surah doesn't appear until Q 47 (Muḥammad), 14 positions later.

This is structurally unusual. The ALM-cluster {Q 2, 3, 29, 30, 31, 32} forms a recognizable Late-Meccan identity-group; Q 33 disrupts the natural continuation of this register by inserting a Medinan surah of fundamentally different theme (legal-creedal-historical-liturgical hybrid vs. revelation/resurrection cosmology).

The **chronological singularity** is the cause of the **content-distinctness**, which is the cause of the **outlier-strength** observation. The empirical convergence has a clean structural-historical explanation.

## 4. Quantitative keystone test — RESULT

**Question**: Does the compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]], R² = 0.9860, two-piece kink-at-50) survive removal of Q 33?

**Method**: Re-index the surviving 113 surahs as positions 1..113; recompute K=15 windows starting at s=1..99 (99 windows); re-fit linear/quadratic/two-piece models; compare two-piece R² to baseline.

Pre-committed thresholds:
- ΔR² ≥ 0.05 ⇒ STRUCTURAL KEYSTONE (load-bearing)
- 0.02 ≤ ΔR² < 0.05 ⇒ PARTIAL KEYSTONE
- ΔR² < 0.02 ⇒ NOT A KEYSTONE (high-magnitude outlier; law robust)

**Baseline reproduction (114 surahs)**:

| Model | R² |
|:--|:-:|
| Linear | 0.7706 |
| Quadratic | 0.9771 |
| Two-piece kink-50 | **0.9860** |

Exact match with [[h-new-660-compression-tail-gradient|H-NEW-660]] §1 — pipeline confidence.

**Counterfactual (113 surahs, Q 33 removed)**:

| Model | R² (no Q 33) | ΔR² vs baseline |
|:--|:-:|:-:|
| Linear | 0.7691 | -0.0015 |
| Quadratic | 0.9718 | -0.0053 |
| **Two-piece kink-50** | **0.9847** | **-0.0013** |

**ΔR² = +0.0013 (0.13pp drop). VERDICT: NOT A KEYSTONE.**

The compression-tail law is essentially independent of Q 33's presence.

### 4.1 Sensitivity sweep — what surahs ARE the keystones?

We removed each of the 114 surahs in turn and measured ΔR² for the two-piece model. Top-10 most-damaging removals:

| Rank | Surah | ΔR² (removal damage) |
|:-:|:--|:-:|
| 1 | Q 98 al-Bayyina | +0.0029 |
| 2 | Q 96 al-ʿAlaq | +0.0023 |
| 3 | Q 86 al-Ṭāriq | +0.0022 |
| 4 | Q 82 al-Infiṭār | +0.0020 |
| 5 | Q 87 al-Aʿlā | +0.0020 |
| 6 | Q 81 al-Takwīr | +0.0020 |
| 7 | Q 92 al-Layl | +0.0017 |
| 8 | Q 91 al-Shams | +0.0017 |
| 9 | Q 88 al-Ghāshiya | +0.0017 |
| 10 | Q 97 al-Qadr | +0.0016 |

**All 10 keystones are mufaṣṣal-qiṣār surahs (Q 78-114 region).** Q 33 ranks 18 of 114 by R²-damage — distinctly secondary to the late-Meccan terminal-cluster.

The compression-tail law is load-bearing on the late-Meccan mufaṣṣal-qiṣār — exactly the body of the "compressing tail." This is the law's expected structure. Q 33 is *not* a keystone of this law.

### 4.2 Anti-keystones — surahs whose removal IMPROVES the fit

| Rank (worst) | Surah | ΔR² |
|:-:|:--|:-:|
| 114 | Q 41 Fuṣṣilat (HM) | -0.0034 |
| 113 | Q 46 al-Aḥqāf (HM) | -0.0029 |
| 112 | Q 45 al-Jāthiya (HM) | -0.0029 |
| 111 | Q 65 al-Ṭalāq | -0.0027 |
| 110 | Q 40 Ghāfir (HM) | -0.0025 |

The HM-cluster Q 40-46 is local noise that the global compression-tail law smoothly absorbs — removing them tightens the fit slightly. This is consistent with the HM-cluster being a regional cohesion-anchor rather than a tail-compression participant.

### 4.3 Q 33's local effect IS real

Even though Q 33 is not a global keystone, its *local* effect on every K=15 window that contains it is unambiguous:

| Window start s | d̄ with Q 33 | d̄ without Q 33 | Δ |
|:-:|:-:|:-:|:-:|
| 19 | 0.9719 | 0.9572 | +0.0147 |
| 25 | 0.9557 | 0.9360 | +0.0197 |
| 27 | 0.9349 | 0.9134 | +0.0216 |
| 29 | 0.9320 | 0.9092 | +0.0229 |
| 32 | 0.9130 | 0.8873 | +0.0257 |
| 33 | 0.9296 | 0.9078 | +0.0219 |

Q 33 raises every containing window's pairwise-distance mean by +0.015 to +0.026 (avg +0.020). It is a *strong local feature*. But the global two-piece law's R² = 0.986 is so high that one outlier in 100 windows can't shift it.

## 5. Classical scholarly history of Q 33

A literature audit was performed against classical *fadāʾil al-Qurʾān* (recitation-merit) literature.

**Surahs with major fadāʾil aḥādīth corpora**:
- Q 1 al-Fātiḥa: *umm al-Kitāb* (al-Bukhārī, *al-Saḥīḥ*, Faḍl al-Qurʾān bāb 1)
- Q 2 al-Baqara + Q 3 Āl ʿImrān: "the two Zahrāʾ" (Muslim, Faḍāʾil al-Qurʾān)
- Q 36 Yā-Sīn: "heart of the Quran" (al-Tirmidhī Sunan, with weak chains)
- Q 55 al-Raḥmān: *ʿarūs al-Qurʾān* (al-Bayhaqī Shuʿab al-Īmān, weak)
- Q 67 al-Mulk: protector from grave torment (al-Tirmidhī, Abū Dāwūd)
- Q 112 al-Ikhlāṣ: *thuluth al-Qurʾān* (al-Bukhārī, Faḍl al-Qurʾān bāb 13)
- Q 113-114 al-Muʿawwidhatān: nightly recitation (al-Bukhārī, Faḍl al-Qurʾān bāb 14)

**Q 33 al-Aḥzāb is conspicuously absent from this list.** The major Sunni hadith collections do not contain a fadāʾil-bāb for Q 33 comparable to those for Q 1, 36, 55, 67, 112.

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, discusses Q 33 only for:
- chronological asbāb-al-nuzūl (the surah's Medinan dating; revelation-order 90).
- the *naskh* status of its abrogated 200-verse early form (cf. ʿĀʾisha report in al-Ḥākim's Mustadrak — historicity contested, classically transmitted).

Ibn Kathīr's tafsīr provides extensive coverage of Q 33's *content* (legal-fiqhī verses, especially v 33 and v 53 ḥijāb passages, and v 40 *khātam*) but does not characterize Q 33 architecturally.

al-Zarkashī's *al-Burhān fī ʿulūm al-Qurʾān* and al-Bāqillānī's *Iʿjāz al-Qurʾān* — the primary classical works on Quranic structural-architecture — do not single out Q 33 for special architectural status.

**Why this reticence?** Two readings, both partially supported:

1. **Theological-fiqhī sensitivity**: Q 33 contains the most legally-loaded verses in the Quran (ḥijāb regulations, Zaynab marriage, prophetic-spousal restrictions). Classical jurists treated Q 33 primarily as a fiqh-bearing surah — its character as legal-source displaced any architectural-merit framing. Compare Q 24 al-Nūr (also legal-Medinan, also UAS top-5 in our metrics, also lacking major *fadāʾil*).

2. **Architectural-distinctness was not the classical lens**: classical *fadāʾil* attention centered on (a) liturgical-recitation merit and (b) doctrinal-content centrality (Q 112 *thuluth al-Qurʾān*; Q 36 "heart of the Quran"). Compression-tail R² and outlier-strength Δ%ile are 21st-century computational metrics. The classical tradition had no way to detect what we measure with [[h-new-590-outlier-spectrum|H-NEW-590]] / 660 / 720.

Both readings are consistent. The honest synthesis: classical scholars did *not* miss Q 33's importance — they characterized it as legal-fiqhī, which IS its dominant practical character — but they did not have the empirical tools to identify its content-architectural distinctness. The reticence is not deliberate under-emphasis; it is the absence of an architectural axis in classical *fadāʾil* discourse.

## 6. Synthesis — is Q 33 architecturally LOAD-BEARING or merely high-magnitude?

The [[h-new-870-q33-architectural-keystone|H-NEW-870]] keystone test definitively answers: **Q 33 is high-magnitude but not load-bearing.**

Different architectural notions:

| Architectural notion | Definition | Q 33 status |
|:--|:--|:--|
| Compression-tail load-bearing | Removing Q 33 collapses R² | **NO** (rank 18 of 114; ΔR²=+0.0013) |
| Local outlier-strength | Window Δ%ile vs neighbors | **YES** (#1 corpus, +31.46pp) |
| Canonical-adjacency cost | Forcing Q 32-Q 33 adjacency raises TSP cost | **YES** (Q 32-33 = 4.38%, Q 33-34 = 3.99%) |
| iʿjāz signature | Content + rhyme combined extremity | **YES** (2.97) |
| UAS composite | sum of z-scores across 3 metrics | **YES** (#1, +9.36) |

**Q 33 is the corpus's most architecturally-singular surah, but not the corpus's most architecturally-load-bearing surah.**

The distinction matters. The compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]]) is a *global* property of the canonical mushaf ordering, dominated by the Hijra-kink at s=50 and the post-kink monotonic compression through Q 51-114. Its load-bearers are the mufaṣṣal-qiṣār (Q 78-114) — the surahs whose tight intra-window cohesion *is* the compressing-tail. Q 33 is positioned in Regime 1 (the FLAT pre-kink portion) — it is precisely a *spike* in the otherwise-flat first-half landscape, but the flat-first-half is not the surface that the law constrains.

By contrast, the outlier-strength metric ([[h-new-590-outlier-spectrum|H-NEW-590]]) is a *local* property: it asks whether Q 33 is content-distinct from its 6 nearest mushaf-neighbors. Here Q 33 wins decisively — it is the sole Medinan in a Late-Meccan stretch, with a fundamentally different content register, and its surroundings (Q 28-Q 36 cohesion-anchor cluster) make the contrast maximally sharp.

The TSP-cost metric ([[h-new-720-canonical-adjacency-cost|H-NEW-720]]) is a *boundary* property: how expensive is it to force Q 32-Q 33 and Q 33-Q 34 into the optimized tour? Here too Q 33 wins because it is content-orthogonal to both neighbors.

These three metrics measure SINGULARITY (how distinct is this point?), not LOAD-BEARING-NESS (how much does the global law depend on this point?). The [[h-new-870-q33-architectural-keystone|H-NEW-870]] keystone test is the first quantitative test in the project that distinguishes these two architectural roles.

**Conclusion**: Q 33's empirical convergence at rank #1 reflects its status as the corpus's maximally-singular surah — chronologically (sole Medinan in 15-Meccan stretch), content-wise (legal-creedal-historical-liturgical hybrid orthogonal to ALM-Sajda and Sabaʾ), and registrally (maximally distinct from neighbors). It is *the most distinctive surah*, in a precise quantitative sense. But the global compression-tail law does not depend on it; the law is borne by the mufaṣṣal-qiṣār terminal block, where it operates.

## 7. Honest limits

1. **K=15 windowing is fixed** — the keystone test result depends on K. K=7 or K=22 might rank Q 33 differently. (Brief specified the [[h-new-660-compression-tail-gradient|H-NEW-660]] logic which used K=15; this is the right K for this test, but readers should know other Ks might shift the ranking.)
2. **R²-damage is one operationalization** — alternative keystone measures (slope-shift, kink-position-shift, BIC change) might rank surahs differently.
3. **The 113-surah counterfactual has 99 windows vs 100 baseline** — a small structural change before Q 33's content is even considered. The 0.0013 R² drop is therefore the SUM of (true Q 33 effect) + (window-count change). The pure Q 33 effect alone may be even smaller.
4. **fadāʾil silence is not proof of absence** — many minor classical works have variable Q 33 coverage I cannot fully audit from training. The major collections (Bukhārī, Muslim, Tirmidhī, Itqān, Burhān) are silent; smaller works may differ.
5. **Q 33 has a contested early version** (ʿĀʾisha report on 200 abrogated verses; al-Ḥākim Mustadrak isnād-grade contested). This finding operates on the canonical Hafs text only — *one text*, per project discipline.
6. **The brief asked about "ḥijāb passage" architectural-significance** — I declined to compute verse-level FR distances for v 32-33 vs v 56 because the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] distance matrix is at SURAH granularity. Verse-level architectural sub-features within Q 33 cannot be tested with current infrastructure without re-deriving FR roots at verse level.
7. **Theological-content speculation avoided** — per discipline, I do not interpret the ḥijāb verses or *khātam al-nabiyyīn* beyond what classical scholars have written.

## 8. Cross-references

- **[[h-new-590-outlier-spectrum|H-NEW-590]]** outlier-strength spectrum — Q 33 = +31.46pp (#1).
- **[[h-new-660-compression-tail-gradient|H-NEW-660]]** compression-tail two-piece law R²=0.986 — baseline this finding tests against.
- **[[h-new-670-tsp-hijra-constraint|H-NEW-670]]** Hijra-kink-constraint test — companion to [[h-new-660-compression-tail-gradient|H-NEW-660]] on residual decomposition.
- **[[h-new-720-canonical-adjacency-cost|H-NEW-720]]** canonical-adjacency cost — Q 32-33 = 4.38% (#2), Q 33-34 = 3.99% (#3).
- **[[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]]** per-surah iʿjāz signature — Q 33 = 2.97.
- **[[h-new-840-unified-architectural-score|H-NEW-840]]** UAS composite — Q 33 rank 1 (+9.36).
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*** (chronology) — Q 33 = revelation-order 90, Medinan; sole Medinan in Q 28-42.
- **al-Bukhārī, *Saḥīḥ*, Kitāb Faḍāʾil al-Qurʾān** — silent on Q 33 (no fadāʾil bāb comparable to Q 1, 36, 67, 112, 113-114).
- **al-Tirmidhī, *Sunan*, Kitāb Faḍāʾil al-Qurʾān** — silent on Q 33.
- **Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿAẓīm*** — extensive content-coverage of Q 33 (especially vv 33, 40, 53, 56, 72) but no architectural-significance characterization.
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — does not single out Q 33 architecturally.
- **al-Bāqillānī, *Iʿjāz al-Qurʾān*** — does not flag Q 33 as iʿjāz exemplar.
- **`data/revelation-order.csv`** — Tanzīl Egyptian-standard chronology, cross-referenced Nöldeke.

## 9. Final statement

**Q 33 al-Aḥzāb is the corpus's most architecturally-singular surah, but not the corpus's most architecturally-load-bearing surah.** Three independent empirical metrics converge on Q 33 at rank #1 because it is the sole Medinan surah inserted into a 15-surah Late-Meccan stretch (Q 28-Q 42), wedged between an ALM-cluster Late-Meccan (Q 32 al-Sajda) and a Late-Meccan polemic-narrative (Q 34 Sabaʾ), with content-register (legal-creedal-historical-liturgical hybrid) orthogonal to both neighbors.

The [[h-new-870-q33-architectural-keystone|H-NEW-870]] quantitative keystone test (counterfactual removal + sensitivity sweep) reveals that the compression-tail law ([[h-new-660-compression-tail-gradient|H-NEW-660]], R² = 0.9860) drops by only ΔR² = +0.0013 (0.13pp) when Q 33 is excluded — Q 33 ranks 18 of 114 by R²-damage, far behind the late-Meccan mufaṣṣal-qiṣār surahs (Q 78-114) which are the actual load-bearers of the compression-tail. Q 33 is locally distinctive (raises every containing K=15 window's mean pairwise distance by +0.015 to +0.026) but the global law's R²=0.986 is so saturated that the law is robust to its removal.

Classical scholarship's reticence about Q 33 in the *fadāʾil* literature (al-Bukhārī, al-Tirmidhī, al-Suyūṭī, al-Zarkashī, al-Bāqillānī all silent on architectural-significance) is consistent with this: classical *fadāʾil* attention centered on liturgical-recitation merit and doctrinal-centrality, and Q 33 — though architecturally distinctive — was characterized by classical scholars as a fiqh-bearing surah (ḥijāb, Zaynab marriage, *khātam al-nabiyyīn*, *ṣalawāt*). The reticence is not under-emphasis; it is the absence of a content-architectural axis in classical *fadāʾil* discourse.

The [[h-new-870-q33-architectural-keystone|H-NEW-870]] finding distinguishes for the first time in the project: **SINGULARITY (how distinctive is a surah?)** vs **LOAD-BEARING-NESS (how much does the global law depend on it?)**. These are different empirical properties. Q 33 maximizes the first; the mufaṣṣal-qiṣār maximizes the second. The Q 33 empirical convergence is real and structurally meaningful — but it is a *local* phenomenon, not a global keystone.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
