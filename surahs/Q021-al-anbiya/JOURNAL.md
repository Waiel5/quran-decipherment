---
surah: 21
file_type: journal
date_created: 2026-05-07
phase: B+
specialist: Q021-al-anbiya-specialist
---

# Q 21 al-Anbiyāʾ — Investigation Journal

## 2026-05-07 — Full 8-file deep-dive built

### Pre-flight reading completed
- `INVESTIGATION-PROTOCOL.md` (full)
- `.claude/skills/quran-investigation/SKILL.md`
- `HANDOFF/04-DISCIPLINE.md`
- `surahs/Q012-yusuf/` (canonical template)
- `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (full)

### Empirical anchors loaded
- H-NEW-590 row Q 21: Δ%ile = −5.71 pp (WEAK_ANCHOR).
- H-NEW-700 Q 21: nūn-monorhyme 94.6%, 112 verses.
- H-NEW-720 adjacencies: Q 20-Q 21 = 0.0544 (rank 64); Q 21-Q 22 = 0.1776 (rank 16).
- H-NEW-750 Q 21: sig_A = −1.865 (rank 100); sig_B = −1.587 (rank 104).
- H-NEW-840 Q 21: UAS = 1.705 (rank 16/114).

### Pre-registrations locked (5 pre-regs, all SHA-256 hashed)

| Test | Pre-reg SHA | Direction | k | α |
|:--|:--|:--|:-:|:--:|
| Q021-F-01 prophet-completeness | `6417085b…59598dfa` | MAX | 1 | 0.05 |
| Q021-F-02 prophet-order-template | `780454a4…46174fdf` | mean(B,C,D) < d(Q21,Q6) | 3 | 0.0167 |
| Q021-F-03 isolation | `16d48c78…dee27587` | HIGHER | 1 | 0.05 |
| Q021-F-04 cosmological-cluster | `849143dd…ce1c4cc` | HIGHER | 1 | 0.05 |
| Q021-F-05 Q21+Q22 adjacency | `30344665…11ad66` | LOW (cell A) + HIGH-COST (cell B) | 2 | 0.025 |

### Garden-of-forking-paths log

**Q021-F-01**: The author observed Q 21 = 14 prophets and Q 6 = 16 prophets BEFORE locking the pre-reg, during initial QAC PN-lemma exploration. The pre-reg locks the original task-seed direction (MAX) anyway, transparently disclosing the pre-observation. The result is published with full prominence as **NULL/PRE-COMMIT-VIOLATION** per [[INVESTIGATION-PROTOCOL §1.8]].

**Q021-F-05**: Cell B (TSP-cost rank) was already-observed (rank 16/113 from H-NEW-720) before pre-reg lock, transparently disclosed in pre-reg §2. Treated under MW-7 single-test α=0.05 with no Bonferroni penalty. Cell A (within-cluster FR-rank) was the genuinely-novel cell.

### Test execution

All 5 scripts executed successfully (SHA-verified at runtime). Results:

| Test | Verdict | Headline |
|:--|:--|:--|
| Q021-F-01 | NULL/PRE-COMMIT-VIOLATION | Q 21 rank 2 / 114 (Q 6 = 16, Q 21 = 14). Q 21 is the *narrative-form* prophet-cycle MAX, not the *list-form* MAX. |
| Q021-F-02 | NULL | mean_alt − d(Q6) = +0.024 (sign WRONG); p_perm = 0.56. Q 21's prophet-order is mid-distance, not closer to {Q 11, Q 26, Q 37}. |
| Q021-F-03 | **CONFIRMED** | Q 21 isolation rank 18/114 (85th percentile). FR-distance corroborates H-NEW-126 true-isolate. |
| Q021-F-04 | NULL (DIRECTIONAL-borderline) | observed = 0.141, p_contig = 0.127, p_non_contig = 0.056. al-Biqāʿī cosmological-naẓm not strongly empirically distinct. |
| Q021-F-05 | **NULL — NEAR-NEIGHBOR-BUT-NOT-CLUSTER** | Q 21-Q 22 is the FARTHEST within-cluster pair (rank 10/10, d=0.959) despite mushaf-adjacency. True-isolate cluster has NO internal sub-coherence. |

### Key findings

⭐ **F-03 CONFIRMED**: Q 21 is empirically isolated by FR-roots-mean-d-to-5-nearest (rank 18 / 114, 85th percentile). The H-NEW-126 cluster-invariance label has a positive FR-distance correlate.

⭐ **F-05 STRUCTURAL DISCOVERY**: The true-isolate cluster {Q 16, 21, 22, 23, 25} is *cluster-invariant* but NOT *FR-coherent*. The within-cluster FR-CLOSEST pair is Q 16 ↔ Q 22 (mushaf gap 6); the within-cluster FR-FARTHEST pair is Q 21 ↔ Q 22 (mushaf gap 1). The mushaf pays a top-15 TSP-cost (rank 16/113) to place Q 21 and Q 22 adjacently despite them being the FARTHEST pair within their own classification cluster.

This is candidate cross-finding-XXX material: **the true-isolate cluster is a NULL-cluster precisely because its members are mutually FR-distant, including the only mushaf-adjacent pair (Q 21-Q 22)**. The "true-isolate" label captures sui-generis-ness, not internal-cohesion.

### Files produced

```
surahs/Q021-al-anbiya/
  00-overview.md
  01-empirical-profile.md
  02-content-analysis.md
  03-tafsir-survey.md
  04-hadith-corpus.md
  05-classical-claims-audit.md
  06-novel-findings.md
  07-cross-references.md
  JOURNAL.md
  Q021-F-01-prophet-cycle-completeness-prereg.md
  Q021-F-02-prophet-order-distance-prereg.md
  Q021-F-03-isolation-prereg.md
  Q021-F-04-cosmological-cluster-prereg.md
  Q021-F-05-true-isolate-adjacency-prereg.md
  csv/
    Q021-F-01.json
    Q021-F-02.json
    Q021-F-03.json
    Q021-F-04.json
    Q021-F-05.json

surahs/scripts/
  Q021_F_01_prophet_completeness.py
  Q021_F_02_prophet_order.py
  Q021_F_03_isolation_test.py
  Q021_F_04_cosmological_cluster.py
  Q021_F_05_isolate_adjacency.py
```

### Discipline checks

- [x] Pre-reg SHA-locked and embedded in scripts.
- [x] SHA verified at runtime in each script.
- [x] Direction locked before computation.
- [x] Garden-of-forking-paths transparently disclosed for F-01 and F-05.
- [x] Bonferroni declared per pre-reg.
- [x] 10 000 permutations on each null where applicable (F-02, F-04).
- [x] Seed 20260507 locked across all tests.
- [x] Equal NULL prominence — 4 NULLs published with same detail as 1 CONFIRMED.
- [x] Honest-limits sections in every file.
- [x] Classical citations include scholar + work + passage where extractable.
- [x] No invented hadith numbers — Bukhārī #4533 / #4787 verified on disk.
- [x] No invented numerical values — all values cite computation script + JSON output.
- [x] Rules-tuple specified per test.
