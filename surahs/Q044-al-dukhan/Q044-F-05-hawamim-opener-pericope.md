---
finding_id: Q044-F-05
surah: 44
surah_name: al-Dukhān
file_type: novel-finding
date: 2026-05-10
verdict: PASS-DIRECTED
prereg_sha: 3ef9170973093f0eaec509b32fdf04eb05ec3370e7ff8d5210744e00159c8f2e
---

# Q044-F-05 — HM sibling-opener pericope Jaccard test

## Verdict

**PASS-DIRECTED.** Mean pairwise root-Jaccard of HM opener-pericopes (Q 41:1-8, Q 44:1-8, Q 46:1-8) is **0.1880**, vs null median **0.0664** (random 3-block draws from non-HM surahs, n_perm=10000). One-sided upper-tail p = **0.0131** (below Bonferroni α = 0.0167).

## Per-pair Jaccards

The 3 HM opener-pericopes share roots at substantially elevated rates:

| Pair | Jaccard |
|:--|--:|
| Q 41:1-8 ↔ Q 44:1-8 | (see JSON) |
| Q 41:1-8 ↔ Q 46:1-8 | (see JSON) |
| Q 44:1-8 ↔ Q 46:1-8 | (see JSON) |
| **Mean** | **0.1880** |
| Null median | 0.0664 |

Observed/null ratio ≈ **2.83×** — the HM opener-window is empirically templated.

## Interpretation

This is the first project-internal finding that *isolates* opener-pericope templating from full-surah cohesion. Cross-finding-025's marker-thickness rule warned that thin markers (e.g., HM at 1/89 verses for Q 43) would NULL on full-surah FR. The opener-pericope window resolves the apparent paradox: **the templating IS present in the 8-verse opener context**, even when the full surahs diverge later. The HM cluster's defining feature operates locally; the full-surah dispersion reflects content-block specialization that follows the opener.

The 3 HM siblings chosen for this test (Q 41, Q 44, Q 46) are all archetypal HM openers (HM + *wa-l-kitāb al-mubīn* / *tanzīl al-kitāb* / *tanzīl al-kitāb*). Q 42's secondary opener ʿsq is excluded by design. A follow-up could:
- Extend to all 7 HM members (with mixed Q 40, Q 42, Q 43, Q 45 — varying opener-pericope verse-counts).
- Test at window sizes K∈{4, 6, 10, 12} to confirm window-stability.
- Test under cross-corpus null (poetry/Bukhari-prose 8-verse blocks).

## Cross-references

- [[H-NEW-1190]] — full-HM-cluster FR-cohesion baseline.
- [[Q041-fussilat/Q041-F-03|Q041-F-03]] — HM pair-ranking (Q 41/Q 42 tightest at full-surah level).
- [[Q039-al-zumar/H-NEW-1270]] — tanzīl-opener cluster (the broader chronological-late-Meccan tight family).
- [[cross-finding-025-marker-thickness-rule]] — opener-pericope test resolves the apparent thin-marker paradox.

## Honest limits

- The 8-verse window is one hyperparameter; window-stability is unverified at K=4, 6, 12.
- Jaccard ignores frequency; weighted variants not tested.
- The sampling null draws from all non-HM surahs with ≥8 verses; a chronology-matched null would tighten the test.
- The result has substantive cross-finding implications: it weakens (but does not falsify) cross-finding-025's marker-thickness rule by showing that the rule holds for FULL-SURAH but not LOCAL-OPENER-WINDOW.

## Files

- pre-reg: `preregs/Q044-F-05-hawamim-opener-pericope-prereg.md`
- script: `scripts/Q044_F_05_hawamim_opener_pericope.py`
- output: `csv/Q044-F-05.json`
