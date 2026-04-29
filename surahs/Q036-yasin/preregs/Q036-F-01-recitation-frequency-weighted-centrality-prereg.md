---
finding_id: Q036-F-01
title: "Q 36 Yāsīn under recitation-frequency-weighted-centrality (the 7th axis explicitly excluded by H-NEW-82)"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 20260428
n_perm: 10000
bonferroni_k: 7
alpha_raw: 0.05
alpha_bonferroni: 0.00714
direction: positive (Q 36 expected to score above corpus-mean centrality under liturgy-weighting; explicit comparison to Q 112 al-Ikhlāṣ corpus FR-centroid)
---

# Q036-F-01 — Recitation-frequency-weighted centrality

## Hypothesis

The classical *qalb al-Qurʾān* claim was empirically tested at multi-axis quantitative form by [[h-new-82-yasin-heart|H-NEW-82]] and **NULL-ed at 0/6 axes**. H-NEW-82's pre-reg explicitly excluded **"recitational frequency in classical practice (a liturgy-weighted centrality)"** as a possible salvage axis — flagged as a possible follow-up.

This pre-reg defines and tests that 7th axis. The hypothesis: under a centrality measure that weights each surah by its **classical-tradition recitation frequency**, Q 36 scores in the top-quintile (rank ≤ 23/114) on liturgy-weighted lexical centrality.

## Locked operationalisation of "recitation frequency"

We use the project's [[h-new-860-hadith-architectural-alignment|H-NEW-860]] hadith-fadāʾil rubric as the recitation-frequency proxy. The rubric is a 0-10 score per surah summarising: dedicated *bāb fadāʾil*-of-the-surah in al-Bukhārī/Muslim/Tirmidhī/Abū Dāwūd/Nasāʾī/Ibn Mājah; recitation-occasion hadith (Friday-night, dying, daily-protection); and surah-name epithets.

**Locked weights table** (from `findings/phase-b-hypotheses/h-new-860.json` per-surah rubric scores, accessed pre-locked):

- 10: Q 1, Q 2, Q 36, Q 67, Q 112
- 9: ...
- 0: most short-mufaṣṣal without dedicated *fadāʾil*

This rubric is **already locked and published** in H-NEW-860; we reuse it as-is, no post-hoc reweighting.

## Centrality metric (LOCKED)

For each surah s, define:

  **W-centrality(s) = Σ_t [fadāʾil_score(t) × root-jaccard(s, t)]** / Σ_t fadāʾil_score(t)

where t ranges over all 114 surahs, fadāʾil_score(t) is the H-NEW-860 rubric score, and root-jaccard(s, t) is the Jaccard overlap of QAC-stem root sets between s and t (computed from `data/morphology/quranic-corpus-morphology-0.4.txt`).

This is the project's 7th centrality axis: a **liturgy-weighted lexical centrality**, distinct from the unweighted A4 lexical-centrality of H-NEW-82 (which produced Q 36 rank 18). The hypothesis: under liturgy-weighting, Q 36 should rise relative to the unweighted ranking because its content overlaps with the high-fadāʾil-weight surahs.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`.

## Direction (LOCKED)

The direction is **POSITIVE**: Q 36 is expected to score in the top-quintile on this 7th axis. A *negative* result (Q 36 outside top-quintile) is a NULL finding to be published with full prominence as confirming the H-NEW-82 binding prior.

## Success criteria

- Q 36 ranked in **top-23 / 114 (top quintile)** on the W-centrality axis: **DIRECTIONAL** for the recitation-frequency hypothesis. (Note: this is NOT a multi-axis "heart" test; it does not over-write H-NEW-82.)
- If Q 36 also ranks **top-5 (rank ≤ 5)** on this axis, the result is **VINDICATED** as a single-axis salvage of the *qalb al-Qurʾān* tradition under the explicit H-NEW-82-excluded operationalisation. Note: this ALONE does not vindicate H-NEW-82 (which required top-5 on ≥ 5 axes); it adds a 7th data-point to the H-NEW-82-cap.
- If Q 36 ranks **outside top-23**: **NULL** (binding prior preserved).

## Bonferroni context

This is a single-axis test, but it lives inside an implicit multi-axis "heart" family of (H-NEW-82's 6 axes + this 7th). Family-wise α = 0.05 / 7 = 0.00714. Q 36 needs rank ≤ ⌊0.00714 × 114⌋ + 1 = 1 to be Bonferroni-significant within the 7-axis family — i.e., Q 36 needs to be **rank 1** on this axis to declare full multi-axis VINDICATION.

This is a high bar. The pre-reg is honest about it.

## Discriminating control

Q 112 al-Ikhlāṣ — empirically the FR-distance centroid of the corpus (rank 1 by minimum mean FR distance, see `01-empirical-profile.md` §3 + H-NEW-111 D-matrix). Q 112 also has fadāʾil-rubric 10/10 (*thuluth al-Qurʾān*). Under the W-centrality metric, **Q 112 should out-rank Q 36** if W-centrality is genuinely discriminating; if Q 36 out-ranks Q 112, the metric is suspect (Q 112 is the binding prior corpus-centroid).

## Output files

- Pre-reg: `preregs/Q036-F-01-recitation-frequency-weighted-centrality-prereg.md`
- Script: `scripts/Q036_F_01_recitation_frequency_weighted_centrality.py`
- JSON: `csv/Q036-F-01.json`
- Findings: `06-novel-findings.md` Q036-F-01 section.
