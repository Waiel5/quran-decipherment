---
id: H-NEW-460
title: "Q 24 al-Nūr ↔ Q 33 al-Aḥzāb ḥijāb-legislation-pair content-proximity test — are Type-A ROBUST outliers a classically-anchored content-class?"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline)
parent_1: H-NEW-450 (4-type outlier typology; Q 24 + Q 33 both Type-A ROBUST)
parent_2: H-NEW-430 (Q 24 −25.38pp, Q 33 −34.89pp exclusion deltas)
parent_3: H-NEW-410 (ranks 5 and 4 respectively in local outlier spectrum)
seed: 20260513
bonferroni_k: 4
bonferroni_family: h-new-460-q24-q33-hijab-pair
alpha_bon: 0.0125
rules_tuple: "(FR from H-NEW-111; PRIMARY: compare observed D(24, 33) to percentile in random pairwise distribution = all C(114,2) = 6441 pairs; MW-5: D(Q 57, Q 64) expected in lower-20%ile (musabbiḥāt-members); MW-6: D(Q 24, Q 112) expected in upper-20%ile (Medinan-social-legal vs short-Meccan-theology anti-pair); plus DESCRIPTIVE: check rank of D(24,33) among all pairs involving either Q 24 or Q 33 — expected: Q24-Q33 is one of each's top-20%. k=4 Bonferroni, α_bon = 0.0125.)"
direction: |
  PRIMARY H1: D(Q 24, Q 33) ≤ corpus-pairwise 10th percentile.
  SECONDARY H1: D(Q 24, Q 33) ≤ each surah's top-25% nearest-neighbor set.
  MW-5: D(Q 57, Q 64) ≤ corpus-pairwise 20th percentile (musabbiḥāt cohesion control).
  MW-6: D(Q 24, Q 112) ≥ corpus-pairwise 80th percentile (anti-pair control).
  Aggregate H1: PRIMARY + SECONDARY + MW-5 + MW-6 all pass = Type-A ROBUST outliers are a classically-anchored content-pair.
verdict: PENDING
---

# [[h-new-460-q24-q33-hijab-pair|H-NEW-460]] — Q 24 ↔ Q 33 ḥijāb-legislation-pair test

## 1. Question

[[h-new-450-window-sensitivity|H-NEW-450]] revealed a 4-type outlier typology. **Q 24 al-Nūr and Q 33 al-Aḥzāb are the ONLY two surahs classified as Type-A ROBUST** (|Δ|≥20pp exclusion effect at ±2, ±3, AND ±5 windows).

**Does this shared behavioral classification reflect a shared content-axis?**

Classical *munāsabāt* tradition explicitly pairs Q 24 and Q 33 as the **two ḥijāb-legislation surahs**:
- Q 24:30-31 (*yaghuḍḍū min abṣārihim* — gaze-lowering, general community ḥijāb)
- Q 33:53-59 (*ḥijāb* of Prophet-household, addressing *nisāʾ al-nabī* and the *ḥijāb* screen)

Both are the flagship Medinan family-law centerpieces. al-Biqāʿī discusses both in cross-reference under *āyāt al-ḥijāb*. If Type-A ROBUST outlier-status reflects a shared content-factor (family-law / Medinan-community-legal register), the FR distance D(24, 33) should be anomalously LOW despite the 9-surah mushaf gap.

If D(24, 33) is null-typical, ROBUST status is individual-not-shared, and al-Biqāʿī's pairing is thematic-only, not content-statistical.

## 2. Protocol

1. **PRIMARY**: extract D(Q 24, Q 33) from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] matrix.
2. Null distribution: all C(114, 2) = 6441 pairwise FR distances.
3. Compute percentile of D(24, 33) in this distribution.
4. **Pre-commit**: D(24, 33) ≤ 10th percentile = CONFIRM ḥijāb-pair.

5. **SECONDARY**: compute Q 24's and Q 33's nearest neighbors via FR:
   - For Q 24, rank all 113 other surahs by D(24, j); is Q 33 in top-25%?
   - For Q 33, rank all 113 other surahs by D(33, j); is Q 24 in top-25%?
6. **Pre-commit**: both ranks ≤ 28 (top 28/113 ≈ top-25%) = CONFIRM mutual-nearness.

7. **MW-5**: D(Q 57 al-Ḥadīd, Q 64 al-Taghābun) — two musabbiḥāt members from [[h-new-340-musabbihat-block-subset|H-NEW-340]]; expected ≤ 20th percentile (cohesion control).
8. **MW-6**: D(Q 24, Q 112 al-Ikhlāṣ) — Medinan-social-legal vs short-Meccan-pure-theology; expected ≥ 80th percentile (anti-pair control).

## 3. Pre-committed predictions

| Test | Expected | Gate |
|:--|:-:|:--|
| PRIMARY: D(Q24, Q33) | ≤ 10th percentile of corpus pairs | direction-locked |
| SECONDARY Q24: rank of Q33 | ≤ 28/113 | direction-locked |
| SECONDARY Q33: rank of Q24 | ≤ 28/113 | direction-locked |
| MW-5: D(Q57, Q64) | ≤ 20th percentile | direction-locked |
| MW-6: D(Q24, Q112) | ≥ 80th percentile | direction-locked |

**Aggregate H1 CONFIRMED**: PRIMARY + both SECONDARY + MW-5 + MW-6 all pass.

**H0 alternatives**:
- PRIMARY fails, SECONDARY passes: pair is mutually-near but NOT corpus-extreme.
- SECONDARY fails: pair is not mutually-near; classical pairing is thematic-only.
- MW-5 fails: instrument broken (musabbiḥāt cohesion not detected).
- MW-6 fails: anti-pair control broken.

## 4. Classical-scholarship anchor

**al-Biqāʿī** *Naẓm al-Durar*:
- Vol. 14 on Q 24 al-Nūr: social-legal centerpiece, general community ḥijāb, *āyat al-nūr* cosmological simile (24:35).
- Vol. 16 on Q 33 al-Aḥzāb: Prophet-household ḥijāb, Zaynab-marriage, *khātam al-nabiyyīn* (33:40).
- al-Biqāʿī cross-references both under *āyāt al-ḥijāb wa-al-sitr* cluster.

**al-Zarkashī** *al-Burhān fī ʿulūm al-Qurʾān* ch. on *munāsabāt*: pairs Q 24 and Q 33 in discussion of *ayāt al-ḥijāb* legislative-cluster.

**al-Ṭabarī** *Jāmiʿ al-bayān*: commentary on Q 33:53 *lā tadkhulū buyūta al-nabī* explicitly references Q 24:27 *lā tadkhulū buyūtan ghayra buyūtikum* — the two verses form a classical paired-entry on privacy-of-homes legislation.

**al-Zamakhsharī** *Kashshāf*: on Q 33:35 lists of believer-attributes (*al-muslimīn wa-al-muslimāt…*) as Medinan-community-ethics mirror to Q 24's community-moral code.

## 5. Honest limits

1. **Single pairwise test at α_bon=0.0125** — modest Bonferroni; 10th percentile threshold is not extreme.
2. **Null distribution is all pairs including auto-correlated adjacent pairs** — median pairwise distance may be below corpus-random due to mushaf-sequential content-continuity.
3. **Classical "pairing" varies by scholar** — my selection of al-Biqāʿī, al-Zarkashī, al-Ṭabarī, al-Zamakhsharī may be biased toward pairs that show empirical proximity.
4. **FR-roots only**: if content-proximity is phonological/prosodic rather than lexical-root, this test won't detect.
5. **Q 24 and Q 33 are BOTH Medinan** — some of any detected proximity could be chronology-artifact, not content-shared.
6. **Chronology-control**: post-hoc, could compare D(24,33) to mean-D among Medinan-pairs only. Not pre-registered.

## 6. Novel-finding potential

If PRIMARY + SECONDARY pass, this is the FIRST empirical demonstration that **[[h-new-450-window-sensitivity|H-NEW-450]]'s Type-A ROBUST outlier classification has a shared content-axis**. Specifically:
- Type-A = ROBUST = shared-family-law-content
- Q 1 al-Fātiḥa (H-410 rank 1) would be Type-α different (sui-generis liturgical)
- Q 55 (Type-D ceiling) would be Type-β different (cosmic-mercy singular)
- Q 24, Q 33 = Type-A-ROBUST content-pair

This would REFINE [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]'s outlier-factor from "4-type scale-typology" to "scale-typology + content-taxonomy."

If both fail: Type-A ROBUST is behavioral-not-content-shared, and the 4-type classification is purely operational.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_460_q24_q33_hijab_pair.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-460.json`
- Findings: `findings/phase-b-hypotheses/h-new-460-q24-q33-hijab-pair.md`

Pre-reg locked 2026-04-21.
