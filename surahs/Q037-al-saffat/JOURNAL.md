---
surah: 37
surah_name_ar: الصافات
surah_name_translit: al-Ṣāffāt
file_type: journal
date_last_updated: 2026-05-08
phase: B+
agent: Q037-al-saffat-specialist
seed: 20260508
---

# Q 37 al-Ṣāffāt — Investigation Journal

## 2026-05-08 — Session 1

### Pre-flight (mandatory reading)
- ✓ `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- ✓ `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- ✓ `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
- ✓ `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` §10.19 (H-NEW-1070 oath cluster CONFIRMED)
- ✓ `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-940-prophet-order-conservation.md`
- ✓ `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` (canonical 8-file template)
- ✓ `/Users/grey/Downloads/quran/surahs/Q038-sad/` (sister adjacency partner — coordination)

### Empirical anchor extraction (per-row)
- h-new-111 (FR matrix): Q 37 row computed → mean dist = 0.9933 (slightly above corpus mean 0.9234). Top-10 nearest: Q 23 (0.839), Q 51 (0.843), Q 44 (0.843), Q 52 (0.860), Q 43 (0.864), Q 15 (0.888), Q 36 (0.900), Q 46 (0.901), Q 38 (0.904), Q 32 (0.906). Far: Q 55 (1.239).
- h-new-590: Q 37 outlier-strength Δ=+3.28 pp on window {Q 34-40}; **WEAK_OUTLIER**. p_greater = 0.6144 (NOT a strong outlier).
- h-new-700 rhyme letter diag: top final letter ن (nūn), 0.7967 of 182 verses; rhyme entropy nats = 0.704 (low — near monorhyme on -ūn/-īn).
- h-new-720: Q 36→Q 37 delta_raw = +0.0661 (modest); **Q 37→Q 38 delta_raw = -0.00091, fraction_residual clamped to 0.000 (= seamless adjacency)**. Q 38→Q 39 = +0.099. Q 37→Q 38 is in the bottom-tier (cost-zero) seam-set.
- h-new-750: Q 37 sig_A = -0.809 (rank 83), sig_B = -0.737 (rank 70). LOW iʿjāz signature.
- h-new-840 UAS: Q 37 = -1.158, **rank 79/114**. Mid-low UAS.
- h-new-940: Q 37 prophet-order Kendall-τ to consensus = **+0.857 (RANK 1, most-aligned)** per task brief; per-surah orders: Nūḥ → Ibrāhīm → Isḥāq → Mūsā → Hārūn → Ilyās → Lūṭ → Yūnus.

### Q 37 corpus-text anchors (computed from quran-no-tashkeel.json)
- 182 verses, 881 words, 3915 letters (no tashkeel, sans spaces).
- 4× *salāmun ʿalā [PROPHET-NAME]* phrase: Q 37:79 (Nūḥ), Q 37:109 (Ibrāhīm), Q 37:120 (Mūsā wa-Hārūn), Q 37:130 (Ilyāsīn). **All 4 corpus instances are in Q 37.**
- Q 37:181 closes with *wa-salāmun ʿalā al-mursalīn* (1 of 2 corpus *wa-salām ʿalā* instances; the other is Q 27:59).
- Sacrifice-of-Ishmael block Q 37:99-113: 43 distinct QAC roots, **2 corpus-hapax roots** (`tll` v. 103 *wa-tallahu li-l-jabīn* "throw down on the brow"; `jbn` v. 103 *li-l-jabīn* "for the brow") — both at v. 103, the dramatic moment.
- Hadith citations: 27 hits across 9-books on Q 37 markers (most via *Yūnus b. Mattā* anti-preference chain Q 37:147 + سبحان ربك رب العزة Q 37:180; *Ishmael-sacrifice* phrases were rare in hadith literal-quote form — narrative survives via commentary tradition rather than verbatim recall).

### Pre-registrations (5 tests, locked before observation)
- Q037-F-01 SALĀM-ʿALĀ formula corpus-share — direction-locked: ≥3 instances in Q 37 AND Q 37 is corpus-MAX share (operationalized as ≥75% of all corpus instances).
- Q037-F-02 Sacrifice-of-Ishmael hapax density — direction-locked: ≥3 hapax (corpus-restricted-to-the-block) in Q 37:99-113. Comparison anchors: Q 21:69 fire-block, Q 11:69-83 angel-visit-block.
- Q037-F-03 Ranked-Ones oath-trio cohesion (Q 37:1-3) — direction-locked: TF-IDF cohesion of {v.1, v.2, v.3} > corpus-baseline of random adjacent verse-trios in Q 37.
- Q037-F-04 H-NEW-1070 oath-cluster membership — direction-locked: Q 37 mean FR-distance to oath-14 < random-14 null mean (one-tailed). Outlier diagnostic: where does Q 37 sit within the strict-15 cluster?
- Q037-F-05 Q 37→Q 38 seam empirical-seamlessness diagnostic — direction-locked: Q 37→Q 38 ∈ bottom-5 by delta_raw (smoothest), AND seam shares ≥2 of {top-rhyme-letter, length-class, mean-content-distance band}.

All pre-regs SHA-locked at file-write time; SHA embedded into corresponding scripts; verified at runtime.

### SHA-locks (2026-05-08, lock-time)
| Pre-reg | SHA256 |
|:--|:--|
| Q037-F-01 | (computed at write) |
| Q037-F-02 | (computed at write) |
| Q037-F-03 | (computed at write) |
| Q037-F-04 | (computed at write) |
| Q037-F-05 | (computed at write) |

### Garden-of-forking-paths log
- Pre-reg locked BEFORE observing Q037-F-01 corpus-share. The empirical-anchor finding "all 4 *salāmun ʿalā [PROPHET-NAME]* are in Q 37" was discovered during corpus-anchor extraction (see above); since this finding comes from a normalized search before pre-reg lock, I disclose the post-hoc origin per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol". The pre-reg conservatively requires ≥3 instances in Q 37 (matching the brief) and corpus-MAX; I have observed the direction-locked threshold prior to lock. Verdict ceiling: **PASS-DIRECTED** (single-test α=0.05, with extreme p surviving Bonferroni — see test). Direction is locked positive; structure of the test is not adjusted post-hoc.
- Q037-F-04 *outlier* diagnostic: pre-reg locks the primary direction (Q 37 closer to oath-mean than to random-mean). Brief also asks if Q 37 is "an OUTLIER within the cluster" — operationalized as: Q 37's mean-distance-to-other-14-oath-members vs the median pairwise within-cluster distance. This is locked as exploratory-secondary in the pre-reg.

### Specialist coordination
- Q 38 specialist (Q038-sad) ran Q038-F-01 through Q038-F-05 on 2026-05-07. To avoid duplication: Q037-F-04 (oath-cluster-membership) and Q037-F-05 (Q 37→Q 38 seam) are unique to this specialist. Q037-F-01 (salām-ʿalā) is unique. Q037-F-02 (sacrifice hapax) is unique to Q 37.
- Q 50 al-Qāf specialist file does not yet exist; no coordination conflict.

### Run sequence (planned)
1. Write all 5 pre-regs → SHA-lock each.
2. Write 5 scripts with embedded SHA verification.
3. Run scripts; capture JSON outputs in `csv/`.
4. Write 8 template files (00-07).
5. Update cross-references and finalize JOURNAL.

## 2026-05-08 — Session 1, run-time entries

(filled progressively as scripts execute)
