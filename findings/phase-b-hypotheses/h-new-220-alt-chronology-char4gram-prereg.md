# H-NEW-220 — Cross-feature replication of [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] under CHAR-4-GRAM

## Pre-registration

**Question.** Under CHAR-4-GRAM feature space (Fisher-Rao angular distance
on top-2000 char-4-grams, L1-normalized + Dirichlet α=0.5), does the mushaf
order STILL produce a Fisher-Rao path length shorter than four alternative
chronologies (Egyptian Standard 1924, Nöldeke 1860/1909, Bell 1937,
Blachère 1947)? This probes whether the mushaf-path-length signal
established under QAC STEM root features ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] → [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]) also
appears under an orthogonal surface-form feature (char-4-grams).

[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] finding (root-feature space): mushaf L=85.76, shorter than all
four chronologies; mushaf ranked 1 of 5; all three Bonferroni-family
chronologies (Egyptian, Bell, Blachère) had p<0.0001 against a uniform-
permutation null but mushaf was strictly shorter than each.

H-NEW-220 replicates under char-4-gram D-matrix (inherited from
[[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]). It is a direct DIFFERENT-FEATURE check of [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]].

## Rules tuple

```
(no-tashkeel,
 char-4-grams with spaces (sliding window),
 K=2000 top char-4-grams,
 Dirichlet α=0.5 smoothing,
 L1-normalized probability vectors,
 Fisher-Rao angular distance = 2·arccos(Σ √(p_i·p_j)),
 basmala-counted-only-in-surah-1,
 Hafs-Kufan,
 D-matrix-inherited-from-H-NEW-111b)
```

## Data sources

- **D matrix**: `findings/phase-b-hypotheses/csv/h-new-111b.json`
  (`D_matrix_upper_triangular`). 114×114 symmetric, zero-diagonal.
  Byte-SHA-256 of source file recorded in output JSON.
- **Egyptian + Nöldeke chronologies**: `data/revelation-order.csv`
  (same source as [[h-new-111-fisher-rao-mushaf|H-NEW-111]] / [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]).
- **Bell 1937 / Blachère 1947 chronologies**: hard-coded rank dicts
  copied verbatim from `scripts/h_new_212_alt_chronology_fisher_rao.py`
  to preserve tie-break and imputation provenance:
    - Bell: surah 15 imputed rank 52 (middle-Meccan median for "M"
      coding in French Wikipedia source).
    - Bell ties: s81 & s82 both rank 15 → mushaf-order secondary sort.
    - Blachère ties: s80 & s84 both rank 24 → mushaf-order secondary sort.

## Primary tests (Bonferroni k=3, α_bon = 0.05/3 = 0.01667)

- **PRIMARY-1** — L_egyptian < L_random (1-sided lower, perm p)
- **PRIMARY-2** — L_bell     < L_random (1-sided lower, perm p)
- **PRIMARY-3** — L_blachere < L_random (1-sided lower, perm p)

Each chronology PASSES if its permutation p < α_bon. These three form
the Bonferroni family; mushaf and Nöldeke are reported descriptively
(not in the correction family, consistent with [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]).

## Descriptive comparisons

- Leaderboard: rank {mushaf, Nöldeke, Egyptian, Bell, Blachère} by L
  (shortest wins).
- Mushaf-wins check: does mushaf have the shortest L of the five?
- Pairwise L_c − L_mushaf in null-SD units, for each chronology c.
- Spearman ρ between chronologies (unchanged: these are ordering-level).

## Null

10,000 uniform permutations of surahs 1..114, seed 20260419 (same as
[[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] for reproducibility of the null-draw mechanism; D matrix
differs so the null L distribution will differ).

## Decision rule (H-NEW-220-level)

Report the leaderboard and whether mushaf retains rank 1 under char-4-gram.

- If mushaf is shortest of 5 AND L_mushaf < L_c for all c ∈ {Nöldeke,
  Egyptian, Bell, Blachère}: [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] and [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] GENERALIZE
  beyond QAC-root features (char-4-gram cross-feature replication).
- If mushaf loses to ≥1 chronology at char-4-gram: [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] signal is
  feature-specific (root-feature-dependent); rank-1-ness of mushaf is
  not a feature-invariant property.
- Bonferroni family verdicts report whether each chronology (Egyptian,
  Bell, Blachère) is itself shorter than random at α_bon regardless of
  the mushaf comparison — these are independent claims.

## Garden-of-forking-paths log (2026-04-17)

1. Used [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]'s D-matrix verbatim (no recomputation). Same K=2000,
   same Dirichlet α, same length control as [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]].
2. Bell/Blachère rank dicts copied verbatim from [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] script;
   same imputation + tie-break policy (documented there).
3. Bonferroni k=3 matches [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] (not k=4, Nöldeke stays descriptive
   to preserve direct comparability).
4. Null seed 20260419 (same as [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]], reused intentionally so
   randomness of null draws is shared across cross-feature checks).
5. Permutation count 10,000 (matches [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]).
6. Reported p_one_sided_lower = (n_perms_le + 1) / (PERMS + 1),
   conservative with pseudocounts.
