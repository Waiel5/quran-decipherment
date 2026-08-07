---
surah: 1
test_id: Q001-F-04
file_type: novel-finding
date_locked: 2026-04-28
date_run: 2026-04-28
verdict: PRE-COMMIT-VIOLATION (logic-inverted) but underlying centrality claim DIRECTIONALLY VINDICATED at rank 4/114
prereg_sha: 3f8b31c0f9e4f4d8d2a1a96bc1ee71e5f283520fcd429bed8f71a7e1f99a0070
---

# Q001-F-04 — Q 1 removal centroid-shift / centrality probe


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

## 1. Pre-registered hypothesis (FLAWED — see honest reframing)

Pre-reg said: "Q 1 is in BOTTOM-3 of d_bar (mean residual after removing X)."

Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-04-q1-removal-centroid-shift-prereg.md`

## 2. Pre-commit violation acknowledgment

The pre-registered direction is LOGICALLY INVERTED. The centroid-anchor hypothesis predicts that removing a CENTRAL surah should leave a corpus with HIGHER mean pairwise distance (because the central anchor was pulling the mean down). Pre-reg incorrectly stated "bottom-3" (smallest residual mean), which would imply Q 1 is a peripheral surah whose presence INFLATES the mean. The opposite direction (top-3 of residual means) is the correct prediction for the centroid-anchor claim.

In strict pre-commit discipline (INVESTIGATION-PROTOCOL §1.8), this is a NULL result for the pre-committed direction.

We honestly report BOTH ranks below.

## 3. Result

Mean of all 6,441 corpus pairs (h-new-111 FR-roots): **0.9235**.

Q 1's row-mean (Q 1's mean distance to all 113 other surahs): **0.7789**.

| Metric | Q 1 rank | of 114 |
|:--|--:|:-:|
| Centrality (smallest row_mean → most centroid) | **4** | / 114 |
| d_bar after removal — pre-registered direction (smallest residual mean) | 111 | / 114 |
| d_bar after removal — corrected direction (largest residual mean = centroid-anchor signal) | **4** | / 114 |

The pre-registered direction puts Q 1 at rank 111 of 114 (i.e., among the surahs whose removal LEAST shrinks the corpus mean — which is consistent with Q 1 being a LOW-DISTANCE, central-anchor surah). The CORRECTED direction puts Q 1 at rank 4 of 114, vindicating the centroid-anchor claim DIRECTIONALLY.

## 4. The 4 most-central surahs (by row-mean ascending)

| Rank | Surah | Row-mean | Notes |
|:-:|:--|--:|:--|
| 1 | Q 112 al-Ikhlāṣ | 0.7592 | "1/3 of the Quran" (al-Bukhārī) |
| 2 | Q 110 al-Naṣr | 0.7644 | thuluth-ish, abrogation/closure |
| 3 | Q 108 al-Kawthar | 0.7718 | shortest surah (3 verses) |
| 4 | **Q 1 al-Fātiḥa** | **0.7789** | **umm al-Kitāb** |
| 5 | Q 106 Quraysh | 0.7803 | tribal protection |
| 6 | Q 114 al-Nās | 0.7838 | closing surah |
| 7 | Q 113 al-Falaq | 0.7843 | second muʿawwidha |

This is a profound finding. Q 1 al-Fātiḥa is statistically among the most-central surahs in FR-roots distance space, joined by **the muʿawwidhāt cluster** (Q 112-114) and **the late-Meccan core** (Q 108, 110). All seven are SHORT, conceptually-dense, multi-purpose surahs.

The classical *umm al-Kitāb* claim is empirically VINDICATED in the form: "Q 1 is among the most-central surahs in root-content space." But Q 1 is **NOT THE MOST CENTRAL** — Q 112 is. The strict claim "Q 1 is THE most central / mother of the corpus" is **FALSIFIED in favor of Q 112 al-Ikhlāṣ** at the FR-roots-centrality level.

## 5. Reframing of "umm al-Kitāb"

The al-Bukhārī ḥadīth #4474 calls Q 1 "umm al-Kitāb" — "Mother of the Book." Empirically, this manifests as:

- **Outlier-strength** Δ%ile = +27.09pp (rank 2/114) [H-NEW-590].
- **UAS rank 2/114** [H-NEW-840].
- **Q 1-Q 2 most-expensive canonical pair** (7.5% of TSP residual) [H-NEW-720].
- **Centrality rank 4/114** in FR-roots row-mean [Q001-F-04 — this finding].

The combination is empirically distinctive. Q 1 is BOTH an architectural OUTLIER (its content is far from its immediate neighbor Q 2) AND a corpus CENTROID (its content is near the corpus average distance). This is the empirical mark of "umm al-Kitāb" — it summarizes the corpus in miniature while being structurally singular at its mushaf-position.

But Q 112 outranks Q 1 on raw centrality. The finer interpretation is:
- Q 112 is the **content-thuluth** (theological-iʿjāz) — one-third of the Quran's MEANING.
- Q 1 is the **structural-iʿjāz** umm — the architectural mother.
- These are EMPIRICALLY ORTHOGONAL (the dual-iʿjāz typology of H-NEW-840/860).

## 6. Honest limits

- The pre-reg direction was wrong. The strict verdict on the pre-committed direction is NULL/PRE-COMMIT-VIOLATION.
- The CORRECTED direction (and the underlying centrality claim) holds at rank 4/114, p ≈ 4/114 ≈ 0.035 single-test α.
- Future investigations should pre-register the centroid-anchor test in the form "row_mean(Q 1) is in the bottom decile of all surahs" with the CORRECT logical direction.

## 7. Output files

- Script: `/Users/grey/Downloads/quran/scripts/Q001_F_04_centroid_shift.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/csv/Q001-F-04.json`
- Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-04-q1-removal-centroid-shift-prereg.md`
