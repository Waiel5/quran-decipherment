# [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] - Formal Biqa'i Medinan inclusio rerun from primary text: pre-registration

```yaml
finding_id: h-new-257a
title: "Formal Biqa'i Medinan inclusio rerun from primary text - does the on-disk Naẓm al-Durar text align with the H-NEW-189 / H-NEW-257 target set better than a naive all-surah baseline?"
parent:
  - h-new-257 (descriptive Biqa'i Medinan inclusio cross-reference; access premise now superseded)
  - h-new-189 / h-new-189.1 (Medinan first↔last inclusio STRONG-PASS)
date: 2026-04-18
specialist: autonomous (H-NEW-257a)
source_primary: data/literature/classical-tafsir/raw/biqai-nazm-al-durar.ShamAY.raw.txt
source_secondary_inspected: data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt
seed: null
rules_tuple: "(primary-text Biqa'i section parser from on-disk ShamAY raw; sequential surah-heading extraction over 114 surahs with locked alias map; first-content verse = v2 for muqaṭṭaʿat-opened surahs else v1; normalized Arabic surface-token overlap proxy for first↔last shared content; de-formulaization stop-list; opening span = first 1500 normalized chars of section; closing span = last 1500 normalized chars of section; exact one-sided Fisher enrichment vs all non-target surahs)"
bonferroni_k: 1
alpha_family: 0.05
alpha_bon: 0.05
target_set:
  - 3
  - 4
  - 8
  - 9
  - 33
  - 47
  - 59
  - 60
  - 63
  - 65
  - 98
```

## 1. Integrity note

This is a **post-format-inspection lock**, not a pristine blind prereg. The raw
Biqa'i files were inspected first to determine whether the text was actually on
disk, how surah headings are encoded, and which closure-phrase families are used
in the commentary. The final rule below is locked **before the production
runner is written and executed**, but not before preliminary format/cue
inspection.

This is disclosed because [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] is a parser-and-scoring construction task,
not a pure black-box rerun of an already-fixed instrument.

## 2. Motivation

[[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]] remained descriptive because it assumed full primary-text access to
Biqa'i's *Naẓm al-Durar* was absent. That premise is now false: two raw text
witnesses are already on disk.

The unresolved question is no longer "do we have the text?" but:

> Under a reproducible primary-text scoring rule, does Biqa'i materially align
> with the empirically identified Medinan inclusio set better than a naive
> background baseline?

The goal is not to prove that Biqa'i names every target surah. The goal is to
replace the old descriptive note with a deterministic, re-runnable scoring task.

## 3. Locked target set

Primary target set = the 11 surahs explicitly enumerated in [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]] as the
named Medinan inclusio-positive surahs inherited from [[h-new-189-medinan-inclusio|H-NEW-189]]/H-NEW-189.1:

- Q 3
- Q 4
- Q 8
- Q 9
- Q 33
- Q 47
- Q 59
- Q 60
- Q 63
- Q 65
- Q 98

Why this set instead of re-deriving a fresh "Medinan" partition:

- [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]] already hard-named these 11 as the task-facing target list.
- The repo's period metadata are not uniform across artifacts; re-opening the
  chronology layer here would silently mutate the parent target.
- [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] is a primary-text scoring rerun, not a chronology re-adjudication.

All other surahs form the naive background baseline.

## 4. Section extraction rule

Use `biqai-nazm-al-durar.ShamAY.raw.txt` as the executable source because its
surah headings are more machine-tractable than the OpenITI dump.

Lock the section parser as follows:

1. Load all 114 surahs from `quran-text/quran-no-tashkeel.json`.
2. Scan the Biqa'i file sequentially in mushaf order.
3. For each surah, find the first matching heading after the previous surah
   heading using only these heading families:
   - `^#+.*سورة ...$`
   - `^# ( سورة ... )$`
4. Use a locked alias map only for known title variants:
   - `التوبة/براءة`
   - `ابراهيم/إبراهيم`
   - `الإسراء/بني إسرائيل`
   - `غافر/المؤمن`
   - `فصلت/حم السجدة`
   - `الإنسان/الانسان/الدهر`
   - `النبإ/النبأ`
   - `الإنفطار/الانفطار`
   - `الإنشقاق/الانشقاق`
   - `الشرح/الانشراح`
   - `المسد/اللهب`
5. A surah section runs from the end of its heading to the start of the next
   heading.

No manual per-surah patching after execution.

## 5. Endpoint-overlap proxy

Because the commentary is raw prose, not QAC morphology, [[h-new-257a-biqai-primary-text-rerun|H-NEW-257a]] uses a
surface-token proxy rather than a hidden root analyzer on the commentary side.

For each surah:

1. `v_first` = verse 2 for muqaṭṭaʿat-opened surahs, verse 1 otherwise.
2. `v_last` = final verse.
3. Normalize Arabic surface text:
   - strip tashkil
   - normalize `أ/إ/آ/ٱ -> ا`
   - normalize `ى -> ي`
   - normalize `ة -> ه`
   - normalize `ؤ -> و`
   - normalize `ئ -> ي`
4. Tokenize on Arabic-letter runs.
5. Keep only tokens of length `>= 3`.
6. Remove a locked basic function-word stop-set:
   - `من في على الى إلى عن ما لا لم لن ثم قد هو هي هم هذا هذه ذلك تلك كان كانت إن أن إنه أنه كل كما يا أي أو بل اذا إذا وهو وهي وهم له لهم بهم بها عليهم عليه فيه فيها بين بعد قبل ربكم ربهم`
7. Remove a locked **de-formulaization** set to stop generic devotional overlap
   from counting as primary evidence:
   - `الله`
   - `والله`
   - `الذين`
   - `ايها`
   - `يايها`
   - `امنوا`
   - `ومن`
   - `وكان`
   - `كانت`
8. Define `shared_endpoint_tokens` as the intersection of the filtered token
   sets of `v_first` and `v_last`.

This is intentionally stricter than [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]]'s prose note. The point is to
distinguish substantive endpoint echo from formulaic overlap.

## 6. Span windows

For each surah section:

- `opening_span` = first 1500 normalized characters
- `closing_span` = last 1500 normalized characters

This is locked to approximate Biqa'i's overt statement-of-purpose zone and his
terminal closure paragraph without hand-selecting local snippets per surah.

## 7. Locked cue families

### 7.1 Direct bridge cues

A section is marked `bridge_cue = True` if the normalized section text matches
any of the following phrase families:

- `رد المقطع على المطلع`
- `رد الختام على الافتتاح`
- `كان اخرها دليلا على اولها`
- `وفى مطلعها مقطعها`
- `انعطف على افتتاحها وختامها`
- `عانق ابتداوها تمامها` / `عانق ابتداؤها تمامها` after normalization
- `رجع بذلك اول السوره الى اخرها`
- generic direct closure templates:
  - `ختم ... افتتح`
  - `اخرها ... اولها`
  - `اولها ... اخرها`

### 7.2 Generic structural cues

`start_cue = True` if the section contains any of:

- `افتتح`
- `افتتحت`
- `اولها`
- `اول السوره`
- `مطلع`
- `مقصودها`

`end_cue = True` if the section contains any of:

- `ختم`
- `ختمت`
- `اخرها`
- `اخر السوره`
- `مقطع`
- `ختامها`
- `تمامها`

## 8. Scoring rule

For each surah, compute:

- `opening_hits` = shared endpoint tokens present in `opening_span`
- `closing_hits` = shared endpoint tokens present in `closing_span`

Then define:

### 8.1 Explicit support

`explicit_support = 1` iff:

- `bridge_cue = True`, and
- at least one shared endpoint token appears in `opening_span` or `closing_span`

Otherwise `explicit_support = 0`.

### 8.2 Material support

`material_support = 1` iff at least one of the following holds:

- `explicit_support = 1`
- at least one shared endpoint token appears in `opening_span` and at least one
  shared endpoint token appears in `closing_span`
- `bridge_cue = True` and there are at least two distinct shared endpoint tokens
  across `opening_hits ∪ closing_hits`
- `start_cue = True` and `end_cue = True` and there are at least two distinct
  shared endpoint tokens across `opening_hits ∪ closing_hits`

Otherwise `material_support = 0`.

### 8.3 Primary binary

`support_positive = 1` iff `explicit_support = 1` or `material_support = 1`.

This is the **primary registered binary** for the enrichment test.

## 9. Statistical test

Primary test:

- Exact one-sided Fisher test on the `2 x 2` table
  - rows = `{target set, all non-target surahs}`
  - columns = `{support_positive = 1, support_positive = 0}`
- Direction locked:
  - target set has higher support-positive rate than background

Primary verdict rule:

- `PASS` if one-sided Fisher `p < 0.05`
- otherwise `NULL`

Secondary descriptive outputs:

- target `explicit_support` count
- target `material_support` count
- background surahs that also score positive

## 10. Honest limits

1. This is a **surface-token proxy** for content-root overlap in commentary, not
   a perfect root-matcher on Biqa'i prose.
2. The de-formulaization list is deliberately small. It removes obvious
   inflation (`الله`, `الذين`, `يا أيها`, etc.) but not every possible generic
   word.
3. Span windows are heuristic. They are locked here to avoid per-surah
   hand-tuning.
4. The target set is inherited from [[h-new-257-biqai-medinan-inclusio-crossref|H-NEW-257]]/H-NEW-189's named surahs rather
   than re-derived from a fresh chronology file because the repo's period labels
   are not uniform across artifacts.
5. The OpenITI raw text was inspected, but the executable parser uses the
   ShamAY witness only; this is a tractability choice, not a claim that the
   other witness is inferior philologically.
6. "Support" here means primary-text alignment with the endpoint-overlap signal,
   not proof that Biqa'i explicitly formulated the modern [[h-new-189-medinan-inclusio|H-NEW-189]] statistic.

## 11. Deliverables

- `scripts/h_new_257a_biqai_primary_text_rerun.py`
- `findings/phase-b-hypotheses/h-new-257a-biqai-primary-text-rerun.md`
- `findings/phase-b-hypotheses/csv/h-new-257a.json`
- `journal/h-new-257a-run-1.md`

Pre-reg locked 2026-04-18. Execution follows.
