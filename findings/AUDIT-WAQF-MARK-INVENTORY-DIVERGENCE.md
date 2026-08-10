# Audit: the project's text files disagree on the waqf marks — and the file F-1 was pointed at is the outlier

**Date:** 2026-08-09
**Status:** DATA-PROVENANCE FINDING. Blocking for F-1; advisory for anything using pause marks.
**Found:** while verifying the frontier map's glyph counts before dispatching F-1's design.

---

## 1. The map's counts are correct — and that is the problem

`HANDOFF/FRONTIER-MAP-2026-08-07.md` F-1 lists, as **verified** data:

> `quran-text/quran-full-tashkeel.json` contains: U+06DA jīm ×2,083; U+06D6 ṣlà ×1,651;
> U+06D7 qlà ×511; U+06D8 mīm ×21; U+06DC saktah ×8; U+06DB muʿānaqa ×6. I counted these directly.

**All six reproduce exactly.** The map is not wrong about its file.

But the file it names is the only one in the repo that gives those numbers. Counting the same
glyphs across every text file on disk:

| file | ṣlà 06D6 | qlà 06D7 | mīm 06D8 | **lā 06D9** | jīm 06DA | muʿān. 06DB | saktah 06DC |
|:--|--:|--:|--:|--:|--:|--:|--:|
| **`quran-full-tashkeel.json`** | **1651** | **511** | **21** | **0** | **2083** | **6** | **8** |
| `quran-min-tashkeel.json` | 1682 | 603 | 22 | **68** | 1972 | 12 | 7 |
| `quran-no-tashkeel.json` | 1682 | 603 | 22 | **68** | 1972 | 12 | 5 |
| `data/alt-text/quran-uthmani-txt.txt` | 1682 | 603 | 22 | **68** | 1972 | 12 | 7 |
| …and 9 further alt-text files | 1682 | 603 | 22 | **68** | 1972 | 12 | 5–7 |

**Twelve files agree with each other. One disagrees with all of them.** And the one that disagrees
is the one F-1 was told to use.

## 2. The divergence is a re-grading, not a truncation

| grade | full-tashkeel | the other twelve | Δ |
|:--|--:|--:|--:|
| jīm (*jāʾiz*, permitted) | 2083 | 1972 | **+111** |
| qlà (*waqf awlā*, stopping preferable) | 511 | 603 | −92 |
| ṣlà (*waṣl awlā*, continuing preferable) | 1651 | 1682 | −31 |
| muʿānaqa | 6 | 12 | −6 |
| mīm (*lāzim*, obligatory) | 21 | 22 | −1 |
| **lā (do NOT stop)** | **0** | **68** | **−68** |

The jīm count moves *up* by 111 while qlà moves *down* by 92. Marks are not merely missing from one
file — **they are graded differently.** A truncation cannot increase a count.

## 3. The consequence for F-1, and it is disqualifying as briefed

F-1's hypothesis is that *"the four Sajāwandī pause grades … track a real syntactic-prosodic
boundary hierarchy."* Run on `quran-full-tashkeel.json`, that test would have been conducted on a
system **missing its entire negative grade.**

**lā (U+06D9) is the mark that means *do not stop here*.** It is the only member of the inventory
that forbids rather than permits or prefers. Testing a "boundary hierarchy" with the prohibition
grade silently absent is testing a different system — and nothing in the run would have flagged it,
because the file parses cleanly, the other six marks are present in plausible numbers, and the map
certifies the counts as verified.

Note also the counter-intuitive fact that makes this easy to miss: **`quran-no-tashkeel.json`
carries MORE waqf marks than `quran-full-tashkeel.json`.** "No tashkeel" strips vowels, not pause
marks. Anyone reasoning that the fullest-vocalised file must carry the fullest annotation reasons
wrongly here.

## 4. What is NOT claimed

**Which inventory is correct is not settled here, and I am not settling it by preference.** Both are
internally consistent. The 12-file consensus is the Tanzil-derived family; the singleton may come
from a different source or a different Tanzil release. Determining which reflects the Madīna muṣḥaf
requires either a printed-muṣḥaf comparison or the upstream provenance record — neither of which is
established on disk, and asserting an answer without one would be exactly the hand-assigned-quantity
failure that [[PROXY-CLAIMS]] governs.

What *is* established: **they differ, the difference includes an entire missing grade, and no
finding using pause marks has ever declared which file it used as a rules-tuple element.**

## 5. Binding consequence

Any test using waqf marks must:

1. **Declare the source file explicitly as a rules-tuple element**, not merely cite "the Uthmānī
   text." The tuple is now known to be outcome-relevant.
2. **Run under both inventories** — the singleton and the 12-file consensus — and report both. This
   is the pause-mark instance of the length-channel rule from
   [[cross-finding-029-the-deciding-parameter]]: when a convention can carry a verdict, you do not
   pick one, you report the sweep.
3. **State whether lā is in scope.** A hierarchy claim that excludes the prohibition grade should
   say so in its title, not its limits.

## 6. The general lesson

The map's counts were labelled *"I counted these directly"* — and that was true. **Verifying a count
against the file it came from cannot detect that the file is the outlier.** The check that finds
this is not re-counting; it is counting the same thing somewhere else. This is the corpus-level form
of the same failure as today's two wrong *Itqān* nawʿ citations, where the mechanically-checkable
field verified perfectly and the unchecked one had drifted.

Related: [[cross-finding-029-the-deciding-parameter]] · [[PROXY-CLAIMS]] · [[ABSENCE-CLAIMS]] ·
[[UNIT-DRIFT-DEFECT]]
