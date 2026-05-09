---
surah: 58
test_id: Q058-F-04
title: Q 58 ḥ-z-b (faction) lexical signature — corpus distribution and within-surah saturation
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q058-F-04-hizb-faction-vocabulary
alpha_bon: 0.01667
---

# Q058-F-04 — Pre-registration: ḥ-z-b "faction" lexical signature in Q 58

## 1. Hypothesis (locked before observation)

The closing verses Q 58:19, 22 contain the famous antithetical *ḥizb al-shayṭān* / *ḥizb Allāh* (party of Satan / party of God) construction, the classical anchor for the "two-camps" or "faction-binary" rhetorical figure in the Quran.

**H1 (one-tailed, locked direction):** Q 58 contains ≥ 3 corpus-instances of the ḥ-z-b root in its 22 verses.

**H2 (one-tailed, locked direction):** The phrase *ḥizb al-shayṭān* (`حزب الشيطان`) is **corpus-EXCLUSIVE** to Q 58. The phrase *ḥizb Allāh* (`حزب الله`) appears in fewer than 3 surahs corpus-wide.

**H3 (one-tailed, locked direction):** Q 58 holds the corpus-MAX share of ḥ-z-b root tokens; specifically, Q 58 contains ≥ 30% of all corpus instances of the ḥ-z-b root.

**H0 (joint):** any of H1, H2, H3 fails.

**Direction:** Q 58 = ḥ-z-b corpus-fingerprint (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **ḥ-z-b root detection**: orthographic-stem match on `حزب` and its declined forms (`حزبا`, `حزبه`, `أحزاب`, `الأحزاب`). Exclude false-positives where `حزب` is a sub-string of an unrelated lemma (e.g., none expected in Quranic vocabulary; manual audit included).
- **Phrase detection**:
  - *ḥizb al-shayṭān*: exact-string match on `حزب الشيطان` (with possible ال- definite article variants).
  - *ḥizb Allāh*: exact-string match on `حزب الله`.

## 3. Test statistic

- **N1**: Q 58 ḥ-z-b root token count.
- **N2a**: corpus surahs containing `حزب الشيطان` (target = 1, just Q 58).
- **N2b**: corpus surahs containing `حزب الله` (target ≤ 2 surahs).
- **N3**: Q 58's share of corpus ḥ-z-b root tokens (target ≥ 0.30).

## 4. Permutation null

**Null A (length-weighted root re-distribution):** Distribute the total corpus ḥ-z-b root tokens across surahs proportional to surah word-length. Compute the probability that Q 58 receives ≥ N1 tokens by chance. n_perm = 10,000, seed = 20260509.

**Null B (binomial closed-form):** Under the null *p̂ = 1/114*, probability that any given surah contains *both* `حزب الشيطان` and `حزب الله` (the antithetical pair) is at most ~10⁻⁴ if the two phrases are independently distributed.

## 5. Success / Failure

- **CONFIRMED**: H1 + H2 + H3 all pass; permutation p_A ≤ α_bon = 0.01667.
- **DIRECTIONAL**: H1 + H2 pass but H3 fails OR p_A > 0.01667.
- **NULL**: H1 fails (Q 58 has < 3 ḥ-z-b root tokens).

## 6. Honest limits known a priori

- Pre-flight inspection: Q 58:19 contains *حزب الشيطان* (twice in v.19 itself) and Q 58:22 contains *حزب الله* (twice in v.22). The exact-phrase pair appears within a 3-verse window (Q 58:19-22) — this antithetical pair structure is highly distinctive. Per HANDOFF/04-DISCIPLINE.md, this is a post-hoc-noticed result. Verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION (e.g., does the ḥ-z-b corpus-fingerprint replicate in chararacter-4-gram H-NEW-111b feature space).
- The classical Quranic vocabulary contains a small ḥ-z-b set (`أحزاب` is also the title of Q 33 al-Aḥzāb, "the confederates"). The Q 33 attestations are likely numerous but in a different lexical sense (military confederation vs. theological faction-binary). The pre-reg distinguishes the two by phrase-level rather than root-level for H2.
- The Q 58 antithetical *ḥizb al-shayṭān ↔ ḥizb Allāh* construction is the semantic-rhetorical origin point for the medieval Islamic political-theology category of *ḥizb* (factions, parties), and its corpus-exclusivity (if confirmed) makes Q 58 the **lexical etymon** for this entire later tradition.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, surface-phrase-and-root-stem-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 3 (H1 + H2 + H3). α_bon = 0.05/3 ≈ 0.01667.

## 9. Coordination

This test is the Q 58-specific lexical-fingerprint check. The H-NEW-1080 short-Medinan-block test (Q058-F-02) addresses content-cluster geometry; this F-04 test addresses surface-vocabulary fingerprint. No overlap.

## 10. SHA256 lock

Computed at write-time, embedded into `scripts/Q058_F_04_hizb_faction.py`, verified at runtime.
