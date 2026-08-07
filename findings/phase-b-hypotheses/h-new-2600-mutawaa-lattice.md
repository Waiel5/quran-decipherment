---
id: H-NEW-2600
title: The muṭāwaʿa lattice — causative reverse-controls hold, in EQTB and without it
date: 2026-08-07
author: Waiel Al-Shujaa
status: LATTICE-STRUCTURED (causative controls reversed as locked) · P1 UNTESTABLE (2 roots) · P3 UNTESTABLE (0 roots)
prereg: prereg-h-new-2600-mutawaa-lattice.md
prereg_sha256: f058b852d5e2aadd8301070962759a8391f05f98749b49da78b2214fdf619b10
run: runs/h-new-2600/20260807T002903Z/
seed: 20260509
family: MORPH-2026-08-07-A
---

# H-NEW-2600 — The falsification control that H-NEW-2540 lacked

**Verdict: LATTICE-STRUCTURED.** Both causative reverse-controls reversed exactly as locked.
The novel muṭāwaʿa arm I→VIII passed. **P1, the strongest registered prediction, could not be
tested — only 2 eligible roots. P3 had none at all.** Reported with full prominence.

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

Across the exploratory lattice: **17 of 34 eligible ordered form pairs have positive T.** Among
the 30 pairs that are *neither* muṭāwaʿa nor causative, **15 of 30 are positive** — a coin flip.

Positive T is not pervasive. It is structured along exactly the relation classical morphology
names, and it inverts on exactly the relation classical morphology says should invert.

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
