---
finding_id: Q023-F-02
title: Q 23:1-11 believer-attributes checklist — corpus-longest contiguous enumeration
date: 2026-05-09
seed: 20260509
status: PRE-REGISTERED
rules_tuple: (no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan)
---

# Q023-F-02 — *muʾminūn-attributes* checklist: corpus-exact longest contiguous block?

## 1. Background

Q 23:1-11 opens with *qad aflaḥa al-muʾminūn* and lists believer-traits across 10-11 verses. Classical mufassirūn (al-Ṭabarī, al-Qurṭubī, al-Biqāʿī) treat this as a **typology-block** with 6 distinct traits (khushūʿ-prayer, iʿrāḍ-laghw, zakāh, ḥifẓ-furūj, riʿāyat-amāna, ḥifẓ-ṣalawāt).

The handoff prompt asks: is this **the corpus-EXACT longest contiguous *believer-attributes* enumeration**, compared to Q 8:2-4, Q 9:71, Q 70:22-35?

## 2. Hypothesis

**Definition of "believer-attributes contiguous enumeration"**: a maximal run of consecutive verses (within one surah) that satisfies all four:

1. **Subject continuity**: subject of the enumeration is "the believers" (al-muʾminūn / al-muttaqūn / alladhīna āmanū / synonymous referent).
2. **Trait-syntax**: each verse adds a relative-pronoun clause (*alladhīna hum...*, *al-...*) or a coordinated descriptive clause describing the believers.
3. **No narrative break**: no narrative-action verses interrupt; no addressee shift.
4. **Trait counter** (rules-tuple-stable count): count distinct trait-clauses (joined relative-pronouns count as separate clauses) within the block.

**Pre-registered DIRECTION**: Q 23:1-11 (or 1-10) is the **LONGEST such contiguous block** in the corpus, measured by:
- (primary) verse-count
- (secondary) trait-clause count

vs the canonical comparators:
- Q 8:2-4 (3 verses)
- Q 9:71 (1 verse, paired-believer description with men-and-women)
- Q 70:22-35 (14 verses but interleaved with eschatological narrative)
- Q 32:15-16 (sajda-block, ~2 verses)
- Q 25:63-77 (al-ʿibād al-Raḥmān block, ~15 verses but narrative-interleaved)

**Failure direction**: if a longer-or-equal contiguous block (by both verse-count AND trait-count) exists, publish as NULL with prominence.

## 3. Test procedure

Two-part test:

### 3.1 Pre-screened comparators

For each of the comparators above, manually verify (using the canonical no-tashkeel text):
- Verse-count of the contiguous block.
- Trait-clause count (rules-tuple: distinct *alladhīna...* / *al-...* / *wa-...* relative-pronoun or descriptive-coordination clauses).
- Whether the block has narrative-break (yes/no).

Compute (verse-count, trait-clause-count, has-narrative-break) for each comparator + Q 23:1-11.

### 3.2 Corpus-wide scan

Programmatic identification: for each surah, find the longest contiguous run of verses where:
- Every verse contains either *alladhīna hum* (lit. "those who ...") **or** *al-...ūn* / *al-...īn* form-IV-active-participle (plural masculine, defining a category) **or** a *wa-alladhīna hum* coordinator.
- The run is not interrupted by a verse without such a marker.

Report top-5 by verse-count and top-5 by clause-count.

## 4. Decision rules

- **PASS-DIRECTED-EXACT (CONFIRMED-CORPUS-EXACT)**: Q 23:1-11 (10-11 verses) has the strictly-largest verse-count AND clause-count AND no-narrative-break among contiguous *believer-attributes* blocks.
- **PASS-DIRECTED-PARTIAL**: Q 23 is largest by verse-count OR by clause-count but not both.
- **NULL**: another surah has a strictly-larger block.

## 5. MW protections

- **MW-1 (instrument)**: marker-set locked above; no post-hoc additions.
- **MW-3 (alt models)**: report under two stricter and two looser marker-definitions (e.g., relative-pronoun only; relative-pronoun OR coordinated participle).
- **MW-6 (instrument-control)**: scan the same corpus for **disbeliever-attributes** blocks (alladhīna kafarū) and report the longest — to check the "longest believer block" claim doesn't fall to a generic relative-pronoun-density artifact.

## 6. Pre-reg lock

This file is locked at SHA256-of-contents. Embedded in the runner script. Verified at runtime.
