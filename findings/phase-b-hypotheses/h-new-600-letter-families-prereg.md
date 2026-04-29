---
id: H-NEW-600
title: "Letter-family content-cohesion paired test — ALM-6 (H-NEW-600) and ALR-5 (H-NEW-610) under one Bonferroni umbrella"
phase: B
status: PRE-REGISTERED 2026-04-28
date: 2026-04-28
agent: h-new-600-specialist
parent_1: H-NEW-570 (muqaṭṭaʿāt-29 NULL @ 65.62%ile; HM-7 @ 20.90%ile; muqaṭṭaʿāt-axis ⊥ content-axis)
parent_2: H-NEW-130 (muqaṭṭaʿāt hub-architecture at letter-level CONFIRMED)
parent_3: H-NEW-97 (ALR letter-cluster → 4/5 PROPHET_PERSON p_mc=0.0059)
seed_alm_primary: 20260430
seed_alr_primary: 20260430
seed_alm_mw5: 20260431
seed_alr_mw5: 20260431
seed_mw6: 20260432
bonferroni_k: 3
bonferroni_family: h-new-600-letter-families
alpha_bon: 0.01667
rules_tuple: |
  (Fisher-Rao distance matrix from H-NEW-111 / no-tashkeel / QAC-STEM root tokens / QAC v0.4 /
  basmala-counted-only-in-surah-1 / mushaf order / Hafs-Kufan / K_top=500 / Dirichlet α=0.5 /
  ALM-6 = {Q 2, 3, 29, 30, 31, 32} / ALR-5 = {Q 10, 11, 12, 14, 15} /
  Q 13 al-Raʿd EXCLUDED from ALR-5 because its opening is ALMR (المر) not ALR (الر);
  PRIMARY = d̄ percentile in 10000 random-K-subset null; K=6 ALM, K=5 ALR; seed 20260430;
  MW-5 replication seed 20260431 with N_perms = 5000;
  MW-6 instrument check = a deterministic non-letter-family random-6 set vs 10000-perm null seed 20260432;
  Bonferroni k=3: ALM PRIMARY, ALR PRIMARY, joint-pattern test (≥1 of 2 ≤ 16.67%ile DIRECTIONAL);
  α_bon = 0.05 / 3 = 0.01667)
direction: |
  PRIMARY ALM-6 H1: d̄(ALM-6) ≤ 1.67%ile (= 5/3 STRICT) ⇒ family content-cohesion CONFIRMED.
  PRIMARY ALR-5 H1: d̄(ALR-5) ≤ 1.67%ile (= 5/3 STRICT) ⇒ family content-cohesion CONFIRMED.
  DIRECTIONAL pass: %ile ≤ 16.67 (cohesion at α=0.05 single-test scale).
  Joint pass: at least 1 of 2 PRIMARY families ≤ 16.67%ile DIRECTIONAL.
  Failure of cohesion (NULL) on BOTH families = vindication of H-NEW-570 generalization
    that "muqaṭṭaʿāt-axis ⊥ content-axis" survives even within letter-families.
verdict: PENDING
---

# [[h-new-600-letter-families|H-NEW-600]]/610 — Paired letter-family content-cohesion test

## 1. Question

[[h-new-570-muqattaat-content-cluster|H-NEW-570]] established that the full muqaṭṭaʿāt-29 set is NOT content-cohesive at whole-surah FR-roots scale (65.62%ile = median); the ḥawāmīm-7 sub-cluster is moderately cohesive only (20.90%ile). [[h-new-570-muqattaat-content-cluster|H-NEW-570]] §9 queued the two natural follow-ups:

- **[[h-new-600-letter-families|H-NEW-600]]**: do the **ALM-6** muqaṭṭaʿāt-surahs {Q 2, 3, 29, 30, 31, 32} cohere on content?
- **H-NEW-610**: do the **ALR-5** muqaṭṭaʿāt-surahs {Q 10, 11, 12, 14, 15} cohere on content?

Each letter-family has a strong classical-scholarship anchor (al-Biqāʿī's *munāsaba* framework explicitly groups by opening-letter sequence). [[h-new-570-muqattaat-content-cluster|H-NEW-570]]'s HM-7 result already gave a partial-NULL on the strongest-classically-cohesive family (ḥawāmīm). ALM and ALR are the next two-largest letter-families; jointly they cover 11 of the 29 muqaṭṭaʿāt-surahs and provide the decisive empirical test of al-Biqāʿī's whole-surah-content-munāsaba framework.

We run BOTH families in one pre-registered Bonferroni-3 family for tight α-control and to avoid garden-of-forking-paths between sequential single tests.

## 2. Letter-family definitions (LOCKED)

### 2.1 ALM-6 (الم) — K=6
**ALM-6** = {Q 2 al-Baqara, Q 3 Āl ʿImrān, Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}

Source: al-Zamakhsharī *Kashshāf*; al-Suyūṭī *Itqān* nawʿ 40 enumeration; [[h-new-130-fisher-rao-residuals|H-NEW-130]] / [[h-new-97-name-letter-joint|H-NEW-97]] corpus tables.

### 2.2 ALR-5 (الر) — K=5
**ALR-5** = {Q 10 Yūnus, Q 11 Hūd, Q 12 Yūsuf, Q 14 Ibrāhīm, Q 15 al-Ḥijr}

Source: al-Suyūṭī *Itqān* nawʿ 40; [[h-new-97-name-letter-joint|H-NEW-97]] (where this exact set appears as the 4/5 PROPHET_PERSON cluster, p_mc = 0.0059).

### 2.3 Q 13 al-Raʿd EXCLUSION rationale (LOCKED)
Q 13 al-Raʿd opens with **ALMR** (المر), not ALR (الر). It is its own 1-element letter-family ALMR-1 in the [[h-new-130-fisher-rao-residuals|H-NEW-130]] / [[h-new-97-name-letter-joint|H-NEW-97]] / [[h-new-570-muqattaat-content-cluster|H-NEW-570]] taxonomy. Including Q 13 in ALR-5 would conflate two distinct letter-sequences and contaminate the family-cohesion signal.

This EXCLUSION is locked. A separate [[h-new-620-divine-name-density|H-NEW-620]] follow-up (queued) will test the full ALMR-disjunction question (does {ALR-5 ∪ {Q 13}} cohere any better or worse than ALR-5 alone?).

## 3. Protocol

### 3.1 PRIMARY tests
1. Load Fisher-Rao distance matrix D from `findings/phase-b-hypotheses/csv/h-new-111.json` (114-surah symmetric matrix).
2. For each family F ∈ {ALM-6, ALR-5}:
   - Compute d̄(F) = mean over C(K, 2) pairs.
   - NULL: 10000 random K-subsets of {1..114}, seed 20260430 (one rng per family, distinct streams).
   - Percentile = % of null draws with d̄ ≤ d̄(F).
3. **STRICT gate**: %ile ≤ 1.67 (= 5/3).
4. **DIRECTIONAL gate**: %ile ≤ 16.67.

### 3.2 MW-5 replication (stability check)
Same as PRIMARY but seed = 20260431 and N_perms = 5000 (half PRIMARY). Stability-check on percentile drift; declared "stable" if PRIMARY %ile and MW-5 %ile differ by ≤ 3 absolute pp.

### 3.3 MW-6 instrument check
A deterministic non-letter-family random-6 sample (chosen pre-run from non-muqaṭṭaʿāt {1..114} \ muqaṭṭaʿāt-29):
**MW-6 set = {Q 5 al-Māʾida, Q 9 al-Tawba, Q 17 al-Isrāʾ, Q 25 al-Furqān, Q 33 al-Aḥzāb, Q 47 Muḥammad}** (6 surahs, mixed register, locked pre-run).

Predicted: %ile in [25%, 75%]ile of random-6 null (seed 20260432, 10000 perms) — should be null-typical, instrument-side check that the random-K null is well-calibrated for K=6.

## 4. Bonferroni accounting

| # | Test | α_bon |
|:--|:--|:--:|
| 1 | ALM-6 PRIMARY | 0.01667 |
| 2 | ALR-5 PRIMARY | 0.01667 |
| 3 | Joint-pattern (≥1 of 2 ≤ 16.67%ile DIRECTIONAL) | 0.01667 |

**Bonferroni k = 3, α_bon = 0.05 / 3 = 0.01667.**

MW-5 (replication) and MW-6 (instrument) are NOT counted as outer-level tests — they are confirmatory diagnostics, not primary hypotheses.

## 5. Pre-commits

| Test | STRICT gate | DIRECTIONAL gate |
|:--|:-:|:-:|
| ALM-6 PRIMARY | ≤ 1.67%ile | ≤ 16.67%ile |
| ALR-5 PRIMARY | ≤ 1.67%ile | ≤ 16.67%ile |
| Joint H1 | ≥1 of 2 STRICT | ≥1 of 2 DIRECTIONAL |

**Aggregate H1 (al-Biqāʿī family-content-munāsaba) CONFIRMED**: at least one family ≤ 1.67%ile STRICT AND second family ≤ 16.67%ile DIRECTIONAL.

**Aggregate NULL** ([[h-new-570-muqattaat-content-cluster|H-NEW-570]] generalization vindicated): both families > 16.67%ile.

**Mixed/PARTIAL**: one ≤ 16.67% DIRECTIONAL, one > 16.67%.

## 6. Classical-scholarship anchors

### 6.1 ALM (al-Biqāʿī, al-Suyūṭī, al-Rāzī)
**al-Biqāʿī** *Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar* on Q 2:1: ALM opens al-Baqara, the longest surah, and al-Biqāʿī's framework predicts that all 6 ALM-opened surahs share *munāsaba* across cosmological / divine-attribute / signs themes. Specifically al-Biqāʿī treats Q 29-32 (al-ʿAnkabūt, al-Rūm, Luqmān, al-Sajda) as a tight thematic-block within ALM (consecutive mushaf positions, all Meccan, shared "signs of Allāh" motif).

**al-Suyūṭī** *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 40 enumerates ALM as the single largest letter-family (6 surahs).

**al-Rāzī** *Mafātīḥ al-ghayb* on Q 2:1 surveys 20+ classical opinions about ALM specifically, often treating it as the canonical case for muqaṭṭaʿāt theorizing.

**Prediction under al-Biqāʿī**: ALM-6 should show family content-cohesion (≤ 16.67%ile DIRECTIONAL).

### 6.2 ALR (al-Biqāʿī, al-Rāzī, [[h-new-97-name-letter-joint|H-NEW-97]])
**al-Biqāʿī** *Naẓm al-Durar* on Q 10:1: ALR-opened surahs are all qiṣaṣ (prophet-narrative)-heavy — Q 10 Yūnus, Q 11 Hūd, Q 12 Yūsuf, Q 14 Ibrāhīm, Q 15 al-Ḥijr (Ṣāliḥ + Lūṭ). al-Biqāʿī treats this as the strongest-cohering letter-family on content grounds.

**al-Rāzī** *Mafātīḥ al-ghayb* vol. 17 on Q 10:1 explicitly notes the qiṣaṣ-cohesion across the ALR family.

**[[h-new-97-name-letter-joint|H-NEW-97]]** EMPIRICALLY confirmed at the surah-name-class level: ALR-5 is 4/5 PROPHET_PERSON (named after a prophet) at p_mc = 0.0059 < α_bon = 0.0125. This is corpus-empirical evidence INDEPENDENT of FR-roots that ALR coheres on prophet-narrative theme.

**Prediction under al-Biqāʿī + [[h-new-97-name-letter-joint|H-NEW-97]]**: ALR-5 should show STRONGER content-cohesion than ALM-6 (≤ 16.67%ile DIRECTIONAL plausible; ≤ 1.67%ile STRICT a stretch but not impossible given [[h-new-97-name-letter-joint|H-NEW-97]] effect-size).

## 7. Honest limits

1. **FR-roots only.** Verse-level, phonological, or rhyme-level cohesion untested.
2. **K=5 and K=6 are small** — percentile resolution under 10000-perm null is ~0.01 absolute (good).
3. **Q 13 al-Raʿd EXCLUDED** from ALR-5 (rationale §2.3); ALMR-disjunction follow-up queued as [[h-new-620-divine-name-density|H-NEW-620]].
4. **Length-variation within each family is large** (Q 2 has 286 verses vs Q 32 has 30; Q 12 has 111 vs Q 15 has 99 — but ALR is more uniform on length).
5. **[[h-new-570-muqattaat-content-cluster|H-NEW-570]] already-NULL on full muqaṭṭaʿāt-29 and HM-7** — prior is that ALM-6 and ALR-5 will also NULL or weak-cohere. [[h-new-97-name-letter-joint|H-NEW-97]] ALR signal at name-level is the main reason for non-trivial alternative hypothesis.
6. **MW-5 = N_perms 5000** (half PRIMARY) is replication-stability check, NOT independent test.
7. **MW-6 random-6 set chosen pre-run** and locked here — no garden-of-forking-paths.

## 8. Deliverables

- This pre-reg locked 2026-04-28; sha256 embedded in run script.
- Run script: `scripts/h_new_600_letter_families.py` (does BOTH ALM and ALR in one execution).
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-600.json`
- Findings markdown: `findings/phase-b-hypotheses/h-new-600-letter-families.md`
- Journal: `journal/h-new-600-run-1.md`

## 9. Direction LOCKED. ONE text. Equal NULL prominence.

Pre-reg locked 2026-04-28.
