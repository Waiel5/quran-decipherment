# Audit: cross-finding-028 is worded more broadly than its anchors support — 0 of 6 extensions have passed

**Date:** 2026-08-09
**Status:** SCOPE NARROWING proposed. The law's numbers stand; its generality does not.
**Trigger:** the INTEGRATE question — *"whether any standing law is now worded more broadly than its
anchors support."* Surfaced by F-14's Step-0 census; verdicts re-verified here from each file.

---

## 1. The law as written

`cross-finding-028-formal-register-coded-discourse-grammar.md`, codified 2026-05-30:

> **"Register is coded in function-words + person-grammar."**

Its anchor is **H-NEW-2530**, status `CONFIRMED`: a 6-feature per-surah vector separates three
registers at 76.9% leave-one-out accuracy against a 44% baseline, p = 10⁻⁴.

## 2. Every attempt to extend it with a fresh lemma count has failed

Six pre-registered attempts to add a new function-word class to the law. Verdicts read directly from
each finding's front-matter, not from any summary:

| finding | what it added | verdict |
|:--|:--|:--|
| H-NEW-2630 | realis/irrealis conditionals (*in* vs *law*) | **NULL-REVERSED** — H2 pre-commit violation, H3/H4 NULL |
| H-NEW-2640 | modality (jussive/subjunctive, certainty particles) | **NULL** — 4/4 registered inferences fail, two reversed |
| H-NEW-2700 | loanword donor language | **ALL FOUR NULL** — including the co-primary, with reversed direction |
| H-NEW-3010 | conditionals again, on the Neuwirth–Sinai labels | **NULL** — 0 of 12 tests clear |
| H-NEW-3020 | donor language, second rater | **NULL** at the primary tuple (κ = 0.386) |
| H-NEW-3040 | modality again, eight length channels | **DIRECTIONAL not PASS** (3/8); orthogonality NOT SUPPORTED |

**Six for six.** Not one added column survived its own pre-registration.

## 3. What that does and does not mean

**It does not refute the law.** H-NEW-2530's 76.9% is real and was not obtained by the route that
keeps failing.

**It bounds the law, and the bound is specific.** Note what H-NEW-2530 actually is: a vector
assembled from **detector outputs of four prior findings** (H-NEW-2250, 2490, 2500, 2520) — iltifāt
type, *thumma*-doubling, genre crosstab, pericope onsets. It is not a fresh lemma count. Every one
of the six failures *is* a fresh lemma count.

So the evidence supports:

> **Register is recoverable from a specific, already-validated set of discourse detectors.**

and does **not** support:

> ~~Register is coded in function-words generally, such that new function-word classes will carry
> it.~~

The second reading is what the law's current wording invites, and it is the reading that six
pre-registered tests have now falsified.

## 4. The law already carries an unrelated correction pointing the same way

`cross-finding-028` bears a 2026-08-07 notice: the pericope-flip test underlying an earlier draft
**flips on pre-Islamic poetry (5/5) and al-Bukhārī (4/5)** under a genre control. The mechanism there
is generic topical burstiness, not anything Quran-specific. The numbers stood; the *"structurally
unusual"* inference did not.

That is the same failure shape as §3 — **a result that holds for its own instrument being read as a
general property.** Two independent routes, one conclusion: the law's anchors are narrower than its
sentence.

## 5. Proposed amendment

Restate as:

> **Register is recoverable at 76.9% LOO from the six-detector vector of H-NEW-2530** (iltifāt type,
> *thumma*-doubling, genre crosstab, pericope onsets). **Six pre-registered attempts to extend this
> to fresh function-word classes — conditionals ×2, modality ×2, loanword donors ×2 — have all
> returned NULL or reversed. The generalisation to function-words at large is not supported.**

This changes no number and retracts no finding. It stops the law claiming a scope its own extension
record contradicts.

## 6. The base rate is itself the useful output

Anyone designing the next particle-vs-register test now has a prior worth writing into their
pre-registration: **0 of 6.** That is not a reason to skip the test — a 7th attempt is exactly how a
base rate gets revised — but it is a reason to state the prior honestly rather than inheriting the
map's optimistic per-item priors, which rated three of these six as likely CONFIRMED before they ran.

Related: [[cross-finding-029-the-deciding-parameter]] · [[AUDIT-REGISTER-PHASE-COLLINEARITY]]
(the register axis is degenerate against phase for 43% of the corpus, which bounds these tests
further) · [[ABSENCE-CLAIMS]]

---

## 7. Why 0-of-6 — a mechanism, built from two facts both already disclosed

This section discovers nothing. It joins two things the project had already written down
separately, and the join explains the base rate in §2.

**Fact one, from `h-new-2500.py` line 60.** The legal register is *defined* by counting two
substrings:

```python
LEGAL_MARKERS = ["يا أيها الذين آمنوا", "كتب عليكم"]
```

**Fact two, from H-NEW-2530 honest-limits §2**, disclosed at publication:

> *"f_iltifāt-type partly co-determines the legal label by construction-adjacency: the legal
> register's defining marker drives both its genre label (via 2500's proxy) and its 2↔3 iltifāt
> dominance. These are not circular (the genre proxy uses yā ayyuhā alladhīna āmanū substrings, NOT
> iltifāt counts), but the two are correlated by the underlying register, which is the point — the
> law claims register IS coded in the grammar."*

That defence is honestly stated and it is not wrong. But put beside §2's record it predicts exactly
what happened:

> **`يا أيها الذين آمنوا` is itself person-grammar** — a second-person plural community vocative.
> So the legal register is *defined* by a grammatical marker, and the feature that best isolates it
> (`f_iltifāt-type`, F = 19.79, the second-strongest of six) measures the same construct the
> definition uses. Where a candidate feature shares that construct, separation is close to
> guaranteed. **Where it does not — conditionals, modality, loanword donors — there is nothing to
> recover, and six pre-registered attempts found nothing.**

So the law is not failing to replicate. **It is succeeding exactly on the span where its
grouping variable and its features share a construct, and failing everywhere else** — which is what
0-of-6 on unrelated word classes looks like from the inside.

This does not retract H-NEW-2530: `f_qālū` (F = 33.54) is the strongest separator and has no such
overlap, so the joint result is not an artefact. It sharpens §5's amendment. The scope is not merely
*"the six-detector vector"* — it is:

> **narrative-onset densities, which are construct-independent of the register definition, plus a
> person-grammar axis that is construct-adjacent to it and should be reported as such.**

**Note on how this section came to exist.** It was nearly published as a discovery. A grep found
H-NEW-2800 had already recorded that *kutiba ʿalaykum* is "the same object as one of the frames",
and a second grep found H-NEW-2530's limits §2 above. Both disclosures were already on disk, made by
the findings themselves at publication. **Three separate times on 2026-08-09 the prior-work check
converted an intended discovery into a citation.** That is the check working, and it is the reason
nothing in this section is claimed as new.

---

## 8. Update 2026-08-10 — the record is 0 of 7, and the seventh was the one that could have complicated §7

H-NEW-3130 (derived-form profile against register) is the seventh pre-registered extension. **NULL,
0 of 6 arms.** It matters more than the six before it for one reason:

**It is the only candidate whose predictor overlapped the construct that *defines* the legal
register.** `آمنوا` parses as a **Form IV verb** — 537 Form IV verbs carry `ROOT:Amn`, 15.4% of all
Form IV verb tokens. §7's mechanism predicts that a feature sharing the defining construct should
*succeed*. So this was the test that could have complicated it.

**It did not.** Ablating the 91 full-vocative Form IV tokens moves the flagship contrast from
−0.0285 to −0.0248 — **the overlap is real, measured, and immaterial.** §7's mechanism survives the
one test designed to strain it.

**What killed it instead was the confound the map named**: permuting verb forms *within root*
reproduces **32.19 of the observed 33.63 accuracy points — 95.7%.** Against a null that knows nothing,
the form profile is a strong classifier (p = 0.0001); against a null that knows only which roots each
surah uses, it is worth 1.4 points at p = 0.41. Root identity does not merely intrude on the form
profile; it very nearly *is* the form profile.

And the mechanism of the residual is legible: the classifier recovers **narrative (recall 0.731) and
legal (0.588) and nothing else** — oath 0.000, hymn 0.000. Those two are the long registers (mean
verse length 10.80 and 19.41 against 4.34 and 5.19). *"Register signature"* here means **"long surahs
separate from short ones,"** which is exactly why residualising on verse length destroys it — a
**385× p-swing**, the largest recorded in this project.

