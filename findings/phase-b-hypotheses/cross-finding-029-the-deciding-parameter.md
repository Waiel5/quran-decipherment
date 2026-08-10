---
id: cross-finding-029
title: The deciding parameter — the quantity that fixed the verdict was not the quantity under test; six distinct parameters found in two days
date: 2026-08-09
author: Waiel Al-Shujaa
type: methodological
status: CONVERGENT — 5 anchors 2026-08-09, extended to 6 deciding parameters 2026-08-10; all self-reported
---

# Cross-finding 029 — the deciding parameter

**Scope warning, stated first.** This is a law about **the instrument, not the text.** Every other
cross-finding in this project asserts something about the Quran. This one asserts nothing about the
Quran. It is filed here because it governs how the others should be read, and because five
independent lanes converged on it in a single day without being pointed at each other.

---

## 1. The five anchors

| # | Result | The quantity under test | **The quantity that actually decided it** |
|:--|:--|:--|:--|
| 1 | [[AUDIT-H-NEW-206-LENGTH-CONFOUND]] | do surah clusters track the muqaṭṭaʿāt? | **`surah_length` was itself a clustering feature** |
| 2 | [[h-new-3010-conditional-register]] | are conditionals register-coded? | **which of three length channels controlled it** — p = 0.0006 vs 0.027–0.044, a ~70× swing |
| 3 | [[h-new-3030-sajdah-glyph]] | are sajdah loci imperative-dense? | **the power of the test** — MDE 3.25× against a corpus whose strongest law runs 1.27–2.58× |
| 4 | [[h-new-3020-loanword-donor-strata]] | do donor languages stratify by phase? | **which rater assigned the donor** — Jeffery vs al-Suyūṭī agree on 52.4%, κ = 0.386 |
| 5 | Two wrong *Itqān* nawʿ citations | what does al-Suyūṭī say? | **which field of the citation nobody could check** — line offsets survived twice, nawʿ numbers rotted twice |

## 2. The claim

> **In each case a free parameter, chosen by the analyst and not recorded as a choice, determined
> the verdict more than the hypothesis did — and in each case it was invisible because nothing
> downstream failed when it was wrong.**

The second clause is what makes this a law rather than a list of mistakes. These are not errors that
announce themselves. A clustering run with length in the feature matrix returns a beautiful
p-value. A test residualised on one length channel returns a clean PASS. An underpowered NULL looks
exactly like a well-powered NULL. A citation to the wrong nawʿ carries correct line offsets and
resolves fine for anyone who checks the offsets. **Every one of these produces a well-formed,
publishable, internally consistent artefact.** That is why they survive.

### 2.1 Why it is a convergence and not a coincidence

The five lanes were dispatched on unrelated hypotheses — clustering, conditionals, prostration
marks, loanwords, and a citation audit — with no shared instrument and no shared data beyond the
corpus itself. Four of the five were *self-reported by the lane that committed the error*, under
briefs that demanded confound disclosure before the primary test. The convergence is therefore a
property of the briefing discipline, not of the hypotheses.

### 2.2 The honest limit on the convergence

**Five anchors on one day is not five independent draws.** They share a cause: the briefs issued
that day all demanded that confounds be reported *before* the primary test, which is precisely the
instruction that makes a deciding parameter visible. Under a different briefing regime the same
five lanes would have produced five clean findings and no convergence. So this cross-finding
documents **what a particular discipline surfaces**, and should not be quoted as a frequency
estimate — "five in one day" is a fact about the method, not about the base rate.

## 3. The rule

> **Declare the deciding parameter, not just the result.**
> Every finding should name the single choice its verdict was most sensitive to, and report the
> verdict under at least one alternative setting of it.

This is stronger than the existing rules-tuple requirement, which asks *which* conventions were
used. This asks **which convention the answer depended on** — a question the analyst can only answer
by varying it.

### 3.1 What each anchor contributes as a concrete check

1. **Before any cluster-versus-label test:** is the label correlated with a feature in the matrix?
2. **Before writing "residualised on length":** length is at least three variables (verse count,
   word count, mean verse length). Name the channel, and run all of them.
3. **Before publishing a NULL:** state the minimum detectable effect. A NULL is a claim of absence
   and is only as wide as the power that produced it. See §3.2.
4. **Before treating a hand-assigned field as data:** find a second rater and report the agreement.
5. **In any citation carrying both a machine locator and a human label:** derive the label from the
   locator. Do not type them side by side — the unchecked field is the one that rots.

### 3.2 The strongest single transfer: a NULL must state its MDE

[[ABSENCE-CLAIMS]] §1 observes that claims of absence go unaudited because nothing downstream fails
when they are wrong — the blocked experiment is simply never run. **An underpowered NULL does
exactly this.** The parallel holds including the failure mode, so the remedy transfers directly:

| | ABSENCE-CLAIMS requires | the parallel requirement |
|:--|:--|:--|
| a claim that X is absent | state the search command and the paths searched | — |
| a NULL result | — | **state the MDE and the power** |

H-NEW-3030 is the worked example. It reports S\* = 12 against S_max = 26, so the design *can*
reject — the untestable branch was computed and **did not fire**. That distinction had to be
computed to be known; asserting either way would have been wrong. Its MDE curve is reusable: any
future n≈15 matched-pool test in this project reads its floor off `B1_quantile_power_curve`
(top quartile for 80% power; 15% power against a uniform above-median effect).

## 4. What this does NOT license

It does not license retro-demoting findings by suspicion. A deciding parameter is a thing you
*find by varying it*, not a thing you allege. Anchor 2 is instructive in exactly this way: F-3's
contrast was real and correctly signed under every channel — only its *significance* moved. The
finding is that the verdict was fragile, not that the effect was fake.

Nor does it apply evenly. [[TIED-OUTCOME-DEFECT]] §7.3 established that 454 of this project's 464
scripts use permutation nulls, which are immune to the specific failure it names. **A standing
convention adopted for general rigour can immunise a corpus against a failure nobody has named
yet** — and that, rather than case-by-case vigilance, is the durable form of this rule.

---

**Anchors:** [[AUDIT-H-NEW-206-LENGTH-CONFOUND]] · [[h-new-3010-conditional-register]] ·
[[h-new-3020-loanword-donor-strata]] · [[h-new-3030-sajdah-glyph]] · [[ERRATUM-COMMIT-eb6a40d0e]]
**Related:** [[UNIT-DRIFT-DEFECT]] · [[ABSENCE-CLAIMS]] · [[PROXY-CLAIMS]] · [[TIED-OUTCOME-DEFECT]]

---

## 5. Extension, 2026-08-10 — the law generalises past length, and the parameter list is now SIX

§1's five anchors were all found on 2026-08-09. Four further lanes closed on 2026-08-10 and each
surfaced a deciding parameter the original file did not name. The pattern is not "length is
underspecified"; **length was simply the first instance.**

| # | deciding parameter | anchor | swing |
|--:|:--|:--|:--|
| 1 | **length channel** — verse count vs word count vs mean verse length | [[h-new-3010-conditional-register]] | **70×** in p |
| 1b | same | [[h-new-3040-modality-axis]] | verdict **flips**, 3 PASS / 5 NULL of 8 |
| 1c | same | [[h-new-3070-deictic-gradient]] | **29×** on H1, 22× on H2 |
| 2 | **control feature set** — which features enter the matrix | [[h-new-3040-modality-axis]] | dropping EMPH flips PASS → NULL |
| 3 | **rater identity** — who assigned a hand-coded label | [[h-new-3020-loanword-donor-strata]] · [[h-new-3090-kinship-affiliation]] | κ = 0.386 / 0.468 — raters agree about half the time |
| 4 | **lemma vs root** — the counting unit | [[h-new-3090-kinship-affiliation]] | **126×** in p |
| 5 | **coarsening choice** — how many classes a categorical is reduced to | [[AUDIT-REGISTER-PHASE-COLLINEARITY]] §CORRECTION | 36.8% → 57.0% degeneracy |
| 6 | **chronology instrument** — Nöldeke vs Egyptian standard | [[h-new-3070-deictic-gradient]] | PASS → **NULL** |

### 5.1 What the extension changes

The original §3 rule — *declare the deciding parameter* — stands. What changes is that **the list is
not closable.** Six parameters found in two days, each by a different lane, none anticipated by the
lane that found it. The honest form of the rule is therefore not a checklist but a procedure:

> **Before locking a design, name every choice that could have gone another way, and run the ones
> you can. Report the verdict under the worst of them.**

Three lanes now build this into the instrument rather than checking it afterward.
[[h-new-3080-quantifier-scope]] takes its p as the **maximum over all non-degenerate length
channels**, so no channel had to be chosen; [[h-new-3070-deictic-gradient]] clears α under the
**worst of nine** settings; [[h-new-3090-kinship-affiliation]] runs 36 cells. That is the mature
form: **not "which parameter decided this?" but "make the verdict survive all of them."**

### 5.2 Two anchors where the parameter did NOT decide — reported because absence of the effect matters

Not every finding is fragile, and saying so is what keeps this from being a universal solvent:

- [[h-new-3090-kinship-affiliation]] — the **length** channel spans only 1.37×–2.0×. Length was
  irrelevant there; the counting unit was everything.
- [[h-new-3080-quantifier-scope]] — survives all four channels, and survives deleting 34.8% of its
  own most formulaic material with the effect **growing**. Its fragility lies elsewhere entirely:
  a denominator of three tokens.

**A deciding parameter is found by varying it, never by alleging it.** Two of the seven anchors
above varied it and found nothing.

