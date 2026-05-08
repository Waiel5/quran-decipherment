---
finding_id: Q004-F-05
title: Q 4:1 marriage-khutba liturgical-citation distinctness
status: PRE-REGISTERED
date: 2026-05-07
specialist: Q004-al-nisa-specialist
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q004-novel-tests-2026-05-07
alpha_bon: 0.01
direction: HIGHER (Q 4:1 hadith-citation density is in the top-5 corpus-wide for non-khawātim verses)
acceptance_window: top-5 of all non-khawātim verses by 9-book hadith citation count
---

# Q004-F-05 — Q 4:1 marriage-khutba liturgical citation: pre-registration

## Hypothesis

Q 4:1 (`yā ayyuhā al-nāsu ittaqū rabbakum alladhī khalaqakum min nafsin wāḥidatin`) is, per al-Tirmidhī (#1105), Abū Dāwūd (#2118), al-Nasāʾī (#1404), Ibn Mājah (#1892), and al-Bukhārī (citing Ibn Masʿūd's *khuṭbat al-ḥāja*), the verse classically recited at the opening of every Islamic marriage contract (the *khuṭbat al-ḥāja*). This is a unique liturgical position. Test: does Q 4:1 have a citation-density across the 9-book hadith corpus that places it in the top-5 of all corpus verses, EXCLUDING the khawātim verses (Q 1:1-7, Q 2:255, Q 2:284-286, Q 36:1-83, Q 67:1-30, Q 112:1-4, Q 113:1-5, Q 114:1-6) which are over-represented for fadāʾil reasons?

## Operationalisation

- Hadith corpus: `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` — 9 books (Bukhari, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī).
- For each book, search for the substring matching Q 4:1's distinctive phrase: `يا أيها الناس اتقوا ربكم الذي خلقكم من نفس واحدة`. Count occurrences; sum across 9 books.
- Comparator: also search for hadith-distinctive phrases of:
  - Q 1:1 (`الحمد لله رب العالمين`)
  - Q 2:255 (`الله لا إله إلا هو الحي القيوم`)
  - Q 2:284 (`لله ما في السماوات وما في الأرض`)
  - Q 36:1 (`يس`)
  - Q 112:1 (`قل هو الله أحد`)
  - Q 4:11 fragment (`يوصيكم الله في أولادكم`)
  - Q 4:43 fragment (`لا تقربوا الصلاة وأنتم سكارى`)
  - Q 4:148 fragment (`لا يحب الله الجهر بالسوء`)
  - Q 4:176 fragment (`يستفتونك قل الله يفتيكم في الكلالة`)
- Primary verdict: Q 4:1's hadith citation count rank within the {non-khawātim} subset (i.e., rank excluding Q 1, Q 2:255, Q 2:284-286, Q 36, Q 67, Q 112, Q 113, Q 114).

## Direction & alternative

- DIRECTION-LOCKED: HIGHER (Q 4:1 rank ≤ 5 in non-khawātim verses).
- Top-10 → DIRECTIONAL.
- > 10: NULL of classical claim.

## Null model

- The "rank" test is descriptive; for inferential significance, compare Q 4:1's count to the median citation-count of all corpus verses (those with ≥ 1 hadith citation), under the bootstrap-resample null (10000 resamples, seed = 20260507).

## Bonferroni

- Family: Q004-novel-tests-2026-05-07, k=5; α_bon = 0.01.

## Honest limits

- Substring search misses verses cited via abbreviation ("akhir al-Baqara"; "Sūrat al-Nisāʾ awwaluhā"). The actual classical citation-density may be higher than measured here.
- The 9-book hadith corpus from `ahmedbaset-json` is not officially canonical-numbered; ḥadīth-numbering correspondence to the printed *Ṣaḥīḥayn* requires cross-checking. This test reports SUBSTRING occurrences, not authenticated citation-count.
- The "khawātim" exclusion list is itself a judgment call. The pre-reg locks the list above; expanding it post-hoc is a violation.
