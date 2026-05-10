---
finding_id: Q028-F-06
title: Q 28 al-Qaṣaṣ Mūsā-token density and absolute-count corpus rank
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q028-novel-findings-wave-H
alpha_bon: 0.01667
direction: ONE-SIDED-UPPER (rank-1 / rank-1 predicted)
status: PRE-REGISTERED
specialist: Q028-al-qasas-wave-H
verdict: TBD
notes: builds on H-NEW-1710 corpus-wide *Mūsā* attestation count (136 in QAC); Q 28 is widely claimed by classical tradition to be "the Moses surah par excellence" and is the largest single Mosesic pericope (vv. 3-43, > 40 verses); test corpus-rank.
---

# Q028-F-06 — Q 28 Mūsā density and absolute-count corpus rank

## 1. Hypothesis

Classical tradition (al-Suyūṭī, *al-Itqān* vol. 1; al-Biqāʿī, *Naẓm al-Durar* on Q 28; al-Ṭabarī, *Jāmiʿ al-bayān* introduction to Q 28) treats Q 28 as the *Sūrat Mūsā* — the surah containing the most extended Moses-narrative arc in the corpus. The Madyan + early-life + Pharaoh-confrontation block runs vv. 3-43, ~40 verses of single-narrative coverage.

Independent of any rhetorical claim, the QAC lemma `muwsaY\`` (Mūsā) is attested **136 times** corpus-wide (per H-NEW-1710 and direct QAC count). The hypothesis is that Q 28 holds the **corpus-rank-1** position on absolute Mūsā count among all 114 surahs, and that this rank is stable to length normalisation.

**H1 (locked, deterministic)**: Q 28's absolute count of QAC-lemma `muwsaY\`` (Mūsā) attestations is **rank 1** among all 114 surahs.

**H2 (locked, deterministic)**: Q 28's Mūsā-per-1000-words density is **top-3** among all 114 surahs (relaxed from rank-1 because Q 20 Ṭā-Hā has a shorter base and high Mūsā count; the prediction is that even normalised, Q 28 is in the top-3 cluster of Mosesic surahs).

**H3 (locked, deterministic)**: Q 28's absolute Mūsā count exceeds **20**.

## 2. Direction-locking

- H1 direction: Q 28 absolute count = rank 1 of 114. Any other rank = FAIL.
- H2 direction: Q 28 normalised density rank ≤ 3 of 114. Rank > 3 = FAIL.
- H3 direction: count ≥ 20. Count < 20 = FAIL.

The direction is locked **before** running the count.

## 3. Method

- Source: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4).
- Filter: lines tagged `LEM:muwsaY\`` with `POS:PN` (proper noun).
- Group by surah (parse from LOCATION `(s:v:w:p)` → s).
- Word-count denominator: total STEM token count per surah (same QAC source).
- Sensitivity-check: also report orthographic-token count using `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` and substring rule `موسى`, to verify the QAC-rank matches the orthographic-rank.

## 4. Test family + Bonferroni

Family: Q028-novel-findings-wave-H (this dispatch's T1/T2/T3), k = 3. α_Bonferroni = 0.05 / 3 = 0.01667.

## 5. Acceptance / failure

- **CONFIRMED** = H1 PASS (rank 1) AND H2 PASS (density top-3) AND H3 PASS (count ≥ 20).
- **DIRECTIONAL** = at least one of {H1, H2, H3} passes.
- **NULL** = all three fail.

## 6. MW protections

- MW-1: length normalisation in H2 (per-1000-words density).
- MW-3: orthographic-substring sensitivity check (alternative model).
- MW-5: positive-control = the QAC corpus total (must equal 136 per H-NEW-1710).
- MW-6: instrument-control = orthographic re-derivation under the project's default rules-tuple.
- MW-7: not invoked (single-claim deterministic test).

## 7. Coordination

This test deepens the classical-claim audit C-5 (Ibn Kathīr's "Madyan-elder = Shuʿayb" passage assumes Q 28 is the surah-of-Mūsā) and the F-05 narrative-density passing finding (which used Mūsā-density as one of three axes; this F-06 isolates the Mūsā axis alone and gives it a deterministic corpus-rank result).

It does NOT duplicate F-05's permutation-test logic; F-06 is a pure descriptive corpus-rank test under a single deterministic threshold.

## 8. Honest expectation

I expect H1 PASS, H2 PASS (likely Q 20 / Q 28 / Q 26 cluster on the density axis), H3 PASS comfortably.

If Q 28 is NOT rank 1 on absolute count, the surprise candidate would be Q 20 Ṭā-Hā (the other major Mosesic surah). If Q 28 is rank 1, the classical "Sūrat Mūsā" attribution is empirically vindicated on the corpus-rank-1-of-114 axis.

## 9. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
