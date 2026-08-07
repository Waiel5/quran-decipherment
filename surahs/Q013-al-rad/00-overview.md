---
surah: 13
surah_name_ar: الرعد
surah_name_translit: al-Raʿd
surah_name_english: The Thunder
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: SCAFFOLD — full template built; 5 novel tests pre-registered + executed under Bonferroni-k=5
---

# Q 13 al-Raʿd — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 13 | canonical |
| Arabic name | الرعد | canonical |
| Transliteration | al-Raʿd | canonical |
| English meaning | "The Thunder" (named after Q 13:13 *yusabbiḥu al-raʿdu bi-ḥamdihi*) | classical |
| Verse count | 43 | Hafs-Kufan, `data/hafs-verse-counts.tsv` line 13 |
| Position in mushaf | 13 | canonical |
| **Type — CONTESTED** | **al-Suyūṭī: MEDINAN; Ibn ʿAbbās tradition: MECCAN; Nöldeke: Late Meccan #90** | `data/revelation-order.csv` Q13 row |
| Position in revelation order (al-Suyūṭī cataloging) | **96 / 114** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **90 / 114 (Late Meccan)** | `data/revelation-order.csv` |
| Word count (no-tashkeel) | **928** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel) | **3,545** | same |
| Mean words/verse | 21.58 | computed |
| **Opening** | **المر ۚ تلك آيات الكتاب ۗ والذي أنزل إليك من ربك الحق** — "ALMR. These are the verses of the Book; and that which has been sent down to you from your Lord is the truth." | muqaṭṭaʿāt + book-reference |
| Sajda verse | **Q 13:15** *wa-li-llāhi yasjudu man fī al-samāwāti wa-l-arḍi* (one of 14 *suwar al-sajda*) | classical |

## 2. ⭐ Corpus-unique structural property — the المر 4-letter muqaṭṭaʿ

**Q 13 is the ONLY surah in the Quran opening with the 4-letter muqaṭṭaʿ المر (alif-lām-mīm-rā).** This is corpus-unique:
- ALR (3-letter) cluster: Q 10, 11, 12, 14, 15 (5 surahs).
- ALM (3-letter) cluster: Q 2, 3, 29, 30, 31, 32 (6 surahs).
- ALMS (4-letter, alif-lām-mīm-ṣād): Q 7 only.
- **ALMR (4-letter, alif-lām-mīm-rā): Q 13 only.**

In the muqaṭṭaʿāt-letter-family lattice, Q 13's letter-set is **structurally between ALM and ALR** — sharing alif-lām-mīm with the ALM cluster and ending in rā (the unique letter of the ALR cluster). Mushaf-position 13 places Q 13 IMMEDIATELY adjacent to the ALR cluster (Q 10, 11, 12 precede; Q 14, 15 follow). Q 13's mushaf placement is **structurally a pivot between the ALR cluster and the rest of the corpus**.

This corpus-unique 4-letter combination is the empirical seed for the F-01 letter-family-lattice test (see `06-novel-findings.md` and `Q013-F-01-almr-lattice-position-prereg.md`).

## 3. Classical chronology — the contested Meccan-vs-Medinan question

The chronology of Q 13 is **classically contested**:

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (Meccan-Medinan classification)**: classifies Q 13 as **Medinan**, citing the asbāb al-nuzūl traditions (Ibn ʿAbbās via certain chains; Mujāhid; the connection of Q 13:43 to ʿAbd Allāh b. Salām, a Medinan Jewish convert).
- **Ibn ʿAbbās tradition (alt. chain) + Mujāhid + ʿIkrima**: Meccan classification is also reported in classical isnāds (al-Ṭabarī cites both positions; al-Qurṭubī summarizes the dispute).
- **Nöldeke (*Geschichte des Qorâns*, vol. 1)**: classifies Q 13 as **Late Meccan**, position 90 in the chronological ordering (`data/revelation-order.csv` `noldeke_phase = Late Meccan`).
- **Stylistic markers** (used by both classical and modern scholars): muqaṭṭaʿāt opener (more typically Meccan), short rhythmic style of vv. 1-15 (Meccan signature), longer more-prosaic style of vv. 28-43 (more Medinan-feel). The surah may itself be a **chronologically-mixed surah** (some verses Meccan, others Medinan inserted), per al-Suyūṭī's *Itqān* nawʿ on chronologically-mixed surahs.

**This contested status makes Q 13 the natural test-case for the Q 5 specialist's chronology-architecture-dissociation finding.** The Q 5 specialist (`Q005-F-05`) demonstrated that Q 5 is architecturally a Q 2-twin (early-Medinan-ṭiwāl head cluster) DESPITE being chronologically late-Medinan. Q 13's contested chronology is exactly the kind of test-case where the dissociation framework should make a clear empirical prediction REGARDLESS of which chronology is "correct" — Q 13's architectural signature is fixed by its mushaf position + length + content-vocabulary, not by the chronology debate. See F-03 and F-05 below for tests.

## 4. Length classification

43 verses, 928 words — short-medium (al-mufaṣṣal-ṭiwāl boundary OR short-prophet-narrative-class). Q 13 sits at mushaf-position 13, in the head-mushaf zone (pre-Hijra-kink at s=50). Per H-NEW-660: predicted d̄_content ≈ 0.96 (head-cohort plateau); observed = 0.964 (`h-new-750.json` `mean_content_distance`). **Spot-on prediction.**

## 5. Rhyme structure

Final-letter distribution across 42 verses with letter-final endings (Q 13:15 is a sajda-verse ending with marker ۩ and is excluded from rāwī count):

| Final letter | Count | % |
|:--:|:--:|:--:|
| **ب (bāʾ)** | **15** | **35.7% — top rāwī** |
| ر (rāʾ) | 8 | 19.0% |
| ل (lām) | 6 | 14.3% |
| ن (nūn) | 5 | 11.9% |
| د (dāl) | 4 | 9.5% |
| ق (qāf) | 3 | 7.1% |
| ع (ʿayn) | 1 | 2.4% |
| (sajda ۩) | 1 | (Q 13:15 excluded) |

**Rhyme entropy (Shannon, nats): 1.7164** — multi-rāwī mixed-rhyme structure (NOT monorhyme). Top-rāwī ب only 35.7% (Q 12 by contrast: ن at 84%; near-monorhyme). This places Q 13 in the **rhyme-diverse mufaṣṣal-pole** of the rhyme-architecture (H-NEW-750 reports `z_rhyme_entropy = 1.72` — well above corpus mean).

The bāʾ-rāwī predominance (in *aḥsana / hisāb / iqāb / al-ʿiqāb* class endings) is consistent with the surah's didactic-cosmological theme (signs, accounts, recompense). The ر, ل, ن secondary rāwīs are common Quranic alternates.

## 6. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **21/114** (mid-pack; not in top-10 like Q 12).
- **Outlier-strength** Δ_pct: **−3.85 pp**, classification **NULL** in window {Q 10–16} (`h-new-590.json` X=13). Q 13 is **NOT a content outlier** vs its mushaf-window — i.e. its content profile is similar to its prophet-narrative-cluster neighbours.
- **iʿjāz sig_A**: +1.323 (rank **19/114** — moderate-high). Q 13 is **structurally iʿjāz-positive** (high local cohesion + moderate content-distinctiveness + high rhyme entropy).
- **Mean FR-content distance**: 0.964 (corpus mean 0.95) — close to corpus-typical.
- **Q 12→Q 13 canonical-adjacency cost**: 0.2158 (rank ≈ 11/113 — top-15 expensive). The Yūsuf→Raʿd seam is structurally costly because of the letter-family-shift (ALR → ALMR) and content-shift (continuous-narrative → didactic-cosmological).
- **Q 13→Q 14 canonical-adjacency cost**: 0.0497 (very low; rank ≈ bottom-quartile). The Raʿd→Ibrāhīm seam is **near-free** despite letter-family difference (ALMR → ALR) — because of FR-content proximity (Q 13's FR-nearest non-self surah is Q 14 at 0.784 — the closest pair containing Q 13).

## 7. Quick content structure

Q 13 is a 43-verse didactic-cosmological-eschatological surah, NOT a continuous narrative:

- vv. 1: opening (المر + book-reference *tilka āyātu al-kitāb*).
- vv. 2-4: signs of creation (heavens raised without pillars; sun and moon; earth's mountains, rivers, fruits-in-pairs).
- vv. 5-11: theological assertion + polemic against deniers; *muqaqqibāt* (succeeding angels) verse 11 (*lā yughayyiru mā bi-qawmin ḥattā yughayyirū mā bi-anfusihim*).
- vv. 12-15: cosmic phenomena — lightning, thunder (*yusabbiḥu al-raʿdu bi-ḥamdihi*), prostration (Q 13:15 sajda).
- vv. 16-18: monotheist polemic; the parable of foam and pure water.
- vv. 19-24: the believers' rewards (Gardens of ʿAdn, *al-rāsikhūna fī al-ʿilm* type virtues).
- vv. 25-26: the deniers' fate.
- vv. 27-29: argument with deniers; **Q 13:28 — *alā bi-dhikri Allāhi taṭmaʾinnu al-qulūb* (the hearts-at-rest verse)**.
- vv. 30-32: messenger-prophetic theology.
- vv. 31: **Q 13:31 — *wa-law anna qurʾānan suyyirat bihi al-jibāl* (the iʿjāz-singular verse: "if there were any Qurʾān by which mountains could be moved...")** — a classical anchor for al-Bāqillānī's *iʿjāz* argument.
- vv. 33-37: divine sovereignty, knowledge.
- vv. 38-42: prophet-history and divine justice; God's plan does not fail.
- v. 43: **Q 13:43 — *qul kafā bi-llāhi shahīdan baynī wa-baynakum wa-man ʿindahu ʿilm al-kitāb*** (the *ʿilm al-kitāb* verse, traditionally connected to ʿAbd Allāh b. Salām via Tirmidhī #3340/#3900).

The surah is a **mini-corpus theological microcosm**: cosmology + polemic + parable + believers' reward + deniers' fate + theology of revelation + iʿjāz declaration + ʿilm-of-the-book closure. This polythematic structure is what makes the chronology debate sharp — different sections feel Meccan or Medinan to different classical scholars.

## 8. Connection to Wave-A/B per-surah findings

- **Q 13:13 thunder-praises-God** is referenced in `data/literature/classical-tafsir/classical-on-rad-verse-28.md` for Q 13:28 palindromic-root structure (a previously-identified empirical signature — the *highest length-normalized jinas-density verse* in the corpus at 0.889).
- Q 13 is mentioned in `Q005-al-maida/06-novel-findings.md` Q005-F-04: Q 13 has 8 covenant tokens / 928 words = 0.86/100w covenant-density (corpus rank 4) — outranks Q 5 al-Māʾida on covenant-density per word despite the smaller text.
- Q 13's 4-letter muqaṭṭaʿ has been **omitted as a separate cluster** in prior letter-family work (H-NEW-610 tested ALR-5, ALM-6, ḤM-7, full-29 — Q 13 fell into the "full-29" cluster but was NOT given its own letter-cluster because it's a singleton). This is the empirical motivation for F-01: is Q 13's content position in the lattice closer to ALM, ALR, or BETWEEN them?

## 9. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md (UAS rank 21; FR-nearest Q 14 at 0.784; outlier NULL; sig_A rank 19/114)
- [x] 02-content-analysis.md (8-section thematic structure; thunder-praise / hearts-at-rest / iʿjāz-singular triplet of marquee verses)
- [x] 03-tafsir-survey.md (≥ 5 mufassirūn surveyed: al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī, al-Biqāʿī, al-Zamakhsharī)
- [x] 04-hadith-corpus.md (key citations: Tirmidhī #3340/#3900 *ʿilm al-kitāb* / ʿAbd Allāh b. Salām; Bukhārī tasbīḥ-bi-ḥamdihi #6438/#7563/#6406; al-muqaqqibāt traditions)
- [x] 05-classical-claims-audit.md (5+ claims: chronology debate, ALMR-uniqueness, *iʿjāz al-fawāṣil*, raʿd-tasbīḥ corpus-unique, Q 13:28 palindrome, Q 13:43 ʿAbd Allāh b. Salām)
- [x] 06-novel-findings.md (Q013-F-01 through F-05, all SHA-locked, Bonferroni-k=5, α_bon=0.01)
- [x] 07-cross-references.md (Q12-Q13-Q14 seams; ALMR vs ALR vs ALM; chronology-architecture-dissociation framework anchor)
- [x] JOURNAL.md (run log, SHA hashes, decision points)
