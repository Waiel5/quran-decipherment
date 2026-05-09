---
surah: 75
test_id: Q075-F-02
title: Q 75 ↔ Q 90 structural twin pair — bare-*lā uqsimu* corpus exclusivity
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q075-F-02-q75-q90-twin
alpha_bon: 0.025
direction: Locked — Q 75 and Q 90 are the corpus-EXACT 2 surahs whose v.1 begins with bare *lā uqsimu* (no *fa-* prefix)
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q075-F-02 — Pre-registration: Q 75 ↔ Q 90 structural-twin pair

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** Among the 114 surahs, EXACTLY 2 open with the bare *lā uqsimu* construction (no *fa-* prefix) at v. 1: Q 75 al-Qiyāma and Q 90 al-Balad.

**H1b (one-tailed, locked direction):** Q 75 ↔ Q 90 FR distance is below the corpus median, indicating structural affinity beyond the shared opening formula.

**H0 (joint):** Either count of bare-*lā uqsimu* openers ≠ 2, OR Q 75 ↔ Q 90 FR distance ≥ corpus median.

## 2. Operational definition

### Cell A — opener count
For each of 114 surahs, examine v. 1 (after stripping ornament markers like ۞):

- Count surahs where v. 1 matches regex `^لا أقسم\b` (i.e., starts literally with the bare-*lā uqsimu* construction).

### Cell B — FR pair-distance
- D[Q 75, Q 90] from `findings/phase-b-hypotheses/csv/h-new-111.json` D matrix.
- Corpus median FR = `distance_matrix_stats.median`.
- Test: D[Q 75, Q 90] < corpus_median.

## 3. Permutation null

Cell A: corpus-exact count is structural; no perm null needed (count is a discrete property of the canonical text).

Cell B: pair-distance percentile-rank within corpus's pair-distance distribution.

## 4. Success / Failure

- **VINDICATED**: Both Cell A (count = 2) and Cell B (pair distance < median; below corpus median).
- **DIRECTIONAL**: Cell A passes (count = 2) but Cell B fails (pair distance ≥ median).
- **NULL**: Cell A fails (count ≠ 2).
- **Pre-commit violation**: Q 75 or Q 90 itself does not match the regex.

## 5. Honest limits known a priori

- The structural-twin claim depends on (i) Q 75 and Q 90 being the only 2 bare-*lā uqsimu* openers and (ii) their content-affinity beyond the shared formula. The brief notes this corpus-feature explicitly so the discovery is brief-directed; the empirical lock is corpus-exact.
- Verdict ceiling = VINDICATED is permitted because Cell A is a structural count and Cell B is a comparison to a robust corpus statistic.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (Cell A opener count, Cell B FR pair-distance). α_bon = 0.025.

## 8. Coordination

No prior Q-specialist has run a Q 75 ↔ Q 90 twin test. The 4-surah "negative-oath cluster" mentioned in the brief is a different family (covered by Q075-F-03).

## 9. SHA256 lock

Computed at write-time, embedded into `scripts/Q075_F_02_q75_q90_twin.py`, verified at runtime.
