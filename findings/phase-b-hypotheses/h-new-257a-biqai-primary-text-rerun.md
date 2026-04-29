---
id: H-NEW-257a
title: "Formal Biqa'i Medinan inclusio rerun from primary text"
phase: B
status: PARTIAL-PASS (exact enrichment under strict primary-text rule; 3/11 target surahs support-positive)
date: 2026-04-18
executed_by: autonomous (H-NEW-257a)
parent: H-NEW-257 / H-NEW-189.1
pre_reg: findings/phase-b-hypotheses/h-new-257a-biqai-primary-text-rerun-prereg.md
source_primary: data/literature/classical-tafsir/raw/biqai-nazm-al-durar.ShamAY.raw.txt
source_secondary_inspected: data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt
verdict: PASS for target-set enrichment; surah-specific majority remains unconfirmed
---

# [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] — Formal Biqa'i Medinan inclusio rerun from primary text

## Headline

The old [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]] access premise is superseded: the primary Biqa'i text is on
disk and can be scored directly.

Under the locked [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] rule, the 11 inherited target surahs are enriched
for **support-positive** Biqa'i sections relative to the naive all-surah
background:

- target set: **3 / 11** support-positive
- non-target background: **6 / 103** support-positive
- exact one-sided Fisher: **p = 0.0412**
- odds ratio: **6.06**
- observed target hits: **Q 4, Q 47, Q 59**
- expected target hits under the global support rate: **0.87**
- observed / expected lift: **3.45x**

This is a **PASS for primary-text enrichment** but only a **PARTIAL**
surah-specific confirmation. Most of the 11 target surahs do **not** pass the
strict de-formulaized rule.

## What was scored

The runner used the on-disk `ShamAY` witness of *Naẓm al-Durar* and parsed all
114 surah sections sequentially by heading.

For each surah it then:

1. took the first content verse (`v2` for muqaṭṭaʿat-opened surahs, else `v1`)
   and the last verse
2. computed their shared normalized surface tokens after a locked
   de-formulaization filter
3. checked whether those shared tokens appear in the opening and/or closing
   spans of Biqa'i's section
4. checked for direct bridge phrases such as:
   - `كان آخرها دليلا على أولها`
   - `فرجع بذلك أول السورة إلى آخرها`
   - `وفى مطلعها مقطعها`

Primary binary:

- `support_positive = explicit_support OR material_support`

The full implementation is in the JSON and script artifacts.

## Target-set table

| Q | Name | De-formulaized shared endpoint tokens | Bridge cue | Support |
|---:|---|---|:---:|:---:|
| 3 | Āl ʿImrān | none | yes | 0 |
| 4 | al-Nisāʾ | `رجالا`, `ونساء` | yes | **1** |
| 8 | al-Anfāl | none | no | 0 |
| 9 | al-Tawbah | none | yes | 0 |
| 33 | al-Aḥzāb | none | no | 0 |
| 47 | Muḥammad | `سبيل` | yes | **1** |
| 59 | al-Ḥashr | `الحكيم`, `السماوات`, `العزيز` | yes | **1** |
| 60 | al-Mumtaḥana | none | yes | 0 |
| 63 | al-Munāfiqūn | none | no | 0 |
| 65 | al-Ṭalāq | none | yes | 0 |
| 98 | al-Bayyinah | none | no | 0 |

Interpretation of the zero rows:

- some target surahs do contain generic structural language, but their
  first↔last overlap collapses under the locked de-formulaization filter
- others do not show a surviving non-formulaic endpoint echo in the opening and
  closing spans under this surface-token proxy

## Strongest positive cases

### Q 4 al-Nisāʾ

This is the cleanest non-formulaic Medinan hit. The overlap tokens
`رجالا / ونساء` survive the de-formulaization filter and appear in both opening
and closing evidence zones. Biqa'i also uses the direct closure phrase
`كان آخرها دليلا على أولها`, then immediately back-cites `[النساء: 1]`.

### Q 47 Muḥammad

The section opens directly on `سبيل الله`, which is the surviving shared
endpoint token, and closes with the overt bridge formula
`فرجع بذلك أول السورة إلى آخرها`. This is the strongest **explicit** target
hit even though the closing span does not retain an additional de-formulaized
token beyond the opener.

### Q 59 al-Ḥashr

Q 59 was already the strongest candidate in [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]], and the primary text
confirms that instinct. The opening/closing evidence retains `الحكيم` and the
opening span also retains `العزيز / السماوات`. Biqa'i closes with a direct
architectural cue: `وفى مطلعها مقطعها`.

## Background hits

Six non-target surahs also score positive under the same strict rule:

- Q 6 al-Anʿām
- Q 17 al-Isrāʾ
- Q 22 al-Ḥajj
- Q 35 Fāṭir
- Q 45 al-Jāthiyah
- Q 112 al-Ikhlāṣ

Two of these matter immediately:

- **Q 6**
- **Q 45**

These are exactly the two Meccan exceptions highlighted in [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]]'s older
descriptive note. That does not alter the [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] primary test, but it is a
useful internal consistency check: the strict primary-text rule independently
rediscovers both exceptions.

## Interpretation

[[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] replaces the old "primary text unavailable" ceiling with a real
primary-text result.

The result is **not** "Biqa'i explicitly marks all or most empirical Medinan
inclusio surahs." That stronger claim still fails.

The result **is**:

1. Biqa'i's primary text aligns with the inherited target set better than a
   naive all-surah baseline.
2. The alignment is concentrated in the strongest non-formulaic endpoint cases,
   especially Q 4, Q 47, and Q 59.
3. Several target surahs that looked promising in the descriptive note do **not**
   survive a strict de-formulaized rerun because their overlap is carried mainly
   by highly formulaic material such as divine-name or communal-address language.

So the honest upgrade from [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]] is:

- **general principle**: still supported
- **primary-text target-set enrichment**: now supported
- **majority surah-specific confirmation**: still not supported

## Honest limits

1. This is a surface-token proxy on the commentary side, not a full root
   analyzer over Biqa'i prose.
2. The de-formulaization filter is intentionally strict. It likely undercounts
   surahs such as Q 60 where the endpoint echo is real but heavily formulaic.
3. The executable parser uses the `ShamAY` witness only because its headings are
   cleaner. The OpenITI witness was inspected but not used for the production
   parse.
4. The target set is inherited from [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]]/H-NEW-189's named surahs rather
   than re-derived from a fresh chronology table because period metadata are not
   uniform across repo artifacts.
5. The PASS verdict is an enrichment-level verdict, not a claim that Biqa'i
   singled out a majority of the empirical set.

## Files

- Script: `scripts/h_new_257a_biqai_primary_text_rerun.py`
- Pre-reg: `findings/phase-b-hypotheses/h-new-257a-biqai-primary-text-rerun-prereg.md`
- JSON: `findings/phase-b-hypotheses/csv/h-new-257a.json`
- Journal: `journal/h-new-257a-run-1.md`
