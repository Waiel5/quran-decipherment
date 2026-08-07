---
finding_id: cross-finding-026-formal
status: FORMAL CODIFICATION (2026-05-29, Wave-M) — bounds cross-finding-025 by separating two mechanisms previously conflated
phase: C
date: 2026-05-29
verdict: The scale-of-aggregation law holds for CROSS-pericope marker-cohesion; it does NOT hold for WITHIN-pericope positional chiasmus
---

# Cross-finding-026 (FORMAL) — The cohesion/chiasmus bifurcation: bounding the scale-of-aggregation law



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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: anti-chiasmus is a property of Arabic prose, not of this corpus
>
> The finding **reproduces** — an independently written ring statistic returns mean
> permutation-z = −0.136 against the published −0.15. But all four matched corpora are
> anti-chiastic: poetry **−0.120**, this corpus **−0.136**, al-Bukhārī **−0.146**, and
> **al-Jāḥiẓ −0.209**. Adab prose is *more* anti-chiastic than this corpus, and roughly a
> third of windows are positive in every corpus (0.339–0.370).
>
> **Honest limit, for this law specifically — and it runs the other way.** This statistic is
> **boundary-sensitive**: arbitrary cuts *destroy* real unit boundaries and should make ring
> structure *harder* for a baseline. A baseline exceeding this corpus under that handicap is
> **strong** evidence, not weak. This is the most robust reversal in the sweep.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

> ## ⛔ CORRECTION NOTICE — 2026-08-07: this law does not discriminate
>
> **Nothing below is deleted and all five flips reproduce.** What did not survive is the reading of
> the flip as a property of *this* corpus.
>
> - Given five best-shot marker classes each, **pre-Islamic poetry flips 5/5 and al-Bukhārī flips
>   4/5** under the identical test. The poetry classes are ordinary content words (`عبلة` —
>   ʿAntara's beloved; `عبس`); the Bukhārī ones are jurisprudential vocabulary (`الماء`, `الإمام`).
> - The mechanism is **topical burstiness**, which every text has — and which this project already
>   identified as the substrate (H-NEW-2330, cited in `cf-026-formal`).
> - The statistic is **mathematically invariant under every redactional randomisation** (marker
>   labels, reading order, title assignment — verified 25/25), so it contributes exactly zero to any
>   conjunction of the pillar laws: L1∧L2∧L3 = L1∧L2 identically.
>
> **What still stands:** the methodological rule. Test at the scale where structure operates; a
> whole-surah NULL is not a terminal verdict. That rule is sound and remains project discipline.
> **What must stop:** reporting a pericope flip as evidence that the Qurʾān is structurally unusual.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md` §7. Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


## The problem this resolves

Cross-finding-025 (formal) established the **pericope-flip law**: thin-marker cohesion NULLs at whole-surah scale and PASSES at pericope scale. Its roster reached 6/6, with **ring-composition (Q002-F-07, §10.81)** logged as the "6th flip." Wave-M (2026-05-29) ran the two decisive corpus-wide tests of that 6th member — and they force a refinement. The word "pericope-scale structure" had silently fused **two different things**:

1. **Cross-pericope marker-cohesion** — do pericopes *in different surahs* that share a marker cohere lexically *with each other*? (a relation BETWEEN pericopes)
2. **Within-pericope positional chiasmus** — is the verse-order *inside a single pericope* a mirror (ABCB′A′)? (a relation INSIDE one pericope)

These are distinct mechanisms. The Wave-M evidence shows the law applies to (1) and **not** to (2).

## The evidence (Wave-M, all pre-registered, proper permutation nulls, seed 20260509)

### Mechanism 1 — cross-pericope marker-cohesion: HOLDS (and extends)

| Test | Marker class | Verdict |
|---|---|---|
| H-NEW-1380 / 1510 / 1520 / 1750 / 1760 (cross-finding-025) | narrative / liturgical / discourse / opener / orthographic-opener | 5× PASS |
| **H-NEW-2260** (Wave-M) | recurring-prophet narrative (Nūḥ, Mūsā) | 2/3 PASS — but **requires a conserved episode-lexicon** (Ibrāhīm NULLs) |
| **H-NEW-2280** (Wave-M) | canonical surah-seam (al-Biqāʿī munāsabah) | PASS-DIRECTED at k=5 (z=+2.89) |

Cross-pericope cohesion is robust across narrative, liturgical, discourse, opener, orthographic, recurring-prophet, and surah-seam marker classes. H-NEW-2260 sharpens the mechanism: cohesion is **content-anchored, not automatic** — sharing a marker is necessary-conditioning but not sufficient; a *conserved episode-lexicon* (ark/flood roots, burning-bush roots) is required. The lexical substrate of this whole mechanism is **H-NEW-2330 burstiness** (topical roots clump within their surah/pericope), which is why pericope-scale tests find cohesion that whole-surah tests dilute.

### Mechanism 2 — within-pericope positional chiasmus: DOES NOT GENERALIZE

| Test | Scale | Verdict |
|---|---|---|
| **H-NEW-2220** (Wave-M) | every pericope window {5,7,9,11,13} × every surah (6,541 windows) | **H1 NULL** — 0/6541 survive Bonferroni; corpus **anti-chiastic** in aggregate (mean perm-z = −0.15; only 33% of windows z>0; raw ring-rate 0.35× chance) |
| **H-NEW-2290** (Wave-M) | every adjacent verse-pair / triplet | **NULL-REVERSED** — pairs are significantly **PARALLEL not chiastic** (z=−3.28, parallel p=0.0013) |
| H-NEW-2030 (prior) | whole-surah ring | NULL (anti-chiastic) |

Positional mirror-symmetry is **rare and local**, not a corpus law, at every scale tested: verse-pair (parallel, not chiastic), pericope-window (anti-chiastic), and whole-surah (anti-chiastic). The famous Q 2:131-144 qibla-block ring (Q002-F-07) is **real but near-unique**: under H-NEW-2220's proper 10,000-perm null it reaches only z=+3.71 (sub-Bonferroni for a family of 6,541), and no other window matches it at family-significance.

## Codified principle

> **The scale-of-aggregation law (cross-finding-025) governs CROSS-pericope marker-cohesion — a lexical relation between pericopes that share a marker. It does NOT govern WITHIN-pericope positional chiasmus, which is anti-correlated with chance at every scale and exists only as isolated, near-unique instances (Q 2:131-144). "Ring-composition at pericope scale" must be split: cross-pericope cohesion is a law; within-pericope mirror-ordering is a rarity.**

### Consequence for the cross-finding-025 roster

The Q002-F-07 ring is **reclassified**: it is a valid single-instance *existence proof* (a real ring exists at Q 2:131-144), **not** a generalizing distributional flip like the other five. The pericope-flip law's law-strength roster is therefore the **5 cross-pericope marker-cohesion flips** (+ the H-NEW-2260 / H-NEW-2280 cross-pericope extensions). This is an honest **contraction** of an over-extended member, made the moment the corpus-wide test became available — the law is *stronger* for shedding a member that does not generalize.

## A self-correction worth recording

H-NEW-2220 also retired an instrument artefact: the earlier chiastic-audit's headline ring scores (z = +9.69 / +6.46 / +6.09 / +5.19, "4 Bonferroni survivors") were products of a **weak 50-shuffle parametric null**. Under a proper 10,000-perm permutation null, *none* survive, and even the strongest real ring (Q 2) drops to z=3.71. This vindicates **Sinai (2017, JQS 19)** at the strong-claim level while preserving the moderate tier (specific pericopes are unusually organised). The lesson generalises: **the null model, not the statistic, decides** — a weak null manufactures significance.

## The broader Wave-M meta-pattern (observed, not yet a law)

Across the 14-specialist wave, a clean separation recurs:
- **Real (CONFIRMED):** head/seal grammar (idhā-cascade 2250, dual-name content-seal 2300), distributional cohesion (qasam-clustering 2210, fāṣila-homogeneity 2240, refrain-spacing 2310), lexical architecture (hapax-Meccan-signature 2320, burstiness 2330), cross-pericope cohesion (2260, 2280).
- **Not real (NULL / retired):** mirror-symmetry below block scale (chiasmus 2220/2290), impressionistic iconicity (emphatic sound-symbolism 2340), region-keyed device density (iltifāt 2200), modern numerology (2230).
- **Classical accuracy:** al-Suyūṭī/al-Dānī *ḍawābiṭ* land at high accuracy (2270: 3 CONFIRMED), the exact mirror of modern numerology's 0% (2230) — the project's recurring "classical-real / modern-numerology-retired" signature.

Provisional meta-statement: **Quranic structure is cohesive and positional (heads, seals, clusters, cross-references) but not symmetric (mirrors/chiasmus) below the block scale, and not iconic at the surah scale.** Logged for future promotion if it recurs.

## Files

- This codification.
- Empirical anchors (all Wave-M, §10.82-§10.93 + ring/chiasmus): `h-new-2220-pericope-ring-sweep.md`, `h-new-2290-verse-pair-chiasmus.md`, `h-new-2260-prophet-cycle-pericope.md`, `h-new-2280-munasabah-seam.md`, `h-new-2330-lexical-burstiness.md`.
- Parent law: `cross-finding-025-formal-scale-of-aggregation-law.md`.

---

*Cross-finding-026 codified 2026-05-29 (Wave-M) by Waiel Al-Shujaa. Cohesion is a law; chiasmus is a rarity; the null model decides. Bismillāhi al-Raḥmāni al-Raḥīm.*
