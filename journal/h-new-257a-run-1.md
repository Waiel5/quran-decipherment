# Journal - H-NEW-257a run 1

- Date: 2026-04-18
- Pre-reg: `findings/phase-b-hypotheses/h-new-257a-biqai-primary-text-rerun-prereg.md`
- Pre-reg SHA-256: `dbd504b3290b280ae0bd0ef14796c19bb8cd5320751f51a721fff549475c8bea`
- Script: `scripts/h_new_257a_biqai_primary_text_rerun.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-257a.json`
- Primary source parsed: `data/literature/classical-tafsir/raw/biqai-nazm-al-durar.ShamAY.raw.txt`
- Secondary source inspected: `data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt`

## Commands

```bash
python3 -m py_compile scripts/h_new_257a_biqai_primary_text_rerun.py
python3 scripts/h_new_257a_biqai_primary_text_rerun.py
```

## Parser status

- sequential surah parser succeeded on `114 / 114` sections
- no manual per-surah parser patches were needed after lock

## Primary result

- target support-positive: `3 / 11`
- background support-positive: `6 / 103`
- exact one-sided Fisher: `p = 0.04118291923524781`
- odds ratio: `6.0625`
- expected target hits under global rate: `0.8684210526315789`
- observed / expected lift: `3.454545454545455`
- verdict: `PASS`

## Target hits

- `Q 4 al-Nisa`
  - shared tokens: `رجالا`, `ونساء`
  - opening hits: `رجالا`, `ونساء`
  - closing hits: `رجالا`, `ونساء`
  - bridge cues: `akhiruha_awwaliha`, `awwaliha_akhiruha`

- `Q 47 Muhammad`
  - shared token: `سبيل`
  - opening hits: `سبيل`
  - closing hits: none
  - bridge cues: `khatama_iftataha`, `awwaliha_akhiruha`

- `Q 59 al-Hashr`
  - shared tokens: `الحكيم`, `السماوات`, `العزيز`
  - opening hits: `الحكيم`, `السماوات`, `العزيز`
  - closing hits: `الحكيم`
  - bridge cue: `anaqa_ibtidauha_tamamaha`

## Background positives

- `Q 6`, `Q 17`, `Q 22`, `Q 35`, `Q 45`, `Q 112`
- notable internal check: `Q 6` and `Q 45` are the same two Meccan exceptions
  previously highlighted in H-NEW-257

## Immediate interpretation

This run upgrades H-NEW-257 from a corpus-access ceiling into a real primary-text
scoring task.

The result is positive but narrow:

- Biqa'i aligns with the inherited target set better than a naive baseline.
- The strong primary-text support is concentrated in `Q 4`, `Q 47`, and `Q 59`.
- The majority of the 11 target surahs still do not pass the strict
  de-formulaized rule.
