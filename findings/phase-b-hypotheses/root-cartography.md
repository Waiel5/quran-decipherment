---
title: Root Cartography of the Quran
phase: B
agent: root-cartographer-run-1
date: 2026-04-12
status: exploratory (no null models run yet)
rules:
  orthography: not-applicable
  word_definition: stem-with-root (Leeds QAC v0.4)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1 (Leeds default)
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: not-applicable (Phase B raw exploration; flags candidates only)
source_corpus: data/morphology/quranic-corpus-morphology-0.4.txt
intermediate_artifacts:
  - data/morphology/root-index.json
  - data/morphology/root-stats.csv
---

# Root Cartography

This report exhaustively maps the distribution of Arabic roots in the Quran
using the Leeds Quranic Arabic Corpus (Dukes 2009, v0.4). It includes
fundamental distribution stats, hapax findings, suspicious-count flags,
entropy-based dispersion measures, replications of the famous Family-B
word-pair claims, a hunt for novel matching-count root pairs, and a
palindromic-root catalog.

**No null models have been run.** Every numerical pattern below is a
candidate flag; nothing here is a confirmed finding under the §3 protocol.

## 0. Headline candidate findings (read-this-first)

These are the three most non-obvious flags this sweep produced. None are
"findings" in the §3 sense — each must still pass null-model testing before
publication. They are listed here so the next agent in the pipeline knows
where to spend null-model budget.

1. **`sjn` (root for prison/imprisonment) appears 12 times, all 12 in Surah 12
   (Yusuf), and Surah 12 has the prison narrative.** Triple coincidence:
   count = surah index = surah whose narrative is *about* the root's meaning.
   Sister anchors in the same vein from §10/§5: `qmS` (shirt) = 6×, all in
   Surah 12 (Yusuf's shirt is the recurring plot device); `khf` (cave) = 6×,
   all in Surah 18 (Al-Kahf, "The Cave"); `myl` (mile/inclination) = 6×, all
   in Surah 4 (An-Nisa, the inheritance laws using mayl). These look like
   genuine surah-anchored thematic vocabulary — the lexical fingerprint of a
   surah's subject matter. The Yusuf one is the most striking because of the
   triple alignment (count, surah index, story content).

2. **The mala'ika/shayatin pair survives at the single-lemma level: `malak`
   = 88, `$ayoTa`n` = 88.** It does NOT survive at the root level (`mlk` = 206
   inflating with mulk/mulook/malik etc.; `$Tn` = 88 root-wise because the
   only lemma under that root is `$ayoTa`n` itself). The pair is reproducible,
   but only by silently selecting the singular-lemma form on the angel side
   while accepting whatever the noise-free root yields on the devil side.
   This is a textbook example of the cherry-picking pattern — and yet the
   number really is 88/88 once that pick is made. Worth a McKay-style §1.4
   comparable-corpus null to see whether matching is unusually frequent for
   the Quran or whether classical Arabic prose at this length produces equally
   striking accidents at similar rates. Note also the count=88 pair group in
   §8 is `$Tn` ⇄ `qrA` (qira'ah, recitation) — a *different* coincidence than
   the literature claim.

3. **Adam = Isa = 25 (lemma-level, proper-noun) verifies cleanly.** This is
   the only Family-B word-pair claim on the primary list that comes through
   without any rule-tuple manipulation. But as noted in §7's verdict, the
   count=25 row of §8 contains 13 *other* roots tied at 25 (Hdd "limits/laws",
   whb "give", $ry "buy", flk "ship/orbit", etc.) — so the Adam/Isa pairing
   was selected from a tie-class of size 14, and the narrative parallel
   ("The example of Isa is like the example of Adam", 3:59) is the only
   reason that one ordered pair was preferred. The number is real; the
   "miracle" framing is selection bias from a 14-element pool.

The other six famous Family-B pairs all **fail** under any rule that doesn't
already bake in a numerically convenient form-filter. See §7 for the detailed
per-pair verdict tables.

## 1. Fundamental distribution stats

- **Total distinct roots:** 1,642
- **Total root-bearing stem segments:** 49,968

### Coverage at thresholds (roots with at least N occurrences)

| Threshold | Roots ≥ N |
|---:|---:|
| ≥ 1 | 1,642 |
| ≥ 2 | 1,247 |
| ≥ 3 | 1,050 |
| ≥ 5 | 833 |
| ≥ 10 | 594 |
| ≥ 20 | 411 |
| ≥ 50 | 203 |
| ≥ 100 | 114 |
| ≥ 200 | 47 |
| ≥ 500 | 12 |
| ≥ 1000 | 3 |
| ≥ 2000 | 1 |

### Roots with exactly N occurrences

| N | Roots == N |
|---:|---:|
| 1 | 395 |
| 2 | 197 |
| 5 | 89 |
| 10 | 27 |
| 100 | 0 |
| 1000 | 0 |

### Top-20 most frequent roots

| Rank | Root (BW) | Root (Arabic) | Occurrences | n_surahs | n_verses |
|---:|---|---|---:|---:|---:|
| 1 | Alh | اله | 2,851 | 86 | 1879 |
| 2 | qwl | قول | 1,722 | 84 | 1383 |
| 3 | kwn | كون | 1,390 | 86 | 1176 |
| 4 | rbb | ربب | 980 | 94 | 871 |
| 5 | Amn | امن | 879 | 77 | 723 |
| 6 | Elm | علم | 854 | 85 | 728 |
| 7 | qwm | قوم | 660 | 79 | 597 |
| 8 | Aty | اتي | 549 | 72 | 486 |
| 9 | kfr | كفر | 525 | 77 | 465 |
| 10 | byn | بين | 523 | 71 | 454 |
| 11 | $yA | شيا | 519 | 73 | 449 |
| 12 | rsl | رسل | 513 | 69 | 429 |
| 13 | ArD | ارض | 461 | 80 | 440 |
| 14 | ywm | يوم | 405 | 75 | 377 |
| 15 | Ayy | ايي | 382 | 59 | 353 |
| 16 | smw | سمو | 381 | 81 | 352 |
| 17 | kll | كلل | 377 | 74 | 355 |
| 18 | E*b | عذب | 373 | 68 | 336 |
| 19 | Eml | عمل | 360 | 68 | 313 |
| 20 | jEl | جعل | 346 | 66 | 311 |

### Hapax roots (occur exactly once)

There are **395** roots that occur exactly once in the entire
Quran. That is roughly the long-tail expectation under any Zipfian
distribution; nothing surprising on its face.

## 2. Hapax-surah roots (single-surah-only roots)

There are **459** roots that occur in one and only one
surah (any number of times). Top surahs by hapax-surah count:

| Rank | Surah | Name | Type | Hapax-surah roots |
|---:|---:|---|---|---:|
| 1 | 2 | Al-Baqarah | medinan | 22 |
| 2 | 12 | Yusuf | meccan | 22 |
| 3 | 4 | An-Nisa | medinan | 17 |
| 4 | 22 | Al-Hajj | medinan | 16 |
| 5 | 7 | Al-A'raf | meccan | 14 |
| 6 | 20 | Taha | meccan | 14 |
| 7 | 5 | Al-Ma'idah | medinan | 13 |
| 8 | 9 | At-Tawbah | medinan | 12 |
| 9 | 55 | Ar-Rahman | medinan | 12 |
| 10 | 6 | Al-An'am | meccan | 11 |
| 11 | 16 | An-Nahl | meccan | 11 |
| 12 | 17 | Al-Isra | meccan | 11 |
| 13 | 18 | Al-Kahf | meccan | 11 |
| 14 | 37 | As-Saffat | meccan | 11 |
| 15 | 19 | Maryam | meccan | 10 |

Surah 2 (Al-Baqarah) and surah 26 (Ash-Shu'ara') will dominate this list
because they are the longest. Length-normalize before drawing conclusions.

## 3. Meccan-only and Medinan-only roots

Filter: total occurrences ≥ 5 (drops most singletons / cherrypicking room).
Surah classification source: amrayn `quran-no-tashkeel.json` `type` field
(traditional Meccan/Medinan attribution; the literature is not unanimous).

**Meccan-only roots (≥5 occ):** 63

Top 25 by occurrence:

| Rank | Root | Arabic | Occurrences | n_surahs |
|---:|---|---|---:|---:|
| 1 | fTr | فطر | 20 | 17 |
| 2 | k$f | كشف | 20 | 14 |
| 3 | fAd | فاد | 16 | 13 |
| 4 | kyl | كيل | 16 | 7 |
| 5 | wSf | وصف | 14 | 7 |
| 6 | jHd | جحد | 12 | 10 |
| 7 | $ml | شمل | 12 | 9 |
| 8 | $qw | شقو | 12 | 7 |
| 9 | sjn | سجن | 12 | 3 |
| 10 | slk | سلك | 12 | 11 |
| 11 | nTq | نطق | 12 | 9 |
| 12 | Hyq | حيق | 10 | 9 |
| 13 | bT$ | بطش | 10 | 8 |
| 14 | rhq | رهق | 10 | 7 |
| 15 | zlf | زلف | 10 | 8 |
| 16 | frT | فرط | 8 | 6 |
| 17 | DrE | ضرع | 8 | 4 |
| 18 | Ey$ | عيش | 8 | 8 |
| 19 | gbr | غبر | 8 | 7 |
| 20 | sry | سري | 8 | 8 |
| 21 | trf | ترف | 8 | 7 |
| 22 | xsf | خسف | 8 | 7 |
| 23 | nwq | نوق | 7 | 6 |
| 24 | DHw | ضحو | 7 | 5 |
| 25 | dkk | دكك | 7 | 4 |

**Medinan-only roots (≥5 occ):** 14

Top 25 by occurrence:

| Rank | Root | Arabic | Occurrences | n_surahs |
|---:|---|---|---:|---:|
| 1 | Hrf | حرف | 6 | 5 |
| 2 | Asr | اسر | 6 | 4 |
| 3 | vqf | ثقف | 6 | 6 |
| 4 | zlzl | زلزل | 6 | 4 |
| 5 | myl | ميل | 6 | 1 |
| 6 | Syd | صيد | 6 | 1 |
| 7 | xdE | خدع | 5 | 3 |
| 8 | $Tr | شطر | 5 | 1 |
| 9 | Ent | عنت | 5 | 5 |
| 10 | n$z | نشز | 5 | 3 |
| 11 | lwy | لوي | 5 | 3 |
| 12 | bgD | بغض | 5 | 3 |
| 13 | Emm | عمم | 5 | 3 |
| 14 | $HH | شحح | 5 | 4 |

## 4. Suspicious-count roots (gold territory)

These are roots whose total occurrence count happens to land on a
numerologically loaded value: 7, 11, 12, 14, 19, 24, 25, 27, 30, 33,
40, 50, 70, 88, 99, 100, 114, 115, 144, 145, 313, 332, 365, 786, 1000.

**This is exhaustive enumeration of every flag**, with no cherry-picking.
The list below WILL contain coincidences — the methodological point is
that we report them all and let the reader judge non-obviousness.

### Count = 7 (32 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Emh | عمه | 7 | 6 | 1 | 2 | 27 |
| Emd | عمد | 7 | 3 | 4 | 4 | 104 |
| mkv | مكث | 7 | 6 | 1 | 13 | 43 |
| xTf | خطف | 6 | 4 | 3 | 2 | 37 |
| qsw | قسو | 6 | 2 | 5 | 2 | 57 |
| bxs | بخس | 6 | 6 | 1 | 2 | 72 |
| brj | برج | 6 | 3 | 4 | 4 | 85 |
| Elq | علق | 6 | 5 | 2 | 4 | 96 |
| ndm | ندم | 6 | 4 | 3 | 5 | 49 |
| nwq | نوق | 6 | 7 | 0 | 7 | 91 |
| bky | بكي | 6 | 6 | 1 | 9 | 53 |
| ESf | عصف | 6 | 6 | 1 | 10 | 105 |
| xmr | خمر | 5 | 2 | 5 | 2 | 47 |
| fyA | فيا | 5 | 1 | 6 | 2 | 59 |
| bEl | بعل | 5 | 2 | 5 | 2 | 37 |
| Eqd | عقد | 5 | 2 | 5 | 2 | 113 |
| grf | غرف | 5 | 5 | 2 | 2 | 39 |
| Hbl | حبل | 5 | 4 | 3 | 3 | 111 |
| HZZ | حظظ | 5 | 2 | 5 | 3 | 41 |
| skr | سكر | 5 | 4 | 3 | 4 | 50 |
| Asw | اسو | 5 | 1 | 6 | 5 | 60 |
| zyt | زيت | 5 | 5 | 2 | 6 | 95 |
| DHw | ضحو | 5 | 7 | 0 | 7 | 93 |
| nkv | نكث | 5 | 3 | 4 | 7 | 48 |
| mwj | موج | 5 | 5 | 2 | 10 | 31 |
| tsE | تسع | 5 | 7 | 0 | 17 | 74 |
| dkk | دكك | 4 | 7 | 0 | 7 | 89 |
| wEy | وعي | 4 | 7 | 0 | 12 | 84 |
| nsk | نسك | 3 | 1 | 6 | 2 | 22 |
| srH | سرح | 3 | 1 | 6 | 2 | 33 |
| nSf | نصف | 3 | 2 | 5 | 2 | 73 |
| bDE | بضع | 2 | 7 | 0 | 12 | 30 |

### Count = 11 (27 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| lgw | لغو | 11 | 9 | 2 | 2 | 88 |
| Trf | طرف | 11 | 8 | 3 | 3 | 55 |
| wqd | وقد | 10 | 4 | 7 | 2 | 104 |
| sHb | سحب | 10 | 7 | 4 | 2 | 54 |
| Enb | عنب | 10 | 9 | 2 | 2 | 80 |
| zbr | زبر | 10 | 9 | 2 | 3 | 54 |
| wkA | وكا | 10 | 8 | 3 | 12 | 76 |
| HSy | حصي | 10 | 9 | 2 | 14 | 78 |
| Twr | طور | 9 | 8 | 3 | 2 | 95 |
| Ayd | ايد | 9 | 2 | 9 | 2 | 61 |
| Hrb | حرب | 9 | 3 | 8 | 2 | 47 |
| qSr | قصر | 9 | 6 | 5 | 4 | 77 |
| TbE | طبع | 9 | 6 | 5 | 4 | 63 |
| jml | جمل | 9 | 9 | 2 | 7 | 77 |
| frr | فرر | 9 | 7 | 4 | 18 | 80 |
| $fq | شفق | 9 | 9 | 2 | 18 | 84 |
| Ewn | عون | 8 | 6 | 5 | 1 | 25 |
| SEq | صعق | 8 | 7 | 4 | 2 | 52 |
| gmm | غمم | 8 | 5 | 6 | 2 | 25 |
| gyZ | غيظ | 8 | 3 | 8 | 3 | 67 |
| ymm | يمم | 7 | 8 | 3 | 2 | 51 |
| wrd | ورد | 7 | 10 | 1 | 11 | 55 |
| sbb | سبب | 6 | 9 | 2 | 2 | 40 |
| fAy | فاي | 6 | 2 | 9 | 2 | 28 |
| Trq | طرق | 6 | 9 | 2 | 4 | 86 |
| sfh | سفه | 5 | 5 | 6 | 2 | 72 |
| rDE | رضع | 5 | 2 | 9 | 2 | 65 |

### Count = 12 (32 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Hsr | حسر | 12 | 9 | 3 | 2 | 69 |
| jby | جبي | 12 | 10 | 2 | 3 | 68 |
| bkr | بكر | 11 | 6 | 6 | 2 | 76 |
| xTb | خطب | 11 | 11 | 1 | 2 | 78 |
| knn | كنن | 11 | 11 | 1 | 2 | 56 |
| Tyn | طين | 11 | 10 | 2 | 3 | 51 |
| wdy | ودي | 11 | 8 | 4 | 4 | 89 |
| slk | سلك | 11 | 12 | 0 | 15 | 74 |
| nTf | نطف | 11 | 10 | 2 | 16 | 80 |
| rhb | رهب | 10 | 5 | 7 | 2 | 59 |
| TmE | طمع | 10 | 8 | 4 | 2 | 74 |
| nb* | نبذ | 10 | 8 | 4 | 2 | 104 |
| lHm | لحم | 10 | 7 | 5 | 2 | 56 |
| byD | بيض | 10 | 9 | 3 | 2 | 37 |
| jHd | جحد | 10 | 12 | 0 | 6 | 46 |
| xrr | خرر | 10 | 11 | 1 | 7 | 38 |
| Hnf | حنف | 9 | 6 | 6 | 2 | 98 |
| sfr | سفر | 9 | 5 | 7 | 2 | 80 |
| Esr | عسر | 9 | 7 | 5 | 2 | 94 |
| drk | درك | 9 | 9 | 3 | 4 | 68 |
| $yE | شيع | 9 | 11 | 1 | 6 | 54 |
| $ml | شمل | 9 | 12 | 0 | 6 | 70 |
| nTq | نطق | 9 | 12 | 0 | 21 | 77 |
| E*r | عذر | 8 | 7 | 5 | 7 | 77 |
| wSl | وصل | 7 | 6 | 6 | 2 | 28 |
| nyl | نيل | 7 | 3 | 9 | 2 | 33 |
| xwD | خوض | 7 | 8 | 4 | 4 | 74 |
| $qw | شقو | 7 | 12 | 0 | 11 | 92 |
| $bh | شبه | 6 | 5 | 7 | 2 | 39 |
| ESw | عصو | 6 | 11 | 1 | 2 | 28 |
| bxl | بخل | 6 | 1 | 11 | 3 | 92 |
| sjn | سجن | 3 | 12 | 0 | 12 | 83 |

### Count = 14 (13 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| rsw | رسو | 13 | 13 | 1 | 7 | 79 |
| rjm | رجم | 12 | 13 | 1 | 3 | 81 |
| zrE | زرع | 12 | 11 | 3 | 6 | 56 |
| fqr | فقر | 11 | 3 | 11 | 2 | 75 |
| E$w | عشو | 11 | 12 | 2 | 3 | 79 |
| ETw | عطو | 11 | 11 | 3 | 9 | 108 |
| Sff | صفف | 11 | 11 | 3 | 18 | 89 |
| vwy | ثوي | 10 | 11 | 3 | 3 | 47 |
| lwm | لوم | 10 | 12 | 2 | 5 | 75 |
| wlj | ولج | 8 | 6 | 8 | 3 | 57 |
| Hrv | حرث | 7 | 8 | 6 | 2 | 68 |
| wSf | وصف | 7 | 14 | 0 | 6 | 43 |
| Swm | صوم | 6 | 1 | 13 | 2 | 58 |

### Count = 19 (8 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Swr | صور | 17 | 14 | 5 | 2 | 82 |
| bld | بلد | 15 | 17 | 2 | 2 | 95 |
| sEr | سعر | 15 | 13 | 6 | 4 | 84 |
| vmn | ثمن | 13 | 8 | 11 | 2 | 69 |
| grb | غرب | 13 | 11 | 8 | 2 | 73 |
| TlE | طلع | 13 | 17 | 2 | 3 | 104 |
| fkh | فكه | 12 | 16 | 3 | 23 | 83 |
| r$d | رشد | 9 | 15 | 4 | 2 | 72 |

### Count = 24 (12 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| kwd | كود | 19 | 16 | 8 | 2 | 72 |
| *ll | ذلل | 17 | 14 | 10 | 2 | 76 |
| jhl | جهل | 17 | 15 | 9 | 2 | 49 |
| fjr | فجر | 16 | 18 | 6 | 2 | 97 |
| wqE | وقع | 16 | 21 | 3 | 4 | 77 |
| gDb | غضب | 15 | 13 | 11 | 1 | 60 |
| fH$ | فحش | 15 | 13 | 11 | 2 | 65 |
| Emr | عمر | 14 | 15 | 9 | 2 | 52 |
| rqb | رقب | 14 | 11 | 13 | 2 | 90 |
| mrD | مرض | 13 | 3 | 21 | 2 | 74 |
| vmr | ثمر | 12 | 17 | 7 | 2 | 47 |
| A*y | اذي | 10 | 4 | 20 | 2 | 61 |

### Count = 25 (13 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Sly | صلي | 21 | 20 | 5 | 4 | 111 |
| flk | فلك | 20 | 23 | 2 | 2 | 45 |
| Hwl | حول | 19 | 17 | 8 | 2 | 46 |
| sqy | سقي | 19 | 18 | 7 | 2 | 91 |
| bTn | بطن | 18 | 15 | 10 | 2 | 57 |
| lsn | لسن | 18 | 17 | 8 | 3 | 90 |
| HDr | حضر | 16 | 16 | 9 | 2 | 81 |
| bsT | بسط | 15 | 16 | 9 | 2 | 71 |
| qsT | قسط | 15 | 9 | 16 | 2 | 72 |
| wEZ | وعظ | 14 | 11 | 14 | 2 | 65 |
| Hdd | حدد | 12 | 4 | 21 | 2 | 65 |
| whb | وهب | 12 | 21 | 4 | 3 | 42 |
| $ry | شري | 8 | 4 | 21 | 2 | 31 |

### Count = 27 (10 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| qmr | قمر | 23 | 24 | 3 | 6 | 91 |
| syr | سير | 21 | 22 | 5 | 3 | 81 |
| mnn | منن | 20 | 18 | 9 | 2 | 95 |
| $jr | شجر | 19 | 21 | 6 | 2 | 56 |
| E$r | عشر | 19 | 15 | 12 | 2 | 89 |
| bwb | بوب | 17 | 21 | 6 | 2 | 78 |
| Ejb | عجب | 17 | 14 | 13 | 2 | 72 |
| msk | مسك | 17 | 17 | 10 | 2 | 83 |
| grr | غرر | 14 | 17 | 10 | 3 | 82 |
| wzr | وزر | 11 | 26 | 1 | 6 | 94 |

### Count = 30 (6 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Afk | افك | 21 | 24 | 6 | 5 | 69 |
| sEy | سعي | 20 | 20 | 10 | 2 | 92 |
| Srf | صرف | 17 | 25 | 5 | 2 | 46 |
| Anv | انث | 17 | 19 | 11 | 2 | 92 |
| Esy | عسي | 16 | 15 | 15 | 2 | 68 |
| qSS | قصص | 14 | 23 | 7 | 2 | 40 |

### Count = 33 (8 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| $ms | شمس | 28 | 28 | 5 | 2 | 91 |
| Er$ | عرش | 25 | 28 | 5 | 2 | 85 |
| qsm | قسم | 24 | 26 | 7 | 4 | 90 |
| Emy | عمي | 22 | 22 | 11 | 2 | 80 |
| jnb | جنب | 21 | 20 | 13 | 3 | 92 |
| Zll | ظلل | 20 | 26 | 7 | 2 | 77 |
| kfy | كفي | 15 | 14 | 19 | 2 | 48 |
| Hjj | حجج | 10 | 10 | 23 | 2 | 45 |

### Count = 40 (3 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| flH | فلح | 24 | 23 | 17 | 2 | 91 |
| $Er | شعر | 23 | 30 | 10 | 2 | 69 |
| mlA | ملا | 18 | 38 | 2 | 2 | 72 |

### Count = 50 (3 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| nfE | نفع | 31 | 32 | 18 | 2 | 87 |
| fsd | فسد | 23 | 33 | 17 | 2 | 89 |
| Tyb | طيب | 23 | 21 | 29 | 2 | 61 |

### Count = 70 (4 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Elw | علو | 41 | 55 | 15 | 2 | 92 |
| mtE | متع | 38 | 43 | 27 | 2 | 80 |
| wkl | وكل | 29 | 44 | 26 | 3 | 73 |
| Erf | عرف | 26 | 20 | 50 | 2 | 83 |

### Count = 88 (2 roots)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| qrA | قرا | 42 | 78 | 10 | 2 | 96 |
| $Tn | شطن | 36 | 53 | 35 | 2 | 81 |

### Count = 99 (1 root)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| Slw | صلو | 37 | 40 | 59 | 2 | 108 |

### Count = 144 (1 root)

| Root | Arabic | n_surahs | meccan | medinan | first | last |
|---|---|---:|---:|---:|---:|---:|
| dwn | دون | 46 | 109 | 35 | 2 | 72 |

## 5. Roots whose total count equals their first-surah index

Filter: total occurrences ≥ 2 (a singleton always trivially has this if it
first appears in surah 1 — too noisy to report).

There are **39** such roots.

| Root | Arabic | Count = first_surah |
|---|---|---:|
| sjn | سجن | 12 |
| wrd | ورد | 11 |
| rhq | رهق | 10 |
| knz | كنز | 9 |
| nwq | نوق | 7 |
| DHw | ضحو | 7 |
| nkv | نكث | 7 |
| dkk | دكك | 7 |
| *rA | ذرا | 6 |
| HSd | حصد | 6 |
| $rE | شرع | 5 |
| myd | ميد | 5 |
| hnA | هنا | 4 |
| sfH | سفح | 4 |
| wfq | وفق | 4 |
| gsl | غسل | 4 |
| msH | مسح | 4 |
| nqr | نقر | 4 |
| slH | سلح | 4 |
| kbt | كبت | 3 |
| qrH | قرح | 3 |
| DjE | ضجع | 3 |
| x*l | خذل | 3 |
| rEd | رعد | 2 |
| SbE | صبع | 2 |
| sfk | سفك | 2 |
| HTT | حطط | 2 |
| glf | غلف | 2 |
| zHzH | زحزح | 2 |
| xrb | خرب | 2 |

## 6. Distribution uniformity (entropy / log N)

Computed as Shannon entropy of the per-surah occurrence vector divided by
log(114). 1.0 == perfectly uniform across all 114 surahs; 0.0 == fully
concentrated in one surah. Filter: total occurrences ≥ 5.

### Top 20 most uniformly distributed (across surahs)

| Rank | Root | Arabic | Occurrences | n_surahs | H_norm |
|---:|---|---|---:|---:|---:|
| 1 | smw | سمو | 381 | 81 | 0.8634 |
| 2 | xlq | خلق | 261 | 75 | 0.8563 |
| 3 | ywm | يوم | 405 | 75 | 0.8555 |
| 4 | ArD | ارض | 461 | 80 | 0.8505 |
| 5 | rAy | راي | 328 | 72 | 0.8479 |
| 6 | jnn | جنن | 201 | 70 | 0.8446 |
| 7 | rbb | ربب | 980 | 94 | 0.8362 |
| 8 | kll | كلل | 377 | 74 | 0.8330 |
| 9 | *kr | ذكر | 292 | 71 | 0.8296 |
| 10 | E*b | عذب | 373 | 68 | 0.8274 |
| 11 | bSr | بصر | 148 | 62 | 0.8221 |
| 12 | jEl | جعل | 346 | 66 | 0.8208 |
| 13 | Eml | عمل | 360 | 68 | 0.8197 |
| 14 | kwn | كون | 1390 | 86 | 0.8185 |
| 15 | rsl | رسل | 513 | 69 | 0.8183 |
| 16 | Elm | علم | 854 | 85 | 0.8176 |
| 17 | qdr | قدر | 132 | 58 | 0.8159 |
| 18 | byn | بين | 523 | 71 | 0.8134 |
| 19 | qbl | قبل | 294 | 64 | 0.8116 |
| 20 | $yA | شيا | 519 | 73 | 0.8102 |

### Top 20 most clustered (lowest entropy among ≥10-occurrence roots)

| Rank | Root | Arabic | Occurrences | n_surahs | H_norm |
|---:|---|---|---:|---:|---:|
| 1 | Alw | الو | 37 | 6 | 0.1470 |
| 2 | sjn | سجن | 12 | 3 | 0.1523 |
| 3 | Hlf | حلف | 13 | 5 | 0.2668 |
| 4 | sfh | سفه | 11 | 5 | 0.2886 |
| 5 | mAy | ماي | 10 | 5 | 0.2995 |
| 6 | Swm | صوم | 14 | 6 | 0.3100 |
| 7 | nSH | نصح | 13 | 6 | 0.3219 |
| 8 | ktm | كتم | 21 | 7 | 0.3311 |
| 9 | nkH | نكح | 23 | 6 | 0.3342 |
| 10 | rDE | رضع | 11 | 5 | 0.3366 |
| 11 | frD | فرض | 18 | 7 | 0.3398 |
| 12 | $bh | شبه | 12 | 6 | 0.3447 |
| 13 | ESw | عصو | 12 | 6 | 0.3447 |
| 14 | sbb | سبب | 11 | 6 | 0.3466 |
| 15 | fAy | فاي | 11 | 6 | 0.3466 |
| 16 | kyl | كيل | 16 | 7 | 0.3508 |
| 17 | jld | جلد | 13 | 6 | 0.3529 |
| 18 | bxl | بخل | 12 | 6 | 0.3539 |
| 19 | Awb | اوب | 17 | 8 | 0.3572 |
| 20 | fty | فتي | 21 | 7 | 0.3590 |

## 7. Replication of Family-B word-pair claims

**Method.** For each pair we report two counts: (a) the **root count**,
which is the number of stem-with-ROOT segments in Leeds QAC bearing the
relevant root, and (b) the **lemma counts**, broken out by individual
dictionary headword. The literature claims usually require a third,
hidden, surface-form filter — we make that filter explicit by reporting
every lemma so the reader can see which subset would be needed to recover
the claimed number.

Verdict legend: **verified** = the claim's number is reproduced under a
plain root-level rule; **partial** = reproduced only under a specific
lemma subset; **failed** = no rule reproduces the number; **requires-
cherry-picking** = a number close to the claim is recoverable but only
after excluding morphologically equivalent forms.

### yawm (day) / layl (night) — claim: both 365

| Side | Root (BW) | Root count | Top lemmas (count) |
|---|---|---:|---|
| yawm | `ywm` | 405 | `yawom` (405) |
| layl | `lyl` | 92 | `layol` (84), `layolap` (8) |

**Verdict:** Natural root counts: A(yawm)=405, B(layl)=92. Targets: A=365, B=365. **FAILED** — no single root or single lemma reproduces the claimed number on either side.

### rajul (man) / imra'a (woman) — claim: both 24

| Side | Root (BW) | Root count | Top lemmas (count) |
|---|---|---:|---|
| rajul | `rjl` | 73 | `rajul` (29), `rijaAl` (28), `rijol` (15), `rajil` (1) |
| imra'a | `mrA` | 38 | `{mora>at` (26), `{mori}` (5), `maro'` (4), `m~ariy^_#` (1), `{moru&NA` (1), `{mora>` (1) |

**Verdict:** Natural root counts: A(rajul)=73, B(imra'a)=38. Targets: A=24, B=24. **FAILED** — no single root or single lemma reproduces the claimed number on either side.

### bahr (sea) / barr (land) — claim: 32 / 13 (~71% sea)

| Side | Root (BW) | Root count | Top lemmas (count) |
|---|---|---:|---|
| bahr | `bHr` | 42 | `baHor` (41), `baHiyrap` (1) |
| barr | `brr` | 32 | `bar~` (22), `bir~` (8), `tabar~u` (2) |

**Verdict:** Natural root counts: A(bahr)=42, B(barr)=32. Targets: A=32, B=13. **FAILED** — no single root or single lemma reproduces the claimed number on either side.

### al-dunya / al-akhira — claim: both 115

| Side | Root (BW) | Root count | Top lemmas (count) |
|---|---|---:|---|
| dunya | `dnw` | 133 | `d~unoyaA` (115), `>adonaY`` (12), `daAniyap` (3), `danaA` (2), `daAn` (1) |
| akhira | `Axr` | 250 | `A^xir` (155), `A^xar` (70), `>ax~ara` (15), `yasota>oxiru` (6), `ta>ax~ara` (3), `musota_#oxiriyn` (1) |

**Verdict:** Natural root counts: A(dunya)=133, B(akhira)=250. Targets: A=115, B=115. **REQUIRES-CHERRY-PICKING** — only one side has a single-lemma exact match: `d~unoyaA` (side A); the other side has no lemma at the target count.

### mala'ika (angels) / shayatin (devils) — claim: both 88

| Side | Root (BW) | Root count | Top lemmas (count) |
|---|---|---:|---|
| malak/mala'ika | `mlk` | 206 | `malak` (88), `mulok` (48), `malakato` (44), `malik` (15), `malakuwt` (4), `ma`lik` (3), `m~amoluwk` (1), `malok` (1) |
| shaytan/shayatin | `$Tn` | 88 | `$ayoTa`n` (88) |

**Verdict:** Natural root counts: A(malak/mala'ika)=206, B(shaytan/shayatin)=88. Targets: A=88, B=88. **PARTIAL** — single-lemma subsets match: `malak`=88, `$ayoTa`n`=88. This requires choosing one lemma per root, which is the cherry-picking the literature does silently.

### al-hayat (life) / al-mawt (death) — claim: both 145

| Side | Root (BW) | Root count | Top lemmas (count) |
|---|---|---:|---|
| hayat | `Hyy` | 184 | `Hayaw`p` (76), `>aHoyaA` (51), `Hay~` (24), `yasotaHoYi.^` (9), `HaY~a` (7), `taHiy~ap` (6), `Hay~a` (4), `m~aHoyaA` (2) |
| mawt | `mwt` | 165 | `mawot` (50), `m~aAta` (39), `m~ay~it` (38), `>amaAta` (21), `mayotap` (6), `m~ayot` (5), `mamaAt` (3), `mawotat` (3) |

**Verdict:** Natural root counts: A(hayat)=184, B(mawt)=165. Targets: A=145, B=145. **FAILED** — no single root or single lemma reproduces the claimed number on either side.

### Adam / Isa (bonus check) — claim: both 25

This pair is in Family B but wasn't on the user's primary list; we checked it
opportunistically. The Leeds QAC proper-noun lemma counts:

| Side | Lemma (BW) | Count |
|---|---|---:|
| Adam | `A^dam` | 25 |
| Isa | `EiysaY` | 25 |

**Verdict:** **VERIFIED at the lemma level.** This is the only Family-B
word-pair claim in this run that survives a clean lemma-level check with no
form-filter cherry-picking. Note however that *both* are proper nouns with
no inflection in the Quran (which collapses lemma vs. surface-form vs. root
into a single number), so the apparent rigor is partly an artifact of the
lexical category. The "miraculousness" framing remains weak: with ~50
proper-noun lemmas in the Quran the chance of *some* matched-count pair is
very high (cf. §8 below — the count=25 row in the matched-pair enumeration
contains 13 distinct roots tied at 25, so picking the Adam/Isa pair from
those 13 is itself a fork).

## 8. Novel matching-count root pairs (count(A) == count(B), both ≥ 10)

**This is the gold-territory enumeration.** We list every pair of distinct
roots whose total occurrence counts in the Leeds QAC are exactly equal,
with both ≥ 10. The methodological point: under the McKay null, with
~2,000 roots above 10 occurrences and a count distribution this peaked,
we *expect* hundreds of accidentally-matching pairs. We report them all.
If apologetic literature picks any single one and calls it a miracle,
we now have the denominator to refute the claim.

- **Distinct count-values with ≥2 roots tied:** 84
- **Total unordered tied pairs:** 2,817

### Selected non-trivial groups

Showing all groups with count between 50 and 1000 — large enough to be
non-trivial, small enough to not be saturated:

| Count | # roots | Roots (BW) |
|---:|---:|---|
| 50 | 3 | fsd, Tyb, nfE |
| 51 | 2 | tHt, Hll |
| 52 | 2 | xbr, DEf |
| 56 | 3 | *hb, nhy, Ajl |
| 57 | 3 | Edd, qry, rwH |
| 59 | 4 | zkw, nsw, Zhr, rdd |
| 60 | 3 | gyb, ftn, fry |
| 61 | 2 | zyd, mss |
| 63 | 7 | Hmd, mwh, tlw, sHr, qDy, Ewd, *wq |
| 64 | 2 | jry, Hml |
| 65 | 2 | xsr, Eyn |
| 66 | 2 | wfy, jrm |
| 67 | 2 | bEv, ksb |
| 68 | 2 | wHd, hlk |
| 69 | 2 | skn, Znn |
| 70 | 4 | mtE, Erf, Elw, wkl |
| 73 | 5 | bAs, rDw, byt, rjl, gny |
| 75 | 3 | Alm, klm, $kr |
| 77 | 2 | Swb, blg |
| 78 | 2 | wjh, wHy |
| 83 | 3 | swy, kyf, Hrm |
| 87 | 2 | xld, twb |
| 88 | 2 | $Tn, qrA |
| 92 | 3 | sbH, sjd, lyl |
| 96 | 3 | qrb, bgy, Axw |
| 97 | 2 | SHb, Ans |
| 102 | 3 | A*n, $dd, wld |
| 104 | 2 | rjE, fDl |
| 108 | 2 | fEl, Ajr |
| 109 | 2 | Akl, Hsb |
| 119 | 2 | Amm, Ezz |
| 123 | 2 | rzq, b$r |
| 127 | 2 | xlf, Ahl |
| 129 | 4 | jmE, nZr, sAl, TwE |
| 140 | 2 | nEm, slm |
| 148 | 2 | bSr, rwd |
| 158 | 2 | bED, nSr |
| 160 | 2 | $hd, nbA |
| 167 | 2 | kvr, swA |
| 168 | 2 | qlb, $rk |
| 170 | 2 | Awl, qtl |
| 184 | 2 | bny, Hyy |
| 194 | 2 | nwr, Hsn |
| 201 | 2 | jnn, End |

Anyone who wants to claim that any one of these tied pairs is
'meaningful' must first explain why the other ~2817 coincident pairs are not.

## 9. Root palindromes

Arabic triliteral roots whose first and last consonants are identical
(letter[0] == letter[-1]). For 3-letter roots this is the canonical
'geminate-end' shape: e.g., `rbb` (lord), `mdd` (extend), `qll` (few).
These roots are common in Arabic and are not in themselves unusual; they
are listed for completeness so any claim about palindromic 'codes' has a
denominator.

- **Total root palindromes (any length):** 8
- **3-letter palindromes:** 8
- **4-letter palindromes:** 0
- **Other lengths:** 0

### Top 25 most frequent 3-letter palindromic roots

| Rank | Root | Arabic | Occurrences | n_surahs |
|---:|---|---|---:|---:|
| 1 | ydy | يدي | 120 | 47 |
| 2 | lyl | ليل | 92 | 49 |
| 3 | tHt | تحت | 51 | 30 |
| 4 | vlv | ثلث | 32 | 20 |
| 5 | bwb | بوب | 27 | 17 |
| 6 | sds | سدس | 5 | 3 |
| 7 | nwn | نون | 1 | 1 |
| 8 | SyS | صيص | 1 | 1 |

## 10. Single-surah roots with high count (thematic anchors)

Roots that appear ≥5 times but only in one surah — strong candidates for
surah-specific lexical signatures.

There are **5** such roots in the top 25.

| Rank | Root | Arabic | Count | Surah | Surah name |
|---:|---|---|---:|---:|---|
| 1 | myl | ميل | 6 | 4 | An-Nisa |
| 2 | Syd | صيد | 6 | 5 | Al-Ma'idah |
| 3 | qmS | قمص | 6 | 12 | Yusuf |
| 4 | khf | كهف | 6 | 18 | Al-Kahf |
| 5 | $Tr | شطر | 5 | 2 | Al-Baqarah |

## 11. Garden-of-forking-paths disclosure

This entire document is exploratory. No hypothesis was pre-registered;
everything was generated post-hoc by sweeping the corpus. The honest
framing is: each section above defines a *family of tests* that any
subsequent finding must be corrected against.

### Choices made after seeing the data
- The 'suspicious counts' list was chosen from the *prior* numerology
  literature (7, 19, 114, 786, 88, 145, 365 etc.) — not from looking at
  the data first. Honest in that respect.
- Threshold 'occurrences ≥ 5' for Meccan/Medinan filtering was chosen to
  drop singleton noise; alternatives (≥ 3, ≥ 10) give qualitatively
  similar lists.
- The novel-matching-count pair section uses ≥ 10 as the floor; this is
  arbitrary but reasonable.

### What this analysis CANNOT conclude
- It cannot conclude that any matched-count pair is 'miraculous'. The
  expected number of accidentally-matching pairs under any reasonable
  null is large (we report it above as a denominator).
- It cannot conclude that any single-surah anchor is 'thematic' — many
  high-frequency single-surah roots are simply names of people in the
  story (e.g., Yusuf in Sura 12, Maryam in Sura 19).
- It cannot adjudicate between traditional Meccan/Medinan attributions
  for the small number of contested surahs.

### Honest discussion of cherry-picking risk in the famous-pair claims

All six Family-B word-pair claims share the same structural defect:
the source counts are not the *natural* root counts. They are obtained
by selecting a specific subset of lemmas / inflectional forms after
the target number is known. Section 7's tables expose this directly:
each pair shows the natural root count (which never matches the claim)
and the lemma breakdown (which lets you see which subset would have to
be carved out to reach the claim).

The Adam/Jesus and qul/qala pairs (which our team's literature review
flagged as the only 'high-confidence' Family-B claims) were not part of
this run — see the lit-catalog and the dedicated replication agent for
those.
