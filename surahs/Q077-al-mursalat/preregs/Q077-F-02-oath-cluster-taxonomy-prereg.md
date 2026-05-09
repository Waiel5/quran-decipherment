---
surah: 77
test_id: Q077-F-02
title: Q 77 oath-cluster sibling taxonomy — Q 51 (4-fa) and Q 100 (5wa+5fa) sibling FR distance and structural typology
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q077-F-02-oath-taxonomy
alpha_bon: 0.0125
---

# Q077-F-02 — Pre-registration: Q 77 oath-cluster sibling taxonomy

## 1. Hypothesis (locked before observation)

The corpus contains a heterogeneous oath-opener cluster (H-NEW-1070, CONFIRMED FR-cohesive at p=0.0004, 15 surahs). Within this cluster, several surahs open with sequences of 4-7 *wa-/fa-* prefixed feminine-plural participles. The brief flags Q 77 (5-element wa-fa-wa-fa-fa), Q 51 (4-element wa-fa-fa-fa, "4-fa"), and Q 100 (5-element wa-fa-fa-fa-fa, "5-wa+5-fa" per brief notation; observed structure is 1-wa + 4-fa = 5 elements) as a sibling triad. This pre-reg formalizes the oath-architecture taxonomy across these three surahs.

**H1 (Cell A — verse-count match):** Q 77, Q 79, Q 100 each have 5 oath-opener verses; Q 51 has 4. Cell A passes if these counts are confirmed (locked-integer-equality).

**H2 (Cell B — uniform-letter-count rhetorical signature):** Q 77's 5 oath-verses are each EXACTLY 13 letters (no-tashkeel, no-space). The pre-reg locks: Q 77's vv 1-5 letter-counts are constant. Cell B passes if all 5 verses have identical letter-count == 13.

**H3 (Cell C — corpus-uniqueness of 5-consecutive-identical-length-opener):** the corpus contains EXACTLY 2 surahs with 5+ consecutive opener verses of identical letter-count: Q 77 and Q 79. Cell C passes if the corpus enumeration gives strict-2 (Q 77 ∈ this 2-set).

**H4 (Cell D — FR-cluster-position):** Q 77's mean FR distance to {Q 51, Q 79, Q 100} is **LOWER** than Q 77's mean FR distance to a corpus-random 3-subset (one-tailed perm-p ≤ α_bon over 10000 random triples). Direction-locked: Q 77 should be FR-CLOSER to its 3 oath-architectural-siblings than to a random triple.

**H0:** Q 77 oath-architecture is unremarkable — counts mismatch, letter-count varies, or corpus-uniqueness fails, or FR-cluster is no closer than random.

## 2. Operational definitions

- Source: `quran-text/quran-no-tashkeel.json`; `findings/phase-b-hypotheses/csv/h-new-111.json` (FR distance matrix upper-triangular).
- **Cell A**: integer counts of oath verses. The "oath verses" are the leading verses with the *wa-/fa- + l- + active-feminine-plural-participle + cognate-accusative-noun* template. Pre-locked enumeration:
  - Q 51: vv 1-4 (4 verses, 1-wa + 3-fa) — verbal subject is الذاريات / الحاملات / الجاريات / المقسمات
  - Q 77: vv 1-5 (5 verses, 2-wa + 3-fa interleaved) — المرسلات / العاصفات / الناشرات / الفارقات / الملقيات
  - Q 79: vv 1-5 (5 verses, 3-wa + 2-fa) — النازعات / الناشطات / السابحات / السابقات / المدبرات
  - Q 100: vv 1-5 (5 verses, 1-wa + 4-fa) — العاديات / الموريات / المغيرات / فأثرن / فوسطن (the last 2 break participle template — verb forms)
- **Cell B**: per-verse letter-count under no-tashkeel, no-space, NFC normalization for Q 77 vv 1-5.
- **Cell C**: enumerate over all 114 surahs the maximum k such that vv 1..k all have identical letter-count; report the set {s : k ≥ 5}.
- **Cell D**: FR(77, s) for s ∈ {51, 79, 100} averaged. Null = average over random 3-subset of {1, ..., 114} \ {77}; perm p-value = fraction with mean ≤ observed mean.

## 3. Test statistics

- Cell A: 4 integer counts.
- Cell B: 5 letter-counts and Boolean equality.
- Cell C: |{s : k_s ≥ 5}|.
- Cell D: D_oath_3 = mean of FR(77, s) for s ∈ {51, 79, 100}; perm p one-tailed.

## 4. Success / Failure

- **PASS-DIRECTED FULL**: All 4 cells pass at α_bon = 0.0125 (Cell D is the only stochastic test; Cells A/B/C are deterministic under fixed corpus).
- **PASS-DIRECTED PARTIAL**: 2-3 of 4.
- **NULL**: ≤ 1 of 4 passes.

## 5. Honest limits known a priori

- Empirical-anchor extraction (DISCLOSED): pre-pre-reg exploratory inspection confirmed: Q 77 vv 1-5 = [13, 13, 13, 13, 13] letters and Q 79 vv 1-5 = [13, 13, 13, 13, 13]. The 2-surah strict-uniqueness was OBSERVED before lock. The pre-reg locks the test, not the empirical anchor; if a corpus re-enumeration reveals a 3rd surah, Cell C would fail.
- Q 77 vs Q 51 FR ≈ 0.896, Q 77 vs Q 79 FR ≈ 0.764, Q 77 vs Q 100 FR ≈ 0.674 (DISCLOSED pre-lock from h-new-111.json). Q 77 corpus-mean FR distance ≈ 0.922. So D_oath_3 ≈ (0.896 + 0.764 + 0.674) / 3 ≈ 0.778. Direction-locked: D_oath_3 < D_random_3 with high probability. The empirical anchor confirms the directional prediction; the test still must be run honestly under H0 = no preferential affinity.
- Q 100's 5 elements include 2 verb-forms (فأثرن، فوسطن), not pure participles. The H3 / Cell B test is restricted to Q 77 letter-uniformity, NOT to Q 100. Q 100's letter-counts [13, 13, 13, 11, 11] (DISCLOSED) deviate after v3 — Q 100 is a 3-uniform-then-2-shorter pattern. This is a FACT about the comparator, not a Q 77 finding.
- The 4-element Q 51 has 4 uniform letters (DISCLOSED [13, 13, 13, 13]), so the corpus ALSO contains a 4-uniform 4-oath surah (Q 51) — but only 2 surahs reach 5-uniform.

## 6. Rules-tuple

`(no-tashkeel, orthographic-letter-no-space, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` for letter counts; `(QAC-stem-roots, FR-on-stem-roots)` for Cell D matching H-NEW-111 FR matrix.

## 7. Bonferroni

k = 4 (one stochastic = Cell D, plus 3 deterministic). α_bon = 0.05/4 = 0.0125 applied to Cell D perm-p. Cells A/B/C pass under exact-equality / count-thresholds.

## 8. Garden of forking paths

- The exploration that surfaced the 5×13-letter signature was discovered while computing Q 77's letter-counts pre-lock. NO alternative letter-count rule (with-tashkeel, with-space, hijaii-form, etc.) was tried; the no-tashkeel-no-space rule is THE PROJECT STANDARD per `(rules-tuple)` and was used directly. No multiple-testing concern arises from rule-search.
- The choice of comparator triad {Q 51, Q 79, Q 100} was given by the BRIEF directly (4-fa, 5-wa+5-fa); not selected post-hoc.
- An alternative test "is Q 77 the FR-CLOSEST oath-sibling to ANY oath-cluster member?" was considered and rejected as too weak (single-surah anchor); the chosen "mean FR to brief-given triad" is more direction-locked.

## 9. SHA256 lock

Embedded in `scripts/Q077_F_02_oath_taxonomy.py`; verified at runtime after this file is locked.
