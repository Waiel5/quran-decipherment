---
id: H-NEW-188
title: Grand correlation matrix + factor analysis of per-surah structural measures
phase: B
status: MIXED (factor structure clear; Pattern-B bundle coherence NULL)
date: 2026-04-17
executed_by: autonomous-agent
seed: 20260419
bonferroni_k: 2
bonferroni_family: h-new-188-grand-correlation
alpha_bon: 0.025
parents: H-NEW-172, H-NEW-159, H-NEW-163, H-NEW-125, H-NEW-141
children_queue: H-NEW-188.1 (varimax rotation), H-NEW-188.2 (partial out Nöldeke and re-cluster)
---

# [[h-new-188-grand-correlation|H-NEW-188]] — Grand correlation matrix + factor analysis

## Setup

114 surahs × 19 features. Features: surah_length, mean_verse_length,
muq_cardinality, allah_density, qul_density, prophet_narrative_density,
legal_term_density, eschatological_density, book_reference_density, oath_density,
divine_name_density, personal_pronoun_density, rhyme_letter_diversity,
refrain_density, loanword_density, alpha_zipf, beta_heap, dispersion,
noldeke_rank.
Missingness: α missing for 21 short surahs (insufficient fit points);
β missing for 35 short surahs. Content-axis and dispersion features complete.

## Top-10 pairwise correlations (Pearson, pairwise-complete)

| pair | r |
|---|:-:|
| allah_density × divine_name_density | +0.959 |
| mean_verse_length × noldeke_rank | +0.899 |
| mean_verse_length × loanword_density | +0.890 |
| mean_verse_length × divine_name_density | +0.878 |
| mean_verse_length × allah_density | +0.857 |
| divine_name_density × noldeke_rank | +0.826 |
| loanword_density × noldeke_rank | +0.820 |
| allah_density × noldeke_rank | +0.812 |
| eschatological_density × loanword_density | +0.746 |
| mean_verse_length × legal_term_density | +0.737 |

The dominant structure is a **long/Medinan-leaning vs short/Early-Meccan axis**
expressed through verse length, Allah/divine-name density, loanword density,
eschatological density, and Nöldeke rank.

## Top-3 principal components

| PC | λ | % var | cum % |
|---|---|---|---|
| PC1 | 7.14 | 37.6 % | 37.6 % |
| PC2 | 2.26 | 11.9 % | 49.5 % |
| PC3 | 1.43 |  7.5 % | 57.0 % |

**PC1 "Long-form/Medinan axis"** (loadings > 0.79):
mean_verse_length +0.96, loanword +0.93, noldeke_rank +0.91,
divine_name +0.86, allah +0.82, eschatological +0.80.

**PC2 "Composition-size / lexical diversity"** (after PC1 absorbs the content signal):
surah_length +0.73, dispersion −0.67, α +0.53, muq_cardinality +0.46, β −0.46,
refrain +0.39. This is a length-of-surah axis contrasted with per-token
repetitiveness (high dispersion = scattered root use = low composition).

**PC3 "Refrain / rhyme idiosyncrasy"**:
refrain +0.56, β −0.55, muq_cardinality −0.43, rhyme_letter_diversity −0.38.
This captures the refrain-heavy short-surah signature (Q 55 Rahmān, Q 77 Mursalāt)
where a single fasila is re-used and β drops.

Top-3 cumulative variance **57.0 % > 50 %** (pre-reg PASS on the factor-count
criterion).

## Hierarchical clustering (1−|r|, complete linkage)

Tightest groupings (first merges):
1. **"Divine signature"**: allah_density ↔ divine_name_density (d=0.04) — the two are
   near-identical because "Allah" dominates the 99-name distribution.
2. **"Medinan apparatus"**: mean_verse_length + noldeke_rank + loanword_density
   (merged at d≤0.18); joined by allah_density + divine_name_density at d=0.30.
3. **"Legal-revelation triangle"**: legal_term_density + book_reference_density
   (d=0.325), merged with eschatological_density at d=0.416.
4. **"Compositional-size"**: α_zipf + dispersion (d=0.416), then + surah_length
   (d=0.460).
5. **"Fasila / refrain"**: refrain_density + β_heap (d=0.644).

## Pre-registered test 1 — factor-loading patterns (PASS)

Top-3 PC cumulative variance 57.0 %; exceeds 50 % threshold. PC1 cleanly
identifies the Medinan-apparatus axis, PC2 the composition-size axis, PC3 the
refrain/rhyme axis. Loadings are interpretable.

## Pre-registered test 2 — Pattern-B bundle coherence (NULL)

Bundle = {qul, book_reference, eschatological, loanword, muq_cardinality}.

| PC | mean \|loading\| on bundle |
|---|:-:|
| PC1 | 0.634 |
| PC2 | 0.129 |
| PC3 | 0.244 |

Max over top-3 PCs = 0.634 (on PC1).
Null (10 000 random 5-feature draws from M=19): mean 0.548, 95-th pctile 0.729.
One-sided p = **0.2174**. **NULL** at α_bon = 0.025.

Sensitivity: listwise-complete (n=79, drops small surahs) gives obs_max 0.535,
p = 0.376 — also NULL.

**Verdict: Pattern-B bundle is NOT a distinctive coherent factor corpus-wide.**
Most of its PC1 loading is driven by the Medinan-apparatus factor (mean_verse_length,
noldeke_rank, allah/divine_name all sit together on PC1 with loadings > 0.8);
a random 5-feature draw from the same matrix matches the bundle's loading
roughly 22 % of the time. The Pattern-B bundle lives inside a broader
"Medinan/long-form" factor rather than constituting its own axis.

## Cross-reference to [[h-new-141-pattern-b-within-late-meccan|H-NEW-141]]

[[h-new-141-pattern-b-within-late-meccan|H-NEW-141]] found the Pattern-B axes pairwise independent *within Late-Meccan*
(mean ρ ≈ +0.07, 0/10 pairs Bonferroni-significant). [[h-new-188-grand-correlation|H-NEW-188]] now shows that
even **corpus-wide**, where a massive Medinan-vs-Early-Meccan gradient exists,
the bundle's PC1 signature is indistinguishable from a random 5-feature draw.
The bundle is period-localised co-peak ([[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]) rather than a
latent psychometric dimension.

## Orthogonality findings

Weakest |r| pairs (effectively orthogonal):
- rhyme_letter_diversity × noldeke_rank  r≈0
- oath_density × beta_heap  r≈0
- qul_density × rhyme_letter_diversity  r≈0

Rhyme-letter diversity is surprisingly uncorrelated with everything —
it is a **clean orthogonal axis**, worth preserving as a distinct structural
measure.

## Implications

1. For dimension-reduction work, 3 PCs capture the structural shape of the corpus
   (Medinan-apparatus / composition-size / refrain-rhyme).
2. **β_heap** and **rhyme_letter_diversity** carry information not captured by
   α or dispersion — β is paired with refrain (PC3), rhyme_letter is near-isolated.
3. The Pattern-B bundle should be retreated as **period-indexed**, not a
   cross-sectional latent. Any model using it as a single latent will be
   mis-specified corpus-wide.
4. allah_density and divine_name_density are **effectively redundant** (r=0.959);
   use one, drop one for parsimony.

## Deliverables

- `findings/phase-b-hypotheses/csv/h-new-188.json` — full numeric output
- `findings/phase-b-hypotheses/csv/h-new-188-corrmatrix.csv` — 19×19 Pearson
- `findings/phase-b-hypotheses/csv/h-new-188-loadings.csv` — PC loadings
- `scripts/h_new_188_grand_correlation.py` — reproducible, seed 20260419
