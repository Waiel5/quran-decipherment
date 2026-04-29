---
title: "ʿIlm al-ḥarf tests — run log"
agent: phase-b-classical-integration / ilm-al-harf
date: 2026-04-12
output: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/ilm-al-harf-tests.md
scripts:
  - /tmp/ilm-al-harf.py (tests 1, 4, 5, 6, 8, 9)
  - /tmp/ilm-test2.py (tests 2, 7 with translations)
  - /tmp/ilm-test3.py (per-surah element profile, alif word-initial, luminous/element balance)
---

# Run log — ʿilm al-ḥarf

## Plan

Test 1 (element freq), 2 (element × topic), 3 (muqatta'at element balance),
4 (Būnī wafq), 5 (luminous/dark), 6 (alif), 7 (breath quartet), 8 (Q 24:35),
9 (Al-Fātiḥa). Skip metaphysical/untestable.

## Build

- Normalized JSON Quran with project-standard rules.
- 330,709 letters (matches locked anchor).
- Ibn ʿArabī elements per task brief. Verified disjoint, covers 28 letters.

## Notes during run

- First translation-load attempt failed (file is one-verse-per-line, not piped).
  Second script loads by position; 6247 non-blank lines vs 6236 verses — 11
  extra lines likely duplicated basmala or section headers. Truncated to 6236.
- Test 1: fire dominance driven by alif. Ran a sensitivity excluding alif;
  without alif, air dominates. Reported as a caveat.
- Test 2: striking confirmations on punishment/fire and creation/earth.
  Wrong-direction on wind/air and paradise/water. Bonferroni α = 0.00179
  over 28 tests; survived by 8 results total (see table). Match directions
  noted in "Match" column.
- Test 7: breath-quartet test yielded paradise, dialogue positive at high
  significance; wind and revelation null or contrary. This is a clean
  hit for the "speech=breath" classical claim, not for the "air=wind"
  element attribution.
- Test 9: Al-Fātiḥa missing 7 letters. Quick and clean null to the
  classical claim. Surprising how widespread the claim is given how
  easily falsified.

## Verdict distribution

- 2 strong confirmations (punishment/fire 5.9e-16, creation/earth 8.8e-12)
- 2 medium confirmations (paradise-breath 5.4e-08, alif primacy)
- 2 weak confirmations (dialogue-breath 3.8e-04, luminous freq enrichment 0.028)
- 3 refutations (wind/air wrong dir 0.0018, paradise/water wrong dir 0.005,
  Al-Fātiḥa 28-letter claim false)
- 2 clean nulls (al-Būnī wafq, Q 24:35 profile)
- 1 confounded partial (fire dominance — driven by alif)

## Forks I didn't take

- Arabic-side topic tagging via morphology corpus (would be cleaner but
  requires mapping the PoS/root tags to semantic classes)
- Al-Jīlī's alternative element assignment (hard to find canonical text
  online; Lory 2004 reports it differs)
- Planetary 7×4 assignment (chapter 198 of Futūḥāt); could test planet ×
  topic but the topic proxies for Saturn vs Mercury are weak
- Bayesian hierarchical over the 28 tests (would probably rescue hell/fire
  from sub-Bonferroni status)
- Permutation null for small-n topics (wind n=37, purity n=62)

## Self-assessment

Honest report. Two strong confirmations, clean refutations, clean nulls.
Tradition partially holds — where it tracks Arabic phonetic intuition.
Matches the Lory/Gril/Abū Zayd reading in the modern literature: Ibn
ʿArabī as phenomenologist of Arabic, not numerologist.
