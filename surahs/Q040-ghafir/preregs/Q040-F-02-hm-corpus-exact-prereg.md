---
id: Q040-F-02
title: HM-opener corpus-EXACT 7-surah identity
date_locked: 2026-05-09
phase: B
status: pre-registered
---

# Q040-F-02 — HM corpus-EXACT identity

## Hypothesis (DIRECTION-LOCKED)

**H1**: The set of surahs whose first verse equals the muqaṭṭaʿāt token *حم* (HM, no-tashkeel) is EXACTLY {Q 40, 41, 42, 43, 44, 45, 46} — the 7 consecutive ḥawāmīm.

Direction: |HM_set| = 7 AND HM_set = {40..46} exactly.

## Why this matters

The H-NEW-1395 cluster hypothesis is predicated on the ḥawāmīm being a corpus-EXACT 7-surah HM-opener set. If the orthographic test reveals a different membership (e.g., Q 42 actually begins حم·عسق, treated separately by some traditions), the cluster definition shifts. This is a definitional sanity test that must hold before the cohesion claim is meaningful.

## Pre-committed protocol

- Source: `quran-text/quran-no-tashkeel.json`.
- Test: for s in 1..114, take `verses[0]['text'].strip()`; flag s if first verse exactly equals `"حم"`.
- Pre-committed expected set: {40, 41, 42, 43, 44, 45, 46}.

## Verdicts

| Outcome | Verdict |
|:--|:--|
| HM_set = {40..46} exactly, all 7 first-verses == "حم" | VINDICATED (corpus-EXACT) |
| HM_set ⊂ {40..46} (some missing, e.g. Q 42 has حم·عسق as one verse) | RULES-TUPLE-FRAGILE; tradition-specific |
| HM_set ⊃ {40..46} or different | DEFINITIONAL ANOMALY; H-NEW-1395 cluster must be re-spec'd |

## Honest limits

1. Hafs-Kufan verse division puts حم alone as v.1 of Q 42 and عسق as v.2. Other reading traditions (e.g., some Madanī counts) combine them. The test is Hafs-Kufan-specific (rules-tuple §1.4).
2. This is a definitional, not a statistical, finding. No null distribution needed.

*Locked 2026-05-09.*
