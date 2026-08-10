# Audit: the register proxy matches 89 times in one file and zero times in every other

**Date:** 2026-08-10
**Status:** FRAGILITY, not a defect. `h-new-2500.py` reads the correct file. Nothing is retracted.
**Found:** while establishing file provenance for F-9 (rasm/imlāʾ), before that lane designed anything.

---

## 1. The measurement

`h-new-2500.py` line 60 defines the legal register by counting two bare-consonantal substrings:

```python
LEGAL_MARKERS = ["يا أيها الذين آمنوا", "كتب عليكم"]
```

Counting those exact strings across the corpus files on disk:

| file | `yā ayyuhā alladhīna āmanū` | `kutiba ʿalaykum` |
|:--|--:|--:|
| **`quran-no-tashkeel.json`** — what the script reads | **89** | **5** |
| `quran-min-tashkeel.json` | 0 | 0 |
| `quran-full-tashkeel.json` | 0 | 0 |
| `data/alt-text/quran-uthmani-txt.txt` | 0 | 0 |
| `data/alt-text/quran-simple-txt.txt` | 0 | 0 |

**The script reads the right file** — line 26 is `quran-text/quran-no-tashkeel.json`. This is not an
error. It is a **total, silent, undeclared single-file dependency.**

## 2. Why the count collapses to zero

Two independent orthographic facts, either of which alone is sufficient:

1. **Vocalisation.** The markers are written without tashkeel. In any vocalised file the same words
   carry fatḥa, shadda and sukūn between the letters, so a bare substring cannot match.
2. **Vocative joining — the F-9 phenomenon itself.** In the Uthmānī rasm the vocative particle *yā*
   is written **joined** to its noun; in the simple orthography it is **separate**:

   | Uthmānī | simple |
   |:--|:--|
   | `يَٰٓأَيُّهَا` (one token) | `يَا أَيُّهَا` (two tokens) |
   | `يَٰٓأَرْضُ` | `يَا أَرْضُ` |
   | `يَبْنَؤُمَّ` (one token) | `يَا ابْنَ أُمَّ` (three) |

   So even stripped of vowels, the Uthmānī text has no space where the marker expects one.

### 2.1 This accounts for the entire token-count discrepancy between the two alt-texts

`quran-uthmani-txt.txt` and `quran-simple-txt.txt` align line-for-line (6,264 each) but the Uthmānī
carries **367 fewer word tokens**. Localised: **363 lines differ in token count — 359 by exactly −1
and 4 by −2.** Every inspected case is vocative joining. The −2 cases are three-word phrases
collapsing to one, as at Q 20:94 (`يَا ابْنَ أُمَّ` → `يَبْنَؤُمَّ`).

**The whole 367-token gap between the project's two "same text, different orthography" files is one
grammatical phenomenon.**

## 3. Why this is a fragility worth recording rather than a defect

Nothing here is wrong. But the failure mode, if the input were ever swapped, is the worst kind:

- **Total, not degraded.** Not fewer matches — *zero*. Every surah would fall through to a
  non-legal class.
- **Silent.** The proxy would return a well-formed 4-class labelling in which the legal register is
  empty. No exception, no warning, no obviously wrong number.
- **Load-bearing.** That proxy defines the register axis for `cross-finding-028` and is consumed by
  at least H-NEW-2250, 2490, 2520, 2530, 2630, 2640, 2800 and the H-NEW-127 family.

This is the same shape as [[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]]: **a file choice that is
verdict-bearing and undeclared.** There, thirteen files disagreed about which pause marks exist.
Here, five files disagree about whether a defining phrase occurs at all.

## 4. The rule

> **A substring matcher over Arabic text is a rules-tuple element, not an implementation detail.**
> Any script matching literal Arabic must declare the orthographic variant it requires, and assert
> a non-zero match count at runtime.

The assertion is one line and converts a silent total failure into a loud one:

```python
assert leg_total > 0, "LEGAL_MARKERS matched nothing — wrong orthographic variant?"
```

`h-new-2500.py` has no such assertion. Neither does any other matcher in the repo that was checked.

## 5. Honest limits

- **No finding is retracted and none should be.** Every consumer of the proxy inherits its labels
  from `csv/h-new-2500.json`, not by re-running the matcher, so the dependency has never actually
  been exercised wrongly. This is a latent hazard, not a realised one.
- **The 89 matches were not verified against the muṣḥaf** — only that they are what the script sees.
  Whether 89 is the correct count of the phrase in the Quran is a separate question this audit does
  not answer.
- **"Every inspected case is vocative joining"** rests on inspecting the three largest deltas and a
  sample of the −1 cases, not all 363. The claim that vocative joining accounts for the *whole* gap
  is therefore strongly supported but not exhaustively verified.

Related: [[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]] · [[cross-finding-029-the-deciding-parameter]] ·
[[AUDIT-CF028-SCOPE-VS-ANCHORS]] §7 (the same marker, in its role as a construct that overlaps the
features tested against it)

---

## 6. The exhaustive classification is STILL OPEN — two lanes and two of my own attempts have failed

§2.1 claims the 367-token gap is *entirely* vocative joining, with the caveat that this rests on the
three largest deltas plus a sample of the −1 cases rather than all 363 lines. **That caveat has not
been discharged, and this section records why rather than leaving the gap silent.**

**Two dispatched lanes produced nothing.** F-9 and its re-dispatch both went idle with no
pre-registration, no script and no run directory. No output to salvage.

**Two of my own attempts produced a number I do not believe.** Both classifiers returned
**"vocative yā = 0.0% of resolved merges"** while printing, in the same output, obviously vocative
examples:

```
line 27   U: يَٰٓأَيُّهَا ٱلنَّاسُ …      S: يَا أَيُّهَا النَّاسُ …
line 41   U: وَقُلْنَا يَٰٓـَٔادَمُ …      S: وَقُلْنَا يَا آدَمُ …
```

A classifier that reports 0% of a category while displaying members of that category is broken. The
second attempt normalised combining marks and alef variants and still bucketed 191 merges under an
**empty-string key**, meaning its normaliser reduced `يَا` to nothing. The bug is in the
normalisation, not in the data.

**I stopped rather than attempt a third pass.** The alternative was to keep adjusting a normaliser
until it produced the answer §2.1 already predicts — which is fitting the instrument to the expected
result, and the number would carry no evidential weight once obtained that way.

### 6.1 What therefore stands and what does not

| claim | status |
|:--|:--|
| 6,264 lines align; Uthmānī carries 367 fewer word tokens | **verified** |
| 363 lines differ in token count; 359 by −1, 4 by −2 | **verified** |
| the −2 cases are three-word phrases collapsing to one (Q 20:94) | **verified by inspection** |
| vocative joining is *the* mechanism | **verified on inspected cases** |
| vocative joining accounts for **all** 363 | **STILL UNVERIFIED** |

Nothing downstream of this file depends on the exhaustive version. The
[[AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE]] result — that the register-defining phrase matches in
one file and no other — rests on direct counts, not on this classification.

**What the task needs is a proper Arabic normaliser with a unit test**, not another ad-hoc strip. The
test is trivial to state: `bare("يَا") == "يا"` and
`bare("يَٰٓأَيُّهَا") == bare("يَا") + bare("أَيُّهَا")`. Both of my attempts would have failed that
assertion on the first line, before touching the corpus.

