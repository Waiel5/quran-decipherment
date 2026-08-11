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

---

## 8. CORRECTION — §4's absence claim is FALSE, and it is this project's own defect class

§4 stated that **"no finding using pause marks has ever declared which file it used as a rules-tuple
element."** That is false on disk, in two places, both **dated 2026-08-07 — two days before this
audit was written**:

- **`h-new-2560-fasila-clause-seal.md` line 18**, YAML front-matter:
  `rules_tuple: "(no-tashkeel for the waqf join, EQTB segment-token, …)"`
- **The same file, line 365**, an entire section headed
  **"H5 rules-tuple disclosure — the waqf annotation is NOT identical across text variants"**, which
  opens: *"Added 2026-08-07 after an independent audit. This is a disclosure the original write-up
  owed and did not give."* It tabulates the glyph counts across all three variants, records that
  full-tashkeel has **zero lā**, 92 fewer qlà and 111 more jīm, and **self-demotes H5 to
  SINGLE-TUPLE on that basis.**
- `h-new-2610-waqf-prosody.md` §7 does the same, and its §0.5 **retracts its own priority claim** in
  2560's favour.

**So the divergence was found on 2026-08-07, disclosed against its own finder's result, and then
re-derived independently on 2026-08-09 by this audit — which asserted its absence.**

This is [[ABSENCE-CLAIMS]]'s defect, committed **inside the file written to catch a data-provenance
defect.** The rule that file states is *"claims of absence are the least audited claims in any
project, because nothing downstream fails when they are wrong."* Nothing downstream failed here
either.

**What survives:** the counts in §1 and §3 are correct and independently reverified; the binding
consequence in §5 is correct and remains; the blind-control generalisation in §3 is correct and was
genuinely new. **What does not:** §4's absence sentence, and any reading of §6's "general lesson"
that implies the project had not noticed. It had, first, and said so against its own interest.

### 8.1 And the automated staleness check has a confirmed false negative

`scripts/check-frontier-staleness.sh` does **not** list F-1 — because `h-new-2610-waqf-prosody.md`
carries no `frontier_item:` tag. The script's own printed caveat is therefore not hypothetical:
**absence from its output is not proof an item is open.** F-1 is the first confirmed instance.
A grep on the topic words found it immediately.

### 8.2 Two further corrections inherited from the same lane

- **The map cites *Itqān* nawʿ 27 for waqf; the recension on disk is nawʿ 28** (H-NEW-2610 §0.1,
  verified at line 5092). Third nawʿ-number error found in this repo.
- **The muṣḥaf places no waqf mark at any verse-end at all** — al-Suyūṭī's rule exempts it
  (nawʿ 28, line 5245). So F-1's clause *"grade predicts verse-final rhyme-class stability"* has **no
  verse-final marks to work with**; H-NEW-2610's H2 correctly re-read it as the pre-pause word at
  verse-*internal* marks.

