---
surah: 59
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
authored_by: Waiel Al-Shujaa
---

# Q 59 al-Ḥashr — Empirical architectural profile

## 1. Length / token / letter inventory

| Measure | Value | Source |
|:--|--:|:--|
| Verse count | 24 | Hafs-Kūfan |
| Word count (no-tashkeel, ornament-stripped) | 447 | Q059-F-01 script computation |
| Letter count (no-tashkeel, sans spaces) | 1,970 | computed |
| Mean words/verse | 18.6 | computed |
| Median verse-length (words) | ~14 | computed |

Q 59 is in the upper third of corpus surahs by total word-count and is the **3rd-longest of the 10 short-Medinan-block surahs** (Q 57-66) behind only Q 57 (W=618) and Q 58 (W=516). The mean 18.6 words/verse is corpus-mid (corpus mean ~12).

## 2. Rhyme architecture

| Final letter | Verses | % |
|:--|--:|--:|
| ن | 14 | 58.3 |
| م | 5 | 20.8 |
| ر | 3 | 12.5 |
| ب | 2 | 8.3 |

**Shannon entropy: 1.108 nats** (moderate — multi-tonal, not monorhyme).

Compare:
- Q 55 al-Raḥmān: 0.42 nats (near-monorhyme on ن via the 31× refrain)
- Q 37 al-Ṣāffāt: 0.70 nats (low; ن-dominant 79.7%)
- Q 59 al-Ḥashr: 1.108 nats (moderate)
- Corpus mean: ~1.4 nats

Q 59 is **multi-rhymed but ن-dominant** — consistent with its mid-Medinan stylistic register where rhyme is less tight than mid-Meccan oath-cluster surahs.

## 3. Divine-name density profile

### Per-verse 99-name token count (proclitic-tolerant substring rule)

| v | F99 | Tokens |
|:-:|:-:|:--|
| 1 | 3 | الله, العزيز, الحكيم |
| 2 | 4 | الله ×2, الله, الله |
| 3 | 1 | الله |
| 4 | 4 | الله ×4 |
| 5 | 1 | الله |
| 6 | 2 | الله ×2 |
| 7 | 4 | الله ×4 |
| 8 | 1 | الله |
| 9 | 0 | — |
| 10 | 0 | — |
| 11 | 1 | الله |
| 12 | 0 | — |
| 13 | 1 | الله |
| 14 | 0 | — |
| 15 | 0 | — |
| 16 | 1 | الله |
| 17 | 0 | — |
| 18 | 2 | الله ×2 |
| 19 | 1 | الله |
| 20 | 0 | — |
| 21 | 1 | الله |
| 22 | **3** | الله, الرحمن, الرحيم |
| 23 | **10** | الله ×2, الملك, القدوس, السلام, المؤمن, المهيمن, العزيز, الجبار, المتكبر |
| 24 | **6** | الله, الخالق, البارئ, المصور, العزيز, الحكيم |

**Per-Q 59 totals**:
- F99 = 44 tokens (sum across 24 verses)
- vv 22-24 carry 19/44 = **43.2% of all Q 59 divine-name tokens** in 3 of 24 verses (12.5% of verses)

### Within-Q 59 3-verse-window ranking (Q059-F-05)

| Rank | Window | F99 | Words | Density |
|:-:|:--|:-:|:-:|:-:|
| 1 | **vv 22-24 (Khawātim)** | **19** | 49 | 0.388 |
| 2 | vv 21-23 | 14 | 50 | 0.280 |
| 3 | vv 6-8 | 8 | 80 | 0.100 |
| 4 | vv 4-6 | 7 | 50 | 0.140 |
| 5 | vv 5-7 | 7 | 75 | 0.093 |

Within-surah word-count-weighted permutation null (N=10,000, seed=20260509):
- p (max-F ≥ 19): **0.0004**
- p (max-density ≥ 0.388): **0.0000**

**Verdict: STRONG-PASS at α_bon = 0.025** for both axes — Q 59:22-24 is the densest internal window even after controlling for length-conditional name-distribution.

## 4. Khawātim absolute corpus rank (Q059-F-01)

Replicates [[h-new-95-khawatim-extension|H-NEW-95]] Cell E:

| Window | F99 | Words | Density | Corpus rank by F | Corpus rank by density (W≥10) |
|:--|:-:|:-:|:-:|:-:|:-:|
| **Q 59:22-24** | **19** | 49 | 0.388 | **1 of 6,234** | 2 of 5,963 |
| Q 1:1-3 (basmala+ḥamd+raḥmān) | 5 | 10 | 0.500 | 1192 | **1 of 5,963** |
| Q 59:23–Q 60:1 | 18 | 85 | 0.212 | 2 of 6,234 | — |
| Q 2:282-284 | 14 | 189 | 0.074 | 3 of 6,234 | — |
| Q 59:21-23 | 14 | 50 | 0.280 | 4 of 6,234 | 7 of 5,963 |

**Honest disclosure: Q 1:1-3 (basmala + al-ḥamdu lillāh + al-raḥmān al-raḥīm) edges Q 59:22-24 on per-token density by 0.500 vs 0.388**. Under absolute count F99, Q 59:22-24 is rank 1 by 5+ token margin. Per the brief's "replicate H-NEW-95 within this finding context" instruction:
- **H-NEW-95 absolute-count finding REPLICATED** at corpus rank 1.
- **The novel "per-token density" extension** does not yield rank-1 Q 59 because basmala+ḥamd is denser per word.

## 5. Q 59 ↔ Q 62 al-Jumuʿah pair test (Q059-F-03)

| Metric | Value |
|:--|--:|
| Q 59 ↔ Q 62 token-set Jaccard | 0.1163 |
| Q 59 ↔ Q 62 harmonic-mean W | 253.6 |
| Length-matched-Medinan-pool size (harmonic ∈ [0.7, 1.5] × obs) | 105 pairs |
| Pool-mean Jaccard | 0.0835 |
| **p (Jaccard ≥ obs) length-matched** | **0.143** |
| **p unconditional 28-Medinan pool** | **0.165** |

**Verdict: NULL.**

Q 59's Medinan partners by token-Jaccard (top-10):

| Rank | Partner | Jaccard |
|:-:|:--|--:|
| 1 | Q 64 al-Taghābun | 0.1643 |
| 2 | Q 58 al-Mujādilah | 0.1366 |
| 3 | Q 57 al-Ḥadīd | 0.1350 |
| 4 | Q 8 al-Anfāl | 0.1164 |
| **5** | **Q 62 al-Jumuʿah** | **0.1163** |
| 6 | Q 24 al-Nūr | 0.1156 |
| 7 | Q 48 al-Fatḥ | 0.1147 |
| 8 | Q 13 al-Raʿd | 0.1111 |
| 9 | Q 60 al-Mumtaḥanah | 0.1093 |
| 10 | Q 49 al-Ḥujurāt | 0.1073 |

**Substantive interpretation**: Q 59 ↔ Q 62 token-bag overlap is INDISTINGUISHABLE from random length-matched-Medinan partners. The H-NEW-95 Khawātim-bridge at Q 62:1 is a **verse-level phenomenon** (3 of the 4 echoed names are Khawātim-exclusive); it does NOT extend to general surah-vocabulary alignment. Q 59's tightest Medinan partner is **Q 64 al-Taghābun** (the OTHER imperfect-tense musabbiḥa), not Q 62.

This is a **negative finding for the Khawātim-cluster-as-surah-cluster claim** — the cluster operates at verse granularity, not surah granularity. Honest replication-failure published with equal prominence per HANDOFF/04-DISCIPLINE §"Honesty over cheerleading."

## 6. Perfect-trio sub-pair structure (Q059-F-02)

Within H-NEW-58c's perfect-tense trio {Q 57, Q 59, Q 61}:

| Pair | Shared char-prefix | Jaccard |
|:--|:-:|:-:|
| Q 57 + Q 59 | 24 | 0.1350 |
| Q 57 + Q 61 | 24 | 0.1062 |
| **Q 59 + Q 61** | **53** | 0.1017 |

**Q 59:1 and Q 61:1 are character-identical for all 53 chars.** Q 57:1 differs at character 24 (والأرض vs وما في الأرض → Q 57 elides the وما في).

**Refinement of [[h-new-58c-musabbihat-tense-split|H-NEW-58c]]**: the perfect-trio is not flat-symmetric; it has a TIGHT INNER PAIR (Q 59+61) and a LOOSE OUTER ELEMENT (Q 57). The Q 57+59 pair (which the brief asked about specifically) is at the **trio prefix-mean (24 chars)**, NOT tighter — the brief's "even tighter than full Q 57/59/61 trio" hypothesis is **rejected**: the trio mean (33.3 chars) is dragged down by the Q 57 outliers; Q 57+59 at 24 is BELOW that mean.

The full musabbiḥāt-5 cluster cohesion within short-Medinan (5 of 10 surahs):
- Observed total-pair-prefix-sum: 138 chars
- Random 5-of-10 short-Medinan subset null (N=10,000): pool-mean ≈ 19 chars
- **p (sum ≥ 138) = 0.0036** → **PASS at α_bon = 0.0167** (Q059-F-02 family k=3).

## 7. Khawātim terminal-three placement (Q059-F-04)

Across 109 corpus surahs with V ≥ 5 verses, only **8 surahs (7.3%)** have their highest-F 99-name 3-verse-window at the absolute terminal-3 position. Restricted to high-F (best-window F ≥ 5), the set narrows to **5 surahs**:

| Surah | Type | V | Best F | Window |
|:--|:--|--:|:-:|:--|
| **Q 59 al-Ḥashr** | Medinan | 24 | **19** | vv 22-24 |
| Q 58 al-Mujādilah | Medinan | 22 | 9 | vv 20-22 |
| Q 48 al-Fatḥ | Medinan | 29 | 8 | vv 27-29 |
| Q 57 al-Ḥadīd | Medinan | 29 | 7 | vv 27-29 |
| Q 73 al-Muzzammil | Meccan | 20 | 7 | vv 18-20 |

**Strong descriptive finding**: 4 of 5 (80%) high-F-terminal surahs are Medinan, and 4 of 5 are inside the H-NEW-1080 short-Medinan-block (Q 57-66) + Q 48 (Medinan tail of the long-Medinan block). The terminal-3 high-F-name placement is a **Medinan-coda divine-name engineering signature**, with Q 59 dominant by F-magnitude (19 vs next 9). Q 73 is the lone Meccan member.

## 8. Cross-feature summary table

| Feature | Q 59 value | Corpus-rank | Verdict |
|:--|--:|:-:|:--|
| 3-verse-window F99 (corpus) | 19 | **1 of 6,234** | H-NEW-95 replicated |
| 3-verse-window density (W≥10, corpus) | 0.388 | 2 of 5,963 | Q 1:1-3 wins on density |
| Within-Q 59 best-window | 19 | 1 of 22 | p=0.0004 within-surah |
| Q 59 ↔ Q 62 Jaccard | 0.116 | rank 5/27 in Q 59's Medinan-partners | NULL |
| Perfect-trio pair tightness (Q 57+59 prefix) | 24 | tied 24 with Q 57+61 | not tightest |
| Perfect-trio pair tightness (Q 59+61 prefix) | 53 | tightest in trio | identical 53 chars |
| Musabbiḥāt-5 cluster sum (within short-Med) | 138 | p=0.0036 | PASS |
| Khawātim terminal-3 placement | YES | 1 of 5 corpus high-F surahs | DESCRIPTIVE |

## 9. Reproducibility

All five JSON outputs at `csv/Q059-F-0[1-5].json` carry SHA-256-locked pre-reg hashes:

| Test | Pre-reg SHA | JSON | Result |
|:--|:--|:--|:--|
| Q059-F-01 | `94185027...0ad0` | `csv/Q059-F-01.json` | PARTIAL (1/2 cells PASS) |
| Q059-F-02 | `62521470...ea9d` | `csv/Q059-F-02.json` | PASS (cluster cohesion) |
| Q059-F-03 | `d0fa6ad0...88d0` | `csv/Q059-F-03.json` | NULL |
| Q059-F-04 | `82bd1f90...af93` | `csv/Q059-F-04.json` | DESCRIPTIVE-PASS |
| Q059-F-05 | `6d7d116c...3ef2` | `csv/Q059-F-05.json` | CONFIRMED |

Seed = 20260509 across all tests. Python 3 stdlib only; deterministic.
