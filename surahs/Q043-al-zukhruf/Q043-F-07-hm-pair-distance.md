---
finding_id: Q043-F-07
surah: 43
surah_name: al-Zukhruf
file_type: novel-finding
date: 2026-05-10
verdict: PASS-DIRECTED
prereg_sha: 4b7630a63ef47d4dfc559611070a5b166144593a1872d5fecfc1a866ea7bd654
---

# Q043-F-07 — Q 43 HM-cluster pair-distance ranking

## Verdict

**PASS-DIRECTED.** Q 43's median FR-distance to other HM-cluster members is **0.8879**, vs the null median of **0.9834** (random size-6 non-HM sample, n_perm=10000). One-sided lower-tail p = **0.0043** (below Bonferroni α = 0.0167).

## Per-pair distances

| Pair | FR distance |
|:--|:--:|
| Q 43 ↔ Q 40 | 0.9109 |
| Q 43 ↔ Q 41 | 0.8557 |
| Q 43 ↔ Q 42 | 0.9912 |
| Q 43 ↔ Q 44 | 0.8647 |
| Q 43 ↔ Q 45 | 0.9011 |
| Q 43 ↔ Q 46 | 0.8747 |

Tightest within-HM neighbors of Q 43: **Q 41** (0.8557) and **Q 44** (0.8647). Loosest: **Q 42** (0.9912) — the Q 42 al-Shūrā ʿsq secondary-opener locus, which has the known heterogeneity-flag in the cluster.

## Interpretation

Q 43 is empirically anchored within the ḥawāmīm cluster on root-distribution despite cross-finding-025's marker-thickness rule warning against thin-marker FR-cohesion. The result indicates that the HM cluster is *not* uniformly thin: Q 43 (89 verses) is large enough that the muqaṭṭaʿāt opener is not the sole shared feature — the late-Meccan prose register, the *tanzīl al-kitāb* class, and the recurring eschatological/messenger themes provide additional shared signal.

This is a *one-surah-to-cluster* cohesion test (not full-cluster cohesion). Q 43 tilts toward HM. Combined with Q045-F-06 (p=0.0002 from Q 45 side), the result strengthens the position that the HM cluster's *core members* (Q 40-46 minus heterogeneity-flag) ARE FR-cohesive when probed pairwise, even when whole-cluster cohesion (H-NEW-1190) is borderline.

## Cross-references

- [[Q041-fussilat/Q041-F-03|Q041-F-03]] — HM ranking with Q 41/Q 42 tightest.
- [[Q045-al-jathiyah/Q045-F-06|Q045-F-06]] — parallel test from Q 45 direction (p=0.0002).
- [[H-NEW-1190]] — full-HM-cluster FR-cohesion test.
- [[cross-finding-025-marker-thickness-rule]] — thin marker → NULL warning (which this test partially weakens).

## Honest limits

- MW-5 (replication) is satisfied by Q045-F-06.
- MW-6 (instrument-control): the test does NOT control for late-Meccan chronology — the HM cluster is largely Late-Meccan, so a chronology-matched control would be a stronger null. Pre-registered in Q 39 H-NEW-1270 tanzīl-opener cluster work.
- The QAC root-distribution is one lens; rhyme-FR and phoneme-FR pairwise tests are not run here.

## Files

- pre-reg: `preregs/Q043-F-07-hm-cluster-pair-distance-prereg.md`
- script: `scripts/Q043_F_07_hm_pair_distance.py`
- output: `csv/Q043-F-07.json`
