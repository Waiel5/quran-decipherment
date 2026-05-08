---
surah: 5
file_type: journal
date_last_updated: 2026-05-07
specialist: Q005-al-maida-specialist
---

# Q 5 al-Māʾida — Investigation Journal

## 2026-05-07 — Specialist dispatch and full deep-dive completion

**Specialist**: Q005-al-maida-specialist (this run).

### Pre-flight reading (verified at run-time)

1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` — read.
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` — read in full.
3. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` — read.
4. Existing surah templates: Q002, Q009 — both 8-file structures inspected.
5. `cross-finding-026-iʿjāz-architecture.md` — read in full, including §13 4-cell typology amendment.

### Pre-registration sequence

All 5 pre-regs were written BEFORE running any computation, with the following frozen elements:
- Hypothesis statement
- Direction (locked)
- Lemma / root family
- Permutation null protocol
- Bonferroni-k = 5; α_bon = 0.01
- Seed 20260507; n_perm 10000

SHA256 of each pre-reg was computed AFTER finalizing and BEFORE the run script executed. The run script verifies these SHAs at runtime; mismatch = fail-fast (verified all 5 PASSED on the actual run).

### Pre-reg SHAs (locked)

| Pre-reg | SHA256 |
|:--|:--|
| Q005-F-01-potb-density-prereg.md | `1edccc500ffad015aebe957e112d3826355f451c66aa37463bf2d56ceb05c165` |
| Q005-F-02-maida-episode-isolation-prereg.md | `e8b0885729bb87d77565c57e1c59414bea682c5cefd32f4dcca02d04f6ea9e9d` |
| Q005-F-03-akmaltu-cluster-prereg.md | `c91092c51bc85bd8dab7ebaf8f5a965b0ff432e2af2a7c501b40cc033286a179` |
| Q005-F-04-covenants-density-prereg.md | `2a1d8cdd705b842926527112671d1871f1f2a96a155c32222c199c9b6e68946d` |
| Q005-F-05-late-medinan-signature-prereg.md | `74117716db9861e84ad2dc3e4f51c8324b1115dde2ae4786f75fb4afd36c84a4` |

### Run sequence

1. Pre-reg SHA verification: ALL 5 PASS.
2. Load QAC v0.4 morphology + Quran no-tashkeel: Q 5 = 422 distinct roots, 684 distinct lemmas, 3,047 words.
3. Run Q005-F-01 PoTB density: result = DIRECTIONAL.
4. Run Q005-F-02 māʾida hapax: result = DIRECTIONAL (NULL on strict 4-family criterion; māʾida-lemma alone is corpus-hapax).
5. Run Q005-F-03 Q 5:3 completion-cluster: result = **VINDICATED p=0.0001**.
6. Run Q005-F-04 covenants density: result = **NULL** (Q 5 corpus-rank 10).
7. Run Q005-F-05 late-Medinan signature: result = **NULL — DIRECTION REVERSED**. Q 5 closer to Q 2 (early-Medinan) than to Q 9 + Q 110 LM-centroid on ALL 4 axes.

### Decision points and garden-of-forking-paths log

- **F-01 lemma family**: ahl al-kitāb excluded (compound). zabūr excluded (3 corpus-attestations, sparse). All other 9 frozen. No post-hoc adjustment.
- **F-04 family**: `Ax*` (akhdh) excluded — too broad. Frozen at {wvq, Ehd, Eqd, nqD}. No post-hoc adjustment.
- **F-05 direction**: pre-committed "Q 5 closer to LM" — REVERSED in observation. Per PRE-REG-STANDARD-01: published as NULL with full prominence. Post-hoc-noticed dissociation discovery is reported with MW-7 single-test-α=0.05 ceiling and replication queue.

### Garden-of-forking-paths — Q005-F-05 specifically

The pre-reg explicitly anticipated that Q 5's nearest FR-neighbors are Q 2, 3, 4, 9, 6 (all al-sabʿ al-ṭiwāl members), and noted: "the FR-axis ALONE places Q 5 among the long-Medinan-legal cluster, not the late-Medinan-creedal cluster. The 4-axis test may therefore tilt toward the EARLY centroid on FR alone but the multi-axis result is unknown."

The observed result is that ALL 4 axes (not just FR) tilt toward the EM centroid. This is more decisive than the pre-reg anticipated. The dissociation is multi-axis, not single-axis. The pre-reg explicitly stated the NULL outcome is "a meaningful finding" — and this is the reported NULL.

### Outputs written

```
surahs/Q005-al-maida/
  00-overview.md
  01-empirical-profile.md
  02-content-analysis.md
  03-tafsir-survey.md
  04-hadith-corpus.md
  05-classical-claims-audit.md
  06-novel-findings.md
  07-cross-references.md
  JOURNAL.md
  Q005-F-01-potb-density-prereg.md (SHA-locked)
  Q005-F-02-maida-episode-isolation-prereg.md (SHA-locked)
  Q005-F-03-akmaltu-cluster-prereg.md (SHA-locked)
  Q005-F-04-covenants-density-prereg.md (SHA-locked)
  Q005-F-05-late-medinan-signature-prereg.md (SHA-locked)
  scripts/Q005_F_all_tests.py (single unified runner; all 5 SHAs verified at runtime)
  csv/Q005-F-01.json
  csv/Q005-F-02.json
  csv/Q005-F-03.json
  csv/Q005-F-04.json
  csv/Q005-F-05.json
```

### Cross-task coordination notes (per task spec)

- Q004-al-nisa specialist runs Q4-specific tests (parallel-running). Q005-F-01 PoTB-density is COMPATIBLE with Q4-F-01-style legal-density (NOT a duplicate) — F-01 is a PoTB-specific lemma family; Q4-F-01 is presumably broader legal-vocabulary. Cross-Medinan-legal joint analysis is queued for cross-finding integration.
- The proposed 7th typology cell (al-sabʿ al-ṭiwāl cohesion-anchor) is queued for cross-finding-026 §13.7 amendment after Q 4 specialist's parallel results provide the second exemplar.

### Honest-limit notes for next agent

1. The Q005-F-05 NULL is the most "lossy" pre-reg failure — the pre-committed direction was REVERSED. Per protocol this is published with full prominence; the post-hoc-noticed chronology-architecture dissociation is interesting and replication-queued (independent test on Q 110, Q 2 expected to confirm the dissociation as a corpus-level pattern).
2. Hadith auto-extraction missed Muslim, Aḥmad, al-Nasāʾī, Mālik, Ibn Mājah Q 5 references because their text-reference patterns differ. A manual second-pass Q005-citations.md build is queued.
3. The PoTB-density test (Q005-F-01) used a frozen 9-lemma family. Adding *ahl al-kitāb* phrase (which is 6× in Q 5, 19% of corpus total) would not change ranks materially because Q 3 has 12 attestations and would also gain a boost.

### Specialist sign-off

All 8 deliverable files written. All 5 pre-regs SHA-locked and verified. All 5 tests run with results in JSON. Verdicts honestly published per equal-NULL-prominence protocol. Post-hoc-noticed dissociation discovery (Q005-F-05) flagged as DIRECTIONAL-noticed under MW-7 single-test-α=0.05 ceiling with explicit replication queue.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
