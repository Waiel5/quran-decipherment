---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 94 al-Sharḥ — Investigation Journal

## 2026-05-30 — Wave-N full 8-file deep-dive (two-pass: stub-then-salvage completion)

### Pass 1 (prior run, stalled)
An earlier run wrote 00-overview, 01-empirical-profile, 02-content-analysis, the pre-reg
(`Q094-F-01-usr-yusr-reprise-prereg.md`), the script (`scripts/Q094_F_01_usr_yusr_reprise.py`), and
`csv/Q094-F-01.json` + the `preregs/` and `scripts/` mirror copies — then stalled before writing 03-07,
JOURNAL, or committing.

### Pass 2 (this session) — completion
**Pre-flight (in order):**
1. Read the quran-investigation skill (SKILL.md).
2. Read `INVESTIGATION-PROTOCOL.md` (full).
3. `ls surahs/Q094-al-sharh/` and read every existing file (00, 01, 02, pre-reg, script, JSON) — confirmed
   00/01/02 complete and high-quality; did NOT rewrite them.
4. Reviewed exemplar `surahs/Q066-al-tahrim/` (03-07 + JOURNAL) for template depth/tone.

**Finalized the pre-registered test (Q094-F-01):**
- Recomputed prereg SHA-256 on disk = `2dd938018b303e0da9e8a1313d3fe710fe83123913e6aaa705c1975908f71d2a`
  — matches `EXPECTED_SHA` embedded in the script.
- Ran `python3 scripts/Q094_F_01_usr_yusr_reprise.py`: printed "SHA OK"; re-wrote `csv/Q094-F-01.json`.
- **Result (all three arms CONFIRMED):**
  - **Arm A:** single-connective hits = `[[94,5,6,"فإن","إن"]]` (A-H1 ✓); whole-string hits = `[[94,5,6]]`
    (A-H2 ✓) → corpus-singleton. **CONFIRMED.**
  - **Arm B:** min-edit = 1 over 5,821 substantive adjacent pairs, unique = Q94:5-6 (B-H1 ✓);
    exact-verbatim-adjacent count = 0 (B-H2 ✓); obs edit 1 vs null-mean 12.83, p_perm 0.0003 (seed 20260509),
    replicated p 0.0001 (seed 20260530) (B-H3 ✓) → **CONFIRMED (3/3).** Edit-2 runner-up family:
    Q74:19-20, Q75:34-35, Q82:17-18, Q102:3-4.
  - **Arm C:** العسر def in v5+v6 ✓; يسرا indef in v5+v6 ✓; root-Jaccard(v5,v6) = 1.0 (`Esr`,`ysr`) ✓ →
    **CONFIRMED** (orthographic asymmetry present; theology out-of-scope).
- No pre-commit violation, no direction reversal in this test.

**Data extraction for the missing files (all from disk, no values from memory):**
- `data/revelation-order.csv`: Q 94 (mushaf 94) = revelation #12, Meccan, Nöldeke #12, Early Meccan;
  Q 93 = #11; Q 95 = #28 — Q 93→Q 94 are consecutive in BOTH mushaf and revelation order.
- `data/hafs-verse-counts.tsv` line 94 = 8.
- `h-new-111.json` (FR): Q 94 mean 0.7936; nearest Q 108 (0.230); Q 93 rank 16 (0.3641); Q 95 rank 15 (0.3614)
  — re-verified by direct matrix scan.
- (01-empirical-profile already integrates h-new-590/700/720/750/840 with exact values + paths.)

**Tafsīr (read from disk; 6 mufassirūn — 03-tafsir-survey):**
- al-Ṭabarī (spa5k `ar-tafsir-al-tabari/94/{1,5,6}.json`): v1 spiritual sharḥ; vv5-6 *lan yaghliba ʿusrun
  yusrayn* via al-Ḥasan (Yūnus/ʿAwf/Maʿmar chains, mursal) + Qatāda + Ibn Masʿūd + Mujāhid.
- al-Zamakhsharī (`raw/zamakhshari-kashshaf.openiti.raw.txt` surah-94 block): istifhām inkārī affirms;
  *fa-in qulta…qultu* dialectic; maʿiyya; *jāʾanī Zayd Zayd* definite-same / indefinite-distinct; two eases =
  conquests-then-Caliphs OR dunyā+ākhira; tafkhīm.
- al-Qurṭubī (spa5k `ar-tafseer-al-qurtubi/94/{1,5}.json`): Meccan-consensus / 8 āyāt; v1 shaqq al-ṣadr
  (Anas←Mālik b. Ṣaʿṣaʿa "fī al-Ṣaḥīḥ"); *a-lam nashraḥ = qad sharaḥnā* (perfect coordination proof);
  v5 taʾkīd (Farrāʾ) vs two-eases (Thaʿlab) + Ibn ʿAbbās + Ibn Masʿūd + ʿUmar's letter + al-Jurjānī's
  *qawl madkhūl* (rider/sword) objection; v6 *ibtidāʾ* — proof = *taʿarrī min fāʾ aw wāw*.
- Ibn Kathīr (spa5k `en-tafisr-ibn-kathir/94/5.json` + `ar-tafsir-ibn-kathir/94/5.json`): v2↔Q48:2; v4
  Mujāhid/Qatāda shahāda; exact grammar *al-ʿusr muʿarraf fī al-ḥālayn fa-huwa mufrad wa-l-yusr munakkar
  fa-taʿaddad … al-ʿusr al-awwal ʿayn al-thānī*; Abū Hurayra *unzila al-maʿūna*; al-Shāfiʿī verses;
  vv7-8 worship-charge.
- al-Jalālayn (spa5k `en-al-jalalayn/94/{5,6}.json`): hardship→assisted-victory.
- Tanwīr al-Miqbas / Ibn ʿAbbās (spa5k `en-tafsir-ibn-abbas/94/{5,6}.json`): consolation-for-poverty.

**Ḥadīth (verified `idInBook` on disk, `ahmedbaset-json/db/by_book/the_9_books` — 04-hadith-corpus):**
- *Shaqq al-ṣadr* (Anas ← Mālik b. Ṣaʿṣaʿa Isrāʾ): Muslim #321 (exact *fa-sharaḥa ṣadrī* + Zamzam), #322;
  Bukhārī #3074 (Bad' al-Khalq), #3254, #3288 (Anbiyāʾ), #3724 (Manāqib al-Anṣār), #5397; Nasāʾī #450
  (Ṣalāh); **Tirmidhī #3430 (Book of Tafsīr, ḥasan ṣaḥīḥ — Abū-ʿĪsā colophon verified)**.
- *Lan yaghliba ʿusrun yusrayn*: **Mālik Muwaṭṭaʾ #1007 (Jihād)** — ʿUmar's letter to Abū ʿUbayda b.
  al-Jarrāḥ (MAWQŪF). 9-book search returns NO marfūʿ ḥadīth of the phrase. The marfūʿ form is MURSAL via
  al-Ḥasan (al-Ṭabarī, Ibn Kathīr). **FLAGGED** — common usage cites it as a prophetic ḥadīth; on disk it
  is an athar of ʿUmar.
- Faḍāʾil of al-Sharḥ specifically: 0 hits in 9-book set → flagged data-gap (not absence claim).

**Classical-claims audit (05) — 7 claims:** Meccan-consensus (VINDICATED), 8 verses (VINDICATED),
*a-lam nashraḥ*=affirmation/perfect coordination (VINDICATED morphological), v6 dropped-fāʾ *ibtidāʾ*
(VINDICATED corpus-SINGLETON via Q094-F-01 A+B), definite/indefinite two-eases grammar (VINDICATED
orthographic asymmetry via Arm C; theology out-of-scope), Q93→Q94 consolation-pair (VINDICATED seam
10/113 + FR 16 + consecutive revelation), *lan yaghliba* ḥadīth soundness (NOT-TESTABLE; mawqūf in 9 books).

**Decision points / honesty notes:**
- Did NOT rewrite the complete 00/01/02 files (per brief). NOTE: like the other salvaged Wave-N stubs, the
  00-overview's §3 line calls H-NEW-590 a value-bearing row (delta_pct −0.07, NULL) which is correct and
  consistent with 01 — no "data-gap" mislabel here; left as-is.
- Q094-F-01 passed cleanly on all three arms; the honest scope-limit is that Arm C verifies the grammatical
  asymmetry, NOT the theological "two eases," NOT the Thaʿlab-vs-Farrāʾ choice (al-Jurjānī's objection shows
  the tradition itself debates it). Documented with equal prominence.
- The *lan yaghliba ʿusrun yusrayn* attribution is corrected: 9-book attestation is ʿUmar's mawqūf
  (Muwaṭṭaʾ #1007), marfūʿ only as al-Ḥasan mursal in tafsīr. No garden-of-forking-paths shift — the
  analysis matched the pre-reg exactly.

**Files produced this pass:** 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings,
07-cross-references, JOURNAL (this). (00/01/02 + pre-reg + script + csv/Q094-F-01.json from Pass 1, re-run/verified.)

**Verdict:** Q094-F-01 = Arm A CONFIRMED (corpus-unique single-fāʾ adjacency) + Arm B CONFIRMED (global
min-edit-1 of 5,821; 0 exact-verbatim adjacencies; p_perm 0.0003/0.0001) + Arm C CONFIRMED (definite-ʿusr /
indefinite-yusr asymmetry, root-Jaccard 1.0). Honest, equal-prominence; clean pass, no pre-commit violation.

**Queued follow-ups:** Q094-F-02 (corpus-wide near-verbatim-adjacent-reprise census: is the edit-2 family
{Q74:19-20, Q75:34-35, Q82:17-18, Q102:3-4} a coherent class, and is Q94:5-6 the only *consolation* member?);
Q094-F-03 (Q93↔Q94 pericope-level paired-unit test: last-k of Q93 vs first-k of Q94 vs scrambled-adjacency null);
Q094-F-04 (is Q94 the corpus's densest 2nd-person *-ka* surah per word-token?).
