---
preregistration_id: Q112-F-04
title: Q 112 al-Ikhlāṣ aḥad-bookend chiasm structure
date: 2026-04-28
phase: B+
seed: 20260428
status: PRE-REGISTERED-LOCKED
---

# Q112-F-04 — Pre-registration: Q 112 *aḥad*-bookend chiasm

## Hypothesis (H1)

Q 112 has a 4-verse symmetric structure with v.1 and v.4 ending in the same word (*aḥad*), forming an A-...-A' bookend.

The structural lock requires:
1. v.1 ends with token *aḥad*.
2. v.4 ends with token *aḥad*.
3. v.2 and v.3 have distinct endings (not *aḥad*) but rhyme with v.1/v.4 on the -ad pattern.
4. The bookend is rules-tuple-stable across all 3 tashkeel variants.

## Method

1. Read v.1 and v.4 final tokens from quran-no-tashkeel.json, quran-min-tashkeel.json, quran-full-tashkeel.json.
2. Verify identity of v.1 final word == v.4 final word == *aḥad*.
3. Verify v.2 and v.3 ending letters are also د (dāl) — confirming rhyme without word-identity.

## Direction

LOCKED: PASS if v.1==v.4==*aḥad* and v.2==*ṣamad* and v.3==*yūlad* across all three tashkeel variants.

## Pre-commit honesty

Any rules-tuple instability (different tokens in different variants) is published as RULES-TUPLE-FRAGILE.
