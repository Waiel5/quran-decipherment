---
surah: 32
surah_name_ar: السجدة
surah_name_translit: al-Sajda
surah_name_english: The Prostration
file_type: overview
date_last_updated: 2026-05-10
phase: B+
verdict: SCAFFOLD — full 8-file template built; 6 novel tests pre-registered (3 pre-existing F-01/F-02/F-03 + 3 brief-mandated F-04/F-05/F-06)
---

# Q 32 al-Sajda — Overview

> The prior single-file deep-dive lives at `00-overview-comprehensive.md`. This file is the 8-file-template canonical overview, integrating the original three tests + the three brief-mandated tests (F-04 ALM-4, F-05 Friday-fajr + al-Munjiya, F-06 Q 32:15 ↔ Q 41:38).

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 32 | mushaf canonical |
| Arabic name | السجدة | `quran-text/quran-no-tashkeel.json[31]` |
| Transliteration | al-Sajda | standard |
| English meaning | "The Prostration" (named for Q 32:15 sajda-verse) | classical |
| Verse count | 30 | `data/hafs-verse-counts.tsv` line 32 (Hafs-Kufan) |
| Position in mushaf | 32 | canonical |
| Type | **Meccan** (late) | al-Suyūṭī, *al-Itqān*, nawʿ 1; `data/revelation-order.csv` row Q32 |
| Position in revelation order (al-Suyūṭī / Tanzil) | **75 / 114** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **70** (Late Meccan, by convention) | `data/revelation-order.csv` |
| Word count (no-tashkeel) | **378** | computed from `quran-text/quran-no-tashkeel.json` |
| Mean words/verse | 12.6 | computed |
| **Opening** | **الم ۚ تنزيل الكتاب لا ريب فيه من رب العالمين** — "ALM. The revelation of the Book in which there is no doubt is from the Lord of the worlds." | muqaṭṭaʿāt (ALM-3-letter) + tanzīl-opener |
| Sajda verse | **Q 32:15** *innamā yuʾminu bi-āyātinā alladhīna idhā dhukkirū bihā kharrū sujjadan wa-sabbaḥū bi-ḥamdi rabbihim wa-hum lā yastakbirūn* (one of 14 *suwar al-sajda*) | al-Suyūṭī, *al-Itqān*, nawʿ 30; al-Bukhārī *Kitāb sujūd al-Qurʾān* |

## 2. ⭐ Corpus-architectural signature

Q 32 occupies three distinguished positions in the corpus's empirical architecture:

1. **al-Munjiya nightly liturgy anchor.** Per al-Tirmidhī *Sunan* (project idInBook 2975): the Prophet would not sleep without reciting Q 32 (Sajda) and Q 67 (Mulk). FR(Q 32, Q 67) = **0.7534** — below corpus mean (0.9235) by 0.81σ; one of the 6 liturgical pairs in cross-finding-028.

2. **Friday-fajr liturgy anchor.** Per al-Bukhārī *Ṣaḥīḥ* (idInBook 870, replicated 1037): the Prophet recited Q 32 + Q 76 in Friday-fajr. FR(Q 32, Q 76) = **0.8395** — below corpus mean by 0.40σ. Q 32 is the only surah in the corpus dual-paired in both a nightly and a Friday-fajr liturgy.

3. **ALM-cluster terminus + structural-break anchor.** Q 32 is the last of the 4 mid-Meccan ALM-openers in mushaf order. The Q 32 → Q 33 canonical-adjacency cost δ = **0.3631** is rank-3 among 113 corpus adjacencies (h-new-720), one of the corpus's three most-expensive seams (after Q 1→Q 2 and Q 32→Q 33 itself).

These three signatures are pre-existing project findings, integrated here.

## 3. ALM-opener cluster context

Q 32 is one of 6 corpus surahs opening with the 3-letter muqaṭṭaʿ ALM (alif-lām-mīm): {Q 2, 3, 29, 30, 31, 32}.

- Medinan ALM subset: {Q 2, Q 3} (per al-Suyūṭī chronology; revelation orders 87, 89).
- Mid-Meccan ALM subset: {Q 29, Q 30, Q 31, Q 32} (revelation orders 85, 84, 57, 75).

The ALM-6 cluster was tested for FR-cohesion in Q030-F-08 and returned PARTIAL (uniform NULL p=0.418; length-matched PASS p=0.0225). This pre-reg's Q032-F-04 tests the ALM-4 mid-Meccan sub-cluster (excluding Q 2, Q 3) for whether the chronologically-tighter subset is FR-tighter. **Result: ALM-4 also returns NULL on both uniform (p=0.366) and length-matched (p=0.126) cells; T_obs = 0.916 vs corpus mean 0.924.** The ALM-axis is confirmed-NOT-FR-cohesive at sub-set granularity, REPLICATING cross-finding-025's marker-thickness rule on a fourth muqaṭṭaʿāt-sub-cluster (after ALR-5, ALM-6, ḤM-7, full-29 all NULL).

## 4. Length classification

30 verses, 378 words — **mufaṣṣal-ṭiwāl / awsāṭ boundary** per al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*. Q 32 sits at mushaf-position 32, below the s=50 Hijra-kink in the compression-tail law. Per H-NEW-660: predicted d̄_content ≈ 0.96 (head-cohort plateau); observed = **0.889** (`h-new-750.json`). Q 32 sits modestly below the head-plateau — slightly more cohesive than the typical head-mushaf surah.

## 5. Rhyme structure

Final-letter distribution across 30 verses (sajda-verse Q 32:15 retains its rāwī despite the ۩ marker):

| Final letter | Approx % | Note |
|:--:|:--:|:--|
| ن (nūn) | **~90%** | top rāwī — monorhyme regime |
| Other | ~10% | minor variants |

**Rhyme entropy (Shannon, nats): 0.389** — z = −0.690 (`h-new-750.json`); near-monorhyme. Q 32 is in the **rhyme-monolithic** pole of the rhyme-architecture, distinct from Q 13's multi-rāwī mufaṣṣal-pole.

## 6. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: 27/114 (top-quartile; structural-iʿjāz of moderate strength).
- **Outlier-strength** Δ_pct: −1.36 pp, classification **NULL** in window {Q 29-35} (`h-new-590.json`). Q 32 is NOT a content outlier vs its mushaf-window.
- **iʿjāz sig_A**: −0.350 (rank 70) — slight theological-iʿjāz lean.
- **iʿjāz sig_B**: −1.322 (rank 95) — rhyme-axis suppressed (consequence of ن-monorhyme).
- **Mean FR-content distance**: 0.889 (below corpus mean 0.923).
- **Q 31→Q 32 canonical-adjacency cost**: 0.1005 (mid-pack).
- **Q 32→Q 33 canonical-adjacency cost**: **0.3631** (rank-3 corpus-wide; 4.4% of L_mushaf) — TOP-3 expensive seam.

## 7. Quick content structure

Q 32 is structured as a 4-part theological-narrative arc (per al-Biqāʿī, *Naẓm al-Durar*):

- **vv. 1-3**: ALM opening + claim that the Book is *tanzīl from the Lord of the worlds*. The opening conspicuously omits an explicit *bayān* of *al-kitāb* compared to Q 2:2, Q 3:3, Q 31:2 ("ALM-exception" feature — Q030-F-08 Cell B-uniform context).
- **vv. 4-9**: Cosmological-creation block — six-day creation, seven heavens, hierarchy of command (*yudabbiru al-amr*), creation of humans from clay then sperm-drop, hearing/sight/hearts.
- **vv. 10-22**: Eschatological + behavioral — the unbeliever's death-bed regret; the believer's prostration (Q 32:15); the warning of the *yawm al-faṣl*; the contrast of believers/unbelievers; chastisement-warning.
- **vv. 23-30**: Mūsā parallel — the Book given to Mūsā, the imāms among the Banū Isrāʾīl, then return to local Mecca-Medina warning + *waiting* injunction.

Content register: **eschatological-creedal** with prophetic-historical anchor. Vocabulary clusters with late-Meccan ālāʾ-cluster Q 27, Q 28, Q 29, Q 30, Q 31.

## 8. The sajda-verse Q 32:15

Q 32:15: *إنما يؤمن بآياتنا الذين إذا ذكروا بها خروا سجدا وسبحوا بحمد ربهم وهم لا يستكبرون*

"Only those believe in Our verses who, when they are reminded by them, fall down in prostration and exalt with praise of their Lord, and they are not arrogant."

Per the Q032-F-01 finding (DIRECTIONAL 1/3), Q 32:15 is a **behavioral-prostration** sajda, distinct from the **cosmic-roll-call** cluster {Q 13:15, Q 16:50, Q 22:18}. Per Q032-F-06 (PARTIAL, rank 10/91), Q 32:15 is the **5th-ranked** pair-partner of the 14 sajda-verses when paired with the cosmic-but-not-purely-roll-call verse Q 41:38 — top-quintile but not strict top-5. Q 32:15 sits in a **behavioral / didactic** sajda-sub-class.

Per Q013-F-08 (Q 13:15 sajda-block-boundary test) the cosmic-roll-call sajda at Q 13:15 does NOT sit at a local content-discontinuity within its host surah; the within-surah-boundary typology is therefore NOT a universal sajda-verse feature.

## 9. Connection to Wave-A/B per-surah findings

- **cross-finding-028** (liturgical-pair FR-cohesion): Q 32 features in 2 of 6 pairs (P2 with Q 76, P6 with Q 67). The brief-mandated Q032-F-05 replicates both pairs at individual-pair scale (Cell A and B z-scores -0.40 and -0.81 respectively; both directional but neither beats the strict 1σ threshold; joint Cell C p_perm = 0.024).
- **Q030-F-08** (ALM-6 cohesion PARTIAL): Q032-F-04 sub-tests ALM-4 mid-Meccan (NULL both cells), confirming the marker-thickness rule.
- **Q022-F-01** (sajda-cosmic clustering VINDICATED for Q 22:18): Q032-F-01 finds Q 32:15 is *behavioral-cluster representative*, NOT cosmic-cluster (DIRECTIONAL 1/3). The sajda-typology refinement is the project's first separation of cosmic vs behavioral sajda-sub-types.

## 10. Investigation status

- [x] 00-overview.md (this file)
- [x] 00-overview-comprehensive.md (prior single-file deep-dive; preserved)
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md (Q032-F-01..F-06; 6 SHA-locked pre-regs; 3 DIRECTIONAL/PARTIAL; 3 NULL)
- [x] 07-cross-references.md
- [x] JOURNAL.md
