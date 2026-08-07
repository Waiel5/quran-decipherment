---
surah: 49
surah_name_ar: الحجرات
surah_name_translit: al-Ḥujurāt
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,130/130b/130c,142,590,700,720,750,840} + cross-finding-013.
---

# Q 49 al-Ḥujurāt — Empirical Architectural Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline numbers

| Metric | Value | Source / interpretation |
|:--|:--:|:--|
| Verse count | 18 | Hafs-Kūfan |
| Word count (no-tashkeel) | 353 | computed |
| Letter count (no-tashkeel, sans spaces) | 1,533 | computed |
| Avg verse length (letters) | 85.17 | LONG-VERSE Medinan paraenesis |
| Avg verse length (words) | 19.61 | LONG-VERSE |
| Median verse length (words) | 18 | between v. 6 (18 words) and v. 17 (19 words) |
| Top final-letter | ن (nūn) | 10/18 verses = 55.6 % (`h-new-700.json` → top_final_letter_frac 0.5556) |
| Second final-letter | م (mīm) | 7/18 verses = 38.9 % |
| Rhyme entropy (nats) | 0.8544 | MEDIUM (z = +0.153 vs corpus mean) |
| Mean content distance (FR) | 0.9510 | slightly below corpus mean 0.9234; z = +0.272 |
| Local cohesion | 1.0998 | LOW LOCAL COHESION; z = -0.570 |
| iʿjāz sig_A | -0.1187 (rank 67/114) | NEAR-MEDIAN al-Bāqillānī iʿjāz al-fawāṣil signal |
| iʿjāz sig_B | -0.4169 (rank 65/114) | NEAR-MEDIAN al-Sakkākī iqāʿ signal |
| UAS (H-NEW-840) | -1.4844 (rank 26 from low; ~rank 89 from high) | LOW unified architectural significance — Q 49 is NOT a strong outlier on macro UAS |
| Outlier-strength Δ %ile (H-NEW-590) | -0.46 pp | NULL (not a strong outlier; window {Q 46-52}) |
| Q 48→Q 49 cost | +0.0830 (delta_raw +0.083; fraction_residual 0.0100) | low — al-Fatḥ → al-Ḥujurāt smooth transition |
| Q 49→Q 50 cost | +0.1771 (delta_raw +0.177; fraction_residual 0.0214) | **8th-highest delta in corpus** (out of 113); top-15-in-3-features hinge |
| Q 50→Q 51 cost | +0.1192 (delta_raw +0.119; fraction_residual 0.0144) | modest — Qāf → al-Dhāriyāt |
| ya-ayyuhā-alladhīna-āmanū count | **5** (rank-1 / 95 by density 0.2778) | CORPUS-EXTREME (Q049-F-01) |
| ya-ayyuhā-al-nāsu count | 1 (v. 13) | broader-address marker — universalist verse |
| Allāh-token count | 27 in 18 verses (1.50 per verse) | dense divine-vocative; rank-3 by per-verse-density of all surahs ≤ 18 verses |

## 2. Fisher-Rao neighborhood (H-NEW-111)

Q 49's top-15 nearest in FR space (decoded from `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`):

| Rank | Surah | Name | FR distance | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 61 | al-Ṣaff | 0.7279 | short Medinan, 14 v., address-formula-driven paraenesis |
| 2 | Q 64 | al-Taghābun | 0.7610 | short Medinan, 18 v. (length-twin), address-formula |
| 3 | Q 63 | al-Munāfiqūn | 0.7620 | short Medinan, 11 v., address-formula |
| 4 | Q 62 | al-Jumʿah | 0.7897 | short Medinan, 11 v., META-cluster hub |
| 5 | Q 66 | al-Taḥrīm | 0.8111 | short Medinan, 12 v., address-formula |
| 6 | Q 59 | al-Ḥashr | 0.8190 | Medinan, 24 v., Khawātim cluster |
| 7 | Q 112 | al-Ikhlāṣ | 0.8398 | Meccan, 4 v. (FR-near despite chronology gap; sui generis) |
| 8 | Q 95 | al-Tīn | 0.8412 | Meccan, 8 v. |
| 9 | Q 58 | al-Mujādalah | 0.8420 | Medinan, 22 v., address-formula |
| 10 | Q 57 | al-Ḥadīd | 0.8433 | Medinan, 29 v., musabbiḥāt + Khawātim |
| 11 | Q 60 | al-Mumtaḥanah | 0.8466 | Medinan, 13 v., address-formula |
| 12 | Q 47 | Muḥammad | 0.8503 | Medinan, 38 v., believer-vs-disbeliever |
| 13 | Q 81 | al-Takwīr | 0.8536 | early Meccan, 29 v. |
| 14 | Q 1 | al-Fātiḥa | 0.8537 | sui-generis short Meccan |
| 15 | Q 110 | al-Naṣr | 0.8547 | Medinan, 3 v. |

Q 49's FR-neighborhood is **dominated by the short-Medinan back-cluster** (Q 47, 57-66 covering 9 of the 15 nearest), with sui-generis short surahs (Q 1, Q 112, Q 110) appearing as secondary neighbors.

| Quantity | Value |
|:--|:--:|
| Q 49 mean FR distance to all 113 | 0.9510 |
| Q 49 mean FR distance to other 26 Medinan | 0.8892 |
| Q 49 mean FR distance to all 87 Meccan | 0.9695 |
| Q 49 mean FR distance to TARGET-SET {Q 61,62,63,64,66} | **0.7703** |

The TARGET-SET 0.7703 is 14.0 % below corpus mean 0.9510 and 11.6 % below length-matched mean 0.8709. See Q049-F-02 (CONFIRMED-PAIR, PASS-DIRECTED).

Far end:
- Q 55 al-Raḥmān: 1.2973 (the iʿjāz-anti-twin / refrain-driven outlier)
- Q 54 al-Qamar: 1.1352 (refrain-Meccan)
- Q 56 al-Wāqiʿah: 1.1231 (eschatological Meccan)
- Q 20 Ṭā-Hā: 1.1222 (long Meccan narrative)
- Q 17 al-Isrāʾ: 1.1102 (long Meccan)

## 3. ⭐ Q 49 → Q 50 universal-hinge status (THE LOAD-BEARING ANCHOR)

The mushaf-order transition Q 49 → Q 50 is one of the THREE universal hinges of the Quran (per H-NEW-130/130b/130c, H-NEW-142, cross-finding-013).

| Feature space | Distance/jump | In top-15? | Source |
|:--|:--:|:--:|:--|
| Root-distribution Fisher-Rao | 1.0035 | ✓ rank 14/15 | H-NEW-130 |
| Char-4-gram Fisher-Rao | 1.0939 | ✓ rank 9/15 | H-NEW-130b |
| Verse-length distribution | 1.3718 | ✓ rank 10/15 | H-NEW-130c (`in_all_three=True`) |
| TSP delta_raw (boundary cost) | 0.1771 | rank 8/113 | H-NEW-720 |
| Nöldeke-chronology gap | 72 positions | rank 1-2/113 | al-Suyūṭī rank 106 vs 34 |

Boundary labels at Q 49→Q 50: `mufassal_alt_49_50`, `muq_presence_change`, `period_Medinan_to_Meccan`, `phase_Medinan_to_Middle Meccan`.

This is a **load-bearing structural feature of the mushaf ring topology**. The 11 % geodesic-residual identified in cross-finding-011 (Quran is FR-information-geodesic optimal at z=-11.46, but with 11 % residual) is *concentrated at hinges of this kind*. Q 49 → Q 50 is one of those concentrating points.

See Q049-F-03 (CONFIRMED-CROSS-FEATURE).

## 4. Outlier-strength (H-NEW-590)

From `findings/phase-b-hypotheses/csv/h-new-590.json`:

| Field | Value |
|:--|:--:|
| Window | {Q 46, Q 47, Q 48, Q 49, Q 50, Q 51, Q 52} |
| d_W | 0.9246 |
| d_W − Q 49 | 0.9259 |
| Δ pp | -0.46 |
| pct_W | 42.52 |
| pct_W − Q 49 | 42.98 |
| p_greater_W | 0.5748 |
| Classification | **NULL** |

Q 49 is **not a content-distinct outlier** within its mushaf-window {Q 46-52}. The cluster Q 46-52 is itself heterogeneous (al-Aḥqāf → Muḥammad → al-Fatḥ → al-Ḥujurāt → Qāf → al-Dhāriyāt → al-Ṭūr — straddling the Q 49→Q 50 hinge).

This is consistent with Q 49 being **structurally important via its TRANSITIONAL role** rather than via outlier-content per se. Q 49 is the LAST major Medinan-period surah in mushaf order; its content profile fits Medinan paraenesis exactly. The unique structural property is its terminal POSITION in the Medinan stretch.

## 5. iʿjāz signature (H-NEW-750)

From `findings/phase-b-hypotheses/csv/h-new-750.json`:

| Component | Value | z-score | Rank |
|:--|:--:|:--:|:--:|
| Rhyme entropy (nats) | 0.8544 | +0.153 | (medium) |
| Mean content distance | 0.9510 | +0.272 | (slightly content-distinct) |
| Local cohesion | 1.0998 | -0.570 | (low local cohesion) |
| sig_A | -0.1187 | — | rank 67/114 (NEAR-MEDIAN) |
| sig_B | -0.4169 | — | rank 65/114 (NEAR-MEDIAN) |

Q 49 is **near-median on both iʿjāz axes**. al-Bāqillānī's iʿjāz al-fawāṣil reading places Q 49 in the middle band — neither a refrain-driven outlier (like Q 55) nor a verse-length-extreme (like Q 78). Its iʿjāz signature is the **average Medinan paraenesis surah**: long verses, modest fāṣila variety, low local cohesion (because the 4 thematic blocks each carry distinct lexicons).

Top final-letter ن (nūn) at 55.6 % rate is consistent with the Medinan rhyme pattern -ūn / -īn.

## 6. Canonical-adjacency cost (H-NEW-720)

| Boundary | delta_raw | fraction_residual | Note |
|:--|:--:|:--:|:--|
| Q 47 → Q 48 | +0.0332 | 0.0040 | low (Muḥammad → al-Fatḥ smooth Medinan) |
| Q 48 → Q 49 | +0.0830 | 0.0100 | modest (al-Fatḥ → al-Ḥujurāt) |
| Q 49 → Q 50 | **+0.1771** | **0.0214** | **HIGH — universal hinge (rank 8/113)** |
| Q 50 → Q 51 | +0.1192 | 0.0144 | modest (Qāf → al-Dhāriyāt) |
| Q 51 → Q 52 | +0.0096 | 0.0012 | very low |

Q 49 → Q 50 is the **8th-most-expensive boundary** in the entire mushaf:

Top-10 most expensive boundaries (per H-NEW-720): Q 1→2, Q 32→33, Q 33→34, Q 9→10, Q 24→25, Q 22→23, Q 42→43, **Q 56→57**, Q 12→13, Q 7→8 — and Q 49→50 is rank 8 with delta_raw 0.177.

(Note: Q 56→57 also carries delta_raw 0.227; Q 49→50 is the 8th. Q 14→15 — the 3rd universal hinge — has delta_raw closer to mean.)

## 7. UAS (H-NEW-840)

| Field | Value |
|:--|:--:|
| UAS | -1.4844 |
| abs_outlier | 0.460 |
| max_cost | 0.1771 |
| abs_ijaz | 0.1187 |
| Rank (low to high) | 26/114 |

Q 49's UAS is below corpus mean. The largest contributor to its UAS is `max_cost = 0.1771` (the Q 49→Q 50 boundary). Without that contribution, Q 49's UAS would be in the bottom-quartile (very low architectural significance). With it, Q 49 is in the bottom-quartile (rank 26 = 23 percentile).

This is consistent with the architectural reading: **Q 49's significance is not in its OWN content-distinctiveness** but in its **TERMINAL POSITION** in the Medinan stretch and the load-bearing transition it forms with Q 50.

## 8. ya-ayyuhā address-formula density (Q049-F-01)

| Surah | Verses | amanu count | Density | Type |
|:--|:--:|:--:|:--:|:--|
| **Q 49** | 18 | **5** | **0.2778** | Medinan |
| Q 60 al-Mumtaḥanah | 13 | 3 | 0.2308 | Medinan |
| Q 61 al-Ṣaff | 14 | 3 | 0.2143 | Medinan |
| Q 66 al-Taḥrīm | 12 | 2 | 0.1667 | Medinan |
| Q 58 al-Mujādalah | 22 | 3 | 0.1364 | Medinan |
| Q 5 al-Māʾidah | 120 | 16 | 0.1333 | Medinan |
| Q 33 al-Aḥzāb | 73 | 7 | 0.0959 | Medinan |
| Q 62 al-Jumʿah | 11 | 1 | 0.0909 | Medinan |
| Q 63 al-Munāfiqūn | 11 | 1 | 0.0909 | Medinan |
| Q 8 al-Anfāl | 75 | 6 | 0.0800 | Medinan |

Across 95 surahs of verse-count ≥ 10, **Q 49 is rank 1**.

Corpus-wide:
- Total *yā-ayyuhā alladhīna āmanū* = 89 attestations.
- ALL 89 are in Medinan surahs (zero Meccan); the formula is a strict Medinan-marker.
- Q 49 carries 5/89 = 5.6 % of all corpus attestations in 18/6,236 = 0.29 % of corpus verse-real-estate → **19.4× concentration above expectation**.

See Q049-F-01 (CONFIRMED).

## 9. Q 49:13 universalist-verse rare-root concentration (Q049-F-04)

Q 49:13 contains 14 unique roots (per QAC v0.4 morphology):

| Root | Q 49:13 count | Corpus total | Note |
|:--|:--:|:--:|:--|
| **شعب ($Eb)** | 1 | **2** | ⭐ corpus-EXACT-doubleton |
| Anv (unthā / female) | 1 | 30 | rare ≤50 |
| krm (k-r-m / honor) | 1 | 47 | rare ≤50 |
| xbr (x-b-r / aware) | 1 | 52 | borderline rare |
| Erf (ʿ-r-f / know) | 1 | 70 | rare ≤100 |
| qbl (q-b-l / facing-tribe) | 1 | 294 | medium |
| *kr (dhikr / remembrance) | 1 | 292 | medium |
| End (ʿ-n-d / "with, near") | 2 | 201 | medium |
| nws (n-ā-s / human) | 1 | 241 | medium |
| jEl (j-ʿ-l / make) | 1 | 346 | medium-high |
| xlq (kh-l-q / create) | 1 | 261 | medium |
| Elm (ʿ-l-m / know-knowledge) | 1 | 854 | high |
| wqy (w-q-y / fear) | 1 | 258 | medium |
| Alh (Allāh) | 2 | 2851 | corpus-extreme |

⭐ **The root شعب (sh-ʿ-b)** appears with corpus-total = 2 — the *strict doubleton*. Q 49:13 carries 1 of the 2 instances; the other is Q 4:90 (`fa-laysa Allāh lakum ʿalayhim sabīlā illā an taʿtatū qawmān baynakum wa-baynahum mīthāq aw jāʾūkum ḥaṣirat ṣudūruhum...`).

The phrase `شعوبا وقبائل` ("peoples and tribes") at Q 49:13 is therefore a **lexical hapax** — the only Quranic occurrence of *shuʿūb* in the universalist sense. (The Q 4:90 occurrence is a different sense: "tribe / people" as a kinship-bond unit, near-synonym to *qawm*.)

This concentration of corpus-rare lexicon at the verse identified by tafsīr as the universalist verse is empirically distinctive: **3 of 14 roots in Q 49:13 are corpus-rare ≤ 50**, and 1 is corpus-EXACT-doubleton.

See Q049-F-04 (CONFIRMED-VERSE-ANOMALY, 3/4 sub-tests pass).

Sub-test 4 (verse-rarity rank in bottom-decile) FAILS at the 0.4-rank-quantile, indicating Q 49:13 is rare-root-enriched but not in the corpus's most rarest decile (where short oath-Meccan verses dominate). Honest reporting: the rare-root concentration in Q 49:13 is REAL, but is not *extreme* in the global rarity-rank ordering — short oath-verses with single-token rare roots beat it on the rarity-mean metric.

## 10. Notable verse-level features

### Q 49:1 — opening with the strongest direct-address Medinan paraenesis:
*yā-ayyuhā alladhīna āmanū lā tuqaddimū bayna yaday Allāhi wa-rasūlih*

This is the surah-opening that contains the syntagm `bayna yaday Allāhi wa-rasūlih` ("between God's hands and His Messenger's hands") — a corpus-EXACT-singleton phrase (the only Quranic occurrence of this exact construction, per `quran-no-tashkeel.json` exact-substring scan).

### Q 49:2 — *aṣwātakum*:
The root **Swt (ṣ-w-t / voice)** appears 8 times corpus-wide. Q 49 carries 3 of those 8 (37.5 %). All in vv. 2-3.

### Q 49:6 — *fa-tabayyanū*:
The root **byn** (b-y-n) Form-V at v. 6 anchors the classical legal injunction to verify reports — al-Jaṣṣāṣ *Aḥkām al-Qurʾān* derives the entire qaḍīyah (jurisprudential rule) of news-verification from this verse.

### Q 49:7 — *al-rāshidūn*:
The qurʾānic-title *al-rāshidūn* (`أُولَئِكَ هُمُ الرَّاشِدُونَ`, "those are the rightly-guided") becomes the eponym of the Sunnī "Khulafāʾ al-Rāshidūn" doctrine (the four Rightly-Guided Caliphs). The Quranic source of the title is exclusively this verse plus Q 9:100.

### Q 49:13 — *shuʿūb wa-qabāʾil*:
The most-cited universalist phrase in the Quran (see §9 above). Its rendering as "peoples and tribes" preserves the sociological taxonomy: *shuʿūb* (larger genealogical groupings, cf. Latin *gens*) > *qabāʾil* (smaller tribal units, cf. Arabic kinship). The pre-tribal-and-pre-ethnic creational equality grounding is the strongest Quranic anchor for non-discrimination ethics.

### Q 49:14 — al-aʿrāb:
The construction *qālat al-aʿrāb āmannā qul lam tuʾminū* (the Bedouins said "we have believed" — say "you have not believed") is a corpus-RARE direct-correction of in-group claim of īmān, of which Q 49:14 is the LOCUS classicus. The same pattern is echoed in Q 9:101 about hypocrites, but Q 49:14 names the al-aʿrāb (Bedouins) specifically, with the asbāb-al-nuzūl context (Banū Tamīm or others — see hadith-corpus survey).

### Q 49:15 — *al-ṣādiqūn*:
A Medinan-formulaic verse-end identification of true believers. Echoes Q 2:177 *ulāʾika alladhīna ṣadaqū* ("those have been truthful").

### Q 49:18 — terminal closing on *ghayb*:
*Allāha yaʿlamu ghayba al-samāwāti wa-l-arḍ* ("God knows the unseen of the heavens and the earth") — a near-Khawātim-style divine-attribute closing that anchors the surah's epistemic-asymmetry reading: humanity's claims are limited; God's knowledge is total. Empirically, the construction `ghayba al-samāwāti wa-l-arḍ` is one of 4-5 corpus instances.

## 11. Cross-references to existing macro-findings

- **H-NEW-111 / cross-finding-011** (Mushaf is FR-information-geodesic): Q 49 contributes 1 universal-hinge boundary at Q 49→Q 50.
- **H-NEW-130 / 130b / 130c** (universal hinges): Q 49→Q 50 is `in_all_three=True`.
- **H-NEW-142** (universal hinges = max chronology-reversal): Q 49→Q 50 is one of 2 LARGEST chronology-reversal points (tied with Q 56→Q 57 at 58 Nöldeke positions per H-NEW-142, or 72 per al-Suyūṭī ranking).
- **cross-finding-013** (Mushaf = topological ring): Q 49 is one of 3 universal-hinge nodes.
- **cross-finding-014** (5-principle unified equation): Q 49 contributes M3 ring-topology empirical data.
- **cross-finding-008** (muqaṭṭaʿāt = book-introduction markers): Q 49 (non-muqaṭṭaʿ-opened) sits adjacent to Q 50 (muqaṭṭaʿ-opened with `qāf`) — empirical contrast point.
- **H-NEW-58c** (musabbiḥāt cluster): Q 49's FR-neighbor cluster {Q 61, Q 62, Q 64, Q 66} OVERLAPS with the musabbiḥāt cluster's mid-tier members.
- **H-NEW-189** (Medinan inclusio): Q 49 is in the Medinan-subset where first↔last root-inclusio is enriched.

## 12. Summary

Q 49 al-Ḥujurāt is empirically:
- The **corpus-rank-1 surah** by Medinan-address-formula density.
- The **terminal Medinan node** before the back-Meccan stretch in mushaf order.
- A **universal-hinge node** at Q 49→Q 50 transition (top-15-in-3-features intersection).
- A **tight FR-cluster anchor** for the short-Medinan back-cluster {Q 61, 62, 63, 64, 66}.
- The **carrier of the corpus's most universalist verse** (v. 13), itself a corpus-EXACT-doubleton on root *shaʿb*.

Its 18-verse, 353-word, 1,533-letter footprint encodes 5 amanu-formulas, 1 al-nāsu-formula, 27 Allāh-tokens, 4 thematic blocks, and 3 corpus-rare ≤50 roots in a single 21-word universalist verse.
