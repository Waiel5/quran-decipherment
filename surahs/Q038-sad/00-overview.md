---
surah: 38
surah_name_ar: ص
surah_name_translit: Ṣād
surah_name_english: Sād (the Arabic letter ṣād)
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — empirical profile complete; full investigation written 2026-05-07; 3 follow-up pre-registered tests (F-06..F-08) added 2026-05-09
---

# Q 38 Ṣād — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 38 | canonical |
| Arabic name | ص | canonical (named after the opening muqaṭṭaʿ letter) |
| Transliteration | Ṣād | canonical |
| English meaning | "Ṣād" (the 14th letter of the Arabic alphabet) | classical |
| Verse count | 88 | Hafs-Kufan |
| Position in mushaf | 38 | canonical |
| Type | Meccan (mid-Meccan, per al-Suyūṭī chronology) | classical |
| Position in revelation order (al-Suyūṭī) | 38 of 114 | al-Suyūṭī, *al-Itqān*, nawʿ 1 |
| Word count (no-tashkeel) | 774 | computed from `quran-no-tashkeel.json` |
| Letter count (no-tashkeel, sans spaces) | 3,104 | computed |
| Opening | ص ۚ والقرآن ذي الذكر — "Ṣād. By the Qurʾān, possessor of reminder/honor." | singleton-letter muqaṭṭaʿ + oath-by-Qurʾān |

## 2. Classical name

The surah is named after its opening muqaṭṭaʿ letter **ص** (ṣād). The naming convention places Q 38 in the small set of muqaṭṭaʿ-named surahs:
- Q 20 ṬāHā (طه)
- Q 36 YāSīn (يس)
- Q 38 Ṣād (ص) — singleton
- Q 50 Qāf (ق) — singleton
- Q 68 al-Qalam (originally نون; renamed after the second word)

The three **single-letter** muqaṭṭaʿāt surahs are Q 38, Q 50, and Q 68. Among these, Q 38 (ص) and Q 50 (ق) form a structural twin: both open with single letter + oath-swearing-by-the-Qurʾān (see §3).

## 3. Opening formula — singleton muqaṭṭaʿ + oath-by-Qurʾān

Q 38:1 opens with:

| Variant | Text |
|:--|:--|
| no-tashkeel | ص ۚ والقرآن ذي الذكر |
| min-tashkeel | صٓ ۚ وَالقُرآنِ ذِي الذِّكرِ |
| full-tashkeel | صٓۚ وَٱلۡقُرۡءَانِ ذِي ٱلذِّكۡرِۚ |

Translation gloss (Sahih International): "Ṣād. By the Qurʾān containing reminder…"

This pairs precisely with Q 50:1 *ق وَالْقُرْآنِ الْمَجِيدِ* — "Qāf. By the Glorious Qurʾān…" These are the **only two corpus verses** where a single muqaṭṭaʿ-letter is immediately followed by an oath swearing by the Qurʾān itself in the same verse. Q038-F-01 (CONFIRMED) places Q 38:1 ↔ Q 50:1 at p=0.0008–0.0027 across three similarity metrics, surviving Bonferroni-3 (α_bon = 0.01667).

**Classical reading**: al-Ṭabarī (*Jāmiʿ al-bayān*, ad loc.), Ibn Kathīr, and al-Rāzī all read the opening pattern as oath-introduced; the muqaṭṭaʿ letter functions either as a divine name, an alphabetical witness, or a phonological anchor for the surah's tone. al-Suyūṭī (*al-Itqān*, nawʿ 40) catalogs Q 38, Q 50, Q 68 as the three single-letter muqaṭṭaʿāt.

## 4. ⭐ Unique structural property — the prophet-cycle saturation surah

Q 38 names **11 prophets** in 88 verses (computed Q038-F-02): Nūḥ, Ibrāhīm, Lūṭ, Ismāʿīl, Isḥāq, Yaʿqūb, Ayyūb, **Dāwūd (×5), Sulaymān (×2)**, al-Yasaʿ, Dhū al-Kifl. Total prophet-token count: 16. Density: 2.067 prophet-tokens per 100 words — **rank 2/114** (only Q 87 al-Aʿlā ranks higher, but Q 87 has only 3 hits in 19 verses, a small-N artifact). Among comparable-length surahs (n ≥ 50), **Q 38 is rank 1/114**.

The prophet-cycle inner structure is:
- **vv. 17-26**: Dāwūd (David) — the trial of judgment between two litigants.
- **vv. 30-40**: Sulaymān (Solomon) — the trial of horses-and-throne.
- **vv. 41-44**: Ayyūb (Job) — the trial of bodily affliction.

This David → Solomon → Job triad is **unique to Q 38** in the Quranic corpus. The triad's lexical-thematic coherence was tested in Q038-F-04 and returned NULL (triad cohesion 0.0161 vs null mean 0.0129; not statistically distinguishable from random 28-verse samples within Q 38). The classical literary reading is thus more about **narrative juxtaposition** than lexical commonality.

## 5. ⭐ Singleton-letter self-amplification (cross-validated)

Q038-F-03 tested whether each of the three singleton-muqaṭṭaʿāt surahs (Q 38 ص, Q 50 ق, Q 68 ن) amplifies its own opening letter at a rate higher than corpus baseline.

| Singleton | Letter | self-rate | corpus-rate | Δ_pp | ratio | p_perm |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| Q 38 | ص | 0.914% | 0.623% | +0.291 | 1.47× | 0.0526 |
| Q 50 | ق | 3.718% | 2.120% | +1.599 | 1.75× | **0.0033** |
| Q 68 | ن | 10.093% | 8.240% | +1.853 | 1.22× | 0.0757 |

**All three direction-locked HIGHER predictions confirmed; only Q 50 passes Bonferroni-3 α=0.0167.** Q 38 misses by 0.036, Q 68 misses by 0.06. The directional signal is consistent across all three singletons (no pre-commit violation), but the strict inferential threshold is met only by Q 50.

Verdict on F-03: **NULL on Bonferroni-3, DIRECTIONAL on direction-of-effect (3/3 in pre-locked direction).**

This is honest reporting: the **singleton-self-amplification** hypothesis has consistent direction across all 3 singletons but only crosses Bonferroni for the strongest (Q 50). The Q 50 ق-amplification is robust at 1.75× the corpus-rate.

## 6. Length classification

88 verses, 774 words — mid-Meccan length. Position s=38 places Q 38 in the head-mushaf zone (pre-Hijra-kink at s=50).

## 7. Rhyme structure

Final-letter distribution across 88 verses (`h-new-700.json` rhyme_letter_diagnostics):
- **ب (bāʾ): 35 verses (39.8%)** — top final letter
- Other letters distribute the remaining 60%
- **Rhyme entropy (Shannon, nats): 1.7129** — z_rhyme_entropy = +1.71 (HIGH-ENTROPY, rank 22/114 on iʿjāz sig_A)

The high rhyme entropy contrasts with monorhyme surahs (Q 12 = 0.53 nats, Q 36 ≈ 0.50). Q 38's rhyme structure is **multi-tonal**, alternating across many final-letters; this reflects its compilation-of-prophet-vignettes form, where each vignette has its own register.

Top final letter ب is consistent with the mid-Meccan -āb / -īb / -aʾāb endings (e.g., *al-aḥzāb*, *al-ʿaẓīm*, *li-l-mutaqīna ḥusna ma-ʾāb*). The 39.8% ب-fraction is moderate; not a monorhyme.

## 8. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **59/114** (UAS=−0.32). Q 38 is **mid-pack** on the unified architectural score.
- **Outlier-strength**: **+2.70 pp** — WEAK_OUTLIER (window {Q 35-41}; Q 38 is mildly content-distinct from its mid-Meccan band).
- **iʿjāz sig_A**: +1.286 (rank 22/114) — moderately HIGH on al-Bāqillānī iʿjāz al-fawāṣil axis.
- **Mean content distance**: 0.9663 (just above corpus mean 0.9235).
- **Q37→Q38 canonical-adjacency cost**: 0.000 length-units (RANK BOTTOM, structurally seamless transition — Q 37 al-Ṣāffāt is also prophet-cycle).
- **Q38→Q39 canonical-adjacency cost**: 0.099 length-units (modest).
- **FR-nearest neighbor**: **Q 50 al-Qāf** at FR=0.854 (singleton-twin pair), then Q 78 al-Nabaʾ (0.833 — actually closest), Q 32 al-Sajda, Q 43 al-Zukhruf.

**Q 38 is mid-architectural-significance with a structurally seamless left seam to Q 37 al-Ṣāffāt and the closest content-affinity to Q 50 al-Qāf and Q 78 al-Nabaʾ.**

## 9. Quick content structure

- **vv. 1-16**: Opening — muqaṭṭaʿ + oath; rebuke of the Quraysh disbelievers; precedent of past nations destroyed for rejection.
- **vv. 17-26**: David's trial — the two litigants and his judgment; sajda location (v. 24).
- **vv. 27-29**: Address to the Prophet — the Quran is sent down for guidance.
- **vv. 30-40**: Solomon's trial — the horses; the throne; the wind.
- **vv. 41-44**: Job's trial — the affliction and remedy.
- **vv. 45-49**: Three Abrahamic patriarchs (Ibrāhīm, Isḥāq, Yaʿqūb), Ismāʿīl, al-Yasaʿ, Dhū al-Kifl.
- **vv. 50-64**: Eschatology — Garden vs Hellfire; conversation among the damned.
- **vv. 65-70**: Address: "qul" - declaration of monotheism.
- **vv. 71-85**: Iblīs / Adam — the angelic prostration narrative; Iblīs's refusal; ejection.
- **vv. 86-88**: Closing — "qul mā asʾalukum ʿalayhi min ajr" (no reward asked) + prophecy *wa-la-taʿlamunna nabaʾahu baʿda ḥīn*.

## 10. The Q 38:24 sajda location

Q 38:24 contains one of the **15 canonical sajdat al-tilāwa** (recitation prostrations) of the Quran. The classical sajda count of 15 (vs alternative 14) hinges on whether Q 38:24 is counted; **Bukhārī #4601** (idInBook) preserves Ibn ʿAbbās's argument (via Mujāhid via al-ʿAwwām) that David is among the prophets the Prophet ﷺ was commanded to follow (Q 6:84-90), therefore the Prophet performed sajda upon recitation of Q 38:24 — establishing it as a sajdat al-shukr / al-tilāwa.

## 11. Cross-references

- [[h-new-590-outlier-spectrum]] — Q 38 +2.70 pp WEAK_OUTLIER.
- [[h-new-840-unified-architectural-score]] — UAS rank 59/114.
- [[h-new-750-ijaz-signature]] — sig_A rank 22 (HIGH).
- [[h-new-720-canonical-adjacency-cost]] — Q 37→Q 38 = 0.000 (seamless), Q 38→Q 39 = 0.099 (modest).
- [[h-new-111-fisher-rao-mushaf]] — Q 38 ↔ Q 50 = 0.854 (singleton-twin).
- [[h-new-165-phonological-predictor]] — Q 38 ص singleton, phonologically maps to TSM cluster (per H-NEW-232).
- [[h-new-232-oq1-singleton-nearest-neighbor]] — Q 38 ص → TSM-cluster (a-priori match satisfied).
- [[cross-finding-026-iʿjāz-architecture]] — Q 38 in mid-iʿjāz typology.

## 12. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 8 pre-regs (Q038-F-01..F-08)
- [x] 8 scripts (SHA-verified)
- [x] 8 JSON outputs in `csv/`
