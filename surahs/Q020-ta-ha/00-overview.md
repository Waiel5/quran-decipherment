---
surah: 20
surah_name_ar: طه
surah_name_translit: Ṭā-Hā
surah_name_english: "Ṭā-Hā"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 6 pre-registered tests landed — F-05 CONFIRMED (v14 divine-self-reference corpus-MAX-in-surah) + F-06 CONFIRMED (Ṭā-Hā burning-bush prototype, z=+5.81) + F-01/F-02/F-03/F-04 NULL
---

# Q 20 Ṭā-Hā — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 20 | canonical |
| Arabic name | طه | canonical (the muqaṭṭaʿāt opener Ṭā-Hā, v 1) |
| Transliteration | Ṭā-Hā | canonical |
| English meaning | "Ṭā-Hā" (the two disjoined letters; no consensus gloss — see §3 and `03-tafsir-survey.md`) | classical |
| Verse count | 135 | Hafs-Kufan (`data/hafs-verse-counts.tsv` line 20: "20 135") |
| Position in mushaf | 20 | canonical |
| Revelation order | #45 (Tanzil Egyptian Standard); Middle Meccan | `data/revelation-order.csv` (line 46: "45,20,طه,Ta-Ha,Meccan,55,Middle Meccan") |
| Type | Meccan (Middle Meccan) | `data/revelation-order.csv` |
| Word count (no-tashkeel, marks stripped) | 1,356 | computed (`scripts/Q020_F_06_musa_hub.py` tokenizer pipeline) |
| Letter count (no-tashkeel, marks stripped) | 5,402 | computed |
| Distinct QAC roots | 324 (837 root-tokens) | `data/morphology/root-index.json` |
| Opening | طه — muqaṭṭaʿāt (two-letter set) | the two-letter muqaṭṭaʿ family {Q 20 ṬH, Q 27 ṬS, Q 36 YS} |
| Predominant rhyme (rāwī) | ى / ي (yāʾ / alif-maqṣūra), **79.3%** of verses | `h-new-700.json` rhyme_letter_diagnostics; `h-new-750.json` |
| Length class | mufaṣṣal-ṭiwāl boundary / long Meccan narrative (135 vv) | al-Zarkashī mufaṣṣal-3-tier (the long-Meccan tier, not al-sabʿ al-ṭiwāl) |

## 2. Why Q 20 matters for the project

1. **The burning-bush prototype of the Mūsā cycle (Q020-F-06, CONFIRMED).** Q 20:9-36 is the longest and
   most detailed of the four H-NEW-2260 Mūsā burning-bush pericopes. It carries **5 of the 6 H-NEW-2260
   episode-signature roots** (`byD` white-hand, `ESw` staff, `Ans` perceived-fire, `Twy` the valley Ṭuwā,
   `*hb` "go [to Pharaoh]" — missing only `dbr`), the **maximum of the cycle**, and its **hub-strength**
   (mean root-Jaccard to the other three retellings Q 27:7-14 / Q 28:29-35 / Q 79:15-26) is
   H = 0.2340 vs a length-matched random-pericope null of 0.1123 — **z = +5.81, p_perm = 0.0001**. The
   Ṭā-Hā pericope is a genuine lexical hub of the conserved-vocabulary Mūsā cycle, directly extending
   H-NEW-2260 (Mūsā PASS, z = +3.34) to the per-pericope, Q-20-anchored level. (Honest MW-7 note: Q 20 is
   the cycle's **#2** hub-strength member, just behind Q 28:29-35 at 0.2549 — see `06-novel-findings.md`.)

2. **The corpus's densest single-verse divine self-affirmation (Q020-F-05, CONFIRMED).** Q 20:14
   *innanī anā Allāhu lā ilāha illā anā fa-ʿbudnī wa-aqim al-ṣalāta li-dhikrī* is the **rank-1 of 135**
   verses in Q 20 by divine-name + 1sg-divine-pronoun density (density 0.5455, 6/11 tokens; permutation
   **p = 0.0015**, seed 20260507). This is the verse classically named in the ʿUmar-conversion narrative
   (al-Bayhaqī *Dalāʾil al-nubuwwa*; al-Suyūṭī *al-Durr al-manthūr* on Q 20:1). The verse-location
   pre-naming has measurable empirical content (it is circumstantially consistent with, not proof of, the
   ḥadīth).

3. **A strong yāʾ-monorhyme over 135 verses.** Q 20's top final-letter ى/ي covers **79.3%** of its
   verses (`h-new-750.json`) — one of the highest single-rāwī fractions among the long narrative surahs.
   The whole Mūsā narrative is carried on a sustained *-ā / -á* (alif-maqṣūra) rhyme. Yet its iʿjāz
   signature sig_A = −1.51 (rank 92/114) is LOW: a tight monorhyme over many verses yields *low* rhyme
   entropy (0.574 nats, z = −0.35), so on the al-Bāqillānī *iʿjāz al-fawāṣil* axis Q 20 scores below
   average — the monorhyme is uniform, not varied. (Structural-iʿjāz ≠ monorhyme; see `01-empirical-profile.md`.)

4. **Content-divergent, but NOT a dispersion outlier.** Q 20's mean content-distance to all other surahs
   is **1.0403** (rank 99/114 ascending — i.e. one of the most content-distant surahs from the corpus
   centroid), driven by its dense, episode-specific Mūsā narrative lexicon. But removing it from its
   {Q 17-23} window changes the window dispersion only weakly (delta_pct = +5.52, p = 0.48, WEAK_OUTLIER,
   NULL by significance; `h-new-590.json`): Q 20 sits inside the long-Meccan-narrative neighborhood
   (its FR nearest neighbors are Q 23, Q 7, Q 51, Q 41, Q 43 — see §3).

5. **The two-letter muqaṭṭaʿ family member that does NOT form a multi-axis cluster (Q020-F-03, NULL).**
   The two-letter-opener trio {Q 20 ṬH, Q 27 ṬS, Q 36 YS} is **not** tighter than random-3 on any of four
   axes (FR-distance, sig_A spread, rhyme-letter consensus, mean_d rank-spread) — 0/4 pass. This is a
   fifth independent confirmation of the project's muqaṭṭaʿāt content-orthogonality law: the letter-axis
   is ⊥ the content/rhyme/iʿjāz axes (al-Suyūṭī's epistemic humility on the disjoined letters, *al-Itqān*
   nawʿ 40, VINDICATED at the two-letter sub-level).

6. **The Mūsā-narrative-purity NULL (Q020-F-01).** Q 20 is **rank 2/114** (not the maximum) on
   Mūsā-narrative-marker verse-fraction (0.2296), behind Q 28 al-Qaṣaṣ (0.2614). A clean NULL against the
   locked "corpus-MAX AND ≥0.55" threshold — the most Mūsā-saturated surah by verse-fraction is al-Qaṣaṣ,
   not Ṭā-Hā, even though Ṭā-Hā's burning-bush pericope is the cycle's lexical prototype (F-06). The two
   facts are consistent: Ṭā-Hā has the deepest single pericope, al-Qaṣaṣ the highest narrative density.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 1.0403 | `h-new-111.json` (Q20 row) |
| Top-5 FR neighbors | Q 23 (0.860), Q 7 (0.865), Q 51 (0.881), Q 41 (0.882), Q 43 (0.891) | `h-new-111.json` |
| 5 farthest | Q 33 (1.174), Q 56 (1.182), Q 9 (1.200), Q 4 (1.203), Q 55 (1.270) | `h-new-111.json` |
| Q 19 (prev surah) rank in Q 20's FR list | 28/113 (FR 0.9806) | `h-new-111.json` |
| Q 21 (next surah) rank in Q 20's FR list | not top-15; FR 0.9558 (rank 17) | `h-new-111.json` |
| Q 19 → Q 20 seam | delta_raw +0.06816, ascending-rank 61/113 | `h-new-720.json` |
| Q 20 → Q 21 seam | delta_raw +0.05441, ascending-rank 50/113 | `h-new-720.json` |
| H-NEW-590 outlier | delta_pct = +5.52, p = 0.48, **WEAK_OUTLIER (NULL by significance)** | `h-new-590.json` |
| H-NEW-700/750 monorhyme | ى/ي (yāʾ), 79.3%; rhyme entropy 0.5741 nats (z = −0.35) | `h-new-700.json` / `h-new-750.json` |
| H-NEW-750 sig_A | −1.5068 (rank 92/114) | `h-new-750.json` |
| H-NEW-750 sig_B | −1.0514 (rank 83/114) | `h-new-750.json` |
| H-NEW-840 UAS | +0.1585 (rank 43/114) | `h-new-840.json` |
| mean_content_distance | 1.0403 (rank 99/114 ascending — content-divergent) | `h-new-750.json` |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| Muqaṭṭaʿāt + consolation prologue | 1-8 | طه; "We did not send the Qurʾān down on you that you should suffer"; the divine self-disclosure *al-raḥmān ʿalā al-ʿarsh istawā*; *lahu al-asmāʾ al-ḥusnā* (v 8) |
| **Mūsā burning-bush + commissioning** | **9-36** | the cycle-prototype pericope (Q020-F-06): the fire at Ṭuwā, *innanī anā Allāh* (v 14), the staff + white hand, the dual commission with Hārūn, the *rabbi-shraḥ-lī-ṣadrī* prayer |
| Mūsā & Hārūn before Firʿawn | 37-79 | the infancy flashback; the confrontation; the magicians' contest and conversion; the sea-crossing |
| **The Sāmirī / golden-calf episode** | **80-98** | the manna-and-quails; the 40-night absence; the Sāmirī's calf; Hārūn's defence; Mūsā's confrontation of the Sāmirī (Q020-F-04 tested this block) |
| Eschatology + the Trumpet | 99-114 | "Thus We relate to you"; the Day of the Trumpet; *lā taḥrik bihi lisānak* parallel *wa-lā taʿjal bi-l-Qurʾān* (v 114); *rabbi zidnī ʿilmā* |
| Ādam & Iblīs + the forgetting of the covenant | 115-127 | the covenant with Ādam; Iblīs's refusal; the tree; the Fall; the promise of guidance |
| Closing exhortation + consolation | 128-135 | the lesson of destroyed generations; *fa-ṣbir ʿalā mā yaqūlūn*; the command to prayer; "every one is waiting" |

## 5. Pre-registered novel findings (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| **Q020-F-06** | **CONFIRMED** | Ṭā-Hā burning-bush pericope (Q 20:9-36) is a lexical HUB of the Mūsā cycle: 5/6 signature roots (cycle-max) + hub-strength z = +5.81, p = 0.0001 vs length-matched null (extends H-NEW-2260) |
| **Q020-F-05** | **CONFIRMED** | Q 20:14 (*innanī anā Allāh*) is the rank-1/135 divine-self-reference verse (density 0.545, p = 0.0015) — the ʿUmar-conversion verse-location has empirical content |
| Q020-F-01 | **NULL** | Mūsā-marker verse-fraction: Q 20 is rank 2/114 (0.230), behind Q 28 al-Qaṣaṣ (0.261) — not corpus-MAX |
| Q020-F-02 | **NULL** | 2nd-person-singular density (Ibn ʿAbbās *yā rajul* vocative test): z = +0.75 (< +1.0 threshold) — does not support the vocative reading on this metric |
| Q020-F-03 | **NULL** | Two-letter muqaṭṭaʿ trio {ṬH, ṬS, YS} cohesion: 0/4 axes — letter-axis ⊥ content (5th muqaṭṭaʿāt-orthogonality confirmation) |
| Q020-F-04 | **NULL** | Sāmirī block (Q 20:85-98) lexical isolation: rank 110/122 (it is among the LEAST isolated windows; the muqaṭṭaʿāt-prologue windows v1-16 are the most distant) |

## 6. Cross-references

- **H-NEW-2260** (prophet-cycle pericope) — Q 20:9-36 is the Mūsā cycle's longest member; Q020-F-06 promotes
  it to the cycle's lexical-hub prototype (z = +5.81).
- **H-NEW-111 / cross-finding-010** — Q 20's FR nearest neighbor Q 23 al-Muʾminūn and #2 Q 7 al-Aʿrāf are
  both long-Meccan narrative surahs; the Mūsā-cycle co-members Q 7 (#2), Q 28 (#6), Q 27 (#9) all rank in
  Q 20's top-9 FR neighbors.
- **H-NEW-590** — Q 20 is a WEAK_OUTLIER (delta_pct +5.52, NULL) of its {Q 17-23} window.
- **H-NEW-720** — Q 19 → Q 20 (rank 61/113) and Q 20 → Q 21 (rank 50/113) are both mid-spectrum seams.
- **muqaṭṭaʿāt-orthogonality law** (H-NEW-610 family) — Q020-F-03 is the fifth independent confirmation at
  the two-letter sub-level.
- **al-asmāʾ al-ḥusnā ledger** (MASTER-FINDINGS-LEDGER §lahu-al-asmāʾ) — Q 20:8 is one of exactly 4
  *lahu al-asmāʾ al-ḥusnā* attestations {Q 7:180, Q 17:110, Q 20:8, Q 59:24}.

## 7. Classical-tradition status

- al-Ṭabarī (*Jāmiʿ al-bayān* on Q 20:1): surveys the طه glosses — Ibn ʿAbbās's *yā rajul* ("O man") in
  some dialects, al-Ḥasan/Saʿīd-b-Jubayr's *yā ṭāhir / hādī*, and the disjoined-letters reading; concludes
  the safe position is that it is among the muqaṭṭaʿāt whose full meaning is with Allāh.
- al-Suyūṭī (*al-Itqān* nawʿ 40, *fawātiḥ al-suwar*; nawʿ 63, *qaṣaṣ al-Qurʾān*): the disjoined-letter
  epistemic humility; Q 20 as a Mūsā-cycle *takrār al-qaṣaṣ* surah.
- al-Rāzī (*Mafātīḥ al-ghayb* on Q 20:1-8): the consolation-frame (*mā anzalnā ʿalayka al-Qurʾāna li-tashqā*)
  and the divine-name theology of v 8 *lahu al-asmāʾ al-ḥusnā* and v 5 *al-raḥmān ʿalā al-ʿarsh istawā*.
- al-Qurṭubī (*al-Jāmiʿ li-aḥkām* on Q 20): the legal and narrative *masāʾil*; the Sāmirī episode; the
  ʿUmar-conversion asbāb-frame for the surah's recitation-effect.
- Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm* on Q 20): the ʿUmar-conversion narrative (the sister Fāṭima
  reciting Q 20); the Mūsā narrative read against the Q 7 / Q 26 / Q 28 parallels.

## 8. Open questions / queued tests

- Q020-F-07 (queued): is Q 20:14 *innanī anā Allāh* the corpus-MAX single-verse divine-self-reference
  density across **all 6,236** verses (F-05 tested only within Q 20)?
- Q020-F-08 (queued): re-run the F-06 hub-strength under a **lemma** lens (rules-tuple sensitivity is
  bidirectional) and add the missing cycle members (Q 26:10-17, Q 37, the Q 7 contest) to widen N.
- Q020-F-09 (queued): the yāʾ/alif-maqṣūra monorhyme — is the 79.3% sustained rhyme over 135 verses the
  longest high-fraction monorhyme run in the corpus, and does it track the *-á* verb-ending narrative register?

---

*Investigation: Wave-N (2026-05-30) Q 20 Ṭā-Hā full deep-dive. Five tests (F-01..F-05) were SHA-locked and
run 2026-05-07; F-06 SHA-locked and run 2026-05-30. See JOURNAL.md for the method log; 06-novel-findings.md
for test detail; 04-hadith-corpus.md for the verified ʿUmar-conversion chain.*
