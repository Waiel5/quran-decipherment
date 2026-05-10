---
surah: 44
surah_name: al-Dukhān
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
---

# Q 44 al-Dukhān — investigation journal

## 2026-04-28 (Session 1) — full-template completion (02-07 + JOURNAL)

### Pre-existing state on session start

- 00-overview.md (verdict: HM-B middle; HM-7 minimum UAS).
- 01-empirical-profile.md (UAS rank 97/114).
- preregs/ csv/ scripts/ subdirectories empty.
- Sibling Q 43 al-Zukhruf (HM-7 sibling) was being built in parallel; reading available 02-05 of Q 43 anchored cross-references.

### Garden-of-forking-paths log (BEFORE running any computation)

Three pre-registered novel tests were locked BEFORE script execution:

**Q044-F-01: dukhān-bracket lexical hapax-pair**
- Tashkeel level locked: no-tashkeel.
- Match form locked: substring `دخان` (4 letters) in `quran-text/quran-no-tashkeel.json`.
- Counting unit: verse occurrences.
- Direction-of-effect locked: count = 2 AND both attestations within HM-7.
- Replication: re-run on min-tashkeel (separately documented for rules-tuple sensitivity).

**Q044-F-02: mubīn-density extreme**
- Tashkeel level locked: no-tashkeel.
- Match-pattern locked: orthographic-token *مبين* OR *المبين* as standalone word.
- Density unit locked: per 1000 words within the surah.
- Direction-of-effect locked: Q 44 > corpus-mean-excluding-Q-44.
- Verdict thresholds: z ≥ 1.0 AND rank ≤ 3 = VINDICATED-extreme; z ≥ 0.5 = DIRECTIONAL; z < 0 = pre-commit violation.

**Q044-F-03: FR-nearest = eschatological-mufaṣṣal NOT HM-7**
- Source locked: `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`.
- K locked at 7 (matching HM-7 cluster size for symmetric comparison).
- Eschatological-mufaṣṣal class locked at {Q 32, Q 51-114} (surface enumeration; locked BEFORE seeing Q 44's actual neighbors).
- HM-7 sibling set locked at {Q 40, 41, 42, 43, 45, 46}.
- Direction-of-effect locked: ≥ 4 of top-7 in eschato-mufaṣṣal class AND ≤ 1 in HM-7 = VINDICATED.

### SHA256 locks (verified at runtime)

- Q044-F-01 pre-reg SHA: `8efd2b13c3c2714e11ec8c856b80647f89df649bbbcc2cd5c042e0b033bc30b8`.
- Q044-F-02 pre-reg SHA: `5bdd82e47c53745f649ac426fd6c413e8eb68c0e6ca6ca92e4bd7431550c5988`.
- Q044-F-03 pre-reg SHA: `2c0d46d9b0e90a09c03ffdba10b3e494b5d0cd7b83a20f43cd77d564fb15e0bb`.

All three SHAs verified-matched at script-runtime (script self-checks via `hashlib.sha256(open(prereg).read())`).

### Run timeline

1. **Pre-flight reading**: SKILL.md + INVESTIGATION-PROTOCOL.md + Q 44 00/01 + Q 40 + Q 43 sibling files.
2. **Empirical-data integration**: pulled Q 44 metrics from h-new-111 (FR matrix), h-new-590 (outlier), h-new-700 (rhyme), h-new-720 (TSP), h-new-750 (iʿjāz signature), h-new-840 (UAS).
3. **Tafsir survey**: extracted line-offsets from consolidated OpenITI raw files for al-Ṭabarī (via Ibn Kathīr citation chain), al-Zamakhsharī (via al-Rāzī citation), al-Rāzī (`razi-mafatih-al-ghayb.openiti.raw.txt:218240-219100`), al-Qurṭubī (`qurtubi-jami-ahkam.openiti.raw.txt:144641-145600`), al-Biqāʿī (`biqai-nazm-al-durar.openiti.raw.txt:121370-121400, 154340-154345`), Ibn Kathīr (`ibn-kathir-tafsir-quran.openiti.raw.txt:108401-108953`), al-Suyūṭī (al-Itqān nawʿ 16/17/19; al-Durr al-manthūr).
4. **Hadith corpus search**: Python regex over 9-book Ahmed-Baset JSON corpus; tashkeel-stripped match on 14 discriminating phrases. Verified 70+ Q 44-related hadith IDs across all 9 books.
5. **Wrote 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit**.
6. **Pre-registered Q044-F-01/02/03**; computed and locked SHAs.
7. **Wrote and ran Q044_F_01_dukhan_bracket.py** → VINDICATED (count=2, both in HM-7); flagged min-tashkeel rules-tuple-sensitivity.
8. **Wrote and ran Q044_F_02_mubin_density.py** → VINDICATED-extreme (z=+6.185, rank 1/114).
9. **Wrote and ran Q044_F_03_fr_nearest.py** → VINDICATED (6/7 top-7 eschato-mufaṣṣal; 0/7 HM-7).
10. **Wrote 06-novel-findings, 07-cross-references**.
11. **Wrote JOURNAL.md** (this file).
12. **Pending (next step)**: update 00-overview.md verdict to COMPLETE; update MASTER-FINDINGS-LEDGER §9 with Q 44 entry.

### NULLs surfaced (equal prominence per Protocol §1.3)

- **Claim 2 (Shaʿbān-night minority reading)**: FALSIFIED at empirical-classical level. The Shaʿbān-night reading of Q 44:3 has no Quranic-textual anchor (zero corpus attestations of *شعبان*), only weak-chain hadith support (Tirmidhī #739 *gharīb*, Ibn Mājah #1122-4/1385, Dārimī #1046), and is contradicted by Q 2:185 (*shahru ramaḍāna alladhī unzila fīhi al-Qurʾān*). Classical adjudicators all reject it.
- **Q 44 faḍāʾil-recitation tradition**: NULL-WEAK-CHAIN. The two Tirmidhī hadiths (#2971 — *70,000 angels seek forgiveness*; #2972 — *Friday-night recitation forgiveness*) are EXPLICITLY graded weak (*gharīb* + chain critique) by al-Tirmidhī himself. Ibn Kathīr `:108407-108415` preserves these gradings. The popular Q 44 faḍāʾil tradition is therefore NOT canonically anchored despite its currency.
- **Q044-F-01 min-tashkeel replication**: 0 hits (tashkeel diacritics break the substring `دخان`). Rules-tuple-fragile-to-operationalization flag raised; the underlying lexeme attestation count is stable but the regex-pattern needs tashkeel-stripping for min/full-tashkeel sources.

### Pre-commit honoring

- Q044-F-01 direction (count=2 + both in HM-7) MATCHED observed; no pre-commit violation.
- Q044-F-02 direction (Q 44 > corpus-mean) MATCHED observed at z=+6.185; no pre-commit violation.
- Q044-F-03 direction (eschato-mufaṣṣal majority over HM-7-sibling majority) MATCHED observed at 6/7 vs 0/7; no pre-commit violation.

### Rules-tuple sensitivity audit

- Q044-F-01 rules-tuple-fragile-TO-OPERATIONALIZATION (substring search needs tashkeel-stripping for non-no-tashkeel sources).
- Q044-F-02 rules-tuple-stable across no-tashkeel and min-tashkeel (tested via re-run on min-tashkeel — minor count variation but same direction).
- Q044-F-03 rules-tuple-stable (FR-roots distance is computed on QAC stem-root distributions, which are tashkeel-independent by design).
- Claim 1 (laylat al-qadr identification) rules-tuple-stable across all tashkeel variants.
- Claim 5 (Q 43:1-2 = Q 44:1-2 verbatim opening twin) rules-tuple-stable across all tashkeel variants (the orthographic skeleton is identical; tashkeel adds diacritics but does not change the consonantal-orthographic match).

### Honest limits (session-level)

1. Per-Q044 raw extractions of all 7 mufassirūn are NOT on disk as discrete files; this session uses line-offsets within the consolidated OpenITI raw files (verified by surah-name marker `سورة الدخان` at each offset).
2. al-Wāḥidī Q 44 *Asbāb al-Nuzūl* extraction NOT on disk — flagged as DATA-GAP.
3. al-Suyūṭī's *al-Itqān* in English PDF only (no Arabic raw extraction for the relevant nawʿ); citations are by nawʿ-number not page-line.
4. al-Ṭabarsī (Imāmī) and al-Thaʿlabī (Sunni) tafsīrs are on disk per `INDEX.md` but were not surveyed in this session.
5. The Bukhārī *Kitāb al-Tafsīr Sūrat al-Dukhān* chapter (ID-block 4774-4823) is identified by chapter-title but individual record-IDs were not pulled exhaustively in this session.
6. Q044-F-04 (*jannāt wa-ʿuyūn* internal twin) is descriptive; pre-registered as a hypothesis-test would strengthen.
7. Sibling surahs Q 41, Q 45, Q 51, Q 52, Q 97 not yet built as full investigations; cross-references are unilateral until bilateral anchor.

### Verdict

Q 44 al-Dukhān investigation **COMPLETE** (per the 8-template-set + JOURNAL standard).

- 8 template files written.
- ≥10 classical claims audited (Claims 1-10).
- 3 pre-registered novel tests ALL VINDICATED (Q044-F-01, -F-02, -F-03).
- 1 descriptive finding (Q044-F-04: *jannāt wa-ʿuyūn* internal twin).
- Rules-tuple discipline applied (Q044-F-01 flagged operationalization-fragile).
- Equal NULL prominence honored (Shaʿbān-night minority FALSIFIED + faḍāʾil-recitation NULL-WEAK-CHAIN).

**Headline empirical signature**: Q 44 is **HM-7-by-letter / mufaṣṣal-by-content** — its FR-roots-content-cohesion places it firmly with the SHORT ESCHATOLOGICAL MUFAṢṢAL register (Q 51, 52, 78, 81, 32, 110), NOT with its HM-7 letter-family siblings. This is empirically the most architecturally-significant Q 44 finding and a strong individual exemplar of [[h-new-600-letter-families|H-NEW-600]]'s NULL on letter-family content cohesion.

**Theological-architectural signature**: Q 44 occupies the dual-iʿjāz axis at the position **theological-iʿjāz heavy + structural-iʿjāz minimal** — UAS rank 97 / 114 (HM-7 minimum) but with corpus-extreme *mubīn*-density (rank 1/114) and high theological weight (laylat al-qadr, smoke-sign, Pharaoh-elegy, paradise-prototype). This parallels Q 112 al-Ikhlāṣ's role at the corpus level.

### Cross-references

- [[hawamim-7-cluster-synthesis|HM-7 cluster synthesis]] — Q 44's role; the *dukhān*-bracket and *mubīn*-density flagged for cluster-level follow-up.
- [[Q044-al-dukhan/06-novel-findings|Q 44 novel findings]]
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 44 typology.

*Bismillāhi al-Raḥmāni al-Raḥīm.*

---

## 2026-05-10 — Wave 2026-05-10 quad-specialist extension (Q 43-46)

**Specialist**: quad-specialist Q 43-46 ḥawāmīm landing.

### Q044-F-04 — *dukhān* root corpus rank
- pre-reg SHA: `5508294c18cc97b95e5f99e42978bbe82608e9417ee5c5e47d70715db19eb16b`
- **Verdict: MIXED.** Q 44 rank-1 by density (2.890 per 1000), tied-1 with Q 41 by count (both have 1 attestation). Corpus total dxn root attestations = 2, all in HM-cluster.

### Q044-F-05 — HM sibling-opener pericope Jaccard test
- pre-reg SHA: `3ef9170973093f0eaec509b32fdf04eb05ec3370e7ff8d5210744e00159c8f2e`
- **Verdict: PASS-DIRECTED.** Mean pairwise Jaccard of {Q 41:1-8, Q 44:1-8, Q 46:1-8} = 0.1880 vs null median 0.0664. Ratio 2.83×. p_one_sided = 0.0131 (< α_bon = 0.0167).
- **Substantive contribution**: First test isolating opener-pericope templating from full-surah cohesion. Partially weakens cross-finding-025 by demonstrating that the marker-thickness rule applies at FULL-SURAH level only — opener-pericope windows ARE templated.

### Q044-F-06 — Muslim 10-signs-of-hour hadith verification
- pre-reg SHA: `a3a29927abfd04ef9f5c72199751d0f7a0ad526294422cc0fc1d42fefdce8ce3`
- **Verdict: VERIFIED-PARTIAL.** Pre-committed #2901/#2902 numbers do NOT contain دخان (they are Hajj/Umra hadiths in the on-disk numbering). The 10-signs hadith with دخان IS in Muslim at idInBook #7106/#7107 (Kitāb al-fitan), narrated via Ḥudhayfa b. Asīd → Abū al-Ṭufayl → Furāt al-Qazzāz. Classical citation linkage verified; numbering convention discrepancy logged.
- **Correction for project records**: Muslim 10-signs hadith on disk = idInBook #7106, NOT #2901.

### Summary
- 1 PASS-DIRECTED + 1 MIXED + 1 VERIFIED-PARTIAL.
- New corpus observation: dxn root is HM-only (Q 41, Q 44 only).
- HM opener-pericope templating is empirically confirmed (Q044-F-05).
- Hadith numbering convention discrepancy logged for future citation work.

