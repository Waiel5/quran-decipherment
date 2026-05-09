---
surah: 8
test_id: Q008-F-02
title: Q 8:17 yaqīn-formula corpus-singleton test (*wa-mā [V] idh [V] wa-lākinna allāha [V]*)
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q008-F-02-yaqin-formula
alpha_bon: 0.025
---

# Q008-F-02 — Pre-registration: Q 8:17 yaqīn-formula corpus-uniqueness

## 1. Hypothesis (locked before observation)

Q 8:17 contains the classical-balāgha keystone *wa-mā ramayta idh ramayta wa-lākinna allāha ramā* — "you did not throw when you threw, but God threw." Classical *balāgha* tradition (al-Bāqillānī *Iʿjāz al-Qurʾān*; al-Rāzī *Mafātīḥ al-ghayb* on Q 8:17; al-Sakkākī *Miftāḥ al-ʿulūm*) treats this verse as paradigmatic of *takhrīj al-fāʿil al-ḥaqīqī* (transferring the agency from the apparent-actor to the True Cause).

**Direction of test (locked):** the construction *wa-mā [V] idh [V] wa-lākinna* with V identical at positions 1 and 2 is **CORPUS-UNIQUE** (occurs exactly once in 6,236 verses, at Q 8:17).

- **H1 (strict, V₁=V₂):** the strict pattern *(و|ف)?ما [V] (إذ|اذ) [V] و?لكنّ?* with V₁ = V₂ at the surface-form level returns **exactly 1 corpus match**, at Q 8:17.
- **H2 (loose, V₁ ≠ V₂ allowed):** the loose pattern *(و|ف)?ما [V₁] (إذ|اذ) [V₂]* (ignoring V-identity) returns ≤3 corpus matches, ALL anchored on Q 8:17 or its immediate context.

**H0:** the construction is corpus-multi (≥2 strict matches in distinct verses).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **Strict pattern**: regex `(?:^|\s)(?:و|ف)?ما\s+(\S+)\s+(?:إذ|اذ)\s+(\S+)(?:\s+\S+){0,3}\s+و?لكنّ?` with the constraint group(1) == group(2) (same surface-form V).
- **Loose pattern**: same regex without the V-identity constraint, also without the *wa-lākin* requirement: `(?:^|\s)(?:و|ف)?ما\s+(\S+)\s+(?:إذ|اذ)\s+(\S+)`.
- **Hit-count**: total number of distinct (surah, verse) tuples matching.

## 3. Test statistic

- **N_strict**: count of strict-pattern matches; pre-locked H1 says N_strict = 1.
- **N_loose**: count of loose-pattern matches; pre-locked H2 says N_loose ≤ 3, all from Q 8:17 or its immediate semantic context.
- **uniqueness_q817_strict**: (1 if Q 8:17 is the sole match) / (0 otherwise).
- **uniqueness_q817_loose**: fraction of loose-matches that are Q 8:17.

## 4. Permutation null

Empirical-corpus-search-NULL: random permutation of 1-grams across the 6,236-verse corpus would not preserve construction-syntax, so a permutation-test on the construction is not directly meaningful. Instead, we compare the singleton-rate to a **density-baseline NULL**: how many other 5-token templates of the form *(prefix)?-X-V-Y-V-Z-V* are corpus-singletons?

- Sample 1000 random 5-token templates from the corpus's distinctive-construction inventory (e.g., other corpus-rare phrase templates like *innamā ... idh*, *wa-laqad ... idh*); compute their singleton-rate.
- Null hypothesis: Q 8:17 yaqīn-formula's singleton-status is no more likely than other rare-phrase singletons.

## 5. Success / Failure

- **CONFIRMED**: N_strict = 1 AND uniqueness_q817_strict = 1 AND N_loose ≤ 3 AND uniqueness_q817_loose ≥ 0.7. Both H1 and H2 pass at α_bon = 0.025 (Bonferroni-2).
- **DIRECTIONAL**: N_strict = 1 but N_loose > 3.
- **NULL**: N_strict ≥ 2 (the formula is NOT corpus-unique).
- **PRE-COMMIT VIOLATION**: Q 8:17 does NOT match the strict pattern at all (the regex was wrongly specified).

## 6. Honest limits known a priori

- The empirical-anchor extraction observed Q 8:17 as the strict-pattern singleton BEFORE the formal pre-reg lock (during pre-flight survey). The post-hoc-noticing applies; verdict ceiling = **PASS-DIRECTED**.
- Independent replication: same regex on `quran-uthmani-consonantal.json` (alternate orthographic conventions) and on `quran-min-tashkeel.json` (with-tashkeel) should converge on the same singleton-result.
- The verse Q 8:17 has the construction TWICE — *fa-lam taqtulūhum wa-lākinna allāha qatalahum* (V = qatala), then *wa-mā ramayta idh ramayta wa-lākinna allāha ramā* (V = ramā). The strict-pattern technically only requires the *wa-mā V idh V wa-lākin* form; the *fa-lam V wa-lākin* parallel-construction (without the *idh* repetition) is structurally-similar but technically distinct.

## 7. Rules-tuple

`(no-tashkeel, regex-word-boundary, surface-form-V-identity, basmala-counted-only-in-Q1, Hafs-Kufan)`.

## 8. Bonferroni

k = 2 (strict + loose pattern); α_bon = 0.025.

## 9. Coordination

This is a Q 8-specific construction-fingerprint test. No other surah specialist has run a yaqīn-formula test.

## 10. SHA256 lock

Computed at write-time; embedded into `scripts/Q008_F_02_yaqin_formula.py`; verified at runtime.
