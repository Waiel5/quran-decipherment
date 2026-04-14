# Companion Data — Integration Notes

Written 2026-04-12 by `morph-data-run-1`. Target reader: the next agent who needs to
join these companion datasets against the `amrayn` corpus at
`/Users/grey/Downloads/quran/quran-text/`.

## Canonical verse index (the glue)

Every file here keys on the Hafs (1..114, 1..Nₛ) surah/verse numbering. The amrayn
JSONs (`quran-*-tashkeel.json`) use the same scheme: surah `id` is 1-114, each verse has
a verse `id` within that surah starting at 1. **Confirmed:** per-surah verse counts in
`morphology/quranic-corpus-morphology-0.4.txt` match `hafs-verse-counts.tsv` exactly
(114 rows, sum = 6236). So any of these files can be joined on the tuple
`(surah_id, verse_id)` without remapping.

Basmala convention: In Tanzil Uthmani, Sahih translation, morphology corpus, and amrayn,
Surah 1 verse 1 *is* the Basmala. All other surahs' Basmalas are **not** given their own
verse row — they're prepended to the first verse's text where present (Surah 9 has none).
This matches Hafs and is consistent across every file in this drop.

## Encoding

- All text files are **UTF-8**, no BOM. Unix LF line endings.
- Morphology file is pure ASCII (Buckwalter transliteration).
- Tanzil `uthmani*` files contain combining marks and the **Arabic presentation forms**
  used in the Madina Mushaf. Expect combining characters above/below letters; iterate
  by grapheme cluster, not by `len(str)`, if you're measuring "letter counts".
- Tanzil `simple*` files use basic Arabic (no presentation forms). `simple-clean` has
  **no diacritics at all** — safest for grep/root matching.
- Tanzil files end with a `#`-prefixed license comment block. Strip with
  `awk '!/^#/ && NF' file` or simply filter lines matching `^\d+\|\d+\|`.

---

## 1. `morphology/quranic-corpus-morphology-0.4.txt`

Quranic Arabic Corpus v0.4 — every segment of every word tagged.

### Layout

- Lines 1-56: copyright / license block (start with `#`).
- Line 57: tab-separated header: `LOCATION\tFORM\tTAG\tFEATURES`
- Lines 58-128276: data rows. One row per **segment** (a word can decompose into
  multiple segments: prefixes, stem, suffixes).

### Columns

| Column | Description |
| --- | --- |
| `LOCATION` | `(surah:verse:word:segment)`, e.g. `(1:1:1:1)`. All 1-based. |
| `FORM` | The Buckwalter-transliterated Arabic surface form of the segment. |
| `TAG` | Coarse POS tag (N, V, P, PN, ADJ, DET, CONJ, PRON, ...). |
| `FEATURES` | Pipe-separated key:value bundle. Includes `PREFIX`/`STEM`/`SUFFIX` marker, `POS:<tag>`, `LEM:<lemma>`, `ROOT:<root>` (Buckwalter), gender (M/F), number (S/D/P), case (NOM/GEN/ACC), definiteness (DEF/INDEF), person, voice, mood, etc. Not all fields appear on every row — stems carry the most; affixes carry a marker only. |

### First 5 data rows
```
(1:1:1:1)	bi	P	PREFIX|bi+
(1:1:1:2)	somi	N	STEM|POS:N|LEM:{som|ROOT:smw|M|GEN
(1:1:2:1)	{ll~ahi	PN	STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN
(1:1:3:1)	{l	DET	PREFIX|Al+
(1:1:3:2)	r~aHoma`ni	ADJ	STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN
```

### How to load (Python)

```python
import re, csv
rows = []
pat = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
with open("morphology/quranic-corpus-morphology-0.4.txt", encoding="utf-8") as f:
    for ln in f:
        if ln.startswith("#") or ln.startswith("LOCATION") or not ln.strip():
            continue
        loc, form, tag, feats = ln.rstrip("\n").split("\t")
        m = pat.match(loc)
        s, v, w, seg = map(int, m.groups())
        feat = dict(kv.split(":", 1) if ":" in kv else (kv, True)
                    for kv in feats.split("|"))
        rows.append((s, v, w, seg, form, tag, feat))
```

Or in pandas: `pd.read_csv(..., sep="\t", skiprows=57)` then parse `LOCATION`
with `.str.extract(r"\((\d+):(\d+):(\d+):(\d+)\)")`.

### Joins

- `(s, v)` → any verse-level file (amrayn, Tanzil txt-2, Sahih).
- `(s, v, w)` → word-level agreement with amrayn text after word-tokenizing
  (amrayn separates on whitespace; word indices are 1-based and line up with the
  corpus's `w`).
- Buckwalter roots (`ROOT:smw` etc.) need a Buckwalter→Arabic map if you want to
  display them. Kais Dukes' transliteration table is at
  `https://corpus.quran.com/java/transliteration.jsp`.

### Row count

128,276 lines total; after dropping 56 comment lines + 1 header = **128,219 segment
rows** covering 77,430 word-tokens across 6,236 verses.

---

## 2. Tanzil text files — `alt-text/quran-*-txt*.txt`

One file per (quranType × outType) combination. Two variants per type:

- `*-txt.txt` — one verse per line, text only.
- `*-txt-2.txt` — one verse per line, prefixed with `surah|ayah|` (use this one).

### First 5 rows of `quran-uthmani-txt-2.txt`
```
1|1|بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1|2|ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
1|3|ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1|4|مَٰلِكِ يَوْمِ ٱلدِّينِ
1|5|إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
```

### First 5 rows of `quran-simple-clean-txt-2.txt` (root/grep friendly)
```
1|1|بسم الله الرحمن الرحيم
1|2|الحمد لله رب العالمين
1|3|الرحمن الرحيم
1|4|مالك يوم الدين
1|5|إياك نعبد وإياك نستعين
```

### How to load (Python)

```python
verses = {}
with open("alt-text/quran-uthmani-txt-2.txt", encoding="utf-8") as f:
    for ln in f:
        if ln.startswith("#") or "|" not in ln:
            continue
        s, v, text = ln.rstrip("\n").split("|", 2)
        verses[(int(s), int(v))] = text
assert len(verses) == 6236
```

Row count: 6,236 data lines + trailing license comment block in each file.

### Which variant to use for which task

| Task | File |
| --- | --- |
| Display / mushaf-accurate rendering | `quran-uthmani-txt-2.txt` |
| Compact Uthmani without pause marks | `quran-uthmani-min-txt-2.txt` |
| Root / lemma matching, grep | `quran-simple-clean-txt-2.txt` |
| Counting diacritics, comparing vowelling | `quran-simple-txt-2.txt` vs `quran-simple-min-txt-2.txt` |
| Alignment with morphology's Buckwalter forms | either Uthmani (Tanzil is the morphology corpus's own base text — see the copyright block embedded at the top of the morphology file) |

### Joining against amrayn

The amrayn `quran-*-tashkeel.json` files use the same (surah, verse) indices.
`quran-simple-clean-txt-2.txt` should be nearly identical (character-for-character
modulo whitespace) to amrayn `quran-flat-no-tashkeel.txt` — useful for cross-validation.

---

## 3. `hafs-verse-counts.tsv`

Two columns, tab-separated, no header.

### First 5 rows
```
1	7
2	286
3	200
4	176
5	120
```

### How to load

```python
counts = {}
with open("hafs-verse-counts.tsv") as f:
    for ln in f:
        s, c = ln.split()
        counts[int(s)] = int(c)
assert sum(counts.values()) == 6236
```

Every surah 1..114 present. Use it to validate that any other dataset you load covers
exactly the right number of verses per surah.

---

## 4. `translations/en.sahih.txt-2.txt`

Sahih International, one verse per line, `surah|ayah|english`.

### First 5 rows
```
1|1|In the name of Allah, the Entirely Merciful, the Especially Merciful.
1|2|[All] praise is [due] to Allah, Lord of the worlds -
1|3|The Entirely Merciful, the Especially Merciful,
1|4|Sovereign of the Day of Recompense.
1|5|It is You we worship and You we ask for help.
```

### How to load

Same pattern as the Tanzil txt-2 files:

```python
en = {}
with open("translations/en.sahih.txt-2.txt", encoding="utf-8") as f:
    for ln in f:
        if ln.startswith("#") or "|" not in ln:
            continue
        s, v, text = ln.rstrip("\n").split("|", 2)
        en[(int(s), int(v))] = text
assert len(en) == 6236
```

### Use it for

Cross-checking semantic claims *only*. Don't feed it to anything that counts letters or
roots. Bracketed clarifications like `[All] praise` are editorial additions by Sahih
International — keep them in place (no cleaning per brief).

---

## Cross-file sanity checks (run these any time you load the data)

```python
assert len(amrayn_verses) == 6236
assert len(tanzil_uthmani) == 6236
assert len(sahih) == 6236
assert max(s for s,_ in morph_rows) == 114
assert sum(counts.values()) == 6236
# per-surah verse counts should match hafs-verse-counts.tsv from every source
```

If any of these fails, something has been silently "cleaned" somewhere and the joins
will be off-by-one.
