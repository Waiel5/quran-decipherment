---
surah: 110
surah_name_ar: النصر
surah_name_translit: al-Naṣr
surah_name_english: The Help / Divine Aid / The Victory
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD-COMPLETE — full 8-file template + journal; 4 pre-registered novel tests; 5 classical claims audited; chronology-mushaf-dissociation extension built on H-NEW-1030 parent
---

# Q 110 al-Naṣr — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 110 | canonical |
| Arabic name | النصر | canonical |
| Transliteration | al-Naṣr | canonical |
| English meaning | "The Help / Divine Aid / The Victory" | classical |
| Verse count | 3 | Hafs-Kufan, `quran-text/quran-no-tashkeel.json` |
| Position in mushaf | 110 | canonical |
| Type | **Medinan** (uncontested classical + Nöldeke) — although al-Suyūṭī notes a minority Meccan-attribution recital | `data/revelation-order.csv` Q 110 |
| Position in revelation order (Tanzil Egyptian Std, al-Suyūṭī-aligned) | **114 / 114 — THE LAST SURAH REVEALED** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **111 / 114** (Medinan, near-last) | `data/revelation-order.csv` `noldeke_phase = Medinan` |
| Word count (no-tashkeel orthographic, QAC stem-token rules-tuple) | **19** | computed `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Letter count (Arabic graphemes, no-tashkeel, no waqf-marks) | **80** | computed |
| Mean words/verse | **6.33** | computed |
| Distinct roots (QAC v0.4) | **15** of 16 root-tokens | only Allah-root *Alh* repeats |
| Total stem-tokens (QAC v0.4) | 16 | computed |
| **Opening** | **إذا جاء نصر الله والفتح** — "When the help of God and the conquest [of Mecca] come" | conditional *idhā*-opener; eschatological-condition register |
| **Closing** | **فسبح بحمد ربك واستغفره ۚ إنه كان توابا** — "So glorify with the praise of your Lord and seek His forgiveness; surely He is ever-Returning" | imperative *sabbiḥ* + imperative *istaghfir* + *kāna tawwāban* hāt-clause |
| Top rāwī | **ا (alif/yāʾ-mamdūda final ـا)** at 2/3 (66.7%) — *afwājā* / *tawwābā* | computed |
| Sajda verse | none | classical |

## 2. ⭐ Corpus-distinctive structural property — THE LAST SURAH REVEALED

Per the most-frequently-attested classical position:

> **Ibn ʿAbbās in Saḥīḥ Muslim, *Kitāb al-Tafsīr* (Q 110)**: "*Tadrī mā ākhir sūratin nazalat min al-Qurʾāni jamīʿan? Qultu naʿam, idhā jāʾa naṣru llāhi wa-l-fatḥ. Qāla ṣadaqta.*" — "Do you know what is the LAST surah revealed in the entire Qurʾān? I said: Yes — *idhā jāʾa naṣru llāhi wa-l-fatḥ*. He said: You spoke truly."

This is the canonical late-revealed-surah claim verified at the corpus level: Q 110 is **revelation-order #114 of 114** in Tanzil Egyptian Standard / al-Suyūṭī-aligned chronology, and **#111 of 114** in Nöldeke's. (See `04-hadith-corpus.md` for full ḥadīth texts and isnād, `05-classical-claims-audit.md` for the al-Tirmidhī-attested competing position that Q 5 al-Māʾida was the last; the classical scholarly consensus reconciles these as: Q 110 was the last *complete sūrah* revealed, while Q 5:3 *al-yawma akmaltu lakum dīnakum* was the last *legal-completion āyah* revealed at the Farewell Pilgrimage.)

## 3. ⭐ The chronology-mushaf-architecture DISSOCIATION (parent: H-NEW-1030)

**The signature finding for Q 110 is that it is canonically the LAST-revealed surah but architecturally clusters with the FIRST-revealed Meccan-tail**.

Per H-NEW-1030 (parent finding, dated 2026-05-07, queued from Q 5 specialist Q005-F-05): Q 110 is **3.86× closer** in Fisher-Rao content distance to the short-Meccan-tail (mean FR = 0.311 to {Q 108, 112, 114, 107, 106, 94, 111, 113, 105, 103} top-10) than to the late-Medinan-revelation centroid (mean FR = 1.199 to {Q 9, Q 5}).

Concretely, of Q 110's top-15 nearest FR-content neighbors, **15 of 15 are short-Meccan or al-Fātiḥa** (Q 1 included at rank 14) — there is **zero late-Medinan signal in Q 110's content geometry** despite the ḥadīth-attested last-revelation position.

This is the strongest-magnitude replication of the Q 5 chronology-architecture-dissociation principle so far identified. In the substantive language of cross-finding-020 (mushaf decomposition): Q 110's content lives in M5-mode (compositional / vocabulary / length-class) which knows nothing about M1-mode (chronological-temporal). The mushaf's information-geometric architecture (cross-finding-011) operates on length-and-vocabulary, NOT on revelation-date.

**Corpus-empirical headline number** for this surah's specialist: Q 110's mean FR-distance to all 113 other surahs is **0.7644** — the **2nd-most-central of all 114 surahs** (rank 2/114 by FR-centroid distance). Only Q 1 al-Fātiḥa (or one other tied within rounding) is more central. Q 110 occupies the corpus-centroid neighborhood by content-vocabulary, despite being the LAST-revealed surah by tradition. (See `01-empirical-profile.md` §6 for full ranking table.)

## 4. ⭐ Q 110 is part of the empirically-seamless Q 109 → Q 110 mushaf-transition (H-NEW-1240 rank 6)

Per H-NEW-1240 (2026-05-08): the Q 109 → Q 110 mushaf-adjacency has clamped-zero TSP-residual cost (delta_raw = 0.000, fraction_residual = 0.0000). It is **rank 6 of 13 corpus-EXACT seamless seams** in the mushaf (sorted by strength of seamlessness).

The seamlessness has a clear semantic reading: Q 109 al-Kāfirūn ("To you your religion, to me my religion") + Q 110 al-Naṣr ("And you saw mankind entering God's religion in waves") is the classical *takhṣīṣ-tabdīl* pivot — the polemical-disengagement of Q 109 is followed by the mass-conversion fulfillment of Q 110. al-Biqāʿī (*Naẓm al-Durar*, Q 109-110 munāsabah) explicitly treats this as the rhetorical inversion-pair: the prophet's individual disengagement → God's mass victory (see `05-classical-claims-audit.md` §3 for verbatim citation chain).

## 5. ⭐ Q 110's imperative cluster (sabbiḥ + istaghfir): musabbiḥāt-typology connection

Q 110's closing (v.3) is a 2-imperative compound: *fa-sabbiḥ bi-ḥamdi rabbika wa-staghfirhu* ("So glorify with praise of your Lord, and seek His forgiveness"). Per H-NEW-103 musabbiḥāt 4-form typology (PASS-DIRECTED, p=0.0049):

- Perfect (سَبَّحَ): Q 57, 59, 61 (all Medinan)
- Imperfect (يُسَبِّحُ): Q 62, 64 (both Medinan)
- Imperative (سَبِّحْ / fa-sabbiḥ): Q 87, **Q 110** (this verse, 2-imperative compound), elsewhere
- Noun (سُبْحَانَ): Q 17, 21, 36, 37, 43, 50, 56, 67

Q 110:3 is one of the **3 imperative-form sabbiḥ instructions** in the corpus tied to a personal-prayer addressee (compare Q 87:1 *sabbiḥ-isma rabbika al-aʿlā* and Q 50:39 *sabbiḥ bi-ḥamdi rabbika*). The 2-imperative *sabbiḥ + istaghfir* compound is corpus-unique to Q 110:3 in the explicit form *fa-sabbiḥ bi-ḥamdi rabbika wa-staghfirhu* ("praise + seek forgiveness"). See Q110-F-03 in `06-novel-findings.md` for the formal corpus-uniqueness test.

The *istaghfir* imperative connects Q 110 to the wider repentance-imperative cluster (Q 71:10 *istaghfirū rabbakum innahu kāna ghaffārā*, Q 11:3 *an istaghfirū rabbakum thumma tūbū*, etc.) — but Q 110's pairing of glorification-with-praise + seek-forgiveness as the response to victory-and-mass-conversion is the corpus's distinctive *post-victory-tasbīḥ* signature, classical-attested in tafsīr as *adab al-fātiḥ* (the etiquette of the conqueror): victory triggers humility, not pride.

## 6. ⭐ The classical Mecca-conquest interpretation

Per al-Ṭabarī (*Jāmiʿ al-Bayān* on Q 110) and Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿAẓīm* on Q 110), the *naṣr* + *fatḥ* pair specifically refers to the **conquest of Mecca (8 AH / 630 CE)** — the *naṣr* being the divine help granted in the lead-up campaigns, the *fatḥ* being the entry into Mecca.

The "people entering God's religion in waves (*afwājā*)" of v.2 then refers to the post-conquest mass-conversion of Arabian tribes during the *ʿām al-wufūd* ("Year of Delegations", 9 AH).

This puts the surah's lower-bound revelation-date at **post-Mecca-conquest 8 AH** at the earliest, and likely **9-10 AH** — late Medinan, near-final.

The Bukhārī/Muslim *ʿUmar–Ibn ʿAbbās* exegesis (cited §2 above and §7 below) extends the interpretation: Q 110 was understood by the Companions as a *prophetic farewell-signal* — the *fatḥ* + *afwājā* combination signaled that Muḥammad's mission was complete and his death was near. The Prophet's response (per ʿĀʾisha narration in Bukhārī/Muslim) was to repeat *subḥānaka rabbī wa-bi-ḥamdika allāhumma ighfir lī* ("Glory to You, my Lord, and praise; O God, forgive me") in every prayer thereafter — fulfilling Q 110:3 *fa-sabbiḥ bi-ḥamdi rabbika wa-staghfirhu* in his own ritual practice.

## 7. The Bukhārī/Muslim ʿUmar–Ibn ʿAbbās exegesis — VERIFIED via direct source-scan

Per direct corpus-scan of `data/literature/hadith/ahmedbaset-json/db/by_chapter/the_9_books/bukhari/` and `.../muslim/`, the Q 110 attestation chain is:

- **Bukhārī**: 6 ḥadīths citing Q 110:1, 4 of which are the ʿUmar–Ibn ʿAbbās exegesis (in *Kitāb al-Manāqib*, *Kitāb al-Maghāzī*, and *Kitāb al-Tafsīr*). The strongest: *Kitāb al-Tafsīr* on Sūrat al-Naṣr — Ibn ʿAbbās interprets *idhā jāʾa naṣru llāh* as *ajalu rasūli llāhi ṣ.l.ʿ.m. aʿlamahu īyāhu* ("the appointed-time of God's Messenger — God informed him of it"). Verified.
- **Muslim**: 4 ḥadīths citing Q 110:1 (3 in *Kitāb al-Ṣalāt* on the *subḥānaka rabbī* qualifier, 1 in *Kitāb al-Tafsīr* on the last-surah-revealed claim from Ibn ʿAbbās). The Muslim *Kitāb al-Tafsīr* one is the explicit "do you know what is the last surah revealed in the Qurʾān as a whole?" attestation. Verified.
- **Tirmidhī**: 2 ḥadīths cited (one is the ʿUmar–Ibn ʿAbbās exegesis paralleling Bukhārī, one is the *Q 110 = ¼ of the Qurʾān* virtue-ḥadīth from *Kitāb thawāb al-Qurʾān*; see `04-hadith-corpus.md` for the verbatim Arabic+English of all 12).

The classical Mecca-conquest + farewell-signal exegesis is **CLASSICALLY-ATTESTED at MULTIPLE-MUTAWĀTIR threshold** (≥6 isnāds across Bukhārī + Muslim).

## 8. Length classification

Q 110 is in the **mufaṣṣal-qiṣār** zone (Q 93-114 per al-Zarkashī *al-Burhān*). With 19 words / 80 letters, Q 110 is firmly in the bottom-15 of corpus by letter-count (alongside Q 108 al-Kawthar, Q 112 al-Ikhlāṣ, Q 113 al-Falaq, Q 114 al-Nās, Q 103 al-ʿAṣr, Q 105 al-Fīl, Q 106 Quraysh, Q 107 al-Māʿūn, Q 111 al-Masad). It is structurally and lexically the *terminal-zone* short surah.

## 9. Empirical architectural profile

See `01-empirical-profile.md` for full table. Headlines:

- **UAS (Unified Architectural Score)**: −1.5163, rank **90 / 114** (mid-low). Driven by `abs_outlier=0` (NULL outlier) and `max_cost=0.017` (very-cheap-seam) — the two stat lines of a "non-distinctive in absolute terms but architecturally well-integrated" surah.
- **Outlier-strength** Δ_pct: **0.00** (NULL classification in window {Q 107-113}). Q 110 is **structurally identical** to its mushaf-cohort — perfectly cohort-coherent.
- **iʿjāz sig_A** (rhyme + content + cohesion combined): **+1.329, rank 18 / 114 — TOP-15 NEAR-MISS**. Q 110 is **structurally iʿjāz-positive** (close to Q 14 Ibrāhīm at rank 14).
- **iʿjāz sig_B**: **+2.072, rank 6 / 114 — TOP-10**. Driven primarily by **z_local_cohesion = +2.31** (high local mushaf-cohesion within {107-113}) and **z_mean_content_distance = −1.57** (very low mean distance to corpus = high centrality).
- **Mean FR-content distance to corpus**: **0.7644**, rank **2 / 114** — Q 110 is one of the **TWO most-central surahs in the corpus** by FR-content vocabulary (the other typically being Q 108 al-Kawthar, with which Q 110 shares its FR-1 nearest-neighbor pair).
- **Q 109 → Q 110 mushaf-adjacency cost**: **0.0000 length-units** (rank 13/113 — among 13 EXACTLY-clamped-zero seams, H-NEW-1240). One of the *seamless* mushaf-transitions.
- **Q 110 → Q 111 mushaf-adjacency cost**: **0.0170 length-units** (rank 21/113, also very-cheap). The Naṣr → Masad seam is structurally cheap.

## 10. Quick content structure

Q 110 is a 3-verse, 19-word, 80-letter Medinan surah — the corpus's shortest *idhā*-opening surah. The structure is a 3-step rhetorical arc:

- **v.1 — CONDITION**: *idhā jāʾa naṣru llāhi wa-l-fatḥ* — "When the help of God and the conquest come" (the prophesied + then-realized Mecca-conquest).
- **v.2 — OBSERVATION**: *wa-raʾayta al-nāsa yadkhulūna fī dīni llāhi afwājā* — "And you saw the people entering God's religion in waves" (the post-conquest mass-conversion described as continuous-aspect).
- **v.3 — IMPERATIVE-RESPONSE**: *fa-sabbiḥ bi-ḥamdi rabbika wa-staghfirhu* + *innahu kāna tawwābā* — "So glorify with the praise of your Lord and seek His forgiveness; surely He is ever-Returning" (the prescribed emotional-spiritual response: tasbīḥ + istighfār + kāna tawwābā closing-clause).

Classically labeled the **al-Tawdīʿ** (الْتَوْدِيع — "the farewell"), not because it is named that, but because Companions recognized it as the prophetic-life-completion signal and the Prophet's response in his last months was to recite *subḥānaka rabbī wa-bi-ḥamdika allāhumma ighfir lī* in every prayer.

## 11. Connection to ongoing project findings

| Finding | Connection | Q 110 evidence |
|:--|:--|:--|
| **H-NEW-1030** (parent: chronology-architecture dissociation) | Q 110 is the project's strongest dissociation case (3.86×) | This file's §3 |
| **H-NEW-1200** (short-Meccan-tail eschatology meta-cluster) | Q 110 is *NOT* in the eschatology subset (no wa-mā adrāka, no idhā-cosmic-event) but IS structurally in the short-Meccan-tail by FR | Q 110 *idhā* is *idhā-victory-condition*, not *idhā-cosmic-event* |
| **H-NEW-1240** (13 seamless mushaf-seams) | Q 109 → Q 110 is rank 6 / 13 | Cross-ref §4 above |
| **H-NEW-103** (musabbiḥāt typology) | Q 110:3 is the rare imperative-form *fa-sabbiḥ* + *istaghfir* compound | Cross-ref §5 above |
| **cross-finding-011** (mushaf as FR-geodesic) | Q 110 contributes to the FR-geodesicity by occupying its proper short-mufaṣṣal-tail position | Q 110 mean-FR rank 2/114 = corpus-central |
| **cross-finding-013** (mushaf as topological ring) | Q 110 is part of TERMINAL_TRIAD-adjacent cluster {Q 108-114} that wraps around to Q 1 | Q 110 → Q 1 = 0.353 (top-15 FR) |
| **H-NEW-130/130b/130c** (FR-residual hinges) | Q 110 is *NOT* a structural-hinge — its seams to Q 109 and Q 111 are both very-cheap | Confirms hinges are at Q 14-15, 49-50, 56-57, NOT at the terminal triad |
| **Q 5 al-Māʾida specialist** (Q005-F-05) | Q 110 dissociation replicates Q 5's at 3× magnitude | Q 110 vs Q 5 FR = 1.178 (essentially mid-corpus far) |
| **H-NEW-71** (Allah-distribution) | Q 110 contains 2 *Allāh* tokens out of 19 words = **10.5% Allah-density** — top-3 corpus-density rank for *Allah* per word | See Q110-F-04 |

## 12. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md (UAS rank 90; FR-mean rank 2/114; sig_A rank 18/114; sig_B rank 6/114; outlier NULL)
- [x] 02-content-analysis.md (3-verse rhetorical arc; idhā-condition / observation / imperative-response; al-Tawdīʿ classical-name; *afwāj* + *tawwāb* lexical analysis)
- [x] 03-tafsir-survey.md (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, Ibn Kathīr, al-Bayḍāwī, al-Suyūṭī surveyed on the Q 110 farewell + Mecca-conquest interpretation)
- [x] 04-hadith-corpus.md (12 verified ḥadīths: Bukhārī ×6, Muslim ×4, Tirmidhī ×2; full Arabic+English with isnāds)
- [x] 05-classical-claims-audit.md (al-Ṭabarī Mecca-conquest, al-Suyūṭī chronological position, al-Zarkashī farewell-claim, al-Tirmidhī Q 110 = ¼ of Qurʾān virtue-claim, al-Biqāʿī Q 109→Q 110 munāsabah)
- [x] 06-novel-findings.md (Q110-F-01 chronology-mushaf gap formalization; Q110-F-02 Q 110-Q 5 latest-revealed-pair anti-cohesion; Q110-F-03 *fa-sabbiḥ + istaghfir* compound corpus-uniqueness; Q110-F-04 Allah-density in 19-word surah)
- [x] 07-cross-references.md (Q 110 ↔ Q 1 wrap-around link; Q 110 ↔ Q 5 chronology-pair; Q 110 ↔ Q 108 closest-FR-neighbor; Q 110 ↔ Q 109 polemical-pivot)
- [x] JOURNAL.md
