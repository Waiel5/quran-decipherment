---
test_id: Q032-F-02
title: "Q 32 ↔ Q 67 architectural-twin extension — content-axis cohesion beyond FR=0.753"
date_locked: 2026-05-08
seed: 20260508
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q032-F-02-twin-axes
alpha_bon: 0.0125
direction_locked: true
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q032-Q047-retry-specialist
parent_findings:
  - cross-finding-028 (Q 32-Q 67 nightly-pair FR=0.753, CONFIRMED tight)
  - h-new-750 (per-surah iʿjāz signature: Q32 sig_A=-0.350, Q67 to fetch)
classical_anchors:
  - al-Tirmidhī, *Sunan*, idInBook 2975 (al-Munjiya pre-sleep nightly recitation Sajda+Mulk)
  - al-Suyūṭī, *al-Itqān*, nawʿ 18 (tartīb tawqīfī)
---

# Q032-F-02 Pre-registration — Q 32 ↔ Q 67 architectural-twin axes

## Hypothesis

Cross-finding-028 confirmed Q 32 ↔ Q 67 as an FR-near-pair (FR=0.7534, vs corpus mean 0.9235; nightly-recitation pair per al-Tirmidhī idInBook 2975). The FR closeness reflects QAC-stem-roots distribution similarity. Twin-architecture should be VISIBLE on additional content-axes if the pair is genuinely twinned (not just FR-fluke):

1. Top final-letter (rhyme rāwī) — same dominant terminal letter
2. iʿjāz signature sig_A (h-new-750) — same sign and similar magnitude
3. Length-class — same al-Suyūṭī length-tier (mufaṣṣal-awsāṭ; both ~30 verses)
4. Divine-name density — both invoke the Lord's sovereignty (Mulk theme; tasbīḥ theme)

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked**: ≥3 of 4 axes show twin-cohesion.

Operational definitions:
- **Axis A1 (rhyme-rāwī)**: top final-letter identical (1=identical, 0=different).
- **Axis A2 (iʿjāz sig_A)**: |sig_A_Q32 − sig_A_Q67| < 0.5 (within tight band).
- **Axis A3 (length-class)**: |verse_count_Q32 − verse_count_Q67| ≤ 5 (both 30 verses → diff=0).
- **Axis A4 (divine-name density)**: Q 32 and Q 67 are both in top-30 corpus-wide for divine-name (Allāh, al-Raḥmān, al-Mulk, al-ʿAzīz, al-Ḥakīm) per-100-words density.

Bonferroni: each axis at α_bon = 0.05/4 = 0.0125 (where applicable). Aggregate prediction: ≥3 axes pass.

## Tests (Bonferroni-4 family)

1. **A1**: top_final_letter(Q32) == top_final_letter(Q67)? (binary; expected pass per h-new-750).
2. **A2**: |sig_A(Q32) − sig_A(Q67)| < 0.5 (tight-band signature match).
3. **A3**: |30 − 30| ≤ 5 ↔ TRUE (length-class twin; this is descriptive, not statistical).
4. **A4**: divine-name density of Q 32 AND Q 67 both in top-30 corpus-wide. Permutation null: rank distribution under random pair selection.

For A4 we use the divine-name list:
{الله, الرحمن, الرحيم, الملك, العزيز, الحكيم, العليم, القدير, اللطيف, الخبير, السميع, البصير, رب, ربك, ربكم, ربنا, ربهم, ربه, ربها, ربهن, ربى}.

## Direction-of-effect lock

Predicted direction: ≥3/4 axes pass.
If only ≤2 pass: NULL — twin-architecture is FR-only, not a multi-axis twin.

## Success criteria

- VINDICATED: 4/4 axes pass.
- DIRECTIONAL: 3/4 pass.
- NULL: ≤2/4 pass.

## Garden-of-forking-paths log

- BEFORE running: chose 4 axes (rhyme, sig_A, length, divine-name). Chose sig_A (not sig_B) because sig_A is the rhyme-content-coupled signature most relevant to twin-architecture.
- BEFORE running: 0.5 sig_A band chosen because corpus sig_A range is ~[-2.5, +2.5] (~5 unit span), so 0.5 = 10% of range = tight similarity threshold.
- BEFORE running: divine-name list selected from `/Users/grey/Downloads/quran/data/asma-al-husna.txt` representative subset + رب-stem (frequent in both surahs).
- BEFORE running: top-30 threshold for A4 chosen because 30/114 ≈ 26% — pre-committed to "both in top-quartile range."
