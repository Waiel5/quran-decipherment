# H-NEW-111 run 1 — 2026-04-17

**Specialist**: h-new-111-specialist
**Task**: Fisher-Rao information-geodesic test of mushaf order
**Seed**: 20260417

## Run log

1. Read pre-reg, locked parameters (K=500, α=0.5, PERMS=10000).
2. Parsed QAC v0.4 STEM-root tokens: 49,968 tokens, 1,642 distinct roots, across all 114 surahs (as expected).
3. Selected top-500 roots by global frequency. Coverage: **91.73%** of all STEM root tokens land in the top-500. Top-5: Alh (اله), qwl (قول), kwn (كون), rbb (ربب), Amn (أمن).
4. Built per-surah count matrix (114×500), applied Dirichlet smoothing α=0.5 per cell, L1-normalized to probability vectors.
5. Computed full 114×114 Fisher-Rao distance matrix (6,441 upper-triangular pairs). Range [0.213, 1.551]. Mean 0.924, median 0.957.
6. L_mushaf = 85.7597.
7. 10,000 random permutations: mean 104.346, sd 1.622, min 98.111. Zero permutations reached L_mushaf. p_primary < 10⁻⁴, z = −11.46.
8. Greedy-NN TSP approximation from all 114 start-nodes: best L = 78.836 (start=53). 2-opt local search tightened to L_min ≈ 77.467.
9. L_mushaf / L_min ≈ 1.107 — near-optimal.
10. Nöldeke order: L_nold = 87.232. Two-sided p = 2×10⁻⁴. Mushaf is shorter than Nöldeke.
11. Tanzil/Egyptian-Std revelation order: L_tanzil = 89.530, even longer than Nöldeke.
12. MW-5 positive control (greedy-NN from surah 1): L = 79.211, p = 1×10⁻⁴. Passes.

## Key surprise

I expected the mushaf to be significantly non-random (the project's prior findings on muqaṭṭāʿat clustering, musabbiḥāt, anchor cluster, etc. imply SOME non-random structure). What I did NOT expect was:

(a) that the mushaf would be **within 11% of TSP-optimum** — this is tight,
(b) that the mushaf would be **shorter than both chronological orderings** — Nöldeke and Tanzil both lose to the mushaf.

This contradicts the naive "chronology is the natural order" framing of historical-critical Quran studies. The mushaf's ordering optimizes consecutive-surah root-distribution continuity BETTER than chronology does.

## Discipline check

- Pre-reg written and SHA-hashed BEFORE results viewed. ✓
- K, α locked in pre-reg frontmatter. ✓
- Bonferroni k=3 declared in YAML. ✓
- Direction locked before running. ✓
- MW-1 (length control via L1 norm) implemented. ✓
- MW-5 (positive control) implemented and fires. ✓
- NULL would have been published with equal prominence had it happened. (Didn't happen — true NULL was nowhere near.)
- PASS-DIRECTED ceiling respected (not claiming CONFIRMED).

## Next steps for the project

1. **H-NEW-112** (independent replication on a distinct feature space): character-n-gram histograms per surah, or verse-length distribution, or divine-name profile.
2. **Robustness**: K ∈ {100, 250, 1000, 2000}, α ∈ {0, 0.1, 1.0}, alternative metrics (Hellinger, JS). If PASS survives variation, elevate confidence.
3. **Sub-structure analysis**: which consecutive pairs contribute MOST to L_mushaf being short? Ranking the 113 consecutive-pair distances may identify design "seams" — consistent with H-NEW-47 (Biqāʿī seam theory).
4. **Cross-check with H-NEW-89 meta-cluster network**: do consecutive mushaf pairs align with the cluster graph?
5. **Concorde-exact TSP**: run `concorde` or `LKH-3` if available to nail down the true L_min — the 2-opt 1.107 ratio is an upper bound; true ratio could be higher.

## Files written

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf-prereg.md`
- `/Users/grey/Downloads/quran/scripts/h_new_111_fisher_rao_mushaf.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md`
- this journal
