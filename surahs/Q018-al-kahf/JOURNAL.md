---
surah: 18
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — Wave D launch (Q 18 al-Kahf full 9-file template + 4 pre-regs/scripts/JSONs)
---

# Q 18 al-Kahf — Investigation Journal

## 2026-04-28 — Wave D specialist run

### Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/` (most-polished 9-file template — used as primary structural reference)
- `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` (single-narrative comparator — for narrative-purity cross-reference)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json` (all Q 18 values pulled)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-268.json` (Q 18 four-narrative spacing-geometry prior)

### H-NEW data integration

Pulled and integrated from on-disk JSON artifacts:

- **H-NEW-840**: Q 18 UAS = 0.046 (rank 46/114 — middle of corpus); component breakdown: |outlier| = 0.39, max_cost = 0.0279, |sig_A| = 2.395.
- **H-NEW-590**: outlier-strength Δ = +0.39 pp (rank 31/114, WEAK_OUTLIER); window {15-21}.
- **H-NEW-720**: Q 17-18 cost rank 86/113 (cheap); Q 18-19 cost rank 92/113 (cheap). Q 18 is cheaply-bracketed — INVERSE of Q 24's expensively-bracketed geometry.
- **H-NEW-750**: sig_A = -2.395 (rank 110/114, 5th-from-bottom = extreme anti-iʿjāz al-fawāṣil); sig_B = -1.922 (rank 110); rhyme entropy 0.052 nats (rank 113/114, second-lowest); top final letter = alif at 99.09%.
- **H-NEW-111**: mean FR distance to corpus 1.0344 (rank 19/114 — high content-distance, well above corpus mean 0.9235); FR-nearest = Q 7 al-Aʿrāf (0.871) — both Mūsā-narrative surahs; FR-farthest = Q 55 al-Raḥmān (1.271).
- **H-NEW-268**: Q 18 four-narrative spacing-geometry DIMENSION-SPECIFIC verdict; joint palindromic-expansion cell (gaps 23-28-23) survives Bonferroni-3 at p = 0.00802. Locked four-narrative blocks: vv. 9-26 / 32-44 / 60-82 / 83-98.

### Q 18 signature facts verified

- 110 verses (Hafs-Kufan); cross-validated against `quran-text/quran-no-tashkeel.json`.
- 1,583 words (no-tashkeel orthographic, mushaf-stripped); 6,552 letters.
- 1,057 root-tokens (rank 12/114 by total root-tokens); 369 distinct roots.
- Meccan, rev-order #69 (al-Suyūṭī chronology) — cross-validated at `data/revelation-order.csv`.
- NO muqaṭṭaʿāt (verified by inspection of v.1 = *al-ḥamdu lillāh* opening).
- *al-ḥamdu lillāh* opener cluster member (Q 1, 6, 18, 34, 35).
- 99.09% alif-monorhyme (109/110); single non-alif verse = v. 13 (*hudan*, ending in alif maqṣūra ى).
- Final word of v. 110 = أحدا (*aḥadan*) ending in alif — mirrors v. 26's closing fāṣila *aḥadan*.

### 4 narrative blocks (verified)

| Block | Verses | Words | Root-tokens | Subject |
|:-:|:-:|:-:|:-:|:--|
| N1 | 9-26 (18 vv.) | 336 | 220 | Aṣḥāb al-Kahf |
| N2 | 32-44 (13 vv.) | 168 | 113 | Two gardens |
| N3 | 60-82 (23 vv.) | 302 | 202 | Mūsā-Khaḍir |
| N4 | 83-101 (19 vv.) | 213 | 136 | Dhū al-Qarnayn |

Frame/bridge verses (vv. 1-8, 27-31, 45-59, 102-110) account for the remaining 38 verses.

### Pre-registered novel tests run (4 pre-regs)

| Pre-reg | SHA-head | Test | Verdict |
|:--|:--|:--|:--|
| Q018-F-01 | `7c17b2377223` | Four-narrative balance (max/min ratios for verses, words, root-tokens) | **NULL with PRE-COMMIT VIOLATION on cells B and C** |
| Q018-F-02 | `1144161236f5` | Narrative-purity rank vs Q 12 (Q 18 in top-25%, < Q 12) | **CONFIRMED on both directions** (Q 18 rank 7/114; Q 12 rank 1/114) |
| Q018-F-03 | `d983419073d2` | 99%-alif-monorhyme + v.110 alif-closure | **CONFIRMED on both cells** (alif-frac 99.09% at p ≈ 4.45 × 10⁻⁸⁸; v.110 ends in alif) |
| Q018-F-04 | `271348cf1154` | Mūsā-Khaḍir block (N3) lexical hapax > random | **NULL with PRE-COMMIT VIOLATION** (N3 hapax 39 < null median 44; p = 0.74) |

**Honest tally**: 2 of 4 CONFIRMED; 2 of 4 NULL with explicit pre-commit-violation prominence. Q018-F-04 has a follow-on observation (N1 = 55 hapax > N3 = 39; cave-companions narrative is the most-hapax-rich block) — reported as POST-HOC, NOT a confirmed finding. This is the project's discipline at work.

### 7 classical claims audited (per `05-classical-claims-audit.md`)

| Audit | Verdict |
|:--|:--|
| 1. al-Biqāʿī's four-fitan reading | VINDICATED on thematic, FALSIFIED on quantitative-balance |
| 2. al-Qurṭubī "Meccan by consensus" | VINDICATED at all empirical signatures |
| 3. First-ten / last-ten Dajjāl-protection variant | RULES-TUPLE-FRAGILE on textual claim; VINDICATED on architectural sub-claim |
| 4. *aḥadan*-fāṣila ring (v. 26 ↔ v. 110) | VINDICATED at exact-text level |
| 5. "8-surah 100% alif-monorhyme cluster" | RULES-TUPLE-FRAGILE; only 4/8 are 100%-alif under strict grapheme convention |
| 6. al-Bāqillānī *iʿjāz al-fawāṣil* applied to Q 18 | FALSIFIED locally (sig_A rank 110/114); VINDICATED globally (corpus r=-0.86) |
| 7. al-Khaḍir as prophet (Sunnī majority) | NOT-EMPIRICALLY-RESOLVABLE on prophet-vs-walī; VINDICATED on *ʿilm ladunī* sub-claim (Q 18:65 corpus-unique) |

### Tafsir survey: 9 mufassirūn

al-Ṭabarī, al-Thaʿlabī, al-Ṭabarsī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Biqāʿī, al-Suyūṭī. All Q 18 content extracted directly from on-disk OpenITI raw text (no per-surah pre-extracts available — DATA-GAP flagged in `03-tafsir-survey.md` §0).

**Key tafsir contributions**:
- al-Qurṭubī: Meccan by consensus + Friday-recitation tradition + 10-verses-Dajjāl tradition.
- al-Rāzī: Q 18 is third of five *al-ḥamdu lillāh*-openers; *maqṣūd* = spiritual cultivation through revelation.
- al-Biqāʿī: four-narratives = four classical fitan (al-dīn, al-māl, al-ʿilm, al-mulk).
- al-Ṭabarī: asbāb of Quraysh's three questions to Madinan rabbis (cave-companions + Dhū al-Qarnayn + al-rūḥ; Q 18 answers first two, Q 17:85 answers third).
- al-Zamakhsharī: *ʿiwajan / qayyiman* as canonical *iqāʿ* example (al-Sakkākī's complementary-pair fāṣila-doctrine).

### Hadith corpus: all 9 books queried

Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī. Headline:
- **Mūsā-al-Khaḍir narrative**: Bukhārī #122, #3261, #3262 — foundational identification of unnamed *ʿabd* as al-Khaḍir; Saʿīd b. Jubayr ← Ibn ʿAbbās ← Ubayy b. Kaʿb chain.
- **10-verses-Dajjāl-protection**: Muslim #1775 (first ten, ṣaḥīḥ); Abū Dāwūd #4325 (variant: first OR last OR closing-verses preserved at same Qatāda layer).
- **Friday-recitation**: al-Dārimī #2641 (Abū Saʿīd al-Khudrī) — earliest 9-book attestation; al-Bayhaqī, al-Ḥākim outside the 9 books.
- **Yājūj-Mājūj eschatology**: 10 hadiths in Bukhārī, 7 in Muslim — fully elaborated Last-Day narrative.
- **Aṣḥāb al-Kahf**: only 1 corpus mention (Tirmidhī #2308 — peripheral mention in long Nawwās Dajjāl-narrative).

### DATA-GAPS flagged

1. **Per-tafsir Q018 extracts**: no `data/literature/classical-tafsir/raw/{tabari,ibn-kathir,qurtubi,zamakhshari,razi,biqai,suyuti}-Q018.txt` files exist on disk (only Q001, Q002, Q009, Q010, Q017 have these). All Q 18 tafsir extracts are sourced directly from full-tafsir openiti raw text. **Recommendation**: commission per-tafsir-Q018 extracts for consistency with other completed surahs.

2. **H-NEW-66 verse-twin network for Q 18**: not directly indexed in on-disk artifacts. Verse-twin cross-references in `07-cross-references.md` §4 are content-derived, not algorithmically computed.

3. **Q 18 specific Q018-citations.md**: not found in `/Users/grey/Downloads/quran/data/literature/hadith/`. Other surahs have Q{NNN}-citations.md (Q001, Q002, Q009, Q033). Future Q 18 hadith-corpus deep-dive should compile this.

4. **al-Bayhaqī / al-Ḥākim Friday-recitation traditions**: outside the 9-book scope; not on-disk in the ahmedbaset-json corpus. Documented but not directly verified.

5. **Q 19, Q 21, Q 26 multi-narrative comparators**: deep-dives not yet started; the multi-narrative-vs-single-narrative typology is operationalized via Q 18 / Q 12 only.

### Files produced

- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/00-overview.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/01-empirical-profile.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/02-content-analysis.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/03-tafsir-survey.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/04-hadith-corpus.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/05-classical-claims-audit.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/06-novel-findings.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/07-cross-references.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/JOURNAL.md` (this file)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/preregs/Q018-F-01-narrative-balance-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/preregs/Q018-F-02-narrative-purity-vs-Q12-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/preregs/Q018-F-03-alif-monorhyme-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/preregs/Q018-F-04-musa-khadir-hapax-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/scripts/Q018_F_01_narrative_balance.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/scripts/Q018_F_02_narrative_purity.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/scripts/Q018_F_03_alif_monorhyme.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/scripts/Q018_F_04_musa_khadir_hapax.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/csv/Q018-F-01.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/csv/Q018-F-02.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/csv/Q018-F-03.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q018-al-kahf/csv/Q018-F-04.json` (NEW)

Plus updates to:
- `/Users/grey/Downloads/quran/KNOWLEDGE-GRAPH.md` — Q 18 navigation entry (Wave D).
- `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` §9 — Wave-D Q 18 entry.

### Garden-of-forking-paths log

The four pre-regs were locked BEFORE running. The pre-reg drafts went through the following decision-points:

1. **Q018-F-01 (narrative-balance)**: original draft asked "are the 4 narratives more balanced than expected"; this was locked as a one-tailed test (observed-ratio < null-median). The empirical result was the OPPOSITE direction — the narratives are LESS balanced than random — yielding a pre-commit violation. Published with full prominence.

2. **Q018-F-02 (narrative-purity vs Q 12)**: pre-reg locked Direction A (top quartile) and Direction B (Q 18 < Q 12 narrative-purity). Both confirmed.

3. **Q018-F-03 (alif-monorhyme)**: cell A binomial pre-locked at α_Bonferroni = 0.025 + 95% floor; cell B is a deterministic point-prediction. The 99.09% observed (109/110) makes the pre-reg 95% floor a conservative threshold; passed by 4 percentage points. v.110 alif-closure confirmed by direct text inspection.

4. **Q018-F-04 (Mūsā-Khaḍir hapax)**: pre-reg locked direction (N3 > random-median). Pre-commit violated — N3 has *fewer* hapax-roots than random. The post-hoc observation that N1 (cave-companions) is the highest-hapax block is documented but explicitly NOT treated as a confirmed finding. A follow-on pre-reg "Q018-F-04r" would test whether N1 is the most-hapax-rich, but this would require fresh pre-registration, not post-hoc adjustment.

No methodology shifts mid-run. All SHA-checksums computed at runtime; pre-reg files locked before script execution.

### Honest pre-commit notes

- All four Q018-F-* novel tests had locked pre-regs WRITTEN BEFORE the run. SHA-checksums computed at runtime and embedded in JSON outputs. No post-hoc adjustments to direction-of-effect.
- The 2 NULL findings (Q018-F-01, Q018-F-04) are pre-commit violations and are reported with full prominence per [[INVESTIGATION-PROTOCOL]] §1.3, §1.8.
- The Q018-F-04 follow-on observation (N1 hapax-count = 55) is explicitly documented as POST-HOC, with the recommendation that fresh pre-registration would be required to elevate it to a confirmed finding.
- The 99.09%-vs-100% alif-monorhyme rules-tuple subtlety (Audit 5) is documented; under phonetic-pause convention all 8 surahs in the cluster qualify, under strict grapheme convention only 5 (Q 18, 48, 72, 76, 91 — Q 65 is 91.67%, Q 87 and Q 92 are *yāʾ*-monorhyme).

### Verdict-of-the-investigation

Q 18 al-Kahf is the corpus's **canonical four-narrative + monolithic-rhyme-register exemplar**, sustaining 99.09% alif-monorhyme across 110 verses (the largest-N near-monorhyme surah in the corpus, p ≈ 4.45 × 10⁻⁸⁸ vs corpus mean). Empirically anti-structural-iʿjāz (sig_A rank 110/114, 5th-from-bottom on al-Bāqillānī's fawāṣil-virtuosity axis) yet sits cheaply between its canonical neighbours Q 17 and Q 19 (both adjacency costs in the bottom-third), giving moderate UAS (rank 46/114) with high mean content-distance (rank 19/114). The four-narrative spacing geometry is locked at p = 0.008 Bonferroni-3 ([[h-new-268-kahf-four-narratives|H-NEW-268]]) on the joint palindromic-expansion cell (gaps 23, 28, 23). Two of four pre-registered novel tests CONFIRMED (narrative-purity rank 7/114; alif-monorhyme at p ≈ 10⁻⁸⁸); two NULL with pre-commit violations (4-narrative content-volume balance NOT achieved; Mūsā-Khaḍir block NOT the most-lexically-isolated — N1 cave-companions is). Seven classical claims audited; four VINDICATED, two RULES-TUPLE-FRAGILE / FALSIFIED-with-refinement, one NOT-EMPIRICALLY-RESOLVABLE. Q 18 establishes a fifth typology cell in cross-finding-026's framework: *anti-iʿjāz al-fawāṣil + monolithic-rhyme-register-sustained-over-large-N*. The Q 18 / Q 24 inverse-bracketing-cost pair and the Q 18 / Q 12 single-vs-multi-narrative typology pair are documented. DATA-GAP for per-tafsir-Q018 extracts is flagged.
