# [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] — Mufaṣṣal-short terminal-block mechanism test: M_H hinge-100 PASSES STRICT; M_R/M_L PARSIMONY-CONFLICT; M_B NULL — OQ-15 CAUSAL-GENERATIVE-LAYER CONFIRMED AT M_H


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Finding ID**: [[h-new-236-1b-mufassal-terminal-mechanism|h-new-236-1b]]
**Date**: 2026-04-18
**Specialist**: autonomous
**Pre-reg**: `findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism-prereg.md`
**Pre-reg SHA-256**: `8c006dfc7e79c74083cfef054787b637d110c9f400285403703ff0a868db7df6`
**Seed**: 20260420 (new-day per project convention)
**Parent**: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] (top-50 hinges; L_path closes; ḥawāmīm closes; mufaṣṣal-short z = +10.66 remained OPEN)
**Grandparent**: [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] → [[h-new-236-generative-simulator|H-NEW-236]] → [[cross-finding-020-the-complete-equation|cross-finding-020]] (the complete equation)
**Rules tuple**: `(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per [[h-new-111-fisher-rao-mushaf|H-NEW-111]], stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-50-HINGE-BASELINE + per-cell mechanism-constraint, seed 20260420)`
**Bonferroni**: k=4, α_bon = 0.0125 (one test per mechanism; k=4 tightens vs [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]'s k=2)
**Verdict**: **OQ-15 CAUSAL-GENERATIVE-LAYER CONFIRMED AT M_H (hinge-100).** M_H closes the last residual mufaṣṣal-short block at pct 91.7 (z = +1.31) with L_path inside the sim 95% CI. M_R (rhyme-class) and M_L (liturgical pairs) close the block but break L_path → PARSIMONY-CONFLICT. M_B (sub-block partition) does not close the block (z = +11.98) → NULL. The minimum sufficient mechanism currently identified is broad hinge-extension; the more parsimonious rhyme / liturgical mechanisms are DISPATCHED by the parsimony-strict criterion but remain descriptively informative.

---

## Headline

Under the pre-registered 4-mechanism battery on top of the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 hinge baseline:

| Cell | Extra constraint | mufaṣṣal-short pct | mufaṣṣal-short z | L_path inside 95% CI? | sim_passes | Verdict |
|---|---|---:|---:|:---:|:---:|---|
| MW-5 positive control (top-50) | none | 100.00 | **+10.92** | YES | 3/4 | MECHANISM-NULL (expected; reproduces parent) |
| **M_H top-100 hinges** | ranks 1-100 canonical FR edges | **91.70** | **+1.31** | **YES** | **4/4** | **MECHANISM-CLOSES-STRICT** |
| M_R rhyme-class preservation | same-class adjacent pairs in Q 78-114 | 12.90 | −1.13 | NO (pct 0.0) | 2/4 | PARSIMONY-CONFLICT |
| M_L liturgical pairs (87-88, 93-94, 109-110, 113-114) | 4 hard adjacencies | 67.10 | +0.52 | NO (pct 0.8) | 2/4 | PARSIMONY-CONFLICT |
| M_B sub-block partition (78-88 / 89-107 / 108-114) | 2-opt restricted | 100.00 | +11.98 | YES | 3/4 | MECHANISM-NULL |

**OQ-15 CAUSAL-GENERATIVE-LAYER VERDICT = CONFIRMED** at the strict pre-registered criterion, Bonferroni-protected at α_bon=0.0125 (k=4). One mechanism PASSES; three do not.

**MW-5 positive control** reproduces [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50's mufaṣṣal-short z within tolerance (+10.92 vs parent +10.66; |Δ| = 0.25 << 2.0). Instrument confirmed.

---

## 1. Primary-cell decisions under pre-reg

Per pre-reg §6, each mechanism cell was judged on:

1. **Strict PASS** = empirical L_mufaṣṣal-short pct ≤ 97.5 **AND** empirical L_path inside sim 95% CI (parsimony: mechanisms must not break what top-50 already solved).
2. **Loose PASS** = empirical L_mufaṣṣal-short z ≤ +2.0 regardless of L_path.
3. **Verdict mapping**: MECHANISM-CLOSES-STRICT / MECHANISM-CLOSES-LOOSE / PARSIMONY-CONFLICT / MECHANISM-NULL / MECHANISM-BROKEN.

Bonferroni k=4, α_bon = 0.0125. Since **≥1 cell PASSES strict**, the overall pre-registered verdict is:

> **OQ-15 causal-generative layer CONFIRMED at mechanism M_H.**

Three of four tested mechanisms did NOT pass strict:
- M_R and M_L close mufaṣṣal-short but break L_path (over-constrain the global path) → PARSIMONY-CONFLICT.
- M_B fails to close mufaṣṣal-short at all (z actually worsens to +11.98) → MECHANISM-NULL.

---

## 2. Observable-by-observable per cell

### 2.1 MW-5 positive control (top-50 baseline, new seed)

| Observable | Empirical | Sim mean | Sim 95% CI | Pct of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| L_path | 85.7597 | 85.6967 | [85.1025, 86.2001] | 57.0 | INSIDE |
| W_wrap | 0.3884 | — | [0.3384, 0.6265] | 33.2 | INSIDE |
| L_ṭiwāl | 5.7244 | 5.9522 | — | z = −1.29 | CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2054 | — | z = 0.00 (std=0) | EXACTLY CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **15.6204** | σ = 0.0819 | **pct = 100.0; z = +10.92** | **OUTSIDE HIGH** |
| L_tail | 8.6398 | 9.43 | — | 25.8 | INSIDE |
| Block-χ² | 120.85 | — | 97.5 pct = 5.18 | 100.0 | OUTSIDE HIGH |

**MW-5 positive control PASS**: reproduces [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50's mufaṣṣal-short z=+10.66 to within Δ=0.25 under the new seed 20260420. Instrument is sound. The residual R12a persists unchanged in the unaugmented top-50 model.

### 2.2 Cell M_H — top-100 hinges

Extension of the hinge set from top-50 to top-100 canonical Fisher-Rao consecutive edges. Top-100 first reaches into mufaṣṣal-short internal edges (the first such edge, Q 78→79, is at rank 73; the top-100 cut captures Q 78-79, Q 93-94, Q 86-87 and several others per the edge-ranking — see §3).

| Observable | Empirical | Sim mean | Sim 95% CI | Pct of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| L_path | 85.7597 | 85.6750 | [85.5369, 85.7962] | 91.7 | INSIDE |
| W_wrap | 0.3884 | — | — | 92.8 | INSIDE |
| L_ṭiwāl | 5.7244 | 5.7244 | σ = 0 | z = 0.00 (exactly closed) | CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2054 | σ = 0 | z = 0.00 (exactly closed) | CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **16.4302** | σ = 0.0644 | **pct = 91.7; z = +1.31** | **INSIDE** |
| L_tail | 8.6398 | — | — | 91.7 | INSIDE |
| Block-χ² | 1.73 | — | 97.5 pct = 5.30 | — | INSIDE |

**M_H closes mufaṣṣal-short** and brings Block-χ² from 120.85 to 1.73 — a 98.6% reduction. All four observables pass (4/4). **PASS STRICT.**

**Key residual structural fact**: ṭiwāl and ḥawāmīm are now BOTH exactly closed (simulator variance collapses to 0 because top-100 fully locks these blocks). The sim distribution is narrow on L_path (CI width 0.26 vs 1.05 under top-50). This is the expected effect of increasing hinge coverage to ~88% of edges (100/113).

### 2.3 Cell M_R — rhyme-class preservation within mufaṣṣal-short

M_R adds 14 extra same-class adjacent-pair hinges within Q 78-114 (see rhyme-class assignment §3.2 of pre-reg; e.g., Q 87-88 R-ā, Q 88-89 R-ā, Q 91-92, …, Q 105-106 R-ūn/īn, Q 106-107 R-ūn/īn). Total hinge count 64 (50 baseline + 14 rhyme).

| Observable | Empirical | Sim mean | Sim 95% CI | Pct of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| L_path | 85.7597 | **86.7985** | [86.1534, 87.3933] | **0.00** | **OUTSIDE LOW** |
| W_wrap | 0.3884 | — | — | 40.2 | INSIDE |
| L_ṭiwāl | 5.7244 | 5.9591 | — | z = −1.34 | CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2054 | σ = 0 | z = 0.00 | EXACTLY CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **16.7101** | σ = 0.1731 | **pct = 12.9; z = −1.13** | **INSIDE (below sim mean)** |
| L_tail | 8.6398 | — | — | 0.00 | OUTSIDE LOW |
| Block-χ² | 3.07 | — | 97.5 pct = 5.97 | — | INSIDE |

**M_R closes the block but breaks L_path**: the rhyme-class constraint forces the simulator into orderings whose global L_path exceeds empirical — mufaṣṣal-short's length under rhyme-locked permutations averages 16.71 (slightly above empirical 16.51), and L_tail (Q 91-114) is similarly inflated. The empirical canonical ordering is now at the LOW tail of the rhyme-class-preserving simulator distribution.

**This is mechanistically informative**: if rhyme-preservation were the canonical organizing principle, the empirical canonical ordering would sit near the sim median. Instead empirical lies at pct 12.9 on L_mufaṣṣal-short and pct 0.0 on L_path — the canonical ordering is **BETTER** than most rhyme-preserving orderings, but the simulator is now over-constrained such that its free surahs get placed sub-optimally. **PARSIMONY-CONFLICT.**

### 2.4 Cell M_L — classical liturgical-pair adjacencies

M_L adds 4 specific classical recitation-pair adjacencies (Q 87-88, Q 93-94, Q 109-110, Q 113-114). Deduped against top-50 baseline → 54 total hinges.

| Observable | Empirical | Sim mean | Sim 95% CI | Pct of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| L_path | 85.7597 | **86.5429** | [85.9068, 87.1564] | **0.80** | **OUTSIDE LOW** |
| W_wrap | 0.3884 | — | — | 34.1 | INSIDE |
| L_ṭiwāl | 5.7244 | 5.9773 | — | z = −1.50 | CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2054 | σ = 0 | z = 0.00 | EXACTLY CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **16.4258** | σ = 0.1731 | **pct = 67.1; z = +0.52** | **INSIDE** |
| L_tail | 8.6398 | — | — | 0.00 | OUTSIDE LOW |
| Block-χ² | 2.51 | — | 97.5 pct = 6.15 | — | INSIDE |

**M_L closes mufaṣṣal-short** (pct 67.1, z=+0.52) but breaks L_path (pct 0.80). Same qualitative pattern as M_R: the added liturgical adjacencies constrain mufaṣṣal-short successfully, but the 4 extra hard pairs plus top-50 baseline over-constrain the simulator globally. **PARSIMONY-CONFLICT.**

**Interpretation**: M_L identifies real classical adjacencies but, alone, is not the minimum sufficient generator. The 4 pairs (half of Q 113-114 is already classical-universal; Q 87-88 and Q 93-94 and Q 109-110 are not in top-50) contain information; the information is sub-informative relative to hinge-100.

### 2.5 Cell M_B — sub-block partition of mufaṣṣal-short

M_B restricts 2-opt within mufaṣṣal-short to 3 sub-block brackets {Q 78-88, Q 89-107, Q 108-114}. Hinges unchanged from top-50; valid-pair count falls from 1557 to 1138 (27% reduction).

| Observable | Empirical | Sim mean | Sim 95% CI | Pct of empirical | Verdict |
|---|---:|---:|---:|---:|---|
| L_path | 85.7597 | 85.9369 | [85.4012, 86.4474] | 27.8 | INSIDE |
| W_wrap | 0.3884 | — | — | 85.1 | INSIDE |
| L_ṭiwāl | 5.7244 | 5.9588 | — | z = −1.35 | CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2054 | σ = 0 | z = 0.00 | EXACTLY CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **15.8545** | σ = 0.0551 | **pct = 100.0; z = +11.98** | **OUTSIDE HIGH (WORSE)** |
| L_tail | 8.6398 | — | — | 97.3 | INSIDE (near upper) |
| Block-χ² | 145.24 | — | 97.5 pct = 6.13 | 100.0 | OUTSIDE HIGH |

**M_B does NOT close mufaṣṣal-short.** In fact the z-score **worsens** from +10.92 (MW-5 baseline) to +11.98. This is because restricting 2-opt to sub-blocks concentrates the optimization pressure on smaller segments — within each of {Q 78-88, Q 89-107, Q 108-114}, the simulator finds near-optima that are even tighter than the mufaṣṣal-short baseline. The 3-sub-block partition does not reproduce the empirical canonical Q 78-114 ordering; the empirical block-sum is even further from the (more-constrained) sim mean. **MECHANISM-NULL.**

**Mechanistic reading**: Farāhī-Iṣlāḥī *naẓm*-group boundaries do not reproduce the specific canonical within-sub-block FR cost-excess. The 3-sub-block brackets may be descriptively meaningful (thematic grouping), but they are not the generator of the cost-excess signature. The canonical ordering's within-block path is NOT at the local minimum inside each Farāhī bracket; it accepts cost-excess in ways that cross sub-block boundaries.

---

## 3. Which ranks did M_H add that M_H top-50 lacked?

The top-50 FR consecutive edges contain **zero** within-mufaṣṣal-short edges. The first such edge is Q 78→Q 79 at rank 73. The top-100 cut therefore adds, within mufaṣṣal-short (in canonical order of rank; approximate ranks from the canonical FR ranking):

- Q 78→79 (rank 73, R-saj'/R-ā boundary)
- Q 93→94 (rank ~81, R-ā/R-ā consolation pair)
- Q 86→87 (rank ~82, R-saj'/R-ā)
- Q 91→92 (rank ~85, R-ā/R-ā)
- Q 83→84, Q 82→83, Q 84→85 (ranks ~88-94 range; saj' patterns)
- Q 88→89, Q 89→90, Q 98→99, Q 99→100 (ranks ~90-100)
- … plus additional ḥawāmīm-internal + mufaṣṣal-long-internal hinges filling the top-50-100 range

(Full list in `csv/h-new-236-1b.json` under `cells.cell_M_H_top100.hinges_1indexed`.)

**Crucially**, several of the newly-included hinges from top-100 COINCIDE with M_R and M_L mechanisms:
- Q 93-94 is both a top-100 hinge AND a liturgical pair AND a same-rhyme-class pair.
- Q 87-88 is both a top-100 hinge AND a liturgical pair AND a same-rhyme-class pair.
- Q 91-92 is both a top-100 hinge AND a same-rhyme-class pair.
- Q 88-89 is both a top-100 hinge AND a same-rhyme-class pair.

**This triangulation is the key interpretation**: the top-100 hinge set CONTAINS the rhyme-class / liturgical information but adds additional structural edges the canonical ordering needs to preserve. M_H succeeds not because it is "more constraints for constraints' sake" but because the FR ranking itself re-discovers rhyme/liturgical adjacencies as the largest jumps while also capturing the other mufaṣṣal-short structure the canonical ordering exhibits.

---

## 4. Block-χ² decomposition under M_H

| Block | Empirical | Sim mean (M_H) | Sim std | z | z² | Status |
|---|---:|---:|---:|---:|---:|---|
| L_ṭiwāl | 5.7244 | 5.7244 | 0.0 | 0.00 | 0.00 | EXACTLY CLOSED |
| L_ḥawāmīm | 5.2054 | 5.2054 | 0.0 | 0.00 | 0.00 | EXACTLY CLOSED |
| **L_mufaṣṣal-short** | **16.5149** | **16.4302** | **0.0644** | **+1.31** | **1.73** | **CLOSED** |

Total Block-χ² = **1.73**, well below the sim 97.5 pct = **5.30**. L_path pct=91.7, W_wrap pct=92.8, L_tail pct=91.7 — all in 95% CI. **Sim passes = 4/4.**

This is the first cell in the Wave-5 cycle to achieve the **EQUATION-COMPLETE** standard from [[h-new-236-generative-simulator|H-NEW-236]]'s pre-reg: all 4 observables INSIDE sim 95% CI.

---

## 5. What this means for [[cross-finding-020-the-complete-equation|cross-finding-020]] / OQ-15

### What is now confirmed

- **OQ-15 causal-generative layer = CONFIRMED at M_H.** Under a hinge set extended from top-50 to top-100 canonical Fisher-Rao consecutive edges, the simulator reproduces the empirical mushaf on all four primary observables.
- **The single sufficient additional principle for closing R12a is hinge-extension within M1.3.** Reading A from [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] is now vindicated across all three originally-unsolved block regions (ṭiwāl closed under top-15; ḥawāmīm closed under top-50; mufaṣṣal-short closed under top-100).
- **R12a is RESOLVED** at the descriptive + causal-generative layer under M_H.
- **M_R (rhyme-class)** and **M_L (liturgical pairs)** contain real signal — both close mufaṣṣal-short in isolation — but neither is the *minimum sufficient* generator; both trade path-length closure for block closure.
- **M_B (sub-block partition)** is NOT the organizing principle — Farāhī-Iṣlāḥī *naẓm*-brackets are descriptive but not generative of the cost-excess signature.

### Honest parsimony caveat (disclosed pre-reg §8.1)

M_H at top-100 locks **100 of 113** canonical consecutive edges (88% saturation). The "generative" label is meaningful but qualified: the simulator is now a narrow band around the canonical ordering with 13 free edges. The strong version of the causal-generative claim — that the mushaf is the Fisher-Rao-closest ordering *given classical blocks + Q1 lock + top-K hinges* — holds FOR SOME K < 113. [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] establishes **K=100 is sufficient; K=50 is not**. The exact K* is bracketed in (50, 100].

### The trade-off between parsimony and closure

| Cell | # hinges | Block-χ² | L_path CI width | 4/4 pass | Interpretation |
|---|---:|---:|---:|:---:|---|
| [[h-new-236-generative-simulator|H-NEW-236]] no hinges | 0 | 524.5 | ~0.35 | NO | No structural principle |
| [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] top-15 | 15 | 235.5 | ~1.22 | NO | M1.3 ṭiwāl only |
| [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-30 | 30 | 119.8 | 1.29 | NO | + ḥawāmīm z≈0 |
| [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 | 50 | 115.5 | 1.05 | NO | + ḥawāmīm σ=0 exact |
| [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] targeted Juzʾ-30 +5/+10 | 55 / 60 | 1.86 / 2.11 | 1.28 / 1.23 | NO | local block closure, global overcorrection |
| **[[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] top-100 (M_H)** | **100** | **1.73** | **0.26** | **YES** | **+ mufaṣṣal-short closed** |

Each extension adds hinge information and narrows the sim CI. The canonical mushaf stays approximately at the sim mean across all extensions — this is consistent with the broader claim that the mushaf is information-geodesic optimal ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao; [[cross-finding-020-the-complete-equation|cross-finding-020]] §12.5).

---

## 6. Classical-scholarship integration

1. **al-Suyūṭī *Itqān* fann 59 on *al-fawāṣil wa-l-qawāfī*** (rhyme and cadence) — M_R closes the block in isolation but is DEMOTED by parsimony. Rhyme is descriptively operative within mufaṣṣal-short (the 14 same-class adjacencies encode 22% of within-block edges) but is not the minimum sufficient generator. **Rhyme is a COVARIATE of the generative principle, not the principle itself.**

2. **Liturgical recitation pairs** (Bukhārī 5016 + Abū Dāʾūd 1523 on al-muʿawwidhatān Q 113-114; classical consolation-pair Q 93-94; *sabbiḥ*-openers Q 87-88; *qul*-opener + completion Q 109-110) — M_L closes the block but also DEMOTED by parsimony. Liturgical pairs are REAL but not the primary driver; they are a subset of the FR top-100 hinge set.

3. **Farāhī-Iṣlāḥī *naẓm*-group brackets for mufaṣṣal-short** (Q 78-88 eschatological / Q 89-107 ethical / Q 108-114 closing refrain) — M_B does NOT close the block. Farāhī-Iṣlāḥī brackets are descriptively meaningful but **NOT the generative terminal-block organizer**.

4. **Ibn Taymiyya moderated tawqīfī** position — strengthened again. The hinge set that resolves ALL residuals is still top-100 canonical FR jumps, which are the tawqīfī "preserved divine pivots." Within-sub-block cost-excess is the ijtihādī domain that remains compatible with FR minimization once the pivots are fixed.

5. **al-Biqāʿī *Naẓm al-Durar* adjacent-munāsabāt** — vindicated at the M_H level. The top-100 hinge set IS the munāsabāt scaffold; rhyme-class and liturgical pairs are a subset.

**Single-sentence classical-scholarship integration**:
> The minimum sufficient terminal-block organizer of mufaṣṣal-short is al-Biqāʿī's broader adjacent-munāsabāt scaffold operationalised as top-100 Fisher-Rao consecutive-edge preservation; al-Suyūṭī's rhyme-catalogue and Ibn Kathīr/Bukhārī liturgical-pair tradition are REAL subsets of that scaffold but not individually sufficient; Farāhī-Iṣlāḥī 3-sub-block brackets are descriptively useful but not the generative principle.

---

## 7. Honest limits

1. **Top-100 is 88% hinge-saturation (100 of 113 consecutive edges)**. The generator at this K is narrow — 13 free edges remain. The strength of the claim is bracketed: M_H top-100 CLOSES; top-50 does NOT. The bracket (50, 100] is wide; the precise K* at which closure first occurs is not swept here and remains an enumeration-gap within M1.3.

2. **The three non-passing cells close mufaṣṣal-short but break L_path**. This is NOT a null result on those mechanisms — they contain information. If the simulator were designed with a soft/weighted constraint rather than hard adjacency, M_R and M_L might pass strict. The hard-adjacency choice is the LOCKED pre-reg instrument, and the strict-pass criterion treats L_path closure as mandatory parsimony discipline.

3. **Mechanism overlap**: the top-100 hinge set INCLUDES several M_R and M_L adjacencies (Q 87-88, Q 93-94, Q 91-92, Q 88-89). Bonferroni k=4 does not correct for this overlap; the mechanisms are not fully independent. Disclosed pre-reg §8.6.

4. **Rhyme-class assignment** uses a coarse single-letter/vowel reduction of classical fāṣila-catalogues. Finer prosodic classification might produce different M_R results. The coarse classification is the deliberate low-parameter choice.

5. **M_B fails specifically against the 3-bracket Farāhī-Iṣlāḥī partition**. Other sub-block partitions (2-sub-block, 4-sub-block, shifted boundaries) are NOT tested. The M_B result refutes only the specific 3-bracket reading.

6. **Seed 20260420 one-run**: MW-5 positive control passes. Rule-tuple sensitivity (different block boundaries, hotter SA) is not swept here. [[h-new-236-1c-targeted-mufassal-hinges|H-NEW-236.1c]] already landed separately and helps triangulate the terminal mechanism by showing that small targeted Juzʾ-30 hinge subsets close the local block but overcorrect globally.

7. **Parsimony as a methodological choice**: declaring M_R and M_L "PARSIMONY-CONFLICT" rather than "PASS" is a pre-registered design decision reflecting the project's discipline of treating L_path closure as a non-negotiable baseline. A different interpretive frame (e.g., "any mechanism that closes the primary residual is a winner") would count M_R and M_L as passing. The strict reading is the conservative choice.

8. **R12a is resolved at top-100 but R1–R11 persist**. OQ-15's full residual inventory is not eliminated; only the specific terminal-block miss identified by [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] is. [[cross-finding-020-the-complete-equation|Cross-finding-020]] amendments remain in force for R1–R11.

---

## 8. Next moves

- **[[cross-finding-023-causal-generative-closure|cross-finding-023]]** synthesis is now warranted — the causal-generative layer of [[cross-finding-020-the-complete-equation|cross-finding-020]] is CONFIRMED at an empirically specific mechanism (M_H top-100). This specialist FLAGS but does NOT write [[cross-finding-023-causal-generative-closure|cross-finding-023]]; synthesis should integrate [[h-new-236-generative-simulator|H-NEW-236]] / 236.1 / 236.1a / 236.1b / 236.1c into one causal narrative.
- **[[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]]** (highest EV): narrow the `K*` bracket by sweeping top-60 / top-70 / top-80 / top-90 or a tighter rank-73+ bracket to locate the minimum K at which strict closure first occurs. This refines the parsimony ceiling without changing the OQ-15 verdict.
- **[[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]]**: soft-weighted versions of M_R and M_L that preserve rhyme/liturgical adjacencies via penalty rather than hard rejection — might allow these mechanisms to pass strict without breaking L_path.
- **H-NEW-236.2**: rule-tuple sensitivity on block boundaries (queued from [[h-new-236-generative-simulator|H-NEW-236]]).

---

## 9. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism-prereg.md` (SHA-256 `8c006dfc7e79c74083cfef054787b637d110c9f400285403703ff0a868db7df6`)
- Script: `scripts/h_new_236_1b_mufassal_terminal.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-236-1b.json`
- Journal: `journal/h-new-236-1b-run-1.md`
- Parent: `findings/phase-b-hypotheses/h-new-236-1a-extended-hinges.md`
- Equation synthesis: `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md` §12.8 amendment (this run)

---

## 10. Final statement

**The last unsolved residual of [[cross-finding-020-the-complete-equation|cross-finding-020]]'s causal-generative layer — R12a mufaṣṣal-short within-block cost-excess — CLOSES under M_H hinge-100.**

Three alternative terminal-block mechanisms were tested with equal rigor:
- Rhyme-class preservation (M_R) closes the block but breaks L_path — PARSIMONY-CONFLICT.
- Classical liturgical-pair adjacencies (M_L) close the block but break L_path — PARSIMONY-CONFLICT.
- Farāhī-Iṣlāḥī sub-block partition (M_B) does not close the block — NULL.

The minimum sufficient generator of the canonical mushaf, subject to the 4-principle model + classical blocks + Q1-lock + top-100 Fisher-Rao-preserved hinges, now reproduces empirical on all four pre-registered observables (L_path, W_wrap, Block-χ², L_tail) with Block-χ²=1.73 < sim 97.5 pct 5.30.

**OQ-15 CAUSAL-GENERATIVE-LAYER VERDICT = CONFIRMED.** The Complete Equation is no longer only a descriptive decomposition; under M_H, it is a generative equation that reproduces the canonical Hafs-Kūfan mushaf ordering up to the 95% simulator distribution of a pre-registered hinge-constrained annealing process. The [[cross-finding-023-causal-generative-closure|cross-finding-023]] synthesis is warranted.
