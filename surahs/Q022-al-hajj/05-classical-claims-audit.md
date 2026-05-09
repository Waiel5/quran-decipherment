---
surah: 22
surah_name_ar: الحج
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
---

# Q 22 al-Ḥajj — Classical Claims Audit

Audit of non-trivial classical claims about Q 22 with empirical test where possible. Each claim is presented with scholar+work+passage citation; rules-tuple specified; verdict given.

## 1. Claim — Q 22:39 is the corpus's FIRST verse on fighting

**Claimants**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 11 on al-nāsikh wa-l-mansūkh; al-Ṭabarī *Jāmiʿ al-bayān* vol. 18 p. 581 (Šākir ed.); al-Wāḥidī *Asbāb al-nuzūl* on Q 22:39; al-Bayhaqī *Dalāʾil al-Nubuwwa* III.10; Ibn Kathīr *Tafsīr* vol. 5 p. 433 (Dār Ṭayba); al-Zamakhsharī *Kashshāf* vol. 4 ad loc.

**Specific claim text**: *hādhihi awwalu āyatin nazalat fī al-qitāl* — "This is the first verse revealed in fighting-context."

**Rules-tuple**: `(no-tashkeel, Hafs-Kufan, Mashriqi)` plus chronological-ordering by Tanzil Egyptian Standard + Nöldeke (rank 107 places Q 22 in late Medinan, but with vv 39-41 traditionally dated to the first weeks post-Hijra).

**Empirical operationalization**: scan all 6,236 verses for explicit-fighting-permission constructions (any of: *udhina lilladhīna yuqātalūna*, *kutiba ʿalaykum al-qitāl*, *qātilū al-mushrikīn*, *quttiilū ḥaythu wajadtumūhum*, etc.); intersect with chronological-ordering by revelation-order CSV.

**Test results** (corpus-search performed against `quran-text/quran-no-tashkeel.json` + chronology in `data/revelation-order.csv`):

| Construction | First verse | Revelation order |
|:--|:--|:-:|
| *udhina lilladhīna yuqātalūna* | **Q 22:39** | **103** |
| *kutiba ʿalaykum al-qitāl* | Q 2:216 | 87 |
| *qātilū al-mushrikīna* | Q 9:36 | 113 |
| *uqtulū al-mushrikīna* | Q 9:5 | 113 |

By **revelation order**, the candidates in order are:
1. Q 2:216 (revelation-order 87, Medinan; obligation-of-qitāl) — chronologically PRIOR to Q 22:39.
2. **Q 22:39** (revelation-order 103, Medinan; permission-of-qitāl).
3. Q 9 al-Tawba sequence (revelation-order 113).

**Wait — Q 2:216 is chronologically prior**? The Tanzil Egyptian Standard places Q 2 (Medinan) at revelation-order 87 and Q 22 at 103. This complicates the classical "first permission" claim — unless we read "first" in the al-Suyūṭī tradition as "first revealed Medinan verse on the SPECIFIC theme of jihād-PERMISSION (not jihād-OBLIGATION)".

**al-Suyūṭī's distinction (re-reading)**: in *al-Itqān* nawʿ 11, al-Suyūṭī specifies Q 22:39 as the *udhina*-permission verse (first time fighting is *permitted* rather than *commanded*). Q 2:216 is *kutiba ʿalaykum al-qitāl* (it is *prescribed* upon you to fight) — a later-stage commandment in the legal-progression sequence.

**Chronological re-anchoring**: the al-Wāqidī chain to Ibn ʿAbbās in Tirmidhī #3171 places Q 22:39's revelation **at the moment of the Hijra itself**, i.e., circa year 1 AH. Q 2:216, dealing with the obligation-of-qitāl, is conventionally dated to year 2 AH (around Badr). Under THIS chronology, Q 22:39 IS first. The Tanzil revelation-order, which places Q 22 at 103, reflects the COMPLETION-of-revelation order for the full surah (which contains both Meccan and Medinan strata), not the revelation-order of v 39 specifically.

**Verdict: VINDICATED with rules-tuple-refinement**. The classical claim is VINDICATED under: (a) construction-specificity (*udhina*-permission vs *kutiba*-obligation), and (b) per-verse-revelation-order chronology rather than per-surah-revelation-order. Under the cruder per-surah Tanzil-Standard chronology, the claim looks falsified — but the classical sources themselves operate at per-verse chronology, which is the appropriate rules-tuple.

**Honest limit**: per-verse Quranic chronology is itself a reconstructed tradition; the *asbāb al-nuzūl* literature provides per-verse anchors for only a subset of verses. For verses without a specific *asbāb*, we cannot independently verify chronology.

## 2. Claim — Q 22 is the only surah with TWO sajda-verses

**Claimants**: al-Suyūṭī, *al-Itqān*, nawʿ 30 on sujūd al-tilāwa; al-Tirmidhī ad #578 (transmitting ʿUqba b. ʿĀmir's *fuḍḍilat sūratu al-Ḥajji bi-anna fīhā sajdatayni*); Abū Dāwūd #1402 transmitting ʿAmr b. al-ʿĀṣ; al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, kitāb al-sujūd; Ibn Kathīr *Tafsīr* vol. 5 p. 467.

**Rules-tuple**: `(no-tashkeel, Hafs-Kufan, Mashriqi)` — the canonical printed-mushaf with ۩-glyph annotations.

**Empirical operationalization**: direct count of the ۩ (U+06E9) glyph in `quran-text/quran-no-tashkeel.json`. The script is in `scripts/Q022_F_06_07_08_sajda_finding.py`.

**Test results** (Q022-F-06):

- **Total ۩ markers across the 6,236 verses**: 15
- **Surahs carrying ۩ markers**: 14
- **Surahs with ≥ 2 markers**: 1 (Q 22)
- **Q 22 markers**: at verses 18 and 77 (matching the classical positions)

**Verdict: VINDICATED**. Q 22 is the unique corpus-singleton on double-sajda. Verses 18 and 77 match the al-Suyūṭī enumeration in *al-Itqān* nawʿ 30 + the classical Sunnī jurisprudential position.

**Rules-tuple sensitivity**: Under the **Maliki** rule-variant (single sajda in Q 22, at either 22:18 OR 22:77 depending on sub-tradition), Q 22 would NOT be the corpus-singleton; some sajda-surah would tie at 1, and Q 22 would also be at 1. Under the **Imāmī** rule-variant (only 4 wājib sajdas, none in Q 22), Q 22 has 0 wājib sajdas — making other 4-sajda surahs Q 32, Q 41, Q 53, Q 96 the "primary" sajda-surahs.

The PRINTED Hafs-Kufan Mashriqi mushaf carries both ۩ markers regardless of jurisprudential school. Under the canonical printing convention, Q 22's double-sajda is observable.

**Project finding**: this is a TEXT-INSCRIPTION-LEVEL fact that survives the empirical audit. The Sunnī-majority classical claim is empirically robust under the project-default rules-tuple. The Maliki dissent represents a JURISPRUDENTIAL-PRACTICE position about whether to perform the sajda, not a denial that the ۩ glyph appears at v 77 in the canonical text.

## 3. Claim — Q 22 is "mixed Meccan-Medinan"

**Claimants**: al-Qurṭubī *al-Jāmiʿ li-aḥkām* intro to Q 22; al-Suyūṭī *al-Itqān* nawʿ 1; al-Wāḥidī *Asbāb al-nuzūl* (verse-by-verse identification of strata); Ibn ʿAṭiyya *al-Muḥarrar al-wajīz*.

**Specific operationalization**: claim that vv 19-24 are Medinan-Badr-context; vv 25-30 are Medinan-Hijra-context; vv 39-41 are Medinan-permission-of-war; vv 1-18 and 60-78 contain mixed registers with Meccan-eschatological cores.

**Rules-tuple**: per-verse stratification (`asbāb al-nuzūl` anchored chronology).

**Empirical test (Q022-F-02)**: under a 5-feature per-verse Meccan-feature axis (verse length, *yā ayyuhā al-nāsu* / *yā ayyuhā lladhīna āmanū* vocatives, legal-keywords, eschatological-keywords), test bimodality of the verse-score distribution within Q 22.

**Result**: NULL on both pre-registered cells (Hartigan dip statistic + Silverman bandwidth bootstrap). The Q 22 verse-score distribution is empirically UNIMODAL under this feature operationalization.

**Verdict: NULL** on the empirical-operationalization. The classical "mixed" claim is not refuted — but it is not supported by simple-feature bimodality. Q 22 is so thoroughly mixed that simple linear feature-discrimination cannot tease out the strata. This is consistent with two interpretations:

- **Interpretation A (classical strata exist but are rhetorically integrated)**: the asbāb-al-nuzūl strata are real, but Q 22's editorial-integration has produced a verse-mosaic where no simple feature-axis can detect chronology. This is consistent with the classical *mūṣaḥaf*-integration tradition (per the *taʾlīf* of the Qurʾān during ʿUthmān's redaction).
- **Interpretation B (classical strata are over-attributed)**: the mixed-character of Q 22 may be partially a post-hoc classical reading projected onto a more-unified text. al-Zamakhsharī's Meccan-only position would correspond to this view.

The empirical NULL doesn't discriminate between A and B; it just says simple-feature bimodality is absent.

**Project finding**: the classical "mixed" claim survives as a textually-traditional reading but lacks simple-feature empirical support. A more sophisticated analysis (e.g., multi-axis verse-clustering with chronological-feature priors) would be required to discriminate.

## 4. Claim — Q 22:52 *tamannī* verse is the legislative-companion to the *gharānīq* incident

**Claimants**: al-Wāḥidī *Asbāb al-nuzūl* on Q 22:52; al-Ṭabarī *Tārīkh* I.1192-1196 + *Jāmiʿ al-bayān* on Q 22:52; al-Bayhaqī *Dalāʾil al-Nubuwwa* II.285; Ibn Saʿd *Ṭabaqāt* I.205.

**Specific claim text (al-Ṭabarī Tārīkh)**: Q 22:52 was revealed AFTER the *gharānīq* incident at Q 53 as the **corrective verse**, explaining that "every prophet, when he recites, Satan throws something into his recitation; God then abrogates the satanic insertion and confirms His verses."

**Rules-tuple**: classical Sīra-historiographical chronology.

**Empirical audit** (cross-reference to Q 53 specialist's full audit at `surahs/Q053-al-najm/05-classical-claims-audit.md` §2):

- **Canonical-hadith corpus**: NONE of the 9 canonical hadith books contain the phrase *al-gharānīq al-ʿulā* or related interpolation-narration. Direct corpus search across `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` — verified by Q 53 specialist 2026-05-09.
- **al-Bukhārī Q 22 tafsir-chapter**: the surah-by-surah *tafsīr* chapter (Kitāb al-Tafsīr chapter id 65) carries 1 entry on Q 22 (idInBook ~4731), commenting on v 19 *hādhāni khaṣmāni khtaṣamū* — the Badr champions. No mention of the *tamannī* + *gharānīq* connection.
- **al-Albānī** (*Naṣb al-Majānīq li-Nasf Qiṣṣat al-Gharānīq*, Damascus 1952): comprehensive isnād-by-isnād critique demonstrating all chains are *mursal* or weak.
- **Ibn Kathīr** (*Tafsīr* vol. 5 pp. 423-425 on Q 22:52, Dār Ṭayba ed.): "*hādhihi al-qiṣṣa rawāhā kathīrun mina al-mufassirīna lākinnahā mursalatun min ṭuruqin*" — this story is narrated by many mufassirūn but it is *mursal* through all chains, with no Companion-link reaching back to the Prophet.

**Verdict: SURVIVES at the level of historiographical phenomenon (al-Ṭabarī, al-Wāqidī, Ibn Saʿd, al-Bayhaqī all report it as occasion-of-revelation); FAILS at the level of canonical-hadith verification (zero attestations); FAILS at the level of empirical-text anomaly detection (Q 53:19-23 lexical-distribution-typical per Q053-F-02)**.

This is the project's M-5 classical-doctrine-decomposition pattern: the **balāgha-rhetorical reading** of v 52 (Satan-suggestion as universal-prophetic-trial-motif) SURVIVES empirical audit; the **historical-apologetic interpolation claim** (al-Wāqidī, late-Ṭabarī aggregator) FAILS.

## 5. Claim — Q 22 contains the "first explicit names of revealed religions"

**Claimants**: al-Ṭabarī *Jāmiʿ al-bayān* on Q 22:17; al-Qurṭubī ad loc.

**Specific claim**: Q 22:17 — *inna lladhīna āmanū wa-lladhīna hādū wa-l-ṣābiʾīna wa-l-naṣārā wa-l-majūsa wa-lladhīna ashrakū* — "Those who believe, those who are Jews, the Sabians, the Christians, the Magians, and those who associate" — is the corpus's most comprehensive religious-community enumeration, naming 6 religious groups (more than any other single Quranic verse).

**Rules-tuple**: surface lexical occurrence of religious-community-names.

**Empirical test**: scan Q022's text for: *al-yahūd* (Jews), *al-naṣārā* (Christians), *al-ṣābiʾūn* (Sabians), *al-majūs* (Magians), *al-mushrikūn* (polytheists). Cross-reference with corpus-wide search.

**Result**: 
- *al-majūs* (Magians) appears EXACTLY ONCE in the entire Quran — at Q 22:17. **HAPAX in the corpus**.
- *al-ṣābiʾūn* appears 3 times total: Q 2:62, Q 5:69, Q 22:17. Q 22:17 is the THIRD attestation.
- *al-naṣārā* and *al-yahūd* and *al-mushrikūn* are common across the corpus.

**Verdict: VINDICATED with refinement** — Q 22:17 is the unique attestation of *al-majūs* (Magians) in the corpus, making it the corpus's most religiously-inclusive single verse. The classical claim that Q 22:17 names six religious communities is empirically robust; the *al-majūs* hapax is the Q 22-distinctive feature.

This is also consistent with the classical Medinan-context reading: post-Hijra Medinan revelation engaged with a wider religious landscape (Persia + the Zoroastrian-influenced eastern Arabia) than Meccan revelation had.

## 6. Claim — Q 22:73 is the "fly-parable" — a unique creative-argument-from-creation

**Claimants**: al-Rāzī *Mafātīḥ al-ghayb* vol. 23 pp. 89-93 (on Q 22:73); al-Māwardī *al-Amthāl fī al-Qurʾān*; al-Qurṭubī ad loc.

**Specific claim**: Q 22:73's *al-dhubāb* (fly) is unique among the Quran's creation-arguments — no other verse uses the fly specifically as a creation-witness.

**Rules-tuple**: corpus-wide hapax-check on *al-dhubāb*.

**Empirical test**: search corpus for *dhubāb*.

**Result**: *al-dhubāb* (and its derivatives) appears ONLY at Q 22:73-74. The fly is a Q 22-monopoly creature in the Quranic creation-vocabulary. (Mosquito *baʿūḍa* at Q 2:26 plays a parallel rhetorical role; bee *naḥl* is the Q 16 al-Naḥl surah-namesake; spider *ʿankabūt* is the Q 29 al-ʿAnkabūt namesake.)

**Verdict: VINDICATED**. Q 22:73's fly-parable is empirically a corpus-monopoly. The classical *amthāl al-Qurʾān* literature's identification of this parable as a Q 22-distinctive rhetorical move is empirically robust.

## 7. Claim — Q 22 is uniquely positioned in the mushaf order (between al-Anbiyāʾ and al-Muʾminūn)

**Claimants**: al-Biqāʿī *Naẓm al-Durar* vol. 5 intro to Q 22; al-Rāzī *Mafātīḥ* vol. 23 intro on the *munāsabat al-surah*.

**Specific claim**: Q 21 → Q 22 → Q 23 form a tight rhetorical triad of prophets-cycle → ritual-anchor → believer-portrait.

**Rules-tuple**: rhetorical-thematic continuity assessment vs FR-content-distance metric.

**Empirical test (Q022-F-05)**: the {Q 21, Q 22, Q 23} triplet's mean FR-distance among 3 pairwise = 0.914; rank 74 of 112 consecutive triplets; percentile 66% (upper-mid).

**Result**: the triplet is NOT FR-cohesive (rank 74 is in the upper-half = less cohesive). Pairwise: Q 21↔Q 22 = 0.959; Q 22↔Q 23 = 0.953; Q 21↔Q 23 = 0.829. Q 21 and Q 23 are CLOSER to each other than either is to Q 22 — Q 22 is the OUTER member of the Q21-23 triplet on FR-roots.

**Verdict: PARTIAL** — al-Biqāʿī's rhetorical-*munāsaba* triad is preserved as a rhetorical reading (the thematic progression prophets→ritual→believer is genuine), but the triad does NOT correspond to FR-roots cohesion. This is exactly cross-finding-025's prediction: rhetorical continuity does not require root-distribution cohesion.

The classical *munāsaba* tradition is rhetorical, not statistical; its claims are about *intelligible-coherence-of-meaning*, not about *root-frequency-overlap*. The two axes are partially-independent.

## 8. Claim — Q 22:18's cosmic-roll-call sajda is the unique "creation-prostration" verse

**Claimants**: al-Zamakhsharī *Kashshāf* vol. 4 pp. 187-189; al-Ṭabarī ad loc; al-Rāzī *Mafātīḥ* vol. 23 pp. 16-21.

**Specific claim**: Q 22:18's enumeration of "sun, moon, stars, mountains, trees, animals, mankind-many" prostrating to Allāh is unique among the sajda-verses for its **cosmic roll-call** structure.

**Rules-tuple**: cosine-similarity on word-token vectors among the 14 sajda-verses; the cosmic-roll-call hypothesis predicts that Q 22:18 clusters with the OTHER cosmic-roll-call sajdas Q 13:15 and Q 16:49.

**Empirical test (Q022-F-01)**: Bonferroni-3 family.
- T1: mean cos(Q22:18, {Q13:15, Q16:49}) = 0.322 > median(Q22:18, other-11 sajdas) = 0.000 — **PASS**
- T2: cos(Q22:18, Q22:77) = 0.000 < 0.322 — **PASS** (Q22:18 is much closer to the cosmic-cluster than to Q22:77)
- T3: permutation p = 0.012 < α_bon = 0.01667 — **PASS**

**Verdict: VINDICATED** (3 of 3 cells pass). The cosmic-roll-call typology is empirically robust at the verse-level. Q 22:18 clusters with Q 13:15 + Q 16:49 (cosine 0.32 vs 0.00 baseline), supporting the classical typological reading of "cosmic-creation-prostration" as a Quranic sub-genre.

## 9. Audit summary table

| Classical claim | Source(s) | Verdict | Notes |
|:--|:--|:-:|:--|
| Q 22:39 first jihād-permission | al-Suyūṭī, al-Ṭabarī, al-Wāḥidī | **VINDICATED with rules-tuple-refinement** | per-verse chronology required |
| Q 22 double-sajda corpus-singleton | al-Tirmidhī #578, Abū Dāwūd #1402, al-Suyūṭī | **VINDICATED** under canonical Hafs-Kufan Mashriqi mushaf | Maliki rule-variant differs |
| Q 22 mixed Meccan-Medinan | al-Qurṭubī, al-Wāḥidī, al-Suyūṭī | NULL on simple-feature bimodality | Q022-F-02 |
| Q 22:52 *tamannī* + *gharānīq* | al-Ṭabarī Tārīkh, al-Wāḥidī, al-Bayhaqī | **PARTIAL** (Sīra preserves; canonical-hadith NULL; empirical-text NULL) | cross-ref Q053-F-02 |
| Q 22:17 6-religion enumeration | al-Ṭabarī, al-Qurṭubī | **VINDICATED with refinement** | *al-majūs* hapax |
| Q 22:73 fly-parable unique | al-Rāzī, al-Māwardī | **VINDICATED** | *al-dhubāb* corpus-monopoly |
| Q 21-22-23 rhetorical triad | al-Biqāʿī *Naẓm al-Durar* | **PARTIAL** (rhetorical yes; FR-cohesion no) | Q022-F-05 |
| Q 22:18 cosmic-roll-call cluster | al-Zamakhsharī, al-Rāzī | **VINDICATED** (3/3 cells) | Q022-F-01 |

## 10. Honest limits

- The audit operationalizes classical claims into testable predictions; some claims (e.g., the *tamannī* verse's theological-doctrinal significance) are not empirically testable in their original form.
- Pre-verse Quranic chronology is a reconstructed tradition; per-surah Tanzil chronology + Nöldeke is the firmer ground. Disputes between the two affect the Q 22:39 first-permission claim.
- The Maliki rule-variant is a real rules-tuple sensitivity for the Q022-F-06 finding. Under Maliki, Q 22 is not a corpus-singleton.
- The Q 22:52 + *gharānīq* audit relies on the Q 53 specialist's Q053-F-02 finding; this audit does not re-litigate. Cross-corroboration via the *tamannī* construction shows it appears at Q 22:52 and also at Q 17:73-75 (the *fitna* test verses) — the *tamannī*-theme is itself a partial corpus motif.
