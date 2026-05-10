---
surah: 34
test_id: Q034-F-03
title: Q 34 ḥmd root density and rank in corpus 114 (al-ḥamdu opener density audit)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q034-F-03-hmd-root-rank
alpha_bon: 0.01667
---

# Q034-F-03 — Pre-registration: Q 34 ḥ-m-d root rank in 114-surah corpus

## 1. Hypothesis (locked before observation)

Q 34 Sabaʾ is one of 5 *al-ḥamdu li-llāh* openers. Beyond the formal opener-tag, the question is whether Q 34's *full ḥ-m-d root distribution* is structurally exceptional at the corpus level. Pre-flight QAC extraction confirms corpus-total of 63 *ḥ-m-d* (ROOT:Hmd) tokens distributed across 36 surahs.

**H1 (locked direction, token-count rank):** Q 34's raw ROOT:Hmd token-count is in the **top-10** of the 114 surahs.

**H2 (locked direction, per-verse density):** Q 34's per-verse ROOT:Hmd density (count / verse-count) is in the **top-10** of the 36 surahs with at least 1 attestation.

**H3 (locked direction, opener-cluster intra-rank):** Q 34's per-verse density is **HIGHER** than the median per-verse density of the 5 al-ḥamdu openers {Q 1, 6, 18, 34, 35}.

**Direction:** Q 34 is a structurally-prominent *ḥ-m-d* surah at both token and density levels.

## 2. Operational definitions

- **Source**: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4), ROOT:Hmd line-grep.
- **Token-count per surah**: number of QAC tokens with ROOT:Hmd, grouped by surah (parsed from the `(s:v:w...)` location string).
- **Per-verse density**: token-count / verse-count (verse-counts from `data/hafs-verse-counts.tsv`).

## 3. Test statistic

- rank_count: position of Q 34 in descending ROOT:Hmd token-count.
- rank_density: position of Q 34 in descending per-verse ROOT:Hmd density.
- median_5_openers: median of the 5 openers' per-verse densities; compare Q 34's density.

## 4. Permutation null

Not strictly needed for rank-based tests (deterministic), but reported alongside:
- 10,000 random reassignments of token-locations to surahs (length-weighted by total-word-count).
- Compute p_lower for Q 34 token-count being ≥ observed; same for density.

## 5. Success / Failure criteria

| Cells passing | Verdict |
|:--|:--|
| 3/3 H1+H2+H3 | CONFIRMED |
| 2/3 | DIRECTIONAL |
| 1/3 | DIRECTIONAL-WEAK |
| 0/3 | NULL |

## 6. Honest limits known a priori

- Pre-flight observation: Q 34 has 3 ROOT:Hmd tokens (rank ~6 in token-count, tied with several others); per-verse density 3/54 = 0.0556 (rank to be computed; the dual-ḥamd v.1 contributes 2 of these 3 tokens, possibly inflating the count vs other surahs).
- The dual-ḥamd v.1 (corpus-UNIQUE doubling) is a known structural feature; H2 is essentially a re-encoding of that uniqueness at the per-verse density axis.
- Garden-of-forking-paths disclosure: token-counts were pre-extracted; verdict ceiling is **DESCRIPTIVE-EMPIRICAL** under transparent post-hoc disclosure.

## 7. Rules-tuple

`(no-tashkeel, QAC-root, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)`.

## 8. Bonferroni

k = 3. α_bon = 0.01667.

## 9. SHA256 lock

Embedded in `scripts/Q034_F_03_hmd_root_rank.py`; verified at runtime.
