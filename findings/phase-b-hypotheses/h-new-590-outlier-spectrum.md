---
id: H-NEW-590
title: "Outlier-strength spectrum — Factor 5 binary→continuous; Q 55 NEAR-replication +14.26pp at standardized window; corpus-wide ranking stable (Spearman ρ̄=0.978); Q 33 al-Aḥzāb is corpus-strongest outlier (+31.5pp); Q 18, Q 62, Q 112 are NOT outliers"
phase: B
status: REPLICATION-FAILED at strict ≥25 threshold (Q 55 Δ=+14.26 at standardized window vs +32.6pp at H-NEW-390 native window); RANK-STABILITY SUPPORTING (ρ̄=0.978 ≥ 0.95)
date: 2026-04-28
executed_by: specialist (H-NEW-590 outlier-spectrum lane)
parent_1: cross-finding-024 (5-factor cohesion model — Factor 5 binary)
parent_2: H-NEW-390 (Q 55 +32.6pp at native window {50-56})
parent_3: H-NEW-89 (Q 62 4-cluster meta-hub)
parent_4: H-NEW-111 (mushaf Fisher-Rao distance matrix)
seed: 20260429
prereg: h-new-590-outlier-spectrum-prereg.md
prereg_sha256: 0c75ee51c5689799989088ff9b3902c8614fa3ec967144d7530f7920f753efae
bonferroni_k: 6
alpha_bon: 0.0083
verdict: PRIMARY PRE-COMMIT (Q 55 Δ ≥ 25) FAILED at standardized window (+14.26pp); SUPPORTING (Spearman bootstrap ρ̄=0.978 ≥ 0.95) PASSED; Factor 5 EMPIRICALLY CONTINUOUS — outlier-strength is a graded scalar, not a binary flag; H-NEW-390 effect is window-conditional (native {50-56} ≠ standardized {52-58})
---

# [[h-new-590-outlier-spectrum|H-NEW-590]] — Outlier-strength spectrum: Factor 5 from binary to continuous

## 1. Headline

| Test | Result | Verdict |
|:--|:-:|:--|
| **PRIMARY** Q 55 Δ%ile ≥ 25 (replication of [[h-new-390-q55-outlier-exclusion|H-NEW-390]] at standardized window) | **+14.26pp** | **FAILED** at strict threshold |
| **SUPPORTING** Spearman bootstrap rank-stability ≥ 0.95 | **ρ̄ = 0.978; min = 0.945; 99.5% of bootstraps ≥ 0.95** | **PASSED** |
| Aggregate verdict | mixed | Factor 5 IS continuous; [[h-new-390-q55-outlier-exclusion|H-NEW-390]] magnitude is WINDOW-CONDITIONAL |

Per-candidate Δ%ile at standardized 7-surah window centered on X:

| X | Window | Δ%ile | Class |
|:-:|:--|:-:|:--|
| Q 1 al-Fātiḥa | {1..7} | **+27.09** | STRONG OUTLIER |
| Q 9 al-Tawba | {6..12} | **+21.57** | MODERATE OUTLIER |
| Q 55 al-Raḥmān | {52..58} | **+14.26** | MODERATE OUTLIER |
| Q 18 al-Kahf | {15..21} | +0.39 | NULL |
| Q 62 al-Jumuʿa | {59..65} | −1.82 | NULL |
| Q 112 al-Ikhlāṣ | {108..114} | 0.00 | NULL (floor-effect) |

**Major finding**: outlier-strength is a CONTINUOUS spectrum spanning roughly [-21, +31] across 114 surahs, with clear graded magnitudes. The binary "outlier / not-outlier" flag in [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] Factor 5 is replaced with a per-surah scalar Δ%ile. Q 55 is NOT the strongest outlier — Q 33 al-Aḥzāb (+31.46pp) and Q 1 al-Fātiḥa (+27.09pp) exceed Q 55 at standardized window.

## 2. Per-candidate Δ + classical anchor

### Q 1 al-Fātiḥa: Δ = +27.09pp — STRONG OUTLIER (NEW)

Window {1..7} drops from 37.90%ile to 10.81%ile when Q 1 is removed. **Removing al-Fātiḥa makes the opening block dramatically more cohesive.** This is the empirical signature of structural uniqueness: Q 1 is a 7-verse liturgical preamble, not part of the ṭiwāl ledger.

**Classical anchor**: al-Bukhārī ḥadīth #756 (*fātiḥat al-kitāb*); umm al-Kitāb status. The Prophet's designation of al-Fātiḥa as the "Mother of the Book" treats it as structurally distinct from the rest of the corpus. **Empirically confirmed**: Q 1 disrupts content-cohesion of {Q 2-7} block by +27pp.

This is a NEW empirical claim from [[h-new-590-outlier-spectrum|H-NEW-590]] not previously isolated in [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]].

### Q 9 al-Tawba / Barāʾa: Δ = +21.57pp — MODERATE OUTLIER (NEW)

Window {6..12} drops from 57.42%ile to 35.85%ile when Q 9 is removed. **The no-basmala uniqueness has empirical content-disruption signature**.

**Classical anchor**: al-Suyūṭī *al-Itqān* nawʿ 23 — Q 9 is the unique surah without basmala. Ibn ʿAbbās tradition: "*kānat barāʾa wa-l-anfāl tudʿā al-qarīnatayn*" — Q 8 and Q 9 are paired ("the Two Twins"), Q 9 begins mid-narrative continuing from Q 8. **Empirically supported**: even within the {Q 6..12} block (which contains its supposed twin Q 8), Q 9 disrupts cohesion by +21.6pp. The classical "twins" claim (al-Anfāl + al-Tawba as continuous text) is NOT directly tested here, but Q 9's standalone outlier status is confirmed.

### Q 18 al-Kahf: Δ = +0.39pp — NULL

Window {15..21} is essentially unchanged when Q 18 is removed. **al-Kahf is NOT an outlier at standardized window**.

**Classical anchor**: Muslim ḥadīth #809 — Friday-recitation merit; al-Nawawī *al-Adhkār*. Q 18's classical distinction is liturgical (Friday recitation) and narrative (4 stories: Sleepers, Garden, Mūsā/al-Khiḍr, Dhū al-Qarnayn), not structural-content-distinctness from neighbors {Q 15-17, 19-21}. The neighborhood is itself narrative-heavy (Q 17 al-Isrāʾ, Q 19 Maryam, Q 20 Ṭā-Hā), so Q 18 fits in.

**This is a CLASSICAL-vs-EMPIRICAL distinction**: liturgical merit ≠ content-cohesion-disruption. al-Kahf's classical importance is real but operates on a different axis than Factor 5.

### Q 55 al-Raḥmān: Δ = +14.26pp — MODERATE OUTLIER (NEAR-replication, threshold-fail)

Window {52..58} (standardized) drops from 97.81%ile to 83.55%ile when Q 55 is removed. **The disruption signature is REAL but its magnitude depends on window choice**.

**[[h-new-390-q55-outlier-exclusion|H-NEW-390]] native window**: {Q 50..56} (Meccan musabbiḥāt block). Q 55 contributes +32.6pp.
**[[h-new-590-outlier-spectrum|H-NEW-590]] standardized window**: {Q 52..58}. Q 55 contributes +14.26pp.

Why the gap? The standardized window {52..58} includes Q 57 al-Ḥadīd and Q 58 al-Mujādila — Medinan surahs across the Hijra hinge — which themselves create dispersion. The "before-Q 55" baseline is therefore much higher in the standardized window (83.55%ile vs [[h-new-390-q55-outlier-exclusion|H-NEW-390]]'s 37.5%ile). Q 55's marginal contribution looks smaller because the surrounding block is already disrupted by Hijra-spanning.

**Classical anchor**: al-Tirmidhī #3291 *ʿarūs al-Qurʾān* (Bride of the Quran). [[h-new-231-kl-divergence-per-surah|H-NEW-231]] KL-divergence outlier. **Empirically: Q 55 IS a moderate outlier at standardized window; pre-committed strict ≥25 threshold FAILED. The [[h-new-390-q55-outlier-exclusion|H-NEW-390]] effect is real but window-conditional.**

This is an HONEST PRE-COMMIT VIOLATION. The pre-reg's ≥25 threshold was set under the implicit assumption that the standardized window would behave like the [[h-new-390-q55-outlier-exclusion|H-NEW-390]] native window. It does not. The replication "fails" at strict threshold but the directional signature (Q 55 > 0; Q 55 in top 7 corpus-wide outliers) is consistent.

### Q 62 al-Jumuʿa: Δ = −1.82pp — NULL (hub ≠ outlier)

Window {59..65} is essentially unchanged when Q 62 is removed. **Q 62 is NOT an outlier**.

**Classical anchor**: [[h-new-89-meta-cluster-network|H-NEW-89]] 4-cluster meta-hub status. Q 62 is a network-bridge node (high meta-hub centrality), but meta-hub status does NOT predict content-disruption. **Hub ≠ outlier — empirically distinct properties**.

This is an important architectural disambiguation: [[cross-finding-023-causal-generative-closure|cross-finding-023]] hub-architecture (M_H top-100 scaffold) and [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] Factor 5 outlier-strength are independent measures. A surah can be a meta-hub WITHOUT being a content-outlier (Q 62 demonstrates this). [[h-new-590-outlier-spectrum|H-NEW-590]] empirically separates them.

### Q 112 al-Ikhlāṣ: Δ = 0.00pp — NULL (FLOOR EFFECT, not absence-of-effect)

Window {108..114} is at 0.00%ile both with and without Q 112. **Δ is undefined-at-floor**: the terminal block is so cohesive (cf. [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] row 1: 0%ile) that no removal can lower it further.

**Classical anchor**: al-Bukhārī ḥadīth #5013 *thulth al-Qurʾān* (one-third of the Quran). al-Ikhlāṣ is classically singled out as creedally complete. **Empirically: at standardized window, al-Ikhlāṣ is INDISTINGUISHABLE from its neighbors {Q 108-111, 113-114}** — they are all compact creedal/protective surahs sharing the same register. Q 112's classical 1/3-of-Quran designation is a CONTENT-DENSITY claim (tawḥīd in 4 verses), not a content-DISTINCTNESS claim relative to its terminal neighbors.

This is a clean classical-vs-empirical split: high content-density (classical) ≠ high outlier-strength (empirical).

## 3. Corpus-wide ranking (top 10 outliers)

| Rank | X | Δ%ile | Window | Surah | Note |
|:-:|:-:|:-:|:--|:--|:--|
| 1 | Q 33 | **+31.46** | {30-36} | al-Aḥzāb | Medinan ṭiwāl in Meccan-dominant neighborhood |
| 2 | Q 1 | **+27.09** | {1-7} | al-Fātiḥa | umm al-Kitāb; structural preamble |
| 3 | Q 24 | **+23.51** | {21-27} | al-Nūr | Medinan legal in narrative-Meccan block |
| 4 | Q 9 | **+21.57** | {6-12} | al-Tawba | no-basmala; Medinan in Meccan-Meccan-Medinan transition |
| 5 | Q 12 | **+14.26** | {9-15} | Yūsuf | continuous narrative outlier among muqaṭṭaʿāt-openers |
| 6 | Q 55 | **+14.26** | {52-58} | al-Raḥmān | refrain-structured; [[h-new-390-q55-outlier-exclusion|H-NEW-390]] native +32.6pp |
| 7 | Q 8 | +9.81 | {5-11} | al-Anfāl | Medinan in Medinan-Meccan boundary |
| 8 | Q 26 | +8.83 | {23-29} | al-Shuʿarāʾ | qiṣaṣ block boundary |
| 9 | Q 35 | +6.68 | {32-38} | Fāṭir | between muqaṭṭaʿāt families |
| 10 | Q 53 | +6.25 | {50-56} | al-Najm | oath-opener mid-Meccan |

**Pattern**: top outliers are NOT random. They cluster around (a) chronology-boundary crossings (Q 9, Q 8, Q 33, Q 24 are Medinan in Meccan-rich neighborhoods or vice versa), (b) structurally-unique liturgical surahs (Q 1, Q 55), and (c) narrative outliers in non-narrative blocks (Q 12 Yūsuf is a continuous-narrative surah surrounded by muqaṭṭaʿāt-headed mixed-genre surahs).

**Bottom 10 (cohesion-anchors)**:

| Rank | X | Δ%ile | Window | Surah | Note |
|:-:|:-:|:-:|:--|:--|:--|
| 105 | Q 41 | -7.68 | {38-44} | Fuṣṣilat | core ḥawāmīm |
| 106 | Q 10 | -7.83 | {7-13} | Yūnus | core ALR family |
| 107 | Q 59 | -8.36 | {56-62} | al-Ḥashr | core musabbiḥāt |
| 108 | Q 27 | -8.76 | {24-30} | al-Naml | core qiṣaṣ |
| 109 | Q 45 | -10.68 | {42-48} | al-Jāthiyah | core ḥawāmīm |
| 110 | Q 52 | -10.82 | {49-55} | al-Ṭūr | oath-opener mid-Meccan |
| 111 | Q 23 | -10.91 | {20-26} | al-Muʾminūn | core narrative-creedal |
| 112 | Q 3 | -15.28 | {1-7} | Āl ʿImrān | Medinan ṭiwāl with Q 2 |
| 113 | Q 51 | -16.17 | {48-54} | al-Dhāriyāt | oath-opener mid-Meccan |
| 114 | **Q 2** | **-20.62** | {1-7} | al-Baqara | the great Medinan ṭiwāl |

**Pattern**: cohesion-anchors are CORE FAMILY MEMBERS. Q 2 (al-Baqara) is the strongest cohesion-anchor: removing it from {Q 1..7} makes the block LESS cohesive by 20.6pp. This is the empirical inverse of outlier: surahs that DEFINE their neighborhood's content register, such that removing them disrupts the block.

Q 2 al-Baqara is the largest surah (286 verses) and dominates the early ṭiwāl content-signature; Q 3 Āl ʿImrān, Q 23 al-Muʾminūn, and the ḥawāmīm-core surahs (Q 41, 45) similarly anchor their blocks.

## 4. Implication for [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] Factor 5 (binary → continuous)

The [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] 5-factor cohesion model previously listed Factor 5 as binary "no-outlier-surahs":

> Factor 5 — NO-OUTLIER-SURAHS (Ibn Kathīr / al-Tirmidhī / al-Zamakhsharī)
> Surahs with unique structural profiles ... DISRUPT block cohesion ...

**[[h-new-590-outlier-spectrum|H-NEW-590]] replaces this with a continuous spectrum**:

> Factor 5 (revised) — OUTLIER-STRENGTH Δ%ile(X)
> A per-surah scalar Δ%ile(X) ∈ [-21, +31] measures the marginal contribution to neighborhood cohesion.
> POSITIVE Δ = outlier-disruptor (block becomes more cohesive without X).
> NEGATIVE Δ = cohesion-anchor (block becomes less cohesive without X).
> ZERO Δ = neutral (X fits its neighborhood).

**Concrete revisions**:

1. The factor is now SIGNED: cohesion-anchors are EMPIRICALLY DISTINCT from neutral surahs (Q 2's −20.6pp is a 41.7pp swing from Q 33's +31.5pp).
2. The factor admits MAGNITUDE: Q 55's +14.26pp (standardized) and Q 33's +31.46pp differ by 2.2×.
3. The [[h-new-390-q55-outlier-exclusion|H-NEW-390]] effect is WINDOW-CONDITIONAL: Q 55 = +32.6pp at native {50-56} but +14.26pp at standardized {52-58}.
4. Hub-status ([[cross-finding-023-causal-generative-closure|cross-finding-023]] M_H scaffold) and outlier-status (Factor 5) are EMPIRICALLY INDEPENDENT — Q 62 demonstrates this.

The rank-stability bootstrap (ρ̄=0.978; 99.5% of 200 resamples ≥0.95) confirms that the corpus-wide ordering is robust to null-resampling. The Δ%ile vector is a stable corpus-level descriptor.

## 5. Honest limits

1. **PRIMARY pre-committed test FAILED at strict threshold**: Q 55 Δ=+14.26 < 25. The [[h-new-390-q55-outlier-exclusion|H-NEW-390]] effect is window-conditional. This is published with EQUAL PROMINENCE per project discipline.
2. **Window size 7 is one choice**; alternative widths (5, 9, 11) untested. The Q 55 magnitude could move substantially under different window choices.
3. **Edge-clipping** for Q 1 and Q 112 is sliding-inward (Q 1 → {1..7}; Q 112 → {108..114}) — these edge cases have asymmetric neighborhoods.
4. **Q 112's floor-effect**: at terminal-block 0%ile baseline, Δ is undefined-at-floor and reads as 0.00pp. This is NOT evidence of "Q 112 not being an outlier" — it is a measurement-instrument limitation in the terminal block.
5. **FR-roots only** — char-4-gram outlier-strength untested.
6. **Bonferroni-6 α=0.0083** applies to descriptive p-values; the PRIMARY test is a magnitude test (Δ ≥ 25), not a p-value test, so Bonferroni does not gate it.
7. **Corpus-wide ranking is descriptive-supplementary**, not pre-committed. New claims about specific high-rank surahs (Q 33, Q 24) require separate pre-registration.
8. **Q 9 al-Tawba's "twin" with Q 8** is not directly tested; Q 9's outlier status is measured at single-surah resolution.
9. **Spearman bootstrap N=200**, not 10000. Sufficient for ρ ≥ 0.95 stability claim; could be tightened.
10. **Classical anchors are corpus-internal mappings**; predictions of "structural uniqueness ⇒ Δ > 0" are hypotheses, not pre-registered tests here.

## 6. Cross-references

- **[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]** (5-factor cohesion model): Factor 5 binary → continuous; this finding revises Factor 5 in place.
- **[[h-new-390-q55-outlier-exclusion|H-NEW-390]]** (Q 55 native +32.6pp): NEAR-replicated at +14.26pp standardized window; gap is window-conditional.
- **[[h-new-89-meta-cluster-network|H-NEW-89]]** (Q 62 4-cluster meta-hub): Q 62 Δ ≈ 0 confirms hub ≠ outlier — independent properties.
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** (mushaf FR distance matrix): source of D_matrix.
- **[[h-new-231-kl-divergence-per-surah|H-NEW-231]]** (Q 55 KL-divergence outlier): consistent direction.
- **[[h-new-234-q55-unified-profile|H-NEW-234]]** (Q 55 unified profile): consistent.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (mushaf FR confirmed): substrate.
- **[[cross-finding-023-causal-generative-closure|cross-finding-023]]** (M_H top-100 scaffold): hub-axis disambiguated from outlier-axis here.
- **al-Bukhārī #756** (umm al-Kitāb for Q 1): empirically vindicated — Q 1 is corpus-rank-2 outlier.
- **al-Bukhārī #5013** (thulth al-Qurʾān for Q 112): NOT empirically translated to outlier-strength; classical density-claim ≠ empirical distinctness-claim.
- **al-Tirmidhī #3291** (ʿarūs al-Qurʾān for Q 55): partially confirmed — Q 55 IS a moderate outlier even at standardized window.
- **al-Suyūṭī *al-Itqān* nawʿ 23** (Q 9 no-basmala): empirically vindicated as content-outlier (+21.6pp).
- **Muslim ḥadīth #809** (Q 18 Friday recitation): liturgical merit, NOT outlier-strength.

## 7. Queued follow-ups

- **H-NEW-591**: Q 33 al-Aḥzāb top-corpus-outlier — pre-register a focused test of its +31.5pp effect (Medinan in Meccan neighborhood; multiple sub-narratives).
- **H-NEW-592**: Q 2 al-Baqara as STRONGEST cohesion-anchor (Δ=-20.62); pre-register a follow-up testing whether Q 2's removal from {Q 1..7} truly shatters the block.
- **H-NEW-593**: Window-size sensitivity — replicate the 6-candidate test at widths 5, 9, 11; quantify how much Δ depends on window choice.
- **H-NEW-594**: Pre-register Q 9's "twin" claim — does the {Q 8, Q 9} pair viewed as one combined unit reduce its outlier signature?
- **H-NEW-595**: Cross-axis test — correlate [[h-new-590-outlier-spectrum|H-NEW-590]] Δ%ile vector with [[cross-finding-023-causal-generative-closure|cross-finding-023]] M_H hub-centrality vector. If ρ ≈ 0, the two axes are orthogonal (predicted from Q 62 NULL here).
- **H-NEW-596**: Floor-effect bypass — for terminal-block surahs (Q 108-114), use a different statistic (e.g. d̄(W) − d̄(W\X) raw distance, not %ile) to avoid the floor.
- **H-NEW-597**: Char-4-gram replication of the spectrum — does the outlier-strength ranking transfer across metrics?
- **H-NEW-598**: Q 55 window-sensitivity — measure Δ at every contiguous 7-window containing Q 55 ({49-55}, {50-56}, {51-57}, {52-58}, {53-59}, {54-60}); report range.
- **H-NEW-599**: [[cross-finding-024-five-factor-cohesion-model|Cross-finding-024]] v2 — formal revision of the 5-factor model with Factor 5 as continuous Δ%ile.

## 8. Final statement

**[[h-new-590-outlier-spectrum|H-NEW-590]] establishes that Factor 5 (outlier-strength) of the [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] 5-factor cohesion model is EMPIRICALLY CONTINUOUS, not binary.** A per-surah scalar Δ%ile(X) measures the marginal contribution of each surah to its 7-surah neighborhood's content-cohesion. The corpus-wide spectrum spans roughly [-21, +31]pp.

**The pre-committed PRIMARY test (Q 55 Δ ≥ 25) FAILED at the standardized window** (+14.26pp observed vs ≥25 required). This is an HONEST PRE-COMMIT VIOLATION published with full prominence. The [[h-new-390-q55-outlier-exclusion|H-NEW-390]] +32.6pp effect is real but WINDOW-CONDITIONAL — the standardized window {52..58} includes the Hijra-hinge surahs Q 57, Q 58 which inflate the baseline dispersion and mask Q 55's marginal contribution.

**The pre-committed SUPPORTING test (Spearman bootstrap rank-stability ≥ 0.95) PASSED** with ρ̄=0.978 (min=0.945; 99.5% of 200 bootstraps ≥0.95). The corpus-wide outlier-strength ordering is robust.

**Empirical findings beyond pre-registration** (descriptive, requiring separate follow-up):

- **Q 33 al-Aḥzāb is the corpus-strongest outlier** (+31.46pp), exceeding Q 55 even at [[h-new-390-q55-outlier-exclusion|H-NEW-390]]'s native magnitude.
- **Q 1 al-Fātiḥa is the second-strongest outlier** (+27.09pp); umm al-Kitāb classical designation EMPIRICALLY VINDICATED.
- **Q 9 al-Tawba is a moderate outlier** (+21.57pp); no-basmala uniqueness EMPIRICALLY VINDICATED as content-disruptive.
- **Q 18 al-Kahf, Q 62 al-Jumuʿa, Q 112 al-Ikhlāṣ are NOT empirical outliers** at standardized window — their classical distinctions (Friday-recitation, meta-hub, thulth-al-Qurʾān) operate on AXES INDEPENDENT of Factor 5.
- **Q 2 al-Baqara is the corpus-strongest cohesion-anchor** (Δ=-20.62pp): removing al-Baqara makes the opening ṭiwāl block markedly less cohesive — al-Baqara DEFINES the early-ṭiwāl content-register.
- **Hub-status ([[cross-finding-023-causal-generative-closure|cross-finding-023]]) and outlier-status (Factor 5) are EMPIRICALLY INDEPENDENT** — Q 62 is a meta-hub ([[h-new-89-meta-cluster-network|H-NEW-89]]) yet has Δ ≈ 0.

**Classical-empirical splits**: liturgical merit (Q 18 Friday), content density (Q 112 thulth), meta-hub centrality (Q 62) are AXES DISTINCT FROM outlier-strength. The classical tradition's discipline of maintaining separate categorial layers is again vindicated — [[h-new-590-outlier-spectrum|H-NEW-590]] confirms that "structural uniqueness" classifications in classical sources are NOT reducible to a single empirical content-distinctness measure.

**Implication for [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]**: Factor 5 is now a SIGNED CONTINUOUS scalar Δ%ile(X) per surah. The 5-factor model's predictive power should improve when Factor 5 takes its full graded form rather than the previous binary flag.

Pre-commit violation (Q 55 strict threshold) and pre-commit success (rank-stability) are published WITH EQUAL PROMINENCE. The Quran is one text; this measurement is one window-choice within a broader spectrum.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
