---
title: Proxy claims — a hand-assigned quantity is an unmeasured claim
author: Waiel Al-Shujaa
date: 2026-08-08
status: STANDING METHODOLOGICAL RULE — applies to every hand-assigned quantity in this repository
established_by: [H-NEW-860.1, H-NEW-2920]
companions: [findings/UNIT-DRIFT-DEFECT.md, findings/ABSENCE-CLAIMS.md]
---

# Proxy claims

## 1. The rule

> **A hand-assigned quantity is a measurement claim. Substituting a score you assigned for a
> quantity you could have computed is an empirical assertion — that your score tracks the
> quantity — and it is the one assertion in the substitution that is never tested.**

And the clause that does the work:

> **Any hand-assigned quantity must either (a) be validated against a computed alternative, or
> (b) carry an explicit statement of why no computed alternative exists — which is itself an
> absence claim and is subject to `findings/ABSENCE-CLAIMS.md`.**

**That last clause is not decoration. The three defects compound, and this repository contains
the worked case of all three at once.**

- A **false absence claim** — *"a formal count would require a ḥadīth-database … which is not
  on disk"* — licensed
- a **hand-built proxy** — a 0–10 rubric over 36 surahs — which then carried
- a **size-loaded correlation** — two variables loading on surah length with opposite signs,
  meeting.

**That is H-NEW-860.** Remove any one of the three and the published claim does not survive to
be cited 61 times. The defects are not independent: the first *authorises* the second, and the
second is what the third is measured on.

---

## 2. The worked example, with both coefficients

**H-NEW-860** reported that classical ḥadīth attention is anti-aligned with architectural
significance: `ρ(rubric, UAS_rank) = +0.330, p = 0.050, N = 36`. The rubric was a hand-built
0–10 score which the finding itself called *"a rough rubric"*
(`findings/phase-b-hypotheses/h-new-860-hadith-architectural-alignment.md:64, 74, 80`).

**H-NEW-860.1** replaced it with a formal count over all 50,884 on-disk ḥadīth records.

| comparison | Spearman ρ | p |
|:--|--:|--:|
| **rubric × formal quotation count, over the 36 surahs the rubric actually scored** | **+0.055** | **0.752** |
| rubric × formal naming count, same 36 | **−0.315** | 0.061 |
| rubric × formal quotation count, all 114 with unscored surahs as 0 | +0.374 | 4.1 × 10⁻⁵ |
| published headline, re-run with the formal count | **−0.2923** | 0.0836 |

**All 18 pre-registered arms carried the opposite sign to the published +0.330, and none
survived a length control.** The diagnosis:

> **The rubric carried no discriminative information where it operated. Against the formal count
> it was not a weak proxy; it was noise.**

**Read rows 1 and 3 together — that pairing is the whole method.** Across all 114 the rubric
looks respectable at +0.374, and every point of that is the binary listed-versus-unlisted split.
**Restricted to the range where it assigned actual values, it is +0.055.** The rubric could
separate presence from absence. It could not rank.

### 2.1 The counter-example, which is why one number is not a verdict

**H-NEW-2920 T1** measured a second hand score — H-NEW-150's 0–17 liturgical-prominence
score — the same way, and it came back **inverted**:

| proxy | full-corpus ρ | **operating-range ρ** | reads as |
|:--|--:|--:|:--|
| H-NEW-860's fadāʾil rubric | +0.374 | **+0.055** | selects well, cannot rank |
| H-NEW-150's liturgical score | +0.066 | **+0.4319** (to +0.5030 on the union instrument) | **ranks respectably, selects badly** |

The 150 score's selection failure is severe and specific: **45 surahs with non-zero formal
reception carry a score of 0**, including **Q 4 al-Nisāʾ — 38 naming links and 232 quotation
records, the second-most-cited surah in the nine books.** Its 27 scored surahs capture **54.1 %**
of all naming links, and its top ten overlaps the formal top ten by **4 of 10**.

**Two hand scores, two opposite failure profiles. Either coefficient alone would have declared
its proxy sound.** This is why §4 requires both.

---

## 3. The detection screens

A quantity is **FLAGGED** if it hits A and B. Apply to the quantity, not to the prose around it.

### Screen A — is the quantity hand-assigned?

Grep for: `hand-coded`, `hand-built`, `hand-curated`, `hand-picked`, `hand-tagged`,
`manually curated`, `rough rubric`, `subjective`, `judged by`, `curated list`, `by eye`,
`my judgment`, `my coding`, `is mine`, `I classified`, `assigned by inspection`, `0–10 score`.

```bash
grep -rniE "hand-(coded|built|curated|picked|tagged|assembled)|manually (curated|assigned|coded|scored|classified)|rough rubric|curated list|by eye|my (judgment|judgement|coding)|is mine\b|I classified" \
  --include='*.md' --include='*.py' findings/ surahs/ scripts/
```

**Also flag, and these are the ones a grep misses:**
- **any hard-coded list of surahs, verses, roots, or forms that is not produced by a rule in
  code** — a set literal in a script is a hand-assignment however it is spelled;
- **any category label whose assignment rule is stated in prose rather than as a function**;
- **any inherited scholarly ordering or classification** — a chronology rank, a
  Meccan/Medinan label, a genre tag. It is not hand-built *by this project*, and it is still
  hand-assigned. See §5.

**Measured cue yields, H-NEW-2920 §4** — run the precise cues first:

| run first | run last, and know why |
|:--|:--|
| `hand-coded` (12 hits, highest precision), `hand-curated` (11), `hand-built` (15), `subjective` (18), `curated list` (6), `hand-tagged` (6) | `by inspection` (39) and `eyeball` (65) are dominated by *"closed-form hypergeometric, reproducible by inspection"* and by preregs honestly disclosing their own post-hoc origins. **Those are the discipline working, not defects.** A sweep that counts them will drown. |

**And the cue that found nothing.** `researcher-judged`, `we classified`, `qualitative score`
and `hand-assigned` return **zero hits each**. A proxy is described here as *"mine"*,
*"hand-coded"*, or *"my judgment"* — first person and informal — **never in the vocabulary an
auditor would naturally reach for.** Search the author's idiom, not the auditor's.

### Screen B — is a computed alternative available?

**Ask the data, not the finding.** The finding's own answer has been wrong every time it has
been checked: `ABSENCE-CLAIMS.md` §6 records five FALSE absences, one of which
(**FALSE #3**) is the exact sentence that licensed the 860 rubric.

**A "no computed alternative exists" answer is an absence claim and inherits every requirement
of `ABSENCE-CLAIMS.md` §4** — state the command, the scope, the measured property and its
threshold, and a positive control on the search. **It may not be inherited from a parent
finding.**

Distinguish, as `ABSENCE-CLAIMS.md` §4 requires, **ABSENT** from **NOT-YET-DERIVED**. A per-verse
tafsīr-attention count is not absent because no CSV holds it; five tafsīr corpora are on disk and
the table has simply never been made. **Derivable is not missing.**

### Screen C — has the agreement ever been measured?

Grep the finding for a coefficient between the proxy and anything computed. **Absence is the
defect.** A sensitivity analysis on the proxy's own weights is not this test — perturbing a score
by ±2 measures its internal stability, not whether it tracks anything real.

---

## 4. The standing requirement

**Any finding that uses a hand-assigned quantity in a statistic must state, in the finding:**

1. **That the quantity is hand-assigned**, and by what rule, in the finding rather than only in
   a pre-registration.
2. **Its operating range** — the units it actually scored, as opposed to the units it left at
   zero or unlisted. **This is the number most often missing and it is the one the verdict turns
   on.**
3. **Either an agreement coefficient against a computed alternative, or an absence claim
   meeting `ABSENCE-CLAIMS.md` §4.**

Four further clauses, each earned by a specific case:

- **Report the agreement over the operating range AND over the full set, and take the
  operating-range figure as primary.** The full-corpus figure is inflated by the
  presence-versus-absence split. H-NEW-860's rubric reads +0.374 full-corpus and +0.055
  in-range; H-NEW-150's score reads +0.066 full-corpus and +0.4319 in-range. **The two
  coefficients answer different questions — *can it select?* and *can it rank?* — and a proxy
  can pass either while failing the other.**
- **A hand score with no denominator can still carry the unit-drift defect.** Neither H-NEW-860's
  rubric nor UAS divides by anything, and ρ(UAS, log word count) = **+0.608** while
  ρ(rubric, log word count) = **−0.522**. Two opposite loadings on a shared nuisance channel
  produce a correlation that is about neither variable. **Declare the size loading of every hand
  score** — one Spearman against log unit size, the same line of code `UNIT-DRIFT-DEFECT.md`
  already asks for. *(This is H-NEW-860.1 §7.4's proposed Screen A′, arrived at independently by
  H-NEW-2920 §2.3.)*
- **A proxy of a proxy must reproduce its declared source, and this is separately checkable.**
  `Q036_F_01_recitation_frequency_weighted_centrality.py:59-99` calls itself *"the LOCKED weights
  table per the pre-reg"* and reproduces H-NEW-860's rubric at **ρ = +0.4878**, dropping **18 of
  its 36 surahs** and changing **30 of 38** retained values. **That failure is independent of
  whether the source was any good**, and it is invisible to any test of the parent.
- **Do not manufacture a body count.** H-NEW-170 replaced hand-picked classical divine-name pairs
  with an exhaustive network on its own initiative; H-NEW-2210 is *"a morphology-grounded
  GENERATOR (not a curated list)"*; H-NEW-2660 replaced a curated coincidence list with 124,148
  enumerated candidates. **Reporting a proxy as sound is a result of the same value as
  condemning one**, and this repository has replaced curated lists with generators unprompted
  more than once.

---

## 5. Inherited classifications are hand-assigned too, and they fail differently

A scholarly ordering imported from outside the project is not hand-built here, and it is still a
hand-assignment: **a category whose rule is prose**. It has no computed ground truth, so §4's
requirement 3 cannot be met head-on. **What can almost always be met is inter-rater agreement**,
and it is usually cheaper than anyone expects.

**The worked case.** `data/revelation-order.csv` carries **two** independent orderings —
`noldeke_order` and `revelation_order` (the Tanzīl Egyptian standard) — in **one file**.

> **ρ(Nöldeke, Egyptian standard) = +0.7714**, Kendall τ = +0.5771.
> **38 of 114 surahs sit more than 20 rank places apart** — Q 99 al-Zalzala by **68**.

**That coefficient already existed, and finding out cost one grep.** H-NEW-2920's first draft
said no finding had ever computed it; `h-new-212-alt-chronology-fisher-rao.md:54-63` publishes
**+0.771** across **four** chronologies, not two. Two separately built harnesses agreeing to
three decimals is worth more than the originality claim it replaced. **Run `ABSENCE-CLAIMS.md`
§3's grep on your own sentence, not only on other people's** — the rule applies to the
document asserting it.

What had genuinely never been done, and is the transferable part, is the **rater swap on a
published content map**: re-scoring an existing finding's axes under a second ordering, using
its own published values so that nothing but the rater changes.

Swapping the rater on H-NEW-125's *"PERVASIVE CHRONOLOGY"* map, using its published axis values
verbatim so nothing but the ordering changes:

- **the surviving axis set falls from 11 of 15 to 9 of 15** (`qul_density` and `surah_length`
  drop out; none is gained);
- **signs agree on 14 of 15 axes** — only a null axis flips;
- **thirteen of fifteen coefficients shrink**, several by more than 0.25:
  mean verse length **+0.9038 → +0.6690**, divine-name density +0.8973 → +0.6258, loanword
  density +0.8329 → +0.5699.

**The rule that follows:**

> **An inherited ordering is typically directionally robust and quantitatively rater-dependent.
> Report the direction as a finding and the magnitude as an upper estimate, and name the rater
> in the same breath as the coefficient.**

And the consequence that reaches outside its own finding: **`UNIT-DRIFT-DEFECT.md` §3's drift
table is rater-specific.** Its Nöldeke block bolds mean verse length at ρ = +0.9038 and instructs
future sessions to control against the strongest channel; under the alternative rater that
channel is +0.6690, verse count falls +0.3903 → +0.2482, and log word count +0.6775 → +0.4436.
A control calibrated on the Nöldeke figure is calibrated on the larger of two defensible
numbers — the conservative direction, and it should be on the record rather than found later.

---

## 6. The four outcomes

Applied to `ρ_op`, the agreement over the **operating range**. Thresholds are the convention
fixed in H-NEW-2920's pre-registration §6 before any coefficient existed, anchored on
H-NEW-860.1's +0.055; they are a convention and not a law, and a reader may re-classify from the
published coefficients.

| outcome | rule | case |
|:--|:--|:--|
| **NOISE** | \|ρ_op\| < 0.20 **and** the host headline fails to reproduce with the formal quantity substituted | H-NEW-860's rubric (+0.055); `Q036_F_01`'s reconstruction (−0.040) |
| **PARTIAL** | anything measurable in between | H-NEW-150's liturgical score (+0.43 to +0.50, headline null on substitution); the Nöldeke rank (+0.7714, surviving set 11 → 9) |
| **CARRIES INFORMATION** | ρ_op ≥ 0.60 **and** the headline reproduces, same sign, still significant at the host's own bar | *none measured yet — the oath-opener list is the likeliest candidate and its test is queued* |
| **NOT-YET-TESTABLE** | no computed alternative exists on disk — **and this is an absence claim, subject to `ABSENCE-CLAIMS.md` §4** | — |

**What a NOISE verdict does and does not do.** It retires the *quantity*, not the subject
matter. H-NEW-860.1 retired a coefficient, not the existence of ḥadīth reception; the
reception-weights CSV it produced is the project's first per-verse reception instrument.

**And PARTIAL is not a soft NOISE.** H-NEW-150's score tracks formal reception at ρ ≈ +0.5 among
the surahs it scored — that is real information about a real thing. What it cannot do is carry a
correlation, because **its headline does not survive substitution**: ρ(formal, cluster degree) is
−0.056, +0.022 and +0.027 across three reception instruments, against the score's published
+0.3121.

---

## 6.1 Provenance is a proxy too — and a folder name is the cheapest one to check

*Added 2026-08-08 by H-NEW-2970, after auditing all thirteen editions under
`data/literature/classical-tafsir/spa5k-tafsir-api/`.*

**A slug is a hand-assigned attribution standing in for a verifiable one.** It has the exact shape
§1 describes: a label somebody assigned, substituted for a fact somebody could have established,
where the substitution asserts *"this folder holds what its name says"* — and that assertion is
the one thing in the substitution nobody tests. It is worse than an ordinary proxy in one respect
and better in another. **Worse**, because a wrong provenance does not degrade a coefficient by
degrees, it inverts the evidential weight outright: a Companion gloss and a modern reading are not
interchangeable authorities, and no sensitivity analysis recovers from a 1,300-year error.
**Better**, because unlike agreement with a computed quantity, this one is *decidable*, usually in
minutes.

> **Standing requirement — before citing any classical source from a slug-named directory, verify
> the author from the text's own internal citations. A folder name is metadata, and metadata is
> not evidence.**

The name-collision clause this extends is `ABSENCE-CLAIMS.md` §4, final bullet — *"a hit is not a
verification, and neither is a miss — open the file"* — which is where that rule lives, not here.
This adds the mechanical test that turns it from a warning into a procedure.

### The death-date test

**A commentary cannot quote someone who died after its author.** Take the latest securely-cited
authority in the text; the author died no earlier than that. Compare against the claimed author's
death date. One inequality settles it.

**This test was not invented here.** `h-new-2620-tafsir-contested.md` §2.4 had already run it on
two slugs of its own accord — rejecting al-Suddī (d. 127) for `ar-tafseer-al-saddi` and rejecting
al-Wāḥidī (d. 468) for `ar-tafsir-al-wasit` because that folder quotes *ṣāḥib al-Kashshāf*,
al-Zamakhsharī, **d. 538, seventy years after al-Wāḥidī** — and it closed with the sentence this
whole clause is trying to make routine: ***"Which one I do not know and do not assert."*** What
§6.1 adds is that the check should be run on **every** slug, not on the ones that happen to look
odd. Two of the tree's four problem directories were found only by the exhaustive pass.

`ar-tafseer-tanwir-al-miqbas/` is labelled *Tanwīr al-Miqbās min tafsīr Ibn ʿAbbās*
(**Ibn ʿAbbās, d. 68 AH**), and over its 6,236 verse files it cites al-Zamakhsharī (d. 538)
254 times and his *Kashshāf* 892 more, Ibn ʿAṭiyya (d. 541) 389, al-Qurṭubī (d. 671) 220,
al-Sakkākī (d. 626) 78, Ibn Mālik (d. 672) 73, al-Raḍī (d. 686) 72, al-Taftāzānī (d. 793) 30,
al-Suyūṭī (d. 911) 13, al-Ālūsī (d. 1270) 8, Muḥammad ʿAbduh (d. 1323) 2. **Ibn ʿAbbās does not
quote al-Raḍī.** The text is Ibn ʿĀshūr's *al-Taḥrīr wa'l-Tanwīr* (d. 1393/1973); the slug
collided on the word *Tanwīr*. Full verification:
`data/literature/classical-tafsir/MISLABELLED-TANWIR-FOLDER.md`.

**Strip diacritics before counting, and reconcile when two counts disagree.** H-NEW-2620's
correction block reports 249 / 220 / 75 / 70 / 69 for al-Zamakhsharī, al-Qurṭubī, al-Sakkākī, Ibn
Mālik and al-Raḍī against the 254 / 220 / 78 / 73 / 72 above. **Every difference is the
diacritics**: searching the raw text reproduces 2620's five figures exactly, searching the
harakāt-stripped text reproduces these. Two harnesses, one corpus, no disagreement — but only
because the discrepancy was chased rather than rounded over.

**And the sharpest dating cue is not a name but a courtesy.** `ar-tafsir-al-wasit/` calls both
Muḥammad ʿAbdallāh Darrāz and Shaykh Muḥammad al-Khiḍr Ḥusayn *"فضيلة **المرحوم**"* — "His
Eminence **the late**" — and both died in **1958 CE**. A *"the late X"* honorific is a hard lower
bound on the sentence containing it, and it needs no death-date table. **Grep `المرحوم` and
`طيب الله ثراه` early, then look up only the modern names they attach to.** Do not use bare
`رحمه الله` for this — every author says it of every predecessor, and it dates nothing.

**Before declaring a citation unverifiable, search the source it actually names.** This audit
nearly recorded one as unresolvable. `razi-99names-test.md:65` attributes the *kāf-hā-yā-ʿayn-ṣād*
decomposition **Kabīr / Hādī / Amīn / ʿAzīz / Ṣādiq** to Ibn ʿAbbās, and it appears in **neither**
Tanwīr folder — the genuine English recension at Q 19:1 gives Kāfī/Hādī/ʿĀlim/Ṣādiq and
Karīm/Hādī/Ḥalīm/ʿĀlim/Ṣādiq instead. But the finding never claimed a Tanwīr source: its own table
says *"Ibn ʿAbbās via al-Durr al-Manthūr 4/679"* — **and *al-Durr al-Manthūr* is on disk.**
`raw/suyuti-durr-manthur.openiti.raw.txt` at **PageV05P477** reads
*«عن ابن عباس في قوله: {كهيعص} قال: **كبير هاد أمين عزيز صادق**»*, with the full transmission —
al-Firyābī, Ibn Abī Shayba, Ibn Jarīr, Ibn Abī Ḥātim, al-Ḥākim *(ṣaḥḥaḥahu)*, al-Bayhaqī — and the
variant *«وفي لفظ: كاف بدل كبير»*. **Verbatim, and the citation is sound.** Checking the two
folders the auditor was thinking about, rather than the work the footnote named, would have
produced a false UNDETERMINABLE. `ABSENCE-CLAIMS.md` §4 already says it: search for the work by
author and title, **not by the filename you happened to open** — and that applies to the auditor
as forcefully as to the author.

**Search titles as well as names, because a scholar is often cited only by his book.** Re-counting
`ar-tafseer-tanwir-al-miqbas/2/2.json` reproduces that file's published figures exactly —
al-Zamakhsharī ×5, al-Raḍī ×3, Ibn Mālik ×2 — **except al-Sakkākī, who returns 0 under his own
name and 3 under `صاحب «المفتاح»`**, "the author of *al-Miftāḥ*". A battery of personal names
alone would have missed him entirely.

### Look for self-declaration first, because it is free

**Before counting anything, grep the data for its own title and for the author's family.** The
Tanwīr folder contains the Arabic sentence *"ليس لها تفسير في كتاب **التحرير والتنوير**"* — "there
is no commentary for it in the book *al-Taḥrīr wa'l-Tanwīr*" — **nine times**, as the placeholder
for verses the work does not cover: `ar-tafseer-tanwir-al-miqbas/21/75.json`, `70/30`, `74/13`,
`74/43`, `74/44`, `74/45`, `75/17`, `101/8`, `113/2`. Two more name the book with the title
truncated (`70/31`, `70/32`), and there are **25** such placeholders in all. **The data names its
own source work, in its own text.** And at
`ar-tafseer-tanwir-al-miqbas/2/271.json` the author writes *"وقال الشيخ ابن عاشور **جدي**"* — "and
Shaykh Ibn ʿĀshūr, **my grandfather**, said" — an authorial self-identification, not an inference.
Both were sitting in the file the whole time. A death-date battery over 15.5 million characters is
the fallback, not the first move.

### The five ways the test misleads, each met in this audit

1. **It refutes; it cannot confirm.** `en-al-jalalayn/` and `en-tafsir-ibn-abbas/` — the genuine
   Ibn ʿAbbās recension — return **zero** securely-cited post-500 AH authorities, because both are
   terse lemma glosses that name almost no one. (The single apparent hit in `en-tafsir-ibn-abbas/`
   is `Razi` inside the personal name *ʿAbd al-Rāziq* — see failure mode 4.) **Zero late citations
   is not a verification; it is no measurement.** For a non-citing text the method has no power and
   you must say so rather than record a pass. *(This is Screen B's ABSENT-versus-NOT-YET-DERIVED
   distinction wearing different clothes: no result is not a clean result.)*
2. **The editorial apparatus is not the author.** `ar-tafsir-al-tabari/` cites al-Suyūṭī (d. 911)
   214 times, Ibn Ḥajar (d. 852) 131 and al-Shawkānī (d. 1250) 8 — every one of them in **Maḥmūd
   Shākir's** modern notes, identifiable by volume:page references (486 hits for
   `الدر المنثور N: N`, 157 numbered *ḥadīth*/*athar* notes, 10,460 print/manuscript sigla). The
   attribution to al-Ṭabarī (d. 310) is **correct**; the naive test would have condemned it.
   *Read the context of the latest hit before believing it* — and note separately that anything
   measuring this edition's text is measuring a 20th-century apparatus along with it.
3. **Homonyms.** `ابن كثير` is the mufassir (d. 774) after `قال` and the Meccan reciter (d. 120)
   after `قرأ` — the latter is why al-Baghawī (d. 516) appears to cite him 199 times.
   `ابن هشام` is the *sīra* author (d. 218) or al-Anṣārī the grammarian (d. 761);
   `أبو حيان` is al-Andalusī (d. 745) or the *rāwī* al-Taymī (d. 145), and in
   `ar-tafseer-al-qurtubi` the single hit is the *rāwī* (`رواه سفيان عن أبي حيان`).
4. **Common words masquerade as names, and so do sloppy regexes.** `النحاس` is al-Naḥḥās (d. 338)
   in al-Qurṭubī and *copper* in al-Muyassar; `الراغب` is al-Rāghib al-Iṣfahānī (d. 502) or simply
   "the desirous". Worse, this audit's own first pass wrote the optional shadda as `الكشَّ?اف` and
   `الفرَّ?اء`, which after diacritic-stripping match **الكاف** and **الفاء** — "the *kāf*", "the
   *fāʾ*" — inflating al-Farrāʾ to 1,417 hits in al-Qurṭubī and inventing 37 Zamakhsharī citations
   in al-Baghawī that do not exist (**the true count is 0**). **Gate every name on a citation verb**
   — `قال|وقال|قاله|ذكره|نقله|عن|عند|كلام|تفسير|صاحب|الإمام|الشيخ|الحافظ|رواه` — **and read the
   latest hit.** An ungated battery is not a measurement.
5. **A folder can be a blend, and then sampling proves nothing.**
   `en-asbab-al-nuzul-by-al-wahidi/` is **28% al-Wāḥidī and 72% something else**, interleaved verse
   by verse — see below. **Verifying one verse verifies one verse.** Classify every unit.

### The census, 2026-08-08 — mostly clean, and that is the result

Thirteen edition directories, each checked against its own internal citations. **Two are
mislabelled** — the Tanwīr folder, already recorded, and one found here. **One was already
disambiguated by the project against a misleading slug** (`ar-tafseer-al-saddi`, H-NEW-2620 §2.4).
**One was honestly marked undeterminable and is now bounded** (`ar-tafsir-al-wasit`). **The
remaining nine carry correct labels** — and state the grade of that honestly: **seven are
positively verified** by a latest-citation earlier than the claimed author's death, and **two
(`en-al-jalalayn`, `en-tafsir-ibn-abbas`) are untested rather than passed**, because they cite no
one and the method has no purchase on them. Nine correct labels; seven verifications.

**The new one: `en-asbab-al-nuzul-by-al-wahidi/` is not one work but two.** Of its 1,089
non-empty entries, only **312 (522,456 chars) are al-Wāḥidī's *Asbāb al-nuzūl*** — full *isnād*
chains, *"was revealed concerning"*. The other **777 (1,345,654 chars, 72.0%) are a Sufi
commentary**, and the decisive citation is at `en-asbab-al-nuzul-by-al-wahidi/20/5.json`:
*"**Shaykh al-Islām Anṣārī** said, 'The sitting of the Lord on the Throne is in the Qurʾān, and I
have faith in it'"* — **Khwāja ʿAbdallāh Anṣārī of Herat died in 481 AH and al-Wāḥidī died in 468.
Al-Wāḥidī cannot quote a man who outlived him by thirteen years.** That refutation is verified.
**The positive identification is an inference, and is offered as one:** the phrase *"the Persian
of this report is this"* means the work's base language is Persian, Anṣārī is its standing
authority, and the English carries the vocabulary of William Chittick's translations — "the Real"
×653, "recognition" ×205, "unneediness" ×22, "the Beginningless" / "the Endless". Those three
together point to **Rashīd al-Dīn Maybudī, *Kashf al-asrār wa ʿuddat al-abrār*** (Persian, 520 AH),
which is built on Anṣārī throughout. Nothing in the folder names itself — `Maybudi` and `Kashf`
both return **0** — so the identification rests on style, not self-declaration, and should be
cited that way. **What is settled either way is that 72% of this directory is not al-Wāḥidī.**
The two works alternate within a single surah: `2/2` is the Sufi text, `2/14` is al-Wāḥidī, and
**all seven verses of Q 1 are the Sufi text** — so a reader who checked al-Fātiḥa to verify the
folder would have seen 100% of the wrong work and 0% of the right one.

| slug | claimed author (`editions.json`) | **verified** author | death | establishing internal citation |
|:--|:--|:--|--:|:--|
| `ar-tafsir-al-tabari` | `Tabari` | al-Ṭabarī ✓ **+ Shākir apparatus** | 310 | main text stops at al-Farrāʾ/Abū ʿUbayda; all post-500 names are in the modern notes |
| `ar-tafseer-al-qurtubi` | `Qurtubi` | al-Qurṭubī ✓ | 671 | Ibn ʿAṭiyya (d. 541) ×410 gated; no securely-cited authority later |
| `ar-tafsir-ibn-kathir` | `Hafiz Ibn Kathir` | Ibn Kathīr ✓ | 774 | Ibn Taymiyya (d. 728) ×13 — his own teacher |
| `ar-tafsir-al-baghawi` | `Baghawy` | al-Baghawī ✓ | 516 | al-Thaʿlabī (d. 427), his teacher. **Anomaly:** `قال القرطبي` at `21/51` and `23/108` — 2 hits in 4.4 M chars, a spot contamination, not a reattribution |
| **`ar-tafseer-tanwir-al-miqbas`** | **`Tanweer`** | **Ibn ʿĀshūr, *al-Taḥrīr wa'l-Tanwīr*** | **1393** | **self-titled ×9; "my grandfather" at `2/271`; al-Ālūsī d. 1270, ʿAbduh d. 1323 — vs Ibn ʿAbbās d. 68** |
| `ar-tafseer-al-saddi` | `Saddi` | al-Saʿdī, *Taysīr al-Karīm al-Raḥmān* ✓ | 1376 | Ibn al-Qayyim (d. 751) ×5, incl. *Jalāʾ al-afhām* by title; Ibn Taymiyya ×1. **Slug reads as al-Suddī (d. 128) — already disambiguated with evidence by H-NEW-2620 prereg §#6** |
| `ar-tafsir-al-wasit` | `Waseet` | **a later-20th-century work** — Ṭanṭāwī's *al-Wasīṭ* on the balance of evidence | **≥1393** | Calls **Muḥammad ʿAbdallāh Darrāz** and **Muḥammad al-Khiḍr Ḥusayn** — both d. **1958 CE** — *"فضيلة المرحوم"*, **the late**; refers to the year **1945**; cites `قال صاحب تفسير التحرير والتنوير` ×3 (first at 2:73), Rashīd Riḍā (d. 1354) ×73 gated, ʿAbduh (d. 1323) ×22. **Not al-Wāḥidī's *al-Wasīṭ* (d. 468) — excluded by nine centuries.** H-NEW-2620 marked this *"not determinable from disk"*; it is now bounded |
| `ar-tafsir-muyassar` | `المیسر` | King Fahd Complex committee ✓ | modern | no gated citation at all; consistent with a committee paraphrase |
| `en-al-jalalayn` | `Al-Jalalayn` | al-Maḥallī + al-Suyūṭī — **not testable by this method** | 864 / 911 | **zero** internal citations; Q 2:2 is 458 chars of lemma gloss |
| **`en-asbab-al-nuzul-by-al-wahidi`** | `Asbab Al-Nuzul by Al-Wahidi` | **al-Wāḥidī 28% + a Persian Sufi commentary 72%** (Maybudī, *Kashf al-asrār*, on style) | 468 / 520 | **Shaykh al-Islām Anṣārī (d. 481) quoted at `20/5` — al-Wāḥidī d. 468** |
| `en-tafisr-ibn-kathir` | `Hafiz Ibn Kathir` | Ibn Kathīr, abridged ✓ | 774 | Ibn Taymiyya (d. 728) ×6; no later name survives inspection |
| `en-tafsir-ibn-abbas` | `Tanwîr al-Miqbâs…` | *Tanwīr al-Miqbās* ✓ — **not testable by this method** | 68 (ascribed) | **zero** internal citations. **This is the genuine recension, and it is English-only** |
| `en-tafsir-maarif-ul-quran` | `Mufti Muhammad Shafi` | Muftī Muḥammad Shafīʿ ✓ | 1396 | Thānwī (d. 1362) ×48, al-Ālūsī ×72, Iqbāl ×3 — all before him |

**Two of thirteen is a good tree, and reporting it as a good tree is the point.** The pull, after
a real failure, is toward finding more — and §4's closing clause applies here as elsewhere:
**reporting a directory as sound is a result of the same value as condemning one.** What made the
two failures findable was not suspicion; it was running the same check on all thirteen.

### Where the error enters, and the one-line prophylactic

**Every problem slug in this tree has a degenerate `editions.json` author field**, and one screen
catches all four: `"Tanweer"`, `"Waseet"` and `"Saddi"` are transliterated **title fragments, not
people**, and `"Asbab Al-Nuzul by Al-Wahidi"` is a **work title in the author slot**. Those four
are precisely the mislabelled edition, the blended edition, the edition that was undeterminable,
and the edition whose slug reads as the wrong man.

**Treat a metadata author field that is not a person's name as an unverified directory.** State
its performance honestly: on this tree the screen's **recall is 4/4 and its precision is 4/7** —
it also flags `المیسر` (a title, and the edition is fine), `Al-Jalalayn` (a dual epithet, fine)
and `Tanwîr al-Miqbâs min Tafsîr Ibn ʿAbbâs` (a title, and the **genuine** recension). It costs
one look at `editions.json` and it never gave a false all-clear, which is the direction that
matters — but it is a triage cue for what to verify first, **not a verdict**. The verification is
still the death-date test.

**The control, and it is the most useful number in this section: the OpenITI tree is 10 for 10.**
The other classical corpus on disk, `data/literature/classical-tafsir/raw/*.openiti.raw.txt`,
embeds real bibliographic metadata in every file — `010.AuthorNAME`, `011.AuthorDIED`,
`020.BookTITLE`. All ten match their filenames exactly: al-Ṭabarī **310**, al-Thaʿlabī **427**,
al-Zamakhsharī **538** (*al-Kashshāf*), al-Ṭabarsī **548**, al-Rāzī **606** (*Mafātīḥ al-ghayb*),
al-Qurṭubī **671**, Ibn Kathīr **774**, al-Biqāʿī **885** (*Naẓm al-durar*), al-Suyūṭī **911** for
both *al-Durr al-manthūr* and *al-Itqān*. **Zero mismatches.**

**So the lesson is not that digital corpora are unreliable.** Two corpora sit in the same
directory; the one that records an author and a death date per file has a perfect record, and the
one whose provenance is a slug has four problems in thirteen. **The defect is the metadata format,
not the medium** — which is the §1 point exactly: a slug is a hand-assignment substituted for a
recorded fact, and the corpus that recorded the fact did not need auditing.

**And a mislabel propagates into every derivative that keeps the slug.** The Q001/Q002 plaintext
extractions at `data/literature/classical-tafsir/raw/` each carry a `# Source: spa5k/tafsir_api →
<slug>` header — good practice, and exactly the mechanism by which a wrong label travels intact.
Four of those files inherit one: `tanwir-miqbas-ar-Q001.txt` and `-Q002.txt` (Ibn ʿĀshūr, not Ibn
ʿAbbās — `Q001` opens with the *naḥt* analysis of the basmala quoting Sībawayh's *bāb al-iḍāfa*),
and `asbab-nuzul-wahidi-en-Q001.txt` (**100% the Sufi text, 0 of 7 verses al-Wāḥidī**) and
`-Q002.txt` (**83 of 128 verses, 72% not al-Wāḥidī**). **Re-verify derivatives separately: the
extraction is downstream of the label, so it is never evidence for it.**

**And the blend already has live consumers.** Ten `surahs/` loci cite that folder as al-Wāḥidī;
**five are genuine** (Q 54:1, 29:1, 30:2, 66:1, 64:14) and **four are the Sufi text** — Q 48:1
(`surahs/Q048-al-fath/03-tafsir-survey.md:189`, marked VERIFIED), Q 71:13
(`surahs/Q071-nuh/03-tafsir-survey.md:84`), Q 58:12 of the pair cited at
`surahs/Q058-al-mujadala/Q058-F-03-najwa-abrogation-prereg.md:32`, and Q 38:1
(`surahs/Q038-sad/03-tafsir-survey.md:13`, which also calls the English folder *"Arabic"*).
**A per-file check would have caught every one, and a folder-level check caught none.** Note what
`surahs/Q071-nuh/04-hadith-corpus.md:77` already says of its own citation — that the material *"is
homiletic"*. **The symptom was recorded and not chased.** When a source reads unlike the work it is
supposed to be, that observation *is* the audit; finish it.

---

## 7. The compound case, stated once more because it is the reason for this document

**H-NEW-860 was all three defects at once**, and the order matters:

1. **`ABSENCE-CLAIMS.md`** — *"which is not on disk"*, an absence claim that never stated its
   search and was false. The corpus had been committed on 2026-04-28, the same day the finding
   was written.
2. **This document** — the false absence *licensed* the hand-built rubric. **A proxy introduced
   because the real quantity was believed unavailable is the highest-risk kind**, because the
   sentence that authorised it is exactly the sentence nobody re-checks.
3. **`UNIT-DRIFT-DEFECT.md`** — the rubric then carried a size-loaded correlation, and the
   published anti-alignment was two opposite size loadings meeting.

**Screen in that order.** Absence first, because it is one grep and it decides whether a proxy
should exist at all. Then agreement, because it decides whether the proxy measures the thing.
Then drift, because it decides whether the correlation measures either of them.

**And screen for UNVERIFIABLE before all three** (`UNIT-DRIFT-DEFECT.md` §6.3): a number no code
in the repository reproduces cannot be validated *or* condemned, and running an agreement
coefficient against an unreproducible baseline measures nothing.

---

## 8. How to apply this in a future session

1. Run §3 Screen A's grep, precise cues first. Expect on the order of thirty self-declaring
   quantities; **25 are catalogued at `findings/phase-b-hypotheses/h-new-2920-proxy-census.md`
   §2 with `file:line`,
   so start from that list rather than re-deriving it.**
2. **Rank by consequence, not by count.** A proxy feeding a published correlation or a standing
   law outranks a descriptive catalogue entry. Count citing files by `UNIT-DRIFT-DEFECT.md`
   §6.2's rule — external files only, own sub-finding family excluded — and remember that
   §6.2's own closing clause applies: **a count is a rough guide, not a queue.**
3. For each, apply Screen B **against the filesystem**, never against the finding's own
   statement about the filesystem.
4. For the top few, **compute the agreement and re-run the host headline.** Report ρ over the
   operating range and over the full set, and declare the size loading of every variable.
5. Classify by §6. **Do the top few properly rather than many badly**, and **say which you did
   not reach** — otherwise the next session re-derives the list instead of extending it.
6. **Correct the document that carries the claim, not only the one that refutes it**
   (`ABSENCE-CLAIMS.md` §4). A correction landing only in the child does not stop the parent
   being inherited again.

**Expect to find that some proxies are fine.** The 860 rubric being noise does not make them all
noise, and two of the three measured so far carry real information. **A hand-built proxy is not
automatically noise — it is automatically an unmeasured claim**, and the only thing that settles
which is the measurement.

---

*Written 2026-08-08 by Waiel Al-Shujaa, after a rubric that reproduced its target at ρ = +0.055
carried a published correlation into 61 files. Substituting a score you assigned for a quantity
you could have computed is itself an empirical claim, and it is the one claim in the substitution
that never gets tested. Bismillāhi al-Raḥmāni al-Raḥīm.*
