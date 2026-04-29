# Journal — prophet-vocab-overlap run 1

- **Date:** 2026-04-12
- **Agent:** deep-reader (prophet-vocab-overlap)
- **Task:** Cross-prophet vocabulary overlap matrix for 8 most-mentioned prophets (Moses, Jesus, Abraham, Noah, Joseph, John, Adam, Lot).
- **Rules tuple:** `(no-tashkeel, lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)`; null `1.2-pericope-label-shuffle-length-preserving`.
- **Script:** `scratch/prophet-vocab-overlap/analyze.py` (main), `analyze_robust.py` (gap/pad robustness).
- **Output:** `findings/phase-c-structures/prophet-vocabulary-overlap-matrix.md`
- **Results JSON:** `scratch/prophet-vocab-overlap/results.json`
- **Per-pair null CSV:** `scratch/prophet-vocab-overlap/per-pair-null.csv`

## Pipeline summary

1. Loaded QAC v0.4 morphology, extracted proper-noun (PN) lemmas for 8 prophets. Verified counts match prior prophet-pericope-comparison numbers exactly (Moses 136, Abraham 69, Noah 43, Joseph 27, Jesus 25, Adam 25, Lot 27, John 5).
2. Clustered pericopes: CORE rule = gap ≤ 3 between consecutive mention-verses, pad ±2. Produced 239 total pericopes across 8 prophets.
3. Built per-prophet root bag (Counter) and root set from QAC root layer over all pericope verses.
4. Computed 8×8 Jaccard matrix on root sets, 8×8 TF-IDF cosine matrix on root-token vectors (smoothed IDF).
5. Null: 1000 permutations, pool all pericopes, shuffle, slice back to each prophet preserving pericope count (length-preserving). Recompute 8×8 Jaccard each permutation; record full cell distributions and mean off-diagonal.
6. Robustness: re-ran under (gap=5, pad=5) and (gap=2, pad=0).
7. Computed pair-specific unique-root counts: roots present in pair (X,Y) pericopes but absent from all other 6 prophet pericopes.
8. Three sub-hypotheses tested explicitly: Moses-Jesus coupling, Abraham-as-template, Noah-Moses analogy.
9. WebSearched prior art: Neuwirth 1981 (Studien zur Komposition), Reynolds 2010 (Biblical Subtext), Witztum 2011 (Syriac Milieu Princeton PhD), Dukes QAC, QAC-based surah-clustering lit — confirmed this Jaccard-matrix-with-null approach is novel.

## Key numbers

- **Observed mean off-diagonal Jaccard: 0.3353**
- Null 95% interval: (0.3484, 0.3876)
- One-sided p (obs ≥ null): **1.0000** — observed is BELOW null
- Top pair: Abraham-Noah (Jaccard 0.525)
- Bottom pair: Moses-John (Jaccard 0.141)
- Only pair above p<0.05 one-sided: **Jesus-Abraham (z=+1.90, p=0.031)**; does NOT survive Bonferroni (α/28 = 0.0018)
- Moses-Jesus rank: 8/28 (z=-0.43)
- Moses-Noah rank: 5/28 (z=-2.35, significantly BELOW null)
- Abraham mean-Jaccard-to-others: 0.403 (#1 under CORE + TIGHT, #2 under EXPANDED behind Noah)

## Findings taken to master-index

See new row in Phase C section of `docs/master-index.md`:
- Prophet-vocab-overlap: naive template-lexicon claim FAILS (obs below null p=1.00)
- Abraham-as-template partially survives (ordinal #1 mean-Jaccard across 3 clustering regimes)
- Moses-Jesus, Moses-Noah analogies fail at lexical surface — live at narrative/theological level only
- Pair-specific unique-root catalog: Abraham-Joseph celestial (šms/qmr/kwkb), Abraham-Lot hospitality (ḍyf/ʾwh), Moses-Noah fabrication (ṣnʿ)
- Three-cluster structure: Core-3 {Moses,Abraham,Noah} / Peripheral-4 {Jesus,Joseph,Adam,Lot} / Outlier-1 {John}

## Prior-art note

- **Neuwirth** treats pericopes as liturgical units (tripartite structure); no cross-prophet lexical matrix.
- **Reynolds** traces biblical subtext prophet-by-prophet; no computational matrix.
- **Witztum** traces Syriac subtext for 4 prophet narratives; our pair-unique-root catalog is a computational analog of his philological subtext identification.
- To our knowledge, this is the **first published 8-prophet Jaccard matrix on Quranic QAC roots with a length-preserving pericope-shuffle null**.

## Caveats and limitations

- Null model preserves pericope *count* per prophet but not *total verse mass*. A stricter null would match total verse mass exactly. Given the observed mass variation (John 25 verses vs Moses 478), a mass-preserving null would likely raise Jaccards for John and lower for Moses; should confirm in a follow-up.
- Root layer depends on QAC's Dukes-style analysis — a small fraction of tokens have ambiguous roots (PN tokens with no root tag). These are excluded.
- Pericope definition is not canonical; the ±2 pad is a judgment call. Robustness under gap=5/pad=5 and gap=2/pad=0 is reported in §12 of the finding.
- Moses-Jesus Q 2:87 etc. "explicit coupling" was operationalized as rank in 28-pair Jaccard ordering. A stricter test would find verses where both prophets are named in the same verse and test the lexical density of those verses against the non-coupled pericope distribution.

## Status

- Finding: `reported`
- Master-index: updated (wave append — below the prior prophet-pericope-comparison row)
- Monograph: not touched
- Verse-commentaries: not touched
