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
