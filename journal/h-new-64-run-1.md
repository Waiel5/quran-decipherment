---
run: H-NEW-64 run-1
date: 2026-04-15
seed: 20260416
outcome: NULL (positive control VALID)
---

# H-NEW-64 Run-1 Journal

## Timeline

- 2026-04-15 (re-dispatch after rate-limit) — Read pre-reg (already
  written before run). LOCKED specs reviewed.
- Verified loader, verse counts (sum 6,236 from hafs-verse-counts.tsv
  col 2), and proper-noun list (no-tashkeel skeleton form).
- Wrote `scripts/h_new_64_juz_boundaries.py`. Built corpus from
  `quran-no-tashkeel.json` via the canonical loader; converted the
  30 juzʾ (surah, verse) starts to global positions; verified all 30
  exist.
- Per-verse precomputation: tokens (whitespace), lengths, last-token
  rhyme bucket (rightmost 2 Arabic letters), proper-noun count
  (substring sum over closed list).
- Computed 4 axis statistics on the 29 juzʾ-internal boundaries.
- Ran 1,000-permutation null with random.sample over POS_VALID =
  {2..6235} \ {surah-start positions} (avoids surah seams in null,
  per pre-reg).
- Computed Bonferroni-corrected p-values (α = 0.01) and joint
  Σz statistic with own null.
- Ran MW-5 positive control: 29 surah-seam positions sampled
  deterministically from the 113 internal seams.
- Per-boundary S_joint ranking computed against per-position
  flat-mean / flat-sd of all null samples (to give a per-boundary
  z-score; SUM-level mean/sd is for the SUM_X-level test).

## Garden-of-forking-paths log (committed BEFORE run)

- Window w = 10: pre-reg LOCKED.
- Per-boundary z-score uses null-flat-mean / null-flat-sd of D_X(p)
  (vs SUM_X mean/sd which is for the SUM-level test). This is the
  natural reading of the pre-reg's "z_X(p) against null_mean_X" for
  the descriptive ranking. Decision committed before viewing rank.
- Surah-seam positions for positive control: deterministic
  random.sample(seed=20260416), no replacement, 29 of 113.
- Proper-noun list rendered in no-tashkeel skeleton (e.g., "ابراهيم"
  not "إبراهيم"; alif normalization). Substring matching as specified.
- No window-edge alteration: truncate at corpus edges, document.

## Key numeric results

- Verdict: **NULL**.
- Positive control: **VALID** (3 of 4 axes exceed observed; A, B, D
  each p < 0.001).
- Axis A (topic): SUM_obs = 26.08, p = 0.860 (FAIL).
- Axis B (rhyme): SUM_obs = 13.10, p = 0.531 (FAIL).
- Axis C (proper-noun): SUM_obs = 12.05, p = 0.014 (FAIL Bonf 0.01;
  marginal trend).
- Axis D (length): SUM_obs = 5.54, p = 0.264 (FAIL).
- Joint Σz: obs = 1.82, p = 0.196 (FAIL).
- Mean S_joint: surah-aligned (n=7) +3.44 vs intra-surah (n=22) −0.67.

## Interpretation

The juzʾ partition is a recitation length-balancer; it does not
prefer natural structural seams. The only juzʾ boundaries that LOOK
natural are the 7 that happen to coincide with surah seams, and they
inherit naturalness from the surahs, not the juzʾ system.

NULL is published with identical prominence per project policy.

## Pipeline integrity

- Positive control: VALID (3/4 axes pass at p < 0.001).
- Bonferroni correction applied (α_Bonf = 0.01).
- Single global RNG seed.
- All decisions logged before viewing per-boundary ranking.

## Files written

- `scripts/h_new_64_juz_boundaries.py`
- `findings/phase-b-hypotheses/csv/h-new-64.json`
- `findings/phase-b-hypotheses/h-new-64-juz-boundaries.md`
- `journal/h-new-64-run-1.md` (this file)
