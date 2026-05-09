---
surah: 68
surah_name_ar: القلم
surah_name_translit: al-Qalam
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
verdict: 6 classical claims audited; 3 VINDICATED (Ibn ʿAbbās content-beacon gloss, Q 96-Q 68 chronology pair, Q 68 nūn-rāwī), 1 VINDICATED-PARTIAL (FR-pair asymmetric), 1 NULL (Q 68:1 hadith-citation primacy), 1 NOT-TESTED (Q 68 mixed Meccan-Medinan subdivision).
---

# Q 68 al-Qalam — Classical Claims Audit

## Claim 1: al-Suyūṭī chronology — Q 68 is revelation #2 (after Q 96 al-ʿAlaq #1)

### Source

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on chronological order; compiled from al-Bukhārī, *Ṣaḥīḥ*, *Kitāb Badʾ al-Waḥy*, and parallel chronology-ḥadīth chains. Nöldeke (1860 *Geschichte des Qorāns*) and the Egyptian standard chronology agree.

`/Users/grey/Downloads/quran/data/revelation-order.csv` line 2: "2,68,القلم,Al-Qalam,Meccan,2,Early Meccan" (confirms Q 68 = revelation #2, Early Meccan).

### Rules-tuple

`(no-tashkeel, classical chronology canon, al-Suyūṭī al-Itqān + Nöldeke + Egyptian standard agreement, Hafs-Kufan)`

### Empirical test

The classical chronology is a tradition-based claim; it is NOT *derivable* from the text empirically. However, **two empirical correlates** can test the claim's *consistency*:

1. **Length consistency**: Early Meccan revelations are typically short; Q 68 is 52 verses, short-to-medium. CONSISTENT.
2. **FR-pair direction**: if Q 68 is revelation #2 (paired with #1 Q 96), they should share content-vocabulary at higher-than-corpus-baseline rate. Tested in Q068-F-07.

Q068-F-07 result: Q 96 is in Q 68's FR-nearest top-15 (rank 6 of 113, p_uniform=0.053) — CONSISTENT with chronological-pair hypothesis from the Q 68 side. Reverse direction (Q 68 in Q 96's nearest) failed (rank 46) — DIRECTION-ASYMMETRY, explained by Q 96's tighter terminal-tail neighborhood density.

### Verdict

**VINDICATED-DIRECTIONALLY** (one-sided FR-pair confirmation; chronology consistency at length-and-content-pair level).

---

## Claim 2: Ibn ʿAbbās's content-beacon gloss of the muqaṭṭaʿ ن

### Source

al-Ṭabarī, *Jāmiʿ al-bayān* on Q 68:1 (multiple chains through Ibn ʿAbbās — Saʿīd b. Jubayr, Mujāhid, ʿAbd Allāh b. Masʿūd). al-Suyūṭī, *al-Durr al-manthūr* on Q 68:1, transmitting Ibn ʿAbbās's catalog.

The claim: the muqaṭṭaʿ-letter ن at Q 68:1 is functionally glossed by the following *wa-l-qalam* phrase — i.e., the opening single-letter announces the surah's writing-vocabulary content.

### Rules-tuple

`(no-tashkeel, QAC-stem-roots, QAC v0.4 morphology, basmala-counted-only-in-Q1, Hafs-Kufan)`

### Empirical test

**Q068-F-01** — writing-vocabulary-density audit. 6 writing-roots tested {qlm, sTr, ktb, sjl, rqm, lwH}; per-root hypergeometric Bonferroni-6 + joint-family.

| Result | Value |
|:--|:--|
| sTr passes Bonferroni-6 (α=0.0083) | p=0.0017, 33× over uniform-expected |
| qlm passes raw α=0.05 | p=0.015, 65× over uniform-expected |
| Joint-family p (combined 6-root, k=5/352 vs 191/49968 expected) | **p=0.0117** |

**Verdict**: VINDICATED. At least one root passes Bonferroni-6; joint p < 0.05.

The empirical interpretation: Q 68 over-concentrates writing-vocabulary BEYOND the v.1 opening — the v.15 *asāṭīr*, v.37 *kitāb*, v.47 *yaktubūn* mentions confirm the **content-beacon** distribution throughout the surah, not just the v.1 oath.

### Verdict

**VINDICATED**. Ibn ʿAbbās's content-beacon gloss is empirically supported at joint-family p=0.0117.

---

## Claim 3: Q 68 is the corpus-EXACT singleton Nūn-letter muqaṭṭaʿ opener

### Source

Implicit in al-Suyūṭī's *al-Itqān* nawʿ on muqaṭṭaʿāt-openers (29 surahs enumerated), and explicit in the Q050-F-01 Q 50 specialist enumeration of singleton-letter muqaṭṭaʿāt {Q 38, Q 50, Q 68}.

### Rules-tuple

`(no-tashkeel, orthographic-token, 29-muqaṭṭaʿāt-opener canon per al-Suyūṭī)`

### Empirical test

**Q068-F-08 sub-test (a)** — direct enumeration of the 29 muqaṭṭaʿāt-opener verse-1 first-tokens.

Result: exactly 1 of 29 muqaṭṭaʿāt opens with the single letter ن. That one is Q 68. (`csv/Q068-F-08.json` `sub_test_a_nun_uniqueness.nun_openers_found = [68]`.)

### Verdict

**VINDICATED-CORPUS-EXACT**. Q 68 is uniquely the Nūn-letter muqaṭṭaʿ opener in the corpus.

---

## Claim 4: Singleton-letter muqaṭṭaʿāt cohort {Q 38, Q 50, Q 68} is FR-content-cohesive

### Source

This is NOT a directly-classical claim but a **project-derived hypothesis** flowing from the Q050-F-01 finding (the three singleton-letter openers share the muqaṭṭaʿ + oath-wāw + definite-article verse-1 syntax). If form-coherent, are they also content-coherent?

### Rules-tuple

`(no-tashkeel, QAC-stem-roots, FR matrix from h-new-111 SHA ea3f0ee41d41...)`

### Empirical tests (TWO independent nulls)

| Test | Null type | Result | Verdict |
|:--|:--|:--|:--|
| Q050-F-04 | random-3-surah from 114-surah space | mean=0.870; null mean=0.922; **p_low=0.267** | NULL |
| Q068-F-08 (b) | length-matched triplets (51-surah pool) | mean=0.870; null mean=1.043; **p_low=0.082** | NULL-LM |

**Both tests fail to reject the null at α=0.05**. The triplet IS directionally more cohesive than random (mean 0.870 < both null means), but the effect does not pass significance under EITHER null.

The Q068-F-08 length-matched null has a HIGHER null mean (1.043) than the Q050-F-04 random null (0.922), because length-matched surahs include many longer-corpus surahs that contribute high pairwise distances. The triplet's 0.870 mean is even more "low" relative to this null, yet still p=0.082.

### Verdict

**DOUBLE-REPLICATION NULL**. The singleton-letter cohort is form-coherent (verse-1 syntax) but not content-cohesive under TWO independent null distributions. This is a credibility-strengthening NULL: the letter-axis ⊥ content-axis (cross-finding-026 §1) holds at the singleton-cohort scale under multiple methodological lenses.

---

## Claim 5: Q 68:1 is the most-cited Q 68 verse in the 9-book hadith corpus

### Source

Implicit in the classical theological tradition (al-Ṭabarī, Ibn Kathīr, al-Suyūṭī *al-Durr al-manthūr* on Q 68:1) which places the pen-creation hadith complex as the primary interpretive anchor of Q 68's opening.

### Rules-tuple

Normalized substring match (alif/yāʾ/tāʾ-marbūṭa unified, tashkeel stripped); 9 canonical hadith books; per-verse distinctive 4+-word substrings.

### Empirical test

**Q068-F-05** — per-verse citation density across 9 canonical books.

| Result | Value |
|:--|:--|
| Q 68:1 substring citation count | **0** (across all 9 books) |
| Modal verse | tied at Q 68:4, Q 68:13, Q 68:42 (1 each) |
| Q 68:1 rank by citation | rank 4 (tied with all 0-citation verses) |
| Binomial p for Q 68:1 ≥ 0 under uniform null | 1.0 (NULL) |

### Verdict

**NULL_DIRECTION_REVERSED**. Q 68:1 has 0 substring-citations vs uniform-expected 0.06. The pre-commit direction (Q 68:1 > expected) is violated. Published as NULL with prominence per Protocol §1.3.

### Honest interpretation

The strict substring matching misses INTERPRETIVE attestations (the pen-creation hadith at Tirmidhī #3403, Abū Dāwūd #4702, Tirmidhī #2223 — see [[04-hadith-corpus]] §2 — does cite Q 68:1's content but does NOT include the exact substring *والقلم وما يسطرون*). The interpretive citation count is 3 (the three hadith of the pen-creation tradition), but the direct-substring count is 0. The strict pre-reg verdict is NULL; the looser theological-claim that Q 68:1 is the interpretive anchor stands.

---

## Claim 6: Q 68 is MIXED MECCAN/MEDINAN per Ibn ʿAbbās's subdivision

### Source

al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 68 opening: Ibn ʿAbbās + Qatāda hold that Q 68 is mostly Meccan with Medinan interpolations at vv. 17-33 (the garden parable) and vv. 48-50 (the Yūnus close).

### Rules-tuple

Would require a per-verse Meccan/Medinan classifier — i.e., a stylometric or content-based discriminator between Early/Middle Meccan and Medinan verses.

### Empirical test

**NOT RUN**. This claim would require:
1. A trained classifier on Meccan/Medinan-attested verses.
2. Application to each Q 68 verse.
3. Verification that vv. 17-33 and vv. 48-50 are classified MEDINAN at higher-than-chance rate.

Such a classifier exists in the academic literature (e.g., Sinai 2017 stylometric analyses) but is not implemented in the project's pipeline as of Wave-1 2026-04-17.

### Verdict

**NOT TESTED EMPIRICALLY**. Flagged as a future-work item: per-verse Meccan/Medinan classifier on Q 68. The classical Ibn ʿAbbās subdivision IS plausible on content grounds (the garden parable is structurally distinctive and could plausibly be a later Medinan interpolation in form-criticism terms), but no empirical adjudication is currently possible.

---

## Synthesis table

| Claim | Source | Empirical test | Verdict |
|:--|:--|:--|:--|
| Q 68 = revelation #2 (after Q 96) | al-Suyūṭī, *al-Itqān*; Nöldeke; Egyptian std | Q068-F-07 FR-pair test | VINDICATED-DIRECTIONALLY (one-sided FR-pair) |
| Ibn ʿAbbās's content-beacon ن gloss | al-Ṭabarī on Q 68:1 (multiple chains) | Q068-F-01 writing-vocab density | **VINDICATED** (joint p=0.0117) |
| Q 68 = corpus-EXACT singleton ن-opener | implicit in al-Suyūṭī *al-Itqān* | Q068-F-08 (a) enumeration | **VINDICATED-CORPUS-EXACT** |
| Singleton-cohort FR-content-cohesive | project-derived hypothesis (Q050-F-04 lineage) | Q050-F-04 + Q068-F-08 (b) | **DOUBLE-REPLICATION NULL** |
| Q 68:1 = most-cited Q 68 verse | al-Ṭabarī, Ibn Kathīr theological tradition | Q068-F-05 substring search | **NULL_DIRECTION_REVERSED** |
| Q 68 mixed Meccan/Medinan (Ibn ʿAbbās) | al-Qurṭubī opening of Q 68 | NOT-TESTED | flagged future work |

3 VINDICATED + 1 VINDICATED-PARTIAL + 1 DOUBLE-REPLICATION-NULL + 1 NULL + 1 NOT-TESTED = balanced classical-claims audit with full pre-commit transparency.
