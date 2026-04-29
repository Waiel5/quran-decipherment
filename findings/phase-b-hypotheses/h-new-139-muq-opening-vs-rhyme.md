---
id: H-NEW-139
title: Muqaṭṭāʿat opening letters predict verse-final rhyme (fāṣila) letters
phase: B
status: PASS-DIRECTED (post-hoc single-test α=0.05 cap; extreme p survives)
date: 2026-04-17
executed_by: team-lead (inline)
parent_findings: [H-NEW-113, cross-finding-008, H-NEW-45, H-NEW-46]
classical_anchor: al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān, §on fawātiḥ al-suwar and muqaṭṭāʿat (classical balāgha claim — the muqaṭṭāʿat letters 'rhyme-prefigure' the surah's fāṣila letters)
seed: 20260417
rules_tuple: (no-tashkeel; 29 muq-opened surahs; top-3 verse-final letters excluding v1 of muq surahs; 10K perm null; subset-size-matched random letter draw from 28-letter alphabet)
bonferroni_k: 1
bonferroni_family: h-new-139-muq-rhyme-overlap
alpha_bon: 0.05
direction: POSITIVE — observed match count > null (one-sided upper-tail)
verdict: RETRACTED (null-model artifact, see H-NEW-139.1)
retraction_date: 2026-04-17
retraction_source: H-NEW-139.1 (frequency-weighted null gives z=-2.43 direction-reversed)
---

# [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] — Muqaṭṭāʿat opening letters predict verse-final rhyme (fāṣila)

> **2026-04-17 RETRACTION NOTICE**: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s PASS-DIRECTED verdict is RETRACTED under [[h-new-139-1-freq-weighted|H-NEW-139.1]] frequency-weighted null replication. The original uniform-28-letter null was the wrong reference distribution; under the correct frequency-weighted null (drawing letters in proportion to their actual fāṣila frequency), z drops from +5.96 to −2.43 (direction-reversed). Observed 21/29 is BELOW the weighted null mean of 24.76. Details: `findings/phase-b-hypotheses/h-new-139-1-freq-weighted.md`. audit-037's adversarial flag is empirically confirmed. Classical al-Suyūṭī rhyme-prefiguration claim is NOT validated by this test.

## Classical anchor

al-Suyūṭī in al-Itqān notes that classical balāgha scholars observed that muqaṭṭāʿat opening letters tend to prefigure each surah's fāṣila (rhyme-ending) letter pattern. This is a rhetorical/aesthetic claim in classical tradition — the muqaṭṭāʿat set the "key" or "mode" of the surah, which is echoed in the verse-endings.

This test operationalizes the claim empirically.

## Hypothesis

For each of 29 muqaṭṭāʿat-opened surahs:
- Let `OPEN(s)` = set of unique Arabic letters in the opening muqaṭṭāʿat string
- Let `TOP3(s)` = top-3 most-frequent verse-final letters (excluding v1, the muqaṭṭāʿat-opening verse itself)
- Define `match(s)` = 1 if `OPEN(s) ∩ TOP3(s) ≠ ∅`

**Observed**: Σ match(s) = **21 / 29**.

## Null

Random subset of same size as `OPEN(s)` drawn uniformly from the 28-letter Arabic alphabet; compute same statistic. 10,000 permutations, seed 20260417.

| Quantity | Value |
|---|---:|
| Observed matches | **21 / 29 (72.4%)** |
| Null mean | 7.30 / 29 (25.2%) |
| Null std | 2.30 |
| Null max (over 10K) | 16 |
| **z-score** | **+5.96** |
| **p_one-sided upper-tail** | **< 0.0001** |

## Per-surah results

| Q | Opening | Top-3 rhyme | Overlap |
|:-:|:--|:--|:-:|
| 2 | الم | ن م ر | 1/3 |
| 3 | الم | ن م ر | 1/3 |
| 7 | المص | ن م ل | 2/4 |
| 10 | الر | ن م ل | 1/3 |
| 11 | الر | ن د ب | **0/3** |
| 12 | الر | ن م ر | 1/3 |
| 13 | المر | ب ر ل | 2/4 |
| 14 | الر | ر د م | 1/3 |
| 15 | الر | ن م ل | 1/3 |
| 19 | كهيعص | ا ن م | **0/5** |
| 20 | طه | ى ا ي | **0/2** |
| 26 | طسم | ن م ل | 1/3 |
| 27 | طس | ن م ۩ | **0/2** |
| 28 | طسم | ن م ل | 1/3 |
| 29 | الم | ن م ر | 1/3 |
| 30 | الم | ن م ر | 1/3 |
| 31 | الم | ر م ن | 1/3 |
| 32 | الم | ن م ۩ | 1/3 |
| 36 | يس | ن م | **0/2** |
| 38 | ص | ب ن ر | **0/1** |
| 40 | حم | ن ب ر | **0/2** |
| 41 | حم | ن م د | 1/2 |
| 42 | حمعسق | ر م ن | 1/5 |
| 43 | حم | ن م ل | 1/2 |
| 44 | حم | ن م | 1/2 |
| 45 | حم | ن م | 1/2 |
| 46 | حم | ن م ر | 1/2 |
| 50 | ق | د ب ج | **0/1** |
| 68 | ن | ن م | 1/1 |

**21 passes, 8 fails**.

## Fail cases analysis (8 surahs where overlap is 0)

- **Q 11 الر**: rhyme ن د ب — dominated by narrative-prophet strong-verb endings (kaddhaba, kāna)
- **Q 19 كهيعص**: rhyme ى ا ي — Maryam surah uses long-vowel rhyme (a distinct prosodic mode); the 5-letter muq is the MOST COMPLEX opening but its rhyme is a different pattern
- **Q 20 طه**: same long-vowel rhyme pattern as Q 19 (ى ا ي)
- **Q 27 طس**: rhyme ن م — Q 27 is Q 26/27/28 trio but uniquely 2-letter muq; rhyme pattern matches Q 26 and Q 28 (طسم), not its own 2-letter opening
- **Q 36 يس**: rhyme ن م — Q 36 is disjoint from its 2-letter opening despite being classically "heart of Quran"
- **Q 38 ص**, **Q 40 حم**, **Q 50 ق**: single-letter openings (ص, ق) with 0 rhyme-match; interesting that single-letter muq are MORE likely to fail this test

## Interpretation

Under PASS framing (21/29 match), classical balāgha is empirically validated at p < 10⁻⁴. The muqaṭṭāʿat opening letters DO correlate systematically with verse-final rhyme letters far beyond chance.

The 8 fail cases cluster into 2 groups:
- **Long-vowel-rhyme surahs** (Q 19, 20): use alif/yaʾ-based rhyme schemes that don't match their consonantal muq openings
- **Single-letter muq** (Q 38, 40 secondary, 50): the 1-letter opening doesn't match; may be because 1-letter is too sparse to show pattern

This is consistent with [[h-new-113-letter-position|H-NEW-113]] (muqaṭṭāʿat letters verse-final-enriched): the muq letters are not only verse-final-positioned in general, they are SPECIFICALLY the rhyme letters of their own surahs.

## Post-hoc disclosure

Test designed 2026-04-17 AFTER [[h-new-113-letter-position|H-NEW-113]] verse-final enrichment was confirmed. Classical balāgha anchor was identified post-hoc but the anchor predates the project (al-Suyūṭī 15th c.). Direction positive was predicted BEFORE running the null. Per project discipline single-test α=0.05 ceiling applies; extreme p (< 10⁻⁴) survives with enormous margin.

Not yet cross-feature replicated; PASS-DIRECTED ceiling stands.

## Connection to prior findings

- **Extends cross-finding-006 (13+ muq design axes)**: adds RHYME-PREFIGURATION as axis 14
- **Extends cross-finding-008 (muq → book-introduction markers)**: muq letters mark book-introduction AND rhyme scheme
- **Refines [[h-new-113-letter-position|H-NEW-113]] (muq verse-final enrichment)**: now resolved at the surah-specific level, not just corpus-level
- **Supports theorist P5 → P1★ merged**: muq letters are multi-function markers (book-intro + chronological + now rhyme-mode)
- **Partially resolves OQ-1 (why specific letter-set per surah)**: answers that the letter-set correlates with the surah's rhyme mode; this is a LOCAL not GLOBAL answer

## Follow-up queue

- [[h-new-139-1-freq-weighted|H-NEW-139.1]]: test the same statistic under independent replication on bigram-level rhyme patterns
- [[h-new-139-2-shuffle-null|H-NEW-139.2]]: for the 8 fail cases, test whether EXTENDED-letter-set (opening + 1-letter neighbors in phonetic space) recovers the match
- Long-vowel-rhyme sub-cluster test (Q 19, 20): is this a distinct rhyme-mode sub-class?

## Classical wisdom integration

al-Suyūṭī's Itqān (nawʿ 71, fawātiḥ al-suwar) discusses multiple interpretations of muqaṭṭāʿat. Among them, the aesthetic claim that they prefigure the surah's rhyme is associated with classical muʿjizāt literature (the miracle-of-the-Quran's-rhetoric tradition). Our empirical confirmation at z = +5.96 is the first quantitative verification of this claim in modern scholarship that I'm aware of.

This is classical scholarship VALIDATED by rigorous statistics — a productive synthesis.

## Files

- Inline script: this session
- Findings: this file
- Pre-reg: embedded in findings frontmatter (inline execution; no standalone pre-reg file given post-hoc origin)
- Permutation null details: reproducible at seed 20260417 with the Python code in session journal
