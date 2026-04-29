---
finding_id: Q009-F-04
prereg_date: 2026-04-28
prereg_type: classical-citation-density audit
status: PRE-REGISTERED
---

# Q009-F-04 — "Last-revealed verse" classical-citation density (pre-registration)

## 1. Background

Multiple competing classical claims exist for "the LAST verse revealed":
- (a) Q 9:128-129 ("لقد جاءكم رسول من أنفسكم...") — al-Suyūṭī *al-Itqān* nawʿ 8 citing Ubayy b. Kaʿb via al-Bukhārī.
- (b) Q 4:176 ("يستفتونك قل الله يفتيكم في الكلالة") — al-Bukhārī, al-Bayhaqī via al-Barāʾ b. ʿĀzib (al-Suyūṭī *Itqān* nawʿ 8).
- (c) Q 2:281 ("واتقوا يوما ترجعون فيه إلى الله") — Ibn ʿAbbās tradition (al-Suyūṭī *Itqān* nawʿ 8: "ākhar āyat nazalat āyat al-ribā").
- (d) Q 5:3 ("اليوم أكملت لكم دينكم") — minority position (Sufyān b. ʿUyayna and others).

al-Suyūṭī harmonizes these: each Companion reported what reached him. But which is the strongest tradition by **citation density** in the classical-tafsir corpus?

## 2. Hypothesis (DIRECTION-LOCKED)

**H1**: In the 7 OpenITI tafsirs (Ṭabarī, Qurṭubī, Rāzī, Ibn Kathīr, Suyūṭī *al-Durr al-manthūr*, Biqāʿī, Zamakhsharī), the joint citation count of "آخر ما نزل" (last revealed) co-occurring with **Q 9:128-129 markers** is greater than the joint count co-occurring with each of {Q 2:281, Q 4:176, Q 5:3} markers individually.

**Direction**: Q 9:128-129 > each rival. LOCKED.

## 3. Null hypothesis

**H0**: All four claims are cited at equal frequency within ±10% in the 7-tafsir corpus.

## 4. Method

For each surah-extract file:
- Search for "آخر ما نزل" (and orthographic variants), within 8-line context window.
- For each window, mark which surah marker (Q9:128, Q4:176/kalāla, Q2:281/ribā, Q5:3/al-yawm akmaltu) appears.
- Tally each (claim, source) pair.

Relevant patterns:
- Q9:128-129: "لقد جاءكم رسول", "آخر سورة", "براءة من آخر القرآن"
- Q4:176: "كلالة", "يستفتونك", "آخر آية"
- Q2:281: "آية الربا", "اتقوا يوما"
- Q5:3: "اليوم أكملت", "حجة الوداع"

## 5. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| Q9:128-129 cite-count > each rival | VINDICATED al-Suyūṭī harmonization with Q9:128 dominant |
| Q4:176 OR Q2:281 dominates | DIRECTIONAL VIOLATION — alternative is the dominant classical claim |
| All cited equally (within 10%) | NULL — al-Suyūṭī's harmonization stands |

## 6. Bonferroni: family k = 5; α_bon = 0.01.

## 7. Pre-commit locked.
