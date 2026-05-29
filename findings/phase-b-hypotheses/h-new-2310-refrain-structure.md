---
id: H-NEW-2310
title: "Refrain / exact-repeated-verse structure — full census + spacing-regularity test"
type: finding
date: 2026-05-29
phase: B+
author: Waiel Al-Shujaa
verdict: "PASS-DIRECTED (5/9 refrain-pairs spaced more regularly than chance; famous anchors Q 55 + Q 77 both PASS, CV-robust, replicated)"
prereg_sha256: 6e4a571eea280ff83774659aa65845323730ddffd7e139ff0fe27b4661086935
seed: 20260509
n_perm: 10000
rules_tuple: "(no-tashkeel, orthographic-token verse-string, NFC+ws-collapsed, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2310 — Refrain / exact-repeated-verse structure

**Pre-reg**: `findings/phase-b-hypotheses/prereg-h-new-2310-refrain-structure.md`
(SHA-256 `6e4a571eea280ff83774659aa65845323730ddffd7e139ff0fe27b4661086935`,
verified at runtime). Seed 20260509, 10000 permutations. Bonferroni k = 9
(α_bon = 0.005556). Direction LOCKED before computation: refrain occurrences are
spaced **more regularly** (lower gap-variance) than random divider placement.

All counts re-derived from `quran-text/quran-no-tashkeel.json` at runtime via
`assert` (Q 55 = 31, Q 77 = 10, Q 54 = 4 confirmed — not assumed).

---

## 1. The exact-repeated-verse census (descriptive)

The corpus contains **94 distinct normalized verse-strings that appear ≥2×**:
- **24 intra-surah** repeated strings (a string recurring within one surah)
- **70 cross-surah** repeated strings (a string recurring in ≥2 surahs)
- **14 surahs** carry at least one intra-surah verse repeat (broad-refrain, ≥2).

### 1.1 Intra-surah refrains with count ≥4 (the inferential family)

| # | Surah | Refrain (no-tashkeel) | Count | N | Positions (ayah) |
|--:|:--|:--|--:|--:|:--|
| 1 | Q 55 al-Raḥmān | فبأي آلاء ربكما تكذبان | **31** | 78 | 13,16,18,21,23,25,28,30,32,34,36,38,40,42,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77 |
| 2 | Q 77 al-Mursalāt | ويل يومئذ للمكذبين | **10** | 50 | 15,19,24,28,34,37,40,45,47,49 |
| 3 | Q 26 al-Shuʿarāʾ | فاتقوا الله وأطيعون | 8 | 227 | 108,110,126,131,144,150,163,179 |
| 4 | Q 26 al-Shuʿarāʾ | وإن ربك لهو العزيز الرحيم | 8 | 227 | 9,68,104,122,140,159,175,191 |
| 5 | Q 26 al-Shuʿarāʾ | إن في ذلك لآية ۖ وما كان أكثرهم مؤمنين | 6 | 227 | 8,67,103,121,174,190 |
| 6 | Q 26 al-Shuʿarāʾ | إني لكم رسول أمين | 5 | 227 | 107,125,143,162,178 |
| 7 | Q 26 al-Shuʿarāʾ | وما أسألكم عليه من أجر ۖ إن أجري إلا على رب العالمين | 5 | 227 | 109,127,145,164,180 |
| 8 | Q 37 al-Ṣāffāt | إلا عباد الله المخلصين | 4 | 182 | 40,74,128,160 |
| 9 | Q 54 al-Qamar | ولقد يسرنا القرآن للذكر فهل من مدكر | 4 | 55 | 17,22,32,40 |

This reproduces the {Q 26, Q 37, Q 54, Q 55, Q 77} strict-refrain set established by
H-NEW-1230 / H-NEW-1320 / H-NEW-1790 (Q 26 quintuple confirmed), under a fourth
independent operationalization. All 5 famous refrains named in the task are present:
*fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* (Q 55, 31×), *waylun yawmaʾidhin
li-l-mukadhdhibīn* (Q 77, 10×), *wa-laqad yassarnā al-Qurʾāna li-l-dhikr* (Q 54, 4×),
plus the Q 26 prophet-cycle ring (5 refrains) and Q 37 (1 refrain ≥4).

### 1.2 Notable cross-surah verbatim repeats

| Global count | # surahs | String | Attestations |
|--:|--:|:--|:--|
| 11 | 2 | ويل يومئذ للمكذبين | Q 77 ×10 + **Q 83:10** (spillover) |
| 7 | 7 | حم (muqaṭṭaʿāt) | Q 40,41,42,43,44,45,46 (ḥawāmīm) |
| 6 | 6 | الم (muqaṭṭaʿāt) | Q 2,3,29,30,31,32 |
| 6 | 6 | ويقولون متى هذا الوعد إن كنتم صادقين | Q 10:48, 21:38, 27:71, 34:29, 36:48, 67:25 |
| 4 | 2 | إنا كذلك نجزي المحسنين | Q 37 ×3 + Q 77:44 |
| 3 | 3 | تنزيل الكتاب من الله العزيز الحكيم | Q 39:1, 45:2, 46:2 |
| 3 | 2 | فسبح باسم ربك العظيم | Q 56:74, 56:96 + Q 69:52 |

The full 94-string census (with every attestation) is in `csv/h-new-2310.json`.
The *wa-yaqūlūna matā hādhā al-waʿd* 6-surah eschatological-polemic refrain and the
ḥawāmīm/ALM muqaṭṭaʿāt rows reproduce H-NEW-1790 §10.70.4 / §10.70.6 exactly.

### 1.3 Near-exact supplement (MW-7 capped) — NULL

No family-refrain string has a single-particle variant that itself recurs ≥2× in
the corpus (edit-ratio ≥0.90 against the census yields **0 pairs**). The strict
refrains are crisp, fully-verbatim repeats with no near-miss siblings in the
repeated-verse pool. Reported as an honest null for the near-exact axis.

---

## 2. Spacing-regularity test — the inferential result

**Pre-committed direction confirmed for 5 of 9 (surah, refrain) pairs.** The
famous macro-refrains both PASS at Bonferroni strength and replicate at a second
seed.

| Surah | Refrain | m | V_obs | null median | p (var, left-tail) | CV-robust | Verdict |
|:--|:--|--:|--:|--:|--:|:-:|:--|
| **Q 55 al-Raḥmān** | fa-bi-ayyi ālāʾi… | 31 | **0.116** | 3.182 | **0.0001** | ✓ | **PASS** |
| **Q 77 al-Mursalāt** | waylun yawmaʾidhin… | 10 | **1.728** | 11.877 | **0.0039** | ✓ | **PASS** |
| Q 26 (rasūl amīn) | innī lakum rasūlun amīn | 5 | 1.188 | 666.2 | **0.0003** | ✓ | **PASS** |
| Q 26 (no-fee) | wa-mā asʾalukum… ajr | 5 | 1.188 | 655.9 | **0.0002** | ✓ | **PASS** |
| Q 26 (obey) | fa-ttaqū Allāh wa-aṭīʿūn | 8 | 27.84 | 391.7 | **0.0013** | ✗ | **PASS** |
| Q 54 al-Qamar | wa-laqad yassarnā… | 4 | 4.222 | 40.67 | 0.0846 | ✗ | NULL |
| Q 37 al-Ṣāffāt | illā ʿibāda Allāh… | 4 | 98.67 | 491.6 | 0.1480 | ✗ | NULL |
| Q 26 (close) | wa-inna rabbaka… ʿazīz | 8 | 223.7 | 390.5 | 0.2213 | ✗ | NULL |
| Q 26 (pre-close) | inna fī dhālika la-āya… | 6 | 308.2 | 560.7 | 0.2494 | ✗ | NULL |

Aggregate: **PASS = 5, DIRECTIONAL = 0, NULL = 4**. Every PASS is in the locked
direction (V_obs below null median); every NULL is direction-true-but-underpowered
(Q 54, p=0.085) or genuinely non-regular (Q 26 close/pre-close, Q 37).

### 2.1 What the result means

**The refrain-as-structural-divider intuition is confirmed where the refrain is a
true partitioner, and correctly rejected where it is not.** The test is *selective*,
not credulous:

- **Q 55** is the corpus exemplar of metronomic partition: 31 occurrences with
  inter-gap variance 0.116 (gaps almost all exactly 2, a few 3). The refrain
  literally clocks the surah. p = 1/10001 at both seeds.
- **Q 77** likewise partitions regularly (gaps 2-6, V = 1.73), p = 0.0039.
- **Q 26's interior prophet-cycle refrains** (rasūl-amīn, no-fee, obey) PASS because
  the Shuʿayb-onward prophet pericopes (Hūd, Ṣāliḥ, Lūṭ, Shuʿayb) close on an almost
  perfectly periodic 18-verse ring (positions 107/125/143/162/178 etc., gaps ≈ 18).
- **Q 26's whole-surah refrains** (close *wa-inna rabbaka…*, pre-close *inna fī
  dhālika…*) are NULL: they begin in the long irregular Mūsā-Pharaoh block
  (positions 8-9, 67-68) and only become periodic later, so their full-surah gap
  sequence is highly variable (V = 224 and 308). The test correctly distinguishes
  the **evenly-partitioning ring refrains** from the **whole-surah bracket refrains**
  inside the SAME surah — a discrimination no count-based inventory could make.
- **Q 54** *wa-laqad yassarnā* is direction-true (V=4.2 < null 40.7) but with only
  m=4 occurrences and N=55 the test is underpowered; raw p=0.085 misses 0.05.
  Honest NULL.
- **Q 37** *illā ʿibāda Allāh al-mukhlaṣīn* is NULL: its 4 occurrences (vv.
  40,74,128,160) sit at the heads of unequally-sized prophet stories, so spacing is
  irregular — the refrain is a *story-marker*, not a metronome. This refines the
  intuition exactly as the pre-reg anticipated: some refrains are rhythmic-emphatic
  partitioners (Q 55/77/26-ring), others are content-boundary markers without
  even spacing (Q 37, Q 26-bracket).

---

## 3. Robustness (MW protections)

- **MW-2**: 10000 permutations per pair.
- **MW-3 (alternative statistic)**: coefficient-of-variation of gaps, same null.
  The 3 strongest PASSes (Q 55, Q 77, Q 26-ring) are robust under BOTH variance and
  CV (CV-robust = ✓). The Q 26 *fa-ttaqū* PASS is variance-significant but not
  CV-robust (its absolute gaps are large, so CV is high even when variance beats
  the null) — flagged honestly.
- **MW-5 (replication)**: Q 55 and Q 77 re-run at seed 20260530 — direction and
  PASS verdict identical (Q 55 p=0.0001, Q 77 p=0.0025).
- **MW-6 (instrument-control)**: a phantom 10-divider placement in Q 56 al-Wāqiʿa
  (96 verses, no ≥4 refrain) yields p=0.6987 — sits at the null median, does NOT
  falsely pass. The test is not trivially significant for any 10-point subset.
- **MW-7**: near-exact census and the Q 26-bracket / Q 37 interpretive notes carry
  the single-test cap.

## 4. Rules-tuple sensitivity

Anchor counts are **invariant** across no-tashkeel and min-tashkeel lenses:
Q 55 = 31, Q 77 = 10, Q 54 = 4 in BOTH. The refrains are diacritic-independent
verbatim repeats; the finding is rules-tuple stable.

## 5. Classical anchoring

- al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on *al-tikrār* (repetition):
  repetition serves *taqrīr* (establishment) and *taqsīm* (partition). The Q 55 /
  Q 77 / Q 26-ring regular-spacing PASS is the empirical correlate of the *taqsīm*
  function; the Q 37 / Q 26-bracket NULL is the *taqrīr*-without-partition case.
- al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 60 (fī tikrār al-āyāt): names the
  Q 55 *fa-bi-ayyi ālāʾ* and Q 77 *waylun yawmaʾidhin* as the paradigm structural
  refrains. Their metronomic spacing (V = 0.12, 1.73) is now quantified.
- al-Tirmidhī #3357 frames Q 55's refrain liturgically (the jinn's responsive
  *wa-lā bi-shayʾin min niʿamika rabbanā nukadhdhib*) — a call-and-response that
  presupposes regular intervals, consistent with the V = 0.12 metronome.

## 6. Honest limits

- The test is per-(surah,refrain) pair; with only m=4 occurrences (Q 54, Q 37) it is
  low-powered, so a NULL there is "not-detected," not "proven-irregular."
- The null places dividers anywhere in {1,…,N}; it does not condition on the
  semantic constraint that a refrain must follow a content-unit. A stricter null
  (block-respecting) would likely make the regular cases even more extreme, so the
  uniform null is conservative for the PASS direction.
- Q 26's five refrains are not independent (they co-occur in the pericope ring), so
  the 3 PASS / 2 NULL split within Q 26 is one structural fact reported five ways,
  not five independent confirmations. Bonferroni k=9 already charges for this.
- The census is exact-verbatim on the no-tashkeel string; refrains that vary by a
  pronoun or particle across attestations (e.g. some prophet-intro variants) are
  NOT counted as the same refrain and appear only if they happen to be verbatim.

## 7. Connections

- **H-NEW-1230 / H-NEW-1320 / H-NEW-1790** (refrain inventory): H-NEW-2310 is the
  4th inter-verifying enumeration AND adds the orthogonal spacing-geometry axis the
  inventory findings did not test.
- **H-NEW-2100** (within-verse reduplication) + **H-NEW-2140** (verse-initial
  anaphora runs): H-NEW-2310 completes the repetition-architecture map at the
  **distributed-refrain / inter-verse-spacing** scale. Scale ladder under
  cross-finding-025-formal: within-verse (2100) → verse-initial-run (2140) →
  distributed-refrain-spacing (**2310**) → cross-surah-refrain (1790 §10.70.6).
- **cross-finding-025-formal (scale-of-aggregation)**: the Q 26 within-surah split
  (interior ring PASS vs whole-surah bracket NULL) is itself a scale-of-aggregation
  effect — regularity is a property of the *pericope-ring* sub-scale, not the
  whole-surah scale.

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2310-refrain-structure.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2310.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2310.json`
- Findings: `findings/phase-b-hypotheses/h-new-2310-refrain-structure.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
