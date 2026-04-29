---
id: H-NEW-380
title: "Hijra-split validation of chronology-homogeneity factor — Meccan {Q 50-56} and Medinan {Q 57-66} halves tested separately"
phase: B
status: PRE-REGISTERED 2026-04-20
date: 2026-04-20
agent: team-lead (inline; ID 380 skip codex range)
parent: H-NEW-370 (mufaṣṣal-ṭiwāl Q 50-66 combined at 50% NULL)
seed: 20260505
bonferroni_k: 2
bonferroni_family: h-new-380-hijra-split
alpha_bon: 0.025
n_perm: 10000
rules_tuple: "(2 chronology-homogeneous subsets: A=Meccan {Q 50-56} N=7; B=Medinan {Q 57-66} N=10; FR from H-NEW-111; 10000-perm nulls; seed 20260505)"
direction: "Cell A d̄_Meccan < null 2.5%ile; Cell B d̄_Medinan < null 2.5%ile; BOTH should pass for chronology-homogeneity hypothesis validation"
verdict: PENDING
---

# [[h-new-380-hijra-split|H-NEW-380]] — Hijra-split validation

## 1. Question

[[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] revealed that mufaṣṣal-ṭiwāl {Q 50-66} at 50.1%ile fails cohesion because it spans the Hijra boundary at Q 56/57 (Meccan → Medinan). The hypothesis: CHRONOLOGY-HOMOGENEITY is a 4th content-cohesion factor.

**Direct test**: split the block at Q 56/57, test each half separately. If both halves cohere while combined block fails, the hypothesis is validated.

## 2. Hypothesis

**H1 (chronology-homogeneity validated)**: both halves pass strict α_bon=0.025.
- Cell A Meccan {Q 50-56} N=7: d̄ < null 2.5%ile
- Cell B Medinan {Q 57-66} N=10: d̄ < null 2.5%ile

**H0**: at least one half fails, suggesting chronology is not the decisive factor.

Pre-committed direction: both halves STRICT PASS.

## 3. Classical set definitions

- **Meccan half**: Q 50 al-Qāf, Q 51 al-Dhāriyāt, Q 52 al-Ṭūr, Q 53 al-Najm, Q 54 al-Qamar, Q 55 al-Raḥmān, Q 56 al-Wāqiʿah (all traditionally Meccan per al-Suyūṭī *Itqān* chronology)
- **Medinan half**: Q 57 al-Ḥadīd, Q 58 al-Mujādila, Q 59 al-Ḥashr, Q 60 al-Mumtaḥana, Q 61 al-Ṣaff, Q 62 al-Jumuʿa, Q 63 al-Munāfiqūn, Q 64 al-Taghābun, Q 65 al-Ṭalāq, Q 66 al-Taḥrīm (all traditionally Medinan)

## 4. Protocol

1. FR distance matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]].
2. Compute d̄_A (N=7) and d̄_B (N=10).
3. Null: 10000 random draws of each N from {1..114}.
4. MW-5: already implicit in the 2-cell parallel design (both cells independently tested).

## 5. Pre-committed predictions

Based on [[h-new-350-al-tiwal-cohesion|H-NEW-350]] pattern (homogeneous Meccan/Medinan blocks cohere strongly):
- Cell A Meccan {Q 50-56}: PASS at strict α; predicted ≤5%ile (short eschatological/oath block — highly homogeneous)
- Cell B Medinan {Q 57-66}: PASS at strict α; predicted ≤5%ile (community-legal Medinan — homogeneous)

If BOTH pass AND combined fails ([[h-new-370-mufassal-tiwal-cohesion|H-NEW-370]] 50%), chronology-homogeneity factor is DEFINITIVELY CONFIRMED.

## 6. Honest limits

1. Classical chronology assignments at Q 56 vs Q 57 boundary are standard but Some scholars have noted Q 54-56 Meccan-Medinan-transitional.
2. N=7 and N=10 are moderate but higher than [[h-new-340-musabbihat-block-subset|H-NEW-340]]'s N=5.
3. FR-roots only.

## 7. Classical anchor

- al-Suyūṭī *Itqān* chronology (Meccan/Medinan designation per revelation-order scholars)
- al-Biqāʿī *Naẓm al-Durar* Q 56→57 transition treatment

## 8. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_380_hijra_split.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-380.json`
- Findings: `findings/phase-b-hypotheses/h-new-380-hijra-split.md`

Pre-reg locked 2026-04-20.
