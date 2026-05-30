---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 103 al-ʿAṣr — Investigation Journal

## 2026-05-30 — Wave-N full 8-file deep-dive (completion of a stalled prior run)

**Context.** A prior run wrote `00-overview`, `01-empirical-profile`, `02-content-analysis`, the pre-reg
(`Q103-F-01-asr-minimal-prereg.md`), the script (`scripts/Q103_F_01_asr_minimal.py`), and the result JSON
(`csv/Q103-F-01.json`), then stalled before writing 03-07 + JOURNAL and before committing. This session
completed the template and finalized the test.

**Pre-flight (in order):**
1. Read the quran-investigation methodology skill (project investigation entry-point).
2. Read `INVESTIGATION-PROTOCOL.md` (full).
3. `ls surahs/Q103-al-asr/` and read every existing file (00, 01, 02, pre-reg, script, JSON) — did NOT
   rewrite the complete files.
4. Reviewed exemplar `surahs/Q066-al-tahrim/` (all 8 files + pre-reg) for structure, depth, tone.

**Existing-file audit (left unchanged — verified complete & disk-grounded):**
- `00-overview.md`, `01-empirical-profile.md`, `02-content-analysis.md` — all H-NEW values cross-checked against
  disk (see below); citations to scholar+work+passage present; left as-is.

**Q103-F-01 finalization (the headline task):**
- **Pre-reg SHA-256** re-confirmed on disk: `shasum -a 256 Q103-F-01-asr-minimal-prereg.md` =
  `b6445946260ce8db4cbb424c8638ad5d5be030adbac6e47af6f9be130364037c` — **matches** the `EXPECTED_SHA` embedded
  in `scripts/Q103_F_01_asr_minimal.py`.
- **Re-ran** `python3 scripts/Q103_F_01_asr_minimal.py` (seed 20260509, 10,000 perms): runtime SHA check passed
  (fail-fast not triggered); output **reproduces** `csv/Q103-F-01.json` exactly.
- **Result:**
  - **Arm A — CONFIRMED (deterministic):** 3-verse surahs = [103,108,110]; rā'-monorhyme 3-verse set = [103,108]
    (A-H1 ✓); Q 103 FR rank-1 neighbour = Q 108 at 0.2399 (A-H2 ✓).
  - **Arm B — DIRECTIONAL:** istiʿlāʾ density 0.0959 (7/73, = H-NEW-2340 #2/114), ṣād 5/7 dominant (B-H1 ✓);
    null mean 0.05005, std 0.02510, **z=+1.827, p_perm=0.07019**, direction obs>null (locked direction holds,
    NOT a pre-commit violation) — does NOT clear α=0.05 → **DIRECTIONAL**.
  - **Arm C — CONFIRMED (deterministic + rank):** wāw-qasam, temporal obj, jawāb v 2, distance 1, v 3 *illā*
    (QAC EXP 103:3:1:1) (C-H1 ✓); local_cohesion 3.0697 rank 10/114, rhyme_entropy 0.0 (C-H2 ✓).

**H-NEW value verification (read from disk this session):**
- `h-new-2340.json`: Q 103 in `top_heavy_surahs` = {heavy_density 0.0959, adhab_density 0.0}, rank #2 behind
  Q 113 (0.1212), ahead of Q 86 (0.0827). `primary` corpus result: rho_heavy_vs_adhab 0.0232, p 0.40516, **NULL**.
- FR rank-1 = Q 108 (0.2399), 3-verse set, local_cohesion rank 10, rhyme entropy 0.0 — all reproduced by the script.

**Tafsīr (read from disk):**
- al-Ṭabarī (`ar-tafsir-al-tabari/103/{1,2,3}.json`): ʿaṣr=dahr preferred; Ibn ʿAbbās "sāʿa min sāʿāt al-nahār",
  al-Ḥasan "al-ʿashī"; ʿAlī *wa-nawāʾib al-dahr* variant = tafsīr not Qurʾān; al-insān generic (exception proves);
  al-ḥaqq = kitāb Allāh (Qatāda/al-Ḥasan), al-ṣabr = ṭāʿat Allāh.
- al-Qurṭubī (`ar-tafseer-al-qurtubi/103/{1,3}.json`): Meccan (Qatāda dissent), 3 āyāt; 5+ ʿaṣr readings; legal
  masʾala (Mālik=year / al-Shāfiʿī=hour); Ubayy b. Kaʿb prophetic-tafsīr (Abū Jahl/Abū Bakr/ʿUmar/ʿUthmān/ʿAlī),
  graded mawqūf on Ibn ʿAbbās.
- al-Rāzī (`raw/razi-mafatih-al-ghayb.openiti.raw.txt` L263739-263868 surah block; L13989-14006 taḥaddī): 4 aqwāl;
  ʿaṣr/ḍuḥā loss/profit diptych; **ice-seller "irḥamū man yadhūbu raʾs māluhu" anecdote** (L263796-263799);
  **Q 103 a named taḥaddī test-case** at Q 2:23 (L14000, w/ al-Kawthar + al-Kāfirūn).
- Ibn Kathīr (`en-tafisr-ibn-kathir/103/{1,3}.json`): **al-Shāfiʿī "if people pondered this surah it would
  suffice them"**; al-Ṭabarānī two-Companions tradition (← ʿAbdullāh b. Ḥiṣn Abī Madīna); Musaylima/ʿAmr b.
  al-ʿĀṣ parody (← al-Kharāʾiṭī *Masāwiʾ al-Akhlāq* vol 2).
- al-Baghawī (`ar-tafsir-al-baghawi/103/{1,3}.json`): ʿaṣr readings; al-ḥaqq=Qurʾān; **Ibrāhīm al-Nakhaʿī ←
  Ibn ʿAwn old-age-decline gloss + cross-ref Q 95:4-6**.
- al-Jalālayn (`en-al-jalalayn/103/{1,2,3}.json`): ʿaṣr=afternoon/prayer; al-insān generic; khusr="his bargaining".

**Ḥadīth (tashkeel-normalized scan of `ahmedbaset-json/db/by_book/the_9_books`):**
- Verified **Aḥmad *Musnad* #639** (`idInBook` 639): al-ʿAṣr in witr 2nd-rakʿa with al-Naṣr + al-Kawthar; 1st-rakʿa
  al-Takāthur. Isnād al-Ḥārith ← ʿAlī (classically ḍaʿīf). Independent recitation-practice echo of the {103,108}
  twin + Q102→Q103 seam.
- **al-Ṭabarānī two-Companions tradition: 0 hits** in 9-book DB (normalized scan for *lā yatafarraqā ḥattā yaqraʾa
  … al-ʿaṣr*) → al-Ṭabarānī *Muʿjam* not on disk → flagged **UNVERIFIABLE ON DISK** (not asserted).
- **Musaylima anecdote** (al-Kharāʾiṭī) — not in 9-book DB → UNVERIFIABLE ON DISK.
- **Surah-named faḍāʾil: 0 hits** in 9-book DB; all 144 *al-ʿaṣr* occurrences = ṣalāt al-ʿaṣr → **DATA-GAP** flagged.
- Verse-of-loss text (*inna al-insāna la-fī khusr* etc.): 0 hits across all 9 books (normalized).

**Files produced this session:** 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings,
07-cross-references, JOURNAL (this). (00/01/02 + pre-reg + script + csv/Q103-F-01.json pre-existed, left unchanged.)

**Decision points / honesty notes:**
- Arm B is **DIRECTIONAL, not CONFIRMED** (p_perm=0.070). Direction was locked obs>null BEFORE the run and held,
  so it is NOT a pre-commit violation; but it does not clear α=0.05 and is reported with equal prominence to the
  CONFIRMED arms. Small-N (73 letters) + wide null + corpus-level NULL of the underlying iconicity hypothesis all
  caution against over-reading.
- al-Shāfiʿī "sufficiency" claim split into theological (NOT-TESTABLE) vs structural (VINDICATED via Q103-F-01 A+C).
- al-Ṭabarānī / al-Kharāʾiṭī traditions honestly flagged as outside the on-disk 9-book set rather than asserted.
- No garden-of-forking-paths shift: the run matched the pre-reg exactly; only completion + verification this session.

**Verdict:** Q103-F-01 = Arm A CONFIRMED (minimal-surah rā'-twin {103,108}, Q108 FR rank-1) + Arm B DIRECTIONAL
(ṣād-iconicity #2/114, p=0.07019) + Arm C CONFIRMED (minimal tripartite qasam→jawāb→istithnāʾ, local_cohesion
rank 10). Honest, equal-prominence reporting.

**Queued follow-ups:** Q103-F-02 (doubled *tawāṣaw bi-X wa-tawāṣaw bi-Y* reciprocal-enjoining template — corpus
frequency); Q103-F-03 (formalize {Q103,Q108} minimal-surah twin at root-Jaccard + rhyme-foot; candidate corpus-wide
H-NEW); Q103-F-04 (re-run Arm B null at content-root-shuffle level to separate lexical-spine from positional emphasis).
