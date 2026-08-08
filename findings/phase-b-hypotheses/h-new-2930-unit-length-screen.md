---
id: H-NEW-2930
title: "The unit-drift screen applied to the pausal-rhyme family — it TRIPS, and the 5.3× headline is inflated"
date: 2026-08-08
author: Waiel Al-Shujaa
status: "SCREEN TRIPPED — Δ tracks unit length at ρ = −0.65 across nine prose books; the corrected residual is 3.63×, not 5.3×"
screens_the: [H-NEW-2870, H-NEW-2880, H-NEW-2890, H-NEW-2910]
applies: findings/UNIT-DRIFT-DEFECT.md
---

# H-NEW-2930 — the screen turned on my own finding

**This screens the session's only surviving positive result, which is my own, and it trips.**

## 1. The screen

`findings/UNIT-DRIFT-DEFECT.md`: *when a density is divided by a unit count, and that unit's size
drifts across the ordering being tested, the measure is testing the drift.*

Δ is a rate over adjacent verse-end pairs. The comparison runs across nine prose books whose
**mean unit lengths span 49.2 to 91.1 words**. So the screen applies, and it was never run.

## 2. It trips

| book | mean unit length | Δ (P1) |
|:--|--:|--:|
| Dārimī | 49.2 | 0.02835 |
| Ibn Mājah | 58.5 | 0.04134 |
| Nasāʾī | 59.0 | 0.03257 |
| Mālik | 63.0 | 0.03768 |
| Abū Dāwūd | 63.1 | 0.02761 |
| Muslim | 64.6 | 0.03249 |
| Bukhārī | 73.2 | 0.03180 |
| Aḥmad | 73.6 | 0.02632 |
| Tirmidhī | 91.1 | 0.01623 |

**Spearman ρ(mean unit length, Δ) = −0.6500.** Shorter units, larger Δ. That is the unit-drift
signature.

## 3. The cost

The Qurʾān: 6,236 verses, 82,375 words, **mean unit length 13.21 words** — **3.7× shorter than
the shortest prose book in the baseline.** It sits far off the end of the very axis that predicts
the outcome.

Linear fit across the nine books: `Δ = 0.05679 − 0.000398 × unit_length`

| | |
|:--|--:|
| predicted Δ at 13.21 words | **0.05154** |
| observed Δ | **0.18690** |
| **residual** | **3.63×** |

**The honest claim is not "5.3× the prose mean." It is "3.63× what the unit-length trend predicts
for a text with verses this short."** Still large, still unexplained by unit length — but **a
third of what was reported.**

## 4. The caveat, which cuts both ways

The extrapolation reaches **0.86 full prose-ranges beyond the shortest book**, on a linear fit
through nine points. **The 3.63× is itself unreliable** — a linear model is not obviously correct
that far out, and the true residual could be larger or smaller.

What is established firmly: **the 5.3× headline is inflated by unit length and must not be quoted
as published.**

## 5. What this does not touch

- **H-NEW-2880's within-corpus null is unaffected.** It permutes the Qurʾān's own citation
  endings against itself, holding class count, class sizes and concentration exactly fixed
  (floor variance 0.00 across 160,000 draws). No cross-corpus unit length enters it. z = +15.03
  stands.
- The **P3 deflation** stands (a deliberately wrong tuple also clears, z = +8.99).
- The **3/12 D-P3 failures** on Ṣaḥīḥ Muslim stand.

The damage is specifically to the **cross-corpus magnitude claim**, which is the one I reported.

## 6. Provenance

A dedicated lane was dispatched to apply all three screens jointly, with written instructions to
screen this family *harder than it would screen someone else's work*. **It returned nothing — no
finding, no run directory, no scratch files.** The screen was then run directly.

That is worth recording: the check that cost this finding two-thirds of its headline existed only
because the failure was pursued after the delegated attempt produced nothing.
