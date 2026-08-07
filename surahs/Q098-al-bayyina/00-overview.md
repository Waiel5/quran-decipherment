---
surah: 98
surah_name_ar: البينة
surah_name_translit: al-Bayyina
surah_name_english: "The Clear Proof / The Evidence"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 1 pre-registered 4-arm test landed — A title-density FALSIFIED (corrects H-NEW-1820 summary) + B/C CONFIRMED (bariyya hapax + unique antonym muqābala) + D NULL (pre-commit violation, jadal-overlap)
---

# Q 98 al-Bayyina — Overview


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
| Surah ID | 98 | canonical |
| Arabic name | البينة | canonical (also titled *Lam Yakun*, from the opening words; *al-Qayyima*) |
| Transliteration | al-Bayyina | canonical |
| English meaning | "The Clear Proof / The Evidence" | classical (root b-y-n) |
| Alternative names | *Lam Yakun* (its opening), *al-Qayyima* (from vv 3/5) | al-Qurṭubī, *al-Jāmiʿ li-aḥkām*, opening of Q 98 ("tafsīr sūrat *lam yakun*") |
| Verse count | 8 | Hafs-Kūfan (`data/hafs-verse-counts.tsv` line 98); **variant: al-Qurṭubī "tisʿ āyāt" = 9** (see audit) |
| Position in mushaf | 98 | canonical |
| Revelation order | #100 (Tanzil Egyptian Standard); Nöldeke #92 | `data/revelation-order.csv` (mushaf_order=98) |
| Type | **Medinan** (Ibn ʿAbbās + jumhūr); Meccan in Yaḥyā b. Sallām's qawl | `data/revelation-order.csv` ("Medinan"); al-Qurṭubī opening |
| Word count (no-tashkeel, marks stripped) | 94 | computed (`scripts/Q098_F_01_bariyya_antithesis.py` pipeline) |
| Letter count (no-tashkeel) | 404 | computed |
| Distinct QAC roots | 42 (60 root-tokens) | `data/morphology/root-index.json` |
| Opening | لم يكن الذين كفروا — "Those who disbelieved … were not …" | direct (negative declarative; no muqaṭṭaʿāt, no qul, no sabbaḥa) |
| Predominant rhyme (rāwī) | **ه/ة (tāʾ marbūṭa as final grapheme), 8/8 verses (100%) — PERFECT monorhyme; rhyme-entropy 0.0** | `h-new-700.json` rhyme_letter_diagnostics; `h-new-750.json` |
| Length class | mufaṣṣal-qiṣār (al-mufaṣṣal short-tier; short Medinan) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 98 matters for the project

1. **The khayr↔sharr al-bariyya minimal-pair muqābala (Q098-F-01 Arm C, CONFIRMED corpus-SINGLETON).**
   Q 98:6 closes `أولئك هم شر البرية` ("those are the WORST of creation") and Q 98:7 closes
   `أولئك هم خير البرية` ("those are the BEST of creation"). Among the corpus's **219** adjacent
   faith-antithetical verse-pairs, Q 98:6-7 is the **ONLY** pair whose verse-tails align with exactly
   ONE substituted word over ≥3 matched trailing words AND whose single pivot is a genuine lexical
   antonym (khayr↔sharr). This is the corpus's tightest *muqābala lafẓiyya* (verbal antithesis with a
   parallel frame): the frame `أولئك هم [X] البرية` is held constant, X flips between the two poles of
   moral value. al-Suyūṭī's ṭibāq/muqābala figure (*Itqān* nawʿ 59) has here a corpus-unique exemplar.

2. **al-bariyya is a corpus hapax-pair (Q098-F-01 Arm B, CONFIRMED).** The rhyme-word البرية ("the
   creation/created beings," root b-r-ʾ) occurs in **exactly 2** positions in the entire Quran — both in
   Q 98 (v6, v7). It appears nowhere else. Q 98 owns the word, and uses it twice, in immediate
   antithetical adjacency.

3. **Title-density-EXACT FALSIFIED (Q098-F-01 Arm A — corrects an unverified ledger summary).** The
   H-NEW-1820 summary-list asserted Q 98 al-Bayyina is "rank-1 in its title-root." On disk this is FALSE:
   Q 98 carries only **2** byn attestations (raw-count rank **59/71**; normalized-density rank 6/71), and
   in the exact eponymous surface-form البينة it is tied/beaten by **4** other surahs (Q 11 leads with 4
   occurrences of على بينة). The surah whose very NAME means "the clear proof" is NOT the clear-proof
   word's density peak — a textbook H-NEW-1820 title-density-independence instance. The ledger summary
   entry is corrected (see `05-classical-claims-audit.md`).

4. **The asymmetric antithesis — al-Rāzī's masʾala 4, deterministically vindicated.** v 6 (disbelievers
   in Hell) reads `خالدين فيها` (abiding therein) WITHOUT أبدا; v 8 (believers' reward) reads
   `خالدين فيها أبدا` (abiding therein FOREVER) WITH أبدا. al-Rāzī (*Mafātīḥ al-ghayb*, Q 98, masʾala 4)
   asks precisely why, and answers "His mercy exceeds His wrath." The sharr↔khayr muqābala is therefore
   NOT perfectly symmetric: the reward-pole is rhetorically expanded. Verified on disk.

5. **The Ubayy b. Kaʿb recitation ḥadīth — the surah's signature faḍīla.** "Allāh commanded me to recite
   to you [Ubayy] *Lam yakun al-ladhīna kafarū*" / "He named me to you?!" / "Yes" / "and Ubayy wept" —
   in al-Bukhārī (#4753, #4754, Kitāb al-Tafsīr), Muslim (#1757, #6185), and al-Tirmidhī (#3888 *ḥasan
   ṣaḥīḥ*, #3889, #3995). One of the most-attested single-surah recitation reports in the corpus, all
   verified on disk (`04-hadith-corpus.md`).

6. **FR-tail short surah, anti-iʿjāz band.** Q 98 sits in the short-surah FR cluster (mean FR 0.8214,
   nearest Q 108, Q 110, Q 112), UAS rank 93/114 — it is NOT a structural-iʿjāz hub. Its architectural
   interest is **micro-structural** (the unique antonym muqābala + the bariyya hapax + the perfect
   monorhyme), not whole-surah-dispersion.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.8214 | `h-new-111.json` (Q98 row) |
| Top-3 FR neighbors | Q 108 (0.495), Q 110 (0.499), Q 112 (0.508) | `h-new-111.json` |
| 5 farthest | Q 3, 4, 6, 12, 26 (long narrative/legal) | `h-new-111.json` |
| Q 97 → Q 98 seam | delta_raw +0.02750, ascending-rank 27/113 | `h-new-720.json` |
| Q 98 → Q 99 seam | delta_raw +0.12653, ascending-rank 91/113 | `h-new-720.json` |
| H-NEW-590 outlier | **NOT computed** (Q98 not in the 6-candidate set {1,9,18,55,62,112}) — data-gap | `h-new-590.json` |
| H-NEW-700 monorhyme | ه/ة (tāʾ-marbūṭa final grapheme), **100% (8/8)**; rhyme-entropy **0.0 nats** | `h-new-700.json` / `h-new-750.json` |
| H-NEW-750 sig_A | −0.3863 (rank 73/114) | `h-new-750.json` |
| H-NEW-750 sig_B | −1.1291 (rank 88/114) | `h-new-750.json` |
| H-NEW-840 UAS | −1.6965 (rank 93/114) | `h-new-840.json` |
| Allāh-substring | 3 tokens, 3/8 verses (37.5%) | computed |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| The non-desisting (munfakkīn) thesis | 1 | the People of the Book + polytheists were not to desist *until the Clear Proof came* |
| Definition of the Clear Proof | 2-3 | a Messenger from Allāh reciting purified scrolls (*ṣuḥuf muṭahhara*) containing upright writings (*kutub qayyima*) |
| The post-proof schism | 4 | those given the Scripture split ONLY *after* the Clear Proof reached them |
| The unifying creed (the dīn al-qayyima) | 5 | they were ordered ONLY to worship Allāh sincerely (*mukhliṣīn … ḥunafāʾ*), establish ṣalāt, give zakāt |
| The disbelievers' end + verdict | 6 | People of the Book + polytheists who disbelieved → Hell-fire, abiding; **"those are the WORST of creation"** |
| The believers' verdict | 7 | those who believed and did righteous deeds → **"those are the BEST of creation"** |
| The believers' reward (the seal) | 8 | Gardens of Eden, rivers beneath, **abiding therein FOREVER (abadan)**; Allāh pleased with them and they with Him — "that is for whoever fears his Lord" |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q098-F-01 Arm A | **title-density-EXACT FALSIFIED** | Q 98 al-Bayyina is rank 59/71 (raw byn) / not rank-1 in البينة — corrects H-NEW-1820 summary; new title-density-independence data point |
| Q098-F-01 Arm B | **CONFIRMED** | al-bariyya (البرية) is a corpus hapax-pair (exactly 2 occurrences, both Q 98:6/7) |
| Q098-F-01 Arm C | **CONFIRMED — corpus-SINGLETON** | Q 98:6-7 is the corpus-UNIQUE adjacent faith-antithetical verse-pair with a single-substitution aligned tail-frame pivoting on the khayr↔sharr antonym (1 of 219) |
| Q098-F-01 Arm D | **NULL (pre-commit violation)** | J(v6,v7)=0.083 > null_mean 0.026 (z=+1.16) — the muqābala verse-pair OVERLAPS (shares the brA frame-root), replicating the H-NEW-2360 jadal-overlap law at verse-pair scale |

## 6. Cross-references

- **H-NEW-1820 (title-density independence)** — Q 98 was wrongly listed in the rank-1 set; Arm A moves it
  to the 47/89 non-rank-1 majority (corrected).
- **H-NEW-2360 (antithesis = jadal-overlap, NOT disjoint-content)** — Arm D is a clean verse-pair-scale
  replication: even the corpus's tightest *surface*-muqābala (Q 98:6-7) is content-OVERLAPPING at the
  root level (shares brA), not disjoint.
- **H-NEW-2290 / F1 faith-field** — Q 98:6-7 is one of 219 adjacent faith-antithetical verse-pairs; the
  Amn↔kfr field instrument flags it.
- **Q 99 al-Zalzala** — forward mushaf neighbor; Q 98 → Q 99 is a mid-expensive seam (rank 91/113).
- **Q 11 Hūd** — title-density foil: Q 11 carries على بينة ×4, the corpus leader in the eponymous form.
- **Q 83 al-Muṭaffifīn (Q083-F-01)** — the destiny-catalogue muqābala precedent that motivated Arm D.

## 7. Classical-tradition status

- **al-Ṭabarī** (*Jāmiʿ al-bayān*, Q 98): glosses *munfakkīn* = "not desisting (muntahīn) until the Clear
  Proof — i.e. this Qurʾān / the Messenger — comes"; surveys the qawls of Mujāhid, Qatāda, Ibn Zayd.
- **al-Zamakhsharī** (*al-Kashshāf*, Q 98): the People-of-the-Book/polytheists "won't budge until the
  promised prophet (in the Tawrāt/Injīl) is sent" reading; the qiraʾāt of البرية (Nāfiʿ: البريئة with
  hamza; *khiyār al-bariyya*); the faḍīla "whoever recites *Lam yakun* will be with *khayr al-bariyya*."
- **al-Rāzī** (*Mafātīḥ al-ghayb*, Q 98): seven masāʾil on vv 6-8, incl. masʾala 4 (the *abadan*
  asymmetry: mercy exceeds wrath), masʾala 6 (the rhetorical force of *hum sharr al-bariyya* — worse than
  thieves, highwaymen, ignorant — "the threat against the evil scholars is greater than against anyone").
- **al-Qurṭubī** (*al-Jāmiʿ li-aḥkām*, Q 98): Meccan (Yaḥyā b. Sallām) vs Medinan (Ibn ʿAbbās + jumhūr);
  **9 āyāt**; the weak (bāṭil, per Ibn al-ʿArabī) Abū al-Dardāʾ faḍīla; the ṣaḥīḥ Ubayy recitation report
  (Bukhārī + Muslim); "the jurisprudence of the teacher reciting to the student."
- **Ibn Kathīr** (*Tafsīr al-Qurʾān al-ʿaẓīm*, Q 98): the Ubayy recitation chains (Aḥmad's Musnad +
  "rawāhu al-Bukhārī wa-Muslim wa-l-Tirmidhī wa-l-Nasāʾī"); *sharr al-bariyya* = "the worst of the
  creation Allāh created (baraʾahā wa-dharaʾahā)."

## 8. Open questions / queued tests

- Q098-F-02 (queued): the *qayyima* triad (*kutub qayyima* v3, *dīn al-qayyima* v5, + the alt-title
  *al-Qayyima*) — is the q-w-m / qayyima cluster a Q 98-distinctive lexical signature?
- Q098-F-03 (queued): formalize the *abadan* reward/punishment asymmetry (v6 no-abadan vs v8 abadan) as
  a corpus-wide test — do believer-reward "khālidīna" clauses carry *abadan* more often than
  disbeliever-punishment ones?
- Q098-F-04 (queued): the 9-verse vs 8-verse counting-tradition split (al-Qurṭubī's *tisʿ āyāt*) —
  locate the variant fāṣila split-point (likely v2/v3 boundary).

---

*Investigation: Wave-N (2026-05-30) Q 98 al-Bayyina full deep-dive (single-specialist landing). See
JOURNAL.md for the method log; 06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified
Ubayy recitation chain.*
