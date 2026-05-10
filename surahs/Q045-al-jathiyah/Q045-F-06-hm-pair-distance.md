---
finding_id: Q045-F-06
surah: 45
surah_name: al-Jāthiyah
file_type: novel-finding
date: 2026-05-10
verdict: PASS-DIRECTED
prereg_sha: 3263cb19d575fe6cc98c3a308456eb911f4a67080fe2f4ab51c0eb9a44611f26
---

# Q045-F-06 — Q 45 HM-cluster pair-distance ranking

## Verdict

**PASS-DIRECTED (highly significant).** Q 45's median FR-distance to other HM-cluster members is **0.8190**, vs the null median of **0.9487** (random size-6 non-HM sample, n_perm=10000). One-sided lower-tail p = **0.0002** (well below Bonferroni α = 0.0167).

## Per-pair distances

| Pair | FR distance |
|:--|:--:|
| Q 45 ↔ Q 40 | 0.8267 |
| Q 45 ↔ Q 41 | **0.7994** (tightest) |
| Q 45 ↔ Q 42 | 0.8011 |
| Q 45 ↔ Q 43 | 0.9011 |
| Q 45 ↔ Q 44 | 0.8439 |
| Q 45 ↔ Q 46 | 0.8112 |

Five of the six HM neighbors of Q 45 sit below FR=0.85 — a very tight cohesion. The tightest pair is **Q 45 ↔ Q 41** at 0.7994, mirroring Q041-F-03's finding that the Q 41-Q 42 pair was tightest within HM (Q 45 ↔ Q 41 is now competitive with that).

## Interpretation

Q 45 al-Jāthiyah is one of the most strongly HM-cohesive surahs by this test (p=0.0002 is well below any pre-registered threshold). The result is striking because Q 45 is the *shortest* HM member (37 verses), which would naively suggest weaker root-distribution stability — yet Q 45's median distance to HM siblings is the lowest among the within-cluster pair-distance tests run today (Q 43: 0.8879; Q 45: 0.8190).

Combined with:
- Q043-F-07 (p=0.0043 for Q 43 within-HM cohesion)
- Q041-F-03 (Q 41-Q 42 tightest within-HM)
- Q039-al-zumar H-NEW-1270 (tanzīl-opener Late-Meccan tightness)

This is the **third independent pairwise-cohesion confirmation** of HM-cluster structure on root-FR, all run under the same direction-lock + Bonferroni discipline. The cumulative finding suggests:

> **The ḥawāmīm cluster IS root-FR-cohesive at the pairwise level, even where it is borderline-cohesive at the whole-cluster level.**

This is consistent with cross-finding-025's marker-thickness rule (whole-cluster cohesion requires multi-axis correlation; pairwise cohesion can succeed on chronological + opener + register alignment alone).

## Cross-references

- [[Q043-al-zukhruf/Q043-F-07|Q043-F-07]] — parallel test from Q 43 direction (p=0.0043).
- [[Q041-fussilat/Q041-F-03|Q041-F-03]] — HM pair-ranking (Q 41/Q 42 tightest at full-surah level).
- [[H-NEW-1190]] — full-HM-cluster FR-cohesion test (borderline).
- [[Q039-al-zumar/H-NEW-1270|H-NEW-1270]] — tanzīl-opener Late-Meccan tight cluster.
- [[cross-finding-025-marker-thickness-rule]] — marker-thickness rule context.

## Honest limits

- MW-5 (replication): satisfied by Q043-F-07.
- MW-6 (instrument-control): a chronology-matched null (Late-Meccan random size-6) would be a stronger control; not run here.
- The QAC root-FR matrix is one lens; rhyme-FR and phoneme-FR pairwise tests are not run here.
- The exceptionally low p-value (0.0002) suggests the test is well-powered for Q 45 specifically; future families of HM-pair tests should consider stricter Bonferroni given the strength of effect.

## Files

- pre-reg: `preregs/Q045-F-06-hm-cluster-pair-distance-prereg.md`
- script: `scripts/Q045_F_06_hm_pair_distance.py`
- output: `csv/Q045-F-06.json`
