# Chronological Revelation Order — Run 1 Journal

**Agent:** chrono-revelation (Phase B novelty)
**Date:** 2026-04-12
**Status:** complete (exploratory; not pre-registered)

## What I did

1. **Acquired the Egyptian Standard ("tartīb al-nuzūl") revelation order** from
   `https://tanzil.net/docs/revelation_order` (a well-known Quranic-text utility
   curated against the Egyptian/King Fu'ad edition). All 114 surahs, position 1
   = surah 96 (Al-'Alaq) ✓; position 113 = surah 9 (At-Tawba); position 114 =
   surah 110 (An-Naṣr). Both of these match the traditional claim that
   At-Tawba and An-Naṣr are among the very last revelations.
2. **Acquired Nöldeke's chronological order** (positions 1-114) and the 4
   periods (Early Meccan: 1-48; Middle Meccan: 49-69; Late Meccan: 70-90;
   Medinan: 91-114) from the Wikipedia "List of chapters in the Quran" table
   and the German `Geschichte des Qorāns` Wikipedia summary. Surah 96 sits at
   Nöldeke position 1 also (good agreement on the start).
3. **Saved both orderings** to `/Users/grey/Downloads/quran/data/revelation-order.csv`
   in a single CSV with the Egyptian order as the canonical default and the
   Nöldeke order + phase as additional columns.
4. **Computed seven per-surah metrics** from `quran-no-tashkeel.json` plus the
   QAC morphology file: average verse length in words, average verse length
   in letters, letter-level Shannon entropy, number of distinct roots, lemma
   type-token ratio, surface-token TTR, mashriqi abjad total, and fasila
   (rhyme-ending) uniformity (proportion of verses sharing the most common
   final 2-letter rhyme).
5. **Compared mushaf vs revelation order** on (a) lag-1 autocorrelation,
   (b) consecutive-pair Jaccard root overlap, and (c) length-detrended
   autocorrelation.
6. **Tested Meccan/Medinan separation** with a 10 000-permutation test on
   each metric and reported Cohen's d.
7. **Computed the Nöldeke 4-phase one-way F** for verse length.
8. **Hunted temporal drift** in 203 frequent roots (≥ 50 occurrences) via
   Spearman ρ vs revelation position.
9. **First-appearance map** for 18 theological terms by root + traced the
   proper-name "Muhammad" (lemma `muHam~ad`) directly through the morphology.
10. **Heaps'-law new-roots curve** in revelation order, with bumps identified.

## Surprises

- **Mushaf order has higher lag-1 autocorrelation than revelation order on
  every length-related metric**, even after log-length detrending. Initially
  this looked like a refutation of the traditional revelation order, but the
  honest interpretation is: the mushaf is sorted (almost) by length, so
  length-correlated metrics are *artificially* smooth in mushaf order. The
  autocorrelation test as posed in task 5 is therefore *not* a fair test of
  which order is "true." I report it anyway, with the caveat.

- **The Nöldeke 4-phase grouping is the cleanest signal in the entire run.**
  One-way F for `avg_v_letters` across the 4 Nöldeke phases = **209.96**
  (k=4 groups, n=114 surahs). The four phase means form a perfect monotone
  ramp: 18.5 → 38.7 → 66.0 → 79.9 letters/verse. This is the strongest
  diachronic signal I found and it shows up only when we use the
  scholarly-traditional ordering — mushaf order does not have this property.

- **The Hijra change-point is real.** The largest change in `avg_v_words`
  along the smoothed revelation-order curve sits at position 88, which is the
  *very next surah after* the Meccan/Medinan boundary at 87. For
  `n_distinct_roots`, the largest change is at position 84 (3 surahs before
  the boundary, but the late Meccan surahs are already long). This is
  consistent with the traditional historical claim that the Hijra produced a
  rhetorical-style discontinuity.

- **The proper name "Muhammad" enters the corpus only at revelation position
  89** (Surah 3, Āl ʿImrān), and all four occurrences (3:144, 33:40, 47:2,
  48:29) are after the Hijra. The name is never used in any of the 86
  pre-Hijra surahs. This is a clean, falsifiable temporal pattern.

- **No frequent root (≥ 50 occurrences) is exclusively Meccan or
  exclusively Medinan.** Even the most strongly Medinan-shifted root in the
  list (`nsw`, "women") has Spearman ρ = +0.917 against revelation position
  but is not actually absent from Meccan surahs.

- **Top "ramp-up" roots are exactly what a historian would predict:**
  `nsw` (women), `nfq` (hypocrisy), `fsq` (rebellion), `Hll` (lawful),
  `Erf` (recognize/manners), `Swb` (recompense), `bAs` (tribulation), `Tyb`
  (good/lawful). All cluster around legal, social, and community-conflict
  themes that fit the Medinan period.

## Caveats and forking-paths disclosure

- **Not pre-registered.** This is a Phase B exploratory novelty run; nothing
  here is a "finding" until pre-reg + null-model audit.
- **Two orderings exist** (Egyptian and Nöldeke). I chose the Egyptian as
  default because the task requested it; results would shift slightly under
  Nöldeke (Surah 33 Al-Aḥzāb is Medinan in Egyptian = position 90 but Nöldeke
  103, etc.). I report both.
- **Permutation test for Meccan/Medinan separation does not adjust for the
  fact that 24 of 114 labels are Medinan**, which inflates power for length
  metrics where the Medinan group is also longer on average. The Cohen's-d
  numbers should be read alongside the p-values.
- **The autocorrelation comparison is biased toward mushaf order** by design,
  because the mushaf is length-sorted and most metrics correlate with length.
  The fair version of the test is the Nöldeke 4-phase F, not lag-1 on the
  full sequence.
- **First-appearance positions** depend on which root tag the QAC assigns;
  proper names like "Muḥammad" do not have a `ROOT:` field in the QAC, so I
  had to trace them by lemma instead. The Hjb (hijab) "first appearance" is
  the lexical first appearance, not the *theological* first appearance — the
  veiling sense in 33:53 is at revelation position 90, while the literal
  "barrier" sense first appears at 38:32 (revelation position 38).
- **fasila_uniformity** is a crude proxy for rhyme — last 2 letters of the
  last word of each verse — and is not the right measure of rhyme structure
  in classical Arabic prosody. Reported for completeness but the signal is
  basically noise (Cohen-d = +0.09, perm-p = 0.67).
- **letter_entropy is essentially flat** across the corpus (Cohen-d = +0.13,
  perm-p = 0.55). The Quran's letter distribution is stable across periods.

## Files written

- `/Users/grey/Downloads/quran/data/revelation-order.csv` — both orderings
- `/Users/grey/Downloads/quran/scratch/chrono/per-surah-revelation-order.csv`
- `/Users/grey/Downloads/quran/scratch/chrono/autocorrelation-table.csv`
- `/Users/grey/Downloads/quran/scratch/chrono/meccan-vs-medinan.csv`
- `/Users/grey/Downloads/quran/scratch/chrono/jaccard-overlap.csv`
- `/Users/grey/Downloads/quran/scratch/chrono/new-roots-curve-revelation.csv`
- `/Users/grey/Downloads/quran/scratch/chrono/root-temporal-trends.csv`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/chronological-revelation.md`

## Sources cited

- Tanzil. "Revelation Order" documentation. https://tanzil.net/docs/revelation_order
- Wikipedia. "List of chapters in the Quran." (Egyptian + Nöldeke columns)
- Wikipedia. "Geschichte des Qorāns" (Nöldeke 4-phase counts: 48/21/21/24)
- Theodor Nöldeke et al., *Geschichte des Qorāns*, 2nd ed. 1909-1938;
  English translation Behn 2013, *The History of the Qurʾān*.

## Time spent

About 90 minutes of agent time including web searches, table extraction,
script writing, two iterations of the analysis, and the write-up.
