---
surah: 84
surah_name_ar: الإنشقاق
surah_name_translit: al-Inshiqāq
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 84 al-Inshiqāq — Investigation Journal

## 2026-05-30 — Wave-N full 8-file deep-dive (completion of a stalled prior run)

**Context.** A prior run wrote 00-overview, 01-empirical-profile, 02-content-analysis and the full
Q084-F-01/F-02/F-03 pre-reg + script + csv triples, then stalled before writing 03-07 + JOURNAL and
before committing. This session completed the template and reproduced all three tests.

**Pre-flight (in order):**
1. Read the quran-investigation skill (SKILL.md) and `INVESTIGATION-PROTOCOL.md` (full).
2. `ls surahs/Q084-al-inshiqaq/` + read every existing file (00, 01, 02; the three preregs/, scripts/,
   csv/ for F-01/F-02/F-03).
3. Reviewed exemplar `surahs/Q066-al-tahrim/` (03-07 + JOURNAL formatting, depth, tone).

**Data re-verification (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 84: 25 verses; **v 2 ≡ v 5** = *وأذنت لربها وحقت* (character-identical;
  phrase corpus-unique — appears ONLY at 84:2 and 84:5); v 21 carries sajda glyph ۩; v 6 carries both
  k-d-ḥ forms (*كادح* + *كدحا*).
- `data/revelation-order.csv`: Q 84 = revelation **#83** (Tanzil EgStd), Meccan, Nöldeke **#29 Early Meccan**.
- `data/hafs-verse-counts.tsv` line 84 = **25**.
- **h-new-111.json**: Q 84 mean FR 0.8263; nearest Q 103/108/106/100/94 (all <0.50, juzʾ-30).
- **h-new-590.json** (`all_surahs_results` X=84): window {81-87}, d_W **0.5952**, d_{W−84} **0.5901**,
  pct 0.26/0.59, **delta_pct −0.33, classification NULL** (cohesion member). [Corrected 01-empirical-profile's
  stale d̄_W value 0.91540 → 0.59524, with the real window-mean from disk.]
- **h-new-700.json**: phoneme_vectors idx83 = [0.01798, 0.03596, 0.04494, 0.12809]; rhyme top_letter ا
  frac 0.24, 25 verses.
- **h-new-750.json** (per_surah Q84): rhyme_entropy 1.79144 (z +1.850); mean_content_distance 0.82630
  (z −0.959); local_cohesion 1.63755; **sig_A +2.80902 rank 2/114**; sig_B +2.01204 rank 7/114.
- **h-new-840.json** (all_uas Q84): UAS **+0.92610, rank 25/114**; abs_outlier 0.330; max_cost 0.06458;
  abs_ijaz 2.80902.
- **h-new-720.json** (per_adjacency): Q 83→84 delta_raw +0.06459 (frac_residual 0.00779, rank 59/113);
  Q 84→85 delta_raw +0.00691 (frac_residual 0.00083, rank 17/113); Σdelta 9.827, mean 0.0870.

**Tafsīr (read from disk):**
- al-Ṭabarī (spa5k `ar-tafsir-al-tabari/84/{1,2,6}`): v1 *taṣaddaʿat fa-kānat abwāban*; v2 *samiʿat
  wa-aṭāʿat*; v6 *ʿāmil … fa-mulāqīh bihi* (Ibn ʿAbbās).
- al-Zamakhsharī (`raw/zamakhshari-kashshaf.openiti.raw.txt`): deleted-apodosis *iʿjāz*; *istiʿāra* of
  *adhinat*; v2≢v5 "different aspect → not takrār."
- al-Rāzī (`raw/razi-mafatih-al-ghayb.openiti.raw.txt`): multi-position apodosis survey; kādiḥ embryo-arc;
  *warāʾa ẓahrih* harmonized with Q 69:25.
- al-Qurṭubī (spa5k `ar-tafseer-al-qurtubi/84/{1,6,19,21}`): **makkiyya fī qawl al-jamīʿ, 25 āya**; v6
  al-insān=genus (or al-Aswad/Ubayy); v19 4-way fork; **v21 Mālik (not ʿazāʾim) vs Ibn al-ʿArabī (yes)**.
- Ibn Kathīr (spa5k `en-tafisr-ibn-kathir/84/{1,6}`): sajda chain Mālik→Abū Salama (Muslim/Nasāʾī) +
  Bukhārī→Abū Rāfiʿ; Jibrīl *mulāqīh* counsel (v6).
- al-Suyūṭī (`raw/suyuti-itqan.openiti.raw.txt`): verse-count variants 23/24/25; sajda among sujūd al-mufaṣṣal.

**Ḥadīth (verified `idInBook` on disk, `ahmedbaset-json/db/by_book/the_9_books`):**
- **Sajda (84:21):** Bukhārī #748, #750, #1043, #1047; Muslim #1199, #1201, #1202, #1204, #1206;
  Abū Dāwūd #1408, #1409; Nasāʾī #963-965, #967-970; Tirmidhī #573 (no grading colophon on disk →
  flagged); Ibn Mājah #792, #793. All Arabic-matched (*إذا السماء انشقت* + *سجد/يسجد*).
- **Ḥisāb yasīr (84:7-8):** Bukhārī #103, **#4732 (Book 65 Kitāb al-Tafsīr)**, #6297, #6298;
  Muslim #7046, #7048; Tirmidhī **#2496 (*ṣaḥīḥ ḥasan*)**, **#3421 (*ḥasan ṣaḥīḥ*)** — gradings read from
  Abū ʿĪsā colophons on disk; Abū Dāwūd #3094.
- **Jibrīl mulāqīh (84:6):** scanned all 9-book collections for *ملاقيه* → **NOT located** as a numbered
  ḥadīth → flagged as Ibn-Kathīr tafsīr-citation only.
- **Faḍāʾil:** none surah-named in the 9-book set → flagged as data-gap, not absence-claim.

**Pre-registration verification (no new pre-reg written — all three were locked by the prior run):**
- F-01 prereg SHA `cd582e24…`; F-02 prereg SHA `61553173…`; **F-03 prereg SHA
  `bf28ee3f6aafcf3fc17d8fcd9718052f5e5ddc054f1a43225c4a5ac051c38ffb`** — recomputed independently
  (`shasum -a 256`) and matches both the file and the script's embedded `EXPECTED_SHA`.

**Computation (all three scripts re-run, JSON reproduced byte-consistent):**
- **Q084-F-01** (`csv/Q084-F-01.json`): intersection {idhā}∩{sajda} = **{84}**, |I|=1; 84:1 idhā pattern ✓,
  84:21 sajda glyph ✓. **CONFIRMED** (deterministic).
- **Q084-F-02** (`csv/Q084-F-02.json`): root k-d-ḥ = 2 forms, 1 verse (Q 84:6); mafʿūl-muṭlaq bigram ✓.
  **CONFIRMED — corpus-SINGLETON** (deterministic).
- **Q084-F-03** (`csv/Q084-F-03.json`, seed 20260509, 10,000 perms; replication 20260511): **[SHA-OK]**;
  S_obs = **4** shared anchors {Ahl, Aty, ktb, srr}; null_mean **5.2953**; **z = −0.334, p_perm = 0.6132**
  (replication p 0.6168). Direction locked S_obs > null mean → **REVERSED**. **NULL (pre-commit violation).**

**Decision point.** Q084-F-03's locked direction reversed → published as NULL with full prominence
(PRE-REG-STANDARD-04, MEMORY equal-NULL-prominence). NOT massaged. The reversal mechanism — Q 84's
mufaṣṣal-qiṣār root-sparsity (vv 7-15 union = 19 roots vs corpus 9-verse mean ~50) means the antithesis
is built by lexical DISJUNCTION (swapping content vocabulary for the two fates) rather than shared-anchor
re-valencing — is documented as a first-class scale-of-aggregation finding (cross-finding-025 instance,
sibling to Q066-F-01 Arm B). No garden-of-forking-paths shift: the analysis matched the pre-reg exactly.
A budget-normalized follow-up (Q084-F-03b) is pre-registered as a SEPARATE test, NOT a post-hoc rescue.

**Garden-of-forking-paths / scope-corrections made this session (honesty log):**
- Corrected 01-empirical-profile's stale H-NEW-590 d̄_W (0.91540 → 0.59524) to the real window-mean on disk.
- Scope-corrected the v2≡v5 "corpus-unique refrain" claim: the *phrase* is corpus-unique (true), but the
  *phenomenon* of intra-surah verbatim refrains is common (Q55 ×31, Q77 ×10, Q56 has two, etc.) — recorded
  in 05 Claim 5 and noted against the queued Q084-F-05.

**Files produced this session:** 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit,
06-novel-findings, 07-cross-references, JOURNAL (this); 01-empirical-profile edited (1 value-correction).
Pre-existing (prior run, not rewritten): 00-overview, 01 (edited), 02; preregs/, scripts/, csv/ for F-01/02/03.

**Verdict:** Q084-F-01 CONFIRMED (corpus-unique biplex marker) + Q084-F-02 CONFIRMED (k-d-ḥ corpus-EXACT) +
Q084-F-03 NULL (pre-commit violation; book-hand antithesis built by lexical disjunction, not shared-anchor
mirroring). Honest, equal-prominence NULL.

**Queued follow-ups:** Q084-F-03b (budget-normalized antithesis re-test — pre-registered, not a rescue);
Q084-F-04 (semantic cascade-merge of vv 1-5, resolving H-NEW-2250 Limit 2); Q084-F-05 (intra-surah refrain
survey among idhā-openers — preliminary scan shows Q 56 also carries refrains, so Q 84 is NOT the only one).
