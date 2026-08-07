---
id: H-NEW-2630
title: Realis vs irrealis conditionals are NOT register-coded — the mood hypothesis is rejected; conditional PRESENCE is the real signal
date: 2026-08-07
author: Waiel Al-Shujaa
status: NULL-REVERSED on the registered mood hypothesis (H2 pre-commit violation; H3/H4 NULL) · H1 PASS but mood-blind · H5 PASS-BUT-MISATTRIBUTED
prereg: prereg-h-new-2630-conditional-register.md
prereg_sha256: 40f899a4bdb807d3ac39c679c532b51ab90fe7f020f4c01b4bd0dcd1281a2a5a
runs:
  - runs/h-new-2630/20260807T005410Z/            # primary, registered
  - runs/h-new-2630/20260807T005746Z-diagnostics/ # post-hoc, MW-7 capped
seed: 20260509
seed_replication: 20260519
family: COND-2026-08-07-A
proposed_amendment_to_cross_finding_028: NONE — the registered hypothesis failed
---

# H-NEW-2630 — The conditional column that is not about mood

**Verdict: the pre-registered hypothesis is REJECTED.** *in* vs *law*/*lawlā* — the
realis/irrealis contrast — does **not** carry register information. One of the four
substantive cells reversed against its locked direction, two returned NULL, and the
one that passed turns out to be mood-blind. cross-finding-028-formal gets **no
amendment** from this test.

A different thing is true, and it is not what I registered: **whether a surah contains
a conditional at all** separates legal-Medinan from eschatological-mufaṣṣal almost
perfectly. That is an unregistered, post-hoc observation and is reported below as a
candidate for a fresh pre-registration, not as a finding.

Pre-reg SHA `40f899a4…2a5a`, runtime-verified. Four frozen inputs SHA-verified. Seeds
20260509 / 20260519, 10,000 permutations per cell, Bonferroni k = 5, α_bon = 0.01.

---

## 1. The registered cells

| # | Hypothesis | Locked direction | Observed | p | Verdict |
|---|---|---|---|---|---|
| **H1** | realis denser in legal | `> 0` | **+0.16815** | **9.999×10⁻⁵** | **PASS** |
| **H2** | irrealis avoids legal | `< 0` | **+0.03795** | 1.00000 | **PRE-COMMIT VIOLATION** |
| **H3** | mood balance separates registers | KW large, legal highest | H = 4.753 | 0.09229 | **NULL** |
| **H4** | …and survives length control | same | H = 1.523 | 0.47715 | **NULL** (ordering also flips) |
| **H5** | it repairs the legal boundary | recall > 8/20 | 8 → **16/20** | 5.999×10⁻⁴ | PASS *(but see §4)* |

### 1.1 H2 is a pre-commit violation, stated with full prominence

I locked the direction that *law*/*lawlā* would be **depleted** in legal-Medinan,
on the reasoning that counterfactual rebuke belongs to polemic rather than to
legislation. Per-verse densities (tuple A):

| register | realis `d_R` | irrealis `d_I` |
|---|---:|---:|
| narrative | 0.05388 | 0.02523 |
| **legal_medinan** | **0.19908** | **0.05276** |
| eschatological_mufaṣṣal | 0.01314 | 0.00673 |

Legal-Medinan is the **highest** register on *both* particles. The locked sign is
wrong. This is not re-describable as a discovery: the substantive claim was that mood
*discriminates*, and the mechanism I proposed for H2 does not exist in the corpus.

### 1.2 H3/H4 — the balance carries nothing

`C(s) = (n_R − n_I)/(n_R + n_I)` is defined for **53 of 91** surahs. Its Kruskal-Wallis
omnibus reaches only p = 0.0923, well outside α_bon = 0.01. Under residualisation on
`log V(s)` and `log T(s)`, it falls to p = 0.4772 **and the locked ordering inverts** —
eschatological becomes the highest-mean class (+0.1021) and legal drops to +0.0211.

My pre-registration §5.1 named H4 the load-bearing cell in advance and committed that
its failure means the whole test is negative regardless of the other cells. H3 failed
before it. That commitment is honoured here.

### 1.3 What H1 actually shows, and what it does not

H1's effect is large and it survives length control: on `d_R` residualised against
`log V(s)` and `log T(s)`, legal-Medinan is at **+0.04343** versus narrative −0.02591
and eschatological −0.00164, diff **+0.05567**, p = 9.999×10⁻⁵.

But length-residualised `d_I` shows the *same* pattern — legal +0.00854, narrative
−0.00467, eschatological −0.00065. Both particles are enriched in legal. So H1 is not
evidence for mood-coding. It is evidence that **legal-Medinan discourse is
conditional-dense**, which is a different claim and one the registered design was not
built to test.

---

## 2. The MW-6 control fired — and it is the whole story

The pre-registration excluded the *generalising* conditionals (`man`, `mā`, "whoever /
whatever") on the ground that their realis/irrealis status is not lexically determined,
and locked the expectation that they would separate the registers **more weakly** than
the mood balance.

They do not:

| instrument | statistic | p |
|---|---|---|
| generalising balance (KW) | H = 3.210 | 0.20228 |
| **generalising density, legal vs rest** | **+0.06214** | **1.9998×10⁻⁴** |

The particles I discarded *because they cannot be scored on the mood axis* concentrate
in legal-Medinan at p = 0.0002 — comparable to the realis particles I kept. Whatever is
happening is a property of **conditionality**, not of **mood**. The control was written
to catch exactly this, and it caught it.

---

## 3. Replication and rules-tuple

- **MW-5 (seed 20260519):** H3 p = 0.09469, H4 p = 0.47635. The NULLs replicate.
- **Rules-tuple stability:** verdicts are identical across all three registered tuples —
  A (per-verse `/V`), B (per-token `/T`), C (widened realis set
  `{<in, <iyn, <im~aA, <il~am}`). H1 PASS / H2 reversed / H3 NULL / H4 NULL in every
  tuple. The result is **RULES-TUPLE-STABLE in its negative direction**; the failure is
  not a normalisation artefact.
- **MW-6 fail-fast assertions, all passed at runtime:** `POS:COND` total = 1049; lemma
  marginals `<in` 578 / `law` 185 / `lawolaA^` 35 / `man` 184 / `maA` 23 reproduced
  exactly; genre marginals reproduced `h-new-2530.json` `n_per_genre`
  (31/20/40/23) exactly.
- **Pipeline validation:** the six-feature baseline reproduces H-NEW-2530's published
  confusion matrix cell-for-cell — narrative 25/3/3, legal 0/8/12, eschatological
  1/2/37, LOO accuracy 0.7692. The classifier is the same instrument, not a re-build.

---

## 4. H5 passed its registered test and I do not believe it means what it says

Adding `C(s)` to the six-feature vector raises legal-Medinan recall from 8/20 to 16/20
(p = 5.999×10⁻⁴) and LOO accuracy from 0.7692 to 0.7912. Registered, direction-locked,
passed.

It is still misattributed, for two reasons.

### 4.1 A specification gap in my own pre-registration

Pre-reg §4 says surahs with no conditional are "undefined, not zero, and are dropped
from `C`-based cells." H5 is a classifier cell and needs all 91 rows, and the
pre-registration **does not say how to fill them**. I filled them with 0.0. That is an
unlocked researcher degree of freedom, and it matters here more than usual: **38 of 91
surahs are undefined**, so the 0-fill silently encodes a definedness indicator inside
the feature. Disclosed rather than buried.

### 4.2 The post-hoc diagnostic (EXPLORATORY, MW-7 capped at α = 0.05)

Run `20260807T005746Z-diagnostics`. Same classifier, same folds; only the added column
varies:

| added feature | LOO acc | legal recall | gain | p |
|---|---:|---:|---:|---:|
| — (six-feature baseline) | 0.7692 | 8/20 | — | — |
| mood balance `C(s)` *(the H5 feature)* | 0.7912 | 16/20 | +8 | 0.00060 |
| **binary "has any conditional"** | 0.8571 | **20/20** | **+12** | 0.00010 |
| total conditional density (mood-blind) | 0.8571 | 17/20 | +9 | 0.00030 |
| realis density only | 0.8681 | 17/20 | +9 | 0.00010 |
| irrealis density only | 0.8132 | 14/20 | +6 | 0.01180 |
| generalising density *(the excluded family)* | 0.7912 | 12/20 | +4 | 0.02440 |
| **all COND lemmas, mood-blind** | **0.8901** | 17/20 | +9 | 0.00010 |
| log verse count *(no linguistics at all)* | 0.7912 | 12/20 | +4 | 0.11319 |

A **single mood-blind bit** — does this surah contain any conditional — recovers
legal-Medinan at **20/20**, beating the mood balance outright. The best overall accuracy
(0.8901) comes from the fully mood-blind all-lemma density. The mood feature is the
*weakest* of the conditional-derived options.

The mechanism is plain in the margins: of the 38 surahs with no realis/irrealis
conditional, **31 are eschatological and 0 are legal**. "Has a conditional" is close to
a perfect negative indicator for the exact class legal was being confused with. That is
what repairs the boundary — not mood.

---

## 5. Honest limits

1. **The registered hypothesis is rejected. This file proposes no amendment to
   cross-finding-028-formal.** The conditional column, as I specified it, does not exist.
2. **The presence signal is entangled with length.** Spearman ρ(has-conditional,
   verse-count) = **+0.6262**, p = 3.17×10⁻¹¹; ρ(`C(s)`, verse-count) = +0.3544,
   p = 5.67×10⁻⁴. Length alone is not sufficient — `log V(s)` gives only 12/20 at
   p = 0.113 while the conditional bit gives 20/20 at p = 0.0001 — but the two cannot be
   separated by this design, which was not built for the question.
3. **§4.1's 0-fill is an unlocked degree of freedom**, and the diagnostic shows it is
   doing part of the work attributed to `C(s)`.
4. **The register labels are H-NEW-2500's surah-scale deterministic proxy**, inheriting
   all of H-NEW-2530's honest limit 1: surahs are internally heterogeneous and the label
   is the *dominant* register only. Q 2 is both legislative and narrative.
5. **Partial circularity in the legal label.** H-NEW-2500's proxy keys legal-Medinan on
   *yā ayyuhā alladhīna āmanū* — a vocative formula, not a conditional — so the label is
   not defined by the feature under test. But legal-Medinan surahs are long, and length
   drives conditional presence, so label and feature share a confounder.
6. **Everything in §4.2 is post-hoc and capped at α = 0.05 single-test under MW-7.**
   None of it may be promoted without a fresh pre-registration.
7. **No qirāʾāt sensitivity.** Ḥafṣ-Kūfan only, as the project standard.

---

## 6. Classical anchoring — what was verified and what was not

- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān* — NOT VERIFIABLE ON DISK, NOT CITED.**
  `data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf` is a
  1,568-page **image-only scan with no text layer**: `pdftotext` produces a 0-byte
  output and `pypdf.extract_text()` returns 0 characters on every sampled page
  (0, 5, 50, 200, 400). The *sharṭ*/*jazāʾ* framing in the pre-registration is therefore
  **my own working hypothesis, not al-Zarkashī's position**, and no passage is attributed
  to him. Acquiring a text-layer edition would be needed to cite him at all.
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*** (English translation on disk,
  `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`,
  extractable) — **VERIFIED at two loci**:
  1. Under *al-Muzāwaja*: *"Here, two meanings are coupled in the conditional phrase and
     its apodosis"* — the *sharṭ*/*jazāʾ* pair as a rhetorical unit.
  2. On the ellipsis of the object of a *shāʾa*-phrase, citing al-Zamlakānī and
     al-Tanūkhī (*al-Aqṣā al-qarīb*): *"If the accusative after the particle 'lau' is
     omitted, it is always mentioned in its apodosis"*, illustrated with Q 41:14
     *qālū law shāʾa rabbunā la-anzala malāʾikatan*, glossed *"If our Sustainer sought to
     send down messengers, He would surely have sent down angels."*
  **MW-6 nawʿ-number tag: UNVERIFIED** — the extraction does not expose nawʿ numbering at
  these loci, so no nawʿ number is asserted.
- **The classical semantics were never in doubt and are not what failed.** al-Suyūṭī's
  *law* example is unambiguously counterfactual. The grammarians' description of the
  particles is correct; what this test rejects is the *distributional* claim I built on
  top of it — that the corpus sorts these particles by register.

---

## 7. Methodological note: the disambiguation this test required

Measured from the frozen QAC file before locking:

| LEM | tagged COND | tagged otherwise | naive substring hits |
|---|---:|---|---:|
| `<in` (إن) | 578 | NEG 114, CERT 5 | **2,396** |
| `law` (لو) | 185 | SUB 16 (*wadda law*) | **339** |
| `lawolaA^` (لولا) | 35 | **EXH 40** | — |

Substring counting would have inflated إن by **4.1×**, لو by **1.8×**, and would have
merged لولا with an exhortative sense that is the *majority* of its attestations (40 of
75). QAC also tags إذا as `T` 405 / `SUR` 3 / `COND` 1, so *idhā* is essentially absent
from the `COND` population and this test is cleanly disjoint from H-NEW-2250.

The disambiguation was necessary but not sufficient: it produced clean populations, and
the clean populations returned a negative answer.

---

## 8. What should be tested next — proposed, not minted

The 20/20 result in §4.2 is the strongest legal-Medinan separation anyone has obtained
on this problem, and it is **not eligible for promotion** from this file: it was noticed
after unblinding, its feature was never registered, and its length entanglement is
unresolved. A new pre-registration should ask, with directions locked in advance:

1. Does mood-blind conditional **presence** separate legal from eschatological *after*
   conditioning on surah length by matched-pair or stratified design — not by OLS
   residualisation, which §1.2 shows is fragile here?
2. Is the effect carried by conditional **syntax** (a protasis-apodosis clause pair) or
   merely by **particle inventory**? A clause-level detector would separate these.
3. Does it replicate on a corpus where "legal" is defined independently of surah length —
   e.g. at the pericope scale, where cross-finding-025-formal predicts thin markers
   behave differently from whole-surah aggregates?

Until that lands, cross-finding-028-formal stands at its four existing columns, with the
legal↔eschatological boundary still its declared soft one.

---

## 9. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2630-conditional-register.md`
- scripts: `findings/phase-b-hypotheses/scripts/h-new-2630.py`,
  `findings/phase-b-hypotheses/scripts/h-new-2630-diagnostics.py`
- runs (both retained, neither superseded):
  `findings/phase-b-hypotheses/runs/h-new-2630/20260807T005410Z/` (registered),
  `findings/phase-b-hypotheses/runs/h-new-2630/20260807T005746Z-diagnostics/` (post-hoc)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2630.json`

---

*H-NEW-2630 — registered hypothesis REJECTED, 2026-08-07, Waiel Al-Shujaa. The particles
are exactly what the grammarians said they were; the corpus simply does not sort them by
register. Bismillāhi al-Raḥmāni al-Raḥīm.*
