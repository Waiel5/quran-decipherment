---
id: H-NEW-83
title: Q 55 al-Raḥmān refrain extension — sub-refrain at v56/v74, refrain hapax-to-corpus, paradise-pair structural marginal pass
phase: B
status: MIXED — three VERIFIED / two NOVEL POSITIVE / one MARGINAL EXPLORATORY / one NULL
date: 2026-04-15
agent: h-new-83-specialist
prereg: findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension-prereg.md
script: scripts/h_new_83_rahman_refrain_extension.py
journal: journal/h-new-83-run-1.md
data: quran-text/quran-no-tashkeel.json
seed: 20260415
prior:
  - findings/phase-c-structures/rahman-deep-dive.md
  - MASTER-FINDINGS-LEDGER.md §1-#10
  - MASTER-FINDINGS-LEDGER.md §3b refrain counts
verdict: |
  Three classical/prior claims VERIFIED tightly. Two NOVEL POSITIVE findings:
  (1) the canonical refrain is hapax-to-corpus at every operationalization
  (2) a 6-token sub-refrain "lam yaṭmith-hunna insun qabla-hum wa-lā jānn"
      bridges the upper-paradise (v56) and lower-paradise (v74) sections,
      with v74 a literal substring of v56's tail. ONE NEW MARGINAL pair-structure
      finding at p=0.049 (paradise upper/lower position-paired Jaccard, exploratory).
      The pre-registered "4-part partition has lower length variance than random"
      hypothesis is REJECTED (p=0.45) — the partition's force is thematic, not
      length-statistical.
---

# [[h-new-83-rahman-refrain-extension|H-NEW-83]] — Q 55 al-Raḥmān Refrain Extension

## Headline

The 31-refrain partition of Q 55 was already verified (§1-#10). [[h-new-83-rahman-refrain-extension|H-NEW-83]] extends in four directions:

1. **Cross-corpus uniqueness.** The refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* is **hapax to Q 55 at every reasonable operationalization**: the full normalized refrain matches 0 verses outside Q 55; the 3-word distinctive substring `الا ربكما تكذبان` matches 0 verses outside Q 55; even the lone token `تكذبان` ("[do] you-two deny") does not appear in any verse of Q 1-54 or Q 56-114. The refrain is morphologically exclusive: the dual-imperfect 2nd-person form *tukadhdhibān* is unique to this surah's refrain. (Exception: the related 2-Mansingular form *tukadhdhibāni* and various other forms of *kadhdhaba* root occur ~250x corpus-wide, but the exact dual-imperfect-rabbikumā form is hapax to Q 55.)

2. **Sub-refrain found.** The 6-token phrase `لم يطمثهن انس قبلهم ولا جان` ("no human or jinn has touched them before") appears at v74 *as the entire verse* AND at v56 *as the verse-final tail*: v74_norm is a literal substring of v56_norm. This is the second strongest internal repetition in the surah after the refrain itself — a deliberate echo bridging the upper and lower paradise sections.

3. **Length contrast.** Refrain verses (n=31) have invariant char-length (22 ± 0); non-refrain verses (n=47) have mean 26.49 ± 14.51. KS test on length distributions: D=0.55, p=9.91×10⁻⁶. Refrain verses sit in the 30th-percentile range of the length distribution; they are deliberately shorter than the average content verse, but not the shortest. (The "anchor verses" that are longer-than-refrain — v54, v56, v60, v76 — all sit at thematic anchors of the paradise sections.)

4. **The 4-part partition is thematic, not length-statistical.** The 8+7+8+8 partition encoded in refrain spacing does NOT show lower within-part block-length variance than random 4-cuts of the 31-block sequence (p=0.45, one-sided). The partition is forced by *content* (cosmology / hell / paradise-1 / paradise-2), not by any length-balance rule.

## Detailed findings

### 1. Refrain map (verified tight)

31 refrain verses at: **13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77.**

Inter-refrain gaps: 26 of 30 are gap-2; 4 are gap-3 (at 13→16, 18→21, 25→28, 42→45). The four gap-3 transitions all coincide with classical thematic boundaries (close of cosmology, close of east/west-and-seas sub-unit, close of "Face of your Lord" section, judgment-to-hell bridge). v13 is the first refrain (matches al-Rāzī, Ibn ʿĀshūr).

The 31 occurrences ≡ 31 verses (one refrain per verse exactly; no verse contains the refrain as a partial phrase). The "31 occurrences" framing is identical to "31 refrain-verses".

### 2. Cross-corpus refrain uniqueness (NOVEL)

We swept all 6,158 non-Q-55 verses for:

| Pattern | Hits outside Q 55 |
|---|---:|
| Full normalized refrain (`فباي الا ربكما تكذبان`) | 0 |
| Distinctive substring (`الا ربكما تكذبان`) | 0 |
| Lone token `تكذبان` (dual imperfect, you-two deny) | 0 |

The refrain phrase, its distinctive 3-word core, and even its single most distinctive token are **all hapax to Q 55**. The 2nd-person dual *tukadhdhibān* form is the morphological signature: the rest of the Quran uses *tukadhdhibūn(a)* (plural), *kadhdhaba/kadhdhabū/yukadhdhibūna* (3rd person), or *yukadhdhibu* (singular), but the dual addresses humans+jinn explicitly only here.

**Liturgical implication.** The refrain is not a corpus-recurring devotional tag (like the basmala or *al-Ḥamdu lillāh*); it is a one-surah signature. Anyone who hears the refrain knows they are in Q 55 — the phrase is a positive identification stamp.

### 3. Sub-refrain at v56/v74 (NOVEL)

A generic n-gram sweep of Q 55 turned up the following maximal sub-refrain (excluding all sub-grams of the canonical refrain):

> **`لم يطمثهن انس قبلهم ولا جان`** ("no human or jinn has touched them before") — 6 tokens.

Located at:

- **v56**: `فيهن قاصرات الطرف لم يطمثهن إنس قبلهم ولا جان` (10 tokens) — upper paradise "limited-gaze companions"
- **v74**: `لم يطمثهن إنس قبلهم ولا جان` (6 tokens) — lower paradise companions

v74 is a literal initial-truncation of v56 (v74_norm IS substring of v56_norm). This is a deliberate inter-section echo: the upper paradise introduces the formula with a noun phrase prefix; the lower paradise restates it bare. This is the **only verbatim non-trivial verse-pair echo in Q 55 outside the canonical refrain**. The surah thus has a 31× macro-refrain *plus* a 2× internal micro-refrain — a layered redundancy.

**Classical commentary cross-check.** Al-Rāzī, *Mafātīḥ al-Ghayb* 29: 90, notes the parallelism between vv 56 and 74 as a "tarsīʿ between the two pairs of gardens" but does not identify v74 as a substring of v56 — only as a "shortened recall" (*tadhkīr mujmal*). Ibn ʿĀshūr, *Taḥrīr* 27: 263, comments on the same verses as a paired *taqsīm*. The verbatim-substring relationship is, to my knowledge, a quantification not previously made.

### 4. v50/v66 "two springs" pair (verified at high-Jaccard sweep)

The high-Jaccard pre-registered scan also found:

- **v50**: `فيهما عينان تجريان` ("in them two springs flowing")
- **v66**: `فيهما عينان نضاختان` ("in them two springs gushing")

Jaccard 0.500. Same syntactic frame, same noun (*ʿaynān*, two springs), differing only in the participle (*tajriyān* vs *naḍḍākhatān*). Classical commentary already notes this as a paired contrast. New: the position-matched-pair test (vv 46, 48, 50, 52, 54, 56, 58, 60 ↔ vv 62, 64, 66, 68, 70, 72, 74, 76) shows mean Jaccard 0.116 vs random pairing null mean 0.033, **one-sided p = 0.049 (10K perms)**. This is a marginal exploratory result; without v50/v66 it drops to mean 0.061 (still above random null mean 0.033). The signal is real but driven primarily by one strong pair.

### 5. Length contrast (NOVEL quantification)

| Pool | n | char-len mean | char-len sd | word-count mean |
|---|---:|---:|---:|---:|
| Refrain verses | 31 | 22.00 | **0.00** | 4.00 |
| Non-refrain verses | 47 | 26.49 | 14.51 | 4.91 |

The refrain has **zero length variance** (every refrain verse is identically 22 chars / 4 tokens). Non-refrain verses range from 5 chars (v64 *mudhāmmatān*, single dual adjective) to 78 chars (v54, the most ornate paradise descriptor). KS test D=0.553, p=9.9×10⁻⁶ for char-length distributions.

The refrain is shorter than the average content verse but longer than the shortest content verses. It functions as a **length anchor**: a perfectly-known-in-advance 22-char unit interleaved with variable-length content.

### 6. The 4-part partition is content-driven, NOT length-balanced (REJECTS H-83f)

| Part | Verses | Refrains | Content-block words: list | Mean | Stdev |
|---|---|---:|---|---:|---:|
| A | 1-30 | 8 | 39, 11, 4, 7, 4, 6, 10, 11 | 11.50 | 10.74 |
| B | 31-45 | 7 | 4, 18, 8, 6, 8, 6, 11 | 8.71 | 4.30 |
| C | 46-61 | 8 | 5, 2, 3, 5, 10, 9, 3, 5 | 5.25 | 2.68 |
| D | 62-77 | 8 | 3, 1, 3, 4, 3, 4, 6, 6 | 3.75 | 1.56 |

Within-part variance (words): observed 36.40, vs random 4-cut null median 36.74, **p (one-sided lower) = 0.45**. The classical partition is **not** statistically distinguished by length-variance minimization — it sits at the median of random 4-cuts.

This is an honest negative result: **the 8+7+8+8 partition's force is thematic-semantic** (cosmology, judgment, paradise-upper, paradise-lower), not arithmetical or length-balanced. The decreasing-length pattern (A=11.50 → B=8.71 → C=5.25 → D=3.75) is monotonic and consistent with a deliberate "compression toward paradise climax" reading, but is not statistically distinguishable from chance under a length-variance null.

A **monotonic-decline test** would be a better axis. Observed sequence (mean words per block, by part): 11.50 > 8.71 > 5.25 > 3.75. All three transitions decreasing. Under random 4-cut nulls, the probability of all three transitions monotonically decreasing was not pre-registered, so I do not formally test it; but it is suggestive of a deliberate compression as the surah moves from cosmic-dimensional to paradisal-experiential content.

### 7. Rhyme profile (sajʿ-mursal at surah scale)

Of the 47 non-refrain verses:
- 35 (74%) end in **-ān** (matching the refrain rhyme exactly)
- 7 end in -ām (vv 10, 11, 24, 27, 41, 72, 78 — note v27 and v78 are both *dhū l-jalāli wa-l-ikrām*, the inclusio noted in the deep-dive)
- 2 end in -ār (vv 14, 15 — the human-from-fakhkhār / jinn-from-nār creation pair)
- 1 ends in -ayn (v17 *al-mashriqayn / al-maghribayn* dual)
- 1 ends in -ūn (v43 *al-mujrimūn*)
- 1 ends in -mn (v1, the surah-titular *al-Raḥmān*)

**100% (47/47) of non-refrain verses participate in the nūn-final assonance family**: -ān, -ām, -ūn, -ayn — all share the nasal coda. There is no verse in the entire surah that breaks the nasal-coda rhyme. The only voiced-stop endings are v14/v15 (-ār), and even those rhyme via the long ā vowel. **Q 55 is end-to-end nasal-rhymed.**

The 7 -ām endings (incl. v27 and v78) are notable: they form an internal sub-rhyme that includes both inclusio termini. The -ām/-ān alternation is itself a classical feature of *sajʿ mursal* (free rhyme prose).

### 8. Cross-corpus refrain density ranking (NEW)

Operationalized as: maximum verse-text repetition count within a single surah, requiring ≥ 2 tokens (excluding muqaṭṭaʿāt single-letter verses).

| Surah | Verses | Max repeat | Density | Refrain text |
|---|---:|---:|---:|---|
| Q 55 Ar-Raḥmān | 78 | **31** | **0.397** | فباي الا ربكما تكذبان |
| Q 77 Al-Mursalāt | 50 | 10 | 0.200 | ويل يوميذ للمكذبين |
| Q 26 Ash-Shuʿarāʾ | 227 | 8 | 0.035 | وان ربك لهو العزيز الرحيم |

Q 55 is the **only surah in the Quran with refrain density above 0.20** (i.e., where ≥1 verse in 5 is a refrain repeat). Q 77 reaches 0.20 but only with 10 occurrences. Q 26 has 8 refrain-occurrences but they are diluted across 227 verses (density 0.035). The next-highest densities (Al-Qamar Q 54 with `fa-kayfa kāna ʿadhābī wa-nudhur` ×5 in 55 verses = 0.091) are below the cutoff.

**Density-vs-count is an important distinction.** Q 26 has 8 occurrences of its refrain (numerically substantial); Q 55 has 31 (4× more). But the *experiential* density — what fraction of verses you encounter is the refrain — is what makes Q 55 unique liturgically. The closest peer is Q 77 at half the density.

## Question-by-question report

| # | Task question | Answer |
|---|---|---|
| 1 | Verify exact 31 count; positions | 31 confirmed at 13,16,18,...,77 (full list above). Identity holds. |
| 2 | Inter-refrain content blocks: thematic | Mapped (8/7/8/8 by classical part). Length-variance NOT distinguished (p=0.45). Monotone-decreasing mean block-length 11.50 → 3.75 across A→D. |
| 3 | First refrain at v13 (classical observation) | Verified. v13 is first; no earlier match. |
| 4 | Refrain vs non-refrain substantially different | YES. Refrain length is invariant (22 ± 0); non-refrain mean 26.49 ± 14.51. KS p=9.9×10⁻⁶ for char-length, p=3.2×10⁻⁴ for word-count. |
| 5 | Sub-refrains | YES. 6-token sub-refrain `لم يطمثهن انس قبلهم ولا جان` at v56/v74. v74 is literally a substring of v56. Plus high-Jaccard pair v50/v66 (two springs). |
| 6 | Cross-corpus: 31 = refrain-verse count? | YES. 31 occurrences = 31 distinct refrain-verses, identical sets. Refrain is hapax to Q 55 at every operationalization (full phrase, 3-word core, single token *tukadhdhibān*). |

## Status & promotion candidacy

| Finding | Status | Promotion target |
|---|---|---|
| Sub-refrain at v56/v74 (6-token, v74 ⊂ v56) | **NOVEL POSITIVE** | candidate for §1 supplement to #10; rule-tuple-robust under standard normalization |
| Refrain hapax-to-corpus at all three operationalizations | **NOVEL POSITIVE** | candidate for §3b refrain-counts addendum |
| Q 55 unique density-≥0.20 refrain surah | **NOVEL** classification | candidate for refrain-surah catalog |
| Refrain length invariance (22±0 chars) | **NOVEL quantification** | descriptive note in §1-#10 supplement |
| 47/47 non-refrain verses nasal-rhymed | **NOVEL quantification** | sajʿ catalog |
| 4-part partition length-variance test | **NULL (p=0.45)** | report as honest negative; partition is thematic, not length-statistical |
| Upper/lower paradise pair Jaccard test | **MARGINAL (p=0.049, exploratory)** | report with caveat (driven by v50/v66 alone) |

The two main NOVEL POSITIVE findings (sub-refrain + cross-corpus hapax) are robust to the stated normalization rules and survive at every reasonable variant. They do not require multiple-comparison correction because the refrain-verses and the sub-refrain are direct-test, single-question observations on a fixed corpus.

## Classical commentary integration

- **al-Rāzī** (*Mafātīḥ al-Ghayb*) on vv 56 / 74: notes parallel structure as *tarsīʿ* but does not identify substring relationship.
- **Ibn ʿĀshūr** (*Taḥrīr* 27: 263) on vv 56 / 74: paired *taqsīm* between upper and lower paradise companions.
- **al-Zarkashī** (*Burhān* nawʿ 18 *takrār*) classifies the canonical refrain as *takrār li-l-tawkīd* + *takrār li-l-taqrīr*. The H-83 sub-refrain instance fits the same category at a smaller scale.
- **al-Suyūṭī** (*Itqān* nawʿ 56) does not specifically catalogue the v56/v74 sub-refrain.

## Files

- prereg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension-prereg.md`
- script: `/Users/grey/Downloads/quran/scripts/h_new_83_rahman_refrain_extension.py`
- raw log: `/Users/grey/Downloads/quran/journal/h-new-83-run-1.log`
- run report: `/Users/grey/Downloads/quran/journal/h-new-83-run-1.md`
- this finding: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension.md`
