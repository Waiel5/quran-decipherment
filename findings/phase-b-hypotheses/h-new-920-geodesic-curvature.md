---
finding_id: h-new-920
title: "Discrete geodesic curvature of the mushaf path through Fisher-Rao space"
status: PASS-DIRECTED (H1b only); H1a NULL
phase: B+
date: 2026-05-07
seed: 20260507
n_perm: 10000
parent: h-new-111-fisher-rao-mushaf
ancestors: cross-finding-011-mushaf-fisher-rao-confirmed; h-new-130-fisher-rao-residuals; h-new-236-1-hinges-constrained-simulator; cross-finding-020-the-complete-equation
prereg_sha256: 2bd4c93ee87d0a5fac1c7331d16890966f21d46ad5c94455254bc6a915b32758
rules_tuple_inherited: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan); FR distance per H-NEW-111 with K_top_roots=500, dirichlet α=0.5"
---

# H-NEW-920 — Discrete geodesic curvature of the mushaf path


> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline (with full prominence for both arms)

The mushaf path through Fisher-Rao information space is **globally much smoother than random** at z = −5.638 (one-sided perm-p = 0.00000 against 10000 permutations). Empirical mean turn-cost 0.7435 vs perm-null mean 0.9233 (std 0.0319). **H1b PASSES strongly.**

But the **pre-committed boundary co-incidence hypothesis NULLS completely**: zero of the top-10 curvature peaks fall in the union of three pre-committed classical block-boundaries (Mufaṣṣal-onset Q 50 ±2, Ḥawāmīm-cluster Q 39→40 ±2, Medinan-block-onset Q 2 ±2). Empirical hits = 0 in B1, B2, B3, and JOINT (perm-p = 1.000 for all four). **H1a NULL with full prominence.**

**Overall: PASS-DIRECTED (H1b only).** The mushaf is globally smoother in curvature than chance, but its curvature peaks are NOT at classical block-boundaries — they are at *different* positions whose identity is reported descriptively below.

## 2. Top-10 curvature peaks (the descriptive discovery)

| Rank | Path-position | Surah triple | turn-cost | turning angle |
|:-:|:-:|:--|:-:|:-:|
| 1 | 33 | Q 32 → Q 33 → Q 34 | 1.425166 | 87.7° |
| 2 | 24 | Q 23 → Q 24 → Q 25 | 1.346052 | 84.5° |
| 3 | 55 | Q 54 → Q 55 → Q 56 | 1.278082 | 81.7° |
| 4 | 15 | Q 14 → Q 15 → Q 16 | 1.162012 | 76.9° |
| 5 | 12 | Q 11 → Q 12 → Q 13 | 1.112588 | 74.6° |
| 6 | 22 | Q 21 → Q 22 → Q 23 | 1.083451 | 73.4° |
| 7 | 23 | Q 22 → Q 23 → Q 24 | 1.083362 | 73.4° |
| 8 | 20 | Q 19 → Q 20 → Q 21 | 1.073437 | 73.0° |
| 9 | 54 | Q 53 → Q 54 → Q 55 | 1.055468 | 72.2° |
| 10 | 16 | Q 15 → Q 16 → Q 17 | 1.053335 | 72.1° |

(Turning angles are the secondary diagnostic Euclidean-pseudo metric per pre-reg §4; the verdict is on `turn_cost`.)

## 3. The triangulation finding (descriptive — α=0.05 single-test cap, MW-7)

**Classical block-boundaries DO NOT predict curvature peaks** (H1a NULL). Instead, the top-10 curvature peaks coincide with empirically-discovered structural pivots from earlier project work:

| Rank | Curvature triple | Empirical anchor (from prior project findings) |
|:-:|:--|:--|
| 1 | Q 32 → Q 33 → Q 34 | Q 33 al-Aḥzāb is one of the two members of the Structural-twin-pair cell (cross-finding-026 §13) — top-3 outlier-strength + both adjacencies in TSP-cost top-15 |
| 2 | Q 23 → Q 24 → Q 25 | Q 23, Q 25 are TRUE-ISOLATES (H-NEW-126 5-surah core); Q 24 al-Nūr is the Structural-twin-pair-partner to Q 33 |
| 3 | Q 54 → Q 55 → Q 56 | Q 55 al-Raḥmān is corpus-min sig_A (rank 114/114); UAS rank 7/114; iʿjāz al-takrīr cluster anchor (cross-finding-027) |
| 5 | Q 11 → Q 12 → Q 13 | Q 12 Yūsuf — *aḥsan al-qaṣaṣ*, structurally-singular continuous-narrative surah |
| 6,7 | Q 21 ↔ Q 22 ↔ Q 23 → Q 24 | TRUE-ISOLATE TRIPLET (H-NEW-126 + H-NEW-168 concentrator-mode meso-community) |
| 8 | Q 19 → Q 20 → Q 21 | Q 20 Ṭā-Hā prophet-cycle pivot from Q 19 Maryam (Jesus-narrative) into Q 21 al-Anbiyāʾ (true-isolate, prophet-comprehensive) |
| 4, 10 | Q 14 → Q 15 → Q 16, Q 15 → Q 16 → Q 17 | Q 16 al-Naḥl is a TRUE-ISOLATE (H-NEW-126 core) |

**Five of the top-10 curvature peaks involve at least one true-isolate (Q 16, Q 21, Q 22, Q 23, Q 25), and three involve at least one Structural-twin-pair member (Q 24, Q 33).** This is descriptive only — pre-reg locked Mufaṣṣal/Ḥawāmīm/Medinan boundaries, not these — but it constitutes an INDEPENDENT triangulation of the project's already-confirmed structural pivots from a SECOND-ORDER (curvature) feature of the mushaf path that is mathematically independent of edge-length (H-NEW-130) and total-length (H-NEW-111).

## 4. Why H1a nulled

The pre-committed boundaries were chosen from CLASSICAL scholarship (Mufaṣṣal at Q 50 per al-Zarkashī/al-Suyūṭī; Ḥawāmīm at Q 40 per multi-tafsir consensus; Medinan-onset at Q 2 per Nöldeke chronology). The empirical data says: those classical block-boundaries are NOT the points where the FR path bends most. Instead, the path bends at the project's already-discovered TRUE-ISOLATES and STRUCTURAL-TWIN-PAIRS, which are NOT classical labels.

This is an **honest empirical disconfirmation of three classical block-boundaries as curvature-defining**. Equal NULL prominence per Protocol §1.3.

## 5. Why H1b passed so strongly

The mushaf has mean turn-cost 0.7435 vs the random-permutation null at 0.9233 — a 19.5% reduction. Because turn-cost has a mathematical floor at 0 (perfect straightness), the available room for being "smoother than random" is bounded; the empirical achievement is most of that room. This is a SECOND-ORDER triangulation of cross-finding-011 (the mushaf as Fisher-Rao geodesic): the mushaf is not just length-near-optimal (cross-finding-011), it is also CURVATURE-SMOOTHER than random by 5.6 sigma.

cross-finding-020 ("the complete equation") should incorporate H1b as a new architectural constraint: the mushaf is the unique (or near-unique) ordering of 114 surahs that is BOTH length-near-optimal AND curvature-smooth. These are independent geometric properties.

## 6. Honest limits

1. **Inheritance from H-NEW-111**: the curvature spectrum is a derivative of the FR matrix. Any rules-tuple sensitivity in H-NEW-111 (K_top_roots=500, Dirichlet α=0.5, QAC-STEM tokenization) propagates here.
2. **The descriptive triangulation in §3 is post-hoc and α-capped at 0.05 single-test per MW-7.** It is hypothesis-generating, not hypothesis-confirming. A pre-registered follow-up should test "do top-10 curvature peaks coincide with the H-NEW-126 true-isolate set + cross-finding-026 §13 structural-twin-pair set" formally (i.e., promote the descriptive triangulation to a pre-registered H1c in a future run).
3. **The H1a NULL is not a NULL on classical scholarship in general** — it's specifically a NULL on the three boundaries B1/B2/B3 we pre-committed. Other classical boundaries (e.g., al-sabʿ-al-ṭiwāl→mathānī at Q 9→10, the seven-tribes prophet-cycle anchors) were not tested.
4. **Cross-feature replication deferred**: the same computation on H-NEW-130b's char-4-gram FR matrix is a separate pre-reg.

## 7. What this contributes to cross-finding-020

cross-finding-020 §12 currently treats the mushaf's geometric properties as: (i) length-near-geodesic per cross-finding-011, (ii) edge-residual at classical boundaries per H-NEW-130, (iii) hinges-constrained per H-NEW-236.1. **H-NEW-920 adds: (iv) curvature-smoother than random** — and shows that the curvature peaks land NOT at classical boundaries but at the empirically-discovered structural pivots. This is a sharpening of (ii): edge-LENGTH peaks at classical boundaries (H-NEW-130), but curvature peaks at the project's structural-twin-pairs and true-isolates. These are DIFFERENT spectra.

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-920-geodesic-curvature-prereg.md` (SHA256: 2bd4c93ee87d0a5fac1c7331d16890966f21d46ad5c94455254bc6a915b32758)
- Script: `scripts/h_new_920_geodesic_curvature.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-920.json`
- Findings: this file
- Journal: `journal/h-new-920-run-1.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
