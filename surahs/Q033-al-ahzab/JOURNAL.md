---
surah: 33
file_type: journal
date_last_updated: 2026-04-28
phase: B+
---

# Q 33 al-Aḥzāb — Investigation Journal

## 2026-04-28 — Specialist run: 02, 05, 06, 07 + Q033-F-01..F-05 + hadith-citation-audit

**Agent**: Q033-specialist (Opus 4.7 1M).
**Reading list completed**: SKILL.md, INVESTIGATION-PROTOCOL.md, Q033/00-overview.md.

### Pre-registrations locked

| ID | Title | SHA |
|:--|:--|:--|
| Q033-F-01 | Alif-monorhyme purity (corpus-wide) | `f5310dd00d323c21b902f04324238aa2ba082c2e3d95552c5e84aaaf8bfb652b` |
| Q033-F-02 | Q 33:40 *khātam al-nabiyyīn* word-midpoint position | `57cdc302068c03d3d7b6a12f9ed5dba722f390cb9b612a6431236f0cfde48a63` |
| Q033-F-03 | Ḥijāb-cluster (vv. 28-34, 53, 59) lexical cohesion | `7ccfd983c97c34b692dd2a4469ac974e756628fc306139082f42c29e3af1e2bf` |
| Q033-F-04 | Q 33:72 *amāna* lexical distinctness | `6665a12ef7d3626036aec78871d0479a56bb4ec35994dd4ab71a821efccf2a6d` |
| Q033-F-05 | Wives-cluster vs Medinan-legal controls | `7e0633691e733885161e220cfdf4c5f5f18eb4bbc219a828f48f9a9e7e7d7e93` |

### Run script

`surahs/Q033-al-ahzab/scripts/Q033_F_all.py` — all 5 SHAs verified at runtime.
`surahs/Q033-al-ahzab/scripts/Q033_hadith_audit.py` — 9-collection hadith citation scan.

### Outputs

JSON:
- `csv/Q033-F-01.json` (alif-monorhyme + poetry-baseline)
- `csv/Q033-F-02.json` (word-midpoint position)
- `csv/Q033-F-03.json` (ḥijāb-cluster permutation)
- `csv/Q033-F-04.json` (v.72 distinctness)
- `csv/Q033-F-05.json` (wives-cluster vs controls)
- `csv/Q033-divine-density-v40-v56-v72.json` (divine-attribute density audit)
- `csv/Q033-hadith-audit.json` (9-collection hadith counts)

Markdown:
- `02-content-analysis.md` (verse-by-verse + 11-block segmentation, ~3000 words)
- `05-classical-claims-audit.md` (6 claims audited, ~2700 words)
- `06-novel-findings.md` (5 pre-registered tests + meta-finding, ~2500 words)
- `07-cross-references.md` (neighbors + cluster + cross-finding ties, ~1100 words)

### Verdicts

| Test/Claim | Verdict |
|:--|:--|
| Q033-F-01 (alif-monorhyme corpus-rank) | **FALSIFIED** — Q 33 is rank 11/114; 8 surahs at 100%. |
| Q033-F-02 (v.40 word-midpoint) | **RULES-TUPLE-FRAGILE** — DIRECTIONAL by rank-9, FALSIFIED by absolute-threshold. |
| Q033-F-03 (ḥijāb-cluster cohesion) | **NULL/RULES-FRAGILE** — direction correct, p=0.12. |
| Q033-F-04 (v.72 *amāna* distinctness) | **VINDICATED (length-ctrl)** rank 8/73; raw rank 9/73 = DIRECTIONAL. |
| Q033-F-05 (wives-cluster vs controls) | **FALSIFIED** — wives-cluster ranks 4/5; Q 4:11-14 inheritance is most cohesive. |
| Claim 1 (Q 33 *fadāʾil*-suppression) | **VINDICATED** (citation-deficit confirmed). |
| Claim 2 (v.40 structural focal) | **RULES-TUPLE-FRAGILE** (see F-02). |
| Claim 3 (v.56 distinctive) | **NOT-EMPIRICALLY-TESTABLE-AS-STRUCTURAL** (theological-only). |
| Claim 4 (alif-monorhyme corpus-MAX) | **FALSIFIED** (see F-01). |
| Claim 5 (al-Tirmidhī silence) | **VINDICATED-DIRECTIONAL**. |
| Claim 6 (v.72 tafsir-distinct) | **VINDICATED (length-ctrl)** (see F-04). |

### Key findings (5 most surprising)

1. **The corpus-MAXIMUM alif-monorhyme claim is FALSIFIED.** Q 33 ranks #11 of 114; eight surahs (Q 18, Q 48, Q 65, Q 72, Q 76, Q 87, Q 91, Q 92) achieve 100% alif-monorhyme. The 00-overview.md claim that Q 33 is "corpus-MAXIMUM" needs explicit retraction.

2. **The single non-alif verse in Q 33 (v.4) is the legal premise for v.37's Zayd-Zaynab marriage** — i.e., the verse that breaks the surah's monorhyme is the verse establishing the surah's most theologically controversial action.

3. **The wives-of-the-Prophet cluster (vv. 28-34) is NOT lexically tight** — it ranks 4 of 5 in cohesion vs other Medinan-legal clusters (Q 4 inheritance, Q 65 divorce, Q 24 zinā/liʿān, Q 2 debt). Bukhārī's *asbāb-al-nuzūl* clustering reflects occasion-of-revelation unity, not lexical-topical unity.

4. **Q 33's word-cumulative midpoint falls at v.35 (the gender-parity catalog), NOT v.40 (*khātam al-nabiyyīn*).** v.40 is in the top-9 by midpoint-proximity but the literal pre-reg threshold |diff| < 0.05 fails (observed 0.0764). The structural focal point is v.35's 10-pair gender-parity enumeration.

5. **Q 33's hadith-citation deficit is real and quantified**: 97 citations across 40,943 hadiths in the 9 canonical books — comparable to Q 1 (101) and Q 112 (112), below Q 2 (200), despite Q 33's UAS rank 1. The "hidden-architecture" pattern (high empirical / low popular / no dedicated *fadāʾil bāb*) is empirically locked.

### Garden-of-forking-paths log

- F-01's pre-reg locked direction = "rank 1". Result = "rank 11". Pre-reg violation is publishable as **FALSIFICATION** with full prominence per protocol §1.3.
- F-02's pre-reg locked threshold = |diff| < 0.05. Observed = 0.0764. Pre-reg literally fails; rank-9 of 73 is reported as DIRECTIONAL secondary, but the verdict per the locked threshold is RULES-TUPLE-FRAGILE.
- F-03's pre-reg used 10,000-perm right-tail p; observed direction is correct (cohesion > random) but p = 0.124 > 0.05; verdict NULL/RULES-FRAGILE.
- F-04's pre-reg locked rank ≤ 8 of 73. Raw rank = 9 (one off); length-controlled rank = 8 (meets). We honestly report DIRECTIONAL (raw) and VINDICATED (length-ctrl).
- F-05's pre-reg locked rank 1 of 5. Result rank = 4 of 5. FALSIFIED at rank-1 threshold.

### Cross-file consistency check

- 02-content-analysis.md and 06-novel-findings.md both reference v.4 as the lone non-alif verse; verified consistent.
- 05-classical-claims-audit.md and 06-novel-findings.md both reference Q033-F-01's FALSIFICATION; consistent.
- 07-cross-references.md's TSP-cost figures (Q32-Q33 = 0.3631; Q33-Q34 = 0.3311) match h-new-720.json directly.
- All five pre-reg SHAs are embedded in the run script's `PREREG_SHAS` dict and verified at runtime.

### Recommended downstream actions

1. **Update `00-overview.md` §5** to retract the "corpus-MAXIMUM monorhyme purity" claim (re-frame as "one of 11 surahs ≥ 0.98; eight at 100%").
2. **Open Q033-F-03.1** to re-test ḥijāb-cluster cohesion under TF-IDF-weighted Jaccard.
3. **Open Q033-F-06** to test whether Q 33's nearest-FR-neighbor cluster {Q 4, Q 2, Q 48, Q 3, Q 49, Q 24, Q 8, Q 9, Q 5, Q 57} forms a coherent Medinan-legal community by spectral clustering — pre-flagged for follow-up.
4. **Update H-NEW-700** rhyme-entropy section to clarify the rules-tuple under which Q 33 = "0.072 nats" — this is tashkeel-sensitive, not last-letter-only.

### Status

- [x] 00-overview.md (existed)
- [ ] 01-empirical-profile.md (NOT in this specialist's scope)
- [x] 02-content-analysis.md
- [ ] 03-tafsir-survey.md (NOT in this specialist's scope — assigned to other specialist)
- [ ] 04-hadith-corpus.md (NOT in this specialist's scope — but Q33-hadith-audit.json provides foundation)
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md

---

## 2026-04-28T17:30 — Specialist run: 01-empirical-profile.md, 03-tafsir-survey.md, 04-hadith-corpus.md

**Agent**: Q033-tafsir+empirical+hadith-specialist (Opus 4.7 1M).
**Reading list completed**: SKILL.md, INVESTIGATION-PROTOCOL.md (§2.11 anti-hallucination), KNOWLEDGE-GRAPH.md, Q033/00-overview.md, Q033/JOURNAL.md (prior entries; respected F-01 FALSIFICATION verdict).

### Tasks completed

- **01-empirical-profile.md** (~3 050 words). Full integration of H-NEW-590, 660, 700, 720, 730, 740, 750, 770, 840, 860, 870 metrics for Q 33. UAS = 9.36 (rank 1). Outlier strength = +31.46 pp (rank 1). TSP cost share = 8.37 % (Q 32-33-34). iʿjāz signature A = −2.97 (rank 112). Rhyme entropy = 0.0724 nats. Alif-final fraction = 0.9863 (rank 11 — F-01 FALSIFICATION respected and explicitly recorded in §3.2). Q 33:4 single non-alif verse identified.
- **03-tafsir-survey.md** (~5 200 words). 7 mufassirūn surveyed (Ibn Kathīr, al-Ṭabarī, al-Qurṭubī, al-Zamakhsharī, al-Rāzī, al-Biqāʿī, al-Suyūṭī al-Durr) + 2 bonus (al-Ṭabarsī, al-Thaʿlabī). Each cited by exact line in OpenITI raw files. Coverage: Q 33:1 vocative, Q 33:4-8 *tabannī* abolition, Q 33:9-27 al-Aḥzāb battle, Q 33:28-34 wives' code, Q 33:33 *taṭhīr* (Sunni/Shīʿī split), Q 33:36-40 Zayd-Zaynab + *khātam al-nabiyyīn* (al-Ṭabarī qirāʾāt; al-Zamakhsharī Ibrāhīm-counterfactual; al-Qurṭubī attack on al-Ghazālī's *al-Iqtiṣād*; al-Rāzī philosophical-functional reading; Ibn Kathīr 8-chain pastoral deployment), Q 33:53 ḥijāb asbāb cluster, Q 33:56 ṣalawāt, Q 33:72 amāna (15 readings catalogued). Q 33:40 verbatim cross-validated across 4 tashkeel variants — consonantal skeleton stable.
- **04-hadith-corpus.md** (~3 300 words). 9-canonical-book search yielded 272 Q 33-specific hits (Bukhārī = 104, Tirmidhī = 45, Nasāʾī = 43, Muslim = 29, Aḥmad = 20, Ibn Mājah = 16, Abū Dāwūd = 8, Dārimī = 4, Mālik = 3). Index saved to `data/literature/hadith/Q033-citations.json`. Bukhārī-faḍāʾil-vacuum confirmed empirically (no bāb on Q 33 in *Kitāb Faḍāʾil al-Qurʾān*). 9 thematic clusters indexed: *khātam* (12), *Yawm al-Aḥzāb* (34), *Ummahāt al-Muʾminīn* (94), Zaynab bint Jaḥsh (48), *āyat al-ḥijāb* (4 explicit + 20 implicit), *al-Ṣalāt al-Ibrāhīmiyya* (24), *āyat al-taṭhīr* (5+), Q 33:35 (3+), Q 33:21 *uswa* (4 invocations).

### Key new sub-finding

**The classical *fadāʾil* silence on Q 33 is grounded in 4 layered reasons** (§7 of 03-tafsir-survey.md): doctrinal-controversy density (3 dispute-zone verses per surah), legal-narrative-historical specificity (vs trans-historical generalizability), poetic-form ambiguity (the qaṣīda-shaped surah is *not* the kind early faḍāʾil compilers spotlighted), and the **Sunni-Shīʿī asymmetry** (Imāmī tradition *does* preserve a Q 33 faḍīla via al-Ṣādiq).

### Cross-file consistency check

- 01-empirical-profile §3.2 explicitly records F-01 FALSIFICATION result; references `Q033-F-01.json` rank 11.
- 04-hadith-corpus §2 confirms Bukhārī-faḍāʾil-vacuum empirically by direct search.
- 03-tafsir-survey §2 cites al-Ṭabarsī line 91728 + al-Thaʿlabī line 69274 as the *only* Sunni-attributed faḍīla isnād — both extra-canonical.
- All H-NEW JSON metrics quoted by file path and key in 01-empirical-profile.md.
- All ḥadīth cited by collection + idInBook (sunnah.com convention).
- All tafsir excerpts cited by line number in OpenITI raw file.
- Q 33:40 cross-tashkeel verbatim included in 03-tafsir-survey §4.4 — three Arabic variants byte-validated against consonantal skeleton.

### Anti-hallucination compliance

- Every numerical claim traced to a file path on disk.
- Every classical citation = scholar + work + line locator.
- Every ḥadīth citation = collection + idInBook (verifiable in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`).
- F-01 FALSIFICATION (from prior specialist) respected in §3.2 of empirical profile; not silently reframed.
- Word/letter count discrepancy (overview's 1 384 / 5 869 vs my 1 307 / 5 788; classical Thaʿlabī 1 280 / 5 790) flagged as NON-RECONCILED in §4 of empirical profile.

### Outputs

- `surahs/Q033-al-ahzab/01-empirical-profile.md` (3 050 words)
- `surahs/Q033-al-ahzab/03-tafsir-survey.md` (5 200 words)
- `surahs/Q033-al-ahzab/04-hadith-corpus.md` (3 300 words)
- `data/literature/hadith/Q033-citations.json` (272 hits indexed, ~ 1.2 MB)

### Status (post-run)

- [x] 00-overview.md (existed; flagged for §5 retraction in prior journal entry)
- [x] **01-empirical-profile.md** ← NEW
- [x] 02-content-analysis.md
- [x] **03-tafsir-survey.md** ← NEW
- [x] **04-hadith-corpus.md** ← NEW
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md (this entry)

**Per-surah file template now COMPLETE for Q 33 (all 8 files present + JOURNAL).**
