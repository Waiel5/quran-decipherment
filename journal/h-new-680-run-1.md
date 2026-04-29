---
id: H-NEW-680
run: 1
date: 2026-04-28
script: scripts/h_new_680_multi_k_compression_tail.py
prereg: findings/phase-b-hypotheses/h-new-680-multi-k-compression-tail-prereg.md
prereg_sha: 316642e9ac0839a63f9f3817e048565ca393b944161fa00e0c4d38874a572c46
seed: 20260434
n_perms_per_K: 10000
---

# H-NEW-680 — Run 1 journal

## What was tested

Generalize the H-NEW-660 single-parameter compression-tail law from K=15 to K ∈ {7, 11, 22}.

Methodology mirrors `h_new_660_compression_tail_gradient.py`:
- FR distance matrix from `csv/h-new-111.json` (114 surahs).
- For each K: 114−K+1 consecutive windows, d̄ via mean pairwise FR distance.
- Three baseline models: linear, quadratic, two-piece-kink.
- Coarse two-piece on grid {25, 50, 75} (matches H-NEW-660 protocol).
- Refined two-piece on grid {25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75} (kink-position CI).
- 10000 permutations per K (random seed `SEED + K` for distinct streams; SEED = 20260434).
- Bonferroni-3 within K (α=0.01667), Bonferroni-3 across K (α=0.00556 — tightening, self-verifies per `feedback_bonferroni_tightening_vs_loosening`).

## Results

| K | linear R² | quadratic R² | two-piece (s=50) R² | two-piece refined kink → R² | β refined | perm p (primary) |
|:-:|:-:|:-:|:-:|:--|:-:|:-:|
|  7 | 0.7459 | 0.9523 | 0.9485 | s=55 → 0.9582 | −0.01265 | <10⁻⁴ |
| 11 | 0.7627 | 0.9712 | 0.9757 | s=55 → 0.9803 | −0.01338 | <10⁻⁴ |
| 22 | 0.7704 | 0.9829 | 0.9933 | s=50 → 0.9933 | −0.01337 | <10⁻⁴ |

All three K values clear:
- R² ≥ 0.50 (primary model) at every K
- p ≤ α_within = 0.01667 (within-K Bonferroni-3)
- p ≤ α_cross = 0.00556 (across-K Bonferroni tightening)
- β < 0 at every K (post-kink slope negative)
- refined kink ∈ [50, 55] at every K (within the locked ±10 window of s=50)

Refined-kink spread = 5 surahs (max 55 − min 50 = 5).

## Per-K kink profile (R² vs candidate kink, refined grid)

K=7 peak at kink=55 (R²=0.9582); K=11 peak at kink=55 (R²=0.9803); K=22 peak at kink=50 (R²=0.9933). Profile shape is unimodal at every K with monotonic ascent from kink=25 → peak and descent past peak.

The K=7 and K=11 R² peak slightly favors s=55 over s=50 (Δ = 0.0097 and 0.0046 respectively); K=22 peaks exactly at s=50. As K grows, the kink slides leftward toward 50 and the curve sharpens. Interpretation: smaller K is more sensitive to local Medinan-ṭiwāl content (Q 57-66 is dense), shifting the empirical kink slightly downstream of the Hijra. Larger K averages over the Q 50-71 region and locks the kink at 50.

## Best/worst windows

| K | best window | best d̄ | worst window | worst d̄ | compression ratio |
|:-:|:--|:-:|:--|:-:|:-:|
|  7 | Q 106-112 | 0.2956 | Q 53-59  | 1.0643 | 3.60× |
| 11 | Q 103-113 | 0.3020 | Q 47-57  | 1.0148 | 3.36× |
| 22 | Q 93-114  | 0.3729 | Q 37-58  | 0.9803 | 2.63× |

Worst windows at all three K straddle the Q 56/57 Hijra boundary. Best windows at all three K terminate at or near Q 114, anchoring the canonical mufaṣṣal-qiṣār core.

## Verdict

STRICT PASS (SCALE-INVARIANT). The two-piece-kink-near-50 single-parameter law is robust across K ∈ {7, 11, 22}.

## Honest divergence to report

At K=7 and K=11, the refined-grid R²-maximizing kink is s=55 rather than s=50. The Δ(R²) between kink=50 and kink=55 is ≤ 0.01 in both cases — visually a flat plateau between s=50 and s=55. The mass of the kink is in the [45, 60] interval at every K. This is consistent with the Hijra hinge being a transition *zone* (Q 50/al-Qāf through Q 60-ish), not a single sharp surah. The K=22 result locks the canonical kink position at s=50 unambiguously.

## Files written

- `findings/phase-b-hypotheses/h-new-680-multi-k-compression-tail-prereg.md` (SHA 316642e9ac0839a63f9f3817e048565ca393b944161fa00e0c4d38874a572c46)
- `scripts/h_new_680_multi_k_compression_tail.py`
- `findings/phase-b-hypotheses/csv/h-new-680.json`
- `findings/phase-b-hypotheses/h-new-680-multi-k-compression-tail.md`
- `journal/h-new-680-run-1.md` (this file)
- `journal/h-new-680-run-1.log`
