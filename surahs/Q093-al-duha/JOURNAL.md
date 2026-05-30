---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 93 al-Ḍuḥā — Investigation Journal

## 2026-05-30 — Wave-N full 8-file deep-dive (single-specialist landing, completion pass)

**Pre-flight (in order):**
1. Read the quran-investigation skill (`SKILL.md`).
2. Read `INVESTIGATION-PROTOCOL.md` (binding methodology).
3. ls'd `surahs/Q093-al-duha/` and read every file already on disk: 00-overview, 01-empirical-profile,
   02-content-analysis, 03-tafsir-survey, the Q093-F-01 pre-reg, all four `csv/` JSONs, and the four
   local `scripts/` (run_q93_q94_pair_cohesion, run_trio_cohesion, run_seam_asymmetry, verify_fatra_hadith).
4. Reviewed exemplar `surahs/Q066-al-tahrim/` (04/05/06/07 + JOURNAL structure, depth, tone).
5. Confirmed the missing/stub files to write: 04-hadith-corpus, 05-classical-claims-audit,
   06-novel-findings, 07-cross-references, JOURNAL (this). Did NOT rewrite the complete 00-03 + pre-reg.

**State found:** a prior run had written 00-03 + the SHA-locked Q093-F-01 pre-reg + the top-level
`scripts/Q093_F_01_duha_sharh_seam.py` + `csv/Q093-F-01.json` + three 2026-05-09 exploratory JSONs
(pair-cohesion, trio-cohesion, seam-asymmetry), then stalled before the hadith/audit/findings/xref files
and before committing. The 00-03 files already cite Q093-F-01 Arm A/B as CONFIRMED.

**Re-verification (all from disk, no values from memory):**
- **Q093-F-01 re-run** (`python3 scripts/Q093_F_01_duha_sharh_seam.py`): printed
  `SHA OK: 2e384496…b41eed` (pre-reg SHA verified at runtime, fail-fast intact). Reproduced
  `csv/Q093-F-01.json` byte-for-byte (git showed no modification). Result confirmed:
  - **Arm A CONFIRMED (scale-dissociation), 4/4, no pre-commit violation:** A-H1 Q 94 FR rank 4/113
    (0.3641, top-5); A-H2 Q 93→Q 94 TSP seam delta_raw −0.01520 rank 10/113 (seamless); A-H3 seam
    root-Jaccard 0.0 at k=3 AND k=5 (≤ corpus means 0.0416/0.0632); A-H4 k=3 percentile 43.4 (≤90).
    Q 92 (control) FR rank 18; Q 93 mean FR 0.81517.
  - **Arm B CONFIRMED:** B-H1 `wjd` at verses [6,7,8] only; B-H2 favor∩command intersection = {`ytm`}
    (unique bridge v 6→v 9). B-H3 census: `ytm` in ≥2 verses only in Q 2, Q 4, Q 93 (12 surahs total).
- **Hadith verification** (`python3 scripts/verify_fatra_hadith.py` → `csv/Q093F04-fatra-hadith-audit.json`,
  plus a direct idInBook extraction): every ḥadīth number in 00-overview verified against
  `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books`:
  - Bukhārī **#1092** (ch 19, Jundub b. ʿAbdallāh, *iḥtabasa Jibrīl*) ✓
  - Bukhārī **#4744**, **#4745** (Book 65 Tafsīr Sūrat al-Ḍuḥā, Jundub b. Sufyān / al-Bajalī) ✓
  - Bukhārī **#4776** (Book 66 region, Jundub, *mā arā shayṭānaka*) ✓
  - Muslim **#4525**, **#4526** (ch 32, Jundub — idolaters'/Jundub-b.-Sufyān wordings) ✓
  - Tirmidhī **#3429** (Book 5 Tafsīr Sūrat al-Ḍuḥā, ch 47, Jundub al-Bajalī; wounded-finger + fatra);
    grading **ḥasan ṣaḥīḥ** read from the on-disk Arabic colophon (*qāla Abū ʿĪsā: hādhā ḥadīth ḥasan
    ṣaḥīḥ*) ✓
  - T2/T3: **no** 9-book ḥadīth cites both Q 93 and Q 94 markers (0 hits) → the "al-Ḍuḥā + al-Sharḥ
    single-revelation" claim is exegetical/juristic, NOT ḥadīth-attested. T4: the Q 92 al-Layl faḍāʾil
    cluster (Muʿādh-ʿishāʾ, Q 87+91+92, 9 hits) is separate from the al-Ḍuḥā occasion.
  - Flagged: the Q 93:5 *fa-tarḍā* intercession narration is cited by al-Qurṭubī as Ṣaḥīḥ Muslim but its
    9-book `idInBook` was NOT isolated this pass (reported as tafsīr-carried, not numbered from memory).
- **Chronology** (`data/revelation-order.csv`, keyed by revelation_order — looked up by mushaf_order=93):
  Q 93 = revelation #11, Nöldeke #13, Meccan; Q 92 al-Layl #9 / Nöldeke #10; Q 94 al-Sharḥ #12 / Nöldeke #12.
- **Verse count** (`data/hafs-verse-counts.tsv` line 93 = 11) confirms al-Qurṭubī's *iḥdā ʿashrata āya*.

**Files written this pass:**
- `04-hadith-corpus.md` — the fatra asbāb with verified idInBook numbers; T1-T4 audit of the
  Q93+Q94-single-revelation claim (verified ABSENT in the 9 books); faḍāʾil data-gap flagged.
- `05-classical-claims-audit.md` — 6 claims: Meccan-by-agreement (VINDICATED), 11 verses (VINDICATED),
  fatra asbāb (VINDICATED), Q93+Q94 "one surah" (SPLIT — whole-surah ✓ / boundary-lexis ✗ / not
  ḥadīth-attested), Ibn Kathīr favor→command parallel (VINDICATED, refined to v6↔9-only lexical),
  al-ḍuḥā/fa-tarḍā gloss (NOT-TESTABLE).
- `06-novel-findings.md` — Q093-F-01 finalized: Arm A CONFIRMED (scale-dissociation), Arm B CONFIRMED;
  cites `csv/Q093-F-01.json` throughout; equal-NULL-prominence note (the boundary-lexical NULL is reported
  with equal weight to the whole-surah CONFIRMED); MW-1..7 + Bonferroni + cross-finding integration.
- `07-cross-references.md` — mushaf seams, FR neighbors (Q 94 = 4th), {Q 90-96} cohesion window, the
  paired-surah bond, the Q 92 oath-frame surface-echo control, H-NEW links, CF-025 role.
- `JOURNAL.md` (this).

**Decision points / honesty notes:**
- Both arms passed in the pre-committed direction; NO direction reversal, NO garden-of-forking-paths shift
  (analysis matched the locked pre-reg exactly). The script's `pre_commit_violation` flag = false.
- The *honest NULL* inside Arm A is the boundary-lexical scale: seam J = 0.0. This is reported with equal
  prominence — the finding's force is that cohesion does NOT live where the classical reading locates it.
- The three 2026-05-09 exploratory JSONs (pair/trio/seam-asymmetry) are corroborating context, NOT the
  SHA-locked primary test; only Q093-F-01 is pre-registered and gating. Documented as such in 06.
- Did NOT edit MASTER-FINDINGS-LEDGER.md; a ledger-ready §10.NN entry is returned in the landing report.
- Did NOT touch the unrelated dirty paths (Q084, Q094) seen in git status; staged ONLY
  `surahs/Q093-al-duha/`.

**Verdict:** Q093-F-01 = **Arm A CONFIRMED (Q 93↔Q 94 scale-dissociation)** + **Arm B CONFIRMED
(favor→command orphan-recall)**. Asbāb fully verified on disk; the Q93+Q94 single-surah claim is
empirically supported at whole-surah scale but is NOT ḥadīth-attested and is boundary-lexically null.

**Queued follow-ups (from 00-overview §8):**
- Q093-F-02: is the *wa-la-sawfa yuʿṭīka rabbuka fa-tarḍā* (*sawfa*+future-divine-gift) a Meccan-consolation distinctive?
- Q093-F-03: corpus census of the *wa-l-layl idhā [verb]* oath-frame (surface-anaphora vs FR-distance gap).
- Q093-F-04: re-run Arm A's seam dissociation across all 13 seamless seams — is whole-surah-smooth-but-lexically-zero systematic in the short-surah tail?
- Candidate corpus-wide H-NEW: the favor→command lexical-recall census (Arm B generalization).
