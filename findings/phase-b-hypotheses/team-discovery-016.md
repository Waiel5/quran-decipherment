---
finding_id: team-discovery-016
phase: B
status: NULL (Quran not distinctive); SIDE-FINDING (Bukhari is the outlier)
date: 2026-04-12
rules_tuple: (no-tashkeel, graphemes, no-spaces, alif/ya variants normalized)
null_model: 5 matched-Arabic baseline corpora (Bukhari, Sīra, Jāḥiẓ, Mutanabbī, Muʿallaqāt)
pre_registration_reference: task #20 in quran-discovery-team task-list
bonferroni_k: 24
alpha_bon: 0.00208
hypothesis_origin: pure novelty (H-NEW-13, computational-tester origination)
related_findings:
  - none direct; complements the letter-frequency unigram tests
---

# H-NEW-13 — Letter-bigram transition-matrix spectrum

## Executive verdict

**NULL on the Quran-distinctiveness hypothesis.** The Quran's bigram
transition matrix spectrum sits INSIDE the variation range of classical
Arabic prose and poetry. No distinctive signature at bigram-Markov
spectral level beyond unigram letter-frequency.

**Unpre-registered side-finding: Bukhari is the outlier.** Bukhari's
|λ_2| = 0.265 is 50% larger than Quran's 0.175 and larger than any
other corpus tested. Bukhari's bigram chain mixes slowly; every other
corpus (including Quran) is in the 0.15-0.18 band.

## Measurements (6 corpora, 30-letter alphabet, Laplace-smoothed)

| corpus | n_chars | \|λ_2\| | spectral gap | H rate (bits/step) |
|---|---:|---:|---:|---:|
| quran | 330,709 | **0.175** | 0.825 | 3.756 |
| bukhari | 2,056,880 | **0.265** | 0.735 | 3.743 |
| sira | 1,090,188 | 0.154 | 0.846 | 3.819 |
| jahiz | 1,422,374 | 0.179 | 0.821 | 3.888 |
| mutanabbi | 34,549 | 0.170 | 0.830 | 3.940 |
| muallaqat | 38,083 | 0.177 | 0.823 | 3.864 |

## Comparisons (Quran vs baseline)

| baseline | Δ\|λ_2\| | Δ gap | Δ H | L1(π, π_Q) |
|---|---:|---:|---:|---:|
| bukhari | -0.089 | +0.089 | +0.013 | 0.214 |
| sira | +0.022 | -0.022 | -0.063 | 0.187 |
| jahiz | -0.004 | +0.004 | -0.132 | 0.131 |
| mutanabbi | +0.005 | -0.005 | -0.184 | 0.172 |
| muallaqat | -0.001 | +0.001 | -0.108 | 0.416* |

*Muʿallaqāt L1 is inflated by preserved tatweel character ـ (0.18 L1 contribution); 
core-letter L1 is ~0.23.

## Observed vs pre-registered criteria

| Test | Criterion | Observed | Verdict |
|---|---|---|---|
| (a) Quran \|λ_2\| distinctively smaller | Δ < -0.03 vs all baselines | Δ ∈ [-0.089, +0.022]; not uniform | **FAIL** |
| (b) Quran entropy rate distinctive | Δ > +0.05 vs all baselines | Δ ∈ [-0.184, +0.013]; Quran is LOWEST | **FAIL** |
| (c) Stationary distribution distinctive | L1 > 0.25 vs all baselines | L1 ∈ [0.13, 0.42]; only Muʿallaqāt > 0.25 | **FAIL** |
| (d) Spectral gap distinctive | Δ > +0.03 vs all baselines | Δ ∈ [-0.022, +0.089]; not uniform | **FAIL** |

No pre-registered criterion satisfied across all five baselines.

## Side-finding: Bukhari's slow-mixing bigram chain

Unpre-registered but striking: Bukhari's |λ_2| = 0.265 is 48% larger
than the mean of the other 5 corpora (0.178). This is ~2.5x the
cross-corpus SD (which is ~0.01 excluding Bukhari).

Plausible explanations:
1. **Formulaic ḥadīth isnād repetition**: "ḥaddathanā X qāla ḥaddathanā Y qāla..."
   produces heavy long-range bigram dependence (certain letter sequences
   highly predict next letters in the chain).
2. **Larger corpus**: with 2M chars Bukhari's matrix is less noisy, but
   more observation is expected to *tighten* eigenvalue estimates, not
   shift them systematically. So size alone doesn't explain it.
3. **Genre-specific phonotactic patterns**: ḥadīth narrative register
   has distinctive repetitive structures.

This side-finding could motivate a pre-registered H-NEW-13.1 test:
*ḥadīth-register bigram-chain slow-mixing is distinctive across
other ḥadīth collections (Muslim, Tirmidhī, etc.)*.

## Interpretation

**For the Quran distinctiveness hypothesis: negative.** At bigram-Markov
spectrum level, the Quran shares its dynamics with classical Arabic
poetry (Mutanabbī, Muʿallaqāt) and secular prose (Jāḥiẓ). This is
consistent with the prior letter-frequency finding being about
*unigram* distinctiveness, not about *chain dynamics*.

**For the Arabic prose-vs-poetry question: a new axis.** The
|λ_2| values cluster 0.15-0.18 for 5 of 6 corpora, with Bukhari
(ḥadīth) at 0.27. Ḥadīth prose is the outlier, not Qurʾān.

## Garden of forking paths (disclosed)

- Alphabet normalization: أ/إ/آ/ٱ → ا, ى → ي, ة → ه. Chosen pre-data.
- Tatweel ـ (U+0640) NOT filtered from Muʿallaqāt raw text — shows up
  as a large stationary-distribution component in that corpus only.
  This is why Muʿallaqāt L1 is 0.42; the meaningful L1 is ~0.23.
- Laplace smoothing α=0.1, not varied.
- Power-iteration for λ_2 with 500 iterations; tested for convergence.
- Stationary distribution from left-eigenvector power iteration, 1000 iters.
- No letter-frequency test repeated (unigram already studied elsewhere).

## Limits

1. **Eigenvalue approximation**: manual power iteration computes |λ_2|
   via deflation Q = P - 1π. For non-symmetric Markov chains this is
   correct for the second-largest-magnitude eigenvalue, but may miss
   a complex-conjugate pair with same magnitude. NumPy's full
   eigendecomposition would be more robust.
2. **No statistical significance test** on the |λ_2| differences —
   effect sizes reported but no null distribution built.
   Bootstrap-resample over characters would provide CIs.
3. **Char-level only**: a word-level or morpheme-level transition
   matrix could show different distinctiveness patterns.
4. **Corpus-size asymmetry**: Bukhari 2M chars vs Mutanabbī 35K chars.
   Small corpora have higher eigenvalue variance.

## Reproducibility

Script: `scratch/team-discovery/h_bigram_spectrum.py`
Result JSON: `scratch/team-discovery/result-bigram-spectrum.json`
Seed: 20260413
Runtime: 3.03s CPU on 2026-04-12

## Classical significance

ʿIlm al-ḥarf-adjacent theorists (e.g., Ikhwān al-Ṣafāʾ, Ibn ʿArabī)
posited that the Qurʾān has distinctive letter-level mathematical
structure. This finding adds bigram-Markov spectrum to the list of
levels at which the distinctiveness fails to appear. Letter frequency
is distinctive; bigram transition dynamics are not.

The Bukhari side-finding is independently interesting: isnād-formulaic
repetition creates measurable slow-mixing in bigram chains. This is a
testable hypothesis about register-specific Arabic phonotactics.
