---
prereg_id: Q041-F-04
title: Q 41:9-12 creation-in-six-days pericope — cluster cohesion with parallel pericopes on root-Jaccard
date: 2026-05-09
seed: 20260509
locked_at: 2026-05-09T23:10:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q041-F-04 — 6-day creation pericope cluster on root-Jaccard

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The 8 *creation-in-six-days* pericopes
{Q 7:54, Q 10:3, Q 11:7, Q 25:59, Q 32:4, Q 41:9-12, Q 50:38, Q 57:4}
form a **tight cluster on QAC root-Jaccard similarity** at pericope-scale, with mean pairwise Jaccard significantly **higher** than a permutation null sampling 8 random verse-spans matched on length.

**Direction**: mean_Jaccard(observed pericope-set) > mean_Jaccard(random matched-length verse-set, permutation null).

**Pericope definitions** (locked):
- Q 7:54 — single verse
- Q 10:3 — single verse
- Q 11:7 — single verse
- Q 25:59 — single verse
- Q 32:4 — single verse
- Q 41:9-12 — 4-verse block
- Q 50:38 — single verse
- Q 57:4 — single verse

## 2. Null

**H0**: The 8 pericopes' mean pairwise root-Jaccard is statistically indistinguishable from random verse-spans of matched length.

## 3. Operationalization

- Roots: QAC v0.4 ROOT tag (`/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`).
- Verse-locator: parse `(s:v:w:seg)` keys, extract `ROOT:xxx` from features field.
- Pericope-bag: union of all roots in the pericope's verses (de-duplicated).
- Pairwise similarity: Jaccard(A, B) = |A ∩ B| / |A ∪ B|.
- Test statistic: mean of (8 choose 2) = 28 pairwise Jaccard values.
- Null: permutation null over random matched-length verse-spans. For each pericope, sample N_PERM=10000 random anchors and take a contiguous span of the same verse-count from any surah (uniform over valid anchors); compute the mean-pairwise-Jaccard for each permutation set.
- p-value: fraction of perms with mean-Jaccard ≥ observed.
- Tie-handling: `(perms_ge + 1) / (N_PERM + 1)`.

## 4. Direction lock

Pre-committed direction: observed mean-Jaccard > null mean. If observed < null mean, NULL via pre-commit violation.

## 5. Bonferroni

Single test (k=1).

## 6. Success / failure criteria

- **VINDICATION**: p_perm ≤ 0.05, observed mean > null mean (direction matches).
- **DIRECTIONAL**: p_perm ∈ (0.05, 0.10] with correct direction.
- **NULL**: p > 0.10, or direction reversed.
- Replication side-check: compute pairwise Jaccard at orthographic-token level as cross-instrument.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q041-F-04.json`: SHA, pericopes, root-bags, 28-pair Jaccard matrix, observed mean, null distribution, p-value, verdict.

## 9. Rationale

The 6-day creation topos is the most-distributed cosmological refrain in the Qurʾān, with 7-8 attestations in distinct surahs. Per H-NEW-1380 principle (pericope-scale cohesion tests outperform surah-scale tests when the thematic marker is verse-localized), root-Jaccard at the pericope-level should detect lexical cohesion that surah-FR misses.

**Comparison to known precedents**:
- H-NEW-1310 NULL: Christ-narrative {Q 3, 5, 19} cluster too thin at surah-FR.
- H-NEW-1320 PASS: 3-tier refrain {Q 55, 77, 26} when measured at the right scale.
- Cross-finding-025: marker-thickness rule — pericope-scale is the natural scale for thin-marker topoi.

The 7-day creation topos has ~25-30 word per pericope; this is a **thin marker at surah-scale** but **thick at pericope-scale**. The pericope-Jaccard test directly probes the topos-cohesion hypothesis.

## 10. Cross-references

- [[h-new-1310-christ-cluster|H-NEW-1310]] — surah-scale NULL
- [[h-new-1320-refrain-3tier|H-NEW-1320]] — pericope-scale PASS-DIRECTED
- [[cross-finding-025-marker-thickness|cross-finding-025]]
- al-Suyūṭī *al-Itqān*, nawʿ 45 *al-mutashābih* (parallel-verse catalog)
- al-Bāqillānī *Iʿjāz al-Qurʾān*, ad creation-pericope variation
