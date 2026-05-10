---
id: Q040-F-04
title: Believer-of-Pharaoh's-family pericope corpus-singleton test
date_locked: 2026-05-09
phase: B
status: pre-registered
---

# Q040-F-04 — Believer-of-Pharaoh's-family pericope (Q 40:28-44) corpus-singleton test

## Hypothesis (DIRECTION-LOCKED)

**H1**: Q 40:28 is the **corpus-singleton** verse containing the phrase combining *مؤمن* (muʾmin, "a believer") with *آل فرعون* (āl Firʿawn, "Pharaoh's family") — i.e. the "believing relative of a tyrant" narrative pattern appears in EXACTLY ONE verse in the Quran (no-tashkeel corpus).

Direction: #{verses containing both مؤمن AND آل فرعون} = 1.

## Theoretical motivation

al-Ṭabarī (*Jāmiʿ al-bayān* ad Q 40:28), al-Qurṭubī (*al-Jāmiʿ* ad loc.), and Ibn Kathīr (tafsīr Sūrat Ghāfir, opening of section 4) all identify the unnamed *rajul muʾmin min āl Firʿawn* as a distinctive Qurʾānic pattern: a covert believer inside a tyrant-clan delivers a 17-verse rhetorical monologue (Q 40:28-44). The narrative type — believing relative of a Quranic tyrant — has no other corpus exemplar (no analog inside Hāmān's, Nimrūd's, or Abū Lahab's circles). This test verifies the corpus-singleton claim at the phrase level.

## Pre-committed protocol

- Source: `quran-text/quran-no-tashkeel.json`.
- Test: for each verse v in corpus, check if v contains substring "مؤمن" AND substring "آل فرعون" (literal phrase, no-tashkeel).
- Count hits; report list of (surah, verse).
- Pre-committed expected: 1 hit, equal to Q 40:28.

## Verdicts

| Outcome | Verdict |
|:--|:--|
| #hits == 1 AND hit == Q 40:28 | CORPUS-SINGLETON VINDICATED |
| #hits ≥ 2 | NULL — pattern is not unique |
| #hits == 0 | DEFINITIONAL ANOMALY — phrase encoded differently than expected |

## Honest limits

1. Phrase-level not narrative-level: the test searches *مؤمن + آل فرعون* in the same verse. A weaker "believing relative" pattern in different lexical clothing across the corpus would not be detected. This test answers the precise phrase-singleton question.
2. Q 28:9 contains Pharaoh's wife (Āsiya bint Muzāḥim) saving Mūsā — also a "believer inside Pharaoh's family" narrative — but uses different phrasing (*imraʾat Firʿawn*, not *muʾmin min āl Firʿawn*). The current test will NOT count Q 28:9 by design; its narrative-level kinship to Q 40:28 is acknowledged in honest-limits.
3. Q 66:11 cites Pharaoh's wife as an exemplar of faith; similarly excluded by phrasing.

*Locked 2026-05-09.*
