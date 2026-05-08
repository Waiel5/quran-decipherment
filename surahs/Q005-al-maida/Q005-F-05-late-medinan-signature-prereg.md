---
finding_id: Q005-F-05
prereg_date: 2026-05-07
prereg_type: multi-axis signature triangulation
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q005 deep-dive (F-01..F-05)
alpha_bon: 0.01
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, FR-roots distance, basmala-counted-only-in-surah-1, Hafs-Kufan, Mashriqi)"
---

# Q005-F-05 — Late-Medinan signature triangulation (FR + sig_A + UAS + rhyme)

## 1. Background

If Q 5 is among the LAST surahs revealed (Egyptian Standard rev #112, Nöldeke #114), its multi-axis architectural signature should resemble the late-Medinan profile (Q 9 rev #113; Q 110 rev #114). The compression-tail-content law (H-NEW-660) predicts d̄_content ≈ 0.96 for early mushaf-position surahs (s ≤ 50). Q 5's mushaf-position is 5 — pre-kink — but its REVELATION position is late. This is a key dissociation.

Empirical question: in 4-axis architectural-signature space {FR-mean-distance, sig_A, sig_B, rhyme-entropy} from H-NEW-111 + H-NEW-750 + H-NEW-840, is Q 5's signature **closer to** (a) the Q 9 + Q 110 late-Medinan centroid than (b) the Q 2 early-Medinan centroid?

## 2. Frozen 4-axis signature

For each surah s, the signature vector is:

```
v(s) = [
  z_FR_mean_dist(s),          # H-NEW-111: mean FR-distance to all other surahs
  z_sig_A(s),                  # H-NEW-750
  z_sig_B(s),                  # H-NEW-750
  z_rhyme_entropy(s),          # H-NEW-750
]
```

Each axis z-normalized over 114 surahs.

## 3. Centroids

- **Late-Medinan centroid LM**: mean of v(Q 9) + v(Q 110). (Q 5 is excluded to avoid self-reference; Q 110 is rev #114, the canonical "last revealed".)
- **Early-Medinan centroid EM**: v(Q 2). (Q 2 is rev #87 Egyptian Standard, early Medinan; al-sabʿ al-ṭiwāl head.)

## 4. Hypothesis (DIRECTION-LOCKED)

**H1 (primary)**: Euclidean distance ‖v(Q 5) − LM‖₂ < ‖v(Q 5) − EM‖₂.

**H1' (auxiliary)**: The above holds for ≥ 3 of the 4 individual axes considered separately.

## 5. Null

**H0**: ‖v(Q 5) − LM‖₂ ≥ ‖v(Q 5) − EM‖₂.

## 6. Method

1. Load FR-mean-distance for each surah from `findings/phase-b-hypotheses/csv/h-new-111.json` (compute mean over the 113 off-diagonal pairs).
2. Load sig_A, sig_B, rhyme_entropy from `h-new-750.json`.
3. z-normalize each axis over 114 surahs.
4. Compute ‖v(Q 5) − LM‖₂, ‖v(Q 5) − EM‖₂.
5. Permutation null: 10000× redraw two random non-Q5 surahs S1, S2 to form a "control LM-prime", and a single random non-Q5 surah S3 as "control EM-prime", and check if ‖v(Q 5) − LM-prime‖ < ‖v(Q 5) − EM-prime‖. p_perm = fraction of permutations where the inequality holds (one-sided lower for our pre-committed direction).
6. Auxiliary check: per-axis distance comparison.

## 7. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| ‖v(Q5)−LM‖ < ‖v(Q5)−EM‖ AND p_perm < α_bon = 0.01 | VINDICATED late-Medinan signature on Q 5 |
| Direction holds but p_perm ≥ α_bon | DIRECTIONAL |
| ‖v(Q5)−LM‖ ≥ ‖v(Q5)−EM‖ | NULL — direction reversed; Q 5 architecturally clusters with Medinan-ṭiwāl head, NOT terminal-Medinan |

## 8. Garden-of-forking-paths log

- The late-Medinan centroid uses {Q 9, Q 110} — the two canonically late surahs that are NOT Q 5 itself. Q 110 is short and creedal — different surface form, but the pre-reg holds because the test is on architectural-signature axes, not surface form.
- Pre-flight observation: Q 5's nearest 5 FR-roots neighbors (from H-NEW-111) are Q 2, Q 3, Q 4, Q 9, Q 6. This means the FR-axis ALONE places Q 5 among the long-Medinan-legal cluster, not the late-Medinan-creedal cluster. The 4-axis test may therefore tilt toward the EARLY centroid on FR alone but the multi-axis result is unknown.
- The pre-registered direction is locked at "Q 5 closer to LM than EM"; if this is reversed, we publish NULL with full prominence — the surah's mushaf-position-driven architectural signature would then DISSOCIATE from its late chronology, and that is a meaningful finding.

## 9. Pre-commit locked.
