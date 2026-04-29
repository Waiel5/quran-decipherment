---
surah: 43
surah_name: al-Zukhruf
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
---

# Q 43 al-Zukhruf — investigation journal

## 2026-04-28 (Session 1, AM) — files 00..05 + Q043-F-01 prereg

The earlier session of 2026-04-28 (timestamps 18:16-18:58 per file mtimes) produced files 00-overview through 05-classical-claims-audit + the Q043-F-01 (verbatim-twin opening) pre-reg + script + JSON. That session's verdicts:

- 00-overview, 01-empirical-profile: HM-B opener; near-monorhyme 88% ن; UAS=33; sig_A=−1.10; Q 42 ↔ Q 43 = costliest HM-7 transition.
- 03-tafsir, 04-hadith, 05-audit: Q 43:4 *umm al-kitāb*, Q 43:31 rich-man, Q 43:61 ʿĪsā-Hour, Q 43-Q 44 verbatim opening pair (the latter recorded as VINDICATED at strict-uniqueness).

## 2026-04-28 (Session 2, PM) — Q043-F-01 verdict revision + Q043-F-02..05 + 06/07/JOURNAL completion

### Garden-of-forking-paths log (BEFORE running Q043-F-02..05)

For each pre-reg, the locked decisions were committed to disk and SHA256-locked BEFORE the script ran:

**Q043-F-02 (entropy break)**:
- Tashkeel: no-tashkeel (matches existing 00-overview values; Q42=2.565 / Q43=0.594 reproduce under no-tashkeel last-grapheme rule).
- Direction: H(43) < min(H(40..42)).
- Verdict thresholds: VINDICATED if H(43) below HM-7 min; DIRECTIONAL if below HM-A min only; NULL otherwise; PRECOMMIT_VIOLATION if H(43) ≥ max(H(40..42)).
- Permutation null: 10 000 perms, MW-2 corpus-prior, seed 20260428.

**Q043-F-03 (al-Raḥmān density)**:
- Lemma: substring `رحمن` (catches all morphological al-Raḥmān forms; the substring is essentially unique to the divine name).
- Density unit: per 1000 orthographic tokens, no-tashkeel.
- Direction: Q 43 rank ≤ 5 corpus-wide.
- Verdict thresholds: VINDICATED at top-5; DIRECTIONAL at top-10; NULL otherwise; PRECOMMIT_VIOLATION at rank > 50.

**Q043-F-04 (zukhruf root)**:
- Source: QAC v0.4 root-index.json key `zxrf`.
- Pre-committed direction: **Q 43 rank > 1** (the surprising direction — that surah-naming is symbolic, not density-driven). Pre-commit honored even though count-tied case is degenerate.

**Q043-F-05 (ʿĪsā 9-window)**:
- Block definition: every contiguous 9-verse window within-surah (not crossing surah boundaries).
- Christological tokens: substrings `عيسى` + `مريم`.
- Direction: Q 43:57-65 percentile ≥ 99 of corpus 9-window distribution.

These choices were locked in `surahs/Q043-al-zukhruf/preregs/Q043-F-0{2,3,4,5}-*-prereg.md` with SHA256 hashes embedded in `scripts/Q043_F_0{2,3,4,5}_*.py`. Each script SHA-verifies at runtime (fail-fast).

### Pre-reg SHA256 trace

| Pre-reg | SHA256 |
|:--|:--|
| Q043-F-01 (prior session) | `6d4d362785f083bd9ff5f1cee533afc0cfa30f55e198031ab3718d10eff331d2` |
| Q043-F-02 entropy break | `1bfd78dd11cad0e36d13e9d3c8b68fbf01e408e3b97f2278eb76bebb7274b9de` |
| Q043-F-03 *Raḥmān* density | `a265de03d897060bb4a4c8ea591051966cc62fd30922ea9ccd3a5cd5e682639d` |
| Q043-F-04 *zukhruf* root | `ff2dd6517aac6582a800cdb48218f07bf1604932d5161ff75cc53e217a2503ff` |
| Q043-F-05 ʿĪsā 9-window | `87fcc04d19b68ef638f2ef83823c24d0b7ca46208fa37ca32604e7e87a668cac` |

All four SHAs verified at runtime (Q043_F_0{2,3,4,5}_*.py). No SHA mismatch occurred.

### Run timeline (2026-04-28 PM)

1. Pre-flight reading: SKILL.md + INVESTIGATION-PROTOCOL.md + existing 00..05 files for Q 43 + sibling models (Q 40 06+07+JOURNAL, Q 41 06, Q 42 06+07+JOURNAL).
2. Verified existing Q043-F-01 JSON: discovered the prior pre-commit was VIOLATED — script found TWO twin pairs (Q 43-Q 44 AND Q 45-Q 46), not one. Logged for prominent disclosure.
3. Empirical pre-flight on h-new-840.json: re-extracted Q 43 record + HM-7 cluster ranking. Q 42 (rank 31) > Q 43 (rank 33) > Q 41 (rank 39) confirmed; consistent with Q 41 + Q 42 prior-session corrections.
4. Pre-registered Q043-F-02 at `1bfd78dd...` and ran → VINDICATED (Q 43 entropy 0.5939 < HM-A min 2.2635; p_perm = 0.0000).
5. Pre-registered Q043-F-03 at `a265de03...` and ran → VINDICATED (Q 43 rank 5; density 8.05/1000).
6. Pre-registered Q043-F-04 at `ff2dd651...` and ran → NULL/precommit-reversed (Q 43 IS rank 1 by density at the count=1-tied case; honest reporting per protocol §1.3).
7. Pre-registered Q043-F-05 at `87fcc04d...` and ran → VINDICATED (Q 43:57-65 at 99.31th percentile of corpus 9-windows).
8. Wrote 06-novel-findings.md (4 tests + Q043-F-01 verdict revision).
9. Wrote 07-cross-references.md (HM-7 reciprocals + cross-finding integrations).
10. Wrote JOURNAL.md.
11. Updated 00-overview verdict line.
12. Appended §9.14, §9.15, §9.16 to MASTER-FINDINGS-LEDGER.md.

### NULLs surfaced (equal prominence per protocol §1.3)

- **Q043-F-01 (prior session)**: pre-commit prediction was that ONLY Q 43-Q 44 share verbatim-identical first-two-verses; the script discovered Q 45-Q 46 ALSO satisfies. Verdict revised to NULL with full prominence. The original 05-classical-claims-audit Claim 4 ("only verbatim-identical 2-verse opening pair") is therefore **incorrect** and is corrected: TWO HM-B adjacent pairs share verbatim-identical openings (Q 43-Q 44 + Q 45-Q 46). The descriptive observation (BOTH HM-B verbatim-twin pairs are within the 4-surah HM-B sub-cluster) is post-hoc and capped at MW-7 single-test α=0.05.
- **Q043-F-04 (zukhruf root)**: pre-committed surprising-direction (Q 43 rank > 1) was REVERSED; Q 43 IS rank 1 at the near-hapax (count=1 in 4 surahs) regime. Not deeply tested; degenerate at this resolution. Recorded with full prominence; the broader claim "surah-naming is symbolic" remains untested at this corpus-scale.

### Pre-commit honoring

| Test | Pre-committed direction | Observed direction |
|:--|:--|:--|
| Q043-F-01 (prior) | only Q 43-Q 44 share twin opening | Q 43-Q 44 + Q 45-Q 46 both share — VIOLATION, NULL |
| Q043-F-02 | H(43) < min(H(40..42)) | matches — VINDICATED |
| Q043-F-03 | Q 43 rank ≤ 5 by *Raḥmān* density | matches at rank 5 — VINDICATED |
| Q043-F-04 | Q 43 rank > 1 by `zxrf` density | reversed — NULL with precommit-flag |
| Q043-F-05 | Q 43:57-65 ≥ 99th percentile | matches at 99.31 — VINDICATED |

3/5 pre-commits honored; 2/5 violated and recorded with full prominence.

### Honest limits

- Per-Q043 raw extractions of Ibn Kathīr / al-Qurṭubī / al-Rāzī were located by surah-name markers within the consolidated OpenITI files, not as discrete per-Q043 extraction files; latter would strengthen citation precision.
- *Faḍāʾil* Q 43 traditions outside the 9-book pull (e.g., *al-Durr al-manthūr*, Abū ʿUbayd) flagged DATA-GAP.
- Q 19 Maryam comparator surah for Q043-F-05 not yet built; the Q 19 ↔ Q 43 christological-diptych cross-link is empirical but un-anchored to a Q 19 specialist file.
- Q 44, 45, 46 (HM-B siblings) not yet built; cross-references are descriptive but un-anchored.
- F-04 is degenerate at the count-tied case; further test on broader near-hapax-named-surahs is queued (Q014 Ibrāhīm, Q036 YāSīn, etc.).
- F-02 used last-grapheme of verse (no-tashkeel rule); classical *qāfiya* analysis would refine. Min-tashkeel and full-tashkeel last-grapheme rankings not pre-committed.

### Verdict

Q 43 al-Zukhruf investigation **COMPLETE** (per the 8-template-set + JOURNAL standard). Three pre-registered novel findings VINDICATED at strict pre-commit (F-02 entropy break, F-03 *Raḥmān* density, F-05 ʿĪsā-block density). Two pre-commits violated and recorded with full prominence (F-01 verbatim-twin uniqueness, F-04 *zukhruf* root direction). 

**Cluster-role**: HM-B opener; **bifurcation step partner with Q 42** at both prosody axis (ΔH=1.97 bits, F-02) and FR-content axis (FR=0.9912, costliest HM-7 transition). 

**Defining empirical fact**: Q 43 sits at the corpus-extreme of the **multi-axis-mixed iʿjāz signature**: rhyme-entropy minimum of HM-7 (anti-iʿjāz fawāṣil at sig_A=−1.10) AND christological-block density at the 99.31th percentile of corpus 9-windows AND *al-Raḥmān* lemma density at corpus rank 5. Q 43 is **theologically dense + prosodically uniform** — a structural pattern previously noted by al-Bāqillānī (*iʿjāz al-fawāṣil*) and al-Khaṭṭābī (*iʿjāz al-maʿnā*) as ORTHOGONAL axes; Q 43 illustrates them at intra-surah scale.

### Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]]
- [[Q043-al-zukhruf/06-novel-findings|Q 43 novel findings]]
- [[Q043-al-zukhruf/07-cross-references|Q 43 cross-references]]
- [[Q040-ghafir/JOURNAL|Q 40 journal]] — sibling model
- [[Q041-fussilat/JOURNAL|Q 41 journal]] — sibling model (UAS-correction precedent)
- [[Q042-al-shura/JOURNAL|Q 42 journal]] — bifurcation-partner journal
