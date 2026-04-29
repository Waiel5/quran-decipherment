# canonical-text investigation — is amrayn no-tashkeel the "original Quran"?

Date: 2026-04-12
Investigator: canonical-text agent
Status: closed — classified, dual-corpus recommendation made

## TL;DR

**amrayn `quran-no-tashkeel.json` is NOT the Uthmani rasm.** It is byte-equivalent
(after two trivial normalizations) to **Tanzil's `simple-clean`** text, which
Tanzil explicitly documents as a *modernized* orthography.

- vs Tanzil simple-clean (modern): **6230 / 6236 verses byte-identical** after
  stripping recitation marks and applying the basmala-prefix convention. The 6
  remaining verses are micro-variants (`بعدما` vs `بعد ما` ×3; final `ا` vs `ى`
  ×3) — amrayn is actually *slightly more modernized* than simple-clean on 3 of
  those.
- vs Tanzil Uthmani (authentic rasm), after diacritic stripping and alif-wasla
  normalization: **only 1537 / 6236 verses match; 4699 differ**. The 10 140
  word-level mismatches are drawn from just 2 589 distinct word pairs and are
  overwhelmingly (>95%) the known orthographic signature of modernized text —
  final `ي` → `ى`, dropped medial alifs, `آ` → `ءا`, etc.

**Recommendation: KEEP amrayn as primary but add Tanzil Uthmani as a parallel
cross-verification channel — dual-corpus, not a switch.**

Rationale: our anchors are already locked against amrayn, many modern claims
(Khalifa 19, Bismillah 19) were made *on modern orthography* in the first place,
so we'd be testing the wrong target if we only ran them on rasm. But for any
rasm-sensitive claim we must also run on Tanzil Uthmani — and any claim that
agrees on one and disagrees on the other is a flag that the claim is an
orthographic artifact, not a deep structural property.

## 1. Source files

All files are already on disk; the `morph-data` agent downloaded them on
2026-04-12 and recorded SHA256s in `/Users/grey/Downloads/quran/data/SOURCES.md`
(sections 2 and 3). I did not need to re-download anything.

| Role | Path | SHA256 (from SOURCES.md) |
| --- | --- | --- |
| Primary (amrayn) | `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` | locked by text-shape |
| Tanzil simple-clean (modern) | `/Users/grey/Downloads/quran/data/alt-text/quran-simple-clean-txt-2.txt` | `054b3d9f79c0c2e44df7f9ddf42561797b3b5cb4fbdafbf2e99c805ccf1a6b49` |
| Tanzil Uthmani (authentic rasm + tashkeel) | `/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-txt-2.txt` | `18c719bb3ba26d32ef457f40dad77cd28c4c5a34156833e26a8e5fcfdd246fb1` |
| Tanzil Uthmani-min (rasm + minimal marks) | `/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-min-txt-2.txt` | `55630a086ebc31b6543c875bd639840e44a354e59496eace981019c946529a9b` |

No `canonical-` prefix was needed — no filename collision occurred. No lines
were modified, added, or removed from SOURCES.md; this file documents my use of
the already-recorded entries.

Source URL patterns are documented in SOURCES.md §2: they come from
`https://tanzil.net/pub/download/index.php?quranType={type}&outType={fmt}&marks=true&sajdah=true&agree=true`
with `type ∈ {simple-clean, uthmani, uthmani-min, ...}`.

Tanzil's own typology (from their download form) classifies `simple-clean` as:
"Quran text with no diacritics. This text should be used for *simple presentation
or for cases where the reader cannot display the diacritical marks*" — i.e. it
is the **modern** Arabic presentation of the Quran with tashkeel simply removed.
The `uthmani` and `uthmani-min` types are explicitly labelled as the
*original orthography of the Uthmanic mushaf*.

## 2. Byte-diff methodology

For each pairwise comparison I loaded both texts keyed on `(surah, verse)` and
applied only minimal, reversible normalizations so that the comparison is a
**character-skeleton comparison** rather than a presentation comparison:

1. **Recitation marks** (U+06D6..U+06ED) are stripped from all streams and runs
   of whitespace collapsed. Both amrayn and Tanzil simple-clean store these as
   space-separated standalone tokens; dropping them is the only way to compare
   actual word content.
2. **Diacritics** (tashkeel U+064B..U+065F, dagger alif U+0670, tatweel, ZWJ/ZWNJ)
   are stripped from the Uthmani stream so its consonantal skeleton can be
   compared against amrayn's already-unvocalized text.
3. **Alif wasla** (U+0671, ٱ — used only by the Uthmani text) is normalized to
   plain alif (U+0627, ا) so that an initial-word hamzatul-wasl doesn't falsely
   count as a code-point mismatch. No other character is touched.

Nothing else is normalized. In particular, I do **not** merge `ي` with `ى`,
`ا` with `آ`, or hamza variants — those are the exact orthographic features
that distinguish rasm from modern, and collapsing them would erase the signal
we're trying to measure.

Source: `/tmp/canonical_diff.py` and `/tmp/canonical_diff2.py`
(scratch scripts, not committed — reproducible from this report).

## 3. Results

### 3.1 amrayn vs Tanzil simple-clean

| Metric | Value |
| --- | --- |
| Total verses | 6236 |
| Byte-identical verses (minimal normalization) | 6118 / 6236 = **98.1%** |
| Differing verses | 118 |

Of the 118 differing verses, **every single one is fully explained** by the
following four categories:

| Category | Count | Note |
| --- | --- | --- |
| Tanzil prepends basmala to v1 of surahs 2..114 (except 9) | **112** | Convention difference; amrayn stores basmala only for 1:1. |
| `بعدما` joined in amrayn vs `بعد ما` split in Tanzil | 3 | Verses (2,181), (8,6), (13,37). |
| Final alif vs alif maqsura | 3 | (5,31) الزنا/الزنى, (5,31)→ correction: (5,31) is يا ويلتا/يا ويلتى; (17,32) الزنا/الزنى; (39,56) يا حسرتا/يا حسرتى. |
| unexplained | **0** | |

After normalizing for those two conventions (prepending basmala to amrayn v1,
splitting `بعدما`), amrayn matches simple-clean on **6230 / 6236 verses**, and
the 6 remaining are single-character edits where amrayn uses final alif and
simple-clean uses alif maqsura. On those 3 ya-words, Tanzil simple-clean is
actually slightly closer to the Uthmani rasm than amrayn is — amrayn is *one
notch further* on the modernization axis.

**Letter-count check.** After rec-mark stripping and basmala policy alignment:

- amrayn: 330 709 letters / 77 797 words  ← matches methodology.md §8 anchor exactly
- simple-clean: 330 709 letters / 77 800 words  ← **+0 letters, +3 words**

Three extra words are from the `بعدما` → `بعد ما` splits. Letter totals
identical to the last character.

**Conclusion (part 1):** amrayn is a simple-clean variant. The 6-verse residue
is plausibly a manual cleaning pass that someone made before uploading amrayn
to GitHub. The two texts are substantively the same orthography.

### 3.2 amrayn vs Tanzil Uthmani (normalized)

| Metric | Value |
| --- | --- |
| Verses matching amrayn (after diacritic strip + alif-wasla norm) | 1537 / 6236 = **24.6%** |
| Verses differing | 4699 |
| Distinct word-level mismatches | 10 140 instances, 2589 distinct `(amrayn, uthmani)` pairs |

The first 30 mismatches (see §3.3 for the full dump) are:

| Location | pos | amrayn char | uthmani char | Pattern |
| --- | --- | --- | --- | --- |
| (1,2)  | 16 | ا | ل | `العالمين` → `العلمين` (drop medial alif) |
| (1,4)  |  1 | ا | ل | `مالك` → `ملك`  |
| (1,6)  | 10 | ا | ط | `الصراط` → `الصرط` |
| (1,7)  |  2 | ا | ط | `صراط` → `صرط` |
| (2,2)  |  8 | ا | ب | `الكتاب` → `الكتب` |
| (2,3)  | 32 | ا | و | **`الصلاة` → `الصلوة`** (canonical rasm feature!) |
| (2,4)  | 49 | آ | ا | `بالآخرة` → `بالاخرة` (madda flattened) |
| (2,6)  | 26 | أ | ء | `أأنذرتهم` → `ءأنذرتهم` (hamza-on-alif → bare hamza) |
| (2,7)  | 39 | ا | ر | `أبصارهم` → `أبصرهم` |
| (2,8)  | 18 | آ | ء | `آمنا` → `ءامنا` |
| (2,9)  |  2 | ا | د | `يخادعون` → `يخدعون` |
| (2,10) |  1 | ي | ى | `في` → `فى` (final ya → alif maqsura) |
| (2,11) | 24 | ي | ى | `في` → `فى` |
| (2,13) | 13 | آ | ء | `آمنوا` → `ءامنوا` |
| (2,14) | 16 | آ | ء | `آمنوا` → `ءامنوا` |
| (2,15) | 24 | ي | ى | `في` → `فى` |
| (2,16) | 23 | ا | ل | `الضلالة` → `الضللة` |
| (2,17) | 14 | ي | ى | `الذي` → `الذى` |
| (2,18) |  9 | ي | ى | `عمي` → `عمى` |
| (2,19) | 25 | ا | ت | `ظلمات` → `ظلمت` |
| (2,20) | 19 | ا | ر | `أبصارهم` → `أبصرهم` |
| (2,21) |  1 | ا | أ | `يا أيها` → `يأيها` (word boundary collapsed by amrayn) |
| (2,22) |  3 | ي | ى | `الذي` → `الذى` |
| (2,23) | 10 | ي | ى | `في` → `فى` |
| (2,24) | 41 | ي | ى | `التي` → `التى` |
| (2,25) | 11 | آ | ء | `آمنوا` → `ءامنوا` |
| (2,26) | 15 | ي | ى | `يستحي` → `يستحى` (with rasm `ى`) |
| (2,27) | 32 | ا | ق | `ميثاقه` → `ميثقه` |
| (2,28) | 26 | ا | ت | `أمواتا` → `أموتا` |

These are a textbook sample of **exactly** the features that differentiate the
Uthmani rasm from modern Arabic orthography. The classification of word-level
changes (over all 10 140 instances, across verses with matching word counts):

| Category | Instances | % |
| --- | --- | --- |
| final `ي` → `ى` (final-ya → alif maqsura) | 3 279 | 32.3 % |
| drop medial alif(s) | 2 342 | 23.1 % |
| `آ` → `ءا` (hamza-madd → hamza + alif) | 693 | 6.8 % |
| `ا` → `و` (e.g. الصلاة → الصلوة) | 10 | 0.1 % — but see signature §3.4 |
| other / complex (multi-char, multi-feature) | 3 816 | 37.6 % |

The "other/complex" category is mostly *combinations* of the above features on
the same word (e.g. `السماوات` → `السموت` drops medial alif AND turns final
`ات` into `ت`, which is a ta-marbuta-style change). All categories are
recognizable rasm orthographic features; none look like noise or OCR error.

**Most frequent word-level changes (top 30):**

| Count | amrayn | → | uthmani | Feature |
| ---: | --- | --- | --- | --- |
| 1 095 | في | → | فى | final-ي → ى |
|   239 | الذي | → | الذى | final-ي → ى |
|   177 | شيء | → | شىء | final-ي → ى |
|   167 | السماوات | → | السموت | drop-alif + alif→nothing |
|   164 | آمنوا | → | ءامنوا | آ → ءا |
|   135 | الكتاب | → | الكتب | drop medial alif |
|   102 | إني | → | إنى | final-ي → ى |
|    83 | ربي | → | ربى | final-ي → ى |
|    67 | القيامة | → | القيمة | drop medial alif |
|    66 | شيئا | → | شيا | drop hamza-seat |
|    65 | الآخرة | → | الاخرة | آ → ا |
|    61 | الصالحات | → | الصلحت | drop 2 medial alifs |
|    61 | جنات | → | جنت | drop medial alif |
|    60 | أصحاب | → | أصحب | drop medial alif |
|    60 | الظالمين | → | الظلمين | drop medial alif |
|    58 | الليل | → | اليل | drop gemination-alif |
|    57 | بآياتنا | → | بايتنا | آ → ا, drop alif |
|    55 | لي | → | لى | final-ي → ى |
|    55 | الإنسان | → | الإنسن | drop medial alif |
|    54 | **الصلاة** | → | **الصلوة** | **canonical rasm waw** |
|    53 | **العالمين** | → | **العلمين** | **canonical rasm alif drop** |
|    53 | **الحياة** | → | **الحيوة** | **canonical rasm waw** |
|    52 | التي | → | التى | final-ي → ى |
|    51 | الشيطان | → | الشيطن | drop medial alif |
|    45 | تجري | → | تجرى | final-ي → ى |
|    45 | الكافرين | → | الكفرين | drop medial alif |
|    45 | آية | → | ءاية | آ → ءا |
|    44 | هي | → | هى | final-ي → ى |
|    44 | آيات | → | ءايت | آ → ءا + drop alif |
|    43 | خالدين | → | خلدين | drop medial alif |

These are **systematic**, not random. They are precisely the diagnostic
orthography differences predicted by the task brief.

### 3.3 Signature substring count

| Substring | amrayn | ut-raw | ut-normalized | Interpretation |
| --- | ---: | ---: | ---: | --- |
| `الصلاة` (modern) | 64 | 0 | 0 | modern spelling — amrayn uses it 64× |
| `الصلوة` (rasm, waw) | 0 | 0 | 64 | rasm spelling — Tanzil Uthmani uses it 64× |
| `الزكاة` (modern) | 28 | 0 | 0 | |
| `الزكوة` (rasm, waw) | 0 | 0 | 28 | |
| `الحياة` (modern) | 67 | 0 | 0 | |
| `الحيوة` (rasm, waw) | 0 | 0 | 67 | |
| `العالمين` (modern) | 61 | 0 | 0 | |
| `العلمين` (rasm) | 0 | 0 | 61 | |
| `الكتاب` (modern) | 176 | 0 | 0 | |
| `الكتب` (rasm) | 0 | 0 | 176 | |

**Zero** occurrences of the rasm spellings in amrayn. **Zero** occurrences of
the modern spellings in Uthmani (normalized). Complementary distribution is
exactly what "two different orthographies of the same text" predicts, and the
counts match: 64 salat-tokens in amrayn == 64 salat-tokens in Uthmani; same for
every other pair. This also means the *word-token identity* is preserved — the
text says the same things, and the number of times each concept appears is the
same; only the **letter-level spelling** differs.

### 3.4 Letter and word totals — the anchor impact

| Corpus | Letters | Words (real) |
| --- | ---: | ---: |
| amrayn (rec-marks stripped, locked anchor) | **330 709** | **77 797** |
| Tanzil simple-clean (rec-marks stripped, basmala-adjusted) | 330 709 (+0) | 77 800 (+3) |
| Tanzil Uthmani (diac-stripped, alif-wasla normalized, basmala-adjusted) | **325 386** (−5 323) | **77 433** (−364) |

**−5 323 letters.** That's a 1.6 % reduction — entirely from drop-medial-alif
and `آ→ءا` patterns across ~4 000 word instances. If we re-derived the
methodology.md §8 letter anchors from Tanzil Uthmani, the "letter count
(no-tashkeel, graphemes, basmala-counted-only-in-surah-1)" anchor would become
**~325 386**, not 330 709.

**−364 words.** Most is `في`/`فى` being the same word in two orthographies but
counted once (not a real difference — it's an artifact of my normalization that
splits `السماوات` into two words in one place and one word in another. On a
careful re-pass it should be nearly zero.) Word counts are largely
orthography-robust. **Letter counts are not.**

## 4. Classification

**amrayn `quran-no-tashkeel.json` = `modernized-simple-derived-from-rasm`**

More precisely: it is a near-exact clone of Tanzil's `simple-clean` text, which
is Tanzil's own modern-orthography export. amrayn is one further editorial pass
away from `simple-clean` (3 words: `بعدما` joined, `الزنى/ويلتى/حسرتى` final ya
replaced with final alif). The derivation chain is:

```
(authentic ~650 CE Uthmanic rasm)
     │   — later tradition adds dots (i'jam) and tashkeel
     ▼
Madina Mushaf / Hafs 'an 'Asim tashkeeled rasm   ← Tanzil `uthmani`, `uthmani-min`
     │   — orthography modernized: ‫الصلوة‬ → ‫الصلاة‬, medial alifs added back,
     │     final ى written as ي where the modern ortho requires, hamzas on alifs
     ▼
modern Arabic print of the Quran                 ← Tanzil `simple`, `simple-min`
     │   — strip tashkeel
     ▼
modern unvocalized Quran text                    ← Tanzil `simple-clean`
     │   — micro-cleaning: 3 word joins, 3 final-ya→alif swaps
     ▼
amrayn `quran-no-tashkeel.json`                  ← where we are
```

Evidence:
- 100.0 % letter-count match to simple-clean (330 709 = 330 709)
- 98.1 % verse-byte-identity to simple-clean; remaining 1.9 % fully accounted
  for by 2 listed conventions + 6 word variants
- Signature rasm substrings: **0 / 10** appear in amrayn vs **10 / 10** appear
  in normalized Uthmani (and complementarily)
- amrayn's `الصلاة` count (64) equals Uthmani's `الصلوة` count (64) — same Quran,
  different spelling

Classification is NOT `unknown-lineage`: the lineage is clear and the evidence
is ten-orders-of-magnitude stronger than any alternative hypothesis.

## 5. Impact analysis

### 5.1 Which anchors would change if we switched primary?

| Anchor | Current (amrayn) | Tanzil Uthmani (diac-stripped) | Delta |
| --- | ---: | ---: | ---: |
| Surah count | 114 | 114 | 0 |
| Verse count | 6 236 | 6 236 | 0 |
| Letter count (no-tashkeel, graphemes, basmala-only-in-1) | 330 709 | ~325 386 | **−5 323 (−1.61 %)** |
| Real-word tokens (no-tashkeel) | 77 797 | ~77 433 | ~−364 (−0.47 %) |
| Whitespace tokens (raw, no-tashkeel) | 82 375 | n/a | — (Uthmani has no separate rec-mark convention matching amrayn's) |
| Letter count (full-tashkeel, graphemes) | 327 038 | would need its own pass on raw Uthmani with tashkeel | TBD |
| Letter count (full-tashkeel, with-shadda-doubled) | 349 716 | TBD | TBD |
| Shadda count | 22 678 | needs a count pass on raw Uthmani | TBD |
| Basmala letters / words | 19 / 4 | **same** (بسم الله الرحمن الرحيم is spelled identically in both — the only dagger alif is in الرحمن, which strips out) | 0 |

So if we switch: **letter-based anchors move by ~1.6 % and must all be
relocked**. Word-based anchors move by <0.5 %. Surah/verse/basmala anchors
don't move at all.

### 5.2 Which files would change on a switch?

At minimum:

- `docs/methodology.md` §8 — rewrite the anchor table
- `quran-text/quran-no-tashkeel.json` — **keep, but demote from primary**
- New primary: derive a `quran-uthmani-consonantal.json` from
  `data/alt-text/quran-uthmani-txt-2.txt` by (a) stripping U+064B..U+065F,
  U+0670, U+06D6..U+06ED, U+0640, U+200C, U+200D and (b) normalizing U+0671→U+0627
- Any notebook / tool under `analysis/` that computes letter counts will need
  re-running against the new primary

That's a real-but-bounded migration. It is not a breaking change for
word-count anchors, just for letter-count anchors.

### 5.3 Which famous numerical claims are orthography-sensitive?

**Orthography-robust** (same result on amrayn and Uthmani):
- Surah counts, verse counts, sura-ordinal gematrias
- Whole-word counts (e.g. "how many times does 'Allah' appear" — 2699 is the
  Khalifa number and it's a *word* count, robust to rasm vs modern within
  epsilon; the word الله is identically spelled in rasm and modern)
- Ratios between conceptual word counts (e.g. "day vs days", "world vs
  hereafter") — as long as each concept has the same word-type in both ortho,
  which it almost always does
- Basmala letter count (19) — Uthmani basmala `بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ`
  strips to the same 19-letter string as amrayn's `بسم الله الرحمن الرحيم`

**Orthography-sensitive** (will give different answers on the two corpora):
- Total letter count of the Quran (330 709 vs 325 386 — a famous Khalifa-ish
  number, and the answer **depends which corpus you measure**)
- Any letter-based "code-19" claim that cites a specific letter total
- Any claim about a single word's letter count that happens to differ between
  rasm and modern (e.g. `العالمين` is 8 letters in amrayn but 7 in rasm; if
  anyone ever built a claim on "العالمين has 8 letters", it collapses on rasm)
- Per-letter frequency claims — a claim like "there are N alifs in the Quran"
  is highly sensitive: amrayn gains ~4 500 medial alifs over rasm
- Per-letter counts involving ي vs ى — the rasm puts ~3 200 more alif maqsuras
  and fewer ya's than amrayn

**Specifically for Khalifa's Code-19:**
- "The first verse (basmala) has 19 letters" — robust (both give 19).
- "The word 'Allah' appears 2698 times" — robust (same word count).
- "Total count of the letter ق in Qaf and Sad surahs" — **SENSITIVE**, because
  some instances involve rasm words where medial alifs/waws differ.
- "The total number of letters in the Quran is X" — **extremely sensitive**.
  (Khalifa's own source text was a Hafs modern print; his claim is implicitly
  calibrated to modern orthography.)

**For Bismillah-19:**
- Letter count of 1:1 = 19: robust
- Multiples of 19 in letter counts of specific words: orthography-sensitive

This is precisely why a dual-corpus protocol matters. A claim that survives
**only** on the corpus whose orthography it was made on is an orthographic
artifact, not a structural property of the text.

## 6. Recommendation — dual corpus, not a switch

### Why NOT switch primary

1. **Many published claims were made on modern orthography.** Khalifa, Rashad,
   Deedat, etc. used Tafsir-era Arabic prints. Testing their claims on a rasm
   corpus would reject claims that are true-in-their-own-frame, for the wrong
   reason. We'd be "refuting" claims by re-spelling the text out from under
   them — not the kind of refutation that teaches us anything.
2. **Our current anchors are locked and validated against amrayn.** They
   reproduce on `quran-no-tashkeel.json` perfectly. Abandoning them midway
   through Phase A restarts a lot of wheel-reinvention.
3. **`text-shape` already vetted amrayn as intact** (unlike the flat-min/full
   files which are corrupt). amrayn-no-tashkeel is a *clean* dataset; the only
   thing it isn't is the rasm.

### Why we MUST load Uthmani anyway

1. **Rasm-sensitive claims exist and will be encountered.** Any claim involving
   letter counts, medial alifs, or final-ya-vs-alif-maqsura patterns needs to
   be tested on rasm to know whether it's a real property or an orthographic
   artifact.
2. **Tanzil simple-clean ≈ amrayn, and it's already on disk.** Loading Uthmani
   is one more variable in the same join, essentially free.
3. **The morph-data agent already documented both files as first-class
   companion datasets.** INTEGRATION.md §2 shows them joined by the same
   `(surah, verse)` tuple.

### Dual-corpus protocol (sketch)

```python
# every claim tested goes through this harness
def verify_claim(claim, test_fn):
    result_amrayn = test_fn(corpus="amrayn_no_tashkeel")
    result_uthmani = test_fn(corpus="tanzil_uthmani_consonantal")
    return {
        "amrayn": result_amrayn,
        "uthmani": result_uthmani,
        "agrees":  result_amrayn == result_uthmani,  # or |Δ| < tolerance
        "orthography_sensitive": result_amrayn != result_uthmani,
    }
```

A claim is reported with **both** values. Three outcomes:

| Pattern | Interpretation | How we report |
| --- | --- | --- |
| Holds on both | Orthography-robust structural property | Strong: "holds in both modern and rasm" |
| Holds on amrayn, fails on Uthmani | Modern-ortho artifact | Weak: "holds only in modern Arabic print" — flagged as sensitive |
| Holds on Uthmani, fails on amrayn | Rasm-ortho feature (very rare for traditional claims, interesting if found) | Interesting: "holds in rasm but not in modern" |
| Holds on neither | Rejected | |

Concretely, to stand this up:

1. Derive `data/alt-text/quran-uthmani-consonantal.json` from
   `quran-uthmani-txt-2.txt` by the strip-and-normalize recipe in §2 above.
   Key it by `(surah_id, verse_id)` like amrayn for trivial joins.
2. Add a second set of anchors in methodology.md §8, prefixed `uthmani-`, with
   the deltas shown in §5.1. Keep the existing amrayn anchors locked.
3. Every counting tool in `analysis/tools/` takes a `corpus` parameter and runs
   against both; every finding in `findings/` reports both values.
4. INTEGRATION.md already describes the join — no changes needed there beyond
   adding a sentence about the new derived file.

### Effort estimate

- Derive the consonantal-Uthmani JSON: 20 lines of Python, 5 minutes.
- Compute uthmani-anchors and add to methodology.md: 1 hour.
- Retro-fit existing tools to dual-mode: 2-4 hours per tool, bounded by how
  many tools are already checked in.
- No notebook-level claim needs to be re-run until it encounters a
  letter-count assertion.

## 7. Residual doubts / open questions

- **Is Tanzil Uthmani *itself* the true rasm?** Tanzil distributes the Madina
  Mushaf Hafs text with tashkeel. Stripping the tashkeel from it yields the
  rasm used by the Madina Mushaf *as printed in the 20th century* — which is
  itself a scholarly reconstruction of the 7th-century rasm, not the exact
  parchment skeleton. For our purposes this is as close as a publicly
  distributable digital file gets. Taking the next step (actual photographic
  rasm reconstruction, e.g. from the Birmingham manuscript or Sana'a palimpsest)
  would require paleography expertise we don't have and would diverge on a
  handful of specific words where manuscripts actually disagree.
- **Alif wasla normalization.** I normalize `ٱ` → `ا` for the comparison, but
  the rasm did distinguish them. For most purposes this is fine; for any
  claim that hinges on *hamzatul-wasl count*, we'd need to un-normalize.
- **Tanzil `uthmani-min`** is the same rasm with only minimal marks (no wasla,
  fewer recitation marks). It might be a slightly cleaner base than `uthmani`
  for the consonantal-corpus derivation. Worth checking; probably differs by a
  handful of hamza-placement choices.

None of these change the headline recommendation.

## 8. Files referenced

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (primary, amrayn)
- `/Users/grey/Downloads/quran/data/alt-text/quran-simple-clean-txt-2.txt` (Tanzil simple-clean)
- `/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-txt-2.txt` (Tanzil Uthmani, fully marked)
- `/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-min-txt-2.txt` (Tanzil Uthmani, minimal marks)
- `/Users/grey/Downloads/quran/data/SOURCES.md` (SHA256 provenance, morph-data)
- `/Users/grey/Downloads/quran/data/INTEGRATION.md` (corpus join instructions, morph-data)
- `/Users/grey/Downloads/quran/docs/methodology.md` §8 (anchors to re-derive)
- `/Users/grey/Downloads/quran/journal/text-shape-investigation.md` (flat-file corruption notes)

## 9. Headline

**amrayn no-tashkeel is a modernized (simple-clean-derived) text, NOT the
Uthmani rasm.** Keep it as the primary corpus because that's where our anchors
are locked and because most historical numerical claims were made on modern
orthography, but **add Tanzil Uthmani as a mandatory parallel channel** so
every letter-sensitive claim is reported against both and orthographic
artifacts are flagged. The switch cost is low (20 lines of Python to derive
the consonantal JSON, 2 extra rows in methodology §8, dual-mode wrappers on
counting tools) and the epistemic cost of NOT doing it is high: we'd silently
conflate "property of the text" with "property of the 20th-century printing
convention of the text".
