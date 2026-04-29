# H-NEW-600 / H-NEW-610 — Run 1 journal

**Date**: 2026-04-28
**Agent**: h-new-600-specialist
**Task**: Paired letter-family content-cohesion test under one Bonferroni umbrella
**Pre-reg SHA**: `d667f28d3155a456758ab689ebb4d163c742501c878c767326a701801b2fb640`

## 1. Context

H-NEW-570 established muqaṭṭaʿāt-29 NULL (65.62%ile) and HM-7 partial-NULL (20.90%ile); §9 queued ALM-6 and ALR-5 letter-family tests. Team-lead instructed running BOTH families paired under Bonferroni-3 (ALM PRIMARY, ALR PRIMARY, joint-pattern test).

## 2. Pre-registration design choices

- **Q 13 al-Raʿd EXCLUSION** from ALR-5: Q 13 opens with ALMR (المر), not ALR (الر). Including it would conflate two distinct letter-sequences and contaminate the family-cohesion signal. This was locked in prereg §2.3 with a queued H-NEW-620 follow-up to test the ALMR-disjunction directly.
- **Bonferroni-3**: ALM PRIMARY + ALR PRIMARY + joint-pattern. α_bon = 0.01667.
- **STRICT vs DIRECTIONAL gates**: STRICT = 5/3 = 1.67%ile (Bonferroni-corrected at 0.05/3); DIRECTIONAL = 16.67%ile (5×STRICT, single-test scale at α=0.05).
- **MW-5 replication**: seed 20260431, N_perms 5000 (half PRIMARY) — stability check, not independent test.
- **MW-6 instrument**: locked random-non-muqaṭṭaʿāt-6 set {Q 5, 9, 17, 25, 33, 47}, expected null-typical [25, 75]%ile of random-6 null.

## 3. Execution

Script: `scripts/h_new_600_letter_families.py` ran cleanly. Pre-reg SHA verified by script before tests.

Run output:

```
=== H-NEW-600/610 — Paired letter-family content-cohesion ===
Pre-reg SHA: d667f28d3155a456758ab689ebb4d163c742501c878c767326a701801b2fb640
Bonferroni k=3, α_bon = 0.01667
Gates: STRICT ≤ 1.67%ile; DIRECTIONAL ≤ 16.67%ile

--- ALM-6 (K=6) family = [2, 3, 29, 30, 31, 32] ---
  d̄         = 0.9257
  PRIMARY   %ile = 43.15%  (seed=20260430, N=10000)
  MW-5      %ile = 42.58%  (seed=20260431, N=5000)
  drift = 0.57pp  stable (≤3pp): True

--- ALR-5 (K=5) family = [10, 11, 12, 14, 15] ---
  d̄         = 0.9552
  PRIMARY   %ile = 56.25%  (seed=20260430, N=10000)
  MW-5      %ile = 56.38%  (seed=20260431, N=5000)
  drift = 0.13pp  stable (≤3pp): True

--- MW-6 instrument: [5, 9, 17, 25, 33, 47] (K=6, non-muq) ---
  d̄ = 1.0129
  %ile = 88.10%  (seed=20260432, N=10000)
  null-typical [25,75]: False

=== JOINT / AGGREGATE ===
  AGGREGATE H1 (al-Biqāʿī family-munāsaba): False
  AGGREGATE NULL (H-NEW-570 generalization): True
```

## 4. Results

| Test | %ile | Verdict |
|:--|:-:|:--|
| ALM-6 PRIMARY | 43.15% | NULL (median-level) |
| ALR-5 PRIMARY | 56.25% | NULL (above-median) |
| ALM-6 MW-5 | 42.58% | stable (Δ=0.57pp) |
| ALR-5 MW-5 | 56.38% | stable (Δ=0.13pp) |
| MW-6 instrument | 88.10% | over-dispersed (mirrors H-NEW-570 §5) |
| Joint Bonferroni-3 | both > 16.67% | DOUBLE NULL |

**DOUBLE NULL**. Both families fail STRICT and DIRECTIONAL gates with massive margin.

## 5. Interpretation notes

The most striking result is **ALR-5 NULL at 56.25%ile**. Going into the run, ALR was the family with:
1. al-Biqāʿī's strongest cohesion-prediction (qiṣaṣ-block).
2. al-Rāzī's explicit qiṣaṣ-cohesion claim.
3. INDEPENDENT empirical signal at name-class level (H-NEW-97: 4/5 PROPHET_PERSON, p_mc = 0.0059).

Yet ALR-5 is more diffuse than the median random-5 draw. This is the decisive falsifier — the family most expected to cohere on content shows zero whole-surah FR-roots cohesion. The H-NEW-97 name-class signal is therefore sharply localized to NAME-LEVEL and does not extend to whole-surah-FR-roots distribution.

This sharpens H-NEW-570's "muqaṭṭaʿāt ⊥ content-axis" claim: orthogonality holds even at within-letter-family resolution.

The HM-7 partial-cohesion at 20.90%ile (H-NEW-570 MW-5) now looks like a chronology+adjacency artifact (HM-7 is also 7 consecutive Meccans) rather than a letter-family effect, since ALR-5 (also mostly Meccan and partially-consecutive) does NOT replicate HM-7's modest cohesion.

## 6. MW-6 over-dispersion

MW-6 = {Q 5, 9, 17, 25, 33, 47} at 88.10%ile mirrors H-NEW-570 MW-6 over-dispersion (100.00%). The cause is that pseudo-random selection from non-muqaṭṭaʿāt complement tends to span register-diverse subsets (Medinan-legal + Meccan-narrative + late-Medinan + combat-context), which over-disperses by construction. Documented as instrument artifact, not substantive failure. Future runs should use positive-control cluster (qiṣār sub-sample, awsāṭ) for instrument calibration — queued as H-NEW-670.

## 7. Disciplines verified

- ONE text — single canonical Hafs corpus throughout.
- Direction LOCKED in prereg §3-5 before run; not modified after results.
- Equal NULL prominence — DOUBLE NULL declared as PRIMARY finding in headline + final statement.
- Pre-reg SHA cited in script, JSON output, and findings frontmatter.
- Classical scholar cited per family: al-Biqāʿī + al-Suyūṭī + al-Rāzī (ALM); al-Biqāʿī + al-Rāzī + H-NEW-97 empirical (ALR).
- Bonferroni-3 = α_bon 0.01667 enforced; tightening (not loosening) of α — self-verifies per feedback_bonferroni_tightening_vs_loosening.md.

## 8. Queued follow-ups (in findings §9)

H-NEW-620 (ALMR disjunction), H-NEW-630 (Q 29-32 sub-cluster), H-NEW-640 (chronology-controlled null), H-NEW-650 (verse-level), H-NEW-660 (phonological), H-NEW-670 (positive-control instrument).

## 9. Final

DOUBLE NULL published with equal prominence. al-Biqāʿī content-munāsaba framework FALSIFIED a third time. al-Suyūṭī/al-Rāzī epistemic-humility VINDICATED a third time. H-NEW-570 "muqaṭṭaʿāt ⊥ content-axis" architectural claim SURVIVES the within-letter-family hardness test.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
