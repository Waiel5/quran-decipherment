---
surah: 3
surah_name_ar: آل عمران
surah_name_translit: Āl ʿImrān
surah_name_english: "The Family of ʿImrān"
file_type: overview
date_last_updated: 2026-05-29
phase: B+
verdict: 1 pre-registered 3-arm test landed — Arm A CONFIRMED ({2-5} smoothest block) + Arm B CONFIRMED (Q3 cohesion anchor) + Arm C NULL (block-smoothness not beyond chance multiplicity)
---

# Q 3 Āl ʿImrān — Overview


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
| Surah ID | 3 | canonical |
| Arabic name | آل عمران | canonical (the family/house of ʿImrān, father of Maryam; from v 33 *āl ʿImrān*) |
| Transliteration | Āl ʿImrān | canonical |
| English meaning | "The Family of ʿImrān" | classical |
| Verse count | 200 | Hafs-Kūfan (`data/hafs-verse-counts.tsv` line 3); al-Zamakhsharī "وهي مائتا آية" |
| Position in mushaf | 3 | canonical |
| Revelation order | #89 (Tanzil Egyptian Standard); Nöldeke #97 | `data/revelation-order.csv` |
| Type | Medinan (مدنية) | al-Zamakhsharī header; Ibn Kathīr ("the first 83 āyāt relate to the Najrān delegation, Hijra year 9") |
| Word count (no-tashkeel, marks stripped) | 3,501 | computed (`scripts/Q003_F_01_tiwal_block.py` pipeline) |
| Letter count (no-tashkeel) | 14,985 | computed |
| Distinct QAC roots | 439 (2,274 root-tokens) | `data/morphology/root-index.json` |
| Opening | الم — *alif-lām-mīm* (muqaṭṭaʿāt) → الله لا إله إلا هو الحي القيوم (v 2) | muqaṭṭaʿāt + creedal |
| Predominant rhyme (rāwī) | ن (nūn), 60.9% (120/197 rhyme-bearing verses) | `h-new-700.json` rhyme_letter_diagnostics |
| Length class | al-sabʿ al-ṭiwāl ("the seven long ones") | al-Suyūṭī *al-Itqān* |

## 2. Why Q 3 matters for the project

1. **The single smoothest contiguous 4-surah block in the muṣḥaf.** The al-sabʿ-al-ṭiwāl head-run
   {Q2, Q3, Q4, Q5} has mean internal TSP-residual seam **−0.03196** — **rank 1/111** among all contiguous
   4-surah blocks (Q003-F-01 Arm A, CONFIRMED). The top three smoothest 4-blocks are all overlapping windows
   inside al-ṭiwāl ({2-5}, {4-7}, {3-6}). Q 3 is the *interior* hinge of this maximally-seamless run.

2. **A content-cohesion ANCHOR, not an outlier.** In H-NEW-590, removing Q 3 from its {Q1-Q7} window
   *raises* the window's dispersion (delta_pct = **−15.28**, classification **COHESION_ANCHOR**) — Q 3 binds
   the long-surah head together (Q003-F-01 Arm B, CONFIRMED). Only Q 4 al-Nisāʾ among the long surahs is a
   (weak) outlier; Q 3 is the most cohesion-binding of the al-ṭiwāl head after the corpus-singletons.

3. **An honest NULL on the statistical surprise of the block.** Q003-F-01 Arm C is a **NULL**: a max-statistic
   permutation null (10,000 random re-arrangements of the 113 seam values, recording the smoothest 4-block
   each time) finds a block at least as smooth as {2-5} in **12.3%** of random arrangements (p_perm = 0.12319).
   The corpus has many negative (seamless) seams, so a smoothest-block this smooth is NOT by itself beyond
   chance once block-multiplicity is controlled. The block's GLOBAL-minimum status (Arm A) is a deterministic
   fact; its statistical *surprise* (Arm C) is not. Published with full prominence per PRE-REG-STANDARD-04.

4. **FR-nearest to al-Baqara.** Q 3's nearest Fisher-Rao neighbour is Q 2 al-Baqara at FR **0.6309** — the
   second-closest surah-pair in the entire corpus's long-surah space. This is the empirical correlate of the
   classical *al-Zahrāwān* pairing (al-Baqara + Āl ʿImrān as "the two luminous ones," Muslim #1766).

5. **The muḥkam / mutashābih locus.** Q 3:7 (*minhu āyātun muḥkamātun hunna umm al-kitāb wa-ukharu
   mutashābihāt*) is the Qurʾān's own self-description of its verse-typology — the foundational proof-text for
   the entire ʿulūm-al-Qurʾān discipline of muḥkam/mutashābih (al-Ṭabarī, al-Zamakhsharī, al-Qurṭubī all treat
   it at length; al-Bukhārī #4547, Muslim on ʿĀʾisha's "iḥdharūhum" ḥadīth).

6. **The Greatest-Name (al-ism al-aʿẓam) bridge to al-Baqara.** Q 3:1-2 (*alif-lām-mīm — Allāhu lā ilāha
   illā huwa al-ḥayy al-qayyūm*) carries the divine *al-Ḥayy al-Qayyūm* formula that Tirmidhī #3562
   (**ḥasan ṣaḥīḥ**) and Abū Dāwūd #1497 identify with Āyat al-Kursī (Q 2:255) as the locus of Allāh's
   Greatest Name — a verbatim creedal bridge between the two *Zahrāwān*.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 1.0943 (well above corpus mean 0.9235 — a long-surah is FR-distant) | `h-new-111.json` (Q3 row) |
| Nearest FR neighbour | **Q 2 al-Baqara** at FR 0.6309 | `h-new-111.json` |
| Top FR neighbours | Q 2 (0.631), Q 5 (0.698), Q 4 (0.793), Q 8 (0.807), Q 6 (0.822) | `h-new-111.json` |
| Q 2 → Q 3 seam | delta_raw = +0.01646, rank 20/113 (smooth) | `h-new-720.json` |
| Q 3 → Q 4 seam | delta_raw = −0.04662, rank 4/113 (**seamless**) | `h-new-720.json` |
| H-NEW-590 | delta_pct = **−15.28**, **COHESION_ANCHOR** | `h-new-590.json` |
| H-NEW-700 rhyme | ن (nūn), 60.9% | `h-new-700.json` |
| H-NEW-750 sig_A | −0.8179 (rank 84/114) | `h-new-750.json` |
| H-NEW-750 sig_B | +0.4281 (rank 45/114) | `h-new-750.json` |
| H-NEW-750 z_mean_content_distance | +1.685 (FR-distant) | `h-new-750.json` |
| H-NEW-840 UAS | +0.4517 (rank 37/114) | `h-new-840.json` |

## 4. Surface structure (major blocks)

| Block | Verses | Function |
|---|---|---|
| Muqaṭṭaʿāt + creed (*al-Ḥayy al-Qayyūm*; the Book confirms prior scripture) | 1-9 | creedal opening; muḥkam/mutashābih (v 7) |
| The supplication of the steadfast (*rabbanā lā tuzigh qulūbanā*) | 8-9 | creedal du'āʾ |
| Polemic vs those who disbelieve; Badr allusion | 10-13 | warning |
| The love of desires vs what is with God; the patient/truthful | 14-17 | wisdom |
| God's witness to His oneness; *inna al-dīna ʿinda Allāh al-islām* | 18-20 | creed |
| People of the Book polemic; Āl ʿImrān / Maryam / Zakariyyā / Yaḥyā narrative | 21-63 | narrative (the surah's name-block) |
| ʿĪsā, the mubāhala (v 61), and the call to the common word | 61-64 | the Najrān-delegation core |
| People-of-the-Book argument; Ibrāhīm as ḥanīf; the Kaʿba (Bakka, v 96) | 64-99 | polemic + qibla |
| The believing community charge; holding to the rope of God | 100-115 | exhortation |
| The Uḥud battle pericope (the long central narrative) | 121-179 | narrative (the defeat at Uḥud) |
| Closing exhortations; *ūlū al-albāb*; the running creed (vv 190-194) | 180-200 | wisdom + du'āʾ + the *ribāṭ* close |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q003-F-01 Arm A | **CONFIRMED** | {Q2,Q3,Q4,Q5} is the rank-1/111 smoothest contiguous 4-surah block in the muṣḥaf (mean seam −0.032); top-3 smoothest blocks all overlap al-ṭiwāl |
| Q003-F-01 Arm B | **CONFIRMED** | Q 3 is a COHESION_ANCHOR of its {Q1-7} window (delta_pct −15.28) — it binds the long-surah head |
| Q003-F-01 Arm C | **NULL** | the {2-5} block smoothness is reproducible by 12.3% of random seam-arrangements (p=0.123) — the block's GLOBAL-min status is deterministic, but not statistically surprising once 111-block multiplicity is controlled |

## 6. Cross-references

- **Q 2 al-Baqara** — FR-nearest neighbour (0.631); the *Zahrāwān* pair (Muslim #1766); the al-ism-al-aʿẓam
  bridge (Q 2:255 ↔ Q 3:2; Tirmidhī #3562); Q 2→Q 3 seam rank 20/113.
- **Q 4 al-Nisāʾ** — Q 3→Q 4 seamless seam (rank 4/113); the two together form half the al-ṭiwāl head; both
  Medinan legal-creedal; the Q4 inheritance law (Q4:11) follows the Q3 wisdom-and-warfare close.
- **H-NEW-720** — {2,3,4,5} rank-1 smoothest 4-block; Q 3→Q 4 rank-4 seamless seam.
- **H-NEW-590** — Q 3 COHESION_ANCHOR of {1-7}.
- **al-Suyūṭī / al-Zarkashī** — al-sabʿ al-ṭiwāl block; muḥkam/mutashābih (*al-Itqān*, *al-Burhān*).

## 7. Classical-tradition status (see `03-tafsir-survey.md`, `05-classical-claims-audit.md`)

- al-Ṭabarī (*Jāmiʿ al-bayān*): muḥkam = the clear, decisive verses (ḥalāl/ḥarām, etc.); umm al-kitāb = the
  bulk and refuge of the Book; mutashābih = the verses whose meaning admits multiplicity.
- al-Zamakhsharī (*al-Kashshāf*): Medinan, 200 āyāt; full grammatical treatment of the *mīm* of *alif-lām-mīm*;
  al-furqān as the genus of revealed Books.
- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*): the muqaṭṭaʿāt as God's secret (al-Shaʿbī, al-Thawrī); the ʿĀʾisha
  ḥadīth (Muslim) on the *zaygh*-hearted who follow the mutashābih.
- Ibn Kathīr (*Tafsīr al-ʿaẓīm*): the first 83 āyāt = the Najrān-delegation occasion; al-Ḥayy al-Qayyūm =
  the Greatest Name (cross-ref Āyat al-Kursī).
- al-Bāqillānī (iʿjāz al-fawāṣil): Q 3 sig_A rank 84/114 — a long legal-narrative surah is structurally
  mid-low on the fawāṣil-variety axis (its rhyme entropy is *above* average, but its FR-content-distance
  z=+1.69 dominates the signature downward).

## 8. Open questions / queued tests

- Q003-F-02 (queued): the Uḥud pericope (vv 121-179) — is it the corpus's longest single battle-narrative
  block by root-token count, and does it carry a within-surah FR-density signature distinct from the
  creedal/polemic blocks?
- Q003-F-03 (queued): the *rabbanā* du'āʾ-refrain (vv 8, 16, 53, 147, 191-194) — is Āl ʿImrān the corpus's
  densest *rabbanā*-vocative supplication surah?
- Q003-F-04 (queued): the al-ism-al-aʿẓam bridge — is the *al-Ḥayy al-Qayyūm* bigram a corpus-rare collocation
  (Q 2:255, Q 3:2, Q 20:111 only)?

---

*Investigation: Wave (2026-05-29) Q 3 Āl ʿImrān full 8-file deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for Q003-F-01 detail; 04-hadith-corpus.md for verified faḍāʾil + Najrān + ism-al-aʿẓam chains.*
