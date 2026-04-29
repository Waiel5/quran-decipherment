# Verse Signature Atlas — Run 1

**Date:** 2026-04-12
**Goal:** Produce a per-verse atlas giving *something* — at minimum a set of
default structural tags plus a one-sentence English characterization — for
every one of the 6,236 canonical Hafs ayat.

## Method

1. Loaded `quran-text/quran-no-tashkeel.json` (authoritative 114-surah / 6,236-verse structure) and `data/translations/en.sahih.txt` (Sahih International), aligning line-by-line to the canonical verse order.
2. Pulled rhyme letters and letter counts from `findings/phase-b-hypotheses/phonetic-profiles-per-verse.csv` and `gematria-verse-totals.csv` — both cover all 6,236 verses.
3. Merged the existing `findings/per-verse-annotations.csv` tag set (5,778 verses pre-tagged there).
4. Overlaid additional findings-level tags from nine verse-level CSVs: rhetorical-questions, vocatives, parables, hapaxes, innama, oath clusters, jinas, divine-names, iltifat.
5. For every verse, appended default structural tags: Meccan/Medinan class, surah id, position class (opening/early/middle/late/closing), length bucket (ultra-short / short / medium / long / very-long), rhyme-ending letter, rhyme conformity vs surah mode, and surface flags (contains-basmala, contains-innama, contains-vocative-ar, qul-imperative, mentions-Allah, ends-with-Allah, opens-with-qad, possible-oath-opening, muqattaat-opener, etc.).
6. Applied a rule-based `characterize()` heuristic on the English translation to produce one of ~18 verb-phrase labels (e.g. "Poses a rhetorical question", "Legislates a ruling", "Describes a sign in nature", "Narrates prophetic history", "Glorifies or praises Allah", …).

## Output

- `/Users/grey/Downloads/quran/findings/verse-signature-atlas.csv` — 6,236 rows × 10 columns.
- `/Users/grey/Downloads/quran/findings/verse-signature-atlas-highlights.md` — top-100 most-tagged table, tag vocabulary, surah density ranking, coverage discussion.

## Coverage

| metric | count | % |
|---|---:|---:|
| total verses | 6,236 | 100.0 |
| verses with ≥ 1 tag | 6,236 | 100.0 |
| verses with 5+ tags | 6,236 | 100.0 |
| verses with 10+ tags | 3,618 | 58.0 |
| verses with 20+ tags | 188 | 3.0 |
| zero-tag verses | 0 | 0.0 |

**Unique tag vocabulary:** 347 distinct tag strings.

## Notes

- Because every verse inherits ≥ 5 structural defaults by construction, the minimum viable annotation is always met.
- Medinan legal ayat (e.g. Q 2:282–283, much of Surat al-Nisa' § inheritance) sit near the low end of the density distribution; they carry their structural defaults plus `medinan`, legal-imperative marker, and their characterization ("Legislates a ruling"), but rarely show up in rhetorical-question / oath / parable / muqatta'at overlays.
- Highest per-verse density sits in Al-Fatiha (avg 31.9 tags/verse) — expected, since Q 1 is the single most-studied pericope in the project.

## Files added / modified

- `scripts/build_verse_atlas.py` — reproducible builder.
- `findings/verse-signature-atlas.csv` — new.
- `findings/verse-signature-atlas-highlights.md` — new.
- `journal/verse-atlas-run-1.md` — this file.
