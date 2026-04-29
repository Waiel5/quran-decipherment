# H-NEW-203 — Run 1 journal

Date: 2026-04-17
Seed: 20260419
Script: `scripts/h_new_203_juz_fisher_rao.py`
Pre-reg: `findings/phase-b-hypotheses/h-new-203-prereg.md` (SHA-256 `479984febf64ea1a903d1e2a753c2332a2ba2dc0c0fbbc4e45fe86f26e7b7423`)

## Setup

Parent findings consulted: H-NEW-111 (surah-level FR path), H-NEW-127 (verse-level FR within 5 surahs), H-NEW-130 (surah-pair FR residuals), H-NEW-64 (juzʾ-boundary 4-axis test). H-NEW-203 extends these into a full verse-level FR analysis aligned to the 30-juzʾ classical partition.

Feature choice (locked in pre-reg before any H-NEW-203 FR computation): QAC v0.4 STEM root tokens, top-K=500 globally, Dirichlet α=0.5 smoothing, Fisher-Rao angular distance, W=20 verse half-window. All parameters inherited from H-NEW-111/127 except W which was newly chosen (rationale: median juzʾ ~ 208 verses → 40-verse window = ~19% of median juzʾ = local scale).

## Run

One production run, 10000 permutations per test, deterministic. Numpy-vectorized (cumsum-based pooling for O(n) precomputation of all 6235 cut distances). Total runtime ~65 seconds.

## Results

- T1 (boundary concentration) p = 0.00040, z = +3.12, PASS.
- T2 (segment coherence) p = 0.99990, z = +3.56, FAIL-with-sign-reversal.
- S2 (surah-seam-matched null) p = 0.00050, z = +3.22 — T1 robust.
- S4 (MW-5 scramble) obs - scramble = +2.31 null-SD — instrument discriminative.

Verdict: **BOUNDARY-ONLY** (PASS-DIRECTED).

## Key observations

1. T1 effect survives surah-seam-matched null. The 22 intra-surah juzʾ cuts (not just the 7 surah-aligned ones) contribute.
2. T2 sign reversal is the novel finding: placing cuts AT big jumps guarantees segments that straddle the variance at those cuts, yielding LOWER segment coherence than cuts placed in uniform regions. The juzʾ partition IS a boundary-placing scheme, not a segment-optimizing scheme.
3. Juzʾ 30 (ʿamma) is the *least* coherent juzʾ AND one of two boundaries (with juzʾ 27) not in the top half of FR jumps. The "juzʾ ʿamma" is classical in length terms, not in root-distribution terms.
4. Juzʾ boundaries 29, 3, 15, 5, 13 are the most structurally prominent — interesting mix of surah-aligned (29, 15) and intra-surah (3, 5, 13).

## Garden of forking paths

- During smoke testing (N_PERM=50 and N_PERM=100), I identified Python-loop pace was too slow for the pre-registered 10000-perm budget. Switched from pure-Python to numpy-vectorized implementation. The MATH is unchanged — same formula, same seed, same parameter values. Verified via N_PERM=200 check that numpy output matched pure-Python output on the test-1 observed value (23.1015) and on null mean/SD to 3 decimal places. This is a numerical-identity refactor, NOT a methodology change, and occurred AFTER pre-reg but BEFORE the 10k production run.
- No other deviations.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-203.json`
- `findings/phase-b-hypotheses/h-new-203-fisher-rao-juz.md`
