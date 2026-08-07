---
id: cross-finding-025
title: Marker-thickness vs Fisher-Rao-cohesion threshold (preliminary synthesis)
date_locked: 2026-05-09
status: PRELIMINARY-SYNTHESIS (5 supporting findings; replication / formalization queued)
sources:
  - cross-finding-008
  - H-NEW-1080
  - H-NEW-1190
  - H-NEW-1200
  - H-NEW-1301
  - H-NEW-1310
  - H-NEW-1320
  - H-NEW-1330
---

# Cross-finding-025 — Marker-thickness vs Fisher-Rao-cohesion threshold



> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
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


## Claim

A thematic, lexical, or liturgical marker drives Fisher-Rao surah-aggregate cohesion **only when the marker correlates with multiple structural axes simultaneously** — equivalently, when the marker covers a substantial fraction of the surah's content OR co-occurs with multiple independent structural features (length, chronology, opening formula, surah-class).

A marker occupying a single verse or a sub-block (<30% of the surah) without independent structural correlation produces NULL FR-cohesion on the H-NEW-111 root-distribution instrument.

This is a **substantive empirical regularity, not a methodological-artifact**: every NULL in the supporting findings used the H-NEW-1200 / HM cluster as positive control, and every PASS used permutation-passed tests at α ≤ 0.05.

## Empirical evidence

### Cohesive clusters (FR-cohesive at the surah-aggregate level)

| Cluster | Surahs | Marker | Marker thickness | FR-cohesion p | Cell A or B |
|:--|:-:|:--|:--|:--:|:--|
| **Muqaṭṭāʿat-opened** | 29 | Verse 1 + 13+ correlated axes (length, chronology, book-reference, formulaic-opening, qul-density, Pattern-B) | "Effectively-100%" via multi-axis correlation | **≤ 10⁻¹²** | cross-finding-008 |
| **H-NEW-1200 eschatology** | 14 | idhā-cosmic-event-opener + dominant eschatology content | 60-90% | **0.00030** | H-NEW-1200 |
| **H-NEW-1190 *wa-mā adrāka mā*** | 10 | Recurring meta-question + explanatory verse + dominant eschatology content | 70-100% | **0.00068** | H-NEW-1190 |
| **H-NEW-1080 short-Medinan** | 10 (Q 57-66) | Length + chronology + cohesive juristic content | 100% (length+chronology defines whole surah) | **0.049** | H-NEW-1080 |
| **H-NEW-1320 refrain top-3** | 3 (Q 55, Q 77, Q 26) | Surah-dominant repeated rhetorical refrain | 20-40% of verses, but dominates rhetorical architecture | **0.0000** (vs verse-permutation null) | H-NEW-1320 |

### Non-cohesive clusters (FR-NULL at the surah-aggregate level)

| Cluster | Surahs | Marker | Marker thickness | FR-cohesion p (length-matched) | Other-axis correlation |
|:--|:-:|:--|:--|:--:|:--|
| **IMPV-qrA inventory** | 4 (Q 17, 69, 73, 96) | Single imperative verb-event (occurs 1-2× per surah) | 1-2 verses out of 19-111 (<5%) | **0.129** NULL | None — span chronology, length, muqaṭṭāʿat |
| **Christ-narrative** | 3 (Q 3, Q 5, Q 19) | Christ-content sub-block | ≈25-30 verses out of 98-200 (≈12-30%) | **0.187** NULL | Q 3 ↔ Q 5 share length+chronology+jurisprudence; Q 19 isolated by prophet-cycle catalog |
| **Sajda-surahs** | 14 | Single sajda-trigger verse | 1 verse per surah (0.5-5%) | **0.110** NULL | Weak: 1.7× muqaṭṭāʿat enrichment (descriptive only) |

### Instrument-control validity

All three NULL findings (H-NEW-1310, H-NEW-1330) used **H-NEW-1190 sub-sample** or **H-NEW-1200 full-cluster** as MW-5 positive control under the same uniform-random null distribution. PCs passed at p ≤ 0.05 in all cases (H-NEW-1310 PC p=0.041; H-NEW-1330 PC p=0.00020). The H-NEW-1301 PC failed because the HM cluster (chosen there) is muqaṭṭāʿat-axis-cohesive but not root-distribution-cohesive — a lesson learned and corrected in subsequent pre-regs.

## The threshold

A working empirical rule of thumb based on the 8 data points:

| Marker thickness regime | Cohesion outcome | Confidence |
|:--|:--|:--|
| ≥ 60% of surah content | CONFIRMED cohesion (3 of 3 regime members PASS) | High |
| 30-60% (rhetorical-dominant refrain) | PASS-DIRECTED cohesion (1 of 1 regime member PASS) | Single data point |
| 10-30% (sub-block) | NULL (1 of 1 regime member NULL) | Single data point |
| < 10% (single-verse marker) | NULL unless structurally-correlated (2 of 2 thin-marker regime NULL on root-distribution) | Medium |
| < 10% but multi-axis correlated (muqaṭṭāʿat) | CONFIRMED at extreme p (1 of 1 PASS) | Strong outlier-exception |

The dominant pattern: **marker thickness alone is insufficient**; what matters is whether the marker is **multi-axis-correlated** with other structural features. The muqaṭṭāʿat is a thin-MARKER (1 verse out of 30-286) but **structurally extreme** because it co-varies with 13+ independent axes — flagging surahs that share length, chronology, opening formula, content register, etc.

## Restated principle

**FR-cohesion principle (cross-finding-025)**: A subset C of surahs is FR-cohesive on root-distribution iff the surahs in C share multiple independent structural features. Sharing a single thematic marker, liturgical trigger, or imperative verb-event is necessary but not sufficient.

Equivalent formulations:
1. Surah-aggregate FR is dominated by length + chronology + content-mode + opening-class. A cluster cohesive on FR has surahs that share at least 2-3 of these features in addition to the marker.
2. A single-verse marker does NOT pull the surah into a different region of root-frequency space; it's too thin to move the centroid. Multi-feature shared structure does.
3. The muqaṭṭāʿat is the corpus's "structural-correlation hub": its single-verse marker correlates with length (longer), chronology (Late-Meccan-peak), opening formula (formulaic), book-reference, qul-density, etc. — making it the **maximum-multi-axis-correlation marker** in the corpus.

## Implications

### For the existing finding catalog

- **cross-finding-008 muqaṭṭāʿat**: NOT a counter-example to cross-finding-025; rather the canonical instance of the multi-axis-correlation principle. The 13+ confirmation axes ARE the multi-axis correlation.
- **H-NEW-141** Late-Meccan apparatus is "compositional-phase signature, not per-surah": consistent with cross-finding-025. The 5 axes co-locate at Late-Meccan phase but are not surah-level latent-co-driven; the principle: phase-stratified clustering, not single-axis clustering.
- **H-NEW-1300** Q 96 *iqraʾ*: the descriptive 4-surah inventory {17, 69, 73, 96} is a single-axis marker; failure to FR-cohere is exactly predicted.
- **H-NEW-1310** Christ-narrative: sub-block thickness ≈12-30%; failure is at the low end of the 10-30% regime, predicted.
- **H-NEW-1330** sajda: thinnest-possible marker (1 trigger verse); failure is predicted strongly.
- **H-NEW-1320** refrain top-3: at 20-40% of surah verses but **rhetorically-dominant**; PASS is consistent with the rule that rhetorical-dominance can substitute for content-dominance.

### For future pre-regs

1. **Pre-test marker thickness before designing FR-cohesion tests**. If the marker occupies <10% of the surah and isn't multi-axis correlated, expect NULL. Save the test budget for richer markers.
2. **Use H-NEW-1190 sub-sample or H-NEW-1200 full cluster as MW-5 positive control on root-distribution FR** — they are the only confirmed FR-tight clusters. Avoid HM cluster (letter-set tight, not FR-tight per H-NEW-1301 lesson).
3. **Test thin markers on alternative feature spaces**, not root-distribution. A sajda-surah cluster might cohere on H-NEW-700 rhyme-and-phoneme; an IMPV-qrA cluster might cohere on verse-twin H-NEW-66.

## Honest limits of this synthesis

- **Sample size is small**: 5 PASS clusters + 3 NULL clusters = 8 data points. The "thickness threshold" framing is provisional, not law-strength.
- **The rhetorical-dominance regime has only 1 data point** (H-NEW-1320 refrain top-3 at saturation 0.20-0.40). Replication needed.
- **The "multi-axis correlation" criterion is qualitative**, not yet operationalized as a quantitative measure. A formal definition would require a feature-correlation matrix and a threshold.
- **Bonferroni-acrossfinding correction not yet applied** at the cross-finding level. With 5 PASS findings + 3 NULL findings = 8 "tests-of-the-meta-rule," α_bon for the meta-claim is 0.0063. The PASS findings cluster well below this; the NULLs are unambiguous; but the rule-of-thumb threshold itself needs formal pre-registration.
- **One cluster (H-NEW-1080) at p=0.049 is at the marginal end of significance**. Drop it from the set and the PASS regime tightens further (3-of-3 ≥30%-thick markers passing); keep it and the boundary at 30-60% extends.
- **Q 1 al-Fātiḥa** is sui-generis (cluster-isolated, content-near-Q-108 per the inline-q1-nearest-neighbors note in 01-WHAT-WE-KNOW). Not in the test set; the meta-rule does not address sui-generis surahs.

## Connection to existing meta-syntheses

- **cross-finding-014** (5-principle unified equation): cross-finding-025 refines M5 (compositional-mode decomposition) by clarifying that *content-themes* drive surah cohesion only when dominant. Thin liturgical markers belong to a separate axis (P3-liturgical or P4 in the M-series).
- **cross-finding-015** (classical-scholarship validation pattern): classical aesthetic-rhetorical claims survive empirical test; classical numerological claims fail. This pattern is explained: aesthetic-rhetorical features tend to be multi-axis-correlated (al-Bāqillānī's iʿjāz al-balāgha touches multiple linguistic features simultaneously); numerological claims are single-axis (a single number alone).
- **cross-finding-017** (B6/B7 staircase): muqaṭṭāʿat marker-system anticipates content flags by one Nöldeke sub-bin. Consistent with cross-finding-025: the muqaṭṭāʿat is multi-axis-correlated and itself drives a chronological-staircase architecture.
- **cross-finding-022** (Wave-5 terminal synthesis): the M1.3 structural-hinges decomposition. cross-finding-025 is orthogonal: hinges are TRANSITION features; thickness is CLUSTER-COHESION features. Both are facets of the global mushaf architecture.

## Queued follow-ups (not yet locked)

- **Cross-finding-025-formal**: lock the marker-thickness operational definition (verse-count fraction OR multi-axis-correlation count) as a quantitative pre-reg. Test on 5-10 new candidate clusters at varying thickness; predict PASS/NULL by thickness regime.
- **H-NEW-1331** (queued): hypergeometric sajda × muqaṭṭāʿat over-representation test. Single test α=0.05.
- **H-NEW-1340** (queued): independent replication of refrain top-3 H-NEW-1320 on a different operationalization (longest-repeated 5-token-window).
- **H-NEW-1311** (queued): IMPV-qrA cluster cohesion on H-NEW-700 rhyme-and-phoneme features.
- **H-NEW-1312** (queued): Quran-internal Mūsā-cycle prophet-narrative cluster {Q 7, 20, 26, 28} FR cohesion.

## Verdict

**PRELIMINARY-SYNTHESIS** at 8 supporting findings. The marker-thickness vs FR-cohesion regularity is empirically robust on the current data but not yet formalized for INDEPENDENT REPLICATION at the meta-level. Future cross-finding-025-formal will lock a quantitative pre-reg.

The principle is already operationally useful for pre-reg planning: avoid designing FR-cohesion tests on thin markers with unrelated surahs unless an alternative feature space is justified.

## Sources

- `findings/phase-b-hypotheses/cross-finding-008-muqattaat-as-book-introduction.md`
- `findings/phase-b-hypotheses/h-new-1080-short-medinan-block.md` (referenced in MASTER-LEDGER)
- `findings/phase-b-hypotheses/h-new-1190-wa-ma-adraka-cluster.md`
- `findings/phase-b-hypotheses/h-new-1200-short-meccan-eschatology.md`
- `findings/phase-b-hypotheses/h-new-1301-impv-qra-cluster.md`
- `findings/phase-b-hypotheses/h-new-1310-christ-narrative-cluster.md`
- `findings/phase-b-hypotheses/h-new-1320-refrain-saturation-corpus-rank.md`
- `findings/phase-b-hypotheses/h-new-1330-sajda-surahs-cluster.md`
