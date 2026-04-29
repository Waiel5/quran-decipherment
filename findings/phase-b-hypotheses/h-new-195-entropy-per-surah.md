---
id: H-NEW-195
title: Per-surah letter-bigram entropy — Quran vs Bukhārī, length-residual correlates
phase: B
status: PARTIAL-PASS (primary PASS; secondary muq FAIL; MW-5 PASS)
date: 2026-04-17
executed_by: team-lead (inline)
seed: 20260419
rules_tuple: "(Hafs-Kūfan; no-tashkeel; raw Arabic letters U+0621..U+064A; cross-verse bigrams; Bukhārī top-114 longest bab-segments, same normalization)"
bonferroni_k: 2
bonferroni_family: h-new-195-bigram-entropy
alpha_bon: 0.025
direction: two-sided (both primary and secondary)
verdict: PARTIAL-PASS
parent_findings:
  - h-new-25 (trigram-entropy Quran<baselines, corpus-level)
  - h-new-159 (Heap β per-surah variance 2.5× Bukhārī)
  - h-new-163 (dispersion ranking all 114 surahs)
  - h-new-172 (per-surah Zipf α)
  - h-new-178 (α,β manifold, +0.034 muq residual)
pre_reg: findings/phase-b-hypotheses/h-new-195-entropy-per-surah-prereg.md
pre_reg_sha256: 7fda988730121eba5fe7dc35bed1a3f8e334459e3641232108601e570fdb1786
script: scripts/h_new_195_per_surah_bigram_entropy.py
outputs:
  - findings/phase-b-hypotheses/csv/h-new-195.json
  - findings/phase-b-hypotheses/csv/h-new-195-per-surah.csv
  - findings/phase-b-hypotheses/csv/h-new-195-bukhari-per-segment.csv
---

# [[h-new-195-entropy-per-surah|H-NEW-195]] — Per-surah letter-bigram entropy

## Headline

- **PRIMARY PASS**: Quran mean H(L2|L1) = 3.164 bits; Bukhārī top-114 bab-segments
  mean = 3.618 bits. Δ = −0.454 bits. Welch t=−6.41, df=120.3, p ≈ 0 (two-sided);
  MWU z=−3.96, p=7.6e−5; paired Wilcoxon (length-sorted) z=−6.84, p≈0.
  **Quran is letter-bigram MORE predictable than matched Bukhārī.** Consistent with
  H-NEW-25's corpus-level finding at trigram resolution; confirmed here at bigram
  resolution with paired length-matched Bukhārī segments.
- **SECONDARY FAIL**: muq vs non-muq residual H(L2|L1): Δ=−0.095 bits (muq LOWER
  residual = more-predictable-for-its-length), MWU z=−2.14, p=0.032 — nominally
  significant but does NOT clear α_bon=0.025.
- **MW-5 PASS**: shuffled Quran H_cond = 3.590 vs unshuffled 3.164, Δ=+0.425 bits
  (shuffling destroys the conditional structure as required).

## Distribution summary

| Corpus | N units | Mean H(L2\|L1) | SD | Min | Max |
|---|---:|---:|---:|---:|---:|
| Quran (114 surahs) | 114 | 3.164 | 0.743 | 1.110 | 3.926 |
| Bukhārī (top-114 bab-seg) | 114 | 3.618 | 0.133 | — | — |

Bukhārī variance is ≈30× smaller than Quran variance because we chose top-114
longest segments (high-N regime where H saturates); Quran surahs span 43 letters
(Q 108) to 26 249 letters (Q 2) so dominate the length axis. Length-regression:
H_cond = −0.054 + 1.049·log₁₀(N_bigrams), R² = 0.885.

## Top-5 lowest H_cond (RAW — most predictable)

| Rank | Q | Name | H_cond | N_letters | Residual |
|:-:|:-:|---|---:|---:|---:|
| 1 | 108 | al-Kawthar | 1.110 | 43 | −0.538 |
| 2 | 112 | al-Ikhlāṣ | 1.269 | 47 | −0.421 |
| 3 | 114 | al-Nās | 1.304 | 80 | −0.632 |
| 4 | 113 | al-Falaq | 1.419 | 73 | −0.475 |
| 5 | 109 | al-Kāfirūn | 1.518 | 99 | −0.517 |

All five are the SHORTEST creedal/protective surahs. Low raw H is length-driven
(tiny vocab in few tens of letters); confirmed by their negative residuals which
mean: **even for their tiny length they are MORE predictable than expected.**
Q 114 al-Nās has the most-negative residual (−0.632) of the entire corpus among
short surahs — its triple-iterated أعوذ / ملك / إله / الناس refrain dominates.

## Top-5 highest H_cond (RAW — most surprising)

| Rank | Q | Name | H_cond | N_letters | Residual |
|:-:|:-:|---|---:|---:|---:|
| 1 | 18 | al-Kahf | 3.926 | 6 552 | −0.024 |
| 2 | 17 | al-Isrāʾ | 3.920 | 6 643 | −0.036 |
| 3 | 20 | Ṭāhā | 3.891 | 5 399 | +0.030 |
| 4 | 7 | al-Aʿrāf | 3.881 | 14 435 | −0.428 |
| 5 | 12 | Yūsuf | 3.879 | 7 307 | −0.120 |

All long mid-Meccan narrative surahs. Raw-highest H is length-driven (more
letters → more bigram-diversity); residuals are near zero meaning these are
"as-expected-for-their-length".

## Top-5 highest RESIDUAL (surprising FOR THEIR LENGTH)

| Rank | Q | Name | H_cond | N_letters | Residual |
|:-:|:-:|---|---:|---:|---:|
| 1 | 74 | al-Muddaththir | 3.484 | 1 035 | +0.375 |
| 2 | 84 | al-Inshiqāq | 3.096 | 445 | +0.373 |
| 3 | 80 | ʿAbasa | 3.180 | 552 | +0.358 |
| 4 | 50 | Qāf | 3.627 | 1 507 | +0.348 |
| 5 | 68 | al-Qalam | 3.550 | 1 289 | +0.341 |

These are **Early-Meccan short oath / eschatological surahs** — Q 74
(2nd-revealed per Nöldeke), Q 68 (4th), Q 84, Q 80 (all Early Meccan); Q 50
(Middle Meccan muqaṭṭāʿ). Their high residual means they are LESS predictable
than a Bukhārī-like bab-segment of the same length: diverse topic-word
vocabulary per letter.

## Top-5 lowest RESIDUAL (predictable FOR THEIR LENGTH)

| Rank | Q | Name | H_cond | N_letters | Residual |
|:-:|:-:|---|---:|---:|---:|
| 1 | 2 | al-Baqara | 3.865 | 26 249 | −0.716 |
| 2 | 114 | al-Nās | 1.304 | 80 | −0.632 |
| 3 | 4 | al-Nisāʾ | 3.808 | 16 332 | −0.557 |
| 4 | 108 | al-Kawthar | 1.110 | 43 | −0.538 |
| 5 | 3 | Āl ʿImrān | 3.803 | 14 985 | −0.523 |

The longest Medinan surahs (Q 2, Q 4, Q 3) dominate low-residual — their
bigram-distribution is more concentrated than expected for their length,
consistent with their legal/narrative register's stereotyped formulas. Q 114
and Q 108 reappear from the raw list; their extreme refrain structure
out-predictables their length prediction.

## Descriptive correlations (residual vs covariates, n=93 ≥ 50 tokens)

| Covariate | Spearman ρ | p (nominal) |
|---|---:|---:|
| **α (Zipf, [[h-new-172-zipf-per-chapter|H-NEW-172]])** | **−0.740** | ≈ 0 |
| dispersion ([[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]) | +0.696 | ≈ 0 |
| Nöldeke order (early→late) | −0.492 | 1e−6 |
| β (Heap, [[h-new-159-heap-beta-per-chapter|H-NEW-159]]) | +0.400 | 7e−5 |
| muq vs non-muq (MWU z) | −2.14 | 0.032 |

**Strongest correlate: Zipf α, ρ = −0.740.** Surahs with steeper Zipf (α high;
concentrated high-freq word distribution) have LOWER bigram-entropy residuals
(more letter-level predictability); conversely surahs with flat Zipf (α low;
diverse vocabulary — Early Meccan short oath surahs) have HIGH residuals. The
magnitude is substantially larger than the α↔β partial correlation
(|ρ|=0.418) from [[h-new-178-alpha-beta-manifold|H-NEW-178]] — the bigram-entropy residual is a more direct
measure of token-level predictability than β, and it tracks α almost as well
as β does ([[h-new-178-alpha-beta-manifold|H-NEW-178]] ρ(α,β)=−0.883 raw).

Nöldeke direction is NEGATIVE: earlier-revealed surahs have higher residual
(less-predictable letter structure); this coincides with the Early-Meccan-is-
stylistically-rich finding (Q 74, Q 68, Q 84, Q 80 in top-5 residual).

## Muqaṭṭāʿat (secondary — FAIL)

| Group | N | Mean residual | MWU z | p |
|---|---:|---:|---:|---:|
| muq | 29 | −0.009 | | |
| non-muq | 64 | +0.086 | | |
| Δ | — | **−0.095** | −2.14 | 0.032 |

The muq effect on bigram-residual is WEAKER than on α-β-manifold residual
([[h-new-178-alpha-beta-manifold|H-NEW-178]], p=0.005). Direction is OPPOSITE to the [[h-new-178-alpha-beta-manifold|H-NEW-178]] finding: [[h-new-178-alpha-beta-manifold|H-NEW-178]]
showed muq residual +0.034 (HIGH on α-β manifold); here muq shows residual
−0.095 (LOW = more-predictable-for-length). These are different residuals
(α-β vs length-only on H_cond) so not directly contradictory, but the signal
weakens at bigram resolution and does not clear α_bon=0.025. **Partial-pass
only; not a new positive axis for muq.**

## MW-5 control

Shuffled-letter Quran gives H_cond = 3.590 bits; unshuffled = 3.164. Δ = +0.425
bits above threshold of 0.1 bits. Instrument valid — conditional bigram
structure is destroyed by shuffling, as expected.

## Interpretation

1. **Quran < Bukhārī bigram-entropy is REAL and length-matched** — the
   paired-Wilcoxon test (each of the 114 largest Bukhārī bab-segments paired
   by rank-length with a Quran surah) gives z=−6.84, p≈0. Quran is letter-
   bigram-structurally MORE constrained than hadith prose. Confirms H-NEW-25's
   trigram result at bigram resolution with paired length-control (not just
   corpus-level aggregation).

2. **Length-residual bigram-entropy is dominated by α** (ρ=−0.74) — surahs
   with steep Zipf slopes (few very-frequent words) have predictable bigrams;
   flat-Zipf Early Meccan surahs (al-Muddaththir, al-Inshiqāq, ʿAbasa, Qāf,
   al-Qalam) have surprising bigrams. This is a NEW finding — previous
   per-surah bigram/trigram entropy work was not length-controlled.

3. **Muqaṭṭāʿat do NOT distinguish at bigram-residual level** (p=0.032, fails
   Bonferroni). The α-β manifold axis ([[h-new-178-alpha-beta-manifold|H-NEW-178]]) was stronger (p=0.005).
   Bigram entropy alone is not a better muq-discriminator than (α,β).

4. Early-Meccan / late-Medinan contrast in residual direction (ρ=−0.49
   Nöldeke) is consistent with the broader narrative that Early-Meccan short
   oath surahs are stylistically rich per letter while Medinan legal surahs
   are more-stereotyped per letter.

## Caveats

- Bukhārī baseline uses top-114 longest bab-segments (letter-count matched
  coarse); paired-Wilcoxon addresses finer length-control.
- 29 muq surahs include both long narrative muq (Q 2 al-Baqara — very low
  residual) and short muq (Q 50 Qāf — very high residual); the muq group is
  heterogeneous and the MWU test may under-detect a real effect against a
  mixed-direction signal.
- Cross-verse bigrams are used (verse-boundary pauses NOT treated as resets);
  sensitivity to this choice not computed (flagged for future).
- The five correlations are descriptive, NOT Bonferroni-corrected among
  themselves (k=2 pre-reg only for primary/secondary).

## Status

- Primary verdict: **PASS** (Quran < Bukhārī, Welch p ≈ 0, three tests agree).
- Secondary verdict: **FAIL** (muq-residual p=0.032 does not clear α_bon=0.025).
- MW-5: **PASS**.
- Overall: **PARTIAL-PASS**.
