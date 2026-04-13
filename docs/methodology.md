# Methodology — Counting Rules and Conventions

**The Quran is one text.** 114 surahs, 6,236 verses, a definite sequence of Arabic words. This document specifies the minor presentation details (diacritics, spelling conventions, word-boundary choices) that counting tools need to agree on when producing numbers about that one text. Do not confuse these technical rules with the existence of "different Qurans" — there is one Quran. Tashkeel, spelling tradition, and translation are rendering choices, not separate works.

**Canonical corpus:** `quran-text/quran-no-tashkeel.json`. Every tool and finding uses this as THE Quran unless a specific claim is letter-pedantic enough to need a spelling-sanity cross-check, in which case the auxiliary file `data/alt-text/quran-uthmani-consonantal.json` (same Quran, traditional mushaf spelling) provides one.

Every claim — replicated or novel — references one of these rule sets via its `rules` tuple. New rule sets are added here as we encounter them in the literature; we never silently "discover" a rule by counting up to a desired number.

## 1. Orthography variants

We have three variants of the Arabic text from amrayn/quran-text:

- `no-tashkeel`: bare consonantal skeleton, no diacritics
- `min-tashkeel`: minimal essential diacritics
- `full-tashkeel`: full diacritics (vowels, sukoon, shaddas)

We will additionally cross-verify against Tanzil's Uthmani text once acquired.

**Resolved 2026-04-12 by `text-shape` agent (see `journal/text-shape-investigation.md`):** the three flat-text variants disagree because **two of the three flat files are corrupt**. `quran-flat-min-tashkeel.txt` and `quran-flat-full-tashkeel.txt` are MySQL `GROUP_CONCAT` dumps that hit the server's 1 MiB ceiling and were silently truncated mid-verse (at surah 61:5 and surah 40:40 respectively); they also begin with a literal SQL header line (`GROUP_CONCAT(text SEPARATOR ' ')\n`). Only `quran-flat-no-tashkeel.txt` is intact, and it is byte-equal to its JSON sibling. **All three JSON files are intact** (114 surahs, 6 236 verses each). **Primary corpus going forward: `quran-no-tashkeel.json`.** Secondary: `quran-full-tashkeel.json` for shadda-doubled / Uthmani claims. Use `quran-min-tashkeel.json` only when minimal tashkeel is the source paper's specified orthography. Do **not** use the truncated flat files for any analysis.

## 2. Word definition

A "word" is ambiguous in Arabic. Possible definitions:

- `orthographic-token`: anything between two whitespace characters in the chosen orthography
- `lemma`: dictionary headword (requires morphological analysis from the Quranic Arabic Corpus)
- `with-clitics-split`: orthographic token with proclitics (`wa-`, `bi-`, `li-`, `ka-`, `fa-`, `sa-`, `al-`) split off as separate tokens
- `with-pronominal-suffixes-split`: orthographic token with attached pronouns (`-hu`, `-ha`, `-hum`, `-na`, etc.) split off
- `dictionary-headword`: distinct headword in a Quranic dictionary

Many famous claims (e.g., the Day/Night word counts) are sensitive to which definition is used. We compute counts under multiple definitions where it matters and flag the divergence.

## 3. Letter definition

- `graphemes`: count of Arabic letter graphemes (alif, ba, ta, ...) in the chosen orthography
- `with-shadda-doubled`: shadda counts as duplication (the consonant under the shadda is counted twice)
- `with-hamza-distinct`: hamza-on-alif (أ إ), hamza-on-waw (ؤ), hamza-on-ya (ئ) are distinct from their carriers
- `with-hamza-collapsed`: all hamza variants count as one letter
- `with-tanwin-as-nun`: tanwin (-an, -in, -un) counts as a final nun (relevant for some Code-19 variants)
- `with-alif-maqsura-as-ya-or-alif`: choice point for ى vs ي vs ا

These choices change letter totals by hundreds. Code-19 family results are extremely sensitive to all of them.

## 4. Basmala policy

The opening basmala (بسم الله الرحمن الرحيم) appears at the head of 113 of 114 surahs (all except At-Tawba) and as verse 1 of Al-Fatiha.

- `counted-in-surah`: the opening basmala of each surah counts toward that surah's letter/word totals. **Canonical interpretation (locked 2026-04-12):** the basmala is prepended to **all 114 surahs**, including Al-Fatiha. Since Al-Fatiha's verse 1 already *is* the basmala, this double-counts it in surah 1. That's the interpretation under which the §8 anchor adjustment `+452 words / +2147 letters` was derived (= 113 basmalas prepended to non-Fatiha/non-Tawba + 1 extra for Al-Fatiha's existing verse 1 being already-counted = 113×4 words = 452; 113×19 letters = 2147 → matches). Tools must prepend even when the first verse already contains the basmala.
- `counted-only-in-surah-1`: the basmala is part of Al-Fatiha only; it is a separator everywhere else. **This is the policy amrayn's JSONs use by construction** — only surah 1 verse 1 stores the basmala text; the 113 other sectional basmalas are absent from the data. All §8 anchors (unless adjustment row is applied) are computed under this policy.
- `always-separator`: basmala is purely a separator and counts nowhere — subtract Al-Fatiha's verse 1 to get this. Adjustment: `−4 words / −19 letters` per §8.

This single choice changes Code-19 results by tens of letters. Khalifa's original work used `counted-only-in-surah-1`, matching the amrayn default.

## 5. Verse numbering

- `hafs-kufan`: 6,236 verses (the dominant modern numbering, what the amrayn dataset uses)
- `warsh-madanian`: 6,214 verses
- `basran`: 6,205
- `damascene`: 6,227

We default to `hafs-kufan`. Claims that depend on alternative numberings will be flagged.

## 6. Abjad / gematria table

Two competing tables exist. Both are **locked** 2026-04-12 — every tool must use these exact values or declare a variant.

- `mashriqi` (eastern, used in most numerology and in Rashad Khalifa's work):
  - ا=1 ب=2 ج=3 د=4 ه=5 و=6 ز=7 ح=8 ط=9 ي=10
  - ك=20 ل=30 م=40 ن=50 س=60 ع=70 ف=80 ص=90
  - ق=100 ر=200 ش=300 ت=400 ث=500 خ=600 ذ=700 ض=800 ظ=900 غ=1000
- `maghribi` (western, used in Maghreb/Andalusian traditions):
  - Same 1–10 and 20–80 sequence (ا..ف)
  - Diverges at ص and later: ص=60, ق=70... — full table below
  - ا=1 ب=2 ج=3 د=4 ه=5 و=6 ز=7 ح=8 ط=9 ي=10
  - ك=20 ل=30 م=40 ن=50 ص=60 ع=70 ف=80 ض=90
  - ق=100 ر=200 س=300 ت=400 ث=500 خ=600 ذ=700 ظ=800 غ=900 ش=1000

**Hamza carrier policy** (locked): the letters أ إ ؤ ئ (hamza on alif/waw/ya) are treated as their *carrier* letter for abjad (so أ = 1 same as ا; ؤ = 6 same as و; ئ = 10 same as ي). The bare hamza ء is skipped (not in standard abjad tables). Tools should warn but not error on unrecognized characters.

We default to `mashriqi` and report when a claim only works under one or the other. Any claim must specify which table it uses in its rules tuple.

## 7. The rules tuple

Every replication and novel-finding markdown file must include a YAML block at the top:

```yaml
rules:
  orthography: ...
  word_definition: ...
  letter_definition: ...
  basmala_policy: ...
  verse_numbering: ...
  abjad_table: ...   # only if gematric, else 'not-applicable'
  null_model: ...    # only for novel findings (Phase B+), else 'not-applicable'
```

If a value is `not-applicable`, say so explicitly. Empty fields are forbidden.

## 8. Anchor values for sanity testing

Locked 2026-04-12 by `text-shape`. These are unit tests for every counting tool we write — if a tool can't reproduce these from the raw data, it's broken. **All anchors are computed from the JSON sources** (`quran-{no,min,full}-tashkeel.json`), which are intact; the flat `min`/`full` files are truncated and must not be used. Word counts assume verses are joined with single ASCII spaces between them (`' '.join(verse.text for surah in data for verse in surah.verses)`) before tokenizing. The amrayn dataset stores the basmala only as verse 1 of surah 1 (basmala-counted-only-in-surah-1 by construction).

| Anchor | Rule tuple | Value | Status |
|---|---|---|---|
| Surah count | any | 114 | ✅ confirmed |
| Verse count | hafs-kufan | 6236 | ✅ confirmed |
| Whitespace tokens (rec-marks NOT filtered) | (no-tashkeel JSON, orthographic-token, basmala-counted-only-in-surah-1) | 82375 | ✅ locked |
| Real-word tokens (rec-mark-only tokens filtered) | (no-tashkeel JSON, orthographic-token, basmala-counted-only-in-surah-1) | 77797 | ✅ locked |
| Real-word tokens | (min-tashkeel JSON, orthographic-token, basmala-counted-only-in-surah-1) | 77430 | ✅ locked |
| Real-word tokens | (full-tashkeel JSON, orthographic-token, basmala-counted-only-in-surah-1) | 77429 | ✅ locked |
| Whitespace tokens (raw, rec-marks NOT filtered) | (min-tashkeel JSON, orthographic-token, basmala-counted-only-in-surah-1) | 82008 | ✅ locked (matches earlier provisional measurement) |
| Letter count | (no-tashkeel JSON, graphemes, basmala-counted-only-in-surah-1) — counts U+0621..064A ∪ U+0671..06D3, excludes recitation marks U+06D6..06ED | 330709 | ✅ locked |
| Letter count | (full-tashkeel JSON, graphemes, basmala-counted-only-in-surah-1) — same range | 327038 | ✅ locked |
| Letter count | (full-tashkeel JSON, with-shadda-doubled, basmala-counted-only-in-surah-1) — graphemes + count of U+0651 | 349716 | ✅ locked |
| Shadda count (U+0651) | full-tashkeel JSON | 22678 | ✅ locked |
| Recitation-mark-only standalone tokens | no-tashkeel JSON or min-tashkeel JSON | 4578 | ✅ locked |
| Basmala letters / words (no-tashkeel) | (no-tashkeel, graphemes) on `بسم الله الرحمن الرحيم` | 19 letters / 4 words | ✅ locked |
| Adjustment for `basmala-counted-in-surah` policy | add 113 × basmala | +452 words, +2147 letters | ✅ locked |
| Adjustment for `always-separator` policy | subtract 1 × basmala | −4 words, −19 letters | ✅ locked |

## 9. The "rule fingerprint" rule

When we report a finding, the headline number is always tagged with a short fingerprint of the rules tuple, e.g. `[mt/orth/sep] 82008 words` reads as "min-tashkeel orthography, orthographic-token word definition, basmala-as-separator". This fingerprint goes in tables and chart captions so the rules can never be silently swapped.
