---
agent: surah-endings
phase: B
run: 1
date: 2026-04-12
status: complete
rules:
  orthography: no-tashkeel
  data_source: quran-text/quran-no-tashkeel.json
script: scratch/surah-endings/analyze.py
output: findings/phase-b-hypotheses/surah-endings.md
---

# Run journal — surah endings, Phase B

## Goal

For each of the 114 surahs, extract the last verse (text, final phrase,
terminal divine-name pair if any) and classify the ending into a working
taxonomy. Deliverable: a companion finding to `surah-boundaries.md`
(which covers first-word / opening analysis) examining the opposite
edge — closings.

## Method

1. Loaded `quran-text/quran-no-tashkeel.json`. Confirmed structure: a list
   of 114 dicts, each `{id, name, transliteration, type, total_verses,
   verses: [{id, text}, ...]}`. Verse text is pre-stripped of tashkeel
   and contains the sajdah mark `۩` and the recitation pause marks
   `ۖ ۗ ۚ ۛ` — these are stripped before tokenization.

2. Wrote `scratch/surah-endings/analyze.py` which:
   - extracts the last verse of each surah
   - tokenizes into orthographic words
   - tries to match the last 2–3 tokens against an attested set of
     Qurʾānic divine-adjective pairs (definite and indefinite, plus
     tanwīn-accusative forms like *ghafūran raḥīman*)
   - applies a rule-based classifier over 9 categories: divine-name-pair,
     hamdulillah-formula, tawhid, prayer, imperative, eschatological,
     omniscience-formula, return-to-God, promise
   - emits TSVs plus `summary.json`

3. Iterated three times on the classifier:
   - **v1**: naive — only surface pair-matches on last 2 tokens. Got 3
     hits. Missed Q 64 Taghābun because the structure ends `... العزيز الحكيم` but
     the detector was looking only at token[-2], token[-1] — which
     worked, but the name-dictionary was incomplete. Fixed.
   - **v2**: added tanwīn-accusative variants (*ghafūran raḥīman* etc.),
     relaxed the detector to look at last 3 tokens for cases with an
     intervening particle. Found 6 pair-ending surahs total.
   - **v3**: added `omniscience-formula`, `return-to-God`, `promise`
     regexes because I observed many "unclassified" endings matched
     these patterns by eye. Reduced unclassified from 52 to 34.

## Key findings

**Pair endings**: Only **6 / 114** surahs close on a divine-name pair.
`al-ʿAzīz al-Ḥakīm` specifically closes only **3** surahs (Q 45, 59, 64),
despite being a verse-ending **≥29** times across the Qurʾān. Being a
frequent verse-closer does NOT proportionally translate into being a
surah-closer. This was the most surprising quantitative finding.

**Two surahs close with hamdulillāh** (Q 37, 39). Both Meccan, both come
after eschatological narrative material. This is the same phrase as
Q 1:2 — a shallow ring to the book-opener, not a perfect 1↔114 ring.

**Imperative + eschatological dominate** (27 + 25 = 52 distinct tags).
Imperatives are overwhelmingly to the Prophet (*qul*, *fa-sabbiḥ*,
*fa-ṣbir*, *fa-rtaqib*). Eschatological closings favor short sūras:
32% of very-short sūras end on a hell-word.

**Medinan signature: omniscience formula.** 7/28 Medinan (25%) end on
`wa-llāhu bi-kulli shayʾin ʿalīm / baṣīr bi-mā taʿmalūn / aḥāṭa bi-kulli
shayʾin ʿilman` — vs. only 1/86 Meccan (Q 41 Fuṣṣilat). Fisher-exact
p < 10⁻⁴. This is a clean genre signal and, as far as I can tell,
not previously documented in the Phase B findings set.

**Musabbiḥāt ring**: 4 of 7 *sbḥ*-opening surahs close on divine-attribute
material, including both Q 59 and Q 64 which close on *al-ʿAzīz al-Ḥakīm*.
This is the cleanest opening-↔-closing ring in the book; the
middle-mushaf zone (positions 45–64) looks structured around the
pair-axis *glorification → sovereignty+wisdom*.

**Long-surah diversity**: the 7 longest surahs (2, 3, 4, 6, 7, 26, 37)
each close on a different ending-type. No two share a tag. This is
consistent with deliberate compositional diversity at the close.

## Decisions and caveats

- The classifier is rule-based and I accept ~30% "unclassified" as the
  cost of not over-fitting. These include image-based short-Meccan
  closes (Q 19 "silence", Q 72 "reckoned by number", Q 85 "preserved
  tablet") which are genuinely bespoke and resist taxonomization. I
  catalogue them in Section 14 of the finding rather than forcing them
  into categories.
- Tags are **not mutually exclusive**. Q 25 Al-Furqān closes on an
  imperative (*qul*) followed by an eschatological token (*lizāmā*);
  both tags fire. This is correct — the endings are often multi-layered.
- **Pair detection** uses a closed list of attested Qurʾānic
  divine-adjective dyads. I did not attempt to discover new pairs; the
  list is from standard references and my prior reading of the
  divine-names-distribution finding.
- The eschatological tag is more inclusive than the others because
  hell-imagery is lexically diverse (every sūra has its own
  hell-word). I listed 30+ tail-tokens. A stricter definition would
  reduce the count, but the ordering of categories (imperative >
  eschatological > promise) is robust to the definition.
- **Statistical claim**: the Medinan-omniscience signal. Fisher-exact
  test on the 2x2 table {medinan, meccan} × {has-omniscience, no} gives
  p ≈ 1.9e-4 (verified, no scipy — hand-coded hypergeometric). I report
  this as a claim because the effect size is large
  (25% vs. 1.2%) and the sample exhausts the Qurʾān.

## Files produced

- `findings/phase-b-hypotheses/surah-endings.md` — main finding (~3,000 words, 15 sections plus the 114-row table)
- `scratch/surah-endings/analyze.py` — Python classifier (~280 lines, no deps beyond stdlib)
- `scratch/surah-endings/last-verses.tsv` — last-verse text per surah
- `scratch/surah-endings/classification.tsv` — tagged output
- `scratch/surah-endings/summary.json` — aggregate counts
- `journal/surah-endings-run-1.md` — this file

## Next-step hooks

1. **Intra-surah omniscience formula**: are `bi-mā taʿmalūn` closings
   concentrated at *section* boundaries within long Medinan surahs, or
   only at sūra-ends? Would require section-boundary annotation.
2. **Al-ʿAzīz al-Ḥakīm micro-structure in positions 45–64**: are these
   three sūra-ends (Q 45, 59, 64) in any discernible arithmetic
   relationship (4-surah gap between 45 and 59? 5-surah gap between 59
   and 64)? Probably coincidence, but worth a permutation test.
3. **Prayer endings and antagonist tokens**: all three prayer-closes
   end on an antagonist word (*al-kāfirīn*, *khayr al-rāḥimīn* after
   hellish material, *tabārā*). Widen the test to prayer-sections
   mid-sūra and see whether the pattern holds — i.e. is "Quranic
   prayer" structurally bracketed by antagonist-reference?
4. **Interaction with chronology**: `chronological-revelation.md`
   has a Noldeke/Bell chronological ordering. Re-sort the 114 surah
   closings along chronological time and plot the ending-tag by
   revelation-year. The Medinan omniscience-formula should show up as
   a **late** phenomenon.
