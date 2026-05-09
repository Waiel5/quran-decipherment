---
surah: 22
surah_name_ar: الحج
surah_name_translit: al-Ḥajj
surah_name_english: "The Pilgrimage"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD-COMPLETE — full 8-file template; Q022-F-01 through Q022-F-08 SHA-locked seed=20260507/20260509; Wave-H sajda follow-up landed 2026-05-09.
---

# Q 22 al-Ḥajj — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 22 | canonical |
| Arabic name | الحج | canonical (named after the central ḥajj-legislation passage vv 25-37) |
| Transliteration | al-Ḥajj | canonical |
| English meaning | "The Pilgrimage" | canonical |
| Verse count | 78 | Hafs-Kufan; `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` |
| Position in mushaf | 22 | canonical |
| Type | Mixed Meccan-Medinan (al-Suyūṭī majority); the standard listing classifies it as **Medinan** (Tanzil + Nöldeke) with significant Meccan strata | classical-disputed |
| Position in revelation order | **103 of 114** (Tanzil Egyptian Standard); Nöldeke rank 107 (Medinan zone) | `/Users/grey/Downloads/quran/data/revelation-order.csv` |
| Word count (no-tashkeel) | **1,354** | computed from `quran-no-tashkeel.json` |
| Unique-word count | 697 | computed |
| Unique QAC roots | **328** | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Letter count (no-tashkeel, no spaces) | **5,389** | computed |
| Avg verse-length | 17.4 words / 69.1 letters | LONG-VERSE register (Medinan-typical) |
| Top final-letter | ر (rāʾ) | **32.5%** of 78 verses; mixed rhyme — see §8 |
| Rhyme entropy (Shannon, nats) | **1.821** | HIGH (z = +1.90 vs corpus) — one of the most rhyme-heterogeneous surahs in the corpus, consistent with thematic-block-driven rhyme-shifts |
| Opening | يا أيها الناس اتقوا ربكم — *yā ayyuhā al-nāsu ttaqū rabbakum* — "O mankind, fear your Lord" | **universal *yā-ayyuhā-al-nās* vocative**; only 4 surahs open this way (Q 4, **Q 22**, Q 31 §16-end, Q 49 partial) |
| Closing | وجاهدوا في الله حق جهاده… ونعم النصير | *jihād-fī-llāh* + *huwa al-mawlā* closing exhortation |

## 2. Classical name and naming convention

The surah is named **al-Ḥajj** after the central ḥajj-legislation block at vv 25-37, anchored by the imperative *wa-adhdhin fī al-nāsi bi-l-ḥajj* — "And proclaim the pilgrimage to mankind" (v 27).

The surah's name is **not** taken from its opening (universal vocative *yā ayyuhā al-nāsu*) but from its thematic-legislative core. This is the canonical "central-theme naming" pattern shared with Q 2 al-Baqara (named after the cow narrative at vv 67-73, not from the *alif-lām-mīm* + *dhālika l-kitāb* opening) and Q 5 al-Māʾida (named after the table-of-Christ pericope vv 112-115 deep within the surah).

The name al-Ḥajj uniquely identifies Q 22 as **the only surah in the corpus whose name and major theme is the pilgrimage-rite** (al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 14 on the *asbāb al-tasmiyya*). For the empirical density-test of this naming-as-density claim, see [`06-novel-findings.md`](06-novel-findings.md) Q022-F-04 and [`01-empirical-profile.md`](01-empirical-profile.md) §11 — Q 22 is rank 2 of 114 (after the 10-word Q 108 al-Kawthar singleton) on pilgrimage-vocabulary-per-100-words.

## 3. Chronology — the classical Meccan/Medinan dispute

Q 22 is the **single most-disputed surah on the Meccan/Medinan question** in the classical tradition.

| Position | Source | Argument |
|:--|:--|:--|
| **Medinan** (majority) | al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1; Tanzil Egyptian Standard; Nöldeke rank 107 | The ḥajj-legislation block (vv 25-37) presupposes Medinan-state ritual administration; the jihād-permission at vv 39-41 is THE FIRST EVER war-permission verse (per al-Wāqidī, Ibn Isḥāq, al-Ṭabarī Tārīkh I.1356) and is Medinan-Hijra-context; vv 19-24 reference the Badr disputants. |
| **Meccan** | al-Zamakhsharī, *al-Kashshāf* on Q 22 (intro); al-Bayḍāwī | The opening cosmic-eschatological block (vv 1-18) carries Meccan eschatological signatures; the universal *yā ayyuhā al-nāsu* vocative is overwhelmingly Meccan. |
| **Mixed/hybrid** | al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān* intro to Q 22; al-Wāḥidī *Asbāb al-nuzūl*; Ibn ʿAṭiyya *al-Muḥarrar al-wajīz* | Specific verses identified as Meccan (1-18 most), Medinan (25-30, 39-41), with intermediate strata. This is **the standard scholarly synthesis**. |

The empirical bimodality test ([`06-novel-findings.md`](06-novel-findings.md) Q022-F-02) under a 5-feature Meccan-Medinan axis returned NULL: under this feature operationalization, the within-Q22 verse-score distribution is unimodal (dip p > 0.05 by 10,000-perm bootstrap), suggesting either (a) the Meccan-Medinan strata are NOT separable on simple-feature axes within Q 22, or (b) the strata are fully integrated rhetorically. See `06-novel-findings.md` for full discussion.

## 4. ⭐ Unique structural property — the CORPUS-SINGLETON DOUBLE-SAJDA surah

**Q 22 is the only surah in the Quran with TWO sajda-verses**, at 22:18 and 22:77. Verified by direct count of the ۩ glyph (U+06E9) across all 6,236 verses (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`): **15 sajda-markers total across 14 surahs**; only Q 22 carries 2. Full enumeration:

| Sajda position | Surah:Verse | Surah-chronology (Nöldeke) | Sajda-type |
|:--|:--|:--|:--|
| 1 | Q 7:206 | Late Meccan | Cosmic + boast-rejection |
| 2 | Q 13:15 | Late Meccan/Medinan | Cosmic roll-call |
| 3 | Q 16:50 | Late Meccan | Cosmic-creatures |
| 4 | Q 17:109 | Late Meccan | Tear-prostration |
| 5 | Q 19:58 | Middle Meccan | Prophets-prostrating |
| 6 | **Q 22:18** | **Mixed-Medinan** | **Cosmic roll-call (sun, moon, stars, mountains, trees, animals, men)** |
| 7 | **Q 22:77** | **Mixed-Medinan** | **Imperative-prostration (*irkaʿū wa-sjudū wa-ʿbudū rabbakum*)** |
| 8 | Q 25:60 | Middle Meccan | al-Raḥmān-recognition |
| 9 | Q 27:26 | Middle Meccan | al-ʿarsh-witness |
| 10 | Q 32:15 | Middle Meccan | Believers-prostrating |
| 11 | Q 38:24 | Middle Meccan | David-prostrating |
| 12 | Q 41:38 | Late Meccan | Sun-and-moon-bow |
| 13 | Q 53:62 | Early Meccan | Final-verse-imperative |
| 14 | Q 84:21 | Early Meccan | Resist-prostration |
| 15 | Q 96:19 | Early Meccan | Approach-and-prostrate |

(Total: 14 surahs, 15 verses. Q 22 carries 2; all others carry 1. See [`06-novel-findings.md`](06-novel-findings.md) Q022-F-06 for the deterministic verification.)

Classical attestations of the double-sajda:
- **Abū Dāwūd, *Sunan* #1402** (ʿAmr b. al-ʿĀṣ): the Prophet taught him 15 sajdas in the Qurʾān including TWO in Surah al-Ḥajj. (Verified on disk at `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/abudawud.json` id 1402.)
- **al-Tirmidhī, *Sunan* #578** (ʿUqba b. ʿĀmir): "I said: 'O Messenger of Allāh, has Sūrat al-Ḥajj been esteemed by two prostrations?' He said: 'Yes; and whoever does not prostrate for them should not recite them.'" Tirmidhī's grading: *isnāduhu laysa bi-dhāka l-qawī* — "the chain is not particularly strong." (Verified on disk at `.../tirmidhi.json` id 578.)
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 30** (on sujūd al-tilāwa): catalogues the 14-surah Sunnī list with the Q 22:77 dispute.

Mālikī jurisprudence dissents: Mālik b. Anas (via al-Mudawwana) and his school recognize only one sajda in Q 22 (some attribute 22:18, others 22:77). Imāmī (Shīʿī) law recognizes only 4 wājib sajdas {Q 32, 41, 53, 96}; Q 22's sajdas are mustaḥabb. The PRINTED Mashriqi-Hafs-Kufan mushaf carries BOTH ۩ markers — making Q 22 the corpus-singleton under the canonical rules-tuple.

## 5. ⭐ Unique structural property — the FIRST QURANIC PERMISSION FOR WAR

**Q 22:39 is the corpus's first explicit permission for the believers to fight.**

> *udhina lilladhīna yuqātalūna bi-annahum ẓulimū, wa-inna Allāha ʿalā naṣrihim laqadīrun*
> "Permission has been given to those who are being fought (against) because they have been wronged — and indeed Allāh is competent to give them victory."

Classical occasion-of-revelation (al-Wāḥidī, *Asbāb al-nuzūl* on Q 22:39; al-Ṭabarī, *Tārīkh al-rusul wa-l-mulūk* I.1356; Ibn Isḥāq via Ibn Hishām, *Sīra* II.40): revealed shortly after the Hijra when the early Muslim community was attacked by Quraysh raiders en route to Medina. The verse opens the Quranic legislative trajectory that later includes Q 2:190-194 (defensive-fighting framework), Q 9 al-Tawba (later jihād-progression), and the prohibition-on-aggression clauses.

al-Suyūṭī (*al-Itqān*, nawʿ 11 on al-nāsikh wa-l-mansūkh): notes that Q 22:39-41 is the *fātiḥat al-qitāl* — "the opening of fighting-discourse" — in the Quranic revelation-chronology.

## 6. ⭐ Unique structural property — the JIHĀD CLOSING IMPERATIVE

Q 22:78 *wa-jāhidū fī Allāhi ḥaqqa jihādihi* — "Strive in the way of God a true striving" — is one of the corpus's strongest jihād-imperatives, paired with the universal vocative opener at v 1. The surah brackets itself with a **dual-universal address** (open: *yā ayyuhā al-nāsu*; close: *wa-jāhidū fī Allāhi*) sandwiching the eschatology + ḥajj + jihād + monotheism quadruple-block.

## 7. Length classification

78 verses, 1,354 words, average 17.4 words/verse — **LONG-VERSE** register. Position s=22 in mushaf places Q 22 within the second of the project's three architectural zones (s=1-50 long-verse zone). Q 22 is at the boundary between the *al-sabʿ al-ṭiwāl* extended cluster (Q 1-9 + Q 10-12 yūnus-yūsuf annex) and the al-mufaṣṣal-precursor middle-mushaf group (Q 21-29). Q 22 belongs to the **mid-mushaf long-verse register** (Q 16-29 stratum).

## 8. Rhyme structure

Final-letter distribution across 78 verses (no-tashkeel):

| Letter | Count | Fraction |
|:--|:-:|:-:|
| ر (rāʾ) | 25 | 32.5% (top) |
| ـن /ون (nūn/wāw-nūn) | rough endings | ~30% (mixed *qadīr*, *naṣīr*, *baṣīr*, *khabīr*, *ʿalīm*) |
| ي/ـيد | 13 | ~16.7% |
| Others (د, ل, م) | balance | ~20% |

**Rhyme entropy: 1.821 nats** — among the **HIGHEST** in the corpus (z = +1.90 vs corpus mean). Compare:
- Q 91 al-Shams = 0.000 (perfect monorhyme)
- Q 53 al-Najm = 0.568 (near-monorhyme on *-ā*)
- Q 2 al-Baqara ≈ 1.40-1.55
- **Q 22 = 1.821** (high heterogeneity)
- Theoretical max for 78 verses ≈ ln(78) ≈ 4.36

This high rhyme-entropy is consistent with Q 22's block-structured thematic shifts: each block (cosmic-1-18, disputants-19-24, ḥajj-25-37, jihād-39-41, monotheism-42-72, sajda-77, jihād-78) carries its own preferred *fāṣila* register. Classical *balāgha* would identify this as *sajʿ mutawāzin* (parallel-but-not-identical rhyme) interspersed with *sajʿ muṭarraf* (varying-length but uniform-rhyme) — al-Khaṭīb al-Tibrīzī's classification (*al-Wāfī*, ch. on sajʿ).

## 9. Empirical architectural profile

See [`01-empirical-profile.md`](01-empirical-profile.md). Headline:

- **UAS rank**: **17 / 114** — moderate-high (top quintile but not top-10).
- **iʿjāz sig_A**: 1.267 (rank 25/114) — moderately high.
- **iʿjāz sig_B**: 1.230 (rank 20/114) — moderately high.
- **Outlier-strength** (X=22 in window {Q 19…25}): Δpp = +5.16 (WEAK_OUTLIER), p_greater_W = 0.283.
- **Mean FR-content distance to other 113 surahs**: 0.988 (slightly above corpus mean 0.924) — Q 22 leans CONTENT-DISTANT, consistent with H-NEW-126 TRUE-ISOLATE membership.
- **Local cohesion** (within-surah): 1.024 (z = −0.67) — slightly less cohesive within-surah than average, consistent with hybrid Meccan-Medinan stratification.
- **Q 21→Q 22 adjacency cost** (TSP-residual): delta = +0.178 (fraction_residual 0.0214) — moderate-cheap transition. The Anbiyāʾ → al-Ḥajj seam is in the cheaper half of canonical adjacencies.
- **Q 22→Q 23 adjacency cost**: delta = +0.260 (fraction_residual 0.0313) — moderate transition. al-Ḥajj → al-Muʾminūn is in the upper-mid expensive range.

## 10. Quick content structure

| Block | vv | Topic |
|:--|:-:|:--|
| 1 | 1-18 | **Cosmic-eschatology**: zalzala-al-sāʿa opener (v 1), dispute-without-knowledge (v 3), debate-cycle of disbelief vs. believer-judgment, closes with the cosmic-roll-call sajda (v 18) |
| 2 | 19-24 | **The two disputants**: Badr-anchored two-parties polemic; fire-of-hell vs garden-rewards |
| 3 | 25-37 | **ḥajj-legislation core**: muqaddasa-Bayt-anchor, ḥajj-proclamation imperative (v 27), shaʿāʾir-Allāh ritual-mantle, hadya-and-budn sacrifice, ṭawāf-and-iʿtikāf, ḥajj-monotheism summary |
| 4 | 38-41 | **First-permission-of-war**: v 39 *udhina lilladhīna*, the corpus-opening jihād-permission verse |
| 5 | 42-72 | **Prophetic-cycle + arguments-from-creation + idol-refutation**: Nūḥ, ʿĀd, Thamūd, prophets-rejected motif (vv 42-46), tawḥīd cluster, fly-creation parable (vv 73-74), all-religions-aspire-to-the-House motif |
| 6 | 73-76 | **Cosmic-witness closing**: kun-fa-yakūn ontology, *Allāhu yaṣṭafī* election-of-prophets |
| 7 | 77-78 | **Imperative-closing**: SECOND sajda at v 77 (*irkaʿū wa-sjudū wa-ʿbudū*), then v 78 *jāhidū fī Allāhi ḥaqqa jihādihi*, *huwa al-mawlā wa-niʿma al-naṣīr* |

Full verse-by-verse analysis: see [`02-content-analysis.md`](02-content-analysis.md).

## 11. Classical commentary lineage

Major classical tafsir on Q 22 (full survey: [`03-tafsir-survey.md`](03-tafsir-survey.md)):

- **al-Ṭabarī** (*Jāmiʿ al-bayān*, vol. 18 of Šākir-Šākir ed.): aggregator treatment; full mawqūf catalog of Meccan/Medinan dispute; Q 22:39 *asbāb* dossier; cosmic-roll-call exegesis of 22:18.
- **al-Zamakhsharī** (*al-Kashshāf*, vol. 4 on Q 22): Muʿtazilite-balāgha treatment; reads Q 22 as predominantly Meccan with Medinan additions; rich literary analysis of the *yā ayyuhā al-nāsu* vocative.
- **al-Rāzī** (*Mafātīḥ al-ghayb*, vol. 23): exhaustive *naẓm* treatment; specifically engages the double-sajda question (*kayfa* and *limādhā*); 4 wajh on the cosmic-roll-call of 22:18.
- **al-Qurṭubī** (*al-Jāmiʿ li-aḥkām al-Qurʾān*, vol. 12): legal-emphasis treatment; full four-madhhab dossier on the obligatoriness of both 22:18 and 22:77 sajdas; ḥajj-legislation chapter.
- **Ibn Kathīr** (*Tafsīr al-Qurʾān al-ʿaẓīm*, vol. 5 of Dār Ṭayba ed.): hadith-anchored treatment; preserves the Tirmidhī #578 + Abu Dawud #1402 narrations on the double-sajda; treats Q 22:39 as the *fātiḥat al-qitāl*.
- **al-Biqāʿī** (*Naẓm al-Durar* on Q 22): *munāsaba* treatment; reads Q 21 → Q 22 → Q 23 as a tight rhetorical triad — Anbiyāʾ (the prophet-cycle catalog) → Ḥajj (the ritual-and-jihād synthesis) → Muʾminūn (the believers' character-portrait), all three sharing the cosmic-resurrection eschatological frame.
- **al-Suyūṭī** (*al-Durr al-manthūr* on Q 22; *al-Itqān* nawʿ 1, nawʿ 11, nawʿ 30): aggregate-tradition treatment; catalogues Meccan/Medinan dispute, the *asbāb* for the first-permission verse, the double-sajda jurisprudential debate.

## 12. Empirical findings (this specialist)

Five pre-registered tests (Q022-F-01 through Q022-F-05) ran 2026-05-07 SHA-locked seed=20260507; three follow-up pre-registered tests (Q022-F-06, F-07, F-08) ran 2026-05-09 SHA-locked seed=20260509 in the Wave-H session. Full details in [`06-novel-findings.md`](06-novel-findings.md). Headline:

| Test | Headline | Verdict |
|:--|:--|:--|
| Q022-F-01 | Q 22:18 cosmic-roll-call sajda cluster with Q 13:15 + Q 16:49 | **VINDICATED** (all 3 cells; perm p=0.012) |
| Q022-F-02 | Q 22 verse-level Meccan-Medinan bimodality on 5-feature axis | **NULL** (dip + Silverman both fail) |
| Q022-F-03 | Q 22 true-isolate persistence across 8 alternative similarity metrics | **NULL** (1 of 8 metrics — FR-roots — places Q22 in top-quartile; H-NEW-126 isolate-status is METRIC-SPECIFIC) |
| Q022-F-04 | Q 22 pilgrimage-vocabulary rate per 100 words > Q 2 and Q 5 | **VINDICATED** (Q22 rank 2/114; Q22 0.31× > Q2 0.23× > Q5 0.14×) |
| Q022-F-05 | Q 21-22-23 true-isolate triplet FR-cohesion | **DEFAULT_VINDICATED** (rank 74/112 triplets, upper-mid — confirms isolate-without-mutual-cohesion) |
| **Q022-F-06** | **Q 22 corpus-singleton on double-sajda (≥2 sajda markers)** | **VINDICATED** (1 of 114 surahs; verses 18, 77) |
| **Q022-F-07** | **Q 22 in UPPER HALF of 14-surah sajda set by FR-distance** | **VINDICATED** (rank 8/14; less-cohesive half) |
| **Q022-F-08** | **Q 22 sajda verses 18 & 77 at major within-surah block-boundaries (top-30%)** | **DIRECTIONAL_SPLIT** (v77 PASS, v18 FAIL — the imperative-sajda is structural, the cosmic-roll-call sajda is mid-block) |

## 13. Cross-references to project findings

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 22 FR matrix row; nearest neighbors Q 16, Q 31, Q 45.
- [[h-new-126-isolate-core|H-NEW-126]] — Q 22 is a CERTIFIED TRUE-ISOLATE; member of {Q 16, 21, 22, 23, 25} immune-to-all-20-cluster-systems core.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 22 weak outlier in window {Q 19…25}, X=22 row.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 22 high rhyme-entropy 1.821 (z = +1.90).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 21→Q 22 cost 0.178 (cheap), Q 22→Q 23 cost 0.260 (moderate-expensive).
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 22 sig_A 1.267 (rank 25); sig_B 1.230 (rank 20).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 22 UAS rank 17/114.
- [[h-new-1330-sajda-surahs-cluster|H-NEW-1330]] — CONFIRMED-NULL: 14 sajda-surahs do NOT form FR-cohesive cluster (perm p=0.571, length-matched p=0.110, PC=0.00020). **Q 22 contributes TWO data points to the 15 sajda-verse population that drove this NULL.** Q022-F-07 confirms Q 22 itself is in the LESS-cohesive half of the cluster (rank 8/14).
- [[h-new-1331-sajda-muqattaat-overrepresentation|H-NEW-1331]] — PASS-DIRECTED: 14 sajda-surahs are 1.97× over-represented for muqaṭṭāʿat-opening (7/14). **Q 22 is in the 7 NON-muqaṭṭāʿat sajda subset** (no opening letter cluster); Q 22's opening is the universal-vocative *yā ayyuhā al-nāsu*, identified at H-NEW-1331 as one of three "alternative-structurally-marked openers" of non-muqaṭṭāʿat sajda surahs (the others: Q 17 subḥāna alladhī asrā; Q 96 iqraʾ).
- [[cross-finding-013-mushaf-as-topological-ring|cross-finding-013]] — Q 22 lies between two universal hinges; the Q 21→Q 22 seam is cheap (Anbiyāʾ-Ḥajj rhetorical continuity) and Q 22→Q 23 seam is mid-expensive (Ḥajj-Muʾminūn thematic shift to character-portrait).
- [[cross-finding-025-multi-axis-architecture|cross-finding-025]] — Q 22's two sajdas provide a TEST CASE for the marker-thickness rule: even a 2-out-of-78-verse sajda density (2.6%) is below the 10% threshold that begets FR-cohesion. Q022-F-07 (Q22 less-cohesive half) directly supports cross-finding-025's marker-thickness threshold.

Full cross-reference matrix: see [`07-cross-references.md`](07-cross-references.md).

## 14. Headline summary

Q 22 al-Ḥajj is **the corpus-singleton on double-sajda**, the **only surah whose name and central theme is the pilgrimage-rite**, the carrier of the Quran's **first explicit permission for fighting** (v 39), and the **single most-disputed Meccan/Medinan surah** in the classical tradition. Two of its 78 verses (vv 18 and 77) carry sajda-markers — verified by direct ۩-glyph enumeration across the canonical Hafs-Kufan Mashriqi mushaf (Q022-F-06 VINDICATED). The double-sajda is attested by Abū Dāwūd *Sunan* #1402 (ʿAmr b. al-ʿĀṣ) and al-Tirmidhī *Sunan* #578 (ʿUqba b. ʿĀmir, isnād noted weak), with Mālikī jurisprudence dissenting. Q 22's content-fingerprint places it in the H-NEW-126 TRUE-ISOLATE core {Q 16, 21, 22, 23, 25} — immune to all 20 cluster-membership systems tested — but Q022-F-03's 8-metric persistence test returns NULL: the isolate-status is METRIC-SPECIFIC to Fisher-Rao on QAC roots. Q 22's pilgrimage-vocabulary density (Q022-F-04 VINDICATED) is rank 2/114, second only to the 10-word Q 108 al-Kawthar; Q 22's rate (0.31× per-100-words) exceeds both Q 2 (0.23×) and Q 5 (0.14×). On the corpus-wide H-NEW-1330 sajda-cluster NULL (CONFIRMED-NULL by independent replication 2026-05-09), Q 22 contributes both data points to the 15-verse sajda population AND itself sits in the less-cohesive half (Q022-F-07 rank 8/14, VINDICATED). Q 22 sits at the structural cross-roads of the Quran: long-verse Medinan legislation embedded within mid-mushaf Meccan-style cosmic eschatology; ḥajj-ritual law set inside a jihād-permission frame; the universal vocative open and the *jihād-fī-llāh* close — bracketing a surah whose thematic heterogeneity is what makes it both a TRUE-ISOLATE and a corpus-bridge.
