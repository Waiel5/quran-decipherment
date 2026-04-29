---
id: H-NEW-182
title: Phonological feature vectors per surah — cluster structure and period/muq correlation
status: PRE-REGISTERED (locked before any vector, cluster label, silhouette, or ROC-AUC viewed)
registered: 2026-04-17
spec_locked_at: 2026-04-17
bonferroni_family: h-new-182-phonological-vectors
bonferroni_k: 3
alpha_bon: 0.01667
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
baselines:
  - data/baseline-corpora/raw/matched-bukhari-77k.txt
seed: 20260419
---

# [[h-new-182-phonological-vectors|H-NEW-182]] — Phonological feature vectors per surah

## Question

Classical Arabic tajwīd / phonology organizes letters along several orthogonal axes:
place of articulation (makhraj), voicing (hams/jahr), emphatic (tafkhīm), manner
(stop/fricative/nasal/etc.), continuant, pharyngealization. If we encode each surah
as the mean phonological-feature vector of its body-letters, does the resulting
114-row design matrix reveal structure? Specifically:

1. Is there nontrivial cluster structure (silhouette > 0)?
2. Do clusters correlate with Meccan vs Medinan?
3. Do clusters separate the 29 muqaṭṭaʿāt surahs from the 85 non-muq surahs?
4. Is the Quran's phonological distribution distinguishable from Bukhārī's
   (phonological-distance null)?

## Pre-committed test family (k = 3, α_per = 0.01667)

**Cell A — k-means silhouette**: fit k=4 k-means on the 114-surah phonological
matrix; observed silhouette must exceed the 95th-percentile of the label-shuffled
null (surah-body text shuffled across surahs, preserving total letter counts).
One-sided.

**Cell B — Meccan/Medinan ROC-AUC**: for a single phonological feature (locked:
fraction of emphatic letters) as a linear scorer, compute ROC-AUC for
Meccan-vs-Medinan classification (n=86 Meccan + 28 Medinan per the JSON `type`
field). Null: ROC-AUC = 0.5. One-sided p via permutation of labels (n = 10 000).

**Cell C — Bukhārī distinctness**: compute the Quran phonological feature vector
(aggregated over all 114 surah bodies, unweighted mean of surah-vectors) and the
Bukhārī vector (over the full noquran Bukhārī corpus), then the Euclidean
distance between them. One-sided p: fraction of bootstrap resamples (block-
bootstrap on Bukhārī tokens, block=100, n=1000) in which the observed Quran-vs-
Bukhārī distance is ≤ the Bukhārī self-resample internal distance. PASS if
Quran-vs-Bukhārī distance exceeds the 95th-percentile of Bukhārī's self-resample
distance distribution.

Bonferroni family = 3. α_Bonferroni = 0.05 / 3 = 0.01667 per cell.

## Phonological feature codebook — LOCKED (extends [[h-new-165-phonological-predictor|H-NEW-165]])

Per-letter binary features (6-dim):

- `labial`      ∈ {ب, ف, م, و}
- `alveolar`    ∈ {ت, د, ط, ز، س، ص، ض، ل، ن، ر}
- `palatal`     ∈ {ج، ش، ي}
- `velar`       ∈ {ك، ق}
- `pharyngeal`  ∈ {ع، ح، خ، غ}
- `glottal`     ∈ {ء، ه}
- `emphatic`    ∈ {ص، ض، ط، ظ}
- `voiced`      ∈ {ب، ج، د، ذ، ز، ض، ظ، ع، غ، ل، م، ن، ر، و، ي، ا}
- `continuant`  ∈ complement of stops {ب، ت، د، ط، ء، ك، ق، ج}

9-dimensional feature vector per surah: mean of per-letter one-hot over body text
(no-tashkeel). Letters not in any feature set contribute zero to that feature.
Spaces and non-Arabic glyphs are excluded before computing means.

## Method — LOCKED

1. **Corpus**: Quran no-tashkeel JSON. For each of 114 surahs, concatenate all
   verse `text` fields (basmala native to JSON for surah 1; verse 1 of sura 27
   contains basmala natively as verse 30). Strip anything not in
   U+0621..U+064A ∪ U+0671..U+06D3. NO stripping of alif variants — keep as
   written (mashriqi rule).
2. **Per-surah vector**: for each surah, compute the 9-d feature vector = mean
   of per-letter one-hot features over all Arabic letters in that surah body.
3. **Standardize**: z-score each feature column across 114 surahs.
4. **k-means**: n_clusters=4, random_state=20260419, n_init=10. Silhouette
   computed via `sklearn.metrics.silhouette_score` with metric="euclidean".
5. **Null for silhouette**: shuffle the z-scored row vectors, re-run k-means
   and silhouette 1000 times (seed 20260419 + i). p = (1 + #{null ≥ obs}) / 1001.
6. **Cell B**: Use raw (non-standardized) `emphatic` feature as scorer;
   `roc_auc_score(y = [type=="medinan"], score = emphatic_fraction)`. Direction:
   LOCKED. If ROC-AUC < 0.5, flip and report 1 - AUC with a flag; p is two-sided
   via label permutation. (Direction flip is allowed since the prereg does not
   claim a sign.)
7. **Cell C**: Bukhārī tokens from `bukhari-noquran.txt`, normalized same as
   Quran. Compute overall feature vector = mean over all letters. Quran-vector =
   mean over all letters in all 114 surahs (letter-weighted, not surah-weighted,
   to match Bukhārī). Distance = Euclidean on the 9-d raw (non-standardized)
   vectors. Null: 1000 block-bootstrap resamples of Bukhārī tokens (block=100
   characters-worth of tokens), recompute Bukhārī-vector, recompute distance to
   the FIXED Quran-vector; also compute 1000 Bukhārī-split-half self-distances.
   p = fraction of Bukhārī self-split distances ≥ observed Quran-Bukhārī
   distance.

## Positive control (MW-5)

Generate 114 "fake surahs" by uniformly IID sampling letters from a fixed 28-letter
alphabet (lengths matched to true surah lengths). Run the full pipeline. Expected:
silhouette near zero, ROC-AUC near 0.5, distance to Bukhārī near the Bukhārī
self-distance. If any expected sanity fails → NULL-BROKEN.

## Garden-of-forking-paths disclosure

- k=4 is LOCKED before viewing data (choice driven by the 4-way classical
  place-of-articulation grouping: front/mid/back/guttural).
- The 9-d feature set mirrors [[h-new-165-phonological-predictor|H-NEW-165]] per-letter codebook but uses binary
  place-of-articulation features rather than the 8-tier makhraj ordinal.
- Emphatic-letter fraction is the single locked scorer for Cell B; alternatives
  (pharyngeal fraction, voiced fraction) are NOT in the Bonferroni family and are
  EXPLORATORY only.
- Bukhārī distinctness uses the unweighted Euclidean distance. Mahalanobis or
  cosine alternatives are NOT in the Bonferroni family.
- Surah 9 has no basmala; surahs 1 + 27 have native basmala. These are facts of
  the Hafs Kufan mushaf, not project choices.

## Acceptance windows

- Cell A: PASS if silhouette > null 95th-percentile AND p_perm < 0.01667.
- Cell B: PASS if |AUC - 0.5| ≥ 0.10 AND two-sided permutation p < 0.01667.
- Cell C: PASS if Quran-Bukhārī distance > Bukhārī self-split 95th-percentile
  AND p < 0.01667.

## Verdict ceiling

PASS-DIRECTED under the H-NEW-N convention. Replication (if PASS) would require
an independent feature codebook (e.g., OpenAIR full-IPA) and independent
clustering algorithm (hierarchical Ward).
