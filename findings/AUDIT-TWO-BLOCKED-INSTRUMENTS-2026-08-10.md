# Audit: two frontier items blocked at Step 0 by their own instruments

**Date:** 2026-08-10
**Status:** F-13 CLOSED as already-answered (sixth staleness case). F-12 coverage-framing BLOCKED.
**Both found before any pre-registration was written.** No lane was spent on either.

---

# Part I — F-13 is H-NEW-3000, and the brief's data path was wrong

## 1. The staleness case

The frontier map defines F-13 as: citation count per verse is *"independent of every structural axis
the project has built — and the **residual** … is where the interesting verses live."*

**That sentence is the title of `h-new-3000-reception-residual-rosters.md`**, run the previous day.
Both rosters are on disk. `OPEN-H-NEW-2980-reception-residual.md` already reads CLOSED.

Sixth confirmed staleness case, after F-3, F-4, F-5, F-8 and F-10.

Its verdict pair is worth quoting because it is the pattern this project keeps rediscovering:
`verdict_locked: SUPPORTED` / `verdict_after_exact_tests: NULL`. Three of six arms cleared on
parametric p; `n_hadith` is **86% tied at zero**, making those p-values 13–57× too liberal; under an
exact null only one arm survived, and it collapsed when surah-mean-centred.

## 2. My brief's data path did not exist as described — my error

I briefed the lane to use `data/literature/hadith/` with *"pre-indexed Q{NNN}-citations.md files."*
It holds **six** files, in three formats, for exactly **Q1, Q2, Q6, Q9, Q19, Q33** — the project's
own deep-dive set — and they are **named-entity regex searches over surah *names***, per-surah, not
per-verse.

Built on those, F-13's outcome variable would have been **the project's own research history**. That
is precisely the failure `h-new-1780` documented in its own limits: it measures *"the grade-mix of
citations the project has made."* The lane caught it only because Step 0 forced `ls` before design.

**The real instrument is clean and is a different file.** `csv/h-new-860-1-reception-weights.csv`
(6,236 rows) is a mechanical verbatim distinctive-span match over a 50,884-record scrape of the nine
canonical books. Independently reverified: all 114 surahs scanned, 99 with ≥1 citation, **15 with
zero**; 749 of 5,371 eligible verses carry any citation (**13.95%**; 86.05% tied at zero).

## 3. What is genuinely new — a 15× incipit channel inside a published NULL

Descriptive only. No test, no p, no pre-registration. Recomputed here from the CSV, every figure
reproducing the lane's report exactly:

| | verse 1 of a surah | every other verse |
|:--|--:|--:|
| rows in the analysis set | **58** (1.1%) | 5,313 |
| share of all 3,147 citations | **14.1%** (445) | 85.9% |
| citations per verse | **7.67** | 0.51 |
| proportion cited at all | **50.0%** | 13.6% |

**A 15.1× rate ratio on 1.1% of the data.** Seven of the twenty most-cited verses are verse 1
(112:1, 87:1, 109:1, 64:1, 113:1, 88:1, 114:1).

**Mechanism.** Ḥadīth identify a surah by its opening words — *"he recited qul huwa Llāhu aḥad"* — so
a verbatim-span instrument scores the incipit as reception of *that verse*. H-NEW-3000 §7.5 notes
reception is "verbatim quotation and explicit naming" and §5 observes two of these are liturgical
incipits, but **the channel is nowhere quantified, and stratification was on `n_words` only, never
on verse position.**

**This does not reopen F-13.** An uncontrolled channel inflating a variable that returned NULL makes
the NULL *more* secure, not less. It is a candidate confound sitting inside a null result, and it
would need its own pre-registration to become anything more.

---

# Part II — F-12's asbāb instrument is truncated exactly where the hypothesis lives

## 4. The truncation

`data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/` — the only
asbāb-specific source on disk. Verified independently:

> **Surahs present: 1–77, no gaps. Absent: 78–114, all 37.**
> Phase of the absent block: **35 Early Meccan, 2 Medinan.**

This is a scrape boundary, not a property of al-Wāḥidī. His printed *Asbāb* covers Q 80 (Ibn Umm
Maktūm), Q 93 (the *fatra*), Q 96 (the first revelation), Q 108 and Q 111 — among the most famous
asbāb in the entire genre. All absent.

## 5. Why this is fatal rather than merely limiting

A coverage variable built here **is the indicator `surah ≤ 77`**. It would predict chronology at
enormous effect size, because juzʾ 30 is where Early Meccan lives.

> **Had the pre-registration been written first, F-12 would have produced a spectacular false
> positive** — and one whose direction flatters the hypothesis, which is the category this project
> has repeatedly found survives longest unaudited.

This is [[ABSENCE-CLAIMS]] in its purest form: **absence of data read as data about absence.**

And it is worse than an ordinary confound. Present-surah phase mix is 52 Meccan / 25 Medinan; absent
is 35 Early Meccan / 2 Medinan. **The truncation and the substantive confound are collinear** — so
"the tradition attends to Medinan legal verses" and "the scraper stopped at 77" are, on this data,
*the same variable*. They cannot be separated by any estimator.

## 6. Second defect, already on record: the directory is a blend

`PROXY-CLAIMS.md` §384–486 audited this same folder on 2026-08-08 and found **~72% is not
al-Wāḥidī** but Maybudī's Persian Sufi commentary *Kashf al-asrār* — settled by the death-date test,
since Anṣārī (d. 481) is quoted where al-Wāḥidī died in 468.

An independent re-classification found **353 entries (32.4%) with al-Wāḥidī isnād formulae, 393
(36.1%) Sufi register, 341 (31.3%) neither — a 31.5% ambiguous fraction.** All seven verses of Q 1
are the Sufi text. The two classifications disagree on the split but agree the directory is a blend.

## 7. The two rules-tuples are not independent

The brief specified Nöldeke and the Egyptian standard as two chronology tuples. `PROXY-CLAIMS.md`
§192–243 already records **ρ = +0.7714, Kendall τ = +0.5771** between them. They must be reported as
a 0.77-correlated pair, not as a clean tuple — a point that also applies to
[[h-new-3070-deictic-gradient]], whose verdict flipped between exactly these two instruments.

---

## 8. What both parts share

Neither lane was blocked by its hypothesis. Both were blocked by **what the data turned out to be**,
and in both cases the brief — mine — asserted a data path without checking it.

> **Step 0 was written to catch re-derivation. It caught two instrument failures instead**, and both
> would have produced publishable, well-formed, wrong results. F-13's would have measured this
> project's own reading history; F-12's would have measured a scrape boundary.

The generalisation for future briefs: **`ls` the path before writing it into a brief.** A data line
in a dispatch document is a claim, and it has now been wrong twice in one day.

Related: [[ABSENCE-CLAIMS]] · [[PROXY-CLAIMS]] · [[cross-finding-029-the-deciding-parameter]] ·
[[AUDIT-WAQF-MARK-INVENTORY-DIVERGENCE]] · [[AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE]]

---

## 9. An open flag, and a check I attempted and failed to run properly

H-NEW-3120 §4.0 raises a live problem with the **MW-2 domain split** — the standing rule that Nöldeke
chronology is a *pseudo*-confound on structural axes but a *genuine* axis on lexical-content ones.

The complication: **ρ(mean verse length, Nöldeke phase) ≈ +0.79 to +0.91**, and mean verse length is
a **structural** property. So at surah granularity a lexical correlation with phase is also, to
within that ρ, a correlation with a structural quantity. **The partition does not separate cleanly.**
This does not refute MW-2 and touches nothing about its anchor directly.

The obvious cheap check is whether MW-2's anchor case — the kitāb/qurʾān axis, published at
**z = −3.75** — survives a mean-verse-length control. **I attempted it and the attempt failed, for a
reason worth recording.**

I reconstructed the axis as `ROOT:{ktb, qrA, Ayy, nzl}` tokens per 1,000 tokens and tested a
Medinan-minus-Meccan contrast over 110 phase-labelled surahs. Result: observed −0.239 per 1,000,
**unstratified p = 0.4822**, stratified on mean-verse-length quintiles p = 0.0794.

**That does not reproduce the published anchor, so it is not a test of it.** Two reasons my
reconstruction is the wrong instrument, both findable in one grep:

1. `cross-finding-012` defines the axis as *"kitāb/qurʾān/āyāt/nazala root tokens **per 100
   verses**"* — a per-verse denominator, not per-token. Different unit, and [[UNIT-DRIFT-DEFECT]]
   exists because that difference is not cosmetic.
2. The same file records the axis as **ρ = +0.574, INVERTED-U, peaking Late Meccan** — so its
   published shape is *not* a monotone Meccan/Medinan contrast. **I tested a two-group difference on
   an axis whose own documentation says it peaks in the middle.** A null was guaranteed by the design
   before any data was involved.

**This is the hand-built-proxy defect** ([[PROXY-CLAIMS]]) committed by the person who spent the day
warning lanes about it: I substituted my own reconstruction for a published instrument and tested the
substitute. The p-values above are arithmetically correct and answer a question nobody asked.

**Status: the flag stands OPEN.** Answering it requires H-NEW-125's actual axis-9 definition and its
computed values, not a reconstruction — and it must test the inverted-U shape the axis actually has.
It remains cheap, and it remains worth doing.

---

## 10. The MW-2 check, run properly — and the anchor citation conflates two instruments

§9 recorded a failed attempt. This is the corrected one, and it produced two results.

### 10.1 The citation is wrong before any statistics

H-NEW-3120 §4.0 describes MW-2's anchor as *"the kitāb/qurʾān axis at z = −3.75."* **Those are two
different instruments and neither is the pair.**

| | what it is | shape | source |
|:--|:--|:--|:--|
| `book_reference_density` (H-NEW-125 axis 9) | roots {ktb, qrA, Ayy, nzl} **per 100 verses** | ρ = +0.574, **inverted-U, peak Late Meccan** | `h-new-125-chronology-content.md:43` |
| **z = −3.75** | ***kitāb* alone**, per verse, Meccan vs Medinan | monotone, Medinan ≫ Meccan | `compression-and-self-reference.md:203` |

The z = −3.75 is a **single-lemma** result from a ten-lemma decomposition, not an axis. §9's failed
attempt used axis 9's four roots with the z-value's two-group contrast — a hybrid matching neither.
**That is why it returned nothing: it tested an instrument that does not exist.**

### 10.2 The check, on the right instrument

*kitāb* surface tokens per verse, 110 phase-labelled surahs, permutation null, seed 20260509,
10,000 permutations:

| | Medinan | Meccan | difference |
|:--|--:|--:|--:|
| this reproduction (no disambiguation) | 0.0568 | 0.0223 | **+0.0345** |
| source, with hand disambiguation | 0.0770 | 0.0243 | +0.0527 |

The Meccan figures agree closely (0.0223 vs 0.0243); mine is lower on the Medinan side, consistent
with the source excluding *kitāb* when it denotes Torah or Gospel and my reproduction excluding
nothing. **This is a looser instrument and is declared as such** — it is not the source's.

| control | p |
|:--|--:|
| unstratified | **0.0051** |
| stratified on mean verse length | **0.3018** |

**The unstratified result reproduces the published direction and significance. It does not survive a
mean-verse-length control.**

### 10.3 Why that does NOT refute the anchor — and this is the point

[[h-new-3120-asbab-chronology]] established, on independent data, that
**ρ(mean verse length, Nöldeke phase) = +0.79 to +0.91.** So *"the anchor fails under a
mean-verse-length control"* is **precisely the claim that cannot be distinguished from "the control
is a near-duplicate of the treatment."**

This is the second independent instance of that inseparability, and it lands on a *lexical-content*
axis — the side of the MW-2 split where chronology is supposed to be a **genuine** axis rather than a
pseudo-confound. **So the split does not rescue this anchor.** At surah granularity, a lexical
phase-effect and a structural length-effect are the same measurement.

**Status: the flag is now RUN and its answer is that the question is not answerable at surah
granularity.** A verse-level or pericope-level design, where mean verse length is not a
near-duplicate of phase, is the only route. Nothing here retracts the anchor, and nothing here
supports it.

### 10.4 What is retractable, independently of any of the above

**The citation "the kitāb/qurʾān axis at z = −3.75" should not be used again.** It names an axis and
attaches a statistic from a different instrument with a different unit, a different lemma set and a
different shape. That is a *bookkeeping* error, not a statistical one, and it is fixable by anyone
in one grep — which is exactly the category [[AUDIT-TWO-BLOCKED-INSTRUMENTS-2026-08-10]] §8 says
tends to survive longest.

