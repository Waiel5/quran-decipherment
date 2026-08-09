---
title: "H-NEW-3030 — F-8 was not merely null, it was unanswerable: an exact minimum-detectable-effect for the sajdah-locus test, and the surah-level confound cleared"
author: Waiel Al-Shujaa
date: 2026-08-09
status: POWER VERDICT ESTABLISHED (UNDERPOWERED-SEVERE) + NULL (headline) + CENSUS REPLICATED
frontier_item: F-8 (HANDOFF/FRONTIER-MAP-2026-08-07.md:234)
prereg_path: findings/phase-b-hypotheses/prereg-h-new-3030-sajdah-glyph.md
prereg_sha256: 712a98af0126158bd6a283790aeea8778cacd0049ff6573dee090df88d293009
script_path: findings/phase-b-hypotheses/scripts/h-new-3030.py
posthoc_script_path: findings/phase-b-hypotheses/scripts/h-new-3030-posthoc.py
run_dir: findings/phase-b-hypotheses/runs/h-new-3030/20260809T065545Z
run_dir_2_directed_reanalysis: findings/phase-b-hypotheses/runs/h-new-3030/20260809T070603Z
posthoc_run_dir: findings/phase-b-hypotheses/runs/h-new-3030-posthoc/20260809T065803Z
prior_work: [H-NEW-2950, H-NEW-1330, H-NEW-1331, H-NEW-1510]
method_parents: [findings/TIED-OUTCOME-DEFECT.md, findings/ABSENCE-CLAIMS.md, findings/PROXY-CLAIMS.md, findings/UNIT-DRIFT-DEFECT.md]
replicates: H-NEW-2950 (exactly — identical rational p-values on all four cells)
corrects: [briefing framing of the 14-vs-15 dispute (§2.3), H-NEW-2270 nawʿ citation (§2.4)]
flags: [SELF-REPORTED-DESIGN-DEFECT — the registered C2 arm is invalid; see §5]
---

> **Two run directories, both retained.** `20260809T065545Z` is the pre-registered run.
> `20260809T070603Z` re-runs it after a directed change that stripped the non-blind C1 arm of its
> verdict (§4.1). **Both rules return NULL** — the change is verdict-invariant, which is why it can
> be reported at all. Neither directory was deleted or edited.

# H-NEW-3030 — the power F-8 actually had

## Abstract — the power verdict, stated first because the brief required it there

**The sajdah-locus test could not have detected the effect it was looking for.** H-NEW-2950
executed F-8 and returned NULL, adding that "the binding constraint at n = 15 is power, not
p-resolution." **That sentence was never computed.** The three quantities it reported under the
heading *power* are p-value floors, which describe resolution. Power was asserted. Here it is
measured, exactly, on the same pools:

| quantity | value | plain statement |
|:--|--:|:--|
| observed S (imperatives at the 15 loci) | **5** | 57th percentile of its own null |
| null mean | **4.375** | |
| **S\*** — smallest total that clears α | **12** | the observation would have to **more than double** |
| **MDE_q** (80 % power) | **0.25** | all 15 loci must sit in the **top quartile** of their own matched neighbourhood |
| **MDE rate ratio** (80 % power) | **3.25×** | the loci must carry **3.25 times** the imperatives of their matched neighbours |
| **j\*** | **4** | at least four loci must be the **single most imperative-dense verse** in their entire neighbourhood |
| power if every locus sat **above its pool median** | **0.150** | a real, uniform, upper-half effect would be missed **85 % of the time** |

> **Locked verdict: UNDERPOWERED-SEVERE.** The two pre-registered criteria disagreed — the
> quantile criterion returned MODERATE (q = 0.25, exactly at the band edge) and the rate-ratio
> criterion returned SEVERE (3.25 ≥ 3.0). Prereg §6.5 locked *"where the two criteria disagree,
> the more severe verdict is taken"* **before either number existed**, precisely so a disagreement
> could not be resolved in whichever direction proved convenient. It was written for a case exactly
> like this one, and it bound.

**This changes what F-8's NULL means.** H-NEW-2950 said the test *did not* detect marking and that
this is not evidence of absence. The correct, stronger statement is that **the design could not
have detected anything short of a threefold effect**, so the NULL carries almost no evidential
weight against textual marking. *Did not detect* and *could not have detected* are different
claims, and only a computed MDE distinguishes them.

**Headline inferential verdict: NULL**, per the locked rule at prereg §7.4. No arm passed.

**Two results stand independently:**

- **The surah-level confound named in the F-8 brief is CLEARED.** The 14 sajdah-bearing surahs are
  not imperative-dense relative to length-matched surahs (p = 0.1505), and this NULL is the
  *strong* kind: the arm carries a known bias **toward** passing, pre-registered as such, and it
  failed anyway.
- **The census replicates exactly**, third-party, from the glyph — 15 loci, identical to
  H-NEW-2950 and to the manual lists of H-NEW-1330/1510. **No discrepancy exists anywhere in the
  chain.**

**And one defect, self-reported: my own C2 arm is invalid.** See §5. It did not change the verdict,
and it is published at full prominence anyway.

---

## 1. What this finding is, and what it is not

**F-8 was already executed.** `h-new-2950-sajdah-loci.md` (2026-08-08) ran the census and the exact
test. **This finding does not re-litigate that verdict and claims no novelty for reproducing it.**

It exists for the two things the F-8 brief demanded that H-NEW-2950 did not do:

1. **State the power before reporting the result.** H-NEW-2950 asserted a power property without
   computing it — the class of defect named by STANDING RULE 3 of 2026-08-07 (*"Never ASSERT a
   robustness property — COMPUTE it"*) and by `findings/PROXY-CLAIMS.md`.
2. **Contrast a within-surah null against a corpus-wide one.** H-NEW-2950 ran the within-surah null
   only, so the confound the brief named was never actually tested.

### 1.1 The pre-registration was NOT blind, and says so in its own §1

H-NEW-2950 is published and I read it before locking. Concealing that would be worse than the
non-blindness itself, so the pre-registration records it in a table:

| component | blind? | consequence |
|:--|:--|:--|
| **B — power / MDE** | **YES** | Power and S\* are functions of the **null over the pools alone**. Neither depends on the observation. Knowing the observed value cannot bias a quantity it does not enter. |
| **C1 — within-surah** | **NO** | Registered as a **replication**; barred from contributing novelty. |
| **C2, C3** | **YES** | Never run before; no prior observation existed. |

**Locked consequence:** the headline may rest only on B, C2 and C3.

---

## 2. Deliverable A — the census, replicated independently

Re-derived from the glyph with a fresh instrument, not inherited.

**U+06E9 ARABIC PLACE OF SAJDAH (۩) — 15 occurrences in `quran-text/quran-full-tashkeel.json`**
(SHA-256 `382a7341…6b6715`):

| # | locus | # | locus | # | locus |
|--:|:--|--:|:--|--:|:--|
| 1 | **Q 7:206** | 6 | **Q 22:18** | 11 | **Q 38:24** |
| 2 | **Q 13:15** | 7 | **Q 22:77** | 12 | **Q 41:38** |
| 3 | **Q 16:50** | 8 | **Q 25:60** | 13 | **Q 53:62** |
| 4 | **Q 17:109** | 9 | **Q 27:26** | 14 | **Q 84:21** |
| 5 | **Q 19:58** | 10 | **Q 32:15** | 15 | **Q 96:19** |

**15 verses in 14 surahs** {7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}; Q 22 alone
carries two. All three keyed JSON variants agree exactly. All ten Tanzil alt-text files carry 15.

**The truncation defect reproduces**: `quran-flat-full-tashkeel.txt` gives **11** and
`quran-flat-min-tashkeel.txt` gives **13**, against 15 in `quran-flat-no-tashkeel.txt` — the 1 MiB
SQL-dump cut H-NEW-2950 §1.3 diagnosed. Independently confirmed; still unrepaired.

### 2.1 Discrepancy against the manual list — NONE, verified by reading both lists

The frontier map notes that prior sajdah work used a manually supplied list rather than the glyph.
Accurate as to provenance. **I read both prior lists directly rather than accepting H-NEW-2950's
audit of them:**

| finding | set used | source read | agrees? |
|:--|:--|:--|:--|
| **H-NEW-1510** | 15 verses | `prereg-h-new-1510-…md` "Pericope inventory" table | **exact, all 15** |
| **H-NEW-1330** | 14 surahs | `h-new-1330-…md` lines 35-48 | **exact** (the glyph set's surah support) |

**No finding in this repository inherits a sajdah-locus discrepancy.** This is a clean negative
audit and it is worth exactly as much as a positive one.

### 2.2 The 14-vs-15 dispute — verified in the Arabic myself, with the search stated

Per `ABSENCE-CLAIMS.md` §4, the search is stated rather than described. File:
`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`. Command: `grep -n "أربع عشرة"`
→ hit at **line 6783**. Enclosing nawʿ header at line 6386:
`### | النوع الخامس والثلاثون: في آداب تلاوته وتاليه`. Nearest preceding page marker: **PageV01P380**
(line 6778).

> يسن السجود عند قراءة آية السجدة **وهي أربع عشرة** … **وفي الحج سجدتان** …
> **وأما ص فمستحبة وليست من عزائم السجود** … وزاد بعضهم آخر الحجر نقله ابن الفرس في أحكامه.

**al-Suyūṭī — a Shāfiʿī — gives fourteen, counts al-Ḥajj twice, and excludes Ṣād explicitly** as
*mustaḥabba* and not among the *ʿazāʾim*. **Citation: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*,
nawʿ 35, V01 p. 380.** Verified by me on disk; not taken from H-NEW-2950, which reports the same
locus and is correct.

I did **not** verify a Ḥanafī primary text on disk and do not assert one exists. The union reading
rests on al-Suyūṭī plus the glyph, both verified.

### 2.3 CORRECTION TO THE BRIEFING — the framing that dispatched this work is wrong

**This is recorded as a correction of record, not a footnote.** The briefing that commissioned
H-NEW-3030, and `HANDOFF/FRONTIER-MAP-2026-08-07.md:238` before it, framed the dispute as:

> *"The 14 vs 15 sajdah dispute (Ḥanafī vs Shāfiʿī counts; Q 38:24 and Q 22:77)."*

**That is the textbook summary. It is not what the on-disk Arabic says**, and the *Itqān* passage
at nawʿ 35 supersedes it on three specific points:

| the framing says | al-Suyūṭī actually writes |
|:--|:--|
| the Shāfiʿī count is **15** | al-Suyūṭī, **a Shāfiʿī**, gives **fourteen** |
| Q 22:77 is **contested** | it is **in** — he says *wa-fī l-Ḥajji sajdatān*, two prostrations in al-Ḥajj |
| Q 38:24 is **contested between schools** | he **excludes** it from the *ʿazāʾim* while still holding prostration there *mustaḥabba* — a distinction of **degree**, not a dispute over membership |

> **The muṣḥaf's 15 is neither school's legal count. It is their union** — every place prostration
> is performed, whether *ʿazīma* or merely *mustaḥabba*. Ṣād is the fifteenth glyph precisely
> because al-Suyūṭī still holds prostration there to be recommended. **The glyph marks the act,
> not the ruling's strength.** And the set has a verified upper boundary: al-Suyūṭī records a
> sixteenth candidate (end of al-Ḥijr, **Q 15:98**, from Ibn al-Faras) which **carries no glyph in
> any variant on disk**.

**The citation of record is: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 35
(*fī ādāb tilāwatihi wa-tālīhi*), V01 p. 380.** It supersedes the Ḥanafī/Shāfiʿī framing wherever
that framing appears.

### 2.4 Where the framing propagated — and a wrong-nawʿ citation found on the way

Repo-wide grep over `findings/`, `surahs/`, `HANDOFF/` and the root docs. **Pre-registrations are
listed but MUST NOT be edited** — they are immutable even when wrong, and a prereg citing a
since-corrected claim is not an error to repair (`UNIT-DRIFT-DEFECT.md` §9.1). Correcting a prereg
would destroy the very thing that makes it evidence.

| file | what it says | class |
|:--|:--|:--|
| **`HANDOFF/FRONTIER-MAP-2026-08-07.md:238`** | *"Ḥanafī vs Shāfiʿī counts; Q 38:24 and Q 22:77"* | **editable — the source that propagated into the brief** |
| `surahs/Q041-fussilat/03-tafsir-survey.md:92` | *"minor count (14 vs 15)"* | editable, vague rather than wrong |
| `surahs/Q032-al-sajda/Q032-F-06-…-prereg.md:88` | *"14 vs 15 vs Shafi'i 14+1"* | **PREREG — do not edit** |
| `findings/…/prereg-h-new-1510-…md:98` | *"Classical-Sunnī 14 … + Q 22:77 (widely held in Shāfiʿī school) = 15"* | **PREREG — do not edit** |
| `findings/…/prereg-h-new-2270-…md:74` | *"Shāfiʿī count, Itqān **nawʿ 19**"* | **PREREG — do not edit** |
| **`findings/…/h-new-2270-itqan-distributional-audit.md:90`** | *"Sajda verse-list (14, Shāfiʿī): al-Itqān **nawʿ 19**, lines 6783-6786"* | **editable — and wrong on the nawʿ** |

**The wrong-nawʿ citation is a separate error and worth more than the framing one.** H-NEW-2270
cites **the same lines I verified** — 6783-6786 — but attributes them to **nawʿ 19**. Verified
against the file's own headers:

| | |
|:--|:--|
| **nawʿ 19** = `في عدد سوره وآياته وكلماته وحروفه` (*on the number of its surahs, verses, words and letters*) | lines **4022-4372** |
| **nawʿ 35** = `في آداب تلاوته وتاليه` (*on the etiquette of its recitation and its reciter*) | lines **6386-6982** |

**Line 6783 lies inside nawʿ 35, sixteen nawʿ away from the one cited.** The error is
understandable — nawʿ 19 is the *counting* nawʿ, exactly where a reader would expect a sajdah
tally to live — but it is not there.

**Two independent citation errors now attach to this one passage**: H-NEW-1510 cites a nawʿ that
does not exist (caught by H-NEW-2950 §3.1a), and H-NEW-2270 cites nawʿ 19 (caught here, and
**missed** by H-NEW-2950's audit). **A passage that three findings have cited and two have cited
wrongly is a signal about citation practice, not about this passage.** The line numbers travelled
correctly every time; only the human-readable locus drifted. Line offsets are checkable
mechanically and nawʿ numbers are not, which is precisely why the unchecked field is the one that
rots.

**I have edited none of these files.** They belong to other lanes; the list is reported for the
ledger keeper, per `ABSENCE-CLAIMS.md` §4 (*a correction that lands only in the child finding does
not stop the parent from being inherited again*).

---

## 3. Deliverable B — the power computation

### 3.1 Why an exact computation was mandatory, not a preference

`TIED-OUTCOME-DEFECT.md` §5 requires the tie fraction be stated in the pre-registration and a
parametric choice justified against it. Measured over all 6,236 QAC verses, `ROOT:sjd` removed:

| outcome | tied at zero | fraction |
|:--|--:|--:|
| **F1 imperative, per verse** | 4,967 / 6,236 | **0.7965** |
| **F2 second-person, per verse** | 3,177 / 6,236 | **0.5095** |

**Both exceed the 50 % threshold at which that rule forbids a parametric p.** No parametric test
appears anywhere in this design — not as a primary, not as a secondary. It also forecloses the
conventional route to power: at a 79.65 % tie fraction there is no usable normal approximation to
invert for a sample-size formula, so power had to be convolved exactly or not computed at all.
**That is very likely why H-NEW-2950 asserted it instead.**

### 3.2 The null is built from large atoms — the signature of a blind design

Exact null of S over the full product space of **1,152,921,504,606,846,976** tuples:

| S | 0 | 1 | 2 | **3** | **4** | **5** | 6 | 7 | … | **12** |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|:-:|--:|
| P | .0242 | .0745 | .1330 | **.1677** | **.1671** | **.1418** | .1084 | .0760 | … | .0037 |

The entire null lives on the integers 0-26, and **16.8 % of its mass sits on the single value
S = 3**. The observed **S = 5** is the 57th percentile. **S\* = 12** is the 99.73rd.

> A null distribution supported on a dozen integers with atoms of 17 % cannot resolve a moderate
> effect. This is what "n = 15" costs, made concrete.

### 3.3 B1 — the quantile alternative (primary power model)

Under H_A(q) each locus draws uniformly from the **top ⌈q·16⌉ members of its own pool by value**.
q = 1 recovers the null; q → 0 places every locus at its pool maximum.

| where every locus sits in its own neighbourhood | q | **power** |
|:--|--:|--:|
| pool maximum | 0.0625 | 1.000 |
| top 3 of 16 | 0.1875 | 1.000 |
| **top quartile** | **0.2500** | **0.902** |
| top 5 of 16 | 0.3125 | 0.705 |
| top 6 of 16 | 0.3750 | 0.432 |
| **upper half (above the pool median)** | **0.5000** | **0.150** |
| top 12 of 16 | 0.7500 | 0.025 |
| no effect | 1.0000 | 0.006 |

> **MDE_q = 0.25.** Eighty-percent power requires **all fifteen loci simultaneously in the top
> quarter** of their own surah- and length-matched neighbourhoods. **If every locus sat merely
> above its pool median — a real, uniform, correctly-directed effect — this design would miss it
> 85 % of the time.**

### 3.4 B2 — the exponential tilt (rate-ratio form)

Tilting each pool by `p_θ(x) ∝ p_0(x)·e^{θx}` and bisecting to 80 % power gives **θ\* = 1.0018**
and

> **MDE rate ratio = 3.254.** The sajdah loci must carry **3.25 times** the imperative density of
> their matched neighbours before this design reaches 80 % power.

For scale: the muqaṭṭaʿāt book-reference law — the strongest surviving claim in this project — has
an honest rate ratio between **1.27 and 2.58** (INVESTIGATION-PROTOCOL correction notice,
2026-08-07). **This design could not have detected an effect as large as the strongest law the
project has established.** That single comparison is the finding.

### 3.5 B3 — the lit-locus count, model-free

Every one of the fifteen pools has **modal value zero**, so the modal configuration gives S = 0.
Promoting loci to their pool maximum, largest gain first, until S ≥ S\* = 12:

> **j\* = 4**, and the four are **Q 7:206, Q 19:58, Q 22:18, Q 22:77**.

**At least four of the fifteen loci must be the single most imperative-dense verse in their entire
matched neighbourhood before this design can register anything at all** — and the four are fixed
by the pools, not chosen. Meanwhile **12 of the 15 loci carry zero imperatives** once the
prostration verb is removed. The design asks for a near-maximal configuration from a set that is
mostly empty.

---

## 4. Deliverable C — the arms, and an exact replication

**Only C2 and C3 carry verdicts.** C1 is non-blind and was stripped of its verdict (§4.1).

| arm | axis | observed | null E | **p (exact, raw)** | p Bonf. | direction | status |
|:--|:--|--:|--:|--:|--:|:-:|:--|
| **C1 within-surah, K=15** | F1 imperative | 5 | 4.375 | 0.4335 | — | as locked | **reproduction check — MATCHES** |
| C1 within-surah, K=15 | F2 second-person | 23 | 20.375 | 0.3588 | — | as locked | reproduction check — **MATCHES** |
| C1 within-surah, K=10 | F1 imperative | 5 | 4.818 | 0.5065 | — | as locked | reproduction check — **MATCHES** |
| C1 within-surah, K=10 | F2 second-person | 23 | 20.818 | 0.3836 | — | as locked | reproduction check — **MATCHES** |
| **C2 corpus-wide, K=15** | F1 imperative | 5 | 7.062 | 0.8041 | 1.000 | **reversed** | **NULL — and arm invalid, §5** |
| C2 corpus-wide, K=15 | F2 second-person | 23 | 43.188 | 0.9744 | 1.000 | **reversed** | **NULL — and arm invalid, §5** |
| **C3 surah-level, K=7** | **F1 imperative** | 340 | 306.500 | **0.1505** | 0.903 | as locked | **NULL** |
| C3 surah-level, K=7 | F2 second-person | 1,884 | 1,935.500 | 0.6083 | 1.000 | reversed | NULL |

**Headline verdict: NULL, under both rules.** The pre-registered rule of prereg §7.4 returns NULL;
so does the directed variant that drops C1 entirely. **The change is verdict-invariant**, which is
the only condition under which a post-registration change to a decision rule can be reported
without contaminating it — it cannot have bought or cost a result.

**Bonferroni stayed at k = 6.** Stripping C1 of its verdict would nominally shrink the family to
4 and raise α from 0.00833 to 0.0125. **It was not shrunk.** Tightening a correction
self-verifies; loosening one after seeing the design is a ratification-level change
(`feedback_bonferroni_tightening_vs_loosening`). k = 6 is conservative here and stands, and the
script asserts it (`self_check`).

### 4.1 C1 is a reproduction check, not a test — and it reproduces exactly

**C1 carries no verdict and is excluded from the family gate.** H-NEW-2950's observed values were
known to me before this pre-registration was locked (§1.1), so C1 is a reproduction, and **a
reproduction either matches or it does not — it cannot PASS or NULL.** The exact p is still
computed and reported, because the p *is* the thing being checked; it simply carries no
inferential weight.

**All four cells reproduce as identical rational numbers**, not merely to published decimals —
compared as stored `p_exact_fraction` strings across the two run directories:

| cell | H-NEW-2950 exact fraction | H-NEW-3030 | identical? |
|:--|:--|:-:|:-:|
| F1, K=15 | `30506516276467/70368744177664` | same | **yes** |
| F2, K=15 | `103430023058136545/288230376151711744` | same | **yes** |
| F1, K=10 | `144511451267/285311670611` | same | **yes** |
| F2, K=10 | `1602388022378716/4177248169415651` | same | **yes** |

**H-NEW-2950's arithmetic is sound.** Its instrument was reused deliberately: a reproduction that
changes the instrument is not a reproduction, and any divergence would have been uninterpretable —
instrument difference, or effect?

**What C1 is actually for, now that it carries no verdict:** it authenticates the pools. The whole
power computation (§3) is a function of those pools, so a bit-exact reproduction of the p-values
they generate is the evidence that the MDE below describes H-NEW-2950's real design and not a
near-miss rebuild of it.

**One consequence must be stated plainly.** With C1 out, the only verdict-bearing arms are C2 and
C3 — and both are *confound-diagnostic* arms whose passes are locked as evidence **against** F-8,
never for it. **So the inferential half of this finding has no route to a PASS for F-8 by
construction.** That is the correct design given the non-blindness, but it means the power
computation is the only component here that speaks to F-8 itself.

### 4.2 C3 — the named confound is cleared, and this is the strong kind of NULL

The F-8 brief named the confound: *sajdah verses may simply be in surahs with high imperative
density overall.* Tested directly — 14 sajdah surahs against pools of the 7 nearest-length
non-sajdah surahs:

> **340 imperatives observed against 306.5 expected. p = 0.1505. NULL.**

**The pre-registration recorded, before the run, that this arm is biased *toward* passing** —
sajdah surahs are long, so their length-matched pools skew shorter (realised mean |Δ| = 118.7
words, max 1,487) and the observed sum is inflated. It failed anyway.

> **A NULL under a bias toward passing is stronger than a NULL under a neutral one.** The
> surah-level channel does not carry the effect. F-8's confound is not the explanation for its
> failure; there is simply nothing at this scale either.

Had C3 passed it would have been **ambiguous** between surah-level marking and length bias, and the
prereg locked that reading in advance too. That asymmetry is why the direction of the bias was
recorded before the number existed rather than after.

---

## 5. SELF-REPORTED DEFECT — my registered C2 arm is invalid

**The C2 corpus-wide arm as pre-registered does not measure what it claims to.** I found this
after the run, by auditing my own control for tautology (STANDING RULE 4, 2026-08-07). Reporting
it at full prominence.

**The mechanism.** Prereg §10 decision 7 broke ties in |Δlength| **deterministically by
(surah, verse) ascending**, chosen so that no seed would enter pool construction. Corpus-wide,
that criterion is almost never binding: every locus has between **18 and 417 exact length
matches**. So the tie-break — not the length criterion — selects the pool, and "earliest in the
mushaf" means **al-Baqara**.

| | |
|:--|--:|
| pool members drawn from **Q 2 alone** | **118 / 225 = 52.4 %** |
| loci whose **entire pool** comes from a single surah | **4 of 15** |
| distinct source surahs across all 225 members | 14 |

Al-Baqara is the longest, most legal, most heavily second-person surah in the corpus. That is the
whole of C2's inflated null: **E[F2] = 43.19 against C1's 20.375.** The "reversal" C2 reports is
substantially an artefact of my own tie-break rule.

**The repaired arm** (post-hoc, not gated, `runs/h-new-3030-posthoc/20260809T065803Z/`): each null
draw takes a verse uniformly at random from **all** non-sajdah verses within ±1 word of the target,
so no ordering can enter. 200,000 draws, seed 20260509.

| axis | observed | registered C2 E | **repaired E** | obs/exp | p (repaired) |
|:--|--:|--:|--:|--:|--:|
| F1 imperative | 5 | 7.062 | **5.109** | **0.979** | 0.550 |
| F2 second-person | 23 | 43.188 | **31.685** | **0.726** | 0.818 |

> **F1 lands essentially exactly on its null (ratio 0.979).** The registered arm's apparent
> deficit was manufactured. F2 remains modestly below expectation but at 0.73×, not 0.53×.

**Three things must be said plainly:**

1. **The headline verdict is unchanged.** C2 failed as registered and fails repaired; the rule at
   §7.4 returns NULL either way. **The defect did not buy or cost a result** — which is why it can
   be reported without any suspicion that reporting it was convenient.
2. **I did not edit the pre-registration.** STANDING RULE 1 of 2026-08-08 forbids editing a
   pre-registration after its run *for any reason, including to correct an error in it*. The
   correction lives here, in the finding, as that rule directs. The prereg still contains the
   defective decision 7, and should.
3. **The lesson generalises beyond this finding.** Decision 7 traded a seed for determinism and
   got a systematic mushaf-order bias in exchange. **A deterministic tie-break is only neutral
   when ties are rare.** Any matched-pool design in this project whose matching variable is
   coarse — verse length, verse count, surah length — is exposed to the same failure, and the
   detection is one line: count how many candidates tie at the optimum before trusting the pool.

---

## 6. Honest limits

1. **The MDE is a property of this design, not of the question.** It says the H-NEW-2950
   instrument at n = 15 cannot see below ~3.25×. A different instrument — pericope-scoped units,
   a continuous score rather than a raw count, or the 15 loci pooled with near-sajdah verses —
   could have more power. **F-8 is not shown to be unanswerable in principle, only unanswered by
   this test.**
2. **Two alternative families, not all of them.** The quantile and tilt models were locked in
   advance and disagreed on the severity band. A different alternative would give a different MDE.
   The full power curve is published (§3.3) so any reader may apply their own threshold or model.
3. **C1 is not a blind arm** (§1.1) and contributes no novelty. Its value here is that it
   reproduces exactly, which authenticates the pools the power computation runs on.
4. **C2 as registered is invalid** (§5). The repaired version is post-hoc and cannot support any
   verdict.
5. **C3's length match is poor** — mean |Δ| = 118.7 words against a mean surah length far larger.
   Only 5.1 % of pool members are within 2 words. The arm is a coarse instrument and its NULL
   should be read as "no large surah-level effect", not "no surah-level effect".
6. **α rendering.** Prereg §7.3 defines α = 0.05/6 and §7.4 renders it as the literal `0.00833333`.
   The script uses 0.05/6 = 0.0083333…, looser than the rendering by 3.3 × 10⁻⁹. No p in this run
   falls in that interval — the smallest is 0.1505 — so nothing turns on it. Recorded rather than
   glossed.
7. **F3 (divine names) was dropped**, on the strength of H-NEW-2950's post-hoc showing it circular.
   That reduced k from 9 to 6 and **tightened** α, which self-verifies under
   `feedback_bonferroni_tightening_vs_loosening`. But it means this finding says nothing about the
   divine-name axis.
8. **Nothing here bears on recitation practice.** The classical claim concerns when a reciter
   prostrates; this measures text.

---

## 7. What this settles, and what it queues

**Settled:**
- **F-8's design was UNDERPOWERED-SEVERE**: MDE 3.25×, S\* = 12 against an observation of 5, and
  15 % power against a uniform upper-half effect. **The NULL is not evidence of absence, and now
  there is a number saying how far from evidence it is.**
- **The surah-level confound is cleared** (p = 0.1505, under a bias toward passing).
- **The census replicates exactly** and **no discrepancy exists** between the glyph and any manual
  list in the repository.
- **al-Suyūṭī's fourteen is verified in the Arabic** at nawʿ 35, V01 p. 380 — independently of
  H-NEW-2950.
- **A deterministic tie-break silently converted a corpus-wide null into an al-Baqara null**
  (§5), and the detection is a one-line candidate count.

**Queued — each needs its own prospective pre-registration:**
- **H-NEW-3031** — an audit sweep for the §5 tie-break defect across every matched-pool design in
  the repository. The screen is mechanical: for each pool, count candidates tying at the optimum.
- **H-NEW-3032** — F-8 re-run at pericope scale, where H-NEW-1510 already found structure, with
  the MDE computed **first** so the design is chosen to have power rather than discovered not to.
- **H-NEW-2953** (from H-NEW-2950, still open) — repair or delete the two truncated flat files.

---

## Sources

- `findings/phase-b-hypotheses/prereg-h-new-3030-sajdah-glyph.md` — SHA-256 `712a98af…d293009`.
- Run: `findings/phase-b-hypotheses/runs/h-new-3030/20260809T065545Z/{result,manifest}.json`.
- Post-hoc: `findings/phase-b-hypotheses/runs/h-new-3030-posthoc/20260809T065803Z/{result,manifest}.json`.
- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4, SHA-256 `a1d12923…5d8c46`.
- `quran-text/quran-full-tashkeel.json` — SHA-256 `382a7341…6b6715`.
- `quran-text/quran-no-tashkeel.json` — SHA-256 `253f72f3…35918a`.
- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` — nawʿ 35 header at line
  6386, masʾala at line 6783, page marker PageV01P380.
- Prior work: `h-new-2950-sajdah-loci.md`, `h-new-1330-sajda-surahs-cluster.md`,
  `prereg-h-new-1510-sajda-pericope-replication.md`.
- Method: `findings/TIED-OUTCOME-DEFECT.md` §5, `findings/ABSENCE-CLAIMS.md` §4,
  `findings/PROXY-CLAIMS.md`, `HANDOFF/CONTINUE-PROMPT.md` STANDING RULES 2026-08-07 §§1,3,4 and
  2026-08-08 §1.
- Frontier: `HANDOFF/FRONTIER-MAP-2026-08-07.md:234` (F-8).
