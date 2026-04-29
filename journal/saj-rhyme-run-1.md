# Journal — saj-rhyme novelty agent — run 1

**Date:** 2026-04-12
**Agent:** saj-rhyme (Phase B novelty)
**Goal:** computational analysis of Quranic rhymed prose (saj') / fasila structure

## Plan

The user requested 11 numbered tasks under the saj' angle:
1. Extract verse-end fasilas, build frequency histogram, find longest run.
2. Per-surah rhyme-uniformity score, top-20 / bot-20.
3. Rhyme-breakers in top-20 uniform surahs.
4. Ar-Rahman refrain count and structure.
5. Rhyme-based ring score; compare to Phase-C root-based ring.
6. Final-letter histogram vs general letter frequency.
7. Meccan vs Medinan rhyme density.
8. Cross-surah rare-fasila linkage.
9. Verse length vs rhyme adherence.
10. Surprises.
11. Prior-art search.

## Decisions

### Orthography
Used `quran-text/quran-full-tashkeel.json` because saj' rhyme is a phonetic phenomenon and full-tashkeel preserves the diacritics that make pause form recoverable. (no-tashkeel collapses cases that pause-form distinguishes.)

### Letter normalisation
- Stripped all diacritics, recitation marks, tatweel, superscript alif, subscript alif, inverted damma. (Ranges: 064B–065F, 0670, 06D6–06ED, 0610–061A, 0640, 0656–0657)
- Dropped bare hamza (U+0621) from the consonant skeleton because the corpus and the user-supplied refrain string differ on whether the hamza in *ʾālāʾi* is written before or absorbed into the alif. With the bare hamza dropped, all 31 Ar-Rahman refrains match.
- Collapsed: أ إ آ ٱ ٲ ٳ → ا (alif variants)
- ؤ → و (waw with hamza)
- ئ → ي (yeh with hamza)
- **ى → ا** (alif maksura → alif). This is the most consequential normalisation choice. Rationale: in pause form, alif maksura sounds /aː/ exactly like terminal alif, and the rhymes in surahs like Al-Aʿlā (every verse ends in alif maksura) need to be unified with surahs whose verses end in plain alif. Disclosed in the forking-paths section.
- ة → ه (teh marbuta → heh, standard pause-form rule)

### Fasila definition
Three keys per verse:
- `fasila_1` = last 1 consonant of normalised skeleton of last word
- `fasila_2` = last 2 consonants
- `fasila_3` = last 3 consonants

`fasila_1` ≈ classical *rawi* (last consonant); `fasila_2` ≈ rawi + the consonant before it; `fasila_3` ≈ a tighter consonant cluster.

## What worked first try

- 6236-verse load was clean.
- 31 Ar-Rahman refrains popped out instantly once I switched to using the corpus's own verse 55:13 as the gold skeleton (after fixing the bare-hamza issue).
- The longest-run search found Surah Maryam vv 41–74 with 34 consecutive `يا` rhymes, which matches qualitative literary observations.
- Final-letter histogram was extremely clean: ن at 50.1% of all endings, with the predicted top-3 (ن, ا, م) covering 80%.

## What surprised me

1. **`U2` ranking misclassifies the famous monorhyme surahs.** Al-Aʿlā has every verse ending in alif but the *consonant before the alif* changes constantly, so its `fasila_2` is `لا` only 3/19 times = 0.16. I had to add a second uniformity score (`U1`) at the final-letter level to recover the obvious classical rhyme. **This is itself a finding** — saj' rhyme operates at two distinct grain sizes in the Quran, and most discussions implicitly use one or the other.

2. **Meccan vs Medinan saj'-density claim is null.** I expected this to be the easiest "famous claim, easily replicable" win. Instead, *every* metric of rhyme density (avg run length on `fasila_1` and `fasila_2`, uniformity `U1` and `U2`) returned p > 0.3. The only Meccan/Medinan difference that's significant (p = 0.0001) is verse *length*, not rhyme density. The folk wisdom is operating through a length effect, not through rhyme tightness. I'm reporting this as a strong null finding.

3. **Al-Kahf is 110 consecutive alif-rhymed verses.** I had not realised how exceptional this is until I sorted by `U1`. By comparison, Maryam's famous `يا` rhyme is "only" 67%; Al-Furqan is 99% (one breaker); Al-Kahf is the unique 100%-at-N=110 case.

4. **Rhyme-ring vs root-ring correlation is essentially zero.** Pearson r = −0.018 across 111 surahs. The two structural-composition signals are independent. I expected at least a mild positive correlation, on the assumption that both should reflect the same underlying composition. They don't.

5. **Maryam vv 34–40 break the `يا` rhyme exactly during the doctrinal Jesus statement.** This is striking and presumably noticed by classical commentators, but I haven't seen it quantified. The next 34 verses (vv 41–74) re-establish the `يا` rhyme without a single break — the longest mono-rhymed run in the entire corpus.

## Bugs / things I had to fix

1. **Refrain detection failed initially** because my hardcoded refrain string used آ (alif with maddah, U+0622) where the corpus uses ءَالَآ (bare hamza + alif + maddah). After dropping the bare hamza from the skeleton normalisation, all 31 instances match.

2. **Initial Meccan/Medinan test only used `fasila_2` run length and missed the more permissive `fasila_1` run length.** Adding both didn't change the verdict — both are non-significant — but the broader test family is more honest.

3. **The first uniformity ranking was misleading** because it only used `fasila_2` and so put Al-Aʿlā in the bottom-20 (`U2` = 0.16) despite it being a famous monorhyme. Switched to also reporting `U1`. Disclosed as a forking-paths choice.

## Things I did NOT do that should be done

1. **Pre-registration.** This is an exploratory novelty run; nothing is pre-registered. All p-values are exploratory and should be demoted accordingly. The strongest single observation (Al-Kahf 110/110 alif under base rate 0.191) is not p-hacked because it's a single descriptive observation, but a pre-registered test of "long surahs are mono-rhymed more often than chance" would be a real Phase-B finding.

2. **Comparable-corpus null** (rigor protocol §1.4). I did not test the Quran's rhyme-density against a real classical Arabic comparable corpus (e.g. early hadith). The saj' baseline in Arabic prose is non-zero and we'd want to compare. This is the natural next step.

3. **Topic-classification of rhyme-breakers.** The Maryam Jesus-statement observation is anecdotal until rhyme-breakers across all top-20 surahs are systematically classified by topic and tested. I have a candidate (translation keyword search) but did not implement.

4. **Cross-surah linkage formal test.** The Kahf↔Jinn observation is striking but unranked against random surah pairs. A proper test would be: across all 6,441 surah pairs, how many share ≥3 rare fasila_3 patterns? Distribution under what null?

5. **The `fasila_1` permutation didn't get a 10⁴ trial run for the ring-score.** Used 500 trials per surah; that's enough for the null to converge but not for tight p-values. This wasn't load-bearing for any conclusion (no surah cleared Holm anyway) but flagged for completeness.

## Ar-Rahman refrain — exact count

**31 occurrences.** Verses: 13, 16, 18, 21, 23, 25, 28, 30, 32, 34, 36, 38, 40, 42, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77.

Pattern: pre-refrain prelude vv 1–12; first refrain at v13; widely-spaced refrains in vv 13–28; bi-versed couplet structure from v 30 onward; pure 15-couplet block in vv 47–77; doxological coda v 78. Already checked against the classical count of "31 refrains" and matches.

## Files written

- `findings/phase-b-hypotheses/saj-rhyme-analysis.md` — full finding writeup
- `findings/phase-b-hypotheses/saj-fasila-per-verse.csv` — per-verse fasila CSV (6236 rows)
- `analysis/notebooks/saj_rhyme.py` — reproducible script
- `analysis/notebooks/saj_rhyme_results.json` — full machine-readable results
- `journal/saj-rhyme-run-1.md` — this file
