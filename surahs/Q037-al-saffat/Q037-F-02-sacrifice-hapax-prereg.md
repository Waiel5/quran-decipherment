---
surah: 37
test_id: Q037-F-02
title: Sacrifice-of-Ishmael narrative-block (Q 37:99-113) hapax-density and lexical isolation
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q037-F-02-sacrifice-block-isolation
alpha_bon: 0.01667
---

# Q037-F-02 — Pre-registration: Sacrifice-of-Ishmael narrative hapax + isolation test

## 1. Hypothesis (locked before observation)

**H1 (locked direction):** The Q 37:99-113 sacrifice-of-Ishmael narrative-block contains **≥3 root-hapax** (roots whose only corpus attestations lie within the block). This pre-reg implements the brief's "Predict ≥3 hapax in this narrative-block."

**H2 (locked direction):** The Q 37:99-113 block has **higher TF-IDF lexical isolation** (mean cosine distance to the rest of Q 37) than the corpus-baseline of random 15-verse spans drawn from comparable mid-Meccan narrative blocks. Operationalization: take a permutation null of 10,000 random 15-verse contiguous spans drawn from the set of mid-Meccan prophet-narrative surahs {Q 7, Q 11, Q 19, Q 21, Q 26, Q 27, Q 28, Q 37, Q 38} (n_pool = 9 surahs); for each span, compute (mean TF-IDF cosine distance from the span to the surah-rest). H1: Q 37:99-113 mean distance > permutation null at α_bon = 0.01667.

**H3 (locked direction):** The block is MORE lexically isolated than (a) Q 21:69 fire-block (Q 21:69-71, the Abraham-fire pericope), and (b) Q 11:69-83 angel-visit-block (Lot+Abraham angel-visit). Operationalization: lexical-isolation = mean TF-IDF cosine distance from block to surah-rest. H1: Q 37:99-113 isolation > both Q 21:69-71 and Q 11:69-83.

## 2. Operational definitions

### Hapax detection (H1)
- Source: `data/morphology/root-index.json` (QAC v0.4 root index).
- Block: all roots attested in any verse v ∈ {Q 37:99, ..., Q 37:113} with verse_word_position recorded.
- Hapax-in-block = root R such that ALL attestations of R in the corpus lie within Q 37:99-113.
- Count: N_hapax_in_block.
- Pass condition: N_hapax_in_block ≥ 3.

### Permutation null (H2)
- For each comparison-surah s ∈ {Q 7, Q 11, Q 19, Q 21, Q 26, Q 27, Q 28, Q 38}, sample N_perm random contiguous 15-verse spans (with replacement); for each span, compute mean TF-IDF cosine distance from span to (surah s minus span).
- TF-IDF: surface-token level, no-tashkeel, IDF computed over Q 37 verse-set + comparison spans.
- Q 37:99-113 mean distance = D_obs.
- p-value = fraction of null spans with distance ≥ D_obs.
- n_perm = 10000, seed 20260508.

### Comparison anchors (H3)
- Q 21:69-71 (Abraham fire). 3 verses.
- Q 11:69-83 (Abraham/Lot angel-visit). 15 verses.
- Compute lexical-isolation as: mean TF-IDF cosine distance from the block tokens to the rest-of-surah tokens. Direct numerical comparison; no permutation test on H3 (pre-committed direction-locked direct comparison).

## 3. Test statistic

- N_hapax_in_block (H1).
- D_obs vs permutation null (H2).
- D_q37_99_113, D_q21_69_71, D_q11_69_83 (H3).

## 4. Success / Failure

- **CONFIRMED**: H1 (≥3 hapax) passes AND H2 (p ≤ α_bon = 0.01667) passes.
- **DIRECTIONAL**: H1 passes but H2 fails OR vice versa.
- **NULL**: Both H1 and H2 fail.
- **Pre-commit violation**: N_hapax_in_block = 0 (would falsify even the qualitative claim).

## 5. Honest limits known a priori

- The QAC root-index might mis-segment some roots. Sensitivity-check: re-run with QAC v0.4 root field directly from `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Corpus-hapax = ALL attestations in this 15-verse block. The narrower form (block-unique within comparable narratives) has been observed during empirical-anchor extraction: 2 corpus-hapax roots (`tll`, `jbn`) at v. 103. The pre-reg's "≥3" threshold is conservative against this prior observation; if the formal definition reveals only 2, **H1 FAILS** as locked. The direction-locked prediction is at risk.
- The TF-IDF cosine null suffers from short-block / vocabulary-drift bias; the mid-Meccan-narrative pool controls for this.
- The block boundary v.99-113 is set by classical content-segmentation (the entire Abraham-and-son sacrifice arc); alternative boundaries (e.g., v.100-113 starting at the prayer for an offspring) are NOT post-hoc adjustments to chase significance — the v.99-113 boundary is locked.

## 6. Rules-tuple

`(no-tashkeel, QAC-root-index + orthographic-token, IDF, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 3 (H1, H2, H3). α_bon = 0.05 / 3 = 0.01667.

## 8. SHA256 lock

Embedded in `scripts/Q037_F_02_sacrifice_hapax.py`; verified at runtime.
