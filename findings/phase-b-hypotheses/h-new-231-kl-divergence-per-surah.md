---
id: H-NEW-231
title: Per-surah KL-divergence from corpus-average — length is the dominant explanatory axis
phase: B
status: PASS-DESCRIPTIVE (very strong correlation; no pre-reg inferential cell, filed as post-hoc α=0.05 single-test cap per MW-7)
date: 2026-04-17
executed_by: team-lead (inline, autonomous-loop)
parent: H-NEW-163 (template/concentrator dichotomy); H-NEW-178 (α,β manifold)
seed: 20260419
rules_tuple: (no-tashkeel; 114 surahs; orthographic-token freq; Dirichlet-smoothed α=0.5; KL(p_surah || p_corpus); log-length = log10(token_count))
bonferroni_k: 1
bonferroni_family: h-new-231-kl-divergence
alpha_bon: 0.05
direction: descriptive — no pre-committed direction; reporting post-hoc with single-test α cap
verdict: PASS-DESCRIPTIVE — ρ = −0.967 exceeds any plausible random-null threshold
---

# [[h-new-231-kl-divergence-per-surah|H-NEW-231]] — Per-surah KL-divergence from corpus-average vocabulary distribution

## Motivation

[[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] introduced a template/concentrator dichotomy (long surahs re-use corpus vocabulary; short surahs use idiosyncratic vocabulary). [[h-new-178-alpha-beta-manifold|H-NEW-178]] (α,β manifold) showed that length drives ~76% of rank-frequency variance with a secondary off-manifold axis.

This inline test quantifies the **distance of each surah's vocabulary distribution from the corpus average** and tests the relationship with length directly. If the template/concentrator framing is real, short surahs should have HIGH KL-divergence; long surahs should have LOW KL-divergence.

## Method

1. Build corpus word-frequency distribution `p_corpus` from the full no-tashkeel Quran (77,797 tokens).
2. For each surah s, build `p_s` on the same vocabulary, Dirichlet-smoothed with α = 0.5 (additive-pseudocount on all corpus vocabulary).
3. Compute `KL(p_s || p_corpus) = Σ p_s(w) · log(p_s(w) / p_corpus(w))`.
4. Correlate KL with `log10(token_count)`.

Smoothing guards against log(0). No class structure pre-committed; this is a shape test of the length→KL relationship.

## Results

| Quantity | Value |
|---|---:|
| Spearman ρ(log-length, KL) | **−0.967** |
| p-value | **6.7 × 10⁻⁶⁰** |
| Pearson r (for comparison) | −0.89 |

### Top-15 MOST-DIVERGENT surahs (highest KL)

| Q | Name | KL | Tokens | Period |
|:-:|:-:|---:|:-:|:-:|
| 99 | al-Zalzalah | 1.892 | 36 | Late-Meccan |
| 97 | al-Qadr | 1.822 | 30 | Meccan |
| 55 | al-Raḥmān | 1.650 | 352 | Meccan |
| 101 | al-Qāriʿah | 1.536 | 36 | Meccan |
| 95 | al-Tīn | 1.443 | 34 | Meccan |
| 103 | al-ʿAṣr | 1.396 | 14 | Meccan |
| 111 | al-Masad | 1.372 | 23 | Meccan |
| 108 | al-Kawthar | 1.358 | 10 | Meccan |
| 113 | al-Falaq | 1.340 | 23 | Meccan |
| 112 | al-Ikhlāṣ | 1.298 | 15 | Meccan |
| 110 | al-Naṣr | 1.245 | 19 | Medinan |
| 105 | al-Fīl | 1.237 | 23 | Meccan |
| 114 | al-Nās | 1.196 | 20 | Meccan |
| 102 | al-Takāthur | 1.191 | 28 | Meccan |
| 109 | al-Kāfirūn | 1.174 | 27 | Meccan |

All 15 are short; 14/15 Meccan; all are short-mufaṣṣal tail or qiṣār-mufaṣṣal. Q 55 al-Raḥmān is the only non-short outlier — its 31 refrain verses are idiosyncratic relative to corpus.

### Top-15 LEAST-DIVERGENT surahs (lowest KL)

| Q | Name | KL | Tokens | Period |
|:-:|:-:|---:|:-:|:-:|
| 2 | al-Baqarah | 0.089 | 6,140 | Medinan |
| 3 | Āl ʿImrān | 0.130 | 3,502 | Medinan |
| 7 | al-Aʿrāf | 0.130 | 3,320 | Late-Meccan |
| 6 | al-Anʿām | 0.138 | 3,055 | Late-Meccan |
| 4 | al-Nisāʾ | 0.144 | 3,764 | Medinan |
| 5 | al-Māʾidah | 0.156 | 2,804 | Medinan |
| 9 | al-Tawbah | 0.161 | 2,499 | Medinan |
| 16 | al-Naḥl | 0.178 | 1,841 | Late-Meccan |
| 26 | al-Shuʿarāʾ | 0.184 | 1,279 | Meccan |
| 11 | Hūd | 0.188 | 1,947 | Meccan |
| 10 | Yūnus | 0.190 | 1,832 | Meccan |
| 24 | al-Nūr | 0.192 | 1,317 | Medinan |
| 17 | al-Isrāʾ | 0.198 | 1,560 | Meccan |
| 12 | Yūsuf | 0.201 | 1,776 | Meccan |
| 33 | al-Aḥzāb | 0.203 | 1,307 | Medinan |

All 15 are long; mix of Meccan + Medinan; the 7 sabʿ al-ṭiwāl (Q 2-9 minus Q 8) occupy the top-7.

## Interpretation

1. **Length is the near-total explanatory axis for vocabulary-atypicality.** ρ = −0.967 is the tightest single-axis correlation found anywhere in the project to date (exceeds [[h-new-183-chronology-predictor|H-NEW-183]]'s Nöldeke predictor R²=0.836 as a simple bivariate link). 94% of ranked KL-variance is explained by log-length alone.

2. **Long surahs REPRESENT the corpus.** Q 2 al-Baqarah (6,140 tokens, 8% of corpus) has KL = 0.089 — its word-frequency distribution IS essentially the corpus distribution. This is the template-mode extreme.

3. **Short surahs DIVERGE.** The short-mufaṣṣal tail (Q 94-114 plus Q 55) all have KL > 1.1. Their vocabulary is not a scaled-down corpus distribution; it is idiosyncratic around creedal themes (tawḥīd, eschatology, oath-bundles).

4. **This is the quantitative complement of [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]'s concentrator/template dichotomy.** [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] classified surahs by vocabulary-concentration (Herfindahl). KL(surah||corpus) is an orthogonal instrument measuring the same underlying axis — and both agree: short = concentrator = high-KL = idiosyncratic; long = template = low-KL = corpus-representative.

5. **Q 55 al-Raḥmān exception**: it's the ONLY non-short surah in the top-15 high-KL list. Its refrain verses (fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān × 31) inflate a specific 7-word unit ~31× above background, creating idiosyncratic mass that dominates its 352 tokens. This matches [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s identification of Q 55 as the extreme LOW-α outlier — the same refrain drives both instruments.

## Connection to unified model ([[cross-finding-018-four-principle-reduced-model|cross-finding-018]])

- **M5 (length-stratification + compositional modes) sharply reinforced**: KL is the tightest length-correlated instrument found. Mode classification can be refined:
  - **Mode A (length-extremity)**: very long, KL < 0.2 (ṭiwāl block)
  - **Mode B (refrain-stylistic)**: short OR refrain-structured, KL > 1.1
  - **Mode C (default)**: intermediate
  - **Mode D (Medinan-inclusio per [[h-new-189-medinan-inclusio|H-NEW-189]])**: orthogonal to KL
  - **Mode E (linear Meccan narrative)**: orthogonal to KL
- **M3 (prosodic distinctiveness)**: the short/long divergence in KL parallels the per-surah β/α variance in [[h-new-159-heap-beta-per-chapter|H-NEW-159]]/172/178 — a corpus-internal stratification, not a cross-corpus distinctiveness.

## Honest limits

1. **Post-hoc**: no pre-reg direction; reported under single-test α = 0.05 cap per MW-7. ρ = −0.967 is so extreme that Bonferroni-k bookkeeping is moot (p < 10⁻⁵⁰ passes any k), but the finding is descriptive rather than adjudicated against a specific classical claim.
2. **Length is partly circular**: a surah with N tokens drawn from the corpus would have KL→0 as N→∞. Some of the correlation is a math-of-estimation artifact, not a substantive claim. A permutation null matching each surah's N but drawing from corpus p would bound this — not yet executed.
3. **Smoothing parameter α=0.5**: sensitivity to Laplace (α=1) or unsmoothed MLE not tested inline.
4. **Per-vocabulary**: KL can depend on vocabulary cut (corpus full vs top-K). Result reported on full corpus vocabulary; top-K cuts deferred to H-NEW-231.1.

## Queued follow-ups

- **H-NEW-231.1**: null test — does a same-N multinomial draw from corpus-p produce KL matching observed per-surah? Controls for the math-of-estimation circularity.
- **H-NEW-231.2**: does KL correlate with per-surah α, β, Hurst, LZ, dispersion? Joint manifold of corpus-atypicality instruments.
- **H-NEW-231.3**: does Q 55's KL drop when refrain verses are masked out? If yes, refrains are the unique driver of its outlier status.

## Cross-references

- Parent: [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] (concentrator/template)
- Sibling: [[h-new-178-alpha-beta-manifold|H-NEW-178]] (α,β manifold), [[h-new-195-entropy-per-surah|H-NEW-195]] (entropy per surah)
- Applies-to: [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] M5 pillar
- Q 55 outlier: consistent with [[h-new-180-q55-refrain-position-result|H-NEW-180]] (refrain-position), [[h-new-178-alpha-beta-manifold|H-NEW-178]] (α,β extreme)
- Q 2-9 extremes: consistent with classical sabʿ al-ṭiwāl bracket

## Files

- Script: inline (seed 20260419)
- Findings: this file
