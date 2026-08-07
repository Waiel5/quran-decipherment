---
surah: 38
file_type: journal
date_started: 2026-05-07
phase: B+
---

# Q 38 Ṣād — Investigation Journal


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

## 2026-05-07 — Specialist run: 8-file scaffold + 5 pre-registered novel tests

**Agent**: Q038-sad-specialist (Opus 4.7, dispatched per project's INVESTIGATION-PROTOCOL.md).

### Pre-flight reading (per skill protocol)
1. `INVESTIGATION-PROTOCOL.md` — read full.
2. `.claude/skills/quran-investigation/SKILL.md` — read full.
3. `HANDOFF/04-DISCIPLINE.md` — read full.
4. `surahs/Q012-yusuf/` — canonical 8-file template; read overview, empirical-profile, novel-findings, classical-claims-audit, JOURNAL.
5. `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` — referenced.
6. `MASTER-FINDINGS-LEDGER.md` §9 — read.
7. `findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json` — inspected for Q 38 entries.
8. `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` — searched bukhari, muslim, abudawud, tirmidhi for Q 38 / sajdat Sad / David fasting / Solomon / Job material.
9. `data/literature/classical-tafsir/spa5k-tafsir-api/{en-tafisr-ibn-kathir, ar-tafsir-al-tabari, ar-tafseer-al-qurtubi}/38.json` — read full Q 38 commentaries.

### Outputs created (9 main files)

- `00-overview.md` — basic facts, opening formula, prophet-cycle saturation, singleton-letter context, sajda location.
- `01-empirical-profile.md` — UAS rank 59/114; outlier +2.70 pp WEAK; sig_A +1.29 (rank 22); FR-nearest = Q 78 (0.833) then Q 50 (0.854); FR-most-distant = Q 9 (1.236), Q 55 (1.193).
- `02-content-analysis.md` — prophet-cycle structure; David-Solomon-Job triad; Iblīs/Adam panel; *innahu awwāb* triple-anaphora (corpus-eponymous); vocabulary fingerprint.
- `03-tafsir-survey.md` — 7+ mufassirūn (al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, al-Zamakhsharī, al-Rāzī, al-Suyūṭī, al-Biqāʿī, al-Ṭabarsī, modern Farāhī/Iṣlāḥī).
- `04-hadith-corpus.md` — Bukhārī chain for sajdat Ṣād (#4601) verified; David-fasting chains (#1903, #1906, #1908, #3279) verified; Abū Dāwūd #1402 + Tirmidhī #579, #3508 verified.
- `05-classical-claims-audit.md` — 7 claims audited: 5 VINDICATED, 1 DIRECTIONAL/RULES-TUPLE-FRAGILE, 1 PENDING-VERIFICATION (al-Bāqillānī source).
- `06-novel-findings.md` — 5 pre-registered tests: 2 CONFIRMED, 2 DIRECTIONAL, 1 NULL.
- `07-cross-references.md` — neighbor surahs Q 37/39, cluster memberships, H-NEW integration, forward-looking open questions.
- `JOURNAL.md` — this file.

### 5 pre-regs (SHA256-locked)

- `Q038-F-01-singleton-twin-prereg.md` SHA `224aeb8bf99f9fd4cd5a21fb205237c06b2b12b3fbbe701e6b3b59f5ead955f7`
- `Q038-F-02-prophet-saturation-prereg.md` SHA `afdee0bf62018ff88559d56d9f889bd65ee430772d7425dcd0719e980d2c6eb5`
- `Q038-F-03-self-letter-prereg.md` SHA `b437c3e2b0f87b375e2bc2a3757ad21225773c46ca03e0b7371faeb42cb41b61`
- `Q038-F-04-davidic-triad-prereg.md` SHA `cf6f80d637c673638ec6b1f54ed95785d91b0f3c34fa65d74859ca5df2ea8bfb`
- `Q038-F-05-anti-cluster-prereg.md` SHA `376d3229c121dd0677d359e15672a0da821dc3e429044f3c7bf664d994f12b76`

### 5 scripts (SHA-verified at runtime)

- `scripts/Q038_F_01_singleton_twin.py`
- `scripts/Q038_F_02_prophet_saturation.py`
- `scripts/Q038_F_03_self_letter.py`
- `scripts/Q038_F_04_davidic_triad.py`
- `scripts/Q038_F_05_anti_cluster.py`

### 5 JSON outputs

- `csv/Q038-F-01.json` — singleton-twin verse-pair similarities.
- `csv/Q038-F-02.json` — 114-surah prophet-density index.
- `csv/Q038-F-03.json` — 3-singleton self-letter amplification.
- `csv/Q038-F-04.json` — Davidic triad TF-IDF cohesion.
- `csv/Q038-F-05.json` — Q 38 vs muq-cluster centroids.

### Key empirical results

| Test | Verdict | Detail |
|:--|:--:|:--|
| Q038-F-01 singleton-twin Q 38:1 ↔ Q 50:1 | **CONFIRMED** | 3/3 metrics pass Bonferroni-3 (p ≤ 0.003 each) |
| Q038-F-02 prophet-cycle saturation | **CONFIRMED** | Q 38 rank 2/114 (rank 1 among n≥50); 11 unique prophets |
| Q038-F-03 singleton self-letter | **DIRECTIONAL** | 3/3 direction-correct; 1/3 (Q 50 ق) passes Bonferroni-3 |
| Q038-F-04 David-Solomon-Job triad | **NULL** | Triad TF-IDF cohesion 0.0161 vs null mean 0.0129 (p=0.146) |
| Q038-F-05 singleton anti-cluster | **DIRECTIONAL** | Δ = +0.101 > 0; but Q 32 + Q 43 in top-5 nearest |
| Classical 1 (singleton-letter twin Q 38/Q 50) | VINDICATED | F-01 confirms |
| Classical 2 (prophet-cycle saturation) | VINDICATED | F-02 confirms |
| Classical 3 (sajdat Ṣād at 38:24) | VINDICATED | Bukhārī #4601 + Abū Dāwūd #1402 chain |
| Classical 4 (singleton self-letter amplification) | RULES-TUPLE-FRAGILE | F-03 |
| Classical 5 (al-Biqāʿī Q 37→Q 38 munāsaba) | VINDICATED | TSP cost 0.000 |
| Classical 6 (al-Zamakhsharī *innahu awwāb* refrain) | VINDICATED | 100% Q 38-eponymous |
| Classical 7 (al-Bāqillānī Q 38:67 iʿjāz) | PENDING-VERIFICATION | Phrase verified, scholar source pending |

### Decision points / garden-of-forking-paths

1. **Q038-F-02 spelling correction (PRE-RUN)**. The pre-reg listed Davīd as داود (standard Arabic), but the Quranic orthography is داوود (with two waws). Spelling was corrected to داوود BEFORE running, NOT after viewing results. Without this correction, Q 38 would have ranked 7/114 (missing 5 Davīd hits). With correction: rank 2/114. This is a **spelling-of-target-string** correction, not a hypothesis adjustment; the test design (rank-on-density) was unchanged. Logged here per protocol §6.4 and disclosed in `06-novel-findings.md` Q038-F-02 garden-of-forking-paths note.

2. **Q038-F-04 NULL is honest**. The David-Solomon-Job triad cohesion was pre-committed as a CONFIRMED test on TF-IDF lexical-cohesion. The result (0.146 not significant; ratio < 1) is NULL. The classical *trial-triad* reading is VINDICATED at the **phrase-anaphoric level** (*innahu awwāb* refrain — see Claim 6 in `05-classical-claims-audit.md`), but NOT at the lexical-vocabulary level. This is reported transparently — the TF-IDF instrument is too coarse to detect anaphora-style structural cohesion. Honest NULL with diagnostic interpretation.

3. **Hadith number verification**. The prompt cited Bukhārī "#1131, #1976" and Muslim "#1159" for David-fasting. These idInBook numbers in the on-disk AhmedBaset corpus do NOT correspond to David-fasting hadith (1131 is light fajr rakʿas; 1976 is ʿUkāẓ marketplace; Muslim 1159 is a Qatāda chain). The actual David-fasting hadith in our local archive are at Bukhārī idInBook **1903, 1906, 1908, 3279, 1098**, and Muslim idInBook **2614, 2630**. This mismatch is disclosed in `04-hadith-corpus.md` §10. NO HADITH NUMBER WAS INVENTED; numbers cited are verified directly from the on-disk JSON via Python.

4. **Coordination with Q 050-qaf specialist (per cross-instructions)**. The Q 38 specialist tests the **verse-level** twin Q 38:1 ↔ Q 50:1 (Q038-F-01 CONFIRMED). The Q 050 specialist (Q050-F-01) should EXTEND or COMPLEMENT, e.g., by auditing the classical *qasamīyāt iftitāḥīya* tradition (oath-introduced openings). The cross-singleton joint test of singleton-self-letter (Q050-F-04) is owned by the Q 50 specialist and should aggregate Q038-F-03's directional 3/3 finding with Q 50 ق passing alone at α_bon. This coordination is documented in `07-cross-references.md` §7.

5. **The Q 78 al-Nabaʾ surprise**. Q 38's #1 FR-nearest is Q 78 (0.833), NOT Q 50 (0.854). This was unexpected; the singleton-twin claim is about the **2nd-nearest** at the surah level, with the **1st-nearest** being a non-singleton eschatological surah. The empirical fact (Q 78 < Q 50 in FR distance) is preserved transparently in `01-empirical-profile.md` §3 and §11 honest-limits. The Q 38 ↔ Q 50 ↔ Q 78 triangle is documented as a follow-up question in `07-cross-references.md` §8.

### Anti-hallucination checklist (compliance)

- [x] Every numerical value traced to a specific JSON file.
- [x] Every classical citation has scholar + work + (where local-extracted) page/chapter / section.
- [x] Verse-text quotations cross-validated across 3 tashkeel variants.
- [x] Hadith citations have collection + idInBook number from the AhmedBaset 9-books extraction; 11 hadith verified directly.
- [x] Q038-F-NN tests are SHA-locked pre-registered before running. SHAs match.
- [x] DATA-GAP / PENDING-VERIFICATION flagged where local source is incomplete (al-Bāqillānī claim 7).
- [x] DIRECTIONAL flagged where Bonferroni-corrected pass-rate falls below pre-committed threshold (F-03, F-05).
- [x] NULL flagged where TF-IDF instrument fails to detect classically-real structural cohesion (F-04 vs Claim 6).
- [x] Spelling correction (داود → داوود) disclosed BEFORE run, NOT post-hoc.
- [x] Hadith-number mismatches with prompt explicitly documented and corrected via on-disk verification.

### Pre-commit violations

None. All five direction-locked tests matched their pre-committed direction (or returned NULL on the directional null hypothesis without reversal). The DIRECTIONAL verdicts on F-03 and F-05 reflect sub-threshold inferential pass-rate, NOT a direction reversal. The NULL on F-04 is on the cohesion-above-null hypothesis, with explicit honest reporting that the structural-cohesion classical reading operates at the phrase-anaphora layer (Claim 6) rather than at the TF-IDF lexical layer the F-04 instrument tests.

### Cross-finding additions

This Q 38 investigation contributes to:
- **cross-finding-026 (iʿjāz architecture)**: Q 38 mid-pack on UAS, top-tier on prophet-density, mid-high on iʿjāz sig_A. Adds: prophet-cycle saturation as a new architectural axis.
- **cross-finding-014 M2 (Late-Meccan Scripture-Announcement)**: Q 38:1 oath-by-Qurʾān is M2-hallmark; the Q 38:1 ↔ Q 50:1 twin tightens the M2 phase identification to specifically the **singleton-letter+oath-by-Qurʾān** sub-pattern.
- **cross-finding-021 (mushaf information-theoretic optimality)**: Q 37→Q 38 = 0.000 cost; Q 38 sits in the well-fitted backbone.
- **NEW corpus-implication finding (potential H-NEW-1XXX)**: the *innahu awwāb* phrase as a 100%-Q-38-eponymous corpus-rare phrase paired with the trial-triad structure. Could be promoted to a global H-NEW finding if confirmed by an independent classical-source check.

### Compliance attestation

This investigation has been conducted per the Quran Decipherment Project's INVESTIGATION-PROTOCOL.md, the quran-investigation skill, and the discipline outlined in HANDOFF/04-DISCIPLINE.md. The five pre-regs were SHA-locked before computation; all scripts SHA-verify at runtime; all classical citations are scholar+work+passage; all hadith citations are verified against on-disk JSON; all numerical values are traced to specific data files. Pre-commit violations: ZERO. Garden-of-forking-paths: 5 entries documented above.

*Bismillāhi al-Raḥmāni al-Raḥīm.*

---

## 2026-05-09 — Follow-up specialist run: 3 additional pre-registered tests (F-06..F-08)

**Agent**: Q038-sad-followup-specialist (single-author voice; dispatched per Wave-H session brief 2026-05-09 PM).

### Outputs added
- `Q038-F-06-sad-density-rank-prereg.md` SHA `06dd2010ce39314f07404cb5cb53cb9d22f5135a9566265df8a63f580735fa48`
- `Q038-F-07-iblis-narrative-cohesion-prereg.md` SHA `9778fb03e21170410a7b6041cf3784b3883cb8ddf63355f87cbdc88e023b0d95`
- `Q038-F-08-david-repentance-marker-prereg.md` SHA `20cd8ed33367cfef0c1bf6acdaba7b25658ccdccfc96a81f39cc0239f950a39f`
- `scripts/Q038_F_06_sad_density_rank.py`
- `scripts/Q038_F_07_iblis_pericope_cohesion.py`
- `scripts/Q038_F_08_david_repentance_marker.py`
- `csv/Q038-F-06.json`, `csv/Q038-F-07.json`, `csv/Q038-F-08.json`
- `06-novel-findings.md` extended with F-06..F-08 sections + updated cross-finding-strength table

### Headline results (seed = 20260509, n_perm = 10000 for F-07/F-08)

| Test | Verdict | Key metric |
|:--|:--:|:--|
| Q038-F-06 ص-density rank in 60-100-verse band | **DIRECTIONAL** | Rank 2/20 (Q 56 al-Wāqiʿa 0.968% vs Q 38 0.914%) — strict rank-1 not met, but DIRECTIONAL band hit |
| Q038-F-07 Iblīs-narrative 7-pericope root-Jaccard | **CONFIRMED** | obs J=0.1456 vs null 0.0650 ± 0.0169 (z=+4.76, p<0.0001); 0 of 10000 perms ≥ obs |
| Q038-F-08 David sajda repentance-marker discriminator | **DIRECTIONAL** | Δ=+4.07 pp (A=4.07%, B=0.00%); direction-matched but small-N (B has 25 tokens) keeps p=0.25 |

### Decision points

1. **F-08 root-string correction PRE-RUN.** The pre-reg's initial §6 listed Buckwalter-style root strings `Awob`, `tawob`, `gh~afar`, `sajad`, `rajaE`, `nadim` (verb-lemma style). A direct grep against `data/morphology/quranic-corpus-morphology-0.4.txt` confirmed the actual QAC v0.4 ROOT-field strings are the consonantal abbreviations `Awb`, `twb`, `gfr`, `sjd`, `rjE`, `ndm`. The pre-reg §6 was corrected to use the actual QAC strings BEFORE SHA-locking. This is a data-format correction, not a hypothesis adjustment. The script verifies all 6 roots have ≥1 attestation in QAC before running (sanity check). Logged per protocol §6.4.

2. **F-07 pericope-level CONFIRMED complements the prior H-NEW NULL on host-surahs.** The earlier 2026-05-07 test of Iblīs-narrative HOST-SURAHS {Q 2, 7, 15, 17, 18, 20, 38} returned NOT FR-cohesive at the whole-surah root-distribution level. F-07 zooms into the actual narrative-pericopes inside those surahs and CONFIRMS strong root-Jaccard cohesion (z=+4.76). This is a clean cross-finding-025 ratification: marker-thickness matters; the Iblīs-narrative is a thin marker at the surah scale but a concentrated narrative trope at the pericope scale. The two results together strengthen the cross-finding-025 operational definition.

3. **F-06 rank-2 result is honest.** The Q 38-vs-Q 56 ص-rate gap is 0.054 pp (a 6% relative gap). The pre-committed rank-1 is not met. The DIRECTIONAL bucket (pre-reg §4 rank 2-3) catches this; no result-massaging needed. Q 56 al-Wāqiʿa's elevated ص is driven by the eschatological *aṣḥāb al-yamīn / aṣḥāb al-shimāl / aṣḥāb al-mashʾama* triad and *al-naṣb / al-naṣīb / al-ṣaffīna* vocabulary.

### Anti-hallucination compliance (F-06..F-08)

- [x] All 3 pre-regs SHA256-locked BEFORE running.
- [x] Pre-reg SHAs embedded in scripts; runtime verification fails-fast on mismatch.
- [x] F-08 QAC root-strings verified against the morphology file before pre-reg SHA-lock.
- [x] No numerical claim made from memory; every value computed from disk and traced to JSON output.
- [x] No hadith numbers invented (none cited in F-06..F-08).
- [x] No verse references invented; the F-07 and F-08 pre-reg verse-ranges are from the brief and align with classical pericope-boundaries.
- [x] Pre-committed directions: F-06 HIGHEST rank-1 (DIRECTIONAL hit on rank-2); F-07 TIGHTER (CONFIRMED); F-08 A > B (DIRECTIONAL hit).
- [x] No pre-commit violations.

### Cumulative tally

8 pre-registered tests total for Q 38 (F-01..F-08): **3 CONFIRMED (F-01, F-02, F-07), 4 DIRECTIONAL (F-03, F-05, F-06, F-08), 1 NULL (F-04)**. All 8 direction-locked-correct. Zero pre-commit violations across the full investigation.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
