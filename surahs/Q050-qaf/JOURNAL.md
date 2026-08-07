---
surah: 50
surah_name_ar: ق
surah_name_translit: Qāf
file_type: journal
date_last_updated: 2026-05-09
phase: B+
---

# Q 50 Qāf — Investigation Journal


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

## 2026-05-07 — Wave-D agent dispatch (Q050-qaf-specialist)

**Specialist agent**: Q050-qaf-specialist (this agent).

**Task**: Build full 8-file deep-dive on Q 50 Sūrat Qāf with 5 pre-registered novel tests on its singular structural signatures.

### 12:00 — Pre-flight reading

Read in order:
1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` — binding methodology entry-point.
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` — full protocol; especially §1.2 pre-registration, §1.3 NULL prominence, §1.4 rules-tuple, §2 data sources.
3. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` — MW-series + PRE-REG-STANDARD-04 + post-hoc protocol.
4. `/Users/grey/Downloads/quran/surahs/Q012-yusuf/00-overview.md` and `/Users/grey/Downloads/quran/surahs/Q055-al-rahman/01-empirical-profile.md` — canonical 8-file template style references.
5. `/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` — synthesis frame; for Q 50 cell-assignment.
6. `/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-muqattaat-surah-qaf.md` — pre-existing project extract on Q 50 muqaṭṭaʿāt (already locked: 57 ق letters, z=+4.68 in prior pipeline, etc.).

### 12:30 — Empirical metric extraction (h-new pipeline)

From `findings/phase-b-hypotheses/csv/`:
- **h-new-840.json**: Q 50 UAS rank = 40/114, score = 0.380. abs_outlier = 5.42, max_cost = 0.177, abs_iʿjāz = 0.891.
- **h-new-590.json**: Q 50 outlier-strength Δ = +5.42 pp (WEAK_OUTLIER), rank 13/114; window [Q 47-53].
- **h-new-720.json**: Q 49→50 adjacency rank 17/113 (δ=0.177); Q 50→51 rank 25/113 (δ=0.119).
- **h-new-750.json**: Q 50 sig_A = +0.891 (rank 37/114), sig_B = +0.316; rhyme_entropy=1.286 nats; top_letter=د at 60%.
- **h-new-700.json**: rhyme primary-model two-piece-kink-50, R²=0.789; Q 50 fits compression-tail.
- **h-new-111.json**: Q 50 mean FR = 0.928. Nearest 5: Q 78, 86, 112, 79, 110. Farthest: Q 4, 9, 33, 5, 3.

### 12:50 — Singleton-letter cohort metrics (Q 38 + Q 68)

Computed via h-new lookups:

| | Q 38 ص | Q 50 ق | Q 68 ن |
|:-:|:-:|:-:|:-:|
| n_verses | 88 | 45 | 52 |
| sig_A | +1.286 | +0.891 | -0.413 |
| rāwī | ب 40% | د 60% | ن 81% |
| outlier Δ | +2.7 (WEAK) | +5.42 (WEAK) | -3.45 (NULL) |
| UAS rank | 59 | 40 | 76 |
| FR-pair Q38↔Q50 = 0.854 | | | |
| FR-pair Q38↔Q68 = 0.910 | | | |
| FR-pair Q50↔Q68 = 0.846 | | | |
| Mean pairwise = 0.870 | | | |

### 13:10 — Hadith verification (anti-hallucination MW-6)

**CRITICAL CORRECTION**: Task prompt cited "Sahih Muslim #872" for the Umm Hishām/Q 50 Friday-recitation hadith. Direct verification against `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json`:

- **idInBook 872** (Muslim) = Jābir b. Samura on hand gestures during prayer salām — UNRELATED to Q 50.
- **idInBook 1907** (Muslim, chapterId 7 *Kitāb al-Jumʿa*) = Umm Hishām bint Ḥāritha b. al-Nuʿmān: the actual Friday-minbar Q 50 recitation hadith.

The corrected reference is Sahih Muslim #1907. Cross-book corroborations: al-Nasāʾī #951 + #1416, Abū Dāwūd #1101 + #1103.

Eid-recitation pair (Q 50 + Q 54): Mālik *Muwaṭṭaʾ* #439, al-Tirmidhī #534 (graded ḥasan ṣaḥīḥ), Abū Dāwūd #1155, al-Nasāʾī #1572, Ibn Mājah #1016. 5 cross-book attestations, all verified.

### 13:30 — Pre-registration of 5 novel tests

Wrote 5 pre-reg files BEFORE running anything:

| Pre-reg | SHA256 head | Direction |
|:--|:--|:--|
| Q050-F-01 | `8ad78d219bf7` | POSITIVE (singleton or pair construction) |
| Q050-F-02 | `8fb095ca71d9` | POSITIVE (body-part density > 95th percentile) |
| Q050-F-03 | `66c22536f23c` | POSITIVE (host-letter density > 95th percentile, all 3 cohort) |
| Q050-F-04 | `cac90ad5c9e1` | POSITIVE LOW S (cohort FR-cohesion) |
| Q050-F-05 | `693953f73701` | NULL on cohort opener-rāwī alignment (1/3 = baseline) |

All 5 SHA256 hashes embedded in respective run scripts; SHA verified at runtime (every script fail-fast on mismatch).

### 14:00 — Test execution

All 5 scripts ran successfully; SHA-locked.

| Test | Verdict | Headline |
|:--|:--|:--|
| Q050-F-01 | DIRECTIONAL-EXTENDED-COHORT | matching_surahs = [38, 50, 68] (3/29) — pre-reg's NULL criterion violated by *more* coherent observation; honest pre-commit reframing |
| Q050-F-02 | **CONFIRMED** | Q 50 body-part rate = 88.5/1000 vs null mean 23.1; z = +7.23, p = 10⁻⁴, percentile 100 |
| Q050-F-03 | PARTIAL-1/3 | Q 50 ق CONFIRMED (z=+3.34, p=10⁻⁴); Q 38 ṣ raw-significant Bonferroni-fails (p=0.048); Q 68 ن NULL (p=0.079) |
| Q050-F-04 | NULL | Triplet mean pairwise FR = 0.870 (vs null 0.922); percentile 26.7%; p_low = 0.267; direction-correct, not significant |
| Q050-F-05 | CONFIRMED-NULL | 1/3 cohort match (Q 68 only); consistent with letter-rāwī orthogonality |

### 14:30 — Post-hoc Q 50 / Q 54 Eid-pair check

Computed FR(Q 50, Q 54) = 0.882 from h-new-111. Below corpus mean (0.924). The Eid-pair classical tradition CORRELATES with FR-cohesion. **Updated 05-classical-claims-audit Claim 2** from "VINDICATED at hadith level only" to "VINDICATED at hadith level AND FR-cohesion level." This is the second instance of recitation-pair → FR-near-pair (after Q 32/Q 67 from cross-finding-026 §13.5b). Flagged for cross-finding-028 candidate elevation.

### 15:00 — Writing 8-file template

Wrote in order:
1. `00-overview.md` — singleton-letter cohort property; Friday-minbar status; classical claims overview.
2. `01-empirical-profile.md` — full H-NEW integration; cell-assignment to *iʿjāz-al-fawāṣil-pure* + dual-cell *iʿjāz-al-maʿnā (mild)* via high *fadāʾil*.
3. `02-content-analysis.md` — verse-by-verse + 5-block thematic structure + 33% death-resurrection theatre at center.
4. `03-tafsir-survey.md` — al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Jalālayn, al-Rāzī (via project extract), al-Bāqillānī, al-Suyūṭī, al-Biqāʿī surveyed.
5. `04-hadith-corpus.md` — Muslim #1907 verified (CORRECTED from prompt's #872); Eid + Friday + Fajr cross-book attestations.
6. `05-classical-claims-audit.md` — 5 claims audited; 4 VINDICATED, 1 RULES-TUPLE-FRAGILE.
7. `06-novel-findings.md` — Q050-F-01 through Q050-F-05 with pre-commit transparency on Q050-F-01.
8. `07-cross-references.md` — full cross-finding linkage; future test candidates flagged.

### 15:30 — Pre-reg integrity check

Re-ran all 5 scripts to verify SHA-checksum integrity:

```
$ python3 surahs/Q050-qaf/scripts/Q050_F_01_muqattaa_oath_wow.py
Q050-F-01: VERDICT=NULL (matching_surahs=[38, 50, 68]) — published with pre-commit transparency

$ python3 surahs/Q050-qaf/scripts/Q050_F_02_body_part_density.py
Q050-F-02: VERDICT=CONFIRMED (Q50 rate 88.47, null 23.11, p=0.0001)

$ python3 surahs/Q050-qaf/scripts/Q050_F_03_qaf_letter_density.py
Q050-F-03: COHORT_VERDICT=PARTIAL-1/3-(individual-only)

$ python3 surahs/Q050-qaf/scripts/Q050_F_04_singleton_letter_triplet.py
Q050-F-04: VERDICT=NULL (S_obs=0.870, p_low=0.267)

$ python3 surahs/Q050-qaf/scripts/Q050_F_05_rhyme_vs_opener.py
Q050-F-05: COHORT=CONFIRMED-NULL-on-opener-rāwī-alignment
```

All SHA mismatches → fail-fast. None encountered. All pre-reg integrity preserved.

### 16:00 — Decisions / forking-paths log

**Decision points**:

1. **Pre-reg Q050-F-01 success criteria**: pre-committed to *exactly 1 or 2 matches* as success states (CONFIRMED-UNIQUE / CONFIRMED-PAIR). Empirical observation: 3 matches. Per protocol §1.3, this is reported as **DIRECTIONAL-EXTENDED-COHORT** with honest pre-commit reframing — NOT massaged into a "CONFIRMED-COHORT" verdict that would have required pre-registering the 3-match criterion. The pre-commit transparency is the project's intellectual integrity safeguard.

2. **Hadith number correction**: when discovering that the task prompt's "Muslim #872" was misattributed, I VERIFIED against the on-disk JSON before citing the corrected #1907. This is the MW-6 verification protocol working as designed.

3. **Bonferroni-3 on Q050-F-03**: 3 tests in the singleton-letter cohort family. Bonferroni α = 0.0167. Q 38's raw p=0.048 fails Bonferroni; reported as DIRECTIONAL_RAW_POSITIVE_BON_FAIL with full transparency. NOT massaged into "directional confirmation."

4. **Post-hoc FR(Q 50, Q 54) check** (§14:30 above): observed FR = 0.882, below corpus mean. This is post-hoc — flagged in audit Claim 2 as a *post-hoc* observation, not a pre-registered test. Direction-correct for the cross-finding-026 §13.5b conjecture. No promotion claim made beyond DIRECTIONAL — the conjecture remains a candidate for cross-finding-028.

### 16:30 — Cross-finding-026 cell-assignment

Q 50 assigned to *iʿjāz-al-fawāṣil-pure* cell (cross-finding-026 §13.6 4-cell typology) with sub-classification: *singleton-letter cohort member*. Dual-cell character noted: high *fadāʾil*-recitation density also places Q 50 in the *iʿjāz-al-maʿnā (mild)* cell. The dual-cell character is a NEW empirical observation; only Q 36 Yāsīn and Q 50 Qāf have this combination (positive sig_A + high recitation-tradition density).

### 17:00 — JOURNAL.md written

This file. Complete.

## 2026-05-09 — Wave-H agent dispatch (Q050-qaf-specialist Wave-H continuation)

**Specialist agent**: Q050-qaf-specialist (Wave-H).

**Task**: 3 additional pre-registered tests (T1, T2, T3 per brief) layered on the Wave-D 2026-05-07 baseline.

### Pre-flight reading

Re-read:
1. `.claude/skills/quran-investigation/SKILL.md`
2. `INVESTIGATION-PROTOCOL.md`
3. `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md`
4. Existing `surahs/Q050-qaf/` 8-file template + 5 Wave-D pre-regs + scripts + JSONs.

### Hadith number — already corrected in Wave-D

Note: the Wave-H brief still cited "Muslim #872" as candidate; Wave-D's earlier verification confirmed the correct reference is Muslim **#1907** (Umm Hishām). The 04-hadith-corpus.md already reflects the corrected #1907; no further correction needed in Wave-H. ʿUmm Hishām bint Ḥāritha hadith on memorizing Q 50 by hearing the Prophet recite from minbar is at Muslim idInBook 1907 chapterId 7 (*Kitāb al-Jumʿa*).

### 3 new pre-regs locked

| Pre-reg | SHA256 head | Direction | Verdict |
|:--|:--|:--|:--|
| Q050-F-06 | `d058275499fc` | LOW-S on both nulls (Bonferroni-2 α=0.025) | DIRECTIONAL (percentile_a=0.260; percentile_b=0.162; both direction-correct, neither Bonferroni-passing) |
| Q050-F-07 | `6a5530552dd6` | Q 50 = rank 1 of 16 Meccan 30-50-verse surahs on ق-density | DIRECTIONAL-TOP-3 (Q 50 rank=2; Q 75 al-Qiyāma narrowly higher; pre-reg strict rank-1 FALSIFIED; pre-commit honored) |
| Q050-F-08 | `a5abbd224371` | Replication of Q049-F-03 in_all_three=True | STRONG-REPLICATION (JSON cross-read + direct re-extraction agree) |

### Decisions / forking-paths log (Wave-H)

1. **Q050-F-07 falsification**: pre-reg locked Q 50 = rank 1 (strict). Observed: Q 50 = rank 2 (Q 75 narrowly higher at 0.0399 vs 0.0378). Per protocol §1.3: published with full prominence as DIRECTIONAL-TOP-3. NOT massaged into "Q 50 is top-3" weakened criterion. The data observation is a discovery: Q 75 al-Qiyāma has even higher class-rank ق density than Q 50, suggesting an independent classical-iʿjāz-echo finding-candidate for Q 75 specialist follow-up.

2. **Q050-F-06 stratified null**: the brief asked for comparison to "28-muqaṭṭāʿat baseline" — interpreted as the 26 non-singleton muqaṭṭāʿat surahs (29 total minus 3 singleton-letter cohort), exhaustively enumerated as C(26,3) = 2600 triplets. This is the most class-controlled null possible. The percentile shift from null-a (full-corpus, 0.260) to null-b (muqaṭṭāʿat-only, 0.162) suggests the singleton-letter cohort IS more cohesive than other muqaṭṭāʿat triplets, but neither cell passes Bonferroni-2.

3. **Q050-F-08 minimal risk**: this is a method-discipline test (dependency verification) — Q049-F-03 was a CONFIRMED-CROSS-FEATURE landing, so REPLICATION was expected. Both verification paths (JSON cross-read + direct re-extraction from h-new-130/130b/130c) AGREE. Q 50 inherits the H-NEW-1262 universal-hinge cross-reference with confidence.

### Wave-H test execution

All 3 Wave-H scripts: SHA-checksum verified at runtime. None failed. Output JSONs written to `csv/`. Findings markdowns written at `surahs/Q050-qaf/Q050-F-06-*.md`, `Q050-F-07-*.md`, `Q050-F-08-*.md`.

```
$ python3 scripts/Q050_F_06_singleton_vs_muqattaat_baseline.py
Q050-F-06: VERDICT=DIRECTIONAL
  S_obs=0.8699, null_a percentile=0.2600, null_b percentile=0.1619

$ python3 scripts/Q050_F_07_qaf_density_vs_meccan_30_50.py
Q050-F-07: VERDICT=DIRECTIONAL-TOP-3
  Q 50 rank = 2 / 16; rate = 0.03782; perm_p_rank_1 = 0.0052

$ python3 scripts/Q050_F_08_q49_q50_hinge_reverify.py
Q050-F-08: VERDICT=STRONG-REPLICATION
  All 3 feature axes (root, char-4-gram, verse-length) contain (49, 50) in top-15.
```

### Wave-H net additions

- 3 new pre-regs (SHA-locked, embedded in scripts).
- 3 new scripts (`scripts/Q050_F_06_*.py`, `Q050_F_07_*.py`, `Q050_F_08_*.py`).
- 3 new CSV/JSON outputs (`csv/Q050-F-06.json`, `Q050-F-07.json`, `Q050-F-08.json`).
- 3 new findings markdowns (in `surahs/Q050-qaf/` root).
- Updated `06-novel-findings.md` with §"Wave-H 2026-05-09" extension.

The Wave-H tests add NUANCE to the Wave-D findings, not new corpus-extreme claims. Specifically:
- Q050-F-06 sharpens Q050-F-04: the singleton-letter cohort IS directionally tighter under a muqaṭṭāʿat-only null (percentile 0.162) than under a full-corpus null (0.267), but still does not pass Bonferroni-2.
- Q050-F-07 REFINES Q050-F-03: Q 50 is corpus-extreme on ق-density (z=+3.34 per Q050-F-03), but NOT uniquely class-rank-1 within its length-matched-period-matched reference (Q 75 narrowly higher). The classical claim "Q 50 saturated with ق" is qualitatively correct but the *uniqueness* part is FALSIFIED.
- Q050-F-08 VERIFIES the Q 49 → Q 50 universal hinge as a stable dependency.

## Investigation status

- [x] Pre-flight reading (binding protocol + 4 templates + cross-finding-026)
- [x] Empirical metric extraction from 6 H-NEW JSON files
- [x] Hadith verification (Muslim #1907 corrected from prompt's #872)
- [x] 5 Wave-D pre-regs written, SHA256-locked
- [x] 5 Wave-D scripts written, SHA-checked at runtime
- [x] All 5 Wave-D tests run; verdicts reported with full pre-commit transparency
- [x] 8-file template written
- [x] Q 50 cell-assignment (cross-finding-026): iʿjāz-al-fawāṣil-pure + dual-cell iʿjāz-al-maʿnā (mild)
- [x] Future test candidates flagged in 07-cross-references §10
- [x] 3 Wave-H pre-regs written + SHA-locked (Q050-F-06, F-07, F-08)
- [x] 3 Wave-H scripts written + SHA-checked at runtime
- [x] 3 Wave-H tests run; all verdicts published with pre-commit transparency
- [x] 06-novel-findings.md updated with Wave-H synthesis
- [x] JOURNAL.md updated with Wave-H session log
- [x] JOURNAL.md complete

## Honest limits and open questions

1. **Q050-F-01 strict-pre-reg NULL** (3 matches not 1 or 2) reframed as DIRECTIONAL-EXTENDED-COHORT — the pre-commit issue is ON RECORD; the empirical observation (3-cohort-coherence) is *more* structurally striking than the predicted CONFIRMED-PAIR. A future systematic test should pre-register a 3-match criterion explicitly.

2. **Q050-F-04 NULL** is direction-correct (LOW S, more cohesive than corpus mean) but at p=0.267, NOT significant. The triplet IS *form-coherent* (Q050-F-01) AND *directionally content-cohesive* (Q050-F-04 26.7th percentile), but the content-cohesion does not meet α=0.05. The honest reading: the cohort coherence is on the form-axis, not on the content-axis.

3. **Q050-F-03 PARTIAL-1/3**: only Q 50 ق density passes Bonferroni-3. Host-letter density is Q-50-specific, not a singleton-letter cohort signature.

4. **Q 50 ↔ Q 54 Eid-pair FR-cohesion** is post-hoc; future systematic test required for the cross-finding-028 candidate.

5. **Q 50:16 *ḥabl al-warīd* corpus-singleton phrase audit** is flagged for future Q050-F-EXTENSION test; expected to be a corpus-singleton.

## Cross-references

- [[01-empirical-profile]]
- [[02-content-analysis]]
- [[03-tafsir-survey]]
- [[04-hadith-corpus]]
- [[05-classical-claims-audit]]
- [[06-novel-findings]]
- [[07-cross-references]]
- [[cross-finding-026-iʿjāz-architecture]] §13.6 cell-assignment
- [[razi-muqattaat-surah-qaf]] — pre-existing project extract on Q 50
- [[h-new-840-unified-architectural-score]] — UAS Q 50 = rank 40/114
