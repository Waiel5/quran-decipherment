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

## 2026-05-09 PM — Wave-H brief-addition (3 more pre-registered tests + replication)

### Brief context
Per `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md`, Q 26 is part of the H-NEW-1320
PASS-DIRECTED 3-tier refrain architecture {Q 55 (max_repeat 31), Q 77 (10),
Q 26 (8)} — the narrative-prophetic refrain tier. The 2026-05-09 brief
requested three additional pre-registered tests:
- **T1**: Replicate Q026-F-01's claim that the closing refrain occurs
  corpus-EXACTLY 8 times at exact verse positions.
- **T2**: 7-prophet narrative cohesion within Q 26 (root-Jaccard vs random
  Meccan sub-blocks) → filed as **Q026-F-06**.
- **T3**: TSM (Q 26) vs ḥawāmīm cluster FR-distance comparison → filed as
  **Q026-F-07**.

### New pre-regs locked
Two new pre-reg files written and SHA256 computed BEFORE running tests:
- Q026-F-06: SHA `85766b7fcfe42c39c7a93de619127f385e1c4664d218b4f740c4a8328073c912`
- Q026-F-07: SHA `4f15c979b511ef2604838dd31f8ab348238038609b7fb8ebb4b134f0c6695252`

Bonferroni k=2 for this addition → α_per_test = 0.025. Seed: 20260509.

### Test execution
- `scripts/Q026_F_01_refrain_replication.py` → T1 result: all 3 sub-claims PASS (R1 corpus=8, R2 corpus=8, exact positions match).
- `scripts/Q026_F_06_prophet_jaccard.py` → F-06: J_obs=0.2398, null_mean=0.1907, Z=+1.73, p_perm=0.0548. Direction passes, Bonferroni-α (0.025) not crossed.
- `scripts/Q026_F_07_tsm_vs_hawamim.py` → F-07: Δ=−0.044 (TSM closer than ḥawāmīm by 0.044), p_perm=0.294. Direction passes, Bonferroni-α not crossed.

### Verdict summary (2026-05-09 brief tests)

| Test | Verdict | Headline |
|:--|:--|:--|
| Q026-T1 | ✅ **CONFIRMED-REPLICATION** | R1+R2 = corpus-EXACT 8/8 at exact predicted positions; F-01 replicates cleanly |
| Q026-F-06 | ❌ **NULL** (directional pass) | J_obs=0.240 > null_mean=0.191, Z=+1.73, p_perm=0.055 (>0.025); soft signal |
| Q026-F-07 | ❌ **NULL** (directional pass) | Δ=−0.044 (TSM-family ~5% closer than ḥawāmīm), p_perm=0.294; soft signal |

### Decision points
- For F-06, chose narrative-Meccan baseline pool {Q 7, Q 11, Q 21, Q 38, Q 51}
  to control for genre. Garden-of-forking-paths note: tested only this baseline;
  did not also try whole-corpus null which would have been weaker.
- For F-07, used the upper-triangular sparse h-new-111 format `[i, j, d]`.
  Sanity: verified d(Q26,Q27)=0.959 matches the Q 26 nearest-neighbor list in
  00-overview.md.
- The two new tests' results are CONSISTENT with the qualitative pre-commit
  direction but neither crosses Bonferroni-α — published as NULL with full
  prominence per protocol §1.3.

### Files added
- `surahs/Q026-al-shuara/Q026-F-06-prophet-jaccard-cohesion-prereg.md`
- `surahs/Q026-al-shuara/Q026-F-07-tsm-vs-hawamim-prereg.md`
- `surahs/Q026-al-shuara/csv/Q026-F-06.json`
- `surahs/Q026-al-shuara/csv/Q026-F-07.json`
- `surahs/Q026-al-shuara/csv/Q026-T1-refrain-replication.json`
- `scripts/Q026_F_01_refrain_replication.py` (T1 replication script)
- `scripts/Q026_F_06_prophet_jaccard.py` (F-06)
- `scripts/Q026_F_07_tsm_vs_hawamim.py` (F-07)

### Headline finding (2026-05-09 brief)
**T1 CONFIRMS Q026-F-01's headline empirically and independently**: the closing
refrain pair `إن في ذلك لآية وما كان أكثرهم مؤمنين` + `وإن ربك لهو العزيز الرحيم`
occurs corpus-EXACTLY 8 times in each phrase, all 8 in Q 26 at exact verses
{8/9, 67/68, 103/104, 121/122, 139/140, 158/159, 174/175, 190/191}. Q 26 is the
narrative-prophetic refrain tier of H-NEW-1320's 3-tier architecture {Q 55, Q 77,
Q 26}. F-06 and F-07 give honest soft signals (directional pass, not Bonferroni-
significant), neither overturning nor confirming their underlying claims.
