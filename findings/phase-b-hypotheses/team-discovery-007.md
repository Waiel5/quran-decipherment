---
finding_id: H-NEW-11
title: Prophet-vocabulary suppression is pan-prophetic (no single prophet drives the below-null signal); ranking is length-correlated (Spearman ρ=+0.79) but not length-explained
rules_tuple: (no-tashkeel, lemma (root layer QAC v0.4), graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
null_model: §1.2 pericope-label-shuffle length-preserving (500 perms per leave-one-out cell)
date: 2026-04-13
acceptance_criterion: (i) leave-one-out: does dropping any single prophet eliminate the below-null signal (i.e. obs ≥ null_mean after drop)? (ii) length artifact: is Spearman ρ(tokens, mean-Jaccard) > 0.9 (= length fully explains ranking)?
verdict: DEEPENS prior finding — suppression is PAN-PROPHETIC; length is a strong but incomplete explainer
---

# [[h-new-11-ext-methodological-null|H-NEW-11]] — Which prophets drive the vocabulary-suppression signal?

## Background

Prior finding (`findings/phase-c-structures/prophet-vocabulary-overlap-matrix.md`): the 8 most-mentioned Quranic prophets (Moses, Jesus, Abraham, Noah, Joseph, John, Adam, Lot) have an aggregate cross-prophet mean Jaccard root-overlap of **0.3353**, which is *below* the length-preserving pericope-shuffle null 95% interval (0.3484, 0.3876), with one-sided p = 1.00. Prophet pericopes share *less* root vocabulary than random length-matched Quranic pericopes — i.e., there is measurable active vocabulary *specialization* across prophets.

This test deepens that single-point finding by asking: **which prophets drive it?**

## Method

Re-parse QAC v0.4. Apply the identical pericope clustering algorithm used in the prior finding (gap ≤ 3, pad ± 2 around proper-noun mentions). For each of the 8 prophets compute:
- Root-set Jaccard to each other prophet
- Mean Jaccard to the other 7 (a per-prophet "typicality" score)
- Total pericope-token count (a length measure)

**Length-artifact diagnostic.** Pearson and Spearman correlation of pericope-token-count vs mean-Jaccard-to-others. If |ρ| > 0.9, the ranking is entirely a length artifact.

**Leave-one-out.** For each prophet, drop them, recompute the 7×7 mean off-diagonal Jaccard, and re-run the length-preserving pericope-shuffle null on the reduced set (500 permutations per LOO cell, seed varied per drop).

## Results

### Per-prophet mean Jaccard to other 7

| Rank | Prophet | Mean Jaccard | Pericope tokens |
|---:|:---|---:|---:|
| 1 | Abraham | **0.4028** | 2,338 |
| 2 | Noah | 0.3917 | 1,797 |
| 3 | Jesus | 0.3718 | 1,384 |
| 4 | Moses | 0.3513 | **4,529** |
| 5 | Lot | 0.3339 | 756 |
| 6 | Adam | 0.3316 | 880 |
| 7 | Joseph | 0.2999 | 859 |
| 8 | John | 0.1992 | 218 |

### Length-artifact test

- **Pearson ρ(tokens, mean-Jaccard) = +0.519**
- **Spearman ρ(rank tokens, rank mean-Jaccard) = +0.786**

Length correlates with typicality-rank but does not fully explain it. The two striking deviations:
- **Moses** has the *largest* pericope mass (4,529 tokens, nearly double Abraham's) but ranks only 4th in mean-Jaccard (0.351). Moses is *semantically specialized*, not template-central, despite being the Quran's most-retold prophet.
- **Abraham** (2,338 tokens, rank 3 in length) ranks **1st** in mean-Jaccard. Abraham is the template prophet even though he's not the most-mentioned — this survives the prior "Abraham-as-template" sub-claim.

### Leave-one-out analysis

Does dropping any single prophet eliminate the below-null (suppression) signal? If yes, that prophet is the "driver"; if no, suppression is pan-prophetic.

| Dropped | obs mean-Jaccard (7×7) | null mean | null sd | z | p(obs ≥ null) | obs − null_mean |
|:---|---:|---:|---:|---:|---:|---:|
| Moses | 0.3299 | 0.3655 | 0.0110 | **−3.23** | 1.000 | −0.0356 |
| Jesus | 0.3231 | 0.3585 | 0.0116 | **−3.05** | 0.998 | −0.0354 |
| Abraham | 0.3128 | 0.3534 | 0.0107 | **−3.80** | 1.000 | **−0.0407** |
| Noah | 0.3165 | 0.3556 | 0.0112 | **−3.50** | 1.000 | −0.0391 |
| Joseph | 0.3471 | 0.3753 | 0.0119 | **−2.37** | 0.992 | −0.0283 |
| John | 0.3807 | 0.4114 | 0.0090 | **−3.41** | 1.000 | −0.0307 |
| Adam | 0.3365 | 0.3667 | 0.0114 | **−2.65** | 0.992 | −0.0302 |
| Lot | 0.3357 | 0.3634 | 0.0118 | **−2.35** | 0.994 | −0.0276 |

**Every single drop keeps the suppression signal alive** at z between −2.35 and −3.80. No prophet, when removed, eliminates the below-null outcome. The strongest single contributor is Abraham (obs − null = −0.041), but the signal is not *Abraham-driven* — it's *everywhere-distributed*.

## Verdict

**DEEPENS prior finding.** The sub-hypothesis "vocabulary suppression is driven by a few prophets" is **refuted**. Suppression is pan-prophetic: every prophet's pericope is, on net, less vocabulary-shared with its peers than length-matched random pericopes would produce.

The secondary finding — length-artifact test — is **partially but not fully explanatory**. Spearman ρ = +0.79 between pericope-token-count and mean-Jaccard ranking is high (big pericopes cover more roots, so by set theory share more). But Pearson ρ = +0.52 shows the linear relationship is weak, and Moses (the largest pericope mass) sits at rank 4. Moses's mass is *linguistically specialized* into Moses-distinctive roots rather than shared template roots.

## Interpretation

Three readings, consistent with the data:

1. **Hagiographic specialization.** Each prophet pericope is linguistically scaffolded by roots specific to that prophet's story arc — wolves and robes for Joseph, deluge-vocabulary for Noah, Pharaoh/staff/magicians for Moses. The Quran actively *particularizes* the shared theological template (warner + rejection + deliverance) through prophet-specific lexical color. This is not "shared template → shared lexicon" but rather "shared template → prophet-specific lexicon."

2. **Moses as the specialized giant.** Moses's position — largest pericope mass but rank-4 mean-Jaccard — is specifically interesting. Moses alone among the prophets has a sui-generis technical vocabulary (rod, magicians, covenant-tablets, manna, quail, twelve-tribes, etc.) that the other prophet pericopes do not draw from. Moses is a lexically *closed* pericope.

3. **Pan-prophetic "particularization" is not a length artifact.** If it were, leave-one-out on John (the smallest, 218 tokens, lowest mean-Jaccard 0.20) would collapse the signal; it does not. The suppression persists at z = −3.41 even without John. The below-null phenomenon is a property of the *matrix of 8*, not of any one outlier.

## Classical anchor

This result supports al-Suyūṭī's treatment of *qiṣaṣ al-anbiyāʾ* (Itqān nawʿ 65) not as *tikrār bi-lā fāʾida* (repetition without benefit) but as *taksīr al-qiṣṣa al-wāḥida ʿalā wujūh* (shattering one story into facets). Each prophet retelling selects a distinct slice of the shared template. The Quran's qiṣaṣ system is **specialization-preserving**, not template-preserving — classical scholars called this *badaʾiʿ al-qaṣaṣ* (marvels of narrative variation), now operationally defined at root level.

## Garden of forking paths

- **Leave-one-out seed variance**: each LOO cell uses a deterministic seed derived from hash(prophet_name + 'seed'); 500 perms per cell. A larger n would tighten the σ estimates by ~√2 but would not change any verdict.
- **Pericope clustering parameters**: gap=3 pad=2 inherited from prior finding for lineage consistency. Robust alternatives (gap=5 pad=5, gap=2 pad=0) were explored in the prior finding and did not reverse the below-null direction; not re-checked here because the sub-hypothesis is about *per-prophet* contribution, not aggregate.
- **Length covariate modeling**: I report only ρ. A regression controlling for pericope length did not change the LOO verdict qualitatively; included for completeness in result JSON but not headline.

## Output files

- `scratch/team-discovery/h_new_11_prophet_deepening.py` — script.
- `scratch/team-discovery/result_h_new_11.json` — per-prophet + LOO + correlations.
