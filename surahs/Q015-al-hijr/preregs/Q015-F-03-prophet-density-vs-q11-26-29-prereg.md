---
surah: 15
test_id: Q015-F-03
title: Q 15 prophet-density vs Q 11/26/29 (Lot+Saliḥ-tribe surahs)
file_type: pre-registration
date_locked: 2026-05-08
seed: 20260508
bonferroni_k: 3
bonferroni_family: Q015-F-family-2026-05-08
alpha_bon: 0.0167
---

# Q015-F-03 — Pre-registration: Q 15 prophet-name density vs Q 11/26/29

## 1. Hypothesis (locked before observation)

**Background**: Q 15 contains the Lot narrative (Q 15:51-77, 27 verses) and the Hijr-tribe (Thamūd / Ṣāliḥ-tribe) narrative (Q 15:80-84, 5 verses). Other Lot-narrative + Ṣāliḥ-tribe Quranic surahs are Q 11 (Hūd, with extensive Lot + Ṣāliḥ + Hūd + Nūḥ + Shuʿayb cycle), Q 26 (al-Shuʿarāʾ, with Lot + Ṣāliḥ + Mūsā + Nūḥ + Hūd + Shuʿayb), Q 29 (al-ʿAnkabūt, with Lot + Ṣāliḥ + Nūḥ + Mūsā + Shuʿayb).

This test computes the prophet-name density (named-prophet-attestations per 1,000 words) for Q 15 vs Q 11, 26, 29 and asks: is Q 15's prophet-density LOWER than Q 11/26/29's, despite hosting Lot + Hijr-tribe narratives?

**H1 (direction-locked, one-tailed)**: Q 15's prophet-name density (per 1,000 words, computed across all named prophets — Lūṭ, Ṣāliḥ, Thamūd, Mūsā, Nūḥ, Hūd, Shuʿayb, Ibrāhīm, Yūsuf, Yaʿqūb, Ismāʿīl, Isḥāq, ʿĪsā, Yūnus, Dāwūd, Sulaymān, Yaḥyā, Zakariyā, Ilyās, Ayyūb, Idrīs, Dhū al-Kifl) is **LOWER** than Q 11's, Q 26's, AND Q 29's prophet-densities.

**H0**: Q 15's prophet-density ≥ that of Q 11, 26, OR 29.

**Direction LOCKED**: Q 15 has the LOWEST prophet-density among the 4-surah comparison set.

## 2. Operational definition

**Surah text**: full no-tashkeel surah-level text (concatenated verses).

**Prophet-name list (Arabic forms)**: 
[إبراهيم, لوط, صالح, ثمود, موسى, نوح, هود, شعيب, عيسى, يوسف, يعقوب, إسماعيل, إسحاق, يونس, داود, سليمان, زكريا, يحيى, إلياس, أيوب, إدريس, ذو الكفل, محمد]

**Density metric**: `density(s) = total_attestations(s) / n_words(s) × 1000`, where total_attestations is the sum of substring-attestations across all prophet-names in the surah's text.

## 3. Test statistic

**Primary (direction-locked)**: density(Q 15) < min(density(Q 11), density(Q 26), density(Q 29)).

**Secondary** (descriptive): rank of Q 15 among the 4-surah comparison; per-surah density values.

## 4. Success / Failure thresholds

- **CONFIRMED**: density(Q 15) is LOWEST of {Q 11, 15, 26, 29} (rank 4 of 4).
- **DIRECTIONAL**: density(Q 15) is below the median of the 4-surah set.
- **NULL**: density(Q 15) is NOT below the lowest of {Q 11, 26, 29}.
- **PRE-COMMIT VIOLATION**: density(Q 15) is highest among the 4 (the OPPOSITE direction).

## 5. Honest limits known a priori

- The substring-search counts attestations as substring-occurrences, NOT distinct prophet-mentions. A prophet-name appearing multiple times in one verse counts each occurrence.
- Q 15 has fewer verses (99) but very short verses (mean 6.7 w/v); Q 11 has 123 verses with longer verses (mean 17 w/v); Q 26 has 227 verses with mean 6 w/v; Q 29 has 69 verses with mean 15 w/v. The density metric (per 1000 words) controls for length-confound.
- Q 15's "prophet-narrative" content is dominated by the Iblīs-rebellion-creation block (vv. 28-44, 119 words = 18% of surah) which does NOT name prophets explicitly; Q 11/26/29 have iterative-prophet-cycle structures with named prophets in each cycle. The empirical prediction is consistent with Q 15's distinct content register.
- The prophet-name list is not exhaustive (e.g., does not include allusions like *al-yaqīn al-rāsikh* or kunyas). We use a fixed standard list as pre-locked.

## 6. Rules-tuple

`(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Permutation null

Not applicable for a 4-surah-comparison-rank test. The test is direction-locked.

## 8. SHA256 lock

To be computed at write-time. Embedded in `scripts/Q015_F_all_tests.py`.
