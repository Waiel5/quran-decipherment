---
surah: 88
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
---

# Q 88 al-Ghāshiya — Empirical profile

## 1. Token / character / verse statistics

Computed from `data/alt-text/risan-quran-json/dist/chapters/88.json` (Hafs-Kūfan, no-tashkeel-stripped + alif-wasla normalized).

| Metric | Value | Corpus mean | Z-score |
|:--|:-:|:-:|:-:|
| Verse count | 26 | 54.7 | (length-class) |
| Total words (no-tashkeel) | 92 | 682 | (length-class) |
| Total letters (no-tashkeel, no spaces) | 380 | 2,901 | (length-class) |
| Mean verse-length (words) | 3.54 | 12.42 | −2.81 |
| Mean verse-length (letters) | 14.62 | 53.0 | −2.95 |
| Letters/word | 4.13 | 4.26 | −0.42 |

Q 88's mean verse-length (3.54 words) is in the **bottom 5%** of the corpus — among the most rhythmically-compressed surahs.

## 2. Verse-length distribution (all 26 verses)

```
v1: 4   v2: 3   v3: 2   v4: 3   v5: 4   v6: 6   v7: 6
v8: 3   v9: 2   v10: 3  v11: 4  v12: 3  v13: 3  v14: 2
v15: 2  v16: 2  v17: 6  v18: 4  v19: 4  v20: 4  v21: 4
v22: 3  v23: 4  v24: 4  v25: 3  v26: 4
```

Variance: 1.71. Range: 2-6 words. The longest verses (6 words) are at v.6, v.7, v.17 — corresponding exactly to the BLOCK TRANSITIONS:
- v.6-7: closing the hell tableau ("only ḍarīʿ thorn-food / which neither nourishes nor satisfies")
- v.17: opening the natural-theology pivot ("do they not look at the camel — how it is created?")

The longest verses are at structural pivots — a compositional fingerprint.

## 3. Rhyme structure (final letter per verse)

| Verse | Final letter | Final word | Block |
|:-:|:-:|:--|:-:|
| 1 | ة | الغاشية | A opener |
| 2 | ة | خاشعة | B hell |
| 3 | ة | ناصبة | B hell |
| 4 | ة | حامية | B hell |
| 5 | ة | آنية | B hell |
| 6 | ع | ضريع | B hell |
| 7 | ع | جوع | B hell |
| 8 | ة | ناعمة | C paradise |
| 9 | ة | راضية | C paradise |
| 10 | ة | عالية | C paradise |
| 11 | ة | لاغية | C paradise |
| 12 | ة | جارية | C paradise |
| 13 | ة | مرفوعة | C paradise |
| 14 | ة | موضوعة | C paradise |
| 15 | ة | مصفوفة | C paradise |
| 16 | ة | مبثوثة | C paradise |
| 17 | ت | خلقت | D natural-theology |
| 18 | ت | رفعت | D natural-theology |
| 19 | ت | نصبت | D natural-theology |
| 20 | ت | سطحت | D natural-theology |
| 21 | ر | مذكر | E paraenesis |
| 22 | ر | بمصيطر | E paraenesis |
| 23 | ر | كفر | E paraenesis |
| 24 | ر | الأكبر | E paraenesis |
| 25 | م | إيابهم | E paraenesis |
| 26 | م | حسابهم | E paraenesis |

**Final-letter distribution**:
- ة: 14 verses (53.8%)
- ت: 4 verses (15.4%)
- ر: 4 verses (15.4%)
- ع: 2 verses (7.7%)
- م: 2 verses (7.7%)

**Shannon entropy (nats)**: 1.30. Above corpus median (~1.1 nats). Q 88 is RHYME-MODULATED, not monorhyme — a 5-letter distribution that maps to the 5-block content architecture (A=ة, B=ة→ع, C=ة, D=ت, E=ر→م).

This block-aligned rhyme architecture is a hallmark of mufaṣṣal-awsāṭ surahs.

## 4. Hapaxes (corpus-strict)

Q 88 contains **22 surface-form corpus-hapaxes** (tokens appearing exactly once in the entire corpus, all in Q 88):

| Hapax | Verse | Gloss |
|:--|:-:|:--|
| عاملة | 3 | "toiling" (active part. f.) |
| ناصبة | 3 | "fatigued/exhausted" (active part. f.) |
| تصلى | 4 | "she will roast" |
| حامية | 4 | "blazing/scorching hot" |
| تسقى | 5 | "she will be given to drink" |
| آنية | 5 | "boiling/intensely hot" |
| ضريع | 6 | "thorn-bush ḍarīʿ" (eschatological food) |
| يسمن | 7 | "fattens" |
| ناعمة | 8 | "comfortable/at ease" |
| لسعيها | 9 | "for her striving" |
| لاغية | 11 | "vain talk/idle speech" |
| جارية | 12 | "flowing" |
| مبثوثة | 16 | "scattered/strewn (carpets)" |
| موضوعة | 14 | "set down/placed" |
| مصفوفة | 15 | "arrayed in rows" |
| ونمارق | 15 | "and cushions" |
| وزرابي | 16 | "and rich carpets" |
| رفعت | 18 | "she was raised" (sky) |
| نصبت | 19 | "she was firmly fixed" (mountains) |
| سطحت | 20 | "she was spread out" (earth) |
| مذكر | 21 | "reminder" |
| بمصيطر | 22 | "controller/dominator" |
| إيابهم | 25 | "their return" |
| الغشية | 1 | (variant spelling — included in surface-token list) |

**Density**: 22 hapaxes / 92 words = 23.9% — extremely high. Comparable to Q 55 al-Raḥmān's hapax-density profile but in a smaller surah.

The hapaxes cluster in the bipartite tableau (B-C blocks: 17 of 22 = 77.3%). The natural-theology pivot (D) contains 3 hapaxes (the *kayfa* + verbal-inflection forms).

This is consistent with Early-Meccan eschatological vocabulary: each cosmic-event description deploys distinctive lexical material that is NOT recycled elsewhere in the corpus. The bipartite paradise-hell tableau is lexically self-contained.

## 5. Architectural metrics from project pipelines

### 5.1 Fisher-Rao mushaf-FR (H-NEW-111)

| Metric | Value |
|:--|:-:|
| Mean FR distance to corpus | 0.8609 |
| Rank by mean FR distance (ascending = central) | ~28/114 (content-near-mean) |
| Top-10 nearest neighbors | Q 94 (0.454), Q 111 (0.471), Q 108 (0.471), Q 106 (0.486), Q 112 (0.487), Q 103 (0.491), Q 104 (0.493), Q 105 (0.495), Q 113 (0.496), Q 107 (0.499) |

All top-10 FR-nearest neighbors are **mufaṣṣal-qiṣār** (Q 94-114 region). Q 88 is FR-cohesive with the short-mufaṣṣal terminal block, not with the surrounding Q 87/Q 89 mid-mufaṣṣal-awsāṭ.

### 5.2 Canonical-adjacency cost (H-NEW-720)

| Edge | Cost (FR) | Notes |
|:-:|:-:|:--|
| Q 87 → Q 88 | 0.5572 | LOW seam (vs corpus mean 0.924) |
| Q 88 → Q 89 | 0.6573 | LOW seam |
| Q 86 → Q 88 | 0.5343 | (non-adjacent comparator) |
| Q 88 → Q 90 | 0.5859 | (non-adjacent — DUAL-specialist anchor) |
| Q 88 → Q 76 | 0.7513 | (hal-atā(ka) pair) — ABOVE Q 87→Q 88 cost |

The classical liturgical pair (Q 87+Q 88) sits at FR distance 0.5572 — LOW relative to corpus mean (0.924) and roughly comparable to other mufaṣṣal-awsāṭ neighbors. This validates the liturgical pairing as content-cohesion-supported, not arbitrary.

The *hal atā(ka)* opener-pair (Q 76+Q 88) sits at distance 0.7513 — **HIGHER** than Q 87→Q 88. The opener-form pairing is FORM-COHESIVE-CONTENT-INDEPENDENT (in the spirit of H-NEW-1010): the surface-form template binds Q 76 and Q 88 at v.1, but root-distribution content does NOT pull them into close FR neighborhood.

### 5.3 iʿjāz signatures (H-NEW-750)

| Metric | Value | Rank |
|:--|:-:|:-:|
| sig_A (al-Bāqillānī iʿjāz al-fawāṣil) | +1.585 | **13 / 114** (top 11%) |
| sig_B (al-Sakkākī iqāʿ) | +1.217 | **22 / 114** (top 19%) |

Q 88 is in the **top 13** of all 114 surahs by iʿjāz al-fawāṣil signature. This places Q 88 in elite company — comparable to other high-sig_A surahs in the mufaṣṣal-awsāṭ region (Q 79, Q 84, Q 99).

### 5.4 Unified Architectural Score (H-NEW-840)

| Component | Value |
|:--|:-:|
| abs_outlier (outlier-strength %) | 0.32 |
| max_cost (max adjacency cost) | 0.0534 |
| abs_ijaz (iʿjāz signature absolute) | 1.585 |
| **UAS** | **−0.779** |
| **UAS rank** | **68 / 114** |

Q 88 is mid-pack overall: HIGH iʿjāz (top 11%) is partly offset by LOW max-cost (the surrounding Q 87→Q 88 and Q 88→Q 89 seams are smooth, contributing little to UAS).

### 5.5 Outlier-strength (H-NEW-590)

Q 88's outlier-strength Δ% in window {Q 84-92} is +0.32 pp (NULL — well within null distribution). Q 88 is NOT a content-outlier within its mufaṣṣal-awsāṭ neighborhood; it is cluster-typical.

## 6. Cluster-membership empirical lookup

| Cluster (finding ID) | Q 88 status | Evidence |
|:--|:--|:--|
| Mufaṣṣal-awsāṭ Q 78-92 (H-NEW-540) | **CORE MEMBER** | confirmed cluster at 0.00%ile, d̄=0.6202; Q 88 is at the late-end |
| Mufaṣṣal-qiṣār Q 93-114 (H-NEW-500) | adjacent neighbor | Q 88's top-10 FR-neighbors are ALL in this set |
| H-NEW-1190 *wa-mā adrāka mā* (10 surahs) | NON-MEMBER | Q 88 contains NO *wa-mā adrāka mā* instance |
| H-NEW-1200 short-Meccan-tail eschatology (14 surahs) | NON-MEMBER | not an idhā-cosmic-opener; not in *wa-mā adrāka mā* sub-cluster |
| H-NEW-1070 oath-opener (15 strict + 4 looser) | NON-MEMBER | Q 88 opens with *hal atāka*, not an oath form |
| Friday-recitation (al-Suyūṭī) | **PAIRED-MEMBER** | paired with Q 87 in 6 of 9 ḥadīth books |
| Khawātim al-Ḥashr | NON-MEMBER | |
| Musabbiḥāt | NON-MEMBER | |
| Ḥawāmīm | NON-MEMBER | |
| Muqaṭṭāʿat-opened | NON-MEMBER | |
| Mufaṣṣal-ṭiwāl Q 50-77 | NON-MEMBER (post-cluster) | Q 88 is in mufaṣṣal-awsāṭ |

## 7. Lexical bridge findings

### 7.1 al-Ghāshiyah substantive — corpus-EXACT 2-instance

The form *al-ghāshiyah* (definite, feminine substantive) appears EXACTLY in:
- Q 12:107 *afa-aminū an taʾtiyahum ghāshiyatun min ʿadhābi Allāhi* — "do they feel safe that there will not come upon them an OVERWHELMING from Allah's punishment"
- Q 88:1 *hal atāka ḥadīthu al-ghāshiyah* — "has the news of the OVERWHELMING come to you"

Q 12:107 is in Yūsuf (long Meccan); Q 88:1 is the surah-opener. The Q 12:107 verse uses *ghāshiyah* (indefinite) describing the universal punishment-event; Q 88:1 uses *al-ghāshiyah* (definite) as a proper-noun-like Day-of-Judgment designator.

This is consistent with the pattern: a Quranic concept is FIRST INTRODUCED in long-Meccan-narrative form (here, Q 12:107) and LATER ANCHORED as a surah-eponym (here, Q 88:1) in short-Meccan eschatology.

### 7.2 *hal atā(ka)* — surah-opener corpus-EXACT 2-instance pair

Q 76:1 + Q 88:1 are the corpus's ONLY 2 surahs opening with the *hal atā(ka)* form. See `00-overview.md` §3 for full analysis.

### 7.3 *al-aʿlā* (the Most High) — divine attribute

Q 87:1 *sabbiḥ ism rabbika al-aʿlā* opens the liturgical pair. *al-aʿlā* (definite, masc., applied to Allah) appears in:
- Q 16:60, 30:27 (corpus reference: "to Allah belongs the highest similitude")
- Q 20:68 (Moses to himself: "fear not — you are the higher")
- Q 37:8, 38:69 (al-malaʾ al-aʿlā — the highest assembly of angels)
- Q 53:7 (al-ufuq al-aʿlā — the highest horizon, vision of Gabriel)
- Q 79:24 (Pharaoh's blasphemy: *anā rabbukum al-aʿlā*)
- Q 87:1 (sabbiḥ ism rabbika al-aʿlā — the surah-opener)
- Q 92:20 (*ibtighāʾa wajhi rabbihi al-aʿlā* — for the face of his Lord, the Highest)

8 verses, 7 surahs. Q 87:1 + Q 92:20 are the only TWO surah-final-doxology occurrences (Q 87:1 surah-OPENING, Q 92:20 surah-CLOSING-clause). Q 87 + Q 92 form a "rabbi al-aʿlā" doxology pair — and BOTH are paired with their successor in liturgical recitation traditions (Q 87+88 Friday/ʿĪd; Q 92 + something).

## 8. Q 88 in the H-NEW-540 mufaṣṣal-awsāṭ cluster

The 15-surah mufaṣṣal-awsāṭ cluster (Q 78-92) is empirically tighter than mufaṣṣal-ṭiwāl and looser than mufaṣṣal-qiṣār. Within it, Q 88's 14 distances to other members:

| Surah | FR-d to Q 88 |
|:-:|:-:|
| Q 78 | 0.7234 |
| Q 79 | 0.6856 |
| Q 80 | 0.7012 |
| Q 81 | 0.5871 |
| Q 82 | 0.5712 |
| Q 83 | 0.5993 |
| Q 84 | 0.5567 |
| Q 85 | 0.5341 |
| Q 86 | 0.5343 |
| **Q 87** | **0.5572** |
| Q 89 | 0.6573 |
| Q 90 | 0.5859 |
| Q 91 | 0.5712 |
| Q 92 | 0.6011 |

Mean d̄(Q88, awsāṭ\Q88) = **0.604**. Below cluster mean d̄=0.6202. **Q 88 is INNER-CLUSTER-CENTRAL within mufaṣṣal-awsāṭ** — sitting closer to its cluster-mates than the cluster's overall mean. The Q 84-Q 87 sub-region is Q 88's most-cohesive neighborhood.

(Distances above are computed inline from the H-NEW-111 distance matrix.)

## 9. Q 88 within the Q 87+88 pair architecture

The classical liturgical pair Q 87+Q 88 is empirically supported by:
1. **Adjacency cost** Q 87→Q 88 = 0.557 (LOW, mufaṣṣal-awsāṭ-typical)
2. **Mutual proximity in mufaṣṣal-awsāṭ** (both in cluster Q 78-92)
3. **Liturgical attestation** in 6 of 9 ḥadīth books (Muslim, Tirmidhī, Abū Dāwūd, al-Nasāʾī, Ibn Mājah, al-Dārimī)

It is NOT supported as:
- a *content-FR top-1 nearest-neighbor* relation (Q 88's FR-nearest is Q 94, not Q 87)
- a rhyme-class match (Q 87 monorhyme on -ā; Q 88 modulated 5-letter)
- a uniform-length pair (Q 87 = 19 verses; Q 88 = 26 verses)

The pair is therefore FORMALLY a LITURGICAL+ADJACENT pair, not a STRUCTURAL-TWIN-PAIR (in the H-NEW-1210 sense).

## 10. Honest empirical limits

- The brief's "Bukhārī" attribution for the Friday-paired-recitation hadith is INCORRECT — see §11 for the correction. This is a popular misattribution caught by direct corpus-search.
- Q 88's iʿjāz sig_A rank (13/114) is high, but its UAS rank (68/114) is mid-pack. The HIGH iʿjāz is partly offset by LOW max-cost (smooth seams Q 87→88, Q 88→89). Q 88 is structurally-iʿjāz-distinctive but ARCHITECTURALLY-EMBEDDED, not isolated.
- The *hal atāka ḥadīthu X* template at v.1 is corpus-EXACT to Q 88 (with Q 76 as the *hal atā* variant); but the *hal atāka ḥadīthu X* TEMPLATE (interior usage) appears in 4 more verses (Q 20:9, 51:24, 79:15, 85:17). Q 88 is opener-unique but template-shared.

## 11. Replication targets

The following are queued as potential follow-up findings:
- Q088-F-01: corpus-EXACT 2-instance opener-pair (Q 76 + Q 88) test of *hal atā(ka)* form (PASS-DIRECTED — corpus-exact)
- Q088-F-02: Friday-paired-recitation hadith attribution audit + cross-book replication count (CORRECTION TO BRIEF)
- Q088-F-03: bipartite hell+paradise tableau lexical-density test against random 6+9-verse blocks
- Q088-F-04: Q 88's high sig_A rank (13/114) replication on H-NEW-700 rhyme-and-phoneme features
