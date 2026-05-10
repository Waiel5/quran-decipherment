---
finding_id: Q027-F-12
title: "Solomon-Sabaʾ pericope cohesion: Q 27:22-44 vs Q 34:15-19 — pericope-scale root-Jaccard PASS per cross-finding-025-formal"
phase: B+
date: 2026-05-10
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
rules_tuple: "(no-tashkeel; QAC v0.4 stem-ROOT field; basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
parent_finding: cross-finding-025-formal (scale-of-aggregation flip law)
companion_finding: Q027-F-08 (whole-surah FR Q 27 ↔ Q 34 < Q 27 ↔ Q 38, DIRECTIONAL)
---

# Q027-F-12 — Solomon-Sabaʾ pericope cohesion (cross-finding-025-formal pericope-scale test)

## Hypothesis (locked, direction-tighter)

**H1 (locked direction)**: The two corpus-attested Solomon-Sabaʾ narrative pericopes — **Q 27:22-44** (Hudhud's report on Sabaʾ + Solomon's letter + Bilqīs's reception, 23 verses) and **Q 34:15-19** (the eponymous Sabaʾ verses describing the kingdom's gardens, dam-burst, and divine retribution, 5 verses) — exhibit **root-Jaccard cohesion ABOVE the corpus baseline of pericope-pairs of matched aggregate length**.

Specifically:
- Observed statistic: pairwise Jaccard of the (Q 27:22-44 root-set ∪ Q 34:15-19 root-set) intersection / union, J_obs.
- Null distribution: 10,000 random pericope-pairs drawn from the corpus with the same (N1, N2) verse-counts (23 + 5), matched on aggregate length, seed 20260509.
- **Locked direction**: J_obs > J_null_mean (one-sided upper-tail).
- **Locked threshold**: PASS-CONFIRMED at p_perm ≤ 0.05 (uncorrected) — this is a single pericope-scale test on a pre-specified marker (Solomon-narrative), so no Bonferroni family applies. PASS-DIRECTED at p_perm ∈ (0.05, 0.10].

## Rationale (cross-finding-025-formal pericope-scale principle)

Per [[cross-finding-025-formal-scale-of-aggregation-law|cross-finding-025-formal]] (triple-flip confirmation 2026-05-09 PM), thin markers (Iblīs, sajda, prophet-vocative) that NULL at whole-surah scale flip to PASS at pericope scale. The Solomon-narrative is a **thick marker** at the pericope window (Q 27:22-44 = 23 verses; Q 34:15-19 = 5 verses; total 28 verses), making it a candidate for **PASS at BOTH scales**.

Q027-F-08 already showed whole-surah Q 27 ↔ Q 34 FR-distance 0.866 < Q 27 ↔ Q 38 0.991 (DIRECTIONAL, aux p ≈ 0.146 — modest at whole-surah scale). The cross-finding-025-formal principle predicts that at the pericope window, the Solomon-Sabaʾ shared narrative material should produce **clear above-baseline cohesion**.

Pre-registered direction-tighter prediction: PASS-CONFIRMED.

## Method (deterministic + permutation null)

1. Load QAC v0.4 morphology (`data/morphology/quranic-corpus-morphology-0.4.txt`); build map `(s, v) → set of stem-roots`.
2. Build pericope-A root-set R_A = ⋃ roots(27, v) for v ∈ {22, 23, ..., 44} (23 verses).
3. Build pericope-B root-set R_B = ⋃ roots(34, v) for v ∈ {15, 16, 17, 18, 19} (5 verses).
4. Compute J_obs = |R_A ∩ R_B| / |R_A ∪ R_B|.
5. Permutation null: draw 10,000 random pericope-pairs (P_A, P_B) where P_A is a 23-verse contiguous window from a random surah s ≠ {27, 34} and P_B is a 5-verse contiguous window from a random surah s' ≠ {27, 34, s}; compute J_null distribution.
6. p_perm = #{J_null ≥ J_obs} / 10,000.
7. Report: J_obs, J_null_mean, J_null_std, z-score, p_perm, direction-match.

Additional aux statistics (NOT pre-registered direction-locked; report for transparency):
- Per-verse-normalized concordance: average per-verse root-overlap of vv in pericope-B with R_A.
- Top shared roots in R_A ∩ R_B.

## Pre-registered success criteria

- **PASS-CONFIRMED**: J_obs > J_null_mean AND p_perm ≤ 0.05.
- **PASS-DIRECTED**: J_obs > J_null_mean AND 0.05 < p_perm ≤ 0.10.
- **NULL**: 0.10 < p_perm ≤ 0.50 with J_obs > J_null_mean (directional but weak).
- **PRE-COMMIT-VIOLATION**: J_obs < J_null_mean (reversed direction).

## Classical anchors

- al-Biqāʿī, *Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar*, on Q 27-Q 34 munāsabah: explicit identification of the Solomon-Sabaʾ narrative as a thematic bridge between the two surahs (Q 27 names the queen narrative; Q 34 names the kingdom).
- al-Rāzī, *Mafātīḥ al-ghayb*, on Q 34:15: identifies Sabaʾ as the same Sabaʾ of Q 27, providing the canonical inter-surah link.
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 34:15-19: explicit cross-reference to the Q 27 narrative.
- al-Suyūṭī, *al-Itqān*, nawʿ on munāsabāt al-suwar: catalogues the Q 27-Q 34 connection.

## Garden-of-forking-paths

The pericope windows Q 27:22-44 and Q 34:15-19 are pre-specified from the dispatch (the 2026-05-10 specialist brief) and correspond to the **standard mufassir-identified Solomon-Sabaʾ narrative blocks**: Q 27:22-44 = the Hudhud-Sabaʾ-letter-throne narrative; Q 34:15-19 = the Sabaʾ-kingdom-dam-burst narrative. No alternative window-boundaries considered. The instrument (QAC stem-root Jaccard) is the cross-finding-025-formal canonical instrument. Seed 20260509 matches the cross-finding-025-formal canonical seed. 10,000 perms matches the canonical permutation count.

## Honest limits (pre-committed)

- Block sizes differ (23 vs 5 verses); the pericope-B is shorter and contributes fewer unique roots. Jaccard tolerates size asymmetry, but per-verse normalization (reported as aux statistic, not pre-registered direction-locked) is the cleaner secondary read.
- The QAC v0.4 root tags include some lemma-level genericness (frequent roots like *q-w-l*, *ʾ-l-h*, *m-l-k* appear in both pericopes and would appear in many random pericope-pairs); the null distribution accounts for this.
- A single-pericope-pair test does not constitute a corpus-wide replication of cross-finding-025-formal; it is a single application to the Solomon-Sabaʾ thick-marker class. PASS here strengthens the cross-finding-025-formal evidence; NULL would either falsify the thick-marker prediction at the upper end of marker thickness, or surface a Solomon-narrative-specific exception.
- The pre-registered direction is **PASS-CONFIRMED**, NOT NULL. This is a one-sided upper-tail prediction grounded in cross-finding-025-formal + Q027-F-08 whole-surah DIRECTIONAL signal + four classical mufassir anchors. Reversed direction (J_obs < J_null_mean) would be a pre-commit violation, published with full prominence as NULL.

## Pre-commit declaration

The SHA256 of this file is embedded in the runner script for fail-fast verification per §1.2.
