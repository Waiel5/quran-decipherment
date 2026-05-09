---
test_id: Q022-F-06
title: "Q 22 al-Ḥajj is the corpus-singleton on double-sajda (≥2 sajda markers)"
date_locked: 2026-05-09
seed: 20260509
n_perm: 0
bonferroni_k: 1
bonferroni_family: Q022-F-06-double-sajda-singleton
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q022-al-hajj-specialist
---

# Q022-F-06 Pre-registration — Q 22 corpus-singleton double-sajda

## Hypothesis

Classical Sunnī tradition holds that Q 22 al-Ḥajj contains TWO sajdas (22:18 and 22:77) — a unique status in the Quran. al-Tirmidhī *Sunan* #578 records ʿUqba b. ʿĀmir's question to the Prophet: "Has Surah al-Ḥajj been esteemed by two prostrations?" — answered affirmatively. Abū Dāwūd *Sunan* #1402 records ʿAmr b. al-ʿĀṣ stating the Prophet taught him 15 sajdas including TWO in Surah al-Ḥajj. al-Suyūṭī (*al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 30 on sujūd al-tilāwa) catalogs the dispute, with Mālikī school dissenting on 22:77.

The empirical claim under the Hafs-Kufan Mashriqi printed mushaf is testable: count the sajda-glyph (۩, U+06E9) per surah; verify exactly one surah has ≥2 markers.

## Pre-committed prediction

**Direction-locked**: Counting the ۩ glyph in `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` across all 6,236 verses, exactly ONE surah (Q 22) carries ≥2 sajda markers. All other 13 sajda-bearing surahs carry exactly 1.

## Test (Bonferroni-1, α=0.05)

Deterministic verification — no permutation required:

1. **T1a — corpus enumeration**: Scan all verses; record (s, v) pairs containing ۩.
2. **T1b — per-surah count**: Aggregate by surah.
3. **T1c — singleton verification**: |{s : count(s) ≥ 2}| = 1 AND that singleton surah is Q 22.

## Direction-of-effect lock

Predicted: T1c TRUE.
If T1c FALSE (zero or ≥2 surahs with double-sajda), publish as NULL pre-commit violation.

## Success criteria

- VINDICATED: T1c TRUE (Q 22 is the unique double-sajda surah) AND the two markers are at verses 18 and 77.
- DIRECTIONAL: T1c TRUE on count but verse-positions disagree with classical (18, 77).
- NULL: T1c FALSE.

## Rules-tuple sensitivity notes

- Maliki tradition (al-Mālik, al-Tirmidhī #578 ad fin) holds only ONE sajda in Q 22, at 22:77 (some say 22:18). Under the Mashriqi printed mushaf (the data file used), BOTH ۩ are present. The empirical test is operating under the Mashriqi-Hafs-Kufan rules-tuple, which IS the Sunnī majority position.
- Imāmī (Shīʿī) lists only 4 wājib sajdas {Q 32, 41, 53, 96} — Q 22 is mustaḥabb (recommended) not wājib but the GLYPH is still present in the printed mushaf.

## Garden-of-forking-paths log

- BEFORE running: chose ۩ glyph (U+06E9) over al-Suyūṭī's textual enumeration because the printed mushaf is the canonical operationalization for "the Quran's text contains a sajda here."
- BEFORE running: counting via no-tashkeel variant because the glyph is preserved across all four variants (verified in scaffolding).
- BEFORE running: classical-Sunnī count = 14 surahs, 15 verses. Test is unique-double-sajda-surah, not total count.

## Honest limits

- The test is essentially a corpus-count confirmation of a classical-tradition-encoded printing convention. It is empirically falsifiable: a different printing convention could lack 22:77's marker. The data file used carries the Sunnī standard.
- The Maliki rule-variant remains DIRECTIONAL — under Maliki, 22:18 only (or 22:77 only depending on report); under that variant Q 22 would NOT be the corpus-singleton.
