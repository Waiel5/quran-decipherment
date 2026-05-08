---
surah: 38
test_id: Q038-F-02
title: Prophet-cycle saturation — Q 38 prophet-name density per 100 words vs other prophet-cycle surahs
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 1
bonferroni_family: Q038-F-02-prophet-saturation
alpha_bon: 0.05
---

# Q038-F-02 — Pre-registration: prophet-cycle saturation index

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 38 has the **highest prophet-name density per 100 words** among the corpus. Classical claim: Q 38 names ≥7 prophets (Dāwūd, Sulaymān, Ayyūb, Ibrāhīm, Isḥāq, Yaʿqūb, Ismāʿīl, al-Yasaʿ, Dhū al-Kifl) within 88 verses. Density = (#tokens of named-prophet) / (#words) × 100.

**H0:** Q 38 ranks ≥ 5 in the corpus on prophet-name density per 100 words.

**Direction:** Q 38 should rank in the **top 3/114** on prophet-name density (LOCKED). Pre-committed comparison set: Q 7 (al-Aʿrāf), Q 11 (Hūd), Q 21 (al-Anbiyāʾ), Q 26 (al-Shuʿarāʾ), Q 37 (al-Ṣāffāt), Q 38 (Ṣād).

## 2. Operational definition

**Named-prophet token set** (no-tashkeel exact-match Arabic strings, Quranic-prophet canonical 25):
آدم, نوح, إدريس, هود, صالح, إبراهيم, لوط, إسماعيل, إسحاق, يعقوب, يوسف, شعيب, أيوب, ذا الكفل, موسى, هارون, داود, سليمان, إلياس, اليسع, يونس, زكريا, يحيى, عيسى, محمد.

(Plus inflected forms with prefixes/suffixes via word-boundary regex on no-tashkeel text: prefixes ل/و/ف/ب/ك, suffixes none, since these are proper nouns.)

**Per-surah metric**: `prophet_density_per_100w = #prophet_token_hits / #words × 100`.

## 3. Test statistic

- Primary: Q 38's rank on `prophet_density_per_100w` (1 = highest).
- Secondary: count of unique named-prophets per surah; Q 38 should be in top 3 on uniques.
- Tertiary: prophet-density × verse-count interaction (control for surah length).

## 4. Success / Failure

- **Strict success (CONFIRMED)**: Q 38 ranks 1, 2, or 3 / 114 on `prophet_density_per_100w`.
- **Directional**: Q 38 ranks in top 6/114.
- **NULL**: Q 38 ranks ≥ 25/114.
- **Pre-commit violation**: Q 38 below median (≥ rank 57) — would falsify the prophet-saturation hypothesis.

## 5. Honest limits known a priori

- "Named prophet" is a curator decision; some scholars include Luqmān (Q 31), Khiḍr (Q 18), Dhū al-Qarnayn (Q 18) — these are NOT in the test set (they are not univocally accepted as prophets in classical tradition).
- Inflectional variants like وداود vs داود are caught by word-boundary regex; this might over-count or under-count depending on the exact orthography in tashkeel-stripped form.
- Surahs that are mainly *about one* prophet (Q 12 Yūsuf, Q 71 Nūḥ) will have very high density of one name but low density of multiple-name. The test detects density, not breadth; secondary statistic measures uniques.
- Q 19 Maryam may rank above Q 38 because of repeated *Maryam, ʿĪsā, Yaḥyā, Ibrāhīm* attestations — pre-commit acknowledges this and locks Q 38 as expected to be top-3 (not necessarily top-1).

## 6. Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

To be computed at run-time. Embedded in `scripts/Q038_F_02_prophet_saturation.py`.
