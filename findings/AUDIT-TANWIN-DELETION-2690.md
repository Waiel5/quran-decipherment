# Audit: the scansion instrument deletes 77.66% of the Quran's nunation, and its positive control could not have caught it

**Date:** 2026-08-10
**Status:** VERIFIED DEFECT, undischarged since 2026-08-08. Affects H-NEW-2690 and H-NEW-2730.
**Found:** by the F-2 lane at Step 0; logged earlier by H-NEW-2870 §1.1 addressed to *"whoever owns
those findings"* and never actioned. Every figure below independently reverified before publication.

---

## 1. The defect

`findings/phase-b-hypotheses/scripts/h-new-2690.py` defines a `DROP` set of characters discarded
before syllabification. It contains **U+0656, U+0657 and U+065E**.

Unicode names those *ARABIC SUBSCRIPT ALEF*, *ARABIC INVERTED DAMMA* and *ARABIC INVERTED SMALL V*.
**In the Uthmānī encoding they are tanwīn** — kasratān, fatḥatān and ḍammatān respectively.

Counted directly in `quran-text/quran-full-tashkeel.json`:

| codepoint | role in Uthmānī encoding | count |
|:--|:--|--:|
| U+0656 | tanwīn kasr | 1,935 |
| U+0657 | tanwīn fatḥ | 2,901 |
| U+065E | tanwīn ḍamm | 1,807 |
| **dropped total** | | **6,643** |
| U+064B/C/D | classic tanwīn, correctly handled | 1,911 |

> **6,643 of 8,554 tanwīn — 77.66% of the corpus's nunation — are deleted before any syllable is
> weighed.**

## 2. Why it matters specifically for prosody

Tanwīn is a **consonantal** ending (*-an*, *-un*, *-in*). Deleting it changes syllable weight
directly, which is the quantity being measured.

Worse, it is the exact operation **pausal reduction** performs. H-NEW-2690 ran three pausal tuples —
`P_forceheavy`, `P_pausal`, `P_none` — to contrast the presence and absence of pausal rules. But the
`DROP` set removes 77.66% of the tanwīn **in all three, before any pausal rule executes.** The
contrast the design rested on was substantially vacuous on the tanwīn channel.

## 3. The part worth generalising: the positive control was structurally blind

H-NEW-2690's hard gate was the muʿallaqāt — three vocalised pre-Islamic poems, scanned at 0.771
per-*bayt* accuracy, 3 of 3 poems correctly identified. That gate passed, and it could not have
failed:

| corpus | affected codepoints | classic tanwīn |
|:--|--:|--:|
| muʿallaqa (ʿAmr b. Kulthūm) | **0** | 114 |
| muʿallaqa (ʿAntara) | **0** | 93 |
| muʿallaqa (al-Ḥārith) | **0** | 102 |
| **Quran (full tashkeel)** | **6,643** | 1,911 |

**The scanner deletes 77.66% of the Quran's tanwīn and 0% of the control corpus's.** The control
exercises only the classic codepoints, which the scanner handles correctly.

> **A positive control validates an instrument only on the encoding features that the control corpus
> exercises.** The Uthmānī muṣḥaf uses codepoints that pre-Islamic poetry files never use, so no
> amount of accuracy on the muʿallaqāt could have surfaced this.

This is a distinct failure from anything in [[cross-finding-029-the-deciding-parameter]]. There, a
free parameter decided a verdict. Here, **the validation instrument and the target corpus do not
overlap on the feature that broke** — the control is not wrong, it is *inapplicable*, and nothing
announces that.

## 4. The fix already exists and has never been back-applied

`scripts/h-new-2990.py` line 146 carries the repaired mapping, written per H-NEW-2870 prereg §4.1:

```python
TANWIN_REMAP = {"ٗ": FATHATAN, "ٞ": DAMMATAN, "ٖ": KASRATAN}
```

It remaps rather than drops. It has never been applied to H-NEW-2690 or H-NEW-2730.

## 5. Scope — what this does and does not put in question

**It does not automatically overturn either finding.** H-NEW-2730 independently demoted H-NEW-2690's
central claim by a *matched-length* control (re-cutting the Quran's own verses to ḥadīth sentence
lengths moves the statistic 99.4% of the way to ḥadīth, using no baseline text at all). That
demolition does not depend on syllable weights being right.

**What is in question is every quantity computed from syllable weight** — the meter-matching results,
the three pausal tuples, and the per-*baḥr* comparisons. Those need re-running under the repaired
phonemiser before any of them is cited again.

Recorded as **R2** on the F-2 lane's residual list: an instrument-repair replication with a known fix,
not a new hypothesis.

Related: [[cross-finding-029-the-deciding-parameter]] · [[PROXY-CLAIMS]] ·
[[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]] (the same corpus, a different encoding divergence)

---

## 6. The defect is Qurʾān-SPECIFIC, so every comparison in the family was asymmetric

Counting the affected codepoints in each comparison arm sharpens §3 considerably:

| arm | affected codepoints | classic tanwīn |
|:--|--:|--:|
| **Qurʾān** | **6,643** | 1,911 |
| muʿallaqa (ʿAmr b. Kulthūm) | **0** | 114 |
| muʿallaqa (ʿAntara) | **0** | 93 |
| muʿallaqa (al-Ḥārith) | **0** | 102 |
| Sunan al-Dārimī | **0** | 15,798 |
| Ṣaḥīḥ al-Bukhārī | **0** | 46,606 |

*(Verified here: the Qurʾān row and the three muʿallaqāt. The two prose rows are the F-2 lane's
figures — my file glob did not resolve those corpora and I did not confirm them.)*

**Every corpus the Qurʾān was compared against loses zero tanwīn. The Qurʾān loses 77.66%.** So every
poetry-vs-Qurʾān and prose-vs-Qurʾān comparison in this family was **asymmetric, in one direction,
on one side only.**

This is also the precise reason §3's blind control was blind: **the muʿallaqāt do not exercise the
encoding that broke.** The two facts are the same fact seen from either end.

## 7. The repair replication is pre-registered — and its primary target is the family's only survivor

`prereg-h-new-3140-tanwin-repair-replication.md`, SHA `3c896203…5779a0`, typed as an
**instrument-repair replication**: no hypothesis is restated or reopened, and H-NEW-2690's
pre-registration is not edited.

Two features worth recording as method:

**It names, before running, the result it cannot claim.** §0 states that the repair cannot rescue
H1b, and gives the mechanical reason: H-NEW-2730's demolition rests on a *within-corpus self-recut*
and a *matched-length bin*, both invariant to a uniform phonemiser change because **both sides move
together**. A length-driven artefact does not stop being length-driven because the weights beneath it
changed. The prereg says outright: *"If this run returns 'conclusion unchanged' on D8, that is the
expected result and must not be reported as a vindication of H1b."*

**Its primary target is the one thing it can legitimately destroy.** Because the defect is
Qurʾān-specific and every comparison arm is clean, the arm most exposed to repair is **H1a — the
family's sole surviving result.** If the primary target fires `CONCLUSION-CHANGED`, the honest
summary of the entire scansion family becomes *nothing survives*.

**And it carries a void condition.** Self-check S4: the *defective* arm must reproduce the
2026-08-07 published values exactly. **If S4 fails, the run is void and no repaired number is
reported at all** — the harness must be shown to reproduce the original before any corrected figure
is trusted.

