# Length-channel triage — batch A, and a published statistic that is a LAPACK artifact

**Date:** 2026-08-11
**Status:** DIAGNOSTIC SCREEN. **No verdict authority.** Nothing here demotes anything; it ranks what
to read.
**Resolves:** 4 of the 20 candidates in [[AUDIT-LENGTH-CHANNEL-EXPOSURE]] §3.

---

## 1. The check

For each finding: Spearman ρ between its **grouping variable** and each of *verse count*, *word
count*, *mean verse length*. If the channel actually controlled is not the one with the largest |ρ|,
the control under-corrects and a pass may be inflated. **The gap is what matters** — a finding using
a channel at ρ = 0.40 when the dominant is 0.45 is barely exposed; one using ρ = 0.03 when the
dominant is 0.23 is not.

## 2. Batch A

| finding | grouping variable | channel used | dominant | gap | verdict |
|:--|:--|:--|:--|--:|:--|
| `h-new-91-rare-root-density` | per-surah rarity (`geom_mean_freq`) | token count (ρ 0.553) | **mean verse length (0.762)** | **+0.209** | **EXPOSED** |
| `h-new-85-oath-openers` | oath-opener indicator | verse count (ρ 0.029) | **mean verse length (0.227)** | **+0.198** | **EXPOSED** |
| `h-new-112-spectral-network` | Fiedler sign partition | verse count (0.275) | word count (0.310) | +0.035 | EXPOSED, barely |
| `h-new-46-1-chronology-disentangle` | muqaṭṭaʿāt indicator | — | — | — | **NOT-APPLICABLE** |

### 2.1 h-new-85 — the clearance holds only in the blind channel

Cell 4 returned NULL and the finding concludes **"Length is NOT a marker of oath-opening."** That
clearance is computed in the **verse-count** channel, where ρ = **−0.029** — effectively blind. In
mean verse length the association is **8× larger** (−0.227): **oath-openers have shorter verses.**

Consequence: cells 1, 2, 2b and 3 carry **no length control at all**, and they sit on a short-verse
confound that the finding believes it cleared.

### 2.2 h-new-91 — its own trigger would have fired harder

The prereg's rule is *"if |ρ_raw| > 0.5, report length-residualised rank only."* It fired at **0.554**
on token count. **On mean verse length it would have fired at 0.762.** The reconstruction is exact —
ρ = +0.553678 against the recorded T2 of +0.553678, to six decimals.

Aggravating: T4 (ρ = +0.668) and T5 (genre ANOVA) apply **no length control of any kind**, and both
variables are strongly mean-verse-length loaded.

### 2.3 h-new-46-1 — NOT-APPLICABLE, and why that matters

**Length is the outcome, not a control.** The regression is `verse_count ~ Medinan + muqaṭṭaʿāt`, and
the control applied is *chronology*, not length. Under-correction cannot inflate anything.

**But its control variable is itself channel-split, dramatically:** `I(Medinan)` against the three
channels is ρ = **−0.035** (verse count), +0.199 (word count), **+0.569** (mean verse length).
Medinan and Meccan surahs have **near-identical verse counts but far longer Medinan verses.**

So the headline *"chronology absorbs ~0% of the muqaṭṭaʿāt-length signal"* is true **specifically
because length was operationalised as verse count.** Its rules-tuple does lock that metric, so this
is honest operationalisation rather than hidden under-control — but **the "~0%" must not be read as
channel-general.**

## 3. The escalation — H-NEW-112's Fiedler partition is not reproducible

**λ₂ = 2.6552×10⁻¹⁶.** Verified directly from `csv/h-new-112.json`. That is numerically zero: the
graph's disconnected components make the second eigenvector **an arbitrary basis choice inside a
degenerate null space**.

Re-running the finding's own code with the same seed and data produced a **different partition** —
88/26 against the recorded 100/14 — and a different contingency table (`[[36,52],[21,5]]`,
χ² = 12.755, p = 3.55×10⁻⁴) against the published `[[45,55],[12,2]]`, χ² = 8.143, p = 4.32×10⁻³.

**Same qualitative pass, but the published statistic is a LAPACK artifact rather than a property of
the data.** The recorded vector had to be substituted to reconstruct the grouping variable at all,
and that substitution is flagged rather than hidden.

This is **not** a length-channel finding and it is more serious than one. It belongs to the family in
[[cross-finding-030-three-ways-a-control-fails]] only by analogy: a well-formed number, honestly
reported, that does not measure what it appears to.

## 4. Batch-wide pattern

**Mean verse length dominates 2 of 4 rows — and is never the channel anyone controlled on.** All four
scripts reach for verse count or token count; none touches mean verse length. Where it dominates
(85, 91) the gaps are **0.19–0.21**; where it does not (46.1, 112) the gaps are **≤ 0.08**.

**The exposure concentrates exactly where the outcome is a per-verse rate.** That is the mechanism, and
it is predictable in advance: a per-verse rate divided by a verse count that varies in length is
[[UNIT-DRIFT-DEFECT]]'s subject.

## 5. Limits

- **This is a screen.** An EXPOSED verdict says *read this*, not *this is wrong*.
- **16 of the 20 candidates remain unresolved.**
- One channel identification was corrected during the batch: `h-new-91` controls on a **token** count,
  not verse count, so the original screen misclassified it. The exposure is real regardless.
- My own first pass at this table was **wrong in sign** — a rank function that broke ties by original
  position, on a grouping that is 75% tied, injected the muṣḥaf-index signal (ρ = −0.84 with verse
  count) and inverted the muqaṭṭaʿāt correlation from +0.476 to −0.099. Caught by a sanity check
  against a known fact (muqaṭṭaʿāt surahs are 3.3× longer), not by inspection. **A deterministic
  tie-break is only neutral when ties are rare** — the same rule H-NEW-3030 recorded in August.

---

## 6. Batch B — and the largest exposure in the project

| finding | grouping variable | channel used | dominant | gap | verdict |
|:--|:--|:--|:--|--:|:--|
| **`h-new-127-6-jurjani-tier-bridge`** | Jurjānī asyndeton tier | verse count (**0.122**) | **mean verse length (0.795)** | **+0.674** | **EXPOSED — severe** |
| `h-new-150-liturgical-hub` | liturgical score | verse count (0.138) | verse count | — | **CLEAR** |
| `h-new-155-q1-sui-generis` | is-Q1 (1 vs 113) | verse count (0.129) | verse count | — | **CLEAR**, near-vacuous |
| `h-new-140-divine-name-pair-cohesion` | name-pair | none | — | — | **NOT-APPLICABLE** |

### 6.1 h-new-127-6 — both sides of the test point at the uncontrolled channel

Verified here independently (tier counts 17/32/65 reproduce exactly):

| | ρ with the Jurjānī tier |
|:--|--:|
| verse count — **the channel the null matched** | **−0.122** |
| word count | −0.461 |
| **mean verse length** | **−0.795** |

And the **observable** points the same way: ρ(gzip_z, mvl) = **+0.853**, ρ(gzip_z, n_verses) = +0.536.

> **The grouping variable is −0.80 on mean verse length. The observable is +0.85 on mean verse
> length. The null matched verse count, at 0.12.**

**The mechanism is mechanical, not statistical.** The null block for a surah of long verses is drawn
from the corpus-average pool, so it is *shorter in characters* than the surah it stands for — and
gzip ratio improves with input length. **Long-verse surahs therefore score "anomalously
compressible" by construction**, and the Jurjānī tier is largely a verse-length grader. The
verse-count matching does not even neutralise its own channel: residual ρ = +0.536.

**Blast radius.** The `h-new-127-*` family contains **24 finding documents**; the lane identifies
**127-3 through 127-11** as consuming the same locked `gzip_z`. This is the largest exposure the
screen has produced, by a factor of 3 over the next largest.

### 6.2 Two CLEAR verdicts, and why one of them is thin

`h-new-150` is genuinely clear — **no channel exceeds |ρ| = 0.14** against either variable, and the
outcome is uncorrelated with all three (max 0.036). Worth noting against the finding's own text: it
attributes a secondary FAIL to a length confound, and **the numbers do not support that mechanism.**
Whatever collapsed its residual ρ from 0.312 to 0.086 is not a monotone length effect. That error
runs *conservative*, so it is out of this screen's scope — but the stated mechanism is wrong.

`h-new-155` is CLEAR **only by the letter of the screen.** With one 1 and 113 zeros, the three ρ are
just Q1's rank on each channel and come out near-tied — **the screen cannot discriminate.** The lane
went further: Q1 has 29 words against an expected 87 (3.0×), and only **8 of 20,000** random 7-verse
windows are that short, so Q1 sits outside its null's effective support. The bias is liberal and
monotone — but small, buying ~+0.003 dispersion against an observed excess of +0.107. **Under-corrects,
does not threaten the finding.**

## 7. Running total

**8 of 20 candidates resolved:** 4 EXPOSED (127-6 severe, 91, 85, 112 barely), 2 CLEAR,
2 NOT-APPLICABLE. **12 remain.**

**The batch-wide pattern from §4 holds and strengthens:** mean verse length is the dominant channel in
4 of 8 resolved rows and **was never the channel anyone controlled on.** Every script reaches for
verse count or token count.

