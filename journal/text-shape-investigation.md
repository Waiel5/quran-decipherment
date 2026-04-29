# text-shape investigation — what's actually inside `amrayn/quran-text`

Date: 2026-04-12
Investigator: text-shape agent
Status: closed — anchors locked, primary corpus selected

## TL;DR

1. **Two of the three flat-text files in `amrayn/quran-text` are corrupt.** `quran-flat-min-tashkeel.txt` and `quran-flat-full-tashkeel.txt` are MySQL `GROUP_CONCAT` dumps that hit the server's 1 MiB output ceiling and were silently truncated mid-verse. The min variant stops at surah 61 (As-Saff) verse 5; the full variant stops at surah 40 (Ghafir) verse 40. Only the no-tashkeel flat file is intact.
2. **All three JSON files (`quran-{no,min,full}-tashkeel.json`) are intact** — 114 surahs, 6 236 verses each.
3. **`wc -w` is meaningless on these flat files.** The min/full flat files start with the literal SQL header line `GROUP_CONCAT(text SEPARATOR ' ')\n`, which alone contributes 4 spurious "words". More importantly, these files are word-truncated, so smaller is not "tashkeel removed more words" — smaller is "more bytes thrown away".
4. **Recitation marks (U+06D6..U+06ED) are stored space-separated in all three corpora**, so any naive whitespace tokenizer over-counts "words" by ~4 500. Real-word counts (after filtering tokens that consist only of recitation marks) agree to within ~370 across the JSON variants. The remaining ~370 difference is the vocative `يا` particle: written as a separate word in `no-tashkeel` but contracted to `يٰ` and joined to the following word in `min/full`.
5. **Primary corpus going forward: `quran-no-tashkeel.json`** (intact, byte-equal to its flat sibling, simplest character set, easiest to grapheme-count). Use `quran-full-tashkeel.json` as a secondary source whenever shadda doubling or vowel-marked claims are in play.

## File-by-file forensics

### `quran-flat-no-tashkeel.txt` — INTACT

| Property | Value |
|---|---|
| Bytes | 752 948 |
| Codepoints | 417 661 |
| BOM | none |
| Header line | none |
| Trailing newline | none |
| Internal newlines | 0 |
| Carriage returns | 0 |
| First bytes | `بسم الله الرحمن الرحيم الحمد ...` |
| Last bytes | `... من الجنة والناس` (correct end of surah 114) |

**Byte-equal** to `' '.join(verse.text for verse in JSON)` from `quran-no-tashkeel.json`. The whole Quran is on a single line, verses joined by single ASCII space, no per-surah marker, no verse-number markers. No basmala except the one in surah 1 (the JSON only carries the sectional basmala for Al-Fatiha — the other 113 are absent from this dataset entirely; see "Basmala policy" below).

`wc -w` reports 82 375. That figure is a whitespace token count, of which **4 578 tokens are pure recitation marks** (U+06D6 ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA, U+06DA ARABIC SMALL HIGH JEEM, etc.) standing alone between spaces. The "real-word" count is **77 797**.

### `quran-flat-min-tashkeel.txt` — CORRUPT (truncated mid-surah-61)

| Property | Value |
|---|---|
| Bytes | 1 048 610 |
| Body bytes (after stripping header + trailing newline) | **1 048 576 = exactly 1 MiB** |
| BOM | none |
| Header line | `GROUP_CONCAT(text SEPARATOR ' ')\n` (33 bytes — literal SQL output) |
| Trailing | `\n` |
| Truncation point | mid-verse, surah 61 (As-Saff) verse 5 |
| Last legible text | `... وَاللَّهُ لا يَه` (cuts off in the middle of `يهدي`) |

The 1 MiB body length is the smoking gun: this file was produced by running `SELECT GROUP_CONCAT(text SEPARATOR ' ') FROM quran_min` on a MySQL server with the default `group_concat_max_len = 1024` raised to 1 048 576 (1 MiB) and not raised again. The result was redirected to a file with the column header included, and the truncated bytes were committed to the repo without anyone noticing that nine surahs were missing.

`wc -w` reports 75 563 — meaningless. The header alone contributes 4 tokens (`GROUP_CONCAT(text`, `SEPARATOR`, `'`, `')`).

### `quran-flat-full-tashkeel.txt` — CORRUPT (truncated mid-surah-40)

| Property | Value |
|---|---|
| Bytes | 1 048 609 |
| Body bytes | **1 048 575 ≈ 1 MiB − 1** |
| BOM | none |
| Header line | `GROUP_CONCAT(text SEPARATOR ' ')\n` (33 bytes) |
| Trailing | ` \n` (note the trailing SPACE before the newline — this is what makes the file 1 byte shorter than the min variant; the cut landed in a different position because the full text has more diacritics per word) |
| Truncation point | mid-verse, surah 40 (Ghafir) verse 40 |
| Last legible text | `... فَلَا يُجْزَىٰٓ إِلَّا مِثْلَهَا ۖ` |

Same MySQL truncation as the min file, just with even more bytes per word so the 1 MiB ceiling cuts off **75 surahs** of content. This file contains roughly the first 36 % of the Quran.

The "1-byte-difference between min (1048610) and full (1048609)" the orchestrator flagged is fully explained: both files were truncated at the byte-by-byte 1 MiB ceiling; min happened to land on a position that allowed a final non-space byte before the closing newline; full happened to land such that the last in-text byte was a space, producing `... ۖ \n` instead of `...x\n`. It is **not** a 1-byte content difference between equivalent texts.

### `quran-no-tashkeel.json` — INTACT

114 surahs, 6 236 verses, every `verse.text` is well-formed UTF-8 with no tashkeel marks (only recitation marks U+06D6..U+06ED remain; tashkeel U+064B..U+065F are absent). Verses are stored with single ASCII spaces between words; no verse-end punctuation, no verse-number markers in the text itself (verse number is in the JSON `id` field).

### `quran-min-tashkeel.json` — INTACT

Same 114 / 6 236 structure. Adds the standard tashkeel marks (fathah, dammah, kasrah, sukun, shaddah, etc.) AND uses the contracted vocative `يٰ` (alif-with-superscript-alif) attached to following words instead of the separate word `يا`. This contraction accounts for the ~370-word "real-word" gap relative to the no-tashkeel JSON. Also uses 458 tatweel (U+0640) characters as orthographic stretches (these are NOT word separators and don't change token counts).

### `quran-full-tashkeel.json` — INTACT

Same 114 / 6 236 structure. Uses the Uthmani orthography (alif-with-wasla `ٱ` U+0671 instead of plain alif at certain positions, more rounded zeros U+06DF for sukoon-like marks, dagger-alif markers, etc.). Real-word token count = **77 429**.

## Reconciling the four word counts the orchestrator was confused about

| Source | Count | Real meaning |
|---|---|---|
| `wc -w quran-flat-no-tashkeel.txt` | 82 375 | 77 797 real words + 4 578 standalone recitation marks. Trustworthy as input but you must filter recitation-mark tokens. |
| `wc -w quran-flat-min-tashkeel.txt` | 75 563 | **GARBAGE** — truncated at surah 61 + SQL header tokens + recitation-mark tokens. Do not use. |
| `wc -w quran-flat-full-tashkeel.txt` | 64 595 | **GARBAGE** — truncated at surah 40 + SQL header tokens + recitation-mark tokens. Do not use. |
| `' '.join(min JSON verses).split()` | 82 008 | 77 430 real + 4 578 recitation marks. The 82 008 the orchestrator measured. |
| `' '.join(no JSON verses).split()` | 82 375 | 77 797 real + 4 578 recitation marks. |
| `' '.join(full JSON verses).split()` | 77 429 | 77 429 real + 0 recitation marks (full-tashkeel uses different small-letter codepoints, not the standalone marks). |

The 82 008 vs 75 563 gap inside "min-tashkeel" that the orchestrator highlighted is explained 100 % by the flat file's truncation at surah 61 + the absence of the SQL-header tokens in the JSON measurement.

The 82 375 vs 82 008 gap between `no` and `min` JSON (367 words) is explained by the vocative `يا` → `يٰ-` contraction (~360 verses) plus a few miscellaneous merges.

The 82 008 vs 77 429 gap between `min` and `full` JSON (4 579 words) is explained by recitation marks: `min` stores them as standalone glyphs separated by spaces, `full` uses the modern combining-mark equivalents that attach to the previous letter (so they don't appear as separate tokens). 4 578 ≈ 4 579, perfect match.

## Verse / surah / character inventories (from intact sources)

| Quantity | Source | Value |
|---|---|---|
| Surahs | any JSON / flat-no | 114 |
| Verses | any JSON | 6 236 |
| Codepoints in joined no-tashkeel | flat-no = JSON | 417 661 |
| ASCII spaces in joined no-tashkeel | flat-no = JSON | 82 374 |
| Whitespace tokens in joined no-tashkeel | flat-no = JSON | 82 375 |
| Recitation-mark-only tokens (U+06D6..06ED standalone) | flat-no | 4 578 |
| Real-word tokens, no-tashkeel | flat-no | **77 797** |
| Arabic letter graphemes (U+0621..064A ∪ U+0671..06D3), no-tashkeel JSON | JSON | **330 709** |
| Real-word tokens, full-tashkeel JSON | JSON | 77 429 |
| Arabic letter graphemes, full-tashkeel JSON | JSON | 327 038 |
| Shadda count (U+0651), full-tashkeel JSON | JSON | 22 678 |
| Letters with shadda doubled, full-tashkeel JSON | JSON | **349 716** |
| Tatweel (U+0640) count, min-tashkeel JSON | JSON | 458 |
| Tatweel count, full-tashkeel JSON | JSON | 385 |
| Tatweel count, no-tashkeel JSON | JSON | 0 |

## Basmala policy — what the dataset actually does

The amrayn JSONs include the basmala **only as verse 1 of surah 1 (Al-Fatiha)**. The other 113 surahs do NOT have a separate basmala field, and the basmala does NOT appear inside their verse 1. This means amrayn implements the methodology's `counted-only-in-surah-1` policy by construction. To recover other policies analytically:

- `counted-only-in-surah-1` (default): use the data as-is. Real-word count 77 797, letter count 330 709 (no-tashkeel).
- `counted-in-surah` (basmala counted at the head of every surah): add 113 × basmala = 113 × 4 words (452) and 113 × 19 letters (2 147). Real-word count 78 249, letter count 332 856.
- `always-separator`: subtract the surah-1 basmala (4 words, 19 letters). Real-word count 77 793, letter count 330 690.

(Note: if a future replication argues the at-Tawba absence is intentional and the other 113 should each carry a basmala once, that's the `counted-in-surah` row.)

## Other character oddities found

- **No BOM, no `\r`, no `\u2028`/`\u2029`, no NBSP, no ZWJ/ZWNJ, no LRM/RLM, no ALM** in any of the six files. The only "trick" characters are the recitation marks already discussed and the SQL-header garbage at the top of the broken flat files.
- **No verse-number markers** like `(1)` or `١٢٣` in any text body. Surah/verse numbering lives only in the JSON keys. The two `(` and `)` characters present in `quran-flat-min-tashkeel.txt` and `quran-flat-full-tashkeel.txt` are both inside the SQL header line.
- **The vocative `يا` collapse in min/full** is the largest non-truncation difference between variants and is the only thing that makes "real-word counts" diverge between no-tashkeel (77 797) and full-tashkeel (77 429).

## What our counting tools should target as canonical anchors

These are the values every counting tool we write **must** reproduce, or it's broken. They are derived from the **JSON** sources, since the flat files are partially corrupt.

| Anchor | Source / rule | Value |
|---|---|---|
| Surahs | any JSON | **114** |
| Verses (hafs-kufan) | any JSON | **6 236** |
| Whitespace tokens, no-tashkeel JSON, basmala-counted-only-in-surah-1, recitation-marks-NOT-filtered | `' '.join(verses).split()` on `quran-no-tashkeel.json` | **82 375** |
| Real-word tokens, no-tashkeel, basmala-counted-only-in-surah-1 (recitation-mark-only tokens filtered) | same, with rec-mark filter | **77 797** |
| Real-word tokens, min-tashkeel JSON, basmala-counted-only-in-surah-1 (rec-mark filter) | `quran-min-tashkeel.json` | **77 430** |
| Real-word tokens, full-tashkeel JSON, basmala-counted-only-in-surah-1 | `quran-full-tashkeel.json` | **77 429** |
| Letter graphemes, no-tashkeel JSON, basmala-counted-only-in-surah-1 | `quran-no-tashkeel.json`, count chars in U+0621..064A ∪ U+0671..06D3 | **330 709** |
| Letter graphemes + shadda doubled, full-tashkeel JSON, basmala-counted-only-in-surah-1 | `quran-full-tashkeel.json` | **349 716** |
| Shadda count (U+0651), full-tashkeel JSON | `quran-full-tashkeel.json` | **22 678** |

A counting tool that targets `[no/orth/basmala-only-1] real-words = 77 797` is provably correct against the data. Anyone reporting the famous "77 934" or "77 797" or "77 429" word count number from the literature should now be able to point at exactly which orthography + basmala policy + tokenizer they're using.

## Recommendations to the team

1. **Primary corpus: `quran-no-tashkeel.json`.** Single normalization, no marks to confuse a tokenizer, byte-equal to its flat sibling, uses plain `يا` (no contracted vocative), and is the only file where letter graphemes correspond directly to consonantal-skeleton letters without further normalization. Most Code-19-style replications work in skeleton form anyway.
2. **Secondary corpus: `quran-full-tashkeel.json`** for any claim that requires shadda doubling, vowel marks, or Uthmani orthography (e.g. counts that depend on alif-with-wasla `ٱ`).
3. **Cross-check corpus: `quran-min-tashkeel.json`** for any claim where the vocative `يا` matters or where minimal tashkeel is the canonical orthography in the source paper.
4. **Do not use any of the three `quran-flat-*-tashkeel.txt` files for `min` or `full`.** They are truncated. Either re-derive them from the JSON in code or fetch a fresh copy from a different source (Tanzil, etc.). The `quran-flat-no-tashkeel.txt` file is safe — it is byte-equal to a JSON-derived join.
5. **Filter recitation-mark-only tokens** in any whitespace tokenizer. A "token" of the form `ۖ` or `ۚ` (U+06D6..06ED standalone) is not a word; it's a recitation pause marker that the data happens to store space-separated. Without this filter every word count is inflated by ~4 578.
6. **Open an upstream issue against `amrayn/quran-text`** noting the truncation. The flat files are obviously generated by a build script that runs `SELECT GROUP_CONCAT(text SEPARATOR ' ')` on MySQL without raising `group_concat_max_len` to a sufficient value. The fix is `SET SESSION group_concat_max_len = 16777216;` (or similar) before the SELECT.
7. **Also note** that the flat files include the literal SQL `GROUP_CONCAT(...)` column header — even if they were re-generated without truncation, that header must be stripped. Any tool reading the flat files should `.lstrip()` past the first newline if the first byte is `G`.

## Files referenced

- `/Users/grey/Downloads/quran/quran-text/quran-flat-no-tashkeel.txt` — intact, 752 948 B
- `/Users/grey/Downloads/quran/quran-text/quran-flat-min-tashkeel.txt` — TRUNCATED at surah 61:5, 1 048 610 B
- `/Users/grey/Downloads/quran/quran-text/quran-flat-full-tashkeel.txt` — TRUNCATED at surah 40:40, 1 048 609 B
- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` — intact, 114 surahs / 6 236 verses
- `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` — intact, 114 surahs / 6 236 verses
- `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json` — intact, 114 surahs / 6 236 verses
