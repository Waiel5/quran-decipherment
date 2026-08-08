---
id: H-NEW-2940
title: "The inverse re-cut — merging this corpus's own verses to prose unit lengths closes none of the gap"
date: 2026-08-08
author: Waiel Al-Shujaa
status: "MEASURED — f = −0.0067 at 65.1 words. The residual is real and LARGER than H-NEW-2930's extrapolation suggested: 6.08×, in range, not 3.63× by extrapolation."
prereg: findings/phase-b-hypotheses/prereg-h-new-2940-inverse-recut.md
prereg_sha256: 27a2d9cdf54fa2c9d73450fc831823abbaed21641204f6b52b2de2e432d51257
run: runs/h-new-2940/20260808T115534Z
supersedes: findings/phase-b-hypotheses/h-new-2930-unit-length-screen.md §3
closes: findings/phase-b-hypotheses/OPEN-H-NEW-2940-inverse-recut.md
---

# H-NEW-2940 — the extrapolation replaced by a measurement

H-NEW-2930 corrected the pausal cross-corpus headline from 5.3× to 3.63× by **extrapolating a
nine-point linear fit 0.86 prose-ranges below the shortest book in its baseline**, and said in
its own §4 that the 3.63× was therefore unreliable in both directions.

**It was unreliable in the direction that favours the null.** Measured rather than extrapolated,
the residual is **6.08×**.

## 1. The reproduction gate, which ran first

The instrument is sections 0–6 of `scripts/h-new-2870.py` executed verbatim — the phonemiser,
the pausal conventions, both rime extractors, the corpus load, and its GATE A and GATE B, all
re-run. Nothing was reimplemented.

| | |
|:--|--:|
| Δ native (rime R2, tuple P1) | **0.18686703691604045** |
| published value | 0.18686703691604045 |
| absolute difference | **0.0** |

Bit-identical. GATE A passed, GATE B passed 6/6.

*On the number itself:* H-NEW-2930 and the brief both write this as **0.18690**. That is
0.186867 at four decimals — the same number, not a discrepancy.

## 2. The measurement

Merge this corpus's own adjacent verses into longer units, never spanning a surah, and measure Δ
at the merged length. No baseline text is required. A unit's label is the label of its **joined**
text; the run gates that against the label of its last constituent verse over all **18,516** unit
labels — **0 mismatches**, confirming merging is exactly a thinning of the ending sequence.

**Primary arm — greedy accumulation to 65 words** (threshold T = 59, chosen by a Δ-free rule;
1,189 units, 1,075 adjacent pairs, achieved mean length **65.121 words**):

| | native | merged at 65.121 w |
|:--|--:|--:|
| A(C) | 0.34842 | 0.27163 |
| A(P1) | 0.53528 | 0.45953 |
| **Δ** | **0.18687** | **0.18791** |

Both agreement rates fall as the compared endings move apart. **The gap between them does not.**

## 3. The one number

    f = (Δ_native − Δ_merged) / (Δ_native − Δ_prose)
      = (0.18687 − 0.18791) / (0.18687 − 0.03049)

**f = −0.0067.** Merging this corpus to mid-prose unit length closes **none** of the gap — it
is 0.7% the wrong way, i.e. Δ is marginally *larger* at 65 words than at 12.4.

Every arm agrees. The largest share of the gap closed anywhere, across four target lengths and
both merge rules, is **12.3%**:

| target | rule | achieved length | Δ | f | residual |
|--:|:--|--:|--:|--:|--:|
| 50 | greedy | 50.475 | 0.17465 | +0.078 | 4.76× |
| 50 | fixed g=4 | 48.423 | 0.17104 | +0.101 | 4.56× |
| **65** | **greedy** | **65.121** | **0.18791** | **−0.007** | **6.08×** |
| 65 | fixed g=5 | 60.116 | 0.20102 | −0.091 | 6.11× |
| 75 | greedy | 75.320 | 0.18818 | −0.008 | 7.01× |
| 75 | fixed g=6 | 71.363 | 0.18641 | +0.003 | 6.56× |
| 91 | greedy | 90.773 | 0.16779 | +0.122 | 8.11× |
| 91 | fixed g=8 | 93.967 | 0.16761 | +0.123 | 8.63× |

Non-gating diagnostics concur: phase-averaging the fixed-group grid over all five offsets gives
Δ = 0.18431 (sd 0.00917); a geometric random segmentation at the same mean length gives
Δ = 0.18207 / 0.18266 across two seeds; and native Δ restricted to only the surahs that survive
each merge stays at 0.1856–0.1875, so the result is not an artefact of short surahs dropping out.

## 4. The successor to 3.63×

At 65.121 words the comparison sits **inside** the 49.2–91.1 word prose range. Nothing is
extrapolated:

| | |
|:--|--:|
| nine-book fit predicts at 65.121 w | 0.03090 |
| measured, merged | **0.18791** |
| **in-range residual** | **6.08×** |

H-NEW-2930's extrapolation understated the residual by **40%**. The linear model was not
merely uncertain that far out — out at 12.4 words it predicted 0.0519, well above what the trend
actually delivers where the trend can be checked.

## 5. Why the two re-cut controls point in opposite directions, and what that settles

H-NEW-2880's D3 control re-cuts this corpus at its **native** length but with boundaries in
arbitrary places (verse lengths shuffled; only 12.8% of pseudo-boundaries land on a real verse
end). It gives Δ = **0.02840** — the prose value.

This run holds the boundaries fixed and makes the units **5× longer**. It gives Δ = **0.18791** —
the native value.

|  | native length | 5× length |
|:--|--:|--:|
| **real boundaries** | 0.18687 | **0.18791** |
| **arbitrary boundaries** | 0.02840 | — |

Δ is indifferent to how long the unit is and collapses entirely when the boundary moves.
**The effect is located in boundary placement, not unit length.** That is the question
`findings/UNIT-DRIFT-DEFECT.md` exists to ask, and here the screen does not trip.

## 6. Two defects in H-NEW-2930's baseline, both found and declared before the run

**(a) The Qurʾān's unit length was measured on the wrong file.** The nine prose books' lengths
(49.16–91.12) were measured by `arabic_words()` in `scripts/h-new-2890.py`. On that same
tokeniser this corpus is **77,429 words / 6,236 verses = 12.4165** — the figure `h-new-2890.py`
itself prints, as `12.4`. H-NEW-2930 instead used 13.21 from the Tanzil `.txt` (82,260 words), a
different file with different word splitting, and plugged it into a fit calibrated on
`arabic_words` lengths. Consequence: predicted Δ moves 0.05154 → 0.05187, residual 3.63× → 3.60×.
**Immaterial to its conclusion, and reported rather than quietly fixed.**

**(b) Each of its nine per-book Δ values is a maximum over six cells.** Reconstructed from the
frozen H-NEW-2910 result, every entry in 2930's table is the largest of that book's
{S5, S3, S0} stripping × {all, readable} cells — and H-NEW-2910 designates no primary
segmentation. This **inflates the prose baseline**, which makes the residual **conservative**.
Recomputing against internally consistent alternatives moves nothing that matters: f = −0.0066
against all three of the S5, S3 and S0 readable means, residual 6.30× / 6.25× / 6.39×.

The refit gate confirms the reconstruction: refitting 2930's own table reproduces its published
slope −0.000398 and intercept 0.05679.

## 7. Verdict against the rule locked before the run

The pre-registered grid: f ≥ 0.75 → the magnitude claim is finished and withdrawn; f ≤ 0.25 →
the residual is real and larger than the extrapolation suggested; between → partial.

**f = −0.0067. The residual is real, and larger: 6.08× in range, against 3.63× by
extrapolation.**

The honest statement of the cross-corpus magnitude is no longer "~3.6× by extrapolation, with
the extrapolation acknowledged as unreliable". It is **6.08× at matched unit length, measured**.

## 8. What was never at stake

**H-NEW-2880's within-corpus null is untouched**, as its own §5 and the OPEN file both said in
advance. It permutes this corpus's citation endings against itself with class count, class sizes
and concentration held exactly fixed — floor variance 0.00 across 160,000 draws, z = **+15.03**,
0/10,000. No cross-corpus unit length enters it, and none entered it here.

## 9. Provenance

This question sat unrun after three dispatched lanes failed on it — two produced no artifacts at
all, one died mid-response. It was deliberately not attempted by hand, because a hand-rolled
rime extractor would produce a Δ that could not be compared to the published one. Executing the
pinned parent's sections 0–6 verbatim is what makes the 0.0 reproduction difference in §1
meaningful, and it is what let the two baseline defects in §6 be found at all.

Pre-registration SHA-256 `27a2d9cd…51257`, embedded in the runner and verified at runtime;
11 frozen inputs verified including the parent runner; immutable run directory
`runs/h-new-2940/20260808T115534Z`; per-arm checkpoints written outside it. There is no p-value
in this test and none was invented — it is a magnitude comparison, decided on f.
