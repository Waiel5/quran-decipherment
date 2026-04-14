# Companion Data Sources

All files acquired on **2026-04-12** by `morph-data-run-1` agent.
Preserved as downloaded (no reformatting, no re-encoding). Raw bytes on disk.

## 1. Quranic Arabic Corpus (Kais Dukes, Leeds)

Gold-standard morphological annotation of the Quran. Version 0.4 (2011-05-02).
Site: https://corpus.quran.com/

### `morphology/quranic-corpus-morphology-0.4.zip`
- **Source URL:** `https://corpus.quran.com/download/default.jsp`
  (POST form with `txtEmail` + `downloadID=3` + `validEmail`)
- **License:** GNU General Public License (see copyright block at top of .txt)
- **Date acquired:** 2026-04-12
- **Size:** 1,028,754 bytes (advertised "1,005 KB" on download page — match)
- **SHA256:** `fda26f87cc58b42fc992a3ad666a562805b636f34bcecb46326d048337ca7999`

### `morphology/quranic-corpus-morphology-0.4.txt` (extracted)
- Extracted from the zip above (single-file archive).
- **Original mtime from zip:** 2011-05-02 01:38 UTC
- **Size:** 6,309,503 bytes (128,276 lines; 57 lines of header, then 1 column header, then 128,218 data rows)
- **SHA256:** `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`
- **Encoding:** ASCII (Buckwalter-transliterated Arabic in `FORM` and `FEATURES` columns).
  No BOM. Unix line endings.

### Treebank / Ontology — NOT OBTAINED
- `https://corpus.quran.com/treebank.jsp` is a browser-only viewer, not a bulk download.
- `https://corpus.quran.com/ontology.jsp` likewise.
- Version 0.4 release notes list only one downloadable file (morphology). No treebank or
  ontology export is offered. Noted and moved on per instructions.

## 2. Tanzil Quran Text (tanzil.net)

All Tanzil files include Creative Commons BY-ND 3.0 Unported terms in their trailing comment
block. Text type selection matches Tanzil's own typology.
Site: https://tanzil.net/download/

Download URL pattern (discovered from the form on `/download/`):
```
https://tanzil.net/pub/download/index.php?quranType={type}&outType={fmt}&marks=true&sajdah=true&agree=true
```
where `type ∈ {simple, simple-plain, simple-min, simple-clean, uthmani, uthmani-min}`
and `fmt ∈ {txt, txt-2, xml, sql}`. `txt-2` = one line per verse prefixed with
`surah|ayah|`; `txt` = text-only one line per verse.

Downloaded pairs (txt and txt-2) for: simple, simple-min, simple-clean, uthmani, uthmani-min.
(Did not download `simple-plain` — not required, and `simple` already matches the default.)

| File | Size | SHA256 |
| --- | ---: | --- |
| `alt-text/quran-uthmani-txt.txt` | 1,347,874 | `e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8` |
| `alt-text/quran-uthmani-txt-2.txt` | 1,384,015 | `18c719bb3ba26d32ef457f40dad77cd28c4c5a34156833e26a8e5fcfdd246fb1` |
| `alt-text/quran-uthmani-min-txt.txt` | 1,149,812 | `3569cf6f04208c539ccd293f94d4844e79c56b3954e63b8767b0162e505d2cc2` |
| `alt-text/quran-uthmani-min-txt-2.txt` | 1,185,953 | `55630a086ebc31b6543c875bd639840e44a354e59496eace981019c946529a9b` |
| `alt-text/quran-simple-txt.txt` | 1,315,086 | `777c190d8e4ab081a80b4f10f5e309f1ab2a87e4d3ea97e5a7eabc59f4fe0b72` |
| `alt-text/quran-simple-txt-2.txt` | 1,351,227 | `dc8b285387da51dc4ce3ff8ed44d23c7e683d37f9490e23c0796c821cf159e86` |
| `alt-text/quran-simple-min-txt.txt` | 1,144,216 | `f564f9f2f3c29f153df06145b91cbf358c3f35e61142f251c4871e9ab03221ee` |
| `alt-text/quran-simple-min-txt-2.txt` | 1,180,357 | `28166c355f940bf58b8ebd67676af52f5752533c11a6eabe364845969403e9ec` |
| `alt-text/quran-simple-clean-txt.txt` | 758,172 | `2b3744abfc1e080aa66821fd897a9485d4da6cef9712f5972ea1d1e59bb0684b` |
| `alt-text/quran-simple-clean-txt-2.txt` | 794,313 | `054b3d9f79c0c2e44df7f9ddf42561797b3b5cb4fbdafbf2e99c805ccf1a6b49` |

- **License:** Creative Commons BY-ND 3.0 Unported (Tanzil.info). No modification allowed.
- **Date acquired:** 2026-04-12
- **Encoding:** UTF-8 (no BOM). Unix line endings. Trailing license comment block in each file.

## 3. Hafs Verse-Count Reference

### `hafs-verse-counts.tsv`
- **Source:** Derived directly by counting data rows (lines matching `^\d+\|\d+\|`) in
  `alt-text/quran-uthmani-txt-2.txt` (Tanzil Uthmani, Hafs numbering).
- **Why this source:** Tanzil's Uthmani text *is* the Hafs `an Asim recitation text as
  printed in the Madina Mushaf, so the row counts per surah are, by construction, the
  canonical Hafs verse totals. This avoids introducing a second authority.
- **Format:** Two-column TSV, `surah_id\tverse_count`, no header. 114 rows. Sums to 6236
  (canonical Hafs total).
- **Sanity spot-checks:** 1=7, 2=286, 3=200, 9=129, 36=83, 55=78, 108=3, 114=6. All match
  published Hafs counts.
- **Size:** 751 bytes  | **SHA256:** `e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba`
- **Generating command (for reproducibility):**
  ```sh
  awk -F'|' '!/^#/ && NF==3 {counts[$1]++} END {for (i=1;i<=114;i++) printf "%d\t%d\n", i, counts[i]}' \
      alt-text/quran-uthmani-txt-2.txt > hafs-verse-counts.tsv
  ```
- **Date acquired:** 2026-04-12

## 4. English Translation (Sahih International)

### `translations/en.sahih.txt-2.txt`
- **Source URL:** `https://tanzil.net/trans/?transID=en.sahih&type=txt-2`
- **Translator:** Sahih International
- **License:** Tanzil text license (CC BY-ND; see file trailer). Translation copyright
  belongs to Sahih International — check `https://tanzil.net/trans/` for the detailed
  per-translation notice.
- **Date acquired:** 2026-04-12
- **Size:** 898,049 bytes  | **SHA256:** `a1778a1a56695d9b59ae910809ec46d9f4a55f05961de51cd56e6ebcf9040883`
- **Format:** `surah|ayah|text` one line per verse, UTF-8 (ASCII-only in practice), no BOM.

### `translations/en.sahih.txt` (bonus plaintext)
- **Source URL:** `https://tanzil.net/trans/?transID=en.sahih&type=txt`
- **Size:** 861,908 bytes  | **SHA256:** `c44e0b75b7447e843625e4cc0ca3db89920280d176d2ddd77fe18c2a0aef3bcd`
- Same content, without surah|ayah prefix. Kept in case a tool prefers raw lines.

## 5. Baseline classical Arabic corpora (cross-textual control)

Acquired **2026-04-12** by `cross-baseline-run-1` agent for the
phase-B novelty pipeline. Purpose: provide a length-matched, register-matched,
date-matched control population so that any "the Quran is unusual in X" claim
can be tested against an actual Arabic null. Saved to
`data/baseline-corpora/raw/`. All files are UTF-8, no BOM, plaintext.

### 5.1 Pre-Islamic poetry — the Mu'allaqat (seven Golden Odes)

Source: Arabic Wikisource pages. Acquisition path:
`https://ar.wikisource.org/w/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&titles=<title>`.
Stripped of `{{template}}` markup; the verse contents inside `{{أبيات|…}}`
templates and inside hemistich wikitables were preserved. Hemistich
boundaries (`\\` or `||`) collapsed to single spaces.

| File | Source title | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `muallaqa-imru-al-qais.txt` | معلقة امرئ القيس | 12,384 | `06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14` |
| `muallaqa-tarafa.txt` | معلقة طرفة بن العبد | 11,753 | `5d103de0f56af0598bc98a6eabd66f075c9425080a71ac0914658e71820adfc1` |
| `muallaqa-zuhayr.txt` | معلقة زهير بن أبي سلمى | 10,502 | `9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2` |
| `muallaqa-labid.txt` | معلقة لبيد بن ربيعة | 24,822 | `ade71a4225cbcec1da43f537af65fe7b8e7a0649a7fbb724fa1f654409325b6b` |
| `muallaqa-amr-bin-kulthum.txt` | معلقة عمرو بن كلثوم | 16,051 | `d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720` |
| `muallaqa-antara.txt` | معلقة عنترة بن شداد | 7,141 | `4df797e787fa41d3ca84e6ef0a321d1cb934c54d18846d3ebfb7d65de6c118c6` |
| `muallaqa-harith.txt` | معلقة الحارث بن حلزة اليشكري | 24,827 | `372b00e49d9065eb46fbcf242b992b25e7cda66a4326f3dc11b53769a48069ff` |

License: Wikisource content is CC-BY-SA 4.0.

### 5.2 Full diwans of the Mu'allaqat poets — OpenITI (KITAB project)

Source: Open Islamicate Texts Initiative GitHub repos. Format: OpenITI
mARkdown (header `######OpenITI#`, `#META#…` block, then `#`-prefixed
text with `~~`/`%~%` line breaks and `%` hemistich markers). Stripped of
all metadata, mARkdown markers, page references, and structural pipes
to produce plaintext Arabic.

| File | OpenITI URI | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `diwan-imru-al-qais.txt` | `0001ImruQaysIbnHujr.Diwan.Shamela0027112-ara1` | 214,342 | `40668e0bce8914a1ecbf9d812654d363aae87bacfe99b5acf9376d05fbca1b94` |
| `diwan-tarafa.txt` | `0001TarafaIbnCabd.Diwan.Shamela0036422-ara1` | 55,867 | `6349387b3c23cd1f0dfa23490a15a6b1efc2fb09de45c4b17c138cb0ce99eb5f` |
| `diwan-zuhayr.txt` | `0001ZuhayrIbnAbiSulma.Diwan.JK007516-ara1` | 44,347 | `acd8be6ce8fa5609b410dc867adc243ad8e4dd597d3afcf881f6a832ea13ab7c` |
| `diwan-antara.txt` | `0001CantaraIbnShaddad.Diwan.ShamAY0037906-ara1` | 280,969 | `37b7c12564a6f297108c7ac844e5e65853368268532ec75062fd40330b354164` |
| `diwan-amr-ibn-kulthum.txt` | `0001CamrIbnKulthum.Diwan.ShamAY0037904-ara1` | 723 | `a5702c3046c781562248857f4f89c4491605f662d7e9e207edf1bf9422d20edf` |
| `diwan-harith.txt` | `0001HarithIbnHilliza.Diwan.ShamAY0037848-ara1` | 15,051 | `1677c24c4fee9bb569bbad245ff9dd4d2aa47b714aeb02997d26d90de8b1c48b` |
| `diwan-labid.txt` | `0041LabidIbnRabica.Diwan.Shamela0035077-ara1` | 138,514 | `8f8aacfadf0e6fe3efeeb8910eb2e9e4bbd3a27c8d466f55435f754eb9c4ec1f` |

Source URLs (raw):
`https://raw.githubusercontent.com/OpenITI/0025AH/master/data/0001…/0001….Diwan/<file>`
and `…/0050AH/master/data/0041LabidIbnRabica/0041LabidIbnRabica.Diwan/<file>`.

### 5.3 Abbasid poetry — Diwan al-Mutanabbi

| File | OpenITI URI | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `mutanabbi-diwan.txt` | `0354Mutanabbi.Diwan.JK007610-ara1.completed` | 79,820 | `d1bbed14b25111436af4149bacb5ff7cf3f400979a16e13cc45bf0d9a7ca89b9` |

`https://raw.githubusercontent.com/OpenITI/0375AH/master/data/0354Mutanabbi/0354Mutanabbi.Diwan/0354Mutanabbi.Diwan.JK007610-ara1.completed`.

### 5.4 Abbasid prose — al-Jahiz, Kitab al-Hayawan

| File | OpenITI URI | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `jahiz-hayawan.txt` | `0255Jahiz.Hayawan.Shamela0023775-ara1.completed` | 3,363,348 | `419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd` |

`https://raw.githubusercontent.com/OpenITI/0275AH/master/data/0255Jahiz/0255Jahiz.Hayawan/0255Jahiz.Hayawan.Shamela0023775-ara1.completed`.
**Quranic-quotation tags (`@QUR…@`) inside the OpenITI markdown were
stripped before plaintext export** so the corpus does not trivially
correlate with the Quran.

### 5.5 Sira ibn Hisham (the Prophet's biography)

| File | OpenITI URI | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `sira-ibn-hisham.txt` | `0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1.completed` | 2,566,373 | `527ac03a18201914fc5c4c80e7a698c2f74e2475c9ff48d1586bcfeccbdb247f` |

`https://raw.githubusercontent.com/OpenITI/0225AH/master/data/0213IbnHisham/0213IbnHisham.SiraNabawiyya/0213IbnHisham.SiraNabawiyya.Shamela0023833-ara1.completed`.
Quranic-quotation tags stripped at OpenITI level same as Jahiz.

### 5.6 Sahih al-Bukhari (the largest hadith collection)

| File | Source | Bytes | SHA256 |
| --- | --- | ---: | --- |
| `bukhari.txt` | Arabic Wikisource: 79 sub-pages of `صحيح البخاري` concatenated | 5,202,212 | `370dfe3520c8940812893a745b7b93f57eb1e10305f98726349966388794530c` |
| `bukhari-noquran.txt` | Same, with Quranic word-trigram overlap stripped (~5.6 % of tokens) | 4,640,009 | `0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100` |
| `matched-bukhari-77k.txt` | First 77,797 tokens of `bukhari-noquran.txt` (Quran-length matched) | 683,870 | `972e64ffd275e0afca21ea7cbe38c916735cc3b1f75d15180908538dbf283579` |

Bukhari was acquired via the MediaWiki API from 79 distinct
`صحيح البخاري/كتاب…` sub-pages enumerated by `list=allpages&apprefix=`.
The `-noquran` derivative is produced by `data/baseline-corpora/strip_quran_quotes.py`
which removes any token whose ±1-window trigram matches a Quranic
word trigram (Quran trigrams = 65,043). This is conservative
(over-removes when the Quran has rhyming common-word trigrams) but sufficient
to depress the trivial Quran-overlap signal in letter-frequency comparisons.

### 5.7 Reproducibility scripts

- `data/baseline-corpora/fetch_wikisource.py` — Mu'allaqat from Wikisource
- `data/baseline-corpora/fetch_bulk.py` — Bukhari from Wikisource
- `data/baseline-corpora/fetch_openiti.py` — diwans, Mutanabbi, Jahiz, Sira from OpenITI
- `data/baseline-corpora/strip_quran_quotes.py` — Quran-trigram stripper
- `data/baseline-corpora/analyze.py` — basic stats + tests 1, 2, 4
- `data/baseline-corpora/analyze2.py` — letter z-tests + test 3 (div-19)
