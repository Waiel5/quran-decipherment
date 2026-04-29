---
id: h-new-750-run-1
date: 2026-04-28
finding: H-NEW-750
seed: 20260445
prereg_sha: 766439fa44444bca5573929085cec998d6409c25e7f91a9481a840ae239b4e88
verdict: DIRECTIONAL — 3/6 pre-commits hit; cross-measure ρ=+0.8696
---

# H-NEW-750 — Per-surah iʿjāz-signature run journal

## Setup

- Pre-reg locked at SHA `766439fa44444bca5573929085cec998d6409c25e7f91a9481a840ae239b4e88` BEFORE script construction.
- Two measures committed in pre-reg:
  - **A**: z(rhyme_entropy) − z(mean_content_distance_to_others)
  - **B**: z(rhyme_entropy) + z(local_cohesion ±2 mushaf-neighbors)
- Six pre-commits: Q 112 top-5, Q 113/114 top-15, Q 1 top-30, Q 2 bottom-15, Q 33 bottom-30.
- Bonferroni-2 α = 0.025 (two measures).
- Seed 20260445.

## Data sources

- `findings/phase-b-hypotheses/csv/h-new-111.json` — Fisher-Rao D matrix (114×114, upper-tri).
- `quran-text/quran-no-tashkeel.json` — verse texts for final-letter extraction.
- 28-letter Arabic basis + variant normalization adopted from H-NEW-700 (`get_final_letter()` ported).

## Run

Single execution of `scripts/h_new_750_per_surah_iʿjāz.py`. SHA matched expected.

## Headline numbers

| Metric | Value |
|:--|:-:|
| Cross-measure Spearman ρ | **+0.8696** (STRONG agreement) |
| Pre-commit hits (Measure A) | 3/6 |
| Pre-commit hits (Measure B) | 2/6 |
| Pre-commit hits (EITHER) | 3/6 |
| Verdict | DIRECTIONAL |

## Top-5 + bottom-5 (Measure A)

**Top-5**: Q 86 (+3.020), Q 84 (+2.809), Q 89 (+2.226), Q 96 (+2.111), Q 82 (+1.942).

**Bottom-5**: Q 55 (−3.173), Q 4 (−3.146), Q 33 (−2.966), Q 17 (−2.396), Q 18 (−2.395).

## Top-5 + bottom-5 (Measure B)

**Top-5**: Q 106 (+3.433), Q 113 (+3.243), Q 86 (+2.375), Q 102 (+2.191), Q 109 (+2.158).

**Bottom-5**: Q 54 (−2.131), Q 33 (−2.085), Q 48 (−2.014), Q 25 (−1.924), Q 18 (−1.922).

## Pre-commit verifications

| Surah | Pred | Rank A | Rank B | A-hit | B-hit | EITHER |
|:--|:--|:-:|:-:|:-:|:-:|:-:|
| Q 112 al-Ikhlāṣ | top-5 | 54 | 18 | MISS | MISS | **MISS** |
| Q 113 al-Falaq | top-15 | 7 | 2 | HIT | HIT | **HIT** |
| Q 114 al-Nās | top-15 | 60 | 21 | MISS | MISS | **MISS** |
| Q 1 al-Fātiḥa | top-30 | 24 | 87 | HIT | MISS | **HIT** |
| Q 2 al-Baqara | bottom-15 | 85 | 60 | MISS | MISS | **MISS** |
| Q 33 al-Aḥzāb | bottom-30 | 112 | 113 | HIT | HIT | **HIT** |

**3/6 EITHER-hits.** STRICT (≥4) NOT met; DIRECTIONAL (≥3) met.

## What was learned

1. **Q 112 al-Ikhlāṣ is monorhyme** (4 verses all ending in د → Shannon entropy = 0). The "compact-rhyme" framing in the prereg was wrong: the entropy measure fundamentally penalizes monorhyme. The pre-commit failure is highly informative.

2. **Q 114 al-Nās is also monorhyme** (6 verses all ending in س). Same issue.

3. **The empirical iʿjāz cluster is mid-mufaṣṣal, not very-end**: Q 84, 86, 89, 100, 106, 113 (intersection top-10 across both measures). This is al-Suyūṭī's *al-mufaṣṣal al-mutawassiṭ*, not the *qiṣār-jiddan*.

4. **Q 33 al-Aḥzāb hit hard at the bottom**: rank 112 / 113. 99% alif-final + high content-distance.

5. **Q 2 al-Baqara missed the bottom-15**: it ranks 85 / 60. Despite size, its rhyme-entropy (1.011) is unexpectedly high — top final letter ن at only 0.67. Q 2 is *long-mixed-register* but not *rhyme-uniform-and-content-mixed*.

6. **Q 1 al-Fātiḥa is GLOBALLY iʿjāz-signed (rank 24 by A) but LOCALLY orphaned (rank 87 by B)** — its ±2 mushaf-neighbors (Q 2, Q 3) are content-distant, breaking the local-cohesion measure.

7. **Cross-measure ρ = +0.87** — the rank concept is metric-stable even when specific predictions fail.

## Architecture insight

At per-surah level, three distinct types emerged:

| Type | Content | Rhyme | Examples |
|:--|:--|:--|:--|
| iʿjāz al-fawāṣil proper | central | diverse | Q 84, 86, 89, 100, 106, 113 |
| iʿjāz al-maʿnā / creedal monolith | central | minimal | Q 112, 114 |
| anti-iʿjāz / ṭiwāl-mixed | peripheral | uniform | Q 17, 18, 33, 48, 54 |

The window-level finding could not see this bifurcation.

## Discipline

- ONE-text discipline maintained (no spelling/edition variants invoked).
- NULL/MISS reported with equal prominence as PASS/HIT.
- Pre-commit FAILURE for Q 112 reported honestly as INFORMATIVE.
- All classical anchors named with primary work + author for top-10.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-750-per-surah-iʿjāz-signature-prereg.md`
- Script: `scripts/h_new_750_per_surah_iʿjāz.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-750.json`
- Findings: `findings/phase-b-hypotheses/h-new-750-per-surah-iʿjāz-signature.md`

## Queued follow-ups (for next session)

- H-NEW-751: normalized rhyme entropy (entropy / ln(n_distinct_letters)) — would Q 112 then top-5?
- H-NEW-752: distinct-letter-count rhyme metric (unweighted).
- H-NEW-753: formal 3-cluster k-means on (mc_dist, rh_ent) plane.
- H-NEW-754: muʿallaqāt control (per-poem rhyme entropy & content centrality).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
