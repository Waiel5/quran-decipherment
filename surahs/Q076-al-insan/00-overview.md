---
surah: 76
surah_name_ar: الإنسان / الدهر
surah_name_translit: Al-Insān / Al-Dahr
surah_name_english: "The Human Being" / "Time"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — full template built; 4 novel tests pre-registered + executed under Bonferroni-k=4
---

# Q 76 al-Insān (al-Dahr) — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 76 | canonical |
| Arabic name | الإنسان (al-Insān) — "The Human Being" | canonical (mushaf header) |
| Alternate name | الدهر (al-Dahr) — "Time" / "Aeon" | classical, attested al-Bukhārī Saḥīḥ #1037, Muslim #9200, Tirmidhī #26300 |
| Transliteration | Al-Insān (Al-Dahr) | canonical |
| Verse count | 31 | Hafs-Kūfan, `data/hafs-verse-counts.tsv` |
| Position in mushaf | 76 | canonical |
| Type | **DISPUTED** — Tanzil Egyptian Standard (Sunni traditional): **Medinan** (revelation-order #98); Nöldeke: **Middle Meccan** (Nöldeke-order #52). The disagreement is the largest phase-shift among Q 76's mushaf-neighbors (Q 73, 74, 75, 77, 78 are all Early Meccan in both schemes). | `data/revelation-order.csv` |
| Word count (no-tashkeel, basmala-counted-only-in-Q-1) | **250** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, all non-space chars) | **1,094** | same |
| Mean words/verse | **8.06** | computed |
| **Opening** | **هل أتى على الإنسان حين من الدهر لم يكن شيئا مذكورا** — "Has there come upon the human a span of time when he was not a thing mentioned?" | classical mufassirūn unanimous on rhetorical-question genre |
| **Top rāwī** | **ا (alif)** at **100% (31/31)** — Q 76 is **single-rāwī alif corpus-EXACT** | computed `findings/phase-b-hypotheses/csv/h-new-750.json` |
| Sajda verse | none (Q 76 is NOT a *sūrat al-sajda*) | classical |

## 2. ⭐ Corpus-EXACT-EXTREME — Q 76 paradise-tableau density

**Q 76 ranks 1/114 surahs in paradise-vocabulary density at 18.0% (per `Q076-F-01`)**, more than 1.84× the rank-2 surah (Q 88 al-Ghāshiya at 9.78%). Of the **5,174 sliding 11-verse windows** in the corpus, **all top-5 windows are inside Q 76**, and **9 of the top-10** are inside Q 76 — only Q 56 al-Wāqiʿah's vv. 28-38 cracks the top-10 at rank 9 (30.77%). The 11-verse window Q 76:11-21 reaches **46.43% paradise-density** (39 paradise tokens / 84 words), the highest verbal-density of jannah-imagery in the entire Qurʾān.

Permutation null: A length-matched random permutation of 31 verses across the corpus reaches Q 76's density 0/10,000 times (p < 0.0001, null max = 3.957%). A paradise-vocab-shuffle null (368 paradise-tokens redistributed by per-verse word-weight) places Q 76 at rank 1 only 5/10,000 times (p = 0.0005). Both are below α_bon = 0.0125 (Bonferroni-4 corrected).

This is a **CORPUS-EXACT-EXTREME** verdict — the most-paradise-saturated surah in the Qurʾān, with rank-1 status replicated on 4 independent operationalizations (per-surah density, sliding-window density, length-matched null, vocab-distribution null).

## 3. ⭐ Corpus-EXACT — longest 100%-alif single-rāwī surah

Q 76's 31 verses ALL end in alif (alif-tanwīn or alif-mamdūda — `mudhakkūrā`, `baṣīrā`, `kafūrā`, `saʿīrā`, `kāfūrā`, `tafjīrā`, `mustaṭīrā`, `wa-asīrā`, `shakūrā`, `qamṭarīrā`, `wa-surūrā`, `wa-ḥarīrā`, `zamharīrā`, `tadhlīlā`, `qawārīrā`, `taqdīrā`, `zanjabīlā`, `salsabīlā`, `manthūrā`, `kabīrā`, `ṭuhūrā`, `mashkūrā`, `tanzīlā`, `kafūrā`, `wa-aṣīlā`, `ṭawīlā`, `thaqīlā`, `tabdīlā`, `sabīlā`, `ḥakīmā`, `alīmā`).

Across the entire 114-surah corpus, **only 4 surahs achieve 100% alif-rāwī**:
| Q | Verses (all alif) |
|--:|--:|
| **Q 76 al-Insān** | **31** ⭐ rank 1 |
| Q 48 al-Fatḥ | 29 |
| Q 72 al-Jinn | 28 |
| Q 91 al-Shams | 15 |

Q 76 is **rank-1 / 4** of the 100%-alif surahs and **rank-2 / 13** of all 100%-monorhyme surahs (only Q 54 al-Qamar exceeds it at 55 verses, all rāʾ). The combination *(31 verses) × (100% alif rāwī)* gives Q 76 a **rhyme_entropy = 0.0** with **n_verses = 31** — the longest such stretch on alif anywhere in the corpus.

This is per `Q076-F-02` — verdict CONFIRMED-CORPUS-EXACT.

## 4. ⭐ Q 75 ↔ Q 76 mushaf-adjacent pair: creation-resurrection bracket

Among the 113 mushaf-adjacent pairs, **only TWO pairs have the creation-triplet roots {xlq (create), Ans (human), nTf (sperm-drop)} present in BOTH surahs**:
- Q 22 al-Ḥajj ↔ Q 23 al-Muʾminūn
- **Q 75 al-Qiyāma ↔ Q 76 al-Insān** ⭐

A random pair has 0.68% probability of triplet co-occurrence (10,000-perm null). The adjacent-pair empirical rate is 1.77% (2/113). Q 75 establishes the resurrection-axis ("lā uqsimu bi-yawm al-qiyāma… a-yaḥsabu l-insānu allan najmaʿa ʿiẓāmahu") and Q 76 establishes the original-creation axis from sperm-drop ("innā khalaqnā l-insāna min nuṭfatin amshājin nabtalīhi"). The pair forms a deliberate **resurrection ↔ creation bracket** at the mid-Mufaṣṣal boundary.

Q 75 ↔ Q 76 FR-distance = **0.8165** (24th percentile of 6,441 corpus pair-distances) — within the FR-close tail. Verdict: CONFIRMED (2/2 cells PASS per `Q076-F-03`).

## 5. ⭐ Shīʿī Ahl-al-Bayt revelation-cause: AUDIT-VERIFIED-NEGATIVE in Sunni canonical corpus

The Imāmī Shīʿī tafsir tradition (al-Ṭabarsī *Majmaʿ al-Bayān*; *Tafsīr al-ʿAyyāshī*) holds that Q 76:5–22 was revealed about ʿAlī, Fāṭima, al-Ḥasan, and al-Ḥusayn after they fed an orphan, a poor man, and a captive on three consecutive days while breaking fast on water alone. Al-Suyūṭī's *al-Durr al-Manthūr* (Sunni-side) reports the narrative on isolated chains via Ibn Mardawayh, ʿAbd b. Ḥumayd, al-Ḥākim, and al-Wāḥidī's *Asbāb al-Nuzūl*.

**Audit result (`Q076-F-04`)**: The revelation-cause narrative does NOT appear at canonical-ṣaḥīḥ rank in any of the 6 Sunni canonical hadith corpora (Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Ibn Mājah, al-Nasāʾī). Cross-corpus search returns **0 hits** for the 4-keyword threshold {Ahl al-Bayt + Fāṭima + ʿAlī + Ḥasan/Ḥusayn} co-occurring with Q 76 markers.

**What IS canonically attested for Q 76**: the Friday-Fajr recitation pattern (Prophet recited Q 32 al-Sajda in rakaʿa 1 + Q 76 al-Insān/al-Dahr in rakaʿa 2 of Friday Fajr). Verified across:
- **Bukhārī #870** + **#1037** (in Friday-prayer chapter)
- **Muslim #9200** (bk2 #1923, parallel chain)
- **Tirmidhī #26300** (bk5 #520, parallel)
- **Abū Dāwūd #21579** (parallel)

The audit verdict is **AUDIT-VERIFIED-NEGATIVE-AND-FRIDAY-CONFIRMED**: the Imāmī revelation-cause narrative is not Sunni-canonically corroborated, while the Friday-Fajr recitation pattern is canonically attested across at least 4 Kutub al-Sitta works. This is NOT a refutation of the Imāmī claim under Imāmī sanad standards (which the audit explicitly does not engage); the project's standard requires Sunni-canonical corroboration for findings to enter the Sunni-side classical-claim ledger.

## 6. Chronology classification dispute — Q 76 is the largest phase-discrepancy in its mushaf-neighborhood

The Tanzil Egyptian Standard (Sunni traditional consensus) places Q 76 at revelation-order #98 with classification **Medinan**. Nöldeke's chronology places Q 76 at order #52 with classification **Middle Meccan**. This is a **46-position phase-discrepancy**, the largest among Q 76's mushaf-neighbors (Q 73-78), all of which are Early Meccan in both schemes.

| Surah | Tanzil order | Tanzil phase | Nöldeke order | Nöldeke phase |
|--:|--:|:--|--:|:--|
| Q 73 al-Muzzammil | 3 | Meccan | 23 | Early Meccan |
| Q 74 al-Muddaththir | 4 | Meccan | 2 | Early Meccan |
| Q 75 al-Qiyāma | 31 | Meccan | 36 | Early Meccan |
| **Q 76 al-Insān** | **98** | **Medinan** | **52** | **Middle Meccan** |
| Q 77 al-Mursalāt | 33 | Meccan | 32 | Early Meccan |
| Q 78 al-Nabaʾ | 80 | Meccan | 33 | Early Meccan |

The phase-dispute structure: Sunni tradition (al-Wāḥidī *Asbāb al-Nuzūl*; al-Suyūṭī *al-Itqān*) classifies Q 76 as **Medinan-late** because the Ahl-al-Bayt revelation-cause narrative (if accepted) requires post-Hijra setting (the captive-feeding requires post-Battle-of-Badr context for *asīr*). Western critical scholarship (Nöldeke, Bell) classifies Q 76 as **Middle Meccan** based on stylistic features: short rhythmic verses, single-rāwī monorhyme, eschatological tableau, no legal content. The empirical structural signature (4-axis structural tests on the corpus) tends toward the Nöldeke reading per `01-empirical-profile.md` §6.

## 7. ALR / muqaṭṭāʿat membership

Q 76 is **NOT a muqaṭṭaʿāt-opened surah** (no ALR / ALM / حم / etc. opener). It opens with a rhetorical question (`hal atā`) — a corpus-rare opening style.

## 8. FR-cohort

Q 76's nearest-12 FR-content neighbors (per `h-new-111.json`):
| Rank | Q | FR distance |
|:-:|:-:|:-:|
| 1 | Q 110 al-Naṣr | 0.6883 |
| 2 | Q 112 al-Ikhlāṣ | 0.6955 |
| 3 | Q 113 al-Falaq | 0.7067 |
| 4 | Q 106 Quraysh | 0.7070 |
| 5 | Q 1 al-Fātiḥa | 0.7092 |
| 6 | Q 96 al-ʿAlaq | 0.7112 |
| 7 | Q 107 al-Māʿūn | 0.7131 |
| 8 | Q 108 al-Kawthar | 0.7131 |
| 9 | Q 100 al-ʿĀdiyāt | 0.7161 |
| 10 | Q 105 al-Fīl | 0.7235 |
| 11 | Q 101 al-Qāriʿa | 0.7238 |
| 12 | Q 97 al-Qadr | 0.7256 |

Q 76's FR-content neighborhood is **the short-Mufaṣṣal terminal-block** (Q 96-114) plus Q 1 — the same "TERMINAL_TRIAD plus Q 1" cluster that participates in cross-finding-013's mushaf ring-topology closure. This places Q 76 in the corpus's compact-eschatology / single-rāwī / terminal-Mufaṣṣal FR cohort rather than in the long-Medinan or Late-Meccan apparatus zone.

Q 75 (mushaf-prev) is FR-rank #43 of 113 from Q 76's row at d = 0.8165, putting Q 75 outside Q 76's FR-close cohort despite being mushaf-adjacent and creation-axis-paired. **Q 76 is FR-paired with the short-Mufaṣṣal but mushaf-paired with Q 75 al-Qiyāma**. This dual-pairing is itself a structural signature.

## 9. Length classification

31 verses, 250 words — **mufaṣṣal-awsaṭ class** (between the short tail and the medium block, on the Mufaṣṣal-terminal-trajectory). Mean 8.06 words/verse — short-rhythmic register.

## 10. Mushaf-adjacency seam costs (per `h-new-720`)

| Pair | delta_raw | rank in expense |
|:--|:--:|:--:|
| Q 75 → Q 76 | +0.05179 | rank 66 / 113 |
| Q 76 → Q 77 | +0.08790 | rank 41 / 113 |

Both transitions are mid-rank in TSP-cost (neither in the universal-hinge top-15 nor in the clamped-zero seamless bottom-13). The Q 75 → Q 76 seam is structurally inexpensive — consistent with the creation-resurrection bracket reading.

## 11. Connection to existing project findings

- **cross-finding-013** (mushaf ring-topology): Q 76's FR-close cohort is the TERMINAL_TRIAD wraparound zone. Q 76 sits "off-ring" in the mushaf at position 76 but FR-clusters with the Q 110-114 wrap-around tail. This is a candidate for a "mushaf ring radius-extension" finding (queued — see `07-cross-references.md` §3).
- **cross-finding-022** (terminal Wave-5 synthesis): Q 76 is the highest-paradise-density anchor of the eschatology-meta-cluster spanning Q 78-83 (per H-NEW-1200). Q 76's CORPUS-EXACT-EXTREME density extends this cluster's empirical scope.
- **cross-finding-027** (iʿjāz al-takrīr architecture): Q 76's monorhyme + paradise-tableau structure is candidate-architecture for refrain-as-iʿjāz; queued for downstream comparison with Q 55 al-Raḥmān (H-NEW-1250) and Q 26 al-Shuʿarāʾ.

## 12. JOURNAL note (this specialist run, 2026-05-09)

All 4 SHA-locked tests PASS at α_bon = 0.0125 (Bonferroni-4):
- Q076-F-01: paradise-density CORPUS-EXACT-EXTREME
- Q076-F-02: monorhyme CORPUS-EXACT (longest 100%-alif)
- Q076-F-03: Q 75-76 creation-resurrection pair CONFIRMED
- Q076-F-04: Shīʿī Ahl-al-Bayt revelation-cause AUDIT-VERIFIED-NEGATIVE in Sunni canonical corpus + Friday-Fajr recitation CONFIRMED

H-NEW-1280 and H-NEW-1290 are queued for the master ledger.
