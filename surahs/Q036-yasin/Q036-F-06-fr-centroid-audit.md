---
surah: 36
finding_id: Q036-F-06
title: "Heart of the Qurʾān" empirical FR-centroid audit — Q 112 confirmed, Q 36 mid-pack
date: 2026-05-09
phase: B+
verdict: PASS-DIRECTED-REAFFIRMED
pre_reg_sha256: 69c0782025c1ae13c951fd5ab019f5ce1ca34591042c987c881c39b5c301a4b1
---

# Q036-F-06 — Q 36 is NOT the corpus FR-centroid; Q 112 is


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Background and pre-committed direction

The classical *qalb al-Qurʾān* tradition (al-Tirmidhī idInBook=2970, isnād-weak per al-Tirmidhī's own grading) names Q 36 as the "heart of the Qurʾān". The project has tested this on:

- 6 axes by [[h-new-82-yasin-heart|H-NEW-82]] (positional, lexical-centroid, eigenvector, theme) — **0/6 PASS**.
- 1 axis by Q036-F-01 (liturgy-weighted Jaccard) — **NULL**.

This pre-reg adds an 8th: the project-canonical Fisher-Rao distance centroid (H-NEW-111 D-matrix, K=500 truncation, Dirichlet α=0.5 smoothing). The pre-committed direction was: **Q 112 in top-3, Q 36 outside top-30**.

## Result

| Surah | Mean FR distance to corpus | Rank |
|:--|:-:|:-:|
| **Q 112 al-Ikhlāṣ** | **0.7592** | **1/114** |
| Q 1 al-Fātiḥa | 0.8240 | 2/114 |
| Q 113 al-Falaq | (top-10) | 7/114 |
| Q 114 al-Nās | (top-10) | 6/114 |
| Q 109 al-Kāfirūn | (top-10) | 4/114 |
| **Q 36 Yāsīn** | **0.9430** | **64/114** |

(Top-10 full list in `csv/Q036-F-06.json`.)

**Both pre-committed conditions hold**:
- Q 112 rank 1 ≤ 3 ✓
- Q 36 rank 64 ≥ 30 ✓

**Verdict**: **PASS-DIRECTED-REAFFIRMED**. The classical *qalb al-Qurʾān* claim, in its quantitative-FR-centrality form, is NULL'd on yet another axis (now 8 independent operationalisations, 0 PASS). The empirical corpus FR-centroid is Q 112 al-Ikhlāṣ, not Q 36.

## Interpretation

The metric is **biased toward short-and-theologically-broad** surahs: Q 112's high-frequency theological-core vocabulary (`Alh`, `Hd`, `SmD`, `wld`, `kfA`) shares roots with most other surahs because those roots are nearly universal. This is the standing reading of [[Q112-F-01|Q112-F-01]] which originally locked Q 112's rank-1 status at p < 0.0125 (Bonferroni-4).

Q 36 ranks 64/114 — slightly below corpus median. This is consistent with its **mid-pack architectural profile** documented across the H-NEW corpus (UAS rank 35, outlier-strength weak-anchor, sig_A rank 80, sig_B rank 85). Q 36 is well-integrated into the corpus, but it is not maximally central by any quantitative measure.

The classical hadith's status as a **theological-and-liturgical** claim (Q 36's centrality in *fadāʾil* practice and its eschatology presentation) is not addressed here; that claim is on a different axis from FR-centrality and is queued under cross-finding-026's *iʿjāz-al-maʿnā* cell typology (where Q 36's nearest fadāʾil-10 peer is Q 67, not Q 1/Q 2 — see Q036-F-02).

## Honest limits

- The H-NEW-111 metric uses Dirichlet smoothing at α=0.5 with K=500-root truncation. Under different smoothing or truncation, the rank ordering of mid-pack surahs (Q 36 included) is mildly perturbed but the top-3 centroid identification (Q 112 #1) is rules-tuple-stable.
- Mean FR is one of several centrality measures; a graph-theoretic eigenvector-centrality variant is in [[h-new-82-yasin-heart|H-NEW-82]] (also NULL on Q 36).
- Q 36's mid-pack rank does NOT mean Q 36 is structurally insignificant; it means Q 36 is **representative**, not **central**. These are distinct properties.

## What this resolves

The classical *qalb al-Qurʾān* claim, on the **8 quantitative-centrality axes** the project has now tested, returns **0/8 PASS** for Q 36. The 1400-year-old liturgical tradition (Q 36 recited over the dying, Q 36's high *fadāʾil*-grade) is real and well-attested in our hadith corpus — but it is **not corroborated** by quantitative-centrality measures. The disconnect between liturgical-centrality and quantitative-centrality is itself an empirical fact about how the corpus is structured: liturgy-weight is orthogonal to root-distribution-centrality.

This is consistent with the dual-iʿjāz typology of [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]: structural-iʿjāz (al-Bāqillānī axis, UAS-driven) is empirically distinct from meaning-iʿjāz (al-Khaṭṭābī axis, liturgy-driven). Q 36 sits firmly on the meaning-iʿjāz axis and absents itself from the structural-iʿjāz top tier.

## Cross-references

- [[Q112-F-01|Q112-F-01]] — Q 112 FR-centroid rank-1 finding (the binding prior; this audit reaffirms).
- [[h-new-82-yasin-heart|H-NEW-82]] — the binding 6-axis NULL on Q 36 *qalb al-Qurʾān*; this audit adds an 8th axis.
- Q036-F-01 — the 7th axis (liturgy-weighted Jaccard) NULL.
- Q036-F-02 — Q 36 belongs to the meaning-iʿjāz cell (nearest fadāʾil-10 peer = Q 67).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — dual-iʿjāz typology.

## Output

- `csv/Q036-F-06.json` — full JSON including top-10 centroid table and median-rank cross-check.

*Pre-reg sha-256 `69c0782025c1ae13…b5c301a4b1` verified at runtime.*
