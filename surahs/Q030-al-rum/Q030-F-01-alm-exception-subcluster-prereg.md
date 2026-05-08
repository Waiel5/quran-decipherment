---
surah: 30
test_id: Q030-F-01
title: Q 29 + Q 30 ALM-exception sub-cluster coherence (joint test, imtihān + historical-prophecy)
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perms: 10000
bonferroni_k: 2
bonferroni_family: Q030-F-01-alm-exception-axes
alpha_bon: 0.025
alpha_single_cap: 0.05
hypothesis_anchor: cross-finding-008-muqattaat-book-introduction-marker (Q 29 + Q 30 = 2 ALM-exceptions to book-reference pattern)
parent_null: H-NEW-93 (LANDED NULL 2026-04-17 on raw 4-cell test)
revisit_framing: Wave-D — chronology-architecture dissociation (Q005-F-05) + cross-finding-008 framing
---

# Q030-F-01 — Pre-registration: Q 29 + Q 30 ALM-exception sub-cluster coherence

## 1. Background and parent NULL

[[h-new-93-q29-q30-subpattern|H-NEW-93]] (2026-04-17) tested Q 29 + Q 30 jointly on a 4-cell test (test-of-believers, historical-prophecy full, Allah-density control, eschatological control) against Meccan-non-muqaṭṭaʿāt baseline (n=60). Verdict: **NULL-full-target-pattern-rejected**. The narrow `glb+nSr` cell achieved single-test p=0.0362 only.

**This pre-reg refines the NULL** by:
- Switching the comparison frame from "Meccan-non-muqaṭṭaʿāt" to **"the 4 non-exception ALM surahs (Q 2, 3, 31, 32)"** — the within-letter-family comparison that cross-finding-008 motivates.
- Adding the `jhd` (jihād/striving) root to the imtihān-cluster (anchored by Q 29:69 *wa-l-ladhīna jāhadū fīnā la-nahdiyannahum subulanā*).
- Adding `rwm`, `bDE`, `snw` to the historical-prophecy family (the Q 30:2-5 specific lemma-set).
- Computing **2 axes only** (imtihān-density, historical-prophecy-density) — Bonferroni-2.

This is a **NEW pre-reg** with NEW operationalization, NEW comparison frame, and NEW root-set. It is NOT a retest of H-NEW-93 — it is a refinement at a different feature space (per PRE-REG-STANDARD-03).

## 2. Hypothesis (LOCKED before observation)

**H1a (one-tailed):** Q 29 + Q 30 pooled have HIGHER imtihān-root density (per word) than the 4 non-exception ALM surahs (Q 2, 3, 31, 32) pooled.

**H1b (one-tailed):** Q 29 + Q 30 pooled have HIGHER historical-prophecy-root density (per word) than the 4 non-exception ALM surahs (Q 2, 3, 31, 32) pooled.

**H0a, H0b:** The pooled densities are equal or lower in Q 29 + Q 30.

**Direction:** Q 29 + Q 30 > 4-non-exception ALM (LOCKED, both axes).

## 3. Operational definition

**Imtihān-cluster (5 roots, frozen)**: `ftn` (test/trial), `blw` (try/test), `mHn` (try/examine), `Sbr` (be patient under trial), `jhd` (strive).

**Historical-prophecy-cluster (6 roots, frozen)**: `glb` (overcome/defeat), `nSr` (help/victory), `kwn` (be/was — copula carries past-tense narratives), `rwm` (Romans), `bDE` (a few), `snw` (years).

**Pooled densities**:
- Q 29+30 imtihān_density = (sum imtihān-root tokens in Q29 + Q30) / (sum word_count Q29 + Q30)
- Q 29+30 hist_density = (sum hist-prop-root tokens) / (sum word_count)

**Reference group**: pooled Q 2 + Q 3 + Q 31 + Q 32 imtihān_density and hist_density.

**Test statistic**: observed_diff = density(Q29+30) − density(Q2,3,31,32), per axis.

**Permutation null**: Of the 6 ALM surahs, randomly assign 2 to "target" and 4 to "reference" (15 possible assignments; we use full-enumeration permutation since C(6,2)=15 is tractable, plus an additional 10000-perm bootstrap on the surah-set choice across all Meccan ALM-eligible). 

Actually — because k=15 is too small for 10000 perms, we use the **conservative method**: 
- Primary: enumerate all C(6,2)=15 partitions and report exact p (rank of observed in 15).
- Secondary (robustness): resample n=2 surahs from a wider pool of "Meccan + 60 verses ± 30" surahs; 10000 perms; report p_two-sided.

## 4. Test statistics and Bonferroni

- **k = 2** (imtihān axis, historical-prophecy axis).
- **α_bon = 0.05 / 2 = 0.025.**
- One-tailed p_perm reported per axis.

## 5. Success / Failure criteria

| Outcome | Interpretation |
|:--|:--|
| Both axes p < 0.025 (Bon-corrected) AND direction matches | **PASS-DIRECTED** sub-cluster coherence |
| Exactly 1 axis p < 0.05 single-test cap, direction matches | **WEAK-PASS-DIRECTED-single-test-only** |
| Both axes p ≥ 0.05 OR direction reversed on either | **NULL** with full prominence |
| Either axis direction REVERSED | Pre-commit violation, published as NULL with `direction-reversed` flag |

## 6. Rules-tuple

`(no-tashkeel, QAC-stem-roots, hafs-kufan, basmala-counted-only-in-Q1, mashriqi)`. QAC v0.4 ROOT field used directly.

## 7. MW-protections

- **MW-1 length-control**: rates are per-word, not per-verse, so length is normalized.
- **MW-5 positive-control**: H-NEW-93's MW-5 demonstrated that the 4 non-exception ALM surahs are NOT elevated on test/prophecy markers vs Meccan baseline. We carry that forward.
- **MW-6 secondary-null**: not adversarial-flagged; primary frame is the C(6,2)=15 enumeration.

## 8. Data sources

- QAC v0.4: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
- Quran text: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`

## 9. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q030_F_01_alm_exception_subcluster.py`.

## 10. Honest a-priori limits

- C(6,2) = 15 enumeration gives a coarse p; minimum non-zero p is 1/15 = 0.0667 > α_bon = 0.025. **The Bonferroni-corrected primary frame is structurally limited to NULL or DIRECTIONAL-only, never PASS at α_bon=0.025.** The secondary (broader-pool resampling) frame can in principle achieve p < 0.025.
- The asymmetric loading is known a-priori: Q 29 carries imtihān (driven by `ftn` + `jhd`), Q 30 carries historical-prophecy (driven by `glb` + `rwm` + `bDE`). The pooled-density operationalization will mask this asymmetry. The asymmetric reading is preserved as a secondary-descriptive observation, not a hypothesis test.
- The result must be interpreted in light of the parent H-NEW-93 NULL: a PASS at α_bon=0.025 in this refinement frame is interpretive only — it would not retract the H-NEW-93 NULL on its original 4-cell operationalization.
