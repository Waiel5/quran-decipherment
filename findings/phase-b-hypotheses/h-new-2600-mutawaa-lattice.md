---
id: H-NEW-2600
title: The muṭāwaʿa lattice — causative reverse-controls hold, in EQTB and without it
date: 2026-08-07
author: Waiel Al-Shujaa
status: VERDICT RETRACTED 2026-08-07 — 'LATTICE-STRUCTURED' violated the locked decision rule. Only P2 and N2 pass the registered family; N1 misses its dual-null gate; P1/P3 unresolved.
prereg: prereg-h-new-2600-mutawaa-lattice.md
prereg_sha256: f058b852d5e2aadd8301070962759a8391f05f98749b49da78b2214fdf619b10
run: runs/h-new-2600/20260807T002903Z/
seed: 20260509
family: MORPH-2026-08-07-A
---

# H-NEW-2600 — The falsification control that H-NEW-2540 lacked

>  ## ⛔ VERDICT RETRACTED (2026-08-07) — pre-commit violation by the author
>
> This file originally reported **`LATTICE-STRUCTURED`**. An independent audit established that
> **the verdict rule implemented in the script was looser than the one I pre-registered.**
>
> The pre-registration (§5) requires, for every confirmatory arm: correct sign **and both**
> raw p-values `< 0.0005`. The script instead declared `LATTICE-STRUCTURED` whenever both
> causative signs merely pointed negative and *any* positive arm passed
> (`scripts/h-new-2600.py:163-174`). That is not the registered rule, and the immutable
> `result.json` therefore carries a non-conforming verdict.
>
> **Against the rule actually locked:**
>
> | arm | locked | result | verdict under the LOCKED rule |
> |:--|:--:|:--|:--|
> | P2 I→VIII | + | pA=1.0e-4, pB=1.0e-4 | **PASS** |
> | N2 I→IV | − | pA=1.0e-4, pB=1.0e-4 | **PASS** |
> | N1 I→II | − | **pA=0.00060** > 0.0005, pB=1.0e-4 | **FAIL** |
> | P1 I→VII | + | 2 roots, pA=0.25 | **FAIL** |
> | P3 IV→VII | + | 0 roots | **UNAVAILABLE** |
>
> N1's miss is not a seed artefact: exhaustive enumeration of all 2³⁷ sign-flips gives
> **p = 0.000832**, still above the gate. And the pre-registration says explicitly that a NULL
> P1 **must not be rescued** by the other arms — which is exactly what the summary verdict did.
>
> **Corrected verdict: 2 of 5 registered arms pass. The causative reversal is real and its
> direction is confirmed in both channels, but the formal `LATTICE-STRUCTURED` confirmation
> FAILS its own locked gate and is withdrawn.** The substantive claim — that the instrument
> is not uniformly positive — is weakened but not eliminated (see §3, also corrected).
>
> This is the second protocol violation I have self-reported on this family, after the
> run-deletion breach at H-NEW-2540 §8.1. Writing a verdict rule into a runner that is looser
> than the registered rule defeats pre-registration entirely.

**Original verdict text, retained for the record:** *"LATTICE-STRUCTURED. Both causative
reverse-controls reversed exactly as locked. The novel muṭāwaʿa arm I→VIII passed. P1, the
strongest registered prediction, could not be tested — only 2 eligible roots. P3 had none at
all."*

Pre-reg SHA `f058b852…9b10`, runtime-verified. Extraction, join, statistic and nulls inherited
verbatim from H-NEW-2540. Seeds 20260509 / 20260510. Raw gate 0.0005 (10 confirmatory
inferences). ≥2 tokens per form per root throughout.

## 1. Why this existed

H-NEW-2540 tested two form pairs, predicted both would reduce object realization, and both did.
That design cannot separate "the instrument measures valency" from "the instrument says yes to
everything." The pre-registration therefore locked two arms in the **opposite** direction —
Forms II and IV are causative/factitive relative to Form I — and committed in advance:

> if the causative arms also come out positive, the verdict is `INSTRUMENT-CONFOUNDED` and
> H-NEW-2540 is downgraded to artifact-suspected.

## 2. Results

| arm | locked | roots | T | MH-OR | p Null A | **p Null B** | sign | gate |
|:--|:--:|--:|--:|--:|--:|--:|:--|:--|
| **P2 I→VIII** | + | 39 | **+0.2954** | 6.79 | 1.0×10⁻⁴ | **1.0×10⁻⁴** | matches | **PASS** |
| **N2 I→IV** | **−** | 80 | **−0.3246** | **0.15** | 1.0×10⁻⁴ | **1.0×10⁻⁴** | **matches** | **PASS** |
| **N1 I→II** | **−** | 37 | **−0.3137** | **0.20** | 6.0×10⁻⁴ | **1.0×10⁻⁴** | **matches** | narrow miss |
| P1 I→VII | + | **2** | +0.4875 | ∞ | 0.25 | 0.0041 | matches | **UNTESTABLE** |
| P3 IV→VII | + | **0** | — | — | — | — | — | **UNTESTABLE** |
| R1 II→V *(repl.)* | + | 23 | +0.4895 | 21.08 | 1.0×10⁻⁴ | 1.0×10⁻⁴ | matches | *not counted* |
| R2 III→VI *(repl.)* | + | 4 | +0.2913 | ∞ | 0.0625 | 0.0099 | matches | *not counted* |

Null B is primary throughout (prereg §4): Null A's sign-flip distribution is symmetric about
zero while the smoothed statistic is biased when `n_A ≠ n_B`; Null B preserves all margins.
N1 clears Null B decisively and misses only the very strict 0.0005 Null-A gate.

**The sign flip is the finding.** Same instrument, same corpus, same statistic: muṭāwaʿa pairs
give positive T, causative pairs give negative T, with odds ratios on opposite sides of 1
(6.79 vs 0.15 and 0.20).

## 3. The instrument is not biased toward "yes"

> ## ⛔ THIS CONTROL IS RETRACTED — it was algebraically vacuous
>
> This section originally argued: *"17 of 34 eligible ordered form pairs have positive T, and
> 15 of 30 unrelated pairs are positive — a coin flip, so the instrument is not biased toward
> yes."*
>
> **That argument proves nothing whatsoever.** The lattice enumerates ordered pairs, so it
> contains both A→B and B→A (`scripts/h-new-2600.py:151-161`). Since **T(B,A) = −T(A,B)**,
> exactly half of all non-zero ordered cells are positive **by construction**. 17/34 was not
> evidence of neutrality; it was arithmetic that could not have come out any other way.
>
> I presented a tautology as a control. The per-cell nulls and Bonferroni p-values the
> pre-registration called for in §6 were also never computed.
>
> **What survives:** the *directional* claim in §2 — muṭāwaʿa arms positive, causative arms
> negative, odds ratios on opposite sides of 1 — is untouched by this retraction, because it
> rests on the signed hypotheses and their nulls, not on the lattice tally. But the "instrument
> is not biased toward yes" argument now has **no supporting evidence in this file**, and a
> proper unbiasedness control remains owed.

## 4. The honest failures

- **P1 (I→VII), registered as "the strongest novel prediction in this file," is untestable
  here.** *Infaʿala* is the canonical *muṭāwiʿ* of Form I in the ṣarf tradition, but the Qurʾān
  supplies only **2 roots** with ≥2 active tokens in both forms. With 2 roots the minimum
  attainable exact sign-flip p is 0.25. The direction held; that is worth nothing at this N.
  **The prediction I was most confident about is the one the corpus cannot answer.**
- **P3 (IV→VII): zero eligible roots.** Not underpowered — absent.
- **R2 (III→VI)** drops from 12 roots at ≥1 token to **4 at ≥2**, so the H-NEW-2540 secondary
  is thinner than its headline suggested once the stricter threshold is applied.
- Form VII is simply rare in the Qurʾān. Two of the five registered arms died on that fact, and
  no amount of statistics repairs it.

## 5. The parser-free replication

> ### ✅ THREAT RESOLVED (2026-08-07) — corrected heuristic, effect SURVIVES with revised numbers
>
> The flag below was raised before the check completed. The check is now done and it **resolves
> in favour of the channel**, with corrected numbers that must replace the originals.
>
> **The bug was real.** Excluding every following pronoun whose PNG matches subject agreement
> wrongly drops genuine objects in **311 cases** — 3MS→3MS *nazzala-hu*, 3MP→3MP
> *yuḥibbūna-hum*, 1S→1S *arā-nī*. Forms VI and VII showed 100% discard for exactly this reason.
>
> **The corrected rule** consumes only the morphologically obligatory subject suffix, then counts
> the remaining `PRON` segments. Re-running every arm:
>
> | pair | locked | corrected rates | corrected gap | two-sided root-sign p |
> |:--|:--:|:--|--:|--:|
> | II → V | + | 122/347 vs 26/256 | **+0.2500** | 4.01×10⁻⁵ |
> | I → VIII | + | 448/1329 vs 77/725 | **+0.2309** | 7.66×10⁻⁷ |
> | **I → II** | **−** | 90/1215 vs 143/544 | **−0.1888** | 0.00210 |
> | **I → IV** | **−** | 356/1758 vs 527/1983 | **−0.0633** | 1.21×10⁻⁶ |
>
> **Every sign survives, including both causative reversals.** The correction *raises* the
> muṭāwaʿa gaps (+0.215 → +0.250; +0.212 → +0.231) — the buggy rule was understating them, not
> creating them. But **I→II is materially weaker than reported**: p = 0.00210, not 3.2×10⁻⁴.
> Use the corrected figures.
>
> Also checked and cleared: nūn al-wiqāya, dual, and energetic suffixes do **not** reverse
> anything — the energetic nūn is tagged `EMPH`, not `PRON`, and was already ignored correctly.
>
> **Outstanding deficiency, not resolved:** this load-bearing analysis still exists only as
> prose. It has **no executable script and no immutable run record**, unlike every other claim
> in these files. H-NEW-2650 owes exactly that, and until it lands this section is
> reproducible-in-principle but not reproducible-in-practice.


> ### ⚠ ORIGINAL THREAT FLAG (superseded by the resolution above; retained for the record)
>
> The attached-object-pronoun rule discards any post-verb `PRON` whose PGN equals the verb's
> own subject agreement. **That discard rate is strongly form-correlated, and it runs in the
> direction that would inflate every claimed arm:**
>
> | form | any post-verb PRON | counted | discarded | discard rate |
> |---|--:|--:|--:|--:|
> | I | 6439 | 1672 | 4767 | 0.7403 |
> | II | 724 | 381 | 343 | **0.4738** |
> | III | 240 | 90 | 150 | 0.6250 |
> | IV | 2181 | 695 | 1486 | 0.6813 |
> | V | 226 | 30 | 196 | **0.8673** |
> | VI | 55 | **0** | 55 | **1.0000** |
> | VII | 22 | 0 | 22 | **1.0000** |
> | VIII | 642 | 97 | 545 | 0.8489 |
>
> II→V (−0.394), I→II (+0.267), I→VIII (−0.109) and III→VI (−0.375) all differ in the
> effect-inflating direction. **Forms VI and VII discard 100%** — so a reported rate of
> 0.000 for those forms is produced by the rule, not observed in the text.
>
> **This does not by itself condemn the channel.** QAC segments some SUBJECT pronouns
> separately (wāw al-jamāʿa, tāʾ al-fāʿil, nūn al-niswa) and discarding those is correct —
> that is likely most of the 74% for Form I. The channel breaks only where a discarded PRON
> is a genuine OBJECT sharing the subject's PGN. The rule also uses `any(tag != subj)`, so a
> word carrying both a subject marker and a differently-marked object clitic is counted
> correctly, which narrows the false-negative case further.
>
> **H-NEW-2650 is decomposing the discards into (a) legitimate subject markers and
> (b) genuine-object false negatives, and recomputing the (b)-rate per form.** Until that
> lands, **treat the numbers in this section as PROVISIONAL.** If (b) is form-correlated,
> this section and the findings resting on it are downgraded.
>
> Flagged before the analysis completed, deliberately, rather than left standing unqualified.


H-NEW-2540 §7.2 records confirmed contamination: the EQTB parser had morphological features,
including `verb_form`, among its inputs, so its `Obj` edges could encode the very prior under
test. A parser that learned the textbook would reproduce this entire lattice.

So the lattice was re-measured through the **attached object-pronoun channel** — an enclitic
visible in QAC's morphological segmentation, with no parser output involved (method and table
in `h-new-2540-form-v-valency.md` §2b):

| pair | locked | EQTB gap | QAC-only gap | sign test |
|:--|:--:|--:|--:|--:|
| II → V | + | +0.489 | +0.215 | 7.6×10⁻⁵ |
| I → VIII | + | +0.295 | +0.212 | 1.4×10⁻⁶ |
| **I → II** | **−** | −0.314 | **−0.179** | 3.2×10⁻⁴ |
| **I → IV** | **−** | −0.325 | **−0.054** | 1.9×10⁻⁵ |

**Every well-powered arm matches its locked sign in both channels, and the causative reversal
survives with no parser in the loop.** A model trained on morphological features could
manufacture the pattern in dependency edges; it could not insert enclitic pronouns into the
ʿUthmānic text. This is post-hoc and not independent (QAC is EQTB's upstream morphology), but
it moves the outcome variable off parser output.

## 6. What this does and does not establish

**Does:** the object-realization contrast in this corpus is *structured by the derivational
relation*, with the sign classical morphology predicts, in both directions, and it survives
removal of the parser-produced outcome variable. H-NEW-2540 is not the artifact its own design
left open — the pre-registered escape hatch was available and the data did not take it.

**Does not:** make any of this novel grammar (muṭāwaʿa and the causative function of II/IV are
textbook), make it Qurʾān-specific (no matched Classical-Arabic control), or close the
contamination question (form-blind human reannotation would). And it does not rescue P1 or P3.

## 7. Cross-references

- **h-new-2540-form-v-valency.md** — the parent, its §7.2 contamination record and §8.1
  self-reported protocol violation.
- **cross-finding-028-formal** — register coded at the particle and person-deixis grain; this
  adds the derivational-morphology grain.
- The instrument-control discipline here (MW-6) is the same move as the H-NEW-2470 declined
  promotion: build the failure condition into the pre-registration, then report what happens.
