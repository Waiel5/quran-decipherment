---
title: Vocalised ḥadīth corpus — source manifest
author: Waiel Al-Shujaa
date_acquired: 2026-04-28
date_documented: 2026-08-07
status: on disk, committed; the only fully vocalised Classical Arabic prose in this repository
used_by: H-NEW-2890
---

# Vocalised ḥadīth corpus — source manifest

**Why this file exists.** H-NEW-2870 §6.2 and H-NEW-2880 §5.2 both reported the pausal-rhyme
negative control as **NOT COMPUTABLE**, on the ground that no vocalised Arabic prose existed on
disk. **That was wrong, and the error was one of census scope, not of data.** Both censuses
enumerated `data/baseline-corpora/` only. This corpus — fully vocalised, 50,884 reports across
nine canonical books — has been in `data/literature/hadith/` since 2026-04-28. It is documented
here so no future test repeats the mistake.

The prose baselines in `data/baseline-corpora/` remain genuinely unvocalised and remain unusable
for any test needing the citation (waṣl) form: `bukhari-noquran.txt` carries **0** ḥarakāt over
2,056,880 Arabic characters, `jahiz-hayawan.txt` **0** over 1,422,374, `sira-ibn-hisham.txt`
**0** over 1,090,188. **This corpus is a different edition of overlapping works, not the same
files re-read.**

## Source

- Dataset: `AhmedBaset/hadith-json` — a JSON database of 50,884 ḥadīth in Arabic and English.
- Upstream: <https://github.com/AhmedBaset/hadith-json>
- Provenance stated by the dataset's own README: scraped from <https://sunnah.com/>, covering
  17 canonical collections.
- Local path: `data/literature/hadith/ahmedbaset-json/`
- Layouts: `db/by_book/` (one file per book) and `db/by_chapter/` (one file per chapter).
- Record schema: `{id, idInBook, chapterId, bookId, arabic, english:{narrator, text}}`.
- **Licence: not stated in the acquired snapshot.** The upstream repository carries no licence
  file in the copy on disk, and none is asserted here. The underlying texts are classical works
  long in the public domain; the *compilation* is third-party. **Treat as
  research-use-only, and do not redistribute the JSON.** Verify the upstream licence before any
  use beyond internal analysis.
- Upstream caveat carried over: Musnad Aḥmad chapters 8–30 are missing from the source data.

## Files and SHA-256 — `db/by_book/the_9_books/`

| file | work | bytes | SHA-256 |
|:--|:--|--:|:--|
| `bukhari.json` | Ṣaḥīḥ al-Bukhārī | 12,751,095 | `9d2e4194786c275f64f627c834711ea0e339a8fe226d5e9569ef962595a562f1` |
| `muslim.json` | Ṣaḥīḥ Muslim | 11,453,925 | `12e3cbe8e2c83acc787b3e1e644877eff0feab11f1b32493386c60703d9076ae` |
| `nasai.json` | Sunan al-Nasāʾī | 7,886,743 | `d32d122202ab17af5f12b91b2b3737b1e208d9feff3e92effd027f10da56befe` |
| `abudawud.json` | Sunan Abī Dāwūd | 7,876,864 | `da55afe7f372a803f4c484da2982c440c62a8b3d891d3cc50a687606a56b9884` |
| `tirmidhi.json` | Jāmiʿ al-Tirmidhī | 7,660,980 | `9ba6da92af6b0db9768c67f4c562c24bbbdb7be83509a78c40994c6d93366437` |
| `ibnmajah.json` | Sunan Ibn Mājah | 5,723,666 | `6c5d2abcabb0c880ae09cb3f03f1f716c166a14b89d5243bc04ad65e1023119d` |
| `malik.json` | Muwaṭṭaʾ Mālik | 3,266,633 | `a926eb6395a391c2b7a571cceef8bc058a9d06960a2135f37964a18dc5348ef8` |
| `darimi.json` | Sunan al-Dārimī | 3,054,859 | `45ec3ac92b072287e6c7451084f55f50a2676e0eab2ec165c4ffecfa57f41d2a` |
| `ahmed.json` | Musnad Aḥmad (partial) | 2,377,018 | `d889aedc76563439a230d0b557d2059b29de169ed310a064a92638dc84566d32` |

## Vocalisation — measured, not assumed

Measured 2026-08-07 on the `arabic` field of every record. **Density alone is not the operative
screen**; what a citation-vs-pausal test needs is that the *unit-final* word carry its case
vowel, so the unit-final mark census is given beside it. The Qurʾān is on the same row basis.

| text | units | words | Arabic chars | ḥarakāt / char | **unit-final vocalised** | mean unit length |
|:--|--:|--:|--:|--:|--:|--:|
| al-Bukhārī | 7,277 | 532,876 | 2,031,955 | **0.7702** | **0.9426** | 73.2 |
| Muslim | 7,459 | 481,905 | 1,860,463 | 0.7965 | 0.9405 | 64.6 |
| Abū Dāwūd | 5,276 | 332,995 | 1,276,978 | 0.7962 | 0.9505 | 63.1 |
| al-Tirmidhī | 4,053 | 369,293 | 1,400,469 | 0.7954 | **0.9887** | 91.1 |
| al-Nasāʾī | 5,768 | 340,547 | 1,303,302 | 0.7883 | 0.9511 | 59.0 |
| Ibn Mājah | 4,345 | 253,973 | 938,815 | 0.7911 | 0.9484 | 58.5 |
| Mālik | 1,860 | 117,204 | 443,249 | 0.8201 | 0.9457 | 63.0 |
| Aḥmad (partial) | 1,374 | 101,139 | 385,078 | 0.8829 | 0.9512 | 73.6 |
| al-Dārimī | 3,406 | 167,449 | 644,575 | 0.8659 | 0.9445 | 49.2 |
| **Qurʾān** (reference) | 6,236 | 77,429 | 313,555 | **0.7801** | **0.9843** | 12.4 |

**al-Bukhārī's ḥarakāt density, 0.7702, is essentially the Qurʾān's own 0.7801.** All nine books
clear the ≥ 0.90 unit-final vocalisation threshold that H-NEW-2870 §6.4 pre-declared for its
poetry arm.

Two limits of the vocalisation, both measured:

- The honorific formulae are written **unvocalised** in this edition (`صلى الله عليه وسلم`,
  `رضى الله عنها`). 3.6 % of al-Bukhārī's reports end on `وسلم`, which carries no case vowel.
- Unit-final sukūn — a genuinely unrecoverable ending — is 5.7 % in al-Bukhārī against 1.6 % in
  the Qurʾān.

## Qurʾānic contamination — measured

Ḥadīth quotes the Qurʾān, so any use as a control against the Qurʾān must strip it. Share of
reports containing at least one Qurʾānic word n-gram, on the unvocalised skeleton:

| text | trigram | 5-gram |
|:--|--:|--:|
| al-Bukhārī | 22.5 % | 4.0 % |
| Muslim | 17.8 % | 3.1 % |

The repository's existing convention (`data/baseline-corpora/strip_quran_quotes.py`, documented
at `data/SOURCES.md` §5.6) is **word-trigram** overlap, which its own note describes as
over-removing.

## Reproducing the acquisition

The corpus is already committed. To re-fetch from upstream, pin a tag rather than `main` — the
dataset's README warns the format may change:

```bash
curl -L 'https://raw.githubusercontent.com/AhmedBaset/hadith-json/v1.2.0/db/by_book/the_9_books/bukhari.json' \
  -o bukhari.json
shasum -a 256 bukhari.json
```

*Bismillāhi al-Raḥmāni al-Raḥīm.*
