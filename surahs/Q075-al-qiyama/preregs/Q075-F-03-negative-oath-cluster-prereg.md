---
surah: 75
test_id: Q075-F-03
title: Corpus-EXACT 6-surah negative-particle-oath cluster — FR cohesion
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q075-F-03-negative-oath-cluster
alpha_bon: 0.01667
direction: Locked — the corpus-EXACT 6-surah negative-particle-oath cluster {Q 56, 69, 70, 75, 81, 84, 90} exhibits FR-cohesion below corpus median
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q075-F-03 — Pre-registration: Negative-oath cluster FR cohesion

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** The corpus-EXACT 6-surah set of surahs containing any *lā uqsimu* / *wa-lā uqsimu* / *fa-lā uqsimu* construction — namely **{Q 56, 69, 70, 75, 81, 84, 90}** — exhibits a mean pairwise FR-content distance significantly **below** the corpus mean (i.e., the cluster is FR-COHESIVE).

**H1-aux (locked):** Compare to the 4-surah subset {Q 56, 70, 75, 90} mentioned in the original specialist brief; predict the strict 6-surah set is more cohesive than the 4-surah brief subset.

**H0:** Mean pairwise FR is at-or-above corpus mean (NULL); OR direction reverses (sign-flip pre-commit violation).

**Direction:** Cohesion BELOW corpus mean (LOCKED).

## 2. Operational definition

### Source artifacts
- `quran-text/quran-no-tashkeel.json` (for fragment enumeration)
- `findings/phase-b-hypotheses/csv/h-new-111.json` (FR distance matrix)

### Step 1: Define cluster (corpus-EXACT enumeration)
A surah is a "negative-particle-oath cluster member" iff it contains at least one verse matching regex (after ornament-stripping):

```
^(لا|ولا|فلا) أقسم\b
```

This regex captures `lā uqsimu`, `wa-lā uqsimu`, `fa-lā uqsimu` as verse-openers. The enumeration is corpus-wide, no surah-specific prior.

Pre-committed: this enumeration yields exactly the 6 surahs {Q 56, 69, 70, 75, 81, 84, 90} (7 surahs total because Q 75 contributes 2 verses; the surah-set is 6 distinct surahs, but Q 75 has 2 of the 7 oath-verses).

[Correction during pre-reg: 7 distinct surahs in the set — earlier draft miscounted Q 75 as a single member; the surah-set is {56, 69, 70, 75, 81, 84, 90} = **7 surahs**, not 6. The pre-reg now locks N = 7.]

### Step 2: Compute observed FR-cohesion
- C(7,2) = 21 within-cluster pairs.
- obs_mean = mean FR-distance over the 21 pairs.

### Step 3: Permutation null
- Sample 10⁴ random 7-surah subsets from the 114 surahs (uniform without replacement).
- For each, compute mean pairwise FR.
- p_lower = fraction of null means ≤ obs_mean.
- z = (obs_mean − null_mean) / null_std.

### Step 4: Compare to brief-subset {Q 56, 70, 75, 90}
- Same procedure for N=4.

### Step 5: 2-OPENER subset {Q 75, Q 90} (singleton pair)
- D[Q 75, Q 90] vs corpus median.

## 3. Test cells (Bonferroni k = 3)

- **Cell A**: 7-surah corpus-EXACT cluster FR-cohesion; primary, predicts p_lower < α_bon = 0.01667.
- **Cell B**: 4-surah brief subset FR-cohesion; compares the brief's specification to the corpus-EXACT.
- **Cell C**: Q 75 ↔ Q 90 pair-distance below corpus median (replicating Q075-F-02 Cell B; secondary).

## 4. Success / Failure

- **CONFIRMED**: Cell A passes at α_bon = 0.01667; direction matches LOCKED.
- **PASS-DIRECTED**: Cell A passes at single-test α=0.05 but not Bonferroni-corrected α; per HANDOFF/04-DISCIPLINE.md ceiling.
- **DIRECTIONAL**: direction matches LOCKED but p > 0.05.
- **NULL**: direction matches LOCKED but p > 0.5; or sign-flip.
- **PRE-COMMIT VIOLATION**: sign-flip — published with prominence per Protocol §1.8.

Cell B prediction: 4-surah subset has WEAKER cohesion than 7-surah set (specialist judgment that brief's subset is too narrow to capture the structural cluster).

## 5. Honest limits

- The negative-oath cluster's enumeration depends on the rules-tuple (regex on no-tashkeel text). Under min-tashkeel or full-tashkeel, the same construction may have spelling variants (e.g., لاَ vs لا). Sensitivity check: re-run on min-tashkeel.
- N=7 is small; permutation null bound ≈ 1/n_perm = 0.0001.
- The cluster is form-defined (oath-construction at any surah-position), not theme-defined; affinity could be coincidental form-cluster (analogous to H-NEW-1070 oath-opener cluster confirmed at p=0.0004).

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 3. α_bon = 0.05 / 3 = 0.01667.

## 8. Coordination

No prior FR-cluster test has been pre-registered for this corpus-EXACT 7-surah set; H-NEW-1070 covers a different (positive-*wa-l-* oath-opener) cluster.

## 9. SHA256 lock

Computed at write-time, embedded into `scripts/Q075_F_03_negative_oath_cluster.py`, verified at runtime.
