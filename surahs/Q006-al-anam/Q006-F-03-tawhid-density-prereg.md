---
surah: 6
test_id: Q006-F-03
title: Tawḥīd-anti-idolatry lexical density — Q 6 vs Q 1 vs Q 112 vs corpus
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 2
bonferroni_family: Q006-F-03-tawhid-density
alpha_bon: 0.025
direction_locked: TOP-3 (HIGH-DENSITY)
---

# Q006-F-03 — Pre-registration: Tawḥīd-anti-idolatry lexical density

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 6 al-Anʿām is among the **TOP-3 corpus-densest tawḥīd-anti-idolatry surahs** on a locked lexical cluster combining (a) divine-singularity formulae, (b) anti-idolatry vocabulary. Q 6 is classically the *Sūrat al-Ḥujja* — a sustained creedal argument against shirk. Q 112 (al-Ikhlāṣ) is the *thuluth al-Qurʾān* tawḥīd-distillation; Q 1 (al-Fātiḥa) is the prayer-formulation. H1 predicts: Q 6 sits in the same tawḥīd-density top-cluster as these two, with empirical signature distinct from generic Meccan or Medinan registers.

**Direction:** Q 6 in top-3 of corpus on the joint metric (LOCKED).

**H0:** Q 6 ranks > rank 5 on tawḥīd-density.

**Pre-commit violation:** Q 6 ranks > rank 10.

## 2. Operational definition

**Tawḥīd cluster (locked surface-form regex set):**
- لا إله إلا (literally: "no god except"): \bلا\s+إله\s+إلا\b
- لا شريك (no partner): \bلا\s+شريك\b
- شريك / شركاء / شركاءهم / شركائكم (associates): \bشرك(?:اء|ائ|اءه|اءك)\w*\b OR \bشريك\w*\b
- وحده (alone, only Him): \bوحده\b
- اتخذ\w+ ولد (took as child / sired offspring polemic): \bاتخذ\w*\s+\w*ولد\b
- يشركون (they associate): \bيشركون\b OR \bأشركوا\b OR \bأشركتم\b OR \bتشركوا\b
- بشرك (polytheism root tokens): \bالشرك\b
- لله الواحد (Allāh the One): regex with الواحد proximate to الله

**Per-surah metrics:**
- Cell A: `tawhid_token_count` = total occurrences across all clusters.
- Cell B: `tawhid_density_per_100_words` = (count / total_words) × 100.

Bonferroni k=2, α_bon = 0.025.

## 3. Test statistic / Success / Failure

- **CONFIRMED:** Q 6 in top-3 on Cell B (length-controlled density). Direction matches.
- **DIRECTIONAL:** Q 6 in top-5 on Cell B.
- **NULL:** Q 6 ≥ rank 6 on Cell B.
- **Pre-commit violation:** Q 6 ≥ rank 10 on Cell B.

Cell A is reported as supplementary (raw count is length-confounded).

Cross-validation (descriptive only, not part of pre-reg verdict):
- Where do Q 1 and Q 112 rank? Sanity-check expected: Q 112 rank-1 on Cell B (4 verses, formulaic *qul huwa allāhu aḥad*). Q 1 expected near top on Cell B (formulaic in 7 verses).

## 4. Garden-of-forking-paths log (BEFORE observation)

Author has not observed corpus-wide rankings on this cluster. Cluster definitions are derived from classical Sufi/kalāmī catalogs of *kalimāt al-tawḥīd* (cf. al-Suyūṭī *al-Itqān* nawʿ on tawḥīd; al-Bāqillānī *iʿjāz al-tawḥīd*). The Cell A vs Cell B split is standard length-controlled-density methodology (cf. Q012-F-03).

Single-verse short-surah artifacts: Q 112's 4 verses + 14 words give a high density on the *qul huwa* formula — this is the empirically-anchored tawḥīd-thuluth claim, NOT an artifact. Pre-reg ratifies that Q 112 IS expected to top Cell B; the test is whether Q 6 (5,000-word surah) joins it in the top cluster.

## 5. Honest limits known a priori

- Regex-based; misses anti-idolatry vocabulary in metaphorical or implicit form (e.g., *al-ʿālamīn*, *bal*, *am*, *afa*).
- Lexical cluster is curated from kalāmī tradition; alternative selections (e.g., Sufi *waḥdat al-wujūd* terms) would produce different rankings.
- Q 109 al-Kāfirūn (anti-idolatry creedal-disavowal) might score very high; competitors include Q 112, Q 109, Q 6, Q 7, Q 19, Q 21.

## 6. Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at pre-reg-completion. Embedded into `surahs/scripts/Q006_F_03_tawhid_density.py`.
