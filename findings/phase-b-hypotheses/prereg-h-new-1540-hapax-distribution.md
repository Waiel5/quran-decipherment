---
id: H-NEW-1540
title: Hapax-legomenon (corpus-singleton roots) distribution across 114 surahs
date_locked: 2026-05-09
phase: B
status: pre-registered
seed: 20260509
n_perm: 10000
---

# H-NEW-1540 — Pre-registration

## Hypothesis (DIRECTION-LOCKED before observation)

**H1 (primary)**: The distribution of hapax-legomenon root-tokens across the 114 surahs is significantly NON-UNIFORM relative to a length-proportional null. Specifically, hapax-density (hapax-tokens / surah-word-count) deviates from corpus baseline such that the observed *coefficient of variation* (CV) and *max-density* statistics LIE IN THE UPPER TAIL of a length-proportional permutation null.

**H2 (directional cell)**: At least 3 surahs have hapax-density ≥ 2 × length-weighted corpus baseline.

Direction: CV(observed) ≥ CV(null) (one-tailed upper); max-density(observed) ≥ max-density(null) (one-tailed upper); count of surahs with density ≥ 2× baseline ≥ 3.

## Theoretical motivation

A hapax legomenon is a root appearing exactly once in the corpus. They are the most-specific lexical fingerprints — any surah carrying a hapax bears a unique semantic marker. Classical rhetorical tradition treats hapaxes as a sub-class of iʿjāz markers:

- **al-Suyūṭī**, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 39 (*al-gharīb*, "the rare/unusual"), catalogues lexical rarities surah-by-surah and treats them as a separate scholarly discipline. He devotes nawʿ 38 to *al-mufradāt* (singletons) — words used only once — explicitly arguing that their irreducibility is part of the corpus's stylistic precision.
- **al-Bāqillānī**, *Iʿjāz al-Qurʾān*, on the *balāgha*-axis of iʿjāz, identifies precise word-choice (including hapaxes that resist substitution) as evidence of inimitability.

If the corpus is uniform in lexical novelty, hapaxes should distribute proportional to surah length. If certain surahs (e.g., narrative surahs introducing foreign vocabulary, or short eschatological surahs with idiosyncratic vocabulary) carry hapaxes far above the length-proportional expectation, the distribution is "lumpy" — a measurable architectural property.

## Pre-committed measurement protocol

- Tashkeel: no-tashkeel (rules-tuple §1.4 default).
- Token: QAC stem-root (per H-NEW-111 and `data/morphology/root-index.json`).
- Surah word-count denominator: orthographic-token count from `quran-text/quran-no-tashkeel.json` (split on whitespace).
- Reading: Hafs-Kufan.
- Basmala: counted only in Q 1 (the Q 1 word-count denominator already includes its basmala; for Q 2-114, the basmala is NOT included in the published text in `quran-no-tashkeel.json` as a separate verse — it is paratextual; if present as verse 0/header, it is excluded).
- Hapax set: roots with exactly 1 attestation in `root-index.json`.

**Per-surah statistics**:
- `hapax_count(s)` = number of hapax-root tokens in surah s (each hapax is a single attestation by definition; sum over hapax set).
- `word_count(s)` = orthographic word count of surah s.
- `hapax_density(s)` = `hapax_count(s) / word_count(s)`.
- `baseline = sum(hapax_count) / sum(word_count)` (length-weighted corpus average).
- `ratio(s) = hapax_density(s) / baseline`.

**Corpus-wide statistics**:
- `obs_CV` = stddev(density) / mean(density) across 114 surahs.
- `obs_max_density` = max over 114 surahs of hapax_density(s).
- `obs_n_above_2x` = count of surahs with `ratio(s) ≥ 2.0`.

## Null distribution

Length-proportional permutation: randomly redistribute the |H| hapax-tokens across the 114 surahs, where each surah s receives tokens with probability `word_count(s) / sum(word_count)`. 10,000 permutations, `random.Random(SEED=20260509)`.

For each perm:
- `null_CV[i]`, `null_max_density[i]`, `null_n_above_2x[i]`.

**p-values** (one-tailed upper):
- `p_CV = #{null_CV ≥ obs_CV} / 10000`
- `p_max = #{null_max_density ≥ obs_max_density} / 10000`
- `p_count = #{null_n_above_2x ≥ obs_n_above_2x} / 10000`

## Bonferroni correction

k = 3 cells (CV, max-density, count-above-2x).
α_corrected = 0.05 / 3 = **α_Bonf ≈ 0.0167**.

## MW protections

- **MW-1** (instrument-prior): root-index.json + word-count metric pre-specified.
- **MW-2** (corpus-prior): 10,000 length-proportional permutations.
- **MW-3** (alternative-models): two statistics (CV + max + count) reported jointly; equal-probability null reported as ablation.
- **MW-4** (over-fitting): no fitted parameters; threshold ratio = 2.0 fixed pre-observation.
- **MW-5** (replication): also report an equal-probability null (each surah equiprobable, independent of word count) as a sensitivity check. NOT used for the primary verdict.
- **MW-6** (instrument-control): the null treats all 114 surahs as the same population; no surah-class selection.
- **MW-7** (post-hoc cap): top-10 and bottom-10 rankings are descriptive; their clustering interpretation is post-hoc and capped at descriptive-only.

## Verdicts

| Outcome | Cells | Verdict |
|:--|:--|:--|
| All 3 cells p ≤ α_Bonf and obs_n_above_2x ≥ 3 | ✓ | PASS-DIRECTED |
| 2 of 3 cells p ≤ α_Bonf | partial | PARTIAL |
| 1 of 3 cells p ≤ α_Bonf | partial | DESCRIPTIVE-ONLY |
| 0 cells significant | — | NULL |
| obs_CV < null mean (reverse direction) | — | NULL with explicit pre-commit reverse-direction note |

## Pre-commit violations and stop conditions

- If observed CV is BELOW null-mean: pre-commit violation → published as NULL with explicit reverse-direction note.
- If observed max-density is BELOW null-mean: pre-commit violation flag.
- Direction is locked one-tailed upper across all three cells.

## Constants

```
SEED   = 20260509
N_PERM = 10_000
RATIO_THRESHOLD = 2.0
```

## Data dependencies

- `/Users/grey/Downloads/quran/data/morphology/root-index.json` — root → list of [surah, verse, word-position]
- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` — per-surah orthographic word count

## Output schema

`findings/phase-b-hypotheses/csv/h-new-1540.json`:
```
{
  "id": "H-NEW-1540",
  "title": "...",
  "prereg_sha": "<computed at runtime>",
  "seed": 20260509,
  "n_perm": 10000,
  "n_hapax_roots": int,
  "n_hapax_tokens": int,
  "baseline_density": float,
  "obs_CV": float,
  "obs_max_density": float,
  "obs_max_surah": int,
  "obs_n_above_2x": int,
  "cell_CV":    {"p": ..., "null_mean": ..., "null_p95": ..., "pass": bool},
  "cell_max":   {"p": ..., "null_mean": ..., "null_p95": ..., "pass": bool},
  "cell_count": {"p": ..., "null_mean": ..., "null_p95": ..., "pass": bool},
  "per_surah": [{"s": int, "word_count": int, "hapax_count": int, "density": float, "ratio": float}, ...],
  "top10_by_density": [...],
  "bottom10_by_density": [...],
  "verdict": "...",
  "alpha_bonf": 0.0167
}
```

## Honest limits

1. **Root-level hapax ≠ word-form hapax**: a hapax-root may surface as multiple inflected word-forms in principle, but by root-index.json's count=1 definition we are picking roots attested exactly once in the corpus. This is the QAC-stem-root sense of "hapax."
2. **QAC coverage**: not every word in the corpus has a QAC root assignment (particles, proper nouns, some loanwords may have no root or a special tag). Hapax counts are over the assigned-root subset. The denominator (word-count) is total orthographic words, so density is intentionally a hapax-tokens-per-total-words ratio, NOT a per-rooted-word ratio. This is conservative: it dilutes density uniformly.
3. **Length-proportional null**: this is the appropriate null because longer surahs mechanically have more opportunities for hapaxes. The equal-probability null is supplied as a sensitivity check, NOT the primary test.
4. **Top-10 cluster interpretation**: any thematic / chronological pattern in the top-10 is post-hoc and reported descriptively only (MW-7 cap).
5. **Hapax "loanword" interpretation**: many corpus-rare words in the Quran are loanwords from Aramaic, Hebrew, Ethiopic, Persian, Greek (per Jeffery 1938). A thematic cluster in the top-10 may simply track narrative surahs introducing foreign material. This is a real finding if observed but does NOT prove "iʿjāz" — it documents lexical-novelty distribution.

*Locked 2026-05-09. Direction one-tailed upper across 3 cells. SHA to be computed and embedded post-write.*
