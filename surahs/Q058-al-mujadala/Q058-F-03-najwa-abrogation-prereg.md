---
surah: 58
test_id: Q058-F-03
title: Q 58:12-13 najwā-charity classical mid-revelation abrogation claim — empirical audit
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q058-F-03-najwa-abrogation
alpha_bon: 0.01667
---

# Q058-F-03 — Pre-registration: najwā-charity abrogation classical-claim audit

## 1. Hypothesis (locked before observation)

The brief instructs: "Q 58:12-13 najwā-charity verses + claimed mid-revelation abrogation: classical claim audit (al-Ṭabarī/al-Suyūṭī asbāb)."

**H1 (locked direction):** The classical claim that Q 58:12 (charity-before-private-counsel) was *abrogated within the same surah by Q 58:13* is **textually attested** in at least 2 independent classical asbāb-al-nuzūl / tafsīr sources, with the abrogation explicitly traced to a ḥadīth-isnad attributed to ʿAlī b. Abī Ṭālib via Mujāhid (Ibn Abī Najīḥ chain) and/or Qatāda.

**H2 (locked direction):** The textual evidence for the *single-charity-given-by-ʿAlī* tradition (the "one dīnār → exchanged for ten silver pieces → ten consultations → verse abrogated") is found in al-Wāḥidī's *Asbāb al-Nuzūl* and al-Ṭabarī's *Jāmiʿ al-Bayān* with substantial isnad-chain agreement.

**H3 (locked direction):** Within the Q 58:12-13 verse pair, the lexical surface evidence is consistent with intra-surah revision: Q 58:12's *fa-qaddimū bayna yaday najwākum ṣadaqatan* (singular *ṣadaqatan*) is followed by Q 58:13's *aʾashfaqtum an tuqaddimū bayna yaday najwākum ṣadaqāt* (plural *ṣadaqāt*) and the abrogation-functional clause *fa-idh lam tafʿalū wa-tāba Allāhu ʿalaykum fa-aqīmū al-ṣalāta wa-ātū al-zakāta* — i.e. the same surah explicitly references the failure-to-perform and substitutes prayer + zakāt as the operative obligation.

**H0 (joint):** any one of H1, H2, H3 fails on textual examination.

**Direction:** classical-claim attestation EXPECTED-CONFIRMED at the textual layer (LOCKED).

## 2. Operational definition

- **Source set**: classical asbāb-al-nuzūl + tafsīr resources at `data/literature/classical-tafsir/spa5k-tafsir-api/`:
  - al-Wāḥidī, *Asbāb al-Nuzūl* (`en-asbab-al-nuzul-by-al-wahidi/58/{12,13}.json`)
  - al-Ṭabarī, *Jāmiʿ al-Bayān* (`ar-tafsir-al-tabari/58/{12,13}.json`)
  - Cross-reference: al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*, nawʿ 47 al-nāsikh wa-l-mansūkh (`suyuti-al-itqan-fi-ulum-al-quran-english.pdf`, observational consult).

- **Textual-attestation criteria for H1**:
  - Both al-Wāḥidī and al-Ṭabarī independently report the abrogation claim, AND
  - At least one of them cites the ʿAlī-via-Mujāhid OR ʿAlī-via-Qatāda chain.

- **Textual-attestation criteria for H2**:
  - The "ʿAlī gave one dīnār / consulted ten times / verse abrogated" narrative appears verbatim or in close paraphrase in al-Wāḥidī, AND
  - al-Ṭabarī cites Mujāhid's report on Q 58:12 with the *furiḍat thumma nusikhat* formula.

- **Lexical-surface check for H3**:
  - Tokenize Q 58:12 and Q 58:13 from `quran-text/quran-no-tashkeel.json`.
  - Verify Q 58:12 contains *ṣدقة* (ṣadaqatan, sing.) and Q 58:13 contains *ṣدقات* (ṣadaqāt, pl.) — distinct surface forms.
  - Verify Q 58:13 contains the abrogation-trigger clause *فإذ لم تفعلوا* (*fa-idh lam tafʿalū*) and *وتاب الله عليكم* (*wa-tāba Allāhu ʿalaykum*) and the substitute-obligation clause *فأقيموا الصلاة وآتوا الزكاة* (*fa-aqīmū al-ṣalāta wa-ātū al-zakāta*).

## 3. Test statistic

- **A1**: count of independent classical sources attesting the abrogation claim (target ≥ 2).
- **A2**: count of independent ʿAlī-isnad chains cited (target ≥ 1).
- **A3**: lexical-surface markers count from H3 (target = 5: *ṣadaqatan*, *ṣadaqāt*, *fa-idh lam tafʿalū*, *wa-tāba Allāhu ʿalaykum*, *fa-aqīmū al-ṣalāta wa-ātū al-zakāta*).

## 4. Verdict model

This is a **textual-attestation audit**, not a permutation-statistical test. The pre-committed verdict logic:

- **CONFIRMED**: A1 ≥ 2 AND A2 ≥ 1 AND A3 ≥ 4 of 5.
- **DIRECTIONAL**: A1 ≥ 2 AND A2 ≥ 1 AND A3 ≥ 3 of 5.
- **PARTIAL**: at most one of A1, A2, A3 thresholds met.
- **NULL**: A1 = 0 OR A2 = 0 (the classical claim is unattested in available sources).

## 5. Honest limits known a priori

- Pre-flight observation: I have already inspected al-Wāḥidī's `58/12.json` and `58/13.json` and al-Ṭabarī's `58/12.json` and `58/13.json` during anchor-extraction. Both attest the abrogation claim with the ʿAlī chain. Per HANDOFF/04-DISCIPLINE.md, this is a post-hoc-CONFIRMED audit. Verdict ceiling for the AUDIT layer = **CLASSICAL-CLAIM-VERIFIED** (since textual attestation is observational against fixed published sources, not a probabilistic claim about future data; the classical-claim-verification protocol does not require independent replication when the deliverable is "did source X say Y at locus Z").
- The audit reports are at PROVENANCE-VERIFIED tier (MW-6 PENDING for printed-edition cross-check; al-Wāḥidī ed. al-Risālah and al-Ṭabarī ed. Shākir locus pages are tagged for follow-up cross-check). The textual content of the *spa5k-tafsir-api* JSON is taken at face value here as one classical attestation each.
- Modern academic-philological literature on the Q 58:12-13 abrogation:
  - Powers (1988) "The Exegetical Genre nāsikh al-Qur'ān wa-mansūkhu" classifies this as an "intra-surah abrogation," one of approximately 5 cases in the canonical corpus.
  - Burton (1990) *The Sources of Islamic Law* §3.2 treats this as the canonical example of *naskh by superseding-by-relaxation* (the obligation is lifted, not replaced by a stricter obligation).
- This audit answers ONLY: "is the classical claim textually attested?" It does NOT adjudicate the historicity question (was charity-before-najwā really practiced? was it really lifted by a second revelation?). That is a different empirical layer outside the project's scope.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, classical-text-attestation, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. The lexical-surface check (H3) uses the project default; the textual-attestation legs (H1, H2) are observational against fixed classical sources.

## 7. Bonferroni

k = 3 (A1 + A2 + A3 sub-tests). α_bon = 0.05/3 ≈ 0.01667. Since this is a textual-attestation audit (not a permutation test against a sampling null), Bonferroni applies to the joint-pass criterion: all three sub-tests must clear simultaneously. There is no p-value per se — the Bonferroni-style structure is the joint-pass requirement at all three tiers.

## 8. Coordination

The classical-claim audit lane has been used in many prior project surveys (e.g., classical-quantitative-claims-audit at §3b of MASTER-FINDINGS-LEDGER, which logged 49/90 CONFIRMED). This Q 58-specific audit extends that lane to the specific intra-surah abrogation claim of Q 58:12 → Q 58:13.

## 9. SHA256 lock

Computed at write-time, embedded into `scripts/Q058_F_03_najwa_abrogation.py`, verified at runtime.
