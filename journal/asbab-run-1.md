# Asbāb al-Nuzūl — Run 1 Journal

**Agent:** asbab-nuzul-agent (Phase B hypothesis)
**Date:** 2026-04-12
**Status:** complete, exploratory (not pre-registered)
**Output:** `findings/phase-b-hypotheses/asbab-nuzul.md`

## What I did

1. **Grounded the genre.** Read al-Wāḥidī's *Asbāb Nuzūl al-Qurʾān* (d. 468 H) as the canonical reference; cross-referenced al-Suyūṭī's *Lubāb al-Nuqūl* and his *al-Itqān* chapter; noted the governing hermeneutic rule *"al-ʿibra bi-ʿumūm al-lafẓ lā bi-khuṣūṣ al-sabab"* (Ibn Taymiyya, Suyūṭī).
2. **Verified nine canonical asbāb directly against the Qurʾānic text** (`quran-text/quran-no-tashkeel.json`):
   - Badr (Q 3:123, 8:7-19, 8:41)
   - Uḥud (Q 3:152-168)
   - Ifk / slander of ʿĀʾisha (Q 24:11-20)
   - Ḥudaybiyya (Q 48:1-3, 48:18-28)
   - Banū al-Naḍīr (Q 59 throughout, unique phrase *li-awwali l-ḥashr* in 59:2)
   - Jewish disputes (Q 2:76-79, 5:41-44)
   - Blind-man rebuke (Q 80:1-16)
   - Zayd and Zaynab (Q 33:37)
   - Satanic Verses tradition (Q 22:52).
3. **Enumerated all explicit event-markers in the corpus** via string-matching nine canonical phrases (*ببدر*, *يوم الفرقان*, *يوم التقى الجمعان*, *يوم حنين*, *لأول الحشر*, *يوم الأحزاب*, *إذ يبايعونك*, *إذ يعدكم الله*, *جاءوا بالإفك*). Result: only 9 explicit hits total; every one is Medinan except the Mosaic-context *yawm al-aḥzāb* at Q 40:30 (which is not about Muḥammad's community).
4. **Computed ʾiḏ-particle density** (the standard narrative-past trigger used in almost every sabab-report): 0.0230/verse Meccan vs 0.0308/verse Medinan, ratio 1.34×. Surah 8 (al-Anfāl) tops the corpus at 0.133.
5. **Audited the *yasʾalūnaka / yastaftūnaka* formula** (the interrogative sabab-trigger): 15 total occurrences, 11 Medinan + 4 Meccan. Classified by topic: Medinan are *all* legal/Sharīʿa; Meccan are *all* metaphysical (Hour, Spirit, Dhū al-Qarnayn, mountains). A categorical topic-partition by period.
6. **Catalogued event-named surahs** (name = the event): al-Anfāl (8), al-Aḥzāb (33), al-Fatḥ (48), al-Ḥashr (59), al-Munāfiqūn (63), al-Taḥrīm (66) are all Medinan; only al-Fīl (105) is Meccan, and it names Muḥammad's birth-year, not a revelation-event.
7. **Verified convergence with project's existing findings:**
   - ʿAbasa 1-9 is a Bonferroni-surviving micro-ring (z = +6.09) per `findings/phase-c-structures/prophet-micro-rings.md`. This is the *same* 9-verse span as the classical blind-man (Ibn Umm Maktūm) sabab. The ring's pronoun-cycle-and-closure *is* the rebuke's dramatic content.
   - Surah 59's *khawātim* analysis (already in the project) is the theological coda to the Banū al-Naḍīr expulsion (verses 1-17).
   - Maryam's two Christological rhyme-breaks (Q 19:34-40, 88-93) per `journal/maryam-deep-run-1.md` are late Meccan, but deliver the theological content the Najrān delegation sabab (classically placed at Q 3:59-61) would later need. Offered as an exploratory re-reading, not a classical sabab-revision.
8. **Wrote the deliverable** with YAML frontmatter in the project's standard format.

## Surprises

- The *yasʾalūnaka* Meccan/Medinan topic partition is **exactly disjoint**: every Medinan occurrence is Sharīʿa, every Meccan occurrence is metaphysics. I expected partial overlap; I found none. This gives an empirically clean signature that a verse has a legal sabab.
- Only **one** contemporary person is named by first name in the Qurʾānic text: Zayd (33:37). Muḥammad (the Prophet) appears 4× as a proper noun; Abū Lahab appears once by *kunya* (111:1); ʿĪsā/Mūsā/etc. are all past prophets. Zayd's naming is genuinely unique. This changes the reading of 33:37: it is the sabab being written *into* the text, not recovered from outside.
- Named battles appear only *retrospectively*. Q 3:123 is Uḥud-era revelation looking back at Badr; Q 9:25 is late-Medinan looking back at Ḥunayn. The Qurʾān never names a battle *during* its occurrence — only once its theological meaning has been fixed.
- Al-Anfāl's *ʾiḏ*-density (0.133/verse) is **5.8× the Meccan baseline**. I did not expect the Badr surah to be this anomalous; it is a single surah doing sabab work for a whole class of events.

## Negative findings

- No evidence that Meccan asbāb density is elevated at all. The classical rule *al-ʿibra bi-ʿumūm al-lafẓ* is empirically supported by the text's own structure.
- The Maryam-as-Najrān hypothesis is weaker than I initially hoped. The Najrān delegation is classically placed in late Medina (9 AH) and Maryam is clearly Meccan. The connection is best phrased as "Maryam supplied theological resources later redeployed," not "Maryam was revealed in response to Najrān."
- The gharānīq / Satanic Verses dispute is genuinely unresolved classically; I report both positions (Ṭabarī/Wāḥidī accepting, Bayhaqī/Rāzī/Ibn Kathīr rejecting) without adjudicating.

## Method choices

- Used no-tashkeel text for string-matching (avoids diacritical variation in event-names).
- Counted *ʾiḏ* by word-initial and space-preceded match only (excludes *ʾiḏā*, which is a different particle with hypothetical/conditional force).
- Did not run a formal null model for sabab-attribution itself — there is no scholarly gold-standard set of "correctly attributed" asbāb against which to calibrate. The genre is irreducibly judgment-based.

## What I did NOT do

- Did not compute formal isnād-quality scores per sabab-report. This would require a separate hadīth-critical agent with access to Wāḥidī's full isnād data.
- Did not replicate Suyūṭī's full 570-report count for Wāḥidī. The cases covered (nine canonical) are the most-cited; the tail is less informative statistically.
- Did not test the Maryam-as-Najrān hypothesis against Reynolds (2018) or Sinai (2019) directly — flagged as a future Phase C agent task.

## One-line takeaway

The Qurʾān's own internal event-anchoring is sparse, Medinan, and categorical: *yasʾalūnaka* partitions Meccan-metaphysics from Medinan-law, and every explicit battle-name is Medinan; the classical *asbāb* genre is the literature that had to grow up to fill the deliberately-left gap.
