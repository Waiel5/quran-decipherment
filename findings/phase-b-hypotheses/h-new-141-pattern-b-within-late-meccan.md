---
id: H-NEW-141
title: Within-Late-Meccan Pattern-B pairwise correlations (theorist Prediction 1)
phase: B
status: NULL (theorist's Prediction 1 REFUTED; model tightening)
date: 2026-04-17
executed_by: team-lead (inline)
source_pre_reg: scratch/theorist-2026-04-17-unified-equation.md §5 Prediction 1
parent: cross-finding-012 (Late-Meccan Pattern-B co-peak); theorist P1★
bonferroni_k: 10
bonferroni_family: h-new-141-within-late-meccan
alpha_bon: 0.005
direction: POSITIVE pairwise ρ > 0.4 (theorist predicted)
verdict: NULL
---

# [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] — Pattern-B pairwise correlation within Late-Meccan

## Hypothesis (theorist Prediction 1)

Under P1★ (Late-Meccan scripture-announcement), the 5 Pattern-B axes should COVARY within Late-Meccan surahs — a single latent factor should drive all of them together.

## Method

21 Late-Meccan surahs per [[h-new-125-chronology-content|H-NEW-125]] classification. Spearman pairwise ρ on all C(5,2)=10 Pattern-B axis pairs. Bonferroni k=10, α_bon=0.005.

## Results

| Pair | ρ | p |
|---|:-:|:-:|
| qul × book_reference | +0.553 | 0.0093 |
| qul × eschatological | −0.016 | 0.947 |
| qul × muq_cardinality | −0.122 | 0.599 |
| qul × loanword | +0.196 | 0.394 |
| book_reference × eschatological | +0.057 | 0.806 |
| book_reference × muq_cardinality | −0.011 | 0.963 |
| book_reference × loanword | −0.091 | 0.695 |
| eschatological × muq_cardinality | −0.044 | 0.848 |
| eschatological × loanword | −0.027 | 0.907 |
| muq_cardinality × loanword | +0.243 | 0.288 |

**Only 1/10 pairs has ρ > 0.4** (qul × book_reference at +0.55).
**0/10 pairs Bonferroni-10 significant**.
**Mean pairwise ρ = +0.07** (essentially zero, consistent with independence).

4-axis sensitivity (exclude muq_cardinality, Bon-6): same result, 1/6 pairs > 0.4.

## Verdict

**NULL**. Theorist's Prediction 1 is REFUTED at pre-registered criterion.

## Interpretation — critical model constraint

The Late-Meccan scripture-announcement apparatus is NOT a single latent factor. It is a **BUNDLE PHENOMENON**:

- Inter-period: 5 axes co-peak at Late-Meccan sub-bin B7 ([[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] PASS-DIRECTED stands)
- Intra-period: the 5 axes are statistically INDEPENDENT within Late-Meccan (this finding)

This means different Late-Meccan surahs emphasize different parts of the apparatus:
- Q 9 al-Tawba is qul-heavy (26.7 per 100v)
- Q 26 al-Shuʿarāʾ is book-ref-heavy (24.8 per 100v)
- Q 11 Hūd is eschatology-heavy (51.2 per 100v)
- Q 7 al-Aʿrāf is muq-cardinality max (4)
- Q 19 Maryam is loanword-heavy (159 per 100v, close to peak)

No single Late-Meccan surah dominates on ALL 5 axes; no two axes strongly covary. The "scripture-announcement phase" is a period-level statistical co-peak, not a surah-level unified dimension.

## Implications for theorist's P1★

P1★ must be refined from:
> "A single latent factor τ(s) drives qul, book-ref, eschatology, muq-cardinality, and loanword densities jointly."

To:
> "5 independent axes happen to co-peak at Nöldeke sub-bin B7 (Hijra-straddling). The co-peak DEFINES the scripture-announcement phase empirically, but no single underlying factor explains within-period variance."

This tightens the model. It also explains:
- Why [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] (muq_cardinality × Pattern-B composite) passed at only ρ=+0.37 (not higher) — the axes are genuinely independent within the muq subset
- Why audit-036 flagged Pattern-B composite "effective dimension < 4" — the composite averages nearly-independent quantities

## Queue

- H-NEW-141.1: same test on Early + Middle + Medinan periods for comparison — is independence UNIQUE to Late-Meccan or a corpus-wide property?
- H-NEW-141.2: factor-analytic test — does a 1-factor model fit the 5 Pattern-B axes worse than a 2-factor or 5-factor model?

## Classical wisdom

This is consistent with classical tafsir observations that Late-Meccan surahs show THEMATIC DIVERSITY rather than a single theme — each surah has its own character (cf. al-Rāzī's Mafātīḥ al-ghayb on surah-by-surah thematic unity). Our empirical independence-within-period mirrors classical recognition that surahs are DISTINCT compositional units, each with their own emphasis.

The Late-Meccan PHASE is a period of heightened scripture-self-awareness; the SURAH-level expression of that phase varies.

## Files

- Script: inline (seed 20260417)
- Findings: this file
