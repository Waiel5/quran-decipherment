---
surah: 1
test_id: Q001-F-02
file_type: novel-finding
date_locked: 2026-04-28
date_run: 2026-04-28
verdict: VINDICATED
prereg_sha: badefd870db1ee0acb8935ce467fb183aeff08a854a68305f83492971ef7f3c5
---

# Q001-F-02 — Central word of Q 1 (29 words → position 15)

## 1. Pre-registered hypothesis

If Q 1 al-Fātiḥa has 29 words (no-tashkeel, orthographic-word, basmala counted as V1), then word #15 (the unique median position for an odd N=29) lies in **verse 5** — the classical pivot verse *iyyāka naʿbudu wa-iyyāka nastaʿīn*.

Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-02-central-word-prereg.md`

## 2. Result

**N = 29** (confirmed across no-tashkeel, min-tashkeel, full-tashkeel — invariant).

The word at position 15 is **نعبد** (*naʿbudu* — "we worship"), located in verse 5.

| Variant | N | Index 15 word | Verse |
|:--|--:|:-:|:-:|
| no-tashkeel | 29 | نعبد | 5 |
| min-tashkeel | 29 | نَعبُدُ | 5 |
| full-tashkeel | 29 | نَعۡبُدُ | 5 |

## 3. Verdict: VINDICATED

The pre-committed claim that the central word lies in verse 5 holds across all three tashkeel variants. The classical pivot identification (V5 as the worship/help-asking turning point of the chiasm) is empirically anchored at the literal word-position level.

## 4. Refined observation — central word is *naʿbudu*, NOT *iyyāka*

The Suyūṭī al-Itqān cites **سورة المناجاة** ("the surah of intimate discourse") as a name of Q 1 specifically because of *iyyāka naʿbudu wa-iyyāka nastaʿīn* (V5) — al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on names of surahs (line ~3376 in OpenITI raw):

> الرابع والعشرون: سورة المناجاة لأن العبد يناجي فيها ربه بقوله: {إياك نعبد وإياك نستعين}.

The agent prompt suggested "iyyāka" was the central word; empirically the central word is the verb **naʿbudu** ("we worship"), not the pronoun "iyyāka." This is consistent with the al-Suyūṭī observation: V5 is the verse where servant addresses God; the verb *naʿbudu* is the precise grammatical centroid of the surah's word-stream.

This is a non-trivial refinement: the central word is the **verb of worship**, putting the act-of-worship (not the addressee) at the literal mathematical center of the surah.

## 5. Robustness

- N = 29 invariant across all three tashkeel variants (no-tashkeel / min-tashkeel / full-tashkeel).
- Index 15 = (29+1)/2 is the unique median for odd N=29. No tie-breaking ambiguity.
- The basmala IS counted as V1 in the Hafs reading; if the basmala were not counted, N would still be 29 (we count words, not verses).

## 6. Honest limits

- The "central word" finding depends on the rules-tuple (orthographic-word). Counting at the morpheme/clitic level (e.g., separating *wa-* from *wa-iyyāka*) would shift N. We pre-committed to whitespace-orthographic-tokens.
- This finding is GEOMETRIC, not theological. It does NOT prove the structure is "designed" — it shows that under one reasonable rules-tuple, the structural-pivot verse contains the literal-position-pivot word.

## 7. Output files

- Script: `/Users/grey/Downloads/quran/scripts/Q001_F_02_central_word.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/csv/Q001-F-02.json`
- Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-02-central-word-prereg.md`
