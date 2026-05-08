---
surah: 26
surah_name_ar: الشعراء
file_type: journal
date_last_updated: 2026-05-07
phase: B+
agent: Q026-al-shuara-specialist
---

# Q 26 al-Shuʿarāʾ — Investigation Journal

## 2026-05-07 — Initial 8-file investigation

### Pre-flight reading completed
- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
- `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` (canonical template)
- `/Users/grey/Downloads/quran/surahs/Q027-al-naml/` (TSM-sister)
- `/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-026-iʿjāz-architecture.md`

### Empirical anchors integrated
- `h-new-111`: Q 26 mean FR-distance = 1.098, rank 110/114; nearest = Q 7 (0.832), Q 15 (0.879), Q 36 (0.903), Q 23 (0.904), Q 11 (0.906). Q 28 (ṬSM sister) = 0.954, NOT in top-10.
- `h-new-590`: Q 26 +8.83pp WEAK_OUTLIER on window {23..29}.
- `h-new-700`: Q 26 nūn-rhyme 85.0%, entropy 0.477 nats.
- `h-new-720`: Q 25-26 = 0.055, Q 26-27 = 0.081 (both low; ṬSM family is structurally cheap canonical run).
- `h-new-750`: Q 26 sig_A = −2.253, rank 108/114 (anti-iʿjāz al-fawāṣil).
- `h-new-840`: Q 26 UAS = 1.822, rank 14/114 (top-13%).

### Pre-registrations locked
All 5 pre-reg files written and SHA256 computed BEFORE running any tests:
- Q026-F-01: SHA `3a99c8aa3b55f856fba0bc849ed06a50d65d181d19353249fdc06a8babb765f8`
- Q026-F-02: SHA `8ad5f22dbc800889e6bfedadc136339cc25004f699ac5a982ffeca860e731b6c`
- Q026-F-03: SHA `c2a39ef90ec770d9932ad2549067fd774b21b9f9e4ee147e9bf687170d8fc4a2`
- Q026-F-04: SHA `2f5a07f6792215a41ccfbcec7d70ef1e6171e84a6611f56d0f376d14c909d8f4`
- Q026-F-05: SHA `dce525681887541a802d1ee319a84dc1a30e88c9db17c1667bceb33d678a25a6`

Bonferroni-family: Q026-F-01..F-05 (k=5). α_bon = 0.01.

### Test execution
Single run, seed 20260507, 10000 perms each. Fail-fast SHA verification at start. All 5 SHAs verified; no mismatches.

### Verdict summary

| Test | Verdict | Headline |
|:--|:--|:--|
| Q026-F-01 | ✅ **CONFIRMED** | Paired R1+R2 refrain corpus-unique (8/8 in Q26, 0 elsewhere); cycle-length Spearman rho = −0.839, p_perm = 0.0083 < α_bon = 0.01 |
| Q026-F-02 | ❌ **NULL** | TSM-3 percentile 29% / 6% / 6% / 41% on 4 axes; 0/4 pass top-5% threshold |
| Q026-F-03 | ❌ **NULL/REFINED** | Coda rank 99/224 by lexical distinctness (mid-pack); top-1 = W_78 (Ibrāhīm-praise) |
| Q026-F-04 | ❌ **PRE-COMMIT VIOLATION / FALSIFIED** | M26-M28 = 0.269 (predicted closest), M26-M20 = 0.195 (observed closest); margin = −0.074, p_perm = 0.78 |
| Q026-F-05 | ❌ **NULL** | Q26 mean-tpv = 5.96, rank 45/114; p_perm = 0.81; LONGER than poetry hemistich (5.96 > 3.4) |

### Decision points / garden-of-forking-paths

- **F-01 cycle boundary definition**: chose R2-end-of-cycle convention (objective). Alternative: R1-start-of-cycle (would shift by 1 verse, no impact on lengths). Pre-committed.
- **F-02 muqaṭṭaʿ reference set**: chose 29-surah muqaṭṭaʿ-set (rather than all 114). Justified: this is the natural reference class for "muqaṭṭaʿ-cluster cohesion" claims. Alternative would inflate the percentile (since muqaṭṭaʿ-set is itself FR-distinctive).
- **F-03 distance metric**: cosine with Laplace +1 smoothing on surah-mean. Alternative (Jensen-Shannon) tested in spot-check (rank stays at 95-100). Robust.
- **F-04 block boundaries**: M26 = 10-67, M28 = 3-43, M20 = 9-79 from classical commentaries. Sensitivity-tested with ±5-verse offsets — direction is robust.
- **F-05 poetry baseline**: chose visible-newline-separated lines as proxy for *bayt*. Hemistich proxy = full-line / 2 (rough). Acknowledged as approximation; the genre-claim is not quantifiable at simple length-statistic level.

### Outputs
- `00-overview.md` — 11-section overview with empirical anchors integrated.
- `01-empirical-profile.md` — H-NEW integration; UAS rank 14/114 highlighted.
- `02-content-analysis.md` — verse-by-verse + 9-block paired-refrain architecture.
- `03-tafsir-survey.md` — al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, al-Rāzī, al-Zamakhsharī, al-Biqāʿī, al-Suyūṭī (7 mufassirūn).
- `04-hadith-corpus.md` — al-Bukhārī #2641/3376/3377/4564/4565, Muslim #407/409/410/412/414/415, al-Tirmidhī #3120, plus Hassan-poetry hadith (al-Bukhārī #2237/3381, Muslim #6236).
- `05-classical-claims-audit.md` — 5 classical claims (3 vindicated, 2 NULL/falsified).
- `06-novel-findings.md` — 5 novel pre-registered tests.
- `07-cross-references.md` — neighbors / clusters / verse-twins / synthesis links.

### Headline finding
**Q026-F-01 CONFIRMED: the paired refrain (R1 `أكثرهم مؤمنين` + R2 `وإن ربك لهو العزيز الرحيم`) is corpus-unique to Q 26 (8 hits each, 0 elsewhere) and the 7 prophet-cycle lengths show monotone-decreasing progression (Spearman rho = −0.839, p_perm = 0.0083). This is the empirical lock on al-Zamakhsharī's qarīna-as-chorus claim, refined by the project-original cycle-compression law (intra-surah analog of [[h-new-660-compression-tail-gradient|H-NEW-660]]).**

### Equal NULL prominence (per protocol §1.3)

The 4 NULL findings are reported with full prominence:
- **F-02 NULL** extends the H-NEW-600 muqaṭṭaʿ-content-cohesion FALSIFIED streak to 5 replications.
- **F-04 PRE-COMMIT VIOLATION** extends it to 6 replications, at the strongest test-form (within shared narrative content). The muqaṭṭaʿ-letter-set is now empirically dead as a content-predictor.
- **F-03 NULL** refines (does not falsify) al-Bāqillānī: the coda's distinctness is rhetorical-theological, not lexical.
- **F-05 NULL** refines the Quran-vs-poetry genre-distinction: not testable at the simple token-count level.

### Files cross-referenced from MASTER-FINDINGS-LEDGER candidates
This investigation should appear in:
- MASTER-FINDINGS-LEDGER under §H-NEW-600 (muqaṭṭaʿ-content NULL streak update)
- KNOWLEDGE-GRAPH under Q 26 al-Shuʿarāʾ entry
- cross-finding-026 (iʿjāz-architecture synthesis) — F-01 refrain-compression law to be added

### Investigation status

- [x] All 8 template files written
- [x] ≥ 5 classical claims audited (5 of 5 done; 3 VINDICATED, 2 NULL/falsified)
- [x] ≥ 3 novel findings pre-registered and tested (5 of 5 done)
- [x] All H-NEW empirical metrics integrated
- [x] Cross-surah references mapped (Q 7, 11, 12, 15, 20, 23, 25, 27, 28, 36)
- [x] Honest-limits sections in each file
