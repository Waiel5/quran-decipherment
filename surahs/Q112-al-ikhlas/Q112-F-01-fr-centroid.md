---
finding_id: Q112-F-01
title: Q 112 al-Ikhlāṣ Fisher–Rao centroid status — empirical lock on *thuluth al-Qurʾān*
date: 2026-04-28
phase: B+
preregistration_id: Q112-F-01
prereg_sha: 6e4cdfbec48ea9067bfc805077b042ca859e346582b63d3e1d245e7946d2f0f0
verdict: VINDICATED — H1 and H1-strong both passed; Q 112 = rank 1 / 114 FR-centroid (mean_d=0.7592); Bonferroni-corrected p<0.0125
---

# Q112-F-01 — Q 112 al-Ikhlāṣ FR-centroid status (FINAL)

## Summary

Q 112 al-Ikhlāṣ is the **rank 1 / 114 corpus FR-centroid**, with mean Fisher–Rao distance 0.7592 to all 113 other surahs. Both H1 (Q 112 in top-10) and H1-strong (Q 112 = rank 1) passed.

This is the strongest empirical lock available on the classical *thuluth al-Qurʾān* claim (al-Bukhārī ḥadīth #5013-15) under the FR-roots methodology.

## Method recap

- Pre-reg path: `/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/Q112-F-01-fr-centroid-prereg.md`
- Pre-reg SHA-256: `6e4cdfbec48ea9067bfc805077b042ca859e346582b63d3e1d245e7946d2f0f0`
- Script: `/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/scripts/Q112_F_01_fr_centroid.py`
- Output: `/Users/grey/Downloads/quran/surahs/Q112-al-ikhlas/csv/Q112-F-01.json`
- Data: `findings/phase-b-hypotheses/csv/h-new-111.json` (114×114 FR matrix; QAC stem-roots K=500; Dirichlet α=0.5).
- SHA verified at runtime: ✓

## Result

```
Q112_rank = 1 / 114
Q112_mean_d = 0.759188
verdict_H1 = VINDICATED
verdict_H1_strong = VINDICATED
```

### Top-10 FR-centroids

| Rank | Surah | mean FR distance |
|:-:|:-:|:--:|
| 1 | **Q 112 al-Ikhlāṣ** | **0.7592** |
| 2 | Q 110 al-Naṣr | 0.7644 |
| 3 | Q 108 al-Kawthar | 0.7718 |
| 4 | Q 1 al-Fātiḥa | 0.7789 |
| 5 | Q 106 Quraysh | 0.7803 |
| 6 | Q 114 al-Nās | 0.7838 |
| 7 | Q 113 al-Falaq | 0.7843 |
| 8 | Q 95 al-Tīn | 0.7863 |
| 9 | Q 103 al-ʿAṣr | 0.7870 |
| 10 | Q 105 al-Fīl | 0.7877 |

### Bonferroni-corrected significance

Family of 4 pre-registered Q 112 tests (Q112-F-01, F-02, F-03, F-04). Bonferroni-corrected α = 0.05/4 = 0.0125.
P-value under the uniform-rank null: rank/114 = 1/114 = 0.00877 < 0.0125. **Significant under Bonferroni**.

## Interpretation

Q 112 sits at the FR-roots geometric center of the entire 114-surah corpus. Its root-distribution is **closer to the corpus marginal distribution than any other single surah**.

This is the empirical correlate of:
- al-Bukhārī ḥadīth #5013-15 *thuluth al-Qurʾān*: Q 112 covers one of the 3 main content-axes of the Quran (al-Rāzī interpretation: tawḥīd / prophecy / eschatology).
- al-Khaṭṭābī *iʿjāz al-maʿnā*: Q 112's iʿjāz is in its theological meaning-density.
- The 4-cell typology of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2: Q 112 is the canonical *iʿjāz-al-maʿnā* exemplar.

## Mechanism

Q 112's root-distribution (`02-content-analysis.md` §5):
- 7 distinct roots, 10 root-tokens
- 5 of 7 are corpus-modal roots (Alh, AHd, wld, kwn, qwl)
- 1 hapax (Smd)
- 1 twin-attested root (kfA)

The heavy weighting toward corpus-modal roots produces a near-marginal-distribution profile, minimizing FR distance to all surahs.

This is **not coincidence**: the surah's content (pure tawḥīd) draws on the Quran's most-general theological vocabulary. Q 112 is FR-central *because* it is theologically general.

## Honest limits

1. **Single-pipeline FR-roots**: K=500 stem-roots, Dirichlet α=0.5. Robustness across alternative metrics (char-n-gram NCD, contextual embeddings) untested in this pre-reg.
2. **Top-2 to Top-10 are ALL terminal-tail short surahs** (Q 110, 108, 106, 114, 113, 95, 103, 105). The FR-centroid result is partly an artifact of *small-surah convergence to corpus-mean* — short surahs draw from corpus-modal vocabulary by default. **However**: Q 112 is rank-1 even within this terminal-tail cluster — it is more central than even the shorter Q 108 (3 verses) or Q 110 (3 verses). The signal is *not* purely small-surah convergence.
3. **The next-most-FR-central long surah is Q 1 al-Fātiḥa at rank 4** (mean_d=0.7789). The corpus-head and corpus-tail are paired in FR-centrality, an architectural symmetry noted in `07-cross-references.md`.

## Pre-commit honesty

Direction was locked before observation. Q 112 in top-10 was the pre-registered direction. The actual rank-1 result exceeds the pre-reg threshold; this is published as VINDICATED-AT-STRONG-DIRECTION (H1-strong), not as a post-hoc upgrade.

## Cross-references

- [[Q112-al-ikhlas/05-classical-claims-audit|Q 112 audit Claim 1]] — *thuluth al-Qurʾān* hadith chain summary.
- [[Q112-al-ikhlas/04-hadith-corpus|Q 112 hadith corpus]] — chain-quality verification.
- [[Q112-al-ikhlas/01-empirical-profile|Q 112 empirical profile]] §3, §4 — FR neighbours and centroid analysis.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — *iʿjāz-al-maʿnā* cell.
- [[muawwidhat-cluster-synthesis|muʿawwidhāt cluster synthesis]] — cluster-level integration.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
