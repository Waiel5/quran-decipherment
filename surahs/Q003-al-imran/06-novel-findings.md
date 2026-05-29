---
surah: 3
surah_name_ar: آل عمران
surah_name_translit: Āl ʿImrān
file_type: novel-findings
date_last_updated: 2026-05-29
phase: B+
verdict: Q003-F-01 — Arm A CONFIRMED (rank-1 smoothest 4-block) + Arm B CONFIRMED (cohesion anchor) + Arm C NULL (not beyond chance multiplicity)
seed: 20260509
n_perm: 10000
---

# Q 3 Āl ʿImrān — Pre-Registered Novel Findings

One pre-registered three-arm test, run with seed 20260509 and 10,000 permutations, pre-reg SHA-256 locked
before computation and verified at runtime.

- **Pre-reg:** `surahs/Q003-al-imran/Q003-F-01-tiwal-block-cohesion-prereg.md`
- **Pre-reg SHA-256:** `40f796b7f07db6196fd397180b449e780382ba154684033fb8ecb2329f80c4d7`
- **Script:** `scripts/Q003_F_01_tiwal_block.py` (verifies SHA at runtime, fail-fast — printed "SHA OK")
- **JSON:** `surahs/Q003-al-imran/csv/Q003-F-01.json`
- **Rules-tuple:** `(no-tashkeel, QAC v0.4 STEM-root, Fisher-Rao, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

The test promotes the classical *al-sabʿ al-ṭiwāl* head-block claim (al-Suyūṭī *al-Itqān*; al-Zarkashī
*al-Burhān*) into three falsifiable, direction-locked instruments: a deterministic block-rank (Arm A), the
independent H-NEW-590 cohesion-anchor classification (Arm B), and a max-statistic permutation null (Arm C).

---

## Q003-F-01 Arm A — {Q2,Q3,Q4,Q5} is the smoothest contiguous 4-block (CONFIRMED)

**Hypothesis (pre-committed):** the al-ṭiwāl head-block {Q2, Q3, Q4, Q5} is the smoothest contiguous
4-surah block in the muṣḥaf on the H-NEW-720 mean-internal-TSP-seam metric.

- **A-H1 (direction-locked):** rank of {2,3,4,5} among 111 contiguous 4-blocks (ascending by mean internal
  seam) = 1.
- **A-H2 (direction-locked):** both Q 3 internal seams (Q2→Q3, Q3→Q4) ≤ corpus seam median.

**Result:**
- {2,3,4,5} internal seams = [+0.01646 (Q2→Q3), −0.04662 (Q3→Q4), −0.06571 (Q4→Q5)]; mean = **−0.03196**.
- **rank = 1/111** (the unique minimum) — **A-H1 PASS.**
- seam median = 0.06211; Q2→Q3 = 0.01646 ≤ median, Q3→Q4 = −0.04662 ≤ median — **A-H2 PASS.**
- Smoothest-6 4-blocks: {2-5} (−0.0320), {4-7} (−0.0270), {3-6} (−0.0233), {91-94} (−0.0138), {84-87}
  (−0.0035), {109-112} (+0.0028). **The top three are all overlapping windows inside al-sabʿ al-ṭiwāl.**

**Verdict: CONFIRMED (deterministic corpus-rank).** The al-ṭiwāl head-block is the corpus's single smoothest
contiguous 4-surah run, and the smoothest *region* of the muṣḥaf is the long-surah head. This is a clean
deterministic corpus fact corroborating the classical al-ṭiwāl grouping.

## Q003-F-01 Arm B — Q 3 is a cohesion anchor of the long-surah head (CONFIRMED)

**Hypothesis (pre-committed):** Q 3 is a cohesion member (not an outlier) of its {Q1-7} window — removing it
*increases* the window's content-dispersion percentile.

- **B-H1 (direction-locked):** delta_pct(X=3) in H-NEW-590 is negative, classification == COHESION_ANCHOR.

**Result:** delta_pct(X=3) = **−15.28**; d̄_W = 0.9154 (with Q3) → d̄_W−X = 0.9462 (without Q3); pct 37.9 →
53.18; **classification = COHESION_ANCHOR** — **B-H1 PASS.**

**Verdict: CONFIRMED.** Removing Q 3 from the {Q1-7} window *raises* its dispersion by 15.28 percentile points
— Q 3 binds the long-surah head together. It is the strongest cohesion anchor of the head after the
corpus-singletons. (Contrast Q 1 al-Fātiḥa, the window's STRONG_OUTLIER at delta_pct +27.09: Q 1 sticks out,
Q 3 binds in.)

## Q003-F-01 Arm C — is the block smoothness beyond chance? (NULL)

**Hypothesis (pre-committed, direction-locked):** the {2,3,4,5} block's mean internal seam is LOWER (smoother)
than a max-statistic permutation null: shuffle the 113 delta_raw values across the 113 seam positions, recompute
the MINIMUM contiguous-4-block mean each perm, compare obs to this distribution (controlling for 111-block
multiplicity).

- **C-H1 (direction-locked):** obs ≤ null distribution of minimum-block means at α = 0.05; p_perm =
  (#{null_min ≤ obs} + 1)/(N+1).

**Result:**
- observed block mean = −0.03196.
- null (10,000 perms): mean of minimum-block-means = **−0.01683**, std 0.0129; **z = −1.174**.
- **p_perm = 0.12319** (1,231 of 10,000 random arrangements produced a smoothest-4-block at least as smooth as
  the observed {2-5} block) — **C-H1 FAIL** (does not clear α = 0.05).

**Verdict: NULL, published with full prominence per PRE-REG-STANDARD-04.** The observed head-block smoothness
is within reach of chance seam-arrangement: ~12% of random 113-seam shuffles produce SOME contiguous 4-block
at least this smooth. **This does NOT retract Arm A** — the {2-5} block IS deterministically the corpus's
smoothest 4-block (rank 1/111). What Arm C shows is that the *degree* of that smoothness is not, by itself,
statistically surprising, because the corpus has many seamless (negative-delta) seams and 111 candidate blocks
to find a minimum over.

**What the NULL teaches (this is a first-class finding).** The al-ṭiwāl block's cohesion is **real and
deterministic** (Arm A rank-1; Arm B cohesion-anchor) but **not anomalously extreme** (Arm C). The classical
al-ṭiwāl grouping correctly identifies the smoothest region of the muṣḥaf — but the project should NOT claim
the smoothness is "beyond chance" at the block level. The honest reading: the long-surah head is the smoothest
4-block AND a content-cohesion anchor, while its statistical surprise is null once block-multiplicity is
controlled. This is a clean instance of distinguishing a **deterministic corpus fact** (Arm A) from a
**statistical-surprise claim** (Arm C) — two different epistemic levels that the protocol requires be reported
separately.

---

## Bonferroni / family summary

Q003-F-01 has one permutation cell (Arm C); α_corrected = 0.05/1 = 0.05. The deterministic cells (A-H1, A-H2,
B-H1) do not consume α.

| Arm / cell | Type | Result | Verdict |
|:--|:--|:--|:--|
| A (A-H1 ∧ A-H2) | deterministic | {2-5} rank 1/111, both seams ≤ median | **CONFIRMED** |
| B (B-H1) | deterministic | delta_pct −15.28, COHESION_ANCHOR | **CONFIRMED** |
| C (C-H1) | permutation (α=0.05) | z=−1.17, p=0.123 | **NULL** |
| **overall** | — | 2 deterministic CONFIRMED + 1 permutation NULL | **SPLIT (honest)** |

## MW protections applied

- **MW-1 (instrument-prior):** mean-internal-seam metric, rank definition, delta_pct sign, and max-statistic
  null all fixed in the pre-reg before any run.
- **MW-2 (corpus-prior):** Arm C used 10,000 permutations of the full 113-seam vector.
- **MW-3 (alternative-models):** Arms A, B, C triangulate the same block-cohesion claim on three different
  instruments (TSP-residual rank, FR-window dispersion, permutation null).
- **MW-5 (replication):** Arms A, B are deterministic and fully replicable from the on-disk JSON; Arm C
  seed-locked at 20260509.
- **MW-6 (instrument-control):** Arm C's max-statistic (minimum over 111 blocks) explicitly controls for the
  multiple-block selection — this is precisely what turned the NULL.
- **MW-7 (post-hoc cap):** the al-ṭiwāl-block claim is classical; promoted to a direction-locked
  pre-registered test before computation.

## Cross-finding integration

- **H-NEW-720 (TSP-residual decomposition)** — Arm A adds the result that the smoothest contiguous 4-block is
  the al-ṭiwāl head {2-5}, and the smoothest *region* of the muṣḥaf is the long-surah head.
- **H-NEW-590 (outlier spectrum)** — Arm B confirms Q 3 as a COHESION_ANCHOR (delta_pct −15.28), complementing
  the Q 1 STRONG_OUTLIER of the same window.
- **Deterministic-fact vs statistical-surprise distinction** — Q003-F-01 is a model case: Arm A (deterministic
  rank-1) is true; Arm C (statistical surprise) is null. Future block-level claims should report both levels.

## Honest limits

- Arm A's rank is on the specific contiguous-4-block-mean metric; a 3-block or 5-block window, or a
  median-instead-of-mean aggregator, would shift the exact ranking (though the al-ṭiwāl head's smoothness is
  robust to these).
- Arm C's NULL is null-definition-dependent: a permutation that preserves the seam autocorrelation structure
  (block-bootstrap) rather than fully shuffling could yield a different p; the full-shuffle max-statistic is
  the pre-committed null and is reported as such.
- Arm B's cohesion-anchor classification is window-definition-dependent (symmetric ±3); see
  `01-empirical-profile.md` §9.

---

*Computed 2026-05-29, seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime.
Script: `scripts/Q003_F_01_tiwal_block.py`; JSON: `csv/Q003-F-01.json`.*
