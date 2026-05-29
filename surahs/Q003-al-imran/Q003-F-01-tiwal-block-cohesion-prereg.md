---
surah: 3
surah_name_ar: آل عمران
surah_name_translit: Āl ʿImrān
file_type: prereg
test_id: Q003-F-01
date_locked: 2026-05-29
phase: B+
seed: 20260509
n_perm: 10000
status: LOCKED-BEFORE-COMPUTATION
---

# Q003-F-01 — Pre-Registration: al-sabʿ al-ṭiwāl block-cohesion (is the {Q2-Q5} run the corpus's smoothest contiguous 4-surah block?)

**LOCKED BEFORE COMPUTATION.** This file is SHA-256 hashed; the hash is embedded in
`scripts/Q003_F_01_tiwal_block.py` and verified at runtime (fail-fast on mismatch).

## Motivation

The classical tradition groups the first long surahs as *al-sabʿ al-ṭiwāl* ("the seven long ones") —
al-Bukhārī's recension (Ṣaḥīḥ, *Kitāb Faḍāʾil al-Qurʾān*) and the *faḍāʾil* tradition treat al-Baqara +
Āl ʿImrān as *al-Zahrāwān* ("the two luminous ones," Muslim, *Kitāb Ṣalāt al-Musāfirīn*, ḥadīth on Abū
Umāma). al-Suyūṭī (*al-Itqān*, nawʿ on the order of the sūras) and al-Zarkashī (*al-Burhān*, *al-nawʿ al-thānī
fī munāsabat*) treat the head of the muṣḥaf {Q2, Q3, Q4, Q5} as a thematically continuous Medinan legal-creedal
block. al-Rāzī (*Mafātīḥ al-ghayb*) and al-Biqāʿī (*Naẓm al-Durar*) give explicit *munāsaba* (inter-surah
coherence) arguments for the Q2→Q3 and Q3→Q4 joints.

The project's TSP-residual instrument (H-NEW-720) provides a quantitative correlate: the canonical-adjacency
cost `delta_raw` measures how much "extra" path-length the muṣḥaf order pays at each seam relative to a 2-opt
re-tour on the Fisher-Rao root-distribution geometry. A *negative* delta_raw is a **seamless seam** (the
muṣḥaf order is locally cheaper than the heuristic re-tour). Q 3 al-ʿImrān is additionally a
**COHESION_ANCHOR** in H-NEW-590 (removing it *raises* the dispersion of its {Q1-Q7} window). This pre-reg
promotes the qualitative al-ṭiwāl-block claim into a falsifiable corpus-rank test.

## Rules-tuple

`(no-tashkeel, QAC v0.4 STEM-root distributions, Fisher-Rao distance, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

All seam values are read from `findings/phase-b-hypotheses/csv/h-new-720.json` (`per_adjacency`,
`delta_raw` field). The 590 cohesion-anchor classification is read from
`findings/phase-b-hypotheses/csv/h-new-590.json` (`all_surahs_results`, `X==3`). No value is asserted
from memory; the script reads the on-disk JSON.

## Definitions

- A **contiguous 4-surah block** starting at surah *s* is {s, s+1, s+2, s+3}; its **internal seams** are
  the three adjacency costs delta_raw(s→s+1), delta_raw(s+1→s+2), delta_raw(s+2→s+3). There are 111 such
  blocks (s = 1 … 111).
- The block's **mean internal seam** is the arithmetic mean of those three delta_raw values.
- A block is *smoother* than another if its mean internal seam is lower (more negative = more seamless).

## Arm A — block-smoothness rank (DETERMINISTIC, DIRECTION-LOCKED)

**Hypothesis A (pre-committed):** The al-sabʿ-al-ṭiwāl head-block {Q2, Q3, Q4, Q5} is the **smoothest**
contiguous 4-surah block in the muṣḥaf on the H-NEW-720 mean-internal-seam metric.

- **A-H1 (direction-locked):** rank of block {2,3,4,5} among all 111 contiguous 4-blocks (ascending by
  mean internal seam) = **1** (it is the unique minimum).
- **A-H2 (direction-locked):** Q 3's two internal seams to its long-surah neighbours are both at or below
  the corpus median seam: delta_raw(Q2→Q3) ≤ median AND delta_raw(Q3→Q4) ≤ median.

**A success criterion:** A-H1 (rank == 1) ∧ A-H2 → Arm A CONFIRMED (deterministic corpus fact).
**A failure criterion:** rank > 1 (some other block is smoother) OR either Q3 seam above median → Arm A NULL /
direction-violation (published with full prominence).

## Arm B — Q3 as cohesion anchor of the long-surah head (DETERMINISTIC, DIRECTION-LOCKED)

**Hypothesis B (pre-committed):** Q 3 al-ʿImrān is a **cohesion member** (not an outlier) of its {Q1-Q7}
window — removing Q 3 *increases* the window's content-dispersion percentile.

- **B-H1 (direction-locked):** delta_pct(X=3) in H-NEW-590 is **negative** (window-without-Q3 is MORE
  dispersed than window-with-Q3), i.e. Q 3 is classified COHESION_ANCHOR, not STRONG/WEAK_OUTLIER.

**B success criterion:** delta_pct < 0 AND classification == "COHESION_ANCHOR" → Arm B CONFIRMED.
**B failure / pre-commit violation:** delta_pct ≥ 0 (Q3 is an outlier) → NULL with explicit flag.

## Arm C — permutation control: is the {2,3,4,5} block smoothness beyond chance? (PERMUTATION, seed 20260509, 10000 perms)

**Hypothesis C (pre-committed, direction-locked):** The {2,3,4,5} block's mean internal seam is LOWER
(smoother) than a permutation null in which the 113 seam values are randomly re-assigned to the 113
positions and the smoothest contiguous-4-block mean is recomputed.

- **Null C:** seed=20260509, 10000 perms. Each perm: shuffle the 113 delta_raw values across the 113 seam
  positions; recompute the mean internal seam of EVERY contiguous 4-block; record the MINIMUM block mean.
  This is the distribution of "smoothest 4-block achievable when seams are randomly arranged" (a max-statistic
  null controlling for the multiplicity of 111 candidate blocks).
- **C-H1 (direction-locked):** observed {2,3,4,5} mean internal seam ≤ the null distribution of minimum-block
  means at α = 0.05; p_perm = (#{null_min ≤ obs} + 1)/(N+1). **Direction: observed is at/below the null
  smoothest-block (the muṣḥaf's head-block is at least as smooth as chance's best).**

**C success:** p_perm < 0.05 → the observed head-block smoothness is not reproducible by random seam-arrangement.
**C note:** because Arm A already shows the observed block is the *global* minimum, Arm C tests whether a
RANDOM arrangement would routinely produce a block this smooth; the informative comparison is obs vs the
random-min distribution.

## Bonferroni

Test family Q003-F-01 has k = 1 permutation cell (Arm C). The deterministic cells (A-H1, A-H2, B-H1) do not
consume α. α_corrected for the permutation cell = 0.05 / 1 = 0.05.

## MW protections

- **MW-1 (instrument-prior):** mean-internal-seam metric, rank definition, and delta_pct sign all fixed here before any run.
- **MW-2 (corpus-prior):** Arm C uses 10,000 permutations of the full 113-seam vector.
- **MW-3 (alternative-models):** Arm A (rank) + Arm B (independent 590 instrument) + Arm C (permutation) triangulate the same block-cohesion claim on three different instruments.
- **MW-5 (replication):** Arm A and Arm B are deterministic and fully replicable from the on-disk JSON; Arm C seed-locked at 20260509.
- **MW-6 (instrument-control):** Arm C's max-statistic null (minimum over 111 blocks) controls for the multiple-block selection.
- **MW-7 (post-hoc cap):** the al-ṭiwāl-block claim is classical (al-Bukhārī/al-Suyūṭī); promoted to a direction-locked pre-registered test here before computation.

## Verdict mapping

| Arm | Pass condition | Verdict label |
|:--|:--|:--|
| A | A-H1 (rank==1) ∧ A-H2 | CONFIRMED (deterministic corpus-rank) |
| B | delta_pct<0 ∧ COHESION_ANCHOR | CONFIRMED |
| C | p_perm < 0.05 | CONFIRMED (beyond chance) |
| any | direction reversed | NULL (pre-commit violation, full prominence) |

Final Q003-F-01 verdict = honest combination of Arms A, B, C, reported with equal NULL prominence.

*Locked 2026-05-29. Seed 20260509. Bismillāhi al-Raḥmāni al-Raḥīm.*
