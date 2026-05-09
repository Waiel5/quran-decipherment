---
surah: 89
test_id: Q089-F-02
title: Q 89:6-14 destroyed-civilizations catalog root-overlap with Q 7 al-Aʿrāf, Q 11 Hūd, Q 26 al-Shuʿarāʾ
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q089-F-02-destroyed-civilizations
alpha_bon: 0.01667
---

# Q089-F-02 — Pre-registration: Q 89:6-14 destroyed-civilizations catalog root-overlap with corpus prophet-narrative-compendia

## 1. Hypothesis (locked before observation)

Q 89:6-14 contains a 9-verse compressed catalog of pre-Islamic destroyed civilizations:
- ʿĀd of Iram of the columns (vv. 6-8)
- Thamūd who hewed the rocks (v. 9)
- Pharaoh of the pegs (v. 10)
- Generic iniquitous-and-destroyed (vv. 11-13)
- *inna rabbaka la-bi-l-mirṣād* (v. 14)

The "destroyed civilizations" theme also appears in extended form in Q 7 al-Aʿrāf (Hūd-ʿĀd, Ṣāliḥ-Thamūd, Mūsā-Firʿawn, Lūṭ), Q 11 Hūd (same 4 + Shuʿayb-Madyan + Nūḥ), Q 26 al-Shuʿarāʾ (poet-cycle of Mūsā-Firʿawn, Ibrāhīm, Nūḥ-deluge, Hūd-ʿĀd, Ṣāliḥ-Thamūd, Lūṭ-Sodom, Shuʿayb-Madyan).

**H1 (locked direction, primary)**: Q 89:6-14's QAC-stem-root signature has ABOVE-RANDOM overlap with the destroyed-civilizations sub-blocks of Q 7, Q 11, Q 26. Operationalized: cosine similarity over the union root-vocabulary of Q 89:6-14 with the 3 reference blocks ≥ a corpus-baseline of random 9-verse spans.

**H2 (locked direction, secondary)**: Q 89:6-14 is more root-similar to the 3 destroyed-civilization compendia (mean cosine over the 3 blocks) than to a random 3-block control set chosen from non-prophet-narrative surahs (e.g., Q 56 al-Wāqiʿah, Q 87 al-Aʿlā, Q 92 al-Layl).

**H3 (locked direction, secondary)**: the EXACT proper-noun set {ʿĀd, Iram, Thamūd, Firʿawn} of Q 89:6-10 — operationalized as the 4-tuple of distinct lemmas — appears jointly in NO OTHER single 9-verse contiguous span across the corpus. Q 89:6-14 holds a corpus-EXACT compressed-catalog signature.

**H0**: Q 89:6-14's vocabulary signature is statistically indistinguishable from random short-Meccan-tail blocks; no compressed-catalog cohesion.

## 2. Operational definitions

- **Source**: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4) for stem-root extraction; `data/alt-text/quran-uthmani-consonantal.json` for surface tokens.
- **Q 89:6-14 block**: 9 verses, root-bag built from QAC stem-roots.
- **Reference blocks** (locked before observation):
  - **Q 7 destroyed-civilizations sub-block**: Q 7:65-102 (Hūd-ʿĀd through Pharaoh-Mūsā). 38 verses.
  - **Q 11 destroyed-civilizations sub-block**: Q 11:25-99 (Nūḥ through Pharaoh). 75 verses (cuts long).
  - **Q 26 destroyed-civilizations sub-block**: Q 26:105-191 (Nūḥ through Shuʿayb). 87 verses.
- **Cosine similarity**: bag-of-roots cosine after L2-normalization.
- **H1 null**: 10,000 random 9-verse contiguous spans drawn from {Q 1..Q 114} with same total-verse-count constraint (no overlap with Q 89). Null mean = mean cosine to the 3 reference blocks.
- **H3 catalog-uniqueness**: scan all 9-verse contiguous spans across all 114 surahs for joint presence of the 4 proper-noun lemmas {ʿAd / ʿAdin (root ع-و-د / proper noun عاد), Iram (إرم), Thamūd (ثمود), Firʿawn (فرعون)}. Use orthographic-token match.

## 3. Test statistic

- **H1**: cos(Q 89:6-14, {Q 7, Q 11, Q 26 blocks}) — mean across 3 blocks. Permutation p = fraction of random 9-verse spans with ≥ this similarity.
- **H2**: signed-difference cos(Q 89:6-14, {Q 7, Q 11, Q 26}) − cos(Q 89:6-14, {Q 56:1-9, Q 87:1-9, Q 92:1-9 controls}). PASS if positive AND > 0.
- **H3**: integer count of 9-verse spans (other than Q 89:6-14) containing all 4 proper-noun lemmas. PASS if = 0.

## 4. Success / Failure

- **CONFIRMED**: ≥ 2/3 sub-tests PASS at α_bon = 0.01667.
- **DIRECTIONAL**: 1/3 PASS.
- **NULL**: 0/3 PASS.
- **Pre-commit violation**: cos(Q 89, controls) > cos(Q 89, references); OR a different 9-verse span ALSO holds the 4-lemma joint signature outside Q 89.

## 5. Honest limits known a priori

- The "destroyed-civilizations corpus pattern" is a CLASSICAL framework (al-Ṭabarī, al-Rāzī, Ibn Kathīr — *qaṣaṣ al-anbiyāʾ* tradition). Q 89 is the corpus's MOST COMPRESSED instance: 9 verses cover 4 destroyed-civilizations (whereas Q 11 takes ~75 verses).
- Empirical-anchor disclosure: it has not been directly checked whether the 4-proper-noun set is corpus-EXACT to Q 89:6-14, BUT classical commentary records that the *Iram dhāt al-ʿimād* phrase is corpus-unique. Brief states "destroyed-civilizations corpus pattern Q 7, 11, 26 connection" as the locked test direction.
- The H3 corpus-EXACT-9-verse-span test is the strongest test; H1/H2 are similarity-baseline tests subject to length and content confound.
- Confound-acknowledgement: short-Meccan-tail surahs (Q 86-91) all share short-verse / oath-style vocabulary; the cosine baseline may be elevated by short-tail-style alone, not by destroyed-civilizations-content per se. The 3-block reference is INTRA-MECCAN-NARRATIVE; the 3-block control is OTHER-MECCAN-STYLES (oath / praise / wisdom). The control is constructed to absorb the short-tail-style confound.

## 6. Rules-tuple

`(no-tashkeel, hamza-normalized, final-yā-normalized, QAC-v0.4-stem-roots, orthographic-tokens-for-PN, bag-of-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 3 (H1, H2, H3). α_bon = 0.01667.

## 8. SHA256 lock

Embedded in `scripts/Q089_F_02_destroyed_civilizations.py`; verified at runtime.
