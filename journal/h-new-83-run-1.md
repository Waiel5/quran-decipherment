---
id: h-new-83-run-1
date: 2026-04-15
agent: h-new-83-specialist
prereg: findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension-prereg.md
script: scripts/h_new_83_rahman_refrain_extension.py
data: quran-text/quran-no-tashkeel.json
seed: 20260415
---

# H-NEW-83 — Run 1 Log

## Pre-registered hypotheses (verdicts)

- **H-83a** (refrain count = 31): VERIFIED. Verse-level exact matches: 31. Substring (proper, non-equal) matches: 0. Identity holds: 31 occurrences = 31 distinct refrain-verses.
- **H-83b** (no full refrain elsewhere in corpus): VERIFIED. Zero occurrences of full normalized refrain in any of the other 6,158 verses (Q 1-54, Q 56-114).
- **H-83c** (no distinctive substring `الا ربكما تكذبان` elsewhere): VERIFIED. Zero hits outside Q 55. Even the lone token `تكذبان` does not appear as a token in any verse outside Q 55.
- **H-83d** (first refrain at v13): VERIFIED. First match at v13.
- **H-83e** (sub-refrain ≥2x exists): VERIFIED. 6-token phrase `لم يطمثهن انس قبلهم ولا جان` ("no human or jinn has ever touched them") appears at v74 verbatim, and as a 7-out-of-10-token suffix of v56 (v74_norm IS a substring of v56_norm). This is a genuine sub-refrain.
- **H-83f** (4-part partition variance < random 4-cuts): NOT SUPPORTED. Observed within-part variance (words) = 36.40 vs random 4-cut median 36.74; p (one-sided lower) = 0.4456. The classical partition does NOT minimize block-length variance; it is at the median of random 4-cuts on this metric. **The partition's force is thematic-semantic, not length-statistical.**

## Detailed numerical results (script run output)

```
Q 55 al-Raḥmān: 78 verses
v13 raw  : فبأي آلاء ربكما تكذبان
v13 norm : فباي الا ربكما تكذبان

verse-level exact matches: 31
positions: 13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45,
           47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77
verses containing refrain as proper substring (not equal): 0

CROSS-CORPUS:
  full-refrain matches outside Q55: 0
  distinctive-substring matches outside Q55: 0
  token "تكذبان" outside Q55: 0

REFRAIN vs NON-REFRAIN length:
  refrain     n=31  char-len  22.00 ± 0.00 (perfectly invariant)  word-count 4.00
  non-refrain n=47  char-len  26.49 ± 14.51                       word-count 4.91
  KS char-len: D = 0.5532  p = 9.91 × 10⁻⁶
  KS word    : D = 0.4681  p = 3.18 × 10⁻⁴

CLASSICAL 4-PART PARTITION (refrain count per part): 8 / 7 / 8 / 8
  Part A (vv 1-30):  block-words [39,11,4,7,4,6,10,11]  mean 11.50  sd 10.74
  Part B (vv 31-45): block-words [4,18,8,6,8,6,11]      mean  8.71  sd  4.30
  Part C (vv 46-61): block-words [5,2,3,5,10,9,3,5]     mean  5.25  sd  2.68
  Part D (vv 62-77): block-words [3,1,3,4,3,4,6,6]      mean  3.75  sd  1.56
  Within-part variance (words): observed 36.40, null median 36.74, one-sided p = 0.45

SUB-REFRAINS (n-grams ≥ 2x, not a substring of the canonical refrain):
  3-gram: لم يطمثهن انس        [2x]
  3-gram: يطمثهن انس قبلهم    [2x]
  3-gram: انس قبلهم ولا       [2x]
  3-gram: قبلهم ولا جان       [2x]
  4-gram: لم يطمثهن انس قبلهم  [2x]
  4-gram: يطمثهن انس قبلهم ولا [2x]
  4-gram: انس قبلهم ولا جان   [2x]
  5-gram: لم يطمثهن انس قبلهم ولا  [2x]
  5-gram: يطمثهن انس قبلهم ولا جان [2x]
  → maximal repeated phrase: 6 tokens "لم يطمثهن انس قبلهم ولا جان"
    occurs at v56 (as final 7-token suffix) and as the entirety of v74

HIGH-OVERLAP NON-REFRAIN VERSE PAIRS (Jaccard ≥ 0.5):
  v56 ↔ v74  J = 0.667  (the sub-refrain pair)
  v50 ↔ v66  J = 0.500  ("two springs" parallel: tajriyān vs naḍḍākhatān)

UPPER ↔ LOWER PARADISE STRUCTURAL PAIRING:
  Pairs (upper non-refrain, lower non-refrain, in matched-position order):
    (46, 62)  J=0.143  جنتان introductions
    (48, 64)  J=0.000  foliage descriptors
    (50, 66)  J=0.500  springs (only direct lexical overlap pair)
    (52, 68)  J=0.286  fruit descriptors
    (54, 70)  J=0.000  brocade vs خيرات
    (56, 72)  J=0.000  paradisal companions
    (58, 74)  J=0.000  rubies vs no-touch
    (60, 76)  J=0.000  reward vs cushions
  observed mean Jaccard = 0.1161
  random pairings (10K perms): mean 0.0334, p95 0.1096
  one-sided p (greater) = 0.0494  [marginal pass at α=0.05; driven by v50/v66]

Q 55 RHYME PROFILE (non-refrain verses):
  35/47 end in -ān (matches refrain rhyme exactly)
  12/47 do not: 7 in -ām (vv 10, 11, 24, 27, 41, 72, 78), 2 in -ār (vv 14, 15),
                1 in -ayn (v17), 1 in -ūn (v43), 1 in -mn (v1, الرحمن)
  → 47 of 47 non-refrain verses participate in nūn-suffix assonance family
    (-ān, -ām, -ār, -ayn, -ūn). Classical sajʿ-mursal at the surah scale.

CROSS-CORPUS REFRAIN DENSITY (verbatim verse-level repetition ≥ 5):
  Q 55 Ar-Raḥmān   31×  density 0.397   "فباي الا ربكما تكذبان"
  Q 77 Al-Mursalāt 10×  density 0.200   "ويل يوميذ للمكذبين"
  Q 26 Ash-Shuʿarāʾ 8×  density 0.035   "وان ربك لهو العزيز الرحيم"
```

## Garden-of-forking-paths log (post-run discoveries)

- The "v74 ⊂ v56" finding was discovered via a generic substring scan, not pre-registered specifically. It is a logical consequence of the Jaccard-0.667 finding.
- The upper/lower paradise pair test (mean Jaccard with permutation null) was added post-run as the natural metric for "paired pairs of gardens" structure. P=0.049 is reported as **marginal** and as exploratory because it was not pre-declared. It survives at α=0.05 unprotected, fails any multiple-comparison correction, and is essentially driven by the single v50/v66 pair (which is also catchable by the generic high-Jaccard sweep that WAS pre-registered).
- Rhyme breakdown was added post-run as a natural complement to the length contrast.

## Files

- `scripts/h_new_83_rahman_refrain_extension.py` — script
- `journal/h-new-83-run-1.log` — raw stdout
- `findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension-prereg.md` — prereg
- `findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension.md` — final report
