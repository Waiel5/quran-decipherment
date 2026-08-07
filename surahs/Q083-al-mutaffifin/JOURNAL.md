---
surah: 83
surah_name_ar: المطففين
surah_name_translit: al-Muṭaffifīn
file_type: journal
date_last_updated: 2026-05-29
phase: B+
---

# Q 83 al-Muṭaffifīn — Investigation Journal


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

## 2026-05-29 — full 8-file deep-dive (single specialist session)

### Pre-flight
- Read the quran-investigation skill and `INVESTIGATION-PROTOCOL.md` (full).
- Studied template surahs `Q073-al-muzzammil/` and `Q089-al-fajr/` (8-file structure, prereg + script +
  csv conventions, SHA-lock pattern in `Q089_F_02_destroyed_civilizations.py`).
- Confirmed Q 83 = id 83, name المطففين, type "meccan" in `quran-text/quran-no-tashkeel.json`, 36 verses.

### Data grounding (all from disk, no values from memory)
- **FR (h-new-111.json):** reconstructed full matrix from `D_matrix_upper_triangular` (entries
  `[i,j,dist]`, 1-based). Q 83 mean-to-corpus = 0.8653 (corpus mean 0.9235), centrality rank 38/114;
  Q 82 is 2nd-nearest (0.5770); Q 2 ranks 109/113 (far). All top-15 neighbours in short-Meccan-tail.
- **Outlier (h-new-590.json):** X=83 delta_pct = −0.26, classification NULL (interior).
- **Rhyme (h-new-700.json):** top_letter ن frac 0.75 (verified: 27/36 ن, 9/36 م).
- **Adjacency (h-new-720.json):** Q82→83 delta_raw +0.0355 (rank 38/113); Q83→84 +0.0646 (rank 59/113).
- **iʿjāz (h-new-750.json):** sig_A +0.198 (rank 55), sig_B −0.339 (rank 64); rhyme_entropy 0.562.
- **UAS (h-new-840.json):** −2.491, rank 110/114 (bottom-5, matches Protocol §3.3).
- **Counts (computed):** 169 words, 750 letters, 118 distinct, TTR 0.698, avg 4.69 w / 20.8 l per verse.
- **Chronology (data/revelation-order.csv):** mushaf 83, revelation_order **86 (last Meccan before Q2
  #87)**, Nöldeke 37, period Meccan.
- **Rebuke-*kallā* (QAC v0.4):** Q 83 = 4 genuine POS:AVR *kallā* (vv. 7,14,15,18), corpus-MAX tie w/
  Q 74; corpus total 33 (matches al-Dānī); Q 4's 4 raw كلا are 0 genuine (homograph) — §10.80 trap.

### Classical sources (all cited from disk)
- al-Qurṭubī `ar-tafseer-al-qurtubi/83.json` — Makkī/Madanī dispute (Ibn Masʿūd/Ḍaḥḥāk/Muqātil Meccan;
  Ḥasan/ʿIkrima Medinan; al-Kalbī/Jābir b. Zayd "between Mecca and Medina"); asbāb; rān hadith; ʿilliyyīn.
- al-Suyūṭī `raw/suyuti-itqan.openiti.raw.txt` — "revealed during the Hijra journey before entering
  Medina" (al-Nasafī); *kallā* in al-waqf nawʿ; Makkī-except-6 tradition.
- al-Zamakhsharī `raw/zamakhshari-kashshaf.openiti.raw.txt` — *kallā radʿ*; the heaven/earth muqābala.
- Ibn Kathīr `ar-tafsir-ibn-kathir/83.json` — al-Shāfiʿī ruʾya argument on v.15 maḥjūbūn; ʿilliyyīn.
- al-Ṭabarī `ar-tafsir-al-tabari/83.json`, al-Baghawī `ar-tafsir-al-baghawi/83.json`.

### Hadith verification (40,943 hadiths scanned in `ahmedbaset-json/by_book/the_9_books/`)
- **Q83:6 standing/sweat:** Bukhārī idInBook 4731 (Tafsīr) + 6292 (Riqāq) + Muslim 7024 (Ṣifat
  al-Qiyāma), all Ibn ʿUmar — ṣaḥīḥ muttafaq.
- **Q83:14 rān/black-spot:** Tirmidhī idInBook 3418 (Tafsīr), Abū Hurayra, grading in matn = **ḥasan
  ṣaḥīḥ**; Ibn Mājah 3982 (Zuhd), Abū Hurayra.
- **Q83:18-19 ʿilliyyīn:** Abū Dāwūd idInBook 3988 (Sunna), Abū Saʿīd al-Khudrī (ḍaʿīf isnād, ʿAṭiyya
  al-ʿAwfī).
- **NUMBERING PROVENANCE:** dataset uses per-book `idInBook`, NOT a print-edition number — flagged in
  04-hadith-corpus; print numbers NOT asserted.
- **DATA-GAP:** the *al-muṭaffifīn* asbāb (al-Nasāʾī ← Ibn ʿAbbās) is tafsir-transmitted but not
  isolable as a numbered 9-book record in this dataset — flagged, not invented.
- **FALSE-POSITIVE LOG:** Muslim 276 (Ḥudhayfa fitan), Ibn Mājah 145 (repentance-door), Bukhārī 206
  (Zubayr) rejected after reading matn — recorded in 04 §5.

### Pre-registered test Q083-F-01
- Wrote `preregs/Q083-F-01-sijjin-illiyyin-antithesis-prereg.md`; SHA-256
  `acd67eb32847fa20631a37fedb608b04ef8f42152edcd618b51e4eaa7602ddc6`.
- Embedded SHA in `scripts/Q083_F_01_sijjin_illiyyin_antithesis.py`; verified at runtime (PASS).
- Verified destiny-root Buckwalter forms against QAC BEFORE running (sijjīn=sjn, ʿilliyyīn=Elw,
  arāʾik=Ark, etc.); corrected the ABRAR set in the script (the prereg locks the sets BY NAME, so the
  Buckwalter encoding is an implementation detail and the SHA-lock on the prereg is untouched).
- **Garden-of-forking-paths:** the block boundary v17/v18 fixed before lock; destiny-root sets fixed
  from the surah's own destiny-nouns before running; H2 deliberately left direction-free.

### Q083-F-01 result (seed 20260509, 10000 perms, k=3, α_bon 0.0167)
- **H1 PRE-COMMIT VIOLATION:** locked "frame-mirror ELEVATED"; observed shared roots = 3 (`ktb, rqm,
  dry`) vs null mean 12.7 → REVERSED (perm-p elevated 0.943). Robust across seeds {20260601, 99999,
  12345} (null mean ≈ 12.8, obs 3 throughout); within-surah null p=0.956. Published as NULL/violation.
- **H2 pivot:** Jaccard 0.0698 vs null 0.1129 → TYPICAL (24th pct low-side).
- **H3 CONFIRMED:** destiny-vocabularies perfectly disjoint (0 leakage both directions).
- **Verdict: DIRECTIONAL** (H1 violation + H3 confirmed). Substantive lesson logged: frame-parallelism ≠
  lexical overlap; the muqābala is a 3-root scaffold + disjoint destiny-lexicon.

### Decision points
- Chose the SIJJĪN↔ʿILLIYYĪN antithesis (brief's strong candidate) over the taṭfīf-concentration test —
  it is the surah's signature structure and classically anchored (al-Rāzī/al-Zamakhsharī muqābala).
- Reported the H1 reversal with full prominence rather than re-locking — per Protocol §1.8 and
  PRE-REG-STANDARD-01.

### Files produced
- 00–07 markdown + JOURNAL; `preregs/Q083-F-01-*-prereg.md`; `scripts/Q083_F_01_*.py`;
  `csv/Q083-F-01.json`.

### Status: investigation-complete (8 files; 5 classical claims audited; 1 pre-registered test with
honest DIRECTIONAL/violation verdict; all empirical metrics integrated; cross-references mapped).
