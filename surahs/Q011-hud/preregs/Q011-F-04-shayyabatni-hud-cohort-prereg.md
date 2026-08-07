---
surah: 11
test_id: Q011-F-04
title: shayyabatnī Hūd 5-surah cohort architectural cohesion
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_family: Q011-F-04
bonferroni_k: 4
alpha_bon: 0.0125
n_perm: 10000
---

# Q011-F-04 — Pre-registration: shayyabatnī-Hūd 5-cohort cohesion


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

## 1. Hypothesis (locked before observation)

**Classical claim (al-Tirmidhī *Shamāʾil* #40, Ibn ʿAbbās → Abū Bakr chain):**
the Prophet (peace be upon him) said *"shayyabatnī Hūd wa-l-Wāqiʿa wa-l-Mursalāt
wa-ʿamma yatasāʾalūn wa-idhā al-shamsu kuwwirat"* — naming **5 surahs** as the
"makers-grey" cohort: Q 11 Hūd, Q 56 al-Wāqiʿa, Q 77 al-Mursalāt, Q 78 al-Nabaʾ
(*ʿamma yatasāʾalūn*), Q 81 al-Takwīr (*idhā al-shamsu kuwwirat*).

**H1 (one-tailed, direction LOCKED on each axis):** the 5-surah cohort
{Q 11, Q 56, Q 77, Q 78, Q 81} is **architecturally more cohesive** than
random 5-surah samples on at least 2 of 4 pre-registered architectural axes:

- **A. Mean pairwise FR-content distance**: cohort mean FR < random-5 null
  (more content-similar).
- **B. sig_A spread (sd of iʿjāz signature A)**: cohort sig_A sd < random-5 null
  (more structurally homogeneous).
- **C. UAS spread (sd of UAS rank)**: cohort UAS sd < random-5 null.
- **D. Mean rhyme-top-letter agreement**: cohort modal-fraction of dominant
  final-letter agreement > random-5 null.

**H0:** Cohort matches random-5 distribution on ≥ 3 of the 4 axes.

**Direction (per axis):** A, B, C — cohort *lower* than null mean
(more cohesive, smaller distance/spread). D — cohort *higher* than null mean
(more rhyme-letter agreement). All LOCKED.

## 2. Operational definition

- **Cohort**: {Q 11, Q 56, Q 77, Q 78, Q 81}.
- **Random-5 null**: 10,000 random samples (without replacement) of 5 surahs
  drawn from {1..114} \ {1} (exclude Q 1 al-Fātiḥa as architectural anchor).
  Seed 20260507.
- **A. FR distance**: from `findings/phase-b-hypotheses/csv/h-new-111.json`
  reconstructed symmetric matrix; mean of all 10 pairwise distances within
  the 5-cohort.
- **B. sig_A**: per-surah `sig_A` from `findings/phase-b-hypotheses/csv/h-new-750.json`;
  cohort sd.
- **C. UAS**: per-surah `UAS` from `findings/phase-b-hypotheses/csv/h-new-840.json`;
  cohort sd.
- **D. Rhyme-letter agreement**: per-surah `top_final_letter` from
  `findings/phase-b-hypotheses/csv/h-new-700.json`; compute the cohort's
  most-common top_final_letter and report the fraction of cohort members
  sharing it (e.g., 4/5 = 0.8 if 4 share `ن`).

## 3. Test statistic

For each axis A, B, C, D — compute the cohort's value, then for each of 10000
random-5 draws compute the same value; one-tailed p-value = fraction of draws
that are at-least-as-extreme in the locked direction.

## 4. Success / Failure (per axis + composite)

| Outcome | Verdict |
|:--|:--|
| ≥ 3 of 4 axes pass at α_bon = 0.0125 | **CONFIRMED** |
| 2 of 4 axes pass at α_bon = 0.0125 | DIRECTIONAL |
| ≤ 1 of 4 axes passes at α_bon = 0.0125 | NULL |
| All 4 axes strongly opposite-direction (cohort *less* cohesive) | Pre-commit violation; NULL with full prominence |

## 5. Bonferroni context

- k=4 axes; α_bon = 0.0125 per axis.
- Composite "≥ 3 of 4 pass at α_bon" is the locked acceptance bar.
- The hadith chain (Tirmidhī Shamāʾil) is *ḥasan-gharīb* per al-Tirmidhī's own
  grading; the 5-surah list is the locked one (Shamāʾil #40 wording).

## 6. Honest limits known a priori

- The classical "Hūd and its sisters" cluster has multiple narrations:
  Shamāʾil #40 (5 surahs as listed) and Shamāʾil #41 (abbreviated:
  *qad shayyabatnī Hūd wa-akhawātuhā* — without enumeration). Other
  classical commentators (e.g., per Ibn Kathīr's tafsīr on Q 11)
  occasionally include Q 99 al-Zalzala. We test the **Shamāʾil #40 5-surah list**
  (the most-specified version); a follow-up test on the {Q 99 included}
  6-surah list could be queued as Q011-F-04.1.
- 5 surahs is small N; the random-5 null distribution will be wide, and
  rare-surah configurations (e.g., 4/5 of the cohort in mufaṣṣal-tail) may
  produce baseline-cohesive draws frequently.
- The cohort mixes long Q 11 (123 vv, head-mushaf) with short Q 78/81
  (mufaṣṣal-tail). On axis A (FR), this **predicts AGAINST cohesion**, since
  compression-tail surahs are FR-far from head-mushaf surahs by H-NEW-660.
  An honest forecast: A may NULL; B and D may be where the signal lives.

## 7. Rules-tuple

`(no-tashkeel for FR; min-tashkeel for rhyme-top-letter; precomputed sig_A and UAS; basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Computed at run-time. Embedded in `scripts/Q011_F_04_shayyabatni_hud_cohort.py`.
