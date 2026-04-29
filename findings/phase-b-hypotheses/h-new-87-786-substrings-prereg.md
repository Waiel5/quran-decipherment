# H-NEW-87 — Pre-registration: Other 786-abjad Multi-word Substrings

**Status:** PRE-REGISTERED (locked before execution).
**Date:** 2026-04-15.
**Specialist:** `h-new-87-specialist`.
**Family/Wave:** `2026-04-15-Wave-Bismillah-Numerology` (companion to [[h-new-50-bismillah-114|H-NEW-50]]).
**Anchor:** the Bismillah `بسم الله الرحمن الرحيم` has mashriqī abjad sum **786**, verified via `analysis/tools/gematria.text_value`. This is the canonical claim used in `findings/phase-b-hypotheses/classical-quantitative-claims-audit.md` (CC-anchor for the 786-claim).

## Question

Is **786** a *unique* abjad signature of the Bismillah inside the Quran's running text, or does the Quran contain other contiguous multi-word phrases whose mashriqī abjad sum is also 786?

## Hypothesis

**H0 (null, default expectation):** 786 is one value out of many possible 4-word phrase totals; under a chance model it should be hit roughly as often as nearby high-density values. The Bismillah is *not* singled out by 786-uniqueness.

**H1 (rare-signature):** 786 is sharply rarer than its neighbours; the Bismillah is essentially the unique 786-substring in the Quran (allowing for incidental matches in non-Bismillah position).

## Procedure (locked)

1. **Corpus:** `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`, loaded via `analysis/tools/loader.load_quran('no-tashkeel')`. Verses concatenated in canonical mushaf order. Token = whitespace-split word.
2. **Abjad table:** mashriqī (project default; methodology.md §6).
3. **Sliding window across the entire concatenated word stream**, for window sizes **w ∈ {3, 4, 5, 6}**. (Bismillah = 4 words = anchor; w=3 and w=5,6 included to bracket the answer.) Window crosses verse and surah boundaries — this is conservative against false uniqueness because it gives 786 *more* chances to occur, not fewer.
4. For each window position record the abjad sum. Catalog every position whose sum equals **786**.
5. Compare to the empirical distribution of all sums in that window size: report rank, density, and the count for ±20 neighbouring values. The "neighbour density" metric is `mean(count[v]) for v in [786-20..786+20] excluding 786` divided by `count[786]` — values >> 1 mean 786 is sparse vs. neighbours; values << 1 mean it is dense.
6. **Bismillah-position handling:** the actual Bismillah at Q 1:1 (and the internal Q 27:30 occurrence per [[h-new-50-bismillah-114|H-NEW-50]]) will appear as 786-substrings of size 4. These are reported separately from "other" matches.
7. **Meaningfulness pass:** for every "other" 786-substring of any window size, record (start_surah, start_verse, start_word_idx, raw text, English glosses if available from translations). Flag substrings that are:
   - syntactically clean (no boundary-cross unless the whole window lies in one verse),
   - contain a divine name or theological core word (الله, الرحمن, الرحيم, ربك, etc.),
   - or constitute a complete classical-style phrase.
   Mark these as "potentially meaningful" — purely a flag, not a statistical claim.

## Decision rules (locked before run)

- **CONFIRMED H1 (uniqueness):** 786 has count = 1 OR 2 (Bismillah + Q 27:30 internal) at w=4 AND neighbour-density ratio ≥ 5 — i.e. neighbours are at least 5× more common than 786.
- **PARTIAL:** 786 occurs ≥ 3 times at w=4 but its neighbour-density ratio is ≥ 2 — i.e. it is rare but not unique.
- **CONTRADICTED H1:** 786 occurs ≥ 3 times at w=4 AND its neighbour-density ratio < 1 — i.e. 786 is at least as common as nearby values, so the Bismillah is *not* numerically singled out.
- **UNDERDETERMINED:** any other combination.

## Multiple-comparison correction

We test 4 window sizes; Bonferroni correction is built into the decision rule by requiring **the w=4 result to be the primary verdict**. The w=3, 5, 6 sizes are reported as exploratory / sensitivity context.

## Garden-of-forking-paths log (BEFORE run)

- Why no-tashkeel corpus? The mashriqī abjad table operates on consonants; tashkeel marks contribute zero in any case (see `gematria._SILENT_SKIP`). Choosing no-tashkeel matches how the canonical Bismillah anchor 786 was computed. Forking decision = locked to no-tashkeel.
- Why mashriqī? The 786 anchor is mashriqī. We do not also test maghribī here — separate hypothesis if needed.
- Why w ∈ {3,4,5,6}? w=4 is the Bismillah's own word count. w=3 and w=5/6 bracket. We do NOT test w=1 (single-word) because single-word abjad values are heavily studied elsewhere (asma al-husna, etc.), and we do NOT test w=2 because at w=2 the value 786 = (e.g.) "الرحيم الرحيم" types of things, which is a different question. Forking decision = locked to {3,4,5,6}.
- Why neighbour density window of ±20? Arbitrary but symmetric. Sensitivity check at ±10 and ±50 reported.
- Cross-boundary windows allowed? YES — locked. Disallowing them would inflate uniqueness artificially.

## Files

- This pre-reg: `findings/phase-b-hypotheses/h-new-87-786-substrings-prereg.md`.
- Script: `scripts/h_new_87_786_substrings.py`.
- Output (results): `findings/phase-b-hypotheses/h-new-87-786-substrings.md`.
- Catalog (data): `findings/phase-b-hypotheses/h-new-87-786-catalog.tsv`.
- Journal: `journal/h-new-87-run-1.md`.
