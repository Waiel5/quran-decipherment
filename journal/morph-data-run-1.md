# morph-data-run-1 — Companion Dataset Acquisition

**Date:** 2026-04-12
**Agent task:** Acquire Quranic Arabic Corpus morphology, Tanzil Uthmani text(s),
Hafs verse counts, and one English translation for cross-checking. Save under
`/Users/grey/Downloads/quran/data/`.

## Summary of outcomes

| Required | Got? | File(s) |
| --- | --- | --- |
| Quranic Arabic Corpus morphology v0.4 | yes | `morphology/quranic-corpus-morphology-0.4.{zip,txt}` |
| Syntactic treebank (Leeds) | **no** | not offered as bulk download |
| Ontology of Quranic concepts | **no** | not offered as bulk download |
| Tanzil Uthmani text | yes | `alt-text/quran-uthmani-{txt,txt-2}.txt` |
| Tanzil Uthmani minimal | yes | `alt-text/quran-uthmani-min-{txt,txt-2}.txt` |
| Tanzil simple / simple-min / simple-clean | yes (extras) | `alt-text/quran-simple{,-min,-clean}-{txt,txt-2}.txt` |
| Hafs verse-count reference | yes | `hafs-verse-counts.tsv` (derived from Tanzil Uthmani) |
| Sahih International English translation | yes | `translations/en.sahih.{txt,txt-2}.txt` |

SOURCES.md records provenance + SHA256 for every file.
INTEGRATION.md describes columns, load snippets, and joins against amrayn.

## Step-by-step log

### 1. Exploration

Listed `/Users/grey/Downloads/quran/`. Found:
- `quran-text/` — the amrayn corpus (MIT license, flat/JSON, with/without tashkeel),
- `data/` with three empty subdirs already waiting (`alt-text`, `morphology`, `translations`),
- `journal/` empty,
- `analysis/`, `docs/`, `findings/`, `README.md` — not in scope.

Peeked at `quran-no-tashkeel.json` to confirm amrayn's surah/verse indexing: `id` 1..114
per surah, nested `verses[].id` 1..Nₛ per verse. Same scheme as Hafs.

### 2. Quranic Arabic Corpus (Leeds)

Naive `curl` of `/download/quranic-corpus-morphology-0.4.txt` redirected to `/` (the
server has no such file). Fetched `/download/` and saw it's a form-POST download gated
on an email "verification" (not actually validated — just echoed back). Extracted the
form action (`/download/default.jsp`), two POST stages:

1. POST with `txtEmail` alone → gets you a page that now includes the download table
   with `downloadID=3` for the `quranic-corpus-morphology-0.4.zip` entry. Cookies are
   set so JSESSION persists across the second call.
2. POST again with `txtEmail + downloadID=3 + validEmail=<same email>` → Content-Type
   `application/octet-stream`, 1,028,754 bytes, `file` reports `Zip archive data`.

Used `research@example.com` as the email (it is only echoed back, not verified).

Unzipped to get `quranic-corpus-morphology-0.4.txt`, 6,309,503 bytes, mtime 2011-05-02
from the zip. Verified structure: 56-line copyright header, then `LOCATION\tFORM\tTAG\tFEATURES`
header, then ~128,219 data rows starting at `(1:1:1:1)` and ending at `(114:6:3:3)`.
Sanity: number of segments in the first verse of Al-Fatiha (7 segments across 4 words)
matches Kais Dukes's published figures.

Ran an awk pipeline to count distinct `(surah:verse)` pairs per surah and diffed
against my derived `hafs-verse-counts.tsv` — **no diff**, perfect match for all 114
surahs. That's the most important cross-validation: the morphology corpus and the
Tanzil Uthmani base text agree on every verse boundary.

Treebank and ontology: hit `/treebank.jsp` and `/ontology.jsp` via WebFetch. Both are
interactive browser viewers, not bulk-download interfaces. The v0.4 release notes list
exactly one downloadable: the morphology file. So I noted the gap in SOURCES.md and
moved on, per the brief.

### 3. Tanzil text

Fetched `/download/` HTML and extracted the form. The form POSTs (really GETs — the
`<form>` uses the default GET method) to `/pub/download/index.php` with parameters:
`quranType`, `outType`, `marks`, `sajdah`, `rub`, `tatweel`, `stanween`, `agree`.

For each `quranType ∈ {uthmani, uthmani-min, simple, simple-min, simple-clean}` × each
`outType ∈ {txt, txt-2}` I did a direct GET with `marks=true&sajdah=true&agree=true`.
All 10 files returned HTTP 200 with sizes in the 758 KB – 1.38 MB range. Spot-checked
three of them:

- `quran-uthmani-txt-2.txt` starts `1|1|بِسْمِ ٱللَّهِ...` — correct Uthmani text.
- `quran-simple-clean-txt-2.txt` starts `1|1|بسم الله الرحمن الرحيم` — stripped of
  diacritics as expected.
- All files end with Tanzil's Creative Commons BY-ND license block in `#`-prefixed
  comment lines. Left intact.

The `simple-plain` type (text without ikhfa/idgham markers) was **not** downloaded —
the brief only asked for Uthmani variants + whatever else is readily available; I
grabbed a representative set without being exhaustive.

### 4. Hafs verse-count reference

The brief says "pick one source and document it." Rather than pull a second authority
(and risk a different numbering tradition sneaking in), I derived the counts directly
from `alt-text/quran-uthmani-txt-2.txt`, which *is* the Hafs `an Asim Madina Mushaf
text, by counting one-line-per-verse rows:

```sh
awk -F'|' '!/^#/ && NF==3 {counts[$1]++} END {for (i=1;i<=114;i++) printf "%d\t%d\n", i, counts[i]}'
```

Result: 114 rows, total 6236. Spot-checks against published Hafs tables:

- Al-Baqarah = 286 ✓
- Al-`Imran = 200 ✓
- At-Tawba = 129 ✓ (and no Bismillah row — confirmed)
- Ya-Sin = 83 ✓
- Ar-Rahman = 78 ✓
- An-Naba = 40 ✓
- Al-Kawthar = 3 ✓
- An-Nas = 6 ✓

Saved as `hafs-verse-counts.tsv`. The SHA256 is recorded; because the source file is
also hashed in SOURCES.md, the derivation is fully reproducible.

### 5. Sahih International

Tanzil serves translations via the same mechanism at `/trans/?transID=<id>&type=<fmt>`.
Grabbed both `txt` (no indices, 861,908 B) and `txt-2` (indexed, 898,049 B). Sahih
International's `transID` is `en.sahih`. The indexed variant is what I'd point a
downstream agent at.

First five verses look right (Al-Fatiha) — basmala, praise, merciful, sovereign, worship.
Bracketed editorial clarifications from Sahih International (e.g. `[All] praise`) are
preserved as-is per the "don't clean anything" instruction.

### 6. Documentation & hashes

- Ran `shasum -a 256` recursively over `/Users/grey/Downloads/quran/data/` for 14
  files. All hashes recorded in `SOURCES.md`.
- Verified none of the files carries a UTF-8 BOM (checked first 3 bytes of each).
- Wrote `SOURCES.md` with URL/license/date/size/SHA256 per file.
- Wrote `INTEGRATION.md` with column descriptions, Python load snippets, first-5-row
  samples, and join instructions against the amrayn corpus.

## Surprises / notes for future runs

1. **The Leeds download gate is trivial to script.** The "email verification" is
   literally an echo — the server just copies whatever you sent as `txtEmail` into
   a JS variable that then gets POSTed back as `validEmail`. Two curl calls do it.
   But you *do* need session cookies between the two POSTs.

2. **Treebank/ontology are genuinely unavailable as downloads.** Don't waste time on
   this in future runs. If a research task needs either, the options are: scrape per-verse
   pages off corpus.quran.com, find an unofficial mirror on GitHub (several partial
   dumps exist), or contact the Leeds group.

3. **The morphology corpus and Tanzil Uthmani share a base text** — confirmed by the
   second copyright block inside `quranic-corpus-morphology-0.4.txt` which cites Tanzil
   Uthmani v1.0.2. This is excellent news for joining: no verse-boundary reconciliation
   needed.

4. **Per-verse counts are a clean integrity check.** If any file claims !=6236 verses
   or disagrees with `hafs-verse-counts.tsv` even once, something got "cleaned" or
   truncated. Add the assertion in INTEGRATION.md to any analysis pipeline.

5. **Buckwalter vs Arabic.** The morphology file is pure ASCII (Buckwalter). If an
   analysis wants to compare roots against the amrayn Arabic text, a Buckwalter→Arabic
   map is needed. Kais Dukes's table is published at
   `https://corpus.quran.com/java/transliteration.jsp` — worth caching in a future run.

6. **amrayn `quran-flat-no-tashkeel.txt` vs Tanzil `quran-simple-clean-txt-2.txt`**
   should be near-identical modulo indexing (amrayn is one massive flat stream without
   verse boundaries; Tanzil is one line per verse). A useful cross-validation exercise
   for the next agent.

## Files acquired (14 total, ~20 MB on disk)

```
data/SOURCES.md
data/INTEGRATION.md
data/hafs-verse-counts.tsv                            751 B
data/morphology/quranic-corpus-morphology-0.4.zip   1,028,754 B
data/morphology/quranic-corpus-morphology-0.4.txt   6,309,503 B
data/alt-text/quran-uthmani-txt.txt                 1,347,874 B
data/alt-text/quran-uthmani-txt-2.txt               1,384,015 B
data/alt-text/quran-uthmani-min-txt.txt             1,149,812 B
data/alt-text/quran-uthmani-min-txt-2.txt           1,185,953 B
data/alt-text/quran-simple-txt.txt                  1,315,086 B
data/alt-text/quran-simple-txt-2.txt                1,351,227 B
data/alt-text/quran-simple-min-txt.txt              1,144,216 B
data/alt-text/quran-simple-min-txt-2.txt            1,180,357 B
data/alt-text/quran-simple-clean-txt.txt              758,172 B
data/alt-text/quran-simple-clean-txt-2.txt            794,313 B
data/translations/en.sahih.txt                        861,908 B
data/translations/en.sahih.txt-2.txt                  898,049 B
```

## Status

Run complete. All required datasets downloaded except treebank and ontology (not
distributed). Documentation in place. Ready for handoff.
