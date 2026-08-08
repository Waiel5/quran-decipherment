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
