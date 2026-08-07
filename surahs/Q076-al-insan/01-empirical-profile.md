---
surah: 76
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
---

# Q 76 al-Insān (al-Dahr) — Empirical Profile


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

## 1. Anchors

| Metric | Q 76 value | Corpus rank | Source |
|:--|--:|:--:|:--|
| Verse count | 31 | — | hafs |
| Word count | 250 | — | quran-no-tashkeel.json |
| Letter count (no-tashkeel) | 1,094 | — | computed |
| Mean words/verse | 8.06 | — | computed |
| Distinct roots | 112 | — | root-index.json (filter for Q 76) |
| Mushaf order | 76 | — | canonical |
| Tanzil revelation order | 98 | — | revelation-order.csv |
| Nöldeke order | 52 | — | revelation-order.csv |
| FR-content mean distance to others | 0.9084 | (corpus median 0.957) | h-new-111.json |
| Rhyme entropy | 0.0 (single-rāwī) | rank 1 of 4 alif-100% surahs | h-new-750.json |

## 2. ⭐ Paradise-vocabulary density — CORPUS-EXACT-EXTREME

Per `Q076-F-01` (4/4 cells PASS):

| Cell | Test | Q 76 | Result |
|:-:|:--|:-:|:-:|
| A | per-surah density rank | 18.000% (rank 1/114, sep 1.84× over rank-2) | PASS |
| B | top-5 of 5,174 11-verse windows | all 5 inside Q 76 (and 9/10 in top-10) | PASS-EXTREME |
| C | length-matched 31-verse permutation null | obs 18.0% vs null mean 0.45%, null max 3.96%, p<0.0001 | PASS |
| D | paradise-vocab-distribution null (10K perms) | rank-1 by chance: 5/10,000, p=0.0005 | PASS |

The classical-balāgha tradition (al-Zamakhsharī *Kashshāf*, al-Rāzī *Mafātīḥ al-Ghayb*, al-Qurṭubī *Jāmiʿ*) treats Q 76:5-22 as the "paradise-tableau core" of the surah. The empirical signature confirms this at the highest possible rigor: **Q 76 is the most paradise-saturated surah in the Qurʾān at any operationalization**.

### 2.1 The 95-term paradise-vocabulary lexicon

The lexicon (saved at `csv/Q076-F-01-paradise-lexicon.json`) covers:

**Core jannah-anatomical**: jannah, abrār, kaʾs, kāfūr, ʿaynā, salsabīl, zanjabīl, sundus, istabraq, arāʾik, dāniya, wildān, lulu, ḥarīr, asāwir, akwāb, qawārīr, fiḍḍa, sharāb, ṭuhūr, naḍrah, surūr, naʿīm, mukhladūn, manthūr, ẓilāl, qaṭūf, fawākih, ḥadāʾiq, firdaws, ʿadn, ḥūr, ʿīn, sidr, ṭalḥ, manḍūd, mamdūda, maskūb, furush, baṭāʾin, mubaththath, marfūʿa, mawḍūʿa, maṣfūfa, kawāʿib, mukhdam, mubtahash, etc.

**Excluded** (polysemous / contrastive): mulk (kingdom-vs-angel), kabīr (too generic), saʿīr/sharr (hellfire-side, contrastive).

### 2.2 The Q 76 paradise-tableau verses (vv. 5-22)

Verses 5-22 contain **35 paradise-tokens / 132 words** (26.5%) and form the densest tableau-block. Verses 11-21 form the **single highest-density 11-verse window in the entire corpus** at 46.43% (39 paradise-tokens / 84 words).

```
v5  : إن [الأبرار] [يشربون] من [كأس] كان مزاجها [كافورا]
v6  : [عينا] يشرب بها عباد الله [يفجرونها] [تفجيرا]
v7  : يوفون بالنذر ويخافون يوما كان شره مستطيرا
v8  : ويطعمون الطعام على حبه مسكينا ويتيما وأسيرا
v9  : إنما نطعمكم لوجه الله لا نريد منكم جزاء ولا شكورا
v10 : إنا نخاف من ربنا يوما عبوسا قمطريرا
v11 : فوقاهم الله شر ذلك اليوم ولقاهم [نضرة] [وسرورا]
v12 : وجزاهم بما صبروا [جنة] [وحريرا]
v13 : [متكئين] فيها على [الأرائك] لا يرون فيها شمسا ولا زمهريرا
v14 : [ودانية] عليهم [ظلالها] وذللت [قطوفها] [تذليلا]
v15 : [ويطاف] عليهم بآنية من [فضة] [وأكواب] كانت [قواريرا]
v16 : [قوارير] من [فضة] قدروها [تقديرا]
v17 : [ويسقون] فيها [كأسا] كان مزاجها [زنجبيلا]
v18 : [عينا] فيها تسمى [سلسبيلا]
v19 : [ويطوف] عليهم [ولدان] [مخلدون] إذا رأيتهم حسبتهم [لؤلؤا] [منثورا]
v20 : وإذا رأيت ثم رأيت [نعيما] وملكا كبيرا
v21 : عاليهم [ثياب] [سندس] خضر [وإستبرق] [وحلوا] [أساور] من [فضة] [وسقاهم] ربهم [شرابا] [طهورا]
v22 : إن هذا كان لكم جزاء وكان سعيكم مشكورا
```

(brackets mark paradise-vocabulary hits; the lexicon includes both bare and cliticized variants)

## 3. ⭐ Single-rāwī monorhyme — CORPUS-EXACT longest 100%-alif

Per `Q076-F-02` (2/2 cells PASS):

| 100%-alif surah | Verses | Rāwī |
|:--|--:|:-:|
| **Q 76 al-Insān** | **31** ⭐ | ا |
| Q 48 al-Fatḥ | 29 | ا |
| Q 72 al-Jinn | 28 | ا |
| Q 91 al-Shams | 15 | ا |

Q 76 is also rank-2 / 13 of all 100%-monorhyme surahs in the corpus (only Q 54 al-Qamar at 55v exceeds it, with rāʾ rāwī).

### 3.1 The fāṣila inventory

All 31 Q 76 fāṣila tokens (verse-final words in Hafs no-tashkeel form):
```
v01 mudhakkūrā    v07 mustaṭīrā    v13 zamharīrā    v19 manthūrā    v25 wa-aṣīlā
v02 baṣīrā        v08 wa-asīrā     v14 tadhlīlā     v20 kabīrā      v26 ṭawīlā
v03 kafūrā        v09 shakūrā      v15 qawārīrā     v21 ṭuhūrā      v27 thaqīlā
v04 saʿīrā        v10 qamṭarīrā    v16 taqdīrā      v22 mashkūrā    v28 tabdīlā
v05 kāfūrā        v11 wa-surūrā    v17 zanjabīlā    v23 tanzīlā     v29 sabīlā
v06 tafjīrā       v12 wa-ḥarīrā    v18 salsabīlā    v24 kafūrā      v30 ḥakīmā
                                                                      v31 alīmā
```

The rhyme-pattern is overwhelmingly **-īrā / -ūrā / -īlā / -ālā** (Form-IV / Form-X passive participles in tanwīn-naṣb plus comparable tanwīn-alif endings). **27 of 31 verses end in tanwīn-alif on a long vowel + r/l/m**. The two final verses Q 76:30-31 (`ḥakīmā`, `alīmā`) shift the consonant from r/l to m, marking the closure of the surah's main rhyme stretch.

This is one of the most metrically-uniform stretches of the Qurʾān at any window length ≥ 28.

## 4. ⭐ Q 75 ↔ Q 76 mushaf-adjacent pair-cohesion

Per `Q076-F-03` (2/2 cells PASS):

- Q 75-76 is **1 of only 2 mushaf-adjacent pairs** with the creation-triplet {xlq, Ans, nTf} in BOTH surahs.
- The random-pair triplet co-occurrence rate is 0.68% (10K-perm null).
- Q 75 ↔ Q 76 FR-distance = **0.8165** at the 24th percentile (within FR-close tail).

### 4.1 The shared-roots inventory between Q 75 and Q 76

22 shared roots: nDr (look), fjr (gush/spring), rwd (will), qrr (settle), Hbb (love), lqy (meet), jEl (make), *kr (mention), bSr (see), kwn (be), Ans (human), nTf (sperm-drop), rbb (lord), $ms (sun), xlq (create), Ejl (hasten), qdr (measure), Hsb (count/reckon), wjh (face), qrA (recite/read), and others.

The shared-root profile is **creation-axis** (xlq, Ans, nTf, jEl), **vision-axis** (nDr, bSr, rAy), **lordship-axis** (rbb, jEl), and **eschatological-attestation** (*kr, Hsb, qdr).

## 5. Surah-level 4-axis architectural signature

Per `h-new-590` and `h-new-840`:

| Axis | Q 76 value | Classification |
|:--|--:|:-:|
| UAS (Unified Architectural Signature) | -0.8089 | NULL (cluster member, not outlier) |
| sig_A (per h-new-750) | -1.246 | low-cohesion outlier (rank 91/114) |
| sig_B | -1.758 | low-cohesion outlier (rank 107/114) |
| z_rhyme_entropy | -1.394 | bottom-tier (single-rāwī) |
| z_mean_content_distance | -0.148 | near-median |
| z_local_cohesion | -0.364 | slightly below median |

Q 76's signature is "high-rhyme-uniformity, near-corpus-median content-distance, slightly-below-median local-cohesion." This is consistent with the surah being a single-tableau composition (one extended paradise-image) rather than a multi-tableau composition (which would yield higher local-cohesion via tableau-clustering).

## 6. Chronology classification

Per `data/revelation-order.csv` Q 76 row:
- **Tanzil Egyptian Standard**: revelation-order #98, **Medinan**
- **Nöldeke**: order #52, **Middle Meccan**

This is the **largest phase-shift in the Q 73-78 mushaf-neighborhood**, with all other surahs in this block agreeing on Early-Meccan (between both schemes).

### 6.1 Sunni traditional argument for Medinan

The classical Sunni position (al-Wāḥidī *Asbāb al-Nuzūl*; al-Suyūṭī *al-Itqān*) classifies Q 76 as Medinan because:
1. The Ahl-al-Bayt revelation-cause narrative requires post-Hijra setting (the *asīr* / captive in Q 76:8 implies post-Badr captives)
2. Surah classified as Medinan in al-Suyūṭī's classification chart
3. Some classical isnāds tie revelation specifically to a Medinan event

### 6.2 Western critical argument for Meccan

Nöldeke and Bell classify Q 76 as Middle Meccan because:
1. Stylistic features: short rhythmic verses, single-rāwī monorhyme, paradise-tableau, no legal content — all hallmarks of Middle Meccan
2. The hal-atā opener pattern (rhetorical question opener) is a Meccan-style feature
3. The *asīr* term need not be war-captive; it can also mean "household-bonded servant" or general "captive" in pre-Islamic Arabian usage

### 6.3 Empirical-structural angle

Q 76's empirical structural features (single-rāwī, paradise-tableau density, FR-cohort with terminal-Mufaṣṣal) are the **stylistic signature of Meccan Mufaṣṣal**, not of Medinan-late surahs (which tend to be longer, multi-rāwī, and have law-text density). The 4-axis structural signature (`h-new-840` UAS = -0.81, low-cohesion-outlier sig_B = -1.76) places Q 76 firmly in the Meccan-Mufaṣṣal cluster.

**Empirical-leaning verdict**: structural features point to Meccan-late or Middle-Meccan rather than Medinan. This does NOT refute the Sunni traditional Medinan classification (which depends on revelation-cause narrative attribution), but it documents that the structural signature is Meccan-typical.

## 7. Mushaf-adjacency cost (per `h-new-720`)

| Pair | delta_raw | Expense rank |
|:--|--:|:--:|
| Q 74 → Q 75 | +0.0962 | rank 49/113 |
| Q 75 → Q 76 | +0.0518 | rank 66/113 |
| Q 76 → Q 77 | +0.0879 | rank 41/113 |

The Q 75 → Q 76 seam is mid-rank in expense (cheaper than half of all transitions); the Q 76 → Q 77 seam is moderately expensive. Neither qualifies as a universal-hinge (top-15) nor as a seamless seam (clamped-zero, bottom-13). Q 76 sits in a structurally-coherent local-Mufaṣṣal block.

## 8. Per-verse word-count distribution

```
v01: 11    v07: 7     v13: 11    v19: 10    v25: 5
v02: 10    v08: 7     v14: 6     v20: 7     v26: 7
v03: 7     v09: 10    v15: 8     v21: 14    v27: 8
v04: 6     v10: 7     v16: 5     v22: 8     v28: 10
v05: 8     v11: 8     v17: 6     v23: 6     v29: 10
v06: 7     v12: 5     v18: 4     v24: 9     v30: 12
                                              v31: 11
```

Mean 8.06; min 4 (v18 *ʿaynan fīhā tusammā salsabīlā*); max 14 (v21 *ʿāliyahum thiyāb sundus khuḍr wa-istabraq…*). The longest verse (v21) carries the densest single-verse paradise-vocabulary load (8 paradise-tokens in 14 words = 57.1%) — the **rank-1 single-verse paradise-density** in the corpus.

## 9. Vocabulary uniqueness

Of Q 76's 197 distinct word-types, **52 (26.4%) are corpus-hapax — appearing ONLY in Q 76**. This is an extremely high uniqueness rate; the corpus average is closer to 8-12%. Examples:
- `kāfūrā` (Q 76:5) — camphor; corpus-only
- `qamṭarīrā` (Q 76:10) — gloomy/severe; corpus-only
- `zamharīrā` (Q 76:13) — bitter cold; corpus-only
- `salsabīlā` (Q 76:18) — Salsabīl (paradise-spring); corpus-only
- `zanjabīlā` (Q 76:17) — ginger; corpus-only
- `qawārīrā` (Q 76:15) — crystal vessels; corpus-only
- `lulūʾā manthūrā` (Q 76:19) — scattered pearls; corpus-only-bigram

Many are paradise-tableau terms; many are eschatological-affect terms (qamṭarīr = severe gloomy, zamharīr = bitter cold). Q 76's paradise-vocabulary is largely Q 76-specific — it adds new lexical material rather than recycling already-established jannah-vocabulary.
