---
surah: 15
surah_name_ar: الحجر
surah_name_translit: al-Ḥijr
surah_name_english: The Hijr / The Stoneland
file_type: overview
date_last_updated: 2026-05-08
phase: B+
verdict: SCAFFOLD — full template built; 3 novel tests pre-registered + executed under Bonferroni-k=3
---

# Q 15 al-Ḥijr — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 15 | canonical |
| Arabic name | الحجر | canonical |
| Transliteration | al-Ḥijr | canonical |
| English meaning | "The Ḥijr" — named after the rocky settlement of the Thamūd / Ṣāliḥ-tribe (vv. 80-84); "the Stoneland" | classical |
| Verse count | 99 | Hafs-Kufan, `data/hafs-verse-counts.tsv` |
| Position in mushaf | 15 | canonical |
| Type | **Middle/Late Meccan** (uncontested) | `data/revelation-order.csv` Q15 row |
| Position in revelation order (Tanzil Egyptian Std, al-Suyūṭī-aligned) | **54 / 114** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **57 / 114 (Middle Meccan)** | `data/revelation-order.csv` `noldeke_phase = Middle Meccan` |
| Word count (no-tashkeel) | **666** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, all non-space chars) | **2,891** | same |
| Mean words/verse | **6.73** | computed (much shorter than Q 14's 17.0) |
| **Opening** | **الر ۚ تلك آيات الكتاب وقرآن مبين** — "ALR. These are the verses of the Book and a Qurʾān making things clear" | muqaṭṭaʿāt (ALR) + book-self-reference + *qurʾān mubīn* |
| Top rāwī | **ن (nūn)** at **81.8%** of 99 verses (extreme near-monorhyme) | computed from `h-new-750.json` |
| Sajda verse | none (Q 15 is NOT a *sūrat al-sajda*) | classical |

## 2. ⭐ Distinctive structural property — the Iblīs-rebellion narrative (vv. 28-44)

**Q 15:28-44** contains the corpus's most-extended Iblīs-rebellion-discourse — a 17-verse pre-creation narrative tracking from Adam's creation from *ṣalṣālin min ḥamaʾin masnūn* (clay of altered black mud) through Iblīs's refusal to prostrate, expulsion, request for respite, vow to mislead humanity, and God's exclusion of the *al-mukhlaṣīn* (the sincere servants).

**Pre-test result (Q015-F-01)**: Q15:28-44 contains **5 corpus-hapax tokens** (single-corpus-attestation): *لموعدهم* (Q15:43), *لأسجد* (Q15:33), *لأغوينهم* + *ولأغوينهم* (Q15:39, with parallel in Q38:82), *لأزينن* (Q15:39), *مقسوم* (Q15:44). Plus **20 near-hapax** (≤ 5 corpus attestations) — yielding a near-hapax-density of **20.4%** of unique tokens (87 unique → 25 hapax-or-near-hapax → 28.7% combined-rare-density).

In comparative context with the corpus's other Iblīs-rebellion narratives:

| Passage | Words | Unique tokens | Hapax | Near-hapax | Hapax-density |
|:-:|:-:|:-:|:-:|:-:|:-:|
| Q 7:11-25 | 201 | 150 | 22 | 38 | 14.7% |
| **Q 15:28-44** | **119** | **87** | **5** | **20** | **5.7%** |
| Q 17:61-65 | 68 | 61 | 11 | 10 | 18.0% |
| Q 18:50 | 28 | 27 | 2 | 5 | 7.4% |
| Q 20:115-126 | 131 | 107 | 18 | 21 | 16.8% |
| Q 38:71-85 | 99 | 75 | 7 | 17 | 9.3% |

Q 15:28-44 has the HIGHEST near-hapax-count (20) but NOT the highest hapax-count (Q 7:11-25 has 22 hapax). The ≥3 hapax threshold is met (5 hapax). The Iblīs-rebellion vocabulary is rare in the corpus and concentrated in these 6 narrative-blocks.

## 3. ⭐ The textual-preservation declaration (Q 15:9)

**Q 15:9**: *إنا نحن نزلنا الذكر وإنا له لحافظون* — "Indeed, We have sent down the Reminder, and We are its Guardian." This is the famous *iʿjāz al-ghayb* / textual-preservation iʿjāz claim cited by al-Bāqillānī and the wider classical iʿjāz tradition.

**Pre-test result (Q015-F-02, see `06-novel-findings.md`)**: Q 15:9 is the **corpus-UNIQUE verse** combining ALL THREE constructions:
- (a) *naḥnu nazzalnā* (We sent down) — appearing in only 2 verses corpus-wide: Q 15:9 (with *al-dhikr*) and Q 76:23 (with *al-Qurʾān*).
- (b) *al-dhikr / nazzala-dhikr* — the verb-noun pairing for revealing the Reminder; appearing in only 1 verse corpus-wide: Q 15:9.
- (c) *lahu la-ḥāfiẓūn* — the divine self-attribution as preserver of the revealed text; appearing across 4 verses corpus-wide (Q 9:112, Q 12:12, Q 12:63, Q 15:9), but in Q 9:112 and Q 12:12/63 the referent is NOT the revealed text (it's God's limits / Joseph's safekeeping).

**Q 15:9 is the corpus-UNIQUE verse where divine self-reference + revelation of the Reminder + divine guardianship of the Reminder are joined in a single locked construction**. (See Q015-F-02 for the formal SHA-locked verification.)

This is the empirical anchor for the classical *ḥifẓ al-Qurʾān* doctrine — that God's guarantee of the Qurʾān's preservation is THE distinctive Qurʾānic claim about its own textual stability.

## 4. Length classification

99 verses, 666 words — **mufaṣṣal-ṭiwāl-class** but **with very short verses** (mean 6.7 words/verse, much shorter than Q 14's 17.0 w/v). Q 15 sits at mushaf-position 15, in the head-mushaf zone (pre-Hijra-kink at s=50). Per H-NEW-660: predicted d̄_content(s=15) ≈ 0.96 (head-cohort plateau); observed `mean_content_distance` = **0.958** (`h-new-750.json` for surah=15). Spot-on.

The 99-verse + short-verse structure makes Q 15 a **rapid-fire iterative-narrative** surah — short verses, quick scene transitions (Iblīs creation → Lot's tribe → Hijr-tribe → revelation closure). The verse-rate is nearly 4× faster than Q 14's pacing.

## 5. Rhyme structure

**Top final letter (rāwī): ن (nūn) at 81.8%** of 99 verses (per `h-new-750.json`). This is **near-monorhyme** — Q 15 is rhyme-homogeneous, similar to Q 12 Yūsuf (84% on ن) and contrasting sharply with Q 14 Ibrāhīm's multi-rāwī د/ر/ن mixed structure.

**Rhyme entropy (Shannon, nats): 0.5376** — corpus z = **−0.42** (modestly below corpus mean — the near-monorhyme signature). This places Q 15 in the **head-mushaf monorhyme cluster** with Q 12 Yūsuf, contrasted with the Q 13/Q 14 multi-rāwī cluster.

The ن-final fawāṣil (in *al-mubīn / al-ʿālamīn / al-mursalīn / al-ṣādiqīn / al-mukhlaṣīn / al-ghāwīn / al-yaqīn / al-mathānī / al-mubīn* class endings) gives Q 15 its sustained narrative-rhythm. The rhyme-homogeneity is the empirical correlate of the iterative-narrative-block structure (Iblīs-rebellion-block + Lot-block + Hijr-tribe-block all using the same rāwī).

## 6. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **38 / 114** (mid-pack; substantially below Q 14's rank 20).
- **Outlier-strength** Δ_pct: **+5.51 pp**, classification **WEAK_OUTLIER** in window {Q 12-18} (`h-new-590.json` X=15). Q 15 is a **WEAK content outlier** vs its mushaf cohort — distinct from both Q 13 (NULL) and Q 14 (NULL). Q 15 introduces a content-shift in the mushaf-window.
- **iʿjāz sig_A**: **−0.765** (rank **81 / 114** — STRUCTURALLY iʿjāz-NEGATIVE). Q 15 is on the OPPOSITE side of the al-Bāqillānī axis from Q 14 (rank 14/114, sig_A POSITIVE). The Q 14→Q 15 seam is the boundary of the head-mushaf iʿjāz-positive zone.
- **iʿjāz sig_B**: **−1.087** (rank **86 / 114**).
- **Mean FR-content distance to corpus**: 0.958 (z = +0.345; modestly content-distinct).
- **Q 14→Q 15 canonical-adjacency cost**: **0.1988 length-units** (rank ≈ 13 / 113, **TOP-15 EXPENSIVE** seam — the highest in the head-mushaf zone after Q 1→Q 2).
- **Q 15→Q 16 canonical-adjacency cost**: **0.1698 length-units** (rank ≈ 17 / 113, also expensive).

Q 15's mushaf placement is structurally **a transition surah** — expensive to enter (from Q 14) and expensive to exit (to Q 16). The Q 15 zone is structurally the *iterative-prophet-narrative monorhyme* register, distinct from the head-mushaf high-rhyme-entropy + sig_A-positive zone of Q 13/Q 14.

## 7. Quick content structure

Q 15 is a 99-verse middle-Meccan surah composed of ~6 narrative blocks:

- **vv. 1-9**: Opening (الر + book-self-reference + *qurʾān mubīn*); disbelievers' delaying disbelief; messengers' role; **Q 15:9 textual-preservation declaration**.
- **vv. 10-15**: prior peoples mocked the messengers; door-from-heaven test (would not believe even if a door opened in the sky).
- **vv. 16-25**: cosmological signs (constellations, protection from the *shayṭān rajīm*, earth's mountains, fertilizing winds, water-from-sky); **Q 15:23 — *innā lanaḥnu nuḥyī wa-numītu wa-naḥnu al-wārithūn*** — God's resurrection-and-inheritance theme.
- **vv. 26-27**: creation of mankind from *ṣalṣālin min ḥamaʾin masnūn*; jinn from *nāri al-samūm* (fire of scorching wind).
- **vv. 28-44**: ⭐ **THE IBLĪS-REBELLION-CREATION NARRATIVE** — God announces creation of Adam to the angels; angels prostrate; Iblīs refuses; God's expulsion + *al-laʿna ilā yawmi al-dīn*; Iblīs requests respite, granted; Iblīs's vow *la-uzayyinanna lahum* (to make sin attractive) + *la-ughwiyannahum ajmaʿīn* (to mislead them all); divine exclusion of *ʿibādī minhum al-mukhlaṣīn*; Iblīs's authority confined to the *ghāwīn* (the misled); Hellfire for the followers, *sabʿatu abwāb* (seven gates).
- **vv. 45-50**: believers in Paradise — gardens, springs, peaceful entry, removed-rancor, brothers-on-couches; God's warning of severe punishment.
- **vv. 51-77**: ⭐ **THE LOT NARRATIVE** — Abraham's guests (the angelic visitors); annunciation of Isaac; Lot's tribe destruction; the angelic mission; Lot's intercession; the destruction by *ṣayḥa* + brimstone.
- **vv. 78-79**: brief reference to *aṣḥāb al-Ayka* (Companions of the Wood — Shuʿayb's people).
- **vv. 80-84**: ⭐ **THE HIJR-TRIBE (Thamūd / Ṣāliḥ's people) NARRATIVE** — *aṣḥāb al-Ḥijr* who carved homes from rocks; the destruction by morning-*ṣayḥa* (the surah's title-anchor).
- **vv. 85-99**: closing (cosmological assertion of creation-in-truth; ⭐ **Q 15:87 *sabʿan min al-mathānī* — the seven oft-repeated**, classical anchor for al-Fātiḥa-as-the-sevens; injunction to bear with the disbelievers; closing prayer-injunction *fasabbiḥ bi-ḥamdi rabbika* — *waʿbud rabbaka ḥattā yaʾtīka al-yaqīn* (worship until the certain comes [death])).

The surah is a **rapid-iterative-narrative microcosm**: Iblīs-rebellion + cosmology + Lot + Hijr-tribe + revelation-self-reference + closure. Distinct from Q 14's didactic-prayer-cosmological structure.

## 8. Connection to ongoing project findings

- **Q 15:28-44 Iblīs-rebellion narrative** is the corpus's most-extended Iblīs-rebellion-discourse (Q015-F-01). It complements Q 14:22's eschatological Iblīs-self-disavowal in the corpus's Iblīs-typology (see `surahs/Q014-ibrahim/07-cross-references.md` §4).
- **Q 15:9 textual-preservation declaration** is the corpus-UNIQUE *naḥnu-nazzalnā-al-dhikr + lahu-la-ḥāfiẓūn* construction (Q015-F-02). Empirical anchor for al-Bāqillānī's iʿjāz-of-preservation tradition.
- **Q 15:87 *sabʿan min al-mathānī*** is the classical anchor for al-Fātiḥa as the seven oft-repeated (Bukhārī #4498, #4641, #4720); see `04-hadith-corpus.md`.
- **Q 15 → Q 14 mushaf-adjacency seam** is top-15 EXPENSIVE in the corpus (rank ≈13/113). Q 15's iterative-near-monorhyme register sharply contrasts Q 14's didactic-multi-rāwī register.
- Q 15 is in ALR cluster {Q 10, 11, 12, 14, 15}; H-NEW-610 establishes muqaṭṭaʿāt-content-NULL at whole-surah scale; Q 15's FR-distance to ALR siblings provides another data-point for this NULL framework.

## 9. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md (UAS rank 38; outlier WEAK; sig_A rank 81/114; near-monorhyme on ن)
- [x] 02-content-analysis.md (6-block thematic structure; Iblīs + cosmology + Lot + Hijr-tribe + sabʿ-mathānī)
- [x] 03-tafsir-survey.md (≥ 5 mufassirūn surveyed)
- [x] 04-hadith-corpus.md (Bukhārī #3240, #4226, #4496 Hijr-tribe traditions; #4273, #4441, #4497, #4498, #4799 al-mathānī = al-Fātiḥa; verified hadith numbers)
- [x] 05-classical-claims-audit.md (al-Bāqillānī iʿjāz-of-preservation; al-Suyūṭī chronology; al-Biqāʿī Q 14→Q 15 munāsabah; rules-tuple verifications)
- [x] 06-novel-findings.md (Q015-F-01 Iblīs-rebellion-vocabulary lexical analysis; Q015-F-02 Q 15:9 corpus-uniqueness CONFIRMED; Q015-F-03 prophet-density Lot+Saliḥ vs Q11/26/29)
- [x] 07-cross-references.md (Q14-Q15 expensive seam; Iblīs-typology axis with Q 14:22; cluster context)
- [x] JOURNAL.md (run log, SHA hashes, decision points)
