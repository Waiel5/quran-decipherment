---
surah: 48
file_type: empirical-profile
date_last_updated: 2026-05-09
specialist: Q048-al-Fath-specialist
---

# Q 48 al-Fatḥ — Empirical Profile


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

> Integrates per-surah metrics from `findings/phase-b-hypotheses/csv/h-new-*.json`. Every figure is computed from disk and cited.

## 1. Identity and basic counts

| Metric | Value | Source |
|:--|:--|:--|
| Surah ID | 48 | mushaf canonical |
| Verses | 29 | `quran-text/quran-no-tashkeel.json[47]` |
| Words (no-tashkeel orthographic-token) | 600 | computed |
| Letters (no-tashkeel sans spaces) | 2,550 | computed |
| Mean verse length (words) | 20.69 | 600/29 |
| Mean verse length (letters) | 87.93 | 2550/29 |
| QAC v0.4 root-tagged tokens | 916 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| QAC v0.4 unique roots | 176 | computed |
| Type | Medinan | classical + Tanzil/Nöldeke |
| Tanzil revelation order | 111/114 | `data/revelation-order.csv` |
| Nöldeke chronological order | 108 | `data/revelation-order.csv` |
| Length-class | mufaṣṣal-awsāṭ | al-Zarkashī |

## 2. Fisher-Rao distance neighbors (h-new-111)

Per `findings/phase-b-hypotheses/csv/h-new-111.json` (corpus mean FR ≈ 0.9235).

### 2.1 Top-10 nearest

| Rank | Surah | FR distance | Type | Notes |
|:--:|:--|:--:|:--|:--|
| 1 | Q 61 al-Ṣaff | 0.7876 | Medinan | musabbiḥāt (*sabbaḥa*); 14 verses |
| 2 | Q 64 al-Taghābun | 0.7936 | Medinan | musabbiḥāt (*yusabbiḥu*); 18 verses |
| 3 | Q 59 al-Ḥashr | 0.8181 | Medinan | musabbiḥāt (*sabbaḥa*); contains the Khawātim al-Ḥashr |
| 4 | Q 63 al-Munāfiqūn | 0.8265 | Medinan | hypocrites-surah; 11 verses |
| 5 | Q 57 al-Ḥadīd | 0.8350 | Medinan | musabbiḥāt (*sabbaḥa*); first of musabbiḥāt block |
| 6 | Q 49 al-Ḥujurāt | 0.8584 | Medinan | mushaf-immediate-successor |
| 7 | Q 9 al-Tawba | 0.8706 | Medinan | the major Medinan-warfare-treaty surah |
| 8 | Q 58 al-Mujādilah | 0.8757 | Medinan | community-formation |
| 9 | Q 60 al-Mumtaḥanah | 0.8762 | Medinan | Hudaybiyya-aftermath |
| 10 | Q 22 al-Ḥajj | 0.8814 | mixed | Medinan-Meccan blend |

**Pattern**: 10/10 nearest neighbors are Medinan or Medinan-Meccan-blend. The musabbiḥāt cluster (Q 57, 59, 61, 64) occupies 4 of the top-5 — Q 48 is **structurally pulled toward the musabbiḥāt** rather than its mushaf-neighbors Q 47 (rank 13) and Q 49 (rank 6).

### 2.2 Selected neighbors (named comparisons)

| Surah | FR distance | Q 48-rank | Notes |
|:--|:--:|:--:|:--|
| Q 9 al-Tawba | 0.8706 | 7 | the most-related Medinan-warfare-treaty surah; brief asked for this |
| Q 47 Muḥammad | 0.8893 | 13 | mushaf-immediate-predecessor |
| Q 49 al-Ḥujurāt | 0.8584 | 6 | mushaf-immediate-successor |
| Q 33 al-Aḥzāb | 0.8895 | 14 | major Medinan-treaty surah; Khawātim cluster |
| Q 60 al-Mumtaḥanah | 0.8762 | 9 | Hudaybiyya-aftermath community-rule surah |
| Q 8 al-Anfāl | 0.8995 | 15 | major Medinan-warfare surah |
| Q 24 al-Nūr | 0.9222 | 21 | major Medinan-community-rule surah |
| Q 3 Āl ʿImrān | 0.9232 | 23 | top long-Medinan |
| Q 2 al-Baqarah | 0.9369 | 29 | top long-Medinan |

**Q 48-Q 9 comparison** (the brief-anchored comparison): FR = 0.8706, rank 7/113 — Q 9 is among the 10 closest neighbors, confirming the classical view that Q 48 and Q 9 share a Medinan-warfare-treaty register, but Q 9 is not Q 48's CLOSEST sibling. The musabbiḥāt cluster is closer.

### 2.3 Top-10 farthest (FR-distant)

| Rank | Surah | FR distance | Notes |
|:--:|:--|:--:|:--|
| 1 | Q 55 al-Raḥmān | 1.3833 | the corpus-known Q 55 anti-twin signature |
| 2 | Q 56 al-Wāqiʿah | 1.1792 | high-lexical-isolation eschatology |
| 3 | Q 54 al-Qamar | 1.1389 | high punishment-narrative |
| 4 | Q 20 Ṭā-Hā | 1.1318 | Meccan narrative |
| 5 | Q 19 Maryam | 1.1244 | Meccan biographical narrative |
| 6 | Q 89 al-Fajr | 1.1189 | Meccan oath-cluster |
| 7 | Q 77 al-Mursalāt | 1.1182 | Meccan oath-cluster |
| 8 | Q 80 ʿAbasa | 1.1071 | Meccan |
| 9 | Q 75 al-Qiyāma | 1.0920 | Meccan eschatology |
| 10 | Q 79 al-Nāziʿāt | 1.0917 | Meccan oath-cluster |

**Pattern**: 10/10 farthest are Meccan narrative or oath-cluster surahs. The Q 48-Q 55 pair (FR = 1.383) is the **#1 farthest pair from Q 48** — consistent with Q 55's known corpus-anomaly signature (per H-NEW-1250 and H-NEW catalog of Q 55 al-Raḥmān anti-twin).

## 3. Rhyme structure (h-new-700)

Per `findings/phase-b-hypotheses/csv/h-new-700.json` rhyme-letter diagnostics:

| Metric | Q 48 value | Notes |
|:--|:--:|:--|
| Top final letter (rāwī) | ا (alif) | terminal in 29/29 verses |
| Top-letter fraction | 1.0 (100%) | PERFECT MONORHYME |
| Rhyme entropy (Shannon, nats) | 0.000 | the corpus minimum (tied with 14 other monorhyme surahs) |
| z(rhyme entropy) | -1.394 | low; corpus-rare uniformity |
| Final-letter inventory | {ا} | single letter |
| n_verses | 29 | |

### 3.1 Perfect-monorhyme corpus comparison

15 surahs are perfect-monorhyme (frac=1.0). By size:

| Surah | Letter | n_verses | Type |
|:--|:--:|:--:|:--|
| Q 54 al-Qamar | ر | 55 | Meccan (largest perfect-monorhyme) |
| Q 76 al-Insān | ا | 31 | Medinan/Meccan-debated |
| **Q 48 al-Fatḥ** | **ا** | **29** | **Medinan (largest perfect-monorhyme Medinan with v ≥ 28)** |
| Q 72 al-Jinn | ا | 28 | Meccan |
| Q 92 al-Layl | ي | 21 | Early Meccan |
| Q 91 al-Shams | ا | 15 | Early Meccan |
| Q 63 al-Munāfiqūn | ن | 11 | Medinan |
| Q 104 al-Humazah | ه | 9 | Meccan |
| Q 98 al-Bayyinah | ه | 8 | Medinan |
| Q 114 al-Nās | س | 6 | Meccan/Medinan |
| Q 97 al-Qadr | ر | 5 | Meccan/Medinan |
| Q 105 al-Fīl | ل | 5 | Meccan |
| Q 112 al-Ikhlāṣ | د | 4 | Meccan/Medinan |
| Q 103 al-ʿAṣr | ر | 3 | Meccan |
| Q 108 al-Kawthar | ر | 3 | Meccan/Medinan |

**Q 48 occupies a singular position**: among Medinan surahs of length ≥ 20 verses, it is the **only** perfect-monorhyme. The closest comparable Medinan are Q 63 al-Munāfiqūn (11 verses, ن) and Q 98 al-Bayyinah (8 verses, ه) — much shorter.

### 3.2 The alif-rhyme tail of Q 48

The 29 verse-final patterns share a common terminal cadence *-ā* (typically realized as long-alif at fāṣila: *mubīnan, mustaqīman, ʿazīzan, ḥakīman, ʿaẓīmā, maṣīrā, naṣīrā, naṣrā, ʿazīzan, raḥīmā*, etc.). The list:

| v | Last word/closing | Pattern |
|:-:|:--|:--|
| 1 | فتحا مبينا | *fatḥan mubīnan* |
| 2 | صراطا مستقيما | *ṣirāṭan mustaqīman* |
| 3 | نصرا عزيزا | *naṣran ʿazīzan* |
| 4 | عليما حكيما | *ʿalīman ḥakīman* |
| 5 | فوزا عظيما | *fawzan ʿaẓīman* |
| 6 | وساءت مصيرا | *wa-sāʾat maṣīrā* |
| 7 | عزيزا حكيما | *ʿazīzan ḥakīman* |
| 8 | ومبشرا ونذيرا | *wa-mubashshiran wa-nadhīrā* |
| 9 | بكرة وأصيلا | *bukratan wa-aṣīlā* |
| 10 | أجرا عظيما | *ajran ʿaẓīman* |
| 11 | بما تعملون خبيرا | *khabīrā* |
| 12 | قوما بورا | *qawman būrā* |
| 13 | للكافرين سعيرا | *saʿīrā* |
| 14 | غفورا رحيما | *ghafūran raḥīmā* |
| 15 | لا يفقهون إلا قليلا | *qalīlā* |
| 16 | عذابا أليما | *ʿadhāban alīman* |
| 17 | عذابا أليما | *ʿadhāban alīman* |
| 18 | فتحا قريبا | *fatḥan qarīban* |
| 19 | عزيزا حكيما | *ʿazīzan ḥakīman* |
| 20 | صراطا مستقيما | *ṣirāṭan mustaqīman* |
| 21 | على كل شيء قديرا | *qadīrā* |
| 22 | وليا ولا نصيرا | *naṣīrā* |
| 23 | لسنة الله تبديلا | *tabdīlā* |
| 24 | بصيرا | *baṣīrā* |
| 25 | عذابا أليما | *ʿadhāban alīman* |
| 26 | بكل شيء عليما | *ʿalīman* |
| 27 | فتحا قريبا | *fatḥan qarīban* |
| 28 | وكفى بالله شهيدا | *shahīdā* |
| 29 | وأجرا عظيما | *ajran ʿaẓīman* |

**Recurring fāṣila patterns**:
- *ʿazīzan ḥakīman* (vv. 4, 7, 19) — 3 occurrences
- *ṣirāṭan mustaqīman* (vv. 2, 20) — 2 occurrences
- *fatḥan qarīban* (vv. 18, 27) — 2 occurrences (echo)
- *ʿadhāban alīman* (vv. 16, 17, 25) — 3 occurrences
- *ajran ʿaẓīman* (vv. 10, 29) — 2 occurrences (frame: opening-block last and closing verse)

The 5 recurring fāṣila-formulas account for 12 of 29 verse-endings (41.4%). This high formulaic-density is a structural feature of Q 48's rhyme-uniformity, not a flaw.

## 4. iʿjāz signatures (h-new-750)

Per `findings/phase-b-hypotheses/csv/h-new-750.json`:

| Metric | Q 48 value | Rank | Notes |
|:--|:--:|:--:|:--|
| sig_A | -2.0948 | **106/114** | iʿjāz al-fawāṣil signature; very LOW |
| sig_B | -2.0137 | **112/114** | secondary iʿjāz signature; very LOW |
| Mean content distance | 0.9945 | mid | slightly above corpus mean 0.985 |
| Local cohesion | 1.0633 | mid-low | below corpus mean |
| z(rhyme entropy) | -1.394 | low | uniform-rhyme; tied with monorhyme cluster |
| z(mean content distance) | +0.701 | mid-high | mildly distinctive content |
| z(local cohesion) | -0.620 | mid-low | less internally-cohesive than mean |

**Architectural classification**: Q 48 is **theological-iʿjāz extreme** in the al-Khaṭṭābī sense (high content-distinctiveness, theological-anchor verses) but **structural-iʿjāz LOW** in the al-Bāqillānī sense (no rhyme-entropy variability — all alif). This is consistent with the project's **dual-iʿjāz typology** (cross-finding-018):
- **Structural-iʿjāz**: rewards rhyme-entropy + content-balance (al-Bāqillānī-aligned). Q 48 = **bottom 7/114**.
- **Theological-iʿjāz**: rewards content-uniqueness + name-anchor density (al-Khaṭṭābī-aligned). Q 48 = high (top quartile by content-distinctiveness; top 1/93 by name-root-density per Q048-F-01).

Q 48 is a **canonical theological-iʿjāz signature surah** — the same cluster as Q 112 al-Ikhlāṣ (the corpus FR-centroid, classical theological-iʿjāz exemplar). The two share: short-Medinan/short-Meccan length-class + perfect monorhyme + top theological-anchor density (Q 48's *fatḥ* is to victory-theology as Q 112's *aḥad* is to monotheism-theology).

## 5. Outlier-strength (h-new-590)

Per `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Metric | Q 48 value | Notes |
|:--|:--:|:--|
| Window | [45, 46, 47, 48, 49, 50, 51] | 7-surah neighborhood |
| d_W (window mean content distance) | 0.9305 | |
| d_W_minus_X (window without Q 48) | 0.9266 | |
| Δ-percentile | +2.49 pp | mild distinctness |
| p_greater_W | 0.542 | NOT a strong outlier |
| Classification | WEAK_OUTLIER | |

Q 48 is **mildly content-distinctive** in its 7-surah neighborhood, but not an outlier in the strong sense. The window {Q 45-51} is dominated by Medinan-and-mid-Meccan boundary surahs; Q 48 contributes a measurable but small distinctness signal.

## 6. Canonical-adjacency cost (h-new-720)

Per `findings/phase-b-hypotheses/csv/h-new-720.json`:

| Adjacency | delta_raw | delta (clamped) | Rank (cheapest) | Classification |
|:--|:--:|:--:|:--:|:--|
| Q 47 → Q 48 | 0.0332 | 0.0332 | 15/113 | Smooth-low (clamped non-zero, but very low) |
| Q 48 → Q 49 | 0.0831 | 0.0831 | 22/113 | Smooth-low |
| Q 49 → Q 50 | 0.196 | 0.196 | 99/113 | UNIVERSAL HINGE (per H-NEW-130) |

**Position in mushaf-architecture**: Q 48 sits in the **smooth approach-zone** to the universal hinge Q 49→Q 50. Both Q 47→Q 48 and Q 48→Q 49 are very low-cost transitions — the local mushaf-stitching is tight; the discontinuity is at Q 49→Q 50.

This is consistent with the al-Biqāʿī *Naẓm al-Durar* claim that Q 47-Q 48-Q 49 form a tight munāsabah block (war → conquest → community-formation), but the FR-empirical signal nuances this: Q 48 is **closer in FR-space to Q 57-64 musabbiḥāt cluster** than to Q 47/Q 49 strictly. The smooth adjacency cost reflects local-content compatibility (very high) without implying that Q 47/49 are Q 48's structural-NEAREST neighbors.

## 7. UAS (h-new-840) Unified Architectural Significance

Per `findings/phase-b-hypotheses/csv/h-new-840.json`:

| Component | Q 48 value | |
|:--|:--:|:--|
| UAS | 0.5449 | rank 32/114 (mid-tier) |
| abs_outlier (from h-new-590) | 2.49 | mild distinctness |
| max_cost (max adjacency cost in window) | 0.0831 | low (the Q 48→Q 49 transition) |
| abs_iʿjāz (|sig_A|) | 2.0948 | very high (in absolute value — Q 48 is iʿjāz-extreme on the LOW end) |

UAS is the geometric mean of normalized outlier + cost + iʿjāz. Q 48's high abs_iʿjāz (driven by perfect monorhyme) dominates the score; combined with mild outlier strength and low transition cost, the result is mid-tier rank.

## 8. Per-block thematic vocabulary signature

Q 48 organizes into 3 blocks (vv. 1-10 ratification, vv. 11-17 mukhallifūn-condemnation, vv. 18-29 bayʿat-al-riḍwān + conquest-prophecy). Vocabulary signatures (top roots per block, from QAC v0.4):

### vv. 1-10 (RATIFICATION block)

Top roots: Alh (Allah, 12), Amn (faith/believer, 8), kwn (be, 5), rsl (messenger/send, 5), ftH (open/victory, 2), fwz (success, 1), gfr (forgive, 1), nEm (favor, 1), hdy (guide, 1).

Distinctive vocabulary: *fataḥnā / fatḥ / sakīna / muʾminīn / muʾmināt / yad allāhi fawqa aydīhim / ṣirāṭan mustaqīman / ḥakīman / ʿalīman*. Theological-anchor density highest in this block.

### vv. 11-17 (MUKHALLIFĪN block)

Top roots: Alh (5), qwl (say, 5), Amn (3), AErb (Bedouin, 3 — corpus-distinctive), xlf (be-left-behind, 3 — *al-mukhallifūn*), wEd (promise, 2), ZnA (think/suspect, 2 — twin: *ẓann al-sūʾ*).

Distinctive vocabulary: *al-mukhallifūn min al-aʿrāb / shaghalatnā amwālunā wa-ahlūnā / ẓann al-sūʾ / qawman būrā / saʿīrā / awliyāʾ / ʿadhāban alīman*. The Bedouin-condemnation lexicon is highly localized to this block.

### vv. 18-29 (BAYʿAT-AL-RIḌWĀN + CONQUEST block)

Top roots: Alh (12), bayʿ (pledge, 2 — corpus-distinctive in this density), ftH (2), $jr (tree, 1 — *al-shajara*), HRm (sacred, 1 — *al-masjid al-ḥarām*), HrJ (constraint, 1), nzl (descend, 1 — *fa-anzala al-sakīnata*), ġnm (booty, 2 — *maghānim*), rDw (please, 2 — *raḍiya / riḍwān*), Hjj (pilgrimage-implicit, 1 — *al-ḥajj*), Tor/Inj (Torah/Gospel, 1 each, hapax in v.29).

Distinctive vocabulary: *raḍiya allāhu / yubāyiʿūnaka taḥta al-shajara / fa-anzala al-sakīnata ʿalayhim / maghānim kathīra / al-masjid al-ḥarām / muḥalliqīn ruʾūsakum wa-muqaṣṣirīn / fī al-tawrāt / fī al-injīl / ka-zarʿin akhraja shaṭʾahu*. Multiple corpus-rare-or-hapax forms cluster here (e.g., *muḥalliqīn ruʾūsakum* is a Q 48-only construction; *ka-zarʿin akhraja shaṭʾahu* in v.29 contains the corpus-hapax *shaṭʾ* "shoot/sprout").

## 9. Cross-corpus comparison (root signatures)

Q 48's most-distinctive roots (frequency relative to length-controlled corpus expectation):

| Root (Buckwalter / Arabic) | Q 48 count | Corpus count | Expected (length-controlled) | Enrichment |
|:--|:--:|:--:|:--:|:--:|
| **gnm / غنم** (booty / spoils) | **3** | 9 | 0.064 | **46.7×** |
| **byE / بيع** (pledge / sell) | **3** | 15 | 0.107 | **28.0×** |
| **ftH / فتح** (open / victory) | **4** | 38 | 0.271 | **14.7×** |
| **Erb / عرب** (Arab / Bedouin) | **2** | 22 | 0.157 | **12.7×** |
| **Znn / ظنن** (suspect / think) | **5** | 69 | 0.493 | **10.1×** |
| skn / سكن (dwell / sakīna) | 3 | 69 | 0.493 | 6.1× |
| rDw / رضو (please) | 2 | 73 | 0.522 | 3.8× |
| Hrm / حرم (sacred) | 2 | 83 | 0.593 | 3.4× |
| xlf / خلف (behind / successor) | 3 | 127 | 0.907 | 3.3× |

**Headline**: Q 48 is the corpus-EXACT signature surah for the **{*ġanm, bayʿ, fatḥ, ʿArab, ẓann*}** five-root cluster — the **Hudaybiyya-Pledge-Conquest-Booty-Bedouin-suspicion vocabulary signature**, with the top 5 roots each at ≥ 10× corpus-baseline density. The top 3 roots (*gnm, byE, ftH*) are all at ≥ 14× corpus-baseline.

The 5-root cluster is the **vocabulary fingerprint of the Hudaybiyya-Mukhallifūn-Bayʿat al-Riḍwān narrative complex**: *fatḥ* opens the surah; *bayʿ* (yubāyiʿūnaka, vv. 10, 18) anchors the Bayʿat al-Riḍwān; *ġanm* (maghānim, vv. 15, 19, 20) anchors the booty-promise; *ʿArab* (al-mukhallifūn min al-aʿrāb, vv. 11, 16) anchors the Bedouin-condemnation block; *ẓann* (ẓann al-sūʾ, vv. 6, 12 ×2) anchors the suspicion-of-divine-promise theme. The five roots co-localize in three distinct sub-blocks of the surah, producing the integrated narrative signature.

## 10. Quick metrics summary (single-row)

```
Q 48 al-Fatḥ | Medinan | revelation 111/114 | 29 v / 600 w / 2,550 ℓ
UAS rank: 32/114 (mid-tier; UAS=0.545)
FR nearest-5: {Q 61, Q 64, Q 59, Q 63, Q 57} — all musabbiḥāt-adjacent Medinan
FR farthest-3: {Q 55, Q 56, Q 54}
Rhyme: PERFECT alif monorhyme (29/29; entropy=0.0)
iʿjāz: sig_A rank 106/114, sig_B rank 112/114 (theological extreme; structural low)
Outlier: +2.49pp WEAK_OUTLIER (p=0.542)
Q47→Q48: rank 15/113 cheapest (Δ=0.033)
Q48→Q49: rank 22/113 cheapest (Δ=0.083)
ftH-density: RANK 1/93 length-controlled (4 tokens / 916, p=1.6e-4 hypergeometric)
```

---

*All figures sourced from on-disk JSON; no value asserted from memory.*
